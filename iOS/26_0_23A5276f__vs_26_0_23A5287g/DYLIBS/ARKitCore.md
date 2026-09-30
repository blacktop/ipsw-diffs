## ARKitCore

> `/System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore`

```diff

-738.0.1.0.0
-  __TEXT.__text: 0x194494
+738.0.2.0.0
+  __TEXT.__text: 0x194770
   __TEXT.__auth_stubs: 0x3c80
   __TEXT.__objc_methlist: 0x110dc
   __TEXT.__const: 0x2c118
+  __TEXT.__gcc_except_tab: 0x13d80
+  __TEXT.__oslogstring: 0x1e604
   __TEXT.__cstring: 0x1d925
-  __TEXT.__oslogstring: 0x1e511
-  __TEXT.__gcc_except_tab: 0x13e14
   __TEXT.__ustring: 0xe6
-  __TEXT.__unwind_info: 0x6590
+  __TEXT.__unwind_info: 0x6708
   __TEXT.__objc_classname: 0x2027
-  __TEXT.__objc_methname: 0x2a2e8
+  __TEXT.__objc_methname: 0x2a2dc
   __TEXT.__objc_methtype: 0xa641
   __TEXT.__objc_stubs: 0x1ac00
   __DATA_CONST.__got: 0x1680

   __DATA_CONST.__objc_superrefs: 0x790
   __DATA_CONST.__objc_arraydata: 0x880
   __AUTH_CONST.__auth_got: 0x1e58
-  __AUTH_CONST.__const: 0x3c98
+  __AUTH_CONST.__const: 0x3cb8
   __AUTH_CONST.__cfstring: 0x10480
   __AUTH_CONST.__objc_const: 0x3ce20
   __AUTH_CONST.__objc_intobj: 0x3240
-  __AUTH_CONST.__objc_doubleobj: 0x380
   __AUTH_CONST.__objc_arrayobj: 0x600
+  __AUTH_CONST.__objc_doubleobj: 0x380
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x3660
   __AUTH.__data: 0x10
   __DATA.__objc_ivar: 0x1ff8
   __DATA.__data: 0x1ca0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x1de0
+  __DATA.__bss: 0x1dd8
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1d60
-  __DATA_DIRTY.__bss: 0x4a8
+  __DATA_DIRTY.__bss: 0x4c8
   __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libchannel.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/librealtime_safety.dylib
-  UUID: 3B5F2A97-D300-34C6-97B6-BDA6AF011D3B
-  Functions: 7766
-  Symbols:   30055
-  CStrings:  14412
+  UUID: 2F1911FF-4763-33FD-B1B9-4A06A592223C
+  Functions: 7767
+  Symbols:   30066
+  CStrings:  14414
 
Symbols:
+ -[ARSceneDepthTechnique _safeProcessData:].cold.3
+ OBJC_IVAR_$_ARTechniqueGatherContext._stateLock
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDictionary_$_ARPersonDetectionData
+ __OBJC_$_CATEGORY_NSDictionary_$_ARPersonDetectionData
+ __OBJC_$_CLASS_METHODS_NSDictionary(ARPersonDetectionData|ARAdditions)
- OBJC_IVAR_$_ARTechniqueGatherContext._gatherLock
- __OBJC_$_CATEGORY_CLASS_METHODS_NSDictionary_$_ARAdditions
- __OBJC_$_CATEGORY_NSDictionary_$_ARAdditions
- __OBJC_$_INSTANCE_METHODS_NSDictionary(ARAdditions|ARPersonDetectionData)
CStrings:
+ "%{public}@ <%p>: Downscaled data is dropped, the downscaling technique is not prepared yet."
+ "%{public}@ <%p>: Received unexpected data, downScalingResults is empty."
+ "Error: %{public}@ <%p>: Received unexpected data, downScalingResults is empty."
- "_gatherLock"

```
