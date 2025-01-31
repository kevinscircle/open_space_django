// JavasCriipt
//let owner = document.getElementById("ownerName").val("Kevin");

// jQuery
//let owner2 = $("#ownerName2").val();



function initTypingAnimation(toRotate, period = 500) {
    console.log("initTypingAnimation")
    let loopNum = 0;
    let text = '';
    let isDeleting = false;
    const el = document.querySelector('.wrap');

    function tick() {
        let i = loopNum % toRotate.length;
        let fullText = toRotate[i];
        let updatedText = isDeleting
            ? fullText.substring(0, text.length - 1)
            : fullText.substring(0, text.length + 1);

        text = updatedText;

        el.innerHTML = text;

        let delta = 300 - Math.random() * 100;

        if (isDeleting) {
            delta /= 2;
        }

        if (!isDeleting && updatedText === fullText) {

            delta = period;
            isDeleting = true;
        } else if (isDeleting && updatedText === '') {

            isDeleting = false;
            loopNum++;
            delta = 500;
        }

        setTimeout(tick, delta);
    }

    tick();
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    try {
        //const toRotate = JSON.parse(document.getElementById('toRotate').textContent);
        const toRotate = [
            "Explore",
            "Create",
            "Inspire or get inspired",
        ];
        initTypingAnimation(toRotate);
    } catch (error) {
        console.error('Error initializing typing animation:', error);
    }
});