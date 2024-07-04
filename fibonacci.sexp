(brilisp
    (define ((print int) (n int)))

    (define ((fibonacci int) (n int))
        (set (check int) (const 2))
        (set (res bool) (lt n check))
        (br res l_true l_false)

        (label l_true)
        (ret n)

        (label l_false)
        (set (minus_1 int) (const -1))
        (set (n_minus_1 int) (add n minus_1))
        (set (fib_1 int) (call fibonacci n_minus_1))
        (set (minus_2 int) (const -2))
        (set (n_minus_2 int) (add n minus_2))        
        (set (fib_2 int) (call fibonacci n_minus_2))
        (set (fib_sum int) (add fib_1 fib_2))
        (ret fib_sum))

    (define ((main void))
        (set (n int) (const 6))
        (set (tmp int) (call fibonacci n))
        (set (temp int) (call print tmp))
        (ret)
    ))

    
    

        
        
