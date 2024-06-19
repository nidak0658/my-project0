let displayValue = '0';
let firstOperand = null;
let operator = null;
let waitingForSecondOperand = false;

const display = document.getElementById('display');

function addToDisplay(digit) {
    if (waitingForSecondOperand === true) {
        displayValue = digit;
        waitingForSecondOperand = false;
    } else {
        displayValue = displayValue === '0' ? digit : displayValue + digit;
    }
    updateDisplay();
}

function setOperator(op) {
    if (operator !== null && !waitingForSecondOperand) {
        calculate();
    }
    firstOperand = parseFloat(displayValue);
    operator = op;
    waitingForSecondOperand = true;
}

function calculate() {
    if (operator === null || waitingForSecondOperand) return;

    const secondOperand = parseFloat(displayValue);
    let result = 0;

    switch (operator) {
        case '+':
            result = firstOperand + secondOperand;
            break;
        case '-':
            result = firstOperand - secondOperand;
            break;
        case '*':
            result = firstOperand * secondOperand;
            break;
        case '/':
            result = firstOperand / secondOperand;
            break;
        default:
            return;
    }

    displayValue = result.toString();
    operator = null;
    firstOperand = result;
    waitingForSecondOperand = true;
    updateDisplay();
}

function clearDisplay() {
    displayValue = '0';
    firstOperand = null;
    operator = null;
    waitingForSecondOperand = false;
    updateDisplay();
}

function updateDisplay() {
    display.textContent = displayValue;
}
