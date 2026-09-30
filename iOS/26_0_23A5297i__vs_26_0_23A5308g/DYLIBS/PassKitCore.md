## PassKitCore

> `/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore`

```diff

-1626.8.0.0.0
-  __TEXT.__text: 0x7ba4c4
-  __TEXT.__auth_stubs: 0x49b0
-  __TEXT.__objc_methlist: 0x6bec0
-  __TEXT.__const: 0x23a58
-  __TEXT.__cstring: 0x67a9c
-  __TEXT.__swift5_typeref: 0x581c
-  __TEXT.__constg_swiftt: 0x4d54
-  __TEXT.__swift5_reflstr: 0x41fd
+1629.6.0.0.0
+  __TEXT.__text: 0x7bc008
+  __TEXT.__auth_stubs: 0x49d0
+  __TEXT.__objc_methlist: 0x6c240
+  __TEXT.__const: 0x23ac8
+  __TEXT.__cstring: 0x68a9b
+  __TEXT.__swift5_typeref: 0x58c4
+  __TEXT.__constg_swiftt: 0x4d74
+  __TEXT.__swift5_reflstr: 0x41ed
   __TEXT.__swift5_fieldmd: 0x5104
-  __TEXT.__swift5_builtin: 0x3ac
+  __TEXT.__swift5_builtin: 0x3c0
   __TEXT.__swift5_assocty: 0x960
   __TEXT.__swift5_proto: 0xc80
-  __TEXT.__swift5_types: 0x518
-  __TEXT.__swift5_capture: 0x3d04
-  __TEXT.__oslogstring: 0x3483f
+  __TEXT.__swift5_types: 0x51c
+  __TEXT.__swift5_capture: 0x3d7c
+  __TEXT.__oslogstring: 0x3480f
   __TEXT.__swift_as_entry: 0xa0
   __TEXT.__swift_as_ret: 0xa8
   __TEXT.__swift5_protos: 0x40

   __TEXT.__swift5_types2: 0x4
   __TEXT.__gcc_except_tab: 0x7620
   __TEXT.__ustring: 0x1e7a
-  __TEXT.__unwind_info: 0x1b4d0
-  __TEXT.__eh_frame: 0x4a28
-  __TEXT.__objc_classname: 0xf7e0
-  __TEXT.__objc_methname: 0xcab2b
-  __TEXT.__objc_methtype: 0x17494
-  __TEXT.__objc_stubs: 0x59d60
-  __DATA_CONST.__got: 0x4930
-  __DATA_CONST.__const: 0x20c28
-  __DATA_CONST.__objc_classlist: 0x3a60
+  __TEXT.__unwind_info: 0x1b628
+  __TEXT.__eh_frame: 0x49f0
+  __TEXT.__objc_classname: 0xf878
+  __TEXT.__objc_methname: 0xcb205
+  __TEXT.__objc_methtype: 0x175f3
+  __TEXT.__objc_stubs: 0x5a0e0
+  __DATA_CONST.__got: 0x4978
+  __DATA_CONST.__const: 0x20fa0
+  __DATA_CONST.__objc_classlist: 0x3a80
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_protolist: 0x590
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23198
+  __DATA_CONST.__objc_selrefs: 0x232c8
   __DATA_CONST.__objc_protorefs: 0x250
-  __DATA_CONST.__objc_superrefs: 0x2ef0
-  __DATA_CONST.__objc_arraydata: 0x25d0
-  __AUTH_CONST.__auth_got: 0x24e8
-  __AUTH_CONST.__const: 0x1df48
-  __AUTH_CONST.__cfstring: 0x6f8c0
-  __AUTH_CONST.__objc_const: 0xc2fb0
-  __AUTH_CONST.__objc_arrayobj: 0xaf8
+  __DATA_CONST.__objc_superrefs: 0x2f00
+  __DATA_CONST.__objc_arraydata: 0x26e8
+  __AUTH_CONST.__auth_got: 0x24f8
+  __AUTH_CONST.__const: 0x1e558
+  __AUTH_CONST.__cfstring: 0x70de0
+  __AUTH_CONST.__objc_const: 0xc34d0
+  __AUTH_CONST.__objc_arrayobj: 0xc90
   __AUTH_CONST.__objc_intobj: 0x1068
   __AUTH_CONST.__objc_dictobj: 0x1540
   __AUTH_CONST.__objc_doubleobj: 0x2b0
-  __AUTH.__objc_data: 0x20370
+  __AUTH.__objc_data: 0x204b0
   __AUTH.__data: 0x3628
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0x6400
-  __DATA.__data: 0x7cd0
+  __DATA.__objc_ivar: 0x6430
+  __DATA.__data: 0x7cf0
   __DATA.__bss: 0x18498
-  __DATA.__common: 0xbf0
-  __DATA_DIRTY.__objc_ivar: 0x25b4
+  __DATA.__common: 0xc00
+  __DATA_DIRTY.__objc_ivar: 0x25c0
   __DATA_DIRTY.__objc_data: 0x57a8
   __DATA_DIRTY.__data: 0x160
-  __DATA_DIRTY.__bss: 0xcb8
+  __DATA_DIRTY.__bss: 0xcc0
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 08236E08-1B4A-3359-9AC2-2E8BDBD3A637
-  Functions: 49218
-  Symbols:   127474
-  CStrings:  66828
+  UUID: 89EB870F-4F47-3338-9DFB-53DF9C809991
+  Functions: 49353
+  Symbols:   127879
+  CStrings:  67234
 
Symbols:
+ +[PKAnalyticsErrorTextClassifier analyticsValueForResult:]
+ +[PKAnalyticsErrorTextClassifier classifyErrorText:]
+ +[PKAnalyticsErrorTextClassifier containsAnyTerm:inText:]
+ +[PKCreditAccountController shouldShowCardNumbersWithAccountAvailabilityInfo:dpanSuffixForPaymentApplication:]
+ +[PKPaymentDefaultDataProvider defaultDataProvider]
+ +[PKPaymentMessage canArchiveWithTransaction:]
+ +[PKPaymentOffersController dashboardInstance]
+ +[PKPaymentService paymentService]
+ +[PKProvisioningAnalyticsSessionPreflightReporter createUnaffiliatedReporter]
+ +[PKVirtualCard countOfVirtualCards]
+ -[PKAccount cardAvailabilityInfo]
+ -[PKAccountCardAvailabilityInfo .cxx_destruct]
+ -[PKAccountCardAvailabilityInfo accountState]
+ -[PKAccountCardAvailabilityInfo accountType]
+ -[PKAccountCardAvailabilityInfo initWithAccountState:accountType:supportedFeatures:]
+ -[PKAccountCardAvailabilityInfo supportedFeatures]
+ -[PKAutoFillCardCredential _setExpirationDate:]
+ -[PKAutoFillCardCredential initWithCardholderName:pan:expirationDate:securityCode:billingAddress:]
+ -[PKAutoFillCardDescriptor cardIsInWallet]
+ -[PKAutoFillCardDescriptor setCardIsInWallet:]
+ -[PKBalanceSummaryFetcher dealloc]
+ -[PKDashboardTransactionFetcher dealloc]
+ -[PKDiscoveryCard backgroundMediaCropped]
+ -[PKDiscoveryCard backgroundMediaExpanded]
+ -[PKDiscoveryMedia _remoteAssetForScale:]
+ -[PKDiscoveryMedia downloadImageDataWithScale:shouldWriteData:completion:]
+ -[PKDiscoveryMedia imageDataFromCacheWithScale:]
+ -[PKFPANCredential expiration]
+ -[PKMutableAutofillCardCredential setExpirationDate:]
+ -[PKPassShareActivationOption localizationKeyPostfixForInitiation]
+ -[PKPassShareActivationOptions containsKeyFob]
+ -[PKPassShareActivationOptions localizationKeyPostfixForInitiation]
+ -[PKPassVerificationMethod debugTypeDescription]
+ -[PKPaymentAuthorizationDataModel hasAutomaticallyPresentedPass]
+ -[PKPaymentAuthorizationDataModel setHasAutomaticallyPresentedPass:]
+ -[PKPaymentDefaultDataProvider paymentOfferCriteriaForPassUniqueID:criteriaType:completion:]
+ -[PKPaymentMessage shouldMessageArchiveWithTransaction:]
+ -[PKPaymentOffersController _initDashboardInstance]
+ -[PKPaymentOffersController _initWithPaymentService:paymentWebService:configuration:]
+ -[PKPaymentOffersController updateSessionDetails:]
+ -[PKPaymentPassActionExternalActionContent displayName]
+ -[PKPaymentProvisioningController analyticsReporter]
+ -[PKPaymentProvisioningController setAnalyticsReporter:]
+ -[PKPaymentRequest localizedPhysicalButtonConfirmationTitle]
+ -[PKPaymentRequest setLocalizedPhysicalButtonConfirmationTitle:]
+ -[PKPaymentService scheduleApplePayDemoActivitySignal]
+ -[PKPaymentService(FPAN) activeAutoFillCardCount]
+ -[PKPaymentService(PaymentOffers) paymentOfferCriteriaForPassUniqueID:criteriaType:completion:]
+ -[PKPaymentSetupFieldBuiltInCardExpiration init]
+ -[PKPaymentSetupProduct showOtherProviders]
+ -[PKPaymentSetupProductModel _updatePaymentSetupProduct:displayName:localizedDescription:longLocalizedDescription:partnerArray:productIdentifier:paymentOptions:termsURL:provisioningMethodDetailsList:readerModeMetadata:requiredFields:imageAssets:minimumOSVersion:region:regionData:hsa2Requirement:suppressPendingPurchases:supportedTransitNetworkIdentifiers:onboardingItems:actionBaseURL:productState:minimumProductAge:maximumProductAge:minimumTargetUserSupportedAge:associatedStoreIdentifiers:appLaunchURL:regionIdentifier:type:localizedNotificationTitle:localizedNotificationMessage:discoveryCardIdentifier:clientInfo:searchTerms:featureIdentifier:criteriaIdentifier:showOtherProviders:]
+ -[PKPaymentWebServiceLocalProxyTargetDevice canSaveFPANCardWithDescriptor:credential:completion:]
+ -[PKPaymentWebServiceRemoteProxyTargetDevice canSaveFPANCardWithDescriptor:credential:completion:]
+ -[PKPaymentWebServiceTargetDevice canSaveFPANCardWithDescriptor:credential:completion:]
+ -[PKPeerPaymentAccount isOwnerAccountPersonalized]
+ -[PKProvisioningAnalyticsSession createPreflightReporter]
+ -[PKProvisioningAnalyticsSession reportPreflightEventForReporter:context:]
+ -[PKProvisioningAnalyticsSession reportProvisioningStepForReporter:step:success:error:context:]
+ -[PKProvisioningAnalyticsSession reportProvisioningStepStartForReporter:step:context:]
+ -[PKProvisioningAnalyticsSessionPreflightReporter .cxx_destruct]
+ -[PKProvisioningAnalyticsSessionPreflightReporter _reportPreflightStepCompleteForContext:token:]
+ -[PKProvisioningAnalyticsSessionPreflightReporter _sendPendingEvents]
+ -[PKProvisioningAnalyticsSessionPreflightReporter affiliateReporter:]
+ -[PKProvisioningAnalyticsSessionPreflightReporter finishPreflightForToken:]
+ -[PKProvisioningAnalyticsSessionPreflightReporter reportAppExtensionPreflightComplete:token:]
+ -[PKProvisioningAnalyticsSessionPreflightReporter reportCredentialsPreflightComplete:token:]
+ -[PKProvisioningAnalyticsSessionPreflightReporter reportPreflightStepComplete:itemCount:token:]
+ -[PKProvisioningAnalyticsSessionPreflightReporter reportPreflightStepComplete:token:]
+ -[PKProvisioningAnalyticsSessionPreflightReporter startPreflight]
+ -[PKProvisioningAnalyticsSessionPreflightToken .cxx_destruct]
+ -[PKProvisioningAnalyticsSessionPreflightToken init]
+ -[PKProvisioningAnalyticsSessionPreflightToken start]
+ -[PKProvisioningAnalyticsSessionPreflightToken stepProperties]
+ -[PKProvisioningAnalyticsSessionStepReporter _reportProvisioningStep:finishedWithStatus:error:context:]
+ -[PKProvisioningAnalyticsSessionStepReporter reportProvisioningStep:finishedWithStatus:context:]
+ -[PKProvisioningAnalyticsSessionStepReporter reportProvisioningStepStart:]
+ -[PKProvisioningAnalyticsSessionStepReporter reportProvisioningStepStart:context:]
+ -[PKProvisioningAnalyticsSessionSubjectHandle _startReportingIfNecessary]
+ -[PKProvisioningAnalyticsSessionUIReporter setPass:]
+ -[PKSearchTransactionTypeResult creditDebitIndicator]
+ -[PKSearchTransactionTypeResult setCreditDebitIndicator:]
+ -[PKSpringAnimationFactory factoryWithInvertedVelocity]
+ GCC_except_table100
+ GCC_except_table106
+ GCC_except_table111
+ GCC_except_table116
+ GCC_except_table122
+ GCC_except_table126
+ GCC_except_table133
+ GCC_except_table134
+ GCC_except_table140
+ GCC_except_table149
+ GCC_except_table159
+ GCC_except_table169
+ GCC_except_table170
+ GCC_except_table177
+ GCC_except_table180
+ GCC_except_table215
+ GCC_except_table219
+ GCC_except_table232
+ GCC_except_table239
+ GCC_except_table249
+ GCC_except_table252
+ GCC_except_table258
+ GCC_except_table267
+ GCC_except_table270
+ GCC_except_table281
+ GCC_except_table283
+ GCC_except_table319
+ GCC_except_table323
+ GCC_except_table328
+ GCC_except_table333
+ GCC_except_table349
+ GCC_except_table357
+ GCC_except_table365
+ GCC_except_table380
+ GCC_except_table384
+ GCC_except_table389
+ GCC_except_table403
+ GCC_except_table406
+ GCC_except_table408
+ GCC_except_table410
+ GCC_except_table412
+ GCC_except_table423
+ GCC_except_table439
+ GCC_except_table449
+ GCC_except_table450
+ GCC_except_table455
+ GCC_except_table464
+ GCC_except_table466
+ GCC_except_table519
+ GCC_except_table523
+ GCC_except_table543
+ GCC_except_table546
+ GCC_except_table549
+ GCC_except_table567
+ GCC_except_table572
+ GCC_except_table66
+ GCC_except_table660
+ GCC_except_table67
+ GCC_except_table703
+ GCC_except_table711
+ GCC_except_table729
+ GCC_except_table80
+ GCC_except_table847
+ _.str.105
+ _.str.114
+ _.str.242
+ _.str.246
+ _.str.248
+ _.str.257
+ _.str.263
+ _.str.265
+ _.str.266
+ _.str.267
+ _.str.279
+ _.str.285
+ _.str.286
+ _.str.287
+ _.str.295
+ _.str.296
+ _.str.307
+ _.str.309
+ _.str.34
+ _.str.874
+ _.str.93
+ _.str.94
+ _NSFileProtectionCompleteUntilFirstUserAuthentication
+ _OBJC_CLASS_$_PKAccountCardAvailabilityInfo
+ _OBJC_CLASS_$_PKAnalyticsErrorTextClassifier
+ _OBJC_CLASS_$_PKProvisioningAnalyticsSessionPreflightReporter
+ _OBJC_CLASS_$_PKProvisioningAnalyticsSessionPreflightToken
+ _OBJC_IVAR_$_PKAccountCardAvailabilityInfo._accountState
+ _OBJC_IVAR_$_PKAccountCardAvailabilityInfo._accountType
+ _OBJC_IVAR_$_PKAccountCardAvailabilityInfo._supportedFeatures
+ _OBJC_IVAR_$_PKAutoFillCardCredential._expirationDate
+ _OBJC_IVAR_$_PKAutoFillCardCredential._expirationDateFormatter
+ _OBJC_IVAR_$_PKAutoFillCardDescriptor._cardIsInWallet
+ _OBJC_IVAR_$_PKDiscoveryCard._backgroundMediaByKey
+ _OBJC_IVAR_$_PKPaymentAuthorizationDataModel._hasAutomaticallyPresentedPass
+ _OBJC_IVAR_$_PKPaymentPassActionExternalActionContent._displayName
+ _OBJC_IVAR_$_PKPaymentProvisioningController._analyticsReporter
+ _OBJC_IVAR_$_PKPaymentRequest._localizedPhysicalButtonConfirmationTitle
+ _OBJC_IVAR_$_PKPaymentSetupProduct._showOtherProviders
+ _OBJC_IVAR_$_PKProvisioningAnalyticsSessionPreflightToken._start
+ _OBJC_IVAR_$_PKProvisioningAnalyticsSessionPreflightToken._stepProperties
+ _OBJC_IVAR_$_PKProvisioningAnalyticsSessionSubjectHandle._archivedParent
+ _OBJC_IVAR_$_PKProvisioningAnalyticsSessionSubjectHandle._didBeginSubject
+ _OBJC_IVAR_$_PKSearchTransactionTypeResult._creditDebitIndicator
+ _OBJC_IVAR_$_PKSpringAnimationFactory._invertedFactory
+ _OBJC_METACLASS_$_PKAccountCardAvailabilityInfo
+ _OBJC_METACLASS_$_PKAnalyticsErrorTextClassifier
+ _OBJC_METACLASS_$_PKProvisioningAnalyticsSessionPreflightReporter
+ _OBJC_METACLASS_$_PKProvisioningAnalyticsSessionPreflightToken
+ _PDScheduledActivityRemoveAll
+ _PKAccessibilityIdentifierMerchandisingDetails
+ _PKAccessibilityIdentifierOfferConfirmation
+ _PKAggDKeyApplePayButtonAppBundleIdentifierKey
+ _PKAggDKeyApplePayButtonCardContextCardArt
+ _PKAggDKeyApplePayButtonDeviceTypeKey
+ _PKAggDKeyApplePayButtonEnvironmentInApp
+ _PKAggDKeyApplePayButtonEnvironmentKey
+ _PKAggDKeyApplePayButtonErrorTypeButtonFinalContentNotRendered
+ _PKAggDKeyApplePayButtonErrorTypeXPCServiceInterrupted
+ _PKAggDKeyApplePayButtonErrorTypeXPCServiceInvalidated
+ _PKAggDKeyApplePayButtonEvent
+ _PKAggDKeyApplePayButtonEventType
+ _PKAggDKeyApplePayButtonEventTypeApplePayButtonRequest
+ _PKAggDKeyApplePayButtonIsDynamicKey
+ _PKAggDKeyApplePayButtonIssuer
+ _PKAggDKeyApplePayButtonNetworkName
+ _PKAggDKeyApplePayButtonOSVersionKey
+ _PKAggDKeyApplePayButtonProductSubType
+ _PKAggDKeyApplePayButtonReferralSource
+ _PKAggDKeyApplePayButtonTypeAddMoney
+ _PKAggDKeyApplePayButtonTypeBook
+ _PKAggDKeyApplePayButtonTypeBuy
+ _PKAggDKeyApplePayButtonTypeCheckout
+ _PKAggDKeyApplePayButtonTypeContinue
+ _PKAggDKeyApplePayButtonTypeContribute
+ _PKAggDKeyApplePayButtonTypeDonate
+ _PKAggDKeyApplePayButtonTypeInStore
+ _PKAggDKeyApplePayButtonTypeKey
+ _PKAggDKeyApplePayButtonTypeOrder
+ _PKAggDKeyApplePayButtonTypePlain
+ _PKAggDKeyApplePayButtonTypeReload
+ _PKAggDKeyApplePayButtonTypeRent
+ _PKAggDKeyApplePayButtonTypeSetUp
+ _PKAggDKeyApplePayButtonTypeSubscribe
+ _PKAggDKeyApplePayButtonTypeSupport
+ _PKAggDKeyApplePayButtonTypeTip
+ _PKAggDKeyApplePayButtonTypeTopUp
+ _PKAnalyticsApplePayButtonRequestEventDailyLimit
+ _PKAnalyticsKeyReportApplePayDemoCompletedWithinKey
+ _PKAnalyticsKeyReportHasContactlessTransactionWithinKey
+ _PKAnalyticsKeyReportHasPaymentPassKey
+ _PKAnalyticsReportAccountNumberSpecified
+ _PKAnalyticsReportAddMoney
+ _PKAnalyticsReportAddMoneySpecified
+ _PKAnalyticsReportApplePayDemoActivityFollowUpTag
+ _PKAnalyticsReportBalanceDetailsPageTag
+ _PKAnalyticsReportBankConnectInfoPageTag
+ _PKAnalyticsReportConnectedCardTermsUpdate
+ _PKAnalyticsReportDashboardMessage
+ _PKAnalyticsReportDashboardMessageDismiss
+ _PKAnalyticsReportDashboardMessageType
+ _PKAnalyticsReportDigitalServicing
+ _PKAnalyticsReportDigitalServicingSpecified
+ _PKAnalyticsReportErrorTextGroupKey
+ _PKAnalyticsReportEventTypePreflightStatus
+ _PKAnalyticsReportEventTypeSetupFlowFinished
+ _PKAnalyticsReportFrontOfPass
+ _PKAnalyticsReportIBANSpecified
+ _PKAnalyticsReportIncorrectMerchantInfo
+ _PKAnalyticsReportIsBankConnected
+ _PKAnalyticsReportIsBankEligible
+ _PKAnalyticsReportIsSpendingSummaryAvailable
+ _PKAnalyticsReportLinkToMaps
+ _PKAnalyticsReportManageConnection
+ _PKAnalyticsReportPassAutomaticSelectionAppliedKey
+ _PKAnalyticsReportPayBill
+ _PKAnalyticsReportPayBillSpecified
+ _PKAnalyticsReportPeriod1Month
+ _PKAnalyticsReportPeriod6Months
+ _PKAnalyticsReportPriorMonthButtonTag
+ _PKAnalyticsReportPriorYearButtonTag
+ _PKAnalyticsReportProvisioningStepStartKey
+ _PKAnalyticsReportReferralSourcePlusButton
+ _PKAnalyticsReportRoutingNumberSpecified
+ _PKAnalyticsReportSetupFieldsPrefilledKey
+ _PKAnalyticsReportSetupFieldsVisibleKey
+ _PKAnalyticsReportSortCodeSpecified
+ _PKAnalyticsReportSpendingSummaryViewCategoryButtonTag
+ _PKAnalyticsReportSpendingSummaryViewMerchantButtonTag
+ _PKAnalyticsReportTransactionButtonTag
+ _PKAnalyticsReportTransactionDate
+ _PKAnalyticsReportTransactionMapSpecified
+ _PKAnalyticsReportTransactionStatus
+ _PKAnalyticsReportTransactionSummaryPageTag
+ _PKAnalyticsReportTransactionType
+ _PKAnalyticsReportUpdateLinkSpecified
+ _PKAnalyticsReportVerificationChannelOptionsKey
+ _PKAnalyticsSubjectApplePayUserEducationDemo
+ _PKAnalyticsSubjectFinanceKitSetup
+ _PKAnalyticsSubjectFinanceKitTransactionPicker
+ _PKExpirationDateFormatter
+ _PKMPANsUnifiedViewEnabled
+ _PKMapsSnapshotsCacheCreateDirectory
+ _PKMapsSnapshotsCacheCreateDirectoryURL
+ _PKMapsSnapshotsCacheCreateFileURL
+ _PKMerchantCategoryFromFKPaymentTransactionCategory
+ _PKPassAssetDownloadCacheCreateDirectory
+ _PKPassAssetDownloadCacheCreateDirectoryURL
+ _PKPassAssetDownloadCacheCreateFileURL
+ _PKPaymentRequestClientAnalyticsParametersArchivedParentTokenKey
+ _PKPaymentRequestLocalizedPhysicalButtonConfirmationTitleKey
+ _PKPaymentSetupProductShowOtherProvidersKey
+ _PKPaymentSheetShowExpressProvisioning
+ _PKRemoteInstrumentThumbnailsCacheCreateDirectory
+ _PKRemoteInstrumentThumbnailsCacheCreateDirectoryURL
+ _PKRemoteInstrumentThumbnailsCacheCreateFileURL
+ _PKSFSymbolPrefixForCurrencyCode
+ _PKSetMerchantTokenUpcomingPaymentNotificationsEnabled
+ _PKSharedCacheCreateDirectory
+ _PKSharedCacheCreateDirectoryURL
+ _PKSharedCacheCreateFileURL
+ _PKSupportsSearchForPass
+ _PPKAggDKeyApplePayButtonErrorType
+ _PPKAggDKeyApplePayButtonErrorTypeNoPassImageReceived
+ __MergedGlobals.29
+ __MergedGlobals.35
+ __OBJC_$_CLASS_METHODS_PKAnalyticsErrorTextClassifier
+ __OBJC_$_CLASS_METHODS_PKPaymentDefaultDataProvider
+ __OBJC_$_CLASS_METHODS_PKPaymentOffersController
+ __OBJC_$_CLASS_METHODS_PKPaymentService
+ __OBJC_$_CLASS_METHODS_PKProvisioningAnalyticsSessionPreflightReporter
+ __OBJC_$_INSTANCE_METHODS_PKAccountCardAvailabilityInfo
+ __OBJC_$_INSTANCE_METHODS_PKProvisioningAnalyticsSessionPreflightReporter
+ __OBJC_$_INSTANCE_METHODS_PKProvisioningAnalyticsSessionPreflightToken
+ __OBJC_$_INSTANCE_VARIABLES_PKAccountCardAvailabilityInfo
+ __OBJC_$_INSTANCE_VARIABLES_PKProvisioningAnalyticsSessionPreflightReporter
+ __OBJC_$_INSTANCE_VARIABLES_PKProvisioningAnalyticsSessionPreflightToken
+ __OBJC_$_PROP_LIST_PKAccountCardAvailabilityInfo
+ __OBJC_$_PROP_LIST_PKProvisioningAnalyticsSessionPreflightToken
+ __OBJC_$_PROP_LIST_PKSpringAnimationFactory.71
+ __OBJC_CLASS_RO_$_PKAccountCardAvailabilityInfo
+ __OBJC_CLASS_RO_$_PKAnalyticsErrorTextClassifier
+ __OBJC_CLASS_RO_$_PKProvisioningAnalyticsSessionPreflightReporter
+ __OBJC_CLASS_RO_$_PKProvisioningAnalyticsSessionPreflightToken
+ __OBJC_METACLASS_RO_$_PKAccountCardAvailabilityInfo
+ __OBJC_METACLASS_RO_$_PKAnalyticsErrorTextClassifier
+ __OBJC_METACLASS_RO_$_PKProvisioningAnalyticsSessionPreflightReporter
+ __OBJC_METACLASS_RO_$_PKProvisioningAnalyticsSessionPreflightToken
+ __PDScheduledActivityRemoveAll
+ ___100-[PKPaymentService submitUserConfirmation:forTransactionIdentifier:sessionExchangeToken:completion:]_block_invoke.319
+ ___101-[PKPaymentService transactionCountByPeriodForRequest:calendar:unit:includePurchaseTotal:completion:]_block_invoke.150
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke.529
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke.535
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_2.530
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_2.536
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_3.531
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_3.537
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_4.532
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_5.533
+ ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_6.534
+ ___102-[PKPaymentService recordPaymentApplicationUsageForPassUniqueIdentifier:paymentApplicationIdentifier:]_block_invoke.242
+ ___103-[PKPaymentService submitTransactionSignatureForTransactionIdentifier:sessionExchangeToken:completion:]_block_invoke.322
+ ___104-[PKMobileAssetManager dynamicAssetWithIdentifier:mappedIdentifierPrefix:parameters:timeout:completion:]_block_invoke.396
+ ___104-[PKMobileAssetManager dynamicAssetWithIdentifier:mappedIdentifierPrefix:parameters:timeout:completion:]_block_invoke.397
+ ___104-[PKSecureElement createAliroHomeKeyWithReaderIdentifier:readerPublicKey:homeIdentifier:withCompletion:]_block_invoke.313
+ ___106-[PKPaymentService submitBarcodePaymentEvent:forPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.324
+ ___107-[PKPaymentService insertOrUpdatePaymentTransaction:forPassUniqueIdentifier:paymentApplication:completion:]_block_invoke.141
+ ___107-[PKPaymentService registerAuxiliaryCapabilityForPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.306
+ ___107-[PKPaymentService retrieveDecryptedBarcodeCredentialForPassUniqueIdentifier:authorization:withCompletion:]_block_invoke.310
+ ___108-[PKPaymentService(PaymentOffers) updatePaymentRewardsRedemptionsWithPassUniqueIdentifier:limit:completion:]_block_invoke.39
+ ___109-[PKPaymentService conflictingExpressPassIdentifiersForPassInformation:withReferenceExpressState:completion:]_block_invoke.231
+ ___109-[PKPaymentService peerPaymentCounterpartHandlesForTransactionSourceIdentifier:startDate:endDate:completion:]_block_invoke.138
+ ___109-[PKPaymentService(PaymentOffers) paymentRewardsRedemptionsForPassUniqueIdentifier:paymentHashes:completion:]_block_invoke.37
+ ___109-[PKPaymentWebService _performVerificationRequest:selectedMethodGroup:selectedMethod:pass:taskID:completion:]_block_invoke.466
+ ___110+[PKCreditAccountController shouldShowCardNumbersWithAccountAvailabilityInfo:dpanSuffixForPaymentApplication:]_block_invoke
+ ___110-[PKRemoteAssetManager _downloadRemoteAssetItem:withCloudStoreCoordinatorDelegate:shouldWriteData:completion:]_block_invoke.51
+ ___111-[PKPaymentProvisioningController resolveLocalEligibilityRequirementsForAppleBalanceCredential:withCompletion:]_block_invoke.568
+ ___111-[PKPaymentProvisioningController resolveLocalEligibilityRequirementsForAppleBalanceCredential:withCompletion:]_block_invoke.576
+ ___111-[PKPaymentService conflictingExpressPassIdentifiersForPassConfiguration:withReferenceExpressState:completion:]_block_invoke.230
+ ___112-[PKPaymentService _submitVerificationCode:verificationData:forDPANIdentifier:usingSynchronousProxy:completion:]_block_invoke.135
+ ___112-[PKPaymentService retrievePINEncryptionCertificateForPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.314
+ ___115-[PKPaymentService passUniqueIdentifierForTransactionWithServiceIdentifier:transactionSourceIdentifier:completion:]_block_invoke.177
+ ___115-[PKPaymentWebService backgroundDownloadRemotePassAssets:forSuffixesAndScreenScales:cloudStoreCoordinatorDelegate:]_block_invoke.720
+ ___115-[PKPaymentWebService backgroundDownloadRemotePassAssets:forSuffixesAndScreenScales:cloudStoreCoordinatorDelegate:]_block_invoke.723
+ ___115-[PKPaymentWebService backgroundDownloadRemotePassAssets:forSuffixesAndScreenScales:cloudStoreCoordinatorDelegate:]_block_invoke.727
+ ___115-[PKPaymentWebService backgroundDownloadRemotePassAssets:forSuffixesAndScreenScales:cloudStoreCoordinatorDelegate:]_block_invoke.729
+ ___115-[PKPaymentWebService backgroundDownloadRemotePassAssets:forSuffixesAndScreenScales:cloudStoreCoordinatorDelegate:]_block_invoke_2.730
+ ___117-[PKPaymentService insertOrUpdateValueAddedServiceTransaction:forPassUniqueIdentifier:paymentTransaction:completion:]_block_invoke.209
+ ___119-[PKPaymentService transactionsForTransactionSourceIdentifiers:withTransactionSource:withBackingData:limit:completion:]_block_invoke.148
+ ___127-[PKPaymentService removeMapsDataForTransactionWithIdentifier:forTransactionSourceIdentifier:issueReportIdentifier:completion:]_block_invoke.144
+ ___128-[PKPaymentService cashbackByPeriodForTransactionSourceIdentifiers:withStartDate:endDate:calendar:calendarUnit:type:completion:]_block_invoke.152
+ ___128-[PKPaymentService retrieveDecryptedBarcodeCredentialForPassUniqueIdentifier:authorization:sessionExchangeToken:withCompletion:]_block_invoke.312
+ ___130-[PKPaymentWebService _passActionGroupIncludingAppletDataWithRemoteContentPassActionGroup:forPass:forDeviceIdentifier:completion:]_block_invoke.763
+ ___132-[PKDashboardTransactionFetcher _processPaymentPassTransactionsWithTransactions:synchronous:currentMonthOnly:sendTransactionsBlock:]_block_invoke.87
+ ___132-[PKDashboardTransactionFetcher _processPaymentPassTransactionsWithTransactions:synchronous:currentMonthOnly:sendTransactionsBlock:]_block_invoke_2.89
+ ___136-[PKPaymentService transactionsForTransactionSourceIdentifiers:matchingMerchant:withTransactionSource:withBackingData:limit:completion:]_block_invoke.154
+ ___137-[PKPaymentService transactionsForTransactionSourceIdentifiers:withTransactionSource:withBackingData:startDate:endDate:limit:completion:]_block_invoke.145
+ ___140-[PKPaymentService rangingSuspensionReasonForAppletSubcredentialIdentifier:paymentApplicationIdentifier:secureElementIdentifier:completion:]_block_invoke.285
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.431
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.435
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.436
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke_2.432
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke_2.434
+ ___144-[PKPaymentService pendingTransactionsForTransactionSourceIdentifiers:withTransactionSource:withBackingData:startDate:endDate:limit:completion:]_block_invoke.158
+ ___145-[PKPaymentService approvedTransactionsForTransactionSourceIdentifiers:withTransactionSource:withBackingData:startDate:endDate:limit:completion:]_block_invoke.157
+ ___149-[PKPaymentService processTransitTransactionEventWithHistory:transactionDate:forPaymentApplication:withPassUniqueIdentifier:expressTransactionState:]_block_invoke.241
+ ___151-[PKPaymentService transactionsForTransactionSourceIdentifiers:withTransactionSource:withBackingData:startDate:endDate:orderedByDate:limit:completion:]_block_invoke.147
+ ___153-[PKPaymentService transactionsForTransactionSourceIdentifiers:withPeerPaymentCounterpartHandles:withTransactionSource:withBackingData:limit:completion:]_block_invoke.153
+ ___154-[PKPaymentService installmentPlanTransactionsForTransactionSourceIdentifiers:accountIdentifier:redeemed:withRedemptionType:startDate:endDate:completion:]_block_invoke.169
+ ___157-[PKPaymentService transactionsForTransactionSourceIdentifiers:withTransactionType:withTransactionSource:withBackingData:startDate:endDate:limit:completion:]_block_invoke.156
+ ___157-[PKPaymentService(PaymentOffers) paymentOffersMerchandisingForSessionDetails:merchandisingIdentifiers:needsProvisioningMerchandisingIdentifiers:completion:]_block_invoke.42
+ ___158-[PKPaymentService transactionsForTransactionSourceIdentifiers:withMerchantCategory:withTransactionSource:withBackingData:startDate:endDate:limit:completion:]_block_invoke.155
+ ___36+[PKWebService _sharedCookieStorage]_block_invoke_2
+ ___36-[PKPaymentService consistencyCheck]_block_invoke.259
+ ___37-[PKIDSManager deleteArchivedDevices]_block_invoke
+ ___38-[PKDiscoveryCard initWithDictionary:]_block_invoke
+ ___42-[PKPeerPaymentRecipientCache _canReadMap]_block_invoke
+ ___43-[PKPaymentService productsWithCompletion:]_block_invoke.354
+ ___43-[PKPeerPaymentRecipientCache _canWriteMap]_block_invoke
+ ___44-[PKPaymentService initializeSecureElement:]_block_invoke.219
+ ___45-[PKPaymentService insertUserLegalAgreement:]_block_invoke.397
+ ___46-[PKIDSManager _createThumbnailCacheDirectory]_block_invoke
+ ___46-[PKPassShareActivationOptions containsKeyFob]_block_invoke
+ ___46-[PKPeerPaymentRecipientCache _writeMapToDisk]_block_invoke
+ ___48-[PKPaymentService mapsMerchantsWithCompletion:]_block_invoke.180
+ ___48-[PKSecureElement SEPPairingInfoWithCompletion:]_block_invoke.266
+ ___49-[PKPaymentHeroImage imageFilePathForImageModel:]_block_invoke
+ ___49-[PKPaymentService currentSecureElementSnapshot:]_block_invoke.385
+ ___49-[PKPaymentService deleteReservation:completion:]_block_invoke.389
+ ___49-[PKPaymentService(FPAN) activeAutoFillCardCount]_block_invoke
+ ___50-[PKPaymentOffersController updateSessionDetails:]_block_invoke
+ ___50-[PKPaymentOffersController updateSessionDetails:]_block_invoke_2
+ ___50-[PKPaymentService sharedPaymentWebServiceContext]_block_invoke.278
+ ___50-[PKPaymentService submitApplyRequest:completion:]_block_invoke.342
+ ___50-[PKPaymentService submitTermsRequest:completion:]_block_invoke.346
+ ___50-[PKPeerPaymentRecipientCache _updateMapsFromDisk]_block_invoke
+ ___51-[PKPaymentService logoImageDataForURL:completion:]_block_invoke.173
+ ___51-[PKPaymentService productsWithRequest:completion:]_block_invoke.352
+ ___51-[PKPaymentService submitDeleteRequest:completion:]_block_invoke.347
+ ___51-[PKSecureElement appletWithIdentifier:completion:]_block_invoke.279
+ ___52+[PKPaymentHeroImageManifest manifestFileForRegion:]_block_invoke
+ ___52-[PKSecureElement signatureForAuthToken:completion:]_block_invoke.307
+ ___52-[PKSecureElement signedPlatformDataWithCompletion:]_block_invoke.310
+ ___53-[PKPaymentService submitDocumentRequest:completion:]_block_invoke.344
+ ___53-[PKWebService URLSession:task:didCompleteWithError:]_block_invoke.333
+ ___53-[PKWebService URLSession:task:didCompleteWithError:]_block_invoke.339
+ ___53-[PKWebService URLSession:task:didCompleteWithError:]_block_invoke.340
+ ___54-[PKPaymentService featureApplicationsWithCompletion:]_block_invoke.340
+ ___54-[PKPaymentService regionsWithIdentifiers:completion:]_block_invoke.288
+ ___54-[PKPaymentService transactionsForRequest:completion:]_block_invoke.170
+ ___55-[PKPaymentService performDeviceCheckInWithCompletion:]_block_invoke.351
+ ___55-[PKPaymentService pushProvisioningSharingIdentifiers:]_block_invoke.372
+ ___55-[PKSecureElement appletCredentialsForAIDs:completion:]_block_invoke.273
+ ___56+[PKDiagnostics saveTransitState:forPaymentApplication:]_block_invoke_2
+ ___56+[PKDiagnostics saveTransitState:forPaymentApplication:]_block_invoke_3
+ ___56-[PKPaymentService credentialWithIdentifier:completion:]_block_invoke.368
+ ___57-[PKPaymentService regionsMatchingName:types:completion:]_block_invoke.289
+ ___57-[PKPaymentService submitVerificationRequest:completion:]_block_invoke.345
+ ___58-[PKPaymentService familyMembersIgnoringCache:completion:]_block_invoke.325
+ ___58-[PKSecureElement allAppletsAndCredentialsWithCompletion:]_block_invoke.269
+ ___59-[PKPaymentService memberTypeForCurrentUserWithCompletion:]_block_invoke.326
+ ___59-[PKPaymentService performProductActionRequest:completion:]_block_invoke.355
+ ___59-[PKPaymentService requiresUpgradedPasscodeWithCompletion:]_block_invoke.304
+ ___59-[PKPaymentService storeTransactionReceiptData:completion:]_block_invoke.393
+ ___59-[PKPaymentService subcredentialInvitationsWithCompletion:]_block_invoke.362
+ ___60-[PKPaymentProvisioningController _noteProvisioningDidBegin]_block_invoke.609
+ ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke.877
+ ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke.883
+ ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke_2.876
+ ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke_2.880
+ ___61-[PKPaymentService changePasscodeFrom:toPasscode:completion:]_block_invoke.305
+ ___61-[PKPaymentService statusForShareableCredentials:completion:]_block_invoke.375
+ ___61-[PKPaymentWebService configurePaymentServiceWithCompletion:]_block_invoke.337
+ ___61-[PKPaymentWebService configurePaymentServiceWithCompletion:]_block_invoke.342
+ ___61-[PKPaymentWebService provisionPassesWithRequest:completion:]_block_invoke.439
+ ___62-[PKPaymentOffersController _performCancelRequest:completion:]_block_invoke.193
+ ___62-[PKPaymentOffersController _performCancelRequest:completion:]_block_invoke_2.194
+ ___62-[PKPaymentOffersController _performSelectRequest:completion:]_block_invoke.189
+ ___62-[PKPaymentOffersController _performSelectRequest:completion:]_block_invoke_2.190
+ ___62-[PKPaymentService addRemoteDevicePendingProvisioningReceipt:]_block_invoke.293
+ ___62-[PKPaymentService generateUnderlyingKeyReportWithCompletion:]_block_invoke.299
+ ___62-[PKPaymentService transactionReceiptWithUniqueID:completion:]_block_invoke.390
+ ___62-[PKPaymentService transactionsForPredicate:limit:completion:]_block_invoke.175
+ ___63-[PKPaymentOffersController _performCatalogRequest:completion:]_block_invoke.145
+ ___63-[PKPaymentOffersController _performCatalogRequest:completion:]_block_invoke.149
+ ___63-[PKPaymentOffersController _performCatalogRequest:completion:]_block_invoke_2.150
+ ___63-[PKPaymentOffersController _performConfirmRequest:completion:]_block_invoke.181
+ ___63-[PKPaymentOffersController _performConfirmRequest:completion:]_block_invoke_2.182
+ ___63-[PKPaymentOffersController _performConfirmRequest:completion:]_block_invoke_3.180
+ ___63-[PKPaymentOffersController _performConfirmRequest:completion:]_block_invoke_3.184
+ ___63-[PKPaymentService currentPasscodeMeetsUpgradedPasscodePolicy:]_block_invoke.303
+ ___63-[PKPaymentService photosForFamilyMembersWithDSIDs:completion:]_block_invoke.329
+ ___63-[PKPaymentService refreshMerchantTokenMetadataWithCompletion:]_block_invoke.291
+ ___63-[PKPaymentService removeExpressPassesWithCardType:completion:]_block_invoke.235
+ ___63-[PKPaymentWebService _nonceWithRequest:serviceURL:completion:]_block_invoke.809
+ ___63-[PKPaymentWebService sendOwnershipTokensForReason:completion:]_block_invoke.382
+ ___63-[PKPaymentWebService sendOwnershipTokensForReason:completion:]_block_invoke_2.383
+ ___64-[PKPaymentService displayTapToRadarAlertForRequest:completion:]_block_invoke.122
+ ___64-[PKPaymentService enforceUpgradedPasscodePolicyWithCompletion:]_block_invoke.302
+ ___64-[PKPaymentService featureApplicationWithIdentifier:completion:]_block_invoke.341
+ ___64-[PKPaymentService passOwnershipTokenWithIdentifier:completion:]_block_invoke.356
+ ___64-[PKPaymentService redeemPaymentShareableCredential:completion:]_block_invoke.381
+ ___64-[PKPaymentService revokeCredentialsWithIdentifiers:completion:]_block_invoke.366
+ ___64-[PKPaymentWebServiceLocalProxyTargetDevice initWithConnection:]_block_invoke.292
+ ___65-[PKAutoFillCardManager userDidUseCardWithDescriptor:credential:]_block_invoke.65
+ ___65-[PKPaymentService isPassExpressWithUniqueIdentifier:completion:]_block_invoke.240
+ ___65-[PKPaymentService notifyForFPANCardImportConsentWithCompletion:]_block_invoke.295
+ ___65-[PKPaymentService passSharesForCredentialIdentifier:completion:]_block_invoke.370
+ ___65-[PKPaymentService pendingFamilyMembersIgnoringCache:completion:]_block_invoke.328
+ ___65-[PKPaymentService revokeMerchantTokenWithIdentifier:completion:]_block_invoke.292
+ ___65-[PKPaymentService sharedPaymentWebServiceContextWithCompletion:]_block_invoke.280
+ ___65-[PKPaymentService transactionsTotalAmountForRequest:completion:]_block_invoke.171
+ ___65-[PKPaymentWebService _applePayTrustPublicKeyHashWithCompletion:]_block_invoke.952
+ ___65-[PKSecureElement initializeSecureElementIfNecessaryWithHandler:]_block_invoke.263
+ ___66-[PKPaymentService defaultPaymentPassIngestionSpecificIdentifier:]_block_invoke.330
+ ___66-[PKPaymentService registerCredentialsWithIdentifiers:completion:]_block_invoke.364
+ ___66-[PKPaymentService setBalanceReminder:forBalance:pass:completion:]_block_invoke.192
+ ___66-[PKPaymentService transactionWithReferenceIdentifier:completion:]_block_invoke.166
+ ___67-[PKPassShareActivationOptions localizationKeyPostfixForInitiation]_block_invoke
+ ___67-[PKPassShareActivationOptions localizationKeyPostfixForInitiation]_block_invoke_2
+ ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.314
+ ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.321
+ ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.328
+ ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.336
+ ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.345
+ ___67-[PKPaymentService addPlaceholderPassWithConfiguration:completion:]_block_invoke.360
+ ___67-[PKPaymentService clearFPANCardImportNotificationsWithCompletion:]_block_invoke.297
+ ___67-[PKPaymentService redeemProvisioningSharingIdentifier:completion:]_block_invoke.383
+ ___67-[PKPaymentService requestNotificationAuthorizationWithCompletion:]_block_invoke.263
+ ___67-[PKSecureElement consistencyCheckDeviceCredentialsWithCompletion:]_block_invoke.277
+ ___68-[PKPaymentService deleteTransactionReceiptWithUniqueID:completion:]_block_invoke.394
+ ___68-[PKPaymentService transactionWithTransactionIdentifier:completion:]_block_invoke.160
+ ___68-[PKPaymentService updateAllMapsBrandAndMerchantDataWithCompletion:]_block_invoke.281
+ ___68-[PKPaymentWebService retrieveMerchantTokensWithRequest:completion:]_block_invoke.787
+ ___68-[PKSecureElement markAppletsWithIdentifiersForDeletion:completion:]_block_invoke.299
+ ___69+[PKPaymentHeroImageManifest saveManifestDataToDeviceForRegion:data:]_block_invoke
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.345
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.347
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.354
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.356
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.372
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.373
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.378
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_2.357
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_2.366
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_2.375
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_2.379
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_3.359
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_3.376
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_3.381
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_4.360
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_4.371
+ ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_4.377
+ ___69-[PKPaymentOffersController _performMerchandisingRequest:completion:]_block_invoke.133
+ ___69-[PKPaymentOffersController _performPaymentOffersRequest:completion:]_block_invoke.165
+ ___69-[PKPaymentOffersController _performPaymentOffersRequest:completion:]_block_invoke_2.166
+ ___69-[PKPaymentService featureApplicationsForProvisioningWithCompletion:]_block_invoke.334
+ ___69-[PKPaymentService initializeSecureElementIfNecessaryWithCompletion:]_block_invoke.217
+ ___69-[PKPaymentService removeExpressPassWithUniqueIdentifier:completion:]_block_invoke.237
+ ___69-[PKPaymentService reserveStorageForAppletTypes:metadata:completion:]_block_invoke.387
+ ___69-[PKPaymentService setExpressWithPassInformation:credential:handler:]_block_invoke.234
+ ___69-[PKSecureElement _startSecureElementManagerSessionWithType:handler:]_block_invoke.245
+ ___69-[PKSecureElement _startSecureElementManagerSessionWithType:handler:]_block_invoke.248
+ ___70-[PKMobileAssetManager _downloadPrefetchableAssetsForType:completion:]_block_invoke.405
+ ___70-[PKMobileAssetManager _downloadPrefetchableAssetsForType:completion:]_block_invoke.410
+ ___70-[PKPaymentOffersController _performDynamicContentRequest:completion:]_block_invoke.199
+ ___70-[PKPaymentOffersController _performDynamicContentRequest:completion:]_block_invoke.201
+ ___70-[PKPaymentOffersController _performDynamicContentRequest:completion:]_block_invoke_2.202
+ ___70-[PKPaymentOffersController _performRewardsBalanceRequest:completion:]_block_invoke.242
+ ___70-[PKPaymentOffersController _performRewardsBalanceRequest:completion:]_block_invoke.244
+ ___70-[PKPaymentOffersController _performRewardsBalanceRequest:completion:]_block_invoke_2.243
+ ___70-[PKPaymentOffersController _performRewardsBalanceRequest:completion:]_block_invoke_2.245
+ ___70-[PKPaymentProvisioningController deleteCredential:completionHandler:]_block_invoke.737
+ ___70-[PKPaymentProvisioningController deleteCredential:completionHandler:]_block_invoke.740
+ ___70-[PKPaymentService accountAttestationAnonymizationSaltWithCompletion:]_block_invoke.357
+ ___70-[PKPaymentService revokeCredentialsWithReaderIdentifiers:completion:]_block_invoke.367
+ ___70-[PKPaymentService suggestPaymentFPANCredentialImport:withCompletion:]_block_invoke.294
+ ___70-[PKPaymentService transactionsWithTransactionIdentifiers:completion:]_block_invoke.161
+ ___70-[PKPaymentWebService _handlePassListDownloadTask:data:fromPushTopic:]_block_invoke.907
+ ___70-[PKSecureElement signChallenge:forPaymentApplication:withCompletion:]_block_invoke.301
+ ___70-[PKSecureElement signChallenge:signatureEntanglementMode:completion:]_block_invoke.302
+ ___71-[PKPaymentService featureApplicationsForAccountIdentifier:completion:]_block_invoke.331
+ ___71-[PKPaymentService plansForPaymentPassWithUniqueIdentifier:completion:]_block_invoke.189
+ ___71-[PKPaymentService removeExpressPassWithUniqueIdentifierV2:completion:]_block_invoke.236
+ ___71-[PKPaymentService setExpressWithPassConfiguration:credential:handler:]_block_invoke.232
+ ___72-[PKPaymentProvisioningController _identityConfigurationWithCompletion:]_block_invoke.472
+ ___73-[PKPaymentAuthorizationStateMachine _performRewrapRequestImplWithParam:]_block_invoke.292
+ ___73-[PKPaymentAuthorizationStateMachine _performRewrapRequestImplWithParam:]_block_invoke.296
+ ___73-[PKPaymentAuthorizationStateMachine _performRewrapRequestImplWithParam:]_block_invoke_2.299
+ ___73-[PKPaymentService ambiguousTransactionWithServiceIdentifier:completion:]_block_invoke.396
+ ___73-[PKPaymentService clearFPANCardImportNotificationHistoryWithCompletion:]_block_invoke.298
+ ___73-[PKPaymentService featureApplicationWithReferenceIdentifier:completion:]_block_invoke.336
+ ___73-[PKPaymentWebService URLSession:downloadTask:didFinishDownloadingToURL:]_block_invoke.861
+ ___73-[PKSecureElement peerPaymentEnrollmentDataWithAlternateDSID:completion:]_block_invoke.336
+ ___73-[PKSecureElement peerPaymentEnrollmentDataWithAlternateDSID:completion:]_block_invoke.339
+ ___73-[PKSecureElement peerPaymentEnrollmentDataWithAlternateDSID:completion:]_block_invoke_2.337
+ ___73-[PKSecureElement peerPaymentEnrollmentDataWithAlternateDSID:completion:]_block_invoke_3.338
+ ___74-[PKDiscoveryMedia downloadImageDataWithScale:shouldWriteData:completion:]_block_invoke
+ ___74-[PKMobileAssetManager _downloadAsset:isDiscretionary:timeout:completion:]_block_invoke.442
+ ___74-[PKPaymentService balancesForPaymentPassWithUniqueIdentifier:completion:]_block_invoke.188
+ ___74-[PKPaymentService messagesForPaymentPassWithUniqueIdentifier:completion:]_block_invoke.187
+ ___74-[PKPaymentService notifyForFPANCardImportWithCredentials:withCompletion:]_block_invoke.296
+ ___74-[PKPaymentService setAccountAttestationAnonymizationSalt:withCompletion:]_block_invoke.359
+ ___74-[PKPaymentService setCommutePlanReminder:forCommutePlan:pass:completion:]_block_invoke.196
+ ___74-[PKPaymentService valueAddedServiceTransactionWithIdentifier:completion:]_block_invoke.212
+ ___74-[PKPaymentWebService backgroundPerformDeviceCheckInForRegion:identifier:]_block_invoke.389
+ ___74-[PKSecureElement createAliroHydraKeyWithServerParameters:withCompletion:]_block_invoke.314
+ ___75-[PKPaymentService balanceReminderThresholdForBalance:pass:withCompletion:]_block_invoke.190
+ ___75-[PKPaymentService commutePlanReminderForCommputePlan:pass:withCompletion:]_block_invoke.194
+ ___75-[PKPaymentService prepareProvisioningTarget:checkFamilyCircle:completion:]_block_invoke.378
+ ___75-[PKPaymentService spendingCategoryTransactionGroupsForRequest:completion:]_block_invoke.151
+ ___75-[PKPaymentService submitEncryptedPIN:forTransactionIdentifier:completion:]_block_invoke.320
+ ___75-[PKPaymentService transactionTagsForTransactionWithIdentifier:completion:]_block_invoke.395
+ ___76-[PKPaymentWebServiceRemoteProxyTargetDevice initWithWebService:connection:]_block_invoke.637
+ ___77+[PKRemotePaymentInstrument(Caching) thumbnailCachePathForManifestHash:size:]_block_invoke
+ ___77-[PKPaymentService sendDeviceSharingCapabilitiesRequestForHandle:completion:]_block_invoke.398
+ ___77-[PKPaymentService updateFeatureApplicationsForAccountIdentifier:completion:]_block_invoke.332
+ ___77-[PKPaymentService updateMetadataOnPassWithIdentifier:credential:completion:]_block_invoke.363
+ ___78-[PKPaymentProvisioningController _requestProvisioning:withCompletionHandler:]_block_invoke.641
+ ___78-[PKPaymentProvisioningController _requestProvisioning:withCompletionHandler:]_block_invoke_2.642
+ ___78-[PKPaymentProvisioningController _startLocationSearchWithTimeout:completion:]_block_invoke.668
+ ___78-[PKPaymentService categoryVisualizationMagnitudesForPassUniqueID:completion:]_block_invoke.350
+ ___78-[PKPaymentService featureApplicationsForAccountUserInvitationWithCompletion:]_block_invoke.335
+ ___78-[PKPaymentService hasTransactionsForTransactionSourceIdentifiers:completion:]_block_invoke.140
+ ___78-[PKPaymentService requestNotificationAuthorizationIfNecessaryWithCompletion:]_block_invoke.262
+ ___79-[PKAccountService accountBalancesForAccountIdentifier:startDate:endDate:type:]_block_invoke.57
+ ___79-[PKPaymentProvisioningController _associateCredentials:withCompletionHandler:]_block_invoke.371
+ ___79-[PKPaymentService submitUserConfirmation:forTransactionIdentifier:completion:]_block_invoke.317
+ ___79-[PKPaymentWebService retrieveMerchantTokensUnifiedListWithRequest:completion:]_block_invoke.785
+ ___80-[PKMobileAssetManager performScheduledActivityWithIdentifier:activityCriteria:]_block_invoke.421
+ ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.397
+ ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.404
+ ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.413
+ ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.421
+ ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.425
+ ___80-[PKPaymentProvisioningController requestPurchasesForProduct:completionHandler:]_block_invoke.515
+ ___80-[PKPaymentProvisioningController requestPurchasesForProduct:completionHandler:]_block_invoke.518
+ ___80-[PKPaymentService passUniqueIdentifierForTransactionWithIdentifier:completion:]_block_invoke.176
+ ___80-[PKPaymentWebService _registerIfNeededWithResponse:task:isRedirect:completion:]_block_invoke.949
+ ___80-[PKPaymentWebService _registerIfNeededWithResponse:task:isRedirect:completion:]_block_invoke.951
+ ___81-[PKRemoteAssetManager addRemoteAssetData:shouldWriteData:forManifestItem:error:]_block_invoke.56
+ ___81-[PKSecureElement initializeSecureElementQueuingServerConnection:withCompletion:]_block_invoke.262
+ ___82-[PKPaymentService markAuthenticationCompleteForTransactionIdentifier:completion:]_block_invoke.316
+ ___83-[PKPaymentService installmentPlansWithTransactionReferennceIdentifier:completion:]_block_invoke.168
+ ___83-[PKPaymentService installmentTransactionsForInstallmentPlanIdentifier:completion:]_block_invoke.167
+ ___83-[PKPaymentService mapsMerchantWithIdentifier:resultProviderIdentifier:completion:]_block_invoke.282
+ ___83-[PKPaymentService saveProvisioningSupportData:forPassUniqueIdentifier:completion:]_block_invoke.373
+ ___83-[PKPaymentService transactionSourceTypeForTransactionSourceIdentifier:completion:]_block_invoke.163
+ ___83-[PKPaymentService transactionsRequiringReviewForAccountWithIdentifier:completion:]_block_invoke.349
+ ___83-[PKPaymentWebService _performRewrapRequest:serviceURL:responseHandler:completion:]_block_invoke.834
+ ___83-[PKSecureElement _executeSecureElementAsyncSessionHandlersWithSession:completion:]_block_invoke.250
+ ___84-[PKPaymentService passUniqueIdentifiersForTransactionSourceIdentifiers:completion:]_block_invoke.178
+ ___84-[PKPaymentService setDefaultPaymentApplication:forPassUniqueIdentifier:completion:]_block_invoke.214
+ ___84-[PKPaymentService(PaymentOffers) didInteractWithConfirmationRecordFollowupMessage:]_block_invoke.35
+ ___85-[PKPaymentProvisioningController _setupAccountCredentialForProvisioning:completion:]_block_invoke.538
+ ___85-[PKPaymentProvisioningController _setupAccountCredentialForProvisioning:completion:]_block_invoke.540
+ ___85-[PKPaymentProvisioningController _setupAccountCredentialForProvisioning:completion:]_block_invoke_2.542
+ ___85-[PKPaymentService setDefaultExpressTransitPassIdentifier:withCredential:completion:]_block_invoke.222
+ ___85-[PKPaymentService submitBarcodePaymentEvent:forPassUniqueIdentifier:withCompletion:]_block_invoke.323
+ ___85-[PKPaymentWebService _performApplePayTrustRegistrationWithURL:pushToken:completion:]_block_invoke.370
+ ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke.495
+ ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke.498
+ ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke_2.500
+ ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke_3.501
+ ___86-[PKPaymentService userNotificationActionPerformed:notificationIdentifier:completion:]_block_invoke.265
+ ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.437
+ ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.443
+ ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.450
+ ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.454
+ ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.459
+ ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.463
+ ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke_2.464
+ ___87-[PKPaymentService conflictingExpressPassIdentifiersForPassInformation:withCompletion:]_block_invoke.229
+ ___87-[PKPaymentService transactionsWithTransactionSource:withBackingData:limit:completion:]_block_invoke.159
+ ___87-[PKPaymentService transitStateWithPassUniqueIdentifier:paymentApplication:completion:]_block_invoke.245
+ ___87-[PKPaymentWebService _handleRetryAfterRegisterWithRequest:response:completionHandler:]_block_invoke.921
+ ___88-[PKPaymentAuthorizationStateMachine _performPrepareTransactionDetailsRequestWithParam:]_block_invoke.283
+ ___88-[PKPaymentAuthorizationStateMachine _performPrepareTransactionDetailsRequestWithParam:]_block_invoke_2.285
+ ___88-[PKPaymentService valueAddedServiceTransactionsForPaymentTransaction:limit:completion:]_block_invoke.211
+ ___89-[PKAutoFillCardManager activeFPANCardsWithOptions:allowedCardTypes:sortType:completion:]_block_invoke.40
+ ___89-[PKPaymentService conflictingExpressPassIdentifiersForPassConfiguration:withCompletion:]_block_invoke.228
+ ___89-[PKPaymentService processedAuthenticationMechanism:forTransactionIdentifier:completion:]_block_invoke.315
+ ___89-[PKPaymentService submitTransactionAnswerForTransaction:questionType:answer:completion:]_block_invoke.348
+ ___90-[PKPaymentService clearProvisioningSupportDataOfType:forPassUniqueIdentifier:completion:]_block_invoke.374
+ ___91-[PKPaymentProvisioningController verifyPassIsSupportedForExpressInLocalMarket:completion:]_block_invoke.648
+ ___91-[PKPaymentProvisioningController verifyPassIsSupportedForExpressInLocalMarket:completion:]_block_invoke.651
+ ___91-[PKPaymentProvisioningController verifyPassIsSupportedForExpressInLocalMarket:completion:]_block_invoke.653
+ ___91-[PKPaymentService retrievePINEncryptionCertificateForPassUniqueIdentifier:withCompletion:]_block_invoke.313
+ ___91-[PKPaymentService setDefaultExpressFelicaTransitPassIdentifier:withCredential:completion:]_block_invoke.220
+ ___92-[PKPaymentService transactionWithServiceIdentifier:transactionSourceIdentifier:completion:]_block_invoke.165
+ ___92-[PKProvisioningAnalyticsSessionPreflightReporter reportCredentialsPreflightComplete:token:]_block_invoke
+ ___92-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:]_block_invoke.293
+ ___92-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:]_block_invoke.294
+ ___92-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:]_block_invoke_2.295
+ ___93-[PKPaymentService cancelAutoTopUpForPassWithUniqueIdentifier:balanceIdentifiers:completion:]_block_invoke.193
+ ___93-[PKPaymentService fetchBarcodesForPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.308
+ ___93-[PKPaymentService transactionsRelatedToTransaction:transactionSourceIdentifiers:completion:]_block_invoke.205
+ ___93-[PKSecureElement generateTransactionKeyWithReaderIdentifier:readerPublicKey:withCompletion:]_block_invoke.311
+ ___94-[PKPaymentService sharingInvitationWasInvalidated:withCredentialIdentifier:error:completion:]_block_invoke.371
+ ___94-[PKPaymentService transactionsWithFullPaymentHashes:transactionSourceIdentifiers:completion:]_block_invoke.162
+ ___94-[PKPaymentService valueAddedServiceTransactionsForPassWithUniqueIdentifier:limit:completion:]_block_invoke.210
+ ___95-[PKPaymentService insertOrUpdatePaymentTransaction:forTransactionSourceIdentifier:completion:]_block_invoke.143
+ ___95-[PKPaymentService(PaymentOffers) paymentOfferCriteriaForPassUniqueID:criteriaType:completion:]_block_invoke
+ ___95-[PKPaymentService(PaymentOffers) paymentOfferCriteriaForPassUniqueID:criteriaType:completion:]_block_invoke.33
+ ___96-[PKPaymentService ambiguousPassUniqueIdentifierForTransactionWithServiceIdentifier:completion:]_block_invoke.179
+ ___96-[PKPaymentService invalidateAuxiliaryCapabilityCertificatesForPassUniqueIdentifier:completion:]_block_invoke.307
+ ___96-[PKPaymentService merchantForPassUniqueIdentifier:withAuxiliaryPassInformationItem:completion:]_block_invoke.290
+ ___96-[PKPaymentService provideEncryptedPushProvisioningTarget:sharingInstanceIdentifier:completion:]_block_invoke.377
+ ___96-[PKPaymentService submitEncryptedPIN:forTransactionIdentifier:sessionExchangeToken:completion:]_block_invoke.321
+ ___96-[PKPaymentService transactionReceiptForTransactionWithIdentifier:updateIfNecessary:completion:]_block_invoke.392
+ ___96-[PKPaymentWebService _backgroundDownloadCloudStoreAssetsForItem:cloudStoreCoordinatorDelegate:]_block_invoke.898
+ ___96-[PKPaymentWebService _backgroundDownloadCloudStoreAssetsForItem:cloudStoreCoordinatorDelegate:]_block_invoke.900
+ ___96-[PKPaymentWebService _backgroundDownloadCloudStoreAssetsForItem:cloudStoreCoordinatorDelegate:]_block_invoke_2.899
+ ___96-[PKPaymentWebService _backgroundDownloadCloudStoreAssetsForItem:cloudStoreCoordinatorDelegate:]_block_invoke_2.903
+ ___96-[PKPaymentWebService registerDeviceAtBrokerURL:withConsistencyCheckResults:retries:completion:]_block_invoke.347
+ ___96-[PKPaymentWebService registerDeviceAtBrokerURL:withConsistencyCheckResults:retries:completion:]_block_invoke.354
+ ___97-[PKPaymentService augmentedProductForInstallmentConfiguration:experimentDetails:withCompletion:]_block_invoke.338
+ ___97-[PKPaymentWebServiceLocalProxyTargetDevice canSaveFPANCardWithDescriptor:credential:completion:]_block_invoke
+ ___97-[PKPaymentWebServiceLocalProxyTargetDevice canSaveFPANCardWithDescriptor:credential:completion:]_block_invoke_2
+ ___97-[PKPaymentWebServiceLocalProxyTargetDevice canSaveFPANCardWithDescriptor:credential:completion:]_block_invoke_3
+ ___98-[PKDashboardTransactionFetcher _addCashbackTransactions:synchronous:currentMonthOnly:completion:]_block_invoke.77
+ ___98-[PKPaymentService updatePreferredCategory:forTransactionsWithIdentifiers:paymentPass:completion:]_block_invoke.206
+ ___98-[PKPaymentWebServiceRemoteProxyTargetDevice canSaveFPANCardWithDescriptor:credential:completion:]_block_invoke
+ ___99+[PKSecureElement accessSecureElementManagerSessionWithSessionExchangeToken:callbackQueue:handler:]_block_invoke.242
+ ___99+[PKSecureElement accessSecureElementManagerSessionWithSessionExchangeToken:callbackQueue:handler:]_block_invoke.243
+ ___99-[PKPaymentService userNotificationActionPerformed:applicationMessageContentIdentifier:completion:]_block_invoke.264
+ ___99-[PKPaymentService(PaymentOffers) updatePaymentRewardsBalancesWithPassUniqueIdentifier:completion:]_block_invoke.38
+ ___Block_byref_object_copy_.537
+ ___Block_byref_object_dispose_.538
+ ___PDScheduledActivityRemoveAll_block_invoke
+ ___PKCacheFile_block_invoke
+ ___PKCacheFile_block_invoke.219
+ ___PKCachedFileForSHA1Exists_block_invoke
+ ___PKCachedFileForSHA1_block_invoke
+ ___PKExpirationDateFormatter_block_invoke
+ ___PKPeerPaymentRemoveRecurringPaymentRecentMemoIcon_block_invoke.1104
+ ___PKRequestContactAccessWithCompletion_block_invoke.317
+ ___PKRequiredPaymentSetupFileURLs_block_invoke
+ ___PKSharedCacheCreateDirectory_block_invoke
+ ___PKSharedCacheCreateFileURL_block_invoke
+ ___PKSharedCacheRemoveObjectForKey_block_invoke_2
+ ___PKSharedCacheSetObjectForKey_block_invoke_2
+ ____CanReadFromSharedCache_block_invoke
+ ____CanWriteToSharedCacheDirectory_block_invoke
+ ____SharedCacheDictionary_block_invoke_2
+ ___block_descriptor_32_e30_v28?0B8"NSError"12"NSURL"20l
+ ___block_descriptor_32_e36_B16?0"PKAccountFeatureDescriptor"8l
+ ___block_descriptor_32_e39_"NSString"16?0"PKPaymentCredential"8l
+ ___block_descriptor_40_e8_32s_e15_v16?0"NSURL"8ls32l8
+ ___block_descriptor_40_e8_32w_e15_v16?0"NSURL"8lw32l8
+ ___block_descriptor_48_e8_32s40bs_e32_v16?0"PKPaymentOfferCriteria"8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e33_v16?0"PKFPANCardCanSaveResult"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48w_e17_v16?0"NSArray"8lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56s_e38_v28?0B8"NSNull"12"<PKCancelable>"20ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e30_v28?0B8"NSError"12"NSURL"20ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64bs72r80r_e61_v32?0"PKAsyncOperationState"8"NSNull"16?<v?"NSNull"B>24ls32l8s64l8s40l8r72l8s48l8s56l8r80l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72r80r_e32_v28?0B8"NSArray"12"NSError"20ls32l8s40l8r72l8r80l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72r80r_e32_v28?0B8"NSError"12"NSArray"20ls32l8r72l8s40l8r80l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72r80r_e5_v8?0ls32l8r72l8r80l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.1012
+ ___block_literal_global.1014
+ ___block_literal_global.1019
+ ___block_literal_global.1027
+ ___block_literal_global.1030
+ ___block_literal_global.1058
+ ___block_literal_global.1063
+ ___block_literal_global.1065
+ ___block_literal_global.1070
+ ___block_literal_global.1075
+ ___block_literal_global.1080
+ ___block_literal_global.1085
+ ___block_literal_global.1090
+ ___block_literal_global.1095
+ ___block_literal_global.1100
+ ___block_literal_global.1103
+ ___block_literal_global.1105
+ ___block_literal_global.1107
+ ___block_literal_global.1115
+ ___block_literal_global.1117
+ ___block_literal_global.1126
+ ___block_literal_global.1127
+ ___block_literal_global.1134
+ ___block_literal_global.1140
+ ___block_literal_global.1143
+ ___block_literal_global.1151
+ ___block_literal_global.116
+ ___block_literal_global.1235
+ ___block_literal_global.1239
+ ___block_literal_global.1242
+ ___block_literal_global.1254
+ ___block_literal_global.1268
+ ___block_literal_global.1308
+ ___block_literal_global.1324
+ ___block_literal_global.1328
+ ___block_literal_global.1425
+ ___block_literal_global.1427
+ ___block_literal_global.1430
+ ___block_literal_global.1666
+ ___block_literal_global.1668
+ ___block_literal_global.1673
+ ___block_literal_global.1677
+ ___block_literal_global.1691
+ ___block_literal_global.1693
+ ___block_literal_global.1698
+ ___block_literal_global.1712
+ ___block_literal_global.1718
+ ___block_literal_global.1721
+ ___block_literal_global.1723
+ ___block_literal_global.1725
+ ___block_literal_global.1727
+ ___block_literal_global.1729
+ ___block_literal_global.1732
+ ___block_literal_global.184
+ ___block_literal_global.186
+ ___block_literal_global.198
+ ___block_literal_global.200
+ ___block_literal_global.202
+ ___block_literal_global.204
+ ___block_literal_global.206
+ ___block_literal_global.208
+ ___block_literal_global.214
+ ___block_literal_global.216
+ ___block_literal_global.218
+ ___block_literal_global.219
+ ___block_literal_global.228
+ ___block_literal_global.244
+ ___block_literal_global.251
+ ___block_literal_global.255
+ ___block_literal_global.257
+ ___block_literal_global.261
+ ___block_literal_global.267
+ ___block_literal_global.269
+ ___block_literal_global.276
+ ___block_literal_global.285
+ ___block_literal_global.303
+ ___block_literal_global.304
+ ___block_literal_global.307
+ ___block_literal_global.316
+ ___block_literal_global.332
+ ___block_literal_global.333
+ ___block_literal_global.348
+ ___block_literal_global.358
+ ___block_literal_global.366
+ ___block_literal_global.376
+ ___block_literal_global.382
+ ___block_literal_global.383
+ ___block_literal_global.393
+ ___block_literal_global.423
+ ___block_literal_global.424
+ ___block_literal_global.425
+ ___block_literal_global.427
+ ___block_literal_global.444
+ ___block_literal_global.446
+ ___block_literal_global.448
+ ___block_literal_global.480
+ ___block_literal_global.504
+ ___block_literal_global.524
+ ___block_literal_global.530
+ ___block_literal_global.532
+ ___block_literal_global.546
+ ___block_literal_global.654
+ ___block_literal_global.700
+ ___block_literal_global.724
+ ___block_literal_global.726
+ ___block_literal_global.730
+ ___block_literal_global.734
+ ___block_literal_global.737
+ ___block_literal_global.767
+ ___block_literal_global.769
+ ___block_literal_global.788
+ ___block_literal_global.860
+ ___block_literal_global.879
+ ___block_literal_global.882
+ ___block_literal_global.902
+ ___block_literal_global.905
+ ___block_literal_global.909
+ ___block_literal_global.911
+ ___block_literal_global.927
+ ___block_literal_global.947
+ ___block_literal_global.949
+ ___block_literal_global.951
+ ___block_literal_global.953
+ ___block_literal_global.955
+ ___block_literal_global.957
+ ___block_literal_global.982
+ ___block_literal_global.984
+ ___block_literal_global.999
+ _block_copy_helper.115
+ _block_copy_helper.119
+ _block_copy_helper.126
+ _block_copy_helper.132
+ _block_copy_helper.139
+ _block_copy_helper.146
+ _block_copy_helper.149
+ _block_copy_helper.163
+ _block_copy_helper.171
+ _block_copy_helper.178
+ _block_copy_helper.199
+ _block_copy_helper.243
+ _block_copy_helper.268
+ _block_copy_helper.279
+ _block_copy_helper.296
+ _block_copy_helper.42
+ _block_copy_helper.48
+ _block_copy_helper.77
+ _block_descriptor.117
+ _block_descriptor.121
+ _block_descriptor.128
+ _block_descriptor.134
+ _block_descriptor.141
+ _block_descriptor.148
+ _block_descriptor.151
+ _block_descriptor.165
+ _block_descriptor.173
+ _block_descriptor.180
+ _block_descriptor.201
+ _block_descriptor.245
+ _block_descriptor.270
+ _block_descriptor.281
+ _block_descriptor.298
+ _block_descriptor.44
+ _block_descriptor.50
+ _block_descriptor.79
+ _block_destroy_helper.116
+ _block_destroy_helper.120
+ _block_destroy_helper.127
+ _block_destroy_helper.133
+ _block_destroy_helper.140
+ _block_destroy_helper.147
+ _block_destroy_helper.150
+ _block_destroy_helper.164
+ _block_destroy_helper.172
+ _block_destroy_helper.179
+ _block_destroy_helper.200
+ _block_destroy_helper.244
+ _block_destroy_helper.269
+ _block_destroy_helper.280
+ _block_destroy_helper.297
+ _block_destroy_helper.43
+ _block_destroy_helper.49
+ _block_destroy_helper.78
+ _objc_msgSend$_initDashboardInstance
+ _objc_msgSend$_initWithPaymentService:paymentWebService:configuration:
+ _objc_msgSend$_remoteAssetForScale:
+ _objc_msgSend$_reportPreflightStepCompleteForContext:token:
+ _objc_msgSend$_reportProvisioningStep:finishedWithStatus:error:context:
+ _objc_msgSend$_sendPendingEvents
+ _objc_msgSend$_setExpirationDate:
+ _objc_msgSend$_startReportingIfNecessary
+ _objc_msgSend$_updatePaymentSetupProduct:displayName:localizedDescription:longLocalizedDescription:partnerArray:productIdentifier:paymentOptions:termsURL:provisioningMethodDetailsList:readerModeMetadata:requiredFields:imageAssets:minimumOSVersion:region:regionData:hsa2Requirement:suppressPendingPurchases:supportedTransitNetworkIdentifiers:onboardingItems:actionBaseURL:productState:minimumProductAge:maximumProductAge:minimumTargetUserSupportedAge:associatedStoreIdentifiers:appLaunchURL:regionIdentifier:type:localizedNotificationTitle:localizedNotificationMessage:discoveryCardIdentifier:clientInfo:searchTerms:featureIdentifier:criteriaIdentifier:showOtherProviders:
+ _objc_msgSend$activeAutoFillCardCount
+ _objc_msgSend$affiliateReporter:
+ _objc_msgSend$analyticsReporter
+ _objc_msgSend$analyticsValueForResult:
+ _objc_msgSend$canArchiveWithTransaction:
+ _objc_msgSend$categoryAndSource
+ _objc_msgSend$classifyErrorText:
+ _objc_msgSend$containsAnyTerm:inText:
+ _objc_msgSend$createUnaffiliatedReporter
+ _objc_msgSend$defaultDataProvider
+ _objc_msgSend$finishPreflightForToken:
+ _objc_msgSend$initWithAccountState:accountType:supportedFeatures:
+ _objc_msgSend$initWithCardholderName:pan:expirationDate:securityCode:billingAddress:
+ _objc_msgSend$initWithPaymentHash:transactionDate:merchantName:merchantRawName:industryCategory:industryCode:merchantType:merchantCountryCode:terminalIdentifier:merchantAdditionalData:paymentNetwork:isMerchantTokenTransaction:isCoarseLocation:location:merchantIdentifier:merchantRawCANL:merchantRawCity:merchantRawState:merchantRawCountry:merchantCity:merchantZip:merchantState:merchantCleanConfidenceLevel:rewardsAmount:rewardsCurrency:rewardsEligibilityReason:adamIdentifier:webURL:webMerchantIdentifier:webMerchantName:isIssuerInstallmentTransaction:issuerInstallmentManagementURL:
+ _objc_msgSend$isOwnerAccountPersonalized
+ _objc_msgSend$localizationKeyPostfixForInitiation
+ _objc_msgSend$paymentOfferCriteriaForPassUniqueID:criteriaType:completion:
+ _objc_msgSend$paymentService
+ _objc_msgSend$reportAppExtensionPreflightComplete:token:
+ _objc_msgSend$reportCredentialsPreflightComplete:token:
+ _objc_msgSend$reportPreflightEventForReporter:context:
+ _objc_msgSend$reportPreflightStepComplete:itemCount:token:
+ _objc_msgSend$reportProvisioningStepForReporter:step:success:error:context:
+ _objc_msgSend$reportProvisioningStepStartForReporter:step:context:
+ _objc_msgSend$scheduleApplePayDemoActivitySignal
+ _objc_msgSend$setCardIsInWallet:
+ _objc_msgSend$setLocalizedConfirmationTitle:
+ _objc_msgSend$setResponder:
+ _objc_msgSend$start
+ _objc_msgSend$startPreflight
+ _objc_msgSend$stepProperties
+ _objc_msgSend$topUpType
+ _objc_msgSend$updateReasonIsInitialDownload
+ _objc_msgSend$updateSessionDetails:
+ _objectdestroy.107Tm
+ _objectdestroy.113Tm
+ _objectdestroy.206Tm
+ _objectdestroy.36Tm
+ _objectdestroy.6Tm
+ _objectdestroy.94Tm
+ _symbolic So34PKContinuityProximityAdvertisementCSo47PKProvisioningContinuityDiscoveryRequestMessageCIeggo_
+ _symbolic So34PKFPANCardDescriptorCredentialPairC
+ _symbolic So47PKProvisioningContinuityDiscoveryRequestMessageCSgIegg_
+ _symbolic _____ 10Foundation8TimeZoneV
+ _symbolic _____ So33PKContinuityProximityVerifierTypeV
- +[PKAnalyticsReporter(PKDashboard) updateIdentityEventToReportDashboardAnalytics:forPass:]
- +[PKCreditAccountController shouldShowCardNumbersWithAccount:andPass:]
- +[PKVirtualCard queryKeychainForCountOfVirtualCards:]
- -[PKAccountService countOfVirtualCardsInKeychain]
- -[PKAutoFillCardCredential _setExpiration:]
- -[PKDiscoveryCard backgroundColor]
- -[PKDiscoveryMedia _remoteAssetForScale:isExpandedView:]
- -[PKDiscoveryMedia downloadImageDataWithScale:shouldWriteData:isExpandedView:completion:]
- -[PKDiscoveryMedia imageDataFromCacheWithScale:isExpandedView:]
- -[PKDiscoveryMedia localAssetURL]
- -[PKMutableAutofillCardCredential setExpiration:]
- -[PKPassLibrary supportsSearchForPassUniqueID:]
- -[PKPassShareActivationOptions localizationKeyPostfix]
- -[PKPaymentMessage archiveOnNextTransaction]
- -[PKPaymentRequest localizedBiometricConfirmationTitle]
- -[PKPaymentRequest setLocalizedBiometricConfirmationTitle:]
- -[PKPaymentService(FPAN) activeAutoFillFPANCardCount]
- -[PKPaymentSetupProductModel _updatePaymentSetupProduct:displayName:localizedDescription:longLocalizedDescription:partnerArray:productIdentifier:paymentOptions:termsURL:provisioningMethodDetailsList:readerModeMetadata:requiredFields:imageAssets:minimumOSVersion:region:regionData:hsa2Requirement:suppressPendingPurchases:supportedTransitNetworkIdentifiers:onboardingItems:actionBaseURL:productState:minimumProductAge:maximumProductAge:minimumTargetUserSupportedAge:associatedStoreIdentifiers:appLaunchURL:regionIdentifier:type:localizedNotificationTitle:localizedNotificationMessage:discoveryCardIdentifier:clientInfo:searchTerms:featureIdentifier:criteriaIdentifier:]
- -[PKPeerPaymentAccount isOwnerAccountActivePersonalized]
- -[PKProvisioningAnalyticsSession reportProvisioningStepForReporter:step:success:error:]
- GCC_except_table102
- GCC_except_table107
- GCC_except_table112
- GCC_except_table124
- GCC_except_table129
- GCC_except_table136
- GCC_except_table166
- GCC_except_table167
- GCC_except_table175
- GCC_except_table178
- GCC_except_table184
- GCC_except_table208
- GCC_except_table213
- GCC_except_table217
- GCC_except_table233
- GCC_except_table237
- GCC_except_table238
- GCC_except_table244
- GCC_except_table251
- GCC_except_table254
- GCC_except_table260
- GCC_except_table265
- GCC_except_table269
- GCC_except_table279
- GCC_except_table282
- GCC_except_table301
- GCC_except_table312
- GCC_except_table317
- GCC_except_table325
- GCC_except_table327
- GCC_except_table332
- GCC_except_table336
- GCC_except_table348
- GCC_except_table356
- GCC_except_table362
- GCC_except_table371
- GCC_except_table379
- GCC_except_table386
- GCC_except_table391
- GCC_except_table402
- GCC_except_table405
- GCC_except_table407
- GCC_except_table409
- GCC_except_table411
- GCC_except_table422
- GCC_except_table438
- GCC_except_table447
- GCC_except_table454
- GCC_except_table457
- GCC_except_table465
- GCC_except_table467
- GCC_except_table521
- GCC_except_table545
- GCC_except_table548
- GCC_except_table551
- GCC_except_table569
- GCC_except_table574
- GCC_except_table58
- GCC_except_table62
- GCC_except_table656
- GCC_except_table699
- GCC_except_table707
- GCC_except_table727
- GCC_except_table845
- GCC_except_table92
- GCC_except_table94
- GCC_except_table98
- _.str.102
- _.str.237
- _.str.241
- _.str.243
- _.str.252
- _.str.253
- _.str.260
- _.str.261
- _.str.262
- _.str.274
- _.str.275
- _.str.276
- _.str.282
- _.str.290
- _.str.291
- _.str.302
- _.str.304
- _.str.869
- _.str.90
- _.str.91
- _OBJC_IVAR_$_PKAutoFillCardCredential._expiration
- _OBJC_IVAR_$_PKDiscoveryCard._backgroundColor
- _OBJC_IVAR_$_PKDiscoveryCard._backgroundMedia
- _OBJC_IVAR_$_PKDiscoveryMedia._localAssetURL
- _OBJC_IVAR_$_PKPaymentRequest._localizedBiometricConfirmationTitle
- _OBJC_IVAR_$_PKProvisioningAnalyticsSessionSubjectHandle._didBeginWalletProvisioningSubject
- _PKEnableSeamlessMigration
- _PKEnableSeamlessMigrationKey
- _PKMapsSnapshotsCacheURL
- _PKPassAssetDownloadCachePath
- _PKPaymentRequestLocalizedBiometricConfirmationTitleKey
- _PKPeerPaymentGroupRequestTrackingEnabled
- _PKPeerPaymentGroupRequestTrackingEnabledKey
- _PKPeerPaymentRecipientCacheArchivePath
- _PKPeerPaymentRecipientCacheDirectoryPath
- _PKPreauthorizedPaymentNotificationsDisabledKey
- _PKPreauthorizedPaymentsNotificationsDisabled
- _PKRemoteInstrumentThumbnailsCachePath
- _PKSetPreauthorizedPaymentsNotificationsDisabled
- _PKSharedCacheDismissedAppleBalanceReadyKey
- __CanWriteToSharedCacheDirectory
- __CanWriteToSharedCacheDirectory.__writeAccess
- __MergedGlobals.25
- __MergedGlobals.33
- __OBJC_$_PROP_LIST_PKSpringAnimationFactory.67
- __SharedCacheFilePath
- ___100-[PKPaymentService submitUserConfirmation:forTransactionIdentifier:sessionExchangeToken:completion:]_block_invoke.318
- ___101-[PKPaymentService transactionCountByPeriodForRequest:calendar:unit:includePurchaseTotal:completion:]_block_invoke.149
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke.528
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke.534
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_2.529
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_2.535
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_3.530
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_3.536
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_4.531
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_5.532
- ___102-[PKPaymentProvisioningController setupProductForProvisioning:includePurchases:withCompletionHandler:]_block_invoke_6.533
- ___102-[PKPaymentService recordPaymentApplicationUsageForPassUniqueIdentifier:paymentApplicationIdentifier:]_block_invoke.241
- ___103-[PKPaymentService submitTransactionSignatureForTransactionIdentifier:sessionExchangeToken:completion:]_block_invoke.321
- ___104-[PKMobileAssetManager dynamicAssetWithIdentifier:mappedIdentifierPrefix:parameters:timeout:completion:]_block_invoke.393
- ___104-[PKMobileAssetManager dynamicAssetWithIdentifier:mappedIdentifierPrefix:parameters:timeout:completion:]_block_invoke.394
- ___104-[PKSecureElement createAliroHomeKeyWithReaderIdentifier:readerPublicKey:homeIdentifier:withCompletion:]_block_invoke.315
- ___106-[PKPaymentService submitBarcodePaymentEvent:forPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.323
- ___107-[PKPaymentService insertOrUpdatePaymentTransaction:forPassUniqueIdentifier:paymentApplication:completion:]_block_invoke.140
- ___107-[PKPaymentService registerAuxiliaryCapabilityForPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.305
- ___107-[PKPaymentService retrieveDecryptedBarcodeCredentialForPassUniqueIdentifier:authorization:withCompletion:]_block_invoke.309
- ___108-[PKPaymentService(PaymentOffers) updatePaymentRewardsRedemptionsWithPassUniqueIdentifier:limit:completion:]_block_invoke.37
- ___109-[PKPaymentService conflictingExpressPassIdentifiersForPassInformation:withReferenceExpressState:completion:]_block_invoke.230
- ___109-[PKPaymentService peerPaymentCounterpartHandlesForTransactionSourceIdentifier:startDate:endDate:completion:]_block_invoke.137
- ___109-[PKPaymentService(PaymentOffers) paymentRewardsRedemptionsForPassUniqueIdentifier:paymentHashes:completion:]_block_invoke.35
- ___109-[PKPaymentWebService _performVerificationRequest:selectedMethodGroup:selectedMethod:pass:taskID:completion:]_block_invoke.460
- ___111-[PKPaymentProvisioningController resolveLocalEligibilityRequirementsForAppleBalanceCredential:withCompletion:]_block_invoke.567
- ___111-[PKPaymentProvisioningController resolveLocalEligibilityRequirementsForAppleBalanceCredential:withCompletion:]_block_invoke.575
- ___111-[PKPaymentService conflictingExpressPassIdentifiersForPassConfiguration:withReferenceExpressState:completion:]_block_invoke.229
- ___112-[PKPaymentService _submitVerificationCode:verificationData:forDPANIdentifier:usingSynchronousProxy:completion:]_block_invoke.134
- ___112-[PKPaymentService retrievePINEncryptionCertificateForPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.313
- ___115-[PKPaymentService passUniqueIdentifierForTransactionWithServiceIdentifier:transactionSourceIdentifier:completion:]_block_invoke.176
- ___115-[PKPaymentWebService backgroundDownloadRemotePassAssets:forSuffixesAndScreenScales:cloudStoreCoordinatorDelegate:]_block_invoke.714
- ___115-[PKPaymentWebService backgroundDownloadRemotePassAssets:forSuffixesAndScreenScales:cloudStoreCoordinatorDelegate:]_block_invoke.719
- ___115-[PKPaymentWebService backgroundDownloadRemotePassAssets:forSuffixesAndScreenScales:cloudStoreCoordinatorDelegate:]_block_invoke.721
- ___115-[PKPaymentWebService backgroundDownloadRemotePassAssets:forSuffixesAndScreenScales:cloudStoreCoordinatorDelegate:]_block_invoke_2.722
- ___117-[PKPaymentService insertOrUpdateValueAddedServiceTransaction:forPassUniqueIdentifier:paymentTransaction:completion:]_block_invoke.208
- ___119-[PKPaymentService transactionsForTransactionSourceIdentifiers:withTransactionSource:withBackingData:limit:completion:]_block_invoke.147
- ___127-[PKPaymentService removeMapsDataForTransactionWithIdentifier:forTransactionSourceIdentifier:issueReportIdentifier:completion:]_block_invoke.143
- ___128-[PKPaymentService cashbackByPeriodForTransactionSourceIdentifiers:withStartDate:endDate:calendar:calendarUnit:type:completion:]_block_invoke.151
- ___128-[PKPaymentService retrieveDecryptedBarcodeCredentialForPassUniqueIdentifier:authorization:sessionExchangeToken:withCompletion:]_block_invoke.311
- ___130-[PKPaymentWebService _passActionGroupIncludingAppletDataWithRemoteContentPassActionGroup:forPass:forDeviceIdentifier:completion:]_block_invoke.755
- ___132-[PKDashboardTransactionFetcher _processPaymentPassTransactionsWithTransactions:synchronous:currentMonthOnly:sendTransactionsBlock:]_block_invoke.85
- ___132-[PKDashboardTransactionFetcher _processPaymentPassTransactionsWithTransactions:synchronous:currentMonthOnly:sendTransactionsBlock:]_block_invoke_2.87
- ___136-[PKPaymentService transactionsForTransactionSourceIdentifiers:matchingMerchant:withTransactionSource:withBackingData:limit:completion:]_block_invoke.153
- ___137-[PKPaymentService transactionsForTransactionSourceIdentifiers:withTransactionSource:withBackingData:startDate:endDate:limit:completion:]_block_invoke.144
- ___140-[PKPaymentService rangingSuspensionReasonForAppletSubcredentialIdentifier:paymentApplicationIdentifier:secureElementIdentifier:completion:]_block_invoke.284
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.428
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.430
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.432
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke_2.429
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke_2.431
- ___144-[PKPaymentService pendingTransactionsForTransactionSourceIdentifiers:withTransactionSource:withBackingData:startDate:endDate:limit:completion:]_block_invoke.157
- ___145-[PKPaymentService approvedTransactionsForTransactionSourceIdentifiers:withTransactionSource:withBackingData:startDate:endDate:limit:completion:]_block_invoke.156
- ___149-[PKPaymentService processTransitTransactionEventWithHistory:transactionDate:forPaymentApplication:withPassUniqueIdentifier:expressTransactionState:]_block_invoke.240
- ___151-[PKPaymentService transactionsForTransactionSourceIdentifiers:withTransactionSource:withBackingData:startDate:endDate:orderedByDate:limit:completion:]_block_invoke.146
- ___153-[PKPaymentService transactionsForTransactionSourceIdentifiers:withPeerPaymentCounterpartHandles:withTransactionSource:withBackingData:limit:completion:]_block_invoke.152
- ___154-[PKPaymentService installmentPlanTransactionsForTransactionSourceIdentifiers:accountIdentifier:redeemed:withRedemptionType:startDate:endDate:completion:]_block_invoke.168
- ___157-[PKPaymentService transactionsForTransactionSourceIdentifiers:withTransactionType:withTransactionSource:withBackingData:startDate:endDate:limit:completion:]_block_invoke.155
- ___157-[PKPaymentService(PaymentOffers) paymentOffersMerchandisingForSessionDetails:merchandisingIdentifiers:needsProvisioningMerchandisingIdentifiers:completion:]_block_invoke.40
- ___158-[PKPaymentService transactionsForTransactionSourceIdentifiers:withMerchantCategory:withTransactionSource:withBackingData:startDate:endDate:limit:completion:]_block_invoke.154
- ___36-[PKPaymentService consistencyCheck]_block_invoke.258
- ___38+[PKSecureElement sharedSecureElement]_block_invoke
- ___42-[PKAutoFillCardCredential expirationDate]_block_invoke
- ___43-[PKPaymentService productsWithCompletion:]_block_invoke.353
- ___44-[PKPaymentService initializeSecureElement:]_block_invoke.218
- ___45-[PKFPANCredential initWithSafariDictionary:]_block_invoke
- ___45-[PKPaymentService insertUserLegalAgreement:]_block_invoke.396
- ___47-[PKPassLibrary supportsSearchForPassUniqueID:]_block_invoke
- ___48-[PKPaymentService mapsMerchantsWithCompletion:]_block_invoke.179
- ___48-[PKSecureElement SEPPairingInfoWithCompletion:]_block_invoke.268
- ___49-[PKAccountService countOfVirtualCardsInKeychain]_block_invoke
- ___49-[PKAccountService countOfVirtualCardsInKeychain]_block_invoke.48
- ___49-[PKPaymentService currentSecureElementSnapshot:]_block_invoke.384
- ___49-[PKPaymentService deleteReservation:completion:]_block_invoke.388
- ___50-[PKPaymentService sharedPaymentWebServiceContext]_block_invoke.277
- ___50-[PKPaymentService submitApplyRequest:completion:]_block_invoke.341
- ___50-[PKPaymentService submitTermsRequest:completion:]_block_invoke.345
- ___51-[PKPaymentService logoImageDataForURL:completion:]_block_invoke.172
- ___51-[PKPaymentService productsWithRequest:completion:]_block_invoke.351
- ___51-[PKPaymentService submitDeleteRequest:completion:]_block_invoke.346
- ___51-[PKSecureElement appletWithIdentifier:completion:]_block_invoke.281
- ___52-[PKSecureElement signatureForAuthToken:completion:]_block_invoke.309
- ___52-[PKSecureElement signedPlatformDataWithCompletion:]_block_invoke.312
- ___53-[PKPaymentService submitDocumentRequest:completion:]_block_invoke.343
- ___53-[PKPaymentService(FPAN) activeAutoFillFPANCardCount]_block_invoke
- ___53-[PKWebService URLSession:task:didCompleteWithError:]_block_invoke.331
- ___53-[PKWebService URLSession:task:didCompleteWithError:]_block_invoke.337
- ___53-[PKWebService URLSession:task:didCompleteWithError:]_block_invoke.338
- ___54-[PKPassShareActivationOptions localizationKeyPostfix]_block_invoke
- ___54-[PKPassShareActivationOptions localizationKeyPostfix]_block_invoke_2
- ___54-[PKPaymentService featureApplicationsWithCompletion:]_block_invoke.339
- ___54-[PKPaymentService regionsWithIdentifiers:completion:]_block_invoke.287
- ___54-[PKPaymentService transactionsForRequest:completion:]_block_invoke.169
- ___55-[PKPaymentService performDeviceCheckInWithCompletion:]_block_invoke.350
- ___55-[PKPaymentService pushProvisioningSharingIdentifiers:]_block_invoke.371
- ___55-[PKSecureElement appletCredentialsForAIDs:completion:]_block_invoke.275
- ___56-[PKDiscoveryMedia _remoteAssetForScale:isExpandedView:]_block_invoke
- ___56-[PKPaymentService credentialWithIdentifier:completion:]_block_invoke.367
- ___57-[PKPaymentService regionsMatchingName:types:completion:]_block_invoke.288
- ___57-[PKPaymentService submitVerificationRequest:completion:]_block_invoke.344
- ___58-[PKPaymentService familyMembersIgnoringCache:completion:]_block_invoke.324
- ___58-[PKSecureElement allAppletsAndCredentialsWithCompletion:]_block_invoke.271
- ___59-[PKPaymentService memberTypeForCurrentUserWithCompletion:]_block_invoke.325
- ___59-[PKPaymentService performProductActionRequest:completion:]_block_invoke.354
- ___59-[PKPaymentService requiresUpgradedPasscodeWithCompletion:]_block_invoke.303
- ___59-[PKPaymentService storeTransactionReceiptData:completion:]_block_invoke.392
- ___59-[PKPaymentService subcredentialInvitationsWithCompletion:]_block_invoke.361
- ___60-[PKPaymentProvisioningController _noteProvisioningDidBegin]_block_invoke.608
- ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke.861
- ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke.867
- ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke_2.864
- ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke_2.868
- ___61-[PKPaymentService changePasscodeFrom:toPasscode:completion:]_block_invoke.304
- ___61-[PKPaymentService statusForShareableCredentials:completion:]_block_invoke.374
- ___61-[PKPaymentWebService configurePaymentServiceWithCompletion:]_block_invoke.331
- ___61-[PKPaymentWebService configurePaymentServiceWithCompletion:]_block_invoke.336
- ___61-[PKPaymentWebService provisionPassesWithRequest:completion:]_block_invoke.433
- ___62-[PKPaymentOffersController _performCancelRequest:completion:]_block_invoke.190
- ___62-[PKPaymentOffersController _performCancelRequest:completion:]_block_invoke_2.191
- ___62-[PKPaymentOffersController _performSelectRequest:completion:]_block_invoke.186
- ___62-[PKPaymentOffersController _performSelectRequest:completion:]_block_invoke_2.187
- ___62-[PKPaymentService addRemoteDevicePendingProvisioningReceipt:]_block_invoke.292
- ___62-[PKPaymentService generateUnderlyingKeyReportWithCompletion:]_block_invoke.298
- ___62-[PKPaymentService transactionReceiptWithUniqueID:completion:]_block_invoke.389
- ___62-[PKPaymentService transactionsForPredicate:limit:completion:]_block_invoke.174
- ___63-[PKPaymentOffersController _performCatalogRequest:completion:]_block_invoke.142
- ___63-[PKPaymentOffersController _performCatalogRequest:completion:]_block_invoke.146
- ___63-[PKPaymentOffersController _performCatalogRequest:completion:]_block_invoke_2.147
- ___63-[PKPaymentOffersController _performConfirmRequest:completion:]_block_invoke.175
- ___63-[PKPaymentOffersController _performConfirmRequest:completion:]_block_invoke_2.176
- ___63-[PKPaymentOffersController _performConfirmRequest:completion:]_block_invoke_3.177
- ___63-[PKPaymentOffersController _performConfirmRequest:completion:]_block_invoke_3.181
- ___63-[PKPaymentService currentPasscodeMeetsUpgradedPasscodePolicy:]_block_invoke.302
- ___63-[PKPaymentService photosForFamilyMembersWithDSIDs:completion:]_block_invoke.328
- ___63-[PKPaymentService refreshMerchantTokenMetadataWithCompletion:]_block_invoke.290
- ___63-[PKPaymentService removeExpressPassesWithCardType:completion:]_block_invoke.234
- ___63-[PKPaymentWebService _nonceWithRequest:serviceURL:completion:]_block_invoke.801
- ___63-[PKPaymentWebService sendOwnershipTokensForReason:completion:]_block_invoke.376
- ___63-[PKPaymentWebService sendOwnershipTokensForReason:completion:]_block_invoke_2.377
- ___64-[PKPaymentService displayTapToRadarAlertForRequest:completion:]_block_invoke.121
- ___64-[PKPaymentService enforceUpgradedPasscodePolicyWithCompletion:]_block_invoke.301
- ___64-[PKPaymentService featureApplicationWithIdentifier:completion:]_block_invoke.340
- ___64-[PKPaymentService passOwnershipTokenWithIdentifier:completion:]_block_invoke.355
- ___64-[PKPaymentService redeemPaymentShareableCredential:completion:]_block_invoke.380
- ___64-[PKPaymentService revokeCredentialsWithIdentifiers:completion:]_block_invoke.365
- ___64-[PKPaymentWebServiceLocalProxyTargetDevice initWithConnection:]_block_invoke.290
- ___65-[PKAutoFillCardManager userDidUseCardWithDescriptor:credential:]_block_invoke.61
- ___65-[PKPaymentService isPassExpressWithUniqueIdentifier:completion:]_block_invoke.239
- ___65-[PKPaymentService notifyForFPANCardImportConsentWithCompletion:]_block_invoke.294
- ___65-[PKPaymentService passSharesForCredentialIdentifier:completion:]_block_invoke.369
- ___65-[PKPaymentService pendingFamilyMembersIgnoringCache:completion:]_block_invoke.327
- ___65-[PKPaymentService revokeMerchantTokenWithIdentifier:completion:]_block_invoke.291
- ___65-[PKPaymentService sharedPaymentWebServiceContextWithCompletion:]_block_invoke.279
- ___65-[PKPaymentService transactionsTotalAmountForRequest:completion:]_block_invoke.170
- ___65-[PKPaymentWebService _applePayTrustPublicKeyHashWithCompletion:]_block_invoke.944
- ___65-[PKSecureElement initializeSecureElementIfNecessaryWithHandler:]_block_invoke.265
- ___66-[PKPaymentService defaultPaymentPassIngestionSpecificIdentifier:]_block_invoke.329
- ___66-[PKPaymentService registerCredentialsWithIdentifiers:completion:]_block_invoke.363
- ___66-[PKPaymentService setBalanceReminder:forBalance:pass:completion:]_block_invoke.191
- ___66-[PKPaymentService transactionWithReferenceIdentifier:completion:]_block_invoke.165
- ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.313
- ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.320
- ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.327
- ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.335
- ___67-[PKPaymentProvisioningController retrieveAllAvailableCredentials:]_block_invoke.344
- ___67-[PKPaymentService addPlaceholderPassWithConfiguration:completion:]_block_invoke.359
- ___67-[PKPaymentService clearFPANCardImportNotificationsWithCompletion:]_block_invoke.296
- ___67-[PKPaymentService redeemProvisioningSharingIdentifier:completion:]_block_invoke.382
- ___67-[PKPaymentService requestNotificationAuthorizationWithCompletion:]_block_invoke.262
- ___67-[PKSecureElement consistencyCheckDeviceCredentialsWithCompletion:]_block_invoke.279
- ___68-[PKPaymentService deleteTransactionReceiptWithUniqueID:completion:]_block_invoke.393
- ___68-[PKPaymentService transactionWithTransactionIdentifier:completion:]_block_invoke.159
- ___68-[PKPaymentService updateAllMapsBrandAndMerchantDataWithCompletion:]_block_invoke.280
- ___68-[PKPaymentWebService retrieveMerchantTokensWithRequest:completion:]_block_invoke.779
- ___68-[PKSecureElement markAppletsWithIdentifiersForDeletion:completion:]_block_invoke.301
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.337
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.339
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.346
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.348
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.357
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.364
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke.370
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_2.349
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_2.358
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_2.367
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_2.371
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_3.351
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_3.360
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_3.373
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_4.352
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_4.363
- ___69-[PKPaymentAuthorizationStateMachine _performAuthorizationWithParam:]_block_invoke_4.369
- ___69-[PKPaymentOffersController _performMerchandisingRequest:completion:]_block_invoke.130
- ___69-[PKPaymentOffersController _performPaymentOffersRequest:completion:]_block_invoke.159
- ___69-[PKPaymentOffersController _performPaymentOffersRequest:completion:]_block_invoke_2.160
- ___69-[PKPaymentService featureApplicationsForProvisioningWithCompletion:]_block_invoke.333
- ___69-[PKPaymentService initializeSecureElementIfNecessaryWithCompletion:]_block_invoke.216
- ___69-[PKPaymentService removeExpressPassWithUniqueIdentifier:completion:]_block_invoke.236
- ___69-[PKPaymentService reserveStorageForAppletTypes:metadata:completion:]_block_invoke.386
- ___69-[PKPaymentService setExpressWithPassInformation:credential:handler:]_block_invoke.233
- ___69-[PKSecureElement _startSecureElementManagerSessionWithType:handler:]_block_invoke.249
- ___69-[PKSecureElement _startSecureElementManagerSessionWithType:handler:]_block_invoke.250
- ___70-[PKMobileAssetManager _downloadPrefetchableAssetsForType:completion:]_block_invoke.402
- ___70-[PKMobileAssetManager _downloadPrefetchableAssetsForType:completion:]_block_invoke.404
- ___70-[PKPaymentOffersController _performDynamicContentRequest:completion:]_block_invoke.196
- ___70-[PKPaymentOffersController _performDynamicContentRequest:completion:]_block_invoke.198
- ___70-[PKPaymentOffersController _performDynamicContentRequest:completion:]_block_invoke_2.199
- ___70-[PKPaymentOffersController _performRewardsBalanceRequest:completion:]_block_invoke.233
- ___70-[PKPaymentOffersController _performRewardsBalanceRequest:completion:]_block_invoke.241
- ___70-[PKPaymentOffersController _performRewardsBalanceRequest:completion:]_block_invoke_2.237
- ___70-[PKPaymentOffersController _performRewardsBalanceRequest:completion:]_block_invoke_2.242
- ___70-[PKPaymentProvisioningController deleteCredential:completionHandler:]_block_invoke.735
- ___70-[PKPaymentProvisioningController deleteCredential:completionHandler:]_block_invoke.738
- ___70-[PKPaymentService accountAttestationAnonymizationSaltWithCompletion:]_block_invoke.356
- ___70-[PKPaymentService revokeCredentialsWithReaderIdentifiers:completion:]_block_invoke.366
- ___70-[PKPaymentService suggestPaymentFPANCredentialImport:withCompletion:]_block_invoke.293
- ___70-[PKPaymentService transactionsWithTransactionIdentifiers:completion:]_block_invoke.160
- ___70-[PKPaymentWebService _handlePassListDownloadTask:data:fromPushTopic:]_block_invoke.899
- ___70-[PKSecureElement signChallenge:forPaymentApplication:withCompletion:]_block_invoke.303
- ___70-[PKSecureElement signChallenge:signatureEntanglementMode:completion:]_block_invoke.304
- ___71-[PKPaymentService featureApplicationsForAccountIdentifier:completion:]_block_invoke.330
- ___71-[PKPaymentService plansForPaymentPassWithUniqueIdentifier:completion:]_block_invoke.188
- ___71-[PKPaymentService removeExpressPassWithUniqueIdentifierV2:completion:]_block_invoke.235
- ___71-[PKPaymentService setExpressWithPassConfiguration:credential:handler:]_block_invoke.231
- ___72-[PKPaymentProvisioningController _identityConfigurationWithCompletion:]_block_invoke.470
- ___73-[PKPaymentAuthorizationStateMachine _performRewrapRequestImplWithParam:]_block_invoke.284
- ___73-[PKPaymentAuthorizationStateMachine _performRewrapRequestImplWithParam:]_block_invoke.288
- ___73-[PKPaymentAuthorizationStateMachine _performRewrapRequestImplWithParam:]_block_invoke_2.291
- ___73-[PKPaymentService ambiguousTransactionWithServiceIdentifier:completion:]_block_invoke.395
- ___73-[PKPaymentService clearFPANCardImportNotificationHistoryWithCompletion:]_block_invoke.297
- ___73-[PKPaymentService featureApplicationWithReferenceIdentifier:completion:]_block_invoke.335
- ___73-[PKPaymentWebService URLSession:downloadTask:didFinishDownloadingToURL:]_block_invoke.853
- ___73-[PKSecureElement peerPaymentEnrollmentDataWithAlternateDSID:completion:]_block_invoke.338
- ___73-[PKSecureElement peerPaymentEnrollmentDataWithAlternateDSID:completion:]_block_invoke.341
- ___73-[PKSecureElement peerPaymentEnrollmentDataWithAlternateDSID:completion:]_block_invoke_2.339
- ___73-[PKSecureElement peerPaymentEnrollmentDataWithAlternateDSID:completion:]_block_invoke_3.340
- ___74-[PKMobileAssetManager _downloadAsset:isDiscretionary:timeout:completion:]_block_invoke.439
- ___74-[PKPaymentService balancesForPaymentPassWithUniqueIdentifier:completion:]_block_invoke.187
- ___74-[PKPaymentService messagesForPaymentPassWithUniqueIdentifier:completion:]_block_invoke.186
- ___74-[PKPaymentService notifyForFPANCardImportWithCredentials:withCompletion:]_block_invoke.295
- ___74-[PKPaymentService setAccountAttestationAnonymizationSalt:withCompletion:]_block_invoke.358
- ___74-[PKPaymentService setCommutePlanReminder:forCommutePlan:pass:completion:]_block_invoke.195
- ___74-[PKPaymentService valueAddedServiceTransactionWithIdentifier:completion:]_block_invoke.211
- ___74-[PKPaymentWebService backgroundPerformDeviceCheckInForRegion:identifier:]_block_invoke.383
- ___74-[PKSecureElement createAliroHydraKeyWithServerParameters:withCompletion:]_block_invoke.316
- ___75-[PKPaymentService balanceReminderThresholdForBalance:pass:withCompletion:]_block_invoke.189
- ___75-[PKPaymentService commutePlanReminderForCommputePlan:pass:withCompletion:]_block_invoke.193
- ___75-[PKPaymentService prepareProvisioningTarget:checkFamilyCircle:completion:]_block_invoke.377
- ___75-[PKPaymentService spendingCategoryTransactionGroupsForRequest:completion:]_block_invoke.150
- ___75-[PKPaymentService submitEncryptedPIN:forTransactionIdentifier:completion:]_block_invoke.319
- ___75-[PKPaymentService transactionTagsForTransactionWithIdentifier:completion:]_block_invoke.394
- ___76-[PKPaymentWebServiceRemoteProxyTargetDevice initWithWebService:connection:]_block_invoke.634
- ___77-[PKPaymentService sendDeviceSharingCapabilitiesRequestForHandle:completion:]_block_invoke.397
- ___77-[PKPaymentService updateFeatureApplicationsForAccountIdentifier:completion:]_block_invoke.331
- ___77-[PKPaymentService updateMetadataOnPassWithIdentifier:credential:completion:]_block_invoke.362
- ___77-[PKPaymentSetupFieldsModel prefillValuesWithPaymentCredential:targetDevice:]_block_invoke
- ___78-[PKPaymentProvisioningController _requestProvisioning:withCompletionHandler:]_block_invoke.640
- ___78-[PKPaymentProvisioningController _requestProvisioning:withCompletionHandler:]_block_invoke_2.641
- ___78-[PKPaymentProvisioningController _startLocationSearchWithTimeout:completion:]_block_invoke.666
- ___78-[PKPaymentService categoryVisualizationMagnitudesForPassUniqueID:completion:]_block_invoke.349
- ___78-[PKPaymentService featureApplicationsForAccountUserInvitationWithCompletion:]_block_invoke.334
- ___78-[PKPaymentService hasTransactionsForTransactionSourceIdentifiers:completion:]_block_invoke.139
- ___78-[PKPaymentService requestNotificationAuthorizationIfNecessaryWithCompletion:]_block_invoke.261
- ___79-[PKAccountService accountBalancesForAccountIdentifier:startDate:endDate:type:]_block_invoke.61
- ___79-[PKPaymentProvisioningController _associateCredentials:withCompletionHandler:]_block_invoke.370
- ___79-[PKPaymentService submitUserConfirmation:forTransactionIdentifier:completion:]_block_invoke.316
- ___79-[PKPaymentWebService retrieveMerchantTokensUnifiedListWithRequest:completion:]_block_invoke.777
- ___80-[PKMobileAssetManager performScheduledActivityWithIdentifier:activityCriteria:]_block_invoke.418
- ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.396
- ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.403
- ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.412
- ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.420
- ___80-[PKPaymentProvisioningController cachedPaymentSetupProductModelWithCompletion:]_block_invoke.424
- ___80-[PKPaymentProvisioningController requestPurchasesForProduct:completionHandler:]_block_invoke.514
- ___80-[PKPaymentProvisioningController requestPurchasesForProduct:completionHandler:]_block_invoke.517
- ___80-[PKPaymentService passUniqueIdentifierForTransactionWithIdentifier:completion:]_block_invoke.175
- ___80-[PKPaymentWebService _registerIfNeededWithResponse:task:isRedirect:completion:]_block_invoke.941
- ___80-[PKPaymentWebService _registerIfNeededWithResponse:task:isRedirect:completion:]_block_invoke.943
- ___81-[PKRemoteAssetManager addRemoteAssetData:shouldWriteData:forManifestItem:error:]_block_invoke.55
- ___81-[PKSecureElement initializeSecureElementQueuingServerConnection:withCompletion:]_block_invoke.264
- ___82-[PKPaymentService markAuthenticationCompleteForTransactionIdentifier:completion:]_block_invoke.315
- ___83-[PKPaymentService installmentPlansWithTransactionReferennceIdentifier:completion:]_block_invoke.167
- ___83-[PKPaymentService installmentTransactionsForInstallmentPlanIdentifier:completion:]_block_invoke.166
- ___83-[PKPaymentService mapsMerchantWithIdentifier:resultProviderIdentifier:completion:]_block_invoke.281
- ___83-[PKPaymentService saveProvisioningSupportData:forPassUniqueIdentifier:completion:]_block_invoke.372
- ___83-[PKPaymentService transactionSourceTypeForTransactionSourceIdentifier:completion:]_block_invoke.162
- ___83-[PKPaymentService transactionsRequiringReviewForAccountWithIdentifier:completion:]_block_invoke.348
- ___83-[PKPaymentWebService _performRewrapRequest:serviceURL:responseHandler:completion:]_block_invoke.826
- ___83-[PKSecureElement _executeSecureElementAsyncSessionHandlersWithSession:completion:]_block_invoke.252
- ___84-[PKPaymentOffersController initWithPaymentService:paymentWebService:configuration:]_block_invoke
- ___84-[PKPaymentOffersController initWithPaymentService:paymentWebService:configuration:]_block_invoke_2
- ___84-[PKPaymentService passUniqueIdentifiersForTransactionSourceIdentifiers:completion:]_block_invoke.177
- ___84-[PKPaymentService setDefaultPaymentApplication:forPassUniqueIdentifier:completion:]_block_invoke.213
- ___84-[PKPaymentService(PaymentOffers) didInteractWithConfirmationRecordFollowupMessage:]_block_invoke.33
- ___85-[PKPaymentProvisioningController _setupAccountCredentialForProvisioning:completion:]_block_invoke.537
- ___85-[PKPaymentProvisioningController _setupAccountCredentialForProvisioning:completion:]_block_invoke.539
- ___85-[PKPaymentProvisioningController _setupAccountCredentialForProvisioning:completion:]_block_invoke_2.541
- ___85-[PKPaymentService setDefaultExpressTransitPassIdentifier:withCredential:completion:]_block_invoke.221
- ___85-[PKPaymentService submitBarcodePaymentEvent:forPassUniqueIdentifier:withCompletion:]_block_invoke.322
- ___85-[PKPaymentWebService _performApplePayTrustRegistrationWithURL:pushToken:completion:]_block_invoke.364
- ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke.494
- ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke.497
- ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke_2.499
- ___86-[PKPaymentProvisioningController provisioningExtensionProductsWithCompletionHandler:]_block_invoke_3.500
- ___86-[PKPaymentService userNotificationActionPerformed:notificationIdentifier:completion:]_block_invoke.264
- ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.436
- ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.442
- ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.449
- ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.453
- ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.458
- ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke.462
- ___87-[PKPaymentProvisioningController updatePaymentSetupProductModelWithCompletionHandler:]_block_invoke_2.463
- ___87-[PKPaymentService conflictingExpressPassIdentifiersForPassInformation:withCompletion:]_block_invoke.228
- ___87-[PKPaymentService transactionsWithTransactionSource:withBackingData:limit:completion:]_block_invoke.158
- ___87-[PKPaymentService transitStateWithPassUniqueIdentifier:paymentApplication:completion:]_block_invoke.244
- ___87-[PKPaymentWebService _handleRetryAfterRegisterWithRequest:response:completionHandler:]_block_invoke.913
- ___88-[PKPaymentAuthorizationStateMachine _performPrepareTransactionDetailsRequestWithParam:]_block_invoke.277
- ___88-[PKPaymentService valueAddedServiceTransactionsForPaymentTransaction:limit:completion:]_block_invoke.210
- ___89-[PKAutoFillCardManager activeFPANCardsWithOptions:allowedCardTypes:sortType:completion:]_block_invoke.41
- ___89-[PKDiscoveryMedia downloadImageDataWithScale:shouldWriteData:isExpandedView:completion:]_block_invoke
- ___89-[PKPaymentService conflictingExpressPassIdentifiersForPassConfiguration:withCompletion:]_block_invoke.227
- ___89-[PKPaymentService processedAuthenticationMechanism:forTransactionIdentifier:completion:]_block_invoke.314
- ___89-[PKPaymentService submitTransactionAnswerForTransaction:questionType:answer:completion:]_block_invoke.347
- ___90-[PKPaymentService clearProvisioningSupportDataOfType:forPassUniqueIdentifier:completion:]_block_invoke.373
- ___91-[PKPaymentProvisioningController verifyPassIsSupportedForExpressInLocalMarket:completion:]_block_invoke.646
- ___91-[PKPaymentProvisioningController verifyPassIsSupportedForExpressInLocalMarket:completion:]_block_invoke.650
- ___91-[PKPaymentProvisioningController verifyPassIsSupportedForExpressInLocalMarket:completion:]_block_invoke.652
- ___91-[PKPaymentService retrievePINEncryptionCertificateForPassUniqueIdentifier:withCompletion:]_block_invoke.312
- ___91-[PKPaymentService setDefaultExpressFelicaTransitPassIdentifier:withCredential:completion:]_block_invoke.219
- ___92-[PKPaymentService transactionWithServiceIdentifier:transactionSourceIdentifier:completion:]_block_invoke.164
- ___92-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:]_block_invoke.295
- ___92-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:]_block_invoke.298
- ___92-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:]_block_invoke_2.297
- ___93-[PKPaymentService cancelAutoTopUpForPassWithUniqueIdentifier:balanceIdentifiers:completion:]_block_invoke.192
- ___93-[PKPaymentService fetchBarcodesForPassUniqueIdentifier:sessionExchangeToken:withCompletion:]_block_invoke.307
- ___93-[PKPaymentService transactionsRelatedToTransaction:transactionSourceIdentifiers:completion:]_block_invoke.204
- ___93-[PKSecureElement generateTransactionKeyWithReaderIdentifier:readerPublicKey:withCompletion:]_block_invoke.313
- ___94-[PKPaymentService sharingInvitationWasInvalidated:withCredentialIdentifier:error:completion:]_block_invoke.370
- ___94-[PKPaymentService transactionsWithFullPaymentHashes:transactionSourceIdentifiers:completion:]_block_invoke.161
- ___94-[PKPaymentService valueAddedServiceTransactionsForPassWithUniqueIdentifier:limit:completion:]_block_invoke.209
- ___95-[PKPaymentService insertOrUpdatePaymentTransaction:forTransactionSourceIdentifier:completion:]_block_invoke.142
- ___96-[PKPaymentService ambiguousPassUniqueIdentifierForTransactionWithServiceIdentifier:completion:]_block_invoke.178
- ___96-[PKPaymentService invalidateAuxiliaryCapabilityCertificatesForPassUniqueIdentifier:completion:]_block_invoke.306
- ___96-[PKPaymentService merchantForPassUniqueIdentifier:withAuxiliaryPassInformationItem:completion:]_block_invoke.289
- ___96-[PKPaymentService provideEncryptedPushProvisioningTarget:sharingInstanceIdentifier:completion:]_block_invoke.376
- ___96-[PKPaymentService submitEncryptedPIN:forTransactionIdentifier:sessionExchangeToken:completion:]_block_invoke.320
- ___96-[PKPaymentService transactionReceiptForTransactionWithIdentifier:updateIfNecessary:completion:]_block_invoke.391
- ___96-[PKPaymentWebService _backgroundDownloadCloudStoreAssetsForItem:cloudStoreCoordinatorDelegate:]_block_invoke.890
- ___96-[PKPaymentWebService _backgroundDownloadCloudStoreAssetsForItem:cloudStoreCoordinatorDelegate:]_block_invoke.892
- ___96-[PKPaymentWebService _backgroundDownloadCloudStoreAssetsForItem:cloudStoreCoordinatorDelegate:]_block_invoke_2.891
- ___96-[PKPaymentWebService _backgroundDownloadCloudStoreAssetsForItem:cloudStoreCoordinatorDelegate:]_block_invoke_2.895
- ___96-[PKPaymentWebService registerDeviceAtBrokerURL:withConsistencyCheckResults:retries:completion:]_block_invoke.341
- ___96-[PKPaymentWebService registerDeviceAtBrokerURL:withConsistencyCheckResults:retries:completion:]_block_invoke.348
- ___97-[PKPaymentService augmentedProductForInstallmentConfiguration:experimentDetails:withCompletion:]_block_invoke.337
- ___98-[PKDashboardTransactionFetcher _addCashbackTransactions:synchronous:currentMonthOnly:completion:]_block_invoke.75
- ___98-[PKPaymentService updatePreferredCategory:forTransactionsWithIdentifiers:paymentPass:completion:]_block_invoke.205
- ___99+[PKSecureElement accessSecureElementManagerSessionWithSessionExchangeToken:callbackQueue:handler:]_block_invoke.244
- ___99+[PKSecureElement accessSecureElementManagerSessionWithSessionExchangeToken:callbackQueue:handler:]_block_invoke.245
- ___99-[PKPaymentService userNotificationActionPerformed:applicationMessageContentIdentifier:completion:]_block_invoke.263
- ___99-[PKPaymentService(PaymentOffers) updatePaymentRewardsBalancesWithPassUniqueIdentifier:completion:]_block_invoke.36
- ___Block_byref_object_copy_.539
- ___Block_byref_object_dispose_.540
- ___PKPeerPaymentRemoveRecurringPaymentRecentMemoIcon_block_invoke.1113
- ___PKRequestContactAccessWithCompletion_block_invoke.312
- ___block_descriptor_48_e8_32s40r_e20_v24?0Q8"NSError"16lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e20_v24?0q8"NSError"16lr40l8s32l8
- ___block_descriptor_48_e8_32s40s_e38_v28?0B8"NSNull"12"<PKCancelable>"20ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e17_v16?0"NSArray"8lw40l8s32l8
- ___block_descriptor_57_e8_32s40s48r_e18_"NSString"12?0B8ls32l8s40l8r48l8
- ___block_descriptor_72_e8_32s40s48bs56r64r_e61_v32?0"PKAsyncOperationState"8"NSNull"16?<v?"NSNull"B>24ls32l8s48l8s40l8r56l8r64l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e32_v28?0B8"NSArray"12"NSError"20ls32l8s40l8r56l8r64l8s48l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e32_v28?0B8"NSError"12"NSArray"20ls32l8r56l8s40l8r64l8s48l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0ls32l8r56l8r64l8s40l8s48l8
- ___block_literal_global.1003
- ___block_literal_global.1005
- ___block_literal_global.1010
- ___block_literal_global.1018
- ___block_literal_global.1021
- ___block_literal_global.1049
- ___block_literal_global.1054
- ___block_literal_global.1056
- ___block_literal_global.1061
- ___block_literal_global.1066
- ___block_literal_global.1071
- ___block_literal_global.1076
- ___block_literal_global.1081
- ___block_literal_global.1086
- ___block_literal_global.1091
- ___block_literal_global.1096
- ___block_literal_global.1098
- ___block_literal_global.1106
- ___block_literal_global.1108
- ___block_literal_global.1110
- ___block_literal_global.1112
- ___block_literal_global.1137
- ___block_literal_global.1142
- ___block_literal_global.1144
- ___block_literal_global.1149
- ___block_literal_global.1152
- ___block_literal_global.1221
- ___block_literal_global.1226
- ___block_literal_global.1233
- ___block_literal_global.1236
- ___block_literal_global.1259
- ___block_literal_global.1300
- ___block_literal_global.1317
- ___block_literal_global.1321
- ___block_literal_global.1416
- ___block_literal_global.1418
- ___block_literal_global.1421
- ___block_literal_global.1479
- ___block_literal_global.1481
- ___block_literal_global.1486
- ___block_literal_global.1490
- ___block_literal_global.1504
- ___block_literal_global.1506
- ___block_literal_global.1511
- ___block_literal_global.1525
- ___block_literal_global.1534
- ___block_literal_global.1537
- ___block_literal_global.1539
- ___block_literal_global.1542
- ___block_literal_global.181
- ___block_literal_global.188
- ___block_literal_global.199
- ___block_literal_global.201
- ___block_literal_global.203
- ___block_literal_global.205
- ___block_literal_global.207
- ___block_literal_global.209
- ___block_literal_global.213
- ___block_literal_global.220
- ___block_literal_global.223
- ___block_literal_global.225
- ___block_literal_global.238
- ___block_literal_global.243
- ___block_literal_global.245
- ___block_literal_global.250
- ___block_literal_global.252
- ___block_literal_global.254
- ___block_literal_global.266
- ___block_literal_global.268
- ___block_literal_global.270
- ___block_literal_global.275
- ___block_literal_global.284
- ___block_literal_global.286
- ___block_literal_global.288
- ___block_literal_global.296
- ___block_literal_global.298
- ___block_literal_global.299
- ___block_literal_global.300
- ___block_literal_global.324
- ___block_literal_global.347
- ___block_literal_global.360
- ___block_literal_global.369
- ___block_literal_global.378
- ___block_literal_global.381
- ___block_literal_global.390
- ___block_literal_global.414
- ___block_literal_global.417
- ___block_literal_global.422
- ___block_literal_global.436
- ___block_literal_global.438
- ___block_literal_global.440
- ___block_literal_global.481
- ___block_literal_global.503
- ___block_literal_global.522
- ___block_literal_global.529
- ___block_literal_global.531
- ___block_literal_global.540
- ___block_literal_global.647
- ___block_literal_global.673
- ___block_literal_global.675
- ___block_literal_global.684
- ___block_literal_global.693
- ___block_literal_global.696
- ___block_literal_global.721
- ___block_literal_global.729
- ___block_literal_global.731
- ___block_literal_global.735
- ___block_literal_global.762
- ___block_literal_global.783
- ___block_literal_global.851
- ___block_literal_global.852
- ___block_literal_global.855
- ___block_literal_global.866
- ___block_literal_global.894
- ___block_literal_global.897
- ___block_literal_global.901
- ___block_literal_global.903
- ___block_literal_global.922
- ___block_literal_global.937
- ___block_literal_global.939
- ___block_literal_global.946
- ___block_literal_global.948
- ___block_literal_global.950
- ___block_literal_global.952
- ___block_literal_global.981
- _block_copy_helper.105
- _block_copy_helper.111
- _block_copy_helper.112
- _block_copy_helper.118
- _block_copy_helper.125
- _block_copy_helper.130
- _block_copy_helper.135
- _block_copy_helper.142
- _block_copy_helper.159
- _block_copy_helper.167
- _block_copy_helper.239
- _block_copy_helper.264
- _block_copy_helper.275
- _block_copy_helper.292
- _block_copy_helper.69
- _block_copy_helper.95
- _block_descriptor.107
- _block_descriptor.113
- _block_descriptor.114
- _block_descriptor.120
- _block_descriptor.127
- _block_descriptor.132
- _block_descriptor.137
- _block_descriptor.144
- _block_descriptor.161
- _block_descriptor.169
- _block_descriptor.241
- _block_descriptor.266
- _block_descriptor.277
- _block_descriptor.294
- _block_descriptor.71
- _block_descriptor.97
- _block_destroy_helper.106
- _block_destroy_helper.112
- _block_destroy_helper.113
- _block_destroy_helper.119
- _block_destroy_helper.126
- _block_destroy_helper.131
- _block_destroy_helper.136
- _block_destroy_helper.143
- _block_destroy_helper.160
- _block_destroy_helper.168
- _block_destroy_helper.240
- _block_destroy_helper.265
- _block_destroy_helper.276
- _block_destroy_helper.293
- _block_destroy_helper.70
- _block_destroy_helper.96
- _objc_msgSend$_remoteAssetForScale:isExpandedView:
- _objc_msgSend$_setExpiration:
- _objc_msgSend$_updatePaymentSetupProduct:displayName:localizedDescription:longLocalizedDescription:partnerArray:productIdentifier:paymentOptions:termsURL:provisioningMethodDetailsList:readerModeMetadata:requiredFields:imageAssets:minimumOSVersion:region:regionData:hsa2Requirement:suppressPendingPurchases:supportedTransitNetworkIdentifiers:onboardingItems:actionBaseURL:productState:minimumProductAge:maximumProductAge:minimumTargetUserSupportedAge:associatedStoreIdentifiers:appLaunchURL:regionIdentifier:type:localizedNotificationTitle:localizedNotificationMessage:discoveryCardIdentifier:clientInfo:searchTerms:featureIdentifier:criteriaIdentifier:
- _objc_msgSend$activeAutoFillFPANCardCount
- _objc_msgSend$countOfVirtualCardsInKeychain
- _objc_msgSend$countOfVirtualCardsInKeychainWithCompletion:
- _objc_msgSend$fileURLWithPathComponents:
- _objc_msgSend$initWithCardholderName:pan:expiration:securityCode:billingAddress:
- _objc_msgSend$initWithPaymentHash:transactionDate:merchantName:merchantRawName:industryCategory:industryCode:merchantType:merchantCountryCode:terminalIdentifier:merchantAdditionalData:paymentNetwork:isMerchantTokenTransaction:isCoarseLocation:location:merchantIdentifier:merchantRawCANL:merchantRawCity:merchantRawState:merchantRawCountry:merchantCity:merchantZip:merchantState:merchantCleanConfidenceLevel:rewardsAmount:rewardsCurrency:rewardsEligibilityReason:adamIdentifier:webURL:webMerchantIdentifier:webMerchantName:
- _objc_msgSend$isEqualToDateInterval:
- _objc_msgSend$isOwnerAccountActivePersonalized
- _objc_msgSend$reportProvisioningStepForReporter:step:success:error:
- _objc_msgSend$supportsRequestPhysicalCard
- _objc_msgSend$supportsSearchForPassUniqueID:completion:
- _objc_msgSend$virtualCardCountWithActiveVPAN
- _objectdestroy.103Tm
- _objectdestroy.109Tm
- _objectdestroy.202Tm
- _objectdestroy.29Tm
- _objectdestroy.54Tm
- _objectdestroy.90Tm
- _symbolic _____ySo7PKColorCG 11PassKitCore14CodableWrapperV
- _symbolic _____ySo7PKColorCGSg 11PassKitCore14CodableWrapperV
CStrings:
+ ".count"
+ ".duration"
+ "@\"NSString\"16@?0@\"PKPaymentCredential\"8"
+ "@\"PKAppProtectionApp\""
+ "@\"PKProvisioningAnalyticsSessionPreflightReporter\""
+ "@\"PKSpringAnimationFactory\""
+ "AUD"
+ "AZN"
+ "Address Error"
+ "B16@?0@\"PKAccountFeatureDescriptor\"8"
+ "BRL"
+ "Billing Address Error"
+ "CAD"
+ "CAR_KEY_SHARING_CONFIRM_PASSCODE_TITLE"
+ "CHF"
+ "CLP"
+ "CODE"
+ "COP"
+ "CRC"
+ "Caches"
+ "Contact Error"
+ "Contactless Interface Session stopping transaction due to a credential identifier mismatch, the current credential cannot satisfy the reader request."
+ "DKK"
+ "GEL"
+ "ILS"
+ "INR"
+ "JCBAutoFill"
+ "KRW"
+ "KZT"
+ "MNT"
+ "MPANsUnifiedView"
+ "MXN"
+ "MYR"
+ "NOK"
+ "Others"
+ "PEN"
+ "PKAccountCardAvailabilityInfo"
+ "PKAnalyticsErrorTextClassifier"
+ "PKExpirationDateFormatter failed to update date formatter with recent twoDigitStartDate"
+ "PKProvisioningAnalyticsSessionPreflightReporter"
+ "PKProvisioningAnalyticsSessionPreflightToken"
+ "PLN"
+ "PYG"
+ "Q1"
+ "RTC reporting for subject: %@ initiated with session ID: %@ and session token: %@"
+ "RUB"
+ "Registering Scheduled Activity Client: %@"
+ "SEK"
+ "SGD"
+ "Shipping Address Error"
+ "T@\"NSDate\",R,C,N,V_expirationDate"
+ "T@\"NSMutableDictionary\",R,N,V_stepProperties"
+ "T@\"NSSet\",R,N,V_supportedFeatures"
+ "T@\"NSString\",C,N,V_localizedPhysicalButtonConfirmationTitle"
+ "T@\"PKDiscoveryMedia\",R,N"
+ "T@\"PKProvisioningAnalyticsSessionPreflightReporter\",&,N"
+ "TB,N,V_cardIsInWallet"
+ "TB,N,V_hasAutomaticallyPresentedPass"
+ "TB,R,N,V_showOtherProviders"
+ "TQ,R,N,V_accountState"
+ "TQ,R,N,V_accountType"
+ "Td,R,N,V_start"
+ "UAH"
+ "Updating payment offer session details %@"
+ "VELOCITY_ERROR_MESSAGE"
+ "VELOCITY_ERROR_TITLE"
+ "VND"
+ "_analyticsReporter"
+ "_archivedParent"
+ "_backgroundMediaByKey"
+ "_cardIsInWallet"
+ "_didBeginSubject"
+ "_expirationDateFormatter"
+ "_hasAutomaticallyPresentedPass"
+ "_initDashboardInstance"
+ "_initWithPaymentService:paymentWebService:configuration:"
+ "_invertedFactory"
+ "_isUnaffiliated"
+ "_localizedPhysicalButtonConfirmationTitle"
+ "_noCredentialForISO18013Request"
+ "_pendingEventsToReport"
+ "_remoteAssetForScale:"
+ "_reportPreflightStepCompleteForContext:token:"
+ "_reportProvisioningStep:finishedWithStatus:error:context:"
+ "_sendPendingEvents"
+ "_setExpirationDate:"
+ "_showOtherProviders"
+ "_startReportingIfNecessary"
+ "_stepProperties"
+ "_updatePaymentSetupProduct:displayName:localizedDescription:longLocalizedDescription:partnerArray:productIdentifier:paymentOptions:termsURL:provisioningMethodDetailsList:readerModeMetadata:requiredFields:imageAssets:minimumOSVersion:region:regionData:hsa2Requirement:suppressPendingPurchases:supportedTransitNetworkIdentifiers:onboardingItems:actionBaseURL:productState:minimumProductAge:maximumProductAge:minimumTargetUserSupportedAge:associatedStoreIdentifiers:appLaunchURL:regionIdentifier:type:localizedNotificationTitle:localizedNotificationMessage:discoveryCardIdentifier:clientInfo:searchTerms:featureIdentifier:criteriaIdentifier:showOtherProviders:"
+ "accountNumberSpecified"
+ "activityFollowUp"
+ "addMoneySpecified"
+ "affiliateReporter:"
+ "analyticsReporter"
+ "analyticsValueForResult:"
+ "appExtension.count"
+ "appExtension.duration"
+ "applePayDemoCompletedWithin"
+ "applePayUserEducationDemo"
+ "australiandollarsign"
+ "automaticSelectionApplied"
+ "backgroundMediaCropped"
+ "backgroundMediaExpanded"
+ "balanceDetails"
+ "bankConnectInfoPage"
+ "billing"
+ "brazilianrealsign"
+ "canArchiveWithTransaction:"
+ "cardAvailabilityInfo"
+ "cardIsInWallet"
+ "cardIsInWallet: '%@'; "
+ "categoryAndSource"
+ "chineseyuanrenminbisign"
+ "classifyErrorText:"
+ "coloncurrencysign"
+ "com.apple.application-icon.passbook-stub.wallet"
+ "com.apple.application-icon.passbook.wallet"
+ "com.apple.wallet.ecom.smartButtons"
+ "com.apple.wallet.ecom.smartButtons.appBundleID"
+ "com.apple.wallet.ecom.smartButtons.buttonType"
+ "com.apple.wallet.ecom.smartButtons.buttonType.addMoney"
+ "com.apple.wallet.ecom.smartButtons.buttonType.book"
+ "com.apple.wallet.ecom.smartButtons.buttonType.buy"
+ "com.apple.wallet.ecom.smartButtons.buttonType.checkout"
+ "com.apple.wallet.ecom.smartButtons.buttonType.continue"
+ "com.apple.wallet.ecom.smartButtons.buttonType.contribute"
+ "com.apple.wallet.ecom.smartButtons.buttonType.donate"
+ "com.apple.wallet.ecom.smartButtons.buttonType.inStore"
+ "com.apple.wallet.ecom.smartButtons.buttonType.order"
+ "com.apple.wallet.ecom.smartButtons.buttonType.plain"
+ "com.apple.wallet.ecom.smartButtons.buttonType.reload"
+ "com.apple.wallet.ecom.smartButtons.buttonType.rent"
+ "com.apple.wallet.ecom.smartButtons.buttonType.setup"
+ "com.apple.wallet.ecom.smartButtons.buttonType.subscribe"
+ "com.apple.wallet.ecom.smartButtons.buttonType.support"
+ "com.apple.wallet.ecom.smartButtons.buttonType.tip"
+ "com.apple.wallet.ecom.smartButtons.buttonType.topUp"
+ "com.apple.wallet.ecom.smartButtons.deviceType"
+ "com.apple.wallet.ecom.smartButtons.environment"
+ "com.apple.wallet.ecom.smartButtons.environment.inApp"
+ "com.apple.wallet.ecom.smartButtons.errorType"
+ "com.apple.wallet.ecom.smartButtons.errorType.ButtonFinalContentNotRendered"
+ "com.apple.wallet.ecom.smartButtons.errorType.NoPassImageReceived"
+ "com.apple.wallet.ecom.smartButtons.errorType.XPCServiceInterrupted"
+ "com.apple.wallet.ecom.smartButtons.errorType.XPCServiceInvalidated"
+ "com.apple.wallet.ecom.smartButtons.eventType"
+ "com.apple.wallet.ecom.smartButtons.eventType.applePayButtonRequest"
+ "com.apple.wallet.ecom.smartButtons.isDynamic"
+ "com.apple.wallet.ecom.smartButtons.issuer"
+ "com.apple.wallet.ecom.smartButtons.networkName"
+ "com.apple.wallet.ecom.smartButtons.osVersion"
+ "com.apple.wallet.ecom.smartButtons.productSubType"
+ "com.apple.wallet.ecom.smartButtons.referralSource.cardArt"
+ "com.apple.wallet.ecom.smartButtons.referralSource.smartButton"
+ "connectedCardTermsUpdate"
+ "containsAnyTerm:inText:"
+ "containsKeyFob"
+ "countOfVirtualCards"
+ "county"
+ "createPreflightReporter"
+ "createUnaffiliatedReporter"
+ "credentials.%@.count"
+ "credentials.count"
+ "credentials.duration"
+ "creditDebitIndicator: '%ld'; "
+ "danishkronesign"
+ "dashboardInstance"
+ "dashboardMessageDismiss"
+ "dashboardMessageType"
+ "debugTypeDescription"
+ "defaultDataProvider"
+ "deliver"
+ "digitalServicing"
+ "digitalServicingSpecified"
+ "dollarsign"
+ "dongsign"
+ "downloadImageDataWithScale:shouldWriteData:completion:"
+ "eir code"
+ "eircode"
+ "errorTextGroup"
+ "eurosign"
+ "factoryWithInvertedVelocity"
+ "financeKitSetup"
+ "financeKitTransactionPicker"
+ "finishPreflightForToken:"
+ "flowFinished"
+ "francsign"
+ "frontOfPass"
+ "guaranisign"
+ "hasAutomaticallyPresentedPass"
+ "hasContactlessTransactionWithin"
+ "hryvniasign"
+ "iBanSpecified"
+ "imageDataFromCacheWithScale:"
+ "indianrupeesign"
+ "initWithAccountState:accountType:supportedFeatures:"
+ "initWithCardholderName:pan:expirationDate:securityCode:billingAddress:"
+ "initWithPaymentHash:transactionDate:merchantName:merchantRawName:industryCategory:industryCode:merchantType:merchantCountryCode:terminalIdentifier:merchantAdditionalData:paymentNetwork:isMerchantTokenTransaction:isCoarseLocation:location:merchantIdentifier:merchantRawCANL:merchantRawCity:merchantRawState:merchantRawCountry:merchantCity:merchantZip:merchantState:merchantCleanConfidenceLevel:rewardsAmount:rewardsCurrency:rewardsEligibilityReason:adamIdentifier:webURL:webMerchantIdentifier:webMerchantName:isIssuerInstallmentTransaction:issuerInstallmentManagementURL:"
+ "isBankConnected"
+ "isBankEligible"
+ "isOwnerAccountPersonalized"
+ "isSpendingSummaryAvailable"
+ "larisign"
+ "linkToMaps"
+ "localizationKeyPostfixForInitiation"
+ "localizedPhysicalButtonConfirmationTitle"
+ "malaysianringgitsign"
+ "manageConnection"
+ "manatsign"
+ "merchandising-details"
+ "norwegiankronesign"
+ "offer-confirmation"
+ "oneMonth"
+ "payBill"
+ "payBillSpecified"
+ "paymentOfferCriteriaForPassUniqueID:criteriaType:completion:"
+ "peruviansolessign"
+ "pesosign"
+ "polishzlotysign"
+ "post code"
+ "postal code"
+ "postalcode"
+ "postcode"
+ "preflightStatus"
+ "priorMonthButton"
+ "priorYearButton"
+ "provisioningStepStart"
+ "reportAppExtensionPreflightComplete:token:"
+ "reportCredentialsPreflightComplete:token:"
+ "reportIncorrectMerchantInfo"
+ "reportPreflightEventForReporter:context:"
+ "reportPreflightStepComplete:itemCount:token:"
+ "reportPreflightStepComplete:token:"
+ "reportProvisioningStep:finishedWithStatus:context:"
+ "reportProvisioningStepForReporter:step:success:error:context:"
+ "reportProvisioningStepStart:"
+ "reportProvisioningStepStart:context:"
+ "reportProvisioningStepStartForReporter:step:context:"
+ "routingNumberSpecified"
+ "rublesign"
+ "scheduleApplePayDemoActivitySignal"
+ "setAnalyticsReporter:"
+ "setCardIsInWallet:"
+ "setHasAutomaticallyPresentedPass:"
+ "setLocalizedPhysicalButtonConfirmationTitle:"
+ "setupFieldsPrefilled"
+ "setupFieldsVisible"
+ "shekelsign"
+ "ship"
+ "shouldMessageArchiveWithTransaction:"
+ "shouldShowCardNumbersWithAccountAvailabilityInfo:dpanSuffixForPaymentApplication:"
+ "showOtherProviders"
+ "showOtherProvidersForAppProvisioningMethod"
+ "singaporedollarsign"
+ "sixMonths"
+ "sortCodeSpecified"
+ "spendingSummaryViewCategoryButton"
+ "spendingSummaryViewMerchantButton"
+ "startPreflight"
+ "stepProperties"
+ "sterlingsign"
+ "swedishkronasign"
+ "tengesign"
+ "transactionButton"
+ "transactionMapSpecified"
+ "transactionSummary"
+ "tugriksign"
+ "unable to find bundle identifier"
+ "updateLinkSpecified"
+ "updateSessionDetails:"
+ "v16@?0@\"PKPaymentOfferCriteria\"8"
+ "v28@?0B8@\"NSError\"12@\"NSURL\"20"
+ "v304@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224@232@240@248@256@264@272@280@288@296"
+ "v32@0:8@\"PKProvisioningAnalyticsSessionPreflightReporter\"16@\"NSDictionary\"24"
+ "v36@0:8d16B24@?28"
+ "v40@0:8@\"NSString\"16Q24@?<v@?@\"PKPaymentOfferCriteria\">32"
+ "v40@0:8@\"PKAutoFillCardDescriptor\"16@\"PKAutoFillCardCredential\"24@?<v@?@\"PKFPANCardCanSaveResult\">32"
+ "v40@0:8@\"PKProvisioningAnalyticsSessionStepReporter\"16@\"NSString\"24@\"NSDictionary\"32"
+ "v52@0:8@\"PKProvisioningAnalyticsSessionStepReporter\"16@\"NSString\"24B32@\"NSError\"36@\"NSDictionary\"44"
+ "v52@0:8@16@24B32@36@44"
+ "verificationChannelOptions"
+ "wonsign"
+ "yensign"
+ "zip code"
+ "zipcode"
+ "\xb1"
- "@\"NSString\"12@?0B8"
- "@28@0:8d16B24"
- "AppleBalanceReadyDismissed"
- "Contactless Interface Session Stopping Transaction"
- "Demo/Instructions.plist"
- "Error fetching count of cards %@"
- "Error: Failed to read peer payment recipient cache data from path: %@ with error: %@"
- "PEER_PAYMENT_TOP_UP_ITEM_FORMAT"
- "PKAccountOtherCardNumbersViewController failed to update date formatter with recent twoDigitStartDate"
- "PKEnableSeamlessMigrationKey"
- "PKPeerPaymentGroupRequestTrackingEnabledKey"
- "PKPreauthorizedPaymentNotificationsDisabled"
- "Q!"
- "RTC reporting for subject: %@ initiated with session ID: %@"
- "Rejecting result in chat that has multiple recipients"
- "T@\"NSString\",C,N,V_localizedBiometricConfirmationTitle"
- "T@\"NSURL\",R,N,V_localAssetURL"
- "T@\"PKDiscoveryMedia\",R,N,V_backgroundMedia"
- "Using cached payment offers catalog %@"
- "XPC Error fetching count %@"
- "_backgroundMedia"
- "_localAssetURL"
- "_localizedBiometricConfirmationTitle"
- "_remoteAssetForScale:isExpandedView:"
- "_setExpiration:"
- "_updatePaymentSetupProduct:displayName:localizedDescription:longLocalizedDescription:partnerArray:productIdentifier:paymentOptions:termsURL:provisioningMethodDetailsList:readerModeMetadata:requiredFields:imageAssets:minimumOSVersion:region:regionData:hsa2Requirement:suppressPendingPurchases:supportedTransitNetworkIdentifiers:onboardingItems:actionBaseURL:productState:minimumProductAge:maximumProductAge:minimumTargetUserSupportedAge:associatedStoreIdentifiers:appLaunchURL:regionIdentifier:type:localizedNotificationTitle:localizedNotificationMessage:discoveryCardIdentifier:clientInfo:searchTerms:featureIdentifier:criteriaIdentifier:"
- "activeAutoFillFPANCardCount"
- "archiveOnNextTransaction"
- "countOfVirtualCardsInKeychain"
- "countOfVirtualCardsInKeychainWithCompletion:"
- "cropped%@"
- "downloadImageDataWithScale:shouldWriteData:isExpandedView:completion:"
- "expanded%@"
- "fileURLWithPathComponents:"
- "imageDataFromCacheWithScale:isExpandedView:"
- "initWithPaymentHash:transactionDate:merchantName:merchantRawName:industryCategory:industryCode:merchantType:merchantCountryCode:terminalIdentifier:merchantAdditionalData:paymentNetwork:isMerchantTokenTransaction:isCoarseLocation:location:merchantIdentifier:merchantRawCANL:merchantRawCity:merchantRawState:merchantRawCountry:merchantCity:merchantZip:merchantState:merchantCleanConfidenceLevel:rewardsAmount:rewardsCurrency:rewardsEligibilityReason:adamIdentifier:webURL:webMerchantIdentifier:webMerchantName:"
- "isEqualToDateInterval:"
- "isOwnerAccountActivePersonalized"
- "localAsset"
- "localAssetURL"
- "localizedBiometricConfirmationTitle"
- "passBackgroundColor"
- "queryKeychainForCountOfVirtualCards:"
- "reportProvisioningStepForReporter:step:success:error:"
- "setLocalizedBiometricConfirmationTitle:"
- "shouldShowCardNumbersWithAccount:andPass:"
- "supportsSearchForPassUniqueID:"
- "supportsSearchForPassUniqueID:completion:"
- "updateIdentityEventToReportDashboardAnalytics:forPass:"
- "v24@0:8@?<v@?Q@\"NSError\">16"
- "v24@0:8@?<v@?q@\"NSError\">16"
- "v296@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224@232@240@248@256@264@272@280@288"
- "v40@0:8d16B24B28@?32"
- "v44@0:8@\"PKProvisioningAnalyticsSessionStepReporter\"16@\"NSString\"24B32@\"NSError\"36"
- "v44@0:8@16@24B32@36"

```
