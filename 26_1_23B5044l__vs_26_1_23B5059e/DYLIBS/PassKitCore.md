## PassKitCore

> `/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore`

```diff

-1640.2.0.0.0
-  __TEXT.__text: 0x7c3cc4
+1642.2.4.0.0
+  __TEXT.__text: 0x7c4f04
   __TEXT.__auth_stubs: 0x4a40
-  __TEXT.__objc_methlist: 0x6c768
+  __TEXT.__objc_methlist: 0x6c790
   __TEXT.__const: 0x23be8
-  __TEXT.__cstring: 0x68a62
-  __TEXT.__swift5_typeref: 0x593a
-  __TEXT.__constg_swiftt: 0x4e2c
+  __TEXT.__cstring: 0x68d33
+  __TEXT.__swift5_typeref: 0x594a
+  __TEXT.__constg_swiftt: 0x4e34
   __TEXT.__swift5_reflstr: 0x42dd
   __TEXT.__swift5_fieldmd: 0x51cc
   __TEXT.__swift5_builtin: 0x3c0

   __TEXT.__swift5_proto: 0xc94
   __TEXT.__swift5_types: 0x524
   __TEXT.__swift5_capture: 0x3ddc
-  __TEXT.__oslogstring: 0x34af9
+  __TEXT.__oslogstring: 0x34c87
   __TEXT.__swift_as_entry: 0xa8
   __TEXT.__swift_as_ret: 0xa8
   __TEXT.__swift5_protos: 0x40

   __TEXT.__swift5_types2: 0x4
   __TEXT.__gcc_except_tab: 0x76a4
   __TEXT.__ustring: 0x1e7a
-  __TEXT.__unwind_info: 0x1b830
+  __TEXT.__unwind_info: 0x1b880
   __TEXT.__eh_frame: 0x4b30
-  __TEXT.__objc_classname: 0xf8ec
-  __TEXT.__objc_methname: 0xcbcad
-  __TEXT.__objc_methtype: 0x17901
+  __TEXT.__objc_classname: 0xf8ef
+  __TEXT.__objc_methname: 0xcbd9a
+  __TEXT.__objc_methtype: 0x178f5
   __TEXT.__objc_stubs: 0x59e80
   __DATA_CONST.__got: 0x49b0
-  __DATA_CONST.__const: 0x21090
+  __DATA_CONST.__const: 0x21178
   __DATA_CONST.__objc_classlist: 0x3aa0
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_protolist: 0x590
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23350
+  __DATA_CONST.__objc_selrefs: 0x23370
   __DATA_CONST.__objc_protorefs: 0x250
   __DATA_CONST.__objc_superrefs: 0x2f10
-  __DATA_CONST.__objc_arraydata: 0x27b8
+  __DATA_CONST.__objc_arraydata: 0x27d8
   __AUTH_CONST.__auth_got: 0x2530
-  __AUTH_CONST.__const: 0x1e7b8
-  __AUTH_CONST.__cfstring: 0x70f60
-  __AUTH_CONST.__objc_const: 0xc3c70
-  __AUTH_CONST.__objc_arrayobj: 0xd20
+  __AUTH_CONST.__const: 0x1e7f8
+  __AUTH_CONST.__cfstring: 0x71220
+  __AUTH_CONST.__objc_const: 0xc3c60
+  __AUTH_CONST.__objc_arrayobj: 0xd38
   __AUTH_CONST.__objc_intobj: 0x1080
   __AUTH_CONST.__objc_dictobj: 0x1518
   __AUTH_CONST.__objc_doubleobj: 0x2b0
-  __AUTH.__objc_data: 0x20580
+  __AUTH.__objc_data: 0x20588
   __AUTH.__data: 0x3768
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0x6478
-  __DATA.__data: 0x7d70
-  __DATA.__bss: 0x18728
+  __DATA.__objc_ivar: 0x647c
+  __DATA.__data: 0x7d90
+  __DATA.__bss: 0x18270
   __DATA.__common: 0xc00
-  __DATA_DIRTY.__objc_ivar: 0x25cc
+  __DATA_DIRTY.__objc_ivar: 0x25c8
   __DATA_DIRTY.__objc_data: 0x57a8
   __DATA_DIRTY.__data: 0x160
-  __DATA_DIRTY.__bss: 0xcc0
+  __DATA_DIRTY.__bss: 0x1180
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1212848A-AB34-328D-AD5C-C1609B690BE4
-  Functions: 49530
-  Symbols:   128171
-  CStrings:  67334
+  UUID: 3FFB6A45-9230-3A06-8C7F-CC9AC7CA42C8
+  Functions: 49553
+  Symbols:   128216
+  CStrings:  67394
 
Symbols:
+ +[PKCoreSpotlightUtilities _allPassFields:]
+ +[PKCoreSpotlightUtilities searchableItemForTransaction:passUniqueID:passLocalizedDescription:regions:tags:keywords:imageGenerator:contactResolver:completion:]
+ +[PKCoreSpotlightUtilities textContentAttributeForTransaction:passLocalizedDescription:]
+ +[PKPassEntitlementsComposer isOwnerPass:]
+ -[PKDiscoveryCallToAction backgroundBlurStyle]
+ -[PKDynamicProvisioningPageContent requiresExplicitPrimaryAction]
+ -[PKDynamicProvisioningPageContent setRequiresExplicitPrimaryAction:]
+ -[PKMobileAssetManager _purgeAssets:completion:]
+ -[PKMobileAssetManager _purgeCashStickers]
+ -[PKMobileAssetManager _queryForCashStickers]
+ -[PKMobileAssetManager cachedCashStickerBundle]
+ -[PKMobileAssetManager hasCashStickers]
+ -[PKMobileAssetManager updateCashStickersIfNecessary]
+ -[PKPassUpcomingPassInformationImageManifestItem SHA256]
+ -[PKPassUpcomingPassInformationImageManifestItem _createValidatedImageFromData:error:]
+ -[PKPaymentDefaultDataProvider spendingCategoryTransactionGroupsForRequest:gregorianCalendarUnit:]
+ -[PKPaymentDefaultDataProvider transactionCountByPeriodForRequest:gregorianCalendarUnit:includePurchaseTotal:completion:]
+ -[PKPaymentOffersController _handleOffersChangedForPassUniqueID:didRemove:]
+ -[PKPaymentService spendingCategoryTransactionGroupsForRequest:gregorianCalendarUnit:]
+ -[PKPaymentService transactionCountByPeriodForRequest:gregorianCalendarUnit:includePurchaseTotal:completion:]
+ -[PKPaymentWebServiceConfiguration cashStickersAssetPrefetchTimeIntervalForRegion:]
+ -[PKSecureElementPass setAccessType:]
+ GCC_except_table112
+ GCC_except_table156
+ GCC_except_table183
+ GCC_except_table237
+ GCC_except_table388
+ GCC_except_table411
+ GCC_except_table414
+ GCC_except_table416
+ GCC_except_table418
+ GCC_except_table420
+ GCC_except_table477
+ GCC_except_table528
+ GCC_except_table530
+ GCC_except_table534
+ GCC_except_table538
+ GCC_except_table553
+ GCC_except_table740
+ GCC_except_table858
+ _OBJC_IVAR_$_PKDiscoveryCallToAction._backgroundBlurStyle
+ _OBJC_IVAR_$_PKDynamicProvisioningPageContent._requiresExplicitPrimaryAction
+ _OBJC_IVAR_$_PKPassUpcomingPassInformationImageManifestItem._SHA256
+ _OBJC_IVAR_$_PKProvisioningAnalyticsSession._provisioningSubjectHandle
+ _PKAggDKeyApplePayButtonErrorType
+ _PKAggDKeyApplePayButtonErrorTypeNoPassImageReceived
+ _PKAnalyticsReportCarKeyAddToWalletPageTag
+ _PKAnalyticsReportCarKeyAddingKeyPageTag
+ _PKAnalyticsReportCarKeyAuthenticationPageTag
+ _PKAnalyticsReportCarKeyCarPairingCodePageTag
+ _PKAnalyticsReportCarKeyConfirmOsloPageTag
+ _PKAnalyticsReportCarKeyUsingCarKeysPageTag
+ _PKAnalyticsReportViewOtherProvidersTag
+ _PKAnalyticsSubjectAccessActivitySignals
+ _PKAppleCashMessagesStickerExtensionVisibilityChangedNotification
+ _PKAppleCashReportMessagesStickerExtensionVisibilityChanged
+ _PKAppleCashStickerPackIsEligibleForDownload
+ _PKAppleCashStickerPackIsVisible
+ _PKDiscoveryCardBlurStyleFromString
+ _PKIsCarKeyPass
+ _PKMobileAssetFeatureCashStickersAssets
+ _PKMobileAssetPrefetchCashStickersAssetsActivityIdentifier
+ _PKPeerPaymentSetIsSetup
+ _PKSecureElementPassAccessType
+ _PKURLActionRouteSharePass
+ _PKURLActionRouteViewPassShares
+ _PKUserNotificationActionRoutePeerPaymentSendOrRequest
+ __OBJC_$_CLASS_METHODS_PKPassEntitlementsComposer
+ ___104-[PKMobileAssetManager dynamicAssetWithIdentifier:mappedIdentifierPrefix:parameters:timeout:completion:]_block_invoke.402
+ ___104-[PKMobileAssetManager dynamicAssetWithIdentifier:mappedIdentifierPrefix:parameters:timeout:completion:]_block_invoke.403
+ ___109-[PKPaymentService transactionCountByPeriodForRequest:gregorianCalendarUnit:includePurchaseTotal:completion:]_block_invoke
+ ___109-[PKPaymentService transactionCountByPeriodForRequest:gregorianCalendarUnit:includePurchaseTotal:completion:]_block_invoke.150
+ ___109-[PKPaymentService transactionCountByPeriodForRequest:gregorianCalendarUnit:includePurchaseTotal:completion:]_block_invoke_2
+ ___109-[PKPaymentService transactionCountByPeriodForRequest:gregorianCalendarUnit:includePurchaseTotal:completion:]_block_invoke_3
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.454
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.456
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.458
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.459
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke_2.455
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke_2.457
+ ___159+[PKCoreSpotlightUtilities searchableItemForTransaction:passUniqueID:passLocalizedDescription:regions:tags:keywords:imageGenerator:contactResolver:completion:]_block_invoke
+ ___159+[PKCoreSpotlightUtilities searchableItemForTransaction:passUniqueID:passLocalizedDescription:regions:tags:keywords:imageGenerator:contactResolver:completion:]_block_invoke_2
+ ___159+[PKCoreSpotlightUtilities searchableItemForTransaction:passUniqueID:passLocalizedDescription:regions:tags:keywords:imageGenerator:contactResolver:completion:]_block_invoke_3
+ ___159+[PKCoreSpotlightUtilities searchableItemForTransaction:passUniqueID:passLocalizedDescription:regions:tags:keywords:imageGenerator:contactResolver:completion:]_block_invoke_4
+ ___42-[PKMobileAssetManager _purgeCashStickers]_block_invoke
+ ___43+[PKCoreSpotlightUtilities _allPassFields:]_block_invoke
+ ___48-[PKMobileAssetManager _purgeAssets:completion:]_block_invoke
+ ___48-[PKMobileAssetManager _purgeAssets:completion:]_block_invoke.461
+ ___48-[PKMobileAssetManager _purgeAssets:completion:]_block_invoke_2
+ ___53-[PKMobileAssetManager updateCashStickersIfNecessary]_block_invoke
+ ___70-[PKMobileAssetManager _downloadPrefetchableAssetsForType:completion:]_block_invoke.429
+ ___70-[PKMobileAssetManager _downloadPrefetchableAssetsForType:completion:]_block_invoke.431
+ ___70-[PKMobileAssetManager _downloadPrefetchableAssetsForType:completion:]_block_invoke.434
+ ___74-[PKMobileAssetManager _downloadAsset:isDiscretionary:timeout:completion:]_block_invoke.466
+ ___75-[PKPaymentOffersController _handleOffersChangedForPassUniqueID:didRemove:]_block_invoke
+ ___75-[PKPaymentOffersController _handleOffersChangedForPassUniqueID:didRemove:]_block_invoke_2
+ ___80-[PKMobileAssetManager performScheduledActivityWithIdentifier:activityCriteria:]_block_invoke.444
+ ___86-[PKPassUpcomingPassInformationImageManifestItem _createValidatedImageFromData:error:]_block_invoke
+ ___86-[PKPaymentService spendingCategoryTransactionGroupsForRequest:gregorianCalendarUnit:]_block_invoke
+ ___97+[PKCoreSpotlightUtilities searchableItemForPass:passTiles:passKitServicesXPCService:completion:]_block_invoke.280
+ ___PKAppleCashReportMessagesStickerExtensionVisibilityChanged_block_invoke
+ ___PKPeerPaymentProcessMessageWithDataURLAndProperties_block_invoke.240
+ ___block_descriptor_40_e17_B16?0"NSError"8l
+ ___block_descriptor_40_e8_32bs_e30_v28?0B812"<PKCancelable>"20ls32l8
+ ___block_descriptor_41_e8_32s_e8_v12?0B8ls32l8
+ ___block_literal_global.128
+ ___block_literal_global.234
+ ___block_literal_global.399
+ ___block_literal_global.443
+ ___block_literal_global.534
+ _block_copy_helper.54
+ _block_descriptor.56
+ _block_destroy_helper.55
+ _objc_msgSend$_allPassFields:
+ _objc_msgSend$_createValidatedImageFromData:error:
+ _objc_msgSend$_handleOffersChangedForPassUniqueID:didRemove:
+ _objc_msgSend$_purgeAssets:completion:
+ _objc_msgSend$_purgeCashStickers
+ _objc_msgSend$_queryForCashStickers
+ _objc_msgSend$cachedCashStickerBundle
+ _objc_msgSend$hasCashStickers
+ _objc_msgSend$setAccessType:
+ _objc_msgSend$spendingCategoryTransactionGroupsForRequest:gregorianCalendarUnit:
+ _objc_msgSend$spendingCategoryTransactionGroupsForRequest:gregorianCalendarUnit:completion:
+ _objc_msgSend$textContentAttributeForTransaction:passLocalizedDescription:
+ _objc_msgSend$transactionCountByPeriodForRequest:gregorianCalendarUnit:includePurchaseTotal:completion:
+ _objc_msgSend$updateCashStickersIfNecessary
+ _symbolic So20PKFPANCardDescriptorC
+ _symbolic So24PKAutoFillCardCredentialC
- +[PKCoreSpotlightUtilities _extraDataAttributeForPass:]
- +[PKCoreSpotlightUtilities searchableItemForTransaction:pass:regions:tags:keywords:imageGenerator:contactResolver:completion:]
- +[PKCoreSpotlightUtilities textContentAttributeForTransaction:pass:]
- +[PKProtobufPaymentRequest thumbnailImagesType]
- -[PKPassUpcomingPassInformationImageManifestItem SHA256Hex]
- -[PKPaymentDefaultDataProvider spendingCategoryTransactionGroupsForRequest:byCalendarUnit:]
- -[PKPaymentDefaultDataProvider transactionCountByPeriodForRequest:calendar:calendarUnit:includePurchaseTotal:completion:]
- -[PKPaymentOffersController _handleOffersChangedForPassUniqueID:]
- -[PKPaymentPassContent accessType]
- -[PKPaymentPassContent setAccessType:]
- -[PKPaymentRequest setThumbnailImages:]
- -[PKPaymentRequest thumbnailImages]
- -[PKPaymentService spendingCategoryTransactionGroupsForRequest:byCalendarUnit:]
- -[PKProtobufPaymentRequest addThumbnailImages:]
- -[PKProtobufPaymentRequest clearThumbnailImages]
- -[PKProtobufPaymentRequest setThumbnailImages:]
- -[PKProtobufPaymentRequest thumbnailImagesAtIndex:]
- -[PKProtobufPaymentRequest thumbnailImagesCount]
- -[PKProtobufPaymentRequest thumbnailImages]
- GCC_except_table182
- GCC_except_table236
- GCC_except_table238
- GCC_except_table252
- GCC_except_table387
- GCC_except_table410
- GCC_except_table413
- GCC_except_table415
- GCC_except_table417
- GCC_except_table419
- GCC_except_table476
- GCC_except_table527
- GCC_except_table529
- GCC_except_table533
- GCC_except_table537
- GCC_except_table552
- GCC_except_table739
- GCC_except_table857
- _OBJC_IVAR_$_PKPassUpcomingPassInformationImageManifestItem._SHA256Hex
- _OBJC_IVAR_$_PKPaymentRequest._thumbnailImages
- _OBJC_IVAR_$_PKProvisioningAnalyticsSession._defaultSubjectHandle
- _PKAnalyticsReportEventTypeProvisioningProgress
- _PKPaymentRequestThumbnailImagesKey
- _PPKAggDKeyApplePayButtonErrorType
- _PPKAggDKeyApplePayButtonErrorTypeNoPassImageReceived
- ___101-[PKPaymentService transactionCountByPeriodForRequest:calendar:unit:includePurchaseTotal:completion:]_block_invoke
- ___101-[PKPaymentService transactionCountByPeriodForRequest:calendar:unit:includePurchaseTotal:completion:]_block_invoke.150
- ___101-[PKPaymentService transactionCountByPeriodForRequest:calendar:unit:includePurchaseTotal:completion:]_block_invoke_2
- ___101-[PKPaymentService transactionCountByPeriodForRequest:calendar:unit:includePurchaseTotal:completion:]_block_invoke_3
- ___104-[PKMobileAssetManager dynamicAssetWithIdentifier:mappedIdentifierPrefix:parameters:timeout:completion:]_block_invoke.396
- ___104-[PKMobileAssetManager dynamicAssetWithIdentifier:mappedIdentifierPrefix:parameters:timeout:completion:]_block_invoke.397
- ___126+[PKCoreSpotlightUtilities searchableItemForTransaction:pass:regions:tags:keywords:imageGenerator:contactResolver:completion:]_block_invoke
- ___126+[PKCoreSpotlightUtilities searchableItemForTransaction:pass:regions:tags:keywords:imageGenerator:contactResolver:completion:]_block_invoke_2
- ___126+[PKCoreSpotlightUtilities searchableItemForTransaction:pass:regions:tags:keywords:imageGenerator:contactResolver:completion:]_block_invoke_3
- ___126+[PKCoreSpotlightUtilities searchableItemForTransaction:pass:regions:tags:keywords:imageGenerator:contactResolver:completion:]_block_invoke_4
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.431
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.433
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.435
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.436
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke_2.432
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke_2.434
- ___37-[PKMobileAssetManager _purgeAssets:]_block_invoke
- ___55+[PKCoreSpotlightUtilities _extraDataAttributeForPass:]_block_invoke
- ___65-[PKPaymentOffersController _handleOffersChangedForPassUniqueID:]_block_invoke
- ___65-[PKPaymentOffersController _handleOffersChangedForPassUniqueID:]_block_invoke_2
- ___70-[PKMobileAssetManager _downloadPrefetchableAssetsForType:completion:]_block_invoke.405
- ___70-[PKMobileAssetManager _downloadPrefetchableAssetsForType:completion:]_block_invoke.407
- ___70-[PKMobileAssetManager _downloadPrefetchableAssetsForType:completion:]_block_invoke.410
- ___74-[PKMobileAssetManager _downloadAsset:isDiscretionary:timeout:completion:]_block_invoke.442
- ___79-[PKPaymentService spendingCategoryTransactionGroupsForRequest:byCalendarUnit:]_block_invoke
- ___80-[PKMobileAssetManager performScheduledActivityWithIdentifier:activityCriteria:]_block_invoke.421
- ___97+[PKCoreSpotlightUtilities searchableItemForPass:passTiles:passKitServicesXPCService:completion:]_block_invoke.276
- ___PKPeerPaymentProcessMessageWithDataURLAndProperties_block_invoke.234
- ___block_literal_global.231
- ___block_literal_global.420
- ___block_literal_global.423
- ___block_literal_global.533
- ___block_literal_global.690
- _block_copy_helper.42
- _block_copy_helper.45
- _block_copy_helper.48
- _block_descriptor.44
- _block_descriptor.47
- _block_descriptor.50
- _block_destroy_helper.43
- _block_destroy_helper.46
- _block_destroy_helper.49
- _objc_msgSend$_extraDataAttributeForPass:
- _objc_msgSend$_handleOffersChangedForPassUniqueID:
- _objc_msgSend$addThumbnailImages:
- _objc_msgSend$clearThumbnailImages
- _objc_msgSend$numberWithUnsignedLong:
- _objc_msgSend$setThumbnailImages:
- _objc_msgSend$spendingCategoryTransactionGroupsForRequest:byCalendarUnit:
- _objc_msgSend$spendingCategoryTransactionGroupsForRequest:byCalendarUnit:completion:
- _objc_msgSend$textContentAttributeForTransaction:pass:
- _objc_msgSend$thumbnailImages
- _objc_msgSend$thumbnailImagesAtIndex:
- _objc_msgSend$thumbnailImagesCount
- _objc_msgSend$transactionCountByPeriodForRequest:calendar:calendarUnit:includePurchaseTotal:completion:
- _objc_msgSend$transactionCountByPeriodForRequest:calendar:unit:includePurchaseTotal:completion:
- _symbolic So34PKFPANCardDescriptorCredentialPairC
CStrings:
+ "AppleCashStickers"
+ "CARD_PIN_CODE_PLACEHOLDER"
+ "CONTINUITY_FAILED_TO_FIND_DEVICE_MESSAGE_AMBIGUOUS_CAR_KEY"
+ "CONTINUITY_FAILED_TO_FIND_DEVICE_MESSAGE_OWNER_CAR_KEY"
+ "CONTINUITY_FAILED_TO_FIND_DEVICE_MESSAGE_SHARED_CAR_KEY"
+ "Can save result: %@"
+ "Finished prefetch of apple cash sticker assets with success %ld"
+ "PKAppleCashMessagesStickerExtensionVisibilityChangedNotification"
+ "PKPeerPaymentUtilities: PKPeerPaymentSetIsSetup %ld -> %ld"
+ "PassKitCore/ProvisioningCarKeyStepFindSource.swift"
+ "PassKitCore/ProvisioningCarKeyStepRequestInvite.swift"
+ "Passbook_rawPassJson"
+ "PrefetchAppleCashStickersAssets"
+ "Purge of cash stickers failed with result %lu"
+ "Purging apple cash sticker assets because they are not eligible for download"
+ "Skipping update of apple cash sticker assets because none are on device or eligible for download"
+ "Stickers"
+ "T@\"NSData\",R,C,N,V_SHA256"
+ "TB,N,V_requiresExplicitPrimaryAction"
+ "Tq,R,N,V_backgroundBlurStyle"
+ "[PKPassUpcomingPassInformationImageManifestItem] Unable to decode sha256 value"
+ "_SHA256"
+ "_allPassFields:"
+ "_backgroundBlurStyle"
+ "_createValidatedImageFromData:error:"
+ "_handleOffersChangedForPassUniqueID:didRemove:"
+ "_provisioningSubjectHandle"
+ "_purgeAssets:completion:"
+ "_purgeCashStickers"
+ "_queryForCashStickers"
+ "_requiresExplicitPrimaryAction"
+ "addCarKeyToWallet"
+ "addingKey"
+ "appleCashStickerAssetPrefetchTimeInterval"
+ "backgroundBlurStyle"
+ "cachedCashStickerBundle"
+ "carPairingCode"
+ "cashStickersAssetPrefetchTimeIntervalForRegion:"
+ "confirmAddKeyOsloSheet"
+ "defaultAppleCashStickerAssetPrefetchTimeInterval"
+ "gif"
+ "hasCashStickers"
+ "isOwnerPass:"
+ "jpeg"
+ "jpg"
+ "otherProviders"
+ "passPresentmentFeed"
+ "peerPaymentSendOrRequest"
+ "requiresExplicitPrimaryAction"
+ "searchableItemForTransaction:passUniqueID:passLocalizedDescription:regions:tags:keywords:imageGenerator:contactResolver:completion:"
+ "setRequiresExplicitPrimaryAction:"
+ "sharePass"
+ "sharesList"
+ "spendingCategoryTransactionGroupsForRequest:gregorianCalendarUnit:"
+ "spendingCategoryTransactionGroupsForRequest:gregorianCalendarUnit:completion:"
+ "textContentAttributeForTransaction:passLocalizedDescription:"
+ "thick"
+ "thin"
+ "transactionCountByPeriodForRequest:gregorianCalendarUnit:includePurchaseTotal:completion:"
+ "updateCashStickersIfNecessary"
+ "usingCarKeys"
+ "v44@0:8@\"PKPaymentTransactionRequest\"16Q24B32@?<v@?@\"NSArray\">36"
+ "v88@0:8@16@24@32@40@48@56@64@72@?80"
+ "\xf0a"
- "CONTINUITY_FAILED_TO_FIND_DEVICE_MESSAGE_KEY"
- "Falling back to hardcoded time interval for prefetch %@"
- "SHA256Hex"
- "T@\"NSArray\",&,N,V_thumbnailImages"
- "T@\"NSMutableArray\",&,N,V_thumbnailImages"
- "T@\"NSString\",R,C,N,V_SHA256Hex"
- "_SHA256Hex"
- "_defaultSubjectHandle"
- "_extraDataAttributeForPass:"
- "_handleOffersChangedForPassUniqueID:"
- "_thumbnailImages"
- "addThumbnailImages:"
- "clearThumbnailImages"
- "numberWithUnsignedLong:"
- "provisioningProgress"
- "searchableItemForTransaction:pass:regions:tags:keywords:imageGenerator:contactResolver:completion:"
- "setThumbnailImages:"
- "spendingCategoryTransactionGroupsForRequest:byCalendarUnit:"
- "spendingCategoryTransactionGroupsForRequest:byCalendarUnit:completion:"
- "textContentAttributeForTransaction:pass:"
- "thumbnailImages"
- "thumbnailImagesAtIndex:"
- "thumbnailImagesCount"
- "thumbnailImagesType"
- "transactionCountByPeriodForRequest:calendar:calendarUnit:includePurchaseTotal:completion:"
- "v52@0:8@\"PKPaymentTransactionRequest\"16@\"NSCalendar\"24Q32B40@?<v@?@\"NSArray\">44"
- "v80@0:8@16@24@32@40@48@56@64@?72"

```
