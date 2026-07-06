## Feedback Assistant

> `/System/Library/CoreServices/Applications/Feedback Assistant.app/Contents/MacOS/Feedback Assistant`

```diff

-  __TEXT.__text: 0xad8b0
-  __TEXT.__auth_stubs: 0x21c0
-  __TEXT.__objc_stubs: 0xf940
-  __TEXT.__objc_methlist: 0x9484
+  __TEXT.__text: 0xae45c
+  __TEXT.__auth_stubs: 0x21e0
+  __TEXT.__objc_stubs: 0xf960
+  __TEXT.__objc_methlist: 0x9494
   __TEXT.__const: 0x3084
   __TEXT.__gcc_except_tab: 0x59c
-  __TEXT.__objc_methname: 0x19405
-  __TEXT.__oslogstring: 0x2e9c
-  __TEXT.__cstring: 0x6361
+  __TEXT.__objc_methname: 0x193d5
+  __TEXT.__oslogstring: 0x2f2c
+  __TEXT.__cstring: 0x6351
   __TEXT.__objc_classname: 0x1c72
-  __TEXT.__objc_methtype: 0x5dc6
+  __TEXT.__objc_methtype: 0x5db6
   __TEXT.__ustring: 0x14e
-  __TEXT.__constg_swiftt: 0x20d8
-  __TEXT.__swift5_typeref: 0x2ee0
+  __TEXT.__constg_swiftt: 0x20e0
+  __TEXT.__swift5_typeref: 0x2f34
   __TEXT.__swift5_fieldmd: 0xe40
   __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_reflstr: 0xe06
   __TEXT.__swift5_assocty: 0x2a0
   __TEXT.__swift5_proto: 0x114
   __TEXT.__swift5_types: 0x140
-  __TEXT.__swift5_capture: 0x724
+  __TEXT.__swift5_capture: 0x730
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x2af8
+  __TEXT.__unwind_info: 0x2ae8
   __TEXT.__eh_frame: 0x918
-  __DATA_CONST.__const: 0x38f8
+  __DATA_CONST.__const: 0x38e8
   __DATA_CONST.__cfstring: 0x42e0
   __DATA_CONST.__objc_classlist: 0x488
   __DATA_CONST.__objc_catlist: 0x90

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__auth_got: 0x10f0
-  __DATA_CONST.__got: 0xd50
-  __DATA_CONST.__auth_ptr: 0x6b0
+  __DATA_CONST.__auth_got: 0x1100
+  __DATA_CONST.__got: 0xdc0
+  __DATA_CONST.__auth_ptr: 0x6c8
   __DATA.__objc_const: 0x1b050
-  __DATA.__objc_selrefs: 0x5f78
+  __DATA.__objc_selrefs: 0x5f80
   __DATA.__objc_ivar: 0x690
-  __DATA.__objc_data: 0x5318
-  __DATA.__data: 0x3358
+  __DATA.__objc_data: 0x5320
+  __DATA.__data: 0x3378
   __DATA.__bss: 0x2500
   __DATA.__common: 0x138
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4231
-  Symbols:   1175
-  CStrings:  6443
+  Functions: 4236
+  Symbols:   1178
+  CStrings:  6444
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__bss : content changed
~ __DATA.__common : content changed
Symbols:
+ _$s12FeedbackCore25FBKPresubmissionCheckStepOMn
+ _$s12FeedbackCore25FBKPresubmissionCheckStepON
+ _$s12FeedbackCore31FBKPresubmissionCheckControllerC11currentStepAA0cdG0OyFTj
+ _$s12FeedbackCore31FBKPresubmissionCheckControllerC16markStepComplete_12didShowAlertyAA0cdG0O_SbtFTj
+ _$s12FeedbackCore31FBKPresubmissionCheckControllerCMa
+ _$s12FeedbackCore31FBKPresubmissionCheckControllerCMn
- _$ss5NeverON
- _$ss5NeverOs5ErrorsWP
- _swift_willThrowTypedImpl
CStrings:
+ "Skipping step [%{public}s]: deviceConnectivity is iOS-only"
+ "Unhandled step: [%{public}s] in macOS draft presubmission flow"
+ "Unhandled step: [%{public}s] in macOS feedback followup presubmission flow"
+ "checkPresubmissionConsentWithHandler:"
+ "checkRequiredAnswersWithSuccess:"
+ "handlePresubmissionChecks:"
+ "updateFileStateAndSubmit"
- "Skipping presubmission consent because DE consent was already presented."
- "checkPresubmissionConsentWithCompletionHandlerAndShowedDEConsent:withHandler:"
- "checkRequiredAnswersCompletionWithHandler:"
- "performAllPresubmissionChecksWithCompletionHandler:"
- "v16@?0B8B12"
- "v28@0:8B16@?20"

```
