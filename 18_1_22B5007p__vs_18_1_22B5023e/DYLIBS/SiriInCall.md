## SiriInCall

> `/System/Library/PrivateFrameworks/SiriInCall.framework/SiriInCall`

```diff

 3400.14.1.0.0
-  __TEXT.__text: 0x7cec
-  __TEXT.__auth_stubs: 0x950
+  __TEXT.__text: 0x7ac0
+  __TEXT.__auth_stubs: 0x930
   __TEXT.__const: 0x4f8
-  __TEXT.__swift5_typeref: 0x248
+  __TEXT.__swift5_typeref: 0x246
   __TEXT.__swift5_fieldmd: 0x16c
   __TEXT.__constg_swiftt: 0x4b0
   __TEXT.__swift5_builtin: 0x64

   __TEXT.__cstring: 0x6d1
   __TEXT.__oslogstring: 0x455
   __TEXT.__swift5_capture: 0x64
-  __TEXT.__unwind_info: 0x328
-  __TEXT.__eh_frame: 0x150
+  __TEXT.__unwind_info: 0x320
+  __TEXT.__eh_frame: 0x120
   __TEXT.__objc_classname: 0x24
   __TEXT.__objc_methname: 0x509
   __TEXT.__objc_methtype: 0x19e
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0xd0
+  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x168
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x4a8
-  __AUTH_CONST.__auth_ptr: 0x1d0
+  __AUTH_CONST.__auth_got: 0x498
+  __AUTH_CONST.__auth_ptr: 0x1e0
   __AUTH_CONST.__const: 0x418
   __AUTH_CONST.__objc_const: 0x5a8
   __AUTH.__data: 0x30
-  __DATA.__data: 0x1c0
+  __DATA.__data: 0x1b0
   __DATA.__bss: 0x280
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x90
-  __DATA_DIRTY.__data: 0x1c0
+  __DATA_DIRTY.__data: 0x1d8
   __DATA_DIRTY.__common: 0x60
   __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 253
-  Symbols:   143
-  CStrings:  0
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 254
+  Symbols:   149
+  CStrings:  91
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _swift_continuation_await
- _swift_continuation_init
CStrings:
+ "DetailedCellTextField"
+ "_OBJC_CLASS_$_PKAccountBankAccountsViewController"
+ "_OBJC_CLASS_$_PKAccountScheduledPaymentCell"
+ "_OBJC_CLASS_$_PKAccountSupportTopicExplanationLinkSectionController"
+ "_OBJC_CLASS_$_PKAddBankAccountInformationViewController"
+ "_OBJC_CLASS_$_PKAddressEditorTableViewCell"
+ "_OBJC_CLASS_$_PKApplyCannotResumeIDVViewController"
+ "_OBJC_CLASS_$_PKApplyFieldsCollectionViewController"
+ "_OBJC_CLASS_$_PKApplyVerificationSMSOTPViewController"
+ "_OBJC_CLASS_$_PKConfigurablePassDetailSectionsController"
+ "_OBJC_CLASS_$_PKConnectedCircleView"
+ "_OBJC_CLASS_$_PKDashboardInstallmentPlanStatusItemPresenter"
+ "_OBJC_CLASS_$_PKDashboardPaymentPassDataSource"
+ "_OBJC_CLASS_$_PKEditPendingCacheRequest"
+ "_OBJC_CLASS_$_PKEditTableViewController"
+ "_OBJC_CLASS_$_PKEventTicketFaceBucketsFactory"
+ "_OBJC_CLASS_$_PKGradientVerticalConnector"
+ "_OBJC_CLASS_$_PKImageSequenceView"
+ "_OBJC_CLASS_$_PKInboxMessageContentConfiguration"
+ "_OBJC_CLASS_$_PKPassSnapshotCacheItem"
+ "_OBJC_CLASS_$_PKPassTransitProductsViewController"
+ "_OBJC_CLASS_$_PKPasscodeUpgradeExplanationViewController"
+ "_OBJC_CLASS_$_PKPayLaterFinancingPlanCostSectionController"
+ "_OBJC_CLASS_$_PKPayLaterMoreInformationViewController"
+ "_OBJC_CLASS_$_PKPayLaterUpdateUserInfoFieldsViewController"
+ "_OBJC_CLASS_$_PKPaymentAuthorizationViewController"
+ "_OBJC_CLASS_$_PKPaymentCardViewPresenter"
+ "_OBJC_CLASS_$_PKPaymentPreferenceButtonCell"
+ "_OBJC_CLASS_$_PKPaymentPreferenceDetailedCell"
+ "_OBJC_CLASS_$_PKPeerPaymentRecurringPaymentDetailSectionController"
+ "_OBJC_CLASS_$_PKPortraitNavigationController"
+ "_OBJC_CLASS_$_PKProvisioningReaderModeViewController"
+ "_OBJC_CLASS_$_PKRemoteActionGroupViewController"
+ "_OBJC_CLASS_$_PKRewardsHubSummarySectionController"
+ "_OBJC_CLASS_$_PKRewardsHubViewController"
+ "_OBJC_CLASS_$_PKShareableCredentialMessage"
+ "_OBJC_CLASS_$_PKStackedTextItemGroupView"
+ "_OBJC_CLASS_$_PKSubcredentialInvitationAcceptedViewController"
+ "_OBJC_CLASS_$_PKThresholdTopUpActionItem"
+ "_OBJC_CLASS_$_PKThresholdTopUpActionsSectionController"
+ "_OBJC_CLASS_$_PKThumbnailCollectionViewCell"
+ "_OBJC_CLASS_$_PKTransactionSpotlightDebugDetailsViewController"
+ "_OBJC_CLASS_$_PKTransitPassProductHeaderView"
+ "_OBJC_CLASS_$_PKVehicleInitiatedPairingViewController"
+ "_OBJC_CLASS_$__PKDashboardItemWrapper"
+ "_OBJC_METACLASS_$_PKAccountScheduledPaymentCell"
+ "_OBJC_METACLASS_$_PKAddBankAccountInformationViewController"
+ "_OBJC_METACLASS_$_PKAddressEditorTableViewCell"
+ "_OBJC_METACLASS_$_PKApplyCannotResumeIDVViewController"
+ "_OBJC_METACLASS_$_PKApplyFieldsCollectionViewController"
+ "_OBJC_METACLASS_$_PKApplyVerificationSMSOTPViewController"
+ "_OBJC_METACLASS_$_PKConfigurablePassDetailSectionsController"
+ "_OBJC_METACLASS_$_PKConnectedCircleView"
+ "_OBJC_METACLASS_$_PKDashboardInstallmentPlanStatusItemPresenter"
+ "_OBJC_METACLASS_$_PKDashboardPaymentPassDataSource"
+ "_OBJC_METACLASS_$_PKEditPendingCacheRequest"
+ "_OBJC_METACLASS_$_PKEditTableViewController"
+ "_OBJC_METACLASS_$_PKEventTicketFaceBucketsFactory"
+ "_OBJC_METACLASS_$_PKExpiredTableViewController"
+ "_OBJC_METACLASS_$_PKGradientVerticalConnector"
+ "_OBJC_METACLASS_$_PKImageSequenceView"
+ "_OBJC_METACLASS_$_PKInboxMessageContentConfiguration"
+ "_OBJC_METACLASS_$_PKPassSnapshotCacheItem"
+ "_OBJC_METACLASS_$_PKPassTransitProductsViewController"
+ "_OBJC_METACLASS_$_PKPasscodeUpgradeExplanationViewController"
+ "_OBJC_METACLASS_$_PKPayLaterFinancingPlanCostSectionController"
+ "_OBJC_METACLASS_$_PKPayLaterUpdateUserInfoFieldsViewController"
+ "_OBJC_METACLASS_$_PKPaymentAuthorizationViewController"
+ "_OBJC_METACLASS_$_PKPaymentCardViewPresenter"
+ "_OBJC_METACLASS_$_PKPaymentPreferenceButtonCell"
+ "_OBJC_METACLASS_$_PKPaymentPreferenceDetailedCell"
+ "_OBJC_METACLASS_$_PKPeerPaymentRecurringPaymentDetailSectionController"
+ "_OBJC_METACLASS_$_PKPortraitNavigationController"
+ "_OBJC_METACLASS_$_PKProvisioningReaderModeViewController"
+ "_OBJC_METACLASS_$_PKRemoteActionGroupViewController"
+ "_OBJC_METACLASS_$_PKRewardsHubSummarySectionController"
+ "_OBJC_METACLASS_$_PKRewardsHubViewController"
+ "_OBJC_METACLASS_$_PKShareableCredentialMessage"
+ "_OBJC_METACLASS_$_PKStackedTextItemGroupView"
+ "_OBJC_METACLASS_$_PKSubcredentialInvitationAcceptedViewController"
+ "_OBJC_METACLASS_$_PKThresholdTopUpActionItem"
+ "_OBJC_METACLASS_$_PKThresholdTopUpActionsSectionController"
+ "_OBJC_METACLASS_$_PKThumbnailCollectionViewCell"
+ "_OBJC_METACLASS_$_PKTransactionSpotlightDebugDetailsViewController"
+ "_OBJC_METACLASS_$_PKTransitPassProductHeaderView"
+ "_OBJC_METACLASS_$_PKVehicleInitiatedPairingViewController"
+ "_OBJC_METACLASS_$__PKDashboardItemWrapper"
+ "iredTableViewController"
+ "mentAddAssociatedAccountIdentityVerificationExplanationViewController"
+ "ntroller"
+ "ontroller"

```
