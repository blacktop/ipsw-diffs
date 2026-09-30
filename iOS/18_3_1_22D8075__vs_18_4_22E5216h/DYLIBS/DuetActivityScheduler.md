## DuetActivityScheduler

> `/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler`

```diff

-1786.80.10.0.0
-  __TEXT.__text: 0x2e50c
-  __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_methlist: 0x2e4c
-  __TEXT.__const: 0x148
-  __TEXT.__gcc_except_tab: 0x12d0
-  __TEXT.__cstring: 0x21fe
-  __TEXT.__oslogstring: 0x2adb
-  __TEXT.__unwind_info: 0xde0
-  __TEXT.__objc_classname: 0x686
-  __TEXT.__objc_methname: 0x8df3
-  __TEXT.__objc_methtype: 0x15f9
-  __TEXT.__objc_stubs: 0x50a0
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0xcf8
-  __DATA_CONST.__objc_classlist: 0x108
+1856.100.90.0.0
+  __TEXT.__text: 0x30ad8
+  __TEXT.__auth_stubs: 0x690
+  __TEXT.__objc_methlist: 0x3c40
+  __TEXT.__const: 0x150
+  __TEXT.__gcc_except_tab: 0x131c
+  __TEXT.__cstring: 0x239e
+  __TEXT.__oslogstring: 0x2c11
+  __TEXT.__unwind_info: 0xe98
+  __TEXT.__objc_classname: 0x6e1
+  __TEXT.__objc_methname: 0x9460
+  __TEXT.__objc_methtype: 0x16a3
+  __TEXT.__objc_stubs: 0x54e0
+  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__const: 0xe90
+  __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x108
+  __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2018
+  __DATA_CONST.__objc_selrefs: 0x2230
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xd0
+  __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x110
-  __AUTH_CONST.__auth_got: 0x348
-  __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0x3340
-  __AUTH_CONST.__objc_const: 0x7b40
+  __AUTH_CONST.__auth_got: 0x358
+  __AUTH_CONST.__const: 0x260
+  __AUTH_CONST.__cfstring: 0x3380
+  __AUTH_CONST.__objc_const: 0x6b40
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x394
-  __DATA.__data: 0xd80
-  __DATA.__bss: 0x58
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x3c8
+  __DATA.__data: 0xde0
+  __DATA.__bss: 0x50
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x870
-  __DATA_DIRTY.__bss: 0x100
+  __DATA_DIRTY.__objc_data: 0x8c0
+  __DATA_DIRTY.__bss: 0x108
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
   - /System/Library/PrivateFrameworks/AppConduit.framework/AppConduit
+  - /System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
+  - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
+  - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet
   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1281
-  Symbols:   1669
-  CStrings:  2479
+  Functions: 1365
+  Symbols:   1765
+  CStrings:  2583
 
Symbols:
+ _BiomeLibrary
+ _OBJC_CLASS_$_BMPublisherOptions
+ _OBJC_CLASS_$_BPSSequence
+ _OBJC_CLASS_$_BPSTuple
+ _OBJC_CLASS_$__DASBMHistogramBuilder
+ _OBJC_CLASS_$__DASBMMinimumSpanConfiguration
+ _OBJC_CLASS_$__DASHistogram
+ _OBJC_METACLASS_$__DASBMHistogramBuilder
+ _OBJC_METACLASS_$__DASBMMinimumSpanConfiguration
+ _OBJC_METACLASS_$__DASHistogram
+ _objc_opt_respondsToSelector
- _OBJC_CLASS_$_NSDateInterval
- _OBJC_CLASS_$__DKAnyStringIdentifier
- _OBJC_CLASS_$__DKHistogramQuery
CStrings:
+ "\x02\x11"
+ "\x11e\x12C\x12\x1a\x11\x15\x12\x11$\"\x11\x12"
+ ", Maximum Runtime: %ld"
+ ", Run When App Launch Unlikely: %d"
+ "@\"BPSPublisher\""
+ "@\"BPSTuple\"16@?0@\"BMStoreEvent\"8"
+ "@\"NSString\"16@?0@\"BMStoreEvent\"8"
+ "@\"_DASBMMinimumSpanConfiguration\""
+ "@\"_DASHistogram\"16@0:8"
+ "@40@0:8d16@?24@?32"
+ "@56@0:8@16@24@32@?40@?48"
+ "App"
+ "B16@?0@\"BMStoreEvent\"8"
+ "B16@?0@\"BPSTuple\"8"
+ "BiomeHistogramBuilder"
+ "Coalescing view for %@ at %@"
+ "Coalescing view for %@ at %@ (Cache)"
+ "DuetActivitySchedulerPairedSystemContext"
+ "Failed to get remote devices: %@"
+ "Failed to open sink for %@: %@"
+ "InFocus"
+ "MinimumSpanConfiguration"
+ "Paired device identifier update: %@ -> %@"
+ "Remote results for app usage history: %@"
+ "Selected device (%@) for app usage history."
+ "T@\"BPSPublisher\",&,N,V_publisher"
+ "T@\"NSCountedSet\",R,C,N,V_counts"
+ "T@\"NSDictionary\",R,C,N,V_countsDictionary"
+ "T@\"NSMutableDictionary\",&,N,V_lastWidgetViewCache"
+ "T@\"NSString\",C,N,V_pairedDeviceIdentifier"
+ "T@\"_DASBMMinimumSpanConfiguration\",C,N,V_minimumSpanConfiguration"
+ "T@?,C,N,V_aggregationKeyBlock"
+ "T@?,C,N,V_filter"
+ "T@?,C,N,V_spanMarkerBlock"
+ "T@?,C,N,V_transform"
+ "TB,N,V_runWhenAppLaunchUnlikely"
+ "TB,N,V_saveSpans"
+ "Td,N,V_minimumSpanDuration"
+ "Tried to derive spans with an invalid configuration; bailing"
+ "_DASBMHistogramBuilder"
+ "_DASBMMinimumSpanConfiguration"
+ "_DASHistogram"
+ "_DASHistogramBuilder"
+ "_aggregationKeyBlock"
+ "_counts"
+ "_countsDictionary"
+ "_filter"
+ "_lastWidgetViewCache"
+ "_minimumSpanConfiguration"
+ "_minimumSpanDuration"
+ "_pairedDeviceIdentifier"
+ "_publisher"
+ "_runWhenAppLaunchUnlikely"
+ "_saveSpans"
+ "_spanMarkerBlock"
+ "_transform"
+ "activityCanceledWithReason:expirationReason:"
+ "aggregationKeyBlock"
+ "builderWithPublisher:"
+ "builderWithPublisher:saveSpans:"
+ "clientFailedtoExpireTaskWithIdentifier:"
+ "collect"
+ "com.apple.DuetActivityScheduler"
+ "components:fromDate:"
+ "configurationWithMinimumDuration:aggregationKey:spanMarker:"
+ "counts"
+ "countsDictionary"
+ "dateFromAbsoluteTime:"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "deriveSpanTuplesWithMinimumDurationOnStream:"
+ "deriveSpansWithMinimumDurationOnStream:"
+ "error"
+ "eventBody"
+ "filter"
+ "filterWithIsIncluded:"
+ "first"
+ "handleClientFailedtoExpireTaskWithIdentifier [taskIdentifier: %@] Failed: %@"
+ "handleClientFailedtoExpireTaskWithIdentifier:completionHandler:"
+ "histogram"
+ "histogramOnResponseQueue:withCompletion:"
+ "idsDeviceIdentifier"
+ "initWithClientIdentifier:context:callbackQueue:systemConditionChangeCallback:trafficCancelationHander:"
+ "initWithEvents:"
+ "initWithFirst:second:"
+ "initWithPublisher:saveSpans:"
+ "initWithSequence:"
+ "isAfter:"
+ "isBefore:"
+ "isSameDayOfWeekAs:withCalendar:"
+ "lastWidgetViewCache"
+ "mapWithTransform:"
+ "minimumSpanConfiguration"
+ "minimumSpanDuration"
+ "pairedDeviceIdentifier"
+ "publisher"
+ "publisherForDevice:withUseCase:options:"
+ "publisherWithSpansMeetingMinimumDuration:"
+ "q24@?0@\"BMStoreEvent\"8@\"BMStoreEvent\"16"
+ "q24@?0@\"BPSTuple\"8@\"BPSTuple\"16"
+ "remoteDevicesWithError:"
+ "runWhenAppLaunchUnkely"
+ "runWhenAppLaunchUnlikely"
+ "sanitizeWidgetViews:"
+ "saveSpans"
+ "second"
+ "setAggregationKeyBlock:"
+ "setEndDate:"
+ "setFilter:"
+ "setLastWidgetViewCache:"
+ "setMinimumSpanConfiguration:"
+ "setMinimumSpanDuration:"
+ "setPairedDeviceIdentifier:"
+ "setPublisher:"
+ "setRunWhenAppLaunchUnlikely:"
+ "setSaveSpans:"
+ "setSpanMarkerBlock:"
+ "setTransform:"
+ "sinkWithCompletion:receiveInput:"
+ "sortUsingComparator:"
+ "spanMarkerBlock"
+ "starting"
+ "state"
+ "timestamp"
+ "transform"
+ "v16@?0@\"BPSCompletion\"8"
+ "v32@0:8@\"NSObject<OS_dispatch_queue>\"16@?<v@?@\"_DASHistogram\">24"
+ "v32@0:8@\"_DASActivity\"16q24"
+ "v32@0:8@16q24"
+ "v32@?0@\"NSString\"8@\"NSMutableArray\"16^B24"
+ "weekday"
- "\x11e\x12B\x11\x12\x1a\x11\x15\x12\x11$\"\x11\x12"
- "@\"<_DKKnowledgeQuerying>\""
- "@64@0:8@16@24@32@40@?48@?56"
- "Error obtaining results for app usage history: %@"
- "Obtained results for histogram: %@"
- "PairedDeviceForecast"
- "T@\"<_DKKnowledgeQuerying>\",&,N,V_knowledgeStore"
- "Tq,N,V_relevancy"
- "_knowledgeStore"
- "_relevancy"
- "countDictionary"
- "distantFuture"
- "eventStreamWithName:valueType:"
- "executeQuery:error:"
- "histogramQueryForStream:interval:withPredicate:"
- "initWithClientIdentifier:context:knowledgeStore:callbackQueue:systemConditionChangeCallback:trafficCancelationHander:"
- "initWithStartDate:endDate:"
- "knowledgeStore"
- "pairedDeviceStream"
- "predicateWithValue:"
- "relevancy"
- "setIncludeLocalResults:"
- "setIncludeRemoteResults:"
- "setKnowledgeStore:"
- "setRelevancy:"
- "type"

```
