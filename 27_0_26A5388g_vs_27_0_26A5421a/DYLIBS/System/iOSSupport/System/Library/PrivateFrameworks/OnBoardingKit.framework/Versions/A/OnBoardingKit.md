## OnBoardingKit

> `/System/iOSSupport/System/Library/PrivateFrameworks/OnBoardingKit.framework/Versions/A/OnBoardingKit`

```diff

-3977.0.20.0.0
-  __TEXT.__text: 0x38348
-  __TEXT.__objc_methlist: 0x50ac
-  __TEXT.__cstring: 0x18b9
+3977.0.23.0.0
+  __TEXT.__text: 0x387fc
+  __TEXT.__objc_methlist: 0x50ec
+  __TEXT.__cstring: 0x18a9
   __TEXT.__const: 0x4e4
-  __TEXT.__oslogstring: 0xc52
+  __TEXT.__oslogstring: 0xc5d
   __TEXT.__ustring: 0x4
   __TEXT.__gcc_except_tab: 0xa4
   __TEXT.__swift5_typeref: 0xe
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xd98
+  __TEXT.__unwind_info: 0xda0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3578
+  __DATA_CONST.__objc_selrefs: 0x35e0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0x90
-  __DATA_CONST.__got: 0x448
+  __DATA_CONST.__got: 0x458
   __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0x2000
-  __AUTH_CONST.__objc_const: 0xa748
+  __AUTH_CONST.__objc_const: 0xa778
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x470
+  __AUTH_CONST.__auth_got: 0x450
   __AUTH.__objc_data: 0xb40
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x590
+  __DATA.__objc_ivar: 0x594
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x48
   __DATA.__common: 0x60

   - /System/Library/Frameworks/Symbols.framework/Versions/A/Symbols
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
-  - /System/iOSSupport/System/Library/Frameworks/UIKit.framework/UIKit
   - /System/iOSSupport/System/Library/Frameworks/UIKit.framework/Versions/A/UIKit
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1577
-  Symbols:   4272
-  CStrings:  343
+  Functions: 1582
+  Symbols:   4287
+  CStrings:  342
 
Symbols:
+ -[OBButtonTray _limitPrivacyLinkContentSizeCategory]
+ -[OBButtonTray _pocketContentIsButtonsOnly]
+ -[OBPrivacyFlow _bestStringConsideringNetworkForKeyWithPrefix:language:preferredDeviceType:withGenerativeSuffix:countryPolicySuffix:]
+ -[OBPrivacyFlow _stringForKeyWithPrefix:language:preferredDeviceType:withGenerativeSuffix:countryPolicySuffix:withNetworkSuffix:]
+ -[OBPrivacyFlow _stringKeyWithCapabilitiesFromPrefix:withNetwork:withGenerative:countryPolicySuffix:]
+ -[OBPrivacyFlow localizedButtonSecondaryCaptionForLanguage:preferredDeviceType:]
+ -[OBPrivacyLinkButton _captionAttributes]
+ -[OBPrivacyLinkButton initWithCaption:captionAttachmentImage:secondaryCaption:buttonText:symbolName:useLargeIcon:displayLanguage:]
+ -[OBPrivacyLinkButton secondaryCaptionText]
+ -[OBTableWelcomeController _setAdditionalTopInsetForColumnLayout]
+ GCC_except_table13
+ OBJC_IVAR_$_OBPrivacyLinkButton._secondaryCaptionText
+ _OBJC_CLASS_$_UIScrollEdgeEffectStyle
+ _UIContentSizeCategoryUnspecified
+ _objc_msgSend$_bestStringConsideringNetworkForKeyWithPrefix:language:preferredDeviceType:withGenerativeSuffix:countryPolicySuffix:
+ _objc_msgSend$_captionAttributes
+ _objc_msgSend$_limitPrivacyLinkContentSizeCategory
+ _objc_msgSend$_pocketContentIsButtonsOnly
+ _objc_msgSend$_scrollView
+ _objc_msgSend$_setAdditionalTopInsetForColumnLayout
+ _objc_msgSend$_setStyle:
+ _objc_msgSend$_stringForKeyWithPrefix:language:preferredDeviceType:withGenerativeSuffix:countryPolicySuffix:withNetworkSuffix:
+ _objc_msgSend$_stringKeyWithCapabilitiesFromPrefix:withNetwork:withGenerative:countryPolicySuffix:
+ _objc_msgSend$_style
+ _objc_msgSend$automaticStyle
+ _objc_msgSend$bottomEdgeEffect
+ _objc_msgSend$hardStyle
+ _objc_msgSend$initWithCaption:captionAttachmentImage:secondaryCaption:buttonText:symbolName:useLargeIcon:displayLanguage:
+ _objc_msgSend$localizedButtonSecondaryCaptionForLanguage:preferredDeviceType:
+ _objc_msgSend$setPreferredContentSizeCategory:
+ _objc_msgSend$traitOverrides
- -[OBCapabilities _eligibilityContextHasCountryPolicyChina:]
- -[OBCapabilities _eligibilityCountryPolicyStringIsChina:]
- -[OBPrivacyFlow _bestStringConsideringNetworkForKeyWithPrefix:language:preferredDeviceType:withGenerativeSuffix:withGMEChinaSuffix:]
- -[OBPrivacyFlow _stringForKeyWithPrefix:language:preferredDeviceType:withGenerativeSuffix:withGMEChinaSuffix:withNetworkSuffix:]
- -[OBPrivacyFlow _stringKeyWithCapabilitiesFromPrefix:withNetwork:withGenerative:withGMEChinaSuffix:]
- GCC_except_table15
- _objc_msgSend$_bestStringConsideringNetworkForKeyWithPrefix:language:preferredDeviceType:withGenerativeSuffix:withGMEChinaSuffix:
- _objc_msgSend$_eligibilityContextHasCountryPolicyChina:
- _objc_msgSend$_eligibilityCountryPolicyStringIsChina:
- _objc_msgSend$_stringForKeyWithPrefix:language:preferredDeviceType:withGenerativeSuffix:withGMEChinaSuffix:withNetworkSuffix:
- _objc_msgSend$_stringKeyWithCapabilitiesFromPrefix:withNetwork:withGenerative:withGMEChinaSuffix:
- _objc_msgSend$initWithCaption:captionAttachmentImage:buttonText:symbolName:useLargeIcon:displayLanguage:
- _xpc_array_get_count
- _xpc_array_get_string
- _xpc_dictionary_get_array
- _xpc_dictionary_get_string
CStrings:
+ "BUTTON_CAPTION_SECONDARY"
+ "Failed to get Bembidion (China privacy) eligibility with error %d"
+ "_NOTGMECHINA"
- "CHN"
- "Failed to get eligibility for greymatter with error %d"
- "OS_ELIGIBILITY_CONTEXT_COUNTRY_POLICY"
- "_"
```
