(brilisp
	(define ((print int) (n int)))

	(define ((main int))
		(set (v0 int) (const 11))
		(set (v1 int) (const 22))
		(set (res int) (add v0 v1))
		(set (temp int) (call print res))
		(ret temp)))
