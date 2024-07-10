## ScreenReader

> `/System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/ScreenReader`

```diff

-947.0.0.0.0
-  __TEXT.__text: 0x2949f8
+950.1.1.0.0
+  __TEXT.__text: 0x29532c
   __TEXT.__auth_stubs: 0x2990
-  __TEXT.__objc_methlist: 0x22b14
-  __TEXT.__const: 0xda2
-  __TEXT.__gcc_except_tab: 0x2ffc
-  __TEXT.__cstring: 0x1fbe9
+  __TEXT.__objc_methlist: 0x22b64
+  __TEXT.__const: 0xd92
+  __TEXT.__gcc_except_tab: 0x2fec
+  __TEXT.__cstring: 0x1fbc9
   __TEXT.__dlopen_cstrs: 0x6d5
   __TEXT.__oslogstring: 0x339
   __TEXT.__ustring: 0x3c
   __TEXT.__swift5_typeref: 0x5
   __TEXT.__dof_SCRMapEle: 0x47e
   __TEXT.__dof_SCRSpeech: 0x21a
-  __TEXT.__unwind_info: 0x7e98
+  __TEXT.__unwind_info: 0x7eb0
   __TEXT.__objc_classname: 0x3242
-  __TEXT.__objc_methname: 0x52605
-  __TEXT.__objc_methtype: 0x7d31
-  __TEXT.__objc_stubs: 0x3ec80
+  __TEXT.__objc_methname: 0x52718
+  __TEXT.__objc_methtype: 0x7d37
+  __TEXT.__objc_stubs: 0x3ed80
   __DATA_CONST.__got: 0x1a80
-  __DATA_CONST.__const: 0x2058
+  __DATA_CONST.__const: 0x2060
   __DATA_CONST.__objc_classlist: 0xce8
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12670
+  __DATA_CONST.__objc_selrefs: 0x126a8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x998
   __DATA_CONST.__objc_arraydata: 0x770
   __AUTH_CONST.__auth_got: 0x14d8
   __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x39b0
-  __AUTH_CONST.__cfstring: 0x245e0
+  __AUTH_CONST.__const: 0x39f0
+  __AUTH_CONST.__cfstring: 0x24600
   __AUTH_CONST.__objc_const: 0x310a8
   __AUTH_CONST.__objc_arrayobj: 0x1b0
   __AUTH_CONST.__objc_intobj: 0x13c8

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 12588
-  Symbols:   28628
-  CStrings:  4981
+  Functions: 12597
+  Symbols:   28649
+  CStrings:  4982
 
Symbols:
+ +[SCRBrailleUtilities _brailleVariantsForElement:attributedText:isPlaceholder:brailleFocus:echoRange:selectionRange:]
+ +[SCRBrailleUtilities addBrailleTextVariantsForElement:attributedText:isPlaceholder:echoRange:selectionRange:request:]
+ -[SCRApplication _uiElementForKeyboardFocusIfWindowOrDialogUIElement:request:]
+ -[SCRApplication _uiElementForKeyboardFocusInWebDialogUIElement:]
+ -[SCRButton fullItemDescriptionForMenu]
+ -[SCRCUserDefaults(SCRCUserDefaultsSpeechConvenience) legacyDefaultVoiceID]
+ -[SCRCUserDefaults(SCRCUserDefaultsSpeechConvenience) setAutomaticallySwitchVoiceBasedOnLanguage:]
+ -[SCRCUserDefaults(SCRCUserDefaultsSpeechConvenience) speechVoiceIDForActivity]
+ -[SCRCUserDefaults(SCRCUserDefaultsSpeechConvenience) speechVoiceIDForRotor]
+ -[SCRCUserDefaults(SCRCUserDefaultsSpeechConvenience) validNumber:]
+ GCC_except_table147
+ ___35-[SCRStandardText rotorIdentifiers]_block_invoke
+ ___65-[SCRWebArea _handleVerticalMovementWithDirection:event:request:]_block_invoke
+ __block_literal_global.1228
+ __block_literal_global.1349
+ __block_literal_global.461
+ __block_literal_global.827
+ __block_literal_global.922
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_ScreenReader
+ _objc_msgSend$_brailleVariantsForElement:attributedText:isPlaceholder:brailleFocus:echoRange:selectionRange:
+ _objc_msgSend$_uiElementForKeyboardFocusIfWindowOrDialogUIElement:request:
+ _objc_msgSend$_uiElementForKeyboardFocusInWebDialogUIElement:
+ _objc_msgSend$_verifyValidFocusChain
+ _objc_msgSend$accessibilityIndexOfChild:
+ _objc_msgSend$addBrailleTextVariantsForElement:attributedText:isPlaceholder:echoRange:selectionRange:request:
+ _objc_msgSend$displayNameForKey:value:
+ _objc_msgSend$legacyDefaultVoiceID
+ _objc_msgSend$nilOutIfSystemLanguageID:
+ _objc_msgSend$setLanguageDetectionEnabled:
+ _objc_msgSend$speechVoiceIDForActivity
+ _objc_msgSend$speechVoiceIDForRotor
+ _objc_msgSend$validNumber:
+ _soft_AXVoiceNameForVoiceId
+ soft_AXVoiceNameForVoiceId.cold.1
- +[SCRBrailleUtilities _brailleVariantsForElement:attributedText:brailleFocus:echoRange:selectionRange:]
- +[SCRBrailleUtilities addBrailleTextVariantsForElement:attributedText:echoRange:selectionRange:request:]
- -[SCRElement(SCRWebElementUtilities) elementIsContentEditableRoot:]
- -[SCRWebAreaBookendGroup statusDescription]
- -[_SCRSpeechAttributeVoiceGuideItem initWithVoiceSelection:identifier:guide:].cold.1
- __block_literal_global.1225
- __block_literal_global.1346
- __block_literal_global.824
- __block_literal_global.919
- _objc_msgSend$_brailleVariantsForElement:attributedText:brailleFocus:echoRange:selectionRange:
- _objc_msgSend$_isSystemWideCategory:
- _objc_msgSend$addBrailleTextVariantsForElement:attributedText:echoRange:selectionRange:request:
- _objc_msgSend$elementIsContentEditableRoot:
- _objc_msgSend$registry
CStrings:
+ "%!@(MISSING) - %!@(MISSING)"
+ "wuu"
- "editable status for a content editable element"

```
