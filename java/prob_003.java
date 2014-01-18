import static java.lang.System.out;
import java.math.BigInteger;

class EulerProblem003 {
    public static void main(String[] args)
    {
        BigInteger z = new BigInteger("600851475143");
        int i = 2;
        int m = 10000;

        Boolean[] comp_nums = new Boolean[m];

        for (int j = 0; j < m; j++)
            comp_nums[j] = false;

        while (i <= m / 2)
        {
            if (comp_nums[i-1] == false)
                for (int k = 2*i; k < m + 1; k += i)
                    comp_nums[k-1] = true;
            i++;
        }

        for (int j = 1; j < comp_nums.length; j++)
        {
            if (!comp_nums[j])
            {
                BigInteger a = BigInteger.valueOf(j+1);
                if (z.mod(a).equals(BigInteger.ZERO))
                {
                    z = z.divide(a);
                    out.println("factor: " + (j+1));
                    if (z.equals(BigInteger.valueOf(1)))
                        break;
                }
            }
        }
    }
}

/**
m = int(1e4)

i = 2

# Find all prime numbers up to ten thousand
comp_nums = [False] * m
while i <= m / 2:
    if not comp_nums[i-1]:
        for x in range(2*i, m+1, i):
            comp_nums[x-1] = True
    i += 1
foo = [j+1 for j, y in enumerate(comp_nums) if not y and j+1 > 1]

print 'Found primes up to ten thousand! Factoring...'

for x in foo:
    if not z % x:
        y = z / x
        print '{} / {} = {}'.format(z, x, y)
        z = y

if z == 1:
    print 'Factorized!'
**/