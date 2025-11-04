## RemoteXPC

> `/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC`

```diff

-3089.42.1.0.0
-  __TEXT.__text: 0xf774
-  __TEXT.__auth_stubs: 0xa60
+3089.60.3.0.0
+  __TEXT.__text: 0xf780
+  __TEXT.__auth_stubs: 0xa70
   __TEXT.__objc_methlist: 0x2ac
   __TEXT.__const: 0xa0
   __TEXT.__gcc_except_tab: 0x318

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x540
+  __AUTH_CONST.__auth_got: 0x548
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__objc_const: 0xf88
   __DATA.__objc_ivar: 0x12c

   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6982B79A-DA0A-3FB8-BCA2-09082C0D96E4
+  UUID: 5FF15235-2A4F-365E-AC07-5139DA330B32
   Functions: 363
-  Symbols:   1173
+  Symbols:   1174
   CStrings:  456
 
Symbols:
+ _nw_protocol_http2_transport_parameters_set_tunnel_teardown_delay
Functions:
~ _xpc_remote_connection_setup_nw_parameters : 356 -> 368

```
