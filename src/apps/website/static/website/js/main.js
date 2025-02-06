
$(function () {
    /**
     * ===============================================
     *      TABLE OF CONTENT
     * ===============================================
     * # Loader
     * # Real Time
     * # Popup Menu
     * # Gsap Smooth Scroll
     * # Experience Popup
     * # Custom Cursor
     * # Contact Form
     *
     */


    /* ===== Loader ===== */
    $(window).on('load', function () {
        setTimeout(() => {
            $('.preloader-wrap').delay('500').fadeOut(1000);
        }, 200);
        setTimeout(() => {
            // $('.hero-sec .hero-footer-wrap.scroll-from-bottom').addClass('animated');
            scroll_animations();
        }, 800);
    });



    /* ===== Real Time ===== */
    if ($('.realtime').length) {
        startTime();
    }
    
    function startTime() {
        const timeEl = document.querySelectorAll('.realtime');
        var today = new Date();
        var h = today.getHours();
        var m = today.getMinutes();
        var ampm = h >= 12 ? 'PM' : 'AM';
        h = h % 12;
        h = h ? h : 12; // the hour '0' should be '12'
        m = checkTime(m);
        timeEl.forEach(item => {
            item.innerHTML = h + ":" + m + " " + ampm;

        });
        var t = setTimeout(startTime, 500);
    }
    
    function checkTime(i) {
        if (i < 10) {
            i = "0" + i;
        }  // add zero in front of numbers < 10
        return i;
    }


    // Custom Mouse Cursor for Work
    if (document.querySelectorAll('.work-box')) {
        document.querySelectorAll('.work-box').forEach(box => {
            const hoverElement = box.querySelector('.hover_mouse');

            box.addEventListener('mousemove', (event) => {
                const boxRect = box.getBoundingClientRect();
                const mouseX = event.clientX - boxRect.left;
                const mouseY = event.clientY - boxRect.top;

                if (hoverElement) {
                    hoverElement.style.transform = `translate3d(${mouseX - 50}px, ${mouseY - 50}px, 0)`;
                    hoverElement.classList.add('active');
                }
            });

            if (hoverElement) {
                box.addEventListener('mouseleave', () => {
                    // hoverElement.style.transform = `translate3d(0, 0, 0)`;
                    hoverElement.classList.remove('active');
                });
            }

            box.addEventListener('mouseenter', function () {
                // Animate cursorBall on mouseenter
                cursorBall.classList.add('hovered');
                gsap.to(cursorBall, {
                    duration: 0.3,
                    scale: 2, // Increase scale
                    opacity: 0, // Set opacity to 0
                    ease: 0.1
                });
            });
    
            box.addEventListener('mouseleave', function () {
                // Restore cursorBall on mouseleave
                cursorBall.classList.remove('hovered');
                gsap.to(cursorBall, {
                    duration: 0.3,
                    scale: 1, // Restore scale to normal
                    opacity: 1, // Restore opacity
                    ease: 'power2.out'
                });
            });
        });
    }



    /* ===== # Popup Menu ===== */
    if ($('.show-navigation-popover').length) {
        $(document).on('click', '.show-navigation-popover', function (e) {
            e.preventDefault();
            $('.popup-menu-wrap').addClass('active');
            $('body').css({
                overflow: 'hidden'
            })
        });
        $(document).on('click', '.close-navigation-btn', function (e) {
            e.preventDefault();
            $('.popup-menu-wrap').removeClass('active');
            $('body').css({
                overflowX: 'hidden',
                overflowY: 'auto'
            })
        });
    }



    /* ===== # Gsap Smooth Scroll ===== */

    // window.addEventListener('scroll', {
    //     scroll_animations
    // });


    /* ===== # Experience Popup ===== */
    $(document).on('click', '.experience-box .experience-button-box .experience-button', function (e) {
        e.preventDefault();
        $('.experience-popup').addClass('active');
    });
    $(document).on('click', '.experience-popup .experience-popup-content-wrap .close-experience-popup-btn', function () {
        $('.experience-popup').removeClass('active');
    });


    /* ==== # Custom Cursor ===== */
    const cursorBall = document.getElementById('ball');

    document.addEventListener('mousemove', function (e) {
        // Update cursor position and opacity on mousemove
        gsap.to(cursorBall, {
            duration: 0.3,
            x: e.clientX,
            y: e.clientY,
            opacity: 1, // Ensure cursor is visible
            ease: 'power2.out'
        });
    });

    // Hover effect on elements
    const hoverElements = document.querySelectorAll('a');
    hoverElements.forEach(function (element) {
        element.addEventListener('mouseenter', function () {
            // Animate cursorBall on mouseenter
            cursorBall.classList.add('hovered');
            gsap.to(cursorBall, {
                duration: 0.3,
                scale: 2, // Increase scale
                opacity: 0, // Set opacity to 0
                ease: 0.1
            });
        });

        element.addEventListener('mouseleave', function () {
            // Restore cursorBall on mouseleave
            cursorBall.classList.remove('hovered');
            gsap.to(cursorBall, {
                duration: 0.3,
                scale: 1, // Restore scale to normal
                opacity: 1, // Restore opacity
                ease: 'power2.out'
            });
        });
    });

});



function scroll_animations() {
    // var allow_on_mobile = !0;
    // if (typeof config_scroll_animation_on_mobile !== "undefined") allow_on_mobile = config_scroll_animation_on_mobile;
    // if (allow_on_mobile == !1 && is_mobile_device) return;
    var defaults = {
        ease: 4,
        animation: "fade_from_bottom",
        once: !1,
        delay: 0, // Default delay value
    };
    gsap.utils.toArray(".scroll-animation").forEach(function (box) {
        var gsap_obj = {};
        var settings = {
            // ease: box.dataset.animationEase || defaults.ease,
            duration: box.dataset.animationDuration || defaults.duration,
            delay: box.dataset.animationDelay || defaults.delay, // Get the delay from data attribute or use default
        };
        var animations = {
            slide_up: {
                y: -180,
            },
            slide_down: {
                y: 180,
            },
            slide_up2: {
                y: -100,
            },
            slide_down2: {
                y: 100,
            },
            fade_from_bottom: {
                y: 180,
                opacity: 0,
            },
            fade_from_top: {
                y: -180,
                opacity: 0,
            },
            fade_from_bottom2: {
                y: 100,
                opacity: 0,
            },
            fade_from_top2: {
                y: -100,
                opacity: 0,
            },
            fade_from_left: {
                x: -180,
                opacity: 0,
            },
            fade_from_right: {
                x: 180,
                opacity: 0,
            },
            fade_in: {
                opacity: 0,
            },
            rotate_up: {
                y: 180,
                rotation: 10,
                opacity: 0,
            },
            boldz_zoom_out: {
                scale: 2,
            },
            boldz_zoom_in: {
                scale: 0,
                opacity: 1,
            },
            slide_and_scale: {
                // y: 180,
                scale: 1,
                opacity: 1
            },
        };
        var globalWidth = window.innerWidth;
        if (globalWidth > 809) {
            var transWidth = '10%';
        } else {
            var transWidth = '30%';
        }
        var scroll_trigger = {
            scrollTrigger: {
                trigger: box,
                once: defaults.once,
                // start: "top bottom+=20%",
                start: "top bottom+="+transWidth,
                toggleActions: "play none none reverse",
                markers: !1,
                onUpdate: function(self) {
                    // Get the current position of the box relative to the viewport
                    // var bounding = box.getBoundingClientRect();
                    // var offsetTopFromViewport = bounding.top;

                    
                    // if (box.dataset.animation == 'slide_and_scale') {
                    //     console.log("Offset from top:", offsetTopFromViewport);

                    //     // Example: Toggle opacity and scale based on offset
                    //     if (offsetTopFromViewport < 0) {
                    //         const replaceVal = Math.abs(offsetTopFromViewport);
                    //         console.log(replaceVal, 'if');
                    //         // box.style.transform = `translateY(${replaceVal}px)`;
                    //         gsap.to(box, { y: replaceVal, duration: 0.5 });
                    //     } else {
                    //         console.log('else');
                    //         // box.style.transform = `translateY(0px)`;
                    //         gsap.to(box, { y: 0, duration: 0.5 });
                    //     }
                    // }
                }
            },
        };
        if (box.dataset.animation == 'boldz_zoom_out') {
            scroll_trigger = {
                scrollTrigger: {
                    trigger: box,
                    once: defaults.once,
                    // start: "top bottom+=20%",
                    start: "top bottom",
                    toggleActions: "play none none reverse",
                    markers: !1,
                },
            };
        }
        if (box.dataset.animation == 'boldz_zoom_in') {
            scroll_trigger = {
                scrollTrigger: {
                    trigger: box,
                    once: defaults.once,
                    // start: "top bottom+=20%",
                    start: "top bottom",
                    toggleActions: "play none none reverse",
                    markers: !1,
                },
            };
        }
        jQuery.extend(gsap_obj, settings);
        jQuery.extend(gsap_obj, animations[box.dataset.animation || defaults.animation]);
        jQuery.extend(gsap_obj, scroll_trigger);
        gsap.from(box, gsap_obj);
    });
}