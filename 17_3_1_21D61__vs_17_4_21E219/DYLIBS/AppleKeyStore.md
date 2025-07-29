## AppleKeyStore

> `/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore`

```diff

-1555.80.3.0.0
-  __TEXT.__text: 0x2980c
-  __TEXT.__auth_stubs: 0xd20
-  __TEXT.__const: 0x27b0
+1655.102.1.0.0
+  __TEXT.__text: 0x290fc
+  __TEXT.__auth_stubs: 0xce0
+  __TEXT.__const: 0x28c1
   __TEXT.__cstring: 0x21c0
   __TEXT.__oslogstring: 0xd3
-  __TEXT.__unwind_info: 0x8a0
+  __TEXT.__unwind_info: 0x88c
   __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x30f8
+  __DATA_CONST.__const: 0x32c8
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__cfstring: 0x3a0
-  __AUTH_CONST.__auth_got: 0x690
+  __AUTH_CONST.__auth_got: 0x670
   __DATA.__data: 0x758
   __DATA.__bss: 0x68
   __DATA.__common: 0x28

   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
-  UUID: 8140F203-E355-3F5B-A37C-F0F9CE12D6BC
-  Functions: 728
-  Symbols:   2044
+  UUID: A36B787A-2D99-386F-9FBA-709A52EC001E
+  Functions: 718
+  Symbols:   2032
   CStrings:  399
 
Symbols:
+ _AKS_FV_MDM_RECOVERY_KEY_UUID
+ _BASepAppRoot
+ _BASepAppRootPublicKey
+ _BASepAppRootSKID
+ _BASepAppRootSPKI
+ _CTEvaluateBAA
+ _CTEvaluateBAASepApp
+ _CTGetBAARootType
+ _CTGetBAASubCAType
+ _MFi4RootSKID
+ _X509ExtensionParseCertifiedChipIntermediate
+ _X509PolicyBAASepApp
+ __baa_sep_app_root_public_key
+ __baa_sep_app_root_skid
+ __baa_sep_app_root_spki
+ __baa_system_root_skid
+ __baa_user_root_skid
+ __mfi4_root_skid
+ _calloc
+ _firebloom_ccpbkdf2_hmac
+ _malloc
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
- _malloc_type_calloc
- _malloc_type_malloc

```
