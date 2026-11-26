"""A small, playable Rock-Paper-Scissors game (tkinter + Pillow)."""

from pathlib import Path
from random import choice
from tkinter import Button, Frame, Label, Tk, NW
import tkinter.font as tkfont

from PIL import Image, ImageTk

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "image"
ICON_SIZE = (80, 80)


class Screen:
    """Window with the scoreboard, the result and the three hand buttons."""

    FONT_NAME = "Ivy"
    FONT_SIZE_SMALL = 10
    FONT_SIZE_MEDIUM = 12
    FONT_SIZE_LARGE = 30
    WHITE = "#FFFFFF"
    BLACK = "#333333"
    BOTTOM = "#3b3b3b"
    WIN_COLOR = "#66bb6a"
    LOSE_COLOR = "#ef5350"
    DRAW_COLOR = "#bdbdbd"

    IMAGE_FILES = {
        "rock": "HandRock.png",
        "paper": "HandPaper.png",
        "scissors": "HandScissors.png",
    }
    MOVE_NAMES = {
        "rock": "Rock",
        "paper": "Paper",
        "scissors": "Scissors",
    }
    RESULT_TEXT = {
        "win": "You win!",
        "lose": "PC wins!",
        "draw": "Draw!",
    }

    def __init__(self, on_play, on_reset):
        self.on_play = on_play
        self.on_reset = on_reset

        self.janela = Tk()
        self.janela.title("Rock, Paper, Scissors")
        self.janela.geometry("320x430")
        self.janela.resizable(False, False)
        self.janela.configure(bg=self.BOTTOM)

        self.font_name = self._resolve_font()
        self._photos = {}  # PhotoImage needs a live reference or the icon disappears

        self._build_scoreboard()
        self._build_result()
        self._build_buttons()
        self._bind_keys()

    def _font(self, size, weight="normal"):
        return (self.font_name, size, weight)

    def _resolve_font(self):
        """Use 'Ivy' when available, otherwise a font that exists on the system."""
        families = tkfont.families(self.janela)
        if self.FONT_NAME in families:
            return self.FONT_NAME
        for candidate in ("Segoe UI", "Arial", "Helvetica"):
            if candidate in families:
                return candidate
        return "TkDefaultFont"

    def _build_scoreboard(self):
        self.top_frame = Frame(
            self.janela, width=320, height=100, bg=self.BLACK,
            relief="raised", bd=1
        )
        self.top_frame.grid(row=0, column=0, sticky=NW)
        self.top_frame.grid_propagate(False)

        self.user_points = Label(
            self.top_frame, text="0", font=self._font(self.FONT_SIZE_LARGE, "bold"),
            bg=self.BLACK, fg=self.WHITE
        )
        self.user_points.place(x=95, y=40, anchor="center")

        self.divider = Label(
            self.top_frame, text=":", font=self._font(self.FONT_SIZE_LARGE, "bold"),
            bg=self.BLACK, fg=self.WHITE
        )
        self.divider.place(x=160, y=40, anchor="center")

        self.machine_points = Label(
            self.top_frame, text="0", font=self._font(self.FONT_SIZE_LARGE, "bold"),
            bg=self.BLACK, fg=self.WHITE
        )
        self.machine_points.place(x=225, y=40, anchor="center")

        self.user_label = Label(
            self.top_frame, text="You", font=self._font(self.FONT_SIZE_SMALL, "bold"),
            bg=self.BLACK, fg=self.WHITE
        )
        self.user_label.place(x=95, y=78, anchor="center")

        self.machine_label = Label(
            self.top_frame, text="PC", font=self._font(self.FONT_SIZE_SMALL, "bold"),
            bg=self.BLACK, fg=self.WHITE
        )
        self.machine_label.place(x=225, y=78, anchor="center")

    def _build_result(self):
        self.result_frame = Frame(self.janela, width=320, height=70, bg=self.BOTTOM)
        self.result_frame.grid(row=1, column=0, sticky=NW)
        self.result_frame.grid_propagate(False)

        self.result_label = Label(
            self.result_frame, text="Choose your move",
            font=self._font(16, "bold"), bg=self.BOTTOM, fg=self.WHITE
        )
        self.result_label.pack(expand=True)

        self.choice_label = Label(
            self.result_frame, text="", font=self._font(self.FONT_SIZE_SMALL),
            bg=self.BOTTOM, fg="#dddddd"
        )
        self.choice_label.pack()

    def _build_buttons(self):
        self.lower_frame = Frame(
            self.janela, width=320, height=205, bg=self.WHITE, relief="flat"
        )
        self.lower_frame.grid(row=2, column=0, sticky=NW)
        self.lower_frame.grid_propagate(False)

        for column, move in enumerate(("rock", "paper", "scissors")):
            icon_path = IMAGE_DIR / self.IMAGE_FILES[move]
            icon = Image.open(icon_path).convert("RGBA").resize(
                ICON_SIZE, Image.Resampling.LANCZOS
            )
            photo = ImageTk.PhotoImage(icon)
            self._photos[move] = photo

            button = Button(
                self.lower_frame, image=photo, text=self.MOVE_NAMES[move],
                compound="top", font=self._font(self.FONT_SIZE_MEDIUM, "bold"),
                bg=self.WHITE, relief="flat", cursor="hand2",
                command=lambda chosen=move: self.on_play(chosen),
            )
            button.grid(row=0, column=column, padx=12, pady=28)

        self.reset_button = Button(
            self.janela, text="Reset score", font=self._font(self.FONT_SIZE_SMALL),
            bg=self.BOTTOM, fg=self.WHITE, relief="flat", cursor="hand2",
            command=self.on_reset,
        )
        self.reset_button.grid(row=3, column=0, pady=8)

    def _bind_keys(self):
        for key, move in (("1", "rock"), ("2", "paper"), ("3", "scissors")):
            self.janela.bind(key, lambda event, chosen=move: self.on_play(chosen))
        self.janela.bind("r", lambda event: self.on_reset())

    def update_score(self, user_score, machine_score):
        self.user_points.config(text=str(user_score))
        self.machine_points.config(text=str(machine_score))

    def show_round(self, user_move, machine_move, outcome):
        colors = {
            "win": self.WIN_COLOR,
            "lose": self.LOSE_COLOR,
            "draw": self.DRAW_COLOR,
        }
        self.result_label.config(
            text=self.RESULT_TEXT[outcome], fg=colors[outcome]
        )
        self.choice_label.config(
            text="You: {}  |  PC: {}".format(
                self.MOVE_NAMES[user_move], self.MOVE_NAMES[machine_move]
            )
        )

    def reset(self):
        self.update_score(0, 0)
        self.result_label.config(text="Choose your move", fg=self.WHITE)
        self.choice_label.config(text="")

    def start(self):
        """Start the tkinter event loop."""
        self.janela.mainloop()


class Game:
    """Rules and score. It only creates the UI when start() is called."""

    MOVES = ("rock", "paper", "scissors")
    WINS_AGAINST = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }

    def __init__(self):
        self.user_score = 0
        self.machine_score = 0
        self.screen = None

    @classmethod
    def resolve(cls, user_move, machine_move):
        """Return 'win', 'lose' or 'draw' without touching the interface."""
        if user_move not in cls.MOVES or machine_move not in cls.MOVES:
            raise ValueError(
                "Invalid move. Use: {}.".format(", ".join(cls.MOVES))
            )
        if user_move == machine_move:
            return "draw"
        return "win" if cls.WINS_AGAINST[user_move] == machine_move else "lose"

    def play(self, user_move, machine_move=None):
        """Play one round; machine_move can be forced (useful for tests)."""
        machine_move = machine_move or choice(self.MOVES)
        outcome = self.resolve(user_move, machine_move)

        if outcome == "win":
            self.user_score += 1
        elif outcome == "lose":
            self.machine_score += 1

        if self.screen is not None:
            self.screen.show_round(user_move, machine_move, outcome)
            self.screen.update_score(self.user_score, self.machine_score)

        return outcome

    def reset(self):
        self.user_score = 0
        self.machine_score = 0
        if self.screen is not None:
            self.screen.reset()

    def start(self):
        """Build the window and start the game."""
        self.screen = Screen(on_play=self.play, on_reset=self.reset)
        self.screen.start()


if __name__ == "__main__":
    Game().start()
