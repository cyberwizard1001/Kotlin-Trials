fun main()
{
    val firstFlip = Coin()
    println("Coin 1 says ${firstFlip.flip()}")
    
    val secondFlip = Coin()
    println("Coin 2 says ${secondFlip.flip()}")
}

class Coin
{
    fun flip() : String
    {
        val flipRange = 0..1
        val selection = flipRange.random()
        
        if(selection==0)
        	return "head"
        
        else
        	return "tail"
    }
}