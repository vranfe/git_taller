-- Script SQL para SQLite
-- Tabla Producto
CREATE TABLE IF NOT EXISTS Producto (
    codigo VARCHAR(20) PRIMARY KEY NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL CHECK (precio >= 0),
    cantidad INTEGER NOT NULL CHECK (cantidad >= 0)
);

-- Registros de ejemplo (opcional)
INSERT INTO Producto (codigo, nombre, descripcion, precio, cantidad) VALUES
('P001', 'Laptop Lenovo', 'Core i5 8GB RAM 256GB SSD', 650.00, 10),
('P002', 'Mouse Inalámbrico', 'Óptico 1600 DPI', 15.00, 30),
('P003', 'Teclado Mecánico', 'RGB Switch Azul', 45.00, 15);
