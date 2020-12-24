
var updateBtns = document.getElementsByClassName('update-cart')
for(var i=0;i<updateBtns.length;i++ )
{
    updateBtns[i].addEventListener("click",function(){
        var productid=this.dataset.product
        var action=this.dataset.action
        console.log('productid:', productid,'action:',action)
        console.log('USER:' , user)
        if(user=='AnonymousUser'){addcookieitem(productid,action)}
        else{updateUserOrder(productid,action)}

        
    })
}
function addcookieitem(productid,action)
{
    console.log('not logged in..')
    
    if(action=='add_cart')
    { 
        if(cart[productid] == undefined)
        {
            cart[productid]={'quantity':1}
        }
    }
    if(action=='add'){
        
            cart[productid]['quantity']+=1
        }
    
    if (action == 'remove'){
		cart[productid]['quantity'] -= 1

		if (cart[productid]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productid];
		}
    }
    console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	location.reload()
    
}
function updateUserOrder(productid,action)
{
    var url='/updateitem/'
    console.log('user is logged in')
    fetch(url,{
        method:'POST',
    headers:{
        'Content-Type':'application/json',
        'X-CSRFToken': csrftoken,
    },
    body:JSON.stringify({'productid': productid , 'action': action})
    })

    .then((Response) => {
        return Response.json()})

    .then((data) => {
        console.log('data:',data)
        //location.reload()
    })
}