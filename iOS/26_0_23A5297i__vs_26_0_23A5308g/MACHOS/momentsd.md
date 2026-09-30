## momentsd

> `/usr/libexec/momentsd`

```diff

-277.0.0.0.0
-  __TEXT.__text: 0x24b0d8
-  __TEXT.__auth_stubs: 0x1ae0
-  __TEXT.__objc_stubs: 0x1d200
+295.0.0.0.0
+  __TEXT.__text: 0x24b2ec
+  __TEXT.__auth_stubs: 0x1ad0
+  __TEXT.__objc_stubs: 0x1d240
   __TEXT.__objc_methlist: 0x111e0
-  __TEXT.__cstring: 0x2618f
+  __TEXT.__cstring: 0x260ef
   __TEXT.__objc_classname: 0x1b58
   __TEXT.__objc_methtype: 0x315e
-  __TEXT.__objc_methname: 0x36c94
-  __TEXT.__oslogstring: 0x2ee9b
+  __TEXT.__objc_methname: 0x36cb9
+  __TEXT.__oslogstring: 0x2f09b
   __TEXT.__const: 0x1231
-  __TEXT.__gcc_except_tab: 0x7e04
+  __TEXT.__gcc_except_tab: 0x7dec
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x51
   __TEXT.__constg_swiftt: 0x5ec

   __TEXT.__swift_as_entry: 0x44
   __TEXT.__swift_as_ret: 0x4c
   __TEXT.__swift5_proto: 0xc
-  __TEXT.__unwind_info: 0x4e68
+  __TEXT.__unwind_info: 0x4e50
   __TEXT.__eh_frame: 0xa68
-  __DATA_CONST.__auth_got: 0xd88
+  __DATA_CONST.__auth_got: 0xd80
   __DATA_CONST.__got: 0xba8
   __DATA_CONST.__auth_ptr: 0x160
-  __DATA_CONST.__const: 0xb4c8
-  __DATA_CONST.__cfstring: 0x24ee0
+  __DATA_CONST.__const: 0xb4a0
+  __DATA_CONST.__cfstring: 0x24e80
   __DATA_CONST.__objc_classlist: 0x7b8
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x128

   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x5f0
   __DATA_CONST.__objc_intobj: 0x3ea0
-  __DATA_CONST.__objc_arraydata: 0x16b8
+  __DATA_CONST.__objc_arraydata: 0x16b0
   __DATA_CONST.__objc_arrayobj: 0xac8
   __DATA_CONST.__objc_doubleobj: 0x4c0
   __DATA_CONST.__objc_dictobj: 0xf0
   __DATA_CONST.__objc_floatobj: 0x250
-  __DATA.__objc_const: 0x1d2b0
-  __DATA.__objc_selrefs: 0x92b0
-  __DATA.__objc_ivar: 0x16c8
+  __DATA.__objc_const: 0x1d2d0
+  __DATA.__objc_selrefs: 0x92c0
+  __DATA.__objc_ivar: 0x16cc
   __DATA.__objc_data: 0x55c0
   __DATA.__data: 0x18c8
   __DATA.__common: 0x2e4

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BD488A65-2823-3A66-8DEF-FBDF58AFEA5D
-  Functions: 8405
-  Symbols:   59636
-  CStrings:  20618
+  UUID: FE0B3A7C-BE30-3C74-B53F-7E4B15B981FF
+  Functions: 8406
+  Symbols:   59639
+  CStrings:  20621
 
Symbols:
+ -[MOCloudKitPushNotifications apsEnvironmentString].cold.1
+ OBJC_IVAR_$_MOCloudKitPushNotifications._momentsUI
+ __37-[MOPromptMetrics getAndSetAgeGender]_block_invoke.1931
+ __45-[MOTrendsAnalyzer(Metrics) setCommonFields:]_block_invoke.606
+ __49-[MOBiomeManager _updateDataStreamWithEngagement]_block_invoke.668
+ __49-[MOHealthKitManager _rehydrateWorkouts:handler:]_block_invoke.445
+ __49-[MOHealthKitManager _rehydrateWorkouts:handler:]_block_invoke.445.cold.1
+ __49-[MOHealthKitManager _rehydrateWorkouts:handler:]_block_invoke.446
+ __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.456
+ __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.457
+ __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.457.cold.1
+ __51-[MOCloudKitPushNotifications apsEnvironmentString]_block_invoke.cold.1
+ __52-[MOHealthKitManager _rehydrateStateOfMind:handler:]_block_invoke.448
+ __52-[MOHealthKitManager _rehydrateStateOfMind:handler:]_block_invoke.448.cold.1
+ __52-[MOHealthKitManager _rehydrateStateOfMind:handler:]_block_invoke.449
+ __59-[MOCloudKitPushNotifications subscribeWithSubscriptionID:]_block_invoke.15
+ __59-[MOCloudKitPushNotifications subscribeWithSubscriptionID:]_block_invoke.20
+ __59-[MOCloudKitPushNotifications subscribeWithSubscriptionID:]_block_invoke.26
+ __59-[MOCloudKitPushNotifications subscribeWithSubscriptionID:]_block_invoke_2.23
+ __62-[MOBiomeManager donateEvents:andBundles:andOnboardingStatus:]_block_invoke.652
+ __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.682
+ __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.692
+ __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.707
+ __66-[MOHealthKitManager _rehydrateStoredEvents:fromWorkouts:handler:]_block_invoke.454
+ __69-[MOBiomeManager fetchMomentsEngagementForBundles:CompletionHandler:]_block_invoke.672
+ __82-[MOBiomeManager fetchMomentsEventDataBetweenStartDate:EndDate:CompletionHandler:]_block_invoke.675
+ __82-[MOBiomeManager fetchMomentsEventDataBetweenStartDate:EndDate:CompletionHandler:]_block_invoke_2.676
+ __91-[MOHealthKitManager _fetchWorkoutEventsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.482
+ __95-[MOHealthKitManager _fetchStateOfMindEventsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.483
+ __block_literal_global.428
+ __block_literal_global.430
+ __block_literal_global.432
+ __block_literal_global.434
+ __block_literal_global.493
+ __block_literal_global.498
+ __block_literal_global.600
+ _objc_msgSend$stringForKey:
+ _objc_msgSend$synchronize
- _NSLog
- __37-[MOPromptMetrics getAndSetAgeGender]_block_invoke.1928
- __45-[MOTrendsAnalyzer(Metrics) setCommonFields:]_block_invoke.603
- __49-[MOBiomeManager _updateDataStreamWithEngagement]_block_invoke.665
- __49-[MOHealthKitManager _rehydrateWorkouts:handler:]_block_invoke.442
- __49-[MOHealthKitManager _rehydrateWorkouts:handler:]_block_invoke.442.cold.1
- __49-[MOHealthKitManager _rehydrateWorkouts:handler:]_block_invoke.443
- __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.453
- __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.454
- __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.454.cold.1
- __52-[MOHealthKitManager _rehydrateStateOfMind:handler:]_block_invoke.445
- __52-[MOHealthKitManager _rehydrateStateOfMind:handler:]_block_invoke.445.cold.1
- __52-[MOHealthKitManager _rehydrateStateOfMind:handler:]_block_invoke.446
- __59-[MOCloudKitPushNotifications subscribeWithSubscriptionID:]_block_invoke.14
- __59-[MOCloudKitPushNotifications subscribeWithSubscriptionID:]_block_invoke.19
- __59-[MOCloudKitPushNotifications subscribeWithSubscriptionID:]_block_invoke.24
- __59-[MOCloudKitPushNotifications subscribeWithSubscriptionID:]_block_invoke_2.22
- __62-[MOBiomeManager donateEvents:andBundles:andOnboardingStatus:]_block_invoke.649
- __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.679
- __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.689
- __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.704
- __66-[MOHealthKitManager _rehydrateStoredEvents:fromWorkouts:handler:]_block_invoke.451
- __69-[MOBiomeManager fetchMomentsEngagementForBundles:CompletionHandler:]_block_invoke.669
- __82-[MOBiomeManager fetchMomentsEventDataBetweenStartDate:EndDate:CompletionHandler:]_block_invoke.672
- __82-[MOBiomeManager fetchMomentsEventDataBetweenStartDate:EndDate:CompletionHandler:]_block_invoke_2.673
- __91-[MOHealthKitManager _fetchWorkoutEventsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.479
- __95-[MOHealthKitManager _fetchStateOfMindEventsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.480
- ___97-[MOCloudKitPushNotifications initWithNamedDelegatePort:apsTopics:subscriptionID:onNotification:]_block_invoke
- ___block_descriptor_48_e8_32s40w_e8_v12?0i8lw40l8s32l8
- __block_literal_global.425
- __block_literal_global.427
- __block_literal_global.429
- __block_literal_global.431
- __block_literal_global.490
- __block_literal_global.495
- __block_literal_global.597
CStrings:
+ "/System/Library/Moments/HolidayTuningParameters.json"
+ "/System/Library/Moments/MUIDCategories.json"
+ "SubscribeWithSubscriptionID"
+ "[subscribeWithSubscriptionID] Already subscribed for: %@"
+ "[subscribeWithSubscriptionID] Already subscribing, skipping..."
+ "[subscribeWithSubscriptionID] ERROR: Deleting iCloud Subscription: %@ %@"
+ "[subscribeWithSubscriptionID] ERROR: Registering iCloud Notification: %@"
+ "[subscribeWithSubscriptionID] ERROR: iCloud Subscription: %@ %@"
+ "[subscribeWithSubscriptionID] Error getting server preferred push environment %@"
+ "[subscribeWithSubscriptionID] Received public token"
+ "[subscribeWithSubscriptionID] Received push notification %@"
+ "[subscribeWithSubscriptionID] Successfully deleted subscribed: %@"
+ "[subscribeWithSubscriptionID] Successfully registered iCloud Notification"
+ "[subscribeWithSubscriptionID] Successfully subscribed for: %@"
+ "[subscribeWithSubscriptionID] Timeout getting server preferred push environment"
+ "[subscribeWithSubscriptionID] Using push environment %@"
+ "_momentsUI"
+ "stringForKey:"
+ "synchronize"
- "/System/Library/Trial/NamespaceDescriptors/HolidayTuningParameters.json"
- "/System/Library/Trial/NamespaceDescriptors/MUIDCategories.json"
- "ERROR: Deleting iCloud Subscription: %@ %@"
- "ERROR: Registering iCloud Notification: %@"
- "ERROR: iCloud Subscription: %@ %@"
- "Error getting server preferred push environment %@"
- "Received public token"
- "Received push notification %@"
- "Successfully deleted subscribed: %@"
- "Successfully registered iCloud Notification"
- "Successfully subscribed: %@"
- "Timeout getting server preferred push environment"
- "Using push environment %@"
- "[subscribeWithSubscriptionID] Already subscribbing, skipping..."
- "com.apple.cloudd.authorizationChanged"
- "sky"

```
