const contact=document.getElementById('contact-content');
const about=document.getElementById('about-content');
const aboutbtn=document.getElementById('aboutbtn')
const contactbtn=document.getElementById('contactbtn')

aboutbtn.addEventListener('click', ()=>{
    const aboutBox = new WinBox({
        'title':'xterm',
        'mount':about
    })
})

contactbtn.addEventListener('click', ()=>{
    const aboutBox = new WinBox({
        'title':'xterm',
        'mount':contact
    })
})
