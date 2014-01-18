import static java.lang.System.out;


class EulerProblem004 {
    public static void main(String[] args)
    {

        int largest_pal = 0;

        for (int i = 999; i >= 100; i--)
        {
            for (int j = 999; j >= 100; j--)
            {
                int a = i * j;
                String str = Integer.toString(a);

                int c = (int) (Math.floor((Math.log10(a) + 1)/ 2));

                if (a > largest_pal)
                {
                    StringBuilder sb =
                        new StringBuilder(str.substring(str.length() - c));

                    if (sb.reverse().toString().equals(str.substring(0, c)))
                        largest_pal = a;
                }
            }
        }

        out.println("pal = " + largest_pal);

    }
}
