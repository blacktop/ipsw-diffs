## libLAPACK.dylib

> `/System/ExclaveKit/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libLAPACK.dylib`

```diff

-1510.0.0.0.0
-  __TEXT.__text: 0x123264
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__const: 0x160
-  __TEXT.__cstring: 0x308
-  __TEXT.__gcc_except_tab: 0x4f0
-  __TEXT.__unwind_info: 0xc20
-  __TEXT.__eh_frame: 0x138
-  __DATA.__auth_got: 0x370
-  __DATA.__got: 0x20
-  __DATA.__auth_ptr: 0x70
-  __DATA.__const: 0x2c0
+1510.60.2.0.0
+  __TEXT.__text: 0x3e73e8
+  __TEXT.__auth_stubs: 0xbe0
+  __TEXT.__const: 0x7b0
+  __TEXT.__cstring: 0x7ab
+  __TEXT.__gcc_except_tab: 0x13f0
+  __TEXT.__unwind_info: 0x2650
+  __TEXT.__eh_frame: 0x788
+  __DATA.__auth_got: 0x5f8
+  __DATA.__got: 0x30
+  __DATA.__auth_ptr: 0x120
+  __DATA.__const: 0x5c0
   __DATA.__data: 0x4
   __DATA.__bss: 0x38
   - /System/ExclaveKit/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBLAS.dylib
   - /System/ExclaveKit/System/Library/Frameworks/MobileGestalt.framework/MobileGestalt
   - /System/ExclaveKit/usr/lib/libSystem.dylib
   - /System/ExclaveKit/usr/lib/libc++.dylib
-  Functions: 1291
-  Symbols:   234
-  CStrings:  132
+  Functions: 3913
+  Symbols:   393
+  CStrings:  300
 
Symbols:
+ _APL_dgemm
+ _APL_dgemm_LU
+ _APL_dgemm_QR
+ _APL_dsyrk
+ _APL_dtrsm
+ __ZNSt20bad_array_new_lengthC1Ev
+ __ZNSt20bad_array_new_lengthD1Ev
+ __ZSt9terminatev
+ __ZTISt20bad_array_new_length
+ __ZdaPvSt19__type_descriptor_t
+ __ZdlPvSt19__type_descriptor_t
+ __ZnamSt19__type_descriptor_t
+ __ZnwmSt19__type_descriptor_t
+ ___cxa_begin_catch
+ ___memcpy_chk
+ _cblas_dasum$NEWLAPACK
+ _cblas_dasum$NEWLAPACK$ILP64
+ _cblas_daxpy$NEWLAPACK
+ _cblas_daxpy$NEWLAPACK$ILP64
+ _cblas_dcopy$NEWLAPACK
+ _cblas_dcopy$NEWLAPACK$ILP64
+ _cblas_ddot$NEWLAPACK
+ _cblas_ddot$NEWLAPACK$ILP64
+ _cblas_dgemm$NEWLAPACK
+ _cblas_dgemm$NEWLAPACK$ILP64
+ _cblas_dgemv$NEWLAPACK
+ _cblas_dgemv$NEWLAPACK$ILP64
+ _cblas_dger$NEWLAPACK
+ _cblas_dger$NEWLAPACK$ILP64
+ _cblas_dnrm2$NEWLAPACK
+ _cblas_dnrm2$NEWLAPACK$ILP64
+ _cblas_drot$NEWLAPACK
+ _cblas_drot$NEWLAPACK$ILP64
+ _cblas_dscal$NEWLAPACK
+ _cblas_dscal$NEWLAPACK$ILP64
+ _cblas_dswap$NEWLAPACK
+ _cblas_dswap$NEWLAPACK$ILP64
+ _cblas_dsymv$NEWLAPACK
+ _cblas_dsymv$NEWLAPACK$ILP64
+ _cblas_dsyr$NEWLAPACK
+ _cblas_dsyr$NEWLAPACK$ILP64
+ _cblas_dsyr2$NEWLAPACK
+ _cblas_dsyr2$NEWLAPACK$ILP64
+ _cblas_dsyr2k$NEWLAPACK
+ _cblas_dsyr2k$NEWLAPACK$ILP64
+ _cblas_dsyrk$NEWLAPACK
+ _cblas_dsyrk$NEWLAPACK$ILP64
+ _cblas_dtbsv$NEWLAPACK
+ _cblas_dtbsv$NEWLAPACK$ILP64
+ _cblas_dtrmm$NEWLAPACK
+ _cblas_dtrmm$NEWLAPACK$ILP64
+ _cblas_dtrmv$NEWLAPACK
+ _cblas_dtrmv$NEWLAPACK$ILP64
+ _cblas_dtrsm$NEWLAPACK
+ _cblas_dtrsm$NEWLAPACK$ILP64
+ _cblas_dtrsv$NEWLAPACK
+ _cblas_dtrsv$NEWLAPACK$ILP64
+ _cblas_idamax$NEWLAPACK
+ _cblas_idamax$NEWLAPACK$ILP64
+ _cblas_saxpy$NEWLAPACK
+ _cblas_saxpy$NEWLAPACK$ILP64
+ _cblas_snrm2$NEWLAPACK
+ _cblas_snrm2$NEWLAPACK$ILP64
+ _cblas_srot$NEWLAPACK
+ _cblas_srot$NEWLAPACK$ILP64
+ _cblas_ssymv$NEWLAPACK
+ _cblas_ssymv$NEWLAPACK$ILP64
+ _cblas_ssyr$NEWLAPACK
+ _cblas_ssyr$NEWLAPACK$ILP64
+ _cblas_ssyr2$NEWLAPACK
+ _cblas_ssyr2$NEWLAPACK$ILP64
+ _cblas_ssyr2k$NEWLAPACK
+ _cblas_ssyr2k$NEWLAPACK$ILP64
+ _dgbsv$NEWLAPACK
+ _dgbsv$NEWLAPACK$ILP64
+ _dgePack_A_NoTran
+ _dgePack_A_Tran
+ _dgePack_B_NoTran
+ _dgePack_B_Tran
+ _dgecon$NEWLAPACK
+ _dgecon$NEWLAPACK$ILP64
+ _dgeev$NEWLAPACK
+ _dgeev$NEWLAPACK$ILP64
+ _dgeqrf$NEWLAPACK
+ _dgeqrf$NEWLAPACK$ILP64
+ _dgesdd$NEWLAPACK
+ _dgesdd$NEWLAPACK$ILP64
+ _dgesv$NEWLAPACK
+ _dgesv$NEWLAPACK$ILP64
+ _dgesvd$NEWLAPACK
+ _dgesvd$NEWLAPACK$ILP64
+ _dgetrf$NEWLAPACK
+ _dgetrf$NEWLAPACK$ILP64
+ _dgetri$NEWLAPACK
+ _dgetri$NEWLAPACK$ILP64
+ _dgetrs$NEWLAPACK
+ _dgetrs$NEWLAPACK$ILP64
+ _dorgqr$NEWLAPACK
+ _dorgqr$NEWLAPACK$ILP64
+ _dormqr$NEWLAPACK
+ _dormqr$NEWLAPACK$ILP64
+ _dposv$NEWLAPACK
+ _dposv$NEWLAPACK$ILP64
+ _dpotrf$NEWLAPACK
+ _dpotrf$NEWLAPACK$ILP64
+ _dpotri$NEWLAPACK
+ _dpotri$NEWLAPACK$ILP64
+ _dpotrs$NEWLAPACK
+ _dpotrs$NEWLAPACK$ILP64
+ _dpstrf$NEWLAPACK
+ _dpstrf$NEWLAPACK$ILP64
+ _dsyev$NEWLAPACK
+ _dsyev$NEWLAPACK$ILP64
+ _dsysv$NEWLAPACK
+ _dsysv$NEWLAPACK$ILP64
+ _dsytrf$NEWLAPACK
+ _dsytrf$NEWLAPACK$ILP64
+ _dsytrs$NEWLAPACK
+ _dsytrs$NEWLAPACK$ILP64
+ _dtrtri$NEWLAPACK
+ _dtrtri$NEWLAPACK$ILP64
+ _dtrtrs$NEWLAPACK
+ _dtrtrs$NEWLAPACK$ILP64
+ _log
+ _log10
+ _log10f
+ _memset_pattern16
+ _memset_pattern8
+ _pow
+ _sgeev$NEWLAPACK
+ _sgeev$NEWLAPACK$ILP64
+ _sgeqrf$NEWLAPACK
+ _sgeqrf$NEWLAPACK$ILP64
+ _sgesdd$NEWLAPACK
+ _sgesdd$NEWLAPACK$ILP64
+ _sgesv$NEWLAPACK
+ _sgesv$NEWLAPACK$ILP64
+ _sgesvd$NEWLAPACK
+ _sgesvd$NEWLAPACK$ILP64
+ _sgetrs$NEWLAPACK
+ _sgetrs$NEWLAPACK$ILP64
+ _sorgqr$NEWLAPACK
+ _sorgqr$NEWLAPACK$ILP64
+ _sormqr$NEWLAPACK
+ _sormqr$NEWLAPACK$ILP64
+ _sposv$NEWLAPACK
+ _sposv$NEWLAPACK$ILP64
+ _spotrs$NEWLAPACK
+ _spotrs$NEWLAPACK$ILP64
+ _ssyev$NEWLAPACK
+ _ssyev$NEWLAPACK$ILP64
+ _ssysv$NEWLAPACK
+ _ssysv$NEWLAPACK$ILP64
+ _ssytrf$NEWLAPACK
+ _ssytrf$NEWLAPACK$ILP64
+ _ssytrs$NEWLAPACK
+ _ssytrs$NEWLAPACK$ILP64
+ _strtrs$NEWLAPACK
+ _strtrs$NEWLAPACK$ILP64
CStrings:
+ "ALL"
+ "Backward"
+ "Base"
+ "DBDSDC"
+ "DBDSQR"
+ "DGBSV "
+ "DGBTF2"
+ "DGBTRF"
+ "DGBTRS"
+ "DGEBAK"
+ "DGEBAL"
+ "DGEBD2"
+ "DGEBRD"
+ "DGECON"
+ "DGEEV "
+ "DGEHD2"
+ "DGEHRD"
+ "DGELQ2"
+ "DGELQF"
+ "DGEQR2"
+ "DGEQRF"
+ "DGESDD"
+ "DGESV "
+ "DGESVD"
+ "DGETF2"
+ "DGETRF"
+ "DGETRF2"
+ "DGETRI"
+ "DGETRS"
+ "DHSEQR"
+ "DLAQR0"
+ "DLAQR3"
+ "DLAQR4"
+ "DLASCL"
+ "DLASD0"
+ "DLASD1"
+ "DLASD2"
+ "DLASD3"
+ "DLASD6"
+ "DLASD7"
+ "DLASD8"
+ "DLASDA"
+ "DLASDQ"
+ "DLASQ1"
+ "DLASR "
+ "DLASRT"
+ "DLATRS"
+ "DLAUU2"
+ "DLAUUM"
+ "DORG2L"
+ "DORG2R"
+ "DORGBR"
+ "DORGHR"
+ "DORGL2"
+ "DORGLQ"
+ "DORGQL"
+ "DORGQR"
+ "DORGTR"
+ "DORM2R"
+ "DORMBR"
+ "DORMHR"
+ "DORML2"
+ "DORMLQ"
+ "DORMQR"
+ "DPOSV "
+ "DPOTF2"
+ "DPOTRF"
+ "DPOTRF2"
+ "DPOTRI"
+ "DPOTRS"
+ "DPSTF2"
+ "DPSTRF"
+ "DSTEQR"
+ "DSTERF"
+ "DSYCONV"
+ "DSYEV "
+ "DSYSV "
+ "DSYTD2"
+ "DSYTF2"
+ "DSYTRD"
+ "DSYTRF"
+ "DSYTRS"
+ "DSYTRS2"
+ "DTREVC"
+ "DTREVC3"
+ "DTREXC"
+ "DTRTI2"
+ "DTRTRI"
+ "DTRTRS"
+ "Full"
+ "GEQRF"
+ "Max"
+ "NO TRANSPOSE"
+ "NON-UNIT"
+ "No Trans"
+ "No Transpose"
+ "PRECISION"
+ "RIGHT"
+ "SAFE MINIMUM"
+ "SBDSDC"
+ "SBDSQR"
+ "SGEBAK"
+ "SGEBAL"
+ "SGEBD2"
+ "SGEBRD"
+ "SGEEV "
+ "SGEHD2"
+ "SGEHRD"
+ "SGELQ2"
+ "SGELQF"
+ "SGEQR2"
+ "SGEQRF"
+ "SGESDD"
+ "SGESV "
+ "SGESVD"
+ "SGETRS"
+ "SHSEQR"
+ "SLAQR0"
+ "SLAQR3"
+ "SLAQR4"
+ "SLASD0"
+ "SLASD1"
+ "SLASD2"
+ "SLASD3"
+ "SLASD6"
+ "SLASD7"
+ "SLASD8"
+ "SLASDA"
+ "SLASDQ"
+ "SLASR "
+ "SORG2L"
+ "SORG2R"
+ "SORGBR"
+ "SORGHR"
+ "SORGL2"
+ "SORGLQ"
+ "SORGQL"
+ "SORGQR"
+ "SORGTR"
+ "SORM2R"
+ "SORMBR"
+ "SORMHR"
+ "SORML2"
+ "SORMLQ"
+ "SORMQR"
+ "SPOSV "
+ "SPOTRS"
+ "SSTEQR"
+ "SSTERF"
+ "SSYCONV"
+ "SSYEV "
+ "SSYSV "
+ "SSYTD2"
+ "SSYTF2"
+ "SSYTRD"
+ "SSYTRF"
+ "SSYTRS"
+ "SSYTRS2"
+ "STREVC"
+ "STREVC3"
+ "STREXC"
+ "STRTRS"
+ "SV"
+ "SafMin"
+ "Trans"
+ "UNIT"
+ "Y"
+ "vector"

```
