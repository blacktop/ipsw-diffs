## libcorecrypto_noasm.dylib

> `/usr/lib/system/libcorecrypto_noasm.dylib`

```diff

-1922.80.3.0.0
-  __TEXT.__text: 0x7b7e8
+1922.80.7.0.0
+  __TEXT.__text: 0x7bb08
   __TEXT.__auth_stubs: 0x230
   __TEXT.__const: 0x1df88
-  __TEXT.__cstring: 0x5f4d
+  __TEXT.__cstring: 0x5f92
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
   __TEXT.__unwind_info: 0x1a98
   __TEXT.__eh_frame: 0x3a0
   __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0x2208
+  __DATA_CONST.__const: 0x21a8
   __AUTH_CONST.__auth_got: 0x118
   __AUTH_CONST.__const: 0x1820
   __AUTH.__data: 0xb8

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: C3240CCD-05E3-39E4-8F16-BC5998F50217
+  UUID: 0A0ED533-B4CE-3EE2-BBA2-365D84FC51E3
   Functions: 2313
   Symbols:   4120
-  CStrings:  545
+  CStrings:  549
 
Functions:
~ _fipspost_post_indicator : 10524 -> 11316
~ _ccrsa_decrypt_oaep_blinded_ws : 304 -> 312
CStrings:
+ "cccmac_one_shot_generate"
+ "cccmac_one_shot_verify"
+ "ccrng"
+ "ccrng_generate"

```
