## PassKitCore

> `/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore`

```diff

-1552.5.17.0.0
-  __TEXT.__text: 0x5eeffc
+1552.6.11.0.0
+  __TEXT.__text: 0x5f07e4
   __TEXT.__auth_stubs: 0x3a40
-  __TEXT.__objc_methlist: 0x581d8
+  __TEXT.__objc_methlist: 0x58370
   __TEXT.__const: 0x64f0
-  __TEXT.__cstring: 0x5ab12
+  __TEXT.__cstring: 0x5ac62
   __TEXT.__constg_swiftt: 0x1720
   __TEXT.__swift5_typeref: 0x1bd6
   __TEXT.__swift5_builtin: 0x154

   __TEXT.__swift5_capture: 0x1560
   __TEXT.__swift5_mpenum: 0x68
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__gcc_except_tab: 0x5200
-  __TEXT.__oslogstring: 0x29e97
+  __TEXT.__gcc_except_tab: 0x5214
+  __TEXT.__oslogstring: 0x29f0e
   __TEXT.__ustring: 0x1c5c
-  __TEXT.__unwind_info: 0x15c28
+  __TEXT.__unwind_info: 0x15bc4
   __TEXT.__eh_frame: 0x1078
-  __TEXT.__objc_classname: 0xd6e5
-  __TEXT.__objc_methname: 0xb1a8c
-  __TEXT.__objc_methtype: 0x1472e
-  __TEXT.__objc_stubs: 0x4fac0
+  __TEXT.__objc_classname: 0xd6e2
+  __TEXT.__objc_methname: 0xb1dde
+  __TEXT.__objc_methtype: 0x1474e
+  __TEXT.__objc_stubs: 0x4fbc0
   __DATA_CONST.__got: 0xdc0
-  __DATA_CONST.__const: 0x1b7b0
+  __DATA_CONST.__const: 0x1b7e8
   __DATA_CONST.__objc_classlist: 0x3198
   __DATA_CONST.__objc_catlist: 0x118
   __DATA_CONST.__objc_protolist: 0x4a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x89918
-  __DATA_CONST.__objc_selrefs: 0x1e828
+  __DATA_CONST.__objc_const: 0x89bd8
+  __DATA_CONST.__objc_selrefs: 0x1e8b8
   __DATA_CONST.__objc_protorefs: 0x198
   __DATA_CONST.__objc_classrefs: 0x2eb8
   __DATA_CONST.__objc_superrefs: 0x2740
   __DATA_CONST.__objc_arraydata: 0x3000
-  __AUTH_CONST.__const: 0xa6f0
+  __AUTH_CONST.__const: 0xa6d0
   __AUTH_CONST.__auth_ptr: 0xb8
   __AUTH_CONST.__objc_const: 0x2a7d0
-  __AUTH_CONST.__cfstring: 0x61040
+  __AUTH_CONST.__cfstring: 0x61240
   __AUTH_CONST.__objc_arrayobj: 0xa08
   __AUTH_CONST.__objc_intobj: 0xfc0
   __AUTH_CONST.__objc_dictobj: 0x1db0
   __AUTH_CONST.__objc_doubleobj: 0x2b0
   __AUTH_CONST.__auth_got: 0x1d30
-  __AUTH.__objc_data: 0x1a928
-  __AUTH.__data: 0x15c0
-  __DATA.__objc_ivar: 0x59dc
-  __DATA.__data: 0x5120
+  __AUTH.__objc_data: 0x1a748
+  __AUTH.__data: 0x15f0
+  __DATA.__objc_ivar: 0x5a00
+  __DATA.__data: 0x5290
   __DATA.__thread_vars: 0x18
   __DATA.__thread_bss: 0x8
   __DATA.__common: 0x1a8
-  __DATA.__bss: 0x2428
-  __DATA_DIRTY.__objc_ivar: 0x20a8
-  __DATA_DIRTY.__objc_data: 0x4b50
-  __DATA_DIRTY.__data: 0x148
-  __DATA_DIRTY.__bss: 0x1040
+  __DATA.__bss: 0x22c8
+  __DATA_DIRTY.__objc_ivar: 0x20b8
+  __DATA_DIRTY.__objc_data: 0x4d30
+  __DATA_DIRTY.__data: 0x120
+  __DATA_DIRTY.__bss: 0x1038
   __DATA_DIRTY.__common: 0x40
   SMOOTH.SMOOTH: 0xc
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 39519
-  Symbols:   110236
-  CStrings:  46043
+  Functions: 39554
+  Symbols:   110328
+  CStrings:  46091
 
Symbols:
+ -[NSDate(PKDateAdditions) isDateLessThanNDays:afterDate:]
+ -[PKPassLibrary pendingUserNotificationsWithIdentifier:completion:]
+ -[PKPassLibrary updateDate:forPendingNotificationWithIdentifier:]
+ -[PKPaymentAuthorizationDataModel praguePolicyRequired]
+ -[PKPaymentBalance expirationDate]
+ -[PKPaymentBalance isExpired]
+ -[PKPaymentBalance setExpirationDate:]
+ -[PKPaymentBalance setIsExpired:]
+ -[PKPaymentCommutePlanDetail initWithIdentifier:uniqueIdentifier:startDate:expiryDate:title:description:]
+ -[PKPaymentCommutePlanDetail setUniqueIdentifier:]
+ -[PKPaymentCommutePlanDetail uniqueIdentifier]
+ -[PKPaymentDigitalIssuanceMetadata serviceProviderLocalizedDisplayName]
+ -[PKPaymentPassAction actionUpdatedWithDictionary:localizations:]
+ -[PKPaymentPassAction initWithDictionary:localizations:]
+ -[PKPaymentPassAction serviceProviderLocalizedDisplayName]
+ -[PKPaymentPassAction setServiceProviderLocalizedDisplayName:]
+ -[PKPaymentPassActionGroup initWithDictionary:localizations:]
+ -[PKPaymentPassContent actionLocalizations]
+ -[PKPaymentPassContent setActionLocalizations:]
+ -[PKPaymentProvisioningController paymentDataProvider]
+ -[PKPaymentProvisioningController setPaymentDataProvider:]
+ -[PKPaymentRemoteContentPassActionGroupResponse initWithExistingActionGroup:data:pass:]
+ -[PKPaymentRemoteContentPassActionResponse initWithExistingAction:pass:data:]
+ -[PKPaymentSetupFieldBuiltInDateOfBirth disallowCurrentYear]
+ -[PKPaymentSetupFieldBuiltInDateOfBirth setDisallowCurrentYear:]
+ -[PKPaymentWebService _passActionWithRemoteContentPassAction:serviceProviderData:pass:completion:]
+ -[PKPaymentWebService passActionWithRemoteContentPassAction:serviceProviderData:pass:completion:]
+ -[PKPeerPaymentAccountFeatureDescriptor isSupported]
+ -[PKPeerPaymentAccountFeatureDescriptor setSupported:]
+ -[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:]
+ -[PKSecureElementPass actionLocalizations]
+ -[PKSecureElementPass contactlessActivationGroupingType]
+ -[PKSecureElementPass setContactlessActivationGroupingType:]
+ -[PKTransactionReleasedData merchantNameOverride]
+ -[PKTransactionReleasedData setMerchantNameOverride:]
+ -[PKTransitAppletCommutePlan initWithIdentifier:uniqueIdentifier:startDate:expirationDate:status:]
+ -[PKTransitAppletCommutePlan setUniqueIdentifier:]
+ -[PKTransitAppletCommutePlan uniqueIdentifier]
+ -[PKTransitAppletHistoryRecord _transactionAmountsWithBalanceLabels:planLabels:unitDictionary:]
+ -[PKTransitBalanceModel hasDeviceBoundCommutePlans]
+ -[PKTransitCommutePlan foreignReferenceIdentifiers]
+ -[PKTransitCommutePlan isDeviceBound]
+ -[PKTransitCommutePlan mutableCopyWithZone:]
+ -[PKTransitCommutePlan setIsDeviceBound:]
+ -[PKTransitCommutePlan setUniqueIdentifier:]
+ -[PKTransitCommutePlan uniqueIdentifier]
+ -[PKTransitCommutePlan updateWithCommutePlanDetail:]
+ GCC_except_table103
+ GCC_except_table119
+ GCC_except_table142
+ GCC_except_table218
+ GCC_except_table391
+ GCC_except_table448
+ GCC_except_table456
+ GCC_except_table472
+ GCC_except_table475
+ GCC_except_table496
+ GCC_except_table577
+ GCC_except_table620
+ GCC_except_table628
+ GCC_except_table70
+ _.str.802
+ _OBJC_IVAR_$_PKPaymentBalance._expirationDate
+ _OBJC_IVAR_$_PKPaymentBalance._isExpired
+ _OBJC_IVAR_$_PKPaymentCommutePlanDetail._uniqueIdentifier
+ _OBJC_IVAR_$_PKPaymentDigitalIssuanceMetadata._serviceProviderLocalizedDisplayName
+ _OBJC_IVAR_$_PKPaymentPassAction._serviceProviderLocalizedDisplayName
+ _OBJC_IVAR_$_PKPaymentProvisioningController._paymentDataProvider
+ _OBJC_IVAR_$_PKTransactionReleasedData._merchantNameOverride
+ _OBJC_IVAR_$_PKTransitAppletCommutePlan._uniqueIdentifier
+ _OBJC_IVAR_$_PKTransitBalanceModel._dynamicPlansByUniqueId
+ _OBJC_IVAR_$_PKTransitCommutePlan._isDeviceBound
+ _OBJC_IVAR_$_PKTransitCommutePlan._uniqueIdentifier
+ _PKDeviceVersionMeetsRequiredVersion
+ _PKPassKeyContactlessActivationGroupingType
+ _PKPassPaymentActionLocalizations
+ _PKPaymentDigitalIssuanceMetadataServiceProviderLocalizedDisplayNameKey
+ _PKPaymentNetworkBankAxept
+ _PKPaymentNetworkNAPAS
+ _PKURLActionRouteConnectedCards
+ _PKURLSubactionRouteTermsAndConditions
+ __MergedGlobals.33
+ __XPCActivityIdentifier
+ ___128-[PKPaymentWebService passActionWithRemoteContentPassAction:forDeviceIdentifier:passTypeIdentifier:passSerialNumber:completion:]_block_invoke
+ ___130-[PKPaymentWebService _passActionGroupIncludingAppletDataWithRemoteContentPassActionGroup:forPass:forDeviceIdentifier:completion:]_block_invoke.597
+ ___51-[PKPaymentDevice rewrapDataWithCompletionHandler:]_block_invoke.402
+ ___52-[PKSecureElement signatureForAuthToken:completion:]_block_invoke.297
+ ___52-[PKSecureElement signedPlatformDataWithCompletion:]_block_invoke.300
+ ___56-[PKPaymentPassAction initWithDictionary:localizations:]_block_invoke
+ ___56-[PKPaymentPassAction initWithDictionary:localizations:]_block_invoke_2
+ ___56-[PKPaymentWebService _handlePassListDownloadTask:data:]_block_invoke.708
+ ___56-[PKPaymentWebService _handlePassListDownloadTask:data:]_block_invoke.709
+ ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke.684
+ ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke.689
+ ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke_2.688
+ ___63-[PKPaymentWebService _nonceWithRequest:serviceURL:completion:]_block_invoke.629
+ ___65-[PKPaymentDevice _populateDeviceMetadata:withFields:completion:]_block_invoke.407
+ ___65-[PKPaymentDevice _populateDeviceMetadata:withFields:completion:]_block_invoke.410
+ ___65-[PKPaymentPassAction actionUpdatedWithDictionary:localizations:]_block_invoke
+ ___65-[PKPaymentWebService _applePayTrustPublicKeyHashWithCompletion:]_block_invoke.752
+ ___67-[PKPassLibrary pendingUserNotificationsWithIdentifier:completion:]_block_invoke
+ ___67-[PKPassLibrary pendingUserNotificationsWithIdentifier:completion:]_block_invoke_2
+ ___67-[PKPassLibrary pendingUserNotificationsWithIdentifier:completion:]_block_invoke_3
+ ___67-[PKPassLibrary pendingUserNotificationsWithIdentifier:completion:]_block_invoke_4
+ ___68-[PKPaymentWebService retrieveMerchantTokensWithRequest:completion:]_block_invoke.618
+ ___68-[PKSecureElement markAppletsWithIdentifiersForDeletion:completion:]_block_invoke.290
+ ___70-[PKSecureElement signChallenge:forPaymentApplication:withCompletion:]_block_invoke.292
+ ___73-[PKSecureElement peerPaymentEnrollmentDataWithAlternateDSID:completion:]_block_invoke.324
+ ___73-[PKSecureElement peerPaymentEnrollmentDataWithAlternateDSID:completion:]_block_invoke_2.325
+ ___78-[PKPaymentWebService _passActionWithRemoteContentPassAction:pass:completion:]_block_invoke
+ ___80-[PKPaymentWebService _registerIfNeededWithResponse:task:isRedirect:completion:]_block_invoke.749
+ ___80-[PKPaymentWebService _registerIfNeededWithResponse:task:isRedirect:completion:]_block_invoke.751
+ ___83-[PKPaymentWebService _performRewrapRequest:serviceURL:responseHandler:completion:]_block_invoke.654
+ ___87-[PKPaymentWebService _handleRetryAfterRegisterWithRequest:response:completionHandler:]_block_invoke.721
+ ___92-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:]_block_invoke
+ ___92-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:]_block_invoke.284
+ ___92-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:]_block_invoke.285
+ ___92-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:]_block_invoke.287
+ ___92-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:]_block_invoke_2
+ ___92-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:]_block_invoke_2.286
+ ___93-[PKSecureElement generateTransactionKeyWithReaderIdentifier:readerPublicKey:withCompletion:]_block_invoke.301
+ ___96-[PKPaymentWebService _backgroundDownloadCloudStoreAssetsforItem:cloudStoreCoordinatorDelegate:]_block_invoke.705
+ ___96-[PKPaymentWebService _backgroundDownloadCloudStoreAssetsforItem:cloudStoreCoordinatorDelegate:]_block_invoke_2.706
+ ___Block_byref_object_copy_.520
+ ___Block_byref_object_dispose_.521
+ ___block_descriptor_49_e8_32s40bs_e51_v24?0"NFSecureElementManagerSession"8"NSError"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e34_v24?0"NSDictionary"8"NSError"16ls56l8s32l8s40l8s48l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs_e34_v24?0"NSDictionary"8"NSError"16ls80l8s32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.1068
+ ___block_literal_global.1073
+ ___block_literal_global.1077
+ ___block_literal_global.1080
+ ___block_literal_global.1083
+ ___block_literal_global.1092
+ ___block_literal_global.1096
+ ___block_literal_global.1106
+ ___block_literal_global.1196
+ ___block_literal_global.1200
+ ___block_literal_global.1268
+ ___block_literal_global.1270
+ ___block_literal_global.1273
+ ___block_literal_global.1331
+ ___block_literal_global.1333
+ ___block_literal_global.1342
+ ___block_literal_global.1356
+ ___block_literal_global.1358
+ ___block_literal_global.1363
+ ___block_literal_global.1377
+ ___block_literal_global.1386
+ ___block_literal_global.1389
+ ___block_literal_global.1391
+ ___block_literal_global.1394
+ ___block_literal_global.557
+ ___block_literal_global.616
+ ___block_literal_global.621
+ ___block_literal_global.627
+ ___block_literal_global.632
+ ___block_literal_global.637
+ ___block_literal_global.645
+ ___block_literal_global.647
+ ___block_literal_global.649
+ ___block_literal_global.652
+ ___block_literal_global.654
+ ___block_literal_global.686
+ ___block_literal_global.692
+ ___block_literal_global.695
+ ___block_literal_global.697
+ ___block_literal_global.711
+ ___block_literal_global.755
+ ___block_literal_global.783
+ ___block_literal_global.835
+ ___block_literal_global.837
+ ___block_literal_global.842
+ ___block_literal_global.844
+ ___block_literal_global.846
+ ___block_literal_global.848
+ ___block_literal_global.850
+ ___block_literal_global.876
+ ___block_literal_global.890
+ ___block_literal_global.892
+ ___block_literal_global.897
+ ___block_literal_global.905
+ ___block_literal_global.908
+ ___block_literal_global.939
+ ___block_literal_global.949
+ ___block_literal_global.962
+ ___block_literal_global.992
+ __unnamed_array_storage.1092
+ __unnamed_array_storage.646
+ __unnamed_array_storage.647
+ __unnamed_array_storage.651
+ __unnamed_array_storage.662
+ __unnamed_array_storage.663
+ __unnamed_array_storage.667
+ __unnamed_array_storage.713
+ __unnamed_array_storage.714
+ __unnamed_array_storage.718
+ _objc_msgSend$_passActionWithRemoteContentPassAction:serviceProviderData:pass:completion:
+ _objc_msgSend$_transactionAmountsWithBalanceLabels:planLabels:unitDictionary:
+ _objc_msgSend$actionLocalizations
+ _objc_msgSend$actionUpdatedWithDictionary:localizations:
+ _objc_msgSend$deleteAllAppletsOfType:queueConnection:error:
+ _objc_msgSend$initWithDictionary:localizations:
+ _objc_msgSend$initWithExistingAction:pass:data:
+ _objc_msgSend$initWithExistingActionGroup:data:pass:
+ _objc_msgSend$isDeviceBound
+ _objc_msgSend$markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:
+ _objc_msgSend$pendingUserNotificationsWithIdentifier:completion:
+ _objc_msgSend$setActionLocalizations:
+ _objc_msgSend$setContactlessActivationGroupingType:
+ _objc_msgSend$setIsDeviceBound:
+ _objc_msgSend$updateDate:forPendingNotificationWithIdentifier:
+ _objc_msgSend$updateWithCommutePlanDetail:
- -[PKPassLibrary pendingUserNotificationsWithCompletion:]
- -[PKPaymentCommutePlanDetail initWithIdentifier:startDate:expiryDate:title:description:]
- -[PKPaymentPassAction actionUpdatedWithDictionary:]
- -[PKPaymentPassAction initWithDictionary:]
- -[PKPaymentPassActionGroup initWithDictionary:]
- -[PKPaymentRemoteContentPassActionGroupResponse initWithExistingActionGroup:data:]
- -[PKPaymentRemoteContentPassActionResponse initWithExistingAction:data:]
- -[PKPaymentWebService _passActionWithRemoteContentPassAction:forDeviceIdentifier:passTypeIdentifier:passSerialNumber:completion:]
- -[PKPaymentWebService _passActionWithRemoteContentPassAction:serviceProviderData:forDeviceIdentifier:passTypeIdentifier:passSerialNumber:completion:]
- -[PKPaymentWebService passActionWithRemoteContentPassAction:serviceProviderData:forDeviceIdentifier:passTypeIdentifier:passSerialNumber:completion:]
- -[PKSecureElementPass setPaymentOptionSelectable:]
- -[PKTransitAppletCommutePlan initWithIdentifier:startDate:expirationDate:status:]
- -[PKTransitAppletHistoryRecord _transactionAmountsWithBalanceLabels:unitDictionary:]
- GCC_except_table102
- GCC_except_table117
- GCC_except_table140
- GCC_except_table216
- GCC_except_table447
- GCC_except_table455
- GCC_except_table457
- GCC_except_table471
- GCC_except_table474
- GCC_except_table477
- GCC_except_table495
- GCC_except_table578
- GCC_except_table621
- GCC_except_table629
- _.str.792
- _OBJC_IVAR_$_PKPaymentSetupFieldBuiltInDateOfBirth._minimumAge
- _OBJC_IVAR_$_PKTransitBalanceModel._dynamicPlansById
- __MergedGlobals.31
- ___129-[PKPaymentWebService _passActionWithRemoteContentPassAction:forDeviceIdentifier:passTypeIdentifier:passSerialNumber:completion:]_block_invoke
- ___130-[PKPaymentWebService _passActionGroupIncludingAppletDataWithRemoteContentPassActionGroup:forPass:forDeviceIdentifier:completion:]_block_invoke.600
- ___42-[PKPaymentPassAction initWithDictionary:]_block_invoke
- ___49-[PKPaymentPassAction initWithDictionary:bundle:]_block_invoke
- ___51-[PKPaymentDevice rewrapDataWithCompletionHandler:]_block_invoke.403
- ___51-[PKPaymentPassAction actionUpdatedWithDictionary:]_block_invoke
- ___52-[PKSecureElement signatureForAuthToken:completion:]_block_invoke.296
- ___52-[PKSecureElement signedPlatformDataWithCompletion:]_block_invoke.299
- ___56-[PKPassLibrary pendingUserNotificationsWithCompletion:]_block_invoke
- ___56-[PKPassLibrary pendingUserNotificationsWithCompletion:]_block_invoke_2
- ___56-[PKPassLibrary pendingUserNotificationsWithCompletion:]_block_invoke_3
- ___56-[PKPassLibrary pendingUserNotificationsWithCompletion:]_block_invoke_4
- ___56-[PKPaymentWebService _handlePassListDownloadTask:data:]_block_invoke.711
- ___56-[PKPaymentWebService _handlePassListDownloadTask:data:]_block_invoke.712
- ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke.692
- ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke.693
- ___60-[PKPaymentWebService URLSession:task:didCompleteWithError:]_block_invoke_2.691
- ___63-[PKPaymentWebService _nonceWithRequest:serviceURL:completion:]_block_invoke.632
- ___65-[PKPaymentDevice _populateDeviceMetadata:withFields:completion:]_block_invoke.408
- ___65-[PKPaymentDevice _populateDeviceMetadata:withFields:completion:]_block_invoke.413
- ___65-[PKPaymentWebService _applePayTrustPublicKeyHashWithCompletion:]_block_invoke.755
- ___67-[PKPaymentDevice registrationDataWithAuthToken:completionHandler:]_block_invoke.391
- ___68-[PKPaymentWebService retrieveMerchantTokensWithRequest:completion:]_block_invoke.621
- ___68-[PKSecureElement markAppletsWithIdentifiersForDeletion:completion:]_block_invoke.289
- ___70-[PKSecureElement signChallenge:forPaymentApplication:withCompletion:]_block_invoke.291
- ___73-[PKSecureElement peerPaymentEnrollmentDataWithAlternateDSID:completion:]_block_invoke.323
- ___73-[PKSecureElement peerPaymentEnrollmentDataWithAlternateDSID:completion:]_block_invoke_2.324
- ___80-[PKPaymentWebService _registerIfNeededWithResponse:task:isRedirect:completion:]_block_invoke.752
- ___80-[PKPaymentWebService _registerIfNeededWithResponse:task:isRedirect:completion:]_block_invoke.754
- ___81-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:completion:]_block_invoke.283
- ___81-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:completion:]_block_invoke.284
- ___81-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:completion:]_block_invoke.286
- ___81-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:completion:]_block_invoke_2
- ___81-[PKSecureElement markAllAppletsForDeletionWithExternalAuthorization:completion:]_block_invoke_2.285
- ___83-[PKPaymentWebService _performRewrapRequest:serviceURL:responseHandler:completion:]_block_invoke.657
- ___87-[PKPaymentWebService _handleRetryAfterRegisterWithRequest:response:completionHandler:]_block_invoke.724
- ___93-[PKSecureElement generateTransactionKeyWithReaderIdentifier:readerPublicKey:withCompletion:]_block_invoke.300
- ___96-[PKPaymentWebService _backgroundDownloadCloudStoreAssetsforItem:cloudStoreCoordinatorDelegate:]_block_invoke.708
- ___96-[PKPaymentWebService _backgroundDownloadCloudStoreAssetsforItem:cloudStoreCoordinatorDelegate:]_block_invoke_2.709
- ___Block_byref_object_copy_.519
- ___Block_byref_object_dispose_.520
- ___PKRootVolumeIsBootVolume_block_invoke
- ___PKRootVolumeIsBootVolume_block_invoke_2
- ___block_descriptor_56_e8_32s40bs48bs_e30_v28?0B8"NSData"12"NSData"20ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e34_v24?0"NSDictionary"8"NSError"16ls64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_88_e8_32s40s48s56s64s72bs_e34_v24?0"NSDictionary"8"NSError"16ls72l8s32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.1048
- ___block_literal_global.1053
- ___block_literal_global.1057
- ___block_literal_global.1063
- ___block_literal_global.1072
- ___block_literal_global.1086
- ___block_literal_global.1100
- ___block_literal_global.1190
- ___block_literal_global.1194
- ___block_literal_global.1248
- ___block_literal_global.1250
- ___block_literal_global.1311
- ___block_literal_global.1313
- ___block_literal_global.1318
- ___block_literal_global.1322
- ___block_literal_global.1336
- ___block_literal_global.1343
- ___block_literal_global.1357
- ___block_literal_global.1366
- ___block_literal_global.1369
- ___block_literal_global.1371
- ___block_literal_global.1374
- ___block_literal_global.402
- ___block_literal_global.556
- ___block_literal_global.604
- ___block_literal_global.609
- ___block_literal_global.615
- ___block_literal_global.620
- ___block_literal_global.625
- ___block_literal_global.630
- ___block_literal_global.635
- ___block_literal_global.640
- ___block_literal_global.644
- ___block_literal_global.648
- ___block_literal_global.651
- ___block_literal_global.680
- ___block_literal_global.683
- ___block_literal_global.685
- ___block_literal_global.687
- ___block_literal_global.689
- ___block_literal_global.714
- ___block_literal_global.753
- ___block_literal_global.781
- ___block_literal_global.810
- ___block_literal_global.825
- ___block_literal_global.827
- ___block_literal_global.830
- ___block_literal_global.832
- ___block_literal_global.834
- ___block_literal_global.836
- ___block_literal_global.838
- ___block_literal_global.847
- ___block_literal_global.856
- ___block_literal_global.870
- ___block_literal_global.872
- ___block_literal_global.877
- ___block_literal_global.885
- ___block_literal_global.888
- ___block_literal_global.904
- ___block_literal_global.909
- ___block_literal_global.914
- ___block_literal_global.919
- ___block_literal_global.942
- ___block_literal_global.972
- __unnamed_array_storage.1087
- __unnamed_array_storage.649
- __unnamed_array_storage.653
- __unnamed_array_storage.654
- __unnamed_array_storage.665
- __unnamed_array_storage.669
- __unnamed_array_storage.670
- __unnamed_array_storage.716
- __unnamed_array_storage.720
- __unnamed_array_storage.721
- _objc_msgSend$_passActionWithRemoteContentPassAction:forDeviceIdentifier:passTypeIdentifier:passSerialNumber:completion:
- _objc_msgSend$_passActionWithRemoteContentPassAction:serviceProviderData:forDeviceIdentifier:passTypeIdentifier:passSerialNumber:completion:
- _objc_msgSend$_transactionAmountsWithBalanceLabels:unitDictionary:
- _objc_msgSend$actionUpdatedWithDictionary:
- _objc_msgSend$initWithExistingAction:data:
- _objc_msgSend$initWithExistingActionGroup:data:
- _objc_msgSend$pendingUserNotificationsWithCompletion:
- _objc_msgSend$setPaymentOptionSelectable:
CStrings:
+ "\x01\x15\x15"
+ "\x05\x11\x19\x15\x15\x15%"
+ "\x06\x13\x13:1\x14\x13\x11\x11\x1f\x02"
+ "\x13\x16"
+ "\x1e\x17"
+ "\"\x15\x13\x1f\x0e"
+ ", initiative: %@"
+ "Applet Plan: %@ %@ %@ %@ %@"
+ "BankAxept"
+ "CommutePlanUniqueIdentifier"
+ "Count Plan: %@ %@ %ld %@ %@ %lu"
+ "NAPAS"
+ "NETWORK_NAME_BANKAXEPT"
+ "NETWORK_NAME_BANKAXEPT_CARD_NAME"
+ "NETWORK_NAME_NAPAS"
+ "NETWORK_NAME_NAPAS_CARD_NAME"
+ "PKPaymentDevice: se-sep sync failed!!! Proceeding with registration..."
+ "T@\"<PKPaymentDataProvider>\",&,N,V_paymentDataProvider"
+ "T@\"NSDictionary\",C,N,V_actionLocalizations"
+ "T@\"NSString\",&,N,V_merchantNameOverride"
+ "T@\"NSString\",C,N,V_serviceProviderLocalizedDisplayName"
+ "T@\"NSString\",R,C,N,V_serviceProviderLocalizedDisplayName"
+ "TB,N,V_disallowCurrentYear"
+ "TB,N,V_isDeviceBound"
+ "TB,N,V_isExpired"
+ "TQ,N,V_contactlessActivationGroupingType"
+ "Timed Plan: %@ %@ %@ %@ %@ %@ %lu"
+ "UniqueIdentifier"
+ "XPC activity identifiers cannot be longer than 128 characters"
+ "XPC activity identifiers cannot be longer than 128 characters\n%@"
+ "_actionLocalizations"
+ "_contactlessActivationGroupingType"
+ "_disallowCurrentYear"
+ "_dynamicPlansByUniqueId"
+ "_isDeviceBound"
+ "_isExpired"
+ "_passActionWithRemoteContentPassAction:serviceProviderData:pass:completion:"
+ "_serviceProviderLocalizedDisplayName"
+ "_transactionAmountsWithBalanceLabels:planLabels:unitDictionary:"
+ "actionLocalizations"
+ "actionUpdatedWithDictionary:localizations:"
+ "applePayLaterAvailability: %@, "
+ "connected-cards"
+ "contactlessActivationGroupingType"
+ "deleteAllAppletsOfType:queueConnection:error:"
+ "disallowCurrentYear"
+ "hasDeviceBoundCommutePlans"
+ "initWithDictionary:localizations:"
+ "initWithExistingAction:pass:data:"
+ "initWithExistingActionGroup:data:pass:"
+ "initWithIdentifier:uniqueIdentifier:startDate:expirationDate:status:"
+ "initWithIdentifier:uniqueIdentifier:startDate:expiryDate:title:description:"
+ "isDateLessThanNDays:afterDate:"
+ "isDeviceBound"
+ "markAllAppletsForDeletionWithExternalAuthorization:obliterate:completion:"
+ "merchantNameOverride: '%@'; "
+ "passActionWithRemoteContentPassAction:serviceProviderData:pass:completion:"
+ "pendingUserNotificationsWithIdentifier:completion:"
+ "praguePolicyRequired"
+ "serviceProviderLocalizedDisplayName"
+ "setActionLocalizations:"
+ "setContactlessActivationGroupingType:"
+ "setDisallowCurrentYear:"
+ "setIsDeviceBound:"
+ "setIsExpired:"
+ "setPaymentDataProvider:"
+ "setServiceProviderLocalizedDisplayName:"
+ "supported: '%@'; "
+ "terms-and-conditions"
+ "updateDate:forPendingNotificationWithIdentifier:"
+ "updateWithCommutePlanDetail:"
+ "v32@0:8@\"NSDate\"16@\"NSString\"24"
- "\x01\x14\x15"
- "\x05\x11\x19\x15\x14\x15%"
- "\x06\x13\x13:1\x14\x12\x11\x11\x1f\x02"
- "\x13\x15"
- "\x1d\x17"
- "\x1f\x01"
- "\"\x15\x1f\x0f\x02"
- "Applet Plan: %@ %@ %@ %@"
- "Count Plan: %@ %ld %@ %@ %lu"
- "Error: Action remote content requires applet data."
- "PKPaymentDevice: se-sep sync failed - declining to generate registration data."
- "TB,N,GisPaymentOptionSelectable,V_paymentOptionSelectable"
- "Timed Plan: %@ %@ %@ %@ %@ %lu"
- "_dynamicPlansById"
- "_passActionWithRemoteContentPassAction:forDeviceIdentifier:passTypeIdentifier:passSerialNumber:completion:"
- "_passActionWithRemoteContentPassAction:serviceProviderData:forDeviceIdentifier:passTypeIdentifier:passSerialNumber:completion:"
- "_paymentOptionSelectable"
- "_transactionAmountsWithBalanceLabels:unitDictionary:"
- "actionUpdatedWithDictionary:"
- "applePayLaterAvailability: %@"
- "initWithExistingAction:data:"
- "initWithExistingActionGroup:data:"
- "initWithIdentifier:startDate:expirationDate:status:"
- "initWithIdentifier:startDate:expiryDate:title:description:"
- "initiative: %@"
- "passActionWithRemoteContentPassAction:serviceProviderData:forDeviceIdentifier:passTypeIdentifier:passSerialNumber:completion:"
- "paymentOptionSelectable"
- "pendingUserNotificationsWithCompletion:"
- "setPaymentOptionSelectable:"

```
