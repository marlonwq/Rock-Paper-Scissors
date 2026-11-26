const MOVES = ["rock", "paper", "scissors"];
const WINS_AGAINST = { rock: "scissors", paper: "rock", scissors: "paper" };
const NAMES = { rock: "Rock", paper: "Paper", scissors: "Scissors" };
const MESSAGES = { win: "You win!", lose: "PC wins!", draw: "Draw!" };
const COLORS = { win: "var(--win)", lose: "var(--lose)", draw: "var(--draw)" };

const ui = {
  userScore: document.getElementById("user-score"),
  pcScore: document.getElementById("pc-score"),
  result: document.getElementById("result"),
  choices: document.getElementById("choices"),
  bestOfThree: document.getElementById("best-of-three"),
  reset: document.getElementById("reset"),
  buttons: Array.from(document.querySelectorAll("[data-move]")),
};

let userScore = 0;
let pcScore = 0;
let finished = false;

function resolve(userMove, machineMove) {
  if (userMove === machineMove) return "draw";
  return WINS_AGAINST[userMove] === machineMove ? "win" : "lose";
}

function updateScores() {
  ui.userScore.textContent = String(userScore);
  ui.pcScore.textContent = String(pcScore);
}

function setButtonsEnabled(enabled) {
  ui.buttons.forEach((button) => { button.disabled = !enabled; });
}

function play(userMove) {
  if (finished || !MOVES.includes(userMove)) return;

  const machineMove = MOVES[Math.floor(Math.random() * MOVES.length)];
  const outcome = resolve(userMove, machineMove);

  if (outcome === "win") userScore += 1;
  if (outcome === "lose") pcScore += 1;

  updateScores();
  ui.result.textContent = MESSAGES[outcome];
  ui.result.style.color = COLORS[outcome];
  ui.choices.textContent = `You: ${NAMES[userMove]} · PC: ${NAMES[machineMove]}`;

  if (ui.bestOfThree.checked && (userScore === 2 || pcScore === 2)) {
    finished = true;
    ui.result.textContent = userScore === 2
      ? "You win the best of 3!"
      : "PC wins the best of 3!";
    setButtonsEnabled(false);
  }
}

function reset() {
  userScore = 0;
  pcScore = 0;
  finished = false;
  updateScores();
  setButtonsEnabled(true);
  ui.result.textContent = "Choose your move";
  ui.result.style.color = "var(--white)";
  ui.choices.textContent = "";
}

ui.buttons.forEach((button) => {
  button.addEventListener("click", () => play(button.dataset.move));
});
ui.reset.addEventListener("click", reset);
ui.bestOfThree.addEventListener("change", reset);

document.addEventListener("keydown", (event) => {
  const keyMoves = { "1": "rock", "2": "paper", "3": "scissors" };
  if (keyMoves[event.key]) play(keyMoves[event.key]);
  if (event.key.toLowerCase() === "r") reset();
});
