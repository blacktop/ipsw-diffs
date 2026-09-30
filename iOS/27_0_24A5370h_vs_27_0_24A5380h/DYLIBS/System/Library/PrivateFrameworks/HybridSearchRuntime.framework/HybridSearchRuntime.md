## HybridSearchRuntime

> `/System/Library/PrivateFrameworks/HybridSearchRuntime.framework/HybridSearchRuntime`

```diff

-  __TEXT.__text: 0x252548
+  __TEXT.__text: 0x25ed28
   __TEXT.__objc_methlist: 0x684
-  __TEXT.__const: 0xbb90
-  __TEXT.__constg_swiftt: 0x3848
-  __TEXT.__swift5_typeref: 0x5aa2
+  __TEXT.__const: 0xbe80
+  __TEXT.__constg_swiftt: 0x38d8
+  __TEXT.__swift5_typeref: 0x5c02
   __TEXT.__swift5_builtin: 0x12c
-  __TEXT.__swift5_reflstr: 0x1fb0
-  __TEXT.__swift5_fieldmd: 0x2a50
+  __TEXT.__swift5_reflstr: 0x2070
+  __TEXT.__swift5_fieldmd: 0x2b20
   __TEXT.__swift5_assocty: 0xba0
-  __TEXT.__cstring: 0xe801
-  __TEXT.__swift5_capture: 0x3be8
-  __TEXT.__oslogstring: 0x6dfd
+  __TEXT.__cstring: 0xe891
+  __TEXT.__swift5_capture: 0x3d90
+  __TEXT.__oslogstring: 0x6ead
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__swift5_proto: 0x5e8
-  __TEXT.__swift5_types: 0x448
-  __TEXT.__swift_as_entry: 0xdf8
-  __TEXT.__swift_as_ret: 0x13d4
-  __TEXT.__swift_as_cont: 0x2c88
+  __TEXT.__swift5_proto: 0x5ec
+  __TEXT.__swift5_types: 0x454
+  __TEXT.__swift_as_entry: 0xe88
+  __TEXT.__swift_as_ret: 0x1470
+  __TEXT.__swift_as_cont: 0x2cc4
   __TEXT.__swift5_protos: 0x7c
   __TEXT.__swift5_types2: 0x8
   __TEXT.__gcc_except_tab: 0x60
-  __TEXT.__unwind_info: 0x8fd0
-  __TEXT.__eh_frame: 0x1e4bc
+  __TEXT.__unwind_info: 0x9698
+  __TEXT.__eh_frame: 0x1f070
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1438
+  __DATA_CONST.__objc_selrefs: 0x1448
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__got: 0x1cd0
-  __AUTH_CONST.__const: 0xd0a0
+  __DATA_CONST.__got: 0x1ce8
+  __AUTH_CONST.__const: 0xd670
   __AUTH_CONST.__cfstring: 0x1a0
-  __AUTH_CONST.__objc_const: 0x25d8
+  __AUTH_CONST.__objc_const: 0x2618
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x2a88
-  __AUTH.__objc_data: 0x240
-  __AUTH.__data: 0x2110
-  __DATA.__data: 0x2988
-  __DATA.__bss: 0x66a0
-  __DATA.__common: 0x80
-  __DATA_DIRTY.__objc_data: 0x250
-  __DATA_DIRTY.__data: 0x2e78
-  __DATA_DIRTY.__bss: 0x2180
-  __DATA_DIRTY.__common: 0x20
+  __AUTH_CONST.__auth_got: 0x2b40
+  __AUTH.__objc_data: 0x1a0
+  __AUTH.__data: 0x1a38
+  __DATA.__data: 0x2920
+  __DATA.__bss: 0x5f20
+  __DATA.__common: 0x20
+  __DATA_DIRTY.__objc_data: 0x2f0
+  __DATA_DIRTY.__data: 0x3700
+  __DATA_DIRTY.__bss: 0x2900
+  __DATA_DIRTY.__common: 0x80
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/EventKit.framework/EventKit

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/GenerativeSearch.framework/GenerativeSearch
   - /System/Library/PrivateFrameworks/HybridDatabase.framework/HybridDatabase
+  - /System/Library/PrivateFrameworks/HybridSearch.framework/HybridSearch
   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary
   - /System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices
   - /System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/ProactiveDaemonSupport

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12043
+  Functions: 12246
   Symbols:   374
-  CStrings:  955
+  CStrings:  960
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_types2 : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
Symbols:
+ _AnalyticsSendEventSync
+ __exit
- _objc_release_x12
- _swift_runtimeSupportsNoncopyableTypes
CStrings:
+ "FTSRetokenizeTask"
+ "HybridIndex incremental FTS retokenize succeeded."
+ "Safety check completed: verdict=%{sensitive}s for requestIdentifier: %{public}s"
+ "Start HybridIndex incremental FTS retokenize."
+ "Truncated oversized FTS content: %{public}ld → %{public}ld chars"
+ "com.apple.GenerativeSearch.PeriodicTasks.FTSRetokenizeTask"
+ "com.apple.HybridSearch.search.safetyVerdict"
+ "perform(text:checkSafety:safetyThreshold:safetyBlockingDisabled:embeddingModelProperties:contextLength:allowTruncation:sendAnalyticsEvent:)"
- "Safety Block: query deemed unsafe (score=%f, threshold=%f) for requestIdentifier: %{public}s"
- "_kMDItemIsTwoFactorCode"
- "perform(text:checkSafety:safetyThreshold:embeddingModelProperties:contextLength:allowTruncation:)"

```
