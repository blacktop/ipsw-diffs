## SeymourAppStore

> `/System/Library/PrivateFrameworks/SeymourAppStore.framework/SeymourAppStore`

```diff

-  __TEXT.__text: 0x10850
+  __TEXT.__text: 0x128c0
   __TEXT.__objc_methlist: 0x1dc
-  __TEXT.__const: 0x6e0
-  __TEXT.__constg_swiftt: 0x444
-  __TEXT.__swift5_typeref: 0x598
-  __TEXT.__swift5_reflstr: 0x218
-  __TEXT.__swift5_fieldmd: 0x2bc
+  __TEXT.__const: 0x740
+  __TEXT.__constg_swiftt: 0x460
+  __TEXT.__swift5_typeref: 0x59e
+  __TEXT.__swift5_fieldmd: 0x2d8
+  __TEXT.__cstring: 0x377
+  __TEXT.__swift5_capture: 0x188
+  __TEXT.__oslogstring: 0x81a
   __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_reflstr: 0x248
+  __TEXT.__swift5_types: 0x38
+  __TEXT.__swift_as_entry: 0x48
+  __TEXT.__swift_as_ret: 0x48
+  __TEXT.__swift_as_cont: 0x70
   __TEXT.__swift5_proto: 0x20
-  __TEXT.__swift5_types: 0x34
-  __TEXT.__swift_as_entry: 0x30
-  __TEXT.__swift_as_ret: 0x38
-  __TEXT.__swift_as_cont: 0x50
-  __TEXT.__cstring: 0x177
-  __TEXT.__oslogstring: 0x74a
-  __TEXT.__swift5_capture: 0x168
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x428
-  __TEXT.__eh_frame: 0x7cc
+  __TEXT.__unwind_info: 0x498
+  __TEXT.__eh_frame: 0x944
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x238
+  __DATA_CONST.__objc_selrefs: 0x270
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x730
-  __AUTH_CONST.__objc_const: 0x780
-  __AUTH_CONST.__auth_got: 0x6f8
+  __AUTH_CONST.__const: 0x7f0
+  __AUTH_CONST.__objc_const: 0x7a0
+  __AUTH_CONST.__auth_got: 0x728
   __AUTH.__objc_data: 0x90
   __AUTH.__data: 0x120
-  __DATA.__data: 0x2a0
+  __DATA.__data: 0x2c0
   __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0x130
   __DATA_DIRTY.__data: 0x640

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 283
-  Symbols:   497
-  CStrings:  34
+  Functions: 316
+  Symbols:   525
+  CStrings:  45
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ _OBJC_CLASS_$_AMSAcknowledgePrivacyTask
+ _OBJC_CLASS_$_AMSDefaults
+ ___swift_closure_destructorTm
+ _objc_msgSend$acknowledgePrivacy
+ _objc_msgSend$acknowledgePrivacyOverride
+ _objc_msgSend$acknowledgementNeededForPrivacyIdentifier:
+ _objc_msgSend$hasPreviouslyAcknowledgedPrivacyIdentifier:
+ _objc_msgSend$hasRejectedPrivacyIdentifier:
+ _objc_msgSend$initWithPrivacyIdentifier:
+ _objc_msgSend$rejectPrivacy
+ _symbolic _____ 15SeymourAppStore28PrivacyAcknowledgementSystemV
- _os_proc_available_memory
CStrings:
+ "AppStoreListener.approvePrivacyAcknowledgement"
+ "AppStoreListener.rejectPrivacyAcknowledgement"
+ "AppStoreListener.resolveNoticePrivacyPreference"
+ "AppStoreListener.resolveOptInPrivacyPreference"
+ "SeymourAppStore/PrivacyAcknowledgementSystem.swift"
+ "[%{public}s] %{public}s begin footprint=%{public}fKB"
+ "[PrivacyAcknowledgementSystem] approvePrivacyAcknowledgement completed result = %{bool}d"
+ "[PrivacyAcknowledgementSystem] rejectPrivacyAcknowledgement completed result = %{bool}d"
+ "approvePrivacyAcknowledgement(privacyIdentifier:)"
+ "rejectPrivacyAcknowledgement(privacyIdentifier:)"
+ "resolveNoticePrivacyPreference(privacyIdentifier:)"
+ "resolveOptInPrivacyPreference(privacyIdentifier:)"
- "[%{public}s] %{public}s begin mem=%{public}fKB"

```
