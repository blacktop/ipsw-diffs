## HybridSearchRuntime

> `/System/Library/PrivateFrameworks/HybridSearchRuntime.framework/Versions/A/HybridSearchRuntime`

```diff

-  __TEXT.__text: 0x25a904
+  __TEXT.__text: 0x267294
   __TEXT.__objc_methlist: 0x6b4
-  __TEXT.__const: 0xbbd0
-  __TEXT.__constg_swiftt: 0x3848
-  __TEXT.__swift5_typeref: 0x5aa2
+  __TEXT.__const: 0xbec0
+  __TEXT.__constg_swiftt: 0x38d8
+  __TEXT.__swift5_typeref: 0x5c02
   __TEXT.__swift5_builtin: 0x12c
-  __TEXT.__swift5_reflstr: 0x1fb0
-  __TEXT.__swift5_fieldmd: 0x2a50
+  __TEXT.__swift5_reflstr: 0x2070
+  __TEXT.__swift5_fieldmd: 0x2b20
   __TEXT.__swift5_assocty: 0xba0
-  __TEXT.__cstring: 0xe901
-  __TEXT.__swift5_capture: 0x3be8
-  __TEXT.__oslogstring: 0x6e3d
+  __TEXT.__cstring: 0xe991
+  __TEXT.__swift5_capture: 0x3dd0
+  __TEXT.__oslogstring: 0x6eed
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__swift5_proto: 0x5e8
-  __TEXT.__swift5_types: 0x448
-  __TEXT.__swift_as_entry: 0xe00
-  __TEXT.__swift_as_ret: 0x13dc
-  __TEXT.__swift_as_cont: 0x2ca0
+  __TEXT.__swift5_proto: 0x5ec
+  __TEXT.__swift5_types: 0x454
+  __TEXT.__swift_as_entry: 0xe90
+  __TEXT.__swift_as_ret: 0x1478
+  __TEXT.__swift_as_cont: 0x2cdc
   __TEXT.__swift5_protos: 0x7c
   __TEXT.__swift5_types2: 0x8
   __TEXT.__gcc_except_tab: 0x60
-  __TEXT.__unwind_info: 0x9690
-  __TEXT.__eh_frame: 0x1e5ac
+  __TEXT.__unwind_info: 0x9d60
+  __TEXT.__eh_frame: 0x1f138
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1448
+  __DATA_CONST.__objc_selrefs: 0x1458
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__got: 0x1cd0
-  __AUTH_CONST.__const: 0xd100
+  __DATA_CONST.__got: 0x1ce8
+  __AUTH_CONST.__const: 0xd770
   __AUTH_CONST.__cfstring: 0x1a0
-  __AUTH_CONST.__objc_const: 0x25e8
+  __AUTH_CONST.__objc_const: 0x2628
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x2900
-  __AUTH.__objc_data: 0x240
-  __AUTH.__data: 0x2110
-  __DATA.__data: 0x2988
-  __DATA.__bss: 0x66a0
-  __DATA.__common: 0x80
-  __DATA_DIRTY.__objc_data: 0x250
-  __DATA_DIRTY.__data: 0x2e28
-  __DATA_DIRTY.__bss: 0x2180
-  __DATA_DIRTY.__common: 0x20
+  __AUTH_CONST.__auth_got: 0x29c0
+  __AUTH.__objc_data: 0x1a0
+  __AUTH.__data: 0x1a38
+  __DATA.__data: 0x2920
+  __DATA.__bss: 0x5f20
+  __DATA.__common: 0x20
+  __DATA_DIRTY.__objc_data: 0x2f0
+  __DATA_DIRTY.__data: 0x36b0
+  __DATA_DIRTY.__bss: 0x2900
+  __DATA_DIRTY.__common: 0x80
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/EventKit.framework/Versions/A/EventKit

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/GenerativeSearch.framework/Versions/A/GenerativeSearch
   - /System/Library/PrivateFrameworks/HybridDatabase.framework/Versions/A/HybridDatabase
+  - /System/Library/PrivateFrameworks/HybridSearch.framework/Versions/A/HybridSearch
   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/Versions/A/IntelligencePlatformLibrary
   - /System/Library/PrivateFrameworks/MediaAnalysisServices.framework/Versions/A/MediaAnalysisServices
   - /System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/Versions/A/ProactiveDaemonSupport

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12037
-  Symbols:   322
-  CStrings:  962
+  Functions: 12273
+  Symbols:   323
+  CStrings:  967
 
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
