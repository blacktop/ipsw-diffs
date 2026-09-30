## AttentionAwareness

> `/System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness`

```diff

-240.0.0.0.0
-  __TEXT.__text: 0x37c50
+240.40.1.0.0
+  __TEXT.__text: 0x37a8c
   __TEXT.__auth_stubs: 0x9c0
-  __TEXT.__objc_methlist: 0x276c
-  __TEXT.__const: 0x178
+  __TEXT.__objc_methlist: 0x2744
+  __TEXT.__const: 0x160
   __TEXT.__gcc_except_tab: 0x820
-  __TEXT.__oslogstring: 0x55d5
-  __TEXT.__cstring: 0x39af
+  __TEXT.__oslogstring: 0x5569
+  __TEXT.__cstring: 0x3989
   __TEXT.__unwind_info: 0xc80
-  __TEXT.__objc_classname: 0x5da
-  __TEXT.__objc_methname: 0x530e
-  __TEXT.__objc_methtype: 0x1908
-  __TEXT.__objc_stubs: 0x43c0
+  __TEXT.__objc_classname: 0x5dc
+  __TEXT.__objc_methname: 0x5248
+  __TEXT.__objc_methtype: 0x1902
+  __TEXT.__objc_stubs: 0x4320
   __DATA_CONST.__got: 0x210
   __DATA_CONST.__const: 0xe20
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1450
+  __DATA_CONST.__objc_selrefs: 0x1428
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x4f8
   __AUTH_CONST.__const: 0x3c8
-  __AUTH_CONST.__cfstring: 0x1d00
-  __AUTH_CONST.__objc_const: 0x50e8
+  __AUTH_CONST.__cfstring: 0x1ce0
+  __AUTH_CONST.__objc_const: 0x5088
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x54c
+  __DATA.__objc_ivar: 0x544
   __DATA.__data: 0xae0
   __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0x820

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 261732B3-5438-3244-BF7B-D4BC4A80540C
-  Functions: 957
-  Symbols:   3653
-  CStrings:  2346
+  UUID: C45D8564-FABB-3E95-B13B-2B541B6FCA79
+  Functions: 954
+  Symbols:   3640
+  CStrings:  2336
 
Symbols:
+ GCC_except_table506
+ GCC_except_table512
+ GCC_except_table517
+ GCC_except_table521
+ GCC_except_table525
+ GCC_except_table530
+ GCC_except_table534
+ GCC_except_table538
+ GCC_except_table605
+ GCC_except_table629
+ GCC_except_table706
+ GCC_except_table838
+ GCC_except_table864
+ GCC_except_table868
+ GCC_except_table872
+ GCC_except_table877
+ GCC_except_table879
+ GCC_except_table890
+ GCC_except_table892
+ GCC_except_table897
+ GCC_except_table903
+ GCC_except_table905
+ ___Block_byref_object_copy_.1630
+ ___Block_byref_object_copy_.2045
+ ___Block_byref_object_copy_.2313
+ ___Block_byref_object_dispose_.1631
+ ___Block_byref_object_dispose_.2046
+ ___Block_byref_object_dispose_.2314
+ ___block_literal_global.1568
+ ___block_literal_global.1646
+ ___block_literal_global.2065
+ ___block_literal_global.2345
+ ___block_literal_global.2714
- -[AWAttentionSampler lastAttentionScore]
- -[AWAttentionSampler setLastAttentionScore:]
- -[AWFaceDetectAttentionEvent attentionScore]
- GCC_except_table508
- GCC_except_table514
- GCC_except_table519
- GCC_except_table523
- GCC_except_table527
- GCC_except_table532
- GCC_except_table536
- GCC_except_table540
- GCC_except_table607
- GCC_except_table631
- GCC_except_table708
- GCC_except_table841
- GCC_except_table867
- GCC_except_table871
- GCC_except_table878
- GCC_except_table882
- GCC_except_table883
- GCC_except_table893
- GCC_except_table895
- GCC_except_table900
- GCC_except_table906
- GCC_except_table908
- _OBJC_IVAR_$_AWAttentionSampler._lastAttentionScore
- _OBJC_IVAR_$_AWFaceDetectAttentionEvent._attentionScore
- ___Block_byref_object_copy_.1635
- ___Block_byref_object_copy_.2050
- ___Block_byref_object_copy_.2318
- ___Block_byref_object_dispose_.1636
- ___Block_byref_object_dispose_.2051
- ___Block_byref_object_dispose_.2319
- ___block_literal_global.1573
- ___block_literal_global.1651
- ___block_literal_global.2070
- ___block_literal_global.2350
- ___block_literal_global.2720
- _objc_msgSend$attentionScore
- _objc_msgSend$hasPayingAttentionConfidence
- _objc_msgSend$lastAttentionScore
- _objc_msgSend$payingAttentionConfidence
- _objc_msgSend$setLastAttentionScore:
CStrings:
+ "%13.5f: %@ operation %p currentOperation %p faceDetectStateChanged %s pitch: %@ yaw: %@ roll: %@ orientation: %@ faceDetectionScore: %@"
+ "%13.5f: Received metadata in %@ faceDetectStateChanged %s pitch: %f yaw: %f roll: %f orientation: %@ faceDetectionScore: %f"
+ "%30s:%-4d: %13.5f: %@ faceDetectStateChanged %s pitch: %13.5f yaw: %13.5f roll: %13.5f orientation: %@ distance: %13.5f eyeReliefFaceState:%@ faceDetectionScore: %f"
+ "%30s:%-4d: %13.5f: %@ operation %p currentOperation %p faceDetectStateChanged %s pitch: %@ yaw: %@ roll: %@ orientation: %@ distance: %@ eyeReliefFaceState:%@ faceDetectionScore: %f"
+ "%30s:%-4d: %13.5f: %@ operation %p currentOperation %p faceDetectStateChanged %s pitch: %@ yaw: %@ roll: %@ orientation: %@ faceDetectionScore: %@"
+ "%30s:%-4d: %13.5f: Received metadata in %@ faceDetectStateChanged %s pitch: %f yaw: %f roll: %f orientation: %@ faceDetectionScore: %f"
+ "<%@: %p> (timestamp: %13.5f metadataValid %u pitch %13.5f yaw %13.5f roll %13.5f orientation %@ distance %13.5f faceState: %@ metadataType: %@ motionData: %@ motionResult: %@ faceDetectionScore: %13.5f %@)"
+ "@40@0:8d16Q24^{AWFaceDetectMetadata=BdddQdQQ[16f]QfQ{CGRect={CGPoint=dd}{CGSize=dd}}}32"
+ "B56@0:8^{__IOHIDEvent=}16Q24^(?={AWFaceDetectMetadata=BdddQdQQ[16f]QfQ{CGRect={CGPoint=dd}{CGSize=dd}}}{AWRemoteMetadata=qqQB}{AWDigitizerButtonKeyboardMetadata=Q^{__CFString}})32^{__IOHIDService=}40@48"
+ "v200@0:8{AWFaceDetectMetadata=BdddQdQQ[16f]QfQ{CGRect={CGPoint=dd}{CGSize=dd}}}16"
+ "v28@0:8i16^{AWFaceDetectMetadata=BdddQdQQ[16f]QfQ{CGRect={CGPoint=dd}{CGSize=dd}}}20"
+ "v36@0:8i16^(?={AWFaceDetectMetadata=BdddQdQQ[16f]QfQ{CGRect={CGPoint=dd}{CGSize=dd}}}iii)20@28"
+ "v40@0:8Q16Q24^(?={AWFaceDetectMetadata=BdddQdQQ[16f]QfQ{CGRect={CGPoint=dd}{CGSize=dd}}}{AWRemoteMetadata=qqQB}{AWDigitizerButtonKeyboardMetadata=Q^{__CFString}})32"
+ "\x81"
- "%13.5f: %@ operation %p currentOperation %p faceDetectStateChanged %s pitch: %@ yaw: %@ roll: %@ orientation: %@ attentionScore: %@faceDetectionScore: %@"
- "%13.5f: Received metadata in %@ faceDetectStateChanged %s pitch: %f yaw: %f roll: %f orientation: %@ attentionScore: %ffaceDetectionScore: %f"
- "%30s:%-4d: %13.5f: %@ faceDetectStateChanged %s pitch: %13.5f yaw: %13.5f roll: %13.5f orientation: %@ distance: %13.5f eyeReliefFaceState:%@ attentionScore: %ffaceDetectionScore: %f"
- "%30s:%-4d: %13.5f: %@ operation %p currentOperation %p faceDetectStateChanged %s pitch: %@ yaw: %@ roll: %@ orientation: %@ attentionScore: %@faceDetectionScore: %@"
- "%30s:%-4d: %13.5f: %@ operation %p currentOperation %p faceDetectStateChanged %s pitch: %@ yaw: %@ roll: %@ orientation: %@ distance: %@ eyeReliefFaceState:%@ attentionScore: %ffaceDetectionScore: %f"
- "%30s:%-4d: %13.5f: Received metadata in %@ faceDetectStateChanged %s pitch: %f yaw: %f roll: %f orientation: %@ attentionScore: %ffaceDetectionScore: %f"
- "<%@: %p> (timestamp: %13.5f metadataValid %u pitch %13.5f yaw %13.5f roll %13.5f orientation %@ distance %13.5f faceState: %@ metadataType: %@ motionData: %@ motionResult: %@ attentionScore: %13.5f faceDetectionScore: %13.5f %@)"
- "@40@0:8d16Q24^{AWFaceDetectMetadata=BdddQdQQ[16f]QffQ{CGRect={CGPoint=dd}{CGSize=dd}}}32"
- "B56@0:8^{__IOHIDEvent=}16Q24^(?={AWFaceDetectMetadata=BdddQdQQ[16f]QffQ{CGRect={CGPoint=dd}{CGSize=dd}}}{AWRemoteMetadata=qqQB}{AWDigitizerButtonKeyboardMetadata=Q^{__CFString}})32^{__IOHIDService=}40@48"
- "Tf,N,V_lastAttentionScore"
- "Tf,R,N,V_attentionScore"
- "_attentionScore"
- "_lastAttentionScore"
- "attentionScore"
- "hasPayingAttentionConfidence"
- "lastAttentionScore"
- "payingAttentionConfidence"
- "setLastAttentionScore:"
- "v200@0:8{AWFaceDetectMetadata=BdddQdQQ[16f]QffQ{CGRect={CGPoint=dd}{CGSize=dd}}}16"
- "v28@0:8i16^{AWFaceDetectMetadata=BdddQdQQ[16f]QffQ{CGRect={CGPoint=dd}{CGSize=dd}}}20"
- "v36@0:8i16^(?={AWFaceDetectMetadata=BdddQdQQ[16f]QffQ{CGRect={CGPoint=dd}{CGSize=dd}}}iii)20@28"
- "v40@0:8Q16Q24^(?={AWFaceDetectMetadata=BdddQdQQ[16f]QffQ{CGRect={CGPoint=dd}{CGSize=dd}}}{AWRemoteMetadata=qqQB}{AWDigitizerButtonKeyboardMetadata=Q^{__CFString}})32"

```
