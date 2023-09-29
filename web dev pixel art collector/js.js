// getting color_selector and get the color stored in it
const color_selector = document.getElementById("color_selector");

let color_selected = "#0000ff";
color_selector.addEventListener("input", function(){
    color_selected = color_selector.value;
    console.log(color_selected);
});

function make_eraser() {
    color_selected = "#FFFFFF";
};

// creating canvas stuff for drawing 
const user_canvas = document.getElementById("user_canvas");
let ctx = user_canvas.getContext('2d');
const pixel_size = 20;

let drawing = false;
user_canvas.addEventListener("mousedown", (e) => {
    drawing = true;
    draw(e);
});

user_canvas.addEventListener("mousemove", (e) => {
    if (!drawing) return;
    draw(e);
});

user_canvas.addEventListener("mouseup", (e) => {
    drawing = false;
});

user_canvas.addEventListener("mouseout", () => {
    if (drawing) drawing = false;
});

function draw(e) {
    const canvas_rect = user_canvas.getBoundingClientRect();
    let x = Math.floor((e.clientX - canvas_rect.left) / pixel_size);
    let y = Math.floor((e.clientY - canvas_rect.top) / pixel_size);
    ctx.fillStyle = color_selected;
    ctx.fillRect(x * pixel_size, y * pixel_size, pixel_size, pixel_size);
};

// creating resizeable canvas
function change_canvas_size(){
    let canvas_width = Math.floor(parseInt(document.getElementById("canvas_width_adjust").value)) * pixel_size; 
    let canvas_height = Math.floor(parseInt(document.getElementById("canvas_height_adjust").value)) * pixel_size;
    let user_screen_width = window.innerWidth;
    let user_screen_height = window.innerHeight;
    // making sure the user has actually put in a usable value within the inputs prior to adjusting canvas size
    if (!isNaN(canvas_height) && !isNaN(canvas_width) && canvas_height > 0 && canvas_width > 0 && canvas_width <= user_screen_width && canvas_height <= user_screen_height){
        user_canvas.width = canvas_width;
        user_canvas.height = canvas_height;
        ctx.clearRect(0, 0, user_canvas.clientWidth, user_canvas.clientHeight);
    } else {
        alert("The size you inputed is in incorrect format or you tried to make it too big! Please try again.");
    };
};

// creating downloadable image from canvas
function download() {
    const dataURL = user_canvas.toDataURL();

    const downloadLink = document.createElement('a');
    downloadLink.href = dataURL;
    downloadLink.download = "user_canvas.png";
    downloadLink.target = "_blank";
    downloadLink.click();
};

function unmute_and_hide_youtube_player() {
    let iframe = document.getElementById("youtube_player");
    let iframeRect = iframe.getBoundingClientRect();

    // iframe.style.display = "none";
};