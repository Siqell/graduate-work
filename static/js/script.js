// ----------Анимации при скролле----------

const animEl_s = document.querySelectorAll('.animScroll');
if(animEl_s.length > 0){
	window.addEventListener('scroll', animOnScroll);
	function animOnScroll(argument) {
		for (let i = 0; i < animEl_s.length; i++) {
			const animScroll = animEl_s[i];
			const animElHeight = animScroll.offsetHeight;
			const animElOffset = offset(animScroll).top;
			const animStart = 4;

			let animElPoint = window.innerHeight - animElHeight / animStart;
			if (animElHeight > window.innerHeight){
				animElPoint = window.innerHeight - window.innerHeight / animStart;
			}

			if (pageYOffset > (animElOffset - animElPoint) && pageXOffset < (animElOffset + animElPoint)){
				animScroll.classList.add('anim_scroll');
			}else{
				if(!animScroll.classList.contains('no-anim-after')){
					animScroll.classList.remove('anim_scroll');
				}
				
			}
		}
	}
	function offset(el){
		const rect = el.getBoundingClientRect(),
			scrollLeft = window.pageXOffset || document.documentElement.scrollLeft,
			scrollTop = window.pageYOffset || document.documentElement.scrollTop;
		return {top: rect.top + scrollTop, left: rect.left + scrollLeft}
	}


	setTimeout(() => {
		animOnScroll()
	}, 300);

}




// ----------Переключение слайдов в слайдере по кнопкам----------

const img = document.querySelector('.imgBox');
if (img){
	
	const slides = img.getElementsByTagName('img');
	var i = 0;

	function nextSlide(){
	    slides[i].classList.remove('active');
	    i = (i + 1) % slides.length;
	    slides[i].classList.add('active');
	    makeTimer();
	}
	function PrevSlide(){
	    slides[i].classList.remove('active');
	    i = (i - 1 + slides.length) % slides.length;
	    slides[i].classList.add('active');
		makeTimer();
	}
}


// ----------Авто смена слайдов-----------
var timer = 0;
makeTimer();
function makeTimer(){
    clearInterval(timer)
    timer = setInterval(function(){
        nextSlide();
    },5000);
}





// ----------выбор файла(текст на кнопке)----------


		

let inputs = document.querySelectorAll('.input__file');
delete inputs[0];
delete inputs[2];
Array.prototype.forEach.call(inputs, function (input) {
	let label = input.nextElementSibling,
		labelVal = label.innerText;
	input.addEventListener('change', function (e) {
		let countFiles = '';
		if (this.files && this.files.length >= 1)
			countFiles = this.files.length;

		if (countFiles)
			label.querySelector('.input__file-text').innerText = 'Готово!';
		else
			label.querySelector('.input__file-text').innerText = labelVal;
	});
});

