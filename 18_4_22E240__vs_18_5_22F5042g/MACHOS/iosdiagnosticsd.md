## iosdiagnosticsd

> `/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iosdiagnosticsd`

```diff

-820.100.58.0.0
-  __TEXT.__text: 0xcb4c
+820.120.55.0.0
+  __TEXT.__text: 0xce58
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_stubs: 0x2500
-  __TEXT.__objc_methlist: 0x15ac
-  __TEXT.__const: 0x78
-  __TEXT.__objc_methname: 0x32b2
-  __TEXT.__oslogstring: 0x9e7
-  __TEXT.__cstring: 0xa56
+  __TEXT.__objc_stubs: 0x2520
+  __TEXT.__objc_methlist: 0x15bc
+  __TEXT.__const: 0x80
+  __TEXT.__objc_methname: 0x32e8
+  __TEXT.__oslogstring: 0xac1
+  __TEXT.__cstring: 0xb26
   __TEXT.__objc_classname: 0x34c
   __TEXT.__objc_methtype: 0x1041
-  __TEXT.__gcc_except_tab: 0x504
+  __TEXT.__gcc_except_tab: 0x514
   __TEXT.__dlopen_cstrs: 0xfc
   __TEXT.__unwind_info: 0x4a0
   __DATA_CONST.__auth_got: 0x358
   __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0x5a8
-  __DATA_CONST.__cfstring: 0xc80
+  __DATA_CONST.__const: 0x5b0
+  __DATA_CONST.__cfstring: 0xca0
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x4628
-  __DATA.__objc_selrefs: 0xd18
+  __DATA.__objc_const: 0x4630
+  __DATA.__objc_selrefs: 0xd28
   __DATA.__objc_ivar: 0x13c
   __DATA.__objc_data: 0x820
   __DATA.__data: 0x5a0

   - /usr/lib/libobjc.A.dylib
   Functions: 403
   Symbols:   188
-  CStrings:  952
+  CStrings:  962
 
CStrings:
+ "-[DAIDSMessengerProxy receiveMessage:data:fromDestination:expectsResponse:response:]_block_invoke"
+ "-[DDWatchMessageReceiver receiveMessage:data:fromDestination:expectsResponse:response:]"
+ "[DADeviceDecoratorWithSync] Received %@ message"
+ "[DADeviceDecoratorWithSync] Routing %@ message to %@"
+ "[DAIDSMessengerProxy] %s, receiver: %@"
+ "[DDMain] Adding a pending task for the %@ message"
+ "[DDWatchMessageReceiver] %s"
+ "device:didRequestOperationMode:"
+ "requestAssessmentMode"
+ "startInOperationMode:"

```
