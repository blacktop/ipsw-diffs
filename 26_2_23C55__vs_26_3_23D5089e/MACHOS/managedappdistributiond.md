## managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

-3.2.14.2.11
-  __TEXT.__text: 0x6b0940
-  __TEXT.__auth_stubs: 0x6670
+3.3.1.0.0
+  __TEXT.__text: 0x6b2424
+  __TEXT.__auth_stubs: 0x6690
   __TEXT.__objc_stubs: 0x1aa0
   __TEXT.__objc_methlist: 0x2354
-  __TEXT.__const: 0x40270
+  __TEXT.__const: 0x40330
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_methname: 0x6814
-  __TEXT.__cstring: 0x10325
-  __TEXT.__oslogstring: 0x11d82
+  __TEXT.__cstring: 0x10595
+  __TEXT.__oslogstring: 0x11d42
   __TEXT.__objc_classname: 0x410
   __TEXT.__objc_methtype: 0x1540
   __TEXT.__gcc_except_tab: 0x518
   __TEXT.__dlopen_cstrs: 0xc8
   __TEXT.__constg_swiftt: 0x6818
-  __TEXT.__swift5_typeref: 0x5a36
-  __TEXT.__swift5_proto: 0x1724
+  __TEXT.__swift5_typeref: 0x5a3e
+  __TEXT.__swift5_proto: 0x1728
   __TEXT.__swift5_types: 0x948
-  __TEXT.__swift_as_entry: 0xad8
-  __TEXT.__swift_as_ret: 0x1624
+  __TEXT.__swift_as_entry: 0xae4
+  __TEXT.__swift_as_ret: 0x1648
   __TEXT.__swift5_protos: 0xa4
-  __TEXT.__unwind_info: 0x12198
-  __TEXT.__eh_frame: 0x38c54
-  __DATA_CONST.__auth_got: 0x3348
-  __DATA_CONST.__got: 0x1f00
+  __TEXT.__unwind_info: 0x122a0
+  __TEXT.__eh_frame: 0x38f2c
+  __DATA_CONST.__auth_got: 0x3358
+  __DATA_CONST.__got: 0x1f10
   __DATA_CONST.__auth_ptr: 0x1868
-  __DATA_CONST.__const: 0x2e218
+  __DATA_CONST.__const: 0x2e318
   __DATA_CONST.__cfstring: 0xae0
   __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_protolist: 0x170

   __DATA.__objc_selrefs: 0x1dc0
   __DATA.__objc_ivar: 0xcc
   __DATA.__objc_data: 0x20b0
-  __DATA.__data: 0xd5a0
-  __DATA.__bss: 0x2cbd0
+  __DATA.__data: 0xd590
+  __DATA.__bss: 0x2cc50
   __DATA.__common: 0xd98
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 35C15C2A-D1ED-3F31-8748-AA76513D28D0
-  Functions: 15658
-  Symbols:   3065
-  CStrings:  4231
+  UUID: B5E617CF-1C5D-30C2-A016-ADBFB2D5DEF9
+  Functions: 15714
+  Symbols:   3069
+  CStrings:  4238
 
Symbols:
+ _$s22ManagedAppDistribution9ConditionO23forceDeltaUpdateFailureyA2CmFWC
+ _$s22ManagedAppDistribution9ConditionO29forceDistributorSwitchFailureyA2CmFWC
+ _$s22ManagedAppDistribution9ConditionO8isActive8criteriaS2byXK_tF
+ _$s22ManagedAppDistribution9ConditionOMa
CStrings:
+ "Cannot Replace App"
+ "Ignoring placeholder install for presumed active install of %s"
+ "ManagedAppDistribution.SwitchingDistributor.Failure.Prompt.AppStore.Body"
+ "ManagedAppDistribution.SwitchingDistributor.Failure.Prompt.Marketplace.Body"
+ "ManagedAppDistribution.SwitchingDistributor.Failure.Prompt.Title"
+ "ManagedAppDistribution.SwitchingDistributor.Failure.Prompt.Web.Body"
+ "“@@appName@@” couldn't be replaced with a version from the App Store. Try again."
+ "“@@appName@@” couldn't be replaced with a version from “@@domain@@”. Try again."
+ "“@@appName@@” couldn't be replaced with a version from “@@marketplaceName@@”. Try again."
- "DoForceDeltaUpdateFailure"
- "[%@] Forcing failure of delta update (expect further error messages prior to expected retry with full update)…"

```
