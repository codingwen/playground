// kotlin

fun main(args: Array<String>) {
    val name = "Sam"
    val str1 = "Hello," + name
    val str2 = "Hello, $name"
    val str3 = "Hello, $name, your name's length is ${name.length}"

    val rawstring = """
    fun main(args: Array<String>) {
        val name = "Sam"
        val str1 = "Hello," + name
        val str2 = "Hello, $name"
        val str3 = "Hello, $name, your name's length is ${name.length}" 
    }
    """

    println(rawstring)
    println(name)
    println(str1)
    println(str2)
    println(str3)
}
