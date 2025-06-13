## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1262.600.61.2.9
-  __TEXT.__text: 0x846f0
-  __TEXT.__auth_stubs: 0xd70
-  __TEXT.__objc_methlist: 0x2064
-  __TEXT.__const: 0x1a8
-  __TEXT.__gcc_except_tab: 0x7d1c
-  __TEXT.__cstring: 0x2afc
-  __TEXT.__oslogstring: 0x13346
-  __TEXT.__unwind_info: 0x1bec
-  __TEXT.__objc_classname: 0x499
-  __TEXT.__objc_methname: 0xee26
-  __TEXT.__objc_methtype: 0x251d
-  __TEXT.__objc_stubs: 0xa6e0
+1262.700.71.2.1
+  __TEXT.__text: 0x85070
+  __TEXT.__auth_stubs: 0xd80
+  __TEXT.__objc_methlist: 0x20e4
+  __TEXT.__const: 0x1b0
+  __TEXT.__gcc_except_tab: 0x7de0
+  __TEXT.__cstring: 0x2b35
+  __TEXT.__oslogstring: 0x13441
+  __TEXT.__unwind_info: 0x1c2c
+  __TEXT.__objc_classname: 0x4b4
+  __TEXT.__objc_methname: 0xeff2
+  __TEXT.__objc_methtype: 0x2546
+  __TEXT.__objc_stubs: 0xa800
   __DATA_CONST.__got: 0x8a8
   __DATA_CONST.__const: 0x1fe0
-  __DATA_CONST.__objc_classlist: 0xc0
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x26e8
-  __DATA_CONST.__objc_selrefs: 0x2d80
-  __DATA_CONST.__objc_classrefs: 0x428
-  __DATA_CONST.__objc_superrefs: 0x90
-  __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__objc_const: 0xa70
+  __DATA_CONST.__objc_const: 0x2828
+  __DATA_CONST.__objc_selrefs: 0x2de0
+  __DATA_CONST.__objc_classrefs: 0x430
+  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_arraydata: 0x28
+  __AUTH_CONST.__objc_const: 0xab8
   __AUTH_CONST.__const: 0x6c0
-  __AUTH_CONST.__cfstring: 0x3180
-  __AUTH_CONST.__objc_intobj: 0x2d0
+  __AUTH_CONST.__cfstring: 0x31e0
+  __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x6c8
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x1a8
+  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__auth_got: 0x6d0
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x1b4
   __DATA.__data: 0x3d8
   __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0x550

   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 156C0263-F8A4-3134-B6CC-7D9F682DF1BD
-  Functions: 1107
-  Symbols:   669
-  CStrings:  4336
+  UUID: 8A020575-21DC-3A06-9575-3AB5CADD9B7A
+  Functions: 1117
+  Symbols:   670
+  CStrings:  4370
 
Symbols:
+ __IMAllowSMSDowngradeRequests
CStrings:
+ "\x03\x1b"
+ "@\"MessageDowngradeController\""
+ "Downgrading %@ to SMS until %@"
+ "Incoming message %@ fromID %@ command %@"
+ "Invalid expiration date"
+ "Invalid preferred service type"
+ "MessageDowngradeController"
+ "No preferred service type"
+ "T@\"IDSService\",&,N,V_liteService"
+ "T@\"MessageDowngradeController\",R,N,V_downgradeController"
+ "Unknown command ID: %@"
+ "Unspecified preferred service, doing nothing"
+ "Upgrading %@ back to iMessage"
+ "_downgradeController"
+ "_expirationDateFromMessage:"
+ "_handleIncomingServiceUpdateMessage:fromID:context:"
+ "_liteService"
+ "_preferredServiceFromMessage:"
+ "clearDowngradeRequestForHandleID:"
+ "com.apple.madrid.lite"
+ "downgradeController"
+ "downgradeRequestedForHandleID:expirationDate:preferredService:"
+ "dp"
+ "eX"
+ "earlierDate:"
+ "liteService"
+ "originalCommand"
+ "q24@0:8@16"
+ "serviceSwitchRequestReceivedForChatWithIdentifier:"
+ "setLiteService:"
- "\x03\x1a"

```
