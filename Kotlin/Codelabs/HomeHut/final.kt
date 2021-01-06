import kotlin.math.PI

fun main() {
    
    val squareCabin = SquareCabin(6, 50.0)

    with(squareCabin){
        println("\nSquare Cabin\n============")
    	println("Capacity: ${capacity}")
    	println("Material: ${BuildingMaterial}")
    	println("Has room? ${hasRoom()}")   
        println("Floor area: ${floorArea()}")
    }
    
    val roundHut = RoundHut(3, 10.0)
    
    with(roundHut) {
    println("\nRound Hut\n=========")
    println("Material: ${BuildingMaterial}")
    println("Capacity: ${capacity}")
    println("Has room? ${hasRoom()}")
    println("Floor area: ${floorArea()}")
    
    val roundTower = RoundTower(4, 15.5)
    
    
	with(roundTower) {
    println("\nRound Tower\n==========")
    println("Material: ${BuildingMaterial}")
    println("Capacity: ${capacity}")
    println("Has room? ${hasRoom()}")
    println("Floor area: ${floorArea()}")
}
}
    
    
}

abstract class Dwelling(private var residents : Int){
    
    abstract val BuildingMaterial : String
    abstract val capacity: Int
    abstract fun floorArea(): Double
    
    fun hasRoom() : Boolean {
        return residents < capacity
    }
    
}

class SquareCabin(residents: Int,val length: Double) : Dwelling(residents) {
    override val BuildingMaterial = "Wood"
    override val capacity = 6
    
    override fun floorArea(): Double {
    return length * length}
    
}

open class RoundHut(residents: Int, val radius: Double) : Dwelling(residents) {
    override val BuildingMaterial = "Straw"
    override val capacity = 4
    
    override fun floorArea(): Double {
    return PI * radius * radius}
}

class RoundTower(residents: Int, radius: Double, floors:Int = 2) : RoundHut(residents,radius) {
    override val BuildingMaterial = "Stone"
    override val capacity = 4*floors
    
    override fun floorArea(): Double {
    return PI * radius * radius * floors
}
}





