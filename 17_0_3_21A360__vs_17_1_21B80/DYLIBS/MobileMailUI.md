## MobileMailUI

> `/System/Library/PrivateFrameworks/MobileMailUI.framework/MobileMailUI`

```diff

-3774.100.2.2.5
-  __TEXT.__text: 0x36924
+3774.200.91.2.1
+  __TEXT.__text: 0x3a440
   __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_methlist: 0x31e0
-  __TEXT.__const: 0x15407
-  __TEXT.__gcc_except_tab: 0x7730
-  __TEXT.__cstring: 0x286f
+  __TEXT.__objc_methlist: 0x3520
+  __TEXT.__gcc_except_tab: 0x8130
+  __TEXT.__cstring: 0x2b59
+  __TEXT.__ustring: 0x318
+  __TEXT.__const: 0x1546b
   __TEXT.__oslogstring: 0x19d2
-  __TEXT.__ustring: 0x4c
-  __TEXT.__unwind_info: 0x20c8
-  __TEXT.__objc_classname: 0x9d5
-  __TEXT.__objc_methname: 0xfb64
-  __TEXT.__objc_methtype: 0x3f0a
-  __TEXT.__objc_stubs: 0xaa20
+  __TEXT.__unwind_info: 0x2334
+  __TEXT.__objc_classname: 0xa2f
+  __TEXT.__objc_methname: 0x10960
+  __TEXT.__objc_methtype: 0x404a
+  __TEXT.__objc_stubs: 0xb440
   __DATA_CONST.__got: 0x360
-  __DATA_CONST.__const: 0x1180
-  __DATA_CONST.__objc_classlist: 0x188
+  __DATA_CONST.__const: 0x11c8
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7808
-  __DATA_CONST.__objc_selrefs: 0x32d0
+  __DATA_CONST.__objc_const: 0x7b78
+  __DATA_CONST.__objc_selrefs: 0x35d0
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__cfstring: 0x28e0
+  __AUTH_CONST.__cfstring: 0x2da0
+  __AUTH_CONST.__objc_const: 0x1500
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__objc_const: 0x13e0
-  __AUTH_CONST.__const: 0x3e0
+  __AUTH_CONST.__const: 0x400
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__auth_got: 0x4d0
-  __AUTH.__objc_data: 0x460
+  __AUTH.__objc_data: 0x550
   __AUTH.__data: 0x10
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x5f8
-  __DATA.__objc_superrefs: 0x118
-  __DATA.__objc_ivar: 0x408
+  __DATA.__objc_classrefs: 0x618
+  __DATA.__objc_superrefs: 0x130
+  __DATA.__objc_ivar: 0x440
   __DATA.__data: 0xf90
   __DATA.__bss: 0x68
   __DATA_DIRTY.__objc_data: 0xaf0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x190
   - /System/Library/Frameworks/Accounts.framework/Accounts
+  - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/AccountsUI.framework/AccountsUI
   - /System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/CertInfo.framework/CertInfo
   - /System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices
   - /System/Library/PrivateFrameworks/ContactsAutocompleteUI.framework/ContactsAutocompleteUI
   - /System/Library/PrivateFrameworks/CoreSuggestions.framework/CoreSuggestions

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1235
-  Symbols:   5987
-  CStrings:  3368
+  Functions: 1313
+  Symbols:   6314
+  CStrings:  3543
 
Symbols:
+ +[MFContactCardInteractions contactCardInteractionWithViewController:blockedSenderManager:]
+ -[BIMIVerifiedDomainHeaderView .cxx_destruct]
+ -[BIMIVerifiedDomainHeaderView _setupSubViews]
+ -[BIMIVerifiedDomainHeaderView domain]
+ -[BIMIVerifiedDomainHeaderView initWithFrame:domain:mailProviderDisplayName:]
+ -[BIMIVerifiedDomainHeaderView learnMoreButtonPressed:]
+ -[BIMIVerifiedDomainHeaderView mailProviderDisplayName]
+ -[BIMIVerifiedDomainHeaderView setDomain:]
+ -[BIMIVerifiedDomainHeaderView setMailProviderDisplayName:]
+ -[MFContactCardInteractions .cxx_destruct]
+ -[MFContactCardInteractions _addVIP:]
+ -[MFContactCardInteractions _blockContact:]
+ -[MFContactCardInteractions _removeVIP:]
+ -[MFContactCardInteractions _startSearch:]
+ -[MFContactCardInteractions _unblockContact:]
+ -[MFContactCardInteractions _updateBlockContactCardButtonForViewController:]
+ -[MFContactCardInteractions _updateContactCardButtonsForViewController:]
+ -[MFContactCardInteractions _updateSearchContactCardButtonForViewController:]
+ -[MFContactCardInteractions _updateVIPContactCardButtonForViewController:]
+ -[MFContactCardInteractions blockedSenderManager]
+ -[MFContactCardInteractions configureInteractionsWithInteractionDelegate:]
+ -[MFContactCardInteractions contactViewController]
+ -[MFContactCardInteractions contact]
+ -[MFContactCardInteractions currentVIP]
+ -[MFContactCardInteractions delegate]
+ -[MFContactCardInteractions displayName]
+ -[MFContactCardInteractions emailAddressSet]
+ -[MFContactCardInteractions initWithViewController:blockedSenderManager:]
+ -[MFContactCardInteractions isBlocked]
+ -[MFContactCardInteractions setContactViewController:]
+ -[MFContactCardInteractions setCurrentVIP:]
+ -[MFContactCardInteractions setDelegate:]
+ -[MFContactCardInteractions setDisplayName:]
+ -[MFContactCardInteractions setEmailAddressSet:]
+ -[MFContactCardInteractions setIsBlocked:]
+ -[MFContactCardInteractions workerScheduler]
+ -[MFContactMessageInteraction .cxx_destruct]
+ -[MFContactMessageInteraction _certificateControllerDidFinish]
+ -[MFContactMessageInteraction _configureSecureMIMEPersonHeaderView:]
+ -[MFContactMessageInteraction _handleTrustDidChange]
+ -[MFContactMessageInteraction _presentCertificateTrustInfo:]
+ -[MFContactMessageInteraction _updateHeaderView]
+ -[MFContactMessageInteraction _viewEncryptionCertificateButtonTapped:]
+ -[MFContactMessageInteraction _viewSigningCertificateButtonTapped:]
+ -[MFContactMessageInteraction addNotificationObservers]
+ -[MFContactMessageInteraction certificateKeychainManager]
+ -[MFContactMessageInteraction certificateViewController]
+ -[MFContactMessageInteraction delegate]
+ -[MFContactMessageInteraction headerView]
+ -[MFContactMessageInteraction init]
+ -[MFContactMessageInteraction installCertificateWithTrustException:]
+ -[MFContactMessageInteraction performCertificateActionInstall]
+ -[MFContactMessageInteraction performCertificateActionRemove]
+ -[MFContactMessageInteraction performCertificateActionTrustAndInstall]
+ -[MFContactMessageInteraction performCertificateActionTrust]
+ -[MFContactMessageInteraction performCertificateActionUntrust]
+ -[MFContactMessageInteraction presentingViewController]
+ -[MFContactMessageInteraction promptOrInstallCertificationWithBlock:]
+ -[MFContactMessageInteraction promptToReplaceCurrentCertificateWithBlock:]
+ -[MFContactMessageInteraction refreshCertificateViewControllerStatus]
+ -[MFContactMessageInteraction securityInformation]
+ -[MFContactMessageInteraction setCertificateKeychainManager:]
+ -[MFContactMessageInteraction setCertificateViewController:certificateTrustInfo:]
+ -[MFContactMessageInteraction setDelegate:]
+ -[MFContactMessageInteraction setSecurityInformation:]
+ -[MFContactMessageInteraction shouldShowContactHeader]
+ -[MFContactMessageInteraction updateCertificateAction]
+ -[MFContactMessageInteraction updateWithSecurityInformation:]
+ GCC_except_table102
+ GCC_except_table105
+ GCC_except_table120
+ GCC_except_table126
+ GCC_except_table133
+ GCC_except_table136
+ GCC_except_table140
+ GCC_except_table142
+ GCC_except_table145
+ GCC_except_table151
+ GCC_except_table153
+ GCC_except_table158
+ GCC_except_table160
+ GCC_except_table171
+ GCC_except_table181
+ GCC_except_table184
+ GCC_except_table193
+ GCC_except_table196
+ GCC_except_table199
+ GCC_except_table203
+ GCC_except_table205
+ GCC_except_table208
+ GCC_except_table212
+ GCC_except_table216
+ GCC_except_table220
+ GCC_except_table225
+ GCC_except_table227
+ GCC_except_table232
+ GCC_except_table242
+ GCC_except_table244
+ GCC_except_table247
+ GCC_except_table250
+ GCC_except_table255
+ GCC_except_table259
+ GCC_except_table262
+ GCC_except_table264
+ GCC_except_table336
+ GCC_except_table337
+ GCC_except_table344
+ GCC_except_table46
+ GCC_except_table50
+ GCC_except_table58
+ GCC_except_table64
+ GCC_except_table68
+ GCC_except_table77
+ GCC_except_table83
+ GCC_except_table86
+ GCC_except_table88
+ GCC_except_table91
+ GCC_except_table98
+ _OBJC_CLASS_$_BIMIVerifiedDomainHeaderView
+ _OBJC_CLASS_$_CNContactFormatter
+ _OBJC_CLASS_$_CertificateViewController
+ _OBJC_CLASS_$_EMVIP
+ _OBJC_CLASS_$_MFContactCardInteractions
+ _OBJC_CLASS_$_MFContactMessageInteraction
+ _OBJC_CLASS_$_MFSecureMIMEPersonHeaderView
+ _OBJC_IVAR_$_BIMIVerifiedDomainHeaderView._domain
+ _OBJC_IVAR_$_BIMIVerifiedDomainHeaderView._mailProviderDisplayName
+ _OBJC_IVAR_$_MFContactCardInteractions._blockedSenderManager
+ _OBJC_IVAR_$_MFContactCardInteractions._contactViewController
+ _OBJC_IVAR_$_MFContactCardInteractions._currentVIP
+ _OBJC_IVAR_$_MFContactCardInteractions._delegate
+ _OBJC_IVAR_$_MFContactCardInteractions._displayName
+ _OBJC_IVAR_$_MFContactCardInteractions._emailAddressSet
+ _OBJC_IVAR_$_MFContactCardInteractions._isBlocked
+ _OBJC_IVAR_$_MFContactCardInteractions._workerScheduler
+ _OBJC_IVAR_$_MFContactMessageInteraction._certificateKeychainManager
+ _OBJC_IVAR_$_MFContactMessageInteraction._certificateTrustInfo
+ _OBJC_IVAR_$_MFContactMessageInteraction._certificateViewController
+ _OBJC_IVAR_$_MFContactMessageInteraction._delegate
+ _OBJC_IVAR_$_MFContactMessageInteraction._securityInformation
+ _OBJC_METACLASS_$_BIMIVerifiedDomainHeaderView
+ _OBJC_METACLASS_$_MFContactCardInteractions
+ _OBJC_METACLASS_$_MFContactMessageInteraction
+ __OBJC_$_CLASS_METHODS_MFContactCardInteractions
+ __OBJC_$_INSTANCE_METHODS_BIMIVerifiedDomainHeaderView
+ __OBJC_$_INSTANCE_METHODS_MFContactCardInteractions
+ __OBJC_$_INSTANCE_METHODS_MFContactMessageInteraction
+ __OBJC_$_INSTANCE_VARIABLES_BIMIVerifiedDomainHeaderView
+ __OBJC_$_INSTANCE_VARIABLES_MFContactCardInteractions
+ __OBJC_$_INSTANCE_VARIABLES_MFContactMessageInteraction
+ __OBJC_$_PROP_LIST_BIMIVerifiedDomainHeaderView
+ __OBJC_$_PROP_LIST_MFContactCardInteractions
+ __OBJC_$_PROP_LIST_MFContactMessageInteraction
+ __OBJC_CLASS_RO_$_BIMIVerifiedDomainHeaderView
+ __OBJC_CLASS_RO_$_MFContactCardInteractions
+ __OBJC_CLASS_RO_$_MFContactMessageInteraction
+ __OBJC_METACLASS_RO_$_BIMIVerifiedDomainHeaderView
+ __OBJC_METACLASS_RO_$_MFContactCardInteractions
+ __OBJC_METACLASS_RO_$_MFContactMessageInteraction
+ ___43-[MFContactCardInteractions _blockContact:]_block_invoke
+ ___43-[MFContactCardInteractions _blockContact:]_block_invoke_2
+ ___45-[MFContactCardInteractions _unblockContact:]_block_invoke
+ ___54-[MFContactMessageInteraction updateCertificateAction]_block_invoke
+ ___54-[MFContactMessageInteraction updateCertificateAction]_block_invoke_2
+ ___54-[MFContactMessageInteraction updateCertificateAction]_block_invoke_3
+ ___54-[MFContactMessageInteraction updateCertificateAction]_block_invoke_4
+ ___54-[MFContactMessageInteraction updateCertificateAction]_block_invoke_5
+ ___60-[MFMessageContentView _webView:renderingProgressDidChange:]_block_invoke.367
+ ___60-[MFMessageContentView generateSnapshotImageWithCompletion:]_block_invoke.273
+ ___62-[MFContactMessageInteraction performCertificateActionInstall]_block_invoke
+ ___70-[MFContactMessageInteraction performCertificateActionTrustAndInstall]_block_invoke
+ ___73-[MFMessageContentView _webView:webContentProcessDidTerminateWithReason:]_block_invoke.368
+ ___74-[MFContactCardInteractions configureInteractionsWithInteractionDelegate:]_block_invoke
+ ___74-[MFContactMessageInteraction promptToReplaceCurrentCertificateWithBlock:]_block_invoke
+ ___block_descriptor_32_e24_16?0"CNLabeledValue"8l
+ ___block_descriptor_40_ea8_32bs_e23_v16?0"UIAlertAction"8ls32l8
+ ___block_literal_global.1428
+ ___block_literal_global.254
+ __unnamed_array_storage.349
+ _objc_msgSend$_configureSecureMIMEPersonHeaderView:
+ _objc_msgSend$_presentCertificateTrustInfo:
+ _objc_msgSend$_setupSubViews
+ _objc_msgSend$_updateBlockContactCardButtonForViewController:
+ _objc_msgSend$_updateContactCardButtonsForViewController:
+ _objc_msgSend$_updateHeaderView
+ _objc_msgSend$_updateSearchContactCardButtonForViewController:
+ _objc_msgSend$_updateVIPContactCardButtonForViewController:
+ _objc_msgSend$addActionWithTitle:target:selector:inGroup:destructive:
+ _objc_msgSend$addNotificationObservers
+ _objc_msgSend$addTrustException
+ _objc_msgSend$addressForSaving
+ _objc_msgSend$blockContact:
+ _objc_msgSend$blockedSenderManager
+ _objc_msgSend$canSaveCertificateToKeychain
+ _objc_msgSend$canSearchForContactFromContactCardInteractions:
+ _objc_msgSend$cardBottomGroup
+ _objc_msgSend$certificateKeychainManager
+ _objc_msgSend$certificateType
+ _objc_msgSend$certificateViewController
+ _objc_msgSend$contact
+ _objc_msgSend$contactCardInteractions:triggerSearchForDisplayName:emailAddresses:
+ _objc_msgSend$contactMessageInteraction:didUpdateHeaderView:
+ _objc_msgSend$contactViewController
+ _objc_msgSend$contentViewController
+ _objc_msgSend$currentVIP
+ _objc_msgSend$deleteVIPWithIdentifier:
+ _objc_msgSend$emailAddressSet
+ _objc_msgSend$encryptionCertificateTrustInfo
+ _objc_msgSend$hasSeparateSigningAndEncryptionCertificates
+ _objc_msgSend$hasTrustException
+ _objc_msgSend$initWithIdentifier:name:emailAddresses:
+ _objc_msgSend$initWithTitle:style:target:action:
+ _objc_msgSend$initWithTrust:action:
+ _objc_msgSend$initWithViewController:blockedSenderManager:
+ _objc_msgSend$installCertificateWithTrustException:
+ _objc_msgSend$isBlockedSenderEnabled
+ _objc_msgSend$isContactBlocked:
+ _objc_msgSend$isMailVIP
+ _objc_msgSend$keychainStatus
+ _objc_msgSend$mailProviderDisplayName
+ _objc_msgSend$navigationController
+ _objc_msgSend$openURL:options:completionHandler:
+ _objc_msgSend$performCertificateActionInstall
+ _objc_msgSend$performCertificateActionRemove
+ _objc_msgSend$performCertificateActionTrust
+ _objc_msgSend$performCertificateActionTrustAndInstall
+ _objc_msgSend$performCertificateActionUntrust
+ _objc_msgSend$presentingViewController
+ _objc_msgSend$presentingViewControllerForMessageInteraction:
+ _objc_msgSend$promptOrInstallCertificationWithBlock:
+ _objc_msgSend$promptToReplaceCurrentCertificateWithBlock:
+ _objc_msgSend$refreshCertificateViewControllerStatus
+ _objc_msgSend$removeActionWithTarget:selector:inGroup:
+ _objc_msgSend$removeCertificateFromKeychain
+ _objc_msgSend$removeTrustException
+ _objc_msgSend$saveCertificateToKeychain
+ _objc_msgSend$saveVIP:
+ _objc_msgSend$setButtons:
+ _objc_msgSend$setCertUIAction:
+ _objc_msgSend$setCertificateKeychainManager:
+ _objc_msgSend$setCertificateViewController:certificateTrustInfo:
+ _objc_msgSend$setCurrentVIP:
+ _objc_msgSend$setDirectionalLayoutMargins:
+ _objc_msgSend$setEmailAddressSet:
+ _objc_msgSend$setExplanationText:
+ _objc_msgSend$setIsBlocked:
+ _objc_msgSend$setIsMailVIP:
+ _objc_msgSend$setLayoutMarginsRelativeArrangement:
+ _objc_msgSend$setSecureLabelText:
+ _objc_msgSend$setShowCertificateButton:localizedTitle:localizedDescription:destructive:handler:
+ _objc_msgSend$setSignedLabelText:
+ _objc_msgSend$setSpacing:
+ _objc_msgSend$setWarningLabelText:
+ _objc_msgSend$shouldShowContactHeader
+ _objc_msgSend$stringFromContact:style:
+ _objc_msgSend$tableView
+ _objc_msgSend$trust
+ _objc_msgSend$unblockContact:
+ _objc_msgSend$updateCertificateAction
+ _objc_msgSend$value
- -[MFMessageContentView findOverlayView]
- -[MFMessageContentView setFindOverlayView:]
- GCC_except_table101
- GCC_except_table104
- GCC_except_table119
- GCC_except_table125
- GCC_except_table132
- GCC_except_table135
- GCC_except_table138
- GCC_except_table141
- GCC_except_table144
- GCC_except_table150
- GCC_except_table152
- GCC_except_table156
- GCC_except_table159
- GCC_except_table170
- GCC_except_table180
- GCC_except_table183
- GCC_except_table192
- GCC_except_table194
- GCC_except_table198
- GCC_except_table202
- GCC_except_table204
- GCC_except_table206
- GCC_except_table211
- GCC_except_table214
- GCC_except_table217
- GCC_except_table223
- GCC_except_table226
- GCC_except_table231
- GCC_except_table241
- GCC_except_table243
- GCC_except_table246
- GCC_except_table248
- GCC_except_table254
- GCC_except_table258
- GCC_except_table261
- GCC_except_table263
- GCC_except_table265
- GCC_except_table338
- GCC_except_table339
- GCC_except_table346
- GCC_except_table49
- GCC_except_table57
- GCC_except_table63
- GCC_except_table66
- GCC_except_table76
- GCC_except_table82
- GCC_except_table84
- GCC_except_table87
- GCC_except_table90
- GCC_except_table96
- _OBJC_IVAR_$_MFMessageContentView._findOverlayView
- ___60-[MFMessageContentView _webView:renderingProgressDidChange:]_block_invoke.368
- ___60-[MFMessageContentView generateSnapshotImageWithCompletion:]_block_invoke.274
- ___73-[MFMessageContentView _webView:webContentProcessDidTerminateWithReason:]_block_invoke.369
- ___block_literal_global.1442
- ___block_literal_global.255
- __unnamed_array_storage.350
CStrings:
+ "\x01\x13"
+ "\vAd!T*\x18"
+ "\x12"
+ "5"
+ "@\"<MFContactCardInteractionDelegate>\""
+ "@\"<MFContactMessageInteractionDelegate>\""
+ "@\"CNContactViewController\""
+ "@\"CertificateViewController\""
+ "@\"EAEmailAddressSet\""
+ "@\"EMBlockedSenderManager\""
+ "@\"EMCertificateTrustInformation\""
+ "@\"EMVIP\""
+ "@\"MFCertificateTrustInformationKeychainManager\""
+ "@16@?0@\"CNLabeledValue\"8"
+ "@64@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48@56"
+ "ADD_VIP"
+ "BIMIVerifiedDomainHeaderView"
+ "BIMI_KB_LINK"
+ "BLOCK_CONTACT"
+ "BLOCK_CONTACT_CONFIRMATION"
+ "CANCEL"
+ "CERTIFICATE"
+ "DECRYPTION_ERROR"
+ "DONE"
+ "ENCRYPTED"
+ "ENCRYPTED_DESCRIPTION"
+ "ENCRYPTION_CERTIFICATE_DESCRIPTION"
+ "INSTALL"
+ "INSTALL_CERTIFICATE"
+ "Learn More"
+ "MFContactCardInteractions"
+ "MFContactMessageInteraction"
+ "OVERWRITE_CERTIFICATE_DESCRIPTION_FORMAT"
+ "REMOVE"
+ "REMOVE_VIP"
+ "SEARCH_MAIL_FOR_CONTACT_ADDRESSES"
+ "SIGNATURE_ERROR"
+ "SIGNED"
+ "SIGNED_AND_ENCRYPTED_DESCRIPTION"
+ "SIGNED_DESCRIPTION"
+ "SIGNING_CERTIFICATE_DESCRIPTION"
+ "SMIME_CONFIRM_SIGNATURE_FORMAT"
+ "SMIME_UNREADABLE_SIG"
+ "T@\"<EFScheduler>\",R,N,V_workerScheduler"
+ "T@\"<MFContactCardInteractionDelegate>\",W,N,V_delegate"
+ "T@\"<MFContactMessageInteractionDelegate>\",W,N,V_delegate"
+ "T@\"CNContactViewController\",W,N,V_contactViewController"
+ "T@\"CertificateViewController\",R,N,V_certificateViewController"
+ "T@\"EAEmailAddressSet\",&,N,V_emailAddressSet"
+ "T@\"EMBlockedSenderManager\",R,N,V_blockedSenderManager"
+ "T@\"EMVIP\",&,N,V_currentVIP"
+ "T@\"MFCertificateTrustInformationKeychainManager\",&,N,V_certificateKeychainManager"
+ "T@\"MFSecureMIMEPersonHeaderView\",R,N"
+ "T@\"NSString\",&,N,V_displayName"
+ "T@\"NSString\",C,N,V_domain"
+ "T@\"NSString\",C,N,V_mailProviderDisplayName"
+ "T@\"UIViewController\",R,N"
+ "TB,N,V_isBlocked"
+ "TRUST"
+ "There was a problem reading the digital signature for this message."
+ "UNBLOCK_CONTACT"
+ "UNTRUST"
+ "UNTRUSTED_SIGNATURE"
+ "VIEW_CERTIFICATE"
+ "VIEW_ENCRYPTION_CERTIFICATE"
+ "VIEW_SIGNING_CERTIFICATE"
+ "Verified Logo"
+ "_addVIP:"
+ "_blockContact:"
+ "_blockedSenderManager"
+ "_certificateControllerDidFinish"
+ "_certificateKeychainManager"
+ "_certificateTrustInfo"
+ "_certificateViewController"
+ "_configureSecureMIMEPersonHeaderView:"
+ "_contactViewController"
+ "_currentVIP"
+ "_displayName"
+ "_domain"
+ "_emailAddressSet"
+ "_handleTrustDidChange"
+ "_isBlocked"
+ "_mailProviderDisplayName"
+ "_presentCertificateTrustInfo:"
+ "_removeVIP:"
+ "_setupSubViews"
+ "_startSearch:"
+ "_unblockContact:"
+ "_updateBlockContactCardButtonForViewController:"
+ "_updateContactCardButtonsForViewController:"
+ "_updateHeaderView"
+ "_updateSearchContactCardButtonForViewController:"
+ "_updateVIPContactCardButtonForViewController:"
+ "_viewEncryptionCertificateButtonTapped:"
+ "_viewSigningCertificateButtonTapped:"
+ "_workerScheduler"
+ "addActionWithTitle:target:selector:inGroup:destructive:"
+ "addNotificationObservers"
+ "addTrustException"
+ "addressForSaving"
+ "blockContact:"
+ "blockedSenderManager"
+ "canSaveCertificateToKeychain"
+ "canSearchForContactFromContactCardInteractions:"
+ "cardBottomGroup"
+ "certificateKeychainManager"
+ "certificateType"
+ "certificateViewController"
+ "com.apple.email.MFContactCardInteractions.workerScheduler"
+ "configureInteractionsWithInteractionDelegate:"
+ "contact"
+ "contactCardInteractionWithViewController:blockedSenderManager:"
+ "contactCardInteractions:triggerSearchForDisplayName:emailAddresses:"
+ "contactMessageInteraction:didUpdateHeaderView:"
+ "contactViewController"
+ "contentViewController"
+ "currentVIP"
+ "emailAddressSet"
+ "encryptionCertificateTrustInfo"
+ "hasSeparateSigningAndEncryptionCertificates"
+ "hasTrustException"
+ "initWithFrame:domain:mailProviderDisplayName:"
+ "initWithIdentifier:name:emailAddresses:"
+ "initWithTitle:style:target:action:"
+ "initWithTrust:action:"
+ "initWithViewController:blockedSenderManager:"
+ "installCertificateWithTrustException:"
+ "isBlockedSenderEnabled"
+ "isContactBlocked:"
+ "isMailVIP"
+ "keychainStatus"
+ "learnMoreButtonPressed:"
+ "mailProviderDisplayName"
+ "navigationController"
+ "openURL:options:completionHandler:"
+ "performCertificateActionInstall"
+ "performCertificateActionRemove"
+ "performCertificateActionTrust"
+ "performCertificateActionTrustAndInstall"
+ "performCertificateActionUntrust"
+ "presentingViewController"
+ "presentingViewControllerForMessageInteraction:"
+ "promptOrInstallCertificationWithBlock:"
+ "promptToReplaceCurrentCertificateWithBlock:"
+ "refreshCertificateViewControllerStatus"
+ "removeActionWithTarget:selector:inGroup:"
+ "removeCertificateFromKeychain"
+ "removeTrustException"
+ "saveCertificateToKeychain"
+ "setButtons:"
+ "setCertUIAction:"
+ "setCertificateKeychainManager:"
+ "setCertificateViewController:certificateTrustInfo:"
+ "setContactViewController:"
+ "setCurrentVIP:"
+ "setDirectionalLayoutMargins:"
+ "setDomain:"
+ "setEmailAddressSet:"
+ "setExplanationText:"
+ "setIsBlocked:"
+ "setIsMailVIP:"
+ "setLayoutMarginsRelativeArrangement:"
+ "setMailProviderDisplayName:"
+ "setSecureLabelText:"
+ "setShowCertificateButton:localizedTitle:localizedDescription:destructive:handler:"
+ "setSignedLabelText:"
+ "setSpacing:"
+ "setWarningLabelText:"
+ "shouldShowContactHeader"
+ "stringFromContact:style:"
+ "tableView"
+ "trust"
+ "unblockContact:"
+ "updateCertificateAction"
+ "value"
+ "workerScheduler"
- "\vAd!T*\x19"

```
