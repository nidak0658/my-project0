document.addEventListener('DOMContentLoaded', function() {
    const loginBtn = document.getElementById('login-btn');
    const logoutBtn = document.getElementById('logout-btn');
    const feedsContainer = document.getElementById('feeds');

    let loggedIn = false; // Flag to track user login status

    // Function to simulate user login (for demonstration)
    function login() {
        // Simulate successful login
        loggedIn = true;
        loginBtn.style.display = 'none';
        logoutBtn.style.display = 'block';
        fetchSocialMediaFeeds(); // Fetch feeds after login
    }

    // Function to simulate user logout (for demonstration)
    function logout() {
        // Simulate logout
        loggedIn = false;
        loginBtn.style.display = 'block';
        logoutBtn.style.display = 'none';
        clearFeeds(); // Clear feeds on logout
    }

    // Function to fetch social media feeds (simulated)
    function fetchSocialMediaFeeds() {
        // Simulated data for demonstration
        const feeds = [
            { platform: 'Twitter', content: 'Tweet content...' },
            { platform: 'Facebook', content: 'Post content...' },
            { platform: 'Instagram', content: 'Photo caption...' }
            // Add more feeds as needed
        ];

        // Clear previous feeds
        clearFeeds();

        // Display feeds
        feeds.forEach(feed => {
            const feedItem = document.createElement('div');
            feedItem.classList.add('feed-item');
            feedItem.innerHTML = `
                <h2>${feed.platform}</h2>
                <p>${feed.content}</p>
            `;
            feedsContainer.appendChild(feedItem);
        });
    }

    // Function to clear feeds
    function clearFeeds() {
        feedsContainer.innerHTML = '';
    }

    // Event listeners for login and logout buttons (simulated)
    loginBtn.addEventListener('click', login);
    logoutBtn.addEventListener('click', logout);

    // Initialize: Hide logout button initially
    logoutBtn.style.display = 'none';
});
