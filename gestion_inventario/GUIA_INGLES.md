# Video Presentation Script in English (Actividad 6)

This guide provides a concise, structured script to present the project in English for your evaluation video.

---

## 🎬 Suggested Video Outline (3-5 minutes)

### 1. Introduction (30 seconds)
> "Hello everyone! My name is [Your Name], and today I am going to present my Inventory Management System developed in Java. 
> The main goal of this project is to implement data persistence using SQLite, JDBC, and the DAO design pattern."

### 2. Architecture and Structure (45 seconds)
> "The project follows a clean architecture based on four main classes:
> 1. **Producto**: The model class representing product attributes: code, name, description, price, and stock quantity.
> 2. **ConexionDB**: Manages the SQLite database connection through JDBC and ensures the `Producto` table is created automatically.
> 3. **ProductoDAO**: Encapsulates the CRUD operations using parameterized PreparedStatements to prevent SQL injection and manage resources safely.
> 4. **MenuPrincipal**: The console user interface that provides an interactive menu and validates all user inputs."

### 3. Live Demonstration (CRUD Operations) (2-3 minutes)

#### RF1 - Create (Registering a Product)
> "Let's start by running the application.
> I will select Option 1 to register a new product:
> - Code: `P001`
> - Name: `Wireless Mouse`
> - Description: `Ergonomic 1600 DPI`
> - Price: `19.99`
> - Quantity: `25`
> As you can see, the product has been successfully registered."

#### RF2 - Read (Consulting and Searching)
> "Now, I will select Option 2 to list all products in our inventory. The product `P001` appears on the screen.
> Next, with Option 3, I can search specifically by code `P001`.
> With Option 4, I can search by keyword, for example typing 'Mouse', and it finds matching records."

#### RF3 - Update (Modifying Product Information)
> "Using Option 5, we can update an existing product. 
> I enter the code `P001`, and the system shows the current values. 
> I'll change the price to `17.50` and the quantity to `30`. 
> When we list the products again, we can see the updated information."

#### RF4 - Delete (Deleting with Confirmation)
> "Option 6 allows us to delete a product. 
> If I choose code `P001`, the system asks for confirmation: 'Are you sure you want to delete this product? (S/N)'. 
> If I type 'S', it is safely removed from the database."

### 4. Demonstrating Data Persistence (RF5) (45 seconds)
> "To demonstrate data persistence:
> I will quickly add a product `P100`, 'Gaming Laptop'.
> Now I choose Option 7 to exit the application. The program is completely closed.
> When I launch the program again and select Option 2 to list products, notice that `P100` is still there. 
> The data was saved permanently in the `inventario.db` file."

### 5. Conclusion (15 seconds)
> "In conclusion, this project fulfills all CRUD operations, ensures reliable data validation, and guarantees persistence across executions using Java, JDBC, and SQLite. Thank you very much for your time!"
