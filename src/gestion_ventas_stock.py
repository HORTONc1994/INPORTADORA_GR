from abc import ABC, abstractmethod

# 1. Interfaz Estrategia para el cálculo de ventas en INPORTADORA_GR
class EstrategiaVenta(ABC):
    @abstractmethod
    def calcular_total(self, subtotal: float) -> float:
        pass

# 2. Estrategias Concretas según el tipo de cliente/venta
class VentaDetalle(EstrategiaVenta):
    """Venta estándar al detalle: aplica 18% de ITBIS sin descuento."""
    def calcular_total(self, subtotal: float) -> float:
        itbis = subtotal * 0.18
        return round(subtotal + itbis, 2)

class VentaMayorista(EstrategiaVenta):
    """Venta al por mayor: aplica 15% de descuento por volumen + 18% ITBIS."""
    def calcular_total(self, subtotal: float) -> float:
        con_descuento = subtotal * 0.85
        itbis = con_descuento * 0.18
        return round(con_descuento + itbis, 2)

class VentaExenta(EstrategiaVenta):
    """Venta con comprobante gubernamental o régimen especial exento de ITBIS."""
    def calcular_total(self, subtotal: float) -> float:
        return round(subtotal, 2)

# 3. Contexto: Módulo de Procesamiento de Ventas y Control de Stock
class ProcesadorVenta:
    def __init__(self, estrategia: EstrategiaVenta):
        self._estrategia = estrategia

    def cambiar_estrategia(self, estrategia: EstrategiaVenta) -> None:
        self._estrategia = estrategia

    def procesar_venta(self, producto: str, cantidad: int, precio_unitario: float, stock_actual: int) -> dict:
        if cantidad > stock_actual:
            raise ValueError(f"Stock insuficiente para '{producto}'. Disponible: {stock_actual}")
        
        subtotal = cantidad * precio_unitario
        total_final = self._estrategia.calcular_total(subtotal)
        nuevo_stock = stock_actual - cantidad

        return {
            "producto": producto,
            "cantidad": cantidad,
            "subtotal": subtotal,
            "total_cobrar": total_final,
            "stock_restante": nuevo_stock
        }

# --- Ejecución de prueba para evidencia en consola ---
if __name__ == "__main__":
    procesador = ProcesadorVenta(VentaDetalle())
    print("1. Venta Detalle:", procesador.procesar_venta("Taladro Percutor", 2, 3500.0, 20))

    procesador.cambiar_estrategia(VentaMayorista())
    print("2. Venta Mayorista:", procesador.procesar_venta("Taladro Percutor", 10, 3500.0, 18))

    procesador.cambiar_estrategia(VentaExenta())
    print("3. Venta Exenta:", procesador.procesar_venta("Taladro Percutor", 5, 3500.0, 8))
