## AOSUI

> `/System/Library/PrivateFrameworks/AOSUI.framework/Versions/A/AOSUI`

```diff

-874.0.0.0.0
-  __TEXT.__text: 0x1241cc
+872.0.0.0.0
+  __TEXT.__text: 0x123224
   __TEXT.__auth_stubs: 0x1310
-  __TEXT.__objc_methlist: 0xe24c
+  __TEXT.__objc_methlist: 0xe1e4
   __TEXT.__const: 0x2c8
-  __TEXT.__cstring: 0x1314e
-  __TEXT.__oslogstring: 0xb7b7
-  __TEXT.__gcc_except_tab: 0x1890
+  __TEXT.__cstring: 0x13061
+  __TEXT.__oslogstring: 0xb72c
+  __TEXT.__gcc_except_tab: 0x1840
   __TEXT.__ustring: 0x132
   __TEXT.__dlopen_cstrs: 0x192
-  __TEXT.__unwind_info: 0x4428
-  __TEXT.__objc_classname: 0x2153
-  __TEXT.__objc_methname: 0x2a118
-  __TEXT.__objc_methtype: 0x749e
-  __TEXT.__objc_stubs: 0x1a420
-  __DATA_CONST.__got: 0x1850
-  __DATA_CONST.__const: 0xe00
+  __TEXT.__unwind_info: 0x43c8
+  __TEXT.__objc_classname: 0x214d
+  __TEXT.__objc_methname: 0x29fc5
+  __TEXT.__objc_methtype: 0x74d1
+  __TEXT.__objc_stubs: 0x1a300
+  __DATA_CONST.__got: 0x1838
+  __DATA_CONST.__const: 0xde0
   __DATA_CONST.__objc_classlist: 0x690
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8af0
+  __DATA_CONST.__objc_selrefs: 0x8aa8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x478
   __DATA_CONST.__objc_arraydata: 0x130
   __AUTH_CONST.__auth_got: 0x998
-  __AUTH_CONST.__const: 0x4190
-  __AUTH_CONST.__cfstring: 0xccc0
-  __AUTH_CONST.__objc_const: 0x330f0
+  __AUTH_CONST.__const: 0x4170
+  __AUTH_CONST.__cfstring: 0xcc20
+  __AUTH_CONST.__objc_const: 0x33110
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH.__objc_data: 0x18b0
-  __DATA.__objc_ivar: 0x1480
+  __DATA.__objc_ivar: 0x1484
   __DATA.__data: 0x2290
   __DATA.__bss: 0x338
   __DATA.__common: 0x28

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6961
-  Symbols:   16674
-  CStrings:  2276
+  Functions: 6942
+  Symbols:   16638
+  CStrings:  2270
 
Symbols:
+ -[AOSUIRecoveryFactorController presentAccountRecoveryFlowWithContext:completionHandler:].cold.1
+ GCC_except_table51
+ GCC_except_table70
+ GCC_except_table80
+ GCC_except_table89
+ GCC_except_table93
+ OBJC_IVAR_$_AOSUIRecoveryFactorController._recoveryContactsViewController
+ OBJC_IVAR_$_AOSUIRecoveryFactorController._viewController
+ OBJC_IVAR_$_AOSUIRecoveryFactorController._viewModel
+ __53-[AOSUIMyCustodianActionHandler doDestructiveAction:]_block_invoke.55
+ __59-[AOSUIRecoveryFactorController startAddingRecoveryContact]_block_invoke.35
+ __66-[MMService _validateDataclassAccessWithWindow:completionHandler:]_block_invoke.185
+ __68-[AOSUIMyCustodianActionHandler _dismissAndPresentPostRemovalAlert:]_block_invoke.66
+ __68-[AOSUIMyCustodianActionHandler _dismissAndPresentPostRemovalAlert:]_block_invoke.69
+ __68-[AOSUIMyCustodianActionHandler _dismissAndPresentPostRemovalAlert:]_block_invoke.69.cold.1
+ __68-[AOSUIMyCustodianActionHandler _dismissAndPresentPostRemovalAlert:]_block_invoke.79
+ __69-[AOSUIAccountBeneficiaryViewController _fetchAllInheritanceContacts]_block_invoke.52.cold.1
+ __69-[AOSUIAccountBeneficiaryViewController _fetchAllInheritanceContacts]_block_invoke.52.cold.2
+ _objc_msgSend$initWithBenefactorHandle:
- -[AOSUIAccountContactBaseViewModel custodianshipInfo]
- -[AOSUIAccountContactBaseViewModel setCustodianshipInfo:]
- -[AOSUIInheritanceInvitationHandler _acceptInheritanceInviteWithID:completion:]
- -[AOSUIInheritanceInvitationHandler _declineInheritanceInviteWithID:completion:]
- -[AOSUIInheritanceInvitationHandler _removeFollowUpWithCompletion:]
- -[AOSUIInheritanceInvitationHandler _setfirstButtonToDismissForContainerView:]
- -[AOSUIInheritanceInvitationHandler _showInheritanceInvitationAcceptedView]
- -[AOSUIInheritanceInvitationHandler secondButtonPressed]
- -[AOSUIRecoveryFactorController _presentRecoveryContactViewWithCompletionHandler:].cold.1
- -[AOSUITrustedContactInvitationHandler firstButtonPressed].cold.1
- -[MMService _policyRestrictsDataclass]
- -[MMService isSupportedForCurrentUser].cold.2
- GCC_except_table44
- GCC_except_table52
- GCC_except_table75
- GCC_except_table79
- GCC_except_table81
- OBJC_IVAR_$_AOSUIAccountContactBaseViewModel._custodianshipInfo
- OBJC_IVAR_$_MMService._isMAID
- _OBJC_CLASS_$_AACustodianshipInfo
- _OBJC_CLASS_$_AADataclassManager
- _OBJC_CLASS_$_AAFDeviceInfo
- __45-[AOSUIInheritanceInvitationHandler _dismiss]_block_invoke.64
- __53-[AOSUIMyCustodianActionHandler doDestructiveAction:]_block_invoke.59
- __55-[AOSUIInheritanceInvitationHandler firstButtonPressed]_block_invoke.cold.1
- __56-[AOSUIInheritanceInvitationHandler secondButtonPressed]_block_invoke.cold.1
- __56-[AOSUIInheritanceInvitationHandler secondButtonPressed]_block_invoke.cold.2
- __59-[AOSUIRecoveryFactorController startAddingRecoveryContact]_block_invoke.34
- __66-[MMService _validateDataclassAccessWithWindow:completionHandler:]_block_invoke.186
- __68-[AOSUIMyCustodianActionHandler _dismissAndPresentPostRemovalAlert:]_block_invoke.70
- __68-[AOSUIMyCustodianActionHandler _dismissAndPresentPostRemovalAlert:]_block_invoke.73
- __68-[AOSUIMyCustodianActionHandler _dismissAndPresentPostRemovalAlert:]_block_invoke.73.cold.1
- __68-[AOSUIMyCustodianActionHandler _dismissAndPresentPostRemovalAlert:]_block_invoke.83
- __69-[AOSUIAccountBeneficiaryViewController _fetchAllInheritanceContacts]_block_invoke_2.cold.1
- __69-[AOSUIAccountBeneficiaryViewController _fetchAllInheritanceContacts]_block_invoke_2.cold.2
- ___55-[AOSUIInheritanceInvitationHandler firstButtonPressed]_block_invoke
- ___56-[AOSUIInheritanceInvitationHandler secondButtonPressed]_block_invoke
- ___69-[AOSUIAccountBeneficiaryViewController _fetchAllInheritanceContacts]_block_invoke_2
- ___75-[AOSUIInheritanceInvitationHandler _showInheritanceInvitationAcceptedView]_block_invoke
- ___block_descriptor_32_e31_B24?0"AALocalContactInfo"8Q16l
- __block_literal_global.55
- _objc_msgSend$_acceptInheritanceInviteWithID:completion:
- _objc_msgSend$_declineInheritanceInviteWithID:completion:
- _objc_msgSend$_policyRestrictsDataclass
- _objc_msgSend$_showInheritanceInvitationAcceptedView
- _objc_msgSend$aaf_filter:
- _objc_msgSend$initWithBenefactorFullName:firstName:handle:benefactorInfo:
- _objc_msgSend$initWithID:status:ownerHandle:
- _objc_msgSend$isVirtualMachine
- _objc_msgSend$policyRestrictsDataclass:
- _objc_msgSend$respondToInvitation:accepted:completion:
CStrings:
+ "com.apple.Passwords-Settings.extension"
- "B24@?0@\"AALocalContactInfo\"8Q16"
- "RATCHET_RC_ADD_NOT_ALLOWED_MESSAGE_VM"
- "RATCHET_RC_DELETE_NOT_ALLOWED_ALERT_TITLE_MAC"
- "RATCHET_RC_DELETE_NOT_ALLOWED_MESSAGE"
- "RATCHET_RC_DELETE_NOT_ALLOWED_MESSAGE_VM"
- "com.apple.AAFollowUpIdentifier.beneficiaryInvitationReminder"
- "com.apple.Passwords"

```
