## TextInput

> `/System/Library/PrivateFrameworks/TextInput.framework/TextInput`

```diff

-3479.228.0.0.0
-  __TEXT.__text: 0x76978
-  __TEXT.__auth_stubs: 0xec0
-  __TEXT.__objc_methlist: 0xa214
-  __TEXT.__const: 0x470
-  __TEXT.__cstring: 0x1407e
-  __TEXT.__ustring: 0x3f76
-  __TEXT.__dlopen_cstrs: 0x459
-  __TEXT.__oslogstring: 0x604
-  __TEXT.__unwind_info: 0x1d00
-  __TEXT.__objc_classname: 0x1523
-  __TEXT.__objc_methname: 0x183b6
-  __TEXT.__objc_methtype: 0x36c4
-  __TEXT.__objc_stubs: 0xc880
-  __DATA_CONST.__got: 0x630
-  __DATA_CONST.__const: 0x2198
-  __DATA_CONST.__objc_classlist: 0x598
-  __DATA_CONST.__objc_catlist: 0x28
+3479.317.0.0.0
+  __TEXT.__text: 0x7bd7c
+  __TEXT.__auth_stubs: 0xf00
+  __TEXT.__objc_methlist: 0xb140
+  __TEXT.__dlopen_cstrs: 0x4b9
+  __TEXT.__const: 0x4a0
+  __TEXT.__cstring: 0x14d2c
+  __TEXT.__ustring: 0x59d8
+  __TEXT.__oslogstring: 0x663
+  __TEXT.__unwind_info: 0x1e70
+  __TEXT.__objc_classname: 0x154a
+  __TEXT.__objc_methname: 0x190ae
+  __TEXT.__objc_methtype: 0x3768
+  __TEXT.__objc_stubs: 0xcdc0
+  __DATA_CONST.__got: 0x660
+  __DATA_CONST.__const: 0x2300
+  __DATA_CONST.__objc_classlist: 0x5a0
+  __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x51a0
-  __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x3f0
-  __DATA_CONST.__objc_arraydata: 0x23fb0
-  __AUTH_CONST.__auth_got: 0x768
+  __DATA_CONST.__objc_selrefs: 0x5420
+  __DATA_CONST.__objc_protorefs: 0x58
+  __DATA_CONST.__objc_superrefs: 0x3f8
+  __DATA_CONST.__objc_arraydata: 0x271c8
+  __AUTH_CONST.__auth_got: 0x788
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0xc60
-  __AUTH_CONST.__cfstring: 0x390e0
-  __AUTH_CONST.__objc_const: 0x12788
-  __AUTH_CONST.__objc_arrayobj: 0x3b88
-  __AUTH_CONST.__objc_dictobj: 0xc0d0
-  __AUTH_CONST.__objc_intobj: 0xcc0
+  __AUTH_CONST.__const: 0xcc0
+  __AUTH_CONST.__cfstring: 0x40620
+  __AUTH_CONST.__objc_const: 0x115e8
+  __AUTH_CONST.__objc_arrayobj: 0x3e88
+  __AUTH_CONST.__objc_dictobj: 0xc490
+  __AUTH_CONST.__objc_intobj: 0xcd8
   __AUTH_CONST.__objc_doubleobj: 0xc0
-  __AUTH.__objc_data: 0x23a0
-  __DATA.__objc_ivar: 0xb28
+  __AUTH.__objc_data: 0x23f0
+  __DATA.__objc_ivar: 0xb48
   __DATA.__data: 0xbd0
-  __DATA.__bss: 0x720
+  __DATA.__bss: 0x760
   __DATA_DIRTY.__objc_data: 0x1450
-  __DATA_DIRTY.__bss: 0x2b8
+  __DATA_DIRTY.__bss: 0x2a8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3786
-  Symbols:   5032
-  CStrings:  9378
+  Functions: 3865
+  Symbols:   5152
+  CStrings:  9555
 
Symbols:
+ _CFArrayGetCount
+ _CFArrayGetValueAtIndex
+ _CFStringCreateArrayWithFindResults
+ _NSInvalidArgumentException
+ _NSRangeException
+ _OBJC_CLASS_$_NSException
+ _OBJC_CLASS_$_NSMutableAttributedString
+ _OBJC_CLASS_$_TIAttributedDocumentState
+ _OBJC_METACLASS_$_TIAttributedDocumentState
+ _TIActiveMultilingualKeyboardDictationMappingsPreference
+ _TIArchivedInputModeConfigurationInputModesKey
+ _TIArchivedInputModeConfigurationPlatformKey
+ _TIArchivedInputModeConfigurationPlatform_iOS
+ _TIArchivedInputModeConfigurationPlatform_macOS
+ _TIArchivedInputModeConfigurationPreferredLanguagesKey
+ _TIArchivedInputModeConfigurationPreferredLocaleKey
+ _TIArchivedInputModeConfigurationVersionKey
+ _TIGetIndicScriptComposerRules
+ _TIGetMacInputSourcesMap
+ _TIInputModePropertiesTypeToSiriEnabled
+ _TIInputModePropertiesTypeToSiriEnabledUnderDevelopment
+ _TIIsTypeToSiriModeEnabled
+ _TIKeyboardDidShowGenmojiTipPreference
+ _TIPersonaUniqueIdentifierSelfPreference
+ _TIRemoteDeviceIDSIdentifierPreference
+ __NSMethodExceptionProem
+ __tiAttributedStringForString
+ _objc_retainAutoreleasedReturnValue
- _TIISTypetoSiriMode
- _strncmp
CStrings:
+ "%@: Index %lu out of bounds; string length %lu"
+ "%@: Range {%lu, %lu} out of bounds; string length %lu"
+ "%@: nil argument"
+ "%s  TIKeyboardState with TIAttributedDocumentState: non-serializable attribute encountered: %@"
+ "%s: %@"
+ "-[TIInputModeController _archivedInputModeConfigurationFrom:]"
+ "-[TIInputModeController inputModesFromArchivedInputModeConfiguration:]"
+ "-[TIKeyboardState encodeWithCoder:]_block_invoke_2"
+ "; attributedDocumentState = %@"
+ "@\"NSAttributedString\""
+ "@\"NSDictionary\"16@?0@\"NSDictionary\"8"
+ "@\"TIAttributedDocumentState\""
+ "@40@0:8{_NSRange=QQ}16@32"
+ "@56@0:8@16@24Q32{_NSRange=QQ}40"
+ "@hw=%@"
+ "AFPreferences"
+ "ActiveMultilingualKeyboardDictationMappings"
+ "Beng"
+ "Deva"
+ "Gujr"
+ "Guru"
+ "KeyboardDidShowGenmojiTip"
+ "MacInputSourcesMap.plist"
+ "Mlym"
+ "O\x02#"
+ "OTP"
+ "PersonaUniqueIdentifierSelf"
+ "Q56@0:8@16@24Q32{_NSRange=QQ}40"
+ "RemoteDeviceIDSIdentifier"
+ "SecureCoding"
+ "T@\"NSAttributedString\",R,N"
+ "T@\"NSAttributedString\",R,N,V_contextAfterInput"
+ "T@\"NSAttributedString\",R,N,V_contextBeforeInput"
+ "T@\"NSAttributedString\",R,N,V_markedText"
+ "T@\"NSAttributedString\",R,N,V_selectedText"
+ "T@\"TIAttributedDocumentState\",&,N,V_attributedDocumentState"
+ "TB,N,V_isOneTimeCodeThatRequiresAuthentication"
+ "TIAttributedDocumentState"
+ "TIIndicScriptComposerRules.plist"
+ "UIKeyboardTypeToSiriEnabled"
+ "UIKeyboardTypeToSiriUnderDevelopment"
+ "_archivedInputModeConfigurationFrom:"
+ "_attributedDocumentState"
+ "_attributedString:byTrimmingWordsAfterIndex:"
+ "_attributedString:byTrimmingWordsBeforeIndex:"
+ "_attributedString:matchesAttributedString:"
+ "_indexByTrimmingWordsAfterIndex:"
+ "_indexByTrimmingWordsBeforeIndex:"
+ "_inputModeConfiguration"
+ "_inputModesFromInputModeConfiguration:"
+ "_isOneTimeCodeThatRequiresAuthentication"
+ "_ti_attributedString:matchesAttributedStringIgnoringNullity:"
+ "_ti_attributedStringByAppendingAttributedString:"
+ "_ti_attributedStringByAppendingString:"
+ "_ti_attributedStringByKeepingAttributes:"
+ "_ti_attributedStringByRemovingAttributes:"
+ "_ti_attributedStringWithIterator:"
+ "_ti_attributedSubstringFromIndex:"
+ "_ti_attributedSubstringToIndex:"
+ "_ti_decodeWithCoder:forKey:attributeIterator:"
+ "_ti_encodeWithCoder:forKey:attributeIterator:"
+ "_ti_encodeWithCoder:forKey:keepingAttributes:"
+ "_ti_encodeWithCoder:forKey:removingAttributes:"
+ "_ti_replaceOccurrencesOfString:withString:options:range:"
+ "_ti_stringByReplacingCharactersInRange:withString:"
+ "_ti_stringByReplacingOccurrencesOfString:withString:options:range:"
+ "addAttributes:range:"
+ "appendAttributedString:"
+ "archivedInputModeConfiguration"
+ "attributedDocumentState"
+ "attributedDocumentStateForTestingWithContextBefore:selectedText:contextAfter:"
+ "attributedDocumentStateForTestingWithContextBefore:selectedText:contextAfter:markedText:selectedRangeInMarkedText:"
+ "attributedDocumentStateForTestingWithPlainContextBefore:selectedText:contextAfter:"
+ "attributedDocumentStateForTestingWithPlainContextBefore:selectedText:contextAfter:markedText:selectedRangeInMarkedText:"
+ "attributedDocumentStateForTestingWithPlainText:selectedRange:"
+ "attributedDocumentStateForTestingWithText:selectedRange:"
+ "attributedDocumentStateWithContextBefore:markedText:selectedRange:contextAfter:"
+ "attributedDocumentStateWithContextBefore:selectedText:contextAfter:"
+ "attributedDocumentStateWithDocumentState:"
+ "attributedString"
+ "attributedSubstringFromRange:"
+ "attributesAtIndex:effectiveRange:"
+ "bn@sw=Bengali-Alphabetic"
+ "com.apple.inputmethod.AinuIM.Ainu"
+ "com.apple.inputmethod.Korean.2SetKorean"
+ "com.apple.inputmethod.Korean.390Sebulshik"
+ "com.apple.inputmethod.Korean.3SetKorean"
+ "com.apple.inputmethod.Korean.GongjinCheongRomaja"
+ "com.apple.inputmethod.Korean.HNCRomaja"
+ "com.apple.inputmethod.Kotoeri.KanaTyping.Japanese"
+ "com.apple.inputmethod.Kotoeri.KanaTyping.Japanese.FullWidthRoman"
+ "com.apple.inputmethod.Kotoeri.KanaTyping.Japanese.HalfWidthKana"
+ "com.apple.inputmethod.Kotoeri.KanaTyping.Japanese.Katakana"
+ "com.apple.inputmethod.Kotoeri.KanaTyping.Roman"
+ "com.apple.inputmethod.Kotoeri.RomajiTyping.Japanese"
+ "com.apple.inputmethod.Kotoeri.RomajiTyping.Japanese.FullWidthRoman"
+ "com.apple.inputmethod.Kotoeri.RomajiTyping.Japanese.HalfWidthKana"
+ "com.apple.inputmethod.Kotoeri.RomajiTyping.Japanese.Katakana"
+ "com.apple.inputmethod.Kotoeri.RomajiTyping.Roman"
+ "com.apple.inputmethod.SCIM.ITABC"
+ "com.apple.inputmethod.SCIM.Shuangpin"
+ "com.apple.inputmethod.SCIM.WBH"
+ "com.apple.inputmethod.SCIM.WBX"
+ "com.apple.inputmethod.TCIM.Cangjie"
+ "com.apple.inputmethod.TCIM.Jianyi"
+ "com.apple.inputmethod.TCIM.Pinyin"
+ "com.apple.inputmethod.TCIM.Shuangpin"
+ "com.apple.inputmethod.TCIM.WBH"
+ "com.apple.inputmethod.TCIM.Zhuyin"
+ "com.apple.inputmethod.TCIM.ZhuyinEten"
+ "com.apple.inputmethod.TYIM.Cangjie"
+ "com.apple.inputmethod.TYIM.Phonetic"
+ "com.apple.inputmethod.TYIM.Stroke"
+ "com.apple.inputmethod.TYIM.Sucheng"
+ "com.apple.inputmethod.Tamil.AnjalIM"
+ "com.apple.inputmethod.Tamil.Tamil99"
+ "com.apple.inputmethod.TransliterationIM.bn"
+ "com.apple.inputmethod.TransliterationIM.gu"
+ "com.apple.inputmethod.TransliterationIM.hi"
+ "com.apple.inputmethod.TransliterationIM.kn"
+ "com.apple.inputmethod.TransliterationIM.ml"
+ "com.apple.inputmethod.TransliterationIM.mr"
+ "com.apple.inputmethod.TransliterationIM.pa"
+ "com.apple.inputmethod.TransliterationIM.ta"
+ "com.apple.inputmethod.TransliterationIM.te"
+ "com.apple.inputmethod.TransliterationIM.ur"
+ "com.apple.inputmethod.VietnameseIM.VietnameseSimpleTelex"
+ "com.apple.inputmethod.VietnameseIM.VietnameseTelex"
+ "com.apple.inputmethod.VietnameseIM.VietnameseVIQR"
+ "com.apple.inputmethod.VietnameseIM.VietnameseVNI"
+ "com.apple.keylayout."
+ "documentStateWithAttributeIterator:"
+ "enumerateAttributesInRange:options:usingBlock:"
+ "gu@sw=Gujarati-Alphabetic"
+ "hi@sw=Hindi-Alphabetic"
+ "iOS"
+ "initWithString:attributes:"
+ "inputModes"
+ "inputModesFromArchivedInputModeConfiguration:"
+ "isEqualToAttributedString:"
+ "isOneTimeCodeThatRequiresAuthentication"
+ "isTextEqualIgnoringMarkedText:"
+ "ja_JP-Kana@hw=KANA"
+ "keyboardCandidateInputStringUsedWithAutofillExtraThatSignifiesOTPExtra"
+ "kn@sw=Kannada-Alphabetic"
+ "macOS"
+ "ml@sw=Malayalam-Alphabetic"
+ "mostPreferredLanguageOf:withPreferredLanguages:forUsage:options:"
+ "mr@sw=Marathi-Alphabetic"
+ "or@sw=Oriya-Alphabetic"
+ "pa@sw=Punjabi-Alphabetic"
+ "personaUniqueIdentifierSelf"
+ "platform"
+ "preferredLocale"
+ "raise:format:"
+ "registerRemoteDeviceWithIDSIdentifier:user:"
+ "remoteDeviceIDSIdentifer"
+ "removeAttribute:range:"
+ "replaceCharactersInRange:withAttributedString:"
+ "setAttributedDocumentState:"
+ "setIsOneTimeCodeThatRequiresAuthentication:"
+ "sharedPreferences"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices"
+ "sortedArrayUsingSelector:"
+ "ta@hw=Tamil99"
+ "ta@sw=Tamil-Alphabetic"
+ "te@sw=Telugu-Alphabetic"
+ "transformedInputModesFromInputModes:sourcePlatform:targetPlatform:preferredLanguages:preferredLocale:"
+ "type_to_siri_under_development"
+ "unboundedAttributedDocumentStateForTestingWithContextBefore:selectedText:contextAfter:"
+ "unboundedAttributedDocumentStateForTestingWithPlainContextBefore:selectedText:contextAfter:"
+ "updateLastUsedDictionaryLanguageInMultilingualKeyboard:activeDictationlanguage:"
+ "ur@sw=Urdu-Alphabetic"
+ "ur_PK"
+ "v32@0:8@\"NSArray\"16@24"
+ "v40@?0@\"NSDictionary\"8{_NSRange=QQ}16^B32"
- "O\x01#"
- "fd"

```
