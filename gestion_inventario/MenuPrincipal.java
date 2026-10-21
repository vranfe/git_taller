import java.math.BigDecimal;
import java.util.List;
import java.util.Scanner;

/**
 * Menú principal por consola para interactuar con el sistema de inventario.
 */
public class MenuPrincipal {
    private static final Scanner scanner = new Scanner(System.in);
    private static final ProductoDAO dao = new ProductoDAO();

    public static void main(String[] args) {
        ConexionDB.crearTabla();
        int opcion = 0;

        do {
            System.out.println("\n==================================");
            System.out.println("      GESTIÓN DE INVENTARIO       ");
            System.out.println("==================================");
            System.out.println("1. Registrar producto");
            System.out.println("2. Consultar todos los productos");
            System.out.println("3. Buscar producto por código");
            System.out.println("4. Buscar productos por nombre");
            System.out.println("5. Actualizar producto");
            System.out.println("6. Eliminar producto");
            System.out.println("7. Salir");
            System.out.print("Seleccione una opción: ");

            try {
                opcion = Integer.parseInt(scanner.nextLine().trim());
            } catch (NumberFormatException e) {
                opcion = 0;
            }

            switch (opcion) {
                case 1: registrar(); break;
                case 2: listar(); break;
                case 3: buscarPorCodigo(); break;
                case 4: buscarPorNombre(); break;
                case 5: actualizar(); break;
                case 6: eliminar(); break;
                case 7: System.out.println("Datos guardados en SQLite. ¡Programa finalizado!"); break;
                default: System.out.println("Opción no válida. Intente nuevamente.");
            }
        } while (opcion != 7);
    }

    private static void registrar() {
        System.out.println("\n--- REGISTRAR PRODUCTO ---");
        System.out.print("Código: ");
        String codigo = scanner.nextLine().trim();
        if (codigo.isEmpty()) {
            System.out.println("El código no puede estar vacío.");
            return;
        }
        if (dao.buscarPorCodigo(codigo) != null) {
            System.out.println("Error: Ya existe un producto con el código '" + codigo + "'.");
            return;
        }

        System.out.print("Nombre: ");
        String nombre = scanner.nextLine().trim();
        if (nombre.isEmpty()) {
            System.out.println("El nombre es obligatorio.");
            return;
        }

        System.out.print("Descripción: ");
        String descripcion = scanner.nextLine().trim();

        System.out.print("Precio: ");
        BigDecimal precio;
        try {
            precio = new BigDecimal(scanner.nextLine().trim().replace(",", "."));
            if (precio.compareTo(BigDecimal.ZERO) < 0) {
                System.out.println("El precio no puede ser negativo.");
                return;
            }
        } catch (Exception e) {
            System.out.println("Precio inválido.");
            return;
        }

        System.out.print("Cantidad: ");
        int cantidad;
        try {
            cantidad = Integer.parseInt(scanner.nextLine().trim());
            if (cantidad < 0) {
                System.out.println("La cantidad no puede ser negativa.");
                return;
            }
        } catch (Exception e) {
            System.out.println("Cantidad inválida.");
            return;
        }

        Producto nuevo = new Producto(codigo, nombre, descripcion, precio, cantidad);
        if (dao.insertar(nuevo)) {
            System.out.println("¡Producto registrado exitosamente!");
        }
    }

    private static void listar() {
        System.out.println("\n--- INVENTARIO DE PRODUCTOS ---");
        List<Producto> productos = dao.listarTodos();
        if (productos.isEmpty()) {
            System.out.println("No hay productos registrados.");
        } else {
            for (Producto p : productos) {
                System.out.println(p);
            }
            System.out.println("Total: " + productos.size() + " producto(s).");
        }
    }

    private static void buscarPorCodigo() {
        System.out.println("\n--- BUSCAR POR CÓDIGO ---");
        System.out.print("Ingrese código: ");
        String codigo = scanner.nextLine().trim();
        Producto p = dao.buscarPorCodigo(codigo);
        if (p != null) {
            System.out.println("Producto encontrado: " + p);
        } else {
            System.out.println("No se encontró ningún producto con el código '" + codigo + "'.");
        }
    }

    private static void buscarPorNombre() {
        System.out.println("\n--- BUSCAR POR NOMBRE ---");
        System.out.print("Ingrese nombre a buscar: ");
        String nombre = scanner.nextLine().trim();
        List<Producto> encontrados = dao.buscarPorNombre(nombre);
        if (encontrados.isEmpty()) {
            System.out.println("No se encontraron productos con ese nombre.");
        } else {
            for (Producto p : encontrados) {
                System.out.println(p);
            }
        }
    }

    private static void actualizar() {
        System.out.println("\n--- ACTUALIZAR PRODUCTO ---");
        System.out.print("Código del producto a modificar: ");
        String codigo = scanner.nextLine().trim();
        Producto p = dao.buscarPorCodigo(codigo);
        if (p == null) {
            System.out.println("El producto con código '" + codigo + "' no existe.");
            return;
        }

        System.out.println("Datos actuales: " + p);
        System.out.print("Nuevo precio (Enter para conservar actual): ");
        String precioStr = scanner.nextLine().trim();
        if (!precioStr.isEmpty()) {
            try {
                BigDecimal nuevoPrecio = new BigDecimal(precioStr.replace(",", "."));
                if (nuevoPrecio.compareTo(BigDecimal.ZERO) >= 0) {
                    p.setPrecio(nuevoPrecio);
                } else {
                    System.out.println("El precio no puede ser negativo.");
                    return;
                }
            } catch (Exception e) {
                System.out.println("Precio inválido. Operación cancelada.");
                return;
            }
        }

        System.out.print("Nueva cantidad (Enter para conservar actual): ");
        String cantStr = scanner.nextLine().trim();
        if (!cantStr.isEmpty()) {
            try {
                int nuevaCantidad = Integer.parseInt(cantStr);
                if (nuevaCantidad >= 0) {
                    p.setCantidad(nuevaCantidad);
                } else {
                    System.out.println("La cantidad no puede ser negativa.");
                    return;
                }
            } catch (Exception e) {
                System.out.println("Cantidad inválida. Operación cancelada.");
                return;
            }
        }

        System.out.print("Nueva descripción (Enter para conservar actual): ");
        String nuevaDesc = scanner.nextLine().trim();
        if (!nuevaDesc.isEmpty()) {
            p.setDescripcion(nuevaDesc);
        }

        if (dao.actualizar(p)) {
            System.out.println("¡Producto actualizado exitosamente!");
            System.out.println("Datos nuevos: " + p);
        }
    }

    private static void eliminar() {
        System.out.println("\n--- ELIMINAR PRODUCTO ---");
        System.out.print("Código del producto a eliminar: ");
        String codigo = scanner.nextLine().trim();
        Producto p = dao.buscarPorCodigo(codigo);
        if (p == null) {
            System.out.println("El producto con código '" + codigo + "' no existe.");
            return;
        }

        System.out.println("Producto a eliminar: " + p);
        System.out.print("¿Está seguro de eliminarlo? (S/N): ");
        String confirmacion = scanner.nextLine().trim();
        if (confirmacion.equalsIgnoreCase("S")) {
            if (dao.eliminar(codigo)) {
                System.out.println("¡Producto eliminado exitosamente!");
            }
        } else {
            System.out.println("Operación cancelada. El producto no fue eliminado.");
        }
    }
}
