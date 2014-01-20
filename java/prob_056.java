import static java.lang.System.out;
import java.util.List;
import java.util.ArrayList;
import java.math.BigInteger;

class EulerProblem056
{

    private final static int limit = 100;

    private static int DigitSum(BigInteger x)
    {
        int dSum = 0;
        char[] ca = x.toString().toCharArray();
        for (int i = 0; i < ca.length; i++)
        {
            dSum += ca[i];
        }
        return dSum - 48 * ca.length;
    }

    private static BigInteger pow(int base, int exponent)
    {

        BigInteger bBase = BigInteger.valueOf(base);
        BigInteger result = BigInteger.ONE;
        while(exponent-- > 0)
        {
            result = result.multiply(bBase);
        }
        return result;
    }

    public static void main(String[] args)
    {
        int result = 0;
        int maxSum = 0;

        for (int a = limit-1; a > 0; a--)
        {
            for (int b = limit-1; b > 0; b--)
            {
                int foo = DigitSum(pow(a, b));
                if (foo > maxSum)
                {
                    maxSum = foo;
                    out.println(maxSum);
                }
            }
        }
    }
}
