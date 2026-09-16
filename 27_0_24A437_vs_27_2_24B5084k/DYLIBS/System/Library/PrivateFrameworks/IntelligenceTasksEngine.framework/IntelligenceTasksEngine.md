## IntelligenceTasksEngine

> `/System/Library/PrivateFrameworks/IntelligenceTasksEngine.framework/IntelligenceTasksEngine`

```diff

-250.0.0.3.0
-  __TEXT.__text: 0x1f0d0
+255.0.2.0.0
+  __TEXT.__text: 0x2445c
   __TEXT.__objc_methlist: 0x14c
-  __TEXT.__const: 0xf58
-  __TEXT.__oslogstring: 0xc69
-  __TEXT.__constg_swiftt: 0x528
-  __TEXT.__swift5_typeref: 0x758
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0x359
-  __TEXT.__swift5_fieldmd: 0x480
-  __TEXT.__swift5_types: 0x58
-  __TEXT.__swift5_assocty: 0x68
-  __TEXT.__swift5_capture: 0x3cc
-  __TEXT.__cstring: 0x523
+  __TEXT.__const: 0x1188
+  __TEXT.__oslogstring: 0xce9
+  __TEXT.__constg_swiftt: 0x5e0
+  __TEXT.__swift5_typeref: 0x7de
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_reflstr: 0x379
+  __TEXT.__swift5_fieldmd: 0x518
+  __TEXT.__swift5_assocty: 0x80
+  __TEXT.__swift5_proto: 0x8c
+  __TEXT.__swift5_types: 0x60
+  __TEXT.__swift5_capture: 0x56c
+  __TEXT.__cstring: 0x603
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__swift5_proto: 0x7c
-  __TEXT.__swift_as_entry: 0xb8
-  __TEXT.__swift_as_ret: 0xc4
-  __TEXT.__swift_as_cont: 0x140
+  __TEXT.__swift_as_entry: 0xe8
+  __TEXT.__swift_as_ret: 0xe8
+  __TEXT.__swift_as_cont: 0x170
   __TEXT.__swift5_acfuncs: 0x28
-  __TEXT.__unwind_info: 0xa08
-  __TEXT.__eh_frame: 0x18f4
+  __TEXT.__unwind_info: 0xb68
+  __TEXT.__eh_frame: 0x1ce4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x270
+  __DATA_CONST.__objc_selrefs: 0x2b0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x11f0
+  __AUTH_CONST.__const: 0x1638
   __AUTH_CONST.__objc_const: 0x578
-  __AUTH_CONST.__auth_got: 0x7d8
+  __AUTH_CONST.__auth_got: 0x858
   __AUTH.__objc_data: 0x98
   __AUTH.__data: 0x218
-  __DATA.__data: 0x340
+  __DATA.__data: 0x370
   __DATA.__common: 0x20
   __DATA_DIRTY.__data: 0x2e8
   __DATA_DIRTY.__bss: 0x80

   - /System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
+  - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary
   - /System/Library/PrivateFrameworks/IntelligenceTasks.framework/IntelligenceTasks
   - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
   - /System/Library/PrivateFrameworks/XPCDistributed.framework/XPCDistributed

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 890
-  Symbols:   594
-  CStrings:  86
+  Functions: 1007
+  Symbols:   625
+  CStrings:  93
 
Symbols:
+ ___swift_allocate_boxed_opaque_existential_1
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ ___swift_mutable_project_boxed_opaque_existential_1
+ __objc_autoreleasePoolPop
+ __objc_autoreleasePoolPush
+ __swiftEmptySetSingleton
+ _associated conformance So21BMDataProtectionClassVSHSCSQ
+ _objc_msgSend$configuration
+ _objc_msgSend$disableResultStreaming
+ _objc_msgSend$executePruningPolicyForAccount:includeStorageCleanup:
+ _objc_msgSend$poll
+ _objc_msgSend$protectionClass
+ _objc_msgSend$queryContext
+ _objc_msgSend$setDisableResultStreaming:
+ _objc_msgSend$storeConfig
+ _swift_getAssociatedConformanceWitness
+ _swift_getAssociatedTypeWitness
+ _swift_makeBoxUnique
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _symbolic So13CSSearchQueryCSgXw
+ _symbolic So13CSSearchQueryCSgXwz_Xx
+ _symbolic So9BMAccountCSg
+ _symbolic Su
+ _symbolic _____ 23IntelligenceTasksEngine010BackgroundB0O16ExpeditedPruningO
+ _symbolic _____ 23IntelligenceTasksEngine010BackgroundB0O16ExpeditedPruningO16ProtectionClassAV
+ _symbolic _____ 23IntelligenceTasksEngine010BackgroundB0O16ExpeditedPruningO16ProtectionClassBV
+ _symbolic _____ 23IntelligenceTasksEngine010BackgroundB0O16ExpeditedPruningO16ProtectionClassCV
+ _symbolic _____ 23IntelligenceTasksEngine13LibraryLoaderO
+ _symbolic _____ So21BMDataProtectionClassV
+ _symbolic _____ySo9BMAccountCSgG s23_ContiguousArrayStorageC
+ _symbolic _____y_____G s11_SetStorageC So21BMDataProtectionClassV
- _swift_retain_x28
- _symbolic So13CSSearchQueryC
CStrings:
+ "%{public}s: no stream for %{public}s"
+ "%{public}s: pruning %{public}s"
+ "ExpeditedPruning: running %{public}s"
+ "com.apple.intelligencetasksd.streams.prune.expedited.A"
+ "com.apple.intelligencetasksd.streams.prune.expedited.B"
+ "com.apple.intelligencetasksd.streams.prune.expedited.C"
+ "kMDItemRecipientEmailAddresses"
```
