## libcorecrypto_trace.dylib

> `/usr/lib/system/libcorecrypto_trace.dylib`

```diff

-1922.40.11.0.0
-  __TEXT.__text: 0x86294
+1922.40.14.0.0
+  __TEXT.__text: 0x86254
   __TEXT.__auth_stubs: 0x230
   __TEXT.__cstring: 0x6284
   __TEXT.__const: 0x1e338

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 5C934550-67A6-3415-A273-61E24AE6A6FA
+  UUID: 6A657EF2-9A54-3E92-A33C-B2E3A10B2C73
   Functions: 2441
   Symbols:   4402
   CStrings:  578
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
~ sub_2988d3b78 -> sub_299cb2b14 : 8 -> 12
~ _OUTLINED_FUNCTION_1 : 36 -> 68
~ _ccmldsa_poly_make_hint : 80 -> 96
~ _cczp_sub : 276 -> 260

```
