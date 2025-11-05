## OnBoardingKit

> `/System/iOSSupport/System/Library/PrivateFrameworks/OnBoardingKit.framework/Versions/A/OnBoardingKit`

```diff

-3934.1.0.0.0
-  __TEXT.__text: 0x2f64c
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_methlist: 0x4078
-  __TEXT.__const: 0x4f6
-  __TEXT.__cstring: 0x16dd
-  __TEXT.__oslogstring: 0x7e9
+3941.3.0.0.0
+  __TEXT.__text: 0x30954
+  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__objc_methlist: 0x47b4
+  __TEXT.__const: 0x566
+  __TEXT.__cstring: 0x174d
+  __TEXT.__oslogstring: 0xafa
   __TEXT.__ustring: 0x4
-  __TEXT.__gcc_except_tab: 0x30
+  __TEXT.__gcc_except_tab: 0x80
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xbb8
-  __TEXT.__objc_classname: 0x8c3
-  __TEXT.__objc_methname: 0xb316
-  __TEXT.__objc_methtype: 0x1019
-  __TEXT.__objc_stubs: 0x87c0
-  __DATA_CONST.__got: 0x3c8
-  __DATA_CONST.__const: 0x5e0
+  __TEXT.__unwind_info: 0xbf8
+  __TEXT.__objc_classname: 0x8d6
+  __TEXT.__objc_methname: 0xbca0
+  __TEXT.__objc_methtype: 0x148b
+  __TEXT.__objc_stubs: 0x8a80
+  __DATA_CONST.__got: 0x3e0
+  __DATA_CONST.__const: 0x628
   __DATA_CONST.__objc_classlist: 0x288
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x70
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29d0
+  __DATA_CONST.__objc_selrefs: 0x2dc8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0xa0
-  __AUTH_CONST.__auth_got: 0x368
+  __AUTH_CONST.__auth_got: 0x388
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x1dc0
-  __AUTH_CONST.__objc_const: 0xa040
+  __AUTH_CONST.__cfstring: 0x1e40
+  __AUTH_CONST.__objc_const: 0x9cf0
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x10e0
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x4bc
-  __DATA.__data: 0x540
+  __DATA.__objc_ivar: 0x4c0
+  __DATA.__data: 0x5a0
   __DATA.__bss: 0x78
   __DATA.__common: 0x60
   __DATA_DIRTY.__objc_data: 0x820

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 91CB803A-F604-3E2F-B2C1-CA33D2817B6B
-  Functions: 1363
-  Symbols:   3845
-  CStrings:  2742
+  UUID: CECCBCAF-B70B-3B05-98FF-B62DD95EA3AB
+  Functions: 1382
+  Symbols:   3912
+  CStrings:  2850
 
Symbols:
+ +[OBAnalyticsManager sharedManager].cold.1
+ +[OBBundleManager sharedManager].cold.1
+ +[OBCapabilities sharedCapabilities].cold.1
+ +[OBDevice currentDevice].cold.1
+ +[OBViewUtilities _isNavigationItemEligibleForCustomization:usingHeaderView:]
+ +[OBViewUtilities _setBackButtonTitleOnNavigationItem:usingHeaderView:isHeaderViewVisible:]
+ +[OBViewUtilities shouldUpdateAlphaForNavigationItem:andHeaderView:inScrollView:]
+ +[OBViewUtilities updateAlphaForNavigationItem:andHeaderView:usingNavigationTitleAlpha:animated:]
+ -[OBBaseWelcomeController insetsForTemplateType:].cold.1
+ -[OBCapabilities _eligibilityContextHasCountryPolicyChina:]
+ -[OBCapabilities _eligibilityCountryPolicyStringIsChina:]
+ -[OBCapabilities eligibilityForGreymatterHasCountryPolicyChina]
+ -[OBCapabilities eligibilityForGreymatterHasCountryPolicyChina].cold.1
+ -[OBCapabilities isWAPI].cold.1
+ -[OBCapabilities overrideEligibilityForGreymatterHasCountryPolicyChina]
+ -[OBCapabilities setOverrideEligibilityForGreymatterHasCountryPolicyChina:]
+ -[OBPrivacyFlow _bestStringConsideringCMEChinaForKeyWithPrefix:language:preferredDeviceType:withGenerativeSuffix:]
+ -[OBPrivacyFlow _bestStringConsideringGenerativeForKeyWithPrefix:language:preferredDeviceType:]
+ -[OBPrivacyFlow _bestStringConsideringNetworkForKeyWithPrefix:language:preferredDeviceType:withGenerativeSuffix:withGMEChinaSuffix:]
+ -[OBPrivacyFlow _stringForKeyWithPrefix:language:preferredDeviceType:withGenerativeSuffix:withGMEChinaSuffix:withNetworkSuffix:]
+ -[OBPrivacyFlow _stringKeyWithCapabilitiesFromPrefix:withNetwork:withGenerative:withGMEChinaSuffix:]
+ -[OBPrivacySplashListView textView:primaryActionForTextItem:defaultAction:]
+ GCC_except_table13
+ GCC_except_table8
+ OBJC_IVAR_$_OBCapabilities._overrideEligibilityForGreymatterHasCountryPolicyChina
+ _OBJC_CLASS_$_UIAction
+ _OBJC_CLASS_$_UITraitDisplayScale
+ _OBLogFile.cold.1
+ _OBLoggingFacility.cold.1
+ _UIContentSizeCategoryMedium
+ __75-[OBPrivacySplashListView textView:primaryActionForTextItem:defaultAction:]_block_invoke.16
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UITextViewDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UITextViewDelegate
+ __OBJC_$_PROTOCOL_REFS_UITextViewDelegate
+ __OBJC_CLASS_PROTOCOLS_$_OBPrivacySplashListView
+ __OBJC_LABEL_PROTOCOL_$_UITextViewDelegate
+ __OBJC_PROTOCOL_$_UITextViewDelegate
+ ___75-[OBPrivacySplashListView textView:primaryActionForTextItem:defaultAction:]_block_invoke
+ ___97+[OBViewUtilities updateAlphaForNavigationItem:andHeaderView:usingNavigationTitleAlpha:animated:]_block_invoke
+ ___97+[OBViewUtilities updateAlphaForNavigationItem:andHeaderView:usingNavigationTitleAlpha:animated:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e18_v16?0"UIAction"8ls32l8
+ ___block_descriptor_40_e8_32s_e8_v12?0B8ls32l8
+ ___block_descriptor_57_e8_32s40s_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s_e5_v8?0ls32l8s40l8
+ _objc_msgSend$_bestStringConsideringCMEChinaForKeyWithPrefix:language:preferredDeviceType:withGenerativeSuffix:
+ _objc_msgSend$_bestStringConsideringGenerativeForKeyWithPrefix:language:preferredDeviceType:
+ _objc_msgSend$_bestStringConsideringNetworkForKeyWithPrefix:language:preferredDeviceType:withGenerativeSuffix:withGMEChinaSuffix:
+ _objc_msgSend$_eligibilityContextHasCountryPolicyChina:
+ _objc_msgSend$_eligibilityCountryPolicyStringIsChina:
+ _objc_msgSend$_fontAdjustedForContentSizeCategoryCompatibleWithTraitCollection:
+ _objc_msgSend$_isNavigationItemEligibleForCustomization:usingHeaderView:
+ _objc_msgSend$_setBackButtonTitleOnNavigationItem:usingHeaderView:isHeaderViewVisible:
+ _objc_msgSend$_stringForKeyWithPrefix:language:preferredDeviceType:withGenerativeSuffix:withGMEChinaSuffix:withNetworkSuffix:
+ _objc_msgSend$_stringKeyWithCapabilitiesFromPrefix:withNetwork:withGenerative:withGMEChinaSuffix:
+ _objc_msgSend$actionWithHandler:
+ _objc_msgSend$animationKeys
+ _objc_msgSend$ascender
+ _objc_msgSend$backButtonTitle
+ _objc_msgSend$configurationWithFont:scale:
+ _objc_msgSend$eligibilityForGreymatterHasCountryPolicyChina
+ _objc_msgSend$languageIdentifier
+ _objc_msgSend$link
+ _objc_msgSend$registerForTraitChanges:withAction:
+ _objc_msgSend$setAdjustsFontForContentSizeCategory:
+ _objc_msgSend$setBackButtonTitle:
+ _objc_msgSend$setTitleView:
+ _objc_msgSend$shouldUpdateAlphaForNavigationItem:andHeaderView:inScrollView:
+ _objc_msgSend$updateAlphaForNavigationItem:andHeaderView:usingNavigationTitleAlpha:animated:
+ _xpc_array_get_count
+ _xpc_array_get_string
+ _xpc_dictionary_get_array
+ _xpc_dictionary_get_string
- +[OBViewUtilities shouldUpdateNavigationBarWithNavigationItem:forHeaderView:inScrollView:]
- -[OBPrivacyFlow _stringKeyWithCapabilitiesFromPrefix:withNetwork:withGenerative:]
- -[OBStackedIconTextList traitCollectionDidChange:]
- ___93+[OBViewUtilities updateNavigationBarWithNavigationItem:forHeaderView:inScrollView:animated:]_block_invoke
- ___93+[OBViewUtilities updateNavigationBarWithNavigationItem:forHeaderView:inScrollView:animated:]_block_invoke_2
- ___93+[OBViewUtilities updateNavigationBarWithNavigationItem:forHeaderView:inScrollView:animated:]_block_invoke_3
- ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
- ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_OnBoardingKit
- _objc_msgSend$_backgroundHidden
- _objc_msgSend$_stringKeyWithCapabilitiesFromPrefix:withNetwork:withGenerative:
CStrings:
+ "@\"NSArray\"40@0:8@\"UITextView\"16{_NSRange=QQ}24"
+ "@\"UIAction\"40@0:8@\"UITextView\"16@\"UITextItem\"24@\"UIAction\"32"
+ "@\"UIConversationContext\"16@0:8"
+ "@\"UIMenu\"48@0:8@\"UITextView\"16{_NSRange=QQ}24@\"NSArray\"40"
+ "@\"UITextItemMenuConfiguration\"40@0:8@\"UITextView\"16@\"UITextItem\"24@\"UIMenu\"32"
+ "@36@0:8@16B24B28B32"
+ "@40@0:8@16{_NSRange=QQ}24"
+ "@44@0:8@16@24Q32B40"
+ "@48@0:8@16@24Q32B40B44"
+ "@52@0:8@16@24Q32B40B44B48"
+ "B24@0:8@\"UITextView\"16"
+ "B24@0:8r*16"
+ "B48@0:8@\"UITextView\"16@\"NSTextAttachment\"24{_NSRange=QQ}32"
+ "B48@0:8@\"UITextView\"16@\"NSURL\"24{_NSRange=QQ}32"
+ "B48@0:8@\"UITextView\"16{_NSRange=QQ}24@\"NSString\"40"
+ "B48@0:8@16@24{_NSRange=QQ}32"
+ "B56@0:8@\"UITextView\"16@\"NSTextAttachment\"24{_NSRange=QQ}32q48"
+ "B56@0:8@\"UITextView\"16@\"NSURL\"24{_NSRange=QQ}32q48"
+ "B56@0:8@16@24{_NSRange=QQ}32q48"
+ "CHN"
+ "Failed to get eligibility for greymatter with error %d"
+ "OS_ELIGIBILITY_CONTEXT_COUNTRY_POLICY"
+ "Privacy splash did open %@ with success %d"
+ "Privacy splash returning custom primary action for link %@"
+ "Privacy splash textView:primaryActionForTextItem:..."
+ "Privacy splash will open %@"
+ "T@\"NSNumber\",&,N,V_overrideEligibilityForGreymatterHasCountryPolicyChina"
+ "T@\"UIConversationContext\",?,&,N"
+ "UICTFontTextStyleShortEmphasizedBody"
+ "UITextViewDelegate"
+ "_"
+ "_GMECHINA"
+ "_bestStringConsideringCMEChinaForKeyWithPrefix:language:preferredDeviceType:withGenerativeSuffix:"
+ "_bestStringConsideringGenerativeForKeyWithPrefix:language:preferredDeviceType:"
+ "_bestStringConsideringNetworkForKeyWithPrefix:language:preferredDeviceType:withGenerativeSuffix:withGMEChinaSuffix:"
+ "_eligibilityContextHasCountryPolicyChina:"
+ "_eligibilityCountryPolicyStringIsChina:"
+ "_fontAdjustedForContentSizeCategoryCompatibleWithTraitCollection:"
+ "_isNavigationItemEligibleForCustomization:usingHeaderView:"
+ "_overrideEligibilityForGreymatterHasCountryPolicyChina"
+ "_potentialAdditionalDisplayLanguage languageIdentifier %@"
+ "_potentialAdditionalDisplayLanguage returning %@"
+ "_setBackButtonTitleOnNavigationItem:usingHeaderView:isHeaderViewVisible:"
+ "_stringForKeyWithPrefix:language:preferredDeviceType:withGenerativeSuffix:withGMEChinaSuffix:withNetworkSuffix:"
+ "_stringKeyWithCapabilitiesFromPrefix:withNetwork:withGenerative:withGMEChinaSuffix:"
+ "actionWithHandler:"
+ "additionalDisplayLanguageForDisplayLanguage additionalDisplayLanguage %@ resolvedDisplayLanguage %@"
+ "additionalDisplayLanguageForDisplayLanguage displayLanguage %@"
+ "additionalDisplayLanguageForDisplayLanguage languageCode %@"
+ "additionalDisplayLanguageForDisplayLanguage returning %@"
+ "additionalDisplayLanguageForDisplayLanguage returning _overrideAdditionalDisplayLanguage %@"
+ "animationKeys"
+ "ascender"
+ "backButtonTitle"
+ "configurationWithFont:scale:"
+ "conversationContext"
+ "eligibilityForGreymatterHasCountryPolicyChina"
+ "languageIdentifier"
+ "link"
+ "overrideEligibilityForGreymatterHasCountryPolicyChina"
+ "registerForTraitChanges:withAction:"
+ "setAdjustsFontForContentSizeCategory:"
+ "setBackButtonTitle:"
+ "setConversationContext:"
+ "setOverrideEligibilityForGreymatterHasCountryPolicyChina:"
+ "setTitleView:"
+ "shouldUpdateAlphaForNavigationItem:andHeaderView:inScrollView:"
+ "splash controller in catalyst path"
+ "splash controller viewWillAppear"
+ "textField:insertInputSuggestion:"
+ "textView:didBeginFormattingWithViewController:"
+ "textView:didEndFormattingWithViewController:"
+ "textView:editMenuForTextInRange:suggestedActions:"
+ "textView:insertInputSuggestion:"
+ "textView:menuConfigurationForTextItem:defaultMenu:"
+ "textView:primaryActionForTextItem:defaultAction:"
+ "textView:shouldChangeTextInRange:replacementText:"
+ "textView:shouldInteractWithTextAttachment:inRange:"
+ "textView:shouldInteractWithTextAttachment:inRange:interaction:"
+ "textView:shouldInteractWithURL:inRange:"
+ "textView:shouldInteractWithURL:inRange:interaction:"
+ "textView:textItemMenuWillDisplayForTextItem:animator:"
+ "textView:textItemMenuWillEndForTextItem:animator:"
+ "textView:willBeginFormattingWithViewController:"
+ "textView:willDismissEditMenuWithAnimator:"
+ "textView:willEndFormattingWithViewController:"
+ "textView:willPresentEditMenuWithAnimator:"
+ "textView:writingToolsIgnoredRangesInEnclosingRange:"
+ "textViewDidBeginEditing:"
+ "textViewDidChange:"
+ "textViewDidChangeSelection:"
+ "textViewDidEndEditing:"
+ "textViewShouldBeginEditing:"
+ "textViewShouldEndEditing:"
+ "textViewWritingToolsDidEnd:"
+ "textViewWritingToolsWillBegin:"
+ "updateAlphaForNavigationItem:andHeaderView:usingNavigationTitleAlpha:animated:"
+ "v16@?0@\"UIAction\"8"
+ "v24@0:8@\"UIConversationContext\"16"
+ "v24@0:8@\"UITextView\"16"
+ "v32@0:8@\"UITextField\"16@\"UIInputSuggestion\"24"
+ "v32@0:8@\"UITextView\"16@\"<UIEditMenuInteractionAnimating>\"24"
+ "v32@0:8@\"UITextView\"16@\"UIInputSuggestion\"24"
+ "v32@0:8@\"UITextView\"16@\"UITextFormattingViewController\"24"
+ "v36@0:8@16@24B32"
+ "v40@0:8@\"UITextView\"16@\"UITextItem\"24@\"<UIContextMenuInteractionAnimating>\"32"
+ "v44@0:8@16@24d32B40"
- "_backgroundHidden"
- "_stringKeyWithCapabilitiesFromPrefix:withNetwork:withGenerative:"
- "shouldUpdateNavigationBarWithNavigationItem:forHeaderView:inScrollView:"

```
