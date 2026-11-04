## FeedbackService

> `/System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService`

```diff

-242.0.0.0.0
-  __TEXT.__text: 0x93690
-  __TEXT.__objc_methlist: 0x1510
-  __TEXT.__const: 0xcb24
-  __TEXT.__oslogstring: 0x1656
-  __TEXT.__cstring: 0x2df2
+243.3.0.0.0
+  __TEXT.__text: 0x95fc8
+  __TEXT.__objc_methlist: 0x151c
+  __TEXT.__const: 0xcda4
+  __TEXT.__oslogstring: 0x1606
+  __TEXT.__cstring: 0x2ff2
   __TEXT.__ustring: 0xd8
   __TEXT.__gcc_except_tab: 0xb8
-  __TEXT.__swift5_typeref: 0x2b0d
-  __TEXT.__constg_swiftt: 0x25a4
-  __TEXT.__swift5_reflstr: 0x1382
-  __TEXT.__swift5_fieldmd: 0x2790
+  __TEXT.__swift5_typeref: 0x2b91
+  __TEXT.__constg_swiftt: 0x25dc
+  __TEXT.__swift5_reflstr: 0x1412
+  __TEXT.__swift5_fieldmd: 0x2810
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_mpenum: 0x44
-  __TEXT.__swift5_proto: 0xb5c
-  __TEXT.__swift5_types: 0x380
-  __TEXT.__swift5_capture: 0x60c
-  __TEXT.__swift_as_entry: 0x9c
-  __TEXT.__swift_as_ret: 0x98
-  __TEXT.__swift_as_cont: 0x154
-  __TEXT.__swift5_assocty: 0x168
+  __TEXT.__swift5_proto: 0xb7c
+  __TEXT.__swift5_types: 0x388
+  __TEXT.__swift5_capture: 0x5ec
+  __TEXT.__swift_as_entry: 0xa0
+  __TEXT.__swift_as_ret: 0x9c
+  __TEXT.__swift_as_cont: 0x164
+  __TEXT.__swift5_assocty: 0x180
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x33e8
-  __TEXT.__eh_frame: 0x29a8
+  __TEXT.__unwind_info: 0x34d8
+  __TEXT.__eh_frame: 0x2a68
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc70
+  __DATA_CONST.__objc_selrefs: 0xc78
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x78
-  __DATA_CONST.__got: 0x440
-  __AUTH_CONST.__const: 0x6290
+  __DATA_CONST.__got: 0x450
+  __AUTH_CONST.__const: 0x6330
   __AUTH_CONST.__cfstring: 0x1020
-  __AUTH_CONST.__objc_const: 0x31a8
-  __AUTH_CONST.__auth_got: 0xbc0
+  __AUTH_CONST.__objc_const: 0x31b0
+  __AUTH_CONST.__auth_got: 0xc30
   __AUTH.__objc_data: 0x440
-  __AUTH.__data: 0x110
+  __AUTH.__data: 0x118
   __DATA.__objc_ivar: 0x138
-  __DATA.__data: 0x1650
+  __DATA.__data: 0x16b8
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x18d0
-  __DATA_DIRTY.__data: 0x1740
+  __DATA_DIRTY.__data: 0x1730
   __DATA_DIRTY.__bss: 0xb5a0
   __DATA_DIRTY.__common: 0xd0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3941
-  Symbols:   2147
-  CStrings:  493
+  Functions: 3997
+  Symbols:   2161
+  CStrings:  497
 
Symbols:
+ _associated conformance 15FeedbackService14FBKSEvaluationC21RemoteEvaluationErrorO10Foundation13CustomNSErrorAAs0F0
+ _associated conformance 15FeedbackService14FBKSEvaluationC21RemoteEvaluationErrorOSHAASQ
+ _associated conformance 15FeedbackService7FailureV10Foundation13CustomNSErrorAAs5Error
+ _swift_release_x12
+ _swift_retain_x27
+ _symbolic ScCy_____Sg______pG 10Foundation4DataV s5ErrorP
+ _symbolic ScCy___________pG 15FeedbackService12FBKSDonationC14DeletionResultV s5ErrorP
+ _symbolic Shy_____G 10Foundation4UUIDV
+ _symbolic _____ 15FeedbackService12FBKSDonationC14DeletionResultV
+ _symbolic _____ 15FeedbackService14FBKSEvaluationC21RemoteEvaluationErrorO
+ _symbolic _____Sg 10Foundation4DataV
+ _symbolic _____y_____G s11_SetStorageC 10Foundation4UUIDV
+ _symbolic _____y___________pGIegn_ s6ResultOsRi_zRi0_zrlE 15FeedbackService12FBKSDonationC08DeletionA0V s5ErrorP
+ _type_layout_string 15FeedbackService12FBKSDonationC14DeletionResultV
CStrings:
+ "Another remote evaluation is already in progress"
+ "Failed to decode FBKSEvaluation"
+ "Remote evaluation finished with evaluation action [%{public}s] evaluationID [%{public}s] feedbackID [%{public}s] answers [%{public}s]"
+ "The Feedback Form closed without reporting an evaluation"
+ "The Feedback Form did not report an evaluation in time"
+ "_remoteEvaluateReturningEvaluation(action:sceneID:bundleID:showFeedbackForm:associateWithAppleAccount:)"
+ "_sendRemoteEvaluationRequest(action:sceneID:bundleID:showFeedbackForm:associateWithAppleAccount:returnsEvaluation:)"
+ "com.apple.FeedbackService.RemoteEvaluation"
+ "remoteEvaluateForResult(action:sceneID:bundleID:associateWithAppleAccount:showFeedbackForm:)"
+ "returnsEvaluation"
- "Donation is not supported on FCS"
- "Failed to decode FBKSInteraction"
- "Remote evaluation finished bad JSON FBKEvaluation"
- "Remote evaluation finished with evaluation %{public}@"
- "Remote evaluation finished. No FBKSInteraction"
- "_remoteEvaluate(action:showFeedbackForm:associateWithAppleAccount:)"
```
