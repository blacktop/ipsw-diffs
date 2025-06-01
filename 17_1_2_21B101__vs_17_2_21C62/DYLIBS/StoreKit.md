## StoreKit

> `/System/Library/Frameworks/StoreKit.framework/StoreKit`

```diff

-813.1.7.0.0
-  __TEXT.__text: 0x144c20
-  __TEXT.__auth_stubs: 0x3000
-  __TEXT.__objc_methlist: 0x4734
-  __TEXT.__gcc_except_tab: 0xf1c
-  __TEXT.__const: 0x8330
-  __TEXT.__cstring: 0x644a
-  __TEXT.__oslogstring: 0x22ee
+813.2.8.0.0
+  __TEXT.__text: 0x16f9b0
+  __TEXT.__auth_stubs: 0x3120
+  __TEXT.__objc_methlist: 0x46f4
+  __TEXT.__gcc_except_tab: 0xef0
+  __TEXT.__const: 0x942a
+  __TEXT.__cstring: 0x731a
+  __TEXT.__oslogstring: 0x1fe0
   __TEXT.__dlopen_cstrs: 0x3dd
-  __TEXT.__constg_swiftt: 0x2678
-  __TEXT.__swift5_typeref: 0x2d7c
-  __TEXT.__swift5_builtin: 0x1f4
-  __TEXT.__swift5_reflstr: 0x1bac
-  __TEXT.__swift5_fieldmd: 0x27dc
-  __TEXT.__swift5_capture: 0xb70
-  __TEXT.__swift5_assocty: 0xa70
-  __TEXT.__swift5_proto: 0x7d8
-  __TEXT.__swift5_types: 0x370
+  __TEXT.__swift5_typeref: 0x3263
+  __TEXT.__constg_swiftt: 0x2a84
+  __TEXT.__swift5_reflstr: 0x1d35
+  __TEXT.__swift5_fieldmd: 0x2c24
+  __TEXT.__swift5_builtin: 0x208
+  __TEXT.__swift5_assocty: 0xa88
+  __TEXT.__swift5_proto: 0x920
+  __TEXT.__swift5_types: 0x3bc
+  __TEXT.__swift5_capture: 0xd3c
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__swift5_protos: 0x28
-  __TEXT.__unwind_info: 0x6804
-  __TEXT.__eh_frame: 0x7748
-  __TEXT.__objc_classname: 0x122a
-  __TEXT.__objc_methname: 0xc9c4
-  __TEXT.__objc_methtype: 0x2b66
-  __TEXT.__objc_stubs: 0x8340
-  __DATA_CONST.__got: 0x798
-  __DATA_CONST.__const: 0x1900
-  __DATA_CONST.__objc_classlist: 0x3d0
+  __TEXT.__swift5_protos: 0x38
+  __TEXT.__unwind_info: 0x6ecc
+  __TEXT.__eh_frame: 0x8660
+  __TEXT.__objc_classname: 0x1202
+  __TEXT.__objc_methname: 0xc902
+  __TEXT.__objc_methtype: 0x2af5
+  __TEXT.__objc_stubs: 0x8240
+  __DATA_CONST.__got: 0x7b0
+  __DATA_CONST.__const: 0x1960
+  __DATA_CONST.__objc_classlist: 0x3c8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x132b0
-  __DATA_CONST.__objc_selrefs: 0x2cf0
+  __DATA_CONST.__objc_const: 0x12eb0
+  __DATA_CONST.__objc_selrefs: 0x2cd8
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__const: 0x8270
-  __AUTH_CONST.__objc_const: 0x2828
-  __AUTH_CONST.__cfstring: 0x3700
+  __AUTH_CONST.__const: 0x94c8
+  __AUTH_CONST.__objc_const: 0x2798
+  __AUTH_CONST.__cfstring: 0x3720
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1810
-  __AUTH.__objc_data: 0x24b8
-  __AUTH.__data: 0x24e0
-  __DATA.__objc_protorefs: 0x118
-  __DATA.__objc_classrefs: 0x570
-  __DATA.__objc_superrefs: 0x238
-  __DATA.__objc_ivar: 0x5d8
-  __DATA.__data: 0x7fd8
-  __DATA.__bss: 0xb620
-  __DATA.__common: 0x60
+  __AUTH_CONST.__auth_got: 0x18a0
+  __AUTH.__objc_data: 0x2488
+  __AUTH.__data: 0x27c8
+  __DATA.__objc_protorefs: 0x110
+  __DATA.__objc_classrefs: 0x580
+  __DATA.__objc_superrefs: 0x228
+  __DATA.__objc_ivar: 0x5d0
+  __DATA.__data: 0x8258
+  __DATA.__bss: 0xdc30
+  __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 54F79750-144E-36D9-B3F1-3D606ACAEA13
-  Functions: 10132
-  Symbols:   13362
-  CStrings:  4075
+  UUID: EFDF6838-6D43-3E69-906B-5238AB709FDC
+  Functions: 11107
+  Symbols:   14041
+  CStrings:  4154
 
Symbols:
+ -[SKCloudServiceSetupViewController _reportCompletionForInlineOfferUnsupported]
+ -[SKPaymentQueue(Package) notifyPurchaseIntentObserversForProducts:]
+ -[SKProductLookupResponse deepLinkURL]
+ -[SKProductLookupResponse initWithResult:extensionID:productURL:isEntitled:parameters:deepLinkURL:]
+ -[SKProductRemoteViewTask _displayItemIfNeeded]
+ -[SKServiceBroker overrideServiceWithErrorHandler:]
+ -[SKServiceBroker overrideSynchronousServiceWithErrorHandler:]
+ -[SKServiceBroker purchaseIntentServiceWithErrorHandler:]
+ GCC_except_table102
+ GCC_except_table111
+ GCC_except_table40
+ GCC_except_table46
+ GCC_except_table65
+ GCC_except_table71
+ GCC_except_table80
+ GCC_except_table88
+ GCC_except_table91
+ GCC_except_table93
+ GCC_except_table95
+ GCC_except_table97
+ _OBJC_IVAR_$_SKCloudServiceSetupViewController._alertController
+ _OBJC_IVAR_$_SKCloudServiceSetupViewController._isInlineOfferUnsupported
+ _OBJC_IVAR_$_SKProductLookupResponse._deepLinkURL
+ _OBJC_IVAR_$_SKProductRemoteViewTask._deepLinkURL
+ _OUTLINED_FUNCTION_324
+ _OUTLINED_FUNCTION_325
+ _OUTLINED_FUNCTION_326
+ _OUTLINED_FUNCTION_327
+ _OUTLINED_FUNCTION_328
+ _OUTLINED_FUNCTION_329
+ _OUTLINED_FUNCTION_330
+ _OUTLINED_FUNCTION_331
+ _OUTLINED_FUNCTION_332
+ _OUTLINED_FUNCTION_333
+ _OUTLINED_FUNCTION_334
+ _OUTLINED_FUNCTION_335
+ _OUTLINED_FUNCTION_336
+ _OUTLINED_FUNCTION_337
+ _OUTLINED_FUNCTION_338
+ _OUTLINED_FUNCTION_339
+ _OUTLINED_FUNCTION_340
+ _OUTLINED_FUNCTION_341
+ _OUTLINED_FUNCTION_342
+ _OUTLINED_FUNCTION_343
+ _OUTLINED_FUNCTION_344
+ _OUTLINED_FUNCTION_345
+ _OUTLINED_FUNCTION_346
+ _OUTLINED_FUNCTION_347
+ _OUTLINED_FUNCTION_348
+ _OUTLINED_FUNCTION_349
+ _OUTLINED_FUNCTION_350
+ _OUTLINED_FUNCTION_351
+ _OUTLINED_FUNCTION_352
+ _OUTLINED_FUNCTION_353
+ _OUTLINED_FUNCTION_354
+ _OUTLINED_FUNCTION_355
+ _OUTLINED_FUNCTION_356
+ _OUTLINED_FUNCTION_357
+ _OUTLINED_FUNCTION_358
+ _OUTLINED_FUNCTION_359
+ _OUTLINED_FUNCTION_360
+ _OUTLINED_FUNCTION_361
+ _OUTLINED_FUNCTION_362
+ _OUTLINED_FUNCTION_363
+ _OUTLINED_FUNCTION_364
+ _OUTLINED_FUNCTION_365
+ _OUTLINED_FUNCTION_366
+ _OUTLINED_FUNCTION_367
+ _OUTLINED_FUNCTION_368
+ _OUTLINED_FUNCTION_369
+ _OUTLINED_FUNCTION_370
+ _OUTLINED_FUNCTION_371
+ _OUTLINED_FUNCTION_372
+ _OUTLINED_FUNCTION_373
+ _OUTLINED_FUNCTION_374
+ _OUTLINED_FUNCTION_375
+ _OUTLINED_FUNCTION_376
+ _OUTLINED_FUNCTION_377
+ _OUTLINED_FUNCTION_378
+ _OUTLINED_FUNCTION_379
+ _OUTLINED_FUNCTION_380
+ _OUTLINED_FUNCTION_381
+ _OUTLINED_FUNCTION_382
+ _OUTLINED_FUNCTION_383
+ _OUTLINED_FUNCTION_384
+ _OUTLINED_FUNCTION_385
+ _OUTLINED_FUNCTION_386
+ _OUTLINED_FUNCTION_387
+ _OUTLINED_FUNCTION_388
+ _OUTLINED_FUNCTION_389
+ _OUTLINED_FUNCTION_390
+ _OUTLINED_FUNCTION_391
+ _OUTLINED_FUNCTION_392
+ _OUTLINED_FUNCTION_393
+ _OUTLINED_FUNCTION_394
+ _OUTLINED_FUNCTION_395
+ _OUTLINED_FUNCTION_396
+ _OUTLINED_FUNCTION_397
+ _OUTLINED_FUNCTION_398
+ _OUTLINED_FUNCTION_399
+ _OUTLINED_FUNCTION_400
+ _OUTLINED_FUNCTION_401
+ _OUTLINED_FUNCTION_402
+ _OUTLINED_FUNCTION_403
+ _OUTLINED_FUNCTION_404
+ _OUTLINED_FUNCTION_405
+ _OUTLINED_FUNCTION_406
+ _OUTLINED_FUNCTION_407
+ _OUTLINED_FUNCTION_408
+ _OUTLINED_FUNCTION_409
+ _OUTLINED_FUNCTION_410
+ _OUTLINED_FUNCTION_411
+ _OUTLINED_FUNCTION_412
+ _OUTLINED_FUNCTION_413
+ _OUTLINED_FUNCTION_414
+ _OUTLINED_FUNCTION_415
+ _OUTLINED_FUNCTION_416
+ _OUTLINED_FUNCTION_417
+ _OUTLINED_FUNCTION_418
+ _OUTLINED_FUNCTION_419
+ _OUTLINED_FUNCTION_420
+ _OUTLINED_FUNCTION_421
+ _OUTLINED_FUNCTION_422
+ _OUTLINED_FUNCTION_423
+ _OUTLINED_FUNCTION_424
+ _OUTLINED_FUNCTION_425
+ _OUTLINED_FUNCTION_426
+ _OUTLINED_FUNCTION_427
+ _OUTLINED_FUNCTION_428
+ _OUTLINED_FUNCTION_429
+ _OUTLINED_FUNCTION_430
+ _OUTLINED_FUNCTION_431
+ _OUTLINED_FUNCTION_432
+ _OUTLINED_FUNCTION_433
+ _OUTLINED_FUNCTION_434
+ _OUTLINED_FUNCTION_435
+ _OUTLINED_FUNCTION_436
+ _OUTLINED_FUNCTION_437
+ _OUTLINED_FUNCTION_438
+ _OUTLINED_FUNCTION_439
+ _OUTLINED_FUNCTION_440
+ _OUTLINED_FUNCTION_441
+ _OUTLINED_FUNCTION_442
+ _OUTLINED_FUNCTION_443
+ _OUTLINED_FUNCTION_444
+ _OUTLINED_FUNCTION_445
+ _OUTLINED_FUNCTION_446
+ _OUTLINED_FUNCTION_447
+ _OUTLINED_FUNCTION_448
+ _OUTLINED_FUNCTION_449
+ _OUTLINED_FUNCTION_450
+ _OUTLINED_FUNCTION_451
+ _OUTLINED_FUNCTION_452
+ _OUTLINED_FUNCTION_453
+ _OUTLINED_FUNCTION_454
+ _OUTLINED_FUNCTION_455
+ _OUTLINED_FUNCTION_456
+ _OUTLINED_FUNCTION_457
+ _OUTLINED_FUNCTION_458
+ _OUTLINED_FUNCTION_459
+ _OUTLINED_FUNCTION_460
+ _OUTLINED_FUNCTION_461
+ _OUTLINED_FUNCTION_462
+ _OUTLINED_FUNCTION_463
+ _OUTLINED_FUNCTION_464
+ _OUTLINED_FUNCTION_465
+ _OUTLINED_FUNCTION_466
+ _OUTLINED_FUNCTION_467
+ _OUTLINED_FUNCTION_468
+ __DATA_SKInstallSheetStatusUpdateRequest
+ __DATA_SKPurchaseIntent
+ __IVARS_SKInstallSheetStatusUpdateRequest
+ __IVARS_SKPurchaseIntent
+ __IVARS__TtC8StoreKit15SKTwoErrorEvent
+ __IVARS__TtCV8StoreKit14PurchaseIntent22PurchaseIntentListener
+ __METACLASS_DATA_SKInstallSheetStatusUpdateRequest
+ __METACLASS_DATA_SKPurchaseIntent
+ __OBJC_$_CLASS_METHODS_SKPaymentQueue(Package|Internal|Private)
+ __OBJC_$_INSTANCE_METHODS_SKPaymentQueue(Package|Internal|Private)
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OverrideService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PurchaseIntentService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_OverrideService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PurchaseIntentService
+ __OBJC_LABEL_PROTOCOL_$_OverrideService
+ __OBJC_LABEL_PROTOCOL_$_PurchaseIntentService
+ __OBJC_PROTOCOL_$_OverrideService
+ __OBJC_PROTOCOL_$_PurchaseIntentService
+ __PROPERTIES_SKPurchaseIntent
+ ___38-[SKPaymentQueue _processTransaction:]_block_invoke.103
+ ___38-[SKPaymentQueue _processTransaction:]_block_invoke.103.cold.1
+ ___42-[SKPaymentQueue _checkServerQueueForced:]_block_invoke.90
+ ___47-[SKProductRemoteViewTask _displayItemIfNeeded]_block_invoke
+ ___47-[SKProductRemoteViewTask _displayItemIfNeeded]_block_invoke_2
+ ___47-[SKProductRemoteViewTask _displayItemIfNeeded]_block_invoke_3
+ ___48-[SKClientBroker _checkStorefrontChangedNotify:]_block_invoke.32
+ ___48-[SKPaymentQueue _updatedTransactions:restored:]_block_invoke.109
+ ___48-[SKProductRemoteViewTask _showExtensionWithID:]_block_invoke.45
+ ___51-[SKServiceBroker overrideServiceWithErrorHandler:]_block_invoke
+ ___57-[SKServiceBroker purchaseIntentServiceWithErrorHandler:]_block_invoke
+ ___59-[SKClientBroker _handleUnfinishedTransactionsNotification]_block_invoke.34
+ ___59-[SKClientBroker _handleUnfinishedTransactionsNotification]_block_invoke.34.cold.1
+ ___62-[SKProductRemoteViewTask loadProductWithURL:completionBlock:]_block_invoke.cold.2
+ ___62-[SKServiceBroker overrideSynchronousServiceWithErrorHandler:]_block_invoke
+ ___66-[SKProductRemoteViewTask lookupProductWithParameters:completion:]_block_invoke.cold.2
+ ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.38
+ ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.38.cold.1
+ ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.40
+ ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.40.cold.1
+ ___67-[SKStoreProductViewController loadProductWithURL:completionBlock:]_block_invoke_2
+ ___68-[SKPaymentQueue(Package) notifyPurchaseIntentObserversForProducts:]_block_invoke
+ ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_literal_global.32
+ ___block_literal_global.42
+ ___block_literal_global.51
+ ___block_literal_global.55
+ ___swift_memcpy40_8
+ _associated conformance 15StoreKit_Shared14ClientOverrideV6ServerO10CodingKeysOSHAASQ
+ _associated conformance 15StoreKit_Shared14ClientOverrideV6ServerO10CodingKeysOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 15StoreKit_Shared14ClientOverrideV6ServerO10CodingKeysOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15StoreKit_Shared14ClientOverrideV6ServerO19XcodeTestCodingKeysOSHAASQ
+ _associated conformance 15StoreKit_Shared14ClientOverrideV6ServerO19XcodeTestCodingKeysOs0I3KeyAAs23CustomStringConvertible
+ _associated conformance 15StoreKit_Shared14ClientOverrideV6ServerO19XcodeTestCodingKeysOs0I3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15StoreKit_Shared21ClientOverrideRequestV10CodingKeys33_E3B6664E0869A8AECE5EB77EA32CD978LLOSHAASQ
+ _associated conformance 15StoreKit_Shared21ClientOverrideRequestV10CodingKeys33_E3B6664E0869A8AECE5EB77EA32CD978LLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 15StoreKit_Shared21ClientOverrideRequestV10CodingKeys33_E3B6664E0869A8AECE5EB77EA32CD978LLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15StoreKit_Shared21PurchaseIntentRequestO3AddV10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063K0LLOSHAASQ
+ _associated conformance 15StoreKit_Shared21PurchaseIntentRequestO3AddV10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063K0LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 15StoreKit_Shared21PurchaseIntentRequestO3AddV10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063K0LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15StoreKit_Shared21PurchaseIntentRequestO4KindO10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063K0LLOSHAASQ
+ _associated conformance 15StoreKit_Shared21PurchaseIntentRequestO4KindO10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063K0LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 15StoreKit_Shared21PurchaseIntentRequestO4KindO10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063K0LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15StoreKit_Shared21PurchaseIntentRequestO4KindO13AllCodingKeys031_BF4C5A2328F50B9FC8FAE275833063L0LLOs0I3KeyAAs23CustomStringConvertible
+ _associated conformance 15StoreKit_Shared21PurchaseIntentRequestO4KindO13AllCodingKeys031_BF4C5A2328F50B9FC8FAE275833063L0LLOs0I3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15StoreKit_Shared21PurchaseIntentRequestO4KindO16ClientCodingKeys031_BF4C5A2328F50B9FC8FAE275833063L0LLOs0I3KeyAAs23CustomStringConvertible
+ _associated conformance 15StoreKit_Shared21PurchaseIntentRequestO4KindO16ClientCodingKeys031_BF4C5A2328F50B9FC8FAE275833063L0LLOs0I3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15StoreKit_Shared21PurchaseIntentRequestO4KindOSHAASQ
+ _associated conformance 15StoreKit_Shared21PurchaseIntentRequestO5QueryV10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063K0LLOSHAASQ
+ _associated conformance 15StoreKit_Shared21PurchaseIntentRequestO5QueryV10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063K0LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 15StoreKit_Shared21PurchaseIntentRequestO5QueryV10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063K0LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15StoreKit_Shared21PurchaseIntentRequestO6RemoveV10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063K0LLOSHAASQ
+ _associated conformance 15StoreKit_Shared21PurchaseIntentRequestO6RemoveV10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063K0LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 15StoreKit_Shared21PurchaseIntentRequestO6RemoveV10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063K0LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15StoreKit_Shared22PurchaseIntentInternalV10CodingKeys33_90EB9D59E00D8FD7BFFB1921DF378322LLOSHAASQ
+ _associated conformance 15StoreKit_Shared22PurchaseIntentInternalV10CodingKeys33_90EB9D59E00D8FD7BFFB1921DF378322LLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 15StoreKit_Shared22PurchaseIntentInternalV10CodingKeys33_90EB9D59E00D8FD7BFFB1921DF378322LLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 8StoreKit0aB10ViewOriginOSHAASQ
+ _associated conformance 8StoreKit11TransactionV3KeyOs06CodingD0AAs23CustomStringConvertible
+ _associated conformance 8StoreKit11TransactionV3KeyOs06CodingD0AAs28CustomDebugStringConvertible
+ _associated conformance 8StoreKit11TransactionV5OfferV11PaymentModeVSHAASQ
+ _associated conformance 8StoreKit11TransactionV5OfferVSHAASQ
+ _block_copy_helper.105
+ _block_copy_helper.107
+ _block_copy_helper.113
+ _block_copy_helper.116
+ _block_copy_helper.122
+ _block_copy_helper.128
+ _block_copy_helper.134
+ _block_copy_helper.33
+ _block_copy_helper.39
+ _block_copy_helper.4
+ _block_copy_helper.45
+ _block_copy_helper.46
+ _block_copy_helper.51
+ _block_copy_helper.57
+ _block_copy_helper.63
+ _block_copy_helper.69
+ _block_copy_helper.87
+ _block_copy_helper.9
+ _block_copy_helper.93
+ _block_copy_helper.99
+ _block_descriptor.101
+ _block_descriptor.107
+ _block_descriptor.109
+ _block_descriptor.11
+ _block_descriptor.115
+ _block_descriptor.118
+ _block_descriptor.124
+ _block_descriptor.130
+ _block_descriptor.136
+ _block_descriptor.35
+ _block_descriptor.41
+ _block_descriptor.47
+ _block_descriptor.48
+ _block_descriptor.53
+ _block_descriptor.59
+ _block_descriptor.6
+ _block_descriptor.65
+ _block_descriptor.71
+ _block_descriptor.89
+ _block_descriptor.95
+ _block_destroy_helper.10
+ _block_destroy_helper.100
+ _block_destroy_helper.106
+ _block_destroy_helper.108
+ _block_destroy_helper.114
+ _block_destroy_helper.117
+ _block_destroy_helper.123
+ _block_destroy_helper.129
+ _block_destroy_helper.135
+ _block_destroy_helper.34
+ _block_destroy_helper.40
+ _block_destroy_helper.46
+ _block_destroy_helper.47
+ _block_destroy_helper.5
+ _block_destroy_helper.52
+ _block_destroy_helper.58
+ _block_destroy_helper.64
+ _block_destroy_helper.70
+ _block_destroy_helper.88
+ _block_destroy_helper.94
+ _kCoreAnalyticsKeyContext
+ _keypath_get_selector_additionalBuyParams
+ _objc_msgSend$_displayItemIfNeeded
+ _objc_msgSend$_reportCompletionForInlineOfferUnsupported
+ _objc_msgSend$_unknownErrorWithUserInfo:
+ _objc_msgSend$canOpenURL:
+ _objc_msgSend$deepLinkURL
+ _objc_msgSend$listenForPurchaseIntents
+ _objc_msgSend$openURL:options:completionHandler:
+ _objc_msgSend$stopListeningForPurchaseIntents
+ _objectdestroy.124Tm
+ _objectdestroy.126Tm
+ _objectdestroy.14Tm
+ _objectdestroy.15Tm
+ _objectdestroy.221Tm
+ _objectdestroy.37Tm
+ _objectdestroy.90Tm
+ _swift_dynamicCastMetatype
+ _symbolic $s15StoreKit_Shared17ClientOverridableP
+ _symbolic $s15StoreKit_Shared24ClientOverridableRequestP
+ _symbolic $s15StoreKit_Shared7RequestP
+ _symbolic $s15StoreKit_Shared8LoggableP
+ _symbolic IeyB_
+ _symbolic SDy__________ySayxG_GG s11AnyHashableV ScS12ContinuationV
+ _symbolic SaySo9SKProductCG
+ _symbolic Say_____G 15StoreKit_Shared22PurchaseIntentInternalV
+ _symbolic ScSySaySo9SKProductCGG
+ _symbolic ScSySay_____GG 8StoreKit7ProductV
+ _symbolic SccySaySSG______pG s5ErrorP
+ _symbolic So14SKPaymentQueueC
+ _symbolic So16SKPurchaseIntentC
+ _symbolic So33SKInstallSheetStatusUpdateRequestC
+ _symbolic So7NSErrorCSgIeyBy_
+ _symbolic Ss
+ _symbolic Ss_Sst
+ _symbolic _____ 15StoreKit_Shared14ClientOverrideV6ServerO10CodingKeysO
+ _symbolic _____ 15StoreKit_Shared14ClientOverrideV6ServerO19XcodeTestCodingKeysO
+ _symbolic _____ 15StoreKit_Shared21ClientOverrideRequestV
+ _symbolic _____ 15StoreKit_Shared21ClientOverrideRequestV10CodingKeys33_E3B6664E0869A8AECE5EB77EA32CD978LLO
+ _symbolic _____ 15StoreKit_Shared21PurchaseIntentRequestO
+ _symbolic _____ 15StoreKit_Shared21PurchaseIntentRequestO3AddV
+ _symbolic _____ 15StoreKit_Shared21PurchaseIntentRequestO3AddV10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063K0LLO
+ _symbolic _____ 15StoreKit_Shared21PurchaseIntentRequestO4KindO
+ _symbolic _____ 15StoreKit_Shared21PurchaseIntentRequestO4KindO10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063K0LLO
+ _symbolic _____ 15StoreKit_Shared21PurchaseIntentRequestO4KindO13AllCodingKeys031_BF4C5A2328F50B9FC8FAE275833063L0LLO
+ _symbolic _____ 15StoreKit_Shared21PurchaseIntentRequestO4KindO16ClientCodingKeys031_BF4C5A2328F50B9FC8FAE275833063L0LLO
+ _symbolic _____ 15StoreKit_Shared21PurchaseIntentRequestO5QueryV
+ _symbolic _____ 15StoreKit_Shared21PurchaseIntentRequestO5QueryV10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063K0LLO
+ _symbolic _____ 15StoreKit_Shared21PurchaseIntentRequestO6RemoveV
+ _symbolic _____ 15StoreKit_Shared21PurchaseIntentRequestO6RemoveV10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063K0LLO
+ _symbolic _____ 15StoreKit_Shared22PurchaseIntentInternalV
+ _symbolic _____ 15StoreKit_Shared22PurchaseIntentInternalV10CodingKeys33_90EB9D59E00D8FD7BFFB1921DF378322LLO
+ _symbolic _____ 8StoreKit0aB10ViewOriginO
+ _symbolic _____ 8StoreKit11TransactionV5OfferV
+ _symbolic _____ 8StoreKit11TransactionV5OfferV11PaymentModeV
+ _symbolic _____ 8StoreKit14PurchaseIntentV0cD8ListenerC
+ _symbolic _____ So19SKErrorEventContextV
+ _symbolic _____Sg 8StoreKit11TransactionV5OfferV
+ _symbolic _____Sg 8StoreKit11TransactionV5OfferV11PaymentModeV
+ _symbolic _____Sg So19SKErrorEventContextV
+ _symbolic _____Sg So9NSDecimala
+ _symbolic _____ySaySo9SKProductCG_G ScS12ContinuationV
+ _symbolic _____ySaySo9SKProductCG_G ScS8IteratorV
+ _symbolic _____ySaySo9SKProductCG_GSg ScS12ContinuationV
+ _symbolic _____ySaySo9SKProductCG__G ScS12ContinuationV11YieldResultO
+ _symbolic _____ySaySo9SKProductCG__G ScS12ContinuationV15BufferingPolicyO
+ _symbolic _____ySay_____G_G ScS12ContinuationV 8StoreKit7ProductV
+ _symbolic _____ySay_____G_G ScS8IteratorV 8StoreKit7ProductV
+ _symbolic _____ySay_____G_GSg ScS12ContinuationV 8StoreKit7ProductV
+ _symbolic _____ySay_____G__G ScS12ContinuationV11YieldResultO 8StoreKit7ProductV
+ _symbolic _____ySay_____G__G ScS12ContinuationV15BufferingPolicyO 8StoreKit7ProductV
+ _symbolic _____ySs_SstG 17_StringProcessing5RegexV
+ _symbolic _____ySs_Sst_G 17_StringProcessing5RegexV5MatchV
+ _symbolic _____ySs_Sst_GSg 17_StringProcessing5RegexV5MatchV
+ _symbolic _____y_So9SKProductCG 8StoreKit14PurchaseIntentV0cD8ListenerC
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared14ClientOverrideV6ServerO10CodingKeysO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared14ClientOverrideV6ServerO19XcodeTestCodingKeysO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared21ClientOverrideRequestV10CodingKeys33_E3B6664E0869A8AECE5EB77EA32CD978LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared21PurchaseIntentRequestO3AddV10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063N0LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared21PurchaseIntentRequestO4KindO10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063N0LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared21PurchaseIntentRequestO4KindO13AllCodingKeys031_BF4C5A2328F50B9FC8FAE275833063O0LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared21PurchaseIntentRequestO4KindO16ClientCodingKeys031_BF4C5A2328F50B9FC8FAE275833063O0LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared21PurchaseIntentRequestO5QueryV10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063N0LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared21PurchaseIntentRequestO6RemoveV10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063N0LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared22PurchaseIntentInternalV10CodingKeys33_90EB9D59E00D8FD7BFFB1921DF378322LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15StoreKit_Shared14ClientOverrideV6ServerO10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15StoreKit_Shared14ClientOverrideV6ServerO19XcodeTestCodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15StoreKit_Shared21ClientOverrideRequestV10CodingKeys33_E3B6664E0869A8AECE5EB77EA32CD978LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15StoreKit_Shared21PurchaseIntentRequestO3AddV10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063N0LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15StoreKit_Shared21PurchaseIntentRequestO4KindO10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063N0LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15StoreKit_Shared21PurchaseIntentRequestO4KindO13AllCodingKeys031_BF4C5A2328F50B9FC8FAE275833063O0LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15StoreKit_Shared21PurchaseIntentRequestO4KindO16ClientCodingKeys031_BF4C5A2328F50B9FC8FAE275833063O0LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15StoreKit_Shared21PurchaseIntentRequestO5QueryV10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063N0LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15StoreKit_Shared21PurchaseIntentRequestO6RemoveV10CodingKeys031_BF4C5A2328F50B9FC8FAE275833063N0LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15StoreKit_Shared22PurchaseIntentInternalV10CodingKeys33_90EB9D59E00D8FD7BFFB1921DF378322LLO
+ _symbolic _____y_____GSg s22KeyedDecodingContainerV 15StoreKit_Shared14ClientOverrideV6ServerO10CodingKeysO
+ _symbolic _____y______G 8StoreKit14PurchaseIntentV0cD8ListenerC AA7ProductV
+ _symbolic _____y__________ySaySo9SKProductCG_GG s17_NativeDictionaryV s11AnyHashableV ScS12ContinuationV
+ _symbolic _____y__________ySay_____G_GG s17_NativeDictionaryV s11AnyHashableV ScS12ContinuationV 8StoreKit7ProductV
- -[SKClientBroker _checkForPendingPurchaseIntents]
- -[SKClientBroker _purchaseIntentObserverAdded]
- -[SKClientBroker _purchaseIntentObserverRemoved]
- -[SKClientBroker receivedPurchaseIntentsForProductIdentifiers:]
- -[SKClientBroker registerPurchaseIntentsListener:]
- -[SKClientBroker unregisterPurchaseIntentsListener:]
- -[SKInstallSheetStatusUpdateRequest .cxx_destruct]
- -[SKInstallSheetStatusUpdateRequest _start]
- -[SKInstallSheetStatusUpdateRequest _start].cold.1
- -[SKInstallSheetStatusUpdateRequest bundleId]
- -[SKInstallSheetStatusUpdateRequest completionHandler]
- -[SKInstallSheetStatusUpdateRequest initWithAppBundleId:isInstallSheetOpen:completionHandler:]
- -[SKInstallSheetStatusUpdateRequest setCompletionHandler:]
- -[SKPaymentQueue _checkForPurchaseIntents]
- -[SKPaymentQueue _checkForPurchaseIntents].cold.1
- -[SKPaymentQueue _notifyObserversAboutPurchaseIntentsForProducts:]
- -[SKPaymentQueue forceSandboxForBundleIdentifier:untilDate:]
- -[SKPaymentQueue receivedPurchaseIntentsForProductIdentifiers:]
- -[SKProductLookupResponse initWithResult:extensionID:productURL:isEntitled:parameters:]
- -[SKProductRemoteViewTask _showExtensionIfNeeded]
- -[SKPurchaseIntent .cxx_destruct]
- -[SKPurchaseIntent initWithBundleId:productIdentifier:]
- -[SKPurchaseIntent initWithBundleId:productIdentifier:appName:productName:]
- -[SKPurchaseIntent send:]
- -[SKStoreProductViewController _viewTapped:]
- GCC_except_table101
- GCC_except_table103
- GCC_except_table105
- GCC_except_table113
- GCC_except_table122
- GCC_except_table31
- GCC_except_table39
- GCC_except_table44
- GCC_except_table52
- GCC_except_table62
- GCC_except_table69
- GCC_except_table73
- GCC_except_table96
- GCC_except_table99
- _OBJC_CLASS_$__TtCVV8StoreKit14PurchaseIntent15PurchaseIntents23PurchaseIntentsListener
- _OBJC_IVAR_$_SKInstallSheetStatusUpdateRequest._bundleId
- _OBJC_IVAR_$_SKInstallSheetStatusUpdateRequest._completionHandler
- _OBJC_IVAR_$_SKPurchaseIntent._appName
- _OBJC_IVAR_$_SKPurchaseIntent._bundleId
- _OBJC_IVAR_$_SKPurchaseIntent._productIdentifer
- _OBJC_IVAR_$_SKPurchaseIntent._productName
- _OBJC_METACLASS_$__TtCVV8StoreKit14PurchaseIntent15PurchaseIntents23PurchaseIntentsListener
- _SKPurchaseIntentAction
- __DATA__TtCVV8StoreKit14PurchaseIntent15PurchaseIntents23PurchaseIntentsListener
- __IVARS__TtCVV8StoreKit14PurchaseIntent15PurchaseIntents23PurchaseIntentsListener
- __METACLASS_DATA__TtCVV8StoreKit14PurchaseIntent15PurchaseIntents23PurchaseIntentsListener
- __OBJC_$_CLASS_METHODS_SKPaymentQueue
- __OBJC_$_INSTANCE_METHODS_SKPaymentQueue
- __OBJC_$_INSTANCE_METHODS__TtCVV8StoreKit14PurchaseIntent15PurchaseIntents23PurchaseIntentsListener
- __OBJC_$_INSTANCE_VARIABLES_SKInstallSheetStatusUpdateRequest
- __OBJC_$_INSTANCE_VARIABLES_SKPurchaseIntent
- __OBJC_$_PROP_LIST_SKInstallSheetStatusUpdateRequest
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SKPurchaseIntentListenerProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_SKPurchaseIntentListenerProtocol
- __OBJC_$_PROTOCOL_REFS_SKPurchaseIntentListenerProtocol
- __OBJC_CLASS_RO_$_SKInstallSheetStatusUpdateRequest
- __OBJC_CLASS_RO_$_SKPurchaseIntent
- __OBJC_LABEL_PROTOCOL_$_SKPurchaseIntentListenerProtocol
- __OBJC_METACLASS_RO_$_SKInstallSheetStatusUpdateRequest
- __OBJC_METACLASS_RO_$_SKPurchaseIntent
- __OBJC_PROTOCOL_$_SKPurchaseIntentListenerProtocol
- __PROTOCOLS__TtCVV8StoreKit14PurchaseIntent15PurchaseIntents23PurchaseIntentsListener
- __PROTOCOLS__TtCVV8StoreKit14PurchaseIntent15PurchaseIntents23PurchaseIntentsListener.3
- ___25-[SKPurchaseIntent send:]_block_invoke
- ___25-[SKPurchaseIntent send:]_block_invoke.3
- ___25-[SKPurchaseIntent send:]_block_invoke.cold.1
- ___38-[SKPaymentQueue _processTransaction:]_block_invoke.116
- ___38-[SKPaymentQueue _processTransaction:]_block_invoke.116.cold.1
- ___42-[SKPaymentQueue _checkForPurchaseIntents]_block_invoke
- ___42-[SKPaymentQueue _checkForPurchaseIntents]_block_invoke.93
- ___42-[SKPaymentQueue _checkForPurchaseIntents]_block_invoke.cold.1
- ___42-[SKPaymentQueue _checkServerQueueForced:]_block_invoke.97
- ___43-[SKInstallSheetStatusUpdateRequest _start]_block_invoke
- ___43-[SKInstallSheetStatusUpdateRequest _start]_block_invoke.1
- ___43-[SKInstallSheetStatusUpdateRequest _start]_block_invoke.3
- ___43-[SKInstallSheetStatusUpdateRequest _start]_block_invoke.cold.1
- ___43-[SKInstallSheetStatusUpdateRequest _start]_block_invoke_2
- ___46-[SKClientBroker _purchaseIntentObserverAdded]_block_invoke
- ___48-[SKClientBroker _checkStorefrontChangedNotify:]_block_invoke.34
- ___48-[SKPaymentQueue _updatedTransactions:restored:]_block_invoke.122
- ___48-[SKProductRemoteViewTask _showExtensionWithID:]_block_invoke.40
- ___49-[SKClientBroker _checkForPendingPurchaseIntents]_block_invoke
- ___49-[SKClientBroker _checkForPendingPurchaseIntents]_block_invoke.38
- ___49-[SKClientBroker _checkForPendingPurchaseIntents]_block_invoke.cold.1
- ___49-[SKProductRemoteViewTask _showExtensionIfNeeded]_block_invoke
- ___59-[SKClientBroker _handleUnfinishedTransactionsNotification]_block_invoke.36
- ___59-[SKClientBroker _handleUnfinishedTransactionsNotification]_block_invoke.36.cold.1
- ___60-[SKPaymentQueue forceSandboxForBundleIdentifier:untilDate:]_block_invoke
- ___60-[SKPaymentQueue forceSandboxForBundleIdentifier:untilDate:]_block_invoke.52
- ___60-[SKPaymentQueue forceSandboxForBundleIdentifier:untilDate:]_block_invoke.cold.1
- ___63-[SKPaymentQueue receivedPurchaseIntentsForProductIdentifiers:]_block_invoke
- ___66-[SKPaymentQueue _notifyObserversAboutPurchaseIntentsForProducts:]_block_invoke
- ___66-[SKPaymentQueue _notifyObserversAboutPurchaseIntentsForProducts:]_block_invoke.113
- ___66-[SKPaymentQueue _notifyObserversAboutPurchaseIntentsForProducts:]_block_invoke.113.cold.1
- ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.33
- ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.33.cold.1
- ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.35
- ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.35.cold.1
- ___block_descriptor_40_e8_32s_e40_v24?0"SKProductsResponse"8"NSError"16ls32l8
- ___block_literal_global.37
- ___block_literal_global.46
- ___block_literal_global.50
- ___block_literal_global.52
- ___unnamed_2
- _associated conformance 15StoreKit_Shared14ClientOverrideV6ServerO10CodingKeys33_4ADCA8A4C6D34513C3587C3642BA7C7BLLOSHAASQ
- _associated conformance 15StoreKit_Shared14ClientOverrideV6ServerO10CodingKeys33_4ADCA8A4C6D34513C3587C3642BA7C7BLLOs0G3KeyAAs23CustomStringConvertible
- _associated conformance 15StoreKit_Shared14ClientOverrideV6ServerO10CodingKeys33_4ADCA8A4C6D34513C3587C3642BA7C7BLLOs0G3KeyAAs28CustomDebugStringConvertible
- _associated conformance 15StoreKit_Shared14ClientOverrideV6ServerO19XcodeTestCodingKeys33_4ADCA8A4C6D34513C3587C3642BA7C7BLLOSHAASQ
- _associated conformance 15StoreKit_Shared14ClientOverrideV6ServerO19XcodeTestCodingKeys33_4ADCA8A4C6D34513C3587C3642BA7C7BLLOs0I3KeyAAs23CustomStringConvertible
- _associated conformance 15StoreKit_Shared14ClientOverrideV6ServerO19XcodeTestCodingKeys33_4ADCA8A4C6D34513C3587C3642BA7C7BLLOs0I3KeyAAs28CustomDebugStringConvertible
- _block_copy_helper.104
- _block_copy_helper.108
- _block_copy_helper.114
- _block_copy_helper.115
- _block_copy_helper.121
- _block_copy_helper.127
- _block_copy_helper.133
- _block_copy_helper.14
- _block_copy_helper.41
- _block_copy_helper.50
- _block_copy_helper.56
- _block_copy_helper.62
- _block_copy_helper.68
- _block_copy_helper.74
- _block_copy_helper.8
- _block_copy_helper.80
- _block_copy_helper.92
- _block_copy_helper.98
- _block_descriptor.10
- _block_descriptor.100
- _block_descriptor.106
- _block_descriptor.110
- _block_descriptor.116
- _block_descriptor.117
- _block_descriptor.123
- _block_descriptor.129
- _block_descriptor.135
- _block_descriptor.16
- _block_descriptor.43
- _block_descriptor.52
- _block_descriptor.58
- _block_descriptor.64
- _block_descriptor.70
- _block_descriptor.76
- _block_descriptor.82
- _block_descriptor.94
- _block_destroy_helper.105
- _block_destroy_helper.109
- _block_destroy_helper.115
- _block_destroy_helper.116
- _block_destroy_helper.122
- _block_destroy_helper.128
- _block_destroy_helper.134
- _block_destroy_helper.15
- _block_destroy_helper.42
- _block_destroy_helper.51
- _block_destroy_helper.57
- _block_destroy_helper.63
- _block_destroy_helper.69
- _block_destroy_helper.75
- _block_destroy_helper.81
- _block_destroy_helper.9
- _block_destroy_helper.93
- _block_destroy_helper.99
- _objc_msgSend$_checkForPendingPurchaseIntents
- _objc_msgSend$_checkForPurchaseIntents
- _objc_msgSend$_notifyObserversAboutPurchaseIntentsForProducts:
- _objc_msgSend$_purchaseIntentObserverAdded
- _objc_msgSend$_purchaseIntentObserverRemoved
- _objc_msgSend$_showExtensionIfNeeded
- _objc_msgSend$addPurchaseIntent:reply:
- _objc_msgSend$bundleId
- _objc_msgSend$clearPurchaseIntentForProductIdentifier:
- _objc_msgSend$completionHandler
- _objc_msgSend$forceSandboxForBundleIdentifier:untilDate:reply:
- _objc_msgSend$purchaseIntentAppInstallSheetOpenForBundleIdentifier:reply:
- _objc_msgSend$purchaseIntentsForClient:clearOnRetrieval:reply:
- _objc_msgSend$receivedPurchaseIntentsForProductIdentifiers:
- _objc_msgSend$setHitTestsAsOpaque:
- _objc_msgSend$sharedDaemonConfig
- _objectdestroy.115Tm
- _objectdestroy.123Tm
- _objectdestroy.125Tm
- _objectdestroy.19Tm
- _objectdestroy.24Tm
- _objectdestroy.89Tm
- _symbolic _____ 15StoreKit_Shared14ClientOverrideV6ServerO10CodingKeys33_4ADCA8A4C6D34513C3587C3642BA7C7BLLO
- _symbolic _____ 15StoreKit_Shared14ClientOverrideV6ServerO19XcodeTestCodingKeys33_4ADCA8A4C6D34513C3587C3642BA7C7BLLO
- _symbolic _____ 8StoreKit14PurchaseIntentV0C7IntentsV0cE8ListenerC
- _symbolic _____yAAy_____y__________GGG s19AsyncFilterSequenceV s0a3MapC0V 8StoreKit11TransactionV12TransactionsV AG
- _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared14ClientOverrideV6ServerO10CodingKeys33_4ADCA8A4C6D34513C3587C3642BA7C7BLLO
- _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared14ClientOverrideV6ServerO17SandboxCodingKeys33_4ADCA8A4C6D34513C3587C3642BA7C7BLLO
- _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared14ClientOverrideV6ServerO19AutomaticCodingKeys33_4ADCA8A4C6D34513C3587C3642BA7C7BLLO
- _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared14ClientOverrideV6ServerO19XcodeTestCodingKeys33_4ADCA8A4C6D34513C3587C3642BA7C7BLLO
- _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared14ClientOverrideV6ServerO20ProductionCodingKeys33_4ADCA8A4C6D34513C3587C3642BA7C7BLLO
- _symbolic _____y_____G s22KeyedEncodingContainerV 15StoreKit_Shared14ClientOverrideV6ServerO10CodingKeys33_4ADCA8A4C6D34513C3587C3642BA7C7BLLO
- _symbolic _____y_____G s22KeyedEncodingContainerV 15StoreKit_Shared14ClientOverrideV6ServerO19XcodeTestCodingKeys33_4ADCA8A4C6D34513C3587C3642BA7C7BLLO
- _symbolic _____y______GSg ScS12ContinuationV 8StoreKit14PurchaseIntentV
- _symbolic _____y__________G s16AsyncMapSequenceV 8StoreKit11TransactionV12TransactionsV AE
- _symbolic _____y_____y__________GG s19AsyncFilterSequenceV s0a3MapC0V 8StoreKit11TransactionV12TransactionsV AG
- _symbolic _____y_____y_____y__________GG_G s19AsyncFilterSequenceV8IteratorV AB s0a3MapC0V 8StoreKit11TransactionV12TransactionsV AI
CStrings:
+ "\x01a"
+ "\nCurrently loading metadata for: "
+ "\x11\x14\x11"
+ "\x11\x1e"
+ " (cached data exists)"
+ " (total loading tasks: "
+ " IDs after sharing an existing collection observer."
+ " IDs because another task is loading the same IDs."
+ " IDs due to memory pressure"
+ " IDs is stale and will be reloaded. Data for "
+ " IDs.\nTask will load metadata for: "
+ " but there is nothing to clean up."
+ " cached product(s) for "
+ " cached products or subscription groups because there are no active observers."
+ " collection observers."
+ " in flight loading tasks"
+ " is purgable because there are no observers."
+ " is stale and will be freed."
+ " product IDs and "
+ " product or group IDs. Will create new task with ID "
+ " product(s) are cached, "
+ " product(s) are missing"
+ " product(s) are unavailable."
+ " subscription group IDs. Total products received: "
+ ", but there was no observer."
+ "/xcode\\[([^\\0]+)\\]/"
+ "@\"UIAlertController\""
+ "@60@0:8@16@24@32B40@44@52"
+ "Adding purchase intent continuation token "
+ "Adding purchase intent for product "
+ "Already waiting to load product metadata"
+ "Cache miss adding collection observer: "
+ "Checking if any cached data is stale because "
+ "Cleaned up task with ID "
+ "Creating new collection observer for "
+ "Creating new observer for "
+ "Creating purchase intent listener for "
+ "Creating purchase intent listener for Product"
+ "Error decoding response: "
+ "Error encoding request "
+ "Error in XPC call for force sandbox: "
+ "Exiting loading task because there are no resources to be loaded."
+ "Expected auto-renewable subscription, actual: "
+ "Failed to decode transaction for %{public}s, price field out of bounds: %{public}ld"
+ "Failed to get XPC remote object"
+ "Failed to load products with error: "
+ "Failed to set app install sheet bundleID "
+ "Finished loading metadata for "
+ "Finished loading metadata for group ID "
+ "Freeing data for "
+ "Handling memory pressure events"
+ "Handling storefront changes"
+ "Ignoring purchase intent check because no one is listening"
+ "Missing offer type"
+ "Missing offerID for offerType "
+ "No purchase intents"
+ "Notified individual observers "
+ "Observer removed for "
+ "OverrideService"
+ "Package"
+ "Product with ID "
+ "PurchaseIntentService"
+ "Removing purchase intent continuation token "
+ "Request failed with error "
+ "Request failed without an error"
+ "Requesting purchase intents after "
+ "Retrying request for "
+ "Server must be auto[matic], prod[uction], sandbox, or xcode[<configuration_file_path>]"
+ "Setting app install sheet bundleID ("
+ "Sharing existing collection observer for "
+ "Sharing existing observer for "
+ "Stopped handling memory pressure events"
+ "Stopped handling storefront changes"
+ "StoreKit_Private.SKInstallSheetStatusUpdateRequest"
+ "StoreKit_Private.SKPurchaseIntent"
+ "Subscription group with ID "
+ "T@\"NSString\",N,C"
+ "T@\"NSURL\",R,N,V_deepLinkURL"
+ "Task cancelled before all observers were updated."
+ "Task cancelled before collection and group observers were updated."
+ "Task cancelled before notifying collection observers of error."
+ "Task cancelled before notifying observers of error."
+ "Task cancelled before starting network request."
+ "Task cancelled before updating observers."
+ "Unable to display product ID."
+ "Waiting to load product metadata"
+ "Will load metadata for "
+ "Will not load metadata for "
+ "Will reload products due to storefront change"
+ "] Adding purchase intent listener"
+ "] Removing purchase intent listener"
+ "^/([a-z][a-z]/)?(app|app-bundle|album|movie|tv-season)([/?]|$)"
+ "_alertController"
+ "_deepLinkURL"
+ "_displayItemIfNeeded"
+ "_isInlineOfferUnsupported"
+ "_reportCompletionForInlineOfferUnsupported"
+ "addPurchaseIntentWithRequest:reply:"
+ "additionalBuyParams"
+ "appName"
+ "canOpenURL:"
+ "clearPurchaseIntentsWithRequest:reply:"
+ "clientOverridesWithReply:"
+ "context"
+ "currency"
+ "deepLinkURL"
+ "initWithResult:extensionID:productURL:isEntitled:parameters:deepLinkURL:"
+ "lastChecked"
+ "listenForPurchaseIntents"
+ "log"
+ "notifyPurchaseIntentObserversForProducts:"
+ "notifyToken"
+ "observer removed"
+ "offerDiscountType"
+ "openURL:options:completionHandler:"
+ "overrideServiceWithErrorHandler:"
+ "overrideSynchronousServiceWithErrorHandler:"
+ "productName"
+ "purchaseIntentServiceWithErrorHandler:"
+ "purchaseIntentsWithRequest:reply:"
+ "setAdditionalBuyParams:"
+ "setAppInstallSheetBundleID:reply:"
+ "setClientOverrideWithRequest:reply:"
+ "stopListeningForPurchaseIntents"
+ "v24@0:8@?<v@?@\"NSData\"@\"NSError\">16"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
+ "\xf0!"
- "\x01Q"
- "\x11\x13\x11"
- "\x11\x1d"
- "\x14"
- "%{public}@: Error in remote proxy while checking for purchase intents: %{public}@"
- "%{public}@: Error in remote proxy while clearing purchase intents: %{public}@"
- "%{public}@: Error in remote proxy while fetching purchase intents: %{public}@"
- "%{public}@: Error in remote proxy while forcing sandbox: %{public}@"
- "%{public}@: No observers found that respond to \"paymentQueue:shouldAddStorePayment:forProduct:\", will not check for purchase intents"
- "%{public}@: viewTapped."
- "@52@0:8@16@24@32B40@44"
- "Error in XPC connection while sending purchase intent %{public}@"
- "Error in connection while sending purchase intent %{public}@"
- "Error loading store products from purchase intent identifiers "
- "Expected auto-renewable subscription"
- "SKPurchaseIntentListenerProtocol"
- "Sending purchase intent install sheet open for bundle ID %{public}@"
- "StoreKit.PurchaseIntentsListener"
- "T@\"NSString\",R,N,V_bundleId"
- "T@?,C,N,V_completionHandler"
- "[SKPaymentQueue]: Tried to send purchase intent: %{public}@ to delegate, delegate does not respond to method paymentQueue:shouldAddStorePayment:forProduct"
- "^/([a-z][a-z]/)?(app|app-bundle|album|movie|tv-season|book|podcast|audiobook)([/?]|$)"
- "_TtCVV8StoreKit14PurchaseIntent15PurchaseIntents23PurchaseIntentsListener"
- "_appName"
- "_bundleId"
- "_checkForPendingPurchaseIntents"
- "_checkForPurchaseIntents"
- "_completionHandler"
- "_notifyObserversAboutPurchaseIntentsForProducts:"
- "_productIdentifer"
- "_productName"
- "_purchaseIntentObserverAdded"
- "_purchaseIntentObserverRemoved"
- "_showExtensionIfNeeded"
- "addPurchaseIntent:reply:"
- "clearPurchaseIntentForProductIdentifier:"
- "clearPurchaseIntentsForBundleIdentifier:"
- "forceSandboxForBundleIdentifier:untilDate:reply:"
- "initWithBundleId:productIdentifier:"
- "initWithResult:extensionID:productURL:isEntitled:parameters:"
- "purchaseIntent"
- "purchaseIntentAppInstallSheetOpenForBundleIdentifier:reply:"
- "purchaseIntentsForClient:clearOnRetrieval:reply:"
- "receivedPurchaseIntentsForProductIdentifiers:"
- "registerPurchaseIntentsListener:"
- "setClientOverrides:forBundleIdentifier:untilDate:reply:"
- "setCompletionHandler:"
- "setHitTestsAsOpaque:"
- "sharedDaemonConfig"
- "unregisterPurchaseIntentsListener:"
- "v32@0:8@\"NSDictionary\"16@?<v@?>24"
- "v32@0:8@\"NSString\"16@?<v@?>24"
- "v40@0:8@\"NSString\"16@\"NSDate\"24@?<v@?>32"
- "v48@0:8@\"NSDictionary\"16@\"NSString\"24@\"NSDate\"32@?<v@?@\"NSError\">40"
- "\xf0\x11"

```
