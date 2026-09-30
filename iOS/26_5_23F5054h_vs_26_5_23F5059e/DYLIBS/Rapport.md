## Rapport

> `/System/Library/PrivateFrameworks/Rapport.framework/Rapport`

```diff

-716.600.2.0.0
-  __TEXT.__text: 0xa2b28
+716.600.13.0.0
+  __TEXT.__text: 0xa2fe0
   __TEXT.__auth_stubs: 0x1e00
-  __TEXT.__objc_methlist: 0x8fbc
+  __TEXT.__objc_methlist: 0x8fc4
   __TEXT.__const: 0x3ad8
-  __TEXT.__cstring: 0x1538c
+  __TEXT.__cstring: 0x154ac
   __TEXT.__gcc_except_tab: 0x1734
   __TEXT.__oslogstring: 0x85d
   __TEXT.__swift5_typeref: 0x7e3

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2b30
+  __TEXT.__unwind_info: 0x2b38
   __TEXT.__eh_frame: 0x8c8
   __TEXT.__objc_classname: 0xbf1
-  __TEXT.__objc_methname: 0x11373
+  __TEXT.__objc_methname: 0x113a3
   __TEXT.__objc_methtype: 0x2d94
-  __TEXT.__objc_stubs: 0x9320
+  __TEXT.__objc_stubs: 0x9360
   __DATA_CONST.__got: 0x440
   __DATA_CONST.__const: 0x2720
   __DATA_CONST.__objc_classlist: 0x2a8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b58
+  __DATA_CONST.__objc_selrefs: 0x3b68
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0xb0
   __AUTH_CONST.__auth_got: 0xf10
   __AUTH_CONST.__const: 0x13d0
-  __AUTH_CONST.__cfstring: 0x5260
+  __AUTH_CONST.__cfstring: 0x52a0
   __AUTH_CONST.__objc_const: 0x10a90
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FF5B8667-FEDB-3119-AA06-4E14F999BCE6
-  Functions: 4674
-  Symbols:   12533
-  CStrings:  7139
+  UUID: 15B79079-B48B-3560-A2CE-D27CD3138186
+  Functions: 4675
+  Symbols:   12537
+  CStrings:  7151
 
Symbols:
+ -[RPConnection logConnectionInformation:options:]
+ ___88-[RPConnection _sendEncryptedRequestID:request:xpcID:options:sendEntry:responseHandler:]_block_invoke.430
+ ___block_literal_global.1397
+ ___block_literal_global.1415
+ _objc_msgSend$fixedPIN
+ _objc_msgSend$logConnectionInformation:options:
- ___88-[RPConnection _sendEncryptedRequestID:request:xpcID:options:sendEntry:responseHandler:]_block_invoke.427
- ___block_literal_global.1384
- ___block_literal_global.1402
Functions:
~ -[RPConnection _clientPairSetupCompleted:] : 532 -> 552
~ -[RPConnection _clientPairVerifyCompleted:] : 1804 -> 1824
~ -[RPConnection _serverPairSetupCompleted:] : 572 -> 592
~ -[RPConnection _serverPairVerifyCompleted:] : 1932 -> 1952
~ -[RPConnection _receivedSystemInfo:xid:] : 4756 -> 4776
~ -[RPConnection _systeminfo] : 2544 -> 2564
~ ___44-[RPConnection _configureForSessionPairing:]_block_invoke_3 : 276 -> 296
+ -[RPConnection logConnectionInformation:options:]
CStrings:
+ "%@ Using IP transport over wireless or wired ethernet"
+ "%@ Using P2P transport over BLE"
+ "%@ Using P2P transport over WiFi"
+ "%@ Using unknown transport"
+ "-[RPConnection logConnectionInformation:options:]"
+ "Received msgID '%@' from %@ with %s\n"
+ "Received msgID '%@', XID 0x%X, %d keys, from %@\n"
+ "SystemInfo"
+ "fixedPIN"
+ "logConnectionInformation:options:"

```
