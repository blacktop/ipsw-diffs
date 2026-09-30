## AuthenticationServices

> `/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices`

```diff

-622.1.19.10.4
-  __TEXT.__text: 0xe9454
-  __TEXT.__auth_stubs: 0x2320
+622.1.21.10.3
+  __TEXT.__text: 0xe9728
+  __TEXT.__auth_stubs: 0x2310
   __TEXT.__objc_methlist: 0x758c
   __TEXT.__const: 0xec64
-  __TEXT.__gcc_except_tab: 0x13f4
-  __TEXT.__cstring: 0xb3a6
+  __TEXT.__gcc_except_tab: 0x13ec
+  __TEXT.__cstring: 0xb526
   __TEXT.__oslogstring: 0x2ee7
   __TEXT.__dlopen_cstrs: 0x308
-  __TEXT.__ustring: 0x6d1c
+  __TEXT.__ustring: 0x6d4e
   __TEXT.__constg_swiftt: 0x14d8
-  __TEXT.__swift5_typeref: 0x1de0
+  __TEXT.__swift5_typeref: 0x1dfe
   __TEXT.__swift5_reflstr: 0x1333
   __TEXT.__swift5_fieldmd: 0x218c
   __TEXT.__swift5_builtin: 0x190

   __TEXT.__swift5_protos: 0x14
   __TEXT.__unwind_info: 0x4118
   __TEXT.__eh_frame: 0x31b0
-  __TEXT.__objc_classname: 0x1f9f
-  __TEXT.__objc_methname: 0x16235
-  __TEXT.__objc_methtype: 0x40e7
-  __TEXT.__objc_stubs: 0xd200
+  __TEXT.__objc_classname: 0x1fc7
+  __TEXT.__objc_methname: 0x16223
+  __TEXT.__objc_methtype: 0x40ee
+  __TEXT.__objc_stubs: 0xd1c0
   __DATA_CONST.__got: 0xe40
   __DATA_CONST.__const: 0x1aa8
-  __DATA_CONST.__objc_classlist: 0x4d8
+  __DATA_CONST.__objc_classlist: 0x4e0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x48e8
+  __DATA_CONST.__objc_selrefs: 0x48d0
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x348
   __DATA_CONST.__objc_arraydata: 0x170
-  __AUTH_CONST.__auth_got: 0x11a8
-  __AUTH_CONST.__const: 0x5ee0
+  __AUTH_CONST.__auth_got: 0x11a0
+  __AUTH_CONST.__const: 0x6098
   __AUTH_CONST.__cfstring: 0x4560
-  __AUTH_CONST.__objc_const: 0xe618
+  __AUTH_CONST.__objc_const: 0xe668
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH.__objc_data: 0x3440
+  __AUTH.__objc_data: 0x3490
   __AUTH.__data: 0xe90
   __DATA.__objc_ivar: 0x6e0
   __DATA.__data: 0x2ac8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B7F1A2D0-DA37-3C30-81BF-CF9A192ED7E9
-  Functions: 5916
-  Symbols:   10548
-  CStrings:  5369
+  UUID: C78A8A74-B7C7-302D-8AA7-EF569D27CC74
+  Functions: 5921
+  Symbols:   10550
+  CStrings:  5375
 
Symbols:
+ -[ASCredentialRequestConfirmButtonSubPane performPasscodeOrPasswordValidation:]
+ -[ASCredentialRequestPaneViewController updatePreferredContentSizeAndLayoutIfNeeded:allowShrinking:]
+ -[ASCredentialRequestPaneViewController updatePreferredContentSize]
+ -[ASCredentialRequestPaneViewController viewWillTransitionToSize:withTransitionCoordinator:]
+ -[_ASCredentialRequestBasicPaneFooterView intrinsicContentSize]
+ GCC_except_table15
+ GCC_except_table21
+ GCC_except_table41
+ GCC_except_table44
+ GCC_except_table47
+ GCC_except_table50
+ GCC_except_table57
+ GCC_except_table62
+ GCC_except_table67
+ GCC_except_table69
+ GCC_except_table71
+ GCC_except_table79
+ _OBJC_CLASS_$__ASCredentialRequestBasicPaneFooterView
+ _OBJC_METACLASS_$__ASCredentialRequestBasicPaneFooterView
+ __OBJC_$_INSTANCE_METHODS__ASCredentialRequestBasicPaneFooterView
+ __OBJC_CLASS_RO_$__ASCredentialRequestBasicPaneFooterView
+ __OBJC_METACLASS_RO_$__ASCredentialRequestBasicPaneFooterView
+ ___56-[_ASWebsiteNameProvider _initWithShouldLoadQuirksList:]_block_invoke_2
+ ___78-[ASCredentialRequestConfirmButtonSubPane authenticationResult:error:context:]_block_invoke.97
+ ___79-[ASCredentialRequestConfirmButtonSubPane performPasscodeOrPasswordValidation:]_block_invoke
+ ___79-[ASCredentialRequestConfirmButtonSubPane performPasscodeOrPasswordValidation:]_block_invoke_2
+ ___79-[ASCredentialRequestConfirmButtonSubPane performPasscodeOrPasswordValidation:]_block_invoke_2.cold.1
+ ___92-[ASCredentialRequestPaneViewController viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke
+ ___block_literal_global.81
+ ___block_literal_global.96
+ _objc_msgSend$performPasscodeOrPasswordValidation:
+ _objc_msgSend$updatePreferredContentSize
+ _objc_msgSend$updatePreferredContentSizeAndLayoutIfNeeded:allowShrinking:
+ _symbolic Sb16isPasskeyRequest_Sb17multipleProvidersSb26hasCredentialsLoginChoicest
- +[ASCredentialRequestIconGenerator systemSecurityKeysIcon]
- +[ASViewServiceInterfaceUtilities navigationBarHeight]
- +[ASViewServiceInterfaceUtilities otherAccountsCellIconSize]
- +[ASViewServiceInterfaceUtilities otherAccountsCellSizeFactor]
- -[ASCredentialRequestConfirmButtonSubPane _performPasscodeOrPasswordValidation:]
- -[ASCredentialRequestPaneViewController _navigationBarHeaderHeight]
- -[ASNavigationController _adjustedContentSizeForPopover:]
- GCC_except_table13
- GCC_except_table16
- GCC_except_table32
- GCC_except_table42
- GCC_except_table46
- GCC_except_table49
- GCC_except_table51
- GCC_except_table59
- GCC_except_table61
- GCC_except_table68
- GCC_except_table70
- GCC_except_table76
- __UISolariumEnabled
- ___78-[ASCredentialRequestConfirmButtonSubPane authenticationResult:error:context:]_block_invoke.91
- ___80-[ASCredentialRequestConfirmButtonSubPane _performPasscodeOrPasswordValidation:]_block_invoke
- ___80-[ASCredentialRequestConfirmButtonSubPane _performPasscodeOrPasswordValidation:]_block_invoke_2
- ___80-[ASCredentialRequestConfirmButtonSubPane _performPasscodeOrPasswordValidation:]_block_invoke_2.cold.1
- ___block_literal_global.78
- ___block_literal_global.93
- _objc_msgSend$_navigationBarHeaderHeight
- _objc_msgSend$_performPasscodeOrPasswordValidation:
- _objc_msgSend$cellIconSize
- _objc_msgSend$navigationBarHeight
- _objc_msgSend$otherAccountsCellSizeFactor
- _symbolic Sb16isPasskeyRequest_Sb17multipleProviderst
CStrings:
+ "?"
+ "@\"ASAuthorizationPublicKeyCredentialPRFAssertionInputValues\""
+ "Turn On iCloud Keychain"
+ "Turn On iCloud Keychain (Button title)"
+ "You can turn on iCloud Keychain in Settings › Apple Account › iCloud › Passwords and Keychain."
+ "You can turn on iCloud Keychain in Settings › Apple ID › iCloud › Passwords and Keychain."
+ "You may be able to choose a passkey to use from one of the apps listed below."
+ "You may be able to choose a passkey to use from the app below."
+ "You may be able to choose a password to use from one of the apps listed below."
+ "You may be able to choose a password to use from the app below."
+ "_ASCredentialRequestBasicPaneFooterView"
+ "isPasskeyRequest multipleProviders hasCredentialsLoginChoices "
+ "performPasscodeOrPasswordValidation:"
+ "updatePreferredContentSize"
+ "updatePreferredContentSizeAndLayoutIfNeeded:allowShrinking:"
+ "v24@0:8B16B20"
+ "v28@0:8B16@20"
+ "v40@0:8{CGSize=dd}16@32"
+ "viewWillTransitionToSize:withTransitionCoordinator:"
+ "“%@” supports passkeys, a stronger alternative to passwords that cannot be leaked or stolen. A passkey for “%@” will be saved in “%@”."
+ "“%@” supports passkeys, a stronger alternative to passwords that cannot be leaked or stolen. A passkey for “%@” will be saved in “%@”. (app)"
+ "“%@” supports passkeys, a stronger alternative to passwords that cannot be leaked or stolen. A passkey for “%@” will be saved in “%@”. (website)"
- "Open “AutoFill & Passwords”"
- "Turn on iCloud Keychain (Button title)"
- "You can enable iCloud Keychain in Settings › Apple Account › iCloud › Passwords and Keychain."
- "You can enable iCloud Keychain in Settings › Apple ID › iCloud › Passwords and Keychain."
- "_adjustedContentSizeForPopover:"
- "_navigationBarHeaderHeight"
- "_performPasscodeOrPasswordValidation:"
- "isPasskeyRequest multipleProviders "
- "navigationBarHeight"
- "otherAccountsCellIconSize"
- "otherAccountsCellSizeFactor"
- "security.key"
- "systemSecurityKeysIcon"
- "v28@0:8B16Q20"
- "{CGSize=dd}32@0:8{CGSize=dd}16"
- "“%@” supports passkeys, a stronger alternative to passwords that cannot be leaked or stolen. Your passkey will be saved in “%@”."
- "“%@” supports passkeys, a stronger alternative to passwords that cannot be leaked or stolen. Your passkey will be saved in “%@”. (app)"
- "“%@” supports passkeys, a stronger alternative to passwords that cannot be leaked or stolen. Your passkey will be saved in “%@”. (website)"

```
