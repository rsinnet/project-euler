import static java.lang.System.out;

class EulerProblem009
{
    public static void main(String[] args)
    {
        for (int a = 1; a < 1000; a++)
            for (int b = 1; b < 1000; b++)
                if (Math.pow(1000 - a - b, 2) == Math.pow(a, 2) + Math.pow(b, 2))
                    out.println("a = " + a + ", b = " + b +
                                ", c = " + Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2)) +
                                ", abc = " + Long.toString((int) (a * b * Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2)))));
    }
}