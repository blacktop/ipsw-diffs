## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

```diff

-981.20.0.0.0
-  __TEXT.__text: 0xb86cc
+981.23.0.0.0
+  __TEXT.__text: 0xb87e4
   __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x8e0c
+  __TEXT.__objc_methlist: 0x8e3c
   __TEXT.__const: 0x1610
-  __TEXT.__cstring: 0xb5d4
-  __TEXT.__oslogstring: 0xd32e
+  __TEXT.__cstring: 0xb770
+  __TEXT.__oslogstring: 0xd3a6
   __TEXT.__gcc_except_tab: 0x1710
   __TEXT.__dlopen_cstrs: 0x241
   __TEXT.__unwind_info: 0x2454
   __TEXT.__objc_classname: 0x1c08
-  __TEXT.__objc_methname: 0x1339d
-  __TEXT.__objc_methtype: 0x29df
-  __TEXT.__objc_stubs: 0xace0
+  __TEXT.__objc_methname: 0x133e7
+  __TEXT.__objc_methtype: 0x2a17
+  __TEXT.__objc_stubs: 0xad40
   __DATA_CONST.__got: 0x510
-  __DATA_CONST.__const: 0x3038
+  __DATA_CONST.__const: 0x3058
   __DATA_CONST.__objc_classlist: 0x730
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1b008
-  __DATA_CONST.__objc_selrefs: 0x4408
+  __DATA_CONST.__objc_const: 0x1b028
+  __DATA_CONST.__objc_selrefs: 0x4418
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_classrefs: 0x718
+  __DATA_CONST.__objc_classrefs: 0x720
   __DATA_CONST.__objc_superrefs: 0x510
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__cfstring: 0xad60
+  __AUTH_CONST.__cfstring: 0xae60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_const: 0x238
   __AUTH_CONST.__objc_intobj: 0xd8

   - /usr/lib/libcompression.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ACAD5113-FE24-35E4-A76E-4A0D8CF92053
-  Functions: 3898
-  Symbols:   13774
-  CStrings:  7785
+  UUID: E71432B2-367F-32E2-B4B7-DBD0276903C0
+  Functions: 3901
+  Symbols:   13787
+  CStrings:  7809
 
Symbols:
+ +[AAUrlBagHelper isLCInviteAcceptanceEnabled]
+ -[AACustodianController repairCustodians:completion:]
+ -[AAOBInheritanceInvitationModel initWithAcceptedViewForBenefactorInfo:]
+ -[AAOBInheritanceInvitationModel initWithBenefactorInfo:]
+ -[AAOBInheritanceInvitationModel initWithModel:]
+ -[AAOBInheritanceInviteMessageModel initWithType:recipientHandle:]
+ -[AAOBInheritanceSetupCompleteModel initWithBeneficiaryName:accessKeyShareType:inviteType:]
+ GCC_except_table100
+ GCC_except_table63
+ GCC_except_table66
+ GCC_except_table78
+ GCC_except_table96
+ _AAOBBeneficiaryIconName
+ _OUTLINED_FUNCTION_9
+ __AAUrlBagInheritanceConfigKey
+ __AAUrlBagLCInviteAcceptanceKey
+ ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.357
+ ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.357.cold.1
+ ___53-[AACustodianController repairCustodians:completion:]_block_invoke
+ ___53-[AACustodianController repairCustodians:completion:]_block_invoke.76
+ ___53-[AACustodianController repairCustodians:completion:]_block_invoke.76.cold.1
+ ___53-[AACustodianController repairCustodians:completion:]_block_invoke.77
+ ___53-[AACustodianController repairCustodians:completion:]_block_invoke.77.cold.1
+ ___65-[AAFollowUpController dismissFollowUpWithIdentifier:completion:]_block_invoke.305
+ ___65-[AAFollowUpController dismissFollowUpWithIdentifier:completion:]_block_invoke.305.cold.1
+ ___65-[AAFollowUpController pendingFollowUpWithIdentifier:completion:]_block_invoke.302
+ ___71-[AAFollowUpController postFollowUpWithIdentifier:userInfo:completion:]_block_invoke.298
+ ___71-[AAFollowUpController postFollowUpWithIdentifier:userInfo:completion:]_block_invoke.298.cold.1
+ ___75-[AAFollowUpController(Convenience) pendingFollowUpsForAccount:completion:]_block_invoke.358
+ ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.362
+ ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.362.cold.1
+ ___87-[AAFollowUpController(Convenience) dismissFollowUpsForAccount:identifiers:completion:]_block_invoke.356
+ ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.354
+ ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.354.cold.1
+ ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.354.cold.2
+ ___91-[AAFollowUpController(Convenience) pendingFollowUpItemUserInfosWithIdentifier:completion:]_block_invoke.365
+ ____AAFollowUpControllerHandleSetupAssistantExited_block_invoke.404
+ ___block_literal_global.368
+ ___block_literal_global.406
+ _kAACustodianInviteEvent
+ _objc_msgSend$custodianshipInfo
+ _objc_msgSend$displayName
+ _objc_msgSend$initWithBeneficiaryName:accessKeyShareType:inviteType:
+ _objc_msgSend$isLCInviteAcceptanceEnabled
+ _objc_msgSend$repairCustodians:completion:
- -[AAFollowUpController _followUpItemForBeneficiaryIneligible:]
- -[AAFollowUpController _followUpItemForBeneficiaryIneligible:].cold.1
- -[AAInheritanceMessageInviteContext _messageForContact:]
- -[AAOBInheritanceInvitationModel initWithBenefactorHandle:]
- -[AAOBInheritanceInvitationModel initWithBenefactorName:handle:]
- GCC_except_table67
- GCC_except_table79
- GCC_except_table95
- GCC_except_table99
- ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.379
- ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.379.cold.1
- ___60-[AACustodianController repairCustodians:remove:completion:]_block_invoke
- ___60-[AACustodianController repairCustodians:remove:completion:]_block_invoke.76
- ___60-[AACustodianController repairCustodians:remove:completion:]_block_invoke.76.cold.1
- ___60-[AACustodianController repairCustodians:remove:completion:]_block_invoke.77
- ___60-[AACustodianController repairCustodians:remove:completion:]_block_invoke.77.cold.1
- ___65-[AAFollowUpController dismissFollowUpWithIdentifier:completion:]_block_invoke.326
- ___65-[AAFollowUpController dismissFollowUpWithIdentifier:completion:]_block_invoke.326.cold.1
- ___65-[AAFollowUpController pendingFollowUpWithIdentifier:completion:]_block_invoke.323
- ___71-[AAFollowUpController postFollowUpWithIdentifier:userInfo:completion:]_block_invoke.319
- ___71-[AAFollowUpController postFollowUpWithIdentifier:userInfo:completion:]_block_invoke.319.cold.1
- ___75-[AAFollowUpController(Convenience) pendingFollowUpsForAccount:completion:]_block_invoke.380
- ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.384
- ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.384.cold.1
- ___87-[AAFollowUpController(Convenience) dismissFollowUpsForAccount:identifiers:completion:]_block_invoke.378
- ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.376
- ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.376.cold.1
- ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.376.cold.2
- ___91-[AAFollowUpController(Convenience) pendingFollowUpItemUserInfosWithIdentifier:completion:]_block_invoke.387
- ____AAFollowUpControllerHandleSetupAssistantExited_block_invoke.426
- ___block_literal_global.390
- ___block_literal_global.428
- _objc_msgSend$_followUpItemForBeneficiaryIneligible:
- _objc_msgSend$repairCustodians:remove:completion:
CStrings:
+ "@40@0:8@16Q24Q32"
+ "BENEFICIARY_ACCEPTED_INVITE_DETAIL_TEXT"
+ "BENEFICIARY_ACCEPTED_INVITE_TITLE"
+ "BENEFICIARY_DECLINED_INVITE_DETAIL_TEXT"
+ "BENEFICIARY_DECLINED_INVITE_TITLE"
+ "Custodians repaired successfully."
+ "Error repairing error: %@"
+ "INHERITANCE_ADDED_MESSAGES_BUBBLE_BODY"
+ "INHERITANCE_ADDED_MESSAGES_BUBBLE_TITLE"
+ "INHERITANCE_ADDED_MESSAGE_DETAIL_TEXT"
+ "INHERITANCE_BENEFICIARY_ADDED_MANAGE_BUTTON"
+ "INHERITANCE_BENEFICIARY_INVITED_DETAIL_TEXT"
+ "INHERITANCE_BENEFICIARY_INVITED_TITLE"
+ "INHERITANCE_INVITED_MESSAGES_BUBBLE_BODY"
+ "INHERITANCE_INVITED_MESSAGES_BUBBLE_TITLE"
+ "INHERITANCE_INVITED_MESSAGE_DETAIL_TEXT"
+ "INHERITANCE_INVITE_COMPLETE_MESSAGE_AFTER_MESSAGING"
+ "INHERITANCE_INVITE_COMPLETE_TITLE"
+ "LCInvite: No IdMS feature flag found. is OS FeatureFlag Enabled %d"
+ "LCInvite: Returning LCInviteAcceptance from urlbag: %@"
+ "LCInvite: inheritanceCfgs from urlbag: %@"
+ "LCInviteAcceptance"
+ "Repairing custodians %@"
+ "com.apple.appleaccount.CustodianInviteEvent"
+ "imageName: %@\title: %@\ndetailText: %@\nprimaryButton: %@\nsecondaryButton: %@\nhelpLinkTitle: %@\nhelpLinkURL: %@\nownerHandle: %@\ncustodianshipInfo: %@\n"
+ "imageName: %@\title: %@\ndetailText: %@\nprimaryButton: %@\nsecondaryButton: %@\nhelpLinkTitle: %@\nhelpLinkURL: %@\nownerHandle: %@\nrecipientHandle: %@\ncustodianshipInfo: %@\n"
+ "inheritanceCfgs"
+ "initWithAcceptedViewForBenefactorInfo:"
+ "initWithBenefactorInfo:"
+ "initWithBeneficiaryName:accessKeyShareType:inviteType:"
+ "initWithModel:"
+ "inviteAcceptance"
+ "isLCInviteAcceptanceEnabled"
+ "repairCustodians:completion:"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
- "AccountBeneficiary.png"
- "Custodians repaired/removed successfully."
- "Error repairing/removing error: %@"
- "FOLLOWUP_BENEFICIARY_INELIGIBLE_BUTTON_DISMISS"
- "FOLLOWUP_BENEFICIARY_INELIGIBLE_BUTTON_PRIMARY"
- "FOLLOWUP_BENEFICIARY_INELIGIBLE_MESSAGE"
- "FOLLOWUP_BENEFICIARY_INELIGIBLE_NOTIFICATION_MESSAGE"
- "FOLLOWUP_BENEFICIARY_INELIGIBLE_NOTIFICATION_TITLE"
- "FOLLOWUP_BENEFICIARY_INELIGIBLE_TITLE"
- "INHERITANCE_INVITE_MESSAGE_BUBBLE"
- "INHERITANCE_INVITE_MESSAGE_DETAIL_TEXT"
- "INHERITANCE_MESSAGES_BUBBLE_INVITE_BODY"
- "INHERITANCE_MESSAGES_BUBBLE_INVITE_BODY_NO_NAME"
- "INHERITANCE_MESSAGES_BUBBLE_TITLE"
- "Repairing custodians %@ and removing custodians %@"
- "_followUpItemForBeneficiaryIneligible:"
- "_messageForContact:"
- "imageName: %@\title: %@\ndetailText: %@\nprimaryButton: %@\nsecondaryButton: %@\nhelpLinkTitle: %@\nhelpLinkURL: %@\nownerHandle: %@\n"
- "initWithBenefactorHandle:"
- "initWithBenefactorName:handle:"

```
