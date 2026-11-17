## com.apple.driver.AppleAVD

> `com.apple.driver.AppleAVD`

```diff

-995.0.0.0.0
-  __TEXT.__os_log: 0x1d318
+996.0.0.0.0
+  __TEXT.__os_log: 0x1d452
   __TEXT.__cstring: 0x8588
   __TEXT.__const: 0xf53cc
-  __TEXT_EXEC.__text: 0x677cc
+  __TEXT_EXEC.__text: 0x67a64
   __TEXT_EXEC.__auth_stubs: 0x6f0
   __DATA.__data: 0x1334
   __DATA.__common: 0x78

   __DATA_CONST.__auth_ptr: 0x10
   Functions: 2328
   Symbols:   0
-  CStrings:  1794
+  CStrings:  1796
 
Functions:
~ __ZN10CAvdApComm14validateFieldsEPhj : 324 -> 464
~ __ZN13PriorityQueue24insertDecodeFrameCommandEP8sPQEntry : 604 -> 672
~ sub_fffffe0008819688 -> sub_fffffe00087b9878 : 716 -> 832
~ sub_fffffe000881a3c4 -> sub_fffffe00087ba628 : 400 -> 508
~ sub_fffffe0008823378 -> sub_fffffe00087c3648 : 716 -> 832
~ __ZN15CAvdApCommViola18patchSliceDataSizeEPh28_DecryptSliceDataSizePatcherj : 716 -> 832
CStrings:
+ "AppleAVD: ERROR: %s(): Invalid workOffset=%u, numWorks=%u\n"
+ "AppleAVD: ERROR: %s(): Validation failed - buffer codec %u, session codec %u\n"
```
