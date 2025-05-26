## DiagnosticRequest

> `/System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest`

```diff

-308.80.4.0.0
-  __TEXT.__text: 0xeee8
-  __TEXT.__auth_stubs: 0x5f0
+316.100.13.0.0
+  __TEXT.__text: 0xf208
+  __TEXT.__auth_stubs: 0x610
   __TEXT.__objc_methlist: 0x438
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x12a1
-  __TEXT.__gcc_except_tab: 0x90
+  __TEXT.__cstring: 0x12a9
+  __TEXT.__gcc_except_tab: 0xac
   __TEXT.__oslogstring: 0x1ef0
-  __TEXT.__unwind_info: 0x270
-  __TEXT.__objc_classname: 0x8a
-  __TEXT.__objc_methname: 0xefd
+  __TEXT.__unwind_info: 0x26c
+  __TEXT.__objc_classname: 0x8c
+  __TEXT.__objc_methname: 0xf4f
   __TEXT.__objc_methtype: 0x1fb
-  __TEXT.__objc_stubs: 0xd40
+  __TEXT.__objc_stubs: 0xd80
   __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x490
+  __DATA_CONST.__const: 0x498
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6e8
-  __DATA_CONST.__objc_selrefs: 0x3c8
+  __DATA_CONST.__objc_const: 0x6c8
+  __DATA_CONST.__objc_selrefs: 0x3d8
+  __DATA_CONST.__objc_classrefs: 0xb8
+  __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__cfstring: 0x940
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__auth_got: 0x308
-  __DATA.__objc_classrefs: 0xb8
-  __DATA.__objc_superrefs: 0x30
-  __DATA.__objc_ivar: 0x74
+  __AUTH_CONST.__auth_got: 0x318
+  __DATA.__objc_ivar: 0x70
   __DATA.__data: 0xd8
   __DATA.__bss: 0x3b0
   __DATA_DIRTY.__const: 0x900

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 298
-  Symbols:   1208
-  CStrings:  628
+  Functions: 301
+  Symbols:   1219
+  CStrings:  634
 
Symbols:
+ -[_DRCConnectionState hasConnection]
+ -[_DRCConnectionState setConnection:]
+ ___48-[_DRCConnectionState sendMessageWithReplySync:]_block_invoke
+ _kDRTriggerUpload_isAsync
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_msgSend$hasConnection
+ _objc_msgSend$setConnection:
- -[_DRCConnectionState cleanupState]
- -[_DRCConnectionState isClosed]
- _OBJC_IVAR_$__DRCConnectionState._isClosed
CStrings:
+ "\x02"
+ "T@\"NSObject<OS_xpc_object>\",&,N,V_connection"
+ "TB,R,N"
+ "hasConnection"
+ "isAsync"
+ "setConnection:"

```
