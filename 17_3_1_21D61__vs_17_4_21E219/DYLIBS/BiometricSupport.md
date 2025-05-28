## BiometricSupport

> `/System/Library/PrivateFrameworks/BiometricSupport.framework/BiometricSupport`

```diff

-460.60.4.0.0
-  __TEXT.__text: 0x4c72c
-  __TEXT.__auth_stubs: 0xf80
+471.100.9.0.0
+  __TEXT.__text: 0x4c12c
+  __TEXT.__auth_stubs: 0xf50
   __TEXT.__objc_methlist: 0x1c90
-  __TEXT.__const: 0xf84
-  __TEXT.__cstring: 0x3e51
+  __TEXT.__const: 0xf94
+  __TEXT.__cstring: 0x3e52
   __TEXT.__oslogstring: 0x2eab
   __TEXT.__gcc_except_tab: 0x9e8
-  __TEXT.__unwind_info: 0xbe4
+  __TEXT.__unwind_info: 0xbc8
   __TEXT.__objc_classname: 0x278
-  __TEXT.__objc_methname: 0x5b3b
+  __TEXT.__objc_methname: 0x5b4b
   __TEXT.__objc_methtype: 0x1429
   __TEXT.__objc_stubs: 0x4420
   __DATA_CONST.__got: 0x158

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x3700
   __DATA_CONST.__objc_selrefs: 0x1740
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x198
+  __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__cfstring: 0x1980
   __AUTH_CONST.__objc_const: 0x6c0
   __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__auth_got: 0x7d0
+  __AUTH_CONST.__auth_got: 0x7b8
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x198
-  __DATA.__objc_superrefs: 0x88
   __DATA.__objc_ivar: 0x200
   __DATA.__data: 0x9f0
   __DATA.__common: 0x28

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1027
-  Symbols:   3802
-  CStrings:  2118
+  Functions: 1011
+  Symbols:   3768
+  CStrings:  2119
 
Symbols:
+ _AKS_FV_MDM_RECOVERY_KEY_UUID
+ ___60-[BiometricKitXPCServer listener:shouldAcceptNewConnection:]_block_invoke.602
+ _calloc
+ _firebloom_ccpbkdf2_hmac
+ _malloc
- ___60-[BiometricKitXPCServer listener:shouldAcceptNewConnection:]_block_invoke.601
- _aks_remote_peer_register
- _cccurve25519_make_key_pair
- _ccder_encode_body
- _ccder_encode_tl
- _cced25519_make_key_pair
- _decode_fv_data
- _decode_fv_key
- _decode_fv_params
- _decode_implicit_raw_octet_string
- _decode_implicit_raw_octet_string_copy
- _decode_implicit_uint64
- _der_decode_any
- _encode_fv_data
- _encode_fv_key
- _encode_fv_params
- _firebloom_cccurve25519
- _firebloom_curve25519_make_key_pair
- _firebloom_ed25519_make_key_pair
- _firebloom_get_sized_copy
- _firebloom_get_sized_len
- _firebloom_ipc_copy_out
- _malloc_type_malloc
CStrings:
+ "AssertMacros: %s, %s file: %s, line: %d, value: %lld\n"
+ "T@\"NSString\",?,R,C"
- "AssertMacros: %s, %s file: %s, line: %d, value: %ld\n"

```
