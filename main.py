info.onCountdownEnd(function () {
    game.reset()
    info.setScore(0)
})
info.onLifeZero(function () {
    game.reset()
    info.setScore(0)
})
let chooseq: boolean[] = []
let allqs: boolean[] = []
music.jumpUp.play()
pause(100)
music.jumpUp.play()
pause(100)
music.jumpUp.play()
pause(100)
music.jumpUp.play()
pause(100)
music.jumpUp.play()
pause(100)
music.jumpUp.play()
pause(100)
music.jumpUp.play()
pause(100)
let mySprite = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.Player)
mySprite.sayText("Welcome to Interstate 20, 285, and A Couple Roads in Texas!")
pause(2000)
mySprite.sayText("You have decided that YOU want to live on the beautiful shores of CADDO LAKE")
pause(2000)
mySprite.sayText(" (or maybe in a houseboat? You saw a cool ad for those).")
pause(2000)
mySprite.sayText("Your goal is to travel by Toyota Corolla from Atlanta, GA to Caddo Lake")
pause(1000)
mySprite.sayText("(A distance of 600 miles)")
pause(2000)
mySprite.sayText("The highway is car-azy! Each day costs you food and health")
pause(1000)
mySprite.sayText("(because fast food, right?).")
pause(1000)
mySprite.sayText("Anyway, you can eat more fast food and stop at a rest area")
pause(2000)
mySprite.sayText("BUT YOU HAVE TO GET TO CADDO LAKE BEFORE THE TIMER RUNS OUT (15 mins)")
pause(2000)
mySprite.sayText("(Otherwise, INFLATION happens and the properties become SUPER EXPENSIVE")
pause(2000)
mySprite.sayText("BUT INFLATION MIGHT ALREADY BE HAPPENING! INFLATION IS A BALLOON!!!!!])")
pause(5000)
mySprite.sayText("Each turn you can take one of 3 actions:")
pause(2000)
mySprite.sayText("CAR TRIP - moves you 50 miles and takes 2 days")
pause(5000)
mySprite.sayText("Rest Area- increases a random number of health levels and takes 2-5 days.")
pause(5000)
mySprite.sayText("Buy Fast Food-adds 50 lbs of food and takes 1-2 days (random).")
pause(2000)
mySprite.sayText("When prompted for an action, you can also enter the following without using up your turn:")
pause(2000)
mySprite.sayText("quit - will end the game")
pause(5000)
mySprite.sayText("Good luck and see you in CYPRESS PARADISE!!!", 500, false)
info.setLife(10)
info.startCountdown(900)
let math_questions_trup: Array = [
"8(2+8) is a numeric expression",
"(2x^2)/3 is an algebraic expression",
"8x(4xy+4y-3) when x=-6 and y=9 is 8784",
"(8a+8(4a-3b)) when a=8, b=-4 is 416",
"8w^3 - 3w^2 + 3w^3 - 10w^4 + 3 Simplified in Standard form is -10w^4 + 11w3 - 3wvi32 + 3",
"9ab^2 - 3b^2(4a + 3b - 8a + 12b) Simplified in Standard form is -45b^3 + 21ab^2, c=45b^3 - 21ab^2",
"The degree of (12a^3 - 6a^3) + (9a + 4a^2) is quadratic",
"The standard form and term name of (24c^3 - 3c^2) - (9c^3 - 3c^3 + 4c^2 + 4c) is 18c^3 - 7c^2 - 4c (trinomial)",
"The degree of 8x^9y^3z^10 is 22",
"The degree of 45q^9 + 8qr^9 + 27s^9 is 10",
"9a^3 - 8a - 3a^2 + 8a^4 + 3 in standard form is 8a^4 + 9a^3 - 3a^2 - 8a + 3",
"8a^4 + 9a^3 - 3a^2 - 8a + 3 in standard form is -6x^3 - 6"
]
let math_questions_false: Array = [
"(40ab^2)(3a^2bx) multiplying monomials is equal to 120a^2b^2x",
"Adding polynomials and putting in standard form, (9a^4 - 6a^2) + (3a^2 - 3a^4 + 11a^2) is equal to 6a^4 + 2a^2",
"dividing monomials, (8x^3y^3)/(8x^2)=64x^5y^3",
"",
"",
"",
"",
"",
"",
"",
"",
""
]
forever(function () {
    while (controller.up.isPressed()) {
        allqs = [math_questions_trup._pickRandom() || math_questions_false._pickRandom()]
        chooseq = [allqs._pickRandom()]
    }
    while (controller.left.isPressed()) {
        allqs = [math_questions_trup._pickRandom() || math_questions_false._pickRandom()]
        chooseq = [allqs._pickRandom()]
    }
    while (controller.down.isPressed()) {
        allqs = [math_questions_trup._pickRandom() || math_questions_false._pickRandom()]
        chooseq = [allqs._pickRandom()]
    }
})
