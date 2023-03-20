
// bad if syntax

void bad(int x)
{
  if (x)
  {
    x = 1;
  }
  else
  {
    x = 2;
  }
  else      // Another double else
  {
    x = 3;
  }
}
