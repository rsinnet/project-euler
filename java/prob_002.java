import static java.lang.System.out;

class EulerProblem002 {
    public static void main(String[] args)
    {
        int fiba = 1;
        int fibb = 1;

        int cumSum = 0;
        while (fibb < 4e6)
        {
            int foo = fiba + fibb;
            fiba = fibb;
            fibb = foo;
            if (fibb % 2 == 0)
                cumSum += fibb;
        }
        out.println("Answer: " + cumSum);
    }
}