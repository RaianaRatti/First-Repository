let todoObjectList = [];
let todoListString = '';

function printOutBoth() {
    todoListString = '';

    for (let index = 0; index < todoObjectList.length; index++) {
        const element = `
            <div>${todoObjectList[index].name}</div>
            <div>${todoObjectList[index].dueDate}</div>
            <button class = "delete-button" onclick = "deleteTask(${index})">Delete</button>
        `

        todoListString = todoListString + element;
    }

    document.querySelector('.display-list-elements').innerHTML = todoListString;
}

function whenYouClickAdd() {
    const choreName = document.querySelector('.chore-input-textbox').value;
    const dueDate = document.querySelector('.date-input-box').value;

    todoObjectList.push({ name: choreName, dueDate: dueDate });
    printOutBoth();

    document.querySelector('.chore-input-textbox').value = '';
}

function deleteTask(index) {
    todoObjectList.splice(index, 1); //delete one element starting at index
    printOutBoth();
}

function clearPlaceHolder(element) {
    element.placeholder = ''
}

function restorePlaceHolder(element, text) {
    if (element.value.trim() === '') {
        element.placeholder = 'Task';
    }
}

document.querySelector('.chore-input-textbox').addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        whenYouClickAdd();
        printOutBoth();
    }
})

document.querySelector('.date-input-box').addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        whenYouClickAdd();
        printOutBoth();
    }
})

document.querySelector('.add-button').addEventListener('click', () => {
        whenYouClickAdd();
        printOutBoth();
})