## libcorecrypto.dylib

> `/usr/lib/system/libcorecrypto.dylib`

```diff

-1922.80.3.0.0
-  __TEXT.__text: 0x85ab0
+1922.80.7.0.0
+  __TEXT.__text: 0x85dd0
   __TEXT.__auth_stubs: 0x230
-  __TEXT.__cstring: 0x5f4d
+  __TEXT.__cstring: 0x5f92
   __TEXT.__const: 0x1e338
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
   __TEXT.__unwind_info: 0x1978
   __TEXT.__eh_frame: 0x350
   __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0x2208
+  __DATA_CONST.__const: 0x21a8
   __AUTH_CONST.__auth_got: 0x118
   __AUTH_CONST.__const: 0x1ea8
   __AUTH.__data: 0xb8

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 93424408-5B86-3E70-8921-312F27392A89
+  UUID: 750CB60B-7AA1-32AE-AC77-C7517F9EA49B
   Functions: 2435
   Symbols:   4382
-  CStrings:  545
+  CStrings:  549
 
Functions:
~ _fipspost_post_indicator : 10524 -> 11316
~ _ccec_projectify : 260 -> 268
CStrings:
+ "cccmac_one_shot_generate"
+ "cccmac_one_shot_verify"
+ "ccrng"
+ "ccrng_generate"

```
