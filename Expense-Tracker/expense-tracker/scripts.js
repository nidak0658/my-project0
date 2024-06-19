document.addEventListener('DOMContentLoaded', function() {
    const expenseForm = document.getElementById('expense-form');
    const descInput = document.getElementById('desc');
    const amountInput = document.getElementById('amount');
    const expenseList = document.getElementById('expense-list');
    
    // Initialize expenses array from local storage or set to empty array
    let expenses = JSON.parse(localStorage.getItem('expenses')) || [];
    
    // Function to render expenses
    function renderExpenses() {
        // Clear previous entries
        expenseList.innerHTML = '';
        
        // Render each expense
        expenses.forEach(function(expense, index) {
            const div = document.createElement('div');
            div.classList.add('expense');
            div.innerHTML = `
                <div>
                    <span>Description:</span> ${expense.desc}
                </div>
                <div>
                    <span>Amount:</span> $${expense.amount}
                </div>
                <button onclick="editExpense(${index})">Edit</button>
                <button onclick="deleteExpense(${index})">Delete</button>
            `;
            expenseList.appendChild(div);
        });
        
        // Save to local storage
        localStorage.setItem('expenses', JSON.stringify(expenses));
    }
    
    // Function to add an expense
    expenseForm.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const desc = descInput.value.trim();
        const amount = parseFloat(amountInput.value.trim());
        
        if (desc === '' || isNaN(amount) || amount <= 0) {
            alert('Please enter valid description and amount.');
            return;
        }
        
        const expense = {
            desc: desc,
            amount: amount
        };
        
        expenses.push(expense);
        renderExpenses();
        
        // Clear input fields
        descInput.value = '';
        amountInput.value = '';
    });
    
    // Function to edit an expense
    window.editExpense = function(index) {
        const editedDesc = prompt('Enter new description:');
        const editedAmount = parseFloat(prompt('Enter new amount:'));
        
        if (editedDesc === null || editedAmount === null || isNaN(editedAmount) || editedAmount <= 0) {
            alert('Invalid input. Please try again.');
            return;
        }
        
        expenses[index].desc = editedDesc;
        expenses[index].amount = editedAmount;
        
        renderExpenses();
    };
    
    // Function to delete an expense
    window.deleteExpense = function(index) {
        if (confirm('Are you sure you want to delete this expense?')) {
            expenses.splice(index, 1);
            renderExpenses();
        }
    };
    
    // Initial rendering
    renderExpenses();
});
