## PassKitCore

> `/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore`

```diff

-1629.6.0.0.0
-  __TEXT.__text: 0x7bc008
-  __TEXT.__auth_stubs: 0x49d0
-  __TEXT.__objc_methlist: 0x6c240
-  __TEXT.__const: 0x23ac8
-  __TEXT.__cstring: 0x68a9b
-  __TEXT.__swift5_typeref: 0x58c4
-  __TEXT.__constg_swiftt: 0x4d74
-  __TEXT.__swift5_reflstr: 0x41ed
-  __TEXT.__swift5_fieldmd: 0x5104
+1632.1.4.0.0
+  __TEXT.__text: 0x7c032c
+  __TEXT.__auth_stubs: 0x4a10
+  __TEXT.__objc_methlist: 0x6c430
+  __TEXT.__const: 0x23a68
+  __TEXT.__cstring: 0x687a0
+  __TEXT.__swift5_typeref: 0x5926
+  __TEXT.__constg_swiftt: 0x4d8c
+  __TEXT.__swift5_reflstr: 0x429d
+  __TEXT.__swift5_fieldmd: 0x517c
   __TEXT.__swift5_builtin: 0x3c0
   __TEXT.__swift5_assocty: 0x960
   __TEXT.__swift5_proto: 0xc80
   __TEXT.__swift5_types: 0x51c
-  __TEXT.__swift5_capture: 0x3d7c
-  __TEXT.__oslogstring: 0x3480f
+  __TEXT.__swift5_capture: 0x3dbc
+  __TEXT.__oslogstring: 0x34990
   __TEXT.__swift_as_entry: 0xa0
   __TEXT.__swift_as_ret: 0xa8
   __TEXT.__swift5_protos: 0x40
   __TEXT.__swift5_mpenum: 0xf0
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x7620
+  __TEXT.__gcc_except_tab: 0x7640
   __TEXT.__ustring: 0x1e7a
-  __TEXT.__unwind_info: 0x1b628
+  __TEXT.__unwind_info: 0x1b6f0
   __TEXT.__eh_frame: 0x49f0
-  __TEXT.__objc_classname: 0xf878
-  __TEXT.__objc_methname: 0xcb205
-  __TEXT.__objc_methtype: 0x175f3
-  __TEXT.__objc_stubs: 0x5a0e0
-  __DATA_CONST.__got: 0x4978
-  __DATA_CONST.__const: 0x20fa0
+  __TEXT.__objc_classname: 0xf886
+  __TEXT.__objc_methname: 0xcb585
+  __TEXT.__objc_methtype: 0x176d6
+  __TEXT.__objc_stubs: 0x59ba0
+  __DATA_CONST.__got: 0x4988
+  __DATA_CONST.__const: 0x21110
   __DATA_CONST.__objc_classlist: 0x3a80
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_protolist: 0x590
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x232c8
+  __DATA_CONST.__objc_selrefs: 0x23258
   __DATA_CONST.__objc_protorefs: 0x250
   __DATA_CONST.__objc_superrefs: 0x2f00
-  __DATA_CONST.__objc_arraydata: 0x26e8
-  __AUTH_CONST.__auth_got: 0x24f8
-  __AUTH_CONST.__const: 0x1e558
-  __AUTH_CONST.__cfstring: 0x70de0
-  __AUTH_CONST.__objc_const: 0xc34d0
-  __AUTH_CONST.__objc_arrayobj: 0xc90
+  __DATA_CONST.__objc_arraydata: 0x2700
+  __AUTH_CONST.__auth_got: 0x2518
+  __AUTH_CONST.__const: 0x1e668
+  __AUTH_CONST.__cfstring: 0x70d60
+  __AUTH_CONST.__objc_const: 0xc3760
+  __AUTH_CONST.__objc_arrayobj: 0xcd8
   __AUTH_CONST.__objc_intobj: 0x1068
   __AUTH_CONST.__objc_dictobj: 0x1540
   __AUTH_CONST.__objc_doubleobj: 0x2b0
-  __AUTH.__objc_data: 0x204b0
-  __AUTH.__data: 0x3628
+  __AUTH.__objc_data: 0x204d8
+  __AUTH.__data: 0x3638
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0x6430
-  __DATA.__data: 0x7cf0
-  __DATA.__bss: 0x18498
+  __DATA.__objc_ivar: 0x645c
+  __DATA.__data: 0x7d30
+  __DATA.__bss: 0x184a8
   __DATA.__common: 0xc00
-  __DATA_DIRTY.__objc_ivar: 0x25c0
+  __DATA_DIRTY.__objc_ivar: 0x25c8
   __DATA_DIRTY.__objc_data: 0x57a8
   __DATA_DIRTY.__data: 0x160
   __DATA_DIRTY.__bss: 0xcc0

   - /System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting
+  - /System/Library/PrivateFrameworks/RenderBox.framework/RenderBox
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SEService.framework/SEService
   - /System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 89EB870F-4F47-3338-9DFB-53DF9C809991
-  Functions: 49353
-  Symbols:   127879
-  CStrings:  67234
+  UUID: 748F44BD-B4FE-3A17-B0F8-5CE206823E28
+  Functions: 49430
+  Symbols:   127998
+  CStrings:  67238
 
Symbols:
+ +[PKIdentityPassCredentialProperty supportsSecureCoding]
+ +[PKPaymentHeroImageManifest manifestFileForRegion:planningToWrite:]
+ +[PKRemotePaymentInstrument(Caching) thumbnailCachePathForManifestHash:size:planningToWrite:]
+ +[PKTCCCoordinator authorizationStatusForCapability:]
+ +[PKTCCCoordinator authorizationStatusForCapability:auditToken:]
+ +[PKTCCCoordinator requestAuthorizationForCapability:completion:]
+ -[PKAccountService accountWithIdentifier:error:]
+ -[PKAddCarKeyPassConfiguration manufacturerOrIssuerIdentifier]
+ -[PKAutoFillCardManager fpanDescriptorAndCredentialForFPAN:descriptor:credential:error:]
+ -[PKDashboardTransactionFetcher filterOutAccountStates:]
+ -[PKDashboardTransactionFetcher filterOutPeerPaymentAccountStates:]
+ -[PKDiscoveryCard backgroundColor]
+ -[PKFlight initWithAirlineCode:airlineName:flightNumber:operatorAirlineCode:operatorFlightNumber:departure:arrival:state:publishedDate:staleDate:dataSource:]
+ -[PKFlight progress]
+ -[PKIdentityPassCredentialProperty .cxx_destruct]
+ -[PKIdentityPassCredentialProperty applicationIdentifier]
+ -[PKIdentityPassCredentialProperty copyWithZone:]
+ -[PKIdentityPassCredentialProperty docType]
+ -[PKIdentityPassCredentialProperty encodeWithCoder:]
+ -[PKIdentityPassCredentialProperty hash]
+ -[PKIdentityPassCredentialProperty initWithCoder:]
+ -[PKIdentityPassCredentialProperty initWithPassUniqueIdentifier:applicationIdentifier:subCredentialIdentifier:]
+ -[PKIdentityPassCredentialProperty initWithPassUniqueIdentifier:applicationIdentifier:subCredentialIdentifier:docType:]
+ -[PKIdentityPassCredentialProperty isEqual:]
+ -[PKIdentityPassCredentialProperty isEqualToPKIdentityPassCredentialProperty:]
+ -[PKIdentityPassCredentialProperty passUniqueIdentifier]
+ -[PKIdentityPassCredentialProperty setApplicationIdentifier:]
+ -[PKIdentityPassCredentialProperty setDocType:]
+ -[PKIdentityPassCredentialProperty setPassUniqueIdentifier:]
+ -[PKIdentityPassCredentialProperty setSubCredentialIdentifier:]
+ -[PKIdentityPassCredentialProperty subCredentialIdentifier]
+ -[PKPassAuxiliaryPassInformationItem _displayableStringForDate:fromField:]
+ -[PKPassLibrary overrideStateOfRelevancyPresentmentOfType:containingPassUniqueIdentifier:newState:completion:]
+ -[PKPassLibrary stateOfRelevancyPresentmentOfType:containingPassUniqueIdentifier:]
+ -[PKPassRelevancyModel isRelevancyActive]
+ -[PKPaymentDefaultDataProvider transactionCountForRequest:completion:]
+ -[PKPaymentOffersController _markOfferConsumedForPassUniqueID:criteriaIdentifier:]
+ -[PKPaymentService transactionCountForRequest:completion:]
+ -[PKPaymentService(FPAN) fpanDescriptorAndCredentialForFPAN:descriptor:credential:error:]
+ -[PKPaymentService(PaymentOffers) updatePaymentOfferCatalogVersion:shouldRemove:]
+ -[PKPaymentSetupFeature _initWithWebKitPropertyListData:]
+ -[PKPaymentSetupFeature _webKitPropertyListData]
+ -[PKPaymentSetupFieldsModel prefillValuesWithFPAN:targetDevice:]
+ -[PKPaymentTransaction(FinanceKit) _fkPaymentTransactionCategory]
+ -[PKPaymentTransactionRequest excludedAccountStates]
+ -[PKPaymentTransactionRequest excludedPeerPaymentAccountStates]
+ -[PKPaymentTransactionRequest setExcludedAccountStates:]
+ -[PKPaymentTransactionRequest setExcludedPeerPaymentAccountStates:]
+ -[PKPaymentWebServiceConfiguration paymentOfferCatalogVersionChangeUpdatePeriodForRegion:]
+ -[PKPaymentWebServiceConfiguration paymentOfferCatalogVersionForRegion:]
+ -[PKPaymentWebServiceLocalProxyTargetDevice fpanDescriptorAndCredentialForFPAN:descriptor:credential:error:]
+ -[PKPaymentWebServiceRemoteProxyTargetDevice fpanDescriptorAndCredentialForFPAN:completion:]
+ -[PKPaymentWebServiceTargetDevice fpanDescriptorAndCredentialForFPAN:descriptor:credential:error:]
+ -[PKProtobufFlightShareMessage backgroundColor]
+ -[PKProtobufFlightShareMessage foregroundColor]
+ -[PKProtobufFlightShareMessage hasBackgroundColor]
+ -[PKProtobufFlightShareMessage hasForegroundColor]
+ -[PKProtobufFlightShareMessage setBackgroundColor:]
+ -[PKProtobufFlightShareMessage setForegroundColor:]
+ -[PKSeatingInformation(Flight) _displayableAirlineSeatsStringForRow:designations:]
+ -[PKSeatingInformation(Flight) _formatSeatLettersForRow:designations:includeSpaceBetweenRowAndSeats:]
+ -[PKSeatingInformation(Flight) _formatSeatNumbersForRow:designations:formatter:includeSpaceBetweenRowAndSeats:]
+ -[PKSeatingInformation(Flight) _formattedAirlineSeatsStringForRow:designation:includeSpaceBetweenRowAndSeats:]
+ -[PKSeatingInformation(Flight) _isStringAllLetters:]
+ -[PKSeatingInformation(Flight) _isStringAllNumbers:formatter:]
+ -[PKSecureElement _setIsInRestrictedMode:]
+ GCC_except_table107
+ GCC_except_table112
+ GCC_except_table129
+ GCC_except_table135
+ GCC_except_table201
+ GCC_except_table231
+ GCC_except_table234
+ GCC_except_table251
+ GCC_except_table254
+ GCC_except_table260
+ GCC_except_table269
+ GCC_except_table272
+ GCC_except_table311
+ GCC_except_table327
+ GCC_except_table330
+ GCC_except_table335
+ GCC_except_table359
+ GCC_except_table405
+ GCC_except_table407
+ GCC_except_table414
+ GCC_except_table416
+ GCC_except_table425
+ GCC_except_table441
+ GCC_except_table470
+ GCC_except_table521
+ GCC_except_table531
+ GCC_except_table662
+ GCC_except_table705
+ GCC_except_table713
+ GCC_except_table733
+ GCC_except_table851
+ GCC_except_table88
+ GCC_except_table98
+ _NSURLFileProtectionCompleteUntilFirstUserAuthentication
+ _NSURLFileProtectionKey
+ _NSURLFileProtectionNone
+ _OBJC_CLASS_$_PKIdentityPassCredentialProperty
+ _OBJC_CLASS_$_RBDevice
+ _OBJC_IVAR_$_PKDashboardTransactionFetcher._excludedAccountStates
+ _OBJC_IVAR_$_PKDashboardTransactionFetcher._excludedPeerPaymentAccountStates
+ _OBJC_IVAR_$_PKDiscoveryCard._backgroundColor
+ _OBJC_IVAR_$_PKFlight._progress
+ _OBJC_IVAR_$_PKIdentityPassCredentialProperty._applicationIdentifier
+ _OBJC_IVAR_$_PKIdentityPassCredentialProperty._docType
+ _OBJC_IVAR_$_PKIdentityPassCredentialProperty._passUniqueIdentifier
+ _OBJC_IVAR_$_PKIdentityPassCredentialProperty._subCredentialIdentifier
+ _OBJC_IVAR_$_PKPaymentTransactionRequest._excludedAccountStates
+ _OBJC_IVAR_$_PKPaymentTransactionRequest._excludedPeerPaymentAccountStates
+ _OBJC_IVAR_$_PKSecureElement._isInRestrictedMode
+ _OBJC_IVAR_$_PKSecureElement._isInRestrictedModeTimestamp
+ _OBJC_IVAR_$_PKSecureElement._lock
+ _OBJC_IVAR_$_PKSecureElement._updatingIsInRestrictedMode
+ _OBJC_METACLASS_$_PKIdentityPassCredentialProperty
+ _PKAnalyticsReportApplePayDemoAuthenticationFailedTag
+ _PKAnalyticsReportApplePayDemoCompleteTag
+ _PKAnalyticsReportApplePayDemoCompletedWithinKey
+ _PKAnalyticsReportApplePayDemoDismissButtonTag
+ _PKAnalyticsReportApplePayDemoEndButtonTag
+ _PKAnalyticsReportApplePayDemoHoldNearReaderTag
+ _PKAnalyticsReportApplePayDemoInstructionsTag
+ _PKAnalyticsReportApplePayDemoPayWithPasscodeButtonTag
+ _PKAnalyticsReportApplePayDemoPracticeAgainButtonTag
+ _PKAnalyticsReportApplePayDemoRequestingAuthenticationTag
+ _PKAnalyticsReportApplePayDemoSourceKey
+ _PKAnalyticsReportApplePayDemoStartButtonTag
+ _PKAnalyticsReportApplePayDemoUserIntentTag
+ _PKAnalyticsReportEligibleForSmartButtonKey
+ _PKAnalyticsReportHasContactlessTransactionWithinKey
+ _PKAnalyticsReportHasPaymentPassKey
+ _PKAnalyticsReportMerchantTokenDetailsRevokeAlertPageTag
+ _PKAnalyticsReportMorePreferencesPageTag
+ _PKAnalyticsReportPreauthorizedMerchantTokenCountKey
+ _PKAnalyticsReportPreauthorizedPaymentsButtonTag
+ _PKAnalyticsReportRevokePaymentButtonTag
+ _PKAutoFillCredentialImageNameForType
+ _PKImageForAutoFillCredentialType
+ _PKLiveActivityAttributesTypeFromString
+ _PKLiveActivityAttributesTypeToString
+ _PKMapsSnapshotsCacheCreateFileURLForWriting
+ _PKMapsSnapshotsCacheCreateFileURLReadOnly
+ _PKPassAssetDownloadCacheCreateFileURLForWriting
+ _PKPassAssetDownloadCacheCreateFileURLReadOnly
+ _PKPassLibraryRelevantInfoSuppressLAAutoStart
+ _PKPassRelevancySystemPresentmentStateFromString
+ _PKPassRelevancySystemPresentmentStateToString
+ _PKRemoteInstrumentThumbnailsCacheCreateFileURLForWriting
+ _PKRemoteInstrumentThumbnailsCacheCreateFileURLReadOnly
+ _PKSeatingInformationNumberFormatter
+ _PKSharedCacheCreateFileURLForWriting
+ _PKSharedCacheCreateFileURLReadOnly
+ _PKVerifyOrUpdateDirectoryFileProtection
+ _TCCAccessPreflight
+ _TCCAccessPreflightWithAuditToken
+ _TCCAccessRequest
+ __FixSharedCacheFileProtection.onceToken
+ __MergedGlobals.27
+ __MergedGlobals.32
+ __MergedGlobals.33
+ __OBJC_$_CLASS_METHODS_PKIdentityPassCredentialProperty
+ __OBJC_$_CLASS_PROP_LIST_PKIdentityPassCredentialProperty
+ __OBJC_$_INSTANCE_METHODS_PKIdentityPassCredentialProperty
+ __OBJC_$_INSTANCE_VARIABLES_PKIdentityPassCredentialProperty
+ __OBJC_$_PROP_LIST_PKIdentityPassCredentialProperty
+ __OBJC_CLASS_PROTOCOLS_$_PKIdentityPassCredentialProperty
+ __OBJC_CLASS_RO_$_PKIdentityPassCredentialProperty
+ __OBJC_METACLASS_RO_$_PKIdentityPassCredentialProperty
+ __Z17PKShortDateStringP6NSDateP10NSTimeZone
+ ___100-[PKPaymentService submitUserConfirmation:forTransactionIdentifier:sessionExchangeToken:completion:]_block_invoke.321
+ ___101-[PKSeatingInformation(Flight) _formatSeatLettersForRow:designations:includeSpaceBetweenRowAndSeats:]_block_invoke
+ ___102-[PKPaymentService recordPaymentApplicationUsageForPassUniqueIdentifier:paymentApplicationIdentifier:]_block_invoke.244
+ ___103-[PKPaymentService submitTransactionSignatureForTransactionIdentifier:sessionExchangeToken:completion:]_block_invoke.324
+ ___104-[PKSecureElement createAliroHomeKeyWithReaderIdentifier:readerPublicKey:homeIdentifier:withCompletion:]_block_invoke.309
+ ___106-[PKPaymentService submitBarcodePaymentEvent:forPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.326
+ ___107-[PKPaymentService registerAuxiliaryCapabilityForPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.308
+ ___107-[PKPaymentService retrieveDecryptedBarcodeCredentialForPassUniqueIdentifier:authorization:withCompletion:]_block_invoke.312
+ ___108-[PKPaymentWebServiceLocalProxyTargetDevice fpanDescriptorAndCredentialForFPAN:descriptor:credential:error:]_block_invoke
+ ___109-[PKPaymentService conflictingExpressPassIdentifiersForPassInformation:withReferenceExpressState:completion:]_block_invoke.233
+ ___110-[PKPassLibrary overrideStateOfRelevancyPresentmentOfType:containingPassUniqueIdentifier:newState:completion:]_block_invoke
+ ___110-[PKPassLibrary overrideStateOfRelevancyPresentmentOfType:containingPassUniqueIdentifier:newState:completion:]_block_invoke.269
+ ___111-[PKPaymentService conflictingExpressPassIdentifiersForPassConfiguration:withReferenceExpressState:completion:]_block_invoke.232
+ ___111-[PKSeatingInformation(Flight) _formatSeatNumbersForRow:designations:formatter:includeSpaceBetweenRowAndSeats:]_block_invoke
+ ___112-[PKPaymentService retrievePINEncryptionCertificateForPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.316
+ ___115-[PKPaymentService passUniqueIdentifierForTransactionWithServiceIdentifier:transactionSourceIdentifier:completion:]_block_invoke.179
+ ___115-[PKPaymentWebService backgroundDownloadRemotePassAssets:forSuffixesAndScreenScales:cloudStoreCoordinatorDelegate:]_block_invoke.725
+ ___115-[PKPaymentWebService backgroundDownloadRemotePassAssets:forSuffixesAndScreenScales:cloudStoreCoordinatorDelegate:]_block_invoke.728
+ ___115-[PKPaymentWebService backgroundDownloadRemotePassAssets:forSuffixesAndScreenScales:cloudStoreCoordinatorDelegate:]_block_invoke.732
+ ___115-[PKPaymentWebService backgroundDownloadRemotePassAssets:forSuffixesAndScreenScales:cloudStoreCoordinatorDelegate:]_block_invoke.734
+ ___115-[PKPaymentWebService backgroundDownloadRemotePassAssets:forSuffixesAndScreenScales:cloudStoreCoordinatorDelegate:]_block_invoke_2.735
+ ___117-[PKPaymentService insertOrUpdateValueAddedServiceTransaction:forPassUniqueIdentifier:paymentTransaction:completion:]_block_invoke.211
+ ___128-[PKPaymentService retrieveDecryptedBarcodeCredentialForPassUniqueIdentifier:authorization:sessionExchangeToken:withCompletion:]_block_invoke.314
+ ___130-[PKPaymentWebService _passActionGroupIncludingAppletDataWithRemoteContentPassActionGroup:forPass:forDeviceIdentifier:completion:]_block_invoke.768
+ ___140-[PKPaymentService rangingSuspensionReasonForAppletSubcredentialIdentifier:paymentApplicationIdentifier:secureElementIdentifier:completion:]_block_invoke.287
+ ___149-[PKPaymentService processTransitTransactionEventWithHistory:transactionDate:forPaymentApplication:withPassUniqueIdentifier:expressTransactionState:]_block_invoke.243
+ ___36-[PKPaymentService consistencyCheck]_block_invoke.261
+ ___37-[PKSecureElement isInRestrictedMode]_block_invoke
+ ___43-[PKPaymentService productsWithCompletion:]_block_invoke.356
+ ___44-[PKPaymentService initializeSecureElement:]_block_invoke.221
+ ___45-[PKPaymentService insertUserLegalAgreement:]_block_invoke.399
+ ___48-[PKAccountService accountWithIdentifier:error:]_block_invoke
+ ___48-[PKPaymentService mapsMerchantsWithCompletion:]_block_invoke.182
+ ___48-[PKSecureElement SEPPairingInfoWithCompletion:]_block_invoke.262
+ ___49-[PKPaymentService currentSecureElementSnapshot:]_block_invoke.387
+ ___49-[PKPaymentService deleteReservation:completion:]_block_invoke.391
+ ___50-[PKPaymentService sharedPaymentWebServiceContext]_block_invoke.280
+ ___50-[PKPaymentService submitApplyRequest:completion:]_block_invoke.344
+ ___50-[PKPaymentService submitTermsRequest:completion:]_block_invoke.348
+ ___51-[PKPaymentService logoImageDataForURL:completion:]_block_invoke.175
+ ___51-[PKPaymentService productsWithRequest:completion:]_block_invoke.354
+ ___51-[PKPaymentService submitDeleteRequest:completion:]_block_invoke.349
+ ___51-[PKSecureElement appletWithIdentifier:completion:]_block_invoke.275
+ ___52-[PKSecureElement signatureForAuthToken:completion:]_block_invoke.303
+ ___52-[PKSecureElement signedPlatformDataWithCompletion:]_block_invoke.306
+ ___53-[PKPaymentService submitDocumentRequest:completion:]_block_invoke.346
+ ___54-[PKPaymentService featureApplicationsWithCompletion:]_block_invoke.342
+ ___54-[PKPaymentService regionsWithIdentifiers:completion:]_block_invoke.290
+ ___55-[PKPaymentService performDeviceCheckInWithCompletion:]_block_invoke.353
+ ___55-[PKPaymentService pushProvisioningSharingIdentifiers:]_block_invoke.374
+ ___55-[PKSecureElement appletCredentialsForAIDs:completion:]_block_invoke.269
+ ___56-[PKPaymentService credentialWithIdentifier:completion:]_block_invoke.370
+ ___57-[PKPaymentService regionsMatchingName:types:completion:]_block_invoke.291
+ ___57-[PKPaymentService submitVerificationRequest:completion:]_block_invoke.347
+ ___58-[PKPaymentService familyMembersIgnoringCache:completion:]_block_invoke.327
+ ___58-[PKPaymentService transactionCountForRequest:completion:]_block_invoke
+ ___58-[PKPaymentService transactionCountForRequest:completion:]_block_invoke.171
+ ___58-[PKPaymentService transactionCountForRequest:completion:]_block_invoke_2
+ ___58-[PKSecureElement allAppletsAndCredentialsWithCompletion:]_block_invoke.265
+ ___59-[PKPaymentService memberTypeForCurrentUserWithCompletion:]_block_invoke.328
+ ___59-[PKPaymentService performProductActionRequest:completion:]_block_invoke.357
+ ___59-[PKPaymentService requiresUpgradedPasscodeWithCompletion:]_block_invoke.306
+ ___59-[PKPaymentService storeTransactionReceiptData:completion:]_block_invoke.395
+ ___59-[PKPaymentService subcredentialInvitationsWithCompletion:]_block_invoke.364
+ ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke.874
+ ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke.880
+ ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke.882
+ ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke.888
+ ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke_2.877
+ ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke_2.881
+ ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke_2.885
+ ___61-[PKPaymentService changePasscodeFrom:toPasscode:completion:]_block_invoke.307
+ ___61-[PKPaymentService statusForShareableCredentials:completion:]_block_invoke.377
+ ___62-[PKPaymentService addRemoteDevicePendingProvisioningReceipt:]_block_invoke.295
+ ___62-[PKPaymentService generateUnderlyingKeyReportWithCompletion:]_block_invoke.301
+ ___62-[PKPaymentService transactionReceiptWithUniqueID:completion:]_block_invoke.392
+ ___62-[PKPaymentService transactionsForPredicate:limit:completion:]_block_invoke.177
+ ___62-[PKPaymentService(FPAN) cachedFPANCredentialsWithCompletion:]_block_invoke.55
+ ___63-[PKPaymentService currentPasscodeMeetsUpgradedPasscodePolicy:]_block_invoke.305
+ ___63-[PKPaymentService photosForFamilyMembersWithDSIDs:completion:]_block_invoke.331
+ ___63-[PKPaymentService refreshMerchantTokenMetadataWithCompletion:]_block_invoke.293
+ ___63-[PKPaymentService removeExpressPassesWithCardType:completion:]_block_invoke.237
+ ___63-[PKPaymentWebService _nonceWithRequest:serviceURL:completion:]_block_invoke.814
+ ___64-[PKPaymentService enforceUpgradedPasscodePolicyWithCompletion:]_block_invoke.304
+ ___64-[PKPaymentService featureApplicationWithIdentifier:completion:]_block_invoke.343
+ ___64-[PKPaymentService passOwnershipTokenWithIdentifier:completion:]_block_invoke.358
+ ___64-[PKPaymentService redeemPaymentShareableCredential:completion:]_block_invoke.383
+ ___64-[PKPaymentService revokeCredentialsWithIdentifiers:completion:]_block_invoke.368
+ ___64-[PKPaymentWebServiceLocalProxyTargetDevice initWithConnection:]_block_invoke.294
+ ___65+[PKTCCCoordinator requestAuthorizationForCapability:completion:]_block_invoke
+ ___65+[PKTCCCoordinator requestAuthorizationForCapability:completion:]_block_invoke_2
+ ___65-[PKAutoFillCardManager userDidUseCardWithDescriptor:credential:]_block_invoke.63
+ ___65-[PKPaymentService isPassExpressWithUniqueIdentifier:completion:]_block_invoke.242
+ ___65-[PKPaymentService notifyForFPANCardImportConsentWithCompletion:]_block_invoke.297
+ ___65-[PKPaymentService passSharesForCredentialIdentifier:completion:]_block_invoke.372
+ ___65-[PKPaymentService pendingFamilyMembersIgnoringCache:completion:]_block_invoke.330
+ ___65-[PKPaymentService revokeMerchantTokenWithIdentifier:completion:]_block_invoke.294
+ ___65-[PKPaymentService sharedPaymentWebServiceContextWithCompletion:]_block_invoke.282
+ ___65-[PKPaymentService transactionsTotalAmountForRequest:completion:]_block_invoke.173
+ ___65-[PKPaymentWebService _applePayTrustPublicKeyHashWithCompletion:]_block_invoke.957
+ ___65-[PKSecureElement initializeSecureElementIfNecessaryWithHandler:]_block_invoke.259
+ ___66-[PKPaymentService defaultPaymentPassIngestionSpecificIdentifier:]_block_invoke.332
+ ___66-[PKPaymentService registerCredentialsWithIdentifiers:completion:]_block_invoke.366
+ ___66-[PKPaymentService setBalanceReminder:forBalance:pass:completion:]_block_invoke.194
+ ___67-[PKPaymentService addPlaceholderPassWithConfiguration:completion:]_block_invoke.362
+ ___67-[PKPaymentService clearFPANCardImportNotificationsWithCompletion:]_block_invoke.299
+ ___67-[PKPaymentService redeemProvisioningSharingIdentifier:completion:]_block_invoke.385
+ ___67-[PKPaymentService requestNotificationAuthorizationWithCompletion:]_block_invoke.265
+ ___67-[PKSecureElement consistencyCheckDeviceCredentialsWithCompletion:]_block_invoke.273
+ ___68+[PKPaymentHeroImageManifest manifestFileForRegion:planningToWrite:]_block_invoke
+ ___68+[PKPaymentHeroImageManifest manifestFileForRegion:planningToWrite:]_block_invoke_2
+ ___68-[PKPaymentService deleteTransactionReceiptWithUniqueID:completion:]_block_invoke.396
+ ___68-[PKPaymentService updateAllMapsBrandAndMerchantDataWithCompletion:]_block_invoke.283
+ ___68-[PKPaymentWebService retrieveMerchantTokensWithRequest:completion:]_block_invoke.792
+ ___68-[PKSecureElement markAppletsWithIdentifiersForDeletion:completion:]_block_invoke.295
+ ___69-[PKPaymentService featureApplicationsForProvisioningWithCompletion:]_block_invoke.336
+ ___69-[PKPaymentService initializeSecureElementIfNecessaryWithCompletion:]_block_invoke.219
+ ___69-[PKPaymentService removeExpressPassWithUniqueIdentifier:completion:]_block_invoke.239
+ ___69-[PKPaymentService reserveStorageForAppletTypes:metadata:completion:]_block_invoke.389
+ ___69-[PKPaymentService setExpressWithPassInformation:credential:handler:]_block_invoke.236
+ ___70-[PKPaymentService accountAttestationAnonymizationSaltWithCompletion:]_block_invoke.359
+ ___70-[PKPaymentService revokeCredentialsWithReaderIdentifiers:completion:]_block_invoke.369
+ ___70-[PKPaymentService suggestPaymentFPANCredentialImport:withCompletion:]_block_invoke.296
+ ___70-[PKPaymentWebService _handlePassListDownloadTask:data:fromPushTopic:]_block_invoke.912
+ ___70-[PKSecureElement signChallenge:forPaymentApplication:withCompletion:]_block_invoke.297
+ ___70-[PKSecureElement signChallenge:signatureEntanglementMode:completion:]_block_invoke.298
+ ___71-[PKPaymentService featureApplicationsForAccountIdentifier:completion:]_block_invoke.333
+ ___71-[PKPaymentService plansForPaymentPassWithUniqueIdentifier:completion:]_block_invoke.191
+ ___71-[PKPaymentService removeExpressPassWithUniqueIdentifierV2:completion:]_block_invoke.238
+ ___71-[PKPaymentService setExpressWithPassConfiguration:credential:handler:]_block_invoke.234
+ ___73-[PKPaymentService ambiguousTransactionWithServiceIdentifier:completion:]_block_invoke.398
+ ___73-[PKPaymentService clearFPANCardImportNotificationHistoryWithCompletion:]_block_invoke.300
+ ___73-[PKPaymentService featureApplicationWithReferenceIdentifier:completion:]_block_invoke.338
+ ___73-[PKPaymentWebService URLSession:downloadTask:didFinishDownloadingToURL:]_block_invoke.866
+ ___73-[PKSecureElement peerPaymentEnrollmentDataWithAlternateDSID:completion:]_block_invoke.332
+ ___73-[PKSecureElement peerPaymentEnrollmentDataWithAlternateDSID:completion:]_block_invoke.335
+ ___73-[PKSecureElement peerPaymentEnrollmentDataWithAlternateDSID:completion:]_block_invoke_2.333
+ ___73-[PKSecureElement peerPaymentEnrollmentDataWithAlternateDSID:completion:]_block_invoke_3.334
+ ___74-[PKPaymentService balancesForPaymentPassWithUniqueIdentifier:completion:]_block_invoke.190
+ ___74-[PKPaymentService messagesForPaymentPassWithUniqueIdentifier:completion:]_block_invoke.189
+ ___74-[PKPaymentService notifyForFPANCardImportWithCredentials:withCompletion:]_block_invoke.298
+ ___74-[PKPaymentService setAccountAttestationAnonymizationSalt:withCompletion:]_block_invoke.361
+ ___74-[PKPaymentService setCommutePlanReminder:forCommutePlan:pass:completion:]_block_invoke.198
+ ___74-[PKPaymentService valueAddedServiceTransactionWithIdentifier:completion:]_block_invoke.214
+ ___74-[PKSecureElement createAliroHydraKeyWithServerParameters:withCompletion:]_block_invoke.310
+ ___75-[PKPaymentService balanceReminderThresholdForBalance:pass:withCompletion:]_block_invoke.192
+ ___75-[PKPaymentService commutePlanReminderForCommputePlan:pass:withCompletion:]_block_invoke.196
+ ___75-[PKPaymentService prepareProvisioningTarget:checkFamilyCircle:completion:]_block_invoke.380
+ ___75-[PKPaymentService submitEncryptedPIN:forTransactionIdentifier:completion:]_block_invoke.322
+ ___75-[PKPaymentService transactionTagsForTransactionWithIdentifier:completion:]_block_invoke.397
+ ___75-[PKPaymentService(FPAN) checkActiveFPANCardsForEligibilityWithCompletion:]_block_invoke.53
+ ___76-[PKPaymentWebServiceRemoteProxyTargetDevice initWithWebService:connection:]_block_invoke.643
+ ___77-[PKPaymentService sendDeviceSharingCapabilitiesRequestForHandle:completion:]_block_invoke.400
+ ___77-[PKPaymentService updateFeatureApplicationsForAccountIdentifier:completion:]_block_invoke.334
+ ___77-[PKPaymentService updateMetadataOnPassWithIdentifier:credential:completion:]_block_invoke.365
+ ___78-[PKPaymentService categoryVisualizationMagnitudesForPassUniqueID:completion:]_block_invoke.352
+ ___78-[PKPaymentService featureApplicationsForAccountUserInvitationWithCompletion:]_block_invoke.337
+ ___78-[PKPaymentService requestNotificationAuthorizationIfNecessaryWithCompletion:]_block_invoke.264
+ ___79-[PKPaymentService submitUserConfirmation:forTransactionIdentifier:completion:]_block_invoke.319
+ ___79-[PKPaymentWebService retrieveMerchantTokensUnifiedListWithRequest:completion:]_block_invoke.790
+ ___80-[PKPaymentService passUniqueIdentifierForTransactionWithIdentifier:completion:]_block_invoke.178
+ ___80-[PKPaymentWebService _registerIfNeededWithResponse:task:isRedirect:completion:]_block_invoke.954
+ ___80-[PKPaymentWebService _registerIfNeededWithResponse:task:isRedirect:completion:]_block_invoke.956
+ ___81-[PKPaymentService(PaymentOffers) updatePaymentOfferCatalogVersion:shouldRemove:]_block_invoke
+ ___81-[PKSecureElement initializeSecureElementQueuingServerConnection:withCompletion:]_block_invoke.258
+ ___82-[PKPassLibrary stateOfRelevancyPresentmentOfType:containingPassUniqueIdentifier:]_block_invoke
+ ___82-[PKPaymentService markAuthenticationCompleteForTransactionIdentifier:completion:]_block_invoke.318
+ ___82-[PKPaymentWebService submitVerificationCode:verificationData:forPass:completion:]_block_invoke
+ ___82-[PKPaymentWebService submitVerificationCode:verificationData:forPass:completion:]_block_invoke_2
+ ___83-[PKPaymentService mapsMerchantWithIdentifier:resultProviderIdentifier:completion:]_block_invoke.284
+ ___83-[PKPaymentService saveProvisioningSupportData:forPassUniqueIdentifier:completion:]_block_invoke.375
+ ___83-[PKPaymentService transactionsRequiringReviewForAccountWithIdentifier:completion:]_block_invoke.351
+ ___83-[PKPaymentWebService _performRewrapRequest:serviceURL:responseHandler:completion:]_block_invoke.839
+ ___84-[PKPaymentService passUniqueIdentifiersForTransactionSourceIdentifiers:completion:]_block_invoke.180
+ ___84-[PKPaymentService setDefaultPaymentApplication:forPassUniqueIdentifier:completion:]_block_invoke.216
+ ___85-[PKPaymentService setDefaultExpressTransitPassIdentifier:withCredential:completion:]_block_invoke.224
+ ___85-[PKPaymentService submitBarcodePaymentEvent:forPassUniqueIdentifier:withCompletion:]_block_invoke.325
+ ___86-[PKPaymentService userNotificationActionPerformed:notificationIdentifier:completion:]_block_invoke.267
+ ___87-[PKPaymentService conflictingExpressPassIdentifiersForPassInformation:withCompletion:]_block_invoke.231
+ ___87-[PKPaymentService transitStateWithPassUniqueIdentifier:paymentApplication:completion:]_block_invoke.247
+ ___87-[PKPaymentWebService _handleRetryAfterRegisterWithRequest:response:completionHandler:]_block_invoke.926
+ ___88-[PKPaymentService valueAddedServiceTransactionsForPaymentTransaction:limit:completion:]_block_invoke.213
+ ___89-[PKAutoFillCardManager activeFPANCardsWithOptions:allowedCardTypes:sortType:completion:]_block_invoke.38
+ ___89-[PKPaymentService conflictingExpressPassIdentifiersForPassConfiguration:withCompletion:]_block_invoke.230
+ ___89-[PKPaymentService processedAuthenticationMechanism:forTransactionIdentifier:completion:]_block_invoke.317
+ ___89-[PKPaymentService submitTransactionAnswerForTransaction:questionType:answer:completion:]_block_invoke.350
+ ___89-[PKPaymentService(FPAN) fpanDescriptorAndCredentialForFPAN:descriptor:credential:error:]_block_invoke
+ ___89-[PKPaymentService(FPAN) fpanDescriptorAndCredentialForFPAN:descriptor:credential:error:]_block_invoke.51
+ ___90-[PKPaymentService clearProvisioningSupportDataOfType:forPassUniqueIdentifier:completion:]_block_invoke.376
+ ___91-[PKPaymentService retrievePINEncryptionCertificateForPassUniqueIdentifier:withCompletion:]_block_invoke.315
+ ___91-[PKPaymentService setDefaultExpressFelicaTransitPassIdentifier:withCredential:completion:]_block_invoke.222
+ ___92-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:]_block_invoke.289
+ ___92-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:]_block_invoke.290
+ ___92-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:]_block_invoke.292
+ ___92-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:]_block_invoke_2.291
+ ___93+[PKRemotePaymentInstrument(Caching) thumbnailCachePathForManifestHash:size:planningToWrite:]_block_invoke
+ ___93+[PKRemotePaymentInstrument(Caching) thumbnailCachePathForManifestHash:size:planningToWrite:]_block_invoke_2
+ ___93-[PKPaymentService cancelAutoTopUpForPassWithUniqueIdentifier:balanceIdentifiers:completion:]_block_invoke.195
+ ___93-[PKPaymentService fetchBarcodesForPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.310
+ ___93-[PKPaymentService transactionsRelatedToTransaction:transactionSourceIdentifiers:completion:]_block_invoke.207
+ ___93-[PKSecureElement generateTransactionKeyWithReaderIdentifier:readerPublicKey:withCompletion:]_block_invoke.307
+ ___94-[PKPaymentService sharingInvitationWasInvalidated:withCredentialIdentifier:error:completion:]_block_invoke.373
+ ___94-[PKPaymentService valueAddedServiceTransactionsForPassWithUniqueIdentifier:limit:completion:]_block_invoke.212
+ ___96-[PKPaymentService ambiguousPassUniqueIdentifierForTransactionWithServiceIdentifier:completion:]_block_invoke.181
+ ___96-[PKPaymentService invalidateAuxiliaryCapabilityCertificatesForPassUniqueIdentifier:completion:]_block_invoke.309
+ ___96-[PKPaymentService merchantForPassUniqueIdentifier:withAuxiliaryPassInformationItem:completion:]_block_invoke.292
+ ___96-[PKPaymentService provideEncryptedPushProvisioningTarget:sharingInstanceIdentifier:completion:]_block_invoke.379
+ ___96-[PKPaymentService submitEncryptedPIN:forTransactionIdentifier:sessionExchangeToken:completion:]_block_invoke.323
+ ___96-[PKPaymentService transactionReceiptForTransactionWithIdentifier:updateIfNecessary:completion:]_block_invoke.394
+ ___96-[PKPaymentWebService _backgroundDownloadCloudStoreAssetsForItem:cloudStoreCoordinatorDelegate:]_block_invoke.903
+ ___96-[PKPaymentWebService _backgroundDownloadCloudStoreAssetsForItem:cloudStoreCoordinatorDelegate:]_block_invoke.905
+ ___96-[PKPaymentWebService _backgroundDownloadCloudStoreAssetsForItem:cloudStoreCoordinatorDelegate:]_block_invoke_2.904
+ ___96-[PKPaymentWebService _backgroundDownloadCloudStoreAssetsForItem:cloudStoreCoordinatorDelegate:]_block_invoke_2.908
+ ___97-[PKPaymentService augmentedProductForInstallmentConfiguration:experimentDetails:withCompletion:]_block_invoke.340
+ ___98-[PKPaymentService updatePreferredCategory:forTransactionsWithIdentifiers:paymentPass:completion:]_block_invoke.208
+ ___99-[PKPaymentService userNotificationActionPerformed:applicationMessageContentIdentifier:completion:]_block_invoke.266
+ ___Block_byref_object_copy_.543
+ ___Block_byref_object_dispose_.544
+ ___PKSharedCacheCreateFileURLReadOnly_block_invoke
+ ____FixSharedCacheFileProtection_block_invoke
+ ____FixSharedCacheFileProtection_block_invoke_2
+ ____Z17PKShortDateStringP6NSDateP10NSTimeZone_block_invoke
+ ___block_descriptor_32_e39_B16?0"PKPassVerificationMethodGroup"8l
+ ___block_descriptor_40_e8_32bs_e8_v12?0C8ls32l8
+ ___block_descriptor_48_e8_32r40r_e31_v24?0"PKAccount"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e18_v16?0"NSNumber"8ls40l8s32l8
+ ___block_descriptor_64_e8_32s40r48r56r_e71_v32?0"PKFPANCardDescriptor"8"PKAutoFillCardCredential"16"NSError"24lr40l8r48l8r56l8s32l8
+ ___block_literal_global.1016
+ ___block_literal_global.1021
+ ___block_literal_global.1060
+ ___block_literal_global.1067
+ ___block_literal_global.1072
+ ___block_literal_global.1077
+ ___block_literal_global.1082
+ ___block_literal_global.1087
+ ___block_literal_global.1092
+ ___block_literal_global.1097
+ ___block_literal_global.1102
+ ___block_literal_global.1109
+ ___block_literal_global.1153
+ ___block_literal_global.1232
+ ___block_literal_global.1237
+ ___block_literal_global.1241
+ ___block_literal_global.1244
+ ___block_literal_global.1247
+ ___block_literal_global.1256
+ ___block_literal_global.1270
+ ___block_literal_global.1313
+ ___block_literal_global.1429
+ ___block_literal_global.1432
+ ___block_literal_global.156
+ ___block_literal_global.1670
+ ___block_literal_global.1675
+ ___block_literal_global.1679
+ ___block_literal_global.1695
+ ___block_literal_global.1700
+ ___block_literal_global.1714
+ ___block_literal_global.1720
+ ___block_literal_global.1731
+ ___block_literal_global.1734
+ ___block_literal_global.188
+ ___block_literal_global.229
+ ___block_literal_global.237
+ ___block_literal_global.241
+ ___block_literal_global.246
+ ___block_literal_global.259
+ ___block_literal_global.263
+ ___block_literal_global.273
+ ___block_literal_global.278
+ ___block_literal_global.281
+ ___block_literal_global.378
+ ___block_literal_global.475
+ ___block_literal_global.655
+ ___block_literal_global.682
+ ___block_literal_global.684
+ ___block_literal_global.691
+ ___block_literal_global.731
+ ___block_literal_global.735
+ ___block_literal_global.865
+ ___block_literal_global.868
+ ___block_literal_global.876
+ ___block_literal_global.884
+ ___block_literal_global.887
+ ___block_literal_global.907
+ ___block_literal_global.910
+ ___block_literal_global.914
+ ___block_literal_global.916
+ _block_copy_helper.104
+ _block_copy_helper.111
+ _block_copy_helper.121
+ _block_copy_helper.128
+ _block_copy_helper.131
+ _block_copy_helper.138
+ _block_copy_helper.144
+ _block_copy_helper.151
+ _block_copy_helper.161
+ _block_copy_helper.88
+ _block_copy_helper.95
+ _block_descriptor.106
+ _block_descriptor.113
+ _block_descriptor.123
+ _block_descriptor.130
+ _block_descriptor.133
+ _block_descriptor.140
+ _block_descriptor.146
+ _block_descriptor.153
+ _block_descriptor.163
+ _block_descriptor.90
+ _block_descriptor.97
+ _block_destroy_helper.105
+ _block_destroy_helper.112
+ _block_destroy_helper.122
+ _block_destroy_helper.129
+ _block_destroy_helper.132
+ _block_destroy_helper.139
+ _block_destroy_helper.145
+ _block_destroy_helper.152
+ _block_destroy_helper.162
+ _block_destroy_helper.89
+ _block_destroy_helper.96
+ _nan
+ _objc_msgSend$CGImage
+ _objc_msgSend$_displayableAirlineSeatsStringForRow:designations:
+ _objc_msgSend$_displayableStringForDate:fromField:
+ _objc_msgSend$_fkPaymentTransactionCategory
+ _objc_msgSend$_formatSeatLettersForRow:designations:includeSpaceBetweenRowAndSeats:
+ _objc_msgSend$_formatSeatNumbersForRow:designations:formatter:includeSpaceBetweenRowAndSeats:
+ _objc_msgSend$_formattedAirlineSeatsStringForRow:designation:includeSpaceBetweenRowAndSeats:
+ _objc_msgSend$_isStringAllLetters:
+ _objc_msgSend$_isStringAllNumbers:formatter:
+ _objc_msgSend$_markOfferConsumedForPassUniqueID:criteriaIdentifier:
+ _objc_msgSend$_setIsInRestrictedMode:
+ _objc_msgSend$authorizationStatusForCapability:
+ _objc_msgSend$dashboardInstance
+ _objc_msgSend$fpanDescriptorAndCredentialForFPAN:completion:
+ _objc_msgSend$fpanDescriptorAndCredentialForFPAN:descriptor:credential:error:
+ _objc_msgSend$fpanDescriptorAndCredentialUsingFPAN:completion:
+ _objc_msgSend$isEqualToPKIdentityPassCredentialProperty:
+ _objc_msgSend$isSMSOTP
+ _objc_msgSend$manifestFileForRegion:planningToWrite:
+ _objc_msgSend$onlyMethod
+ _objc_msgSend$overrideStateOfRelevancyPresentmentOfType:containingPassUniqueIdentifier:newState:completion:
+ _objc_msgSend$prefillValuesWithPaymentCredential:targetDevice:
+ _objc_msgSend$prepareImageForDescriptor:
+ _objc_msgSend$purgeResources
+ _objc_msgSend$requestAuthorizationForCapability:completion:
+ _objc_msgSend$requestStateOfRelevancyPresentmentOfType:containingPassUniqueIdentifier:completion:
+ _objc_msgSend$resourceValuesForKeys:error:
+ _objc_msgSend$setDocType:
+ _objc_msgSend$setExcludedAccountStates:
+ _objc_msgSend$setExcludedPeerPaymentAccountStates:
+ _objc_msgSend$setResourceValues:error:
+ _objc_msgSend$thumbnailCachePathForManifestHash:size:planningToWrite:
+ _objc_msgSend$transactionCountForRequest:completion:
+ _objc_msgSend$updatePaymentOfferCatalogVersion:shouldRemove:
+ _objc_msgSend$usingSynchronousProxy:accountWithIdentifier:completion:
+ _objectdestroy.50Tm
+ _symbolic _____ySo17NSUnitTemperatureCG 10Foundation11MeasurementV
+ _symbolic _____ySo17NSUnitTemperatureCGSg 10Foundation11MeasurementV
+ _symbolic _____ySo17NSUnitTemperatureCGSg_AEt 10Foundation11MeasurementV
- +[PKFlightEstimates supportsSecureCoding]
- +[PKPaymentHeroImageManifest manifestFileForRegion:]
- +[PKRemotePaymentInstrument(Caching) thumbnailCachePathForManifestHash:size:]
- -[PKFlight _fuFlightLeg]
- -[PKFlight _fuFlight]
- -[PKFlight _sfAirportFromAirport:]
- -[PKFlight _sfFlightLeg]
- -[PKFlight _sfFlightStatus]
- -[PKFlight _sfFlight]
- -[PKFlight _sfPegasusFlightState]
- -[PKFlight _stateFromFUFlightState:]
- -[PKFlight initWithAirlineCode:airlineName:flightNumber:operatorAirlineCode:operatorFlightNumber:departure:arrival:state:publishedDate:dataSource:]
- -[PKFlight initWithFUFlight:relevantLeg:]
- -[PKFlight recomputeEstimates]
- -[PKFlightEstimates .cxx_destruct]
- -[PKFlightEstimates copyWithZone:]
- -[PKFlightEstimates description]
- -[PKFlightEstimates encodeWithCoder:]
- -[PKFlightEstimates initWithCoder:]
- -[PKFlightEstimates progress]
- -[PKFlightEstimates setProgress:]
- -[PKFlightEstimates setState:]
- -[PKFlightEstimates staleDate]
- -[PKFlightEstimates state]
- -[PKPassLibrary requestState:forRelevancyPresentmentWithType:associatedWithUniqueIdentifier:completion:]
- -[PKPassLibrary resetAuthorizationForCapability:handler:]
- -[PKPassLibrary stateOfRelevancyPresentmentWithType:associatedWithUniqueIdentifier:]
- -[PKPassRelevancyModel relevancyActive]
- GCC_except_table100
- GCC_except_table109
- GCC_except_table116
- GCC_except_table133
- GCC_except_table140
- GCC_except_table170
- GCC_except_table199
- GCC_except_table210
- GCC_except_table229
- GCC_except_table232
- GCC_except_table252
- GCC_except_table270
- GCC_except_table323
- GCC_except_table326
- GCC_except_table333
- GCC_except_table349
- GCC_except_table357
- GCC_except_table363
- GCC_except_table380
- GCC_except_table403
- GCC_except_table406
- GCC_except_table408
- GCC_except_table423
- GCC_except_table439
- GCC_except_table464
- GCC_except_table517
- GCC_except_table519
- GCC_except_table542
- GCC_except_table572
- GCC_except_table660
- GCC_except_table67
- GCC_except_table703
- GCC_except_table711
- GCC_except_table729
- GCC_except_table80
- GCC_except_table847
- GCC_except_table96
- _.str.114
- _ImageForAutoFillCredentialType
- _OBJC_CLASS_$_FUUtils
- _OBJC_CLASS_$_PKFlightEstimates
- _OBJC_CLASS_$_SFAirport
- _OBJC_CLASS_$_SFFlight
- _OBJC_CLASS_$_SFFlightDateDescriptor
- _OBJC_CLASS_$_SFFlightLeg
- _OBJC_CLASS_$_SFLatLng
- _OBJC_IVAR_$_PKFlightEstimates._progress
- _OBJC_IVAR_$_PKFlightEstimates._staleDate
- _OBJC_IVAR_$_PKFlightEstimates._state
- _OBJC_METACLASS_$_PKFlightEstimates
- _PKAggDKeyApplePayButtonCardContextCardArt
- _PKAnalyticsKeyReportApplePayDemoCompletedWithinKey
- _PKAnalyticsKeyReportHasContactlessTransactionWithinKey
- _PKAnalyticsKeyReportHasPaymentPassKey
- _PKMapsSnapshotsCacheCreateFileURL
- _PKPassAssetDownloadCacheCreateFileURL
- _PKRemoteInstrumentThumbnailsCacheCreateFileURL
- _PKSharedCacheCreateFileURL
- __MergedGlobals.29
- __MergedGlobals.30
- __MergedGlobals.31
- __OBJC_$_CLASS_METHODS_PKFlightEstimates
- __OBJC_$_CLASS_PROP_LIST_PKFlightEstimates
- __OBJC_$_INSTANCE_METHODS_PKFlightEstimates
- __OBJC_$_INSTANCE_VARIABLES_PKFlightEstimates
- __OBJC_$_PROP_LIST_PKFlightEstimates
- __OBJC_CLASS_PROTOCOLS_$_PKFlightEstimates
- __OBJC_CLASS_RO_$_PKFlightEstimates
- __OBJC_METACLASS_RO_$_PKFlightEstimates
- ___100-[PKPaymentService submitUserConfirmation:forTransactionIdentifier:sessionExchangeToken:completion:]_block_invoke.319
- ___102-[PKPaymentService recordPaymentApplicationUsageForPassUniqueIdentifier:paymentApplicationIdentifier:]_block_invoke.242
- ___103-[PKPaymentService submitTransactionSignatureForTransactionIdentifier:sessionExchangeToken:completion:]_block_invoke.322
- ___104-[PKPassLibrary requestState:forRelevancyPresentmentWithType:associatedWithUniqueIdentifier:completion:]_block_invoke
- ___104-[PKPassLibrary requestState:forRelevancyPresentmentWithType:associatedWithUniqueIdentifier:completion:]_block_invoke.269
- ___104-[PKSecureElement createAliroHomeKeyWithReaderIdentifier:readerPublicKey:homeIdentifier:withCompletion:]_block_invoke.313
- ___106-[PKPaymentService submitBarcodePaymentEvent:forPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.324
- ___107-[PKPaymentService registerAuxiliaryCapabilityForPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.306
- ___107-[PKPaymentService retrieveDecryptedBarcodeCredentialForPassUniqueIdentifier:authorization:withCompletion:]_block_invoke.310
- ___109-[PKPaymentService conflictingExpressPassIdentifiersForPassInformation:withReferenceExpressState:completion:]_block_invoke.231
- ___111-[PKPaymentService conflictingExpressPassIdentifiersForPassConfiguration:withReferenceExpressState:completion:]_block_invoke.230
- ___112-[PKPaymentService retrievePINEncryptionCertificateForPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.314
- ___115-[PKPaymentService passUniqueIdentifierForTransactionWithServiceIdentifier:transactionSourceIdentifier:completion:]_block_invoke.177
- ___115-[PKPaymentWebService backgroundDownloadRemotePassAssets:forSuffixesAndScreenScales:cloudStoreCoordinatorDelegate:]_block_invoke.720
- ___115-[PKPaymentWebService backgroundDownloadRemotePassAssets:forSuffixesAndScreenScales:cloudStoreCoordinatorDelegate:]_block_invoke.723
- ___115-[PKPaymentWebService backgroundDownloadRemotePassAssets:forSuffixesAndScreenScales:cloudStoreCoordinatorDelegate:]_block_invoke.727
- ___115-[PKPaymentWebService backgroundDownloadRemotePassAssets:forSuffixesAndScreenScales:cloudStoreCoordinatorDelegate:]_block_invoke.729
- ___115-[PKPaymentWebService backgroundDownloadRemotePassAssets:forSuffixesAndScreenScales:cloudStoreCoordinatorDelegate:]_block_invoke_2.730
- ___117-[PKPaymentService insertOrUpdateValueAddedServiceTransaction:forPassUniqueIdentifier:paymentTransaction:completion:]_block_invoke.209
- ___128-[PKPaymentService retrieveDecryptedBarcodeCredentialForPassUniqueIdentifier:authorization:sessionExchangeToken:withCompletion:]_block_invoke.312
- ___130-[PKPaymentWebService _passActionGroupIncludingAppletDataWithRemoteContentPassActionGroup:forPass:forDeviceIdentifier:completion:]_block_invoke.763
- ___140-[PKPaymentService rangingSuspensionReasonForAppletSubcredentialIdentifier:paymentApplicationIdentifier:secureElementIdentifier:completion:]_block_invoke.285
- ___149-[PKPaymentService processTransitTransactionEventWithHistory:transactionDate:forPaymentApplication:withPassUniqueIdentifier:expressTransactionState:]_block_invoke.241
- ___36-[PKPaymentService consistencyCheck]_block_invoke.259
- ___43-[PKPaymentService productsWithCompletion:]_block_invoke.354
- ___44-[PKPaymentService initializeSecureElement:]_block_invoke.219
- ___45-[PKPaymentService insertUserLegalAgreement:]_block_invoke.397
- ___48-[PKPaymentService mapsMerchantsWithCompletion:]_block_invoke.180
- ___48-[PKSecureElement SEPPairingInfoWithCompletion:]_block_invoke.266
- ___49-[PKPaymentService currentSecureElementSnapshot:]_block_invoke.385
- ___49-[PKPaymentService deleteReservation:completion:]_block_invoke.389
- ___50-[PKPassLibrary authorizationStatusForCapability:]_block_invoke
- ___50-[PKPaymentService sharedPaymentWebServiceContext]_block_invoke.278
- ___50-[PKPaymentService submitApplyRequest:completion:]_block_invoke.342
- ___50-[PKPaymentService submitTermsRequest:completion:]_block_invoke.346
- ___51-[PKPaymentService logoImageDataForURL:completion:]_block_invoke.173
- ___51-[PKPaymentService productsWithRequest:completion:]_block_invoke.352
- ___51-[PKPaymentService submitDeleteRequest:completion:]_block_invoke.347
- ___51-[PKSecureElement appletWithIdentifier:completion:]_block_invoke.279
- ___52+[PKPaymentHeroImageManifest manifestFileForRegion:]_block_invoke
- ___52-[PKSecureElement signatureForAuthToken:completion:]_block_invoke.307
- ___52-[PKSecureElement signedPlatformDataWithCompletion:]_block_invoke.310
- ___53-[PKPaymentService submitDocumentRequest:completion:]_block_invoke.344
- ___54-[PKPaymentService featureApplicationsWithCompletion:]_block_invoke.340
- ___54-[PKPaymentService regionsWithIdentifiers:completion:]_block_invoke.288
- ___55-[PKPaymentService performDeviceCheckInWithCompletion:]_block_invoke.351
- ___55-[PKPaymentService pushProvisioningSharingIdentifiers:]_block_invoke.372
- ___55-[PKSecureElement appletCredentialsForAIDs:completion:]_block_invoke.273
- ___56-[PKPaymentService credentialWithIdentifier:completion:]_block_invoke.368
- ___57-[PKPassLibrary resetAuthorizationForCapability:handler:]_block_invoke
- ___57-[PKPassLibrary resetAuthorizationForCapability:handler:]_block_invoke.322
- ___57-[PKPassLibrary resetAuthorizationForCapability:handler:]_block_invoke_2
- ___57-[PKPaymentService regionsMatchingName:types:completion:]_block_invoke.289
- ___57-[PKPaymentService submitVerificationRequest:completion:]_block_invoke.345
- ___58-[PKPaymentService familyMembersIgnoringCache:completion:]_block_invoke.325
- ___58-[PKSecureElement allAppletsAndCredentialsWithCompletion:]_block_invoke.269
- ___59-[PKPaymentService memberTypeForCurrentUserWithCompletion:]_block_invoke.326
- ___59-[PKPaymentService performProductActionRequest:completion:]_block_invoke.355
- ___59-[PKPaymentService requiresUpgradedPasscodeWithCompletion:]_block_invoke.304
- ___59-[PKPaymentService storeTransactionReceiptData:completion:]_block_invoke.393
- ___59-[PKPaymentService subcredentialInvitationsWithCompletion:]_block_invoke.362
- ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke.869
- ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke.875
- ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke.877
- ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke.883
- ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke_2.872
- ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke_2.876
- ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke_2.880
- ___61-[PKPaymentService changePasscodeFrom:toPasscode:completion:]_block_invoke.305
- ___61-[PKPaymentService statusForShareableCredentials:completion:]_block_invoke.375
- ___62-[PKPassLibrary requestAuthorizationForCapability:completion:]_block_invoke
- ___62-[PKPassLibrary requestAuthorizationForCapability:completion:]_block_invoke.321
- ___62-[PKPassLibrary requestAuthorizationForCapability:completion:]_block_invoke_2
- ___62-[PKPaymentService addRemoteDevicePendingProvisioningReceipt:]_block_invoke.293
- ___62-[PKPaymentService generateUnderlyingKeyReportWithCompletion:]_block_invoke.299
- ___62-[PKPaymentService transactionReceiptWithUniqueID:completion:]_block_invoke.390
- ___62-[PKPaymentService transactionsForPredicate:limit:completion:]_block_invoke.175
- ___62-[PKPaymentService(FPAN) cachedFPANCredentialsWithCompletion:]_block_invoke.53
- ___63-[PKPaymentService currentPasscodeMeetsUpgradedPasscodePolicy:]_block_invoke.303
- ___63-[PKPaymentService photosForFamilyMembersWithDSIDs:completion:]_block_invoke.329
- ___63-[PKPaymentService refreshMerchantTokenMetadataWithCompletion:]_block_invoke.291
- ___63-[PKPaymentService removeExpressPassesWithCardType:completion:]_block_invoke.235
- ___63-[PKPaymentWebService _nonceWithRequest:serviceURL:completion:]_block_invoke.809
- ___64-[PKPaymentService enforceUpgradedPasscodePolicyWithCompletion:]_block_invoke.302
- ___64-[PKPaymentService featureApplicationWithIdentifier:completion:]_block_invoke.341
- ___64-[PKPaymentService passOwnershipTokenWithIdentifier:completion:]_block_invoke.356
- ___64-[PKPaymentService redeemPaymentShareableCredential:completion:]_block_invoke.381
- ___64-[PKPaymentService revokeCredentialsWithIdentifiers:completion:]_block_invoke.366
- ___64-[PKPaymentWebServiceLocalProxyTargetDevice initWithConnection:]_block_invoke.292
- ___65-[PKAutoFillCardManager userDidUseCardWithDescriptor:credential:]_block_invoke.65
- ___65-[PKPaymentService isPassExpressWithUniqueIdentifier:completion:]_block_invoke.240
- ___65-[PKPaymentService notifyForFPANCardImportConsentWithCompletion:]_block_invoke.295
- ___65-[PKPaymentService passSharesForCredentialIdentifier:completion:]_block_invoke.370
- ___65-[PKPaymentService pendingFamilyMembersIgnoringCache:completion:]_block_invoke.328
- ___65-[PKPaymentService revokeMerchantTokenWithIdentifier:completion:]_block_invoke.292
- ___65-[PKPaymentService sharedPaymentWebServiceContextWithCompletion:]_block_invoke.280
- ___65-[PKPaymentService transactionsTotalAmountForRequest:completion:]_block_invoke.171
- ___65-[PKPaymentWebService _applePayTrustPublicKeyHashWithCompletion:]_block_invoke.952
- ___65-[PKSecureElement initializeSecureElementIfNecessaryWithHandler:]_block_invoke.263
- ___66-[PKPaymentService defaultPaymentPassIngestionSpecificIdentifier:]_block_invoke.330
- ___66-[PKPaymentService registerCredentialsWithIdentifiers:completion:]_block_invoke.364
- ___66-[PKPaymentService setBalanceReminder:forBalance:pass:completion:]_block_invoke.192
- ___67-[PKPaymentService addPlaceholderPassWithConfiguration:completion:]_block_invoke.360
- ___67-[PKPaymentService clearFPANCardImportNotificationsWithCompletion:]_block_invoke.297
- ___67-[PKPaymentService redeemProvisioningSharingIdentifier:completion:]_block_invoke.383
- ___67-[PKPaymentService requestNotificationAuthorizationWithCompletion:]_block_invoke.263
- ___67-[PKSecureElement consistencyCheckDeviceCredentialsWithCompletion:]_block_invoke.277
- ___68-[PKPaymentService deleteTransactionReceiptWithUniqueID:completion:]_block_invoke.394
- ___68-[PKPaymentService updateAllMapsBrandAndMerchantDataWithCompletion:]_block_invoke.281
- ___68-[PKPaymentWebService retrieveMerchantTokensWithRequest:completion:]_block_invoke.787
- ___68-[PKSecureElement markAppletsWithIdentifiersForDeletion:completion:]_block_invoke.299
- ___69-[PKPaymentService featureApplicationsForProvisioningWithCompletion:]_block_invoke.334
- ___69-[PKPaymentService initializeSecureElementIfNecessaryWithCompletion:]_block_invoke.217
- ___69-[PKPaymentService removeExpressPassWithUniqueIdentifier:completion:]_block_invoke.237
- ___69-[PKPaymentService reserveStorageForAppletTypes:metadata:completion:]_block_invoke.387
- ___69-[PKPaymentService setExpressWithPassInformation:credential:handler:]_block_invoke.234
- ___70-[PKPaymentService accountAttestationAnonymizationSaltWithCompletion:]_block_invoke.357
- ___70-[PKPaymentService revokeCredentialsWithReaderIdentifiers:completion:]_block_invoke.367
- ___70-[PKPaymentService suggestPaymentFPANCredentialImport:withCompletion:]_block_invoke.294
- ___70-[PKPaymentWebService _handlePassListDownloadTask:data:fromPushTopic:]_block_invoke.907
- ___70-[PKSecureElement signChallenge:forPaymentApplication:withCompletion:]_block_invoke.301
- ___70-[PKSecureElement signChallenge:signatureEntanglementMode:completion:]_block_invoke.302
- ___71-[PKPaymentService featureApplicationsForAccountIdentifier:completion:]_block_invoke.331
- ___71-[PKPaymentService plansForPaymentPassWithUniqueIdentifier:completion:]_block_invoke.189
- ___71-[PKPaymentService removeExpressPassWithUniqueIdentifierV2:completion:]_block_invoke.236
- ___71-[PKPaymentService setExpressWithPassConfiguration:credential:handler:]_block_invoke.232
- ___73-[PKPaymentService ambiguousTransactionWithServiceIdentifier:completion:]_block_invoke.396
- ___73-[PKPaymentService clearFPANCardImportNotificationHistoryWithCompletion:]_block_invoke.298
- ___73-[PKPaymentService featureApplicationWithReferenceIdentifier:completion:]_block_invoke.336
- ___73-[PKPaymentWebService URLSession:downloadTask:didFinishDownloadingToURL:]_block_invoke.861
- ___73-[PKSecureElement peerPaymentEnrollmentDataWithAlternateDSID:completion:]_block_invoke.336
- ___73-[PKSecureElement peerPaymentEnrollmentDataWithAlternateDSID:completion:]_block_invoke.339
- ___73-[PKSecureElement peerPaymentEnrollmentDataWithAlternateDSID:completion:]_block_invoke_2.337
- ___73-[PKSecureElement peerPaymentEnrollmentDataWithAlternateDSID:completion:]_block_invoke_3.338
- ___74-[PKPaymentService balancesForPaymentPassWithUniqueIdentifier:completion:]_block_invoke.188
- ___74-[PKPaymentService messagesForPaymentPassWithUniqueIdentifier:completion:]_block_invoke.187
- ___74-[PKPaymentService notifyForFPANCardImportWithCredentials:withCompletion:]_block_invoke.296
- ___74-[PKPaymentService setAccountAttestationAnonymizationSalt:withCompletion:]_block_invoke.359
- ___74-[PKPaymentService setCommutePlanReminder:forCommutePlan:pass:completion:]_block_invoke.196
- ___74-[PKPaymentService valueAddedServiceTransactionWithIdentifier:completion:]_block_invoke.212
- ___74-[PKSecureElement createAliroHydraKeyWithServerParameters:withCompletion:]_block_invoke.314
- ___75-[PKPaymentService balanceReminderThresholdForBalance:pass:withCompletion:]_block_invoke.190
- ___75-[PKPaymentService commutePlanReminderForCommputePlan:pass:withCompletion:]_block_invoke.194
- ___75-[PKPaymentService prepareProvisioningTarget:checkFamilyCircle:completion:]_block_invoke.378
- ___75-[PKPaymentService submitEncryptedPIN:forTransactionIdentifier:completion:]_block_invoke.320
- ___75-[PKPaymentService transactionTagsForTransactionWithIdentifier:completion:]_block_invoke.395
- ___75-[PKPaymentService(FPAN) checkActiveFPANCardsForEligibilityWithCompletion:]_block_invoke.51
- ___76-[PKPaymentWebServiceRemoteProxyTargetDevice initWithWebService:connection:]_block_invoke.637
- ___77+[PKRemotePaymentInstrument(Caching) thumbnailCachePathForManifestHash:size:]_block_invoke
- ___77-[PKPaymentService sendDeviceSharingCapabilitiesRequestForHandle:completion:]_block_invoke.398
- ___77-[PKPaymentService updateFeatureApplicationsForAccountIdentifier:completion:]_block_invoke.332
- ___77-[PKPaymentService updateMetadataOnPassWithIdentifier:credential:completion:]_block_invoke.363
- ___78-[PKPaymentService categoryVisualizationMagnitudesForPassUniqueID:completion:]_block_invoke.350
- ___78-[PKPaymentService featureApplicationsForAccountUserInvitationWithCompletion:]_block_invoke.335
- ___78-[PKPaymentService requestNotificationAuthorizationIfNecessaryWithCompletion:]_block_invoke.262
- ___79-[PKPaymentService submitUserConfirmation:forTransactionIdentifier:completion:]_block_invoke.317
- ___79-[PKPaymentWebService retrieveMerchantTokensUnifiedListWithRequest:completion:]_block_invoke.785
- ___80-[PKPaymentService passUniqueIdentifierForTransactionWithIdentifier:completion:]_block_invoke.176
- ___80-[PKPaymentWebService _registerIfNeededWithResponse:task:isRedirect:completion:]_block_invoke.949
- ___80-[PKPaymentWebService _registerIfNeededWithResponse:task:isRedirect:completion:]_block_invoke.951
- ___81-[PKSecureElement initializeSecureElementQueuingServerConnection:withCompletion:]_block_invoke.262
- ___82-[PKPaymentService markAuthenticationCompleteForTransactionIdentifier:completion:]_block_invoke.316
- ___83-[PKPaymentService mapsMerchantWithIdentifier:resultProviderIdentifier:completion:]_block_invoke.282
- ___83-[PKPaymentService saveProvisioningSupportData:forPassUniqueIdentifier:completion:]_block_invoke.373
- ___83-[PKPaymentService transactionsRequiringReviewForAccountWithIdentifier:completion:]_block_invoke.349
- ___83-[PKPaymentWebService _performRewrapRequest:serviceURL:responseHandler:completion:]_block_invoke.834
- ___84-[PKPassLibrary stateOfRelevancyPresentmentWithType:associatedWithUniqueIdentifier:]_block_invoke
- ___84-[PKPaymentService passUniqueIdentifiersForTransactionSourceIdentifiers:completion:]_block_invoke.178
- ___84-[PKPaymentService setDefaultPaymentApplication:forPassUniqueIdentifier:completion:]_block_invoke.214
- ___85-[PKPaymentService setDefaultExpressTransitPassIdentifier:withCredential:completion:]_block_invoke.222
- ___85-[PKPaymentService submitBarcodePaymentEvent:forPassUniqueIdentifier:withCompletion:]_block_invoke.323
- ___86-[PKPaymentService userNotificationActionPerformed:notificationIdentifier:completion:]_block_invoke.265
- ___87-[PKPaymentService conflictingExpressPassIdentifiersForPassInformation:withCompletion:]_block_invoke.229
- ___87-[PKPaymentService transitStateWithPassUniqueIdentifier:paymentApplication:completion:]_block_invoke.245
- ___87-[PKPaymentWebService _handleRetryAfterRegisterWithRequest:response:completionHandler:]_block_invoke.921
- ___88-[PKPaymentService valueAddedServiceTransactionsForPaymentTransaction:limit:completion:]_block_invoke.211
- ___89-[PKAutoFillCardManager activeFPANCardsWithOptions:allowedCardTypes:sortType:completion:]_block_invoke.40
- ___89-[PKPaymentService conflictingExpressPassIdentifiersForPassConfiguration:withCompletion:]_block_invoke.228
- ___89-[PKPaymentService processedAuthenticationMechanism:forTransactionIdentifier:completion:]_block_invoke.315
- ___89-[PKPaymentService submitTransactionAnswerForTransaction:questionType:answer:completion:]_block_invoke.348
- ___90-[PKPaymentService clearProvisioningSupportDataOfType:forPassUniqueIdentifier:completion:]_block_invoke.374
- ___91-[PKPaymentService retrievePINEncryptionCertificateForPassUniqueIdentifier:withCompletion:]_block_invoke.313
- ___91-[PKPaymentService setDefaultExpressFelicaTransitPassIdentifier:withCredential:completion:]_block_invoke.220
- ___92-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:]_block_invoke.293
- ___92-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:]_block_invoke.294
- ___92-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:]_block_invoke.296
- ___92-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:]_block_invoke_2.295
- ___93-[PKPaymentService cancelAutoTopUpForPassWithUniqueIdentifier:balanceIdentifiers:completion:]_block_invoke.193
- ___93-[PKPaymentService fetchBarcodesForPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.308
- ___93-[PKPaymentService transactionsRelatedToTransaction:transactionSourceIdentifiers:completion:]_block_invoke.205
- ___93-[PKSecureElement generateTransactionKeyWithReaderIdentifier:readerPublicKey:withCompletion:]_block_invoke.311
- ___94-[PKPaymentService sharingInvitationWasInvalidated:withCredentialIdentifier:error:completion:]_block_invoke.371
- ___94-[PKPaymentService valueAddedServiceTransactionsForPassWithUniqueIdentifier:limit:completion:]_block_invoke.210
- ___96-[PKPaymentService ambiguousPassUniqueIdentifierForTransactionWithServiceIdentifier:completion:]_block_invoke.179
- ___96-[PKPaymentService invalidateAuxiliaryCapabilityCertificatesForPassUniqueIdentifier:completion:]_block_invoke.307
- ___96-[PKPaymentService merchantForPassUniqueIdentifier:withAuxiliaryPassInformationItem:completion:]_block_invoke.290
- ___96-[PKPaymentService provideEncryptedPushProvisioningTarget:sharingInstanceIdentifier:completion:]_block_invoke.377
- ___96-[PKPaymentService submitEncryptedPIN:forTransactionIdentifier:sessionExchangeToken:completion:]_block_invoke.321
- ___96-[PKPaymentService transactionReceiptForTransactionWithIdentifier:updateIfNecessary:completion:]_block_invoke.392
- ___96-[PKPaymentWebService _backgroundDownloadCloudStoreAssetsForItem:cloudStoreCoordinatorDelegate:]_block_invoke.898
- ___96-[PKPaymentWebService _backgroundDownloadCloudStoreAssetsForItem:cloudStoreCoordinatorDelegate:]_block_invoke.900
- ___96-[PKPaymentWebService _backgroundDownloadCloudStoreAssetsForItem:cloudStoreCoordinatorDelegate:]_block_invoke_2.899
- ___96-[PKPaymentWebService _backgroundDownloadCloudStoreAssetsForItem:cloudStoreCoordinatorDelegate:]_block_invoke_2.903
- ___97-[PKPaymentService augmentedProductForInstallmentConfiguration:experimentDetails:withCompletion:]_block_invoke.338
- ___98-[PKPaymentService updatePreferredCategory:forTransactionsWithIdentifiers:paymentPass:completion:]_block_invoke.206
- ___99-[PKPaymentService userNotificationActionPerformed:applicationMessageContentIdentifier:completion:]_block_invoke.264
- ___Block_byref_object_copy_.537
- ___Block_byref_object_dispose_.538
- ___PKSharedCacheCreateFileURL_block_invoke
- ___block_literal_global.1019
- ___block_literal_global.1027
- ___block_literal_global.1030
- ___block_literal_global.1058
- ___block_literal_global.1063
- ___block_literal_global.1070
- ___block_literal_global.1075
- ___block_literal_global.1080
- ___block_literal_global.1085
- ___block_literal_global.1090
- ___block_literal_global.1095
- ___block_literal_global.1100
- ___block_literal_global.1105
- ___block_literal_global.1151
- ___block_literal_global.1230
- ___block_literal_global.1235
- ___block_literal_global.1239
- ___block_literal_global.1242
- ___block_literal_global.1245
- ___block_literal_global.1254
- ___block_literal_global.1268
- ___block_literal_global.1308
- ___block_literal_global.1425
- ___block_literal_global.1430
- ___block_literal_global.151
- ___block_literal_global.1666
- ___block_literal_global.1673
- ___block_literal_global.1677
- ___block_literal_global.1691
- ___block_literal_global.1698
- ___block_literal_global.1712
- ___block_literal_global.1718
- ___block_literal_global.1721
- ___block_literal_global.1732
- ___block_literal_global.183
- ___block_literal_global.185
- ___block_literal_global.198
- ___block_literal_global.208
- ___block_literal_global.219
- ___block_literal_global.239
- ___block_literal_global.242
- ___block_literal_global.244
- ___block_literal_global.251
- ___block_literal_global.261
- ___block_literal_global.267
- ___block_literal_global.276
- ___block_literal_global.285
- ___block_literal_global.287
- ___block_literal_global.376
- ___block_literal_global.480
- ___block_literal_global.524
- ___block_literal_global.654
- ___block_literal_global.734
- ___block_literal_global.737
- ___block_literal_global.860
- ___block_literal_global.863
- ___block_literal_global.871
- ___block_literal_global.874
- ___block_literal_global.882
- ___block_literal_global.902
- ___block_literal_global.905
- ___block_literal_global.909
- ___block_literal_global.911
- _block_copy_helper.119
- _block_copy_helper.126
- _block_copy_helper.132
- _block_copy_helper.139
- _block_copy_helper.149
- _block_copy_helper.77
- _block_descriptor.121
- _block_descriptor.128
- _block_descriptor.134
- _block_descriptor.141
- _block_descriptor.151
- _block_descriptor.79
- _block_destroy_helper.120
- _block_destroy_helper.127
- _block_destroy_helper.133
- _block_destroy_helper.140
- _block_destroy_helper.150
- _block_destroy_helper.78
- _objc_msgSend$IATACode
- _objc_msgSend$_fuFlight
- _objc_msgSend$_fuFlightLeg
- _objc_msgSend$_sfAirportFromAirport:
- _objc_msgSend$_sfFlight
- _objc_msgSend$_sfFlightLeg
- _objc_msgSend$_sfFlightStatus
- _objc_msgSend$_sfPegasusFlightState
- _objc_msgSend$airline
- _objc_msgSend$airport
- _objc_msgSend$arrivalInfo
- _objc_msgSend$authorizationStatusForCapability:handler:
- _objc_msgSend$baggageClaim
- _objc_msgSend$computedFlightState
- _objc_msgSend$convertFlightModel:withError:
- _objc_msgSend$currentGateTime
- _objc_msgSend$currentProgress
- _objc_msgSend$currentRunwayTime
- _objc_msgSend$dateLastUpdated
- _objc_msgSend$dateOfNextExpectedUpdate
- _objc_msgSend$departureInfo
- _objc_msgSend$displayableEndDate
- _objc_msgSend$displayableStartDate
- _objc_msgSend$flightState
- _objc_msgSend$flightTimeStatus
- _objc_msgSend$gate
- _objc_msgSend$gateBufferMinutes
- _objc_msgSend$initWithAirlineCode:airlineName:flightNumber:operatorAirlineCode:operatorFlightNumber:departure:arrival:state:publishedDate:dataSource:
- _objc_msgSend$initWithAirport:terminal:gate:baggageClaim:status:scheduledGateTime:currentGateTime:scheduledRunwayTime:currentRunwayTime:gateBufferMinutes:runwayBufferMinutes:
- _objc_msgSend$initWithAirportCode:name:city:timeZone:location:
- _objc_msgSend$legs
- _objc_msgSend$localizedStringFromDate:dateStyle:timeStyle:
- _objc_msgSend$manifestFileForRegion:
- _objc_msgSend$operatorAirline
- _objc_msgSend$operatorFlightNumber
- _objc_msgSend$originalDate
- _objc_msgSend$queryStateOfRelevancyPresentmentWithType:associatedWithUniqueIdentifier:completion:
- _objc_msgSend$requestAuthorizationForCapability:handler:
- _objc_msgSend$requestState:forRelevancyPresentmentWithType:associatedWithUniqueIdentifier:completion:
- _objc_msgSend$resetAuthorizationForCapability:handler:
- _objc_msgSend$runwayBufferMinutes
- _objc_msgSend$scheduledRunwayTime
- _objc_msgSend$setArrivalAirport:
- _objc_msgSend$setArrivalGate:
- _objc_msgSend$setArrivalGateTime:
- _objc_msgSend$setArrivalPublishedTime:
- _objc_msgSend$setArrivalRunwayTime:
- _objc_msgSend$setArrivalTerminal:
- _objc_msgSend$setBaggageClaim:
- _objc_msgSend$setBufferMinutes:
- _objc_msgSend$setCarrierCode:
- _objc_msgSend$setCarrierName:
- _objc_msgSend$setCode:
- _objc_msgSend$setCurrent:
- _objc_msgSend$setDepartureAirport:
- _objc_msgSend$setDepartureGate:
- _objc_msgSend$setDepartureGateClosedTime:
- _objc_msgSend$setDeparturePublishedTime:
- _objc_msgSend$setDepartureRunwayTime:
- _objc_msgSend$setDepartureTerminal:
- _objc_msgSend$setGateArrivalTimes:
- _objc_msgSend$setGateDepartureTimes:
- _objc_msgSend$setLastUpdatedTime:
- _objc_msgSend$setLat:
- _objc_msgSend$setLegs:
- _objc_msgSend$setLng:
- _objc_msgSend$setOperatorCarrierCode:
- _objc_msgSend$setOperatorFlightNumber:
- _objc_msgSend$setPegasusDefinedState:
- _objc_msgSend$setProgress:
- _objc_msgSend$setRunwayArrivalTimes:
- _objc_msgSend$setRunwayDepartureTimes:
- _objc_msgSend$setScheduled:
- _objc_msgSend$setStaleDate:
- _objc_msgSend$setTimezone:
- _objc_msgSend$terminal
- _objc_msgSend$thumbnailCachePathForManifestHash:size:
CStrings:
+ "@104@0:8@16@24Q32@40Q48@56@64Q72@80@88Q96"
+ "@44@0:8@16{CGSize=dd}24B40"
+ "Attempting to map PKMerchantCategoryCount into FKPaymentTransactionCategory"
+ "CGImage"
+ "Clearing cached session identifiers and payment offers for pass %@, criteriaIdentifier %@"
+ "Error fetching %@ directory file protection. Error: %{public}@"
+ "LOCALIZED_CHARACTER_RANGE_FORMAT"
+ "LOCALIZED_ROW_AND_SEAT_NO_SPACE_FORMAT"
+ "LOCALIZED_ROW_AND_SEAT_WITH_SPACE_FORMAT"
+ "PDServer: failed to update data protection for %@."
+ "PKIdentityPassCredentialProperty"
+ "SupressLAAutoStart"
+ "T@\"NSArray\",&,N,V_excludedAccountStates"
+ "T@\"NSArray\",&,N,V_excludedPeerPaymentAccountStates"
+ "T@\"NSString\",&,N,V_backgroundColor"
+ "T@\"NSString\",&,N,V_foregroundColor"
+ "T@\"NSString\",C,N,V_docType"
+ "TB,N,GisRelevancyActive,V_relevancyActive"
+ "Td,R,N,V_progress"
+ "Updating %@ directory file protection..."
+ "[%s] Starting discovery and verifying proximity"
+ "[%s] Starting discovery over proximity channel"
+ "[%s] Starting discovery without verifying proximity"
+ "_displayableAirlineSeatsStringForRow:designations:"
+ "_displayableStringForDate:fromField:"
+ "_docType"
+ "_excludedAccountStates"
+ "_excludedPeerPaymentAccountStates"
+ "_fkPaymentTransactionCategory"
+ "_formatSeatLettersForRow:designations:includeSpaceBetweenRowAndSeats:"
+ "_formatSeatNumbersForRow:designations:formatter:includeSpaceBetweenRowAndSeats:"
+ "_formattedAirlineSeatsStringForRow:designation:includeSpaceBetweenRowAndSeats:"
+ "_initWithWebKitPropertyListData:"
+ "_isInRestrictedMode"
+ "_isInRestrictedModeTimestamp"
+ "_isStringAllLetters:"
+ "_isStringAllNumbers:formatter:"
+ "_markOfferConsumedForPassUniqueID:criteriaIdentifier:"
+ "_setIsInRestrictedMode:"
+ "_updatingIsInRestrictedMode"
+ "_webKitPropertyListData"
+ "accountWithIdentifier:error:"
+ "authorizationStatusForCapability:auditToken:"
+ "buttonType"
+ "catalogVersionChange"
+ "destinationTemperature"
+ "destinationWeatherConditionString"
+ "destinationWeatherSymbol"
+ "dismissed"
+ "eligibleForSmartButton"
+ "endDemo"
+ "excludedAccountStates"
+ "excludedPeerPaymentAccountStates"
+ "filterOutAccountStates:"
+ "filterOutPeerPaymentAccountStates:"
+ "fpanDescriptorAndCredentialForFPAN:completion:"
+ "fpanDescriptorAndCredentialForFPAN:descriptor:credential:error:"
+ "fpanDescriptorAndCredentialUsingFPAN:completion:"
+ "hasBackgroundColor"
+ "hasForegroundColor"
+ "holdNearReader"
+ "initWithAirlineCode:airlineName:flightNumber:operatorAirlineCode:operatorFlightNumber:departure:arrival:state:publishedDate:staleDate:dataSource:"
+ "initWithPassUniqueIdentifier:applicationIdentifier:subCredentialIdentifier:"
+ "initWithPassUniqueIdentifier:applicationIdentifier:subCredentialIdentifier:docType:"
+ "isDynamic"
+ "isEqualToPKIdentityPassCredentialProperty:"
+ "isRelevancyActive"
+ "manifestFileForRegion:planningToWrite:"
+ "manufacturerOrIssuerIdentifier"
+ "morePreferences"
+ "overrideStateOfRelevancyPresentmentOfType:containingPassUniqueIdentifier:newState:completion:"
+ "payWithPasscode"
+ "paymentOfferCatalogVersion"
+ "paymentOfferCatalogVersionChangeUpdatePeriod"
+ "paymentOfferCatalogVersionChangeUpdatePeriodForRegion:"
+ "paymentOfferCatalogVersionForRegion:"
+ "performProximityVerification"
+ "practiceAgain"
+ "preauthorizedPayments"
+ "preauthorizedPaymentsCount"
+ "prefillValuesWithFPAN:targetDevice:"
+ "prepareImageForDescriptor:"
+ "purgeResources"
+ "q56@0:8q16{?=[8I]}24"
+ "requestStateOfRelevancyPresentmentOfType:containingPassUniqueIdentifier:completion:"
+ "requestingAuthentication"
+ "resourceValuesForKeys:error:"
+ "revokePayment"
+ "revokePaymentAlert"
+ "setDocType:"
+ "setExcludedAccountStates:"
+ "setExcludedPeerPaymentAccountStates:"
+ "setResourceValues:error:"
+ "setUp"
+ "startDemo"
+ "stateOfRelevancyPresentmentOfType:containingPassUniqueIdentifier:"
+ "thumbnailCachePathForManifestHash:size:planningToWrite:"
+ "transactionCountForRequest:completion:"
+ "updatePaymentOfferCatalogVersion:shouldRemove:"
+ "userIntent"
+ "usingSynchronousProxy:accountWithIdentifier:completion:"
+ "v12@?0C8"
+ "v16@?0@\"NSNumber\"8"
+ "v32@0:8@\"NSString\"16@?<v@?@\"PKFPANCardDescriptor\"@\"PKAutoFillCardCredential\"@\"NSError\">24"
+ "v32@0:8@\"PKPaymentTransactionRequest\"16@?<v@?@\"NSNumber\">24"
+ "v32@?0@\"PKFPANCardDescriptor\"8@\"PKAutoFillCardCredential\"16@\"NSError\"24"
+ "v36@0:8B16@\"NSString\"20@?<v@?@\"PKAccount\"@\"NSError\">28"
+ "v48@0:8@\"NSString\"16^@24^@32^@40"
+ "v48@0:8@16^@24^@32^@40"
+ "v48@0:8Q16@\"NSString\"24Q32@?<v@?B@\"NSError\">40"
- "@40@0:8@16{CGSize=dd}24"
- "@96@0:8@16@24Q32@40Q48@56@64Q72@80Q88"
- "AppIcon-Rounded"
- "IATACode"
- "PKFlight: Failed to create FUFlight with error %@"
- "PKFlight: Recomputed estimates: estimates:%@;"
- "PKFlightEstimates"
- "T@\"NSDate\",R,N,V_staleDate"
- "TB,N,V_relevancyActive"
- "Td,N,V_progress"
- "_fuFlight"
- "_fuFlightLeg"
- "_sfAirportFromAirport:"
- "_sfFlight"
- "_sfFlightLeg"
- "_sfFlightStatus"
- "_sfPegasusFlightState"
- "_stateFromFUFlightState:"
- "arrivalInfo"
- "authorizationStatusForCapability:handler:"
- "com.apple.wallet.ecom.smartButtons.appBundleID"
- "com.apple.wallet.ecom.smartButtons.buttonType"
- "com.apple.wallet.ecom.smartButtons.buttonType.addMoney"
- "com.apple.wallet.ecom.smartButtons.buttonType.book"
- "com.apple.wallet.ecom.smartButtons.buttonType.buy"
- "com.apple.wallet.ecom.smartButtons.buttonType.checkout"
- "com.apple.wallet.ecom.smartButtons.buttonType.continue"
- "com.apple.wallet.ecom.smartButtons.buttonType.contribute"
- "com.apple.wallet.ecom.smartButtons.buttonType.donate"
- "com.apple.wallet.ecom.smartButtons.buttonType.inStore"
- "com.apple.wallet.ecom.smartButtons.buttonType.order"
- "com.apple.wallet.ecom.smartButtons.buttonType.plain"
- "com.apple.wallet.ecom.smartButtons.buttonType.reload"
- "com.apple.wallet.ecom.smartButtons.buttonType.rent"
- "com.apple.wallet.ecom.smartButtons.buttonType.setup"
- "com.apple.wallet.ecom.smartButtons.buttonType.subscribe"
- "com.apple.wallet.ecom.smartButtons.buttonType.support"
- "com.apple.wallet.ecom.smartButtons.buttonType.tip"
- "com.apple.wallet.ecom.smartButtons.buttonType.topUp"
- "com.apple.wallet.ecom.smartButtons.deviceType"
- "com.apple.wallet.ecom.smartButtons.environment"
- "com.apple.wallet.ecom.smartButtons.environment.inApp"
- "com.apple.wallet.ecom.smartButtons.errorType"
- "com.apple.wallet.ecom.smartButtons.eventType"
- "com.apple.wallet.ecom.smartButtons.isDynamic"
- "com.apple.wallet.ecom.smartButtons.issuer"
- "com.apple.wallet.ecom.smartButtons.networkName"
- "com.apple.wallet.ecom.smartButtons.osVersion"
- "com.apple.wallet.ecom.smartButtons.productSubType"
- "com.apple.wallet.ecom.smartButtons.referralSource.cardArt"
- "computedFlightState"
- "convertFlightModel:withError:"
- "currentProgress"
- "dateLastUpdated"
- "dateOfNextExpectedUpdate"
- "departureInfo"
- "flightState"
- "flightTimeStatus"
- "initWithAirlineCode:airlineName:flightNumber:operatorAirlineCode:operatorFlightNumber:departure:arrival:state:publishedDate:dataSource:"
- "initWithFUFlight:relevantLeg:"
- "localizedStringFromDate:dateStyle:timeStyle:"
- "manifestFileForRegion:"
- "natual"
- "operatorAirline"
- "progress: '%f'; "
- "queryStateOfRelevancyPresentmentWithType:associatedWithUniqueIdentifier:completion:"
- "recomputeEstimates"
- "requestAuthorizationForCapability:handler:"
- "requestState:forRelevancyPresentmentWithType:associatedWithUniqueIdentifier:completion:"
- "resetAuthorizationForCapability:handler:"
- "setArrivalAirport:"
- "setArrivalGate:"
- "setArrivalGateTime:"
- "setArrivalPublishedTime:"
- "setArrivalRunwayTime:"
- "setArrivalTerminal:"
- "setBufferMinutes:"
- "setCarrierCode:"
- "setCarrierName:"
- "setCurrent:"
- "setDepartureAirport:"
- "setDepartureGate:"
- "setDepartureGateClosedTime:"
- "setDeparturePublishedTime:"
- "setDepartureRunwayTime:"
- "setDepartureTerminal:"
- "setGateArrivalTimes:"
- "setGateDepartureTimes:"
- "setLastUpdatedTime:"
- "setLat:"
- "setLegs:"
- "setLng:"
- "setOperatorCarrierCode:"
- "setPegasusDefinedState:"
- "setProgress:"
- "setRunwayArrivalTimes:"
- "setRunwayDepartureTimes:"
- "setScheduled:"
- "setTimezone:"
- "stateOfRelevancyPresentmentWithType:associatedWithUniqueIdentifier:"
- "thumbnailCachePathForManifestHash:size:"
- "v32@0:8q16@?<v@?>24"
- "v32@0:8q16@?<v@?q>24"
- "v48@0:8Q16Q24@\"NSString\"32@?<v@?B@\"NSError\">40"
- "v48@0:8Q16Q24@32@?40"
- "\xb1"

```
