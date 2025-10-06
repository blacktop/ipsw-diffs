## Portrait

> `/System/Library/PrivateFrameworks/Portrait.framework/Portrait`

```diff

-492.40.4.0.0
-  __TEXT.__text: 0x9d358
+492.40.5.0.0
+  __TEXT.__text: 0x9d3ec
   __TEXT.__auth_stubs: 0x13d0
   __TEXT.__delay_stubs: 0x2ec
   __TEXT.__delay_helper: 0x230
-  __TEXT.__objc_methlist: 0x98d4
+  __TEXT.__objc_methlist: 0x98dc
   __TEXT.__const: 0x21260
   __TEXT.__cstring: 0x6f41
-  __TEXT.__oslogstring: 0x48bb
+  __TEXT.__oslogstring: 0x4908
   __TEXT.__gcc_except_tab: 0x1844
   __TEXT.__ustring: 0x30
   __TEXT.__unwind_info: 0x2130
   __TEXT.__objc_classname: 0x1390
-  __TEXT.__objc_methname: 0x1ae02
-  __TEXT.__objc_methtype: 0x57b2
+  __TEXT.__objc_methname: 0x1ae1f
+  __TEXT.__objc_methtype: 0x5797
   __TEXT.__objc_stubs: 0xfc40
   __DATA_CONST.__got: 0x920
   __DATA_CONST.__const: 0x970

   __AUTH_CONST.__auth_got: 0xa88
   __AUTH_CONST.__const: 0x440
   __AUTH_CONST.__cfstring: 0x5180
-  __AUTH_CONST.__objc_const: 0x1cbc0
+  __AUTH_CONST.__objc_const: 0x1cbf0
   __AUTH_CONST.__objc_intobj: 0xb40
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH.__objc_data: 0x1e50
   __AUTH.__data: 0x9e0
-  __DATA.__objc_ivar: 0x177c
+  __DATA.__objc_ivar: 0x1780
   __DATA.__data: 0x818
-  __DATA.__bss: 0xe58
+  __DATA.__bss: 0xe5c
   __DATA_DIRTY.__objc_data: 0x1860
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 37A40EA7-42F7-39AF-B193-8F062C1C59B7
-  Functions: 4058
-  Symbols:   15083
-  CStrings:  7625
+  UUID: 13E87B68-3E53-3DFC-97B9-DAD6705134F2
+  Functions: 4059
+  Symbols:   15087
+  CStrings:  7626
 
Symbols:
+ -[PTEffectReactionProvider initWithEffectDescriptor:sharedResources:externalHandDetectionsEnabled:]
+ -[PTHandGestureDetector externalCamera]
+ -[PTHandGestureDetector initWithFrameSize:asyncInitQueue:externalHandDetectionsEnabled:externalCamera:]
+ _OBJC_IVAR_$_PTHandGestureDetector._externalCamera
+ ___103-[PTHandGestureDetector initWithFrameSize:asyncInitQueue:externalHandDetectionsEnabled:externalCamera:]_block_invoke
+ ___103-[PTHandGestureDetector initWithFrameSize:asyncInitQueue:externalHandDetectionsEnabled:externalCamera:]_block_invoke.cold.1
+ ___block_descriptor_112_ea8_32s40r48w_e5_v8?0lw48l8r40l8s32l8
+ _objc_msgSend$initWithEffectDescriptor:sharedResources:externalHandDetectionsEnabled:
+ _objc_msgSend$initWithFrameSize:asyncInitQueue:externalHandDetectionsEnabled:externalCamera:
+ _sPTEffectResourcesLock
- -[PTEffectReactionProvider initWithFrameSize:sharedResources:asyncInitQueue:externalHandDetectionsEnabled:]
- -[PTHandGestureDetector initWithFrameSize:asyncInitQueue:externalHandDetectionsEnabled:]
- ___88-[PTHandGestureDetector initWithFrameSize:asyncInitQueue:externalHandDetectionsEnabled:]_block_invoke
- ___88-[PTHandGestureDetector initWithFrameSize:asyncInitQueue:externalHandDetectionsEnabled:]_block_invoke.cold.1
- ___block_descriptor_120_ea8_32s40s48r56w_e5_v8?0lw56l8s32l8r48l8s40l8
- _objc_msgSend$initWithFrameSize:asyncInitQueue:externalHandDetectionsEnabled:
- _objc_msgSend$initWithFrameSize:sharedResources:asyncInitQueue:externalHandDetectionsEnabled:
CStrings:
+ "@48@0:8{CGSize=dd}16@32B40B44"
+ "A1"
+ "GestureDetector: Using hand detection from %@ externalCamera %i instance %p"
+ "GestureDetector: finished creation instance %p"
+ "TB,R,V_externalCamera"
+ "initWithEffectDescriptor:sharedResources:externalHandDetectionsEnabled:"
+ "initWithFrameSize:asyncInitQueue:externalHandDetectionsEnabled:externalCamera:"
- "@44@0:8{CGSize=dd}16@32B40"
- "@52@0:8{CGSize=dd}16@32@40B48"
- "A!"
- "GestureDetector: Using hand detection from %@"
- "a"
- "initWithFrameSize:asyncInitQueue:externalHandDetectionsEnabled:"
- "initWithFrameSize:sharedResources:asyncInitQueue:externalHandDetectionsEnabled:"

```
