## libcorecrypto.dylib

> `/usr/lib/system/libcorecrypto.dylib`

```diff

-1922.40.11.0.0
-  __TEXT.__text: 0x856c8
+1922.40.14.0.0
+  __TEXT.__text: 0x85668
   __TEXT.__auth_stubs: 0x230
   __TEXT.__cstring: 0x5f4d
   __TEXT.__const: 0x1e338

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: E396CF3B-33DF-3A6A-B141-CECBB5AF864B
+  UUID: A83044D4-DEED-3545-9F84-5770D15EE8AE
   Functions: 2434
   Symbols:   4382
   CStrings:  545
Symbols:
+ _ccmldsa_sample_rej_uniform_eta2
+ _ccmldsa_sample_rej_uniform_eta4
- _ccmldsa_sample_rej_coeffs_eta2
- _ccmldsa_sample_rej_coeffs_eta4
Functions:
~ _ccmldsa_sample_rej_coeffs_eta2 -> _ccmldsa_sample_rej_uniform_eta2 : 264 -> 152
~ _ccmldsa_sample_rej_coeffs_eta4 -> _ccmldsa_sample_rej_uniform_eta4 : 228 -> 116
~ _ccmldsa_sample_rej_bounded_poly : 248 -> 312
~ _ccmldsa_sample_in_ball : 552 -> 612
~ _ccz_read_radix : 560 -> 548
~ _ccmldsa_poly_make_hint : 80 -> 96

```
