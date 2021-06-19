class Carrito{

    // Añadir producto
    comprarProducto(e){
        e.preventDefault();
        if(e.target.classList.contains('agregar-a-carrito')){
            const zapatilla = e.target.parentElement.parentElement.parentElement;
            this.leerDatos(zapatilla)
        }
    }

    leerDatos(zapatilla){
        const infoZapatilla = {
            foto : zapatilla.querySelector('.foto').value,
            modelo : zapatilla.querySelector('.modelo span').textContent,
            precio : zapatilla.querySelector('#precio span').textContent,
            id : zapatilla.querySelector('.agregar-a-carrito').getAttribute('data-id'),
            cantidad : 1,
            talla : zapatilla.querySelector('#talla').getAttribute('data-id'),
            stockId : zapatilla.querySelector('#talla').value
        }

        let zapatillasLS;
        let tallaLS;

        zapatillasLS = this.obtenerProductosLocalStorage();

        zapatillasLS.forEach(function(zapatillaLS){
            if(zapatillaLS.stockId === infoZapatilla.stockId){
                tallaLS = zapatillaLS.stockId;
            }
            
        });
        if (tallaLS === infoZapatilla.stockId) {
            Swal.fire({
                icon: 'info',
                title: 'Oops...',
                text: 'El producto ya fue agregado al carrito',
                timer: 1500,
                showConfirmButton: false
            })
        }else{
            Swal.fire({
                icon: 'success',
                text: 'Zapatilla agregada correctamente al carrito',
                timer: 2500,
                showConfirmButton: false
              })
              this.insertarCarrito(infoZapatilla);
        }

    }

    insertarCarrito(zapatilla){
        const row = document.createElement('tr');

        row.innerHTML = `
            <td>
                <img src="${zapatilla.foto}" width=100>
            </td>
            <td>${zapatilla.modelo}</td>

            <td>${zapatilla.precio}</td>
            <td>
                <a href="#" class="borrar-producto material-icons-outlined" data-id="${zapatilla.id}">
                highlight_off
                </a>
            </td>
            `;
        listaProductos.appendChild(row);
        this.guardarProductoLocalStorage(zapatilla);
    }
    eliminarProducto(e){
        let producto, productoID;
        if(e.target.classList.contains('borrar-producto')){
            e.target.parentElement.parentElement.remove();
            producto = e.target.parentElement.parentElement;
            productoID = producto.querySelector('a').getAttribute('data-id');
        }
        this.eliminarProductoLocalStorage(productoID);
        this.calcularTotal();
    }
    vaciarCarrito(e){
        while(listaProductos.firstChild){
            listaProductos.removeChild(listaProductos.firstChild);
        }
        this.vaciarLocalStorage();
        return false;
    }
    guardarProductoLocalStorage(zapatilla){
        let zapatillas;
        zapatillas = this.obtenerProductosLocalStorage();
        zapatillas.push(zapatilla);
        localStorage.setItem('zapatillas', JSON.stringify(zapatillas));
    }

    obtenerProductosLocalStorage(){
        let zapatillaLS;

        if(localStorage.getItem('zapatillas') === null){
            zapatillaLS = [];
        }
        else{
            zapatillaLS = JSON.parse(localStorage.getItem('zapatillas'));
        }

        return zapatillaLS;
    }
    

    eliminarProductoLocalStorage(productoID){
        let zapatillasLS;
        zapatillasLS = this.obtenerProductosLocalStorage();
        zapatillasLS.forEach(function(zapatillaLS, index){

            if(zapatillaLS.id === productoID){
                zapatillaLS.cantidad = 0;
                zapatillasLS.splice(index,1);
            }

        });

        localStorage.setItem('zapatillas', JSON.stringify(zapatillasLS));
    }

    leerLocalStorage(){
        let zapatillasLS;
        zapatillasLS = this.obtenerProductosLocalStorage();
        zapatillasLS.forEach(function(zapatilla){
            const row = document.createElement('tr');

            row.innerHTML = `
                <td>
                    <img src="${zapatilla.foto}" width=100>
                </td>
                <td>${zapatilla.modelo}</td>
                <td>${zapatilla.precio}</td>
                <td>
                    <a href="#" class="borrar-producto material-icons-outlined" data-id="${zapatilla.id}">
                    highlight_off
                    </a>
                </td>
                `;
            listaProductos.appendChild(row);
        });
        
    }

    leerLocalStorageCompra(){
        let zapatillasLS;
        zapatillasLS = this.obtenerProductosLocalStorage();
        zapatillasLS.forEach(function(zapatilla){
            const row = document.createElement('tr');

            row.innerHTML = `
                <td>
                    <img src="${zapatilla.foto}" width=100>
                </td>
                <td>${zapatilla.modelo}</td>
                <td>${zapatilla.talla}</td>
                <td>$ ${zapatilla.precio}</td>
                <td>
                    <input type="number" id="cantidad" class="form-control cantidad" min="1"  value=${zapatilla.cantidad}>
                </td>
                <td id="subtotales">$ ${zapatilla.precio * zapatilla.cantidad}</td>
                <td>
                    <a href="eliminarCarrito/${zapatilla.id}"  class=" borrar-producto material-icons-outlined" data-id="${zapatilla.id}">
                    highlight_off
                    </a>
                </td>
                <input type="hidden" name="zapatilla" value=${zapatilla.id},${zapatilla.talla},${zapatilla.cantidad},${zapatilla.precio * zapatilla.cantidad} multiple>
                `;
            listaCompra.appendChild(row);
        });
        
    }

    vaciarLocalStorage(){
        localStorage.clear();
    }

    procesarPedido(e){
        e.preventDefault();
        location.href = "/carrito";
    }

    calcularTotal(){
        let zapatillasLS;
        let total=0, subtotal=0;
        zapatillasLS = this.obtenerProductosLocalStorage();
        for (let i =0; i < zapatillasLS.length; i++) {
            let element = Number(zapatillasLS[i].precio * zapatillasLS[i].cantidad);
            total = total + element;
        }
        subtotal = total;

        document.getElementById('total-mostrar').value = '$' + subtotal;

        document.getElementById('total').value = subtotal;
    }
    

    obtenerEvento(e) {
        e.preventDefault();
        let id, cantidad, zapatilla, zapatillasLS;
        if (e.target.classList.contains('cantidad')) {
            zapatilla = e.target.parentElement.parentElement;
            id = zapatilla.querySelector('a').getAttribute('data-id');
            cantidad = zapatilla.querySelector('input').value;

            let actualizarMontos = document.querySelectorAll('#subtotales');
            zapatillasLS = this.obtenerProductosLocalStorage();

            zapatillasLS.forEach(function (zapatillaLS, index) {

                if (zapatillaLS.id === id) {
                    zapatillaLS.cantidad = cantidad;        
                    actualizarMontos[index].innerHTML = Number(cantidad * zapatillasLS[index].precio);
                    window.location.reload();
                }    
            });
            localStorage.setItem('zapatillas', JSON.stringify(zapatillasLS));
            
        }
        else {
            console.log("click afuera");
        }
    }



}