## ReplayKit

> `/System/Library/Frameworks/ReplayKit.framework/ReplayKit`

```diff

-650.45.2.0.0
-  __TEXT.__text: 0x2f090
-  __TEXT.__auth_stubs: 0xa70
-  __TEXT.__objc_methlist: 0x2b50
+650.49.1.0.0
+  __TEXT.__text: 0x2f05c
+  __TEXT.__auth_stubs: 0xa80
+  __TEXT.__objc_methlist: 0x2b40
   __TEXT.__const: 0x100
   __TEXT.__gcc_except_tab: 0x108
-  __TEXT.__oslogstring: 0x4733
-  __TEXT.__cstring: 0x58ef
-  __TEXT.__unwind_info: 0x988
+  __TEXT.__oslogstring: 0x46e9
+  __TEXT.__cstring: 0x58b3
+  __TEXT.__unwind_info: 0x980
   __TEXT.__objc_classname: 0x6d9
-  __TEXT.__objc_methname: 0x7ca0
+  __TEXT.__objc_methname: 0x7c61
   __TEXT.__objc_methtype: 0x1adb
-  __TEXT.__objc_stubs: 0x54c0
-  __DATA_CONST.__got: 0x470
+  __TEXT.__objc_stubs: 0x5480
+  __DATA_CONST.__got: 0x478
   __DATA_CONST.__const: 0x9b0
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cd8
+  __DATA_CONST.__objc_selrefs: 0x1cc8
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x548
+  __AUTH_CONST.__auth_got: 0x550
   __AUTH_CONST.__const: 0x9f8
   __AUTH_CONST.__cfstring: 0x1700
-  __AUTH_CONST.__objc_const: 0x5c80
+  __AUTH_CONST.__objc_const: 0x5c60
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xa50
-  __DATA.__objc_ivar: 0x28c
+  __DATA.__objc_ivar: 0x288
   __DATA.__data: 0xb48
   __DATA.__bss: 0x118
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2DE9B88D-4543-376A-AB4B-0E038F1EB50B
-  Functions: 1129
-  Symbols:   4113
-  CStrings:  2511
+  UUID: 26C463FF-7C82-337C-AFF5-FF3C4ADAE5F0
+  Functions: 1128
+  Symbols:   4110
+  CStrings:  2506
 
Symbols:
+ -[RPControlCenterClient startObservingCallIsActiveStateWithHandler:]
+ _CGColorSpaceCreateWithPropertyList
+ ___48-[RPControlCenterClient startHQLRReadyToRecord:]_block_invoke_2
+ ___68-[RPControlCenterClient startObservingCallIsActiveStateWithHandler:]_block_invoke
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ _kIOSurfaceColorSpace
+ _objc_msgSend$startObservingCallIsActiveStateWithHandler:
- -[RPControlCenterClient initAndFetchAVSystemControllerState]
- -[RPControlCenterClient startObservingCallIsActiveState]
- _OBJC_IVAR_$_RPControlCenterClient._isCallActive
- ___56-[RPControlCenterClient startObservingCallIsActiveState]_block_invoke
- ___60-[RPControlCenterClient initAndFetchAVSystemControllerState]_block_invoke
- ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
- _objc_msgSend$initAndFetchAVSystemControllerState
- _objc_msgSend$sharedAVSystemController
- _objc_msgSend$startObservingCallIsActiveState
CStrings:
+ " [INFO] %{public}s:%d notification value for isCallActive=%@"
+ "-[RPControlCenterClient startHQLRReadyToRecord:]_block_invoke_2"
+ "-[RPControlCenterClient startObservingCallIsActiveStateWithHandler:]_block_invoke"
+ "startObservingCallIsActiveStateWithHandler:"
- " [INFO] %{public}s:%d Fetching AVSystemController"
- " [INFO] %{public}s:%d fetched AVSystemController. AVSystemController_CallIsActive=%@"
- "-[RPControlCenterClient initAndFetchAVSystemControllerState]_block_invoke"
- "-[RPControlCenterClient startHQLRReadyToRecord:]_block_invoke"
- "-[RPControlCenterClient startObservingCallIsActiveState]_block_invoke"
- "_isCallActive"
- "initAndFetchAVSystemControllerState"
- "sharedAVSystemController"
- "startObservingCallIsActiveState"

```
