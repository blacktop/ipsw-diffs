## DictionaryUI

> `/System/Library/PrivateFrameworks/DictionaryUI.framework/DictionaryUI`

```diff

-50.0.0.0.0
-  __TEXT.__text: 0x2450
-  __TEXT.__auth_stubs: 0x320
+53.0.0.0.0
+  __TEXT.__text: 0x22a4
   __TEXT.__objc_methlist: 0x32c
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x3c9
-  __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__unwind_info: 0x128
-  __TEXT.__objc_classname: 0x8e
-  __TEXT.__objc_methname: 0xc65
-  __TEXT.__objc_methtype: 0x184
-  __TEXT.__objc_stubs: 0xca0
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__cstring: 0x3d2
+  __TEXT.__gcc_except_tab: 0x84
+  __TEXT.__unwind_info: 0x120
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3b8
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1a0
+  __DATA_CONST.__got: 0xa0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x3a0
   __AUTH_CONST.__objc_const: 0x6b0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x4c
   __DATA_DIRTY.__objc_data: 0xa0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 04F50984-6AC9-3EE7-911D-AB710C6D89DC
+  UUID: 4709C156-1A66-32F9-8E02-2123CF8E4BFC
   Functions: 67
-  Symbols:   385
-  CStrings:  254
+  Symbols:   389
+  CStrings:  62
 
Symbols:
+ ___block_literal_global.539
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x22
+ _objc_retain_x3
+ _objc_retain_x8
- ___block_literal_global.519
- _objc_release_x26
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
Functions:
~ -[DUEntryViewController initWithDefinitionValue:] : 156 -> 152
~ -[DUEntryViewController viewDidLoad] : 400 -> 384
~ -[MAAsset(UIReferenceLibraryViewControllerAdditions_Private) _formatVersion] : 96 -> 88
~ -[MAAsset(UIReferenceLibraryViewControllerAdditions_Private) _contentVersion] : 96 -> 88
~ -[NSArray(UIReferenceLibraryViewControllerAdditions_Private) _filteredArrayOfObjectsPassingTest:] : 96 -> 88
~ -[DUDefinitionValue definition] : 220 -> 200
~ -[DUDefinitionValue longDefinition] : 128 -> 116
~ -[DUDefinitionValue definitionElements] : 212 -> 204
~ -[DUDefinitionValue _HTMLDefinitionForType:] : 212 -> 208
~ -[DUDefinitionValue description] : 140 -> 132
~ -[DUDefinitionValue setRawAsset:] : 64 -> 12
~ -[DUDefinitionDictionary initWithAsset:] : 344 -> 324
~ -[DUDefinitionDictionary setAssetToUpgrade:] : 64 -> 12
~ -[DUDefinitionDictionary localizedLanguageName] : 380 -> 352
~ -[DUDefinitionDictionary localizedSortName] : 104 -> 96
~ -[DUDefinitionDictionary localizedDictionaryName] : 368 -> 336
~ +[DUDefinitionDictionary displayNameForLanguageIdentifier:context:] : 128 -> 124
~ ___67+[DUDefinitionDictionary displayNameForLanguageIdentifier:context:]_block_invoke : 204 -> 188
~ -[DUDefinitionDictionary _hasDefinitionForTerm:] : 152 -> 144
~ -[DUDefinitionDictionary setActivated:] : 100 -> 92
~ -[DUDefinitionDictionary description] : 200 -> 188
~ -[DUDictionaryManager init] : 124 -> 120
~ -[DUDictionaryManager _hasDefinitionForTerm:] : 296 -> 300
~ -[DUDictionaryManager _availableDictionaryAssets] : 208 -> 200
~ -[DUDictionaryManager _allAvailableDefinitionDictionaries] : 1356 -> 1312
~ ___58-[DUDictionaryManager _allAvailableDefinitionDictionaries]_block_invoke : 104 -> 108
~ ___58-[DUDictionaryManager _allAvailableDefinitionDictionaries]_block_invoke_2 : 64 -> 60
~ ___58-[DUDictionaryManager _allAvailableDefinitionDictionaries]_block_invoke_3 : 244 -> 228
~ -[DUDictionaryManager _compareOrderOfDictionary:withDictionary:] : 232 -> 228
~ -[DUDictionaryManager _migrateInstalledStateForNewDictionaries:] : 872 -> 852
CStrings:
- ".cxx_destruct"
- "@\"DUDefinitionValue\""
- "@\"MAAsset\""
- "@\"NSArray\""
- "@\"NSAttributedString\""
- "@\"NSDictionary\""
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8q16"
- "@32@0:8@16@24"
- "@32@0:8@16q24"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "DUDefinitionDictionary"
- "DUDefinitionValue"
- "DUDictionaryManager"
- "DUEntryViewController"
- "T@\"DUDefinitionValue\",&,V_definitionValue"
- "T@\"MAAsset\",&,N,V_rawAsset"
- "T@\"MAAsset\",R,V_rawAsset"
- "T@\"NSArray\",R,V_availableDefinitionDictionaries"
- "T@\"NSAttributedString\",R,V_definition"
- "T@\"NSDictionary\",R,V_definitionElements"
- "T@\"NSString\",R"
- "T@\"NSString\",R,V_definitionLanguage"
- "T@\"NSString\",R,V_localizedDictionaryName"
- "T@\"NSString\",R,V_longDefinition"
- "T@\"NSString\",R,V_term"
- "TB,N,V_activated"
- "TB,R"
- "TB,V_isAppleDictionary"
- "TB,V_isTTYDictionary"
- "T^{__CFArray=},V_foundRecordRefs"
- "T^{__DCSDictionary=},R"
- "Tf,V_progress"
- "Tq,V_preferredOrder"
- "UIReferenceLibraryViewControllerAdditions_Private"
- "^{__CFArray=}"
- "^{__CFArray=}16@0:8"
- "^{__DCSDictionary=}"
- "^{__DCSDictionary=}16@0:8"
- "_HTMLDefinitionForType:"
- "_activated"
- "_addUserStyleSheet:"
- "_allAvailableDefinitionDictionaries"
- "_assetToUpgrade"
- "_availableDefinitionDictionaries"
- "_availableDictionaryAssets"
- "_compareOrderOfDictionary:withDictionary:"
- "_contentVersion"
- "_definition"
- "_definitionElements"
- "_definitionLanguage"
- "_definitionValue"
- "_definitionValueForTerm:"
- "_definitionValuesForTerm:"
- "_dictionary"
- "_dictionaryAssetType"
- "_downloadDictionaryAssetCatalogWithTimeout:completion:"
- "_filteredArrayOfObjectsPassingTest:"
- "_formatVersion"
- "_foundRecordRefs"
- "_hasDefinitionForTerm:"
- "_initiallyEmptyAssets"
- "_isAppleDictionary"
- "_isTTYDictionary"
- "_localizedDictionaryName"
- "_longDefinition"
- "_migrateInstalledStateForNewDictionaries:"
- "_preferredOrder"
- "_progress"
- "_rawAsset"
- "_term"
- "activated"
- "addObject:"
- "addSubview:"
- "appendString:"
- "array"
- "assetManager"
- "attributedString"
- "attributes"
- "availableDefinitionDictionaries"
- "bounds"
- "bundleForClass:"
- "canonicalLanguageIdentifierFromString:"
- "clearColor"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dataUsingEncoding:"
- "dealloc"
- "definition"
- "definitionElements"
- "definitionLanguage"
- "definitionValue"
- "description"
- "dictionaryRef"
- "displayNameForLanguageIdentifier:context:"
- "entryViewControllerWithDefinitionValue:"
- "f"
- "f16@0:8"
- "firstObject"
- "foundRecordRefs"
- "getLocalFileUrl"
- "indexesOfObjectsPassingTest:"
- "init"
- "initWithAsset:"
- "initWithAssetType:"
- "initWithCapacity:"
- "initWithData:options:"
- "initWithDefinitionDictionary:term:"
- "initWithDefinitionValue:"
- "initWithFrame:configuration:"
- "initWithLocaleIdentifier:"
- "initWithNibName:bundle:"
- "initWithSource:forMainFrameOnly:"
- "initWithType:"
- "integerValue"
- "isAppleDictionary"
- "isEqual:"
- "isEqualToString:"
- "isTTYDictionary"
- "length"
- "loadHTMLString:baseURL:"
- "localizedDictionaryName"
- "localizedLanguageName"
- "localizedSortName"
- "localizedStandardCompare:"
- "localizedStringForKey:value:table:"
- "localizedStringForLanguage:context:"
- "longDefinition"
- "mainBundle"
- "needsDownloadNewerVersion"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectsAtIndexes:"
- "preferredLanguages"
- "preferredLocalizations"
- "preferredOrder"
- "progress"
- "purge:"
- "purgeSync"
- "q"
- "q16@0:8"
- "q32@0:8@16@24"
- "queryMetaDataSync"
- "rawAsset"
- "removeObject:"
- "results"
- "returnTypes:"
- "runQueryAndReturnError:"
- "setActivated:"
- "setAllowsCellularAccess:"
- "setAssetToUpgrade:"
- "setAutoresizingMask:"
- "setBackgroundColor:"
- "setDefinitionValue:"
- "setDiscretionary:"
- "setDoNotBlockBeforeFirstUnlock:"
- "setFoundRecordRefs:"
- "setIsAppleDictionary:"
- "setIsTTYDictionary:"
- "setOpaque:"
- "setPreferredOrder:"
- "setProgress:"
- "setQueriesLocalAssetInformationOnly:"
- "setRawAsset:"
- "setTimeoutIntervalForResource:"
- "setTitle:"
- "setUserContentController:"
- "sortUsingComparator:"
- "startCatalogDownload:options:then:"
- "state"
- "stringByDeletingPathExtension"
- "stringWithCapacity:"
- "stringWithFormat:"
- "substringToIndex:"
- "term"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8f16"
- "v24@0:8@16"
- "v24@0:8^{__CFArray=}16"
- "v24@0:8q16"
- "v32@0:8q16@?24"
- "view"
- "viewDidLoad"
- "wasLocal"

```
