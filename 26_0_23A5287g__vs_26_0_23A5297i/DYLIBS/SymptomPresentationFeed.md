## SymptomPresentationFeed

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationFeed.framework/SymptomPresentationFeed`

```diff

-2144.0.0.0.0
+2150.0.0.502.1
   __TEXT.__text: 0x207cc
   __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_methlist: 0x90c
+  __TEXT.__objc_methlist: 0x918
   __TEXT.__cstring: 0x153f
   __TEXT.__const: 0xe8
   __TEXT.__gcc_except_tab: 0x69c
   __TEXT.__oslogstring: 0x25e3
   __TEXT.__unwind_info: 0x470
   __TEXT.__objc_classname: 0xdb
-  __TEXT.__objc_methname: 0x2938
+  __TEXT.__objc_methname: 0x295a
   __TEXT.__objc_methtype: 0xcf6
   __TEXT.__objc_stubs: 0x1be0
   __DATA_CONST.__got: 0x3d8

   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9d8
+  __DATA_CONST.__objc_selrefs: 0x9e0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__auth_got: 0x260
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0x2140
-  __AUTH_CONST.__objc_const: 0xd50
+  __AUTH_CONST.__objc_const: 0xd78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x30
   __DATA.__objc_ivar: 0x60

   - /System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomAnalytics.framework/SymptomAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 89478094-6164-3B04-8FCB-E2CDDB52D502
+  UUID: D6DFCBD0-2227-30A7-8AEC-AC2ADD591536
   Functions: 307
   Symbols:   1373
-  CStrings:  1222
+  CStrings:  1223
 
Symbols:
+ ___38-[NWNetworkOfInterestManager _connect]_block_invoke.129
+ ___49-[NetworkPerformanceFeed resetDataForKeys:reply:]_block_invoke.209
+ ___53-[NWNetworkOfInterestManager proxyHaveNOIs:tornDown:]_block_invoke.201
+ ___56-[NWNetworkOfInterestManager linkThroughputOnNOI:reply:]_block_invoke.181
+ ___57-[NWNetworkOfInterestManager instantQualityForNOI:reply:]_block_invoke.175
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.158
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.195
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.200
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.202
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.206
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke_2.196
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke_2.201
+ ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke_2.203
+ ___59-[NWNetworkOfInterestManager errorPredictionsForNOI:reply:]_block_invoke.192
+ ___59-[NWNetworkOfInterestManager trainingProgressForNOI:reply:]_block_invoke.196
+ ___60-[NWNetworkOfInterestManager interfaceTimelineForNOI:reply:]_block_invoke.200
+ ___60-[NWNetworkOfInterestManager updatePredictionsForNOI:reply:]_block_invoke.172
+ ___63-[NWNetworkOfInterestManager auditableLinkQualityForNOI:reply:]_block_invoke.177
+ ___65-[NetworkPerformanceFeed getPreferCellOverWiFiWithOptions:reply:]_block_invoke.211
+ ___65-[NetworkPerformanceFeed setPreferCellOverWiFiWithOptions:reply:]_block_invoke.213
+ ___67-[NWNetworkOfInterestManager canUseOnAlternateNOI:appStates:reply:]_block_invoke.190
+ ___70-[NWNetworkOfInterestManager dayOfWeekPredictionGroupingForNOI:reply:]_block_invoke.194
+ ___70-[NWNetworkOfInterestManager networkAttachmentInfoForScopedNOI:reply:]_block_invoke.179
+ ___72-[NWNetworkOfInterestManager foregroundNetworkActivityUnderwayOn:reply:]_block_invoke.185
+ ___75-[NWNetworkOfInterestManager trafficInvitesHourlyDistributionForNOI:reply:]_block_invoke.198
+ ___83-[NWNetworkOfInterestManager estimatedDataTransferTimeOnNOI:withPayloadInfo:reply:]_block_invoke.183
+ ___84-[NWNetworkOfInterestManager inquireNOIFor:orPredicate:requestedKeys:options:reply:]_block_invoke.169
+ ___92-[NetworkPerformanceFeed watchpointOn:forIdentifier:andKey:onThreshold:withOptions:uponHit:]_block_invoke.208
- ___38-[NWNetworkOfInterestManager _connect]_block_invoke.128
- ___49-[NetworkPerformanceFeed resetDataForKeys:reply:]_block_invoke.208
- ___53-[NWNetworkOfInterestManager proxyHaveNOIs:tornDown:]_block_invoke.200
- ___56-[NWNetworkOfInterestManager linkThroughputOnNOI:reply:]_block_invoke.179
- ___57-[NWNetworkOfInterestManager instantQualityForNOI:reply:]_block_invoke.173
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.156
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.194
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.198
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.201
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke.204
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke_2.195
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke_2.200
- ___57-[NetworkPerformanceFeed fullScorecardFor:options:reply:]_block_invoke_2.202
- ___59-[NWNetworkOfInterestManager errorPredictionsForNOI:reply:]_block_invoke.190
- ___59-[NWNetworkOfInterestManager trainingProgressForNOI:reply:]_block_invoke.194
- ___60-[NWNetworkOfInterestManager interfaceTimelineForNOI:reply:]_block_invoke.198
- ___60-[NWNetworkOfInterestManager updatePredictionsForNOI:reply:]_block_invoke.170
- ___63-[NWNetworkOfInterestManager auditableLinkQualityForNOI:reply:]_block_invoke.175
- ___65-[NetworkPerformanceFeed getPreferCellOverWiFiWithOptions:reply:]_block_invoke.210
- ___65-[NetworkPerformanceFeed setPreferCellOverWiFiWithOptions:reply:]_block_invoke.212
- ___67-[NWNetworkOfInterestManager canUseOnAlternateNOI:appStates:reply:]_block_invoke.188
- ___70-[NWNetworkOfInterestManager dayOfWeekPredictionGroupingForNOI:reply:]_block_invoke.192
- ___70-[NWNetworkOfInterestManager networkAttachmentInfoForScopedNOI:reply:]_block_invoke.177
- ___72-[NWNetworkOfInterestManager foregroundNetworkActivityUnderwayOn:reply:]_block_invoke.183
- ___75-[NWNetworkOfInterestManager trafficInvitesHourlyDistributionForNOI:reply:]_block_invoke.196
- ___83-[NWNetworkOfInterestManager estimatedDataTransferTimeOnNOI:withPayloadInfo:reply:]_block_invoke.181
- ___84-[NWNetworkOfInterestManager inquireNOIFor:orPredicate:requestedKeys:options:reply:]_block_invoke.167
- ___92-[NetworkPerformanceFeed watchpointOn:forIdentifier:andKey:onThreshold:withOptions:uponHit:]_block_invoke.206
CStrings:
+ "cleanupNDFDeviceRecordsWithReply:"

```
