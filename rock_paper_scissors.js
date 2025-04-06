let userMove = '';
let computerMove = '';
let result = '';
let autoPlayDecider = 0;

let score = {
    wins: 0,
    losses: 0,
    ties: 0
};

score = JSON.parse(localStorage.getItem('score'));

function userMoveFunction(chosenMove) {
    userMove = chosenMove;
}

function userMoveAutoPlayFunction() {
    var randomNumber = Math.random()

    if (randomNumber < (1/3)) {
        userMove = 'rock';
    }
    else if (randomNumber < (2/3)) {
        userMove = 'paper';
    }
    else {
        userMove = 'scissors';
    }
}

function computerMoveFunction() {
    var randomNumber = Math.random()

    if (randomNumber < (1/3)) {
        computerMove = 'rock';
    }
    else if (randomNumber < (2/3)) {
        computerMove = 'paper';
    }
    else {
        computerMove = 'scissors';
    }
}

function decideResult() {
    if (userMove === 'rock') {
        if (computerMove === 'rock') {
            result = 'You tied'
        }
        else if (computerMove === 'paper') {
            result = 'You lose'
        }
        else {
            result = 'You win';
        }
    }

    else if (userMove === 'paper') {
        if (computerMove === 'rock') {
            result = 'You win';
        }
        else if (computerMove === 'paper') {
            result = 'You tied';
        }
        else {
            result = 'You lose';
        }
    }

    else {
        if (computerMove === 'rock') {
            result = 'You lose';
        }
        else if (computerMove === 'paper') {
            result = 'You win';
        }
        else {
            result = 'You tied';
        }
    }
}

function addToScore() {
    if (result === 'You win') {
        score.wins += 1;
    }
    else if (result === 'You lose') {
        score.losses += 1;
    }
    else {
        score.ties += 1;
    }

    localStorage.setItem('score',JSON.stringify(score));
}

function printingScore() {
    
    document.querySelector('.js-score').innerHTML = `Wins: ${score.wins} Losses: ${score.losses}  Ties: ${score.ties}`;
}

function printingRest() {
    document.querySelector('.js-result').innerHTML = result;
    document.querySelector('.js-components').innerHTML = 
        `You 
        <img src = "../images/${userMove}-emoji.png" class = ${userMove}-icon>
        <img src = "../images/${computerMove}-emoji.png" class = ${computerMove}-icon>
        Computer`;
    printingScore()
}

function resetScore() {
    score = {wins: 0, losses: 0, ties: 0};
    printingScore();
    localStorage.setItem('score',JSON.stringify(score));
}

//intervalID needs to be global because (otherwise) it will be reset every time in if loop (I think)

let intervalID;

function changeAutoPlayText() {

    button = document.querySelector('.auto-play-button')

    if (button.innerHTML === 'Auto Play') {
        button.innerHTML = 'Stop';

        intervalID = setInterval(function() {
            userMoveAutoPlayFunction();
            computerMoveFunction();
            decideResult();
            addToScore();
            printingRest();
        }, 1000);

    }
        
    else if (button.innerHTML === 'Stop') {
        button.innerHTML = 'Auto Play';

        clearInterval(intervalID);

    }
}

document.querySelector('.rock-button').addEventListener('click', () => {
    userMoveFunction('rock'); computerMoveFunction(); decideResult(); addToScore(); printingRest();
})

document.querySelector('.paper-button').addEventListener('click', () => {
    userMoveFunction('paper'); computerMoveFunction(); decideResult(); addToScore(); printingRest();
})

document.querySelector('.scissors-button').addEventListener('click', () => {
    userMoveFunction('scissors'); computerMoveFunction(); decideResult(); addToScore(); printingRest();
})

document.querySelector('.reset-button').addEventListener('click', () => {
    resetScore();
})

document.querySelector('.auto-play-button').addEventListener('click', () => {
    changeAutoPlayText();
})

//CODE TO MAKE IT SO THAT IF I PRESS 'r' ROCK IS PLAYED (KEYDOWN FUNCTION USED)

//Explanation: document.body.addEventListener listens for a specific event (it listens for anything to happen - key to be pressed, cursor clicking on the page, ANYTHING) and it saves "whatever event that happened" (in this case 'keydown' because that's our first parameter in the method addEventListener) in an object inside document.body; the name of that object is event

//here we are telling it to listen for a 'keydown' and passing that event (which is an object) as the second parameter in the addEventListener method, which is also a function (we are passing the event through our generic function which is inside the addEventListener function)

document.body.addEventListener('keydown', (event) => {
    if (event.key === 'r') {
        userMoveFunction('rock'); computerMoveFunction(); decideResult(); addToScore(); printingRest();
    }

    else if (event.key === 'p') {
        userMoveFunction('paper'); computerMoveFunction(); decideResult(); addToScore(); printingRest();
    }

    else if (event.key === 's') {
        userMoveFunction('scissors'); computerMoveFunction(); decideResult(); addToScore(); printingRest();
    }
})
