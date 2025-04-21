## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

```diff

-2171.120.30.0.4
-  __TEXT.__text: 0x9f084
+2171.120.44.0.1
+  __TEXT.__text: 0x9fcd8
   __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0x7694
-  __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x147f2
-  __TEXT.__oslogstring: 0xb874
-  __TEXT.__gcc_except_tab: 0x6e0
+  __TEXT.__objc_methlist: 0x76cc
+  __TEXT.__const: 0x138
+  __TEXT.__cstring: 0x1485d
+  __TEXT.__oslogstring: 0xb941
+  __TEXT.__gcc_except_tab: 0x750
   __TEXT.__dlopen_cstrs: 0x41
-  __TEXT.__unwind_info: 0x16b0
+  __TEXT.__unwind_info: 0x16e0
   __TEXT.__objc_classname: 0x700
-  __TEXT.__objc_methname: 0x14b23
-  __TEXT.__objc_methtype: 0xf19
-  __TEXT.__objc_stubs: 0xe320
-  __DATA_CONST.__got: 0x870
-  __DATA_CONST.__const: 0x2208
+  __TEXT.__objc_methname: 0x14c53
+  __TEXT.__objc_methtype: 0xf66
+  __TEXT.__objc_stubs: 0xe3a0
+  __DATA_CONST.__got: 0x888
+  __DATA_CONST.__const: 0x2260
   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x41e8
+  __DATA_CONST.__objc_selrefs: 0x4210
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0xa8
   __AUTH_CONST.__auth_got: 0x460
   __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__cfstring: 0x122c0
+  __AUTH_CONST.__cfstring: 0x12340
   __AUTH_CONST.__objc_const: 0xa190
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2926
-  Symbols:   9915
-  CStrings:  6371
+  Functions: 2936
+  Symbols:   9947
+  CStrings:  6385
 
Symbols:
+ +[MAAutoAsset(SUCoreBorderMAAutoAsset) SUCoreBorder_stageDetermineGroupsAvailableForUpdate:timeoutSecs:completion:]
+ +[SUCoreSpace checkPurgeableSpaceOffloadApps:cacheDeleteUrgency:onlyAvailableBySkippingLaunchCheck:withCompletionQueue:completion:]
+ +[SUCoreSpace checkPurgeableSpaceOffloadApps:fromBasePath:cacheDeleteUrgency:onlyAvailableBySkippingLaunchCheck:withCompletionQueue:completion:]
+ -[SUCoreDocumentation encodedUIBundlePath].cold.3
+ -[SUCoreScan _psusDetermineTimeout]
+ -[SUCoreUpdateDownloader _psusStageTimeout]
+ GCC_except_table69
+ GCC_except_table76
+ GCC_except_table98
+ _NSRunLoopCommonModes
+ __MSUPreferencesCopyValue
+ ___115+[MAAutoAsset(SUCoreBorderMAAutoAsset) SUCoreBorder_stageDetermineGroupsAvailableForUpdate:timeoutSecs:completion:]_block_invoke
+ ___115+[MAAutoAsset(SUCoreBorderMAAutoAsset) SUCoreBorder_stageDetermineGroupsAvailableForUpdate:timeoutSecs:completion:]_block_invoke_2
+ ___139+[MAAutoAsset(SUCoreBorderMAAutoAsset) SUCoreBorder_stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]_block_invoke
+ ___139+[MAAutoAsset(SUCoreBorderMAAutoAsset) SUCoreBorder_stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]_block_invoke_2
+ ___144+[SUCoreSpace checkPurgeableSpaceOffloadApps:fromBasePath:cacheDeleteUrgency:onlyAvailableBySkippingLaunchCheck:withCompletionQueue:completion:]_block_invoke
+ ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke.513
+ ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke_2.514
+ ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke.443
+ ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke_3
+ ___63+[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]_block_invoke.508
+ ___block_descriptor_48_e8_32bs_e17_v16?0"NSTimer"8ls32l8
+ ___block_descriptor_56_e8_32bs40r48r_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24lr40l8r48l8s32l8
+ ___block_descriptor_65_e8_32s40s48bs_e48_v28?0B8"ASDPurgeableAppResponse"12"NSError"20ls48l8s32l8s40l8
+ _kMobileSoftwareUpdatePreSUStagingDetermineTimeoutKey
+ _kMobileSoftwareUpdatePreSUStagingStageTimeoutKey
+ _kSUCoreNotificationPreSUStagingOperationTimedOut
+ _objc_msgSend$SUCoreBorder_stageDetermineGroupsAvailableForUpdate:timeoutSecs:completion:
+ _objc_msgSend$_psusDetermineTimeout
+ _objc_msgSend$_psusStageTimeout
+ _objc_msgSend$checkPurgeableSpaceOffloadApps:fromBasePath:cacheDeleteUrgency:onlyAvailableBySkippingLaunchCheck:withCompletionQueue:completion:
+ _objc_msgSend$errorUserInfo
+ _objc_msgSend$purgeableApps
+ _objc_msgSend$timerWithTimeInterval:repeats:block:
- +[MAAutoAsset(SUCoreBorderMAAutoAsset) SUCoreBorder_stageDetermineGroupsAvailableForUpdate:completion:]
- GCC_except_table97
- ___109+[SUCoreSpace checkPurgeableSpaceOffloadApps:fromBasePath:cacheDeleteUrgency:withCompletionQueue:completion:]_block_invoke
- ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke.510
- ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke_2.511
- ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke.439
- ___63+[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]_block_invoke.514
- ___block_descriptor_64_e8_32s40s48bs_e48_v28?0B8"ASDPurgeableAppResponse"12"NSError"20ls48l8s32l8s40l8
- __os_feature_enabled_impl
- _objc_msgSend$SUCoreBorder_stageDetermineGroupsAvailableForUpdate:completion:
- _objc_msgSend$setPerformAvailablityCheck:
- _objc_msgSend$stringByAppendingPathExtension:
CStrings:
+ "%@ timed out after %ld Secs"
+ "%@ timed out after %lf Secs"
+ "1.0.4"
+ "@40@0:8@16d24@?32"
+ "@52@0:8@16B24q28@?36@?44"
+ "SUCoreBorder_stageDetermineGroupsAvailableForUpdate:timeoutSecs:completion:"
+ "[DOCUMENTATION] Failed to determine encoded UI bundle path due to missing file name"
+ "[DOCUMENTATION] Failed to load update bundle at URL: %{public}@"
+ "[DOCUMENTATION] Loading bundle with localBundleURL:%{public}@ encodedUIBundleFileName:%{public}@"
+ "[DOCUMENTATION] No encoded UI bundle path was found within the update bundle."
+ "[PreSUStaging] purge after a timeout: %@"
+ "[SPACE] app offload purgeable (onlyAvailableBySkippingLaunchCheck:%d) space %lld bytes"
+ "_psusDetermineTimeout"
+ "_psusStageTimeout"
+ "checkPurgeableSpaceOffloadApps:cacheDeleteUrgency:onlyAvailableBySkippingLaunchCheck:withCompletionQueue:completion:"
+ "checkPurgeableSpaceOffloadApps:fromBasePath:cacheDeleteUrgency:onlyAvailableBySkippingLaunchCheck:withCompletionQueue:completion:"
+ "com.apple.SUCore.PSUS.TimedOut"
+ "d16@0:8"
+ "errorUserInfo"
+ "hang"
+ "purgeableApps"
+ "timerWithTimeInterval:repeats:block:"
+ "v52@0:8Q16q24B32@36@?44"
+ "v60@0:8Q16@24q32B40@44@?52"
- "1.0.3"
- "AdoptTVOSUpdate"
- "PineBoard"
- "SUCoreBorder_stageDetermineGroupsAvailableForUpdate:completion:"
- "[DOCUMENTATION] Failed to determine encoded UI bundle path due to no preferences file name"
- "[DOCUMENTATION] No encoded UI bundle path was found at: %{public}@"
- "[SPACE] app offload purgeable space %lld bytes"
- "setPerformAvailablityCheck:"
- "stringByAppendingPathExtension:"
- "v52@0:8@16B24q28@?36@?44"

```
