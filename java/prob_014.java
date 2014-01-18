import static java.lang.System.out;
import java.math.BigInteger;

class EulerProblem014 {
    private final int N = 1000000;
    private int[] sequence_lengths = new int[1*N];

    public EulerProblem014()
    {
        for (int i = 0; i < sequence_lengths.length; i++)
            sequence_lengths[i] = 0;
    }

    private int getCollatzLength(int x)
    {
        int i = 1;
        int y = x;
        BigInteger xx = BigInteger.valueOf(x);
        while (xx.compareTo(BigInteger.valueOf(1)) != 0)
        {
            if (xx.compareTo(BigInteger.valueOf(N)) < 0)
            {
                // sequence caching
                if (sequence_lengths[xx.add(BigInteger.valueOf(-1)).intValue()] != 0)
                {
                    sequence_lengths[y - 1] =
                        sequence_lengths[xx.add(BigInteger.valueOf(-1)).intValue()] + i - 1;
                    return sequence_lengths[y - 1];
                }
            }
            i++;
            if (!xx.mod(BigInteger.valueOf(2)).equals(BigInteger.ZERO))
                xx = xx.multiply(BigInteger.valueOf(3)).add(BigInteger.valueOf(1));
            else
                xx = xx.divide(BigInteger.valueOf(2));
        }
        sequence_lengths[y-1] = i;
        return i;
    }

    public void go()
    {
        int maxCollatz = 0;
        int maxNum = 0;
        int thisCollatz = 0;

        for (int x = 2; x < 1000000; x++)
        {
            thisCollatz = getCollatzLength(x);
            if (thisCollatz > maxCollatz)
            {
                maxCollatz = thisCollatz;
                maxNum = x;
                out.println("New biggest sequence: "
                            + maxNum + ": " + maxCollatz);
            }
        }
        out.println(maxNum + ", " + maxCollatz);
    }
    public static void main(String[] args)
    {
        EulerProblem014 ep = new EulerProblem014();
        ep.go();
    }
}
