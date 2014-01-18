import static java.lang.System.out;

class EulerProblem001 {
    public static void main(String[] args)
    {
        int fiba = 1;
        int fibb = 1;
        
        int cumSum = 0;
        while (fibb < 4000)
        {
            int foo = fiba + fibb;
            fiba = fibb;
            fibb = foo;
            if (fibb % 2 == 0)
                cumSum += i;
        }
        out.println("Answer: " + cumSum);
    }
}