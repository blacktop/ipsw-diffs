## AuthenticationServices

> `/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices`

```diff

-622.1.16.10.3
-  __TEXT.__text: 0xde488
-  __TEXT.__auth_stubs: 0x2260
-  __TEXT.__objc_methlist: 0x778c
-  __TEXT.__const: 0xda64
-  __TEXT.__gcc_except_tab: 0x13c4
-  __TEXT.__cstring: 0x95f6
+622.1.18.10.3
+  __TEXT.__text: 0xe0ae4
+  __TEXT.__auth_stubs: 0x22c0
+  __TEXT.__objc_methlist: 0x756c
+  __TEXT.__const: 0xde44
+  __TEXT.__gcc_except_tab: 0x13d8
+  __TEXT.__cstring: 0x9646
   __TEXT.__oslogstring: 0x2f97
-  __TEXT.__dlopen_cstrs: 0x2a8
+  __TEXT.__dlopen_cstrs: 0x308
   __TEXT.__ustring: 0x6ee0
-  __TEXT.__constg_swiftt: 0x1324
-  __TEXT.__swift5_typeref: 0x1c38
-  __TEXT.__swift5_reflstr: 0x11e3
-  __TEXT.__swift5_fieldmd: 0x1fa0
-  __TEXT.__swift5_builtin: 0x168
+  __TEXT.__constg_swiftt: 0x1460
+  __TEXT.__swift5_typeref: 0x1c78
+  __TEXT.__swift5_reflstr: 0x1243
+  __TEXT.__swift5_fieldmd: 0x202c
+  __TEXT.__swift5_builtin: 0x17c
   __TEXT.__swift5_assocty: 0x5b8
-  __TEXT.__swift5_proto: 0x634
-  __TEXT.__swift5_types: 0x200
-  __TEXT.__swift5_capture: 0x590
+  __TEXT.__swift5_proto: 0x64c
+  __TEXT.__swift5_types: 0x208
+  __TEXT.__swift5_capture: 0x5b0
   __TEXT.__swift_as_entry: 0xd8
   __TEXT.__swift_as_ret: 0xf8
-  __TEXT.__swift5_mpenum: 0x78
+  __TEXT.__swift5_mpenum: 0x88
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x3ea0
-  __TEXT.__eh_frame: 0x2ee8
-  __TEXT.__objc_classname: 0x1fe7
-  __TEXT.__objc_methname: 0x16385
-  __TEXT.__objc_methtype: 0x40f6
-  __TEXT.__objc_stubs: 0xd8e0
-  __DATA_CONST.__got: 0xe58
-  __DATA_CONST.__const: 0x1af8
-  __DATA_CONST.__objc_classlist: 0x4e0
+  __TEXT.__unwind_info: 0x3fa8
+  __TEXT.__eh_frame: 0x3018
+  __TEXT.__objc_classname: 0x1f9d
+  __TEXT.__objc_methname: 0x1608b
+  __TEXT.__objc_methtype: 0x4097
+  __TEXT.__objc_stubs: 0xd340
+  __DATA_CONST.__got: 0xe40
+  __DATA_CONST.__const: 0x1ac8
+  __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x49f0
+  __DATA_CONST.__objc_selrefs: 0x48b8
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__objc_superrefs: 0x358
+  __DATA_CONST.__objc_superrefs: 0x348
   __DATA_CONST.__objc_arraydata: 0x170
-  __AUTH_CONST.__auth_got: 0x1148
-  __AUTH_CONST.__const: 0x5b58
+  __AUTH_CONST.__auth_got: 0x1178
+  __AUTH_CONST.__const: 0x5c38
   __AUTH_CONST.__cfstring: 0x44c0
-  __AUTH_CONST.__objc_const: 0xe8c8
+  __AUTH_CONST.__objc_const: 0xe5a8
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x3490
-  __AUTH.__data: 0xd20
-  __DATA.__objc_ivar: 0x704
+  __AUTH.__objc_data: 0x3440
+  __AUTH.__data: 0xea0
+  __DATA.__objc_ivar: 0x6d4
   __DATA.__data: 0x29e0
-  __DATA.__bss: 0xb760
+  __DATA.__bss: 0xba90
   __DATA.__common: 0x58
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DD8E2467-D86B-3963-80B7-515AE122E7A0
-  Functions: 5750
-  Symbols:   10661
-  CStrings:  5311
+  UUID: A72FEA61-627B-342D-965F-61098CA162AE
+  Functions: 5786
+  Symbols:   10524
+  CStrings:  5265
 
Symbols:
+ -[ASCredentialRequestCABLEConsentViewController _setUpHeader]
+ -[ASCredentialRequestCABLEConsentViewController _subtitleText]
+ -[ASCredentialRequestConfirmButtonSubPane _initializeAuthorizationButtonAddingButtonPadding:]
+ -[ASCredentialRequestConfirmButtonSubPane initWithActivity:auditTokenData:testOptions:addButtonPadding:]
+ -[ASCredentialRequestEnableBluetoothViewController _setUpHeaderPane]
+ -[ASCredentialRequestPaneContext addHeaderWithConfiguration:]
+ -[ASCredentialRequestSecurityKeyViewController initWithPreferredIcon:mode:serviceName:reinsertSecurityKey:]
+ -[ASCredentialRequestSecurityKeyViewController initWithPresentationContext:reinsertSecurityKey:]
+ -[ASPasswordAuthenticationPaneViewController _addCenteredHeaderView:margins:height:customSpacingAfter:]
+ -[ASPasswordAuthenticationPaneViewController _setUpHeader]
+ -[_ASAgentCredentialExchangeListenerProxy invalidate]
+ _CGRectEqualToRect
+ _OBJC_CLASS_$_ASCredentialRequestPaneHeaderConfiguration
+ _OBJC_IVAR_$_ASPasswordAuthenticationPaneViewController._headerConfiguration
+ _OBJC_METACLASS_$_ASCredentialRequestPaneHeaderConfiguration
+ _PasswordManagerUILibraryCore.frameworkLibrary
+ __DATA_ASCredentialRequestPaneHeaderConfiguration
+ __DATA__TtC22AuthenticationServicesP33_69A77571B0FC9B54CADBF6C775CFD2A245ASCredentialRequestPaneHeaderRawConfiguration
+ __INSTANCE_METHODS_ASCredentialRequestPaneHeaderConfiguration
+ __IVARS_ASCredentialRequestPaneHeaderConfiguration
+ __IVARS__TtC22AuthenticationServicesP33_69A77571B0FC9B54CADBF6C775CFD2A245ASCredentialRequestPaneHeaderRawConfiguration
+ __METACLASS_DATA_ASCredentialRequestPaneHeaderConfiguration
+ __METACLASS_DATA__TtC22AuthenticationServicesP33_69A77571B0FC9B54CADBF6C775CFD2A245ASCredentialRequestPaneHeaderRawConfiguration
+ __OBJC_$_CLASS_METHODS_ASCredentialRequestPaneHeaderConfiguration(Helpers)
+ __PROPERTIES_ASCredentialRequestPaneHeaderConfiguration
+ ___PasswordManagerUILibraryCore_block_invoke
+ ___getPMCredentialRequestPaneHeaderClass_block_invoke
+ ___getPMCredentialRequestPaneHeaderClass_block_invoke.cold.1
+ ___getPMCredentialRequestPaneHeaderClass_block_invoke.cold.2
+ _associated conformance 22AuthenticationServices10ASOsloIconOSHAASQ
+ _associated conformance 22AuthenticationServices45ASCredentialRequestPaneHeaderRawConfiguration33_69A77571B0FC9B54CADBF6C775CFD2A2LLCSHAASQ
+ _associated conformance 22AuthenticationServices9ASAppIconOSHAASQ
+ _audit_stringPasswordManagerUI
+ _getPMCredentialRequestPaneHeaderClass.softClass
+ _get_enum_tag_for_layout_string 22AuthenticationServices10ASOsloIconO
+ _keypath_set.3Tm
+ _objc_msgSend$_addCenteredHeaderView:margins:height:customSpacingAfter:
+ _objc_msgSend$_initializeAuthorizationButtonAddingButtonPadding:
+ _objc_msgSend$_setUpHeader
+ _objc_msgSend$_setUpHeaderPane
+ _objc_msgSend$_signInButtonInsetMargin
+ _objc_msgSend$_subtitleText
+ _objc_msgSend$activateSecurityKeyAgainMessageText
+ _objc_msgSend$addHeaderWithConfiguration:
+ _objc_msgSend$credentialProviderHeaderWithApplicationBundleID:title:subtitle:
+ _objc_msgSend$headerConfiguration
+ _objc_msgSend$initWithActivity:auditTokenData:testOptions:addButtonPadding:
+ _objc_msgSend$initWithHeaderConfiguration:
+ _objc_msgSend$initWithPresentationContext:reinsertSecurityKey:
+ _objc_msgSend$initWithTitle:subtitle:
+ _objc_msgSend$passwordManagerHeaderWithTitle:subtitle:
+ _objc_msgSend$securityKeyHeaderWithIcon:title:subtitle:
+ _objc_msgSend$setSubtitle:
+ _swift_getKeyPath
+ _symbolic SS11serviceName_SS4siteSSSg019proxiedOriginDeviceB0t
+ _symbolic SS4name_So8NSBundleC6bundlet
+ _symbolic Sb16isPasskeyRequest_Sb17multipleProviderst
+ _symbolic So7UIImageC5image_t
+ _symbolic _____ 11Observation0A9RegistrarV
+ _symbolic _____ 22AuthenticationServices10ASOsloIconO
+ _symbolic _____ 22AuthenticationServices45ASCredentialRequestPaneHeaderRawConfiguration33_69A77571B0FC9B54CADBF6C775CFD2A2LLC
+ _symbolic _____4mode_t So45ASCredentialRequestSecurityKeyCredentialsModeV
+ _symbolic _____7service_SS8usernameSSSg12creationDatet 22AuthenticationServices24ASAuthorizationUIContextV7ServiceO
+ _symbolic _____Sg 22AuthenticationServices10ASOsloIconO
+ _symbolic ______AAt 22AuthenticationServices10ASOsloIconO
+ _type_layout_string 22AuthenticationServices10ASOsloIconO
- +[ASCredentialRequestIconGenerator _iconForPresentationContext:size:outIconStyle:]
- +[ASCredentialRequestIconGenerator _systemBiometricsIconForPresentationContext:]
- +[ASCredentialRequestIconGenerator headerIconForPresentationContext:]
- +[ASCredentialRequestIconGenerator headerIconForPresentationContext:outIconStyle:]
- +[ASCredentialRequestImageSubPane _appIconViewWithImage:]
- +[ASCredentialRequestImageSubPane _customIconViewWithImage:]
- +[ASCredentialRequestImageSubPane _imageViewWithImage:imageStyle:]
- +[ASCredentialRequestImageSubPane _systemIconViewWithImage:]
- +[ASCredentialRequestInfoLabelSubPane _bodyFont]
- +[ASCredentialRequestInfoLabelSubPane _bodyTextColor]
- +[ASCredentialRequestInfoLabelSubPane _boldTitleFont]
- +[ASCredentialRequestInfoLabelSubPane _boldTitleTextColor]
- +[ASCredentialRequestInfoLabelSubPane _fontForLabelStyle:]
- +[ASCredentialRequestInfoLabelSubPane _infoLabelMarginInset]
- +[ASCredentialRequestInfoLabelSubPane _infoLabelWithString:labelStyle:]
- +[ASCredentialRequestInfoLabelSubPane _textColorForLabelStyle:]
- -[ASCredentialRequestBasicPaneViewController updateSubtitle:]
- -[ASCredentialRequestCABLEConsentViewController _addHeaderSpacerViewWithCustomSpacingAfter:]
- -[ASCredentialRequestCABLEConsentViewController _setUpIconView]
- -[ASCredentialRequestCABLEConsentViewController _setUpTitleView]
- -[ASCredentialRequestConfirmButtonSubPane _initializeAuthorizationButton]
- -[ASCredentialRequestEnableBluetoothViewController _setUpMessagePane]
- -[ASCredentialRequestEnableBluetoothViewController _setUpTitlePane]
- -[ASCredentialRequestImageSubPane .cxx_destruct]
- -[ASCredentialRequestImageSubPane addToStackView:withCustomSpacingAfter:context:]
- -[ASCredentialRequestImageSubPane imageStyle]
- -[ASCredentialRequestImageSubPane imageView]
- -[ASCredentialRequestImageSubPane initWithImage:]
- -[ASCredentialRequestImageSubPane initWithImage:imageStyle:]
- -[ASCredentialRequestImageSubPane setImage:]
- -[ASCredentialRequestInfoLabelSubPane .cxx_destruct]
- -[ASCredentialRequestInfoLabelSubPane initWithString:labelStyle:]
- -[ASCredentialRequestInfoLabelSubPane initWithString:labelType:]
- -[ASCredentialRequestInfoLabelSubPane marginInset]
- -[ASCredentialRequestInfoLabelSubPane setMarginInset:]
- -[ASCredentialRequestInfoLabelSubPane setText:]
- -[ASCredentialRequestInfoLabelSubPane text]
- -[ASCredentialRequestPaneContext _boldTitle_customSpacingAfterTitle]
- -[ASCredentialRequestPaneContext _boldTitle_stackViewTopSpacing]
- -[ASCredentialRequestPaneContext _customSpacingAfterIcon]
- -[ASCredentialRequestPaneContext _customSpacingAfterSubtitle]
- -[ASCredentialRequestPaneContext _customSpacingAfterTitle]
- -[ASCredentialRequestPaneContext _stackViewTopSpacing]
- -[ASCredentialRequestPaneContext _useBoldTitleLayout]
- -[ASCredentialRequestPaneContext addIcon:iconStyle:title:titleStyle:subtitlePane:subtitleStyle:subtitleBottomSpacing:]
- -[ASCredentialRequestSecurityKeyViewController initWithPreferredIcon:mode:serviceName:]
- -[ASPasswordAuthenticationPaneViewController _containerViewHorizontalMargin]
- -[ASPasswordAuthenticationPaneViewController _setUpAndAddIconImage]
- -[ASPasswordAuthenticationPaneViewController _setUpSubtitleLabel]
- -[ASPasswordAuthenticationPaneViewController _topViewMargin]
- _OBJC_CLASS_$_ASCredentialRequestBasicPaneViewControllerConfiguration
- _OBJC_CLASS_$_ASCredentialRequestImageSubPane
- _OBJC_CLASS_$_ASCredentialRequestInfoLabelSubPane
- _OBJC_CLASS_$_NSConstantDoubleNumber
- _OBJC_IVAR_$_ASCredentialRequestBasicPaneViewController._subtitleSubPane
- _OBJC_IVAR_$_ASCredentialRequestImageSubPane._imageStyle
- _OBJC_IVAR_$_ASCredentialRequestImageSubPane._imageView
- _OBJC_IVAR_$_ASCredentialRequestInfoLabelSubPane._infoLabel
- _OBJC_IVAR_$_ASCredentialRequestInfoLabelSubPane._marginInset
- _OBJC_IVAR_$_ASCredentialRequestPaneContext._icon
- _OBJC_IVAR_$_ASCredentialRequestPaneContext._iconStyle
- _OBJC_IVAR_$_ASCredentialRequestPaneContext._subtitleStyle
- _OBJC_IVAR_$_ASCredentialRequestPaneContext._subtitleSubPane
- _OBJC_IVAR_$_ASCredentialRequestPaneContext._title
- _OBJC_IVAR_$_ASCredentialRequestPaneContext._titleStyle
- _OBJC_IVAR_$_ASPasswordAuthenticationPaneViewController._subtitleLabel
- _OBJC_IVAR_$_ASPasswordAuthenticationPaneViewController._titleLabel
- _OBJC_METACLASS_$_ASCredentialRequestBasicPaneViewControllerConfiguration
- _OBJC_METACLASS_$_ASCredentialRequestImageSubPane
- _OBJC_METACLASS_$_ASCredentialRequestInfoLabelSubPane
- _UIFontTextStyleHeadline
- _UIFontWeightMedium
- __CLASS_METHODS_ASCredentialRequestBasicPaneViewControllerConfiguration
- __DATA_ASCredentialRequestBasicPaneViewControllerConfiguration
- __INSTANCE_METHODS_ASCredentialRequestBasicPaneViewControllerConfiguration
- __IVARS_ASCredentialRequestBasicPaneViewControllerConfiguration
- __METACLASS_DATA_ASCredentialRequestBasicPaneViewControllerConfiguration
- __OBJC_$_CLASS_METHODS_ASCredentialRequestImageSubPane
- __OBJC_$_CLASS_METHODS_ASCredentialRequestInfoLabelSubPane
- __OBJC_$_INSTANCE_METHODS_ASCredentialRequestImageSubPane
- __OBJC_$_INSTANCE_METHODS_ASCredentialRequestInfoLabelSubPane
- __OBJC_$_INSTANCE_VARIABLES_ASCredentialRequestImageSubPane
- __OBJC_$_INSTANCE_VARIABLES_ASCredentialRequestInfoLabelSubPane
- __OBJC_$_PROP_LIST_ASCredentialRequestImageSubPane
- __OBJC_$_PROP_LIST_ASCredentialRequestInfoLabelSubPane
- __OBJC_CLASS_RO_$_ASCredentialRequestImageSubPane
- __OBJC_CLASS_RO_$_ASCredentialRequestInfoLabelSubPane
- __OBJC_METACLASS_RO_$_ASCredentialRequestImageSubPane
- __OBJC_METACLASS_RO_$_ASCredentialRequestInfoLabelSubPane
- __PROPERTIES_ASCredentialRequestBasicPaneViewControllerConfiguration
- ___swift_memcpy57_8
- _isUserVerificationConfigured
- _keypath_get_selector_icon
- _keypath_get_selector_iconStyle
- _keypath_get_selector_subtitleStyle
- _keypath_get_selector_titleStyle
- _objc_msgSend$_addHeaderSpacerViewWithCustomSpacingAfter:
- _objc_msgSend$_appIconViewWithImage:
- _objc_msgSend$_bodyFont
- _objc_msgSend$_bodyTextColor
- _objc_msgSend$_boldTitleFont
- _objc_msgSend$_boldTitleTextColor
- _objc_msgSend$_boldTitle_customSpacingAfterTitle
- _objc_msgSend$_boldTitle_stackViewTopSpacing
- _objc_msgSend$_containerViewHorizontalMargin
- _objc_msgSend$_customIconViewWithImage:
- _objc_msgSend$_customSpacingAfterIcon
- _objc_msgSend$_customSpacingAfterSubtitle
- _objc_msgSend$_customSpacingAfterTitle
- _objc_msgSend$_fontForLabelStyle:
- _objc_msgSend$_iconForPresentationContext:size:outIconStyle:
- _objc_msgSend$_imageViewWithImage:imageStyle:
- _objc_msgSend$_infoLabelMarginInset
- _objc_msgSend$_infoLabelWithString:labelStyle:
- _objc_msgSend$_initializeAuthorizationButton
- _objc_msgSend$_setUpAndAddIconImage
- _objc_msgSend$_setUpIconView
- _objc_msgSend$_setUpMessagePane
- _objc_msgSend$_setUpSubtitleLabel
- _objc_msgSend$_setUpTitlePane
- _objc_msgSend$_stackViewTopSpacing
- _objc_msgSend$_subtitleLabelFont
- _objc_msgSend$_systemBiometricsIconForPresentationContext:
- _objc_msgSend$_systemIconViewWithImage:
- _objc_msgSend$_textColorForLabelStyle:
- _objc_msgSend$_titleLabelFont
- _objc_msgSend$_titleLabelTextColor
- _objc_msgSend$_topViewMargin
- _objc_msgSend$_useBoldTitleLayout
- _objc_msgSend$addIcon:iconStyle:title:titleStyle:subtitlePane:subtitleStyle:subtitleBottomSpacing:
- _objc_msgSend$alternativeSecurityKeysIcon
- _objc_msgSend$canEvaluatePolicy:error:
- _objc_msgSend$externalPasskeyLoginChoiceCount
- _objc_msgSend$floatValue
- _objc_msgSend$hasPlatformCredentialRequest
- _objc_msgSend$headerIconCornerRadius
- _objc_msgSend$headerIconForPresentationContext:outIconStyle:
- _objc_msgSend$headerIconSize
- _objc_msgSend$headerMessageColor
- _objc_msgSend$iCloudKeychainPasskeyLoginChoiceCount
- _objc_msgSend$icon
- _objc_msgSend$iconBorderColor
- _objc_msgSend$iconBorderWidth
- _objc_msgSend$iconStyle
- _objc_msgSend$imageWithSymbolConfiguration:
- _objc_msgSend$initWithImage:imageStyle:
- _objc_msgSend$initWithString:labelStyle:
- _objc_msgSend$initWithString:labelType:
- _objc_msgSend$initWithTitle:subtitle:icon:iconStyle:
- _objc_msgSend$initWithTitle:titleStyle:subtitle:subtitleStyle:icon:iconStyle:
- _objc_msgSend$isCABLEAuthenticatorRequest
- _objc_msgSend$requestTypes
- _objc_msgSend$subtitle
- _objc_msgSend$subtitleStyle
- _objc_msgSend$systemPasskeyIcon
- _objc_msgSend$systemSecurityKeysIcon
- _objc_msgSend$titleLabelText
- _objc_msgSend$titleStyle
- _objc_retain_x28
- _symbolic SS11serviceName_SS4siteSSSg019proxiedOriginDeviceB0So7UIImageCSg4icont
- _symbolic Sb14isCABLERequest_Sb17multipleProviderst
- _symbolic So7UIImageCSg
- _symbolic _____4mode_Sb18useAlternativeIcont So45ASCredentialRequestSecurityKeyCredentialsModeV
- _symbolic _____7service_SS8usernamet 22AuthenticationServices24ASAuthorizationUIContextV7ServiceO
- _symbolic _____Sg_ABt So55ASPasswordAuthenticationPaneViewControllerConfigurationC0B8ServicesE13ContentFields33_4AD42645A6C55D1DE304DC57F60A33AALLO
CStrings:
+ "@\"ASCredentialRequestPaneHeaderConfiguration\""
+ "@28@0:8B16q20"
+ "@36@0:8B16q20q28"
+ "@44@0:8@16@24@32B40"
+ "@44@0:8q16q24@32B40"
+ "@56@0:8@16d24@32@40@48"
+ "ASCredentialRequestPaneContext.m"
+ "ASCredentialRequestPaneHeaderConfiguration"
+ "Class getPMCredentialRequestPaneHeaderClass(void)_block_invoke"
+ "Do you want to sign in to “%@” with your password saved on %@? (app)"
+ "Do you want to sign in to “%@” with your password saved on %@? (website)"
+ "Helpers"
+ "PMCredentialRequestPaneHeader"
+ "Sign in to “%@” with your password saved on %@?"
+ "You should only connect to the other device if you scanned a QR code in order to save a passkey."
+ "You should only connect to the other device if you scanned a QR code in order to sign in with a passkey."
+ "You should only connect to the other device if you scanned a QR code in order to sign in with or save a passkey."
+ "Your iPad needs to connect to this device in order to save a passkey."
+ "Your iPad needs to connect to this device in order to sign in with a passkey."
+ "Your iPad needs to connect to this device in order to sign in with or save a passkey."
+ "Your iPhone needs to connect to this device in order to save a passkey."
+ "Your iPhone needs to connect to this device in order to sign in with a passkey."
+ "Your iPhone needs to connect to this device in order to sign in with or save a passkey."
+ "_$observationRegistrar"
+ "_TtC22AuthenticationServicesP33_69A77571B0FC9B54CADBF6C775CFD2A245ASCredentialRequestPaneHeaderRawConfiguration"
+ "_addCenteredHeaderView:margins:height:customSpacingAfter:"
+ "_headerConfiguration"
+ "_initializeAuthorizationButtonAddingButtonPadding:"
+ "_setUpHeader"
+ "_setUpHeaderPane"
+ "_subtitleText"
+ "addHeaderWithConfiguration:"
+ "credentialProviderHeaderWithApplicationBundleID:title:subtitle:"
+ "exclamationmark.triangle"
+ "headerConfiguration"
+ "initWithActivity:auditTokenData:testOptions:addButtonPadding:"
+ "initWithHeaderConfiguration:"
+ "initWithManualPasswordEntryForCredentialProviderWithApplicationBundleID:site:serviceName:proxiedOriginDeviceName:"
+ "initWithManualPasswordEntryForCredentialProviderWithProxiedIconData:proxiedIconScale:site:serviceName:proxiedOriginDeviceName:"
+ "initWithManualPasswordEntryForPasswordManagerWithSite:serviceName:proxiedOriginDeviceName:"
+ "initWithPreferredIcon:mode:serviceName:reinsertSecurityKey:"
+ "initWithPresentationContext:reinsertSecurityKey:"
+ "initWithSecurityKeyEntryForNewPIN:mode:"
+ "initWithSecurityKeyEntryForNewPIN:mode:preferredIcon:"
+ "initWithTitle:subtitle:"
+ "isPasskeyRequest"
+ "isPasskeyRequest multipleProviders "
+ "passwordManagerHeaderWithTitle:subtitle:"
+ "rawConfiguration"
+ "securityKeyHeaderWithIcon:title:subtitle:"
+ "signInFailedErrorWithSubtitle:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI"
+ "v48@0:8@16d24d32d40"
+ "void *PasswordManagerUILibrary(void)"
+ "\x91"
- "@\"ASCredentialRequestBasicPaneViewControllerConfiguration\""
- "@\"ASCredentialRequestInfoLabelSubPane\""
- "@32@0:8@16Q24"
- "@32@0:8@16^q24"
- "@32@0:8B16q20B28"
- "@40@0:8q16q24@32"
- "@48@0:8@16{CGSize=dd}24^q40"
- "@64@0:8@16q24@32q40@48q56"
- "ASCredentialRequestBasicPaneViewControllerConfiguration"
- "ASCredentialRequestImageSubPane"
- "ASCredentialRequestInfoLabelSubPane"
- "AuthenticationServices_Private.ASCredentialRequestBasicPaneViewControllerConfiguration"
- "T@\"UIImage\",N,&,Vicon"
- "T@\"UIImage\",N,R"
- "T@\"UIImageView\",R,N,V_imageView"
- "Td,N,V_marginInset"
- "Tq,N,ViconStyle"
- "Tq,N,VsubtitleStyle"
- "Tq,N,VtitleStyle"
- "Tq,R,N,V_imageStyle"
- "Your iPad needs to connect to this device in order to save a passkey.\n\nYou should only connect to the other device if you scanned a QR code in order to save a passkey."
- "Your iPad needs to connect to this device in order to sign in with a passkey.\n\nYou should only connect to the other device if you scanned a QR code in order to sign in with a passkey."
- "Your iPad needs to connect to this device in order to sign in with or save a passkey.\n\nYou should only connect to the other device if you scanned a QR code in order to sign in with or save a passkey."
- "Your iPhone needs to connect to this device in order to save a passkey.\n\nYou should only connect to the other device if you scanned a QR code in order to save a passkey."
- "Your iPhone needs to connect to this device in order to sign in with a passkey.\n\nYou should only connect to the other device if you scanned a QR code in order to sign in with a passkey."
- "Your iPhone needs to connect to this device in order to sign in with or save a passkey.\n\nYou should only connect to the other device if you scanned a QR code in order to sign in with or save a passkey."
- "_addHeaderSpacerViewWithCustomSpacingAfter:"
- "_appIconViewWithImage:"
- "_bodyFont"
- "_bodyTextColor"
- "_boldTitleFont"
- "_boldTitleTextColor"
- "_boldTitle_customSpacingAfterTitle"
- "_boldTitle_stackViewTopSpacing"
- "_containerViewHorizontalMargin"
- "_customIconViewWithImage:"
- "_customSpacingAfterIcon"
- "_customSpacingAfterSubtitle"
- "_customSpacingAfterTitle"
- "_fontForLabelStyle:"
- "_iconForPresentationContext:size:outIconStyle:"
- "_iconStyle"
- "_imageStyle"
- "_imageViewWithImage:imageStyle:"
- "_infoLabel"
- "_infoLabelMarginInset"
- "_infoLabelWithString:labelStyle:"
- "_initializeAuthorizationButton"
- "_marginInset"
- "_setUpAndAddIconImage"
- "_setUpIconView"
- "_setUpMessagePane"
- "_setUpSubtitleLabel"
- "_setUpTitlePane"
- "_stackViewTopSpacing"
- "_subtitleLabel"
- "_subtitleStyle"
- "_subtitleSubPane"
- "_systemBiometricsIconForPresentationContext:"
- "_systemIconViewWithImage:"
- "_textColorForLabelStyle:"
- "_titleStyle"
- "_topViewMargin"
- "_useBoldTitleLayout"
- "a"
- "addIcon:iconStyle:title:titleStyle:subtitlePane:subtitleStyle:subtitleBottomSpacing:"
- "externalPasskeyLoginChoiceCount"
- "floatValue"
- "hasPlatformCredentialRequest"
- "headerIconForPresentationContext:"
- "headerIconForPresentationContext:outIconStyle:"
- "iCloudKeychainPasskeyLoginChoiceCount"
- "iconStyle"
- "imageStyle"
- "imageView"
- "imageWithSymbolConfiguration:"
- "initWithImage:imageStyle:"
- "initWithManualPasswordEntryForSite:serviceName:proxiedOriginDeviceName:icon:"
- "initWithPreferredIcon:mode:serviceName:"
- "initWithSecurityKeyEntryForNewPIN:mode:useAlternativeIcon:"
- "initWithString:labelStyle:"
- "initWithString:labelType:"
- "initWithTitle:subtitle:icon:iconStyle:"
- "initWithTitle:titleStyle:subtitle:subtitleStyle:icon:iconStyle:"
- "isCABLERequest multipleProviders "
- "marginInset"
- "setIcon:"
- "setIconStyle:"
- "setMarginInset:"
- "setSubtitleStyle:"
- "setTitleStyle:"
- "signInFailedErrorWithPresentationContext:subtitle:"
- "subtitleStyle"
- "titleLabelText"
- "titleStyle"
- "updateSubtitle:"
- "v72@0:8@16q24@32q40@48q56@64"
- "\xa1"

```
