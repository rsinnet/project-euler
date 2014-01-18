import static java.lang.System.out;
import java.util.Set;
import java.util.TreeSet;

class EulerProblem038 {

    public static Boolean isPandigital(int n)
    {
        int digits = 0;
        int count = 0;
        int foo;

        while (n > 0)
        {
            foo = digits;
            digits = digits | 1 << (n % 10 - 1);
            if (foo == digits)
                return false;

            count++;
            n /= 10;
        }
        return digits == (1 << count) - 1;
    }

    public static void main(String[] args)
    {
        int result = 0;
        for (int i = 9387; i >= 9234; i--) {
            result = Integer.parseInt("" + i + 2*i);
            if (isPandigital(result))
                break;
        }

        out.println(result);
    }
}
