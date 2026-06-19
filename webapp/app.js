const products = [
// Бургерҳо
{
name:"Chicken Burger",
price:22,
category:"🍔 Бургерҳо",
photo:"images/burgers/chicken_burger.jpg",
Description: "Куриная  котлета, айсберг, помидор, маринованные огурцы, фирменный соус"
},

{
name:"Baraka Chicken",
price:28,
category:"🍔 Бургерҳо",
photo:"images/burgers/baraka_chicken.jpg",
Description: "Стрипсы, айсберг, помидор, маринованные огурцы, фирменный соус"
},

{
name:"Chicken Cheese",
price:24,
category:"🍔 Бургерҳо",
photo:"images/burgers/chicken_cheese.jpg",
Description: "Куриная  котлета, айсберг, помидор, маринованные огурцы, сыр, фирменный соус"
},

{
name:"Cheese Burger",
price:34,
category:"🍔 Бургерҳо",
photo:"images/burgers/cheese_burger.jpg",
Description: "Говяжье  котлета, айсберг, помидор, маринованные огурцы,красный лук, сыр, фирменный соус"
},

{
name:"Super Burger",
price:39,
category:"🍔 Бургерҳо",
photo:"images/burgers/super_burger.jpg",
Description: "Говяжье  котлета, айсберг, помидор, маринованные огурцы, сыр, фирменный соус"
},

{
name:"StarFood Burger",
price:42,
category:"🍔 Бургерҳо",
photo:"images/burgers/starfood_burger.jpg",
Description: "Говяжье  котлета, айсберг, помидор, маринованные огурцы, жареный халапеньо, Фирменный соус"
},
{
name:"Mushroom Burger",
price:42,
category:"🍔 Бургерҳо",
photo:"images/burgers/mushroom_burger.jpg",
Description: "Говяжье  котлета, айсберг, помидор, маринованные огурцы, жареный грибы, фирменный соус"
},

{
name:"Kids Burger",
price:15,
category:"🍔 Бургерҳо",
photo:"images/burgers/kids_burger.jpg",
Description: "Куриная  Котлета в панировке, свежий огурец, помидор, мягкая булочка с кунжутом"
},
// Твистерҳо
{
name:"Твистер Ролл",
price:35,
category:"🌯 Твистерҳо",
photo:"images/twisters/twister_roll.jpg"
},
{
name:"Твистер",
price:23,
category:"🌯 Твистерҳо",
photo:"images/twisters/twister.jpg"
},

{
name:"Твистер Чиз",
price:25,
category:"🌯 Твистерҳо",
photo:"images/twisters/twister_cheese.jpg"
},
{
name:"Твистер Цезарь",
price:25,
category:"🌯 Твистерҳо",
photo:"images/twisters/twister_caesar.jpg"
},
// Хот-Догҳо
{
name:"Хот-Дог",
price:16,
category:"🌭 Хот-Догҳо",
photo:"images/hotdogs/hotdog.jpg"
},

{
name:"StarFood Хот-Дог",
price:23,
category:"🌭 Хот-Догҳо",
photo:"images/hotdogs/starfood_hotdog.jpg"
},
// Крылышкаҳо
{
name:"Крылышки 3шт",
price:18,
category:"🍗 Крилышкаҳо",
photo:"images/wings/wings_3.jpg"
},

{
name:"Крылышки 5шт",
price:27,
category:"🍗 Крилышкаҳо",
photo:"images/wings/wings_5.jpg"
},

{
name:"Крылышки 7шт",
price:35,
category:"🍗 Крилышкаҳо",
photo:"images/wings/wings_7.jpg"
},
{
name:"Крылышки 1кг",
price:95,
category:"🍗 Крилышкаҳо",
photo:"images/wings/wings_1kg.jpg"
},
// Стрипсы
{
name:"Стрипсы 3шт",
price:18,
category:"🍗 Крилышкаҳо",
photo:"images/wings/strips_3.jpg"
},

{
name:"Стрипсы 5шт",
price:27,
category:"🍗 Крилышкаҳо",
photo:"images/wings/strips_5.jpg"
},
 {
name:"Стрипсы 7шт",
price:35,
category:"🍗 Крилышкаҳо",
photo:"images/wings/strips_7.jpg"
},
{
name:"Стрипсы 1кг",
price:95,
category:"🍗 Крилышкаҳо",
photo:"images/wings/strips_1kg.jpg"
},
// Пицца
{
name:"Маргарита 35см",
price:65,
category:"🍕 Пицца",
photo:"images/pizza/margarita_35.jpg"
},

{
name:"Пепперони 35см",
price:61,
category:"🍕 Пицца",
photo:"images/pizza/pepperoni_35.jpg"
},

{
name:"Мясная 30см",
price:69,
category:"🍕 Пицца",
photo:"images/pizza/meat_30.jpg"
},

{
name:"Мясная 35см",
price:79,
category:"🍕 Пицца",
photo:"images/pizza/meat_35.jpg"
},

{
name:"Куриное с грибами 30см",
price:65,
category:"🍕 Пицца",
photo:"images/pizza/kurenie_30.jpg"
},
{
name:"Куриное с грибами 35см",
price:75,
category:"🍕 Пицца",
photo:"images/pizza/kurenie_35.jpg"
},
{
name:" 4 сыра 30см",
price:59,
category:"🍕 Пицца",
photo:"images/pizza/4cheese_30.jpg"
},
{
name:" 4 сыра 35см",
price:69,
category:"🍕 Пицца",
photo:"images/pizza/4cheese_35.jpg"
},
{
name:"StarFood 30см",
price:75,
category:"🍕 Пицца",
photo:"images/pizza/starfood_30.jpg"
},
{
name:"StarFood 35см",
price:90,
category:"🍕 Пицца",
photo:"images/pizza/starfood_35.jpg"
},
{
name:"Маргарита 30см",
price:53,
category:"🍕 Пицца",
photo:"images/pizza/margarita_30.jpg"
},

{
name:"Пепперони 30см",
price:59,
category:"🍕 Пицца",
photo:"images/pizza/pepperoni_30.jpg"
},
// Гарнирҳо
{
name:"Картофель фри",
price:12,
category:"🍟 Гарнирҳо",
photo:"images/garnish/fries.jpg"
},
{
name:"По деревенски",
price:14,
category:"🍟 Гарнирҳо",
photo:"images/garnish/village_fries.jpg"
},

{
name:"куреиный наггетсы",
price:18,
category:"🍟 Гарнирҳо",
photo:"images/garnish/chicken_nuggets.jpg"
},
{
name:"сырный картофель фри",
price:22,
category:"🍟 Гарнирҳо",
photo:"images/garnish/cheese_fries.jpg"
},
{
name:"куреиный шарики с сыром",
price:18,
category:"🍟 Гарнирҳо",
photo:"images/garnish/chicken_strips.jpg"
},
{
name:"мексиканский крылышки 240г",
price:30,
category:"🍟 Гарнирҳо",
photo:"images/garnish/mexican_wings.jpg"
},
{
name:"мексиканский крылышки 1кг",
price:120,
category:"🍟 Гарнирҳо",
photo:"images/garnish/mexican_wings_1kg.jpg"
},
{
name:"салат кол слоу",
price:4,
category:"🍟 Гарнирҳо",
photo:"images/garnish/salad_coleslaw.jpg"
},

// Қаҳва
{
name:"Latte",
price:15,
category:"☕ Қаҳва",
photo:"images/coffee/latte.jpg"
},
{
name:"Americano",
price:10,
category:"☕ Қаҳва",
photo:"images/coffee/americano.jpg"
},

{
name:"Espresso",
price:10,
category:"☕ Қаҳва",
photo:"images/coffee/espresso.jpg"
},
{
name:"Cappuccino",
price:15,
category:"☕ Қаҳва",
photo:"images/coffee/cappuccino.jpg"
},
{
name:"flat white",
price:15,
category:"☕ Қаҳва",
photo:"images/coffee/flat_white.jpg"
},

{
name:"Espresso",
price:10,
category:"☕ Қаҳва",
photo:"images/coffee/espresso.jpg"
},
{
name:"зелёный чай",
price:4,
category:"☕ Қаҳва",
photo:"images/coffee/green_tea.jpg"
},
// Нӯшокиҳо
{
name:"Fuse Tea",
price:7,
category:"🥤 Нӯшокиҳо",
photo:"images/drinks/fuse_tea.jpg"
},
{
name:"Coca Cola",
price:6,
category:"🥤 Нӯшокиҳо",
photo:"images/drinks/cola.jpg"
},
{
name:"Coca Cola ж/б",
price:8,
category:"🥤 Нӯшокиҳо",
photo:"images/drinks/cola_dark.jpg"
},

{
name:"Fanta",
price:6,
category:"🥤 Нӯшокиҳо",
photo:"images/drinks/fanta.jpg"
},
{
name:"Bonaqua",
price:4,
category:"🥤 Нӯшокиҳо",
photo:"images/drinks/bonaqua.jpg"
},
{
name:"лимонад лесные ягоды",
price:15,
category:"🥤 Нӯшокиҳо",
photo:"images/drinks/lemonade.jpg"
},
{
name:"лимонад манго маракуйя",
price:15,
category:"🥤 Нӯшокиҳо",
photo:"images/drinks/mango_maracuja.jpg"
},
{
name:"лимонад клубника",
price:15,
category:"🥤 Нӯшокиҳо",
photo:"images/drinks/strawberry_lemonade.jpg"
},
{
name:"лимонад мохито",
price:15,
category:"🥤 Нӯшокиҳо",
photo:"images/drinks/mojito_lemonade.jpg"
},
// Соусҳо
{
name:"Чесночный соус",
price:3,
category:"🧂 Соусҳо",
photo:"images/sauces/garlic_sauce.jpg"
},
{
name:"Кетчуп",
price:3,
category:"🧂 Соусҳо",
photo:"images/sauces/ketchup.jpg"
},

{
name:"Сырный соус",
price:3,
category:"🧂 Соусҳо",
photo:"images/sauces/cheese_sauce.jpg"
},
{
name:"Барбекю соус",
price:3,
category:"🧂 Соусҳо",
photo:"images/sauces/barbecue_sauce.jpg"
},
{
name:"халапеньо соус",
price:3,
category:"🧂 Соусҳо",
photo:"images/sauces/halapeno_sauce.jpg"
},
// Комбо
{
name:"Комбо Твистер",
price:78,
category:"🎁 Комбо",
photo:"images/combo/combo_twister.jpg"
},

{
name:"Студент Сет",
price:38,
category:"🎁 Комбо",
photo:"images/combo/student_set.jpg"
},

{
name:"Комбо Бургер",
price:76,
category:"🎁 Комбо",
photo:"images/combo/combo_burger.jpg"
},
{
name:"мини кидс комбо",
price:40,
category:"🎁 Комбо",
photo:"images/combo/combo_kids.jpg"
},
{
name:"сеть дустлар комбо",
price:258,
category:"🎁 Комбо",
photo:"images/combo/combo_adults.jpg"
},


];

const categories = [
"🍔 Бургерҳо",
"🌯 Твистерҳо",
"🌭 Хот-Догҳо",
"🍗 Крилышкаҳо",
"🍕 Пицца",
"🍟 Гарнирҳо",
"☕ Қаҳва",
"🥤 Нӯшокиҳо",
"🧂 Соусҳо",
"🎁 Комбо",
];

const productsDiv = document.getElementById("products");
const categoriesDiv = document.getElementById("categories");

let cart = {};

function renderCategories(){

categoriesDiv.innerHTML="";

categories.forEach(category=>{

const btn=document.createElement("button");

btn.className="category-btn";

btn.innerText=category;

btn.onclick=()=>renderProducts(category);

categoriesDiv.appendChild(btn);

});

}

function renderProducts(category){

productsDiv.innerHTML="";

const filtered=products.filter(
p=>p.category===category
);

filtered.forEach(product=>{

const qty=cart[product.name] || 0;

productsDiv.innerHTML += `
<div class="card">

<img src="${product.photo}">

<h3>${product.name}</h3>
${product.Description ? `
    <p class="descr">
 ${product.Description}
</p>
` : ""}
<div class="price">
${product.price} смн
</div>

<div class="controls">

<button onclick="minus('${product.name}')">
-
</button>

<span id="qty-${product.name}">
${qty}
</span>

<button onclick="plus('${product.name}')">
+
</button>

</div>

</div>
`;

});

}

function plus(name){

cart[name]=(cart[name]||0)+1;

update();
}

function minus(name){

if(cart[name]){

cart[name]--;

if(cart[name]<=0){

delete cart[name];

}

}

update();
}

function update(){

document.querySelectorAll("[id^='qty-']").forEach(el=>{

const name = el.id.replace("qty-","");

el.innerText = cart[name] || 0;

});

let total = 0;
let count = 0;

products.forEach(product=>{

if(cart[product.name]){

total += cart[product.name] * product.price;

count += cart[product.name];

}

});

document.getElementById("cart-total").innerHTML =
`🛒 ${count} дона | ${total} смн`;

}

renderCategories();

renderProducts("🍔 Бургерҳо");
update();
const cartBar = document.getElementById("cart-total");

cartBar.onclick = function(){

let html = "";
let total = 0;

for(let name in cart){

const qty = cart[name];

const product = products.find(
p => p.name === name
);

const sum = qty * product.price;

total += sum;

html += `
<p>
<b>${product.name}</b>
<br>
${qty} x ${product.price} = ${sum} смн
</p>
<hr>
`;

}

if(html === ""){
html = "Сабад холӣ аст";
}

document.getElementById(
"cartItems"
).innerHTML = html;

document.getElementById("cartPrice").innerHTML =
`💰 Ҳамагӣ: ${total} смн`;

document.getElementById(
"cartModal"
).style.display = "block";

};

document.getElementById(
"closeCart"
).onclick = function(){

document.getElementById(
"cartModal"
).style.display = "none";

};

document.getElementById("orderBtn").onclick = function () {

    let items = [];
    let total = 0;

    for(let name in cart){

        const product = products.find(
            p => p.name === name
        );

        if(!product) continue;

        const qty = cart[name];

        const sum = qty * product.price;

        total += sum;

        items.push({

            name: product.name,

            qty: qty,

            sum: sum

        });

    }

    if(items.length === 0){

        alert("Сабад холӣ аст");

        return;
    }

    Telegram.WebApp.sendData(

        JSON.stringify({

            items: items,

            total: total

        })

    );

    Telegram.WebApp.close();

};