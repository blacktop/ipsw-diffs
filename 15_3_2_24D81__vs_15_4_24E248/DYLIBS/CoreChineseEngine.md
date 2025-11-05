## CoreChineseEngine

> `/System/Library/PrivateFrameworks/CoreChineseEngine.framework/Versions/A/CoreChineseEngine`

```diff

 537.0.0.0.0
-  __TEXT.__text: 0x45158
+  __TEXT.__text: 0x44f88
   __TEXT.__auth_stubs: 0xa30
-  __TEXT.__objc_methlist: 0x4688
+  __TEXT.__objc_methlist: 0x486c
   __TEXT.__const: 0x120
   __TEXT.__cstring: 0x3255
   __TEXT.__ustring: 0x404
-  __TEXT.__gcc_except_tab: 0x1064
+  __TEXT.__gcc_except_tab: 0x1070
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__oslogstring: 0x3b
-  __TEXT.__unwind_info: 0x10c8
+  __TEXT.__unwind_info: 0x10d0
   __TEXT.__objc_classname: 0x72d
   __TEXT.__objc_methname: 0xcc28
   __TEXT.__objc_methtype: 0xe6e

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e98
+  __DATA_CONST.__objc_selrefs: 0x2f08
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0x4f0
   __AUTH_CONST.__auth_got: 0x528
   __AUTH_CONST.__const: 0x1180
   __AUTH_CONST.__cfstring: 0x4640
-  __AUTH_CONST.__objc_const: 0x7700
+  __AUTH_CONST.__objc_const: 0x73a0
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x438

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libmecabra.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3D69FF5E-85F6-35CF-AB3F-595143744648
-  Functions: 1698
-  Symbols:   4447
+  UUID: 16F46E15-39D4-3F79-95D7-97FEC6258545
+  Functions: 1720
+  Symbols:   4493
   CStrings:  3463
 
Symbols:
+ +[CIMContactsReader sharedContactsReader].cold.1
+ +[CIMDefinitionToLayoutController sharedLayoutController].cold.1
+ +[CIMHelpController sharedController].cold.1
+ +[CIMMecabraController sharedInstance].cold.1
+ +[CIMMenuController sharedMenuControllerWithDataSource:].cold.1
+ +[CIMMockPreferences sharedUserDefaults].cold.1
+ +[CIMMockUserDefaults sharedPasteboardValueDictionary].cold.1
+ +[CIMPreferences expertTCIMDictionaryDefaultsKeys].cold.1
+ +[CIMPreferences validFuzzyPinyinPairs].cold.1
+ +[CIMPunctuationManager sharedInstance].cold.1
+ +[CIMResourcePathManager sharedResourcePathManager].cold.1
+ +[CIMStatistics sharedStatistics].cold.1
+ +[CIMTextReplacementController sharedOperationQueue].cold.1
+ +[NSCharacterSet(CIMAdditions) URLAndEmailAddressPunctuationCharacterSet].cold.1
+ +[NSCharacterSet(CIMAdditions) pinyinPunctuationCharacterSet].cold.1
+ +[NSCharacterSet(CIMAdditions) punctuationAndSymbolCharacterSet].cold.1
+ +[NSCharacterSet(CIMAdditions) punctuationAndWhitespaceCharacterSet].cold.1
+ +[NSCharacterSet(CIMAdditions) validPinyinCharacterSet].cold.1
+ +[NSCharacterSet(CIMAdditions) zhuyinCharacterSet].cold.1
+ +[NSCharacterSet(CIMAdditions) zhuyinConsonantCharacterSet].cold.1
+ +[NSCharacterSet(CIMAdditions) zhuyinMedialCharacterSet].cold.1
+ +[NSCharacterSet(CIMAdditions) zhuyinPhonemeCharacterSet].cold.1
+ +[NSCharacterSet(CIMAdditions) zhuyinToneCharacterSet].cold.1
+ +[NSCharacterSet(CIMAdditions) zhuyinVowelCharacterSet].cold.1
+ -[CIMBaseEngine IMKCharCodeRemappedKeyCodes].cold.1
+ -[CIMBaseEngine dictionaryForScriptType:].cold.1
+ -[CIMCangjieEngine inputCharacterSet].cold.1
+ -[CIMMecabraZhuyinEngine textReplacementController].cold.1
+ -[CIMPinyinEngine contextualVariantForPunctuation:].cold.1
+ -[CIMPinyinEngine contextualVariantForPunctuation:].cold.2
+ -[CIMPinyinEngine insertPairedPunctuations:].cold.1
+ -[CIMResourcePathManager resourcePathsForKey:inputMode:].cold.1
+ -[CIMStrokeEngine candidatesForInput:].cold.1
+ -[CIMStrokeEngine keyMappings].cold.1
+ -[CIMTextReplacementController textReplacementClientStore].cold.1
+ -[CIMWubixingEngine inputCharacterSet].cold.1
+ -[NSString(CIMAdditions) hasURISchemePrefix].cold.1
+ -[NSString(CIMAdditions) numberForToneMark].cold.1
+ -[NSString(CIMAdditions) stringByApplyingPinyinToneMarkToFirstSyllableWithToneNumber:].cold.1
+ -[NSString(CIMAdditions) stringByApplyingPinyinToneMarkToFirstSyllableWithToneNumber:].cold.2
+ KeyboardServices_Library.cold.1
+ TIAssetManagerClass.cold.1
+ TIInputModeClass.cold.1
+ TIMecabraEnvironmentClass.cold.1
+ __51-[CIMTextReplacementController rebuildWithMecabra:]_block_invoke.cold.1
+ __58-[CIMTextReplacementController textReplacementClientStore]_block_invoke.cold.1

```
