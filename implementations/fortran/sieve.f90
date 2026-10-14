module prime_sieve
  implicit none
contains
  function sieve(n) result(primes)
    integer, intent(in) :: n
    integer, allocatable :: primes(:), candidates(:)
    logical, allocatable :: composite(:)
    integer :: p, m, i
    if (n < 2) then
      allocate(primes(0))
      return
    end if
    allocate(composite(0:n))
    composite = .false.
    p = 2
    do while (p <= n / p)
      if (.not. composite(p)) then
        do m = p * p, n, p
          composite(m) = .true.
        end do
      end if
      p = p + 1
    end do
    candidates = [(i, i=2,n)]
    primes = pack(candidates, .not. composite(2:n))
  end function
end module
program main
  use prime_sieve
  implicit none
  integer :: n, i
  integer, allocatable :: primes(:)
  character(len=32) :: arg
  n = 100
  if (command_argument_count() > 0) then
    call get_command_argument(1, arg)
    read(arg, *) n
  end if
  primes = sieve(n)
  do i = 1, size(primes)
    write(*, '(I0,1X)', advance='no') primes(i)
  end do
  write(*, *)
end program
