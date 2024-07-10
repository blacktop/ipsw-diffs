## libcorecrypto.dylib

> `/usr/lib/system/libcorecrypto.dylib`

```diff

-1736.0.36.0.0
-  __TEXT.__text: 0x8113c
+1736.0.27.0.1
+  __TEXT.__text: 0x809c0
   __TEXT.__auth_stubs: 0x220
-  __TEXT.__cstring: 0x53ea
-  __TEXT.__const: 0x19008
+  __TEXT.__const: 0x19028
+  __TEXT.__cstring: 0x53c6
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x1628
+  __TEXT.__unwind_info: 0x1608
   __TEXT.__eh_frame: 0x2c0
   __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0xf30
+  __DATA_CONST.__const: 0xf20
   __AUTH_CONST.__auth_got: 0x110
   __AUTH_CONST.__auth_ptr: 0x1c8
-  __AUTH_CONST.__const: 0x1aa0
+  __AUTH_CONST.__const: 0x19c8
   __AUTH.__data: 0xb8
   __DATA.__data: 0x6740
-  __DATA.__bss: 0x1808
+  __DATA.__bss: 0x17e8
   __DATA.__common: 0x8
   __DATA_DIRTY.__bss: 0xd8
   - /usr/lib/system/libcompiler_rt.dylib

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  Functions: 2005
-  Symbols:   2449
-  CStrings:  619
+  Functions: 1996
+  Symbols:   2436
+  CStrings:  617
 
Symbols:
- _ccec_sign_composite_msg_ws
- _ccec_verify_composite_digest_ws
- _ccec_verify_composite_msg_ws
- _ccrsa_eme_pkcs1v15_decode_internal_ws
- _ccrsa_sign_pkcs1v15_msg_blinded_ws
- _ccrsa_verify_pkcs1v15_msg_ws
- _ccsha384_vng_arm_hw_compress
- _ccsha384_vng_arm_hw_di
- _ccsha512_256_vng_arm_hw_compress
- _ccsha512_256_vng_arm_hw_di
- _ccsha512_vng_arm_hw_compress
- _ccsha512_vng_arm_hw_di
- ccrsa_eme_pkcs1v15_decode.entropy
- ccrsa_eme_pkcs1v15_decode.entropy_init
CStrings:
- "SHA384_VNG_ARM_HW"
- "SHA512_VNG_ARM_HW"

```
