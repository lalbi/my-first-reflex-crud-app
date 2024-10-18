from reflex import App, route
from models import Categoria

# Página principal que lista todas las categorías
@route('/')
def listar_categorias():
    categorias = Categoria.all()  # Obtenemos todas las categorías
    return f"""
    <h1>Lista de Categorías</h1>
    <table>
      <tr><th>ID</th><th>Nombre</th><th>Acciones</th></tr>
      {"".join(f"<tr><td>{cat.id}</td><td>{cat.nombre}</td><td><a href='/edit/{cat.id}'>Editar</a> | <a href='/delete/{cat.id}'>Eliminar</a></td></tr>" for cat in categorias)}
    </table>
    <form method='POST' action='/create'>
        <input type='text' name='nombre' placeholder='Nombre de la categoría'>
        <button type='submit'>Agregar</button>
    </form>
    """

# Crear nueva categoría
@route('/create', methods=['POST'])
def crear_categoria(nombre: str):
    Categoria.create(nombre=nombre)
    return 'redirect:/'

# Editar una categoría
@route('/edit/{id}', methods=['GET', 'POST'])
def editar_categoria(id: int, nombre: str = None):
    categoria = Categoria.get(id=id)
    if nombre:
        categoria.nombre = nombre
        categoria.save()
        return 'redirect:/'
    return f"""
    <h1>Editar Categoría</h1>
    <form method='POST'>
        <input type='text' name='nombre' value='{categoria.nombre}' placeholder='Nombre de la categoría'>
        <button type='submit'>Guardar</button>
    </form>
    """

# Eliminar una categoría
@route('/delete/{id}', methods=['POST'])
def eliminar_categoria(id: int):
    Categoria.delete(id=id)
    return 'redirect:/'

# Inicializar la aplicación
app = App(routes=[listar_categorias, crear_categoria, editar_categoria, eliminar_categoria])
