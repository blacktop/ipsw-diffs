## AutoFillUI

> `/System/Library/PrivateFrameworks/AutoFillUI.framework/AutoFillUI`

```diff

-71.301.0.0.0
-  __TEXT.__text: 0x20b4c
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_methlist: 0x3500
-  __TEXT.__const: 0x118
-  __TEXT.__cstring: 0x197f
-  __TEXT.__gcc_except_tab: 0x748
-  __TEXT.__ustring: 0xdc
-  __TEXT.__dlopen_cstrs: 0x162
+83.0.0.0.0
+  __TEXT.__text: 0x212cc
+  __TEXT.__auth_stubs: 0x680
+  __TEXT.__objc_methlist: 0x3588
+  __TEXT.__const: 0xf0
+  __TEXT.__cstring: 0x1906
+  __TEXT.__gcc_except_tab: 0x790
+  __TEXT.__ustring: 0xe6
+  __TEXT.__dlopen_cstrs: 0x14e
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x8d0
-  __TEXT.__objc_classname: 0x553
-  __TEXT.__objc_methname: 0x9ce6
-  __TEXT.__objc_methtype: 0x2e71
-  __TEXT.__objc_stubs: 0x5dc0
-  __DATA_CONST.__got: 0x5c8
-  __DATA_CONST.__const: 0x988
+  __TEXT.__unwind_info: 0x890
+  __TEXT.__objc_classname: 0x554
+  __TEXT.__objc_methname: 0x9e1b
+  __TEXT.__objc_methtype: 0x2ec9
+  __TEXT.__objc_stubs: 0x5de0
+  __DATA_CONST.__got: 0x5f8
+  __DATA_CONST.__const: 0x9a0
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25d8
+  __DATA_CONST.__objc_selrefs: 0x2630
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__auth_got: 0x340
-  __AUTH_CONST.__const: 0x440
-  __AUTH_CONST.__cfstring: 0x1840
-  __AUTH_CONST.__objc_const: 0x6b20
+  __AUTH_CONST.__auth_got: 0x350
+  __AUTH_CONST.__const: 0x420
+  __AUTH_CONST.__cfstring: 0x1720
+  __AUTH_CONST.__objc_const: 0x6bc0
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x230
+  __DATA.__objc_ivar: 0x234
   __DATA.__data: 0xaf0
   __DATA.__bss: 0x111
   __DATA_DIRTY.__objc_data: 0x1e0

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TextInput.framework/TextInput
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8E08654C-1640-3CD5-9B4B-B728C44D27FB
-  Functions: 821
-  Symbols:   3456
+  UUID: 256790EB-6875-3F86-B8FD-2516B133D613
+  Functions: 819
+  Symbols:   3460
   CStrings:  2324
 
Symbols:
+ -[AFCreditCard image]
+ -[AFCreditCard initWithName:number:expiration:securityCode:type:icon:nickname:suffix:]
+ -[AFCreditCard setImage:]
+ -[AFUICreditCardViewController createSectionHeaderViewWithTitle:icon:]
+ GCC_except_table23
+ _CGImageGetHeight
+ _CGImageGetWidth
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_IVAR_$_AFCreditCard._image
+ _PassKitCoreLibraryCore.frameworkLibrary
+ _UIContentSizeCategoryExtraLarge
+ _UIFontTextStyleBody
+ _UIFontTextStyleFootnote
+ _UIFontTextStyleHeadline
+ _UIFontTextStyleSubheadline
+ ___73-[AFUIAutoFillCreditCardController _performTextOperationsWithSuggestion:]_block_invoke_4
+ ___PassKitCoreLibraryCore_block_invoke
+ ___block_descriptor_48_e8_32s40s_e19_v20?0B8"NSData"12ls32l8s40l8
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e19_v20?0B8"NSData"12ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.245
+ ___block_literal_global.251
+ ___getPKAutoFillCardManagerClass_block_invoke
+ _audit_stringPassKitCore
+ _getPKAutoFillCardManagerClass.softClass
+ _objc_msgSend$_preferredFontForTextStyle:maximumContentSizeCategory:
+ _objc_msgSend$authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:
+ _objc_msgSend$authenticateIfNecessaryForSuggestion:documentTraits:withCompletionHandler:
+ _objc_msgSend$constraintEqualToConstant:
+ _objc_msgSend$createSectionHeaderViewWithTitle:icon:
+ _objc_msgSend$defaultWorkspace
+ _objc_msgSend$generateAutoFillSuggestionsWithAutoFillMode:textPrefix:documentTraits:externalizedContext:completionHandler:
+ _objc_msgSend$image
+ _objc_msgSend$imageWithCGImage:
+ _objc_msgSend$initWithName:number:expiration:securityCode:type:icon:nickname:suffix:
+ _objc_msgSend$openSensitiveURL:withOptions:
+ _objc_msgSend$setContentHorizontalAlignment:
+ _objc_msgSend$setLineBreakMode:
+ _objc_msgSend$systemBlueColor
+ _objc_msgSend$systemGroupedBackgroundColor
+ _objc_msgSend$urlToListOfCards
- -[AFCreditCard initWithName:number:expiration:securityCode:type:nickname:suffix:]
- -[AFUICreditCardViewController cardIconNameForCreditCard:]
- -[AFUICreditCardViewController createSectionHeaderViewWithTitle:iconName:]
- GCC_except_table21
- _SafariFoundationLibraryCore.frameworkLibrary
- ___43-[AFUICreditCardViewController viewDidLoad]_block_invoke
- ___55-[AFUIExplicitAutoFillController _generateSuggestions:]_block_invoke_5
- ___55-[AFUIExplicitAutoFillController _generateSuggestions:]_block_invoke_6
- ___SafariFoundationLibraryCore_block_invoke
- ___block_descriptor_32_e36_"UIColor"16?0"UITraitCollection"8l
- ___block_descriptor_48_e8_32s40s_e8_v12?0B8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls32l8s48l8s40l8
- ___block_literal_global.16
- ___block_literal_global.243
- ___block_literal_global.249
- ___getSFSafariCreditCardStoreClass_block_invoke
- ___getSFSafariCreditCardStoreClass_block_invoke.cold.1
- _audit_stringSafariFoundation
- _getSFSafariCreditCardStoreClass.softClass
- _objc_msgSend$authenticateIfNecessaryForSuggestion:documentTraits:completionHandler:
- _objc_msgSend$boldSystemFontOfSize:
- _objc_msgSend$capitalizedString
- _objc_msgSend$cardIconNameForCreditCard:
- _objc_msgSend$colorWithDynamicProvider:
- _objc_msgSend$createSectionHeaderViewWithTitle:iconName:
- _objc_msgSend$generateAutoFillSuggestionsWithAutoFillMode:textPrefix:documentTraits:completionHandler:
- _objc_msgSend$imageNamed:inBundle:compatibleWithTraitCollection:
- _objc_msgSend$initWithName:number:expiration:securityCode:type:nickname:suffix:
- _objc_msgSend$shouldAcceptSuggestion:completionHandler:
- _objc_msgSend$showCreditCardSettings
- _objc_msgSend$systemBackgroundColor
- _objc_msgSend$systemFontOfSize:
- _objc_msgSend$uppercaseString
- _objc_msgSend$userInterfaceStyle
CStrings:
+ "\" \" \" \" "
+ "@32@0:8@16^{CGImage=}24"
+ "@80@0:8@16@24@32@40@48^{CGImage=}56@64@72"
+ "AutoFill Card Information"
+ "Choose a Credit or Debit Card to AutoFill."
+ "Manage Cards"
+ "PKAutoFillCardManager"
+ "T^{CGImage=},N,V_image"
+ "Wallet"
+ "WalletFPANUpdates"
+ "^{CGImage=}"
+ "^{CGImage=}16@0:8"
+ "_image"
+ "_preferredFontForTextStyle:maximumContentSizeCategory:"
+ "afui_cc_detection_in_apps"
+ "alignCenter:"
+ "alignJustified:"
+ "alignLeft:"
+ "alignRight:"
+ "authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:"
+ "authenticateIfNecessaryForSuggestion:documentTraits:withCompletionHandler:"
+ "cc-art"
+ "constraintEqualToConstant:"
+ "createSectionHeaderViewWithTitle:icon:"
+ "defaultWorkspace"
+ "generateAutoFillSuggestionsWithAutoFillMode:textPrefix:documentTraits:externalizedContext:completionHandler:"
+ "image"
+ "imageWithCGImage:"
+ "initWithName:number:expiration:securityCode:type:icon:nickname:suffix:"
+ "newFromPasteboard:"
+ "openSensitiveURL:withOptions:"
+ "performClose:"
+ "selectionContainerViewAboveText"
+ "selectionContainerViewBelowText"
+ "setContentHorizontalAlignment:"
+ "setLineBreakMode:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore"
+ "systemBlueColor"
+ "systemGroupedBackgroundColor"
+ "toggleInspector:"
+ "toggleSidebar:"
+ "urlToListOfCards"
+ "v20@?0B8@\"NSData\"12"
+ "v24@0:8^{CGImage=}16"
- "@\"UIColor\"16@?0@\"UITraitCollection\"8"
- "@72@0:8@16@24@32@40@48@56@64"
- "American Express"
- "AutoFill Credit Card"
- "Choose a credit card to AutoFill."
- "CreditCardAmex"
- "CreditCardDiscover"
- "CreditCardGeneric"
- "CreditCardJCB"
- "CreditCardMasterCard"
- "CreditCardVisa"
- "Discover"
- "JCB"
- "Manage Credit Cards..."
- "Mastercard"
- "SFSafariCreditCardStore"
- "Visa"
- "afui_cc_in_apps"
- "authenticateIfNecessaryForSuggestion:documentTraits:completionHandler:"
- "boldSystemFontOfSize:"
- "capitalizedString"
- "cardIconNameForCreditCard:"
- "colorWithDynamicProvider:"
- "createSectionHeaderViewWithTitle:iconName:"
- "generateAutoFillSuggestionsWithAutoFillMode:textPrefix:documentTraits:completionHandler:"
- "imageNamed:inBundle:compatibleWithTraitCollection:"
- "initWithName:number:expiration:securityCode:type:nickname:suffix:"
- "shouldAcceptSuggestion:completionHandler:"
- "showCreditCardSettings"
- "softlink:r:path:/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation"
- "systemBackgroundColor"
- "systemFontOfSize:"
- "uppercaseString"
- "userInterfaceStyle"

```
