import static java.lang.System.out;
import java.util.Set;
import java.util.TreeSet;

class EulerProblem032 {

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

        TreeSet<Integer> set = new TreeSet<Integer>();

        for (int m = 2; m <= 9876; m++)
        {
            for (int n = 2; n <= 9876; n++)
            {
                String str = new String("" + m + n + m*n);
                if (str.length() != 9)
                    continue;
                if (isPandigital(Integer.parseInt(str)))
                {
                    set.add((int) m*n);
                }
            }
        }

        int cSum = 0;
        for (int i : set)
            cSum += i;

        out.println(cSum);
    }
}
