## SymptomPresentationFeed

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationFeed.framework/SymptomPresentationFeed`

```diff

-2169.120.7.0.0
-  __TEXT.__text: 0x21474
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0x918
-  __TEXT.__cstring: 0x153f
+2357.0.0.0.2
+  __TEXT.__text: 0x1f134
+  __TEXT.__objc_methlist: 0x924
+  __TEXT.__cstring: 0x157e
   __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0x678
+  __TEXT.__gcc_except_tab: 0x4ec
   __TEXT.__oslogstring: 0x25e3
-  __TEXT.__unwind_info: 0x488
-  __TEXT.__objc_classname: 0xdb
-  __TEXT.__objc_methname: 0x295a
-  __TEXT.__objc_methtype: 0xcf6
-  __TEXT.__objc_stubs: 0x1be0
-  __DATA_CONST.__got: 0x3d8
-  __DATA_CONST.__const: 0x10a8
+  __TEXT.__unwind_info: 0x480
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x10c0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9e0
+  __DATA_CONST.__objc_selrefs: 0x9e8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x230
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x2140
-  __AUTH_CONST.__objc_const: 0xd78
+  __AUTH_CONST.__cfstring: 0x21a0
+  __AUTH_CONST.__objc_const: 0xda0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x60
   __DATA.__data: 0x198
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x190
-  __DATA_DIRTY.__bss: 0x50
+  __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomAnalytics.framework/SymptomAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B16835F7-34F7-3C38-A848-F3A3382AA722
+  UUID: CE13CFB0-C7AF-37DE-8976-E9A967879ACC
   Functions: 308
-  Symbols:   1367
-  CStrings:  1223
+  Symbols:   1375
+  CStrings:  760
 
Symbols:
+ ___100-[UsageFeed(NetworkDomains) _networkDomainsQueryViewTypeApp:entityName:limit:actions:callbackBlock:]_block_invoke.622
+ ___108-[UsageFeed(NetworkDomains) networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:reply:]_block_invoke.586
+ ___123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.690
+ ___123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.692
+ ___123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.694
+ ___124-[UsageFeed(NetworkDomains) networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:fetchProperties:reply:]_block_invoke.579
+ ___124-[UsageFeed(NetworkDomains) networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:fetchProperties:reply:]_block_invoke.582
+ ___164-[UsageFeed(NetworkDomains) _performNetDomainsQueryOnService:entityName:fetchProps:pred:sort:actions:queryTimer:replyProcessBlock:accumulatedResults:callbackBlock:]_block_invoke.575
+ ___237-[UsageFeed(NetworkDomains) __networkDomainsQueryDomains:entityName:unnamedDomainsOption:limit:actions:accumulatedResults:aggregateProperty:predicate:altAggregateProperty:altPredicate:ipAggregateProperty:replyProcessBlock:callbackBlock:]_block_invoke.650
+ ___237-[UsageFeed(NetworkDomains) __networkDomainsQueryDomains:entityName:unnamedDomainsOption:limit:actions:accumulatedResults:aggregateProperty:predicate:altAggregateProperty:altPredicate:ipAggregateProperty:replyProcessBlock:callbackBlock:]_block_invoke.653
+ ___237-[UsageFeed(NetworkDomains) __networkDomainsQueryDomains:entityName:unnamedDomainsOption:limit:actions:accumulatedResults:aggregateProperty:predicate:altAggregateProperty:altPredicate:ipAggregateProperty:replyProcessBlock:callbackBlock:]_block_invoke_2.651
+ ___38-[NWNetworkOfInterestManager _connect]_block_invoke.131
+ ___49-[NetworkPerformanceFeed resetDataForKeys:reply:]_block_invoke.212
+ ___53-[NWNetworkOfInterestManager proxyHaveNOIs:tornDown:]_block_invoke.203
+ ___56-[NWNetworkOfInterestManager linkThroughputOnNOI:reply:]_block_invoke.182
+ ___56-[NWNetworkOfInterestManager linkThroughputOnNOI:reply:]_block_invoke.183
+ ___57-[NWNetworkOfInterestManager instantQualityForNOI:reply:]_block_invoke.176
+ ___57-[NWNetworkOfInterestManager instantQualityForNOI:reply:]_block_invoke.177
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.160
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.161
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.198
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.203
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.208
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.209
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke_2.199
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke_2.204
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke_2.206
+ ___59-[NWNetworkOfInterestManager errorPredictionsForNOI:reply:]_block_invoke.193
+ ___59-[NWNetworkOfInterestManager errorPredictionsForNOI:reply:]_block_invoke.194
+ ___59-[NWNetworkOfInterestManager trainingProgressForNOI:reply:]_block_invoke.197
+ ___59-[NWNetworkOfInterestManager trainingProgressForNOI:reply:]_block_invoke.198
+ ___60-[NWNetworkOfInterestManager interfaceTimelineForNOI:reply:]_block_invoke.201
+ ___60-[NWNetworkOfInterestManager interfaceTimelineForNOI:reply:]_block_invoke.202
+ ___60-[NWNetworkOfInterestManager updatePredictionsForNOI:reply:]_block_invoke.173
+ ___60-[NWNetworkOfInterestManager updatePredictionsForNOI:reply:]_block_invoke.174
+ ___60-[UsageFeed(NetworkDomains) getNetworkDomainsOptions:reply:]_block_invoke.702
+ ___60-[UsageFeed(NetworkDomains) setNetworkDomainsOptions:reply:]_block_invoke.701
+ ___63-[NWNetworkOfInterestManager auditableLinkQualityForNOI:reply:]_block_invoke.178
+ ___63-[NWNetworkOfInterestManager auditableLinkQualityForNOI:reply:]_block_invoke.179
+ ___65-[NetworkPerformanceFeed getPreferCellOverWiFiWithOptions:reply:]_block_invoke.214
+ ___65-[NetworkPerformanceFeed setPreferCellOverWiFiWithOptions:reply:]_block_invoke.216
+ ___67-[NWNetworkOfInterestManager canUseOnAlternateNOI:appStates:reply:]_block_invoke.191
+ ___67-[NWNetworkOfInterestManager canUseOnAlternateNOI:appStates:reply:]_block_invoke.192
+ ___70-[NWNetworkOfInterestManager dayOfWeekPredictionGroupingForNOI:reply:]_block_invoke.195
+ ___70-[NWNetworkOfInterestManager dayOfWeekPredictionGroupingForNOI:reply:]_block_invoke.196
+ ___70-[NWNetworkOfInterestManager networkAttachmentInfoForScopedNOI:reply:]_block_invoke.180
+ ___70-[NWNetworkOfInterestManager networkAttachmentInfoForScopedNOI:reply:]_block_invoke.181
+ ___72-[NWNetworkOfInterestManager foregroundNetworkActivityUnderwayOn:reply:]_block_invoke.186
+ ___72-[NWNetworkOfInterestManager foregroundNetworkActivityUnderwayOn:reply:]_block_invoke.187
+ ___74-[UsageFeed(NetworkDomains) performNetworkDomainsActionWithOptions:reply:]_block_invoke.703
+ ___75-[NWNetworkOfInterestManager trafficInvitesHourlyDistributionForNOI:reply:]_block_invoke.199
+ ___75-[NWNetworkOfInterestManager trafficInvitesHourlyDistributionForNOI:reply:]_block_invoke.200
+ ___83-[NWNetworkOfInterestManager estimatedDataTransferTimeOnNOI:withPayloadInfo:reply:]_block_invoke.184
+ ___83-[NWNetworkOfInterestManager estimatedDataTransferTimeOnNOI:withPayloadInfo:reply:]_block_invoke.185
+ ___84-[NWNetworkOfInterestManager inquireNOIFor:orPredicate:requestedKeys:options:reply:]_block_invoke.170
+ ___84-[NWNetworkOfInterestManager inquireNOIFor:orPredicate:requestedKeys:options:reply:]_block_invoke.171
+ ___92-[NetworkPerformanceFeed watchpointOn:forIdentifier:andKey:onThreshold:withOptions:uponHit:]_block_invoke.210
+ ___92-[NetworkPerformanceFeed watchpointOn:forIdentifier:andKey:onThreshold:withOptions:uponHit:]_block_invoke.211
+ ___Block_byref_object_copy_.576
+ ___Block_byref_object_dispose_.577
+ ___block_literal_global.589
+ ___block_literal_global.595
+ ___block_literal_global.604
+ _kPerformanceNetAttachFallbacks
+ _kPerformanceNetAttachMigrations
+ _kPerformanceNetAttachPartialConnectivityDetections
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x7
+ _objc_retain_x9
- ___100-[UsageFeed(NetworkDomains) _networkDomainsQueryViewTypeApp:entityName:limit:actions:callbackBlock:]_block_invoke.623
- ___108-[UsageFeed(NetworkDomains) networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:reply:]_block_invoke.587
- ___123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.691
- ___123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.693
- ___123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.695
- ___124-[UsageFeed(NetworkDomains) networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:fetchProperties:reply:]_block_invoke.580
- ___124-[UsageFeed(NetworkDomains) networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:fetchProperties:reply:]_block_invoke.584
- ___164-[UsageFeed(NetworkDomains) _performNetDomainsQueryOnService:entityName:fetchProps:pred:sort:actions:queryTimer:replyProcessBlock:accumulatedResults:callbackBlock:]_block_invoke.576
- ___237-[UsageFeed(NetworkDomains) __networkDomainsQueryDomains:entityName:unnamedDomainsOption:limit:actions:accumulatedResults:aggregateProperty:predicate:altAggregateProperty:altPredicate:ipAggregateProperty:replyProcessBlock:callbackBlock:]_block_invoke.651
- ___237-[UsageFeed(NetworkDomains) __networkDomainsQueryDomains:entityName:unnamedDomainsOption:limit:actions:accumulatedResults:aggregateProperty:predicate:altAggregateProperty:altPredicate:ipAggregateProperty:replyProcessBlock:callbackBlock:]_block_invoke.654
- ___237-[UsageFeed(NetworkDomains) __networkDomainsQueryDomains:entityName:unnamedDomainsOption:limit:actions:accumulatedResults:aggregateProperty:predicate:altAggregateProperty:altPredicate:ipAggregateProperty:replyProcessBlock:callbackBlock:]_block_invoke_2.652
- ___38-[NWNetworkOfInterestManager _connect]_block_invoke.129
- ___49-[NetworkPerformanceFeed resetDataForKeys:reply:]_block_invoke.209
- ___53-[NWNetworkOfInterestManager proxyHaveNOIs:tornDown:]_block_invoke.201
- ___56-[NWNetworkOfInterestManager linkThroughputOnNOI:reply:]_block_invoke.180
- ___56-[NWNetworkOfInterestManager linkThroughputOnNOI:reply:]_block_invoke.181
- ___57-[NWNetworkOfInterestManager instantQualityForNOI:reply:]_block_invoke.174
- ___57-[NWNetworkOfInterestManager instantQualityForNOI:reply:]_block_invoke.175
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.157
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.158
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.195
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.199
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.200
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.206
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke_2.196
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke_2.201
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke_2.203
- ___59-[NWNetworkOfInterestManager errorPredictionsForNOI:reply:]_block_invoke.191
- ___59-[NWNetworkOfInterestManager errorPredictionsForNOI:reply:]_block_invoke.192
- ___59-[NWNetworkOfInterestManager trainingProgressForNOI:reply:]_block_invoke.195
- ___59-[NWNetworkOfInterestManager trainingProgressForNOI:reply:]_block_invoke.196
- ___60-[NWNetworkOfInterestManager interfaceTimelineForNOI:reply:]_block_invoke.199
- ___60-[NWNetworkOfInterestManager interfaceTimelineForNOI:reply:]_block_invoke.200
- ___60-[NWNetworkOfInterestManager updatePredictionsForNOI:reply:]_block_invoke.171
- ___60-[NWNetworkOfInterestManager updatePredictionsForNOI:reply:]_block_invoke.172
- ___60-[UsageFeed(NetworkDomains) getNetworkDomainsOptions:reply:]_block_invoke.703
- ___60-[UsageFeed(NetworkDomains) setNetworkDomainsOptions:reply:]_block_invoke.702
- ___63-[NWNetworkOfInterestManager auditableLinkQualityForNOI:reply:]_block_invoke.176
- ___63-[NWNetworkOfInterestManager auditableLinkQualityForNOI:reply:]_block_invoke.177
- ___65-[NetworkPerformanceFeed getPreferCellOverWiFiWithOptions:reply:]_block_invoke.211
- ___65-[NetworkPerformanceFeed setPreferCellOverWiFiWithOptions:reply:]_block_invoke.213
- ___67-[NWNetworkOfInterestManager canUseOnAlternateNOI:appStates:reply:]_block_invoke.189
- ___67-[NWNetworkOfInterestManager canUseOnAlternateNOI:appStates:reply:]_block_invoke.190
- ___70-[NWNetworkOfInterestManager dayOfWeekPredictionGroupingForNOI:reply:]_block_invoke.193
- ___70-[NWNetworkOfInterestManager dayOfWeekPredictionGroupingForNOI:reply:]_block_invoke.194
- ___70-[NWNetworkOfInterestManager networkAttachmentInfoForScopedNOI:reply:]_block_invoke.178
- ___70-[NWNetworkOfInterestManager networkAttachmentInfoForScopedNOI:reply:]_block_invoke.179
- ___72-[NWNetworkOfInterestManager foregroundNetworkActivityUnderwayOn:reply:]_block_invoke.184
- ___72-[NWNetworkOfInterestManager foregroundNetworkActivityUnderwayOn:reply:]_block_invoke.185
- ___74-[UsageFeed(NetworkDomains) performNetworkDomainsActionWithOptions:reply:]_block_invoke.704
- ___75-[NWNetworkOfInterestManager trafficInvitesHourlyDistributionForNOI:reply:]_block_invoke.197
- ___75-[NWNetworkOfInterestManager trafficInvitesHourlyDistributionForNOI:reply:]_block_invoke.198
- ___83-[NWNetworkOfInterestManager estimatedDataTransferTimeOnNOI:withPayloadInfo:reply:]_block_invoke.182
- ___83-[NWNetworkOfInterestManager estimatedDataTransferTimeOnNOI:withPayloadInfo:reply:]_block_invoke.183
- ___84-[NWNetworkOfInterestManager inquireNOIFor:orPredicate:requestedKeys:options:reply:]_block_invoke.168
- ___84-[NWNetworkOfInterestManager inquireNOIFor:orPredicate:requestedKeys:options:reply:]_block_invoke.169
- ___92-[NetworkPerformanceFeed watchpointOn:forIdentifier:andKey:onThreshold:withOptions:uponHit:]_block_invoke.207
- ___92-[NetworkPerformanceFeed watchpointOn:forIdentifier:andKey:onThreshold:withOptions:uponHit:]_block_invoke.208
- ___Block_byref_object_copy_.577
- ___Block_byref_object_dispose_.578
- ___block_literal_global.590
- ___block_literal_global.596
- ___block_literal_global.605
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "fallbacks"
+ "migrations"
+ "partialConnectivityDetections"
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"<SFClientInterfaceProxy>\""
- "@\"<SFServiceInterface>\""
- "@\"AnalyticsWorkspace\""
- "@\"NSArray\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"UsageAnalytics\""
- "@120@0:8@16^{route_stats_stuct=dddddddddddddddddddddddd}24@32@40@48@56@64@72@80@88@96@104@112"
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@28@0:8@16i24"
- "@32@0:8:16@24"
- "@32@0:8@16^{flow_stats_stuct=dddddddd}24"
- "@36@0:8@16@24B32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8I16I20@24@32"
- "@44@0:8@16@24B32^B36"
- "@48@0:8@16@24@32B40B44"
- "@52@0:8@16@24^B32B40^B44"
- "@56@0:8@16@24@32^d40@48"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B28@0:8i16@?20"
- "B32@0:8@16@?24"
- "B32@0:8i16B20@?24"
- "B36@0:8i16@20@?28"
- "B40@0:8@16@24@32"
- "B40@0:8@16@24@?32"
- "B44@0:8@16@24@32I40"
- "B44@0:8@16@24I32@?36"
- "B48@0:8@16@24@32@40"
- "B48@0:8@16@24@32@?40"
- "B48@0:8@16@24^Q32^Q40"
- "B56@0:8@16@24@32@40@?48"
- "B56@0:8@16@24@32S40S44@?48"
- "B56@0:8@16Q24Q32@40@?48"
- "B60@0:8@16@24S32@36@44@?52"
- "B60@0:8i16@20@28d36@44@?52"
- "B68@0:8@16@24S32@36@44@52@?60"
- "I"
- "NSObject"
- "NWNetworkOfInterestClientProxy"
- "NWNetworkOfInterestManager"
- "NetworkDomains"
- "NetworkPerformanceFeed"
- "ProcessNetStatsIndividualEntity"
- "Q"
- "Q16@0:8"
- "SFClientInterface"
- "SFClientInterfaceProxy"
- "SFServiceInterface"
- "T#,R"
- "T@\"<SFClientInterfaceProxy>\",W,N,V_delegate"
- "T@\"<SFServiceInterface>\",&,N,V_service"
- "T@\"NSArray\",&,N,V_processFeedData"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_callerQueue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "T@,N,V_delegate"
- "T@,W,N,V_delegate"
- "TQ,R"
- "UTF8String"
- "UUIDString"
- "UsageFeed"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "__networkDomainsQueryDomains:entityName:unnamedDomainsOption:limit:actions:accumulatedResults:aggregateProperty:predicate:altAggregateProperty:altPredicate:ipAggregateProperty:replyProcessBlock:callbackBlock:"
- "__networkDomainsQuerySecondLevelViewDomains:entityName:unnamedDomainsOption:limit:actions:viewPredicate:callbackBlock:"
- "__networkDomainsQueryWebsites:entityName:verificationContext:limit:actions:viewPredicate:callbackBlock:"
- "_batchFetchCallbackWithResults:logPrefix:entityName:pred:service:limit:offset:container:actions:reply:"
- "_calendarUsagePresentation:nameKind:source:"
- "_callerQueue"
- "_commonFinalizeRequestFor:orPredicate:options:isStaged:"
- "_commonTrackRequestFor:isAny:isBuiltin:options:isCustom:"
- "_composeLiveUsagePredicateWithNames:kind:isProcNameKey:isSweep:"
- "_composePredicateLineWithName:keyPath:isSweep:wantGeneric:gotGeneric:"
- "_connect"
- "_connection"
- "_consultReturn:advice:"
- "_delegate"
- "_flowMetricsPresentationFromRoll:source:"
- "_formatInstantRouteMetrics:"
- "_formatWatchpointHit:"
- "_getUsageKeyWithProcess:bundleID:extension:isProcNameKey:showExtension:"
- "_legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:"
- "_networkDomainsQueryViewTypeApp:entityName:limit:actions:callbackBlock:"
- "_networkDomainsQueryViewTypeAppDomains:entityName:bundleIdentifier:unnamedDomainsOption:limit:actions:callbackBlock:"
- "_networkDomainsQueryViewTypeAppDomainsOtherContent:entityName:bundleIdentifier:unnamedDomainsOption:limit:actions:callbackBlock:"
- "_networkDomainsQueryViewTypeAppWebsites:entityName:bundleIdentifier:verificationContext:limit:actions:callbackBlock:"
- "_networkDomainsQueryViewTypeDomain:entityName:unnamedDomainsOption:limit:actions:callbackBlock:"
- "_networkDomainsQueryViewTypeDomainApps:entityName:domain:limit:actions:callbackBlock:"
- "_networkDomainsQueryViewTypeDomainWebsites:entityName:domain:limit:actions:callbackBlock:"
- "_networkDomainsQueryViewTypeWebsite:entityName:verificationContext:limit:actions:callbackBlock:"
- "_networkDomainsQueryViewTypeWebsiteApps:entityName:website:limit:actions:callbackBlock:"
- "_networkDomainsQueryViewTypeWebsiteDomains:entityName:website:unnamedDomainsOption:limit:actions:callbackBlock:"
- "_networkDomainsQueryViewTypeWebsiteHits:entityName:website:limit:actions:callbackBlock:"
- "_normalizedOpts:toNetwork:"
- "_performNetDomainsQueryOnService:entityName:fetchProps:pred:sort:actions:queryTimer:replyProcessBlock:accumulatedResults:callbackBlock:"
- "_performRollUp:andMetadata:from:until:"
- "_processFeedData"
- "_processLiveUsageWithPredicate:attributesBlock:outcomeBlock:"
- "_processLiveUsageWithUsages:attributesBlock:outcomeBlock:"
- "_proxyHaveNOIs"
- "_proxyUpdateNOI"
- "_rollFlowMetricsValuesFromDict:toDict:forKey:andRequest:"
- "_rollRouteMetricsValuesFromDict:toDict:forKey:"
- "_rollUsageValuesFromDict:toDict:forKey:subscriberTag:"
- "_rollValuesFrom:toDict:"
- "_routeMetricsPresentationFromRoll:source:since:isKnownGood:isLowInternetDL:isLowInternetUL:isHotSpot:rpmAverage:rpmCount:rpmVariance:rpmExitAverage:rpmExitCount:rpmExitVariance:"
- "_service"
- "_triggerAutoBugCaptureForSubType:subtypeContext:events:replyBlock:"
- "_typicalUsagePresentation:nameKind:source:"
- "_unloadState"
- "_usagePresentationWithProcess:bundleID:extension:source:since:"
- "_validateKeyPath:"
- "addAggregateProperty:"
- "addFetchProperty:"
- "addGroupByProperty:"
- "addObject:"
- "addObjectsFromArray:"
- "algosScoreToDateWithOptionsFor:nameKind:startTime:options:reply:"
- "allKeys"
- "allKeysForObject:"
- "allObjects"
- "allValues"
- "andPredicateWithSubpredicates:"
- "anyObject"
- "arrayWithObjects:count:"
- "auditableLinkQualityForNOI:reply:"
- "autorelease"
- "boolValue"
- "bytes"
- "calendarUsageFor:nameKind:dayResolution:daySlot:weekSlot:reply:"
- "callerQueue"
- "canUseOnAlternateNOI:appStates:reply:"
- "canUseOnAlternateNOI:apps:reply:"
- "class"
- "cleanupNDFDeviceRecordsWithReply:"
- "clearLoggingCounters"
- "closing"
- "compare:"
- "componentsSeparatedByString:"
- "conformsToProtocol:"
- "connection"
- "containsObject:"
- "containsString:"
- "countByEnumeratingWithState:objects:count:"
- "createEndpointEntryFrom:withKey:showDetails:"
- "createSnapshotFor:pred:actions:reply:"
- "dataWithBytes:length:"
- "date"
- "dayOfWeekPredictionGroupingForNOI:reply:"
- "dealloc"
- "debugDescription"
- "defaultWorkspace"
- "delegate"
- "description"
- "destroy"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "didStartTrackingNOI:"
- "didStopTrackingAllNOIs:"
- "didStopTrackingNOI:"
- "displayLoggingCounters:"
- "donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:latitude:longitude:reply:"
- "doubleValue"
- "earlierDate:"
- "entityName"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "errorPredictionsForNOI:reply:"
- "errorWithDomain:code:userInfo:"
- "escapedPatternForString:"
- "estimatedDataTransferTimeOnNOI:withPayloadInfo:reply:"
- "exportedInterface"
- "fetchEntitiesFreeForm:sortDesc:"
- "fetchNDFDeviceRecordsWithReply:"
- "foregroundNetworkActivityUnderwayOn:reply:"
- "fullScorecardFor:options:reply:"
- "getNetworkBitmapsWithNames:startTime:endTime:options:reply:"
- "getNetworkDomainsOptions:reply:"
- "getOption:inScopes:reply:"
- "getPreferCellOverWiFiWithOptions:reply:"
- "getUsageOption:reply:"
- "groupRecordsByBundleId:"
- "handleAnalytics"
- "hasApp"
- "hasProcess"
- "hash"
- "haveNOIs:tornDown:"
- "identifierForUUID:reply:"
- "identityAttrsOnly"
- "init"
- "initWithArray:"
- "initWithCapacity:"
- "initWithDelegate:"
- "initWithDictionary:"
- "initWithFormat:"
- "initWithKey:ascending:"
- "initWithMachServiceName:options:"
- "initWithObjects:"
- "initWithObjectsAndKeys:"
- "initWithSet:copyItems:"
- "initWithSpec:isAny:isBuiltin:scopedToLOI:flags:hasCustomSignature:"
- "initWithSuiteName:"
- "initWithUUIDString:"
- "initWithWorkspace:"
- "initWithWorkspace:entityName:withCache:"
- "initWithWorkspace:withCache:"
- "initWorkspaceWithService:"
- "inquireNOIFor:orPredicate:requestedKeys:options:reply:"
- "instantQualityForNOI:reply:"
- "intValue"
- "integerValue"
- "interfaceTimelineForNOI:reply:"
- "interfaceWithProtocol:"
- "internalQueue"
- "invalidate"
- "isClosing"
- "isEqual:"
- "isEqualToDictionary:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lastObject"
- "lastSkippedTag"
- "lastSubscriberTag"
- "laterDate:"
- "linkThroughputOnNOI:reply:"
- "listNDFDeviceObjectsWithIdentifier:reply:"
- "localizedDescription"
- "mutableCopy"
- "ndfClientCheckInWithReply:"
- "ndfClientSubscriptionIsActive:reply:"
- "networkAttachmentInfoForScopedNOI:reply:"
- "networkBitmapsToDateWithOptionsFor:startTime:endTime:options:reply:"
- "networkDomainInitiatedTypeString:"
- "networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:fetchProperties:reply:"
- "networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:reply:"
- "networkRestrictsMulticastTrafficWithReply:"
- "newFeedProcessData:"
- "null"
- "numAppended"
- "numNewlyCreated"
- "numRolledCellCounts"
- "numUnrolledCellCounts"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInteger:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "nwFunctionalInterfaceTypeForNWInterfaceSubtype:"
- "nwFunctionalInterfaceTypeForNWInterfaceType:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "performActionWithOptions:inScopes:reply:"
- "performAppEndpointTrackingPeriodicTasksWithReply:"
- "performAppExperiencePeriodicTasksWithReply:"
- "performAppPeriodicTasksWithReply:"
- "performAppTrackingPeriodicTasksWithReply:"
- "performNetworkDomainsActionWithOptions:reply:"
- "performPersistentStoreHealthCheckWithReply:"
- "performQueryOnEntity:fetchRequestProperties:pred:sort:actions:reply:"
- "performQueryOnEntity:pred:sort:actions:reply:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pingEndpoints:reply:"
- "predicateWithFormat:"
- "predictWaitUntilKnownGoodNetworkFor:matchSignature:reply:"
- "predictions"
- "prepProcessDataFractionWithTag:andMetadata:from:until:pollInterval:"
- "prepProcessDataFractionWithTag:from:until:pollInterval:"
- "processFeedData"
- "processInfo"
- "processName"
- "proxyHaveNOIs:tornDown:"
- "proxyUpdateNOI:keyPath:change:"
- "rangeOfString:"
- "rangeOfString:options:"
- "rawCounts:forType:txBytes:rxBytes:"
- "registryNOI"
- "release"
- "remoteObjectInterface"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllObjects"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObjectsInArray:"
- "resetDataFor:nameKind:inScopes:reply:"
- "resetDataForKeys:reply:"
- "resetUsageDataFor:nameKind:reply:"
- "resetUsageFor:nameKind:reply:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "retrieveActivityMetrics:reply:"
- "scopedToLOI"
- "self"
- "sendMessage:toEndpoints:reply:"
- "sendPayloadToDaemonWithReply:"
- "service"
- "setCallerQueue:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setConnection:"
- "setConsiderAlternateUpdate:"
- "setDelegate:"
- "setDiscretionaryTrafficInvited:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterfaceClass:"
- "setInterruptionHandler:"
- "setIsTrafficEligible:"
- "setLinkQuality:"
- "setNetworkDomainsOptions:reply:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOption:inScopes:reply:"
- "setPowerCostDL:"
- "setPowerCostUL:"
- "setPredictions:"
- "setPredictionsGeneratedAt:"
- "setPreferCellOverWiFiWithOptions:reply:"
- "setProcessFeedData:"
- "setQueue:"
- "setReferencePoint:reply:"
- "setRemoteObjectInterface:"
- "setService:"
- "setUsageOption:reply:"
- "setValue:forKey:"
- "setWillGetDiscretionaryTrafficInvites:"
- "setWithObject:"
- "setWithObjects:"
- "shortValue"
- "signatureWithDomain:type:subType:subtypeContext:detectedProcess:triggerThresholdValues:"
- "snapshotWithSignature:delay:events:payload:actions:reply:"
- "sortedArrayUsingComparator:"
- "stopTrackingNOIs:"
- "stringWithFormat:"
- "subarrayWithRange:"
- "subscribeToNOIsFor:orPredicate:options:"
- "superclass"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "timeIntervalSinceDate:"
- "trackAllBuiltinNOIsForInterfaceType:options:"
- "trackCustomNOI:options:"
- "trackNOIAnyForInterfaceSubtype:options:"
- "trackNOIAnyForInterfaceType:options:"
- "trafficInvitesHourlyDistributionForNOI:reply:"
- "trainModelAndScore:lastScoreDate:reply:"
- "trainingProgressForNOI:reply:"
- "triggerSendPayloadToDaemonWithInterval:leeway:reply:"
- "typicalUsageFor:nameKind:intervalKind:reply:"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "unsignedShortValue"
- "unsubscribeToNOIs:"
- "updateNOI:keyPath:change:"
- "updatePredictionsForNOI:reply:"
- "updatedNDFDeviceRecords:reply:"
- "usageConsultOn:onlyRelativeToReferencePoint:reply:"
- "usageMarkersWithTag:andMetadata:fromDate:untilDate:"
- "usageToDateFor:nameKind:reply:"
- "usageToDateWithOptionsFor:nameKind:options:reply:"
- "v120@0:8@16@24q32Q40@48@56@64@72@80@88@96@?104@?112"
- "v16@0:8"
- "v24@0:8@\"NSSet\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v28@0:8@\"NSSet\"16B24"
- "v28@0:8@16B24"
- "v28@0:8@?16i24"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"NSError\">20"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSObject<OS_xpc_object>\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?B>24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8q16@24"
- "v36@0:8B16@\"NSDate\"20@?<v@?@\"NSDictionary\"@\"NSError\">28"
- "v36@0:8B16@20@?28"
- "v40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?B>32"
- "v40@0:8@\"NSDictionary\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\">32"
- "v40@0:8@\"NSDictionary\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSObject<OS_xpc_object>\"24@?<v@?@\"NSString\"@\"NSError\">32"
- "v40@0:8@\"NWNetworkOfInterest\"16@\"NSPredicate\"24@\"NSDictionary\"32"
- "v40@0:8@\"NWNetworkOfInterest\"16@\"NSString\"24@\"NSDictionary\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@?24@?32"
- "v40@0:8I16@20@28f36"
- "v40@0:8q16q24@?32"
- "v40@0:8q16q24@?<v@?B>32"
- "v44@0:8@16@24@32B40"
- "v44@0:8C16B20B24@28@36"
- "v44@0:8I16I20@24@32f40"
- "v48@0:8@\"NSArray\"16@\"NSString\"24@\"NSDictionary\"32@?<v@?B>40"
- "v48@0:8@\"NSString\"16@\"NSPredicate\"24@\"NSDictionary\"32@?<v@?@\"NSUUID\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v56@0:8@\"NSString\"16@\"NSPredicate\"24@\"NSSortDescriptor\"32@\"NSDictionary\"40@?<v@?@\"NSArray\">48"
- "v56@0:8@\"NWNetworkOfInterest\"16@\"NSPredicate\"24@\"NSDictionary\"32@\"NSDictionary\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16@24Q32@40@?48"
- "v64@0:8@\"NSString\"16@\"FetchRequestPropertiesDescriptor\"24@\"NSPredicate\"32@\"NSSortDescriptor\"40@\"NSDictionary\"48@?<v@?@\"NSArray\">56"
- "v64@0:8@16@24@32@40@48@?56"
- "v64@0:8@16@24@32Q40@48@?56"
- "v64@0:8@16@24q32Q40@48@?56"
- "v72@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40d48d56@?<v@?@\"NSDictionary\"@\"NSError\">64"
- "v72@0:8@16@24@32@40d48d56@?64"
- "v72@0:8@16@24@32Q40@48@56@?64"
- "v72@0:8@16@24@32q40Q48@56@?64"
- "v72@0:8@16@24q32Q40@48@56@?64"
- "v96@0:8@16@24@32@40@48@56@64@?72@80@?88"
- "v96@0:8@16r*24@32@40@48Q56Q64@72@80@?88"
- "valueForKey:"
- "watchpointOn:forIdentifier:andKey:onThreshold:withOptions:uponHit:"
- "workspace"
- "zone"

```
