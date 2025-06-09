## iOSScreenSharing

> `/System/Library/PrivateFrameworks/iOSScreenSharing.framework/iOSScreenSharing`

```diff

-105.8.0.0.0
-  __TEXT.__text: 0x11bc
-  __TEXT.__auth_stubs: 0x2b0
-  __TEXT.__objc_methlist: 0x230
+112.0.0.0.0
+  __TEXT.__text: 0x102c
+  __TEXT.__auth_stubs: 0x290
+  __TEXT.__objc_methlist: 0x244
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__cstring: 0x1af
-  __TEXT.__oslogstring: 0x1d6
-  __TEXT.__unwind_info: 0xb0
+  __TEXT.__cstring: 0x199
+  __TEXT.__oslogstring: 0x211
+  __TEXT.__unwind_info: 0xa8
   __TEXT.__objc_classname: 0x66
-  __TEXT.__objc_methname: 0x51f
+  __TEXT.__objc_methname: 0x4f2
   __TEXT.__objc_methtype: 0x15f
-  __TEXT.__objc_stubs: 0x480
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__objc_stubs: 0x400
+  __DATA_CONST.__got: 0x98
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x218
+  __DATA_CONST.__objc_selrefs: 0x200
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x168
+  __AUTH_CONST.__auth_got: 0x158
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x1c0
-  __AUTH_CONST.__objc_const: 0x2f0
+  __AUTH_CONST.__cfstring: 0x1a0
+  __AUTH_CONST.__objc_const: 0x2f8
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x180

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5BDC2FA4-120E-3494-98FD-BFC19164BBB5
+  UUID: 5BB5E84A-4DAD-38BC-93DF-D897B27DAB27
   Functions: 24
-  Symbols:   194
-  CStrings:  151
+  Symbols:   187
+  CStrings:  148
 
Symbols:
+ -[ViewServiceHelper requestUserInfo]
+ ___SS_SendStatusBarTapToScreenSharingServer_block_invoke.51
+ ___block_literal_global.104
+ ___block_literal_global.107
+ _objc_msgSend$sendSessionInfoToClient
- ___44-[ViewServiceHelper sendSessionInfoToClient]_block_invoke
- ___SS_SendStatusBarTapToScreenSharingServer_block_invoke_2
- ___block_literal_global.102
- ___block_literal_global.105
- __dispatch_main_q
- _objc_msgSend$lastObject
- _objc_msgSend$objectForKey:
- _objc_msgSend$remoteObjectProxy
- _objc_msgSend$setObject:forKey:
- _objc_msgSend$setUserInfo:
- _objc_opt_new
- _objc_release_x26
Functions:
~ ___SS_SendStatusBarTapToScreenSharingServer_block_invoke : 12 -> 116
~ -[ViewServiceHelper listener:shouldAcceptNewConnection:] : 1080 -> 1212
~ -[ViewServiceHelper sendSessionInfoToClient] -> -[ViewServiceHelper requestUserInfo] : 272 -> 132
~ ___44-[ViewServiceHelper sendSessionInfoToClient]_block_invoke -> -[ViewServiceHelper sendSessionInfoToClient] : 544 -> 48
CStrings:
+ "does not have entitlement"
+ "has entitlement"
+ "helperToolConnection invalidated xpc connection"
+ "iOS view service doesn't support ViewServiceBackChannelProtocol"
+ "requestUserInfo"
- "Sending session info to client"
- "isAppleSupportRequest"
- "lastObject"
- "objectForKey:"
- "remoteObjectProxy"
- "setObject:forKey:"
- "viewServerHelper delegate does not support sessionState message"

```
