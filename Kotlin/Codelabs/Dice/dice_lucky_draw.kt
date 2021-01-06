fun main() {
    val myFirstDice = Dice(6)
    val rollResult = myFirstDice.roll()
    val luckyNumber = (1..6).

    when (rollResult) {
		1 -> println("Better luck next time! You rolled a 1.")
        2 -> println("Better luck next time! You rolled a 2.")
        3 -> println("Better luck next time! You rolled a 3.")
        4 -> println("Congratulations!")
        5 -> println("Better luck next time! You rolled a 5.")
        6 -> println("Better luck next time! You rolled a 6.")
        
    }
}

class Dice(val numSides : Int)
{	
    
    fun roll() : Int
    {
        return (1..numSides).random()
    }
}