## CoreJapaneseEngine

> `/System/Library/PrivateFrameworks/CoreJapaneseEngine.framework/Versions/A/CoreJapaneseEngine`

```diff

 275.200.0.0.0
-  __TEXT.__text: 0x41338
+  __TEXT.__text: 0x40f3c
   __TEXT.__auth_stubs: 0x13f0
-  __TEXT.__objc_methlist: 0x2ba8
+  __TEXT.__objc_methlist: 0x2fc4
   __TEXT.__const: 0x1e8
   __TEXT.__gcc_except_tab: 0x6e8
-  __TEXT.__cstring: 0x2d35
+  __TEXT.__cstring: 0x2d32
   __TEXT.__oslogstring: 0x1384
   __TEXT.__ustring: 0x57a
   __TEXT.__dlopen_cstrs: 0xb1
-  __TEXT.__unwind_info: 0xad0
+  __TEXT.__unwind_info: 0xac8
   __TEXT.__objc_classname: 0x2d2
   __TEXT.__objc_methname: 0xa7a7
   __TEXT.__objc_methtype: 0x105d

   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2620
+  __DATA_CONST.__objc_selrefs: 0x2808
   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0x7b8
   __AUTH_CONST.__auth_got: 0xa10
   __AUTH_CONST.__const: 0xcb0
   __AUTH_CONST.__cfstring: 0x3f20
-  __AUTH_CONST.__objc_const: 0x5158
+  __AUTH_CONST.__objc_const: 0x4998
   __AUTH_CONST.__objc_intobj: 0xaf8
   __AUTH_CONST.__objc_dictobj: 0x280
   __AUTH_CONST.__objc_arrayobj: 0x108

   - /usr/lib/libmecabra.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: E71C33AB-93A5-31EF-8C24-67B95AAE0314
-  Functions: 1211
-  Symbols:   3304
-  CStrings:  3112
+  UUID: 336DAC8D-2643-396B-A89E-1F89468C5AAD
+  Functions: 1237
+  Symbols:   3341
+  CStrings:  3111
 
Symbols:
+ +[JIMAnalysisContext _sharedMecabraQueue].cold.1
+ +[JIMCandidateCellGeometries sharedGeometries].cold.1
+ +[JIMCandidateList _characterInfoForString:].cold.1
+ +[JIMDictionaryTrainer _sharedDictionaryTrainerWithCreation:].cold.1
+ +[JIMEventFilter sharedEventFilter].cold.1
+ +[JIMPeriodicTaskManager _sharedPeriodicTaskManagerWithCreation:].cold.1
+ +[JIMPreferences defaultDictionaryPath].cold.1
+ +[JIMPreferences isBaseSystem].cold.1
+ +[JIMPreferences preferenceKeysForSyncing].cold.1
+ +[JIMPreferences sharedPreferences].cold.1
+ +[JIMSecondaryCandidateController sharedSecondaryCandidateController].cold.1
+ +[JIMSharedSyncObserver _sharedSyncObserver].cold.1
+ -[JIMAnalysisContext censoredConvertedStringsFromString:maxCount:].cold.1
+ -[JIMCandidate _definitionHTML].cold.1
+ -[JIMCandidateList _candidatesForRadicalSortStyleOnlyPersonName:].cold.1
+ -[JIMCandidateList _candidatesForSymbolSortStyle].cold.1
+ -[JIMCandidateList _transliterationLocalizationKeys].cold.1
+ -[JIMEventFilter _unicharForKey:modifiers:keyboardType:keyboardLayout:].cold.1
+ -[JIMPreferences _inputSourceRefFromInputModeID:].cold.1
+ -[JIMPreferences _isInputModeIdentifier:].cold.1
+ -[JIMSession _50onPalette].cold.1
+ -[JIMSession _inputModeFromTISInputModeIdentifier:].cold.1
+ -[JIMSession _isTISInputSourceAvailableForMode:].cold.1
+ -[JIMSession _logHeaderWithString:].cold.1
+ -[JIMSession _testAutoRomanSwitchByKeywordWithCharacters:modifiers:].cold.1
+ -[JIMSession _updateSecondaryCandidatesWithTransliterationCandidates].cold.1
+ -[JIMSession handleTextFrom50onPalette:].cold.1
+ IsJISX0208Character.cold.1
+ IsJapaneseCharacter.cold.1
+ JIMSignpostLogForCategoryClientCall.cold.1
+ JIMSignpostLogForCategoryMecabraCall.cold.1
+ SetTextToSharedJapaneseTokenizer.cold.1
+ SimilarCharactersFromString.cold.1
+ TIAssetManagerClass.cold.1
+ TIInputModeClass.cold.1
+ TIMecabraEnvironmentClass.cold.1
+ TransliterateRomajiToKana.cold.2
+ _bzero
- _strcmp
CStrings:
- ".."

```
