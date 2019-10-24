use strict;
use warnings;
use Time::HiRes;

$| = 1;
my $WAIT = 0.01;

open(my $TEXT, $ARGV[0]);

while (my $line = <$TEXT>) {
  chomp($line);
  for my $c (split(//, $line)) {
    print($c);
    Time::HiRes::sleep($WAIT);
  }

  chomp(my $input = <STDIN>);
  if ($input eq 'q') {
    exit();
  }
}
