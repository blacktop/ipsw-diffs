## MobileAccessoryUpdater

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/MobileAccessoryUpdater`

```diff

-1338.0.37.0.0
-  __TEXT.__text: 0x4b8c
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_methlist: 0xc7c
+1338.0.46.502.1
+  __TEXT.__text: 0x50f8
+  __TEXT.__auth_stubs: 0x530
+  __TEXT.__objc_methlist: 0xc84
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x68
-  __TEXT.__cstring: 0x1993
+  __TEXT.__gcc_except_tab: 0x78
+  __TEXT.__cstring: 0x1a2f
   __TEXT.__oslogstring: 0x5d
-  __TEXT.__unwind_info: 0x230
+  __TEXT.__unwind_info: 0x260
   __TEXT.__objc_classname: 0x1b2
-  __TEXT.__objc_methname: 0x1689
-  __TEXT.__objc_methtype: 0x82f
-  __TEXT.__objc_stubs: 0xb40
-  __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x188
+  __TEXT.__objc_methname: 0x16cd
+  __TEXT.__objc_methtype: 0x841
+  __TEXT.__objc_stubs: 0xc20
+  __DATA_CONST.__got: 0xf0
+  __DATA_CONST.__const: 0x1b0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b8
+  __DATA_CONST.__objc_selrefs: 0x6c8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x290
+  __AUTH_CONST.__auth_got: 0x2a8
   __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__cfstring: 0x10a0
+  __AUTH_CONST.__cfstring: 0x1220
   __AUTH_CONST.__objc_const: 0x20b0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0xf8

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 232E19D9-36A3-3C10-8B50-D5079D241845
-  Functions: 238
-  Symbols:   951
-  CStrings:  758
+  UUID: 6E96FF46-416A-3902-83E6-87C5F9DEB0CD
+  Functions: 243
+  Symbols:   973
+  CStrings:  783
 
Symbols:
+ -[MobileAccessoryUpdater sendMessageForCommand:withOptions:replyHandler:]
+ GCC_except_table7
+ ___40-[MobileAccessoryUpdater getPluginsList]_block_invoke
+ ___42-[MobileAccessoryUpdater createConnection]_block_invoke
+ ___block_descriptor_56_e8_32o40r48r_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8r40l8r48l8
+ _dispatch_time
+ _objc_msgSend$getActiveDeviceClass
+ _objc_msgSend$getActiveDeviceClassCString
+ _objc_msgSend$handleInboundEvent:
+ _objc_msgSend$initWithClientName:replyHandlerQueue:messageHandler:
+ _objc_msgSend$sendMessageForCommand:withOptions:replyHandler:
+ _objc_msgSend$sendMessageToFud:
+ _objc_msgSend$sendMessageToFud:reply:
+ _objc_retain_x8
+ _xpc_dictionary_get_remote_connection
CStrings:
+ "B36@0:8i16@20@?28"
+ "Can't reply to NULL message"
+ "Can't send NULL message"
+ "Can't send NULL xpc message"
+ "Can't send command since filter is not set, command:%@"
+ "Can't send message to NULL connection"
+ "Can't set filter name to nil value"
+ "Could not create a valid connection to daemon"
+ "FUD replied error %@"
+ "Failed to get plugin list"
+ "Failed to get xpc connection from replyTo dict"
+ "FilterIdentifier"
+ "LOADING PLUGIN: _bundleIdentifier = %@, _clientIdentifier = %@ "
+ "NULL reply from getPluginsList request"
+ "Options"
+ "Plugin list = %@"
+ "PluginIdentifier"
+ "PluginsList"
+ "handleInboundEvent:"
+ "sendMessageForCommand:withOptions:replyHandler:"
- "-[MobileAccessoryUpdater getActiveDeviceClassCString]"
- "-[MobileAccessoryUpdater getActiveDeviceClass]"
- "-[MobileAccessoryUpdater getPluginsList]"
- "-[MobileAccessoryUpdater loadPluginWithAccessoryInfo:options:]"
- "-[MobileAccessoryUpdater registerForIdentifier:isGroupIdentifier:]"
- "-[MobileAccessoryUpdater setActiveDeviceClass:]"
- "External client messaging no longer supported"

```
