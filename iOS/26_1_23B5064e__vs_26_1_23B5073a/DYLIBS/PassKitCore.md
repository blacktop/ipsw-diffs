## PassKitCore

> `/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore`

```diff

-1642.2.4.0.0
-  __TEXT.__text: 0x7c4f04
+1642.2.9.5.0
+  __TEXT.__text: 0x7caccc
   __TEXT.__auth_stubs: 0x4a40
-  __TEXT.__objc_methlist: 0x6c798
-  __TEXT.__const: 0x23be8
-  __TEXT.__cstring: 0x68d33
-  __TEXT.__swift5_typeref: 0x594a
+  __TEXT.__objc_methlist: 0x6ca48
+  __TEXT.__const: 0x24898
+  __TEXT.__cstring: 0x68f24
+  __TEXT.__swift5_typeref: 0x5952
   __TEXT.__constg_swiftt: 0x4e34
-  __TEXT.__swift5_reflstr: 0x42dd
+  __TEXT.__swift5_reflstr: 0x42cd
   __TEXT.__swift5_fieldmd: 0x51cc
   __TEXT.__swift5_builtin: 0x3c0
   __TEXT.__swift5_assocty: 0x978
   __TEXT.__swift5_proto: 0xc94
   __TEXT.__swift5_types: 0x524
   __TEXT.__swift5_capture: 0x3ddc
-  __TEXT.__oslogstring: 0x34c87
+  __TEXT.__oslogstring: 0x34c89
   __TEXT.__swift_as_entry: 0xa8
   __TEXT.__swift_as_ret: 0xa8
   __TEXT.__swift5_protos: 0x40
   __TEXT.__swift5_mpenum: 0xf0
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x76a4
+  __TEXT.__gcc_except_tab: 0x76ac
   __TEXT.__ustring: 0x1e7a
-  __TEXT.__unwind_info: 0x1b880
+  __TEXT.__unwind_info: 0x1b980
   __TEXT.__eh_frame: 0x4b30
-  __TEXT.__objc_classname: 0xf8ef
-  __TEXT.__objc_methname: 0xcbdd2
-  __TEXT.__objc_methtype: 0x17941
-  __TEXT.__objc_stubs: 0x59e80
-  __DATA_CONST.__got: 0x49b0
-  __DATA_CONST.__const: 0x21178
-  __DATA_CONST.__objc_classlist: 0x3aa0
+  __TEXT.__objc_classname: 0xf957
+  __TEXT.__objc_methname: 0xcc32e
+  __TEXT.__objc_methtype: 0x179a0
+  __TEXT.__objc_stubs: 0x5a160
+  __DATA_CONST.__got: 0x49d0
+  __DATA_CONST.__const: 0x21328
+  __DATA_CONST.__objc_classlist: 0x3ab8
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_protolist: 0x590
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23378
+  __DATA_CONST.__objc_selrefs: 0x23470
   __DATA_CONST.__objc_protorefs: 0x250
-  __DATA_CONST.__objc_superrefs: 0x2f10
+  __DATA_CONST.__objc_superrefs: 0x2f28
   __DATA_CONST.__objc_arraydata: 0x27d8
   __AUTH_CONST.__auth_got: 0x2530
-  __AUTH_CONST.__const: 0x1e7f8
-  __AUTH_CONST.__cfstring: 0x71220
-  __AUTH_CONST.__objc_const: 0xc3c68
+  __AUTH_CONST.__const: 0x1e838
+  __AUTH_CONST.__cfstring: 0x71520
+  __AUTH_CONST.__objc_const: 0xc4018
   __AUTH_CONST.__objc_arrayobj: 0xd38
   __AUTH_CONST.__objc_intobj: 0x1080
   __AUTH_CONST.__objc_dictobj: 0x1518
   __AUTH_CONST.__objc_doubleobj: 0x2b0
-  __AUTH.__objc_data: 0x20588
+  __AUTH.__objc_data: 0x20678
   __AUTH.__data: 0x3768
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0x647c
+  __DATA.__objc_ivar: 0x648c
   __DATA.__data: 0x7d90
   __DATA.__bss: 0x18270
   __DATA.__common: 0xc00
-  __DATA_DIRTY.__objc_ivar: 0x25c8
+  __DATA_DIRTY.__objc_ivar: 0x25d8
   __DATA_DIRTY.__objc_data: 0x57a8
   __DATA_DIRTY.__data: 0x160
   __DATA_DIRTY.__bss: 0x1180

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 87C7ABF1-F3C0-3448-A787-1A728E33D3D4
-  Functions: 49553
-  Symbols:   128216
-  CStrings:  67396
+  UUID: DBDE4236-D8E0-3559-846A-E16664FDEA06
+  Functions: 49628
+  Symbols:   128410
+  CStrings:  67496
 
Symbols:
+ +[PKContinuityProximityNWAdvertisement supportsSecureCoding]
+ +[PKContinuityProximityNWVerification supportsSecureCoding]
+ +[PKDiagnostics _flightSubscriptions]
+ +[PKDiagnostics _recentFlights]
+ +[PKPassLiveDataConfiguration _defaultEligibleSemanticsForPassStyle:]
+ +[PKPassLiveDataConfiguration configurationForPassStyle:excludingSemantics:]
+ +[PKPassLiveDataConfiguration defaultConfigurationForPassStyle:]
+ +[PKPassLiveDataConfiguration supportsSecureCoding]
+ -[NSArray(PKArrayAdditions) pk_createSetBySafelyApplyingBlock:]
+ -[PKAirport asDictionary]
+ -[PKContinuityProximityNWAdvertisement .cxx_destruct]
+ -[PKContinuityProximityNWAdvertisement _dictionaryRepresentation]
+ -[PKContinuityProximityNWAdvertisement identifier]
+ -[PKContinuityProximityNWAdvertisement initWithDictionary:]
+ -[PKContinuityProximityNWAdvertisement initWithIdentifier:pin:]
+ -[PKContinuityProximityNWAdvertisement pin]
+ -[PKContinuityProximityNWVerification _dictionaryRepresentation]
+ -[PKContinuityProximityNWVerification initWithDictionary:]
+ -[PKContinuityProximityNWVerification init]
+ -[PKFlight asDictionary]
+ -[PKFlight initWithAirlineCode:airlineName:flightNumber:operatorAirlineCode:operatorFlightNumber:departure:arrival:state:publishedDate:staleDate:isEstimated:dataSource:]
+ -[PKFlight isEstimated]
+ -[PKFlight setEstimated:]
+ -[PKFlightStep asDictionary]
+ -[PKFlightSubscription asDictionary]
+ -[PKPass liveDataConfiguration]
+ -[PKPass setTrackBagsURL:]
+ -[PKPass trackBagsURL]
+ -[PKPassContent liveDataConfiguration]
+ -[PKPassContent setLiveDataConfiguration:]
+ -[PKPassField accessibilityLabel]
+ -[PKPassField accessibilityValue]
+ -[PKPassField setAccessibilityLabel:]
+ -[PKPassField setAccessibilityValue:]
+ -[PKPassLibrary flightSubscriptions]
+ -[PKPassLibrary flightsWithScheduledDepartureFromStartDate:endDate:]
+ -[PKPassLiveDataConfiguration .cxx_destruct]
+ -[PKPassLiveDataConfiguration _initWithEligibleSemantics:]
+ -[PKPassLiveDataConfiguration description]
+ -[PKPassLiveDataConfiguration eligibleSemantics]
+ -[PKPassLiveDataConfiguration encodeWithCoder:]
+ -[PKPassLiveDataConfiguration initWithCoder:]
+ -[PKPassLiveDataConfiguration supportsLiveDataForSemanticKey:]
+ -[PKPaymentPassAction _initWithBusinessChatIdentifier:]
+ -[PKPaymentPassAction businessChatIdentifier]
+ -[PKPaymentProvisioningController _filterFPANCredentials:forExistingCredentials:]
+ -[PKPaymentSetupFieldText secureTextVisibility]
+ -[PKPaymentSetupFieldText setSecureTextVisibility:]
+ -[PKPaymentSetupProduct provisioningMethodMetadataForMethod:]
+ -[PKPaymentSetupProduct setProvisioningMethodMetadata:forMethod:]
+ -[PKPaymentWebServiceConfiguration autofillForegroundEligibilityCheckMaxCount:]
+ -[PKPaymentWebServiceConfiguration provisioningProximityVerificationInSetupAssistantEnabledForRegion:]
+ -[PKSetupProductMethod identifier]
+ GCC_except_table122
+ GCC_except_table163
+ GCC_except_table184
+ GCC_except_table223
+ GCC_except_table243
+ GCC_except_table273
+ GCC_except_table275
+ GCC_except_table289
+ GCC_except_table301
+ GCC_except_table306
+ GCC_except_table307
+ GCC_except_table313
+ GCC_except_table318
+ GCC_except_table323
+ GCC_except_table342
+ GCC_except_table355
+ GCC_except_table369
+ GCC_except_table372
+ GCC_except_table393
+ GCC_except_table449
+ GCC_except_table454
+ GCC_except_table456
+ GCC_except_table459
+ GCC_except_table519
+ GCC_except_table527
+ GCC_except_table529
+ GCC_except_table544
+ GCC_except_table547
+ GCC_except_table550
+ GCC_except_table571
+ GCC_except_table664
+ GCC_except_table707
+ GCC_except_table715
+ _OBJC_CLASS_$_PKContinuityProximityNWAdvertisement
+ _OBJC_CLASS_$_PKContinuityProximityNWVerification
+ _OBJC_CLASS_$_PKPassLiveDataConfiguration
+ _OBJC_IVAR_$_PKFlight._estimated
+ _OBJC_IVAR_$_PKPassField._accessibilityLabel
+ _OBJC_IVAR_$_PKPassField._accessibilityValue
+ _OBJC_IVAR_$_PKPassLiveDataConfiguration._eligibleSemantics
+ _OBJC_IVAR_$_PKPaymentPassAction._businessChatIdentifier
+ _OBJC_METACLASS_$_PKContinuityProximityNWAdvertisement
+ _OBJC_METACLASS_$_PKContinuityProximityNWVerification
+ _OBJC_METACLASS_$_PKPassLiveDataConfiguration
+ _PKAccessibilityIdentifierArrivalInfo
+ _PKAccessibilityIdentifierDepartureInfo
+ _PKAnalyticsReportPaymentButtonRequest
+ _PKAnalyticsReportViewAppClipTag
+ _PKAnalyticsReportViewAppsNotOniPhoneTag
+ _PKAnalyticsReportViewAppsOniPhoneTag
+ _PKAnalyticsReportViewCommutePlanTag
+ _PKAnalyticsReportViewExistingCardTag
+ _PKAnalyticsReportViewNewCardTag
+ _PKAnalyticsReportViewSelectOtherProvidersTag
+ _PKPassKeyLiveDataConfiguration
+ _PKPassKeyLiveDataExcludedSemantics
+ _PKPassKeyTrackBagsURL
+ _PKPaymentFieldTextSecureTextVisibilityKey
+ _PKResolvedBoardingPassSemantics
+ __OBJC_$_CLASS_METHODS_PKContinuityProximityNWAdvertisement
+ __OBJC_$_CLASS_METHODS_PKContinuityProximityNWVerification
+ __OBJC_$_CLASS_METHODS_PKPassLiveDataConfiguration
+ __OBJC_$_CLASS_PROP_LIST_PKPassLiveDataConfiguration
+ __OBJC_$_INSTANCE_METHODS_PKContinuityProximityNWAdvertisement
+ __OBJC_$_INSTANCE_METHODS_PKContinuityProximityNWVerification
+ __OBJC_$_INSTANCE_METHODS_PKPassLiveDataConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_PKContinuityProximityNWAdvertisement
+ __OBJC_$_INSTANCE_VARIABLES_PKPassLiveDataConfiguration
+ __OBJC_$_PROP_LIST_PKContinuityProximityNWAdvertisement
+ __OBJC_$_PROP_LIST_PKPassLiveDataConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_PKPassLiveDataConfiguration
+ __OBJC_CLASS_RO_$_PKContinuityProximityNWAdvertisement
+ __OBJC_CLASS_RO_$_PKContinuityProximityNWVerification
+ __OBJC_CLASS_RO_$_PKPassLiveDataConfiguration
+ __OBJC_METACLASS_RO_$_PKContinuityProximityNWAdvertisement
+ __OBJC_METACLASS_RO_$_PKContinuityProximityNWVerification
+ __OBJC_METACLASS_RO_$_PKPassLiveDataConfiguration
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke.541
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_2.542
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_3.543
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_4.538
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_5.539
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_6.540
+ ___111-[PKPaymentProvisioningController resolveLocalEligibilityRequirementsForAppleBalanceCredential:withCompletion:]_block_invoke.574
+ ___111-[PKPaymentProvisioningController resolveLocalEligibilityRequirementsForAppleBalanceCredential:withCompletion:]_block_invoke.582
+ ___36-[PKPassLibrary flightSubscriptions]_block_invoke
+ ___59-[PKPaymentSetupProduct provisioningMethodMetadataForType:]_block_invoke
+ ___60-[PKPaymentProvisioningController _noteProvisioningDidBegin]_block_invoke.615
+ ___61-[PKPaymentProvisioningController retrieveRemoteCredentials:]_block_invoke.297
+ ___61-[PKPaymentProvisioningController retrieveRemoteCredentials:]_block_invoke.299
+ ___61-[PKPaymentProvisioningController retrieveRemoteCredentials:]_block_invoke_2.300
+ ___63-[PKPaymentSetupProduct setProvisioningMethodMetadata:forType:]_block_invoke
+ ___64-[PKPaymentProvisioningController performDeviceCheckInIfNeeded:]_block_invoke.288
+ ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.322
+ ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.329
+ ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.338
+ ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.346
+ ___68-[PKPassLibrary flightsWithScheduledDepartureFromStartDate:endDate:]_block_invoke
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke.259
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke.263
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke.269
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_2.264
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_2.270
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_3.275
+ ___70+[PKDiagnostics generateDiagnosticsPackageWithPassLibrary:completion:]_block_invoke.53
+ ___70-[PKPaymentProvisioningController deleteCredential:completionHandler:]_block_invoke.741
+ ___70-[PKPaymentProvisioningController deleteCredential:completionHandler:]_block_invoke.742
+ ___70-[PKPaymentProvisioningController deleteCredential:completionHandler:]_block_invoke.744
+ ___70-[PKPaymentProvisioningController deleteCredential:completionHandler:]_block_invoke.745
+ ___72-[PKPaymentProvisioningController _identityConfigurationWithCompletion:]_block_invoke.477
+ ___72-[PKPaymentProvisioningController _identityConfigurationWithCompletion:]_block_invoke.478
+ ___78-[PKPaymentProvisioningController _requestProvisioning:withCompletionHandler:]_block_invoke.647
+ ___78-[PKPaymentProvisioningController _requestProvisioning:withCompletionHandler:]_block_invoke_2.648
+ ___78-[PKPaymentProvisioningController _startLocationSearchWithTimeout:completion:]_block_invoke.673
+ ___78-[PKPaymentProvisioningController _startLocationSearchWithTimeout:completion:]_block_invoke.674
+ ___79-[PKPaymentProvisioningController _associateCredentials:withCompletionHandler:]_block_invoke.377
+ ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.403
+ ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.410
+ ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.419
+ ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.427
+ ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.431
+ ___80-[PKPaymentProvisioningController requestPurchasesForProduct:completionHandler:]_block_invoke.521
+ ___80-[PKPaymentProvisioningController requestPurchasesForProduct:completionHandler:]_block_invoke.524
+ ___81-[PKPaymentProvisioningController _filterFPANCredentials:forExistingCredentials:]_block_invoke
+ ___81-[PKPaymentProvisioningController _filterFPANCredentials:forExistingCredentials:]_block_invoke_2
+ ___81-[PKPaymentProvisioningController _filterFPANCredentials:forExistingCredentials:]_block_invoke_3
+ ___81-[PKPaymentProvisioningController _filterFPANCredentials:forExistingCredentials:]_block_invoke_4
+ ___85-[PKPaymentProvisioningController _setupAccountCredentialForProvisioning:completion:]_block_invoke.544
+ ___85-[PKPaymentProvisioningController _setupAccountCredentialForProvisioning:completion:]_block_invoke.546
+ ___85-[PKPaymentProvisioningController _setupAccountCredentialForProvisioning:completion:]_block_invoke_2.548
+ ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke.501
+ ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke.504
+ ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke_2.506
+ ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke_3.507
+ ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.449
+ ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.456
+ ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.460
+ ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.465
+ ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.469
+ ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke_2.470
+ ___91-[PKPaymentProvisioningController verifyPassIsSupportedForExpressInLocalMarket:completion:]_block_invoke.654
+ ___91-[PKPaymentProvisioningController verifyPassIsSupportedForExpressInLocalMarket:completion:]_block_invoke.657
+ ___91-[PKPaymentProvisioningController verifyPassIsSupportedForExpressInLocalMarket:completion:]_block_invoke.659
+ ___PKResolvedBoardingPassSemantics_block_invoke
+ ___block_descriptor_32_e33_B32?0"PKFPANCredential"8Q16^B24l
+ ___block_descriptor_40_e30_B16?0"PKSetupProductMethod"8l
+ ___block_descriptor_40_e8_32s_e33_B32?0"PKFPANCredential"8Q16^B24ls32l8
+ ___block_descriptor_72_e8_32s40bs48r56r64r_e17_v16?0"NSArray"8ls32l8r48l8s40l8r56l8r64l8
+ ___block_descriptor_72_e8_32s40bs48r56r64r_e5_v8?0ls32l8r48l8s40l8r56l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e50_v24?0"PKPaymentEligibilityResponse"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.1121
+ ___block_literal_global.1130
+ ___block_literal_global.1330
+ ___block_literal_global.1334
+ ___block_literal_global.1434
+ ___block_literal_global.1436
+ ___block_literal_global.1439
+ ___block_literal_global.1675
+ ___block_literal_global.1677
+ ___block_literal_global.1682
+ ___block_literal_global.1686
+ ___block_literal_global.1700
+ ___block_literal_global.1702
+ ___block_literal_global.1707
+ ___block_literal_global.1721
+ ___block_literal_global.1727
+ ___block_literal_global.1730
+ ___block_literal_global.1732
+ ___block_literal_global.1734
+ ___block_literal_global.1736
+ ___block_literal_global.1738
+ ___block_literal_global.1741
+ ___block_literal_global.341
+ ___block_literal_global.359
+ ___block_literal_global.362
+ ___block_literal_global.376
+ ___block_literal_global.482
+ ___block_literal_global.510
+ ___block_literal_global.718
+ ___block_literal_global.723
+ ___block_literal_global.733
+ ___block_literal_global.737
+ ___block_literal_global.740
+ ___block_literal_global.965
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ _objc_msgSend$_defaultEligibleSemanticsForPassStyle:
+ _objc_msgSend$_filterFPANCredentials:forExistingCredentials:
+ _objc_msgSend$_flightSubscriptions
+ _objc_msgSend$_initWithEligibleSemantics:
+ _objc_msgSend$_recentFlights
+ _objc_msgSend$autofillForegroundEligibilityCheckMaxCount:
+ _objc_msgSend$cardIsInWallet
+ _objc_msgSend$configurationForPassStyle:excludingSemantics:
+ _objc_msgSend$eligibleSemantics
+ _objc_msgSend$flight
+ _objc_msgSend$flightSubscriptions
+ _objc_msgSend$flightSubscriptionsWithCompletion:
+ _objc_msgSend$flightsWithScheduledDepartureFromStartDate:endDate:
+ _objc_msgSend$flightsWithScheduledDepartureFromStartDate:endDate:completion:
+ _objc_msgSend$gate
+ _objc_msgSend$liveDataConfiguration
+ _objc_msgSend$pk_createSetBySafelyApplyingBlock:
+ _objc_msgSend$provisioningMethodMetadataForMethod:
+ _objc_msgSend$setAccessibilityLabel:
+ _objc_msgSend$setAccessibilityValue:
+ _objc_msgSend$setLiveDataConfiguration:
+ _objc_msgSend$setProvisioningMethodMetadata:forMethod:
+ _objc_msgSend$setSecureTextVisibility:
+ _objc_msgSend$setTrackBagsURL:
+ _objc_msgSend$terminal
+ _symbolic _____Sg So33PKContinuityProximityVerifierTypeV
- -[PKFlight initWithAirlineCode:airlineName:flightNumber:operatorAirlineCode:operatorFlightNumber:departure:arrival:state:publishedDate:staleDate:dataSource:]
- -[PKFlight progress]
- GCC_except_table112
- GCC_except_table126
- GCC_except_table132
- GCC_except_table149
- GCC_except_table159
- GCC_except_table169
- GCC_except_table177
- GCC_except_table180
- GCC_except_table215
- GCC_except_table281
- GCC_except_table297
- GCC_except_table299
- GCC_except_table302
- GCC_except_table305
- GCC_except_table314
- GCC_except_table319
- GCC_except_table338
- GCC_except_table347
- GCC_except_table368
- GCC_except_table384
- GCC_except_table389
- GCC_except_table445
- GCC_except_table452
- GCC_except_table455
- GCC_except_table515
- GCC_except_table523
- GCC_except_table525
- GCC_except_table540
- GCC_except_table543
- GCC_except_table546
- GCC_except_table549
- GCC_except_table567
- GCC_except_table663
- GCC_except_table706
- GCC_except_table714
- _OBJC_IVAR_$_PKFlight._progress
- _PKSecureElementPassAccessType
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke.529
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_2.530
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_3.531
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_4.532
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_5.533
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_6.534
- ___111-[PKPaymentProvisioningController resolveLocalEligibilityRequirementsForAppleBalanceCredential:withCompletion:]_block_invoke.568
- ___111-[PKPaymentProvisioningController resolveLocalEligibilityRequirementsForAppleBalanceCredential:withCompletion:]_block_invoke.576
- ___60-[PKPaymentProvisioningController _noteProvisioningDidBegin]_block_invoke.609
- ___61-[PKPaymentProvisioningController retrieveRemoteCredentials:]_block_invoke.289
- ___61-[PKPaymentProvisioningController retrieveRemoteCredentials:]_block_invoke.291
- ___61-[PKPaymentProvisioningController retrieveRemoteCredentials:]_block_invoke_2.292
- ___64-[PKPaymentProvisioningController performDeviceCheckInIfNeeded:]_block_invoke.280
- ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.314
- ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.321
- ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.328
- ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.336
- ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.345
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke.261
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_2.256
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_2.262
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_3.267
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_6
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_7
- ___70+[PKDiagnostics generateDiagnosticsPackageWithPassLibrary:completion:]_block_invoke.47
- ___70-[PKPaymentProvisioningController deleteCredential:completionHandler:]_block_invoke.736
- ___70-[PKPaymentProvisioningController deleteCredential:completionHandler:]_block_invoke.737
- ___70-[PKPaymentProvisioningController deleteCredential:completionHandler:]_block_invoke.739
- ___70-[PKPaymentProvisioningController deleteCredential:completionHandler:]_block_invoke.740
- ___72-[PKPaymentProvisioningController _identityConfigurationWithCompletion:]_block_invoke.471
- ___72-[PKPaymentProvisioningController _identityConfigurationWithCompletion:]_block_invoke.472
- ___78-[PKPaymentProvisioningController _requestProvisioning:withCompletionHandler:]_block_invoke.641
- ___78-[PKPaymentProvisioningController _requestProvisioning:withCompletionHandler:]_block_invoke_2.642
- ___78-[PKPaymentProvisioningController _startLocationSearchWithTimeout:completion:]_block_invoke.667
- ___78-[PKPaymentProvisioningController _startLocationSearchWithTimeout:completion:]_block_invoke.668
- ___79-[PKPaymentProvisioningController _associateCredentials:withCompletionHandler:]_block_invoke.371
- ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.397
- ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.404
- ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.413
- ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.421
- ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.425
- ___80-[PKPaymentProvisioningController requestPurchasesForProduct:completionHandler:]_block_invoke.515
- ___80-[PKPaymentProvisioningController requestPurchasesForProduct:completionHandler:]_block_invoke.518
- ___85-[PKPaymentProvisioningController _setupAccountCredentialForProvisioning:completion:]_block_invoke.538
- ___85-[PKPaymentProvisioningController _setupAccountCredentialForProvisioning:completion:]_block_invoke.540
- ___85-[PKPaymentProvisioningController _setupAccountCredentialForProvisioning:completion:]_block_invoke_2.542
- ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke.495
- ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke.498
- ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke_2.500
- ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke_3.501
- ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.437
- ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.450
- ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.454
- ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.459
- ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.463
- ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke_2.464
- ___91-[PKPaymentProvisioningController verifyPassIsSupportedForExpressInLocalMarket:completion:]_block_invoke.647
- ___91-[PKPaymentProvisioningController verifyPassIsSupportedForExpressInLocalMarket:completion:]_block_invoke.648
- ___91-[PKPaymentProvisioningController verifyPassIsSupportedForExpressInLocalMarket:completion:]_block_invoke.651
- ___block_descriptor_64_e8_32s40s48r56r_e32_v28?0B8"NSError"12"NSArray"20lr48l8r56l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e50_v24?0"PKPaymentEligibilityResponse"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_literal_global.1117
- ___block_literal_global.1126
- ___block_literal_global.1324
- ___block_literal_global.1328
- ___block_literal_global.1433
- ___block_literal_global.1435
- ___block_literal_global.1438
- ___block_literal_global.1674
- ___block_literal_global.1676
- ___block_literal_global.1681
- ___block_literal_global.1685
- ___block_literal_global.1699
- ___block_literal_global.1701
- ___block_literal_global.1706
- ___block_literal_global.1720
- ___block_literal_global.1726
- ___block_literal_global.1729
- ___block_literal_global.1731
- ___block_literal_global.1733
- ___block_literal_global.1735
- ___block_literal_global.1737
- ___block_literal_global.1740
- ___block_literal_global.348
- ___block_literal_global.370
- ___block_literal_global.475
- ___block_literal_global.504
- ___block_literal_global.711
- ___block_literal_global.716
- ___block_literal_global.731
- ___block_literal_global.738
- ___block_literal_global.958
- ___swift_instantiateConcreteTypeFromMangledName
- ___swift_instantiateConcreteTypeFromMangledNameAbstract
- _objc_msgSend$retrieveSafariCredentials:
- _objc_msgSend$setProvisioningMethodMetadata:forType:
CStrings:
+ "@\"PKPassLiveDataConfiguration\""
+ "@108@0:8@16@24Q32@40Q48@56@64Q72@80@88B96Q100"
+ "B16@?0@\"PKSetupProductMethod\"8"
+ "B32@?0@\"PKFPANCredential\"8Q16^B24"
+ "NW"
+ "PKContinuityProximityNWAdvertisement"
+ "PKContinuityProximityNWVerification"
+ "PKPassLiveDataConfiguration"
+ "PKPaymentProvisioningController: Offers Catalog Fetch"
+ "ProximityVerificationInSetupAssistantEnabled"
+ "T@\"NSSet\",R,C,N,V_eligibleSemantics"
+ "T@\"NSString\",C,N,V_accessibilityLabel"
+ "T@\"NSString\",C,N,V_accessibilityValue"
+ "T@\"NSString\",R,N,V_businessChatIdentifier"
+ "T@\"NSString\",R,N,V_pin"
+ "T@\"NSURL\",C,N,V_trackBagsURL"
+ "T@\"PKPassLiveDataConfiguration\",&,N,V_liveDataConfiguration"
+ "TB,N,GisEstimated,V_estimated"
+ "TB,N,GisSecureVisibleText"
+ "TQ,N,V_secureTextVisibility"
+ "_accessibilityLabel"
+ "_accessibilityValue"
+ "_defaultEligibleSemanticsForPassStyle:"
+ "_eligibleSemantics"
+ "_estimated"
+ "_filterFPANCredentials:forExistingCredentials:"
+ "_flightSubscriptions"
+ "_initWithBusinessChatIdentifier:"
+ "_initWithEligibleSemantics:"
+ "_liveDataConfiguration"
+ "_recentFlights"
+ "_secureTextVisibility"
+ "_trackBagsURL"
+ "accessibilityLabel"
+ "accessibilityValue"
+ "appsNotOniPhone"
+ "appsOniPhone"
+ "arrival-info"
+ "autofillForegroundEligibilityCheckMaxCount"
+ "autofillForegroundEligibilityCheckMaxCount:"
+ "commutePlan"
+ "configurationForPassStyle:excludingSemantics:"
+ "defaultConfigurationForPassStyle:"
+ "departure-info"
+ "eligibleSemantics"
+ "eligibleSemantics: '%@'; "
+ "estimated"
+ "excludedSemantics"
+ "existingCard"
+ "flightSubscriptions"
+ "flightSubscriptionsWithCompletion:"
+ "flights"
+ "flightsWithScheduledDepartureFromStartDate:endDate:"
+ "flightsWithScheduledDepartureFromStartDate:endDate:completion:"
+ "initWithAirlineCode:airlineName:flightNumber:operatorAirlineCode:operatorFlightNumber:departure:arrival:state:publishedDate:staleDate:isEstimated:dataSource:"
+ "initWithIdentifier:pin:"
+ "isEstimated"
+ "isEstimated: '%d'; "
+ "liveDataConfiguration"
+ "offers_catalog"
+ "pk_createSetBySafelyApplyingBlock:"
+ "provisioning:preflight:offers_catalog"
+ "provisioningMethodMetadataForMethod:"
+ "provisioningProximityVerificationInSetupAssistantEnabledForRegion:"
+ "proximityVerificationType"
+ "reveal"
+ "secureTextVisibility"
+ "selectOtherProviders"
+ "service:account:inviteDroppedForSessionID:fromID:context:error:"
+ "setAccessibilityLabel:"
+ "setAccessibilityValue:"
+ "setEstimated:"
+ "setLiveDataConfiguration:"
+ "setProvisioningMethodMetadata:forMethod:"
+ "setSecureTextVisibility:"
+ "setTrackBagsURL:"
+ "short_reveal"
+ "supportsLiveDataForSemanticKey:"
+ "trackBagsURL"
+ "v40@0:8@\"NSDate\"16@\"NSDate\"24@?<v@?@\"NSArray\">32"
+ "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSData\"48@\"NSError\"56"
- "@104@0:8@16@24Q32@40Q48@56@64Q72@80@88Q96"
- "PKPaymentProvisioningController: Safari credentials"
- "TB,N,GisSecureVisibleText,V_secureVisibleText"
- "Td,R,N,V_progress"
- "_progress"
- "_secureVisibleText"
- "initWithAirlineCode:airlineName:flightNumber:operatorAirlineCode:operatorFlightNumber:departure:arrival:state:publishedDate:staleDate:dataSource:"
- "performProximityVerification"
- "provisioning:preflight:safari_creds"
- "safari_creds"
- "service:account:inviteDroppedForSessionID:fromID:error:"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48"

```
