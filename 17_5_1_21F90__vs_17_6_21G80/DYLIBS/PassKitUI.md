## PassKitUI

> `/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI`

```diff

-1552.6.11.0.0
-  __TEXT.__text: 0xbe3798
-  __TEXT.__auth_stubs: 0xa4d0
-  __TEXT.__objc_methlist: 0x4b078
-  __TEXT.__const: 0x28e50
-  __TEXT.__cstring: 0x5fa04
-  __TEXT.__constg_swiftt: 0xe1d0
+1552.7.5.1.0
+  __TEXT.__text: 0xbe581c
+  __TEXT.__auth_stubs: 0xa4c0
+  __TEXT.__objc_methlist: 0x4b2d0
+  __TEXT.__const: 0x28ea0
+  __TEXT.__cstring: 0x5fb3e
+  __TEXT.__constg_swiftt: 0xe20c
   __TEXT.__swift5_typeref: 0x5de30
   __TEXT.__swift5_builtin: 0x758
-  __TEXT.__swift5_reflstr: 0xe12e
-  __TEXT.__swift5_fieldmd: 0xbe64
+  __TEXT.__swift5_reflstr: 0xe17e
+  __TEXT.__swift5_fieldmd: 0xbeb0
   __TEXT.__swift5_assocty: 0x3598
-  __TEXT.__swift5_proto: 0xf34
-  __TEXT.__swift5_types: 0xc28
+  __TEXT.__swift5_proto: 0xf38
+  __TEXT.__swift5_types: 0xc2c
   __TEXT.__swift5_capture: 0x6f8c
   __TEXT.__swift5_protos: 0x30
   __TEXT.__swift5_mpenum: 0x70
-  __TEXT.__gcc_except_tab: 0xf474
-  __TEXT.__oslogstring: 0x193e8
+  __TEXT.__gcc_except_tab: 0xf5cc
+  __TEXT.__oslogstring: 0x19456
   __TEXT.__ustring: 0xcae
-  __TEXT.__unwind_info: 0x27720
+  __TEXT.__unwind_info: 0x277ac
   __TEXT.__eh_frame: 0x59dc
-  __TEXT.__objc_classname: 0x1055d
-  __TEXT.__objc_methname: 0xb6424
-  __TEXT.__objc_methtype: 0x1ff04
-  __TEXT.__objc_stubs: 0x77ac0
+  __TEXT.__objc_classname: 0x1059f
+  __TEXT.__objc_methname: 0xb6866
+  __TEXT.__objc_methtype: 0x1ffce
+  __TEXT.__objc_stubs: 0x77c80
   __DATA_CONST.__got: 0x4308
-  __DATA_CONST.__const: 0x171d0
-  __DATA_CONST.__objc_classlist: 0x2df8
+  __DATA_CONST.__const: 0x17220
+  __DATA_CONST.__objc_classlist: 0x2e08
   __DATA_CONST.__objc_catlist: 0x380
-  __DATA_CONST.__objc_protolist: 0x13d8
+  __DATA_CONST.__objc_protolist: 0x13e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa1ac8
-  __DATA_CONST.__objc_selrefs: 0x23850
+  __DATA_CONST.__objc_const: 0xa2020
+  __DATA_CONST.__objc_selrefs: 0x23900
   __DATA_CONST.__objc_protorefs: 0x438
-  __DATA_CONST.__objc_classrefs: 0x3fd0
-  __DATA_CONST.__objc_superrefs: 0x2448
+  __DATA_CONST.__objc_classrefs: 0x3ff0
+  __DATA_CONST.__objc_superrefs: 0x2450
   __DATA_CONST.__objc_arraydata: 0x550
-  __AUTH_CONST.__const: 0x33108
-  __AUTH_CONST.__objc_const: 0x1ca50
-  __AUTH_CONST.__auth_ptr: 0xc30
-  __AUTH_CONST.__cfstring: 0x32aa0
+  __AUTH_CONST.__const: 0x331e0
+  __AUTH_CONST.__objc_const: 0x1cae0
+  __AUTH_CONST.__auth_ptr: 0xc38
+  __AUTH_CONST.__cfstring: 0x32b00
   __AUTH_CONST.__objc_doubleobj: 0x1c0
   __AUTH_CONST.__objc_intobj: 0x1428
   __AUTH_CONST.__objc_arrayobj: 0x4b0
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH_CONST.__auth_got: 0x5278
-  __AUTH.__objc_data: 0x209c8
-  __AUTH.__data: 0xa8d0
-  __DATA.__objc_ivar: 0x2998
+  __AUTH_CONST.__auth_got: 0x5270
+  __AUTH.__objc_data: 0x20af8
+  __AUTH.__data: 0xa900
+  __DATA.__objc_ivar: 0x29b8
   __DATA.__objc_data: 0x438
-  __DATA.__data: 0x202c8
+  __DATA.__data: 0x20358
   __DATA.__common: 0x3b1
   __DATA.__bss: 0x1ce08
-  __DATA_DIRTY.__objc_ivar: 0x69d0
+  __DATA_DIRTY.__objc_ivar: 0x6a04
   __DATA_DIRTY.__objc_data: 0x2850
   __DATA_DIRTY.__data: 0x120
   __DATA_DIRTY.__bss: 0x2f8

   - /System/Library/Frameworks/LinkPresentation.framework/LinkPresentation
   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/MapKit.framework/MapKit
+  - /System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit
   - /System/Library/Frameworks/MessageUI.framework/MessageUI
   - /System/Library/Frameworks/Messages.framework/Messages
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 56975
-  Symbols:   109711
-  CStrings:  42805
+  Functions: 57040
+  Symbols:   109870
+  CStrings:  42854
 
Symbols:
+ +[PKPaymentSetupOptionsViewController _respondToKeyboardPresentationEvents]
+ -[PKCollapsibleHeaderView additionalCollapsibleHeight]
+ -[PKCollapsibleHeaderView setAdditionalCollapsibleHeight:]
+ -[PKDashboardPaymentPassDataSource reloadAccountWithNewAccount:]
+ -[PKDashboardPaymentProductsTransitPresenter initWithPassGroupView:paymentDataProvider:]
+ -[PKDashboardTransitItem actionGroups]
+ -[PKDashboardTransitItem setActionGroups:]
+ -[PKEditGroupViewController group:didInsertAssociatedAccount:forPass:]
+ -[PKEditGroupViewController group:didRemoveAssociatedAccountForPass:]
+ -[PKEditGroupViewController group:didUpdateAssociatedAccount:forPass:]
+ -[PKEditGroupsViewController group:didInsertAssociatedAccount:forPass:]
+ -[PKEditGroupsViewController group:didRemoveAssociatedAccountForPass:]
+ -[PKEditGroupsViewController group:didUpdateAssociatedAccount:forPass:]
+ -[PKLinkedAppView appLockupViewTapped]
+ -[PKNewPaymentCredentialProvisioningViewController initWithProvisioningController:webService:context:paymentCredential:setupProduct:allowsManualEntry:]
+ -[PKPassGroupView group:didInsertAssociatedAccount:forPass:]
+ -[PKPassGroupView group:didRemoveAssociatedAccountForPass:]
+ -[PKPassGroupView group:didUpdateAssociatedAccount:forPass:]
+ -[PKPassView associatedAccount]
+ -[PKPassView setAssociatedAccount:]
+ -[PKPassbookSettingsController _defaultAppSpecifiers]
+ -[PKPassbookSettingsController reloadSpecifiers]
+ -[PKPassbookSettingsController showController:animate:]
+ -[PKPaymentPassDetailViewController group:didInsertAssociatedAccount:forPass:]
+ -[PKPaymentPassDetailViewController group:didRemoveAssociatedAccountForPass:]
+ -[PKPaymentPassDetailViewController group:didUpdateAssociatedAccount:forPass:]
+ -[PKSimplePrimaryButtonCellView .cxx_destruct]
+ -[PKSimplePrimaryButtonCellView _layoutWithBounds:]
+ -[PKSimplePrimaryButtonCellView _setupViews]
+ -[PKSimplePrimaryButtonCellView _titleFont]
+ -[PKSimplePrimaryButtonCellView _updateContent:]
+ -[PKSimplePrimaryButtonCellView beginUpdates]
+ -[PKSimplePrimaryButtonCellView enableDisclosure]
+ -[PKSimplePrimaryButtonCellView endUpdates:]
+ -[PKSimplePrimaryButtonCellView initWithFrame:]
+ -[PKSimplePrimaryButtonCellView init]
+ -[PKSimplePrimaryButtonCellView layoutIfNeededAnimated:]
+ -[PKSimplePrimaryButtonCellView layoutSubviews]
+ -[PKSimplePrimaryButtonCellView pass]
+ -[PKSimplePrimaryButtonCellView prepareForReuse]
+ -[PKSimplePrimaryButtonCellView setPass:]
+ -[PKSimplePrimaryButtonCellView setTitle:]
+ -[PKSimplePrimaryButtonCellView setTitleColor:]
+ -[PKSimplePrimaryButtonCellView setTitleLineBreakMode:]
+ -[PKSimplePrimaryButtonCellView sizeThatFits:]
+ -[PKSimplePrimaryButtonCellView title]
+ -[PKSimplePrimaryButtonCellView viewType]
+ GCC_except_table111
+ GCC_except_table148
+ GCC_except_table151
+ GCC_except_table180
+ GCC_except_table192
+ GCC_except_table196
+ GCC_except_table214
+ GCC_except_table217
+ GCC_except_table223
+ GCC_except_table230
+ GCC_except_table233
+ GCC_except_table235
+ GCC_except_table257
+ GCC_except_table272
+ GCC_except_table275
+ GCC_except_table294
+ GCC_except_table301
+ GCC_except_table303
+ GCC_except_table317
+ GCC_except_table327
+ GCC_except_table330
+ GCC_except_table338
+ GCC_except_table341
+ GCC_except_table352
+ GCC_except_table355
+ GCC_except_table360
+ GCC_except_table372
+ GCC_except_table375
+ GCC_except_table377
+ GCC_except_table382
+ GCC_except_table400
+ GCC_except_table402
+ GCC_except_table423
+ GCC_except_table435
+ GCC_except_table439
+ GCC_except_table450
+ GCC_except_table479
+ GCC_except_table492
+ GCC_except_table494
+ GCC_except_table546
+ GCC_except_table554
+ GCC_except_table558
+ GCC_except_table561
+ GCC_except_table669
+ _OBJC_CLASS_$_PKSimplePrimaryButtonCellView
+ _OBJC_CLASS_$_PSNFCDefaultAppSpecifier
+ _OBJC_CLASS_$_SESNFCAppSettingsContext
+ _OBJC_CLASS_$__TtC9PassKitUI42ProvisioningPeerPaymentExplanationFlowItem
+ _OBJC_IVAR_$_PKDashboardPaymentPassDataSource._hasUpdatedAccountRewardsDataIfNecessary
+ _OBJC_IVAR_$_PKDashboardPaymentPassDataSource._isShowingPeerPaymentPendingRequests
+ _OBJC_IVAR_$_PKDashboardPaymentProductsTransitPresenter._combinedActionController
+ _OBJC_IVAR_$_PKDashboardPaymentProductsTransitPresenter._paymentDataProvider
+ _OBJC_IVAR_$_PKDashboardPaymentProductsTransitPresenter._sampleSingleCellButtonView
+ _OBJC_IVAR_$_PKDashboardTransitItem._actionGroups
+ _OBJC_IVAR_$_PKPassbookSettingsController._defaultAppSpecifiers
+ _OBJC_IVAR_$_PKPassbookSettingsController._defaultWalletContext
+ _OBJC_IVAR_$_PKPassbookSettingsController._lockscreenSwitchSpecifier
+ _OBJC_METACLASS_$_PKSimplePrimaryButtonCellView
+ _OBJC_METACLASS_$__TtC9PassKitUI42ProvisioningPeerPaymentExplanationFlowItem
+ _PKPassViewRequiredContentSuppressionForImageSnapshot
+ __DATA__TtC9PassKitUI42ProvisioningPeerPaymentExplanationFlowItem
+ __IVARS__TtC9PassKitUI42ProvisioningPeerPaymentExplanationFlowItem
+ __METACLASS_DATA__TtC9PassKitUI42ProvisioningPeerPaymentExplanationFlowItem
+ __OBJC_$_CLASS_METHODS_PKPaymentSetupOptionsViewController
+ __OBJC_$_INSTANCE_METHODS_PKSimplePrimaryButtonCellView
+ __OBJC_$_INSTANCE_METHODS__TtC9PassKitUI42ProvisioningPeerPaymentExplanationFlowItem
+ __OBJC_$_INSTANCE_VARIABLES_PKSimplePrimaryButtonCellView
+ __OBJC_$_PROP_LIST_PKSimplePrimaryButtonCellView
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PSSystemPolicyForAppDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PSSystemPolicyForAppDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PSSystemPolicyForAppDelegate
+ __OBJC_$_PROTOCOL_REFS_PSSystemPolicyForAppDelegate
+ __OBJC_CLASS_PROTOCOLS_$_PKSimplePrimaryButtonCellView
+ __OBJC_CLASS_RO_$_PKSimplePrimaryButtonCellView
+ __OBJC_LABEL_PROTOCOL_$_PSSystemPolicyForAppDelegate
+ __OBJC_METACLASS_RO_$_PKSimplePrimaryButtonCellView
+ __OBJC_PROTOCOL_$_PSSystemPolicyForAppDelegate
+ __PROTOCOLS__TtC9PassKitUI42ProvisioningPeerPaymentExplanationFlowItem
+ __PROTOCOLS__TtC9PassKitUI42ProvisioningPeerPaymentExplanationFlowItem.2
+ ___121-[PKDashboardPaymentProductsTransitPresenter didSelectItem:inCollectionView:atIndexPath:navigationController:canPresent:]_block_invoke
+ ___32-[PKPassView snapshotOfPassView]_block_invoke_2
+ ___34-[PKPassView drawFrontFaceAtSize:]_block_invoke
+ ___46-[PKPassbookSettingsController _fetchAccounts]_block_invoke.652
+ ___46-[PKPassbookSettingsController _fetchAccounts]_block_invoke.653
+ ___48-[PKSimplePrimaryButtonCellView _updateContent:]_block_invoke
+ ___51-[PKPassView snapshotOfFrontFaceWithRequestedSize:]_block_invoke_2
+ ___53-[PKPassbookSettingsController _defaultAppSpecifiers]_block_invoke
+ ___64-[PKDashboardPaymentPassDataSource reloadAccountWithNewAccount:]_block_invoke
+ ___64-[PKDashboardPaymentPassDataSource reloadAccountWithNewAccount:]_block_invoke.408
+ ___64-[PKDashboardPaymentPassDataSource reloadAccountWithNewAccount:]_block_invoke.411
+ ___64-[PKDashboardPaymentPassDataSource reloadAccountWithNewAccount:]_block_invoke.412
+ ___64-[PKDashboardPaymentPassDataSource reloadAccountWithNewAccount:]_block_invoke.414
+ ___64-[PKDashboardPaymentPassDataSource reloadAccountWithNewAccount:]_block_invoke.417
+ ___64-[PKDashboardPaymentPassDataSource reloadAccountWithNewAccount:]_block_invoke_2
+ ___64-[PKDashboardPaymentPassDataSource reloadAccountWithNewAccount:]_block_invoke_2.409
+ ___64-[PKDashboardPaymentPassDataSource reloadAccountWithNewAccount:]_block_invoke_2.413
+ ___64-[PKDashboardPaymentPassDataSource reloadAccountWithNewAccount:]_block_invoke_2.415
+ ___64-[PKDashboardPaymentPassDataSource reloadAccountWithNewAccount:]_block_invoke_3
+ ___67-[PKRemoteActionGroupViewController _rightBarButtonPressedForOslo:]_block_invoke.65
+ ___67-[PKRemoteActionGroupViewController _rightBarButtonPressedForOslo:]_block_invoke_2.68
+ ___67-[PKRemoteActionGroupViewController _rightBarButtonPressedForOslo:]_block_invoke_3.69
+ ___67-[PKRemoteActionGroupViewController _rightBarButtonPressedForOslo:]_block_invoke_4.71
+ ___68-[PKPassbookSettingsController initWithDelegate:dataSource:context:]_block_invoke_4
+ ___68-[PKPassbookSettingsController initWithDelegate:dataSource:context:]_block_invoke_5
+ ___69-[PKPassbookSettingsController _registerForPeerPaymentWithSpecifier:]_block_invoke.584
+ ___70-[PKRemoteActionGroupViewController _canPerformPaymentWithCompletion:]_block_invoke.82
+ ___70-[PKRemoteActionGroupViewController _canPerformPaymentWithCompletion:]_block_invoke_2.84
+ ___71-[PKPassbookSettingsController _unregisterForPeerPaymentWithSpecifier:]_block_invoke.627
+ ___77-[PKNewPaymentCredentialProvisioningViewController defaultHeaderViewSubTitle]_block_invoke
+ ___79-[PKPassbookSettingsController proofingFlowManager:completedProofingWithError:]_block_invoke.792
+ ___80-[PKPassbookSettingsController _credentialPairingContextForPass:withCompletion:]_block_invoke.703
+ ___83-[PKDashboardPaymentPassDataSource reloadPeerPaymentPendingRequestsWithCompletion:]_block_invoke_3
+ ___94-[PKPassbookSettingsController _checkPairedDeviceSupportOfHiddenPassesAndRefreshUIIfNecessary]_block_invoke.660
+ ___94-[PKPassbookSettingsController _checkPairedDeviceSupportOfHiddenPassesAndRefreshUIIfNecessary]_block_invoke.669
+ ___94-[PKPassbookSettingsController _performPhoneToWatchProvisioningForPaymentPass:withCompletion:]_block_invoke.723
+ ___94-[PKPassbookSettingsController _performPhoneToWatchProvisioningForPaymentPass:withCompletion:]_block_invoke.726
+ ___94-[PKPassbookSettingsController _performPhoneToWatchProvisioningForPaymentPass:withCompletion:]_block_invoke.738
+ ___94-[PKPassbookSettingsController _performPhoneToWatchProvisioningForPaymentPass:withCompletion:]_block_invoke.741
+ ___94-[PKPassbookSettingsController _performPhoneToWatchProvisioningForPaymentPass:withCompletion:]_block_invoke_2.727
+ ___94-[PKPassbookSettingsController _performPhoneToWatchProvisioningForPaymentPass:withCompletion:]_block_invoke_2.739
+ ___94-[PKPassbookSettingsController _performPhoneToWatchProvisioningForPaymentPass:withCompletion:]_block_invoke_2.742
+ ___94-[PKPassbookSettingsController _performPhoneToWatchProvisioningForPaymentPass:withCompletion:]_block_invoke_3.744
+ ___94-[PKPassbookSettingsController _performPhoneToWatchProvisioningForPaymentPass:withCompletion:]_block_invoke_4.747
+ ___94-[PKPassbookSettingsController _performPhoneToWatchProvisioningForPaymentPass:withCompletion:]_block_invoke_5.748
+ ___99-[PKPassbookSettingsController _presentCredentialSetupViewControllerForPaymentPass:withCompletion:]_block_invoke.708
+ ___block_descriptor_32_e30_B16?0"PKPaymentApplication"8l
+ ___block_descriptor_32_e48_v32?0"PKPassFaceView"8"PKImage"16"PKColor"24l
+ ___block_descriptor_32_e60_v40?0"PKPassFaceView"8"PKImage"16"PKColor"24"PKImage"32l
+ ___block_descriptor_40_e8_32w_e34_v16?0"PKPaymentBalanceReminder"8lw32l8
+ ___block_descriptor_50_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32bs40bs48w_e32_v28?0B8"NSArray"12"NSError"20lw48l8s32l8s40l8
+ ___block_descriptor_58_e8_32s40w_e31_v24?0"PKAccount"8"NSError"16lw40l8s32l8
+ ___block_descriptor_73_e8_32s40s48bs56bs64w_e5_v8?0lw64l8s32l8s48l8s40l8s56l8
+ ___block_descriptor_74_e8_32s40s48s56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ ___block_literal_global.102
+ ___block_literal_global.111
+ ___block_literal_global.119
+ ___block_literal_global.1275
+ ___block_literal_global.1279
+ ___block_literal_global.136
+ ___block_literal_global.144
+ ___block_literal_global.151
+ ___block_literal_global.264
+ ___block_literal_global.2710
+ ___block_literal_global.2718
+ ___block_literal_global.2722
+ ___block_literal_global.2733
+ ___block_literal_global.2737
+ ___block_literal_global.2786
+ ___block_literal_global.2792
+ ___block_literal_global.2799
+ ___block_literal_global.350
+ ___block_literal_global.375
+ ___block_literal_global.393
+ ___block_literal_global.415
+ ___block_literal_global.417
+ ___block_literal_global.438
+ ___block_literal_global.521
+ ___block_literal_global.731
+ ___block_literal_global.98
+ _objc_msgSend$_defaultAppSpecifiers
+ _objc_msgSend$_initWithID:kind:context:clientID:enableAppDistribution:
+ _objc_msgSend$_respondToKeyboardPresentationEvents
+ _objc_msgSend$associatedAccountForPassUniqueID:
+ _objc_msgSend$bundleId
+ _objc_msgSend$contextWithBundleId:onChange:
+ _objc_msgSend$customProductPageIdentifier
+ _objc_msgSend$doubleClickToggleVisibilityType
+ _objc_msgSend$initWithBundleID:delegate:onChange:
+ _objc_msgSend$initWithPassGroupView:paymentDataProvider:
+ _objc_msgSend$presentProductDetailsViewController
+ _objc_msgSend$reloadAccountWithNewAccount:
+ _objc_msgSend$setAssociatedAccount:
+ _objc_msgSend$setAutomaticallyPresentsProductDetails:
+ _objc_msgSend$settingsController:requestsForcedPresentViewController:animated:completion:
+ _objc_msgSend$shouldShowDefaultNFCAppPicker
+ _symbolic _____ 9PassKitUI42ProvisioningPeerPaymentExplanationFlowItemC
- -[PKDashboardPaymentPassDataSource _canShowPeerPaymentPendingRequests]
- -[PKDashboardPaymentProductsTransitPresenter initWithPassGroupView:]
- -[PKNewPaymentCredentialProvisioningViewController initWithProvisioningController:context:paymentCredential:setupProduct:allowsManualEntry:]
- GCC_except_table104
- GCC_except_table150
- GCC_except_table176
- GCC_except_table182
- GCC_except_table200
- GCC_except_table210
- GCC_except_table212
- GCC_except_table220
- GCC_except_table221
- GCC_except_table229
- GCC_except_table232
- GCC_except_table234
- GCC_except_table242
- GCC_except_table248
- GCC_except_table259
- GCC_except_table261
- GCC_except_table271
- GCC_except_table293
- GCC_except_table302
- GCC_except_table304
- GCC_except_table308
- GCC_except_table311
- GCC_except_table329
- GCC_except_table337
- GCC_except_table354
- GCC_except_table359
- GCC_except_table362
- GCC_except_table365
- GCC_except_table371
- GCC_except_table376
- GCC_except_table378
- GCC_except_table381
- GCC_except_table399
- GCC_except_table401
- GCC_except_table417
- GCC_except_table422
- GCC_except_table429
- GCC_except_table431
- GCC_except_table434
- GCC_except_table438
- GCC_except_table448
- GCC_except_table478
- GCC_except_table491
- GCC_except_table493
- GCC_except_table545
- GCC_except_table548
- GCC_except_table557
- GCC_except_table560
- GCC_except_table666
- _OBJC_IVAR_$_PKSelectActionGroupActionsHeader._loading
- ___46-[PKPassbookSettingsController _fetchAccounts]_block_invoke.648
- ___46-[PKPassbookSettingsController _fetchAccounts]_block_invoke.649
- ___47-[PKSelectActionGroupActionsHeader setLoading:]_block_invoke
- ___47-[PKSelectActionGroupActionsHeader setLoading:]_block_invoke_2
- ___49-[PKDashboardPaymentPassDataSource reloadAccount]_block_invoke
- ___49-[PKDashboardPaymentPassDataSource reloadAccount]_block_invoke.408
- ___49-[PKDashboardPaymentPassDataSource reloadAccount]_block_invoke.411
- ___49-[PKDashboardPaymentPassDataSource reloadAccount]_block_invoke.412
- ___49-[PKDashboardPaymentPassDataSource reloadAccount]_block_invoke.414
- ___49-[PKDashboardPaymentPassDataSource reloadAccount]_block_invoke.417
- ___49-[PKDashboardPaymentPassDataSource reloadAccount]_block_invoke_2
- ___49-[PKDashboardPaymentPassDataSource reloadAccount]_block_invoke_2.409
- ___49-[PKDashboardPaymentPassDataSource reloadAccount]_block_invoke_2.413
- ___49-[PKDashboardPaymentPassDataSource reloadAccount]_block_invoke_2.415
- ___49-[PKDashboardPaymentPassDataSource reloadAccount]_block_invoke_3
- ___67-[PKRemoteActionGroupViewController _rightBarButtonPressedForOslo:]_block_invoke.68
- ___67-[PKRemoteActionGroupViewController _rightBarButtonPressedForOslo:]_block_invoke_2.71
- ___67-[PKRemoteActionGroupViewController _rightBarButtonPressedForOslo:]_block_invoke_3.72
- ___67-[PKRemoteActionGroupViewController _rightBarButtonPressedForOslo:]_block_invoke_4.74
- ___69-[PKPassbookSettingsController _registerForPeerPaymentWithSpecifier:]_block_invoke.580
- ___70-[PKRemoteActionGroupViewController _canPerformPaymentWithCompletion:]_block_invoke.85
- ___70-[PKRemoteActionGroupViewController _canPerformPaymentWithCompletion:]_block_invoke_2.87
- ___71-[PKPassbookSettingsController _unregisterForPeerPaymentWithSpecifier:]_block_invoke.623
- ___79-[PKPassbookSettingsController proofingFlowManager:completedProofingWithError:]_block_invoke.788
- ___80-[PKPassbookSettingsController _credentialPairingContextForPass:withCompletion:]_block_invoke.699
- ___94-[PKPassbookSettingsController _checkPairedDeviceSupportOfHiddenPassesAndRefreshUIIfNecessary]_block_invoke.656
- ___94-[PKPassbookSettingsController _checkPairedDeviceSupportOfHiddenPassesAndRefreshUIIfNecessary]_block_invoke.665
- ___94-[PKPassbookSettingsController _performPhoneToWatchProvisioningForPaymentPass:withCompletion:]_block_invoke.719
- ___94-[PKPassbookSettingsController _performPhoneToWatchProvisioningForPaymentPass:withCompletion:]_block_invoke.722
- ___94-[PKPassbookSettingsController _performPhoneToWatchProvisioningForPaymentPass:withCompletion:]_block_invoke.734
- ___94-[PKPassbookSettingsController _performPhoneToWatchProvisioningForPaymentPass:withCompletion:]_block_invoke.737
- ___94-[PKPassbookSettingsController _performPhoneToWatchProvisioningForPaymentPass:withCompletion:]_block_invoke_2.723
- ___94-[PKPassbookSettingsController _performPhoneToWatchProvisioningForPaymentPass:withCompletion:]_block_invoke_2.735
- ___94-[PKPassbookSettingsController _performPhoneToWatchProvisioningForPaymentPass:withCompletion:]_block_invoke_2.738
- ___94-[PKPassbookSettingsController _performPhoneToWatchProvisioningForPaymentPass:withCompletion:]_block_invoke_3.740
- ___94-[PKPassbookSettingsController _performPhoneToWatchProvisioningForPaymentPass:withCompletion:]_block_invoke_4.743
- ___94-[PKPassbookSettingsController _performPhoneToWatchProvisioningForPaymentPass:withCompletion:]_block_invoke_5.744
- ___99-[PKPassbookSettingsController _presentCredentialSetupViewControllerForPaymentPass:withCompletion:]_block_invoke.704
- ___block_descriptor_40_e8_32s_e48_v32?0"PKPassFaceView"8"PKImage"16"PKColor"24ls32l8
- ___block_descriptor_40_e8_32s_e60_v40?0"PKPassFaceView"8"PKImage"16"PKColor"24"PKImage"32ls32l8
- ___block_descriptor_48_e8_32bs40w_e32_v28?0B8"NSArray"12"NSError"20lw40l8s32l8
- ___block_descriptor_48_e8_32s40s_e17_v16?0"NSArray"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e34_v16?0"PKPaymentBalanceReminder"8lw40l8s32l8
- ___block_descriptor_57_e8_32s40w_e31_v24?0"PKAccount"8"NSError"16lw40l8s32l8
- ___block_descriptor_73_e8_32s40s48s56w_e5_v8?0lw56l8s32l8s40l8s48l8
- ___block_literal_global.1260
- ___block_literal_global.1264
- ___block_literal_global.150
- ___block_literal_global.2705
- ___block_literal_global.2713
- ___block_literal_global.2717
- ___block_literal_global.2730
- ___block_literal_global.2734
- ___block_literal_global.2783
- ___block_literal_global.2789
- ___block_literal_global.2796
- ___block_literal_global.347
- ___block_literal_global.369
- ___block_literal_global.390
- ___block_literal_global.401
- ___block_literal_global.413
- ___block_literal_global.435
- ___block_literal_global.517
- ___block_literal_global.727
- _isPassbookDefault
- _objc_msgSend$_canShowPeerPaymentPendingRequests
- _objc_msgSend$_initWithID:kind:context:clientID:
CStrings:
+ "\x01O\x0f\x03\x1f\x14\x13\x12\x11\x16\x11"
+ "\x02!\x12\x14\x11\x12\x13\x11\"\x11!\x12\x14\x18\x11\x11\x13\x11\x13\x11\x13\x11\x131\x14/\x03\x14\x1f\x02"
+ "\x04\x12\x12\x11!!"
+ "\x13\xf0\xf0\xf0\xe1\xd1"
+ "!!\x12"
+ "@\"PKSimplePrimaryButtonCellView\""
+ "@\"SESNFCAppSettingsContext\""
+ "@60@0:8@16@24q32@40@48B56"
+ "B16@?0@\"PKPaymentApplication\"8"
+ "DASHBOARD_ACCOUNT_LOCKED_BANKRUPTCY_MESSAGE"
+ "DASHBOARD_MORE_MENU_BUY_OTHER_PASSES"
+ "Dashboard (%p): Fetching local account"
+ "Dashboard (%p): Processing account %{public}@, error: %{public}@"
+ "Dashboard (%p): Updating account, last update: %@"
+ "Dashboard loading (%p): for %{public}@, pass feature %{pubflic}@"
+ "E\x113\x11"
+ "PKPassbookSettingsController (%p): dropping request to show view controller (%p): %@"
+ "PKSimplePrimaryButtonCellView"
+ "PSSystemPolicyForAppDelegate"
+ "PassKitUI.ProvisioningPeerPaymentExplanationFlowItem"
+ "PeerPaymentExplanationFlowItem"
+ "T@\"NSArray\",C,N,V_actionGroups"
+ "T@\"PKAccount\",&,N,V_associatedAccount"
+ "Td,N,V_additionalCollapsibleHeight"
+ "_TtC9PassKitUI42ProvisioningPeerPaymentExplanationFlowItem"
+ "_additionalCollapsibleHeight"
+ "_defaultAppSpecifiers"
+ "_defaultWalletContext"
+ "_hasUpdatedAccountRewardsDataIfNecessary"
+ "_initWithID:kind:context:clientID:enableAppDistribution:"
+ "_isShowingPeerPaymentPendingRequests"
+ "_lockscreenSwitchSpecifier"
+ "_respondToKeyboardPresentationEvents"
+ "_sampleSingleCellButtonView"
+ "additionalCollapsibleHeight"
+ "appLockupViewTapped"
+ "associatedAccount"
+ "associatedAccountForPassUniqueID:"
+ "bundleId"
+ "contextWithBundleId:onChange:"
+ "doubleClickToggleVisibilityType"
+ "group:didInsertAssociatedAccount:forPass:"
+ "group:didRemoveAssociatedAccountForPass:"
+ "group:didUpdateAssociatedAccount:forPass:"
+ "initWithBundleID:delegate:onChange:"
+ "initWithPassGroupView:paymentDataProvider:"
+ "initWithProvisioningController:webService:context:paymentCredential:setupProduct:allowsManualEntry:"
+ "paymentProductsTransitPresenterButtonView"
+ "presentProductDetailsViewController"
+ "reloadAccountWithNewAccount:"
+ "reloadSpecifiers"
+ "setAdditionalCollapsibleHeight:"
+ "setAssociatedAccount:"
+ "setAutomaticallyPresentsProductDetails:"
+ "settingsController:requestsForcedPresentViewController:animated:completion:"
+ "shouldShowDefaultNFCAppPicker"
+ "showController:animate:"
+ "systemPolicyForApp:didUpdateForSystemPolicyOptions:withValue:"
+ "v32@0:8@\"PKGroup\"16@\"PKPass\"24"
+ "v40@0:8@\"PKGroup\"16@\"PKAccount\"24@\"PKPass\"32"
+ "v40@0:8@\"PSSystemPolicyForApp\"16Q24@32"
- "\x01O\x0f\x01\x1f\x14\x13\x12\x11\x16"
- "\x02!\x12\x14\x11\x12\x13\x11\"\x11!\x12\x14\x18\x11\x11\x13\x11\x13\x11\x13\x11\x135/\x03\x14\x1f\x02"
- "\x04\x12\x12\x11!"
- "\x13\xf0\xf0\xf0\xc1\xc1"
- "Dashboard getting account"
- "Dashboard loading (%p): for %{public}@, pass feature %{public}@"
- "Dashboard processing account: %{public}@, error: %{public}@"
- "Dashboard updating account, last update: %@"
- "E\x112\x11"
- "_canShowPeerPaymentPendingRequests"
- "_initWithID:kind:context:clientID:"
- "initWithProvisioningController:context:paymentCredential:setupProduct:allowsManualEntry:"

```
