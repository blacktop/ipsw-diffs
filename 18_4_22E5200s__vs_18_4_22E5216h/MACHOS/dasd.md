## dasd

> `/usr/libexec/dasd`

```diff

-1856.100.76.502.1
-  __TEXT.__text: 0x1061ec
-  __TEXT.__auth_stubs: 0x12e0
-  __TEXT.__objc_stubs: 0x16320
-  __TEXT.__objc_methlist: 0x10188
-  __TEXT.__const: 0x8e0
-  __TEXT.__objc_methname: 0x25d1d
-  __TEXT.__cstring: 0xd121
-  __TEXT.__oslogstring: 0xf90a
-  __TEXT.__objc_classname: 0x17a7
-  __TEXT.__objc_methtype: 0x3448
-  __TEXT.__gcc_except_tab: 0x4480
+1856.100.90.0.0
+  __TEXT.__text: 0x105158
+  __TEXT.__auth_stubs: 0x12d0
+  __TEXT.__objc_stubs: 0x16100
+  __TEXT.__objc_methlist: 0xffa0
+  __TEXT.__const: 0x8d8
+  __TEXT.__objc_methname: 0x2583e
+  __TEXT.__cstring: 0xd0c0
+  __TEXT.__oslogstring: 0xf89c
+  __TEXT.__objc_classname: 0x1747
+  __TEXT.__objc_methtype: 0x3398
+  __TEXT.__gcc_except_tab: 0x44ec
   __TEXT.__dlopen_cstrs: 0x488
-  __TEXT.__unwind_info: 0x3af0
-  __DATA_CONST.__auth_got: 0x980
+  __TEXT.__unwind_info: 0x3aa0
+  __DATA_CONST.__auth_got: 0x978
   __DATA_CONST.__got: 0xa48
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x3a48
-  __DATA_CONST.__cfstring: 0xda60
-  __DATA_CONST.__objc_classlist: 0x5d0
-  __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x1b0
+  __DATA_CONST.__const: 0x39b8
+  __DATA_CONST.__cfstring: 0xdae0
+  __DATA_CONST.__objc_classlist: 0x5b8
+  __DATA_CONST.__objc_catlist: 0x30
+  __DATA_CONST.__objc_protolist: 0x1a8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x4f8
+  __DATA_CONST.__objc_superrefs: 0x4e0
   __DATA_CONST.__objc_intobj: 0xed0
   __DATA_CONST.__objc_arraydata: 0x228
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_dictobj: 0x140
-  __DATA.__objc_const: 0x2cc88
-  __DATA.__objc_selrefs: 0x8378
-  __DATA.__objc_ivar: 0x1278
-  __DATA.__objc_data: 0x3a20
-  __DATA.__data: 0x1560
-  __DATA.__bss: 0xb98
+  __DATA.__objc_const: 0x2c950
+  __DATA.__objc_selrefs: 0x82b8
+  __DATA.__objc_ivar: 0x1240
+  __DATA.__objc_data: 0x3930
+  __DATA.__data: 0x1500
+  __DATA.__bss: 0xbc8
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 6469
-  Symbols:   649
-  CStrings:  10238
+  Functions: 6429
+  Symbols:   648
+  CStrings:  10172
 
Symbols:
+ _OBJC_CLASS_$__DASBMHistogramBuilder
+ _OBJC_CLASS_$__DASBMMinimumSpanConfiguration
- _OBJC_CLASS_$_BPSSequence
- _OBJC_CLASS_$__DKApplicationMetadataKey
- _proc_pidinfo
CStrings:
+ "\x11\x12"
+ "\x1f\x01"
+ "@\"_DASTimelinePredictor\""
+ "@48@0:8Q16d24Q32@40"
+ "AppResumeBiomeUseCase"
+ "Error while querying Device.Power.PluggedIn stream: %s\n"
+ "Insufficient history window for deviceActivityLikelihood stream (%@ < %@)"
+ "Successfully completed querying Device.Power.PluggedIn stream\n"
+ "T@\"NSArray\",R,N,V_triggers"
+ "T@\"_DASTimelinePredictor\",&,N,V_predictor"
+ "T@\"_DASTimelinePredictor\",&,N,V_timelinePredictor"
+ "_timelinePredictor"
+ "companionMinimumQualityForActivity:interface:loiStatus:"
+ "companionScoreForActivity:networkQuality:interface:interfaceSubtype:pluginStatus:radioHot:linkAvailable:loiStatus:"
+ "d72@0:8@16q24q32q40B48B52^B56q64"
+ "deviceHasEnoughPluggedInTimeWithMinimumDays:withContext:"
+ "deviceNearby"
+ "deviceNearbyLikelihoodWithStartDate:"
+ "firstEventDateOnPublisher:"
+ "initWithValues:startDate:transitionDates:"
+ "isAfter:"
+ "launchLikelihoodForTop:withMinimumLikelihood:withTemporalResolution:onPublisher:"
+ "loiKey"
+ "minimumQualityForActivity:interface:interfaceSubtype:loiStatus:"
+ "pluginLikelihood returned a nil timeline"
+ "prediction"
+ "publisherWithUseCase:options:"
+ "q48@0:8@16q24q32q40"
+ "scoreForActivity:networkQuality:interface:interfaceSubtype:pluginStatus:radioHot:linkAvailable:loiStatus:"
+ "setTimelinePredictor:"
+ "timelinePredictor"
+ "updateCarryStatusWithContext:"
- "\x01\x18"
- "\x02\x11"
- "\x0e"
- "\x11\x13"
- "\x1f"
- "/defaultPaired/nearby"
- "@\"<_DKKnowledgeQuerying>\""
- "@\"BPSPublisher\""
- "@\"_DASBMMinimumSpanConfiguration\""
- "@\"_DASHistogram\"16@0:8"
- "@\"_DKPredictor\""
- "@40@0:8d16@?24@?32"
- "B16@?0@\"BPSTuple\"8"
- "B32@0:8@16d24"
- "B40@0:8d16@24@32"
- "BiomeHistogramBuilder"
- "Events sent to store successfully"
- "Excluding apps: %@"
- "Failed to open sink for %@: %@"
- "Failed to write profiles to store with error %@ "
- "Insufficient history window for stream: %@"
- "MinimumSpanConfiguration"
- "Not real carry device: %@ events, Last plugin: %@, First plugin: %@"
- "Processed %lu events from %lu profiles"
- "T@\"<_DKKnowledgeQuerying>\",&,N,V_knowledgeStore"
- "T@\"BPSPublisher\",&,N,V_publisher"
- "T@\"NSCountedSet\",R,C,N,V_counts"
- "T@\"NSDictionary\",R,C,N,V_countsDictionary"
- "T@\"_DASBMMinimumSpanConfiguration\",C,N,V_minimumSpanConfiguration"
- "T@\"_DKPredictionTimeline\",&,V_deviceNearbyTimeline"
- "T@\"_DKPredictionTimeline\",&,V_pluginTimeline"
- "T@\"_DKPredictor\",&,N,V_predictor"
- "T@?,C,N,V_aggregationKeyBlock"
- "T@?,C,N,V_filter"
- "T@?,C,N,V_spanMarkerBlock"
- "T@?,C,N,V_transform"
- "TB,N,V_saveSpans"
- "Td,N,V_minimumSpanDuration"
- "Tried to derive spans with an invalid configuration; bailing"
- "_DASBMHistogramBuilder"
- "_DASBMMinimumSpanConfiguration"
- "_DASHistogram"
- "_DASHistogramBuilder"
- "_aggregationKeyBlock"
- "_counts"
- "_countsDictionary"
- "_deviceNearbyTimeline"
- "_filter"
- "_knowledgeStore"
- "_minimumSpanConfiguration"
- "_minimumSpanDuration"
- "_pluginTimeline"
- "_publisher"
- "_saveSpans"
- "_spanMarkerBlock"
- "_transform"
- "aggregationKeyBlock"
- "appInFocusStream"
- "appUsageStream"
- "builderWithPublisher:"
- "com.apple.dasd.prediction.watchNearby"
- "companionMinimumQualityForActivity:interface:"
- "companionScoreForActivity:networkQuality:interface:interfaceSubtype:pluginStatus:radioHot:linkAvailable:"
- "configurationWithMinimumDuration:aggregationKey:spanMarker:"
- "d64@0:8@16q24q32q40B48B52^B56"
- "deviceHasEnoughPluggedInTimeWithMinimumDays:withContext:withKnowledgeStore:"
- "deviceNearbyLikelihood"
- "doesPublisher:satisfyHistoryWindow:"
- "eventWithStream:startDate:endDate:identifierStringValue:metadata:"
- "extensionHostIdentifier"
- "filter"
- "initWithPublisher:saveSpans:"
- "initWithSequence:"
- "initWithTimeIntervalSince1970:"
- "lowLikelihoodPeriodStartForPredictionWithKey:"
- "minimumQualityForActivity:interface:interfaceSubtype:"
- "minimumSpanConfiguration"
- "minimumSpanDuration"
- "predicateForEventsWithStartInDateRangeFrom:to:"
- "predicateForEventsWithStringValueInValues:"
- "predicateForObjectsWithMetadataKey:"
- "predictionForDeviceNearby"
- "predictionForDevicePluggedIn"
- "predictionForStreamWithName:withPredicate:withPredictionType:"
- "publisherWithSpansMeetingMinimumDuration:"
- "q24@?0@\"BMStoreEvent\"8@\"BMStoreEvent\"16"
- "q32@0:8@16q24"
- "saveSpans"
- "scoreForActivity:networkQuality:interface:interfaceSubtype:pluginStatus:radioHot:linkAvailable:"
- "setDeviceNearbyTimeline:"
- "setKnowledgeStore:"
- "setMinimumDaysOfHistory:"
- "setPluginTimeline:"
- "setPublisher:"
- "setSaveSpans:"
- "spanMarkerBlock"
- "topNPredictionQueryForStream:withPredicate:withTopN:withMinLikelihood:"
- "transform"
- "updateCarryStatusWithContext:withKnowledgeStore:"
- "v32@0:8@\"NSObject<OS_dispatch_queue>\"16@?<v@?@\"_DASHistogram\">24"

```
