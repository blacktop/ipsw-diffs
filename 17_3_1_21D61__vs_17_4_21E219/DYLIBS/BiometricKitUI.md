## BiometricKitUI

> `/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`

```diff

-517.0.0.0.0
-  __TEXT.__text: 0x5a0d8
+556.0.0.0.0
+  __TEXT.__text: 0x5a860
   __TEXT.__auth_stubs: 0xde0
-  __TEXT.__objc_methlist: 0x5748
+  __TEXT.__objc_methlist: 0x5778
   __TEXT.__const: 0x894
   __TEXT.__gcc_except_tab: 0xa2c
-  __TEXT.__cstring: 0x2bc6
-  __TEXT.__oslogstring: 0x35f7
+  __TEXT.__cstring: 0x2bb6
+  __TEXT.__oslogstring: 0x3a4d
   __TEXT.__dlopen_cstrs: 0x292
   __TEXT.__swift5_typeref: 0x96
   __TEXT.__swift5_capture: 0x34

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x16d0
+  __TEXT.__unwind_info: 0x16d8
   __TEXT.__objc_classname: 0xc49
-  __TEXT.__objc_methname: 0x12379
+  __TEXT.__objc_methname: 0x124cf
   __TEXT.__objc_methtype: 0x3105
-  __TEXT.__objc_stubs: 0xcba0
+  __TEXT.__objc_stubs: 0xcc60
   __DATA_CONST.__got: 0x280
   __DATA_CONST.__const: 0x1178
   __DATA_CONST.__objc_classlist: 0x208

   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xea20
-  __DATA_CONST.__objc_selrefs: 0x3e08
+  __DATA_CONST.__objc_selrefs: 0x3e38
+  __DATA_CONST.__objc_classrefs: 0x558
+  __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x180
   __AUTH_CONST.__cfstring: 0x2ea0
   __AUTH_CONST.__objc_const: 0x1800

   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__auth_got: 0x708
-  __AUTH.__objc_data: 0x1060
+  __AUTH.__objc_data: 0x1010
   __AUTH.__data: 0xe0
-  __DATA.__objc_classrefs: 0x558
-  __DATA.__objc_superrefs: 0x178
   __DATA.__objc_ivar: 0x958
   __DATA.__data: 0x1018
   __DATA.__bss: 0x2e0
   __DATA.__common: 0x1d0
-  __DATA_DIRTY.__objc_data: 0x460
+  __DATA_DIRTY.__objc_data: 0x4b0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2413
-  Symbols:   8359
-  CStrings:  4378
+  Functions: 2418
+  Symbols:   8375
+  CStrings:  4410
 
Symbols:
+ -[BKUIFaceIDEnrollOperationsHandler needsCancellationForState:]
+ -[BKUIPearlEnrollController setTransparencyForCoachingController]
+ -[BKUIPearlMovieLoopView addAnimatedSelfPotraitIfNeeded]
+ -[BKUIPearlMovieLoopView addAnimatedSelfPotraitIfNeeded].cold.1
+ -[BKUIPearlMovieLoopView landscape]
+ -[BKUIPearlVideoCaptureSession supportMultitaskingCameraAccess]
+ GCC_except_table14
+ GCC_except_table19
+ GCC_except_table52
+ __ZNKSt3__16vectorI12InstanceInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorI12InstanceInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ ___122-[BKUIFaceIDEnrollOperationsHandler startEnrollForEnrollmentType:glassesRequirement:identity:operationStartedActionBlock:]_block_invoke.75
+ ___122-[BKUIFaceIDEnrollOperationsHandler startEnrollForEnrollmentType:glassesRequirement:identity:operationStartedActionBlock:]_block_invoke.76
+ ___122-[BKUIFaceIDEnrollOperationsHandler startEnrollForEnrollmentType:glassesRequirement:identity:operationStartedActionBlock:]_block_invoke.84
+ ___122-[BKUIFaceIDEnrollOperationsHandler startEnrollForEnrollmentType:glassesRequirement:identity:operationStartedActionBlock:]_block_invoke_2.86
+ ___block_literal_global.382
+ ___block_literal_global.386
+ _objc_msgSend$addAnimatedSelfPotraitIfNeeded
+ _objc_msgSend$isMultitaskingCameraAccessSupported
+ _objc_msgSend$needsCancellationForState:
+ _objc_msgSend$setMultitaskingCameraAccessEnabled:
+ _objc_msgSend$setTransparencyForCoachingController
+ _objc_msgSend$supportMultitaskingCameraAccess
- -[BKUIRotationArrowAnimationLayer _recreateArrow]
- GCC_except_table22
- GCC_except_table27
- GCC_except_table50
- __ZNKSt3__16vectorI12InstanceInfoNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorI12InstanceInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___122-[BKUIFaceIDEnrollOperationsHandler startEnrollForEnrollmentType:glassesRequirement:identity:operationStartedActionBlock:]_block_invoke.73
- ___122-[BKUIFaceIDEnrollOperationsHandler startEnrollForEnrollmentType:glassesRequirement:identity:operationStartedActionBlock:]_block_invoke.74
- ___122-[BKUIFaceIDEnrollOperationsHandler startEnrollForEnrollmentType:glassesRequirement:identity:operationStartedActionBlock:]_block_invoke.82
- ___122-[BKUIFaceIDEnrollOperationsHandler startEnrollForEnrollmentType:glassesRequirement:identity:operationStartedActionBlock:]_block_invoke_2.85
- ___block_literal_global.379
- ___block_literal_global.383
CStrings:
+ "%@ Starting Enroll... type:%li identity:%@ enrollOperationInProgress = YES"
+ "BKUIPearlMovieLoopView: adding subview: animated self potrait"
+ "Coaching controller needs to show: model: %ld, %i, orientation: %li, flat: %i"
+ "Coaching controller transparency: %f for orientation: %ld"
+ "Coaching: self.orientation = %lu, rotation = %f"
+ "Coaching: startAnimation"
+ "ForcedRotation: orientation changed: deviceOrientation = %lu, orientation = %lu"
+ "ForcedRotation:[Rotation Callback] device orientation: %i"
+ "ForcedRotation:registerRotationObserver:"
+ "ROTATE_GENERAL"
+ "T@\"<BNPresentableContext>\",?,W,N"
+ "T@\"<BNPresentableContext>\",?,W,N,V_presentableContext"
+ "T@\"<SBUISystemApertureElement>\",?,R,W,N"
+ "T@\"BSAction\",?,R,N"
+ "T@\"NSSet\",?,R,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"NSURL\",?,R,C,N"
+ "T@\"UIColor\",?,R,C,N"
+ "T@\"UIView<SBUISystemApertureAccessoryView>\",?,R,N"
+ "T@\"UIView<SBUISystemApertureAccessoryView>\",?,R,N,V_leadingView"
+ "T@\"UIView<SBUISystemApertureAccessoryView>\",?,R,N,V_trailingView"
+ "T@\"UIViewController\",?,R,N"
+ "TB,?,N"
+ "TB,?,N,V_canRequestAlertingAssertion"
+ "TB,?,R,N"
+ "TB,?,R,N,GisDraggingDismissalEnabled"
+ "TB,?,R,N,GisDraggingInteractionEnabled"
+ "TB,?,R,N,GisTouchOutsideDismissalEnabled"
+ "TQ,?,N"
+ "TQ,?,R,N"
+ "Td,?,R,N"
+ "Tq,?,R,N"
+ "T{CGSize=dd},?,R,N"
+ "_cleanupEnroll: enrollOperationInProgress = NO"
+ "_setupCaptureStack: Not supporting Multitasking Camera Access"
+ "_setupCaptureStack: Supporting Multitasking Camera Access"
+ "addAnimatedSelfPotraitIfNeeded"
+ "animateWithOrientation: will cancelEnrollForRotationIfNeeded with orientation: %lu"
+ "cancelEnrollForRotation: cancelling now"
+ "cancelEnrollForRotation: currentState[%u]demandsCancellation: %@, hasPartialPillCompletion: %@"
+ "cancelEnrollForRotationIfNeeded: cancelling now for orientation: %ld"
+ "cancelEnrollForRotationIfNeeded: will not cancel for orientation: %ld"
+ "deviceOrientationChanged: orientation = %lu, duration = %f"
+ "isMultitaskingCameraAccessSupported"
+ "landscape"
+ "needsCancellationForState:"
+ "retryOperation: enrollOperationInProgress = NO"
+ "setMultitaskingCameraAccessEnabled:"
+ "setTransparencyForCoachingController"
+ "startEnrollForEnrollmentType: enrollOperationInProgress = YES - Enroll already in progress"
+ "supportMultitaskingCameraAccess"
- "%@ Enroll already started!"
- "%@ Starting Enroll... type:%li identity:%@"
- "Coaching controller needs to show: %i, orientation: %li, flat: %i"
- "ROTATE_TO_PORTRAIT_UPSIDE_DOWN"
- "T@\"<BNPresentableContext>\",W,N"
- "T@\"<BNPresentableContext>\",W,N,V_presentableContext"
- "T@\"<SBUISystemApertureElement>\",R,W,N"
- "T@\"BSAction\",R,N"
- "T@\"NSSet\",R,C,N"
- "T@\"NSURL\",R,C,N"
- "T@\"UIColor\",R,C,N"
- "T@\"UIView<SBUISystemApertureAccessoryView>\",R,N"
- "T@\"UIView<SBUISystemApertureAccessoryView>\",R,N,V_leadingView"
- "T@\"UIView<SBUISystemApertureAccessoryView>\",R,N,V_trailingView"
- "TB,N,V_canRequestAlertingAssertion"
- "TB,R,N,GisDraggingDismissalEnabled"
- "TB,R,N,GisDraggingInteractionEnabled"
- "TB,R,N,GisTouchOutsideDismissalEnabled"
- "T{CGSize=dd},R,N"
- "_recreateArrow"

```
