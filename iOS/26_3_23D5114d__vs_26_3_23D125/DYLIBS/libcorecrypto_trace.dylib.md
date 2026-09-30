## libcorecrypto_trace.dylib

> `/usr/lib/system/libcorecrypto_trace.dylib`

```diff

-1922.80.3.0.0
-  __TEXT.__text: 0x86688
+1922.80.7.0.0
+  __TEXT.__text: 0x86988
   __TEXT.__auth_stubs: 0x230
-  __TEXT.__cstring: 0x6284
+  __TEXT.__cstring: 0x62c9
   __TEXT.__const: 0x1e338
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
   __TEXT.__unwind_info: 0x1ae8
   __TEXT.__eh_frame: 0x350
   __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0x2208
+  __DATA_CONST.__const: 0x21a8
   __AUTH_CONST.__auth_got: 0x118
   __AUTH_CONST.__const: 0x1ea8
   __AUTH.__data: 0xd0

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 826D0D74-0D35-3032-8E49-EE53BEE41F6B
+  UUID: D09805BB-D768-3904-922F-711778CCA8E1
   Functions: 2441
   Symbols:   4402
-  CStrings:  578
+  CStrings:  582
 
Functions:
~ _fipspost_post_indicator : 10524 -> 11316
~ _ccder_decode_rsa_pub_n : 100 -> 92
~ _ccn_addmul1_asm : 256 -> 240
CStrings:
+ "cccmac_one_shot_generate"
+ "cccmac_one_shot_verify"
+ "ccrng"
+ "ccrng_generate"

```
