## Moments

> `/System/Library/PrivateFrameworks/Moments.framework/Moments`

```diff

-308.0.2.0.0
-  __TEXT.__text: 0x5cd98
-  __TEXT.__auth_stubs: 0x6a0
+308.0.3.0.0
+  __TEXT.__text: 0x5d280
+  __TEXT.__auth_stubs: 0x6d0
   __TEXT.__objc_methlist: 0x634c
-  __TEXT.__cstring: 0xd2b3
+  __TEXT.__cstring: 0xd34d
   __TEXT.__const: 0x3d0
-  __TEXT.__oslogstring: 0x4e41
+  __TEXT.__oslogstring: 0x4f95
   __TEXT.__gcc_except_tab: 0x478
-  __TEXT.__unwind_info: 0x17e0
+  __TEXT.__unwind_info: 0x17e8
   __TEXT.__objc_classname: 0x90a
   __TEXT.__objc_methname: 0xebde
   __TEXT.__objc_methtype: 0x191c

   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x260
   __DATA_CONST.__objc_arraydata: 0x378
-  __AUTH_CONST.__auth_got: 0x360
+  __AUTH_CONST.__auth_got: 0x378
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0xffa0
+  __AUTH_CONST.__cfstring: 0x10000
   __AUTH_CONST.__objc_const: 0xa480
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0x570

   __AUTH.__objc_data: 0x16d0
   __DATA.__objc_ivar: 0x7a8
   __DATA.__data: 0xb98
-  __DATA.__bss: 0xd8
+  __DATA.__bss: 0xe0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__data: 0x30

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F4316D01-D82F-35F0-9195-FAC8805C9230
-  Functions: 2343
-  Symbols:   8853
-  CStrings:  7297
+  UUID: 49EE4438-A4CC-3494-B235-83AD0E3A07B1
+  Functions: 2346
+  Symbols:   8861
+  CStrings:  7309
 
Symbols:
+ +[MOPersistenceUtilities userCacheDirectoryPath].cold.3
+ +[MOPersistenceUtilities userCacheDirectoryPath].cold.4
+ _NSHomeDirectory
+ ___119-[MOPromptManager fetchEventBundlesWithAllowedSourceTypes:dateInterval:ascending:limit:respectOnboardingDates:handler:]_block_invoke.228
+ ___143-[MOPromptManager fetchEventBundlesWithAllowedSourceTypes:dateInterval:ascending:limit:respectOnboardingDates:respectLearnFromThisApp:handler:]_block_invoke.230
+ ___39-[MOConnection onConnectionInterrupted]_block_invoke.32
+ ___39-[MOPromptManager storeEvents:handler:]_block_invoke.213
+ ___42-[MOPromptManager clearEventsWithHandler:]_block_invoke.242
+ ___42-[MOPromptManager dumpDBStateWithHandler:]_block_invoke.263
+ ___42-[MOPromptManager purgeEventsWithHandler:]_block_invoke.245
+ ___43-[MOPromptManager _purgeEventsWithHandler:]_block_invoke.241
+ ___43-[MOPromptManager bundleEventsWithHandler:]_block_invoke.244
+ ___43-[MOPromptManager runAnalyticsWithHandler:]_block_invoke.246
+ ___44-[MOPromptManager collectEventsWithHandler:]_block_invoke.243
+ ___49-[MOPromptManager analyzeTrendsInEvents:handler:]_block_invoke.247
+ ___50-[MOPromptManager fetchEventsWithOptions:handler:]_block_invoke.215
+ ___50-[MOPromptManager printOnboardingStatusAnalytics:]_block_invoke.266
+ ___54-[MOPromptManager getDiagnosticReporterConfiguration:]_block_invoke.259
+ ___54-[MOPromptManager getDiagnosticReporterConfiguration:]_block_invoke.261
+ ___54-[MOPromptManager printSettingValue:withType:handler:]_block_invoke.265
+ ___54-[MOPromptManager scheduleDatabaseUpgradeWithHandler:]_block_invoke.211
+ ___54-[MOPromptManager setUpNotificationTimerWithFireDate:]_block_invoke.274
+ ___54-[MOPromptManager setUpNotificationTimerWithFireDate:]_block_invoke.274.cold.1
+ ___56-[MOPromptManager fetchEventBundlesWithOptions:handler:]_block_invoke.224
+ ___56-[MOPromptManager fetchEventBundlesWithOptions:handler:]_block_invoke.225
+ ___56-[MOPromptManager triggerFeedbackAssistantFlow:handler:]_block_invoke.271
+ ___57-[MOPromptManager fetchEligiblePOICategoriesWithHandler:]_block_invoke.277
+ ___57-[MOPromptManager printEvergreenBundlesWithSeed:handler:]_block_invoke.258
+ ___58-[MOPromptManager fetchEventBundlesWithPredicate:handler:]_block_invoke.223
+ ___61-[MOPromptManager uploadFeedbackWithDBStateToServer:handler:]_block_invoke.251
+ ___62-[MOPromptManager generateAvailabilityPredictionsWithHandler:]_block_invoke.272
+ ___62-[MOPromptManager refreshEventsWithRefreshVariant:andHandler:]_block_invoke.248
+ ___64-[MOPromptManager getSnapshotDictionaryForAnalyticsWithHandler:]_block_invoke.264
+ ___78-[MOPromptManager acquireBackgroundProcessingPermissionsForMomentsWithHander:]_block_invoke.279
+ ___78-[MOPromptManager generateAvailabilityPredictionsAndRegisterTimerWithHandler:]_block_invoke.273
+ ___87-[MOPromptManager softRefreshEventsWithRefreshVariant:andIgnoreLastTrigger:andHandler:]_block_invoke.249
+ ___block_literal_global.101
+ ___block_literal_global.232
+ ___block_literal_global.234
+ ___block_literal_global.236
+ ___block_literal_global.238
+ ___block_literal_global.240
+ ___block_literal_global.276
+ _getpid
+ _userCacheDirectoryPath._cachedUserCacheDirectoryPath
+ _usleep
- ___119-[MOPromptManager fetchEventBundlesWithAllowedSourceTypes:dateInterval:ascending:limit:respectOnboardingDates:handler:]_block_invoke.225
- ___143-[MOPromptManager fetchEventBundlesWithAllowedSourceTypes:dateInterval:ascending:limit:respectOnboardingDates:respectLearnFromThisApp:handler:]_block_invoke.227
- ___39-[MOConnection onConnectionInterrupted]_block_invoke.29
- ___39-[MOPromptManager storeEvents:handler:]_block_invoke.210
- ___42-[MOPromptManager clearEventsWithHandler:]_block_invoke.239
- ___42-[MOPromptManager dumpDBStateWithHandler:]_block_invoke.260
- ___42-[MOPromptManager purgeEventsWithHandler:]_block_invoke.242
- ___43-[MOPromptManager _purgeEventsWithHandler:]_block_invoke.238
- ___43-[MOPromptManager bundleEventsWithHandler:]_block_invoke.241
- ___43-[MOPromptManager runAnalyticsWithHandler:]_block_invoke.243
- ___44-[MOPromptManager collectEventsWithHandler:]_block_invoke.240
- ___49-[MOPromptManager analyzeTrendsInEvents:handler:]_block_invoke.244
- ___50-[MOPromptManager fetchEventsWithOptions:handler:]_block_invoke.212
- ___50-[MOPromptManager printOnboardingStatusAnalytics:]_block_invoke.263
- ___54-[MOPromptManager getDiagnosticReporterConfiguration:]_block_invoke.256
- ___54-[MOPromptManager getDiagnosticReporterConfiguration:]_block_invoke.258
- ___54-[MOPromptManager printSettingValue:withType:handler:]_block_invoke.262
- ___54-[MOPromptManager scheduleDatabaseUpgradeWithHandler:]_block_invoke.208
- ___54-[MOPromptManager setUpNotificationTimerWithFireDate:]_block_invoke.271
- ___54-[MOPromptManager setUpNotificationTimerWithFireDate:]_block_invoke.271.cold.1
- ___56-[MOPromptManager fetchEventBundlesWithOptions:handler:]_block_invoke.221
- ___56-[MOPromptManager fetchEventBundlesWithOptions:handler:]_block_invoke.222
- ___56-[MOPromptManager triggerFeedbackAssistantFlow:handler:]_block_invoke.268
- ___57-[MOPromptManager fetchEligiblePOICategoriesWithHandler:]_block_invoke.274
- ___57-[MOPromptManager printEvergreenBundlesWithSeed:handler:]_block_invoke.255
- ___58-[MOPromptManager fetchEventBundlesWithPredicate:handler:]_block_invoke.220
- ___61-[MOPromptManager uploadFeedbackWithDBStateToServer:handler:]_block_invoke.248
- ___62-[MOPromptManager generateAvailabilityPredictionsWithHandler:]_block_invoke.269
- ___62-[MOPromptManager refreshEventsWithRefreshVariant:andHandler:]_block_invoke.245
- ___64-[MOPromptManager getSnapshotDictionaryForAnalyticsWithHandler:]_block_invoke.261
- ___78-[MOPromptManager acquireBackgroundProcessingPermissionsForMomentsWithHander:]_block_invoke.276
- ___78-[MOPromptManager generateAvailabilityPredictionsAndRegisterTimerWithHandler:]_block_invoke.270
- ___87-[MOPromptManager softRefreshEventsWithRefreshVariant:andIgnoreLastTrigger:andHandler:]_block_invoke.246
- ___block_literal_global.229
- ___block_literal_global.231
- ___block_literal_global.233
- ___block_literal_global.235
- ___block_literal_global.237
- ___block_literal_global.273
- ___block_literal_global.98
CStrings:
+ "/var/mobile/Library/Caches"
+ "Attempting fallback to hardcoded path: %@"
+ "CRITICAL: NSSearchPathForDirectoriesInDomains failed after %d attempts. PID=%d, home=%@"
+ "CacheDirectoryFailure"
+ "Failed to create fallback directory %@, error: %@"
+ "NSSearchPathForDirectoriesInDomains returned empty on attempt %d, retrying (PID=%d, home=%@)"
+ "NSSearchPathForDirectoriesInDomains(NSCachesDirectory) returned empty after %d attempts. PID=%d, home=%@"
+ "Retry succeeded on attempt %d"
+ "Successfully using fallback path: %@"

```
