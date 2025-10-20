## libcorecrypto_noasm.dylib

> `/usr/lib/system/libcorecrypto_noasm.dylib`

```diff

-1922.40.11.0.0
-  __TEXT.__text: 0x7b734
+1922.40.14.0.0
+  __TEXT.__text: 0x7b6e4
   __TEXT.__auth_stubs: 0x230
   __TEXT.__const: 0x1df88
   __TEXT.__cstring: 0x5f4d

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 503D0D79-90CF-3CC8-B9CD-5B9084626789
+  UUID: 90ED8E09-D640-31D7-9A67-A0369B1016C7
   Functions: 2313
   Symbols:   4120
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
~ _ccrsa_decrypt_oaep_blinded_ws : 308 -> 312
~ _ccmldsa_poly_make_hint : 80 -> 96

```
