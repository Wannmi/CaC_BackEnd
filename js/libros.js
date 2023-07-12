const { createApp } = Vue
createApp({
    data() {
        return {
            productos: [],
            //url:'http://localhost:5000/productos',
            // si el backend esta corriendo local usar localhost 5000(si no lo subieron a pythonanywhere)
            url: 'https://wann.pythonanywhere.com/libros', // si ya lo subieron a pythonanywhere
            error: false,
            cargando: true,
            /*atributos para el guardar los valores del formulario */
            /*Es como un placeholder cuando se agrega un nuevo producto*/
            id: 0,
            titulo: "",
            autor: "",
            idioma: "",
            anio: "",
            genero: "",
            imagen: "",
            stock: 0,
            prestamo: false,
            /*atributo para alternar modo usuario o administrador*/
            admin: false,
        }
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    this.libros = data;
                    this.cargando = false
                })
                .catch(err => {
                    console.error(err);
                    this.error = true
                })
        },
        eliminar(libro) {
            const url = this.url + '/' + libro;
            var options = {
                method: 'DELETE',
            }
            fetch(url, options)
                .then(res => res.text()) // or res.json()
                .then(res => {
                    location.reload();
                })
        },
        grabar() {
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
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            }
            fetch(this.url, options)
                .then(function () {
                    alert("Registro grabado")
                    window.location.href = "../index.html";
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Grabar")
                })
        },
        showMessage() {
            alert("Has reservado este libro");
          },
        modAdm(mod){
            this.admin = mod;
        }
    },
    created() {
        this.fetchData(this.url)
    },
}).mount('#app')
