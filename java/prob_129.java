import static java.lang.System.out;
import java.util.List;
import java.util.ArrayList;
import java.math.BigInteger;

class EulerProblem129
{
    private static int A(int n)
    {
        BigInteger N = BigInteger.valueOf(n);
        if (!N.gcd(BigInteger.TEN).equals(BigInteger.ONE))
            return 0;

        int x = 1;
        int k = 1;

        while (x != 0)
        {
            x = (x * 10 + 1) % n;
            k++;
        }
        return k;
    }

    public static void main(String[] args)
    {

        int limit = 1000001;
        int n = limit;

        while (A(n) < limit)
            n += 2;

        out.println(n);
    }
}
