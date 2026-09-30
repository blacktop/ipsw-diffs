## PassKitCore

> `/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore`

```diff

-1642.5.12.3.0
-  __TEXT.__text: 0x840b64
-  __TEXT.__auth_stubs: 0x4a50
-  __TEXT.__objc_methlist: 0x6e58c
-  __TEXT.__const: 0x25118
+1642.5.14.3.0
+  __TEXT.__text: 0x8407d4
+  __TEXT.__auth_stubs: 0x4a60
+  __TEXT.__objc_methlist: 0x6e794
+  __TEXT.__const: 0x251a8
   __TEXT.__swift5_typeref: 0x637c
-  __TEXT.__cstring: 0x685f8
+  __TEXT.__cstring: 0x687a6
   __TEXT.__constg_swiftt: 0x53c8
   __TEXT.__swift5_reflstr: 0x466d
   __TEXT.__swift5_fieldmd: 0x55d8

   __TEXT.__swift5_proto: 0xcb8
   __TEXT.__swift5_types: 0x568
   __TEXT.__swift5_capture: 0x435c
-  __TEXT.__oslogstring: 0x35f2a
+  __TEXT.__oslogstring: 0x372bd
   __TEXT.__swift_as_entry: 0xa8
   __TEXT.__swift_as_ret: 0xa8
   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_mpenum: 0xf8
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x76f0
+  __TEXT.__gcc_except_tab: 0x779c
   __TEXT.__ustring: 0x1e7a
-  __TEXT.__unwind_info: 0x1f078
+  __TEXT.__unwind_info: 0x1f118
   __TEXT.__eh_frame: 0x4ba0
-  __TEXT.__objc_classname: 0x11089
-  __TEXT.__objc_methname: 0xd08fd
-  __TEXT.__objc_methtype: 0x19040
-  __TEXT.__objc_stubs: 0x5d4c0
-  __DATA_CONST.__got: 0x4b10
-  __DATA_CONST.__const: 0x21780
+  __TEXT.__objc_classname: 0x11092
+  __TEXT.__objc_methname: 0xd0d4d
+  __TEXT.__objc_methtype: 0x190ae
+  __TEXT.__objc_stubs: 0x5d660
+  __DATA_CONST.__got: 0x4b18
+  __DATA_CONST.__const: 0x21980
   __DATA_CONST.__objc_classlist: 0x3c00
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_protolist: 0x590
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23bf0
+  __DATA_CONST.__objc_selrefs: 0x23c70
   __DATA_CONST.__objc_protorefs: 0x250
   __DATA_CONST.__objc_superrefs: 0x3020
   __DATA_CONST.__objc_arraydata: 0x28e8
-  __AUTH_CONST.__auth_got: 0x2538
-  __AUTH_CONST.__const: 0x1fd40
-  __AUTH_CONST.__cfstring: 0x73200
-  __AUTH_CONST.__objc_const: 0xc7c08
+  __AUTH_CONST.__auth_got: 0x2540
+  __AUTH_CONST.__const: 0x1ecd8
+  __AUTH_CONST.__cfstring: 0x734e0
+  __AUTH_CONST.__objc_const: 0xc7e68
   __AUTH_CONST.__objc_arrayobj: 0xd68
   __AUTH_CONST.__objc_intobj: 0x1080
   __AUTH_CONST.__objc_dictobj: 0x15b8

   __AUTH.__data: 0x3eb0
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0x6e78
-  __DATA.__data: 0x8090
+  __DATA.__objc_ivar: 0x6e9c
+  __DATA.__data: 0x8068
   __DATA.__bss: 0x18400
   __DATA.__common: 0xc00
-  __DATA_DIRTY.__objc_ivar: 0x1e2c
+  __DATA_DIRTY.__objc_ivar: 0x1e34
   __DATA_DIRTY.__objc_data: 0x5988
   __DATA_DIRTY.__data: 0x188
   __DATA_DIRTY.__bss: 0x11d8

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9EF672F3-4A9F-35CD-9EAD-5AFF5C44923B
-  Functions: 50494
-  Symbols:   131187
-  CStrings:  68524
+  UUID: FE89C377-9D02-3AA7-88D9-BF96E6E8A9D2
+  Functions: 50554
+  Symbols:   131357
+  CStrings:  68678
 
Symbols:
+ +[PKCreditAccountController supportsCapability:forAccount:paymentApplicationState:dpanSuffix:]
+ +[PKDAManager isCarKeySupportedForManufacturerIdentifier:issuerIdentifier:productPlanIdentifier:error:]
+ +[PKTransitBalanceModel shouldCollectPlan:withAction:]
+ -[PKAutoFillCardCredential canCheckEligibility]
+ -[PKCloudStoreRecordFetchTask completeTaskWithError:throttled:]
+ -[PKCloudStoreRecordFetchTask isCompletedOrThrottled]
+ -[PKDashboardTransactionFetcher _excludedTransactionSourcesWithCompletion:]
+ -[PKDashboardTransactionFetcher filterExcludedTransactionSourceIdentifiers:]
+ -[PKDashboardTransactionFetcher preferredRecentTransactionMinimum]
+ -[PKDashboardTransactionFetcher sendTransactionsWithRequest:useSynchronous:completion:]
+ -[PKDashboardTransactionFetcher setPreferredRecentTransactionMinimum:]
+ -[PKPassLibrary _filterPassesForIssuerRegions:request:]
+ -[PKPassVerificationAppClipMethod usesExternalView]
+ -[PKPassVerificationIssuerAppMethod usesExternalView]
+ -[PKPassVerificationMethod usesExternalView]
+ -[PKPassVerificationMethodGroup usesExternalView]
+ -[PKPassVerificationPhoneCallMethod usesExternalView]
+ -[PKPassVerificationURLMethod usesExternalView]
+ -[PKPaymentDefaultDataProvider excludedTransactionSourceIdentifiersWithCompletion:]
+ -[PKPaymentDigitalIssuanceMetadata initWithDictionary:availableNetworks:]
+ -[PKPaymentDigitalIssuanceMetadata issuerRegions]
+ -[PKPaymentPassAction applyServiceProviderPropertiesToPaymentRequest:]
+ -[PKPaymentPassAction issuerRegions]
+ -[PKPaymentPassAction setIssuerRegions:]
+ -[PKPaymentProvisioningController isInProximitySetup]
+ -[PKPaymentProvisioningController locationManager:didFailWithError:]
+ -[PKPaymentProvisioningController setIsInProximitySetup:]
+ -[PKPaymentRemoteCredentialsRequest isInProximitySetup]
+ -[PKPaymentRemoteCredentialsRequest setIsInProximitySetup:]
+ -[PKPaymentRequest issuerRegions]
+ -[PKPaymentRequest setIssuerRegions:]
+ -[PKPaymentService excludedTransactionSourceIdentifiersWithCompletion:]
+ -[PKPaymentTransactionRequest excludedTransactionSourceIdentifiers]
+ -[PKPaymentTransactionRequest setExcludedTransactionSourceIdentifiers:]
+ -[PKProtobufPaymentRequest hasIssuerRegions]
+ -[PKProtobufPaymentRequest issuerRegions]
+ -[PKProtobufPaymentRequest setIssuerRegions:]
+ -[PKSecureElementProvisioningState hasAcquiredProvisioningAssertion]
+ -[PKSecureElementProvisioningState setHasAcquiredProvisioningAssertion:]
+ -[PKServiceProviderOrder issuerRegions]
+ -[PKServiceProviderOrder setIssuerRegions:]
+ -[PKServiceProviderPaymentRequest initWithServiceProviderOrder:action:]
+ -[PKSetupAssistantUtilityContext proximitySetupLiaison]
+ -[PKSetupAssistantUtilityContext setProximitySetupLiaison:]
+ -[PKUserNotificationReceipt accountBaseURL]
+ -[PKUserNotificationReceipt initWithNotificationIdentifier:accountIdentifier:accountBaseURL:]
+ -[PKUserNotificationReceipt setAccountBaseURL:]
+ GCC_except_table126
+ GCC_except_table151
+ GCC_except_table153
+ GCC_except_table160
+ GCC_except_table180
+ GCC_except_table188
+ GCC_except_table234
+ GCC_except_table280
+ GCC_except_table282
+ GCC_except_table298
+ GCC_except_table310
+ GCC_except_table315
+ GCC_except_table322
+ GCC_except_table326
+ GCC_except_table327
+ GCC_except_table345
+ GCC_except_table351
+ GCC_except_table360
+ GCC_except_table372
+ GCC_except_table381
+ GCC_except_table392
+ GCC_except_table397
+ GCC_except_table402
+ GCC_except_table415
+ GCC_except_table422
+ GCC_except_table424
+ GCC_except_table458
+ GCC_except_table463
+ GCC_except_table468
+ GCC_except_table481
+ GCC_except_table492
+ GCC_except_table528
+ GCC_except_table536
+ GCC_except_table546
+ GCC_except_table561
+ GCC_except_table562
+ GCC_except_table580
+ GCC_except_table748
+ GCC_except_table866
+ _.str.898
+ _OBJC_IVAR_$_PKDashboardTransactionFetcher._excludedTransactionSourceIdentifiers
+ _OBJC_IVAR_$_PKDashboardTransactionFetcher._filterExcludedTransactionSourceIdentifiers
+ _OBJC_IVAR_$_PKDashboardTransactionFetcher._preferredRecentTransactionMinimum
+ _OBJC_IVAR_$_PKPassVerificationMethod._usesExternalView
+ _OBJC_IVAR_$_PKPaymentDigitalIssuanceMetadata._issuerRegions
+ _OBJC_IVAR_$_PKPaymentPassAction._issuerRegions
+ _OBJC_IVAR_$_PKPaymentProvisioningController._isInProximitySetup
+ _OBJC_IVAR_$_PKPaymentRequest._issuerRegions
+ _OBJC_IVAR_$_PKPaymentTransactionRequest._excludedTransactionSourceIdentifiers
+ _OBJC_IVAR_$_PKSecureElementProvisioningState._hasAcquiredProvisioningAssertion
+ _OBJC_IVAR_$_PKServiceProviderOrder._issuerRegions
+ _OBJC_IVAR_$_PKSetupAssistantUtilityContext.proximitySetupLiaison
+ _OBJC_IVAR_$_PKUserNotificationReceipt._accountBaseURL
+ _PKAnalyticsReportPaymentRequestDelegateBundleID
+ _PKAnalyticsReportPaymentRequestDelegateDomain
+ _PKAnalyticsReportPaymentRequestIsDelegate
+ _PKAnalyticsReportSearchSummaryPageTag
+ _PKAnalyticsReportWalletSearchButtonTag
+ _PKAnalyticsReportWalletSearchCategoriesAvailable
+ _PKAnalyticsReportWalletSearchCategoriesButtonTag
+ _PKAnalyticsReportWalletSearchMerchantsAvailable
+ _PKAnalyticsReportWalletSearchMerchantsButtonTag
+ _PKAnalyticsReportWalletSearchOrdersButtonTag
+ _PKAnalyticsReportWalletSearchOthersButtonTag
+ _PKAnalyticsReportWalletSearchPageTag
+ _PKAnalyticsReportWalletSearchPassesAndTicketsButtonTag
+ _PKAnalyticsReportWalletSearchPendingPeerPaymentRequestsButtonTag
+ _PKAnalyticsReportWalletSearchRecentActivityButtonTag
+ _PKAnalyticsReportWalletSearchRecentOrdersAvailable
+ _PKAnalyticsReportWalletSearchRecentWalletActivityAvailable
+ _PKAnalyticsReportWalletSearchSearchBarButtonTag
+ _PKAnalyticsReportWalletSearchSearchResultsAvailable
+ _PKAnalyticsReportWalletSearchSeeAllTapped
+ _PKAnalyticsReportWalletSearchSharePassButtonTag
+ _PKAnalyticsReportWalletSearchTopHitButtonTag
+ _PKAnalyticsReportWalletSearchTransactionsButtonTag
+ _PKAnalyticsReportWalletSearchTriggeredFromExternalSource
+ _PKCanMakePaymentsUsingIssuerRegionsWithCapabilities
+ _PKCloudStoreOperationGroupSuffixViewedTransactionsResumingPowerThrottledFetch
+ _PKNormalizedPaymentNetworkName
+ _PKPaymentDigitalIssuanceMetadataIssuerRegionsKey
+ _PKPaymentNetworkElCorteIngles
+ _PKPaymentRequestIssuerRegionsKey
+ __OBJC_$_CLASS_METHODS_PKTransitBalanceModel
+ __PKGetAcceptedNetworksForIssuerRegion
+ __PKHasExistingPassesForNetworksAndCountries
+ ___100-[PKPassLibrary checkFidoKeyPresenceForRelyingParty:relyingPartyAccountHash:fidoKeyHash:completion:]_block_invoke.262
+ ___100-[PKPassLibrary inAppPrivateLabelPaymentPassesForWebDomain:issuerCountryCodes:isMultiTokensRequest:]_block_invoke.162
+ ___100-[PKPaymentService submitUserConfirmation:forTransactionIdentifier:sessionExchangeToken:completion:]_block_invoke.326
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke.545
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke.551
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_2.546
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_2.552
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_3.547
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_3.553
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_4.548
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_5.549
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_6.550
+ ___102-[PKPaymentService recordPaymentApplicationUsageForPassUniqueIdentifier:paymentApplicationIdentifier:]_block_invoke.250
+ ___103-[PKPaymentService submitTransactionSignatureForTransactionIdentifier:sessionExchangeToken:completion:]_block_invoke.329
+ ___105-[PKPaymentService augmentedProductForInstallmentConfiguration:experimentDetails:feature:withCompletion:]_block_invoke.345
+ ___106-[PKPaymentService submitBarcodePaymentEvent:forPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.331
+ ___107-[PKPaymentService registerAuxiliaryCapabilityForPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.313
+ ___107-[PKPaymentService retrieveDecryptedBarcodeCredentialForPassUniqueIdentifier:authorization:withCompletion:]_block_invoke.317
+ ___108-[PKPassLibrary createFidoKeyForRelyingParty:relyingPartyAccountHash:challenge:externalizedAuth:completion:]_block_invoke.260
+ ___109-[PKPaymentService conflictingExpressPassIdentifiersForPassInformation:withReferenceExpressState:completion:]_block_invoke.238
+ ___110-[PKPassLibrary overrideStateOfRelevancyPresentmentOfType:containingPassUniqueIdentifier:newState:completion:]_block_invoke.280
+ ___111-[PKPaymentProvisioningController resolveLocalEligibilityRequirementsForAppleBalanceCredential:withCompletion:]_block_invoke.584
+ ___111-[PKPaymentProvisioningController resolveLocalEligibilityRequirementsForAppleBalanceCredential:withCompletion:]_block_invoke.592
+ ___111-[PKPaymentService conflictingExpressPassIdentifiersForPassConfiguration:withReferenceExpressState:completion:]_block_invoke.237
+ ___112-[PKPassLibrary inAppPrivateLabelPaymentPassesForApplicationIdentifier:issuerCountryCodes:isMultiTokensRequest:]_block_invoke.160
+ ___112-[PKPaymentService retrievePINEncryptionCertificateForPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.321
+ ___115-[PKPassLibrary hasInAppPrivateLabelPaymentPassesForWebDomain:issuerCountryCodes:isMultiTokensRequest:withHandler:]_block_invoke.163
+ ___115-[PKPaymentService passUniqueIdentifierForTransactionWithServiceIdentifier:transactionSourceIdentifier:completion:]_block_invoke.183
+ ___117-[PKPaymentService insertOrUpdateValueAddedServiceTransaction:forPassUniqueIdentifier:paymentTransaction:completion:]_block_invoke.216
+ ___125+[PKPaymentSetupAssistantRegistrationUtilities preflightPaymentSetupProvisioningController:forSetupAssistant:withCompletion:]_block_invoke.149
+ ___125+[PKPaymentSetupAssistantRegistrationUtilities preflightPaymentSetupProvisioningController:forSetupAssistant:withCompletion:]_block_invoke.150
+ ___125-[PKPaymentService recordPassTransactionActivitySummaryForPassUniqueIdentifier:paymentApplicationIdentifier:presentmentType:]_block_invoke.249
+ ___127-[PKPassLibrary hasInAppPrivateLabelPaymentPassesForApplicationIdentifier:issuerCountryCodes:isMultiTokensRequest:withHandler:]_block_invoke.161
+ ___128-[PKPaymentService retrieveDecryptedBarcodeCredentialForPassUniqueIdentifier:authorization:sessionExchangeToken:withCompletion:]_block_invoke.319
+ ___132-[PKDashboardTransactionFetcher _processPaymentPassTransactionsWithTransactions:synchronous:currentMonthOnly:sendTransactionsBlock:]_block_invoke.91
+ ___132-[PKDashboardTransactionFetcher _processPaymentPassTransactionsWithTransactions:synchronous:currentMonthOnly:sendTransactionsBlock:]_block_invoke_2.93
+ ___134-[PKPassLibrary hasInAppPaymentPassesForNetworks:capabilities:issuerCountryCodes:paymentRequestType:isMultiTokensRequest:withHandler:]_block_invoke.159
+ ___140-[PKPassLibrary configureHomeAuxiliaryCapabilitiesForSerialNumber:homeIdentifier:fromUnifiedAccessDescriptor:andAliroDescriptor:completion:]_block_invoke.190
+ ___140-[PKPaymentService rangingSuspensionReasonForAppletSubcredentialIdentifier:paymentApplicationIdentifier:secureElementIdentifier:completion:]_block_invoke.293
+ ___142-[PKPassLibrary signWithFidoKeyForRelyingParty:relyingPartyAccountHash:fidoKeyHash:challenge:publicKeyIdentifier:externalizedAuth:completion:]_block_invoke.263
+ ___149-[PKPaymentService processTransitTransactionEventWithHistory:transactionDate:forPaymentApplication:withPassUniqueIdentifier:expressTransactionState:]_block_invoke.248
+ ___155-[PKPassLibrary requestPersonalizationOfPassWithUniqueIdentifier:contact:personalizationToken:requiredPersonalizationFields:personalizationSource:handler:]_block_invoke.214
+ ___31-[PKPassLibrary backupMetadata]_block_invoke.254
+ ___35-[PKPassLibrary setBackupMetadata:]_block_invoke.255
+ ___36-[PKPaymentService consistencyCheck]_block_invoke.267
+ ___41-[PKPassLibrary archivePassWithUniqueID:]_block_invoke.300
+ ___41-[PKPassLibrary recoverPassWithUniqueID:]_block_invoke.299
+ ___43-[PKPassLibrary expressFelicaTransitPasses]_block_invoke.233
+ ___43-[PKPaymentService productsWithCompletion:]_block_invoke.361
+ ___44-[PKPaymentService initializeSecureElement:]_block_invoke.226
+ ___45-[PKPaymentService insertUserLegalAgreement:]_block_invoke.404
+ ___47-[PKPassLibrary unexpiredPassesOrderedByGroup:]_block_invoke.165
+ ___48-[PKPassLibrary exportableCardEntry:completion:]_block_invoke.278
+ ___48-[PKPaymentService mapsMerchantsWithCompletion:]_block_invoke.187
+ ___49-[PKPaymentService currentSecureElementSnapshot:]_block_invoke.392
+ ___49-[PKPaymentService deleteReservation:completion:]_block_invoke.396
+ ___50-[PKPassLibrary exportableManifestWithCompletion:]_block_invoke.276
+ ___50-[PKPaymentService sharedPaymentWebServiceContext]_block_invoke.286
+ ___50-[PKPaymentService submitApplyRequest:completion:]_block_invoke.349
+ ___50-[PKPaymentService submitTermsRequest:completion:]_block_invoke.353
+ ___51-[PKPassLibrary resetApplePayWithDiagnosticReason:]_block_invoke.304
+ ___51-[PKPaymentService logoImageDataForURL:completion:]_block_invoke.179
+ ___51-[PKPaymentService productsWithRequest:completion:]_block_invoke.359
+ ___51-[PKPaymentService submitDeleteRequest:completion:]_block_invoke.354
+ ___52-[PKPassLibrary passLocalizedStringForKey:uniqueID:]_block_invoke.172
+ ___52-[PKPaymentAuthorizationDataModel unavailablePasses]_block_invoke.185
+ ___53-[PKPassLibrary canPresentPaymentRequest:completion:]_block_invoke.199
+ ___53-[PKPaymentService submitDocumentRequest:completion:]_block_invoke.351
+ ___54-[PKPassLibrary addISO18013Blobs:cardType:completion:]_block_invoke.269
+ ___54-[PKPassLibrary defaultPaymentPassesWithRemotePasses:]_block_invoke.232
+ ___54-[PKPaymentService featureApplicationsWithCompletion:]_block_invoke.347
+ ___54-[PKPaymentService regionsWithIdentifiers:completion:]_block_invoke.296
+ ___55-[PKPassLibrary _filterPassesForIssuerRegions:request:]_block_invoke
+ ___55-[PKPaymentService performDeviceCheckInWithCompletion:]_block_invoke.358
+ ___55-[PKPaymentService pushProvisioningSharingIdentifiers:]_block_invoke.379
+ ___56-[PKPaymentService credentialWithIdentifier:completion:]_block_invoke.375
+ ___57-[PKPassLibrary _defaultPaymentPassWithoutPaymentRequest]_block_invoke.243
+ ___57-[PKPassLibrary addPassesWithData:withCompletionHandler:]_block_invoke.174
+ ___57-[PKPassLibrary removePassWithUniqueID:diagnosticReason:]_block_invoke.297
+ ___57-[PKPassLibrary removePassesOfType:withDiagnosticReason:]_block_invoke.301
+ ___57-[PKPaymentService regionsMatchingName:types:completion:]_block_invoke.297
+ ___57-[PKPaymentService submitVerificationRequest:completion:]_block_invoke.352
+ ___58-[PKPassLibrary addPassesContainer:withCompletionHandler:]_block_invoke.177
+ ___58-[PKPassLibrary meetsProvisioningRequirements:completion:]_block_invoke.223
+ ___58-[PKPassLibrary prepareForBackupRestoreWithSafeHavenPath:]_block_invoke.259
+ ___58-[PKPaymentService familyMembersIgnoringCache:completion:]_block_invoke.332
+ ___59-[PKPaymentService memberTypeForCurrentUserWithCompletion:]_block_invoke.333
+ ___59-[PKPaymentService performProductActionRequest:completion:]_block_invoke.362
+ ___59-[PKPaymentService requiresUpgradedPasscodeWithCompletion:]_block_invoke.311
+ ___59-[PKPaymentService storeTransactionReceiptData:completion:]_block_invoke.400
+ ___59-[PKPaymentService subcredentialInvitationsWithCompletion:]_block_invoke.369
+ ___60-[PKPassLibrary passUniqueIDsMatchingSearchTerm:completion:]_block_invoke.166
+ ___60-[PKPassLibrary removePassesWithUniqueIDs:diagnosticReason:]_block_invoke.298
+ ___60-[PKPaymentProvisioningController _noteProvisioningDidBegin]_block_invoke.625
+ ___61-[PKPassLibrary availableHomeKeyPassesWithCompletionHandler:]_block_invoke.183
+ ___61-[PKPaymentProvisioningController retrieveRemoteCredentials:]_block_invoke.307
+ ___61-[PKPaymentProvisioningController retrieveRemoteCredentials:]_block_invoke.309
+ ___61-[PKPaymentProvisioningController retrieveRemoteCredentials:]_block_invoke_2.310
+ ___61-[PKPaymentService changePasscodeFrom:toPasscode:completion:]_block_invoke.312
+ ___61-[PKPaymentService statusForShareableCredentials:completion:]_block_invoke.382
+ ___62-[PKPassLibrary addSharedFlight:fromSenderAddress:completion:]_block_invoke.217
+ ___62-[PKPassLibrary canAddCarKeyPassWithConfiguration:completion:]_block_invoke.221
+ ___62-[PKPassLibrary enabledValueAddedServicePassesWithCompletion:]_block_invoke.164
+ ___62-[PKPassLibrary resetApplePayWithDiagnosticReason:completion:]_block_invoke.303
+ ___62-[PKPaymentService addRemoteDevicePendingProvisioningReceipt:]_block_invoke.301
+ ___62-[PKPaymentService generateUnderlyingKeyReportWithCompletion:]_block_invoke.307
+ ___62-[PKPaymentService transactionReceiptWithUniqueID:completion:]_block_invoke.397
+ ___62-[PKPaymentService transactionsForPredicate:limit:completion:]_block_invoke.181
+ ___63-[PKPassLibrary addUnsignedPassesAtURLs:withCompletionHandler:]_block_invoke.179
+ ___63-[PKPassLibrary addUnsignedPassesAtURLs:withCompletionHandler:]_block_invoke_2.180
+ ___63-[PKPaymentService currentPasscodeMeetsUpgradedPasscodePolicy:]_block_invoke.310
+ ___63-[PKPaymentService photosForFamilyMembersWithDSIDs:completion:]_block_invoke.336
+ ___63-[PKPaymentService refreshMerchantTokenMetadataWithCompletion:]_block_invoke.299
+ ___63-[PKPaymentService removeExpressPassesWithCardType:completion:]_block_invoke.242
+ ___64-[PKPassLibrary replaceUnsignedPassAtURL:withCompletionHandler:]_block_invoke.186
+ ___64-[PKPassLibrary replaceUnsignedPassAtURL:withCompletionHandler:]_block_invoke_2.187
+ ___64-[PKPaymentProvisioningController performDeviceCheckInIfNeeded:]_block_invoke.295
+ ___64-[PKPaymentService enforceUpgradedPasscodePolicyWithCompletion:]_block_invoke.309
+ ___64-[PKPaymentService featureApplicationWithIdentifier:completion:]_block_invoke.348
+ ___64-[PKPaymentService passOwnershipTokenWithIdentifier:completion:]_block_invoke.363
+ ___64-[PKPaymentService redeemPaymentShareableCredential:completion:]_block_invoke.388
+ ___64-[PKPaymentService revokeCredentialsWithIdentifiers:completion:]_block_invoke.373
+ ___65-[PKPassLibrary paymentSetupFeaturesForConfiguration:completion:]_block_invoke.197
+ ___65-[PKPaymentService isPassExpressWithUniqueIdentifier:completion:]_block_invoke.247
+ ___65-[PKPaymentService notifyForFPANCardImportConsentWithCompletion:]_block_invoke.303
+ ___65-[PKPaymentService passSharesForCredentialIdentifier:completion:]_block_invoke.377
+ ___65-[PKPaymentService pendingFamilyMembersIgnoringCache:completion:]_block_invoke.335
+ ___65-[PKPaymentService revokeMerchantTokenWithIdentifier:completion:]_block_invoke.300
+ ___65-[PKPaymentService sharedPaymentWebServiceContextWithCompletion:]_block_invoke.288
+ ___65-[PKPaymentService transactionsTotalAmountForRequest:completion:]_block_invoke.177
+ ___66-[PKPaymentService defaultPaymentPassIngestionSpecificIdentifier:]_block_invoke.337
+ ___66-[PKPaymentService registerCredentialsWithIdentifiers:completion:]_block_invoke.371
+ ___66-[PKPaymentService setBalanceReminder:forBalance:pass:completion:]_block_invoke.199
+ ___67-[PKPassLibrary canAddSecureElementPassWithConfiguration:outError:]_block_invoke.219
+ ___67-[PKPassLibrary presentPaymentSetupRequest:orientation:completion:]_block_invoke.196
+ ___67-[PKPassLibrary sortedTransitPassesForAppletDataFormat:completion:]_block_invoke.235
+ ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.332
+ ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.339
+ ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.348
+ ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.356
+ ___67-[PKPaymentService addPlaceholderPassWithConfiguration:completion:]_block_invoke.367
+ ___67-[PKPaymentService clearFPANCardImportNotificationsWithCompletion:]_block_invoke.305
+ ___67-[PKPaymentService redeemProvisioningSharingIdentifier:completion:]_block_invoke.390
+ ___67-[PKPaymentService requestNotificationAuthorizationWithCompletion:]_block_invoke.271
+ ___68-[PKPassLibrary getContainmentStatusAndSettingsForPass:withHandler:]_block_invoke.215
+ ___68-[PKPassLibrary prepareForBackupRestoreWithExistingPreferencesData:]_block_invoke.256
+ ___68-[PKPassLibrary removePassesOfType:withDiagnosticReason:completion:]_block_invoke.302
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke.235
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke.237
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke.243
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke.250
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke.253
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke.270
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke.276
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_2.238
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_2.245
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_2.251
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_2.254
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_2.271
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_2.277
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_3.252
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_3.255
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_3.282
+ ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_4.256
+ ___68-[PKPaymentService deleteTransactionReceiptWithUniqueID:completion:]_block_invoke.401
+ ___68-[PKPaymentService updateAllMapsBrandAndMerchantDataWithCompletion:]_block_invoke.289
+ ___69-[PKPassLibrary addISO18013BlobsFromCredentials:cardType:completion:]_block_invoke.268
+ ___69-[PKPassLibrary canAddSecureElementPassWithConfiguration:completion:]_block_invoke.220
+ ___69-[PKPassLibrary configurePushProvisioningConfigurationV2:completion:]_block_invoke.249
+ ___69-[PKPassLibrary configurePushProvisioningConfigurationV2:completion:]_block_invoke.250
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.354
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.356
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.363
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.365
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.374
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.382
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.387
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_2.366
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_2.375
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_2.384
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_2.388
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_3.368
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_3.377
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_3.385
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_3.390
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_4.369
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_4.386
+ ___69-[PKPaymentService featureApplicationsForProvisioningWithCompletion:]_block_invoke.341
+ ___69-[PKPaymentService initializeSecureElementIfNecessaryWithCompletion:]_block_invoke.224
+ ___69-[PKPaymentService removeExpressPassWithUniqueIdentifier:completion:]_block_invoke.244
+ ___69-[PKPaymentService reserveStorageForAppletTypes:metadata:completion:]_block_invoke.394
+ ___69-[PKPaymentService setExpressWithPassInformation:credential:handler:]_block_invoke.241
+ ___70-[PKPassLibrary addPassesWithIngestionPayloads:withCompletionHandler:]_block_invoke.175
+ ___70-[PKPassLibrary pushProvisioningNoncesWithCredentialCount:completion:]_block_invoke.244
+ ___70-[PKPassLibrary requestUpdateOfObjectWithUniqueIdentifier:completion:]_block_invoke.213
+ ___70-[PKPassLibrary sendRKEPassThroughMessage:forSessionIdentifier:error:]_block_invoke.253
+ ___70-[PKPaymentAuthorizationDataModel acceptedPaymentApplicationsForPass:]_block_invoke
+ ___70-[PKPaymentAuthorizationDataModel acceptedPaymentApplicationsForPass:]_block_invoke.175
+ ___70-[PKPaymentAuthorizationDataModel acceptedPaymentApplicationsForPass:]_block_invoke_2
+ ___70-[PKPaymentService accountAttestationAnonymizationSaltWithCompletion:]_block_invoke.364
+ ___70-[PKPaymentService revokeCredentialsWithReaderIdentifiers:completion:]_block_invoke.374
+ ___70-[PKPaymentService suggestPaymentFPANCredentialImport:withCompletion:]_block_invoke.302
+ ___71-[PKPassLibrary paymentPassWithAssociatedAccountIdentifier:completion:]_block_invoke.198
+ ___71-[PKPaymentService excludedTransactionSourceIdentifiersWithCompletion:]_block_invoke
+ ___71-[PKPaymentService excludedTransactionSourceIdentifiersWithCompletion:]_block_invoke.176
+ ___71-[PKPaymentService excludedTransactionSourceIdentifiersWithCompletion:]_block_invoke_2
+ ___71-[PKPaymentService featureApplicationsForAccountIdentifier:completion:]_block_invoke.338
+ ___71-[PKPaymentService plansForPaymentPassWithUniqueIdentifier:completion:]_block_invoke.196
+ ___71-[PKPaymentService removeExpressPassWithUniqueIdentifierV2:completion:]_block_invoke.243
+ ___71-[PKPaymentService setExpressWithPassConfiguration:credential:handler:]_block_invoke.239
+ ___72-[PKPassLibrary fetchHomePaymentApplicationsForSerialNumber:completion:]_block_invoke.192
+ ___72-[PKPassLibrary provisionHomeKeyPassForSerialNumbers:completionHandler:]_block_invoke.181
+ ___72-[PKPaymentProvisioningController _identityConfigurationWithCompletion:]_block_invoke.487
+ ___72-[PKPaymentProvisioningController _identityConfigurationWithCompletion:]_block_invoke.488
+ ___73-[PKPassLibrary generateAuxiliaryCapabilitiesForRequirements:completion:]_block_invoke.271
+ ___73-[PKPaymentAuthorizationStateMachine _performRewrapRequestImplWithParam:]_block_invoke.301
+ ___73-[PKPaymentAuthorizationStateMachine _performRewrapRequestImplWithParam:]_block_invoke.305
+ ___73-[PKPaymentAuthorizationStateMachine _performRewrapRequestImplWithParam:]_block_invoke_2.308
+ ___73-[PKPaymentDigitalIssuanceMetadata initWithDictionary:availableNetworks:]_block_invoke
+ ___73-[PKPaymentService ambiguousTransactionWithServiceIdentifier:completion:]_block_invoke.403
+ ___73-[PKPaymentService clearFPANCardImportNotificationHistoryWithCompletion:]_block_invoke.306
+ ___73-[PKPaymentService featureApplicationWithReferenceIdentifier:completion:]_block_invoke.343
+ ___74-[PKPassLibrary signData:signatureEntanglementMode:withCompletionHandler:]_block_invoke.274
+ ___74-[PKPaymentService balancesForPaymentPassWithUniqueIdentifier:completion:]_block_invoke.195
+ ___74-[PKPaymentService messagesForPaymentPassWithUniqueIdentifier:completion:]_block_invoke.194
+ ___74-[PKPaymentService notifyForFPANCardImportWithCredentials:withCompletion:]_block_invoke.304
+ ___74-[PKPaymentService setAccountAttestationAnonymizationSalt:withCompletion:]_block_invoke.366
+ ___74-[PKPaymentService setCommutePlanReminder:forCommutePlan:pass:completion:]_block_invoke.203
+ ___74-[PKPaymentService valueAddedServiceTransactionWithIdentifier:completion:]_block_invoke.219
+ ___74-[PKPaymentSetupAssistantCoreController _expressSetupProvisioningContext:]_block_invoke.177
+ ___74-[PKPaymentSetupAssistantCoreController _expressSetupProvisioningContext:]_block_invoke_2.179
+ ___75-[PKDashboardTransactionFetcher _excludedTransactionSourcesWithCompletion:]_block_invoke
+ ___75-[PKDashboardTransactionFetcher _excludedTransactionSourcesWithCompletion:]_block_invoke_2
+ ___75-[PKPaymentService balanceReminderThresholdForBalance:pass:withCompletion:]_block_invoke.197
+ ___75-[PKPaymentService commutePlanReminderForCommputePlan:pass:withCompletion:]_block_invoke.201
+ ___75-[PKPaymentService prepareProvisioningTarget:checkFamilyCircle:completion:]_block_invoke.385
+ ___75-[PKPaymentService submitEncryptedPIN:forTransactionIdentifier:completion:]_block_invoke.327
+ ___75-[PKPaymentService transactionTagsForTransactionWithIdentifier:completion:]_block_invoke.402
+ ___77-[PKPaymentRequirementsRequest _urlRequestWithBuilder:webService:completion:]_block_invoke.398
+ ___77-[PKPaymentService sendDeviceSharingCapabilitiesRequestForHandle:completion:]_block_invoke.405
+ ___77-[PKPaymentService updateFeatureApplicationsForAccountIdentifier:completion:]_block_invoke.339
+ ___77-[PKPaymentService updateMetadataOnPassWithIdentifier:credential:completion:]_block_invoke.370
+ ___78-[PKPassLibrary generateSEEncryptionCertificateForSubCredentialId:completion:]_block_invoke.265
+ ___78-[PKPaymentProvisioningController _requestProvisioning:withCompletionHandler:]_block_invoke.657
+ ___78-[PKPaymentProvisioningController _requestProvisioning:withCompletionHandler:]_block_invoke_2.658
+ ___78-[PKPaymentService categoryVisualizationMagnitudesForPassUniqueID:completion:]_block_invoke.357
+ ___78-[PKPaymentService featureApplicationsForAccountUserInvitationWithCompletion:]_block_invoke.342
+ ___78-[PKPaymentService requestNotificationAuthorizationIfNecessaryWithCompletion:]_block_invoke.270
+ ___78-[PKPaymentSetupAssistantCoreController _hasManuallyAddedSecureElementPasses:]_block_invoke.175
+ ___79-[PKPassLibrary _fetchContentForUniqueID:usingSynchronousProxy:withCompletion:]_block_invoke.226
+ ___79-[PKPassLibrary generateISOEncryptionCertificateForSubCredentialId:completion:]_block_invoke.266
+ ___79-[PKPassLibrary sortedTransitPassesForTransitNetworkIdentifiersWithCompletion:]_block_invoke.234
+ ___79-[PKPaymentProvisioningController _associateCredentials:withCompletionHandler:]_block_invoke.387
+ ___79-[PKPaymentService submitUserConfirmation:forTransactionIdentifier:completion:]_block_invoke.324
+ ___80-[PKPassLibrary presentContactlessInterfaceForDefaultPassFromSource:completion:]_block_invoke.201
+ ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.413
+ ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.420
+ ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.429
+ ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.441
+ ___80-[PKPaymentProvisioningController requestPurchasesForProduct:completionHandler:]_block_invoke.531
+ ___80-[PKPaymentProvisioningController requestPurchasesForProduct:completionHandler:]_block_invoke.534
+ ___80-[PKPaymentService passUniqueIdentifierForTransactionWithIdentifier:completion:]_block_invoke.182
+ ___82-[PKPassLibrary startVehicleConnectionSessionWithPassUniqueIdentifier:completion:]_block_invoke.252
+ ___82-[PKPaymentService markAuthenticationCompleteForTransactionIdentifier:completion:]_block_invoke.323
+ ___83-[PKPassLibrary containsPassWithPassTypeIdentifier:serialNumber:completionHandler:]_block_invoke.168
+ ___83-[PKPaymentService mapsMerchantWithIdentifier:resultProviderIdentifier:completion:]_block_invoke.290
+ ___83-[PKPaymentService saveProvisioningSupportData:forPassUniqueIdentifier:completion:]_block_invoke.380
+ ___83-[PKPaymentService transactionsRequiringReviewForAccountWithIdentifier:completion:]_block_invoke.356
+ ___84-[PKPaymentAuthorizationDataModel _filterAndProcessPaymentPassesUsingConfiguration:]_block_invoke.148
+ ___84-[PKPaymentAuthorizationDataModel _filterAndProcessPaymentPassesUsingConfiguration:]_block_invoke.155
+ ___84-[PKPaymentService passUniqueIdentifiersForTransactionSourceIdentifiers:completion:]_block_invoke.184
+ ___84-[PKPaymentService setDefaultPaymentApplication:forPassUniqueIdentifier:completion:]_block_invoke.221
+ ___85-[PKPaymentProvisioningController _setupAccountCredentialForProvisioning:completion:]_block_invoke.554
+ ___85-[PKPaymentProvisioningController _setupAccountCredentialForProvisioning:completion:]_block_invoke.556
+ ___85-[PKPaymentProvisioningController _setupAccountCredentialForProvisioning:completion:]_block_invoke_2.558
+ ___85-[PKPaymentService setDefaultExpressTransitPassIdentifier:withCredential:completion:]_block_invoke.229
+ ___85-[PKPaymentService submitBarcodePaymentEvent:forPassUniqueIdentifier:withCompletion:]_block_invoke.330
+ ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke.511
+ ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke.514
+ ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke_2.516
+ ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke_3.517
+ ___86-[PKPaymentService userNotificationActionPerformed:notificationIdentifier:completion:]_block_invoke.273
+ ___87-[PKDashboardTransactionFetcher sendTransactionsWithRequest:useSynchronous:completion:]_block_invoke
+ ___87-[PKDashboardTransactionFetcher sendTransactionsWithRequest:useSynchronous:completion:]_block_invoke_10
+ ___87-[PKDashboardTransactionFetcher sendTransactionsWithRequest:useSynchronous:completion:]_block_invoke_11
+ ___87-[PKDashboardTransactionFetcher sendTransactionsWithRequest:useSynchronous:completion:]_block_invoke_12
+ ___87-[PKDashboardTransactionFetcher sendTransactionsWithRequest:useSynchronous:completion:]_block_invoke_13
+ ___87-[PKDashboardTransactionFetcher sendTransactionsWithRequest:useSynchronous:completion:]_block_invoke_14
+ ___87-[PKDashboardTransactionFetcher sendTransactionsWithRequest:useSynchronous:completion:]_block_invoke_15
+ ___87-[PKDashboardTransactionFetcher sendTransactionsWithRequest:useSynchronous:completion:]_block_invoke_16
+ ___87-[PKDashboardTransactionFetcher sendTransactionsWithRequest:useSynchronous:completion:]_block_invoke_17
+ ___87-[PKDashboardTransactionFetcher sendTransactionsWithRequest:useSynchronous:completion:]_block_invoke_2
+ ___87-[PKDashboardTransactionFetcher sendTransactionsWithRequest:useSynchronous:completion:]_block_invoke_3
+ ___87-[PKDashboardTransactionFetcher sendTransactionsWithRequest:useSynchronous:completion:]_block_invoke_4
+ ___87-[PKDashboardTransactionFetcher sendTransactionsWithRequest:useSynchronous:completion:]_block_invoke_5
+ ___87-[PKDashboardTransactionFetcher sendTransactionsWithRequest:useSynchronous:completion:]_block_invoke_6
+ ___87-[PKDashboardTransactionFetcher sendTransactionsWithRequest:useSynchronous:completion:]_block_invoke_7
+ ___87-[PKDashboardTransactionFetcher sendTransactionsWithRequest:useSynchronous:completion:]_block_invoke_8
+ ___87-[PKDashboardTransactionFetcher sendTransactionsWithRequest:useSynchronous:completion:]_block_invoke_9
+ ___87-[PKPassLibrary _getGroupsControllerSnapshotWithOptions:synchronously:retries:handler:]_block_invoke.327
+ ___87-[PKPassLibrary _getGroupsControllerSnapshotWithOptions:synchronously:retries:handler:]_block_invoke.328
+ ___87-[PKPassLibrary generateTransactionKeyWithReaderIdentifier:readerPublicKey:completion:]_block_invoke.188
+ ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.453
+ ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.459
+ ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.470
+ ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.479
+ ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke_2.480
+ ___87-[PKPaymentService conflictingExpressPassIdentifiersForPassInformation:withCompletion:]_block_invoke.236
+ ___87-[PKPaymentService transitStateWithPassUniqueIdentifier:paymentApplication:completion:]_block_invoke.253
+ ___88-[PKPaymentAuthorizationStateMachine _performPrepareTransactionDetailsRequestWithParam:]_block_invoke.292
+ ___88-[PKPaymentAuthorizationStateMachine _performPrepareTransactionDetailsRequestWithParam:]_block_invoke_2.294
+ ___88-[PKPaymentService valueAddedServiceTransactionsForPaymentTransaction:limit:completion:]_block_invoke.218
+ ___89-[PKPassLibrary _activateSecureElementPass:withActivationCode:activationData:completion:]_block_invoke.212
+ ___89-[PKPassLibrary longTermPrivacyKeyForCredentialGroupIdentifier:reuseExisting:completion:]_block_invoke.270
+ ___89-[PKPaymentService conflictingExpressPassIdentifiersForPassConfiguration:withCompletion:]_block_invoke.235
+ ___89-[PKPaymentService processedAuthenticationMechanism:forTransactionIdentifier:completion:]_block_invoke.322
+ ___89-[PKPaymentService submitTransactionAnswerForTransaction:questionType:answer:completion:]_block_invoke.355
+ ___90-[PKPaymentService clearProvisioningSupportDataOfType:forPassUniqueIdentifier:completion:]_block_invoke.381
+ ___91-[PKPassLibrary enableExpressForPassWithPassTypeIdentifier:serialNumber:completionHandler:]_block_invoke.193
+ ___91-[PKPaymentProvisioningController verifyPassIsSupportedForExpressInLocalMarket:completion:]_block_invoke.664
+ ___91-[PKPaymentProvisioningController verifyPassIsSupportedForExpressInLocalMarket:completion:]_block_invoke.667
+ ___91-[PKPaymentProvisioningController verifyPassIsSupportedForExpressInLocalMarket:completion:]_block_invoke.669
+ ___91-[PKPaymentService retrievePINEncryptionCertificateForPassUniqueIdentifier:withCompletion:]_block_invoke.320
+ ___91-[PKPaymentService setDefaultExpressFelicaTransitPassIdentifier:withCredential:completion:]_block_invoke.227
+ ___93-[PKPaymentService cancelAutoTopUpForPassWithUniqueIdentifier:balanceIdentifiers:completion:]_block_invoke.200
+ ___93-[PKPaymentService fetchBarcodesForPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.315
+ ___93-[PKPaymentService transactionsRelatedToTransaction:transactionSourceIdentifiers:completion:]_block_invoke.212
+ ___94-[PKPassLibrary presentContactlessInterfaceForPassWithUniqueIdentifier:fromSource:completion:]_block_invoke.202
+ ___94-[PKPaymentService sharingInvitationWasInvalidated:withCredentialIdentifier:error:completion:]_block_invoke.378
+ ___94-[PKPaymentService valueAddedServiceTransactionsForPassWithUniqueIdentifier:limit:completion:]_block_invoke.217
+ ___96-[PKPassLibrary _getPassesAndCatalogOfPassTypes:synchronously:limitResults:withRetries:handler:]_block_invoke.324
+ ___96-[PKPassLibrary _getPassesAndCatalogOfPassTypes:synchronously:limitResults:withRetries:handler:]_block_invoke.325
+ ___96-[PKPaymentService ambiguousPassUniqueIdentifierForTransactionWithServiceIdentifier:completion:]_block_invoke.186
+ ___96-[PKPaymentService invalidateAuxiliaryCapabilityCertificatesForPassUniqueIdentifier:completion:]_block_invoke.314
+ ___96-[PKPaymentService merchantForPassUniqueIdentifier:withAuxiliaryPassInformationItem:completion:]_block_invoke.298
+ ___96-[PKPaymentService provideEncryptedPushProvisioningTarget:sharingInstanceIdentifier:completion:]_block_invoke.384
+ ___96-[PKPaymentService submitEncryptedPIN:forTransactionIdentifier:sessionExchangeToken:completion:]_block_invoke.328
+ ___96-[PKPaymentService transactionReceiptForTransactionWithIdentifier:updateIfNecessary:completion:]_block_invoke.399
+ ___97-[PKPaymentSetupAssistantCoreController _preflightPaymentSetupProvisioningController:completion:]_block_invoke.150
+ ___97-[PKPaymentSetupAssistantCoreController _preflightPaymentSetupProvisioningController:completion:]_block_invoke.152
+ ___97-[PKPaymentSetupAssistantCoreController _preflightPaymentSetupProvisioningController:completion:]_block_invoke.155
+ ___97-[PKPaymentSetupAssistantCoreController _preflightPaymentSetupProvisioningController:completion:]_block_invoke.157
+ ___97-[PKPaymentSetupAssistantCoreController _preflightPaymentSetupProvisioningController:completion:]_block_invoke.160
+ ___97-[PKPaymentSetupAssistantCoreController _preflightPaymentSetupProvisioningController:completion:]_block_invoke_2
+ ___97-[PKPaymentSetupAssistantCoreController _preflightPaymentSetupProvisioningController:completion:]_block_invoke_3
+ ___98-[PKDashboardTransactionFetcher _addCashbackTransactions:synchronous:currentMonthOnly:completion:]_block_invoke.82
+ ___98-[PKPaymentService updatePreferredCategory:forTransactionsWithIdentifiers:paymentPass:completion:]_block_invoke.213
+ ___99-[PKPassLibrary requestIssuerBoundPassesWithBindingWithData:automaticallyProvision:withCompletion:]_block_invoke.273
+ ___99-[PKPaymentService userNotificationActionPerformed:applicationMessageContentIdentifier:completion:]_block_invoke.272
+ ___PKCanMakePaymentsWithMerchantIdentifierDomainAndSourceApplication_block_invoke.66
+ ___block_descriptor_48_e8_32bs40w_e15_v16?0"NSSet"8lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e38_v24?0"CUMessageSession"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e37_B32?0"PKPaymentApplication"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s_e27_B24?0"PKPaymentPass"8^B16ls32l8s40l8
+ ___block_descriptor_57_e8_32s40bs48w_e15_v16?0"NSSet"8ls32l8w48l8s40l8
+ ___block_descriptor_57_e8_32s40s48s_e30_B32?0"PKPaymentPass"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_66_e8_32s40s48bs56r_e15_v16?0"NSSet"8ls32l8r56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48bs56r_e20_v20?0B8"NSError"12ls32l8r56l8s48l8s40l8
+ ___block_descriptor_88_e8_32s40s48s56r64w_e61_v32?0"PKAsyncOperationState"8"NSNull"16?<v?"NSNull"B>24ls32l8s40l8s48l8w64l8r56l8
+ ___block_descriptor_96_e8_32s40s48s56s64bs72r80w_e20_v20?0B8"NSError"12lw80l8s32l8s64l8s40l8s48l8s56l8r72l8
+ ___block_literal_global.1006
+ ___block_literal_global.1014
+ ___block_literal_global.1023
+ ___block_literal_global.1036
+ ___block_literal_global.1038
+ ___block_literal_global.1040
+ ___block_literal_global.1045
+ ___block_literal_global.1056
+ ___block_literal_global.1059
+ ___block_literal_global.1087
+ ___block_literal_global.1092
+ ___block_literal_global.1094
+ ___block_literal_global.1099
+ ___block_literal_global.1104
+ ___block_literal_global.1109
+ ___block_literal_global.1114
+ ___block_literal_global.1124
+ ___block_literal_global.1129
+ ___block_literal_global.1134
+ ___block_literal_global.1136
+ ___block_literal_global.1144
+ ___block_literal_global.1180
+ ___block_literal_global.1259
+ ___block_literal_global.1264
+ ___block_literal_global.1271
+ ___block_literal_global.1283
+ ___block_literal_global.1296
+ ___block_literal_global.1297
+ ___block_literal_global.1343
+ ___block_literal_global.1347
+ ___block_literal_global.1455
+ ___block_literal_global.1457
+ ___block_literal_global.1460
+ ___block_literal_global.159
+ ___block_literal_global.1696
+ ___block_literal_global.1698
+ ___block_literal_global.1703
+ ___block_literal_global.1707
+ ___block_literal_global.172
+ ___block_literal_global.1721
+ ___block_literal_global.1723
+ ___block_literal_global.1728
+ ___block_literal_global.1748
+ ___block_literal_global.1755
+ ___block_literal_global.1757
+ ___block_literal_global.1759
+ ___block_literal_global.1762
+ ___block_literal_global.1936
+ ___block_literal_global.202
+ ___block_literal_global.205
+ ___block_literal_global.207
+ ___block_literal_global.211
+ ___block_literal_global.234
+ ___block_literal_global.237
+ ___block_literal_global.238
+ ___block_literal_global.252
+ ___block_literal_global.259
+ ___block_literal_global.261
+ ___block_literal_global.263
+ ___block_literal_global.265
+ ___block_literal_global.2668
+ ___block_literal_global.2685
+ ___block_literal_global.269
+ ___block_literal_global.275
+ ___block_literal_global.295
+ ___block_literal_global.308
+ ___block_literal_global.313
+ ___block_literal_global.341
+ ___block_literal_global.351
+ ___block_literal_global.372
+ ___block_literal_global.386
+ ___block_literal_global.435
+ ___block_literal_global.437
+ ___block_literal_global.520
+ ___block_literal_global.538
+ ___block_literal_global.635
+ ___block_literal_global.700
+ ___block_literal_global.702
+ ___block_literal_global.713
+ ___block_literal_global.718
+ ___block_literal_global.723
+ ___block_literal_global.728
+ ___block_literal_global.733
+ ___block_literal_global.738
+ ___block_literal_global.743
+ ___block_literal_global.750
+ ___block_literal_global.753
+ ___block_literal_global.757
+ ___block_literal_global.788
+ ___block_literal_global.791
+ ___block_literal_global.793
+ ___block_literal_global.809
+ ___block_literal_global.855
+ ___block_literal_global.951
+ ___block_literal_global.966
+ ___block_literal_global.968
+ ___block_literal_global.977
+ ___block_literal_global.981
+ _objc_msgSend$_excludedTransactionSourcesWithCompletion:
+ _objc_msgSend$_filterPassesForIssuerRegions:request:
+ _objc_msgSend$applyServiceProviderPropertiesToPaymentRequest:
+ _objc_msgSend$excludedTransactionSourceIdentifiersWithCompletion:
+ _objc_msgSend$hasAcquiredProvisioningAssertion
+ _objc_msgSend$initWithDictionary:availableNetworks:
+ _objc_msgSend$initWithServiceProviderOrder:
+ _objc_msgSend$issuerRegions
+ _objc_msgSend$sendTransactionsWithRequest:useSynchronous:completion:
+ _objc_msgSend$setExcludedTransactionSourceIdentifiers:
+ _objc_msgSend$setIsInProximitySetup:
+ _objc_msgSend$setIssuerRegions:
+ _objc_msgSend$shouldCollectPlan:withAction:
+ _objc_msgSend$supportsCapability:forAccount:paymentApplicationState:dpanSuffix:
+ _objc_msgSend$usesExternalView
+ _objectdestroy.8Tm
- +[PKDAManager isCarKeySupportedForManufacturerIdentifier:issuerIdentifier:productPlanIdentifier:]
- -[PKCloudStoreRecordFetchTask completeTaskWithError:]
- -[PKDashboardTransactionFetcher filterOutAccountStates:]
- -[PKDashboardTransactionFetcher filterOutPeerPaymentAccountStates:]
- -[PKFieldProperties shouldIgnore]
- -[PKPaymentTransactionRequest excludedAccountStates]
- -[PKPaymentTransactionRequest excludedPeerPaymentAccountStates]
- -[PKPaymentTransactionRequest setExcludedAccountStates:]
- -[PKPaymentTransactionRequest setExcludedPeerPaymentAccountStates:]
- -[PKUserNotificationReceipt initWithNotificationIdentifier:accountIdentifier:]
- GCC_except_table142
- GCC_except_table150
- GCC_except_table152
- GCC_except_table231
- GCC_except_table233
- GCC_except_table253
- GCC_except_table279
- GCC_except_table281
- GCC_except_table295
- GCC_except_table307
- GCC_except_table319
- GCC_except_table324
- GCC_except_table325
- GCC_except_table344
- GCC_except_table348
- GCC_except_table357
- GCC_except_table361
- GCC_except_table371
- GCC_except_table378
- GCC_except_table388
- GCC_except_table394
- GCC_except_table399
- GCC_except_table411
- GCC_except_table414
- GCC_except_table416
- GCC_except_table460
- GCC_except_table462
- GCC_except_table477
- GCC_except_table488
- GCC_except_table525
- GCC_except_table532
- GCC_except_table533
- GCC_except_table534
- GCC_except_table535
- GCC_except_table550
- GCC_except_table557
- GCC_except_table577
- GCC_except_table64
- GCC_except_table744
- GCC_except_table862
- _.str.892
- _OBJC_IVAR_$_PKDashboardTransactionFetcher._excludedAccountStates
- _OBJC_IVAR_$_PKDashboardTransactionFetcher._excludedPeerPaymentAccountStates
- _OBJC_IVAR_$_PKPaymentTransactionRequest._excludedAccountStates
- _OBJC_IVAR_$_PKPaymentTransactionRequest._excludedPeerPaymentAccountStates
- ___100-[PKPassLibrary checkFidoKeyPresenceForRelyingParty:relyingPartyAccountHash:fidoKeyHash:completion:]_block_invoke.260
- ___100-[PKPassLibrary inAppPrivateLabelPaymentPassesForWebDomain:issuerCountryCodes:isMultiTokensRequest:]_block_invoke.160
- ___100-[PKPaymentService submitUserConfirmation:forTransactionIdentifier:sessionExchangeToken:completion:]_block_invoke.325
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke.541
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke.547
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_2.542
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_2.548
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_3.543
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_3.549
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_4.544
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_5.545
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_6.546
- ___102-[PKPaymentService recordPaymentApplicationUsageForPassUniqueIdentifier:paymentApplicationIdentifier:]_block_invoke.249
- ___103-[PKPaymentService submitTransactionSignatureForTransactionIdentifier:sessionExchangeToken:completion:]_block_invoke.328
- ___105-[PKPaymentService augmentedProductForInstallmentConfiguration:experimentDetails:feature:withCompletion:]_block_invoke.344
- ___106-[PKPaymentService submitBarcodePaymentEvent:forPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.330
- ___107-[PKPaymentService registerAuxiliaryCapabilityForPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.312
- ___107-[PKPaymentService retrieveDecryptedBarcodeCredentialForPassUniqueIdentifier:authorization:withCompletion:]_block_invoke.316
- ___108-[PKPassLibrary createFidoKeyForRelyingParty:relyingPartyAccountHash:challenge:externalizedAuth:completion:]_block_invoke.258
- ___109-[PKPaymentService conflictingExpressPassIdentifiersForPassInformation:withReferenceExpressState:completion:]_block_invoke.237
- ___110-[PKPassLibrary overrideStateOfRelevancyPresentmentOfType:containingPassUniqueIdentifier:newState:completion:]_block_invoke.278
- ___111-[PKPaymentProvisioningController resolveLocalEligibilityRequirementsForAppleBalanceCredential:withCompletion:]_block_invoke.580
- ___111-[PKPaymentProvisioningController resolveLocalEligibilityRequirementsForAppleBalanceCredential:withCompletion:]_block_invoke.588
- ___111-[PKPaymentService conflictingExpressPassIdentifiersForPassConfiguration:withReferenceExpressState:completion:]_block_invoke.236
- ___112-[PKPassLibrary inAppPrivateLabelPaymentPassesForApplicationIdentifier:issuerCountryCodes:isMultiTokensRequest:]_block_invoke.158
- ___112-[PKPaymentService retrievePINEncryptionCertificateForPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.320
- ___115-[PKPassLibrary hasInAppPrivateLabelPaymentPassesForWebDomain:issuerCountryCodes:isMultiTokensRequest:withHandler:]_block_invoke.161
- ___115-[PKPaymentService passUniqueIdentifierForTransactionWithServiceIdentifier:transactionSourceIdentifier:completion:]_block_invoke.182
- ___117-[PKPaymentService insertOrUpdateValueAddedServiceTransaction:forPassUniqueIdentifier:paymentTransaction:completion:]_block_invoke.215
- ___125+[PKPaymentSetupAssistantRegistrationUtilities preflightPaymentSetupProvisioningController:forSetupAssistant:withCompletion:]_block_invoke.141
- ___125+[PKPaymentSetupAssistantRegistrationUtilities preflightPaymentSetupProvisioningController:forSetupAssistant:withCompletion:]_block_invoke.142
- ___125-[PKPaymentService recordPassTransactionActivitySummaryForPassUniqueIdentifier:paymentApplicationIdentifier:presentmentType:]_block_invoke.248
- ___127-[PKPassLibrary hasInAppPrivateLabelPaymentPassesForApplicationIdentifier:issuerCountryCodes:isMultiTokensRequest:withHandler:]_block_invoke.159
- ___128-[PKPaymentService retrieveDecryptedBarcodeCredentialForPassUniqueIdentifier:authorization:sessionExchangeToken:withCompletion:]_block_invoke.318
- ___132-[PKDashboardTransactionFetcher _processPaymentPassTransactionsWithTransactions:synchronous:currentMonthOnly:sendTransactionsBlock:]_block_invoke.89
- ___132-[PKDashboardTransactionFetcher _processPaymentPassTransactionsWithTransactions:synchronous:currentMonthOnly:sendTransactionsBlock:]_block_invoke_2.91
- ___134-[PKPassLibrary hasInAppPaymentPassesForNetworks:capabilities:issuerCountryCodes:paymentRequestType:isMultiTokensRequest:withHandler:]_block_invoke.157
- ___140-[PKPassLibrary configureHomeAuxiliaryCapabilitiesForSerialNumber:homeIdentifier:fromUnifiedAccessDescriptor:andAliroDescriptor:completion:]_block_invoke.188
- ___140-[PKPaymentService rangingSuspensionReasonForAppletSubcredentialIdentifier:paymentApplicationIdentifier:secureElementIdentifier:completion:]_block_invoke.292
- ___142-[PKPassLibrary signWithFidoKeyForRelyingParty:relyingPartyAccountHash:fidoKeyHash:challenge:publicKeyIdentifier:externalizedAuth:completion:]_block_invoke.261
- ___149-[PKPaymentService processTransitTransactionEventWithHistory:transactionDate:forPaymentApplication:withPassUniqueIdentifier:expressTransactionState:]_block_invoke.247
- ___155-[PKPassLibrary requestPersonalizationOfPassWithUniqueIdentifier:contact:personalizationToken:requiredPersonalizationFields:personalizationSource:handler:]_block_invoke.212
- ___31-[PKPassLibrary backupMetadata]_block_invoke.252
- ___35-[PKPassLibrary setBackupMetadata:]_block_invoke.253
- ___36-[PKPaymentService consistencyCheck]_block_invoke.266
- ___41-[PKPassLibrary archivePassWithUniqueID:]_block_invoke.298
- ___41-[PKPassLibrary recoverPassWithUniqueID:]_block_invoke.297
- ___43-[PKPassLibrary expressFelicaTransitPasses]_block_invoke.231
- ___43-[PKPaymentService productsWithCompletion:]_block_invoke.360
- ___44-[PKPaymentService initializeSecureElement:]_block_invoke.225
- ___45-[PKPaymentService insertUserLegalAgreement:]_block_invoke.403
- ___47-[PKPassLibrary unexpiredPassesOrderedByGroup:]_block_invoke.163
- ___48-[PKPassLibrary exportableCardEntry:completion:]_block_invoke.276
- ___48-[PKPaymentService mapsMerchantsWithCompletion:]_block_invoke.186
- ___49-[PKPaymentService currentSecureElementSnapshot:]_block_invoke.391
- ___49-[PKPaymentService deleteReservation:completion:]_block_invoke.395
- ___50-[PKPassLibrary exportableManifestWithCompletion:]_block_invoke.274
- ___50-[PKPaymentService sharedPaymentWebServiceContext]_block_invoke.285
- ___50-[PKPaymentService submitApplyRequest:completion:]_block_invoke.348
- ___50-[PKPaymentService submitTermsRequest:completion:]_block_invoke.352
- ___51-[PKPassLibrary resetApplePayWithDiagnosticReason:]_block_invoke.302
- ___51-[PKPaymentService logoImageDataForURL:completion:]_block_invoke.178
- ___51-[PKPaymentService productsWithRequest:completion:]_block_invoke.358
- ___51-[PKPaymentService submitDeleteRequest:completion:]_block_invoke.353
- ___52-[PKPassLibrary passLocalizedStringForKey:uniqueID:]_block_invoke.170
- ___52-[PKPaymentAuthorizationDataModel unavailablePasses]_block_invoke_2
- ___53-[PKPassLibrary canPresentPaymentRequest:completion:]_block_invoke.197
- ___53-[PKPaymentService submitDocumentRequest:completion:]_block_invoke.350
- ___54-[PKPassLibrary addISO18013Blobs:cardType:completion:]_block_invoke.267
- ___54-[PKPassLibrary defaultPaymentPassesWithRemotePasses:]_block_invoke.230
- ___54-[PKPaymentService featureApplicationsWithCompletion:]_block_invoke.346
- ___54-[PKPaymentService regionsWithIdentifiers:completion:]_block_invoke.295
- ___55-[PKPaymentDigitalIssuanceMetadata initWithDictionary:]_block_invoke
- ___55-[PKPaymentService performDeviceCheckInWithCompletion:]_block_invoke.357
- ___55-[PKPaymentService pushProvisioningSharingIdentifiers:]_block_invoke.378
- ___56-[PKPaymentService credentialWithIdentifier:completion:]_block_invoke.374
- ___57-[PKPassLibrary _defaultPaymentPassWithoutPaymentRequest]_block_invoke.241
- ___57-[PKPassLibrary addPassesWithData:withCompletionHandler:]_block_invoke.172
- ___57-[PKPassLibrary removePassWithUniqueID:diagnosticReason:]_block_invoke.295
- ___57-[PKPassLibrary removePassesOfType:withDiagnosticReason:]_block_invoke.299
- ___57-[PKPaymentService regionsMatchingName:types:completion:]_block_invoke.296
- ___57-[PKPaymentService submitVerificationRequest:completion:]_block_invoke.351
- ___58-[PKPassLibrary addPassesContainer:withCompletionHandler:]_block_invoke.175
- ___58-[PKPassLibrary meetsProvisioningRequirements:completion:]_block_invoke.221
- ___58-[PKPassLibrary prepareForBackupRestoreWithSafeHavenPath:]_block_invoke.257
- ___58-[PKPaymentService familyMembersIgnoringCache:completion:]_block_invoke.331
- ___59-[PKPaymentService memberTypeForCurrentUserWithCompletion:]_block_invoke.332
- ___59-[PKPaymentService performProductActionRequest:completion:]_block_invoke.361
- ___59-[PKPaymentService requiresUpgradedPasscodeWithCompletion:]_block_invoke.310
- ___59-[PKPaymentService storeTransactionReceiptData:completion:]_block_invoke.399
- ___59-[PKPaymentService subcredentialInvitationsWithCompletion:]_block_invoke.368
- ___60-[PKPassLibrary passUniqueIDsMatchingSearchTerm:completion:]_block_invoke.164
- ___60-[PKPassLibrary removePassesWithUniqueIDs:diagnosticReason:]_block_invoke.296
- ___60-[PKPaymentProvisioningController _noteProvisioningDidBegin]_block_invoke.621
- ___61-[PKPassLibrary availableHomeKeyPassesWithCompletionHandler:]_block_invoke.181
- ___61-[PKPaymentProvisioningController retrieveRemoteCredentials:]_block_invoke.303
- ___61-[PKPaymentProvisioningController retrieveRemoteCredentials:]_block_invoke.305
- ___61-[PKPaymentProvisioningController retrieveRemoteCredentials:]_block_invoke_2.306
- ___61-[PKPaymentService changePasscodeFrom:toPasscode:completion:]_block_invoke.311
- ___61-[PKPaymentService statusForShareableCredentials:completion:]_block_invoke.381
- ___62-[PKPassLibrary addSharedFlight:fromSenderAddress:completion:]_block_invoke.215
- ___62-[PKPassLibrary canAddCarKeyPassWithConfiguration:completion:]_block_invoke.219
- ___62-[PKPassLibrary enabledValueAddedServicePassesWithCompletion:]_block_invoke.162
- ___62-[PKPassLibrary resetApplePayWithDiagnosticReason:completion:]_block_invoke.301
- ___62-[PKPaymentService addRemoteDevicePendingProvisioningReceipt:]_block_invoke.300
- ___62-[PKPaymentService generateUnderlyingKeyReportWithCompletion:]_block_invoke.306
- ___62-[PKPaymentService transactionReceiptWithUniqueID:completion:]_block_invoke.396
- ___62-[PKPaymentService transactionsForPredicate:limit:completion:]_block_invoke.180
- ___63-[PKPassLibrary addUnsignedPassesAtURLs:withCompletionHandler:]_block_invoke.177
- ___63-[PKPassLibrary addUnsignedPassesAtURLs:withCompletionHandler:]_block_invoke_2.178
- ___63-[PKPaymentService currentPasscodeMeetsUpgradedPasscodePolicy:]_block_invoke.309
- ___63-[PKPaymentService photosForFamilyMembersWithDSIDs:completion:]_block_invoke.335
- ___63-[PKPaymentService refreshMerchantTokenMetadataWithCompletion:]_block_invoke.298
- ___63-[PKPaymentService removeExpressPassesWithCardType:completion:]_block_invoke.241
- ___64-[PKPassLibrary replaceUnsignedPassAtURL:withCompletionHandler:]_block_invoke.184
- ___64-[PKPassLibrary replaceUnsignedPassAtURL:withCompletionHandler:]_block_invoke_2.185
- ___64-[PKPaymentProvisioningController performDeviceCheckInIfNeeded:]_block_invoke.291
- ___64-[PKPaymentService enforceUpgradedPasscodePolicyWithCompletion:]_block_invoke.308
- ___64-[PKPaymentService featureApplicationWithIdentifier:completion:]_block_invoke.347
- ___64-[PKPaymentService passOwnershipTokenWithIdentifier:completion:]_block_invoke.362
- ___64-[PKPaymentService redeemPaymentShareableCredential:completion:]_block_invoke.387
- ___64-[PKPaymentService revokeCredentialsWithIdentifiers:completion:]_block_invoke.372
- ___65-[PKPassLibrary paymentSetupFeaturesForConfiguration:completion:]_block_invoke.195
- ___65-[PKPaymentService isPassExpressWithUniqueIdentifier:completion:]_block_invoke.246
- ___65-[PKPaymentService notifyForFPANCardImportConsentWithCompletion:]_block_invoke.302
- ___65-[PKPaymentService passSharesForCredentialIdentifier:completion:]_block_invoke.376
- ___65-[PKPaymentService pendingFamilyMembersIgnoringCache:completion:]_block_invoke.334
- ___65-[PKPaymentService revokeMerchantTokenWithIdentifier:completion:]_block_invoke.299
- ___65-[PKPaymentService sharedPaymentWebServiceContextWithCompletion:]_block_invoke.287
- ___65-[PKPaymentService transactionsTotalAmountForRequest:completion:]_block_invoke.176
- ___66-[PKPaymentService defaultPaymentPassIngestionSpecificIdentifier:]_block_invoke.336
- ___66-[PKPaymentService registerCredentialsWithIdentifiers:completion:]_block_invoke.370
- ___66-[PKPaymentService setBalanceReminder:forBalance:pass:completion:]_block_invoke.198
- ___67-[PKPassLibrary canAddSecureElementPassWithConfiguration:outError:]_block_invoke.217
- ___67-[PKPassLibrary presentPaymentSetupRequest:orientation:completion:]_block_invoke.194
- ___67-[PKPassLibrary sortedTransitPassesForAppletDataFormat:completion:]_block_invoke.233
- ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.328
- ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.335
- ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.344
- ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.352
- ___67-[PKPaymentService addPlaceholderPassWithConfiguration:completion:]_block_invoke.366
- ___67-[PKPaymentService clearFPANCardImportNotificationsWithCompletion:]_block_invoke.304
- ___67-[PKPaymentService redeemProvisioningSharingIdentifier:completion:]_block_invoke.389
- ___67-[PKPaymentService requestNotificationAuthorizationWithCompletion:]_block_invoke.270
- ___68-[PKPassLibrary getContainmentStatusAndSettingsForPass:withHandler:]_block_invoke.213
- ___68-[PKPassLibrary prepareForBackupRestoreWithExistingPreferencesData:]_block_invoke.254
- ___68-[PKPassLibrary removePassesOfType:withDiagnosticReason:completion:]_block_invoke.300
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke.231
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke.233
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke.239
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke.246
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke.249
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke.258
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke.272
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_2.234
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_2.241
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_2.247
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_2.250
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_2.267
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_2.273
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_3.248
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_3.251
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_3.278
- ___68-[PKPaymentProvisioningController preflightWithRequirements:update:]_block_invoke_4.252
- ___68-[PKPaymentService deleteTransactionReceiptWithUniqueID:completion:]_block_invoke.400
- ___68-[PKPaymentService updateAllMapsBrandAndMerchantDataWithCompletion:]_block_invoke.288
- ___69-[PKPassLibrary addISO18013BlobsFromCredentials:cardType:completion:]_block_invoke.266
- ___69-[PKPassLibrary canAddSecureElementPassWithConfiguration:completion:]_block_invoke.218
- ___69-[PKPassLibrary configurePushProvisioningConfigurationV2:completion:]_block_invoke.247
- ___69-[PKPassLibrary configurePushProvisioningConfigurationV2:completion:]_block_invoke.248
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.348
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.350
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.357
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.359
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.368
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.375
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.376
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_2.360
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_2.369
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_2.378
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_2.382
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_3.362
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_3.371
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_3.379
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_3.384
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_4.363
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_4.374
- ___69-[PKPaymentService featureApplicationsForProvisioningWithCompletion:]_block_invoke.340
- ___69-[PKPaymentService initializeSecureElementIfNecessaryWithCompletion:]_block_invoke.223
- ___69-[PKPaymentService removeExpressPassWithUniqueIdentifier:completion:]_block_invoke.243
- ___69-[PKPaymentService reserveStorageForAppletTypes:metadata:completion:]_block_invoke.393
- ___69-[PKPaymentService setExpressWithPassInformation:credential:handler:]_block_invoke.240
- ___70-[PKPassLibrary addPassesWithIngestionPayloads:withCompletionHandler:]_block_invoke.173
- ___70-[PKPassLibrary pushProvisioningNoncesWithCredentialCount:completion:]_block_invoke.242
- ___70-[PKPassLibrary requestUpdateOfObjectWithUniqueIdentifier:completion:]_block_invoke.211
- ___70-[PKPassLibrary sendRKEPassThroughMessage:forSessionIdentifier:error:]_block_invoke.251
- ___70-[PKPaymentService accountAttestationAnonymizationSaltWithCompletion:]_block_invoke.363
- ___70-[PKPaymentService revokeCredentialsWithReaderIdentifiers:completion:]_block_invoke.373
- ___70-[PKPaymentService suggestPaymentFPANCredentialImport:withCompletion:]_block_invoke.301
- ___71-[PKPassLibrary paymentPassWithAssociatedAccountIdentifier:completion:]_block_invoke.196
- ___71-[PKPaymentService featureApplicationsForAccountIdentifier:completion:]_block_invoke.337
- ___71-[PKPaymentService plansForPaymentPassWithUniqueIdentifier:completion:]_block_invoke.195
- ___71-[PKPaymentService removeExpressPassWithUniqueIdentifierV2:completion:]_block_invoke.242
- ___71-[PKPaymentService setExpressWithPassConfiguration:credential:handler:]_block_invoke.238
- ___72-[PKPassLibrary fetchHomePaymentApplicationsForSerialNumber:completion:]_block_invoke.190
- ___72-[PKPassLibrary provisionHomeKeyPassForSerialNumbers:completionHandler:]_block_invoke.179
- ___72-[PKPaymentProvisioningController _identityConfigurationWithCompletion:]_block_invoke.483
- ___72-[PKPaymentProvisioningController _identityConfigurationWithCompletion:]_block_invoke.484
- ___73-[PKPassLibrary generateAuxiliaryCapabilitiesForRequirements:completion:]_block_invoke.269
- ___73-[PKPaymentAuthorizationStateMachine _performRewrapRequestImplWithParam:]_block_invoke.295
- ___73-[PKPaymentAuthorizationStateMachine _performRewrapRequestImplWithParam:]_block_invoke.299
- ___73-[PKPaymentAuthorizationStateMachine _performRewrapRequestImplWithParam:]_block_invoke_2.302
- ___73-[PKPaymentService ambiguousTransactionWithServiceIdentifier:completion:]_block_invoke.402
- ___73-[PKPaymentService clearFPANCardImportNotificationHistoryWithCompletion:]_block_invoke.305
- ___73-[PKPaymentService featureApplicationWithReferenceIdentifier:completion:]_block_invoke.342
- ___74-[PKPassLibrary signData:signatureEntanglementMode:withCompletionHandler:]_block_invoke.272
- ___74-[PKPaymentService balancesForPaymentPassWithUniqueIdentifier:completion:]_block_invoke.194
- ___74-[PKPaymentService messagesForPaymentPassWithUniqueIdentifier:completion:]_block_invoke.193
- ___74-[PKPaymentService notifyForFPANCardImportWithCredentials:withCompletion:]_block_invoke.303
- ___74-[PKPaymentService setAccountAttestationAnonymizationSalt:withCompletion:]_block_invoke.365
- ___74-[PKPaymentService setCommutePlanReminder:forCommutePlan:pass:completion:]_block_invoke.202
- ___74-[PKPaymentService valueAddedServiceTransactionWithIdentifier:completion:]_block_invoke.218
- ___74-[PKPaymentSetupAssistantCoreController _expressSetupProvisioningContext:]_block_invoke.164
- ___74-[PKPaymentSetupAssistantCoreController _expressSetupProvisioningContext:]_block_invoke_2.166
- ___75-[PKPaymentService balanceReminderThresholdForBalance:pass:withCompletion:]_block_invoke.196
- ___75-[PKPaymentService commutePlanReminderForCommputePlan:pass:withCompletion:]_block_invoke.200
- ___75-[PKPaymentService prepareProvisioningTarget:checkFamilyCircle:completion:]_block_invoke.384
- ___75-[PKPaymentService submitEncryptedPIN:forTransactionIdentifier:completion:]_block_invoke.326
- ___75-[PKPaymentService transactionTagsForTransactionWithIdentifier:completion:]_block_invoke.401
- ___77-[PKPaymentRequirementsRequest _urlRequestWithBuilder:webService:completion:]_block_invoke.392
- ___77-[PKPaymentService sendDeviceSharingCapabilitiesRequestForHandle:completion:]_block_invoke.404
- ___77-[PKPaymentService updateFeatureApplicationsForAccountIdentifier:completion:]_block_invoke.338
- ___77-[PKPaymentService updateMetadataOnPassWithIdentifier:credential:completion:]_block_invoke.369
- ___78-[PKPassLibrary generateSEEncryptionCertificateForSubCredentialId:completion:]_block_invoke.263
- ___78-[PKPaymentProvisioningController _requestProvisioning:withCompletionHandler:]_block_invoke.653
- ___78-[PKPaymentProvisioningController _requestProvisioning:withCompletionHandler:]_block_invoke_2.654
- ___78-[PKPaymentService categoryVisualizationMagnitudesForPassUniqueID:completion:]_block_invoke.356
- ___78-[PKPaymentService featureApplicationsForAccountUserInvitationWithCompletion:]_block_invoke.341
- ___78-[PKPaymentService requestNotificationAuthorizationIfNecessaryWithCompletion:]_block_invoke.269
- ___78-[PKPaymentSetupAssistantCoreController _hasManuallyAddedSecureElementPasses:]_block_invoke.162
- ___79-[PKPassLibrary _fetchContentForUniqueID:usingSynchronousProxy:withCompletion:]_block_invoke.224
- ___79-[PKPassLibrary generateISOEncryptionCertificateForSubCredentialId:completion:]_block_invoke.264
- ___79-[PKPassLibrary sortedTransitPassesForTransitNetworkIdentifiersWithCompletion:]_block_invoke.232
- ___79-[PKPaymentProvisioningController _associateCredentials:withCompletionHandler:]_block_invoke.383
- ___79-[PKPaymentService submitUserConfirmation:forTransactionIdentifier:completion:]_block_invoke.323
- ___80-[PKPassLibrary presentContactlessInterfaceForDefaultPassFromSource:completion:]_block_invoke.199
- ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.409
- ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.416
- ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.425
- ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.433
- ___80-[PKPaymentProvisioningController requestPurchasesForProduct:completionHandler:]_block_invoke.527
- ___80-[PKPaymentProvisioningController requestPurchasesForProduct:completionHandler:]_block_invoke.530
- ___80-[PKPaymentService passUniqueIdentifierForTransactionWithIdentifier:completion:]_block_invoke.181
- ___82-[PKPassLibrary startVehicleConnectionSessionWithPassUniqueIdentifier:completion:]_block_invoke.250
- ___82-[PKPaymentService markAuthenticationCompleteForTransactionIdentifier:completion:]_block_invoke.322
- ___83-[PKDashboardTransactionFetcher reloadTransactionsWithAllowSynchronous:completion:]_block_invoke_10
- ___83-[PKDashboardTransactionFetcher reloadTransactionsWithAllowSynchronous:completion:]_block_invoke_11
- ___83-[PKDashboardTransactionFetcher reloadTransactionsWithAllowSynchronous:completion:]_block_invoke_12
- ___83-[PKDashboardTransactionFetcher reloadTransactionsWithAllowSynchronous:completion:]_block_invoke_13
- ___83-[PKDashboardTransactionFetcher reloadTransactionsWithAllowSynchronous:completion:]_block_invoke_14
- ___83-[PKDashboardTransactionFetcher reloadTransactionsWithAllowSynchronous:completion:]_block_invoke_15
- ___83-[PKDashboardTransactionFetcher reloadTransactionsWithAllowSynchronous:completion:]_block_invoke_16
- ___83-[PKDashboardTransactionFetcher reloadTransactionsWithAllowSynchronous:completion:]_block_invoke_17
- ___83-[PKDashboardTransactionFetcher reloadTransactionsWithAllowSynchronous:completion:]_block_invoke_2
- ___83-[PKDashboardTransactionFetcher reloadTransactionsWithAllowSynchronous:completion:]_block_invoke_3
- ___83-[PKDashboardTransactionFetcher reloadTransactionsWithAllowSynchronous:completion:]_block_invoke_4
- ___83-[PKDashboardTransactionFetcher reloadTransactionsWithAllowSynchronous:completion:]_block_invoke_5
- ___83-[PKDashboardTransactionFetcher reloadTransactionsWithAllowSynchronous:completion:]_block_invoke_6
- ___83-[PKDashboardTransactionFetcher reloadTransactionsWithAllowSynchronous:completion:]_block_invoke_7
- ___83-[PKDashboardTransactionFetcher reloadTransactionsWithAllowSynchronous:completion:]_block_invoke_8
- ___83-[PKDashboardTransactionFetcher reloadTransactionsWithAllowSynchronous:completion:]_block_invoke_9
- ___83-[PKPassLibrary containsPassWithPassTypeIdentifier:serialNumber:completionHandler:]_block_invoke.166
- ___83-[PKPaymentService mapsMerchantWithIdentifier:resultProviderIdentifier:completion:]_block_invoke.289
- ___83-[PKPaymentService saveProvisioningSupportData:forPassUniqueIdentifier:completion:]_block_invoke.379
- ___83-[PKPaymentService transactionsRequiringReviewForAccountWithIdentifier:completion:]_block_invoke.355
- ___84-[PKPaymentAuthorizationDataModel _filterAndProcessPaymentPassesUsingConfiguration:]_block_invoke.143
- ___84-[PKPaymentService passUniqueIdentifiersForTransactionSourceIdentifiers:completion:]_block_invoke.183
- ___84-[PKPaymentService setDefaultPaymentApplication:forPassUniqueIdentifier:completion:]_block_invoke.220
- ___85-[PKPaymentProvisioningController _setupAccountCredentialForProvisioning:completion:]_block_invoke.550
- ___85-[PKPaymentProvisioningController _setupAccountCredentialForProvisioning:completion:]_block_invoke.552
- ___85-[PKPaymentProvisioningController _setupAccountCredentialForProvisioning:completion:]_block_invoke_2.554
- ___85-[PKPaymentService setDefaultExpressTransitPassIdentifier:withCredential:completion:]_block_invoke.228
- ___85-[PKPaymentService submitBarcodePaymentEvent:forPassUniqueIdentifier:withCompletion:]_block_invoke.329
- ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke.507
- ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke.510
- ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke_2.512
- ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke_3.513
- ___86-[PKPaymentService userNotificationActionPerformed:notificationIdentifier:completion:]_block_invoke.272
- ___87-[PKPassLibrary _getGroupsControllerSnapshotWithOptions:synchronously:retries:handler:]_block_invoke.325
- ___87-[PKPassLibrary _getGroupsControllerSnapshotWithOptions:synchronously:retries:handler:]_block_invoke.326
- ___87-[PKPassLibrary generateTransactionKeyWithReaderIdentifier:readerPublicKey:completion:]_block_invoke.186
- ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.449
- ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.455
- ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.462
- ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.471
- ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke_2.476
- ___87-[PKPaymentService conflictingExpressPassIdentifiersForPassInformation:withCompletion:]_block_invoke.235
- ___87-[PKPaymentService transitStateWithPassUniqueIdentifier:paymentApplication:completion:]_block_invoke.252
- ___88-[PKPaymentAuthorizationStateMachine _performPrepareTransactionDetailsRequestWithParam:]_block_invoke.286
- ___88-[PKPaymentAuthorizationStateMachine _performPrepareTransactionDetailsRequestWithParam:]_block_invoke_2.288
- ___88-[PKPaymentService valueAddedServiceTransactionsForPaymentTransaction:limit:completion:]_block_invoke.217
- ___89-[PKPassLibrary _activateSecureElementPass:withActivationCode:activationData:completion:]_block_invoke.210
- ___89-[PKPassLibrary longTermPrivacyKeyForCredentialGroupIdentifier:reuseExisting:completion:]_block_invoke.268
- ___89-[PKPaymentService conflictingExpressPassIdentifiersForPassConfiguration:withCompletion:]_block_invoke.234
- ___89-[PKPaymentService processedAuthenticationMechanism:forTransactionIdentifier:completion:]_block_invoke.321
- ___89-[PKPaymentService submitTransactionAnswerForTransaction:questionType:answer:completion:]_block_invoke.354
- ___90-[PKPaymentService clearProvisioningSupportDataOfType:forPassUniqueIdentifier:completion:]_block_invoke.380
- ___91-[PKPassLibrary enableExpressForPassWithPassTypeIdentifier:serialNumber:completionHandler:]_block_invoke.191
- ___91-[PKPaymentProvisioningController verifyPassIsSupportedForExpressInLocalMarket:completion:]_block_invoke.659
- ___91-[PKPaymentProvisioningController verifyPassIsSupportedForExpressInLocalMarket:completion:]_block_invoke.660
- ___91-[PKPaymentProvisioningController verifyPassIsSupportedForExpressInLocalMarket:completion:]_block_invoke.665
- ___91-[PKPaymentService retrievePINEncryptionCertificateForPassUniqueIdentifier:withCompletion:]_block_invoke.319
- ___91-[PKPaymentService setDefaultExpressFelicaTransitPassIdentifier:withCredential:completion:]_block_invoke.226
- ___93-[PKPaymentService cancelAutoTopUpForPassWithUniqueIdentifier:balanceIdentifiers:completion:]_block_invoke.199
- ___93-[PKPaymentService fetchBarcodesForPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.314
- ___93-[PKPaymentService transactionsRelatedToTransaction:transactionSourceIdentifiers:completion:]_block_invoke.211
- ___94-[PKPassLibrary presentContactlessInterfaceForPassWithUniqueIdentifier:fromSource:completion:]_block_invoke.200
- ___94-[PKPaymentService sharingInvitationWasInvalidated:withCredentialIdentifier:error:completion:]_block_invoke.377
- ___94-[PKPaymentService valueAddedServiceTransactionsForPassWithUniqueIdentifier:limit:completion:]_block_invoke.216
- ___96-[PKPassLibrary _getPassesAndCatalogOfPassTypes:synchronously:limitResults:withRetries:handler:]_block_invoke.322
- ___96-[PKPassLibrary _getPassesAndCatalogOfPassTypes:synchronously:limitResults:withRetries:handler:]_block_invoke.323
- ___96-[PKPaymentService ambiguousPassUniqueIdentifierForTransactionWithServiceIdentifier:completion:]_block_invoke.185
- ___96-[PKPaymentService invalidateAuxiliaryCapabilityCertificatesForPassUniqueIdentifier:completion:]_block_invoke.313
- ___96-[PKPaymentService merchantForPassUniqueIdentifier:withAuxiliaryPassInformationItem:completion:]_block_invoke.297
- ___96-[PKPaymentService provideEncryptedPushProvisioningTarget:sharingInstanceIdentifier:completion:]_block_invoke.383
- ___96-[PKPaymentService submitEncryptedPIN:forTransactionIdentifier:sessionExchangeToken:completion:]_block_invoke.327
- ___96-[PKPaymentService transactionReceiptForTransactionWithIdentifier:updateIfNecessary:completion:]_block_invoke.398
- ___97-[PKPaymentSetupAssistantCoreController _preflightPaymentSetupProvisioningController:completion:]_block_invoke.144
- ___97-[PKPaymentSetupAssistantCoreController _preflightPaymentSetupProvisioningController:completion:]_block_invoke.145
- ___97-[PKPaymentSetupAssistantCoreController _preflightPaymentSetupProvisioningController:completion:]_block_invoke.147
- ___98-[PKDashboardTransactionFetcher _addCashbackTransactions:synchronous:currentMonthOnly:completion:]_block_invoke.80
- ___98-[PKPaymentService updatePreferredCategory:forTransactionsWithIdentifiers:paymentPass:completion:]_block_invoke.212
- ___99-[PKPassLibrary requestIssuerBoundPassesWithBindingWithData:automaticallyProvision:withCompletion:]_block_invoke.271
- ___99-[PKPaymentService userNotificationActionPerformed:applicationMessageContentIdentifier:completion:]_block_invoke.271
- ___PKCanMakePaymentsWithMerchantIdentifierDomainAndSourceApplication_block_invoke.52
- ___block_descriptor_56_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_66_e8_32s40s48bs56r_e15_v16?0"NSSet"8lr56l8s32l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48s56bs64w_e20_v20?0B8"NSError"12lw64l8s32l8s40l8s56l8s48l8
- ___block_literal_global.1000
- ___block_literal_global.1002
- ___block_literal_global.1030
- ___block_literal_global.1032
- ___block_literal_global.1034
- ___block_literal_global.1039
- ___block_literal_global.1050
- ___block_literal_global.1053
- ___block_literal_global.1081
- ___block_literal_global.1086
- ___block_literal_global.1088
- ___block_literal_global.1093
- ___block_literal_global.1098
- ___block_literal_global.1103
- ___block_literal_global.1108
- ___block_literal_global.1113
- ___block_literal_global.1118
- ___block_literal_global.1128
- ___block_literal_global.1138
- ___block_literal_global.1174
- ___block_literal_global.1253
- ___block_literal_global.1258
- ___block_literal_global.1262
- ___block_literal_global.1265
- ___block_literal_global.1277
- ___block_literal_global.1290
- ___block_literal_global.1291
- ___block_literal_global.1338
- ___block_literal_global.1342
- ___block_literal_global.1449
- ___block_literal_global.1451
- ___block_literal_global.1454
- ___block_literal_global.153
- ___block_literal_global.160
- ___block_literal_global.1690
- ___block_literal_global.1692
- ___block_literal_global.1697
- ___block_literal_global.1701
- ___block_literal_global.1715
- ___block_literal_global.1717
- ___block_literal_global.1722
- ___block_literal_global.1736
- ___block_literal_global.1745
- ___block_literal_global.1747
- ___block_literal_global.1749
- ___block_literal_global.175
- ___block_literal_global.1756
- ___block_literal_global.1930
- ___block_literal_global.208
- ___block_literal_global.224
- ___block_literal_global.236
- ___block_literal_global.251
- ___block_literal_global.258
- ___block_literal_global.262
- ___block_literal_global.264
- ___block_literal_global.2662
- ___block_literal_global.2679
- ___block_literal_global.268
- ___block_literal_global.276
- ___block_literal_global.278
- ___block_literal_global.283
- ___block_literal_global.294
- ___block_literal_global.304
- ___block_literal_global.310
- ___block_literal_global.335
- ___block_literal_global.347
- ___block_literal_global.365
- ___block_literal_global.368
- ___block_literal_global.424
- ___block_literal_global.516
- ___block_literal_global.537
- ___block_literal_global.622
- ___block_literal_global.696
- ___block_literal_global.701
- ___block_literal_global.712
- ___block_literal_global.717
- ___block_literal_global.722
- ___block_literal_global.727
- ___block_literal_global.732
- ___block_literal_global.737
- ___block_literal_global.742
- ___block_literal_global.744
- ___block_literal_global.782
- ___block_literal_global.785
- ___block_literal_global.787
- ___block_literal_global.795
- ___block_literal_global.849
- ___block_literal_global.960
- ___block_literal_global.962
- ___block_literal_global.965
- ___block_literal_global.967
- ___block_literal_global.969
- _objc_msgSend$setExcludedAccountStates:
- _objc_msgSend$setExcludedPeerPaymentAccountStates:
CStrings:
+ "'default' region checking %lu unlisted countries"
+ "'default' region has empty/nil networks, skipping"
+ "'default' region hasMatchingCards: %@"
+ "'default' region networks: %@"
+ "@\"PKProximitySetupLiaison\"16@0:8"
+ "Accepted pass: '%@' (uniqueID: %@, issuerCountry: %@)"
+ "B48@0:8@16@24@32^@40"
+ "B48@0:8Q16@24q32@40"
+ "Calling hasPassesWithSupportedNetworks - networks: %@, issuerCountryCodes: %@"
+ "Checking region '%@' with networks: %@"
+ "ElCorteIngles"
+ "Failed to send with success, identifier: %@, error: %@"
+ "Global fallback checking %lu unlisted countries"
+ "Global fallback hasMatchingCards: %@"
+ "Incorrect session type used. Delegate session: %{public}@, Delegate Request: %{public}@"
+ "Issuer country codes validation result: %@"
+ "Legacy validation hasMatchingCards: %@"
+ "Location Manager did fail with error: %@"
+ "NETWORK_NAME_ELCORTEINGLES"
+ "NETWORK_NAME_ELCORTEINGLES_CARD_NAME"
+ "Network validation result: %@"
+ "No 'default' region, falling back to global networks: %@"
+ "No issuerRegions, using legacy validation with topLevelNetworks: %@, issuerCountryCodes: %@"
+ "PKCanMakePayments returned: %@"
+ "PKCanMakePaymentsUsingIssuerRegionsWithCapabilities - topLevelNetworks: %@, issuerRegions: %@, capabilities: 0x%lx, issuerCountryCodes: %@"
+ "PKCanMakePaymentsUsingIssuerRegionsWithCapabilities returning NO"
+ "PKCanMakePaymentsUsingNetworksIssuerCountryCodesWithCapabilitiesAndRequestType - networks: %@, issuerCountryCodes: %@, capabilities: 0x%lx"
+ "PKCanMakePaymentsUsingNetworksIssuerCountryCodesWithCapabilitiesAndRequestType returning: %@"
+ "PKViewedTransactions-ResumingPowerThrottledFetch"
+ "Pass filtering: Passes removed after issuerRegions filter: %ld"
+ "Processing 'default' region"
+ "Received cloud zone invitiation: %@, from destination %@"
+ "Region '%@' has empty/nil networks, skipping"
+ "Region '%@' hasMatchingCards: %@"
+ "Remote instrument '%@' (country: %@) using issuerRegions networks: %@"
+ "Remote instrument '%@' ACCEPTED via issuerRegions (network: %@)"
+ "Remote instrument '%@' checking app network '%@' (normalized: '%@') against region networks: %@"
+ "Remote instrument '%@' rejected: empty issuerRegions for country '%@'"
+ "Remote instrument '%@' rejected: network not in issuerRegions for country '%@'"
+ "Skipping region '%@' - not in issuerCountryCodes filter"
+ "T@\"NSData\",&,N,V_issuerRegions"
+ "T@\"NSDictionary\",C,N,V_issuerRegions"
+ "T@\"NSDictionary\",R,C,N,V_issuerRegions"
+ "T@\"NSSet\",&,N,V_excludedTransactionSourceIdentifiers"
+ "T@\"PKProximitySetupLiaison\",&,N"
+ "T@\"PKProximitySetupLiaison\",&,N,VproximitySetupLiaison"
+ "TB,N,V_hasAcquiredProvisioningAssertion"
+ "TB,N,V_isInProximitySetup"
+ "TB,R,N,V_usesExternalView"
+ "TQ,R,N,V_preferredRecentTransactionMinimum"
+ "_PKHasExistingPassesForNetworksAndCountries - networks: %@, issuerCountryCodes: %@, result: %@"
+ "_excludedTransactionSourceIdentifiers"
+ "_excludedTransactionSourcesWithCompletion:"
+ "_filterExcludedTransactionSourceIdentifiers"
+ "_filterPassesForIssuerRegions:request:"
+ "_hasAcquiredProvisioningAssertion"
+ "_isInProximitySetup"
+ "_issuerRegions"
+ "_preferredRecentTransactionMinimum"
+ "_usesExternalView"
+ "acceptedPaymentApplicationsForPass: After issuerRegions filter, %lu applications"
+ "acceptedPaymentApplicationsForPass: App network '%@' in issuerRegions: YES"
+ "acceptedPaymentApplicationsForPass: App network '%@' not in issuerRegions: NO"
+ "acceptedPaymentApplicationsForPass: App rejected - doesn't support in-app payment"
+ "acceptedPaymentApplicationsForPass: App rejected - invalid state"
+ "acceptedPaymentApplicationsForPass: App rejected - merchant country not supported"
+ "acceptedPaymentApplicationsForPass: Final accepted applications: %lu"
+ "acceptedPaymentApplicationsForPass: Pass '%@' no explicit region match, using global networks"
+ "acceptedPaymentApplicationsForPass: Pass '%@' using issuerRegions filtering (country: %@)"
+ "acceptedPaymentApplicationsForPass: Starting with %lu applications"
+ "acceptedPaymentApplicationsForPass: regionNetworks: %@, regionNetworkIDs: %@"
+ "applyServiceProviderPropertiesToPaymentRequest:"
+ "categoriesAvailable"
+ "completeTaskWithError:throttled:"
+ "dc264f98-b0e2-4d96-9248-663a801e4fb1"
+ "delegateBundleID"
+ "delegateDomain"
+ "excludedTransactionSourceIdentifiers"
+ "excludedTransactionSourceIdentifiersWithCompletion:"
+ "filterExcludedTransactionSourceIdentifiers:"
+ "hasClickedOnSeeAll"
+ "hasExternalEntryPoints"
+ "hasIssuerRegions"
+ "hasPassesWithSupportedNetworks returned: %@"
+ "initWithDictionary:availableNetworks:"
+ "initWithNotificationIdentifier:accountIdentifier:accountBaseURL:"
+ "initWithServiceProviderOrder:action:"
+ "isCarKeySupportedForManufacturerIdentifier:issuerIdentifier:productPlanIdentifier:error:"
+ "isCompletedOrThrottled"
+ "isDelegate"
+ "isInProximitySetup"
+ "issuerRegions"
+ "issuerRegions filter: %lu -> %lu passes"
+ "issuerRegions filter: ACCEPT - Network '%@' matches global networks"
+ "issuerRegions filter: ACCEPT - Network '%@' matches region networks"
+ "issuerRegions filter: Checking %lu applications for global network match"
+ "issuerRegions filter: Checking %lu applications for region network match"
+ "issuerRegions filter: Checking app network '%@' (normalized: '%@') against global: %@"
+ "issuerRegions filter: Checking app network '%@' (normalized: '%@') against region: %@"
+ "issuerRegions filter: No app matched region networks"
+ "issuerRegions filter: No region match for country %@, hasDefaultRegion: %@"
+ "issuerRegions filter: Pass '%@' (country: %@) → regionNetworks: %@"
+ "issuerRegions filter: Pass '%@' has no issuer country, falling back to global networks"
+ "issuerRegions filter: REJECT - Card network not in explicit region networks (no fallback)"
+ "issuerRegions filter: REJECT - Country %@ not in supportedCountries"
+ "issuerRegions filter: REJECT - Default exists but returned nil"
+ "issuerRegions filter: REJECT - Empty region array (explicit rejection)"
+ "issuerRegions filter: REJECT - No applications match global networks"
+ "issuerRegions filter: REJECT - No global networks defined"
+ "issuerRegions filter: Region networks found: %@, normalizedRegionNetworks: %@"
+ "issuerRegions validation returning NO - no matching cards found"
+ "issuerRegions: ERROR - 'default' region has unexpected type: %@"
+ "issuerRegions: ERROR - region '%@' has unexpected type: %@"
+ "issuerRegions: Found region '%@' with flat array, networks: %@"
+ "issuerRegions: Found region '%@' with nested dict, networks: %@"
+ "issuerRegions: No match for '%@' and no 'default', falling back to global networks"
+ "issuerRegions: Using 'default' region with flat array, networks: %@"
+ "issuerRegions: Using 'default' region with nested dict, networks: %@"
+ "merchantsAvailable"
+ "others"
+ "passesAndTickets"
+ "pendingRequests"
+ "preferredRecentTransactionMinimum"
+ "recentActivity"
+ "recentOrdersAvailable"
+ "recentWalletActivityAvailable"
+ "searchBar"
+ "searchResultAvailable"
+ "searchSummary"
+ "sendTransactionsWithRequest:useSynchronous:completion:"
+ "setExcludedTransactionSourceIdentifiers:"
+ "setHasAcquiredProvisioningAssertion:"
+ "setIsInProximitySetup:"
+ "setIssuerRegions:"
+ "setPreferredRecentTransactionMinimum:"
+ "shouldCollectPlan:withAction:"
+ "supportsCapability:forAccount:paymentApplicationState:dpanSuffix:"
+ "throttled"
+ "topHit"
+ "unavailablePasses eval: '%@' (uniqueID: %@) isNotAccepted: %@"
+ "unavailablePasses: UNAVAILABLE - '%@'"
+ "unavailablePasses: acceptedPassIDs count: %lu, allPasses count: %lu"
+ "unavailablePasses: acceptedPassIDs: %@"
+ "usesExternalView"
+ "v24@0:8@\"PKProximitySetupLiaison\"16"
+ "walletSearch"
- "DC264F98-332F-481C-B7DE-7E80973B07BF"
- "T@\"NSArray\",&,N,V_excludedAccountStates"
- "T@\"NSArray\",&,N,V_excludedPeerPaymentAccountStates"
- "_excludedAccountStates"
- "_excludedPeerPaymentAccountStates"
- "completeTaskWithError:"
- "excludedAccountStates"
- "excludedPeerPaymentAccountStates"
- "filterOutAccountStates:"
- "filterOutPeerPaymentAccountStates:"
- "initWithNotificationIdentifier:accountIdentifier:"
- "isCarKeySupportedForManufacturerIdentifier:issuerIdentifier:productPlanIdentifier:"
- "setExcludedAccountStates:"
- "setExcludedPeerPaymentAccountStates:"
- "shouldIgnore"

```
