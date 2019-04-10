;; Scheme ;;

;; Q2 code;;

;;>>> (cons 1 (cons 2 (cons 3 nil)))
;;(1 2 3)
;;>>> (list 1 (list 2 (list 3)))
;;(1 (2 (3)))
;;>>> (list 1 (cons 2 (cons 3 nil)))
;; (1 (2 3))
;;>>> (cons 1 (list 2 3))
;; (1 2 3)
;;>>> (cons (list 1) (list 2 3 4))
;; ((1) 2 3 4)


(define (f f g)
	(define zipper (lambda (x) (lambda (y a) (x (y (f (g a)))) ))
	(zipper (lambda (p) (+ p 1))((lambda (q) (* q 2)) 9))))



(define (repeatedly-cube n x)
    (if (zero? n)
        x
        (let
            ((n (- n 1))
            	(y  (repeatedly-cube (- n 1) x)))
            (* y y y))))