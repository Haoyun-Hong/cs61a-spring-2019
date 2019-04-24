(define (accumulate combiner start n term)
  (define (accumulate_helper combiner start n term index result)
  	(cond
  		((> index n) result)
  		(else (accumulate_helper combiner start n term (+ 1 index) (combiner result (term index))))
  		))
  (accumulate_helper combiner start n term 1 start)
)

(define (accumulate-tail combiner start n term) 
  (define (accumulate_helper combiner start n term index result)
  	(cond
  		((> index n) result)
  		(else (accumulate_helper combiner start n term (+ 1 index) (combiner result (term index))))
  		))
  (accumulate_helper combiner start n term 1 start)
)

(define (rle s) 
	(define (rle-helper s previous index)
		(cond
			((null? s) (cons-stream (list previous index) nil))
			((= previous (car  s)) (rle-helper (cdr-stream s) previous (+ 1 index)))
			(else (cons-stream (list previous index) (rle-helper s (car s) 0)))

			))

	(if (null? s) nil
	(rle-helper (cdr-stream s) (car s) 1))
)