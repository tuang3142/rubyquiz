MOD = (1e9 + 7).to_i

def dp(n, k, mem)
  return 0 if k.zero?
  return 1 if n <= 2
  return mem[n][k] unless mem[n][k].zero?

  mem[n][k] = dp(n - 1, k - 1, mem) % MOD
  mem[n][k] = (mem[n][k] + (n - 1) * dp(n - 1, k, mem)) % MOD
end

def rearrange_sticks(n, k)
  mem = 0.upto(n).map { [0] * (k + 1) }
  return dp(n, k, mem)
end

n = 3
k = 2

p rearrange_sticks(3, 2)
