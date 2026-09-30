## libboringssl.dylib

> `/usr/lib/libboringssl.dylib`

```diff

-486.120.2.0.0
-  __TEXT.__text: 0x9df44
-  __TEXT.__auth_stubs: 0x1960
+486.122.1.0.0
+  __TEXT.__text: 0x9e220
+  __TEXT.__auth_stubs: 0x1970
   __TEXT.__objc_methlist: 0x1dc
-  __TEXT.__cstring: 0x105de
+  __TEXT.__cstring: 0x10630
   __TEXT.__const: 0xfef8
   __TEXT.__oslogstring: 0x577e
-  __TEXT.__gcc_except_tab: 0x2900
-  __TEXT.__unwind_info: 0x2488
+  __TEXT.__gcc_except_tab: 0x28e8
+  __TEXT.__unwind_info: 0x2480
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_classname: 0x241
   __TEXT.__objc_methname: 0xe76

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0xcc8
+  __AUTH_CONST.__auth_got: 0xcd0
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x18c8
   __AUTH_CONST.__cfstring: 0xe0

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3117
-  Symbols:   7314
-  CStrings:  3620
+  Functions: 3121
+  Symbols:   7324
+  CStrings:  3623
 
Symbols:
+ _CFSetApplyFunction
+ __ZN4bssl22tls13_client_handshakeEPNS_13SSL_HANDSHAKEE.cold.6
+ __ZN4bssl22tls13_server_handshakeEPNS_13SSL_HANDSHAKEE.cold.3
+ _boringssl_context_info_handler.cold.2
+ _nw_protocol_boringssl_returned_raw_string_pointer_deallocate
- GCC_except_table146
CStrings:
+ "!hs->pake_participant"
+ "do_send_hello_retry_request"
+ "hs->pake_participant == nullptr"

```
