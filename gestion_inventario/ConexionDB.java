import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * Gestiona la conexión JDBC con SQLite y la creación de la tabla.
 */
public class ConexionDB {
    private static final String URL = "jdbc:sqlite:inventario.db";

    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL);
    }

    public static void crearTabla() {
        String sql = "CREATE TABLE IF NOT EXISTS Producto ("
                   + "codigo VARCHAR(20) PRIMARY KEY NOT NULL, "
                   + "nombre VARCHAR(100) NOT NULL, "
                   + "descripcion TEXT, "
                   + "precio DECIMAL(10,2) NOT NULL CHECK (precio >= 0), "
                   + "cantidad INTEGER NOT NULL CHECK (cantidad >= 0));";

        try (Connection conn = getConnection(); Statement stmt = conn.createStatement()) {
            stmt.execute(sql);
        } catch (SQLException e) {
            System.out.println("Error al inicializar la base de datos: " + e.getMessage());
        }
    }
}
