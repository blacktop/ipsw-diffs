## feedbackd

> `/usr/libexec/feedbackd`

```diff

-139.1.0.0.0
-  __TEXT.__text: 0x6e5c8
-  __TEXT.__auth_stubs: 0x1d60
+139.3.0.0.0
+  __TEXT.__text: 0x70b74
+  __TEXT.__auth_stubs: 0x1da0
   __TEXT.__objc_methlist: 0x224
-  __TEXT.__const: 0x1468
+  __TEXT.__const: 0x1478
   __TEXT.__cstring: 0x3a71
-  __TEXT.__objc_methname: 0x1429
-  __TEXT.__oslogstring: 0x2578
-  __TEXT.__swift5_typeref: 0xb99
+  __TEXT.__objc_methname: 0x1463
+  __TEXT.__oslogstring: 0x2738
+  __TEXT.__swift5_typeref: 0xbaf
   __TEXT.__constg_swiftt: 0xb50
   __TEXT.__swift5_fieldmd: 0x710
   __TEXT.__swift5_reflstr: 0x95e

   __TEXT.__swift5_types: 0x94
   __TEXT.__objc_classname: 0x83
   __TEXT.__objc_methtype: 0x258
+  __TEXT.__swift5_capture: 0x4d0
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_capture: 0x46c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x13f8
-  __TEXT.__eh_frame: 0x3600
-  __DATA_CONST.__auth_got: 0xeb0
-  __DATA_CONST.__got: 0x768
-  __DATA_CONST.__auth_ptr: 0x3f0
-  __DATA_CONST.__const: 0x1608
+  __TEXT.__unwind_info: 0x1458
+  __TEXT.__eh_frame: 0x3708
+  __DATA_CONST.__auth_got: 0xed0
+  __DATA_CONST.__got: 0x780
+  __DATA_CONST.__auth_ptr: 0x3f8
+  __DATA_CONST.__const: 0x1720
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA.__objc_const: 0x1a58
-  __DATA.__objc_selrefs: 0x588
+  __DATA.__objc_selrefs: 0x598
   __DATA.__objc_data: 0x928
-  __DATA.__data: 0x1bb8
+  __DATA.__data: 0x1c08
   __DATA.__bss: 0x1d90
   __DATA.__common: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1333
-  Symbols:   815
-  CStrings:  752
+  Functions: 1367
+  Symbols:   823
+  CStrings:  763
 
Symbols:
+ _$s15FeedbackService15FBKSInteractionC13featureDomain8bundleID16prefillQuestions15originalContent09generatedK012modelVersion11diagnostics16auxiliaryMetrics14isHighPriority010evaluationG0A2C07FeatureE0O_SSSgSDyAA8FBKSFormC8QuestionOSaySSGGSgAC0K0OSgAz2PSDySSSiGSgSb10Foundation4UUIDVSgtcfCTj
+ _$sScT6cancelyyF
+ _$sScTss5NeverORszABRs_rlE11isCancelledSbvgZ
+ _$sScTss5NeverORszABRs_rlE5sleep11nanosecondsys6UInt64V_tYaKFZ
+ _$sScTss5NeverORszABRs_rlE5sleep11nanosecondsys6UInt64V_tYaKFZTu
+ _$ss5NeverOMn
+ _$ss5NeverON
+ _$ss5NeverOs5ErrorsWP
+ _swift_retain_n
- _$s15FeedbackService12FBKSDonationC13featureDomain8bundleID16prefillQuestions15originalContent09generatedK012modelVersion11diagnostics16auxiliaryMetrics14isHighPriority010evaluationG0AcA15FBKSInteractionC07FeatureE0O_SSSgSDyAA8FBKSFormC8QuestionOSaySSGGSgAO0K0OA_A2RSDySSSiGSgSb10Foundation4UUIDVSgtcfCTj
CStrings:
+ "Did finish waiting on notification permission check"
+ "Failed to expire background system task with error: %!{(MISSING)public}s"
+ "Notification task %!{(MISSING)public}@ expired"
+ "Post notification error: %!{(MISSING)public}s"
+ "Registering task %!{(MISSING)public}s) with feedbackd."
+ "Setting %!{(MISSING)public}@ completed"
+ "Task %!{(MISSING)public}@ was cancelled"
+ "Will wait on notification permission check"
+ "dictionary is nil or not the right type, will skip"
+ "setExpirationHandler:"
+ "setTaskExpiredWithRetryAfter:error:"

```
