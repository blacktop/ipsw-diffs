## libboringssl.dylib

> `/usr/lib/libboringssl.dylib`

```diff

-532.80.1.0.0
-  __TEXT.__text: 0xa11d4
-  __TEXT.__auth_stubs: 0x1e70
+532.80.2.0.0
+  __TEXT.__text: 0xa1b1c
+  __TEXT.__auth_stubs: 0x1e80
   __TEXT.__objc_methlist: 0x1dc
-  __TEXT.__cstring: 0x10848
+  __TEXT.__cstring: 0x10897
   __TEXT.__const: 0x10018
-  __TEXT.__oslogstring: 0x5de7
+  __TEXT.__oslogstring: 0x5e23
   __TEXT.__gcc_except_tab: 0x2948
-  __TEXT.__unwind_info: 0x24e0
+  __TEXT.__unwind_info: 0x24f0
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_classname: 0x241
-  __TEXT.__objc_methname: 0xecf
+  __TEXT.__objc_methname: 0xf00
   __TEXT.__objc_methtype: 0x62b
   __TEXT.__objc_stubs: 0xa0
-  __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__got: 0xf8
   __DATA_CONST.__const: 0xb890
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xf50
+  __AUTH_CONST.__auth_got: 0xf58
   __AUTH_CONST.__const: 0x1908
   __AUTH_CONST.__cfstring: 0xe0
-  __AUTH_CONST.__objc_const: 0x21a8
+  __AUTH_CONST.__objc_const: 0x21e8
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x308
-  __DATA.__data: 0xd10
+  __DATA.__objc_ivar: 0x310
+  __DATA.__data: 0xd20
   __DATA.__bss: 0x540
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0x210

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 88AE48A8-6DE4-3547-9EF6-BF3D55EB06CC
-  Functions: 3154
-  Symbols:   7471
-  CStrings:  3667
+  UUID: BA0B5F5D-477E-3B0A-B7B2-883182FC46D2
+  Functions: 3158
+  Symbols:   7489
+  CStrings:  3673
 
Symbols:
+ GCC_except_table125
+ GCC_except_table158
+ _OBJC_IVAR_$_boringssl_concrete_boringssl_ctx.certificate_signature_algorithm
+ _OBJC_IVAR_$_boringssl_concrete_boringssl_ctx.old_ats_enforced
+ _SecCertificateCopySignatureAlgorithm
+ _TLS_METRIC_CERTIFICATE_SIGNATURE_ALGORITHM
+ _TLS_METRIC_LEGACY_ATS_PFS
+ ___block_literal_global.88
+ ___boringssl_context_certificate_request_callback_block_invoke.215
+ ___boringssl_context_evaluate_trust_async_external_block_invoke.206
+ ___boringssl_context_evaluate_trust_async_internal_block_invoke.198
+ ___boringssl_context_evaluate_trust_async_internal_block_invoke.202
+ ___boringssl_context_new_session_handler_block_invoke.240
+ ___boringssl_context_update_encryption_level_block_invoke.221
+ _boringssl_context_get_old_ats_enforced
+ _boringssl_context_get_peer_leaf_cert_signature_algorithm
+ _boringssl_context_set_old_ats_enforced
+ _boringssl_helper_SecKeyAlgorithm_to_metrics_reported_value
+ _kSecKeyAlgorithmECDSASignatureMessageX962SHA224
+ _kSecKeyAlgorithmECDSASignatureMessageX962SHA512
+ _kSecKeyAlgorithmEdDSASignatureMessageCurve25519SHA512
+ _kSecKeyAlgorithmEdDSASignatureMessageCurve448SHAKE256
+ _kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA224
- GCC_except_table121
- GCC_except_table154
- ___block_literal_global.84
- ___boringssl_context_certificate_request_callback_block_invoke.213
- ___boringssl_context_evaluate_trust_async_external_block_invoke.204
- ___boringssl_context_evaluate_trust_async_internal_block_invoke.196
- ___boringssl_context_evaluate_trust_async_internal_block_invoke.200
- ___boringssl_context_new_session_handler_block_invoke.238
- ___boringssl_context_update_encryption_level_block_invoke.217
CStrings:
+ "%{public}s(%d) %{public}s[%p] Certificate signature alg: %d"
+ "boringssl_context_set_old_ats_enforced"
+ "cert_signature_algorithm"
+ "certificate_signature_algorithm"
+ "legacy_ats_pfs"
+ "old_ats_enforced"

```
