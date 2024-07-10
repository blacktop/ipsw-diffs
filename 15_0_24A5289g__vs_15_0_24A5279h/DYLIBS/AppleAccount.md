## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/Versions/A/AppleAccount`

```diff

-1002.0.0.0.0
-  __TEXT.__text: 0x167334
-  __TEXT.__auth_stubs: 0x950
-  __TEXT.__objc_methlist: 0x8efc
+1000.0.0.0.0
+  __TEXT.__text: 0x167d18
+  __TEXT.__auth_stubs: 0x930
+  __TEXT.__objc_methlist: 0x8ec4
   __TEXT.__const: 0x43870
-  __TEXT.__cstring: 0xb53e
+  __TEXT.__cstring: 0xb663
   __TEXT.__oslogstring: 0xd07f
-  __TEXT.__gcc_except_tab: 0x2048
+  __TEXT.__gcc_except_tab: 0x2040
   __TEXT.__dlopen_cstrs: 0x287
-  __TEXT.__unwind_info: 0x25c8
+  __TEXT.__unwind_info: 0x25b0
   __TEXT.__eh_frame: 0x88
-  __TEXT.__objc_classname: 0x1c0f
-  __TEXT.__objc_methname: 0x131a9
+  __TEXT.__objc_classname: 0x1c0d
+  __TEXT.__objc_methname: 0x1318c
   __TEXT.__objc_methtype: 0x2913
-  __TEXT.__objc_stubs: 0xa920
+  __TEXT.__objc_stubs: 0xa900
   __DATA_CONST.__got: 0xb00
-  __DATA_CONST.__const: 0x2038
+  __DATA_CONST.__const: 0x2028
   __DATA_CONST.__objc_classlist: 0x738
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x43c8
+  __DATA_CONST.__objc_selrefs: 0x43c0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x520
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__auth_got: 0x4b8
+  __AUTH_CONST.__auth_got: 0x4a8
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0xc030
-  __AUTH_CONST.__cfstring: 0xaaa0
-  __AUTH_CONST.__objc_const: 0x20af8
+  __AUTH_CONST.__cfstring: 0xab60
+  __AUTH_CONST.__objc_const: 0x20a80
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH.__objc_data: 0x1ea0
-  __DATA.__objc_ivar: 0xad4
+  __DATA.__objc_ivar: 0xacc
   __DATA.__data: 0x1318
   __DATA.__bss: 0x3e0
   __DATA.__common: 0xa18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3948
-  Symbols:   9770
-  CStrings:  1657
+  Functions: 3943
+  Symbols:   9759
+  CStrings:  1663
 
Symbols:
+ -[AAFollowUpController _adpUserMissingHealthyCustodianNotification:]
+ -[AAFollowUpController _followUpItemForADPUserMissingHealthyCustodian:]
+ -[AAFollowUpController _followUpItemForBeneficiaryIneligible:]
+ -[AAFollowUpController _followUpItemForBeneficiaryIneligible:].cold.1
+ GCC_except_table45
+ GCC_except_table73
+ GCC_except_table76
+ _AAFollowUpUserInfoHasMultipleRecoveryContacts
+ __101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.393
+ __101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.393.cold.1
+ __103-[AASignInFlowController _delegate_presentGenericTermsUIforAccount:authResults:serverError:completion:]_block_invoke.160
+ __131-[AASignInFlowController _onqueue_saveAccount:withAuthResults:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:]_block_invoke.144
+ __58-[AASignInFlowController prewarmOperationsWithCompletion:]_block_invoke.215
+ __65-[AAFollowUpController dismissFollowUpWithIdentifier:completion:]_block_invoke.340
+ __65-[AAFollowUpController dismissFollowUpWithIdentifier:completion:]_block_invoke.340.cold.1
+ __65-[AAFollowUpController pendingFollowUpWithIdentifier:completion:]_block_invoke.336
+ __71-[AAFollowUpController postFollowUpWithIdentifier:userInfo:completion:]_block_invoke.332
+ __71-[AAFollowUpController postFollowUpWithIdentifier:userInfo:completion:]_block_invoke.332.cold.1
+ __75-[AAFollowUpController(Convenience) pendingFollowUpsForAccount:completion:]_block_invoke.396
+ __80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.400
+ __80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.400.cold.1
+ __81-[AAFollowUpController(Convenience) _filterFollowUpItems:byIdentifier:byAccount:]_block_invoke.410
+ __86-[AASignInFlowController _onqueue_enrollCDPStateForAccount:withCDPContext:completion:]_block_invoke.129
+ __87-[AAFollowUpController(Convenience) dismissFollowUpsForAccount:identifiers:completion:]_block_invoke.392
+ __89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.390
+ __89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.390.cold.1
+ __89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.390.cold.2
+ __91-[AAFollowUpController(Convenience) pendingFollowUpItemUserInfosWithIdentifier:completion:]_block_invoke.403
+ __98-[AASignInFlowController _onqueue_validateAndEnrollCDPStateForAccount:withAuthResults:completion:]_block_invoke.107
+ __98-[AASignInFlowController _onqueue_validateAndEnrollCDPStateForAccount:withAuthResults:completion:]_block_invoke.107.cold.1
+ __block_literal_global.406
+ _getFLNotificationOptionLockscreen
+ _objc_msgSend$_adpUserMissingHealthyCustodianNotification:
+ _objc_msgSend$_followUpItemForADPUserMissingHealthyCustodian:
+ _objc_msgSend$_followUpItemForBeneficiaryIneligible:
+ getFLNotificationOptionLockscreen.cold.1
- -[AAFollowUpController _custodianReviewNotification:].cold.1
- -[AAGenericTermsUIRequest serverInfo]
- -[AAGenericTermsUIRequest setServerInfo:]
- -[AALoginAccountRequest serverInfo]
- -[AALoginAccountRequest setServerInfo:]
- -[AAOBInheritanceInvitationModel initWithBenefactorFullName:firstName:handle:benefactorInfo:]
- -[AAOBInheritanceInvitationModel initWithModel:]
- -[ACAccount(AppleAccount_Internal) _aa_setTermsServerInfo:]
- -[ACAccount(AppleAccount_Internal) _aa_termsServerInfo]
- GCC_except_table69
- GCC_except_table72
- OBJC_IVAR_$_AAGenericTermsUIRequest._serverInfo
- OBJC_IVAR_$_AALoginAccountRequest._serverInfo
- __101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.348
- __101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.348.cold.1
- __103-[AASignInFlowController _delegate_presentGenericTermsUIforAccount:authResults:serverError:completion:]_block_invoke.163
- __131-[AASignInFlowController _onqueue_saveAccount:withAuthResults:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:]_block_invoke.147
- __58-[AASignInFlowController prewarmOperationsWithCompletion:]_block_invoke.218
- __65-[AAFollowUpController dismissFollowUpWithIdentifier:completion:]_block_invoke.298
- __65-[AAFollowUpController dismissFollowUpWithIdentifier:completion:]_block_invoke.298.cold.1
- __65-[AAFollowUpController pendingFollowUpWithIdentifier:completion:]_block_invoke.294
- __71-[AAFollowUpController postFollowUpWithIdentifier:userInfo:completion:]_block_invoke.290
- __71-[AAFollowUpController postFollowUpWithIdentifier:userInfo:completion:]_block_invoke.290.cold.1
- __75-[AAFollowUpController(Convenience) pendingFollowUpsForAccount:completion:]_block_invoke.351
- __80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.355
- __80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.355.cold.1
- __81-[AAFollowUpController(Convenience) _filterFollowUpItems:byIdentifier:byAccount:]_block_invoke.365
- __86-[AASignInFlowController _onqueue_enrollCDPStateForAccount:withCDPContext:completion:]_block_invoke.132
- __87-[AAFollowUpController(Convenience) dismissFollowUpsForAccount:identifiers:completion:]_block_invoke.347
- __89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.345
- __89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.345.cold.1
- __89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.345.cold.2
- __91-[AAFollowUpController(Convenience) pendingFollowUpItemUserInfosWithIdentifier:completion:]_block_invoke.358
- __98-[AASignInFlowController _onqueue_validateAndEnrollCDPStateForAccount:withAuthResults:completion:]_block_invoke.110
- __98-[AASignInFlowController _onqueue_validateAndEnrollCDPStateForAccount:withAuthResults:completion:]_block_invoke.110.cold.1
- __OBJC_$_PROP_LIST_AALoginAccountRequest
- __block_literal_global.361
- _kAAAnalyticsDeviceRemovalReason
- _kAAAnalyticsRecordViabilityState
- _objc_getAssociatedObject
- _objc_msgSend$_aa_setTermsServerInfo:
- _objc_msgSend$_aa_termsServerInfo
- _objc_msgSend$custodianshipInfo
- _objc_msgSend$initWithBenefactorFullName:firstName:handle:benefactorInfo:
- _objc_setAssociatedObject
CStrings:
+ "FOLLOWUP_BENEFICIARY_INELIGIBLE_BUTTON_DISMISS"
+ "FOLLOWUP_BENEFICIARY_INELIGIBLE_BUTTON_PRIMARY"
+ "FOLLOWUP_BENEFICIARY_INELIGIBLE_MESSAGE"
+ "FOLLOWUP_BENEFICIARY_INELIGIBLE_NOTIFICATION_MESSAGE"
+ "FOLLOWUP_BENEFICIARY_INELIGIBLE_NOTIFICATION_TITLE"
+ "FOLLOWUP_BENEFICIARY_INELIGIBLE_TITLE"
+ "FOLLOWUP_HEALTHY_RECOVERY_CONTACTS_MISSING_NOTIFICATION_MESSAGE"
+ "FOLLOWUP_HEALTHY_RECOVERY_CONTACT_MISSING_ADD_RECOVERY_CONTACT"
+ "FOLLOWUP_HEALTHY_RECOVERY_CONTACT_MISSING_BUTTON_DISMISS"
+ "FOLLOWUP_HEALTHY_RECOVERY_CONTACT_MISSING_BUTTON_PRIMARY"
+ "FOLLOWUP_HEALTHY_RECOVERY_CONTACT_MISSING_MESSAGE"
+ "FOLLOWUP_HEALTHY_RECOVERY_CONTACT_MISSING_NOTIFICATION_MESSAGE"
+ "FOLLOWUP_HEALTHY_RECOVERY_CONTACT_MISSING_NOTIFICATION_TITLE_MACOS"
+ "hasMultipleRecoveryContacts"
+ "imageName: %!@(MISSING)\title: %!@(MISSING)\ndetailText: %!@(MISSING)\nprimaryButton: %!@(MISSING)\nsecondaryButton: %!@(MISSING)\nhelpLinkTitle: %!@(MISSING)\nhelpLinkURL: %!@(MISSING)\nownerHandle: %!@(MISSING)\n"
- "BENEFICIARY_DECLINED_INVITE_DETAIL_TEXT"
- "BENEFICIARY_DECLINED_INVITE_TITLE"
- "INHERITANCE_BENEFICIARY_ADDED_MANAGE_BUTTON"
- "INHERITANCE_BENEFICIARY_INVITED_DETAIL_TEXT"
- "INHERITANCE_BENEFICIARY_INVITED_TITLE"
- "deviceRemovalReason"
- "imageName: %!@(MISSING)\title: %!@(MISSING)\ndetailText: %!@(MISSING)\nprimaryButton: %!@(MISSING)\nsecondaryButton: %!@(MISSING)\nhelpLinkTitle: %!@(MISSING)\nhelpLinkURL: %!@(MISSING)\nownerHandle: %!@(MISSING)\ncustodianshipInfo: %!@(MISSING)\n"
- "imageName: %!@(MISSING)\title: %!@(MISSING)\ndetailText: %!@(MISSING)\nprimaryButton: %!@(MISSING)\nsecondaryButton: %!@(MISSING)\nhelpLinkTitle: %!@(MISSING)\nhelpLinkURL: %!@(MISSING)\nownerHandle: %!@(MISSING)\nrecipientHandle: %!@(MISSING)\ncustodianshipInfo: %!@(MISSING)\n"
- "recordViabilityState"

```
