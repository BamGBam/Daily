public class Point {
    int x;
    int y;

    public double distance(Point other) {
        // System.out.println("Point is " + other);
        double diffx = (other.x - this.x);
        double diffy = (other.y - this.y);
        double distance = Math.sqrt((diffx * diffx) + (diffy * diffy));
        return distance;

    }
    // // your code goes here
}