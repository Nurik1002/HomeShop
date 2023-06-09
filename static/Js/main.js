document.addEventListener("DOMContentLoaded", function () {

  // menyu Responsive
  var menyu = document.querySelector(".menyu"), 
  menyu__res__bars = document.querySelector(".menyu__res__bars"),
  menyu__modal = document.querySelector(".menyu__modal");
  menyu__res__bars.addEventListener("click", function() {
    menyu.classList.toggle("active__menyuu");
    menyu__modal.classList.toggle("modal__active");
    menyu__res__bars.classList.toggle("active__bars__exit");
  });
  function scrolltime(){
    if(menyu.classList.contains(".active__menyuu")){
        window.removeEventListener("scroll", scrolltime);
    };
  };
  window.addEventListener("scroll", scrolltime);
  menyu__modal.addEventListener("click", function() {
    menyu.classList.toggle("active__menyuu");
    menyu__modal.classList.toggle("modal__active");
    menyu__res__bars.classList.toggle("active__bars__exit");
  });

  // card
  const All__card = document.querySelector(".All__card"),
  Home__card = document.querySelector(".Home__card"),
  Twoo__card = document.querySelector(".Twoo__card"),
  There__catd = document.querySelector(".There__catd"),
  Uy = document.querySelectorAll(".Uy"),
  Bog = document.querySelectorAll(".Bog"),
  Hovli = document.querySelectorAll(".Hovli");
  All__card.addEventListener("click", function() {
      for(let i = 0; i < Uy.length; i++) {
        Uy[i].style.display="flex";
        Bog[i].style.display="flex";
        Hovli[i].style.display="flex";
      }
  });
  Home__card.addEventListener("click", function() {
      for(let l = 0; l < Uy.length; l++) {
        Uy[l].style.display="flex";
        Bog[l].style.display="none";
        Hovli[l].style.display="none";
      }
  });
  Twoo__card.addEventListener("click", function() {
      for(let o = 0; o < Bog.length; o++) {
        Bog[o].style.display="flex";
        Uy[o].style.display="none";
        Hovli[o].style.display="none";
      }
  });
  There__catd.addEventListener("click", function() {
      for(let r = 0; r < Hovli.length; r++) {
        Hovli[r].style.display="flex";
        Uy[r].style.display="none";
        Bog[r].style.display="none";
      }
  });


  // modal
  const modal=document.querySelector(".modal"),
    yopil=document.querySelectorAll(".btn1"),
    fas=document.querySelector(".befor");
    function open() {
        modal.classList.add("show");
        modal.classList.remove("hide");
        document.body.style.overflow="hidden";
        clearTimeout(x);
    }
    function close() {
        modal.classList.remove("show");
        modal.classList.add("hide");
        document.body.style.overflow="";
    }
    yopil.forEach(ochil => {
        ochil.addEventListener("click", open);        
    });
    fas.addEventListener("click", function(){
        close();
    }); 
     const x=setTimeout(open, 3000);
     modal.addEventListener("click", (e)=>{
        if(e.target==modal){
            close();
        }
    });
    function scrolltime(){
        if(window.pageYOffset + document.documentElement.clientHeight >= document.documentElement.scrollHeight){
            open();
            window.removeEventListener("scroll", scrolltime);
        };
    };
    window.addEventListener("scroll", scrolltime);
  










  // country__item 
  var states__group = document.querySelector(".states__group");
  var statesArr = [
    {id: 1, name: "Afghanistan"}, 
    {id: 2, name: "Algeria"}, 
    {id: 3, name: "Andorra"}, 
    {id: 4, name: "Angola"}, 
    {id: 5, name: "Antigua and Barbuda"}, 
    {id: 6, name: "Argentina"}, 
    {id: 7, name: "Armenia"}, 
    {id: 8, name: "Aruba"}, 
    {id: 9, name: "Australia"}, 
    {id: 10, name: "Austria"}, 
    {id: 11, name: "Azerbaijan"}, 
    {id: 12, name: "Albania"}, 
    {id: 13, name: "American Samoa"}, 
    {id: 14, name: "Bahamas, The"}, 
    {id: 15, name: "Bahrain"}, 
    {id: 16, name: "Bangladesh"}, 
    {id: 17, name: "Barbados"}, 
    {id: 18, name: "Belarus"}, 
    {id: 19, name: "Belgium"}, 
    {id: 20, name: "Belize"}, 
    {id: 21, name: "Benin"}, 
    {id: 22, name: "Bermuda"}, 
    {id: 23, name: "Bhutan"}, 
    {id: 24, name: "Bolivia"}, 
    {id: 25, name: "Bosnia and Herzegovina"}, 
    {id: 26, name: "Botswana"}, 
    {id: 27, name: "Brazil"}, 
    {id: 28, name: "British Virgin Islands"}, 
    {id: 29, name: "Brunei Darussalam"}, 
    {id: 30, name: "Bulgaria"}, 
    {id: 31, name: "Burkina Faso"}, 
    {id: 32, name: "Burundi"}, 
    {id: 33, name: "Cabo Verde"}, 
    {id: 34, name: "Cambodia"}, 
    {id: 35, name: "Cameroon"}, 
    {id: 36, name: "Canada"}, 
    {id: 37, name: "Cayman Islands"}, 
    {id: 38, name: "Central African Republic"}, 
    {id: 39, name: "Chad"}, 
    {id: 40, name: "Channel Islands"}, 
    {id: 41, name: "Chile"}, 
    {id: 42, name: "China"}, 
    {id: 43, name: "Colombia"}, 
    {id: 44, name: "Comoros"}, 
    {id: 45, name: "Congo, Dem. Rep."}, 
    {id: 46, name: "Congo, Rep."}, 
    {id: 47, name: "Costa Rica"}, 
    {id: 48, name: "Cote d'Ivoire"}, 
    {id: 49, name: "Croatia"}, 
    {id: 50, name: "Cuba"}, 
    {id: 51, name: "Curacao"}, 
    {id: 52, name: "Cyprus"}, 
    {id: 53, name: "Czechia"}, 
    {id: 54, name: "Denmark"}, 
    {id: 55, name: "Djibouti"}, 
    {id: 56, name: "Dominica"}, 
    {id: 57, name: "Dominican Republic"}, 
    {id: 58, name: "Ecuador"}, 
    {id: 59, name: "Egypt, Arab Rep."}, 
    {id: 60, name: "El Salvador"}, 
    {id: 61, name: "Equatorial Guinea"}, 
    {id: 62, name: "Eritrea"}, 
    {id: 63, name: "Estonia"}, 
    {id: 64, name: "Eswatini"}, 
    {id: 65, name: "Ethiopia"}, 
    {id: 66, name: "Faroe Islands"}, 
    {id: 67, name: "Fiji"}, 
    {id: 68, name: "Finland"}, 
    {id: 69, name: "France"}, 
    {id: 70, name: "French Polynesia"}, 
    {id: 71, name: "Gabon"}, 
    {id: 72, name: "Gambia, The"}, 
    {id: 73, name: "Georgia"}, 
    {id: 74, name: "Germany"}, 
    {id: 75, name: "Ghana"}, 
    {id: 76, name: "Gibraltar"}, 
    {id: 77, name: "Greece"}, 
    {id: 78, name: "Greenland"}, 
    {id: 79, name: "Grenada"}, 
    {id: 80, name: "Guam"}, 
    {id: 81, name: "Guatemala"}, 
    {id: 82, name: "Guinea"}, 
    {id: 83, name: "Guinea-Bissau"}, 
    {id: 84, name: "Guyana"}, 
    {id: 85, name: "Haiti"}, 
    {id: 86, name: "Honduras"}, 
    {id: 87, name: "Hong Kong SAR, China"}, 
    {id: 88, name: "Hungary"}, 
    {id: 89, name: "Iceland"}, 
    {id: 90, name: "India"}, 
    {id: 91, name: "Indonesia"}, 
    {id: 92, name: "Iran, Islamic Rep."}, 
    {id: 93, name: "Iraq"}, 
    {id: 94, name: "Ireland"}, 
    {id: 95, name: "Isle of Man"}, 
    {id: 96, name: "Israel"}, 
    {id: 97, name: "Italy"}, 
    {id: 98, name: "Jamaica"}, 
    {id: 99, name: "Japan"}, 
    {id: 100, name: "Jordan"}, 
    {id: 101, name: "Kazakhstan"}, 
    {id: 102, name: "Kenya"}, 
    {id: 103, name: "Kiribati"}, 
    {id: 104, name: "Korea, Dem. People's Rep."}, 
    {id: 105, name: "Korea, Rep."}, 
    {id: 106, name: "Kosovo"}, 
    {id: 107, name: "Kuwait"}, 
    {id: 108, name: "Kyrgyz Republic"}, 
    {id: 109, name: "Lao PDR"}, 
    {id: 110, name: "Latvia"}, 
    {id: 111, name: "Lebanon"}, 
    {id: 112, name: "Lesotho"}, 
    {id: 113, name: "Liberia"}, 
    {id: 114, name: "Libya"}, 
    {id: 115, name: "Liechtenstein"}, 
    {id: 116, name: "Lithuania"}, 
    {id: 117, name: "Luxembourg"}, 
    {id: 118, name: "Macao SAR, China"}, 
    {id: 119, name: "Madagascar"}, 
    {id: 120, name: "Malawi"}, 
    {id: 121, name: "Malaysia"}, 
    {id: 122, name: "Maldives"}, 
    {id: 123, name: "Mali"}, 
    {id: 124, name: "Malta"}, 
    {id: 125, name: "Marshall Islands"}, 
    {id: 126, name: "Mauritania"}, 
    {id: 127, name: "Mauritius"}, 
    {id: 128, name: "Mexico"}, 
    {id: 129, name: "Micronesia, Fed. Sts."}, 
    {id: 130, name: "Moldova"}, 
    {id: 131, name: "Monaco"}, 
    {id: 132, name: "Mongolia"}, 
    {id: 133, name: "Montenegro"}, 
    {id: 134, name: "Morocco"}, 
    {id: 135, name: "Mozambique"}, 
    {id: 136, name: "Myanmar"}, 
    {id: 137, name: "Namibia"}, 
    {id: 138, name: "Nauru"}, 
    {id: 139, name: "Nepal"}, 
    {id: 140, name: "Netherlands"}, 
    {id: 141, name: "New Caledonia"}, 
    {id: 142, name: "New Zealand"}, 
    {id: 143, name: "Nicaragua"}, 
    {id: 144, name: "Niger"}, 
    {id: 145, name: "Nigeria"}, 
    {id: 146, name: "North Macedonia"}, 
    {id: 147, name: "Northern Mariana Islands"}, 
    {id: 148, name: "Norway"}, 
    {id: 149, name: "Oman"}, 
    {id: 150, name: "Pakistan"}, 
    {id: 151, name: "Palau"}, 
    {id: 152, name: "Panama"}, 
    {id: 153, name: "Papua New Guinea"}, 
    {id: 154, name: "Paraguay"}, 
    {id: 155, name: "Peru"}, 
    {id: 156, name: "Philippines"}, 
    {id: 157, name: "Poland"}, 
    {id: 158, name: "Portugal"}, 
    {id: 159, name: "Puerto Rico"}, 
    {id: 160, name: "Qatar"}, 
    {id: 161, name: "Romania"}, 
    {id: 162, name: "Russian Federation"}, 
    {id: 163, name: "Rwanda"}, 
    {id: 164, name: "Samoa"}, 
    {id: 165, name: "San Marino"}, 
    {id: 166, name: "Sao Tome and Principe"}, 
    {id: 167, name: "Saudi Arabia"}, 
    {id: 168, name: "Senegal"}, 
    {id: 169, name: "Serbia"}, 
    {id: 170, name: "Seychelles"}, 
    {id: 171, name: "Sierra Leone"}, 
    {id: 172, name: "Singapore"}, 
    {id: 173, name: "Sint Maarten (Dutch part)"}, 
    {id: 174, name: "Slovak Republic"}, 
    {id: 175, name: "Slovenia"}, 
    {id: 176, name: "Solomon Islands"}, 
    {id: 177, name: "Somalia"}, 
    {id: 178, name: "South Africa"}, 
    {id: 179, name: "South Sudan"}, 
    {id: 180, name: "Spain"}, 
    {id: 181, name: "Sri Lanka"}, 
    {id: 182, name: "St. Kitts and Nevis"}, 
    {id: 183, name: "St. Lucia"}, 
    {id: 184, name: "St. Martin (French part)"}, 
    {id: 185, name: "St. Vincent and the Grenadines"}, 
    {id: 186, name: "Sudan"}, 
    {id: 187, name: "Suriname"}, 
    {id: 188, name: "Sweden"}, 
    {id: 189, name: "Switzerland"}, 
    {id: 190, name: "Syrian Arab Republic"}, 
    {id: 191, name: "Tajikistan"}, 
    {id: 192, name: "Tanzania"}, 
    {id: 193, name: "Thailand"}, 
    {id: 194, name: "Timor-Leste"}, 
    {id: 195, name: "Togo"}, 
    {id: 196, name: "Tonga"}, 
    {id: 197, name: "Trinidad and Tobago"}, 
    {id: 198, name: "Tunisia"}, 
    {id: 199, name: "Turkiye"}, 
    {id: 200, name: "Turkmenistan"}, 
    {id: 201, name: "Turks and Caicos Islands"}, 
    {id: 202, name: "Tuvalu"}, 
    {id: 203, name: "Uganda"}, 
    {id: 204, name: "Ukraine"}, 
    {id: 205, name: "United Arab Emirates"}, 
    {id: 206, name: "United Kingdom"}, 
    {id: 207, name: "United States"}, 
    {id: 208, name: "Uruguay"}, 
    {id: 209, name: "Uzbekistan"}, 
    {id: 210, name: "Vanuatu"}, 
    {id: 211, name: "Venezuela, RB"}, 
    {id: 212, name: "Vietnam"}, 
    {id: 213, name: "Virgin Islands (U.S.)"}, 
    {id: 214, name: "West Bank and Gaza"}, 
    {id: 215, name: "Yemen, Rep."}, 
    {id: 216, name: "Zambia"}, 
    {id: 217, name: "Zimbabwe"}, 

  ];
  for(k = 0; k < statesArr.length; k++ ) {
    var stateElement = document.createElement("ul");
    stateElement.classList.add("list-group");
    stateElement.classList.add("d-flex");
    stateElement.classList.add("flex-column");
    stateElement.innerHTML = `<li class="list-group-ite b__m">${statesArr[k].name}</li>`
    states__group.appendChild(stateElement);
  }
  
});
