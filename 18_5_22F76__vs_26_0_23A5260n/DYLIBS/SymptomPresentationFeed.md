## SymptomPresentationFeed

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationFeed.framework/SymptomPresentationFeed`

```diff

-2022.120.2.0.0
-  __TEXT.__text: 0x206c8
+2130.0.0.0.1
+  __TEXT.__text: 0x207cc
   __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_methlist: 0x894
-  __TEXT.__cstring: 0x1503
-  __TEXT.__const: 0x100
+  __TEXT.__objc_methlist: 0x90c
+  __TEXT.__cstring: 0x153f
+  __TEXT.__const: 0xe8
   __TEXT.__gcc_except_tab: 0x69c
-  __TEXT.__oslogstring: 0x25b9
-  __TEXT.__unwind_info: 0x480
+  __TEXT.__oslogstring: 0x25e3
+  __TEXT.__unwind_info: 0x478
   __TEXT.__objc_classname: 0xdb
-  __TEXT.__objc_methname: 0x27ca
-  __TEXT.__objc_methtype: 0xb7f
-  __TEXT.__objc_stubs: 0x1bc0
-  __DATA_CONST.__got: 0x3d0
+  __TEXT.__objc_methname: 0x2938
+  __TEXT.__objc_methtype: 0xcf6
+  __TEXT.__objc_stubs: 0x1be0
+  __DATA_CONST.__got: 0x3d8
   __DATA_CONST.__const: 0x10a8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x980
+  __DATA_CONST.__objc_selrefs: 0x9d8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__auth_got: 0x260
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x2100
-  __AUTH_CONST.__objc_const: 0xbc0
+  __AUTH_CONST.__cfstring: 0x2140
+  __AUTH_CONST.__objc_const: 0xd50
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x30
   __DATA.__objc_ivar: 0x60

   - /System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomAnalytics.framework/SymptomAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 02193252-A401-38F3-A616-751EF136C79F
+  UUID: 0665108D-D77D-33A2-AD6D-0C590FC55434
   Functions: 307
-  Symbols:   1371
-  CStrings:  1195
+  Symbols:   1373
+  CStrings:  1222
 
Symbols:
+ _OBJC_CLASS_$_NSUserDefaults
+ ___100-[UsageFeed(NetworkDomains) _networkDomainsQueryViewTypeApp:entityName:limit:actions:callbackBlock:]_block_invoke.623
+ ___108-[UsageFeed(NetworkDomains) networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:reply:]_block_invoke.587
+ ___123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.691
+ ___123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.693
+ ___123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.695
+ ___124-[UsageFeed(NetworkDomains) networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:fetchProperties:reply:]_block_invoke.580
+ ___124-[UsageFeed(NetworkDomains) networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:fetchProperties:reply:]_block_invoke.583
+ ___124-[UsageFeed(NetworkDomains) networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:fetchProperties:reply:]_block_invoke.584
+ ___164-[UsageFeed(NetworkDomains) _performNetDomainsQueryOnService:entityName:fetchProps:pred:sort:actions:queryTimer:replyProcessBlock:accumulatedResults:callbackBlock:]_block_invoke.576
+ ___237-[UsageFeed(NetworkDomains) __networkDomainsQueryDomains:entityName:unnamedDomainsOption:limit:actions:accumulatedResults:aggregateProperty:predicate:altAggregateProperty:altPredicate:ipAggregateProperty:replyProcessBlock:callbackBlock:]_block_invoke.651
+ ___237-[UsageFeed(NetworkDomains) __networkDomainsQueryDomains:entityName:unnamedDomainsOption:limit:actions:accumulatedResults:aggregateProperty:predicate:altAggregateProperty:altPredicate:ipAggregateProperty:replyProcessBlock:callbackBlock:]_block_invoke.654
+ ___237-[UsageFeed(NetworkDomains) __networkDomainsQueryDomains:entityName:unnamedDomainsOption:limit:actions:accumulatedResults:aggregateProperty:predicate:altAggregateProperty:altPredicate:ipAggregateProperty:replyProcessBlock:callbackBlock:]_block_invoke_2.652
+ ___34-[UsageFeed getUsageOption:reply:]_block_invoke.494
+ ___34-[UsageFeed setUsageOption:reply:]_block_invoke.493
+ ___37-[UsageFeed identifierForUUID:reply:]_block_invoke.497
+ ___38-[NWNetworkOfInterestManager _connect]_block_invoke.128
+ ___46-[UsageFeed resetUsageDataFor:nameKind:reply:]_block_invoke.495
+ ___49-[NetworkPerformanceFeed resetDataForKeys:reply:]_block_invoke.208
+ ___53-[NWNetworkOfInterestManager proxyHaveNOIs:tornDown:]_block_invoke.200
+ ___56-[NWNetworkOfInterestManager linkThroughputOnNOI:reply:]_block_invoke.179
+ ___56-[NWNetworkOfInterestManager linkThroughputOnNOI:reply:]_block_invoke.180
+ ___57-[NWNetworkOfInterestManager instantQualityForNOI:reply:]_block_invoke.173
+ ___57-[NWNetworkOfInterestManager instantQualityForNOI:reply:]_block_invoke.174
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.156
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.157
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.194
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.198
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.199
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.201
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.204
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.205
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke_2.195
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke_2.200
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke_2.202
+ ___57-[UsageFeed typicalUsageFor:nameKind:intervalKind:reply:]_block_invoke.470
+ ___59-[NWNetworkOfInterestManager errorPredictionsForNOI:reply:]_block_invoke.190
+ ___59-[NWNetworkOfInterestManager errorPredictionsForNOI:reply:]_block_invoke.191
+ ___59-[NWNetworkOfInterestManager trainingProgressForNOI:reply:]_block_invoke.194
+ ___59-[NWNetworkOfInterestManager trainingProgressForNOI:reply:]_block_invoke.195
+ ___60-[NWNetworkOfInterestManager interfaceTimelineForNOI:reply:]_block_invoke.198
+ ___60-[NWNetworkOfInterestManager interfaceTimelineForNOI:reply:]_block_invoke.199
+ ___60-[NWNetworkOfInterestManager updatePredictionsForNOI:reply:]_block_invoke.170
+ ___60-[NWNetworkOfInterestManager updatePredictionsForNOI:reply:]_block_invoke.171
+ ___60-[UsageFeed(NetworkDomains) getNetworkDomainsOptions:reply:]_block_invoke.703
+ ___60-[UsageFeed(NetworkDomains) setNetworkDomainsOptions:reply:]_block_invoke.702
+ ___62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.408
+ ___62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.443
+ ___62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.446
+ ___62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.449
+ ___62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke_2.451
+ ___63-[NWNetworkOfInterestManager auditableLinkQualityForNOI:reply:]_block_invoke.175
+ ___63-[NWNetworkOfInterestManager auditableLinkQualityForNOI:reply:]_block_invoke.176
+ ___65-[NetworkPerformanceFeed getPreferCellOverWiFiWithOptions:reply:]_block_invoke.210
+ ___65-[NetworkPerformanceFeed setPreferCellOverWiFiWithOptions:reply:]_block_invoke.212
+ ___67-[NWNetworkOfInterestManager canUseOnAlternateNOI:appStates:reply:]_block_invoke.188
+ ___67-[NWNetworkOfInterestManager canUseOnAlternateNOI:appStates:reply:]_block_invoke.189
+ ___70-[NWNetworkOfInterestManager dayOfWeekPredictionGroupingForNOI:reply:]_block_invoke.192
+ ___70-[NWNetworkOfInterestManager dayOfWeekPredictionGroupingForNOI:reply:]_block_invoke.193
+ ___70-[NWNetworkOfInterestManager networkAttachmentInfoForScopedNOI:reply:]_block_invoke.177
+ ___70-[NWNetworkOfInterestManager networkAttachmentInfoForScopedNOI:reply:]_block_invoke.178
+ ___72-[NWNetworkOfInterestManager foregroundNetworkActivityUnderwayOn:reply:]_block_invoke.183
+ ___72-[NWNetworkOfInterestManager foregroundNetworkActivityUnderwayOn:reply:]_block_invoke.184
+ ___74-[UsageFeed(NetworkDomains) performNetworkDomainsActionWithOptions:reply:]_block_invoke.704
+ ___75-[NWNetworkOfInterestManager trafficInvitesHourlyDistributionForNOI:reply:]_block_invoke.196
+ ___75-[NWNetworkOfInterestManager trafficInvitesHourlyDistributionForNOI:reply:]_block_invoke.197
+ ___76-[UsageFeed calendarUsageFor:nameKind:dayResolution:daySlot:weekSlot:reply:]_block_invoke.482
+ ___76-[UsageFeed calendarUsageFor:nameKind:dayResolution:daySlot:weekSlot:reply:]_block_invoke.486
+ ___76-[UsageFeed calendarUsageFor:nameKind:dayResolution:daySlot:weekSlot:reply:]_block_invoke.490
+ ___77-[UsageFeed algosScoreToDateWithOptionsFor:nameKind:startTime:options:reply:]_block_invoke.492
+ ___80-[UsageFeed networkBitmapsToDateWithOptionsFor:startTime:endTime:options:reply:]_block_invoke.406
+ ___83-[NWNetworkOfInterestManager estimatedDataTransferTimeOnNOI:withPayloadInfo:reply:]_block_invoke.181
+ ___83-[NWNetworkOfInterestManager estimatedDataTransferTimeOnNOI:withPayloadInfo:reply:]_block_invoke.182
+ ___84-[NWNetworkOfInterestManager inquireNOIFor:orPredicate:requestedKeys:options:reply:]_block_invoke.167
+ ___84-[NWNetworkOfInterestManager inquireNOIFor:orPredicate:requestedKeys:options:reply:]_block_invoke.168
+ ___92-[NetworkPerformanceFeed watchpointOn:forIdentifier:andKey:onThreshold:withOptions:uponHit:]_block_invoke.206
+ ___92-[NetworkPerformanceFeed watchpointOn:forIdentifier:andKey:onThreshold:withOptions:uponHit:]_block_invoke.207
+ ___Block_byref_object_copy_.577
+ ___Block_byref_object_dispose_.578
+ ___block_literal_global.590
+ ___block_literal_global.596
+ ___block_literal_global.605
+ _objc_msgSend$initWithSuiteName:
- ___100-[UsageFeed(NetworkDomains) _networkDomainsQueryViewTypeApp:entityName:limit:actions:callbackBlock:]_block_invoke.616
- ___108-[UsageFeed(NetworkDomains) networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:reply:]_block_invoke.580
- ___123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.684
- ___123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.686
- ___123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.688
- ___124-[UsageFeed(NetworkDomains) networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:fetchProperties:reply:]_block_invoke.573
- ___124-[UsageFeed(NetworkDomains) networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:fetchProperties:reply:]_block_invoke.576
- ___124-[UsageFeed(NetworkDomains) networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:fetchProperties:reply:]_block_invoke.577
- ___164-[UsageFeed(NetworkDomains) _performNetDomainsQueryOnService:entityName:fetchProps:pred:sort:actions:queryTimer:replyProcessBlock:accumulatedResults:callbackBlock:]_block_invoke.569
- ___237-[UsageFeed(NetworkDomains) __networkDomainsQueryDomains:entityName:unnamedDomainsOption:limit:actions:accumulatedResults:aggregateProperty:predicate:altAggregateProperty:altPredicate:ipAggregateProperty:replyProcessBlock:callbackBlock:]_block_invoke.644
- ___237-[UsageFeed(NetworkDomains) __networkDomainsQueryDomains:entityName:unnamedDomainsOption:limit:actions:accumulatedResults:aggregateProperty:predicate:altAggregateProperty:altPredicate:ipAggregateProperty:replyProcessBlock:callbackBlock:]_block_invoke.647
- ___237-[UsageFeed(NetworkDomains) __networkDomainsQueryDomains:entityName:unnamedDomainsOption:limit:actions:accumulatedResults:aggregateProperty:predicate:altAggregateProperty:altPredicate:ipAggregateProperty:replyProcessBlock:callbackBlock:]_block_invoke_2.645
- ___34-[UsageFeed getUsageOption:reply:]_block_invoke.487
- ___34-[UsageFeed setUsageOption:reply:]_block_invoke.486
- ___37-[UsageFeed identifierForUUID:reply:]_block_invoke.490
- ___38-[NWNetworkOfInterestManager _connect]_block_invoke.107
- ___46-[UsageFeed resetUsageDataFor:nameKind:reply:]_block_invoke.488
- ___49-[NetworkPerformanceFeed resetDataForKeys:reply:]_block_invoke.187
- ___53-[NWNetworkOfInterestManager proxyHaveNOIs:tornDown:]_block_invoke.179
- ___56-[NWNetworkOfInterestManager linkThroughputOnNOI:reply:]_block_invoke.158
- ___56-[NWNetworkOfInterestManager linkThroughputOnNOI:reply:]_block_invoke.159
- ___57-[NWNetworkOfInterestManager instantQualityForNOI:reply:]_block_invoke.152
- ___57-[NWNetworkOfInterestManager instantQualityForNOI:reply:]_block_invoke.153
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.135
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.136
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.173
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.177
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.178
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.180
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.183
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.184
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke_2.174
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke_2.179
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke_2.181
- ___57-[UsageFeed typicalUsageFor:nameKind:intervalKind:reply:]_block_invoke.463
- ___59-[NWNetworkOfInterestManager errorPredictionsForNOI:reply:]_block_invoke.169
- ___59-[NWNetworkOfInterestManager errorPredictionsForNOI:reply:]_block_invoke.170
- ___59-[NWNetworkOfInterestManager trainingProgressForNOI:reply:]_block_invoke.173
- ___59-[NWNetworkOfInterestManager trainingProgressForNOI:reply:]_block_invoke.174
- ___60-[NWNetworkOfInterestManager interfaceTimelineForNOI:reply:]_block_invoke.177
- ___60-[NWNetworkOfInterestManager interfaceTimelineForNOI:reply:]_block_invoke.178
- ___60-[NWNetworkOfInterestManager updatePredictionsForNOI:reply:]_block_invoke.149
- ___60-[NWNetworkOfInterestManager updatePredictionsForNOI:reply:]_block_invoke.150
- ___60-[UsageFeed(NetworkDomains) getNetworkDomainsOptions:reply:]_block_invoke.696
- ___60-[UsageFeed(NetworkDomains) setNetworkDomainsOptions:reply:]_block_invoke.695
- ___62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.401
- ___62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.436
- ___62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.439
- ___62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.442
- ___62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke_2.444
- ___63-[NWNetworkOfInterestManager auditableLinkQualityForNOI:reply:]_block_invoke.154
- ___63-[NWNetworkOfInterestManager auditableLinkQualityForNOI:reply:]_block_invoke.155
- ___65-[NetworkPerformanceFeed getPreferCellOverWiFiWithOptions:reply:]_block_invoke.189
- ___65-[NetworkPerformanceFeed setPreferCellOverWiFiWithOptions:reply:]_block_invoke.191
- ___67-[NWNetworkOfInterestManager canUseOnAlternateNOI:appStates:reply:]_block_invoke.167
- ___67-[NWNetworkOfInterestManager canUseOnAlternateNOI:appStates:reply:]_block_invoke.168
- ___70-[NWNetworkOfInterestManager dayOfWeekPredictionGroupingForNOI:reply:]_block_invoke.171
- ___70-[NWNetworkOfInterestManager dayOfWeekPredictionGroupingForNOI:reply:]_block_invoke.172
- ___70-[NWNetworkOfInterestManager networkAttachmentInfoForScopedNOI:reply:]_block_invoke.156
- ___70-[NWNetworkOfInterestManager networkAttachmentInfoForScopedNOI:reply:]_block_invoke.157
- ___72-[NWNetworkOfInterestManager foregroundNetworkActivityUnderwayOn:reply:]_block_invoke.162
- ___72-[NWNetworkOfInterestManager foregroundNetworkActivityUnderwayOn:reply:]_block_invoke.163
- ___74-[UsageFeed(NetworkDomains) performNetworkDomainsActionWithOptions:reply:]_block_invoke.697
- ___75-[NWNetworkOfInterestManager trafficInvitesHourlyDistributionForNOI:reply:]_block_invoke.175
- ___75-[NWNetworkOfInterestManager trafficInvitesHourlyDistributionForNOI:reply:]_block_invoke.176
- ___76-[UsageFeed calendarUsageFor:nameKind:dayResolution:daySlot:weekSlot:reply:]_block_invoke.475
- ___76-[UsageFeed calendarUsageFor:nameKind:dayResolution:daySlot:weekSlot:reply:]_block_invoke.479
- ___76-[UsageFeed calendarUsageFor:nameKind:dayResolution:daySlot:weekSlot:reply:]_block_invoke.483
- ___77-[UsageFeed algosScoreToDateWithOptionsFor:nameKind:startTime:options:reply:]_block_invoke.485
- ___80-[UsageFeed networkBitmapsToDateWithOptionsFor:startTime:endTime:options:reply:]_block_invoke.399
- ___83-[NWNetworkOfInterestManager estimatedDataTransferTimeOnNOI:withPayloadInfo:reply:]_block_invoke.160
- ___83-[NWNetworkOfInterestManager estimatedDataTransferTimeOnNOI:withPayloadInfo:reply:]_block_invoke.161
- ___84-[NWNetworkOfInterestManager inquireNOIFor:orPredicate:requestedKeys:options:reply:]_block_invoke.146
- ___84-[NWNetworkOfInterestManager inquireNOIFor:orPredicate:requestedKeys:options:reply:]_block_invoke.147
- ___92-[NetworkPerformanceFeed watchpointOn:forIdentifier:andKey:onThreshold:withOptions:uponHit:]_block_invoke.185
- ___92-[NetworkPerformanceFeed watchpointOn:forIdentifier:andKey:onThreshold:withOptions:uponHit:]_block_invoke.186
- ___Block_byref_object_copy_.570
- ___Block_byref_object_dispose_.571
- ___block_literal_global.583
- ___block_literal_global.589
- ___block_literal_global.598
CStrings:
+ "++ Overriding database fetch limit to %ld"
+ "com.apple.symptomframework.usagefeed"
+ "db_records_fetch_limit"
+ "fetchNDFDeviceRecordsWithReply:"
+ "initWithSuiteName:"
+ "listNDFDeviceObjectsWithIdentifier:reply:"
+ "ndfClientCheckInWithReply:"
+ "ndfClientSubscriptionIsActive:reply:"
+ "networkRestrictsMulticastTrafficWithReply:"
+ "pingEndpoints:reply:"
+ "sendMessage:toEndpoints:reply:"
+ "sendPayloadToDaemonWithReply:"
+ "triggerSendPayloadToDaemonWithInterval:leeway:reply:"
+ "updatedNDFDeviceRecords:reply:"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@0:8@?<v@?B>16"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v28@0:8B16@?20"
+ "v28@0:8B16@?<v@?@\"NSError\">20"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSObject<OS_xpc_object>\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?B>24"
+ "v40@0:8@\"NSString\"16@\"NSObject<OS_xpc_object>\"24@?<v@?@\"NSString\"@\"NSError\">32"
+ "v40@0:8q16q24@?32"
+ "v40@0:8q16q24@?<v@?B>32"

```
