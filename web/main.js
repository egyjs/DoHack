function init(){
  console.log(banner());
  $('#banner').css(this.scrollHeight);
}

function banner() {
  var bannerS	= (function(){ /*
      ===================================================================

         ╔═╗   ╔═╗┬    ──┐ ┌─┐┬ ┬┌─┐┌┐ ┬ ┬
         ╠═╣   ║╣ │ ───┌─┘ ├─┤├─┤├─┤├┴┐└┬┘  @  DoHack
         ╩ ╩ o ╚═╝┴─┘  └── ┴ ┴┴ ┴┴ ┴└─┘ ┴

         follow me in my instagram : •´¯`•.   🎀  [𝑒𝑔𝓎.𝒿𝓈]  🎀   .•`¯´•

         Build By A.ELZAHABY github.com/el3zahaby

      ===================================================================
  */}).toString().split('\n').slice(1, -1).join('\n');

  return bannerS
}
