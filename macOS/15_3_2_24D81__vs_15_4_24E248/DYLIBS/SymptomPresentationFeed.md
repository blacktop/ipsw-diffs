## SymptomPresentationFeed

> `/System/Library/PrivateFrameworks/Symptoms.framework/Versions/A/Frameworks/SymptomPresentationFeed.framework/Versions/A/SymptomPresentationFeed`

```diff

-2001.80.5.0.0
-  __TEXT.__text: 0x1ae90
+2022.100.26.0.0
+  __TEXT.__text: 0x1b000
   __TEXT.__auth_stubs: 0x270
-  __TEXT.__objc_methlist: 0x570
-  __TEXT.__cstring: 0xfeb
+  __TEXT.__objc_methlist: 0x7c8
+  __TEXT.__cstring: 0x1082
   __TEXT.__const: 0x100
   __TEXT.__gcc_except_tab: 0x484
   __TEXT.__oslogstring: 0x1f57
-  __TEXT.__unwind_info: 0x3e0
+  __TEXT.__unwind_info: 0x3e8
   __TEXT.__objc_classname: 0xdb
-  __TEXT.__objc_methname: 0x1fad
-  __TEXT.__objc_methtype: 0xa42
+  __TEXT.__objc_methname: 0x1fc0
+  __TEXT.__objc_methtype: 0xa66
   __TEXT.__objc_stubs: 0x1660
   __DATA_CONST.__got: 0x328
-  __DATA_CONST.__const: 0x490
+  __DATA_CONST.__const: 0x4e0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x778
+  __DATA_CONST.__objc_selrefs: 0x848
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__auth_got: 0x148
   __AUTH_CONST.__const: 0xac0
-  __AUTH_CONST.__cfstring: 0x19c0
-  __AUTH_CONST.__objc_const: 0x1010
+  __AUTH_CONST.__cfstring: 0x1b80
+  __AUTH_CONST.__objc_const: 0xb98
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/Symptoms.framework/Versions/A/Frameworks/SymptomAnalytics.framework/Versions/A/SymptomAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 08D399B2-6811-3B0A-968A-25EE5402030C
-  Functions: 303
-  Symbols:   920
-  CStrings:  990
+  UUID: C53AFB4B-CD0E-395C-BDBC-2E3DF8CB199C
+  Functions: 307
+  Symbols:   934
+  CStrings:  1019
 
Symbols:
+ -[NWNetworkOfInterestManager _connect].cold.1
+ GCC_except_table68
+ GCC_except_table79
+ __123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.507
+ __123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.509
+ __123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.512
+ __164-[UsageFeed(NetworkDomains) _performNetDomainsQueryOnService:entityName:fetchProps:pred:sort:actions:queryTimer:replyProcessBlock:accumulatedResults:callbackBlock:]_block_invoke.504
+ __34-[UsageFeed getUsageOption:reply:]_block_invoke.421
+ __34-[UsageFeed setUsageOption:reply:]_block_invoke.418
+ __37-[UsageFeed identifierForUUID:reply:]_block_invoke.426
+ __38-[NWNetworkOfInterestManager _connect]_block_invoke.104
+ __46-[UsageFeed resetUsageDataFor:nameKind:reply:]_block_invoke.422
+ __49-[NetworkPerformanceFeed resetDataForKeys:reply:]_block_invoke.197
+ __53-[NWNetworkOfInterestManager proxyHaveNOIs:tornDown:]_block_invoke.186
+ __56-[NWNetworkOfInterestManager linkThroughputOnNOI:reply:]_block_invoke.162
+ __57-[NWNetworkOfInterestManager instantQualityForNOI:reply:]_block_invoke.156
+ __57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.145
+ __57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.182
+ __57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.188
+ __57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.192
+ __57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke_2.189
+ __59-[NWNetworkOfInterestManager errorPredictionsForNOI:reply:]_block_invoke.177
+ __59-[NWNetworkOfInterestManager trainingProgressForNOI:reply:]_block_invoke.181
+ __60-[NWNetworkOfInterestManager interfaceTimelineForNOI:reply:]_block_invoke.185
+ __60-[NWNetworkOfInterestManager updatePredictionsForNOI:reply:]_block_invoke.151
+ __62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.353
+ __62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.388
+ __62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.391
+ __62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.394
+ __62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke_2.396
+ __63-[NWNetworkOfInterestManager auditableLinkQualityForNOI:reply:]_block_invoke.158
+ __67-[NWNetworkOfInterestManager canUseOnAlternateNOI:appStates:reply:]_block_invoke.173
+ __70-[NWNetworkOfInterestManager dayOfWeekPredictionGroupingForNOI:reply:]_block_invoke.179
+ __72-[NWNetworkOfInterestManager foregroundNetworkActivityUnderwayOn:reply:]_block_invoke.166
+ __75-[NWNetworkOfInterestManager trafficInvitesHourlyDistributionForNOI:reply:]_block_invoke.183
+ __77-[UsageFeed algosScoreToDateWithOptionsFor:nameKind:startTime:options:reply:]_block_invoke.409
+ __80-[UsageFeed networkBitmapsToDateWithOptionsFor:startTime:endTime:options:reply:]_block_invoke.349
+ __83-[NWNetworkOfInterestManager estimatedDataTransferTimeOnNOI:withPayloadInfo:reply:]_block_invoke.164
+ __84-[NWNetworkOfInterestManager inquireNOIFor:orPredicate:requestedKeys:options:reply:]_block_invoke.146
+ __92-[NetworkPerformanceFeed watchpointOn:forIdentifier:andKey:onThreshold:withOptions:uponHit:]_block_invoke.196
+ __Block_byref_object_copy_.505
+ __Block_byref_object_dispose_.506
+ ___block_descriptor_64_e8_32s40s48bs56bs_e29_v24?0"NSArray"8"NSError"16l
+ ___copy_helper_block_e8_32s40s48b56b
+ _kUsageNetworkBt
+ _kUsageNetworkBtExpensiveInBytes
+ _kUsageNetworkBtExpensiveOutBytes
+ _kUsageNetworkBtInBytes
+ _kUsageNetworkBtInBytes_mean
+ _kUsageNetworkBtInBytes_var
+ _kUsageNetworkBtOutBytes
+ _kUsageNetworkBtOutBytes_mean
+ _kUsageNetworkBtOutBytes_var
+ _kUsageNetworkBtSampleCount
+ networkperfLogHandle.cold.1
+ noiLogHandle.cold.1
+ usageLogHandle.cold.1
- GCC_except_table78
- __123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.466
- __123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.468
- __123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.471
- __164-[UsageFeed(NetworkDomains) _performNetDomainsQueryOnService:entityName:fetchProps:pred:sort:actions:queryTimer:replyProcessBlock:accumulatedResults:callbackBlock:]_block_invoke.463
- __34-[UsageFeed getUsageOption:reply:]_block_invoke.380
- __34-[UsageFeed setUsageOption:reply:]_block_invoke.377
- __37-[UsageFeed identifierForUUID:reply:]_block_invoke.385
- __38-[NWNetworkOfInterestManager _connect]_block_invoke.103
- __46-[UsageFeed resetUsageDataFor:nameKind:reply:]_block_invoke.381
- __49-[NetworkPerformanceFeed resetDataForKeys:reply:]_block_invoke.196
- __53-[NWNetworkOfInterestManager proxyHaveNOIs:tornDown:]_block_invoke.185
- __56-[NWNetworkOfInterestManager linkThroughputOnNOI:reply:]_block_invoke.160
- __57-[NWNetworkOfInterestManager instantQualityForNOI:reply:]_block_invoke.154
- __57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.143
- __57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.181
- __57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.184
- __57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.190
- __57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke_2.188
- __59-[NWNetworkOfInterestManager errorPredictionsForNOI:reply:]_block_invoke.175
- __59-[NWNetworkOfInterestManager trainingProgressForNOI:reply:]_block_invoke.179
- __60-[NWNetworkOfInterestManager interfaceTimelineForNOI:reply:]_block_invoke.183
- __60-[NWNetworkOfInterestManager updatePredictionsForNOI:reply:]_block_invoke.149
- __62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.311
- __62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.346
- __62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.349
- __62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.352
- __62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke_2.354
- __63-[NWNetworkOfInterestManager auditableLinkQualityForNOI:reply:]_block_invoke.156
- __67-[NWNetworkOfInterestManager canUseOnAlternateNOI:appStates:reply:]_block_invoke.171
- __70-[NWNetworkOfInterestManager dayOfWeekPredictionGroupingForNOI:reply:]_block_invoke.177
- __72-[NWNetworkOfInterestManager foregroundNetworkActivityUnderwayOn:reply:]_block_invoke.164
- __75-[NWNetworkOfInterestManager trafficInvitesHourlyDistributionForNOI:reply:]_block_invoke.181
- __77-[UsageFeed algosScoreToDateWithOptionsFor:nameKind:startTime:options:reply:]_block_invoke.368
- __80-[UsageFeed networkBitmapsToDateWithOptionsFor:startTime:endTime:options:reply:]_block_invoke.307
- __83-[NWNetworkOfInterestManager estimatedDataTransferTimeOnNOI:withPayloadInfo:reply:]_block_invoke.162
- __84-[NWNetworkOfInterestManager inquireNOIFor:orPredicate:requestedKeys:options:reply:]_block_invoke.144
- __92-[NetworkPerformanceFeed watchpointOn:forIdentifier:andKey:onThreshold:withOptions:uponHit:]_block_invoke.194
- __Block_byref_object_copy_.464
- __Block_byref_object_dispose_.465
- ___block_descriptor_72_e8_32s40s48s56bs64bs_e29_v24?0"NSArray"8"NSError"16l
- ___copy_helper_block_e8_32s40s48s56b64b
CStrings:
+ "bt"
+ "btExpInBytes"
+ "btExpOutBytes"
+ "btIN"
+ "btIN_exp"
+ "btInBytes"
+ "btInBytesMean"
+ "btInBytesVar"
+ "btOUT"
+ "btOUT_exp"
+ "btOutBytes"
+ "btOutBytesMean"
+ "btOutBytesVar"
+ "btSampleCount"
+ "donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:latitude:longitude:reply:"
+ "v72@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40d48d56@?<v@?@\"NSDictionary\"@\"NSError\">64"
+ "v72@0:8@16@24@32@40d48d56@?64"
- "donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:reply:"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"

```
