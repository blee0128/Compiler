
// bad if syntax

int badone(int x)
{
  int y;

  if x      // Should error here
  {
    badone(1);
  }
}
