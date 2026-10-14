import 'dart:typed_data';
List<int> sieve(int n) {
  if (n < 2) return [];
  final composite = Uint8List(n + 1);
  for (var p = 2; p <= n ~/ p; p++) {
    if (composite[p] != 0) continue;
    for (var m = p * p; m <= n; m += p) { composite[m] = 1; }
  }
  return [for (var i = 2; i <= n; i++) if (composite[i] == 0) i];
}
void main(List<String> args) {
  print(sieve(args.isEmpty ? 100 : int.parse(args[0])).join(' '));
}
