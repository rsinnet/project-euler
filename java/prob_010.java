import static java.lang.System.out;
import java.math.BigInteger;

class EulerProblem010 {
    public static void main(String[] args)
    {
        final int N = 2000000 - 1;
        Boolean[] comp_nums = new Boolean[N];

        for (int j = 0; j < comp_nums.length; j++)
            comp_nums[j] = false;

        int i = 2;
        while (2*i <= N)
        {
            if (!comp_nums[i - 1])
                for (int k = 2*i; k <= N; k += i)
                    comp_nums[k - 1] = true;
            i++;
        }

        BigInteger cSum = BigInteger.valueOf(0);
        for (int j = 1; j < comp_nums.length; j++)
            if (!comp_nums[j])
            {
                cSum = cSum.add(BigInteger.valueOf(j + 1));
            }

        out.println("Answer: " + cSum);
    }
}
