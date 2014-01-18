import static java.lang.System.out;

class EulerProblem006 {
    public static void main(String[] args)
    {
        final int m = 100;

        int a = 0;
        int b = 0;

        for (int i = 0; i <= m; i++)
        {
            a += (int) Math.pow(i, 2);
            b += i;
        }

        b = (int) Math.pow(b, 2);
        out.println(b - a);
    }
}