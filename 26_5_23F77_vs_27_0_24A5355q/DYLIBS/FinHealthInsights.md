## FinHealthInsights

> `/System/Library/PrivateFrameworks/FinHealthInsights.framework/FinHealthInsights`

```diff

-1.8.5.1.0
-  __TEXT.__text: 0x20214
-  __TEXT.__auth_stubs: 0xbe0
+1.9.1.22.0
+  __TEXT.__text: 0x20b64
   __TEXT.__objc_methlist: 0x664
-  __TEXT.__const: 0x1970
-  __TEXT.__gcc_except_tab: 0x230
-  __TEXT.__cstring: 0x865
+  __TEXT.__const: 0x1958
+  __TEXT.__gcc_except_tab: 0x178
+  __TEXT.__cstring: 0x875
   __TEXT.__oslogstring: 0x749
-  __TEXT.__swift5_typeref: 0x4c2
+  __TEXT.__swift5_typeref: 0x4ba
   __TEXT.__swift5_reflstr: 0x3b5
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__constg_swiftt: 0x3d0
   __TEXT.__swift5_fieldmd: 0x5a8
   __TEXT.__swift5_proto: 0x170
   __TEXT.__swift5_types: 0x5c
-  __TEXT.__unwind_info: 0x7c8
+  __TEXT.__unwind_info: 0x7d0
   __TEXT.__eh_frame: 0x6d8
-  __TEXT.__objc_classname: 0x106
-  __TEXT.__objc_methname: 0x137a
-  __TEXT.__objc_methtype: 0x26d
-  __TEXT.__objc_stubs: 0xf40
-  __DATA_CONST.__got: 0x260
-  __DATA_CONST.__const: 0x328
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x338
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x538
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x600
+  __DATA_CONST.__got: 0x260
   __AUTH_CONST.__const: 0xf48
   __AUTH_CONST.__cfstring: 0x720
   __AUTH_CONST.__objc_const: 0xba8
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x680
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0xd8
   __DATA.__objc_ivar: 0x58
-  __DATA.__data: 0x4d8
-  __DATA.__bss: 0x3058
+  __DATA.__data: 0x4d0
+  __DATA.__bss: 0x3088
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4E78B374-1D10-3FD3-BA37-CC696F6963B1
-  Functions: 780
-  Symbols:   863
-  CStrings:  441
+  UUID: E1AA6EED-F7C7-32FD-8916-971F47FDBA08
+  Functions: 785
+  Symbols:   882
+  CStrings:  181
 
Symbols:
+ ___61-[FHInsightsSpendingTrends _computeCategoryAndMerchantTrends]_block_invoke.116
+ ___61-[FHInsightsSpendingTrends _computeCategoryAndMerchantTrends]_block_invoke.124
+ ___88-[FHInsightsFetcher retrieveInsightsWithStartDate:endDate:insightTypeItems:trendWindow:]_block_invoke.113
+ ___block_literal_global.103
+ ___block_literal_global.129
+ ___block_literal_global.176
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_FinHealthInsights
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage_$_FinHealthInsights
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x25
+ _objc_retain_x4
+ _objc_retain_x8
+ _swift_release_x1
+ _swift_release_x11
+ _swift_release_x12
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x24
+ _swift_release_x26
+ _swift_release_x28
+ _swift_release_x3
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain_x20
+ _swift_retain_x22
+ _swift_retain_x25
- ___61-[FHInsightsSpendingTrends _computeCategoryAndMerchantTrends]_block_invoke.122
- ___61-[FHInsightsSpendingTrends _computeCategoryAndMerchantTrends]_block_invoke.130
- ___88-[FHInsightsFetcher retrieveInsightsWithStartDate:endDate:insightTypeItems:trendWindow:]_block_invoke.119
- ___block_literal_global.109
- ___block_literal_global.135
- ___block_literal_global.182
- _objc_retain
- _objc_retain_x26
- _objc_retain_x28
- _swift_retain
- _swift_stdlib_isStackAllocationSafe
- _symbolic ______p s5ErrorP
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"FHDatabaseEntity\""
- "@\"NSDate\""
- "@\"NSDate\"16@0:8"
- "@\"NSDecimalNumber\""
- "@\"NSDecimalNumberHandler\""
- "@\"NSDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@40@0:8d16d24@32"
- "@48@0:8@16@24@32q40"
- "@64@0:8@16@24@32q40@48q56"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "FHCategorySpendInsight"
- "FHFeatureInsight"
- "FHInsightProtocol"
- "FHInsightsFetcher"
- "FHInsightsSpendingTrends"
- "FHMerchantSpendInsight"
- "FHOverallSpendInsight"
- "FHSearchTagSpendInsight"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"FHDatabaseEntity\",C,N,V_insightsDestinationEntity"
- "T@\"FHDatabaseEntity\",C,N,V_transactionAndFeauturesEntities"
- "T@\"NSDate\",C,N"
- "T@\"NSDate\",C,N,VendDate"
- "T@\"NSDate\",C,N,VstartDate"
- "T@\"NSDecimalNumber\",C,N,VaverageAmount"
- "T@\"NSDecimalNumber\",C,N,VspendAmount"
- "T@\"NSDecimalNumber\",C,N,VspendingInsightAmount"
- "T@\"NSDecimalNumber\",C,N,VspendingInsightPercentageValue"
- "T@\"NSDecimalNumberHandler\",&,N,V_roundingBehavior"
- "T@\"NSDictionary\",C,N,V_merchantCounts"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_insightsProcessingQueue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N"
- "T@\"NSString\",C,N,VcurrencyCode"
- "T@\"NSString\",C,N,VmerchantName"
- "T@\"NSString\",C,N,VsearchTagName"
- "T@\"NSString\",C,N,Vtype"
- "T@\"NSString\",R,C"
- "TB,R"
- "TQ,N"
- "TQ,N,VwindowReference"
- "TQ,R"
- "Td,R,N,V_monthlyThreshold"
- "Td,R,N,V_weeklyThreshold"
- "Tq,N"
- "Tq,N,VdetectionType"
- "Tq,N,Vdirection"
- "Tq,N,VmerchantCategory"
- "Tq,N,Vwindow"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC17FinHealthInsights12OrderMatcher"
- "_computeAndStoreTrend:indexedAmountSums:insightFeatureName:insightType:trendWindow:"
- "_computeCategoryAndMerchantTrends"
- "_defaultQueue"
- "_fillFactorWithStartOfPeriodForMostRecentEntryDate:mostRecentEntryDate:endOfPeriodForMostRecentEntryDate:numberOfDaysSinceFirstTransaction:transactionCount:transactionCountForMostRecentPeriod:transactionAmountSums:transactionAmountSumsForMostRecentPeriod:"
- "_init"
- "_insightsDestinationEntity"
- "_insightsProcessingQueue"
- "_kendallCoefficientWithIndexedAmountSums:"
- "_merchantCounts"
- "_monthlyThreshold"
- "_orderedTimeStampAndAmountPair:"
- "_roundingBehavior"
- "_transactionAndFeauturesEntities"
- "_weeklyThreshold"
- "addDateClause:fieldName:expression:"
- "addDecimalNumberValueForField:fieldValue:"
- "addDoubleValueForField:fieldValue:"
- "addIntegerClause:fieldName:expression:"
- "addIntegerValueForField:fieldValue:"
- "addKeyPairsWithJoinType:leftEntity:rightEntity:joinKey:"
- "addNumberValueForField:fieldValue:"
- "addObject:"
- "addStringClause:fieldName:expression:"
- "addStringValueForField:fieldValue:"
- "allKeys"
- "appendFormat:"
- "appendString:"
- "arrayWithObjects:"
- "autorelease"
- "class"
- "clearData"
- "compare:"
- "componentsSeparatedByString:"
- "conformsToProtocol:"
- "containsObject:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d"
- "d16@0:8"
- "d80@0:8@16@24@32Q40Q48Q56d64d72"
- "dateFromString:"
- "dateWithTimeIntervalSinceReferenceDate:"
- "debugDescription"
- "decimalNumberByDividingBy:"
- "decimalNumberByMultiplyingBy:"
- "decimalNumberByRoundingAccordingToBehavior:"
- "decimalNumberBySubtracting:"
- "decimalNumberHandlerWithRoundingMode:scale:raiseOnExactness:raiseOnOverflow:raiseOnUnderflow:raiseOnDivideByZero:"
- "decimalNumberWithDecimal:"
- "decimalNumberWithString:"
- "decimalValue"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "defaultDatabaseAmountMultiplier"
- "description"
- "distantFuture"
- "distantPast"
- "doubleValue"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enumerateKeysAndObjectsUsingBlock:"
- "expressionValueWithObject:context:"
- "expressionWithFormat:argumentArray:"
- "featureLabel"
- "fieldsInOrder"
- "filteredArrayUsingPredicate:"
- "firstObject"
- "greaterThan:"
- "greaterThanOrEqual:"
- "hash"
- "indexOfObject:"
- "init"
- "initWithBuilder:"
- "initWithCoder:"
- "initWithDouble:"
- "initWithEntity:"
- "initWithEntity:joinClause:"
- "initWithMerchantCounts:"
- "initWithWeeklyThreshold:monthlyThreshold:merchantCounts:"
- "insertOrUpdate:upsert:"
- "insightsDestinationEntity"
- "insightsProcessingQueue"
- "intValue"
- "integerValue"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "kendallCoefficientWithIndexedAmountSums:"
- "lastObject"
- "lessThan:"
- "lessThanOrEqual:"
- "merchantCounts"
- "monthlyThreshold"
- "name"
- "now"
- "numberWithDouble:"
- "objectAtIndex:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "overrideMonthlyFillFactor"
- "overrideWeeklyFillFactor"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "predicateWithFormat:"
- "q"
- "q16@0:8"
- "queryDataWithBlock:logicalOperator:selectFields:usingBlock:"
- "reconstructAggregateFeaturesWithProcessingWindow:"
- "reconstructCompoundFeatures:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "retrieveInsightsWithStartDate:endDate:insightTypeItems:trendWindow:"
- "retrieveSpendInsightsWithStartDate:endDate:insightTypeItems:trendWindow:sourceId:accountType:"
- "roundingBehavior"
- "searchTagName"
- "self"
- "setAverageAmount:"
- "setCurrencyCode:"
- "setDateFormat:"
- "setDetectionType:"
- "setDirection:"
- "setEndDate:"
- "setInsightsDestinationEntity:"
- "setMerchantCategory:"
- "setMerchantCounts:"
- "setMerchantName:"
- "setObject:forKey:"
- "setOrAddToDecimalValue:forKey:"
- "setOrAddToDoubleValue:forKey:"
- "setRoundingBehavior:"
- "setSearchTagName:"
- "setSpendAmount:"
- "setSpendingInsightAmount:"
- "setSpendingInsightPercentageValue:"
- "setStartDate:"
- "setThresholdsWithWeeklyThreshold:monthlyThreshold:"
- "setTransactionAndFeauturesEntities:"
- "setType:"
- "setValue:forKey:"
- "setWindow:"
- "setWindowReference:"
- "sharedInstance"
- "signedIntegerAtIndex:"
- "sortUsingComparator:"
- "sortedArrayUsingComparator:"
- "stringValue"
- "stringWithFormat:"
- "subarrayWithRange:"
- "superclass"
- "supportsSecureCoding"
- "timeIntervalSinceReferenceDate"
- "totalSpendAmountBetweenDates:endDate:sourceId:accountType:"
- "transactionAndFeauturesEntities"
- "trendsWithCompletion:"
- "v16@0:8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSDate\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v32@0:8d16d24"
- "v56@0:8@16@24@32@40q48"
- "weeklyThreshold"
- "zero"
- "zone"

```
