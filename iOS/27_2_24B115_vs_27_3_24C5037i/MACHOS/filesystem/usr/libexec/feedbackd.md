## feedbackd

> `/usr/libexec/feedbackd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`

```diff

-242.0.0.0.0
-  __TEXT.__text: 0x7d2e0
-  __TEXT.__auth_stubs: 0x20a0
+243.3.0.0.0
+  __TEXT.__text: 0x80aa4
+  __TEXT.__auth_stubs: 0x2110
   __TEXT.__objc_stubs: 0x1380
-  __TEXT.__objc_methlist: 0x570
-  __TEXT.__const: 0x218c
-  __TEXT.__cstring: 0x2e85
-  __TEXT.__swift5_typeref: 0xe78
-  __TEXT.__oslogstring: 0x291f
-  __TEXT.__constg_swiftt: 0xd54
-  __TEXT.__swift5_fieldmd: 0x8d8
+  __TEXT.__objc_methlist: 0x58c
+  __TEXT.__const: 0x21cc
+  __TEXT.__cstring: 0x2ed5
+  __TEXT.__swift5_typeref: 0xedc
+  __TEXT.__oslogstring: 0x2a3f
+  __TEXT.__constg_swiftt: 0xd94
+  __TEXT.__swift5_fieldmd: 0x930
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0xb02
+  __TEXT.__swift5_reflstr: 0xb42
   __TEXT.__swift5_assocty: 0xf0
   __TEXT.__swift5_proto: 0x118
-  __TEXT.__swift5_types: 0xb4
+  __TEXT.__swift5_types: 0xb8
+  __TEXT.__swift5_capture: 0x858
   __TEXT.__objc_classname: 0x48c
-  __TEXT.__objc_methname: 0x198d
-  __TEXT.__objc_methtype: 0x882
-  __TEXT.__swift5_capture: 0x848
-  __TEXT.__swift_as_entry: 0x114
-  __TEXT.__swift_as_ret: 0x14c
-  __TEXT.__swift_as_cont: 0x474
+  __TEXT.__objc_methname: 0x19c3
+  __TEXT.__objc_methtype: 0x8a2
+  __TEXT.__swift_as_entry: 0x118
+  __TEXT.__swift_as_ret: 0x154
+  __TEXT.__swift_as_cont: 0x484
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x1b40
-  __TEXT.__eh_frame: 0x4820
-  __DATA_CONST.__const: 0x2438
+  __TEXT.__unwind_info: 0x1bf0
+  __TEXT.__eh_frame: 0x4a88
+  __DATA_CONST.__const: 0x2468
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__auth_got: 0x1058
+  __DATA_CONST.__auth_got: 0x1090
   __DATA_CONST.__got: 0x818
-  __DATA_CONST.__auth_ptr: 0x448
-  __DATA.__objc_const: 0x1d28
-  __DATA.__objc_selrefs: 0x688
-  __DATA.__objc_data: 0x890
-  __DATA.__data: 0x1d28
+  __DATA_CONST.__auth_ptr: 0x450
+  __DATA.__objc_const: 0x1d50
+  __DATA.__objc_selrefs: 0x690
+  __DATA.__objc_data: 0x8b0
+  __DATA.__data: 0x1e08
   __DATA.__common: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1584
-  Symbols:   898
-  CStrings:  782
+  Functions: 1622
+  Symbols:   908
+  CStrings:  788
 
Symbols:
+ _$s15FeedbackService14FBKSEvaluationC21RemoteEvaluationErrorO19closedWithoutResultyA2EmFWC
+ _$s15FeedbackService14FBKSEvaluationC21RemoteEvaluationErrorOMa
+ _$s15FeedbackService14FBKSEvaluationC21RemoteEvaluationErrorOMn
+ _$s15FeedbackService14FBKSEvaluationC21RemoteEvaluationErrorOs0F0AAMc
+ _$s15FeedbackService14FBKSEvaluationC7SubjectO16RemoteEvaluationV07returnsF0SbSgvg
+ _$ss15ContiguousArrayV28_allocateBufferUninitialized15minimumCapacitys01_abD0VyxGSi_tFZ
+ _$ss22_minimumMergeRunLengthyS2iF
+ _objc_release_x9
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_getEnumCaseMultiPayload
+ _swift_storeEnumTagMultiPayload
- _$s15FeedbackService12FBKSDonationC13DonationErrorO11unsupportedyA2EmFWC
- _$s15FeedbackService12FBKSDonationC13DonationErrorOMa
- _$s15FeedbackService12FBKSDonationC13DonationErrorOs0E0AAMc
CStrings:
+ "%{public}s deleted: %{public}ld, notFound: %{public}ld, failed: %{public}ld"
+ "Bulk delete finished: deleted [%{public}ld], not found [%{public}ld], failed [%{public}ld]"
+ "Bulk delete: [%{public}ld] ID(s) are still in storage after the pruner passes: [%{public}s]"
+ "Did finish remote evaluation"
+ "Remote evaluation finished without an evaluation: %{public}@"
+ "Remote evaluation finished without reporting an evaluation"
+ "Remote evaluation unexpectedly finished with a filing result"
+ "evaluationData"
+ "remoteViewControllerDidFinishEvaluation(evaluationData:completion:)"
+ "remoteViewControllerDidFinishEvaluationWithEvaluationData:completion:"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\"@\"NSArray\"@\"NSArray\"@\"NSError\">24"
- "%{public}s deleted: %{public}ld, notFound: %{public}ld"
- "Bulk delete finished: deleted [%{public}ld], not found [%{public}ld]"
- "Did finish launching hidden app"
- "Donation not enabled"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
```
