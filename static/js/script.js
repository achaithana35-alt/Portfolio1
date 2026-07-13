```javascript
/*==================================================
            TYPING ANIMATION
==================================================*/

document.addEventListener("DOMContentLoaded", function(){

    const typingElement = document.getElementById("typing");

    if(typingElement){

        new Typed("#typing", {

            strings:[
                "Python Developer",
                "Java Developer",
                "Machine Learning Enthusiast",
                "Full Stack Developer"
            ],

            typeSpeed:80,

            backSpeed:40,

            backDelay:1500,

            loop:true

        });

    }

});


/*==================================================
            NAVBAR SCROLL EFFECT
==================================================*/

window.addEventListener("scroll",function(){

    const navbar=document.querySelector(".custom-navbar");


    if(window.scrollY > 50){

        navbar.style.background =
        "rgba(9,3,17,.9)";

        navbar.style.boxShadow =
        "0 10px 30px rgba(0,0,0,.4)";

    }

    else{

        navbar.style.background =
        "rgba(9,3,17,.45)";

        navbar.style.boxShadow =
        "none";

    }

});



/*==================================================
            ACTIVE NAV LINK
==================================================*/

const sections=document.querySelectorAll("section");

const navLinks=document.querySelectorAll(".nav-link");


window.addEventListener("scroll",()=>{


    let current="";


    sections.forEach(section=>{


        const sectionTop =
        section.offsetTop - 100;


        const sectionHeight =
        section.clientHeight;


        if(
            window.scrollY >= sectionTop &&
            window.scrollY < sectionTop + sectionHeight
        ){

            current=section.getAttribute("id");

        }


    });



    navLinks.forEach(link=>{


        link.classList.remove("active");


        if(
            link.getAttribute("href")
            ==
            "#"+current
        ){

            link.classList.add("active");

        }


    });


});



/*==================================================
            SMOOTH SCROLL
==================================================*/


document.querySelectorAll(
    'a[href^="#"]'
)
.forEach(anchor=>{


    anchor.addEventListener(
        "click",
        function(e){


            e.preventDefault();


            const target=
            document.querySelector(
                this.getAttribute("href")
            );


            if(target){

                target.scrollIntoView({

                    behavior:"smooth"

                });

            }


        }
    );


});



/*==================================================
            SCROLL REVEAL ANIMATION
==================================================*/


const observer =
new IntersectionObserver(
(entries)=>{


entries.forEach(entry=>{


    if(entry.isIntersecting){


        entry.target.classList.add("show");


    }


});


},
{
    threshold:.2
});



document.querySelectorAll(
".fade-up"
)
.forEach(element=>{


    observer.observe(element);


});



/*==================================================
            SKILL BAR ANIMATION
==================================================*/


const skillSection =
document.querySelector("#skills");


let animated=false;


window.addEventListener(
"scroll",
()=>{


if(skillSection){


const position =
skillSection.getBoundingClientRect().top;


const screen =
window.innerHeight;



if(position < screen && !animated){


    const bars =
    document.querySelectorAll(
    ".progress-bar"
    );


    bars.forEach(bar=>{


        let width =
        bar.style.width;


        bar.style.width="0";


        setTimeout(()=>{

            bar.style.width=width;

        },200);


    });



    animated=true;


}



}


});



/*==================================================
            CONTACT FORM VALIDATION
==================================================*/


const contactForm =
document.querySelector(
"#contact form"
);


if(contactForm){


contactForm.addEventListener(
"submit",
function(e){


const name =
document.querySelector(
"input[name='name']"
).value.trim();



const email =
document.querySelector(
"input[name='email']"
).value.trim();



const message =
document.querySelector(
"textarea[name='message']"
).value.trim();



if(
name==="" ||
email==="" ||
message===""
){


alert(
"Please fill all required fields"
);


e.preventDefault();


}



});


}



/*==================================================
            BACK TO TOP BUTTON
==================================================*/


const topButton =
document.createElement(
"button"
);


topButton.innerHTML =
'<i class="fas fa-arrow-up"></i>';


topButton.className =
"back-to-top";


document.body.appendChild(
topButton
);



window.addEventListener(
"scroll",
()=>{


if(window.scrollY > 400){

topButton.style.display="flex";

}

else{

topButton.style.display="none";

}


});



topButton.addEventListener(
"click",
()=>{


window.scrollTo({

top:0,

behavior:"smooth"

});


});



/*==================================================
            PAGE LOAD EFFECT
==================================================*/


window.addEventListener(
"load",
()=>{


document.body.classList.add(
"loaded"
);


});
```
