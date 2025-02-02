"""
Programming paradigms:
    A style of writing code, most real programs are a combination.

    We're learning about OOP, but there are more paradigms out there it's good to know they exist.

    - Procedural:
        - The intuitive way of writing code. (Probably what you've been doing up to now)
            A series of instructions. When it gets too complicated, or a set of instructions
            repeats very often you tend to put those in functions.

        - State is global & mutable.

    - Object-oriented:
        - Objects are used to create abstractions.

        - State is held in objects & is mutable, but its mutation is controlled by the methods
        of the object. (Encapsulation)

        - And more... (I explain later)

    - Functional:
        - Like procedural, but you use way more functions.

        - Functions are "pure" which means they must always return the same output given the same
            input, i.e. they don't depend on global state. e.g.

            def pure(a): return a

            a = 1
            def dirty(): return a

        - Data is not mutable, e.g. you create a new list instead of modifying the elements.

        - You pass functions into other functions as arguments.

        - You call a function from within itself (recursion) instead of using loops.

    - Data-oriented:
        - Like procedural but there's more emphasis on putting all the data into very long structures
            & separating it from the logic, mainly for performance but also simplicity.

        - For the pros.

"""