## libcorecrypto.dylib

> `/usr/lib/system/libcorecrypto.dylib`

```diff

-1638.100.62.0.0
-  __TEXT.__text: 0x879c4
+1638.140.6.0.0
+  __TEXT.__text: 0x88008
   __TEXT.__auth_stubs: 0x220
-  __TEXT.__const: 0x19274
-  __TEXT.__cstring: 0x53aa
+  __TEXT.__const: 0x19334
+  __TEXT.__cstring: 0x53c2
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x1988
+  __TEXT.__unwind_info: 0x1998
   __TEXT.__eh_frame: 0x220
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0xf90

   __AUTH_CONST.__const: 0x1940
   __AUTH_CONST.__auth_got: 0x110
   __AUTH.__data: 0xa0
-  __DATA.__data: 0x6c90
+  __DATA.__data: 0x6868
   __DATA.__bss: 0xd58
   __DATA.__common: 0x8
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  Functions: 2109
-  Symbols:   3626
-  CStrings:  618
+  Functions: 2114
+  Symbols:   3634
+  CStrings:  619
 
Symbols:
+ _ccec_sign_composite_msg_ws
+ _ccec_verify_composite_digest_ws
+ _ccec_verify_composite_msg_ws
+ _ccrsa_sign_pkcs1v15_msg_blinded_ws
+ _ccrsa_verify_pkcs1v15_msg_ws
- _ccdh_gp_fipspost_2048
CStrings:
+ "ccdes3_ecb_decrypt_mode"

```
