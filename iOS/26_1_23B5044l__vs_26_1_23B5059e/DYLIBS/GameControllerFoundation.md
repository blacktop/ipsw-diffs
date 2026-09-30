## GameControllerFoundation

> `/System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation`

```diff

-13.1.4.0.0
-  __TEXT.__text: 0x6e908
+13.1.7.0.0
+  __TEXT.__text: 0x6e9d8
   __TEXT.__auth_stubs: 0x1440
-  __TEXT.__objc_methlist: 0x68dc
+  __TEXT.__objc_methlist: 0x6904
   __TEXT.__const: 0x120
   __TEXT.__gcc_except_tab: 0x32fc
-  __TEXT.__cstring: 0x6fc0
+  __TEXT.__cstring: 0x6fef
   __TEXT.__oslogstring: 0x3171
   __TEXT.__ustring: 0x58
-  __TEXT.__unwind_info: 0x20a8
+  __TEXT.__unwind_info: 0x20a0
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x174f
-  __TEXT.__objc_methname: 0x8ebe
-  __TEXT.__objc_methtype: 0x296a
-  __TEXT.__objc_stubs: 0x5200
-  __DATA_CONST.__got: 0x4b8
+  __TEXT.__objc_methname: 0x8ee5
+  __TEXT.__objc_methtype: 0x2984
+  __TEXT.__objc_stubs: 0x5260
+  __DATA_CONST.__got: 0x4c0
   __DATA_CONST.__const: 0x1bb0
   __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1da0
+  __DATA_CONST.__objc_selrefs: 0x1db0
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x428
   __DATA_CONST.__objc_arraydata: 0x140
   __AUTH_CONST.__auth_got: 0xa38
   __AUTH_CONST.__const: 0x568
-  __AUTH_CONST.__cfstring: 0x6d60
-  __AUTH_CONST.__objc_const: 0x144d8
+  __AUTH_CONST.__cfstring: 0x6d80
+  __AUTH_CONST.__objc_const: 0x144f0
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x26c0
   __AUTH.__data: 0x10b0
-  __DATA.__objc_ivar: 0x854
+  __DATA.__objc_ivar: 0x850
   __DATA.__data: 0x1080
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x148
+  __DATA.__bss: 0x130
   __DATA_DIRTY.__objc_data: 0x500
-  __DATA_DIRTY.__bss: 0x68
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CCCC14A6-BAA6-3292-BC9D-CBFF2198E719
-  Functions: 2852
-  Symbols:   9844
-  CStrings:  4304
+  UUID: 06CF57DD-BA18-3E4E-AD13-F2DA7AED788D
+  Functions: 2854
+  Symbols:   9851
+  CStrings:  4310
 
Symbols:
+ -[GCIONotificationPort addCancellationHandler:onQueue:]
+ -[GCIONotificationPort addCancellationHandler:onQueue:].cold.1
+ -[GCIONotificationPort addCancellationHandler:onQueue:].cold.2
+ -[GCIONotificationPort setQueue:]
+ -[GCIONotificationPort setQueue:].cold.1
+ __OBJC_$_PROP_LIST_GCIONotificationPort
+ ___55-[GCIONotificationPort addCancellationHandler:onQueue:]_block_invoke
+ ___55-[GCIONotificationPort addCancellationHandler:onQueue:]_block_invoke_2
+ _objc_msgSend$addCancellationHandler:onQueue:
+ _objc_msgSend$port
+ _objc_msgSend$queue
+ _objc_msgSend$setQueue:
+ _objc_msgSend$wakePort
- -[GCIONotificationPort initWithMainPort:queue:cancellationHandler:]
- -[GCIONotificationPort setQueue:cancellationHandler:]
- -[GCIONotificationPort setQueue:cancellationHandler:].cold.1
- _OBJC_IVAR_$_GCIONotificationPort._cancellationSource
- ___53-[GCIONotificationPort setQueue:cancellationHandler:]_block_invoke
- ___53-[GCIONotificationPort setQueue:cancellationHandler:]_block_invoke_2
- _objc_msgSend$initWithMainPort:queue:cancellationHandler:
- _objc_msgSend$setQueue:cancellationHandler:
CStrings:
+ "Assertion failed: cancelHandler != ((void *)0)"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "T^{IONotificationPort=},R,V_port"
+ "^{IONotificationPort=}16@0:8"
+ "addCancellationHandler:onQueue:"
+ "setQueue:"
+ "v32@0:8@?16@24"
+ "wakePort"
- "@36@0:8I16@20@?28"
- "_cancellationSource"
- "initWithMainPort:queue:cancellationHandler:"
- "setQueue:cancellationHandler:"

```
