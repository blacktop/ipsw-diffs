## libboringssl.dylib

> `/usr/lib/libboringssl.dylib`

```diff

-532.102.3.0.0
-  __TEXT.__text: 0xa25f4
-  __TEXT.__auth_stubs: 0x1e60
+532.120.5.0.0
+  __TEXT.__text: 0xa262c
+  __TEXT.__auth_stubs: 0x1e50
   __TEXT.__objc_methlist: 0x1dc
   __TEXT.__cstring: 0x121e6
   __TEXT.__const: 0xff48
   __TEXT.__oslogstring: 0x67a3
-  __TEXT.__gcc_except_tab: 0x2af4
-  __TEXT.__unwind_info: 0x25e0
+  __TEXT.__gcc_except_tab: 0x2b0c
+  __TEXT.__unwind_info: 0x25e8
   __TEXT.__eh_frame: 0x130
-  __TEXT.__objc_classname: 0x241
+  __TEXT.__objc_classname: 0x245
   __TEXT.__objc_methname: 0xf8a
   __TEXT.__objc_methtype: 0x62b
   __TEXT.__objc_stubs: 0xa0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xf48
+  __AUTH_CONST.__auth_got: 0xf40
   __AUTH_CONST.__const: 0x1948
   __AUTH_CONST.__cfstring: 0xe0
   __AUTH_CONST.__objc_const: 0x22a8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 177A3DDB-FDA5-3075-8EE1-384B8B5E6C19
+  UUID: CA8BDF39-18F2-303A-8E22-D6ED67DC10ED
   Functions: 3266
-  Symbols:   7765
-  CStrings:  3738
+  Symbols:   7764
+  CStrings:  3739
 
Symbols:
+ ___block_descriptor_56_e8_32bs40r_e8_v12?0B8lu48l8s32l8r40l8
+ ___block_descriptor_64_e8_32s40bs_e8_v12?0B8ls32l8u56l8s40l8
+ ___block_descriptor_65_e8_32s40bs_e5_v8?0ls32l8u56l8s40l8
+ ___block_descriptor_80_e8_32s40s48bs56bs_e5_v8?0lu72l8s32l8s48l8s56l8s40l8
- _SecTrustSetExceptions
- ___block_descriptor_48_e8_32bs_e8_v12?0B8lu40l8s32l8
- ___block_descriptor_72_e8_32s40bs_e8_v12?0B8ls32l8u56l8s40l8
- ___block_descriptor_73_e8_32s40bs_e5_v8?0ls32l8u56l8s40l8
- ___block_descriptor_88_e8_32s40s48bs56bs_e5_v8?0lu72l8s32l8s48l8s56l8s40l8
Functions:
~ __ZN4bssl25tls13_process_certificateEPNS_13SSL_HANDSHAKEERKNS_10SSLMessageEb : 2832 -> 2796
~ _boringssl_context_evaluate_trust_async_external : 784 -> 780
~ ___boringssl_context_evaluate_trust_async_external_block_invoke : 820 -> 812
~ ___boringssl_context_evaluate_trust_async_external_block_invoke_2 : 204 -> 196
~ ___boringssl_context_evaluate_trust_async_external_block_invoke_3 : 5996 -> 6036
~ __ZN4bssl31tls13_add_certificate_in_bufferEPNS_13SSL_HANDSHAKEEbPPhPm : 1628 -> 1636
~ ___boringssl_context_evaluate_trust_async_external_block_invoke.211 : 32 -> 96
CStrings:
+ "0@`"

```
