console.log(location.search) // lee los argumentos pasados a este formulario
var id = location.search.substr(4)
console.log(id)
const { createApp } = Vue
createApp({
    data() {
        return {
            id: 0,
            nombre: "",
            autor: "",
            idioma: "",
            anio: "",
            genero: "",
            imagen: "",
            stock: 0,
            prestamo: false,
            url: 'https://wann.pythonanywhere.com/libros/' + id,
        }
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {

                    console.log(data)
                    this.id = data.id;
                    this.titulo = data.titulo;
                    this.autor = data.autor;
                    this.idioma = data.idioma;
                    this.anio = data.anio;
                    this.genero = data.genero;
                    this.imagen = data.imagen;
                    this.stock = data.stock;
                    this.prestamo = data.prestamo;
                })
                .catch(err => {
                    console.error(err);
                    this.error = true
                })
        },
        modificar() {
            let libro = {
                titulo: this.titulo,
                autor: this.autor,
                idioma: this.idioma,
                anio: this.anio,
                genero: this.genero,
                stock: this.stock,
                imagen: this.imagen,
                prestamo: this.prestamo
            }
            var options = {
                body: JSON.stringify(libro),
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            }
            fetch(this.url, options)
                .then(function () {
                    alert("Registro modificado")
                    window.location.href = "../templates/libros.html";
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Modificar")
                })
        }
    },
    created() {
        this.fetchData(this.url)
    },
}).mount('#app')