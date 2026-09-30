## eapolclient

> `/System/Library/SystemConfiguration/EAPOLController.bundle/eapolclient`

```diff

-368.40.2.0.0
-  __TEXT.__text: 0xd764
-  __TEXT.__auth_stubs: 0xdd0
+368.60.2.0.0
+  __TEXT.__text: 0xdab8
+  __TEXT.__auth_stubs: 0xe60
   __TEXT.__objc_stubs: 0x300
   __TEXT.__objc_methlist: 0x268
-  __TEXT.__const: 0xee
-  __TEXT.__oslogstring: 0x179e
-  __TEXT.__cstring: 0x994
+  __TEXT.__const: 0xf6
+  __TEXT.__oslogstring: 0x1800
+  __TEXT.__cstring: 0xa1a
   __TEXT.__objc_classname: 0x43
   __TEXT.__gcc_except_tab: 0x70
   __TEXT.__objc_methname: 0x647
   __TEXT.__objc_methtype: 0x2d7
-  __TEXT.__unwind_info: 0x238
-  __DATA_CONST.__auth_got: 0x6f8
+  __TEXT.__unwind_info: 0x248
+  __DATA_CONST.__auth_got: 0x740
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x218
-  __DATA_CONST.__cfstring: 0xb20
+  __DATA_CONST.__const: 0x2b8
+  __DATA_CONST.__cfstring: 0xbc0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FC098FD4-618B-3B2D-867F-83EB6D5AC412
-  Functions: 157
-  Symbols:   268
-  CStrings:  547
+  UUID: 9C09C6C2-8858-3797-BDC5-F6781D8521C6
+  Functions: 161
+  Symbols:   277
+  CStrings:  561
 
Symbols:
+ _CFRunLoopPerformBlock
+ _CFRunLoopWakeUp
+ _EAPOLClientActivate
+ _EAPOLClientCancel
+ __SC_crash
+ _dispatch_after
+ _dispatch_queue_create
+ _dispatch_release
+ _dispatch_time
CStrings:
+ "ControllerMessageHandlerQueue"
+ "Retry"
+ "Run"
+ "Stop"
+ "TakeUserInput"
+ "Unknown"
+ "eapolclient received [%@] command from the controller"
+ "eapolclient's main thread is unresponsive to controller's commands"
+ "processing [%@] command from the controller"

```
