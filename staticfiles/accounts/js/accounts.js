document.getElementById('login').addEventListener('click', jumpto_login);

document.getElementById('back_btn').addEventListener('click', jumpto_login);


document.getElementById('signup').addEventListener('click', jumpto_signup);

function jumpto_signup() {

    document.getElementById('back_btn').style.display = 'block';
    document.getElementById('back_btn').style.opacity = '0';
    document.getElementById('Path04').style.transform = 'translate(0px,0px)';
    document.getElementById('Path03').style.transform = 'translate(0px,0px)';
    // document.getElementById('login_img').style.transform = 'translate(0px,812px)';
    document.getElementById('2_page').style.transform = 'translateX(-50%)';
    document.getElementById('Path').style.transform = 'translate(0px,135px)';
    document.getElementById('Path01').style.transform = 'scale(1, -1) translate(0px, -270px)';
    setTimeout(function () {
        document.getElementById('back_btn').style.opacity = '1';
    }, 10);

document.getElementById("email_sign").value = document.getElementById("email_log").value;

};

function jumpto_login() {
    setTimeout(function () {
        document.getElementById('back_btn').style.display = 'none';
    }, 600);

    document.getElementById('2_page').style.transform = 'translateX(0%)';
    // document.getElementById('signup_page').style.transform = 'translateX(0%)';
    document.getElementById('back_btn').style.opacity = '0';
    document.getElementById('Path03').style.transform = 'translate(0px,-189px)';
    document.getElementById('Path04').style.transform = 'translate(0px,-189px)';
    document.getElementById('Path').style.transform = 'translate(0px,0px)';
    document.getElementById('Path01').style.transform = 'scale(1, -1) translate(0px, -135px)';
document.getElementById("email_log").value = document.getElementById("email_sign").value;

};
