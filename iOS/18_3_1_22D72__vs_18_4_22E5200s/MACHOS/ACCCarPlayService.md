## ACCCarPlayService

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCCarPlayService.xpc/ACCCarPlayService`

```diff

-1025.82.1.0.0
-  __TEXT.__text: 0x3c40
+1043.100.28.0.0
+  __TEXT.__text: 0x3cd8
   __TEXT.__auth_stubs: 0x380
   __TEXT.__objc_stubs: 0x340
-  __TEXT.__objc_methlist: 0x11c
-  __TEXT.__cstring: 0x6ea
+  __TEXT.__objc_methlist: 0x29c
+  __TEXT.__cstring: 0x737
   __TEXT.__const: 0x70
   __TEXT.__oslogstring: 0x7ac
   __TEXT.__objc_classname: 0x69
   __TEXT.__objc_methname: 0x5b0
   __TEXT.__objc_methtype: 0x286
-  __TEXT.__gcc_except_tab: 0x9c
+  __TEXT.__gcc_except_tab: 0x90
   __TEXT.__unwind_info: 0x158
   __DATA_CONST.__auth_got: 0x1d0
   __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x4b8
-  __DATA_CONST.__cfstring: 0x260
+  __DATA_CONST.__const: 0x4e0
+  __DATA_CONST.__cfstring: 0x2c0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x838
-  __DATA.__objc_selrefs: 0x110
+  __DATA.__objc_const: 0x578
+  __DATA.__objc_selrefs: 0x1b0
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x1c8

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 82
-  Symbols:   764
-  CStrings:  184
+  Functions: 87
+  Symbols:   791
+  CStrings:  187
 
Symbols:
+ -[ACCCarPlayService carPlayAppLinksStateForCertSerial:withReply:].cold.4
+ -[ACCCarPlayService carPlayStartSessionForConnectionID:properties:withReply:].cold.2
+ -[ACCCarPlayService filterMatchingDigitalCarKeys:forAccessory:withReply:].cold.7
+ -[ACCCarPlayService isCarPlayPairedWithCertSerial:withReply:].cold.4
+ -[ACCCarPlayService isWirelessCarPlayAllowedForCertSerial:withReply:].cold.4
+ __block_literal_global.44
+ __block_literal_global.47
+ __block_literal_global.55
+ __block_literal_global.58
+ _iAPBytesReceived
+ _iAPCarPlayEndpointCreated
+ _iAPCarPlayStartSessionReceived
- __block_literal_global.35
- __block_literal_global.46
- __block_literal_global.49
CStrings:
+ "iAP CarPlay Start Session Received"
+ "iAP2 Bytes Received"
+ "iAP2 Endpoint Created"

```
