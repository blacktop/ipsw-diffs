## SoftwareUpdateUIFoundation

> `/System/Library/PrivateFrameworks/SoftwareUpdateUIFoundation.framework/SoftwareUpdateUIFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_reflstr`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_types2`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`

```diff

-772.0.10.0.0
-  __TEXT.__text: 0xaaa2c
-  __TEXT.__objc_methlist: 0x22cc
-  __TEXT.__cstring: 0x6a48
-  __TEXT.__gcc_except_tab: 0x2394
-  __TEXT.__oslogstring: 0xa757
-  __TEXT.__const: 0x2300
-  __TEXT.__swift5_typeref: 0x75d
+772.0.20.0.0
+  __TEXT.__text: 0xad484
+  __TEXT.__objc_methlist: 0x22f4
+  __TEXT.__const: 0x23c0
+  __TEXT.__cstring: 0x6d48
+  __TEXT.__gcc_except_tab: 0x2500
+  __TEXT.__oslogstring: 0xaab7
+  __TEXT.__swift5_typeref: 0x785
   __TEXT.__swift5_reflstr: 0x61e
-  __TEXT.__swift5_assocty: 0x468
+  __TEXT.__swift5_assocty: 0x480
   __TEXT.__constg_swiftt: 0x502
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_fieldmd: 0x418
-  __TEXT.__swift5_proto: 0x1a4
+  __TEXT.__swift5_proto: 0x1a8
   __TEXT.__swift5_types: 0x70
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_capture: 0x328

   __TEXT.__swift_as_ret: 0x38
   __TEXT.__swift_as_cont: 0x48
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0x11d8
+  __TEXT.__unwind_info: 0x1200
   __TEXT.__eh_frame: 0xb00
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x23a8
+  __DATA_CONST.__const: 0x2448
   __DATA_CONST.__objc_classlist: 0x198
-  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1568
+  __DATA_CONST.__objc_selrefs: 0x1578
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x110
-  __DATA_CONST.__got: 0x458
-  __AUTH_CONST.__const: 0x1770
-  __AUTH_CONST.__cfstring: 0x3e00
-  __AUTH_CONST.__objc_const: 0x69c0
+  __DATA_CONST.__got: 0x460
+  __AUTH_CONST.__const: 0x1790
+  __AUTH_CONST.__cfstring: 0x3f40
+  __AUTH_CONST.__objc_const: 0x6a10
   __AUTH_CONST.__objc_intobj: 0xd8
-  __AUTH_CONST.__auth_got: 0x8f8
+  __AUTH_CONST.__auth_got: 0x910
   __AUTH.__objc_data: 0xff0
   __AUTH.__data: 0x40
   __DATA.__objc_ivar: 0x300
-  __DATA.__data: 0xdf0
-  __DATA.__bss: 0x35e0
+  __DATA.__data: 0xe40
+  __DATA.__bss: 0x3670
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2071
-  Symbols:   2756
-  CStrings:  948
+  Functions: 2096
+  Symbols:   2785
+  CStrings:  967
 
Symbols:
+ +[SUUIRetryConfiguration(Presets) betaProgramsFetchConfiguration]
+ -[SDBetaManager(SUUIRetry) queryProgramsForSystemAccountsWithPlatforms:retryConfiguration:identifier:completion:]
+ GCC_except_table100
+ GCC_except_table110
+ GCC_except_table117
+ GCC_except_table127
+ GCC_except_table142
+ GCC_except_table153
+ GCC_except_table160
+ GCC_except_table165
+ GCC_except_table168
+ GCC_except_table173
+ GCC_except_table181
+ GCC_except_table186
+ GCC_except_table194
+ GCC_except_table199
+ GCC_except_table209
+ GCC_except_table214
+ GCC_except_table215
+ GCC_except_table222
+ GCC_except_table232
+ GCC_except_table235
+ GCC_except_table236
+ GCC_except_table243
+ GCC_except_table251
+ GCC_except_table256
+ GCC_except_table264
+ GCC_except_table267
+ GCC_except_table273
+ GCC_except_table337
+ GCC_except_table79
+ GCC_except_table90
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_SEED_STAGING_EXT_PRERELEASE
+ _SUUIBetaManagerErrorTypeIsTransient
+ _SoftwareUpdateUIFoundationVersionNumber
+ _SoftwareUpdateUIFoundationVersionString
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_SDBetaManager_$_SUUIRetry
+ __OBJC_$_CATEGORY_SDBetaManager_$_SUUIRetry
+ ___113-[SDBetaManager(SUUIRetry) queryProgramsForSystemAccountsWithPlatforms:retryConfiguration:identifier:completion:]_block_invoke
+ ___113-[SDBetaManager(SUUIRetry) queryProgramsForSystemAccountsWithPlatforms:retryConfiguration:identifier:completion:]_block_invoke_2
+ ___65+[SUUIRetryConfiguration(Presets) betaProgramsFetchConfiguration]_block_invoke
+ ___block_descriptor_48_e8_32bs40r_e20_v24?0"NSArray"8q16lr40l8s32l8
+ ___block_descriptor_48_e8_32bs40r_e23_v32?0q816"NSError"24ls32l8r40l8
+ ___block_descriptor_56_e8_32s40r_e26_v16?0?<v?B"NSError">8ls32l8r40l8
+ ___os_log_helper_16_2_4_8_32_8_66_8_66_8_34
+ ___os_log_helper_16_2_4_8_32_8_66_8_66_8_66
+ ___os_log_helper_16_2_5_8_32_8_66_8_0_8_0_8_0
+ ___os_log_helper_16_2_5_8_32_8_66_8_0_8_0_8_34
+ _associated conformance 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV23ProductFamilyIdentifierVs12CaseIterableAA8AllCasessAFP_Sl
+ _betaProgramsFetchConfiguration.config
+ _betaProgramsFetchConfiguration.onceToken
+ _kSUUIBetaProgramsFetchRetryTimeout
+ _kSU_A_PromoteDownload
+ _kSU_A_QueryManagerState
+ _kSU_E_BeginPromoteDownload
+ _kSU_E_PromoteDownloadFailed
+ _kSU_E_PromoteDownloadSuccess
+ _kSU_E_QueryManagerStateFailed
+ _kSU_E_QueryManagerStateSuccess
+ _kSU_E_UpdateOpPromoteToUserInitiated
+ _kSU_S_PromotingDownload
+ _kSU_S_QueryingManagerState
+ _objc_msgSend$betaProgramsFetchConfiguration
+ _objc_msgSend$executeOperation:completion:
+ _objc_msgSend$initWithConfiguration:identifier:
+ _objc_msgSend$queryProgramsForSystemAccountsWithPlatforms:retryConfiguration:identifier:completion:
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _symbolic SDySS_____G 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV12OSIdentifierV
+ _symbolic SS______t 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV12OSIdentifierV
+ _symbolic Say_____G 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV23ProductFamilyIdentifierV
- GCC_except_table107
- GCC_except_table114
- GCC_except_table124
- GCC_except_table140
- GCC_except_table151
- GCC_except_table158
- GCC_except_table159
- GCC_except_table164
- GCC_except_table171
- GCC_except_table179
- GCC_except_table184
- GCC_except_table190
- GCC_except_table197
- GCC_except_table207
- GCC_except_table210
- GCC_except_table213
- GCC_except_table220
- GCC_except_table228
- GCC_except_table233
- GCC_except_table234
- GCC_except_table241
- GCC_except_table249
- GCC_except_table252
- GCC_except_table262
- GCC_except_table265
- GCC_except_table271
- GCC_except_table335
- GCC_except_table76
- GCC_except_table87
- GCC_except_table97
- _MA_PALLAS_AUDIENCE_CUSTOMER_SEASHIP
- _MA_PALLAS_AUDIENCE_INTERNAL_SEASHIP
- ___os_log_helper_16_2_3_8_32_8_64_8_0
- ___os_log_helper_16_2_3_8_32_8_64_8_64
- ___os_log_helper_16_2_4_8_32_8_64_8_0_8_0
- ___os_log_helper_16_2_4_8_32_8_64_8_0_8_64
- ___os_log_helper_16_2_4_8_32_8_66_8_0_8_64
- ___os_log_helper_16_2_4_8_32_8_66_8_64_8_66
- ___os_log_helper_16_2_4_8_32_8_66_8_66_8_32
- ___os_log_helper_16_2_5_8_32_8_64_8_0_8_0_8_0
- ___os_log_helper_16_2_5_8_32_8_66_8_0_8_0_8_32
CStrings:
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nThere is already an update operation running (%{public}@). Ignoring promote request."
+ "%s [%{public}@]: Attempt %lu not finished, scheduling retry in %.2f seconds (next delay: %.2f)"
+ "%s [%{public}@]: Executing attempt %lu of %lu"
+ "%s [%{public}@]: Exhausted all %lu retry attempts"
+ "%s [%{public}@]: Got the device available Beta Programs (count: %ld): %{public}@"
+ "%s [%{public}@]: Ignoring addTask:%{public}@ — the group is already %{public}s."
+ "%s [%{public}@]: Operation aborted on attempt %lu with error: %{public}@"
+ "%s [%{public}@]: Operation cancelled after attempt %lu"
+ "%s [%{public}@]: Operation cancelled before attempt %lu"
+ "%s [%{public}@]: Operation finished on attempt %lu"
+ "%s [%{public}@]: Refreshed current beta program: %{public}@ (program ID: %{public}@"
+ "%s [%{public}@]: Starting retry operation with configuration: %{public}@"
+ "%s [%{public}@]: Starting with %lu task(s); wait-timeout=%.1fs; policy=%{public}s."
+ "%s: Terminal beta-programs query failure (code %ld); not retrying."
+ "%s: Transient beta-programs query failure (code %ld); retrying."
+ "-[SDBetaManager(SUUIRetry) queryProgramsForSystemAccountsWithPlatforms:retryConfiguration:identifier:completion:]_block_invoke"
+ "-[SDBetaManager(SUUIRetry) queryProgramsForSystemAccountsWithPlatforms:retryConfiguration:identifier:completion:]_block_invoke_2"
+ "-[SUUIStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:]"
+ "-[SUUIStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:]_block_invoke"
+ "165413ff-a1b0-4e64-b0a0-25ca4fa99e4a"
+ "BeginPromoteDownload"
+ "Experience reconfiguration [%{public}s]: No changes detected"
+ "Experience reconfiguration failed: Identifier mismatch. Current: '%{public}s', New: '%{public}s'"
+ "Promote to User Initiated (Install After Download)"
+ "PromoteDownload"
+ "PromoteDownloadFailed"
+ "PromoteDownloadSuccess"
+ "PromotingDownload"
+ "QueryManagerState"
+ "QueryManagerStateFailed"
+ "QueryManagerStateSuccess"
+ "QueryingManagerState"
+ "UpdateOpPromoteToUserInitiated"
+ "v16@?0@?<v@?B@@\"NSError\">8"
+ "v32@?0q8@16@\"NSError\"24"
- "%s [%@]: Attempt %lu not finished, scheduling retry in %.2f seconds (next delay: %.2f)"
- "%s [%@]: Executing attempt %lu of %lu"
- "%s [%@]: Exhausted all %lu retry attempts"
- "%s [%@]: Operation aborted on attempt %lu with error: %@"
- "%s [%@]: Operation cancelled after attempt %lu"
- "%s [%@]: Operation cancelled before attempt %lu"
- "%s [%@]: Operation finished on attempt %lu"
- "%s [%@]: Starting retry operation with configuration: %@"
- "%s [%{public}@]: Got the device available Beta Programs (count: %ld): %@"
- "%s [%{public}@]: Ignoring addTask:%{public}@ — the group is already %s."
- "%s [%{public}@]: Refreshed current beta program: %@ (program ID: %{public}@"
- "%s [%{public}@]: Starting with %lu task(s); wait-timeout=%.1fs; policy=%s."
- "Experience reconfiguration [%s]: No changes detected"
- "Experience reconfiguration failed: Identifier mismatch. Current: '%s', New: '%s'"
- "cd060049-2465-43e3-bbb5-d769a66da2d7"
- "ffc25f86-b83c-4139-b8ad-91131d0e5429"
```
