## MDM

> `/System/Library/PrivateFrameworks/MDM.framework/MDM`

```diff

-52.0.0.0.0
-  __TEXT.__text: 0x55dc8
-  __TEXT.__auth_stubs: 0xf70
-  __TEXT.__objc_methlist: 0x417c
+54.0.0.0.0
+  __TEXT.__text: 0x55e68
+  __TEXT.__auth_stubs: 0xf50
+  __TEXT.__objc_methlist: 0x4194
   __TEXT.__const: 0x1a2
-  __TEXT.__gcc_except_tab: 0x1148
-  __TEXT.__cstring: 0x5592
-  __TEXT.__oslogstring: 0x6ccb
+  __TEXT.__gcc_except_tab: 0x114c
+  __TEXT.__cstring: 0x55a2
+  __TEXT.__oslogstring: 0x6d9f
   __TEXT.__dlopen_cstrs: 0x55
   __TEXT.__swift5_typeref: 0x3c
   __TEXT.__swift5_capture: 0x68

   __TEXT.__unwind_info: 0x1218
   __TEXT.__eh_frame: 0x178
   __TEXT.__objc_classname: 0x6c4
-  __TEXT.__objc_methname: 0xeb32
+  __TEXT.__objc_methname: 0xeb37
   __TEXT.__objc_methtype: 0x1b90
   __TEXT.__objc_stubs: 0xb9a0
-  __DATA_CONST.__got: 0x11a8
+  __DATA_CONST.__got: 0x11b0
   __DATA_CONST.__const: 0x1ee8
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x7c8
+  __AUTH_CONST.__auth_got: 0x7b8
   __AUTH_CONST.__const: 0x610
-  __AUTH_CONST.__cfstring: 0x5080
+  __AUTH_CONST.__cfstring: 0x50a0
   __AUTH_CONST.__objc_const: 0x6a40
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x138

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 2866B940-975A-3157-B8A2-8A63D9158ABF
+  UUID: A9B85237-B016-3452-8452-0C583ACA4293
   Functions: 1647
-  Symbols:   6659
-  CStrings:  4262
+  Symbols:   6658
+  CStrings:  4268
 
Symbols:
+ -[MDMDEPPushTokenManager _queue_lastPushTokenHash]
+ -[MDMDEPPushTokenManager _queue_setLastPushTokenHash:]
+ GCC_except_table14
+ GCC_except_table157
+ GCC_except_table161
+ GCC_except_table167
+ GCC_except_table171
+ GCC_except_table178
+ GCC_except_table184
+ GCC_except_table187
+ GCC_except_table189
+ GCC_except_table203
+ GCC_except_table206
+ GCC_except_table211
+ GCC_except_table222
+ GCC_except_table227
+ GCC_except_table237
+ GCC_except_table275
+ GCC_except_table282
+ GCC_except_table293
+ GCC_except_table304
+ GCC_except_table315
+ GCC_except_table319
+ GCC_except_table330
+ GCC_except_table334
+ GCC_except_table350
+ _UMUserManagerErrorDomain
+ ___118-[MDMDEPPushTokenManager _queue_syncPushTokenShouldForce:shouldScheduleRetry:reason:backgroundTask:completionHandler:]_block_invoke.36
+ ___118-[MDMDEPPushTokenManager _queue_syncPushTokenShouldForce:shouldScheduleRetry:reason:backgroundTask:completionHandler:]_block_invoke_2.37
+ ___125-[MDMDEPPushTokenManager _queue_retryPushTokenSyncAfterInterval:shouldForce:shouldScheduleRetry:shouldCallCompletion:reason:]_block_invoke.81
+ ___184-[MDMParser _performInstallApplicationRequestWithManifestURL:iTunesStoreIDObj:bundleId:flagsObj:attributes:configuration:manageChangeStr:purchaseMethodValue:personaID:completionBlock:]_block_invoke.1352
+ ___44-[MDMParser _performSetDefaultApplications:]_block_invoke.1202
+ ___53-[MDMParser _installMedia:assertion:completionBlock:]_block_invoke.1497
+ ___block_descriptor_40_e8_32bs_e28_v24?0"NSData"8"NSError"16ls32l8
+ ___block_literal_global.1048
+ ___block_literal_global.1092
+ ___block_literal_global.1109
+ ___block_literal_global.1197
+ ___block_literal_global.1199
+ ___block_literal_global.1211
+ ___block_literal_global.1376
+ ___block_literal_global.1378
+ ___block_literal_global.1416
+ ___block_literal_global.1421
+ ___block_literal_global.1488
+ _objc_msgSend$_queue_lastPushTokenHash
+ _objc_msgSend$_queue_setLastPushTokenHash:
+ _objc_msgSend$initWithFilePath:excludesFromBackup:
- GCC_except_table158
- GCC_except_table162
- GCC_except_table168
- GCC_except_table172
- GCC_except_table179
- GCC_except_table185
- GCC_except_table188
- GCC_except_table191
- GCC_except_table204
- GCC_except_table207
- GCC_except_table212
- GCC_except_table223
- GCC_except_table228
- GCC_except_table238
- GCC_except_table276
- GCC_except_table283
- GCC_except_table294
- GCC_except_table305
- GCC_except_table316
- GCC_except_table320
- GCC_except_table331
- GCC_except_table335
- GCC_except_table351
- _DMCUMUserManagerClass
- _DMCUMUserManagerErrorDomain
- ___110-[MDMWallpaperUtilities _setWallpaper:forConfigurationWithUUID:setLockScreen:setHomeScreen:completionHandler:]_block_invoke_2
- ___118-[MDMDEPPushTokenManager _queue_syncPushTokenShouldForce:shouldScheduleRetry:reason:backgroundTask:completionHandler:]_block_invoke.33
- ___118-[MDMDEPPushTokenManager _queue_syncPushTokenShouldForce:shouldScheduleRetry:reason:backgroundTask:completionHandler:]_block_invoke_2.34
- ___125-[MDMDEPPushTokenManager _queue_retryPushTokenSyncAfterInterval:shouldForce:shouldScheduleRetry:shouldCallCompletion:reason:]_block_invoke.79
- ___184-[MDMParser _performInstallApplicationRequestWithManifestURL:iTunesStoreIDObj:bundleId:flagsObj:attributes:configuration:manageChangeStr:purchaseMethodValue:personaID:completionBlock:]_block_invoke.1351
- ___44-[MDMParser _performSetDefaultApplications:]_block_invoke.1200
- ___53-[MDMParser _installMedia:assertion:completionBlock:]_block_invoke.1496
- ___57-[MDMServerCore getOrgTokenForMAIDWithCompletionHandler:]_block_invoke_2
- ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8ls56l8s32l8s40l8s48l8
- ___block_literal_global.1047
- ___block_literal_global.1091
- ___block_literal_global.1108
- ___block_literal_global.1196
- ___block_literal_global.1198
- ___block_literal_global.1210
- ___block_literal_global.1375
- ___block_literal_global.1377
- ___block_literal_global.1415
- ___block_literal_global.1420
- ___block_literal_global.1487
- _objc_msgSend$initWithFilePath:
- _objc_msgSend$lastDEPPushTokenHash
- _objc_msgSend$updateCloudConfigurationWithLastPushTokenHash:
CStrings:
+ "Device is on seed build. Skip the random delay"
+ "Failed to get lastPushTokenHash with error: %{public}@"
+ "Failed to set lastPushTokenHash with error: %{public}@"
+ "LastPushTokenHash"
+ "MDMDEPPushTokenManager: syncInterval <= 0. Syncing now"
+ "_queue_lastPushTokenHash"
+ "_queue_setLastPushTokenHash:"
+ "initWithFilePath:excludesFromBackup:"
- "initWithFilePath:"
- "lastDEPPushTokenHash"
- "updateCloudConfigurationWithLastPushTokenHash:"

```
