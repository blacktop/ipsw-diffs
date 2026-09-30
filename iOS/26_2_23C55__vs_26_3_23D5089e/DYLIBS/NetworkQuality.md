## NetworkQuality

> `/System/Library/PrivateFrameworks/NetworkQuality.framework/NetworkQuality`

```diff

-194.40.3.0.0
-  __TEXT.__text: 0x19440
-  __TEXT.__auth_stubs: 0xb80
+194.80.3.0.0
+  __TEXT.__text: 0x19498
+  __TEXT.__auth_stubs: 0xbb0
   __TEXT.__objc_methlist: 0x1734
   __TEXT.__const: 0x188
   __TEXT.__gcc_except_tab: 0x538

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x5d0
+  __AUTH_CONST.__auth_got: 0x5e8
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x19e0
   __AUTH_CONST.__objc_const: 0x37d0

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E662BDB5-D1CF-3CB7-BADE-D3457652BCA5
+  UUID: 861DBBAE-C73B-33D7-BCE7-1E6E650978D1
   Functions: 567
-  Symbols:   2334
+  Symbols:   2337
   CStrings:  1638
 
Symbols:
+ _nw_http3_create_options
+ _nw_protocol_stack_copy_transport_protocol
+ _nw_quic_stream_copy_shared_connection_options
Functions:
~ -[NetworkQualityHTTPServer HTTP3ParametersForServer] : 364 -> 352
~ ___34-[NetworkQualityHTTPServer start:]_block_invoke.20 : 180 -> 280

```
