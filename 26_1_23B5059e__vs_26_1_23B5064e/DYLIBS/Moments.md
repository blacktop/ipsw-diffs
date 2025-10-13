## Moments

> `/System/Library/PrivateFrameworks/Moments.framework/Moments`

```diff

-302.0.10.0.0
-  __TEXT.__text: 0x57428
+302.0.12.0.0
+  __TEXT.__text: 0x576e0
   __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x6334
+  __TEXT.__objc_methlist: 0x634c
   __TEXT.__cstring: 0xd2b3
   __TEXT.__const: 0x3d0
-  __TEXT.__oslogstring: 0x4e14
+  __TEXT.__oslogstring: 0x4e41
   __TEXT.__gcc_except_tab: 0x464
-  __TEXT.__unwind_info: 0x1230
+  __TEXT.__unwind_info: 0x1240
   __TEXT.__objc_classname: 0x90a
-  __TEXT.__objc_methname: 0xeb87
-  __TEXT.__objc_methtype: 0x18f0
-  __TEXT.__objc_stubs: 0x83e0
+  __TEXT.__objc_methname: 0xebde
+  __TEXT.__objc_methtype: 0x191c
+  __TEXT.__objc_stubs: 0x8400
   __DATA_CONST.__got: 0x6b0
   __DATA_CONST.__const: 0x3218
   __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3050
+  __DATA_CONST.__objc_selrefs: 0x3060
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x260
   __DATA_CONST.__objc_arraydata: 0x378
   __AUTH_CONST.__auth_got: 0x390
   __AUTH_CONST.__const: 0x320
   __AUTH_CONST.__cfstring: 0xffa0
-  __AUTH_CONST.__objc_const: 0xa478
+  __AUTH_CONST.__objc_const: 0xa480
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F2F5ED4A-DF04-3B96-B125-4AABAB02C912
-  Functions: 2319
-  Symbols:   8752
-  CStrings:  7293
+  UUID: CDFE2D49-CB3D-3D72-A69A-EEFEBD54A78D
+  Functions: 2323
+  Symbols:   8761
+  CStrings:  7297
 
Symbols:
+ -[MOPromptManager testNotificationAnalyticsWithHandler:]
+ ___119-[MOPromptManager fetchEventBundlesWithAllowedSourceTypes:dateInterval:ascending:limit:respectOnboardingDates:handler:]_block_invoke.225
+ ___143-[MOPromptManager fetchEventBundlesWithAllowedSourceTypes:dateInterval:ascending:limit:respectOnboardingDates:respectLearnFromThisApp:handler:]_block_invoke.227
+ ___39-[MOPromptManager storeEvents:handler:]_block_invoke.210
+ ___42-[MOPromptManager clearEventsWithHandler:]_block_invoke.239
+ ___42-[MOPromptManager dumpDBStateWithHandler:]_block_invoke.260
+ ___42-[MOPromptManager purgeEventsWithHandler:]_block_invoke.242
+ ___43-[MOPromptManager _purgeEventsWithHandler:]_block_invoke.238
+ ___43-[MOPromptManager bundleEventsWithHandler:]_block_invoke.241
+ ___43-[MOPromptManager runAnalyticsWithHandler:]_block_invoke.243
+ ___44-[MOPromptManager collectEventsWithHandler:]_block_invoke.240
+ ___49-[MOPromptManager analyzeTrendsInEvents:handler:]_block_invoke.244
+ ___50-[MOPromptManager fetchEventsWithOptions:handler:]_block_invoke.212
+ ___50-[MOPromptManager printOnboardingStatusAnalytics:]_block_invoke.263
+ ___54-[MOPromptManager getDiagnosticReporterConfiguration:]_block_invoke.258
+ ___54-[MOPromptManager printSettingValue:withType:handler:]_block_invoke.262
+ ___54-[MOPromptManager scheduleDatabaseUpgradeWithHandler:]_block_invoke.208
+ ___54-[MOPromptManager setUpNotificationTimerWithFireDate:]_block_invoke.271
+ ___54-[MOPromptManager setUpNotificationTimerWithFireDate:]_block_invoke.271.cold.1
+ ___56-[MOPromptManager fetchEventBundlesWithOptions:handler:]_block_invoke.221
+ ___56-[MOPromptManager fetchEventBundlesWithOptions:handler:]_block_invoke.222
+ ___56-[MOPromptManager testNotificationAnalyticsWithHandler:]_block_invoke
+ ___56-[MOPromptManager testNotificationAnalyticsWithHandler:]_block_invoke_2
+ ___56-[MOPromptManager testNotificationAnalyticsWithHandler:]_block_invoke_3
+ ___56-[MOPromptManager triggerFeedbackAssistantFlow:handler:]_block_invoke.268
+ ___57-[MOPromptManager fetchEligiblePOICategoriesWithHandler:]_block_invoke.274
+ ___57-[MOPromptManager printEvergreenBundlesWithSeed:handler:]_block_invoke.255
+ ___58-[MOPromptManager fetchEventBundlesWithPredicate:handler:]_block_invoke.220
+ ___61-[MOPromptManager uploadFeedbackWithDBStateToServer:handler:]_block_invoke.248
+ ___62-[MOPromptManager generateAvailabilityPredictionsWithHandler:]_block_invoke.269
+ ___62-[MOPromptManager refreshEventsWithRefreshVariant:andHandler:]_block_invoke.245
+ ___64-[MOPromptManager getSnapshotDictionaryForAnalyticsWithHandler:]_block_invoke.261
+ ___78-[MOPromptManager acquireBackgroundProcessingPermissionsForMomentsWithHander:]_block_invoke.276
+ ___78-[MOPromptManager generateAvailabilityPredictionsAndRegisterTimerWithHandler:]_block_invoke.270
+ ___87-[MOPromptManager softRefreshEventsWithRefreshVariant:andIgnoreLastTrigger:andHandler:]_block_invoke.246
+ ___block_literal_global.237
+ ___block_literal_global.273
+ _objc_msgSend$testNotificationAnalyticsWithContext:andHandler:
- ___119-[MOPromptManager fetchEventBundlesWithAllowedSourceTypes:dateInterval:ascending:limit:respectOnboardingDates:handler:]_block_invoke.223
- ___143-[MOPromptManager fetchEventBundlesWithAllowedSourceTypes:dateInterval:ascending:limit:respectOnboardingDates:respectLearnFromThisApp:handler:]_block_invoke.225
- ___39-[MOPromptManager storeEvents:handler:]_block_invoke.208
- ___42-[MOPromptManager clearEventsWithHandler:]_block_invoke.237
- ___42-[MOPromptManager dumpDBStateWithHandler:]_block_invoke.258
- ___42-[MOPromptManager purgeEventsWithHandler:]_block_invoke.240
- ___43-[MOPromptManager _purgeEventsWithHandler:]_block_invoke.236
- ___43-[MOPromptManager bundleEventsWithHandler:]_block_invoke.239
- ___43-[MOPromptManager runAnalyticsWithHandler:]_block_invoke.241
- ___44-[MOPromptManager collectEventsWithHandler:]_block_invoke.238
- ___49-[MOPromptManager analyzeTrendsInEvents:handler:]_block_invoke.242
- ___50-[MOPromptManager fetchEventsWithOptions:handler:]_block_invoke.210
- ___50-[MOPromptManager printOnboardingStatusAnalytics:]_block_invoke.261
- ___54-[MOPromptManager getDiagnosticReporterConfiguration:]_block_invoke.254
- ___54-[MOPromptManager printSettingValue:withType:handler:]_block_invoke.260
- ___54-[MOPromptManager scheduleDatabaseUpgradeWithHandler:]_block_invoke.206
- ___54-[MOPromptManager setUpNotificationTimerWithFireDate:]_block_invoke.269
- ___54-[MOPromptManager setUpNotificationTimerWithFireDate:]_block_invoke.269.cold.1
- ___56-[MOPromptManager fetchEventBundlesWithOptions:handler:]_block_invoke.219
- ___56-[MOPromptManager fetchEventBundlesWithOptions:handler:]_block_invoke.220
- ___56-[MOPromptManager triggerFeedbackAssistantFlow:handler:]_block_invoke.266
- ___57-[MOPromptManager fetchEligiblePOICategoriesWithHandler:]_block_invoke.272
- ___57-[MOPromptManager printEvergreenBundlesWithSeed:handler:]_block_invoke.253
- ___58-[MOPromptManager fetchEventBundlesWithPredicate:handler:]_block_invoke.218
- ___61-[MOPromptManager uploadFeedbackWithDBStateToServer:handler:]_block_invoke.246
- ___62-[MOPromptManager generateAvailabilityPredictionsWithHandler:]_block_invoke.267
- ___62-[MOPromptManager refreshEventsWithRefreshVariant:andHandler:]_block_invoke.243
- ___64-[MOPromptManager getSnapshotDictionaryForAnalyticsWithHandler:]_block_invoke.259
- ___78-[MOPromptManager acquireBackgroundProcessingPermissionsForMomentsWithHander:]_block_invoke.274
- ___78-[MOPromptManager generateAvailabilityPredictionsAndRegisterTimerWithHandler:]_block_invoke.268
- ___87-[MOPromptManager softRefreshEventsWithRefreshVariant:andIgnoreLastTrigger:andHandler:]_block_invoke.244
- ___block_literal_global.227
- ___block_literal_global.271
CStrings:
+ "calling testNotificationAnalyticsWithHandler"
+ "testNotificationAnalyticsWithContext:andHandler:"
+ "testNotificationAnalyticsWithHandler:"
+ "v32@0:8@\"MOXPCContext\"16@?<v@?@\"NSError\">24"

```
