# Comprehensive English Video Presentation Script (4 to 6 Minutes)

This script is structured specifically to meet the evaluation criteria:
- **Target Duration:** 4:30 – 5:30 minutes (comfortably inside the required 4–6 minute range).
- **Core Topics Covered:** Architecture & DAO pattern, JDBC SQLite persistence process, live CRUD demonstration with validations, and restart persistence test.
- **Format:** Paired with on-screen visual instructions (*Visual Cue*) so you know exactly what to show while speaking.

---

## ⏱️ Video Timing Breakdown

| Section | Topic | Estimated Time |
| :--- | :--- | :---: |
| **Section 1** | Introduction & Project Overview | 0:00 – 0:40 (40s) |
| **Section 2** | Architecture & Layered DAO Design | 0:40 – 1:50 (70s) |
| **Section 3** | Data Persistence with JDBC & SQLite | 1:50 – 2:50 (60s) |
| **Section 4** | Live CRUD Demonstration & Input Validations | 2:50 – 4:30 (100s) |
| **Section 5** | Persistence Verification (App Restart Test) | 4:30 – 5:10 (40s) |
| **Section 6** | Conclusion & Closing | 5:10 – 5:30 (20s) |
| **Total** | | **~ 5 minutes 30 seconds** |

---

## 🎙️ Complete Script (Scene by Scene)

### Section 1: Introduction & Project Overview (0:00 – 0:40)

**[Visual Cue]**: Show your face on webcam or display the project title slide / README file in your code editor.

> "Hello professor and classmates! My name is **[Your Full Name]**, and today I am presenting my Inventory Management System developed in Java.
>
> The main objective of this application is to solve the problem of product catalog management for a business, ensuring complete data persistence using JDBC and SQLite, while adhering to professional software engineering standards such as the Data Access Object pattern and strict input validation.
>
> In this presentation, I will walk you through the system's architecture, explain our database persistence mechanism, and demonstrate each CRUD operation in action."

---

### Section 2: Solution Architecture & Design Patterns (0:40 – 1:50)

**[Visual Cue]**: Open your IDE (IntelliJ, Eclipse, or VS Code) and show the project explorer folder tree, expanding the files: `Producto.java`, `ProductoDAO.java`, `ConexionDB.java`, and `MenuPrincipal.java`.

> "Let's begin by examining the software architecture. To maintain a clean separation of concerns, the project is structured into four distinct components:
>
> 1. **The Model Layer — `Producto.java`**: This is our domain entity. It encapsulates all product attributes: the unique alphanumeric code, product name, detailed description, monetary price using `BigDecimal` for precise decimal calculations, and stock quantity as an integer.
>
> 2. **The Data Access Layer — `ProductoDAO.java`**: This class isolates all SQL communication from the business logic. It implements the DAO design pattern, exposing clean methods such as `insertar`, `listarTodos`, `buscarPorCodigo`, `actualizar`, and `eliminar`.
>
> 3. **The Infrastructure Layer — `ConexionDB.java`**: It centralizes the JDBC connection lifecycle and automates database initialization.
>
> 4. **The Presentation Layer — `MenuPrincipal.java`**: This is our interactive console interface. It is responsible for user interaction, menu rendering, and rigorous data sanitization before invoking the DAO.
>
> This separation guarantees high cohesion and low coupling, making the codebase maintainable and easy to extend."

---

### Section 3: Data Persistence with JDBC & SQLite (1:50 – 2:50)

**[Visual Cue]**: Open `ConexionDB.java` in the editor, highlight the `URL` string and the `try-with-resources` block in `crearTabla()`. Then switch to `ProductoDAO.java` and highlight a `PreparedStatement`.

> "Now, let's look at how data persistence is achieved.
>
> We selected SQLite as our embedded relational database engine. Because it is serverless, the entire database is stored in a single local file called `inventario.db`. This makes deployment straightforward and lightweight.
>
> The connection is established via the official `sqlite-jdbc` driver using the connection string: `jdbc:sqlite:inventario.db`.
>
> When the application boots, the `crearTabla` method executes a DDL script that automatically creates the `Producto` table if it does not already exist. Notice that we enforce integrity constraints directly at the database level: the code is a non-null Primary Key, and both the price and quantity have SQL `CHECK` constraints to prevent negative values.
>
> Furthermore, throughout `ProductoDAO`, we rely strictly on parameterized `PreparedStatement` queries with positional placeholders. This completely eliminates SQL injection vulnerabilities and ensures safe type mapping. We also utilize Java's `try-with-resources` statement across all database calls, guaranteeing that connections, statements, and result sets are deterministically closed, avoiding memory leaks."

---

### Section 4: Live CRUD Demonstration & Input Validations (2:50 – 4:30)

**[Visual Cue]**: Switch to the terminal. Run `ejecutar.bat` or `java -cp ".;lib/*" MenuPrincipal`. The main menu appears on screen.

> "Now, let's see the application in action. I will launch the system using our execution script.
>
> As you can see, we have a clean console menu with seven options. Let's test each requirement step by step.

#### 1. Create (RF1 - Register Product)
> "First, I select Option 1 to register a new product. 
> Notice what happens if I attempt to enter a negative price, such as `-15.00`: the system catches it immediately and rejects the input. The same safety validation applies to negative quantities and empty codes.
> Now, let's enter valid data:
> - Code: `P001`
> - Name: `Mechanical Keyboard`
> - Description: `RGB Backlit Blue Switches`
> - Price: `59.99`
> - Quantity: `20`
> The product is successfully inserted into SQLite."

#### 2. Read (RF2 - Consult and Search)
> "Next, let's verify retrieval.
> - With **Option 2**, we list all registered products. We can see product `P001` displayed with all its formatted attributes.
> - With **Option 3**, we can search by exact code `P001`. It returns our keyboard immediately.
> - With **Option 4**, we can perform a partial text search by name. If I type 'key', the system matches and displays the product, showing that our case-insensitive SQL query works as expected."

#### 3. Update (RF3 - Modify Product)
> "Let's update our item using **Option 5**.
> I enter the code `P001`. The system displays the current values and prompts for new ones. If we press Enter without typing, it retains the existing value.
> Let's change the price to `49.50` and stock quantity to `35`. 
> Upon saving, the updated information is reflected in the database."

#### 4. Delete (RF4 - Remove with Confirmation)
> "For our fourth operation, let's test deletion using **Option 6**.
> If I choose code `P001`, the system displays the product details and asks for explicit confirmation: 'Are you sure you want to delete this product? (S/N)'.
> If I type 'N', the operation is cancelled safely.
> Let's register a temporary item `TEMP`, and now delete it typing 'S'. The record is permanently removed."

---

### Section 5: Persistence Verification (App Restart Test) (4:30 – 5:10)

**[Visual Cue]**: Add a new product (e.g., `P200 - Gaming Headset`), select Option 7 to exit the program, show the terminal returning to the OS prompt, and point out the `inventario.db` file in Windows Explorer. Then relaunch the program and select Option 2.

> "To fulfill Activity 5 and Requirement RF5, we must demonstrate that data survives complete application shutdown.
>
> I will register a permanent product: code `P200`, name `Gaming Headset`, price `75.00`, quantity `12`.
>
> Now, I select **Option 7** to exit the application. As you can see, the Java process has terminated completely and we are back at the operating system prompt. Notice here in our file explorer that `inventario.db` has been updated on disk.
>
> Now, I will re-execute the program from scratch.
> I select **Option 2** to list all products. As you can observe, product `P200` is immediately retrieved with all its data intact. This proves that our persistence mechanism through SQLite is fully functional and reliable."

---

### Section 6: Conclusion & Wrap-up (5:10 – 5:30)

**[Visual Cue]**: Return to the IDE or show the terminal with the successful list output.

> "In conclusion, this project satisfies all functional requirements: registering, querying, updating, deleting, and persisting product data.
>
> From a technical standpoint, we demonstrated a robust architecture utilizing the DAO pattern, parameterized JDBC queries, and SQLite constraints, wrapped in a user-friendly console application.
>
> Thank you very much for your attention!"

---

## 💡 Pronunciation & Technical Keywords Guide

To ensure high clarity during your English recording, review these common technical terms:

| Word / Term | Approximate Phonetic Guide | Meaning in Context |
| :--- | :--- | :--- |
| **SQLite** | *ess-cue-el-lite* (`/ˌɛsˌkjuːˌɛlˈaɪt/`) | The database engine |
| **JDBC** | *jay-dee-bee-see* (`/ˌdʒeɪ diː biː ˈsiː/`) | Java Database Connectivity |
| **DAO** | *dee-ay-oh* or *dow* (`/ˌdiː eɪ ˈoʊ/`) | Data Access Object pattern |
| **Persistence** | *per-SIS-tens* (`/pərˈsɪstəns/`) | Storing data permanently |
| **PreparedStatement** | *pree-pehrd STATE-ment* | Parameterized SQL query |
| **BigDecimal** | *big-DESS-ih-mul* | Java high-precision number class |
| **ResultSet** | *rih-ZULT-set* | Tabular SQL query result |
| **Constraints** | *kun-STRAYNTS* | Database validation rules (CHECK, PK) |
| **Injection** | *in-JEK-shun* | Security vulnerability prevented by parameters |

---

## 📋 Recording Checklist Before Pressing Record

- [ ] Make sure `inventario.db` is reset or clean before starting if you want a fresh demonstration.
- [ ] Have your terminal open with the font size set comfortably large (e.g., 16pt or 18pt) so viewers can read text easily.
- [ ] Have your code editor tabs open in order: `Producto.java` → `ProductoDAO.java` → `ConexionDB.java` → `MenuPrincipal.java`.
- [ ] Keep your microphone close to reduce background noise and speak at a steady, conversational pace.
