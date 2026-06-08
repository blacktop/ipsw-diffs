## FinHealth

> `/System/Library/PrivateFrameworks/FinHealth.framework/FinHealth`

```diff

-1.8.5.1.0
-  __TEXT.__text: 0xcd2c
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_methlist: 0x7c8
-  __TEXT.__const: 0x1ea
-  __TEXT.__gcc_except_tab: 0x490
+1.9.1.22.0
+  __TEXT.__text: 0xc7f0
+  __TEXT.__objc_methlist: 0x7d8
+  __TEXT.__const: 0x25a
+  __TEXT.__gcc_except_tab: 0x4b4
   __TEXT.__oslogstring: 0x336
-  __TEXT.__cstring: 0xf17
-  __TEXT.__swift5_typeref: 0x95
+  __TEXT.__cstring: 0xf27
+  __TEXT.__swift5_typeref: 0x129
   __TEXT.__swift5_reflstr: 0x41
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__constg_swiftt: 0x54

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0x3a8
-  __TEXT.__eh_frame: 0x138
-  __TEXT.__objc_classname: 0xe6
-  __TEXT.__objc_methname: 0x1e82
-  __TEXT.__objc_methtype: 0x7de
-  __TEXT.__objc_stubs: 0x14a0
-  __DATA_CONST.__got: 0x240
-  __DATA_CONST.__const: 0x3a0
+  __TEXT.__swift_as_cont: 0x30
+  __TEXT.__unwind_info: 0x340
+  __TEXT.__eh_frame: 0x1b0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x3b0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x628
+  __DATA_CONST.__objc_selrefs: 0x650
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x368
+  __DATA_CONST.__got: 0x268
   __AUTH_CONST.__const: 0x2a8
   __AUTH_CONST.__cfstring: 0x500
   __AUTH_CONST.__objc_const: 0xb08
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x430
   __AUTH.__objc_data: 0x1b0
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x90
-  __DATA.__data: 0x100
+  __DATA.__data: 0x188
   __DATA.__bss: 0x180
   __DATA_DIRTY.__objc_data: 0xa0
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

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DC294661-820F-3B2C-8FA8-12B317A26BB2
-  Functions: 253
-  Symbols:   882
-  CStrings:  503
+  UUID: E59C2DAF-A969-3471-B4A7-8CDDB30C4BDF
+  Functions: 260
+  Symbols:   920
+  CStrings:  157
 
Symbols:
+ -[FHSearchSuggestionController fetchUserPropertiesWithRequest:completion:]
+ GCC_except_table26
+ GCC_except_table30
+ GCC_except_table62
+ GCC_except_table70
+ _OBJC_CLASS_$_FHEngagementPropertyResponse
+ _OBJC_CLASS_$_NSUUID
+ ___52-[FHSearchSuggestionController _newClientConnection]_block_invoke.111
+ ___60-[FHSearchSuggestionController _sendAllTransactionFeatures:]_block_invoke.97
+ ___61-[FHSearchSuggestionController reevaluateTransactionFeatures]_block_invoke.95
+ ___67-[FHPaymentRingSuggestionController generatePaymentRingSuggestion:]_block_invoke.83
+ ___74-[FHSearchSuggestionController fetchUserPropertiesWithRequest:completion:]_block_invoke
+ ___block_literal_global.99
+ ___swift_async_cont_functlets
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_FinHealth
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage_$_FinHealth
+ _block_copy_helper.21
+ _block_descriptor.23
+ _block_destroy_helper.22
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithValue:
+ _objc_msgSend$propertyName
+ _objc_msgSend$upcomingPaymentsWithAccountID:until:forceSync:currentDate:completion:
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _swift_getObjCClassMetadata
+ _swift_release_x20
+ _swift_release_x21
+ _swift_retain_x2
+ _swift_retain_x20
+ _symbolic Say_____G 13FinHealthCore27UpcomingTransactionsWrapperC
+ _symbolic ScCySay_____G______pG 13FinHealthCore27UpcomingTransactionsWrapperC s5ErrorP
+ _symbolic So15NSDecimalNumberCm
+ _symbolic So6NSDateCm
+ _symbolic So6NSUUIDCm
+ _symbolic So7NSArrayCm
+ _symbolic So8NSStringCm
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____m 13FinHealthCore21CurrencyAmountWrapperC
+ _symbolic _____m 13FinHealthCore26UpcomingTransactionWrapperC
+ _symbolic _____m 13FinHealthCore27UpcomingTransactionsWrapperC
+ _symbolic _____yypG s23_ContiguousArrayStorageC
- GCC_except_table24
- GCC_except_table28
- GCC_except_table60
- GCC_except_table68
- ___52-[FHSearchSuggestionController _newClientConnection]_block_invoke.116
- ___60-[FHSearchSuggestionController _sendAllTransactionFeatures:]_block_invoke.102
- ___61-[FHSearchSuggestionController reevaluateTransactionFeatures]_block_invoke.100
- ___67-[FHPaymentRingSuggestionController generatePaymentRingSuggestion:]_block_invoke.89
- ___block_literal_global.109
- _block_copy_helper.20
- _block_descriptor.22
- _block_destroy_helper.21
- _objc_msgSend$writePredictedTransactionInsights:
CStrings:
- ".cxx_destruct"
- "@\"<FHSuggestionDelegate>\""
- "@\"FHSearchSuggestionController\""
- "@\"FHStatementDetails\""
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSDecimalNumber\""
- "@\"NSDictionary\""
- "@\"NSMutableArray\""
- "@\"NSString\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "@40@0:8@16@24Q32"
- "@48@0:8@16@24@32Q40"
- "@56@0:8Q16@24@32@40@48"
- "@72@0:8@16@24@32@40@48@56@64"
- "@72@0:8@16@24@32@40@48@56B64B68"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B32@0:8@16@24"
- "FHDaemonProtocol"
- "FHPaymentRingData"
- "FHPaymentRingSuggestionController"
- "FHPaymentRingSuggestionRequest"
- "FHSearchSuggestionController"
- "FHStatementDetails"
- "FinHealthXPCServicesProtocol"
- "Q16@0:8"
- "T@\"<FHSuggestionDelegate>\",W,N,V_delegate"
- "T@\"FHStatementDetails\",&,N,V_currentStatement"
- "T@\"FHStatementDetails\",&,N,V_previousStatement"
- "T@\"NSArray\",&,N,V_paymentDetails"
- "T@\"NSDate\",&,N,V_closingDate"
- "T@\"NSDate\",&,N,V_openingDate"
- "T@\"NSDate\",C,N,V_transactionDate"
- "T@\"NSDecimalNumber\",&,N,V_combinedBalance"
- "T@\"NSDecimalNumber\",&,N,V_creditLimit"
- "T@\"NSDecimalNumber\",&,N,V_currentBalance"
- "T@\"NSDecimalNumber\",&,N,V_currentBalanceForMonthZero"
- "T@\"NSDecimalNumber\",&,N,V_currentStatementPaymentsSum"
- "T@\"NSDecimalNumber\",&,N,V_minimumDue"
- "T@\"NSDecimalNumber\",&,N,V_previousStatementPaymentsSum"
- "T@\"NSDecimalNumber\",&,N,V_remainingMinimumPayment"
- "T@\"NSDecimalNumber\",&,N,V_remainingStatementBalance"
- "T@\"NSDecimalNumber\",&,N,V_statementBalance"
- "T@\"NSDecimalNumber\",&,N,V_statementPurchasesSum"
- "T@\"NSDecimalNumber\",C,N,V_transactionAmount"
- "T@\"NSDictionary\",&,N,V_merchantCategoryTransactionSums"
- "T@\"NSMutableArray\",&,N,V_instrumentationCache"
- "T@\"NSString\",&,N,V_currentStatementIdentifier"
- "T@\"NSString\",&,N,V_statementIdentifier"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "TB,N,V_cacheConnectionInitiated"
- "TB,N,V_isMonthOfMerge"
- "TB,N,V_isMonthOne"
- "TB,N,V_isMonthZero"
- "TQ,N,V_paymentAmountCategory"
- "T{os_unfair_lock_s=I},N,V_lockCache"
- "T{os_unfair_lock_s=I},N,V_lockConnection"
- "_TtC9FinHealth20FHInsightsController"
- "_allMandatoryValuesAreSameAmount:"
- "_cacheConnectionInitiated"
- "_calculateThresholdForLastPaymentCategory:statementBalance:lastPaymentCategoryAmount:previousStatementPaymentsSum:statementPurchasesSum:"
- "_categoryIsCurrentBalanceType:"
- "_categoryIsPaymentPlan:"
- "_clientConnection"
- "_closingDate"
- "_combinedBalance"
- "_connection"
- "_creditLimit"
- "_currentBalance"
- "_currentBalanceForMonthZero"
- "_currentStatement"
- "_currentStatementIdentifier"
- "_currentStatementIsLastMonthsStatement"
- "_currentStatementPaymentsSum"
- "_delegate"
- "_fhEqualObjects:obj2:"
- "_filterSuggestions:belowThreshold:"
- "_init"
- "_instrumentationCache"
- "_isMonthOfMerge"
- "_isMonthOne"
- "_isMonthZero"
- "_isOnPaymentPlan"
- "_isOnPlanCompletion"
- "_lockCache"
- "_lockConnection"
- "_merchantCategoryTransactionSums"
- "_minimumDue"
- "_minimumMerchcantCategoriesAboveMinimumAmount:minMerchantCategory1:minMerchantCategory2:minMerchantCategorySum1:minMerchantCategorySum2:merchantCategoryTransactionSums:"
- "_newClientConnection"
- "_openingDate"
- "_paymentAmountCategory"
- "_paymentDetails"
- "_previousSelectedSuggestion"
- "_previousStatement"
- "_previousStatementPaymentsSum"
- "_remainingMinimumPayment"
- "_remainingStatementBalance"
- "_remoteObjectInterface"
- "_remoteObjectProxyWithErrorHandler"
- "_searchController"
- "_sendAllTransactionFeatures:"
- "_statementBalance"
- "_statementIdentifier"
- "_statementPurchasesSum"
- "_suggestedAmountsForPayOffDateForStatementBalance:statementPurchasesSum:creditUtilization:lastPaymentCategory:"
- "_transactionAmount"
- "_transactionDate"
- "_updateOrRecordCacheEntries:instrumentationCacheSize:"
- "_validateInstrumentationRecord:"
- "_zerothOrFirstMonthPaymentRingSuggestionsForList:"
- "accountSummary"
- "addObject:"
- "addObjectsFromArray:"
- "adjustedBalance"
- "aggregateFeaturesWithHandler:"
- "aggregateFeaturesWithProcessSource:completion:"
- "allFeatureInsightsWithStartDate:endDate:insightTypeItems:trendWindow:completion:"
- "allInsightsForDateRange:endDate:insightTypeItems:trendWindow:sourceId:accountType:completion:"
- "allKeys"
- "allPeerPaymentForecastingSignals:"
- "amount"
- "appendFormat:"
- "balanceSummary"
- "cacheConnectionInitiated"
- "category"
- "closingDate"
- "combinedBalance"
- "compare:"
- "connection"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "creditDetails"
- "creditLimit"
- "currentBalance"
- "currentBalanceForMonthZero"
- "currentStatement"
- "currentStatementIdentifier"
- "currentStatementPaymentsSum"
- "dealloc"
- "decimalNumberByAdding:"
- "decimalNumberByDividingBy:"
- "decimalNumberBySubtracting:"
- "decimalNumberWithString:"
- "delegate"
- "deleteAllData:"
- "deleteDataForPasses:completion:"
- "deleteDataForPassesWithSourceIdentifiers:completion:"
- "deleteTransactionById:completion:"
- "deleteTransactionByTransactionIdentifier:completion:"
- "description"
- "details"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithValuesForKeys:"
- "didReceiveInsightChangeUpdate:completion:"
- "didUpdateFeatures:moreComing:readyForNextBatch:error:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "featureLabel"
- "featureRank"
- "featureResponsesForApplication:completion:"
- "featureResponsesForApplication:withCompletion:"
- "featuresForApplication:withCompletion:"
- "featuresWithCompletion:"
- "fetchUserProperties:withParameters:completion:"
- "filteredArrayUsingPredicate:"
- "generatePaymentRingSuggestion:"
- "generatePaymentRingSuggestionsFromConvertedObjects:previousStatementPaymentsSum:currentStatementPaymentsSum:statementPurchasesSum:merchantCategoryTransactionSums:billPaymentSelectedSuggestedAmountData:isMonthZero:isMonthOne:"
- "generatePredictionWithModelType:withModelPathComponent:completion:"
- "getAllPaymentTransactions"
- "getComputedFeaturesForTransactions:completion:"
- "getDisputeDocumentSuggestionsForTransactionId:completion:"
- "getTopTransactionCategoriesWithCountryCode:timeWindow:minRegularTransactionRatio:discretizedTimeOfDay:completion:"
- "getTopTransactionCategoriesWithTimeWindow:completion:"
- "hash"
- "identifier"
- "init"
- "initWithAmount:category:"
- "initWithDelegate:"
- "initWithMachServiceName:options:"
- "initWithServiceName:"
- "initWithTransactionDate:transactionAmount:paymentAmountCategory:"
- "initWithcurrentStatement:previousStatement:previousStatementPaymentsSum:currentStatementPaymentsSum:statementPurchasesSum:merchantCategoryTransactionSums:paymentDetails:"
- "instrumentationCache"
- "intValue"
- "integerValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isEqualToNumber:"
- "isEqualToString:"
- "isInMonthOfMerge"
- "isMonthOfMerge"
- "isMonthOne"
- "isMonthZero"
- "localizedDescription"
- "lockCache"
- "lockConnection"
- "merchantCategory"
- "merchantCategoryTransactionSums"
- "minimumDue"
- "now"
- "numberWithInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "openingDate"
- "paymentAmountCategory"
- "paymentDetails"
- "paymentRingSuggestionsFromSearchFeatures:startDate:endDate:completion:"
- "peerPaymentForecastingSignals:withCompletion:"
- "predicateWithFormat:"
- "predictionsByModelName:modelVersion:completion:"
- "previousStatement"
- "previousStatementPaymentsSum"
- "processInfo"
- "processName"
- "recomputeFeaturesForTransactions:"
- "recordPaymentRingAction:"
- "recordUserInteraction:"
- "recordUserInteraction:completion:"
- "recordUserInteractions:completion:"
- "reevaluateTransactionFeatures"
- "remainingMinimumPayment"
- "remainingStatementBalance"
- "remainingStatementBalanceForInterestCalculation"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllObjects"
- "resume"
- "sendAllTransactionFeatures"
- "server"
- "setAmount:"
- "setCacheConnectionInitiated:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setClosingDate:"
- "setCombinedBalance:"
- "setConnection:"
- "setCreditLimit:"
- "setCurrentBalance:"
- "setCurrentBalanceForMonthZero:"
- "setCurrentStatement:"
- "setCurrentStatementIdentifier:"
- "setCurrentStatementPaymentsSum:"
- "setDelegate:"
- "setInstrumentationCache:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsMonthOfMerge:"
- "setIsMonthOne:"
- "setIsMonthZero:"
- "setLockCache:"
- "setLockConnection:"
- "setMerchantCategory:"
- "setMerchantCategoryTransactionSums:"
- "setMinimumDue:"
- "setObject:forKey:"
- "setOpeningDate:"
- "setPaymentAmountCategory:"
- "setPaymentDetails:"
- "setPreviousStatement:"
- "setPreviousStatementPaymentsSum:"
- "setRemainingMinimumPayment:"
- "setRemainingStatementBalance:"
- "setRemoteObjectInterface:"
- "setStatementBalance:"
- "setStatementIdentifier:"
- "setStatementPurchasesSum:"
- "setTransactionAmount:"
- "setTransactionDate:"
- "setWithObjects:"
- "statementBalance"
- "statementIdentifier"
- "statementPurchasesSum"
- "stringWithFormat:"
- "suggestedAmountCategory"
- "transactionAmount"
- "transactionDate"
- "transactionUpdated:deferFeatureComputation:completion:"
- "transactionWithTransaction:completion:"
- "transactionWithTransactionID:completion:"
- "transactionsByGroupID:completion:"
- "transactionsRequireSyncing"
- "transactionsRequireSyncing:"
- "updatePeerPaymentAccountBalanceWithTransactionSourceId:amount:currencyCode:completion:"
- "updatePeerPaymentForecastingSuggestionStatus:counterpartHandle:amount:completion:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8{os_unfair_lock_s=I}16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8Q16"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"NSArray\"@\"NSError\">20"
- "v32@0:8@\"FHTransaction\"16@?<v@?@\"PKPaymentTransaction\">24"
- "v32@0:8@\"NSArray\"16@?<v@?>24"
- "v32@0:8@\"NSDate\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?>24"
- "v32@0:8@\"NSSet\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"PKPaymentTransaction\">24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?>24"
- "v36@0:8@\"FHTransaction\"16B24@?<v@?@\"FHFeaturesResponse\"@\"NSError\">28"
- "v36@0:8@16B24@?28"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSArray\">32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"NSString\"16@\"NSDate\"24@\"NSDate\"32@?<v@?@\"NSArray\">40"
- "v48@0:8@\"NSString\"16@\"NSDecimalNumber\"24@\"NSString\"32@?<v@?B@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8Q16@\"NSString\"24@\"NSDecimalNumber\"32@?<v@?B@\"NSError\">40"
- "v48@0:8Q16@24@32@?40"
- "v56@0:8@\"NSString\"16Q24d32Q40@?<v@?@\"FHTransactionStatistics\"@\"NSError\">48"
- "v56@0:8@16@24@32q40@?48"
- "v56@0:8@16Q24d32Q40@?48"
- "v64@0:8@16^q24^q32^@40^@48@56"
- "v72@0:8@\"NSDate\"16@\"NSDate\"24@\"NSArray\"32q40@\"NSString\"48q56@?<v@?@\"NSArray\">64"
- "v72@0:8@16@24@32q40@48q56@?64"
- "writeEntityGroups:"
- "writeIncomeInsights:"
- "writePredictedTransactionInsights:"
- "zero"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{os_unfair_lock_s=I}16@0:8"

```
