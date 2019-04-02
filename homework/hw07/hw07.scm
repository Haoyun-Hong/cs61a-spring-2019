(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cdr (cdr s)))
)

(define (sign x)
  'YOUR-CODE-HERE
  (cond
  	((< x 0) -1)
  	((= x 0) 0)
  	((> x 0) 1)
  	)
)

(define (square x) (* x x))

(define (pow b n)
  'YOUR-CODE-HERE
  (cond
  	((= n 0) 1)
  	((even? n) (square (pow b (/ n  2))))
  	((odd? n) (* b (square (pow b (/ (- n 1) 2)))))
  	)
)

(define (ordered? s)
  'YOUR-CODE-HERE
  (cond
  	((null? (cdr s)) True)
  	((> (car s) (cadr s)) False)
  	((< (car s) (cadr s)) (ordered? (cdr s)))
  	((= (car s) (cadr s)) (ordered? (cdr s)))
  	)
)