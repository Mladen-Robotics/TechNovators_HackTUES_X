let active_theme = document.querySelector("#active_theme");
let theme = document.querySelector("#theme");
let white_theme = document.querySelector("#white_theme");
let black_theme = document.querySelector("#black_theme");
let pink_theme = document.querySelector("#pink_theme");
let root = document.querySelector(":root");

let active_font = document.querySelector("#active_font");
let fonts = document.querySelector("#fonts");
let ibm_font = document.querySelector("#ibm_font");
let inconsolata_font = document.querySelector("#inconsolata_font");
let irish_font = document.querySelector("#irish_font");

let title = document.querySelector("#title");
let theme_open = false;
let font_open = false;

let chat_area = document.querySelector("#chat_area");
let user_input = document.querySelector("#input_field input");
let send_btn = document.querySelector("#send_icon");

let content = document.querySelector("#content");
// let user_prompt_placeholder = document.querySelector("#input_field input::placeholder");


let root_style = getComputedStyle(root);


function create_user_message(user_input_data) {
    let user_msg_html_content = `<div class="user_message_wrapper">
    <div class="user_message">
        <p>${user_input_data}</p>
    </div>
    <div class="user_message_pic">
        <img src="images/ai_student.jpg" alt="">
    </div>
</div>`
    chat_area.innerHTML += user_msg_html_content;
    content.scrollTo(0, document.body.scrollHeight);
}

function send_message() {
    let user_input_data = user_input.value;
    create_user_message(user_input_data);
    user_input.value = "";
}

send_btn.addEventListener("click", (e) => {
    send_message();
})

user_input.addEventListener("focus", () => {
    user_input.addEventListener("keydown", (key) => {
        if (key.code == "Enter") {
            key.stopPropagation();
            key.stopImmediatePropagation();
            user_input.blur();
            send_message();
        }
    })

})

active_theme.addEventListener("click", (e) => {
    theme_open = !theme_open;
    console.log("theme " + theme_open);
    fonts.classList.remove("font_open");
    theme.classList.toggle("theme_open");
    white_theme.addEventListener("click", () => {
        theme.classList.remove("theme_open");
        active_theme.style.backgroundImage = "linear-gradient(to right, #53DF3C 50%, #fff 50%, #fff)";
        active_theme.style.borderColor = "#FFA800";
        root.style.setProperty("--bg-color", "#fff");
        root.style.setProperty("--nav-color", "#FFC555");
        root.style.setProperty("--nav-second-color", "#53DF3C");
        root.style.setProperty("--nav-third-color", "#D9D9D9");
        root.style.setProperty("--text-color", "black");
        user_prompt_placeholder.style.color = "";
        root.style.setProperty("--user-prompt-placeholder", "#757575");
    })
    black_theme.addEventListener("click", () => {
        theme.classList.remove("theme_open");
        active_theme.style.backgroundImage = "linear-gradient(to right, #1B1B1B 50%, #005703 50%, #005703)";
        active_theme.style.borderColor = "#FFA800";
        root.style.setProperty("--bg-color", "#1B1B1B");
        root.style.setProperty("--nav-color", "#006704");
        root.style.setProperty("--nav-second-color", "#53DF3C");
        title.setAttribute("src", "images/title_wave_white.svg");
        root.style.setProperty("--nav-third-color", "black");
        root.style.setProperty("--user-prompt-placeholder", "#fff");
        root.style.setProperty("--text-color", "#fff");
    })
    pink_theme.addEventListener("click", () => {
        theme.classList.remove("theme_open");
        active_theme.style.backgroundImage = "linear-gradient(to right, #ED0072 50%, #FA8C7F 50%, #FA8C7F)";
        active_theme.style.borderColor = "#6C0092";
        root.style.setProperty("--bg-color", "#fff");
        root.style.setProperty("--nav-color", "#FA5C79");
        root.style.setProperty("--nav-second-color", "#ED0072");
        title.setAttribute("src", "images/title_wave.svg");
        root.style.setProperty("--nav-third-color", "#D9D9D9");
        root.style.setProperty("--user-prompt-placeholder", "#757575");
        root.style.setProperty("--text-color", "black");
    })
})


document.addEventListener("keydown", (key) => {
    if (key.code == "Escape") {
        user_input.blur();
    }
})


active_font.addEventListener("click", () => {
    font_open = !font_open;
    console.log('font')
    fonts.classList.toggle("font_open");
    theme.classList.remove("theme_open");
    ibm_font.addEventListener("click", (e) => {
        e.stopPropagation();
        fonts.classList.remove("font_open");
        active_font.style.fontFamily = "IBM Plex Sans Hebrew";
        active_font.style.fontStyle = "sans-serif";
        root.style.setProperty("--font-family", "IBM Plex Sans Hebrew");
    })
    inconsolata_font.addEventListener("click", (e) => {
        e.stopPropagation();
        fonts.classList.remove("font_open");
        active_font.style.fontFamily = "Inconsolata";
        active_font.style.fontStyle = "monospace";
        root.style.setProperty("--font-family", "Inconsolata");
    })
    irish_font.addEventListener("click", (e) => {
        e.stopPropagation();
        fonts.classList.remove("font_open");
        active_font.style.fontFamily = "Irish Grover";
        active_font.style.fontStyle = "system-ui";
        root.style.setProperty("--font-family", "Irish Grover");
    })
})

window.addEventListener("click", (event) => {
    console.log(event.target.id);
    console.log(event.target);
    if (event.target.id != "active_theme" && event.target.id != "fontAsd") {
        theme.classList.remove("theme_open");
        fonts.classList.remove("font_open");
        theme.style.borderColor = "red";
        console.log("hello");
    }
})
