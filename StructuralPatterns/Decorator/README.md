## Decorator pattern lets you dynamically change the behavior of an object at run time by wrapping them in an object of a decorator class.

## The Decorator pattern applies when there is a need to dynamically add as well as remove responsibilities to a class, and when subclassing would be impossible due to the large number of subclasses that could result. Decorators provide a alternative to subclassing for extending functionality.

## The Decorator pattern is used to extend the functionality of an object dynamically without having to change the original class source or using inheritance. This is accomplished by creating an object wrapper referred to as a Decorator around the actual object.

##The participants classes in the Decorator pattern are:

##    Component. Interface for objects that can have responsibilities added to them dynamically.
##    Concrete component. Defines an object to which additional responsibilities can be added.
##    Decorator. Maintains a reference to a Component object and defines an interface that conforms to Component's interface.
##    Concrete decorators. Concrete Decorators extend the functionality of the component by adding state or adding behavior.

## When to use Decorator pattern:

##    To add responsibilities to individual objects dynamically without affecting other objects.
##    For responsibilities that can be withdrawn.
##    When extension by subclassing is impractical.
##    Its easy to maintain and extend when the number of choices are more.

