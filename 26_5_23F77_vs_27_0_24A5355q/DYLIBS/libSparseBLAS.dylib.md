## libSparseBLAS.dylib

> `/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparseBLAS.dylib`

```diff

-1551.100.26.0.0
-  __TEXT.__text: 0x256c0
-  __TEXT.__auth_stubs: 0x4a0
+192.0.0.0.1
+  __TEXT.__text: 0x207e0
   __TEXT.__oslogstring: 0x53
-  __TEXT.__cstring: 0x201
-  __TEXT.__const: 0x50
-  __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__unwind_info: 0x3c8
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x8a0
-  __AUTH_CONST.__auth_got: 0x258
+  __TEXT.__cstring: 0x1f8
+  __TEXT.__gcc_except_tab: 0x20
+  __TEXT.__const: 0x40
+  __TEXT.__unwind_info: 0x2a8
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0xa0
+  __DATA_CONST.__weak_got: 0x8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
+  __AUTH_CONST.__weak_auth_got: 0x10
+  __AUTH_CONST.__auth_got: 0x240
   __DATA_DIRTY.__bss: 0x48
   - /System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBLAS.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 93D45C7C-BEA4-3ECC-96B6-EE4362CD6C2B
-  Functions: 295
-  Symbols:   620
-  CStrings:  25
+  UUID: 9F9C30BE-D148-3F6A-927C-B1E459F95A12
+  Functions: 224
+  Symbols:   412
+  CStrings:  24
 
Symbols:
+ GCC_except_table17
+ __ZNSt12length_errorC1B9fqe220100EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE22__init_internal_bufferB9fqe220100Em
+ __ZNSt3__120__throw_length_errorB9fqe220100EPKc
+ _cblas_caxpy$NEWLAPACK
+ _cblas_ccopy$NEWLAPACK
+ _cblas_cgemm$NEWLAPACK
+ _cblas_cgemv$NEWLAPACK
+ _cblas_cscal$NEWLAPACK
+ _cblas_ctrsm$NEWLAPACK
+ _cblas_ctrsv$NEWLAPACK
+ _cblas_dasum$NEWLAPACK
+ _cblas_daxpy$NEWLAPACK
+ _cblas_dcopy$NEWLAPACK
+ _cblas_dgemm$NEWLAPACK
+ _cblas_dgemv$NEWLAPACK
+ _cblas_dnrm2$NEWLAPACK
+ _cblas_dscal$NEWLAPACK
+ _cblas_dsdot$NEWLAPACK
+ _cblas_dtrsm$NEWLAPACK
+ _cblas_dtrsv$NEWLAPACK
+ _cblas_dzasum$NEWLAPACK
+ _cblas_dznrm2$NEWLAPACK
+ _cblas_icamax$NEWLAPACK
+ _cblas_idamax$NEWLAPACK
+ _cblas_isamax$NEWLAPACK
+ _cblas_izamax$NEWLAPACK
+ _cblas_sasum$NEWLAPACK
+ _cblas_saxpy$NEWLAPACK
+ _cblas_scasum$NEWLAPACK
+ _cblas_scnrm2$NEWLAPACK
+ _cblas_scopy$NEWLAPACK
+ _cblas_sgemm$NEWLAPACK
+ _cblas_sgemv$NEWLAPACK
+ _cblas_snrm2$NEWLAPACK
+ _cblas_sscal$NEWLAPACK
+ _cblas_strsm$NEWLAPACK
+ _cblas_strsv$NEWLAPACK
+ _cblas_zaxpy$NEWLAPACK
+ _cblas_zcopy$NEWLAPACK
+ _cblas_zgemm$NEWLAPACK
+ _cblas_zgemv$NEWLAPACK
+ _cblas_zscal$NEWLAPACK
+ _cblas_ztrsm$NEWLAPACK
+ _cblas_ztrsv$NEWLAPACK
- GCC_except_table16
- _CSC_ConjTrans_matrix_vector_product_dense_double_complex
- _CSC_ConjTrans_matrix_vector_product_dense_float_complex
- _CSC_Conj_matrix_vector_product_dense_double_complex
- _CSC_Conj_matrix_vector_product_dense_float_complex
- __NSConcreteStackBlock
- __ZNSt12length_errorC1B9nqe210106EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__120__throw_length_errorB9nqe210106EPKc
- ___block_descriptor_tmp.1
- ___block_descriptor_tmp.10
- ___block_descriptor_tmp.11
- ___block_descriptor_tmp.12
- ___block_descriptor_tmp.13
- ___block_descriptor_tmp.14
- ___block_descriptor_tmp.15
- ___block_descriptor_tmp.16
- ___block_descriptor_tmp.17
- ___block_descriptor_tmp.18
- ___block_descriptor_tmp.19
- ___block_descriptor_tmp.2
- ___block_descriptor_tmp.20
- ___block_descriptor_tmp.21
- ___block_descriptor_tmp.22
- ___block_descriptor_tmp.23
- ___block_descriptor_tmp.24
- ___block_descriptor_tmp.25
- ___block_descriptor_tmp.26
- ___block_descriptor_tmp.27
- ___block_descriptor_tmp.28
- ___block_descriptor_tmp.29
- ___block_descriptor_tmp.3
- ___block_descriptor_tmp.30
- ___block_descriptor_tmp.31
- ___block_descriptor_tmp.32
- ___block_descriptor_tmp.33
- ___block_descriptor_tmp.34
- ___block_descriptor_tmp.35
- ___block_descriptor_tmp.4
- ___block_descriptor_tmp.5
- ___block_descriptor_tmp.6
- ___block_descriptor_tmp.7
- ___block_descriptor_tmp.8
- ___block_descriptor_tmp.9
- ___sparse_inner_product_dense_double_block_invoke
- ___sparse_inner_product_dense_double_complex_block_invoke
- ___sparse_inner_product_dense_float_block_invoke
- ___sparse_inner_product_dense_float_complex_block_invoke
- ___sparse_matrix_product_dense_double_block_invoke
- ___sparse_matrix_product_dense_double_block_invoke_2
- ___sparse_matrix_product_dense_double_block_invoke_3
- ___sparse_matrix_product_dense_double_block_invoke_4
- ___sparse_matrix_product_dense_double_block_invoke_5
- ___sparse_matrix_product_dense_double_block_invoke_6
- ___sparse_matrix_product_dense_double_block_invoke_7
- ___sparse_matrix_product_dense_double_block_invoke_8
- ___sparse_matrix_product_dense_double_complex_block_invoke
- ___sparse_matrix_product_dense_double_complex_block_invoke_2
- ___sparse_matrix_product_dense_double_complex_block_invoke_3
- ___sparse_matrix_product_dense_double_complex_block_invoke_4
- ___sparse_matrix_product_dense_double_complex_block_invoke_5
- ___sparse_matrix_product_dense_double_complex_block_invoke_6
- ___sparse_matrix_product_dense_double_complex_block_invoke_7
- ___sparse_matrix_product_dense_double_complex_block_invoke_8
- ___sparse_matrix_product_dense_float_block_invoke
- ___sparse_matrix_product_dense_float_block_invoke_2
- ___sparse_matrix_product_dense_float_block_invoke_3
- ___sparse_matrix_product_dense_float_block_invoke_4
- ___sparse_matrix_product_dense_float_block_invoke_5
- ___sparse_matrix_product_dense_float_block_invoke_6
- ___sparse_matrix_product_dense_float_block_invoke_7
- ___sparse_matrix_product_dense_float_block_invoke_8
- ___sparse_matrix_product_dense_float_complex_block_invoke
- ___sparse_matrix_product_dense_float_complex_block_invoke_2
- ___sparse_matrix_product_dense_float_complex_block_invoke_3
- ___sparse_matrix_product_dense_float_complex_block_invoke_4
- ___sparse_matrix_product_dense_float_complex_block_invoke_5
- ___sparse_matrix_product_dense_float_complex_block_invoke_6
- ___sparse_matrix_product_dense_float_complex_block_invoke_7
- ___sparse_matrix_product_dense_float_complex_block_invoke_8
- ___sparse_matrix_triangular_solve_dense_double_block_invoke
- ___sparse_matrix_triangular_solve_dense_double_complex_block_invoke
- ___sparse_matrix_triangular_solve_dense_float_block_invoke
- ___sparse_matrix_triangular_solve_dense_float_complex_block_invoke
- ___sparse_matrix_vector_product_dense_double_block_invoke
- ___sparse_matrix_vector_product_dense_double_block_invoke_2
- ___sparse_matrix_vector_product_dense_double_block_invoke_3
- ___sparse_matrix_vector_product_dense_double_block_invoke_4
- ___sparse_matrix_vector_product_dense_double_complex_block_invoke
- ___sparse_matrix_vector_product_dense_double_complex_block_invoke_2
- ___sparse_matrix_vector_product_dense_double_complex_block_invoke_3
- ___sparse_matrix_vector_product_dense_double_complex_block_invoke_4
- ___sparse_matrix_vector_product_dense_double_complex_block_invoke_5
- ___sparse_matrix_vector_product_dense_double_complex_block_invoke_6
- ___sparse_matrix_vector_product_dense_float_block_invoke
- ___sparse_matrix_vector_product_dense_float_block_invoke_2
- ___sparse_matrix_vector_product_dense_float_block_invoke_3
- ___sparse_matrix_vector_product_dense_float_block_invoke_4
- ___sparse_matrix_vector_product_dense_float_complex_block_invoke
- ___sparse_matrix_vector_product_dense_float_complex_block_invoke_2
- ___sparse_matrix_vector_product_dense_float_complex_block_invoke_3
- ___sparse_matrix_vector_product_dense_float_complex_block_invoke_4
- ___sparse_matrix_vector_product_dense_float_complex_block_invoke_5
- ___sparse_matrix_vector_product_dense_float_complex_block_invoke_6
- ___sparse_vector_add_with_scale_dense_double_block_invoke
- ___sparse_vector_add_with_scale_dense_double_complex_block_invoke
- ___sparse_vector_add_with_scale_dense_float_block_invoke
- ___sparse_vector_add_with_scale_dense_float_complex_block_invoke
- _cblas_caxpy
- _cblas_ccopy
- _cblas_cgemm
- _cblas_cgemv
- _cblas_cscal
- _cblas_ctrsm
- _cblas_ctrsv
- _cblas_dasum
- _cblas_daxpy
- _cblas_dcopy
- _cblas_dgemm
- _cblas_dgemv
- _cblas_dnrm2
- _cblas_dscal
- _cblas_dsdot
- _cblas_dtrsm
- _cblas_dtrsv
- _cblas_dzasum
- _cblas_dznrm2
- _cblas_icamax
- _cblas_idamax
- _cblas_isamax
- _cblas_izamax
- _cblas_sasum
- _cblas_saxpy
- _cblas_scasum
- _cblas_scnrm2
- _cblas_scopy
- _cblas_sgemm
- _cblas_sgemv
- _cblas_snrm2
- _cblas_sscal
- _cblas_strsm
- _cblas_strsv
- _cblas_zaxpy
- _cblas_zcopy
- _cblas_zgemm
- _cblas_zgemv
- _cblas_zscal
- _cblas_ztrsm
- _cblas_ztrsv
- _dispatch_apply
- _matrix_triangular_solve_dense_double
- _matrix_triangular_solve_dense_double_complex
- _matrix_triangular_solve_dense_float
- _matrix_triangular_solve_dense_float_complex
CStrings:
- "v16@?0Q8"

```
