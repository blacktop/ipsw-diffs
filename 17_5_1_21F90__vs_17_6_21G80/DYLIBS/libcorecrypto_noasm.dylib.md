## libcorecrypto_noasm.dylib

> `/usr/lib/system/libcorecrypto_noasm.dylib`

```diff

-1638.100.62.0.0
-  __TEXT.__text: 0x7e9a0
+1638.140.6.0.0
+  __TEXT.__text: 0x7efa4
   __TEXT.__auth_stubs: 0x220
-  __TEXT.__const: 0x18f54
-  __TEXT.__cstring: 0x53aa
+  __TEXT.__const: 0x19004
+  __TEXT.__cstring: 0x53c2
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x18a4
+  __TEXT.__unwind_info: 0x18b4
   __TEXT.__eh_frame: 0x270
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0xf90
   __AUTH_CONST.__const: 0x1400
   __AUTH_CONST.__auth_got: 0x110
   __AUTH.__data: 0xa0
-  __DATA.__data: 0x6b68
+  __DATA.__data: 0x6740
   __DATA.__bss: 0x19d0
   __DATA.__common: 0x8
   - /usr/lib/system/libcompiler_rt.dylib

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 40C879D3-08FB-397B-A1B3-8BCD4C87D5D3
-  Functions: 2001
-  Symbols:   3398
-  CStrings:  618
+  UUID: 5574198F-03CF-39E2-8F04-508CB72B62AF
+  Functions: 2006
+  Symbols:   3406
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
