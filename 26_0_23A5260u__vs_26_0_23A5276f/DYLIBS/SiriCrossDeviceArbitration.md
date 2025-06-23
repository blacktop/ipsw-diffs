## SiriCrossDeviceArbitration

> `/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration`

```diff

-3500.47.1.0.0
-  __TEXT.__text: 0x2fba8
+3500.54.1.0.0
+  __TEXT.__text: 0x2fb24
   __TEXT.__auth_stubs: 0x830
   __TEXT.__objc_methlist: 0x2f14
   __TEXT.__dlopen_cstrs: 0x118
-  __TEXT.__const: 0x1e8
+  __TEXT.__const: 0x1e0
   __TEXT.__gcc_except_tab: 0x498
-  __TEXT.__oslogstring: 0x52ae
-  __TEXT.__cstring: 0x59d2
+  __TEXT.__oslogstring: 0x52bc
+  __TEXT.__cstring: 0x59c1
   __TEXT.__unwind_info: 0xc80
   __TEXT.__objc_classname: 0x5f5
-  __TEXT.__objc_methname: 0x7bcb
-  __TEXT.__objc_methtype: 0x1897
+  __TEXT.__objc_methname: 0x7ba2
+  __TEXT.__objc_methtype: 0x1895
   __TEXT.__objc_stubs: 0x5a60
   __DATA_CONST.__got: 0x2f8
-  __DATA_CONST.__const: 0x10f8
+  __DATA_CONST.__const: 0x10d8
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0xa8
   __AUTH_CONST.__auth_got: 0x428
   __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x2700
-  __AUTH_CONST.__objc_const: 0x53d8
+  __AUTH_CONST.__cfstring: 0x2720
+  __AUTH_CONST.__objc_const: 0x5378
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x4f8
+  __DATA.__objc_ivar: 0x4ec
   __DATA.__data: 0x5d0
   __DATA.__bss: 0x180
   __DATA_DIRTY.__objc_data: 0xbe0

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AA119DAC-A6C1-3E75-BD6B-32B78814CAE0
+  UUID: EC28A73D-DBFF-3CEE-BF58-3168A6F83520
   Functions: 1157
-  Symbols:   4124
-  CStrings:  2888
+  Symbols:   4113
+  CStrings:  2885
 
Symbols:
+ -[SCDACoordinator _invalidateTimerHandler]
+ GCC_except_table960
+ ___31-[SCDACoordinator _enterState:]_block_invoke.227
+ ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.325
+ ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.326
+ ___42-[SCDACoordinator _waitWiProx:andExecute:]_block_invoke.355
+ ___52-[SCDACoordinator _createWaitWiProxTimer:waitBlock:]_block_invoke.354
+ ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.333
+ ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.342
+ ___Block_byref_object_copy_.2282
+ ___Block_byref_object_dispose_.2283
+ ___block_literal_global.2277
+ ___block_literal_global.2586
+ ___block_literal_global.349
+ ___block_literal_global.353
+ _objc_msgSend$_invalidateTimerHandler
- -[SCDACoordinator _cancelTimer]
- GCC_except_table961
- _OBJC_IVAR_$_SCDACoordinator._advertInterval
- _OBJC_IVAR_$_SCDACoordinator._delayTarget
- _OBJC_IVAR_$_SCDACoordinator._multipleContinuations
- ___31-[SCDACoordinator _enterState:]_block_invoke.224
- ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.319
- ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.323
- ___42-[SCDACoordinator _waitWiProx:andExecute:]_block_invoke.352
- ___52-[SCDACoordinator _createWaitWiProxTimer:waitBlock:]_block_invoke.351
- ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.330
- ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.339
- ___Block_byref_object_copy_.2286
- ___Block_byref_object_dispose_.2287
- ___block_literal_global.2278
- ___block_literal_global.2567
- ___block_literal_global.343
- ___block_literal_global.350
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_SiriCrossDeviceArbitration
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_SiriCrossDeviceArbitration
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_SiriCrossDeviceArbitration
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_SiriCrossDeviceArbitration
- _objc_msgSend$_cancelTimer
CStrings:
+ "%@-Invalidated"
+ "%s #scda Event token: %@, current event token: %@ for timer: %@"
+ "_invalidateTimerHandler"
+ "\x91"
- "%s #scda Event token: %@, current event token: %@"
- "-[SCDACoordinator _cancelTimer]"
- "_advertInterval"
- "_cancelTimer"
- "_delayTarget"
- "_multipleContinuations"
- "f"
- "\xa1"

```
