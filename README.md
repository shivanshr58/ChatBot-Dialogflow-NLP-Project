# ChatBot-NLP-Project


## About the Project:

Welcome to the Pandeyji Eatery Chatbot project! I'm Shivansh, and I'm excited to share my journey of creating this interactive chatbot designed for Pandeyji Eatery. This project combines elements of FastAPI, Dialogflow, and a local MySQL database to facilitate a seamless ordering experience.

### The Chatbot:

The Pandeyji Eatery Chatbot is designed to make the ordering process smooth and enjoyable. Here's how it works:

1. **New Order:**
   - Users can initiate a new order, and the chatbot guides them through the menu.

2. **Add to Order:**
   - Users can add multiple items to their ongoing order, with the chatbot keeping track of each addition.

3. **Remove from Order:**
   - In case of changes, users can remove specific items from their order, and the chatbot updates the order summary.

4. **Complete Order:**
   - Once satisfied, users can complete their order, and the chatbot records it in the database.

5. **Track Order:**
   - Users can inquire about the status of their order by providing the order ID.

### What the Chatbot Can Do:

- **Place Orders:**
  - Users can place new orders, specifying the quantity of each item.

- **Modify Orders:**
  - Users can add or remove items from their ongoing orders.

- **Order Tracking:**
  - The chatbot provides real-time order tracking, giving users updates on their order status.

### Project Components:

- **Coding:**
  - `main.py`: Main script handling chatbot requests using FastAPI.
  - `db_helper.py`: Python script for database-related operations.
  - `generic_helper.py`: Python script containing generic helper functions.

- **DB:**
  - `pandeyji_eatery.sql`: MySQL database script containing table structures.

- **Website:**
  - `index.html`: Dummy website HTML code.
  - `style.css`: CSS styling for the dummy website.

### How to Explore:

1. **Review Code:**
   - Explore the `coding` folder for the main scripts.
   - Understand how the chatbot processes orders and interacts with the database.

2. **Database Structure:**
   - Check the `db` folder for the MySQL database script (`pandeyji_eatery.sql`) to understand the data structure.

3. **Website Dummy Content:**
   - Examine the `website` folder for the dummy website HTML and CSS (`home.html` and `styles.css`) used for chatbot interaction.

### Why This Project:

This project serves as both a practical implementation of conversational interfaces and a showcase of my coding skills. I wanted to demonstrate how chatbots can enhance user engagement and simplify complex processes like food ordering.

Feel free to explore the code and project structure. If you have any questions or suggestions, I'd love to hear from you!
