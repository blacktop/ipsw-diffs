## libcorecrypto_trace.dylib

> `/usr/lib/system/libcorecrypto_trace.dylib`

```diff

-1638.100.62.0.0
-  __TEXT.__text: 0x88500
+1638.140.6.0.0
+  __TEXT.__text: 0x88b38
   __TEXT.__auth_stubs: 0x220
-  __TEXT.__const: 0x19274
-  __TEXT.__cstring: 0x56aa
+  __TEXT.__const: 0x19334
+  __TEXT.__cstring: 0x56c2
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x1934
+  __TEXT.__unwind_info: 0x1944
   __TEXT.__eh_frame: 0x220
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0xf90
   __AUTH_CONST.__const: 0x1940
   __AUTH_CONST.__auth_got: 0x110
   __AUTH.__data: 0xb8
-  __DATA.__data: 0x6b70
+  __DATA.__data: 0x6748
   __DATA.__bss: 0x2058
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 6EEDAA96-9E68-36C3-A1DE-636AB1BF1DBB
-  Functions: 2116
-  Symbols:   3646
-  CStrings:  649
+  UUID: 1A8F8A1C-82C7-3ED1-9E98-496368E1CDBF
+  Functions: 2121
+  Symbols:   3654
+  CStrings:  650
 
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
