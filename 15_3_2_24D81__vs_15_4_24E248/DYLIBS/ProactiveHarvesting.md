## ProactiveHarvesting

> `/System/Library/PrivateFrameworks/ProactiveHarvesting.framework/Versions/A/ProactiveHarvesting`

```diff

-1271.10.0.0.0
-  __TEXT.__text: 0x40c40
+1276.10.4.0.0
+  __TEXT.__text: 0x40a1c
   __TEXT.__auth_stubs: 0x890
-  __TEXT.__objc_methlist: 0x78e4
+  __TEXT.__objc_methlist: 0x7b94
   __TEXT.__const: 0x19e
   __TEXT.__gcc_except_tab: 0xafc
-  __TEXT.__cstring: 0x242b
+  __TEXT.__cstring: 0x2420
   __TEXT.__oslogstring: 0x442b
-  __TEXT.__unwind_info: 0xb88
+  __TEXT.__unwind_info: 0xb70
   __TEXT.__objc_classname: 0x57c
   __TEXT.__objc_methname: 0x9721
   __TEXT.__objc_methtype: 0xcd3
   __TEXT.__objc_stubs: 0x46a0
   __DATA_CONST.__got: 0x538
-  __DATA_CONST.__const: 0x518
+  __DATA_CONST.__const: 0x530
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x54b0
+  __DATA_CONST.__objc_selrefs: 0x5520
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x458
   __AUTH_CONST.__const: 0x1790
   __AUTH_CONST.__cfstring: 0x2780
-  __AUTH_CONST.__objc_const: 0x4560
+  __AUTH_CONST.__objc_const: 0x40b8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 1744B14A-8443-34E7-8C42-4EF156DA5C66
-  Functions: 2859
+  UUID: B381C729-78FE-3AF3-9974-CDDE789E1F0D
+  Functions: 2853
   Symbols:   4652
-  CStrings:  4154
+  CStrings:  4150
 
Symbols:
+ __124-[HVConsumerCoordinator harvestContentWithMinimumLevelOfService:ignoringDiscretionaryPowerBudget:error:shouldContinueBlock:]_block_invoke.117
+ __26-[HVContentAdmission init]_block_invoke.54
+ __28-[HVXPCInternalService init]_block_invoke.35
+ __30-[HVHtmlParser _endProcessing]_block_invoke.52
+ __31-[HVXPCSysdiagnoseService init]_block_invoke.14
+ __40-[HVScheduledTasks _registerCleanupTask]_block_invoke.40
+ __41-[HVQueue _deleteWithFilter:memory:disk:]_block_invoke.245
+ __41-[HVQueue _deleteWithFilter:memory:disk:]_block_invoke.247
+ __41-[HVQueue _deleteWithFilter:memory:disk:]_block_invoke.252
+ __41-[HVSpotlightDeletionRequest description]_block_invoke.51
+ __42-[HVQueue _filterBlockForDeletionRequest:]_block_invoke.272
+ __42-[HVQueue _filterBlockForDeletionRequest:]_block_invoke.276
+ __47-[HVDataSourceContentState saveStateWithError:]_block_invoke.70
+ __48-[HVQueue cleanupWithError:shouldContinueBlock:]_block_invoke.359
+ __49-[HVDonationReceiver _setUpUserActivityDonations]_block_invoke.16
+ __49-[HVSpotlightDeletionRequest matchesBloomFilter:]_block_invoke.28
+ __49-[HVSpotlightDeletionRequest matchesBloomFilter:]_block_invoke.30
+ __50-[HVContentAdmission _registerConfigurationAsset:]_block_invoke.61
+ __51-[HVQueues enqueueContent:contentProtection:error:]_block_invoke.29
+ __53-[HVContentAdmission _migrateIfNeededWithCompletion:]_block_invoke.94
+ __53-[HVQueues(TestHelpers) waitForObserversWithTimeout:]_block_invoke.131
+ __55-[HVSpotlightDeletionRequest copyWithBundleIdentifier:]_block_invoke.75
+ __55-[HVSpotlightDeletionRequest copyWithBundleIdentifier:]_block_invoke.78
+ __66-[HVScheduledTasks _registerHarvestTaskWithMinimumLevelOfService:]_block_invoke.29
+ __66-[HVXPCInternalServerDelegate listener:shouldAcceptNewConnection:]_block_invoke.54
+ __69-[HVXPCSysdiagnoseServerDelegate listener:shouldAcceptNewConnection:]_block_invoke.21
+ __70-[NSString(HVNSString) hv_dataEnumeratorUsingEncoding:nullTerminated:]_block_invoke.37
+ __80-[HVQueue _filterBlockForBundleIdentifier:contentIdentifierSet:domainSelection:]_block_invoke.296
+ __80-[HVQueue _filterBlockForBundleIdentifier:contentIdentifierSet:domainSelection:]_block_invoke.303
+ __80-[HVQueue _filterBlockForBundleIdentifier:contentIdentifierSet:domainSelection:]_block_invoke.304
+ __82-[HVBudget performWorkForOneDataSource:levelOfService:requireRegistrations:block:]_block_invoke.19
+ __95-[HVQueue dequeueContent:dataSourceContentState:minimumLevelOfService:inMemoryItemsOnly:error:]_block_invoke.200
+ __95-[HVQueue dequeueContent:dataSourceContentState:minimumLevelOfService:inMemoryItemsOnly:error:]_block_invoke.211
+ __95-[HVQueue dequeueContent:dataSourceContentState:minimumLevelOfService:inMemoryItemsOnly:error:]_block_invoke.213
+ __Block_byref_object_copy_.1005
+ __Block_byref_object_copy_.1135
+ __Block_byref_object_copy_.1245
+ __Block_byref_object_copy_.1805
+ __Block_byref_object_copy_.267
+ __Block_byref_object_copy_.300
+ __Block_byref_object_copy_.597
+ __Block_byref_object_copy_.708
+ __Block_byref_object_dispose_.1006
+ __Block_byref_object_dispose_.1136
+ __Block_byref_object_dispose_.1246
+ __Block_byref_object_dispose_.1806
+ __Block_byref_object_dispose_.268
+ __Block_byref_object_dispose_.301
+ __Block_byref_object_dispose_.598
+ __Block_byref_object_dispose_.709
+ __block_literal_global.104
+ __block_literal_global.1064
+ __block_literal_global.1191
+ __block_literal_global.12
+ __block_literal_global.1205
+ __block_literal_global.1282
+ __block_literal_global.132
+ __block_literal_global.133
+ __block_literal_global.14
+ __block_literal_global.15.1268
+ __block_literal_global.1683
+ __block_literal_global.184
+ __block_literal_global.1845
+ __block_literal_global.1894
+ __block_literal_global.1972
+ __block_literal_global.20
+ __block_literal_global.21
+ __block_literal_global.222
+ __block_literal_global.23
+ __block_literal_global.241
+ __block_literal_global.2596
+ __block_literal_global.298
+ __block_literal_global.306
+ __block_literal_global.355
+ __block_literal_global.40
+ __block_literal_global.411
+ __block_literal_global.45
+ __block_literal_global.48
+ __block_literal_global.49
+ __block_literal_global.53
+ __block_literal_global.56
+ __block_literal_global.56.2631
+ __block_literal_global.60
+ __block_literal_global.610
+ __block_literal_global.757
+ __block_literal_global.89
+ server._pasExprOnceResult.2643
+ sharedInstance._pasExprOnceResult.2538
+ sharedInstance._pasExprOnceResult.896
+ sharedInstance._pasOnceToken3.895
- __124-[HVConsumerCoordinator harvestContentWithMinimumLevelOfService:ignoringDiscretionaryPowerBudget:error:shouldContinueBlock:]_block_invoke.111
- __26-[HVContentAdmission init]_block_invoke.48
- __28-[HVXPCInternalService init]_block_invoke.29
- __30-[HVHtmlParser _endProcessing]_block_invoke.46
- __31-[HVXPCSysdiagnoseService init]_block_invoke.8
- __40-[HVScheduledTasks _registerCleanupTask]_block_invoke.34
- __41-[HVQueue _deleteWithFilter:memory:disk:]_block_invoke.239
- __41-[HVQueue _deleteWithFilter:memory:disk:]_block_invoke.241
- __41-[HVQueue _deleteWithFilter:memory:disk:]_block_invoke.246
- __41-[HVSpotlightDeletionRequest description]_block_invoke.39
- __42-[HVQueue _filterBlockForDeletionRequest:]_block_invoke.266
- __42-[HVQueue _filterBlockForDeletionRequest:]_block_invoke.270
- __47-[HVDataSourceContentState saveStateWithError:]_block_invoke.64
- __48-[HVQueue cleanupWithError:shouldContinueBlock:]_block_invoke.353
- __49-[HVDonationReceiver _setUpUserActivityDonations]_block_invoke.10
- __49-[HVSpotlightDeletionRequest matchesBloomFilter:]_block_invoke.22
- __49-[HVSpotlightDeletionRequest matchesBloomFilter:]_block_invoke.24
- __50-[HVContentAdmission _registerConfigurationAsset:]_block_invoke.55
- __51-[HVQueues enqueueContent:contentProtection:error:]_block_invoke.25
- __53-[HVContentAdmission _migrateIfNeededWithCompletion:]_block_invoke.88
- __53-[HVQueues(TestHelpers) waitForObserversWithTimeout:]_block_invoke.125
- __55-[HVSpotlightDeletionRequest copyWithBundleIdentifier:]_block_invoke.66
- __55-[HVSpotlightDeletionRequest copyWithBundleIdentifier:]_block_invoke.69
- __66-[HVScheduledTasks _registerHarvestTaskWithMinimumLevelOfService:]_block_invoke.23
- __66-[HVXPCInternalServerDelegate listener:shouldAcceptNewConnection:]_block_invoke.48
- __69-[HVXPCSysdiagnoseServerDelegate listener:shouldAcceptNewConnection:]_block_invoke.17
- __70-[NSString(HVNSString) hv_dataEnumeratorUsingEncoding:nullTerminated:]_block_invoke.31
- __80-[HVQueue _filterBlockForBundleIdentifier:contentIdentifierSet:domainSelection:]_block_invoke.290
- __80-[HVQueue _filterBlockForBundleIdentifier:contentIdentifierSet:domainSelection:]_block_invoke.297
- __80-[HVQueue _filterBlockForBundleIdentifier:contentIdentifierSet:domainSelection:]_block_invoke.298
- __82-[HVBudget performWorkForOneDataSource:levelOfService:requireRegistrations:block:]_block_invoke.13
- __95-[HVQueue dequeueContent:dataSourceContentState:minimumLevelOfService:inMemoryItemsOnly:error:]_block_invoke.194
- __95-[HVQueue dequeueContent:dataSourceContentState:minimumLevelOfService:inMemoryItemsOnly:error:]_block_invoke.205
- __95-[HVQueue dequeueContent:dataSourceContentState:minimumLevelOfService:inMemoryItemsOnly:error:]_block_invoke.207
- __Block_byref_object_copy_.1041
- __Block_byref_object_copy_.1172
- __Block_byref_object_copy_.1285
- __Block_byref_object_copy_.1844
- __Block_byref_object_copy_.261
- __Block_byref_object_copy_.315
- __Block_byref_object_copy_.628
- __Block_byref_object_copy_.739
- __Block_byref_object_dispose_.1042
- __Block_byref_object_dispose_.1173
- __Block_byref_object_dispose_.1286
- __Block_byref_object_dispose_.1845
- __Block_byref_object_dispose_.262
- __Block_byref_object_dispose_.316
- __Block_byref_object_dispose_.629
- __Block_byref_object_dispose_.740
- __block_literal_global.10
- __block_literal_global.10.1247
- __block_literal_global.11
- __block_literal_global.1101
- __block_literal_global.119
- __block_literal_global.1228
- __block_literal_global.1243
- __block_literal_global.127
- __block_literal_global.13
- __block_literal_global.1320
- __block_literal_global.146
- __block_literal_global.1720
- __block_literal_global.178
- __block_literal_global.1883
- __block_literal_global.1932
- __block_literal_global.2009
- __block_literal_global.216
- __block_literal_global.235
- __block_literal_global.2635
- __block_literal_global.292
- __block_literal_global.31
- __block_literal_global.321
- __block_literal_global.34
- __block_literal_global.349
- __block_literal_global.39
- __block_literal_global.399
- __block_literal_global.41
- __block_literal_global.42
- __block_literal_global.5
- __block_literal_global.50
- __block_literal_global.50.2670
- __block_literal_global.641
- __block_literal_global.68
- __block_literal_global.787
- __block_literal_global.8
- __block_literal_global.83
- server._pasExprOnceResult.2682
- sharedInstance._pasExprOnceResult.2577
- sharedInstance._pasExprOnceResult.929
- sharedInstance._pasOnceToken3.928
CStrings:
- "a"
- "br"
- "hr"
- "id"

```
