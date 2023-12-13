function sendMail(contactForm) {
    emailjs.send("service_58f9ji3", "rubysbooks", {
            "from_name": contactForm.fullname.value,
            "from_email": contactForm.emailaddress.value,
            "message": contactForm.message.value
        })
        .then(function (response) {
            console.log('SUCCESS!', response.status, response.text);
            window.location.reload();
        }, function (error) {
            console.log('FAILED...', error);
        });
    return false; // To block from loading a new page
}