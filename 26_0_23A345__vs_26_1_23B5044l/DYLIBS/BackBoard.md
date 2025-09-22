## BackBoard

> `/System/Library/AccessibilityBundles/BackBoard.axbundle/BackBoard`

```diff

-3004.4.0.0.0
-  __TEXT.__text: 0x223c4
-  __TEXT.__auth_stubs: 0x15f0
-  __TEXT.__objc_methlist: 0x1f2c
+3005.2.0.0.0
+  __TEXT.__text: 0x222b0
+  __TEXT.__auth_stubs: 0x1600
+  __TEXT.__objc_methlist: 0x1f0c
   __TEXT.__const: 0x2ba
-  __TEXT.__gcc_except_tab: 0x5f0
-  __TEXT.__cstring: 0x2338
-  __TEXT.__oslogstring: 0x1925
+  __TEXT.__gcc_except_tab: 0x5d4
+  __TEXT.__cstring: 0x22b8
+  __TEXT.__oslogstring: 0x18f5
   __TEXT.__dlopen_cstrs: 0x2d9
   __TEXT.__constg_swiftt: 0x1fc
   __TEXT.__swift5_typeref: 0xb0

   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_proto: 0x8
-  __TEXT.__unwind_info: 0xb60
+  __TEXT.__unwind_info: 0xb50
   __TEXT.__objc_classname: 0x454
-  __TEXT.__objc_methname: 0x60a3
-  __TEXT.__objc_methtype: 0xa75
-  __TEXT.__objc_stubs: 0x5480
+  __TEXT.__objc_methname: 0x5fa6
+  __TEXT.__objc_methtype: 0xa77
+  __TEXT.__objc_stubs: 0x5400
   __DATA_CONST.__got: 0x628
   __DATA_CONST.__const: 0x8d0
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a10
+  __DATA_CONST.__objc_selrefs: 0x19e8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0xb08
+  __AUTH_CONST.__auth_got: 0xb10
   __AUTH_CONST.__const: 0xcf0
-  __AUTH_CONST.__cfstring: 0x1b60
-  __AUTH_CONST.__objc_const: 0x2a60
+  __AUTH_CONST.__cfstring: 0x1b20
+  __AUTH_CONST.__objc_const: 0x2a50
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x50

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3F6521AD-28C4-387B-9C85-75CC09CFD2EA
-  Functions: 944
-  Symbols:   3651
-  CStrings:  1769
+  UUID: 7311D916-1F25-34D5-8E07-5DC9430E6279
+  Functions: 938
+  Symbols:   3636
+  CStrings:  1757
 
Symbols:
+ _AXEventHIDServiceDisableAccessibilityEventTranslationKey
+ _IOHIDServiceClientCopyProperty
+ _OBJC_IVAR_$_AXBMotionCuesManager._currentMode
+ ___45-[AXBMotionCuesManager setMotionCuesEnabled:]_block_invoke.292
+ ___45-[AXBMotionCuesManager setMotionCuesEnabled:]_block_invoke.292.cold.1
+ ___block_literal_global.291
+ ___block_literal_global.294
+ ___block_literal_global.300
+ ___block_literal_global.343
+ ___block_literal_global.348
+ ___block_literal_global.353
- -[AXBHardwareManager _updateForContinuityStateChange]
- -[AXBHardwareManager setSpringboardContinuityCheckQueue:]
- -[AXBHardwareManager springboardContinuityCheckQueue]
- _OBJC_IVAR_$_AXBHardwareManager._springboardContinuityCheckQueue
- ___26-[AXBHardwareManager init]_block_invoke_6
- ___45-[AXBMotionCuesManager setMotionCuesEnabled:]_block_invoke.296
- ___45-[AXBMotionCuesManager setMotionCuesEnabled:]_block_invoke.296.cold.1
- ____handleContinuityDisplayStateChanged_block_invoke
- ___block_literal_global.351
- ___block_literal_global.356
- __handleContinuityDisplayStateChanged
- _kAXSContinuityDisplayStateChangedNotification
- _objc_msgSend$_updateForContinuityStateChange
- _objc_msgSend$isContinuitySessionActive
- _objc_msgSend$setIgnoreEventsForContinuitySession:
- _objc_msgSend$springboardContinuityCheckQueue
CStrings:
+ "-[AXBMotionCuesManager updateSettings]"
+ "Motion Cues settings changed (enable: %@ -> %@, mode: %@ -> %@)"
- "%s isContinuitySessionActive: %@"
- "-[AXBHardwareManager _updateForContinuityStateChange]"
- "-[AXBMotionCuesManager setMotionCuesEnabled:]"
- "NO"
- "Not sending message because motion cues enablement state is already as requested"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_springboardContinuityCheckQueue"
- "YES"
- "_springboardContinuityCheckQueue"
- "_updateForContinuityStateChange"
- "com.apple.AXBackBoard.ContinuitySessionCheck"
- "isContinuitySessionActive"
- "setIgnoreEventsForContinuitySession:"
- "setSpringboardContinuityCheckQueue:"
- "springboardContinuityCheckQueue"

```
