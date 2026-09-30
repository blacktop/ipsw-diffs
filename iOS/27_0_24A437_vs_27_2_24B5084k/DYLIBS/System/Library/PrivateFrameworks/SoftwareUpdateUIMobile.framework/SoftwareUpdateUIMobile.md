## SoftwareUpdateUIMobile

> `/System/Library/PrivateFrameworks/SoftwareUpdateUIMobile.framework/SoftwareUpdateUIMobile`

```diff

-772.0.20.0.0
-  __TEXT.__text: 0x7c568
-  __TEXT.__objc_methlist: 0x2864
+772.40.11.0.0
+  __TEXT.__text: 0x7e95c
+  __TEXT.__objc_methlist: 0x287c
   __TEXT.__const: 0x450
-  __TEXT.__cstring: 0x4a27
-  __TEXT.__oslogstring: 0x8418
-  __TEXT.__gcc_except_tab: 0x1464
+  __TEXT.__cstring: 0x52f7
+  __TEXT.__oslogstring: 0x8558
+  __TEXT.__gcc_except_tab: 0x149c
   __TEXT.__constg_swiftt: 0xf0
   __TEXT.__swift5_typeref: 0x235
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x1560
+  __TEXT.__unwind_info: 0x15a0
   __TEXT.__eh_frame: 0x388
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9300
+  __DATA_CONST.__const: 0x93a0
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18f8
+  __DATA_CONST.__objc_selrefs: 0x1910
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__got: 0x918

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1160
-  Symbols:   2604
-  CStrings:  693
+  Functions: 1168
+  Symbols:   2620
+  CStrings:  772
 
Symbols:
+ -[SUUIMobileScanOperation useCachedScanResultsIfAvailableForEventInfo:activity:completion:]
+ -[SUUIMobileScanOperation waitForControllerIdleThenScanForEventInfo:activity:]
+ GCC_except_table116
+ GCC_except_table118
+ GCC_except_table120
+ GCC_except_table130
+ GCC_except_table20
+ GCC_except_table22
+ GCC_except_table24
+ GCC_except_table27
+ GCC_except_table29
+ GCC_except_table30
+ GCC_except_table31
+ GCC_except_table38
+ GCC_except_table42
+ GCC_except_table44
+ GCC_except_table59
+ GCC_except_table65
+ GCC_except_table78
+ GCC_except_table79
+ GCC_except_table85
+ GCC_except_table88
+ ___78-[SUUIMobileScanOperation waitForControllerIdleThenScanForEventInfo:activity:]_block_invoke
+ ___91-[SUUIMobileScanOperation useCachedScanResultsIfAvailableForEventInfo:activity:completion:]_block_invoke
+ ___block_descriptor_64_e8_32s40r48w_e8_v12?0B8lw48l8s32l8r40l8
+ ___block_descriptor_64_e8_32s40w_e20_v20?0B8"NSError"12lw40l8s32l8
+ ___block_descriptor_64_e8_32s40w_e8_v12?0B8lw40l8s32l8
+ ___block_descriptor_66_e8_32s40s48w_e20_v20?0B8"NSError"12lw48l8s32l8s40l8
+ ___block_descriptor_73_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48bs56w_e8_v12?0B8lw56l8s48l8s32l8s40l8
+ ___os_log_helper_16_2_3_8_32_8_32_8_66
+ ___os_log_helper_16_2_3_8_32_8_66_8_34
+ _objc_msgSend$isDownloadOnly
+ _objc_msgSend$useCachedScanResultsIfAvailableForEventInfo:activity:completion:
+ _objc_msgSend$waitForControllerIdleThenScanForEventInfo:activity:
- GCC_except_table111
- GCC_except_table113
- GCC_except_table115
- GCC_except_table125
- GCC_except_table21
- GCC_except_table32
- GCC_except_table43
- GCC_except_table46
- GCC_except_table49
- GCC_except_table54
- GCC_except_table57
- GCC_except_table70
- GCC_except_table72
- GCC_except_table73
- GCC_except_table82
- GCC_except_table83
- GCC_except_table86
- ___block_descriptor_65_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
- ___block_descriptor_72_e8_32s40s48r56w_e8_v12?0B8lw56l8s32l8r48l8s40l8
CStrings:
+ "%s [%{public}@|%{public}@]: A concurrent controller scan populated the cache while we waited; served the request from cache. Skipping the redundant full scan."
+ "%s [%{public}@|%{public}@]: Cache inconsistent with controller - invalidating and performing full scan"
+ "%s [->%{public}@]: Updated in-progress download options for downloadAndInstall: %{BOOL}d; error: %{public}@"
+ "%s: %s is nil in %{public}@. Stopping."
+ "%s: Self is nil in %{public}@ [%{public}s]. Stopping."
+ "-[SUUIMobileScanOperation useCachedScanResultsIfAvailableForEventInfo:activity:completion:]_block_invoke"
+ "-[SUUIMobileScanOperation waitForControllerIdleThenScanForEventInfo:activity:]_block_invoke"
+ "DDM-declaration task"
+ "MDM-restrictions task"
+ "authentication-context reply"
+ "authentication-context work hop"
+ "auto-install cancelation delegate notification"
+ "auto-install cancelation dispatch"
+ "auto-install consent reply"
+ "auto-install expiry delegate notification"
+ "auto-install expiry dispatch"
+ "auto-update-scheduled task"
+ "beta-programs task"
+ "cache-consistency reply"
+ "cached-scan-results reply"
+ "cancelation callback dispatch"
+ "cancelation handler dispatch"
+ "clearing-space delegate notification"
+ "clearing-space dispatch"
+ "clearing-space reply"
+ "controller descriptors reply"
+ "controller scan reply"
+ "controller-idle wait reply"
+ "current-auto-install-operation reply"
+ "current-download reply"
+ "download results dispatch"
+ "download-and-schedule results dispatch"
+ "download-constraints prompt dispatch"
+ "download-constraints reply"
+ "download-constraints work hop"
+ "download-failure dispatch"
+ "download-finish delegate notification"
+ "download-invalidated dispatch"
+ "download-options reclassification reply"
+ "download-progress delegate notification"
+ "download-progress dispatch"
+ "download-start delegate notification"
+ "full-scan results dispatch"
+ "install reply"
+ "install-finish delegate notification"
+ "install-now results dispatch"
+ "install-start delegate notification"
+ "install-tonight unscheduled dispatch"
+ "keybag prompt dispatch"
+ "metadata task-group join"
+ "network-change dispatch"
+ "passcode reply"
+ "passcode work hop"
+ "post-idle cache re-check dispatch"
+ "post-idle cached-scan-results reply"
+ "post-start download reply"
+ "purge confirmation dispatch"
+ "purge confirmation reply"
+ "purge confirmation work hop"
+ "ready-for-installation reply"
+ "refresh-scan results dispatch"
+ "rollback restart approval reply"
+ "rollback restart request dispatch"
+ "rollback restart response dispatch"
+ "rollback-eligibility task"
+ "rollback-status task"
+ "scan-finished dispatch"
+ "scan-guard success (download)"
+ "scan-guard success (install)"
+ "scan-guard success (schedule)"
+ "schedule-only results dispatch"
+ "self"
+ "start-download reply"
+ "terms download-options update reply"
+ "terms presentation dispatch"
+ "terms reply"
+ "terms work hop"
+ "unattended purge reply"
+ "updates-downloadable reply"
+ "user-confirmed purge reply"
+ "user-promotion reply"
+ "user-promotion results dispatch"
- "%s [%{public}@|%{public}@]: Cache inconsistent with controller — invalidating and performing full scan"
- "%s: Self is nil in %{public}@. Stopping."
- "-[SUUIMobileStatefulUIManager client:downloadProgressDidChange:]"
```
