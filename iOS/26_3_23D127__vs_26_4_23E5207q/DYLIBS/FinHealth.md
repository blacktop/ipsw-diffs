## FinHealth

> `/System/Library/PrivateFrameworks/FinHealth.framework/FinHealth`

```diff

-1.8.2.4.0
-  __TEXT.__text: 0xc418
-  __TEXT.__auth_stubs: 0x730
+1.8.5.1.0
+  __TEXT.__text: 0xcd2c
+  __TEXT.__auth_stubs: 0x6b0
   __TEXT.__objc_methlist: 0x7c8
   __TEXT.__const: 0x1ea
-  __TEXT.__gcc_except_tab: 0x4ec
+  __TEXT.__gcc_except_tab: 0x490
   __TEXT.__oslogstring: 0x336
-  __TEXT.__cstring: 0xf78
+  __TEXT.__cstring: 0xf17
   __TEXT.__swift5_typeref: 0x95
   __TEXT.__swift5_reflstr: 0x41
   __TEXT.__swift5_assocty: 0x18

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0x318
+  __TEXT.__unwind_info: 0x3a8
   __TEXT.__eh_frame: 0x138
-  __TEXT.__objc_classname: 0xbd
-  __TEXT.__objc_methname: 0x1e7b
-  __TEXT.__objc_methtype: 0x7bb
-  __TEXT.__objc_stubs: 0x13e0
+  __TEXT.__objc_classname: 0xe6
+  __TEXT.__objc_methname: 0x1e82
+  __TEXT.__objc_methtype: 0x7de
+  __TEXT.__objc_stubs: 0x14a0
   __DATA_CONST.__got: 0x240
-  __DATA_CONST.__const: 0x3c0
+  __DATA_CONST.__const: 0x3a0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x628
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x3a8
+  __AUTH_CONST.__auth_got: 0x368
   __AUTH_CONST.__const: 0x2a8
   __AUTH_CONST.__cfstring: 0x500
   __AUTH_CONST.__objc_const: 0xb08

   - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3FAEA26A-433C-3B87-83C3-25149755060C
+  UUID: B2EA5F21-D5F3-3B3D-B794-638591C06730
   Functions: 253
-  Symbols:   890
-  CStrings:  504
+  Symbols:   882
+  CStrings:  503
 
Symbols:
+ _block_copy_helper.1
+ _block_copy_helper.10
+ _block_copy_helper.13
+ _block_copy_helper.17
+ _block_copy_helper.20
+ _block_copy_helper.4
+ _block_copy_helper.7
+ _block_descriptor.12
+ _block_descriptor.15
+ _block_descriptor.19
+ _block_descriptor.22
+ _block_descriptor.3
+ _block_descriptor.6
+ _block_descriptor.9
+ _block_destroy_helper.11
+ _block_destroy_helper.14
+ _block_destroy_helper.18
+ _block_destroy_helper.2
+ _block_destroy_helper.21
+ _block_destroy_helper.5
+ _block_destroy_helper.8
+ _objc_msgSend$didReceiveInsightChangeUpdate:completion:
+ _objc_msgSend$init
+ _objc_msgSend$initWithMachServiceName:options:
+ _objc_msgSend$writeEntityGroups:
+ _objc_msgSend$writeIncomeInsights:
+ _objc_msgSend$writePredictedTransactionInsights:
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftAVFoundation_$_FinHealth
- __swift_FORCE_LOAD_$_swiftCoreAudio
- __swift_FORCE_LOAD_$_swiftCoreAudio_$_FinHealth
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_FinHealth
- __swift_FORCE_LOAD_$_swiftIntents
- __swift_FORCE_LOAD_$_swiftIntents_$_FinHealth
- _block_copy_helper.11
- _block_copy_helper.14
- _block_copy_helper.18
- _block_copy_helper.2
- _block_copy_helper.21
- _block_copy_helper.5
- _block_copy_helper.8
- _block_descriptor.10
- _block_descriptor.13
- _block_descriptor.16
- _block_descriptor.20
- _block_descriptor.23
- _block_descriptor.4
- _block_descriptor.7
- _block_destroy_helper.12
- _block_destroy_helper.15
- _block_destroy_helper.19
- _block_destroy_helper.22
- _block_destroy_helper.3
- _block_destroy_helper.6
- _block_destroy_helper.9
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x28
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
Functions:
~ -[FHSearchSuggestionController initWithDelegate:] : 264 -> 268
~ -[FHSearchSuggestionController init] : 232 -> 236
~ -[FHSearchSuggestionController dealloc] : 224 -> 228
~ -[FHSearchSuggestionController deleteAllData:] : 324 -> 328
~ ___46-[FHSearchSuggestionController deleteAllData:]_block_invoke : 280 -> 288
~ -[FHSearchSuggestionController featuresForApplication:withCompletion:] : 420 -> 428
~ -[FHSearchSuggestionController fetchUserProperties:withParameters:completion:] : 200 -> 192
~ ___78-[FHSearchSuggestionController fetchUserProperties:withParameters:completion:]_block_invoke : 236 -> 248
~ -[FHSearchSuggestionController paymentRingSuggestionsFromSearchFeatures:startDate:endDate:completion:] : 436 -> 428
~ -[FHSearchSuggestionController featureResponsesForApplication:withCompletion:] : 440 -> 444
~ -[FHSearchSuggestionController getDisputeDocumentSuggestionsForTransactionId:completion:] : 200 -> 196
~ -[FHSearchSuggestionController sendAllTransactionFeatures] : 196 -> 200
~ -[FHSearchSuggestionController reevaluateTransactionFeatures] : 540 -> 552
~ ___61-[FHSearchSuggestionController reevaluateTransactionFeatures]_block_invoke : 376 -> 396
~ ___61-[FHSearchSuggestionController reevaluateTransactionFeatures]_block_invoke.100 : 344 -> 352
~ -[FHSearchSuggestionController _sendAllTransactionFeatures:] : 556 -> 568
~ ___60-[FHSearchSuggestionController _sendAllTransactionFeatures:]_block_invoke : 376 -> 396
~ ___60-[FHSearchSuggestionController _sendAllTransactionFeatures:]_block_invoke.102 : 344 -> 352
~ -[FHSearchSuggestionController transactionsRequireSyncing] : 216 -> 224
~ ___58-[FHSearchSuggestionController transactionsRequireSyncing]_block_invoke : 212 -> 220
~ -[FHSearchSuggestionController recordUserInteraction:] : 244 -> 256
~ -[FHSearchSuggestionController _validateInstrumentationRecord:] : 696 -> 704
~ -[FHSearchSuggestionController _updateOrRecordCacheEntries:instrumentationCacheSize:] : 432 -> 444
~ ___85-[FHSearchSuggestionController _updateOrRecordCacheEntries:instrumentationCacheSize:]_block_invoke : 180 -> 184
~ -[FHSearchSuggestionController allPeerPaymentForecastingSignals:] : 352 -> 360
~ -[FHSearchSuggestionController generatePredictionWithModelType:withModelPathComponent:completion:] : 376 -> 372
~ -[FHSearchSuggestionController predictionsByModelName:modelVersion:completion:] : 416 -> 412
~ -[FHSearchSuggestionController updatePeerPaymentForecastingSuggestionStatus:counterpartHandle:amount:completion:] : 384 -> 380
~ -[FHSearchSuggestionController updatePeerPaymentAccountBalanceWithTransactionSourceId:amount:currencyCode:completion:] : 396 -> 388
~ -[FHSearchSuggestionController allFeatureInsightsWithStartDate:endDate:insightTypeItems:trendWindow:completion:] : 420 -> 412
~ -[FHSearchSuggestionController getTopTransactionCategoriesWithCountryCode:timeWindow:minRegularTransactionRatio:discretizedTimeOfDay:completion:] : 240 -> 236
~ -[FHSearchSuggestionController _clientConnection] : 452 -> 468
~ -[FHSearchSuggestionController _newClientConnection] : 532 -> 540
~ ___52-[FHSearchSuggestionController _newClientConnection]_block_invoke : 208 -> 212
~ ___52-[FHSearchSuggestionController _newClientConnection]_block_invoke.116 : 208 -> 212
~ -[FHSearchSuggestionController _remoteObjectInterface] : 2392 -> 2444
~ -[FHSearchSuggestionController _remoteObjectProxyWithErrorHandler] : 252 -> 260
~ ___66-[FHSearchSuggestionController _remoteObjectProxyWithErrorHandler]_block_invoke : 272 -> 280
~ -[FHSearchSuggestionController setConnection:] : 12 -> 64
~ -[FHSearchSuggestionController setInstrumentationCache:] : 12 -> 64
~ -[FHPaymentRingData initWithTransactionDate:transactionAmount:paymentAmountCategory:] : 160 -> 152
~ -[FHPaymentRingData hash] : 120 -> 128
~ -[FHPaymentRingData isEqual:] : 264 -> 280
~ -[FHPaymentRingData description] : 208 -> 216
~ -[FHPaymentRingSuggestionController generatePaymentRingSuggestionsFromConvertedObjects:previousStatementPaymentsSum:currentStatementPaymentsSum:statementPurchasesSum:merchantCategoryTransactionSums:billPaymentSelectedSuggestedAmountData:isMonthZero:isMonthOne:] : 344 -> 364
~ -[FHPaymentRingSuggestionController generatePaymentRingSuggestion:] : 5780 -> 6220
~ ___67-[FHPaymentRingSuggestionController generatePaymentRingSuggestion:]_block_invoke : 212 -> 224
~ ___67-[FHPaymentRingSuggestionController generatePaymentRingSuggestion:]_block_invoke.89 : 428 -> 432
~ -[FHPaymentRingSuggestionController recordPaymentRingAction:] : 420 -> 440
~ -[FHPaymentRingSuggestionController _zerothOrFirstMonthPaymentRingSuggestionsForList:] : 2712 -> 2920
~ -[FHPaymentRingSuggestionController _allMandatoryValuesAreSameAmount:] : 372 -> 392
~ -[FHPaymentRingSuggestionController _minimumMerchcantCategoriesAboveMinimumAmount:minMerchantCategory1:minMerchantCategory2:minMerchantCategorySum1:minMerchantCategorySum2:merchantCategoryTransactionSums:] : 568 -> 564
~ ___205-[FHPaymentRingSuggestionController _minimumMerchcantCategoriesAboveMinimumAmount:minMerchantCategory1:minMerchantCategory2:minMerchantCategorySum1:minMerchantCategorySum2:merchantCategoryTransactionSums:]_block_invoke : 304 -> 296
~ -[FHPaymentRingSuggestionController _suggestedAmountsForPayOffDateForStatementBalance:statementPurchasesSum:creditUtilization:lastPaymentCategory:] : 1448 -> 1604
~ -[FHPaymentRingSuggestionController _calculateThresholdForLastPaymentCategory:statementBalance:lastPaymentCategoryAmount:previousStatementPaymentsSum:statementPurchasesSum:] : 596 -> 624
~ -[FHPaymentRingSuggestionController _filterSuggestions:belowThreshold:] : 400 -> 404
~ -[FHPaymentRingSuggestionRequest initWithcurrentStatement:previousStatement:previousStatementPaymentsSum:currentStatementPaymentsSum:statementPurchasesSum:merchantCategoryTransactionSums:paymentDetails:] : 328 -> 300
~ -[FHPaymentRingSuggestionRequest hash] : 268 -> 296
~ -[FHPaymentRingSuggestionRequest isEqual:] : 616 -> 672
~ -[FHPaymentRingSuggestionRequest description] : 280 -> 284
~ -[FHPaymentRingSuggestionRequest setCurrentStatement:] : 12 -> 64
~ -[FHPaymentRingSuggestionRequest setPreviousStatement:] : 12 -> 64
~ -[FHPaymentRingSuggestionRequest setPreviousStatementPaymentsSum:] : 12 -> 64
~ -[FHPaymentRingSuggestionRequest setCurrentStatementPaymentsSum:] : 12 -> 64
~ -[FHPaymentRingSuggestionRequest setStatementPurchasesSum:] : 12 -> 64
~ -[FHPaymentRingSuggestionRequest setMerchantCategoryTransactionSums:] : 12 -> 64
~ -[FHPaymentRingSuggestionRequest setPaymentDetails:] : 12 -> 64
~ -[FHStatementDetails hash] : 452 -> 496
~ -[FHStatementDetails isEqual:] : 1020 -> 1108
~ -[FHStatementDetails description] : 448 -> 452
~ -[FHStatementDetails setStatementIdentifier:] : 12 -> 64
~ -[FHStatementDetails setOpeningDate:] : 12 -> 64
~ -[FHStatementDetails setClosingDate:] : 12 -> 64
~ -[FHStatementDetails setRemainingStatementBalance:] : 12 -> 64
~ -[FHStatementDetails setCombinedBalance:] : 12 -> 64
~ -[FHStatementDetails setRemainingMinimumPayment:] : 12 -> 64
~ -[FHStatementDetails setMinimumDue:] : 12 -> 64
~ -[FHStatementDetails setCreditLimit:] : 12 -> 64
~ -[FHStatementDetails setStatementBalance:] : 12 -> 64
~ -[FHStatementDetails setCurrentBalance:] : 12 -> 64
~ -[FHStatementDetails setCurrentBalanceForMonthZero:] : 12 -> 64
~ -[FHStatementDetails setCurrentStatementIdentifier:] : 12 -> 64
~ _RequestFromPKAccountSummary : 1948 -> 2180
~ _ResponseToPKBillPaymentSuggestion : 392 -> 396
~ sub_24ee3949c -> sub_253d22dfc : 52 -> 44
~ sub_24ee394d0 -> sub_253d22e28 : 720 -> 656
~ sub_24ee39938 -> sub_253d23250 : 460 -> 472
~ sub_24ee39f14 -> sub_253d23838 : 184 -> 20
~ sub_24ee3a100 -> sub_253d23980 : 1032 -> 1020
~ sub_24ee3a508 -> sub_253d23d7c : 224 -> 200
~ sub_24ee3a658 -> sub_253d23eb4 : 224 -> 200
~ sub_24ee3a84c -> sub_253d24090 : 444 -> 436
~ sub_24ee3aa08 -> sub_253d24244 : 272 -> 252
~ sub_24ee3ad4c -> sub_253d24574 : 420 -> 412
~ sub_24ee3aef0 -> sub_253d24710 : 224 -> 200
~ sub_24ee3b0fc -> sub_253d24904 : 444 -> 436
~ sub_24ee3b2b8 -> sub_253d24ab8 : 272 -> 252
~ _block_copy_helper : 16 -> 20
~ sub_24ee3b4bc -> sub_253d24cac : 92 -> 84
~ ___swift_destroy_boxed_opaque_existential_0 : 76 -> 68
~ sub_24ee3b648 -> sub_253d24e28 : 268 -> 276
~ sub_24ee3b7a0 -> sub_253d24f88 : 304 -> 312
~ sub_24ee3b8d0 -> sub_253d250c0 : 236 -> 244
~ sub_24ee3bcd8 -> sub_253d254d0 : 12 -> 8

```
