import static java.lang.System.out;
import java.util.List;
import java.util.ArrayList;
import java.util.Random;
import java.util.Iterator;
import java.math.BigInteger;

class EulerProblem058
{

    private static int min = 2;

    private static Boolean checkPrimality(int n)
    {
        BigInteger N = BigInteger.valueOf(n);
        Random rand = new Random();
        if (n < 3)
            return false;

        if (n % 2 == 0)
            return false;

        if (n == 3)
            return true;

        BigInteger d = BigInteger.valueOf(n - 1);
        int s = 0;

        while (d.mod(BigInteger.valueOf(2)).equals(BigInteger.ZERO))
        {
            d = d.divide(BigInteger.valueOf(2));
            s++;
        }

        int max = n - 1;

        for (int i = 0; i < 8; i++)
        {
            int a = rand.nextInt((max - min) + 1) + min;
            BigInteger foo = BigInteger.ONE;
            for (int k = 0; d.compareTo(BigInteger.valueOf(k)) > 0; k++)
                foo = foo.multiply(BigInteger.valueOf(a));
            BigInteger x = foo.mod(N);

            if (x.equals(BigInteger.ONE)||
                x.equals(BigInteger.valueOf(n - 1)))
                continue;

            for (int j = 0; j < s - 1; j++)
            {
                x = x.multiply(x).mod(N);
                if (x.equals(BigInteger.valueOf(1)))
                    return false;
                if (x.equals(BigInteger.valueOf(n - 1)))
                    break;

            }

            if (x.equals(BigInteger.valueOf(n - 1)))
                continue;

            return false;
        }
        return true;
    }

    public static void main(String[] args)
    {
        // Generate corner numbers
        List<Integer> l = new ArrayList<Integer>();
        l.add(1);

        int last = 1;

        int n_nums = 1;
        int n_primes = 0;

        for (int i = 3; i <= 171000; i += 2)
        {
            for (int j = 1; j < 5; j++)
            {
                if (checkPrimality((i-1) * j + last))
                    n_primes++;
                n_nums++;
            }
            last += 4 * (i-1);

            double foo = n_primes;
            foo /= n_nums;
            out.println(i + ": " + foo);
            if (foo <= .1)
                break;
        }

        Iterator<Integer> it = l.iterator();

        while(it.hasNext())
        {
            Integer thisInt = it.next();
            out.println(thisInt + ": " + checkPrimality(thisInt));
        }

   }
}
