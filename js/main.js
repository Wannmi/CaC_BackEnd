document.getElementById("header").innerHTML = ` 
<nav class="navbar navbar-expand-sm navbar-light bg-light">
    <div class="container">
        <a class="navbar-brand" href="../index.html">Biblioteca</a>
    </div>
        <button type="button" class="btn btn-outline-primary me-2" v-on:click="modAdm(false)">Usuario</button>
        <button type="button" class="btn btn-outline-secondary me-2" v-on:click="modAdm(true)">Admin</button>
</nav>`