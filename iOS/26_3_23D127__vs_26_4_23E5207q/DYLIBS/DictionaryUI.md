## DictionaryUI

> `/System/Library/PrivateFrameworks/DictionaryUI.framework/DictionaryUI`

```diff

 50.0.0.0.0
-  __TEXT.__text: 0x2290
-  __TEXT.__auth_stubs: 0x360
+  __TEXT.__text: 0x2450
+  __TEXT.__auth_stubs: 0x320
   __TEXT.__objc_methlist: 0x32c
   __TEXT.__const: 0x50
   __TEXT.__cstring: 0x3c9
-  __TEXT.__gcc_except_tab: 0x84
-  __TEXT.__unwind_info: 0x120
+  __TEXT.__gcc_except_tab: 0x88
+  __TEXT.__unwind_info: 0x128
   __TEXT.__objc_classname: 0x8e
   __TEXT.__objc_methname: 0xc65
   __TEXT.__objc_methtype: 0x184

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3b8
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1c0
+  __AUTH_CONST.__auth_got: 0x1a0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x3a0
   __AUTH_CONST.__objc_const: 0x6b0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6848A46E-92D5-3999-8587-277F12E5F15E
+  UUID: 0F546C5D-6C1F-3762-8951-953A0C2D7054
   Functions: 67
-  Symbols:   389
+  Symbols:   385
   CStrings:  254
 
Symbols:
+ _objc_release_x26
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x26
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x22
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ -[DUEntryViewController initWithDefinitionValue:] : 152 -> 156
~ -[DUEntryViewController viewDidLoad] : 384 -> 400
~ -[MAAsset(UIReferenceLibraryViewControllerAdditions_Private) _formatVersion] : 88 -> 96
~ -[MAAsset(UIReferenceLibraryViewControllerAdditions_Private) _contentVersion] : 88 -> 96
~ -[NSArray(UIReferenceLibraryViewControllerAdditions_Private) _filteredArrayOfObjectsPassingTest:] : 88 -> 96
~ -[DUDefinitionValue definition] : 200 -> 220
~ -[DUDefinitionValue longDefinition] : 116 -> 128
~ -[DUDefinitionValue definitionElements] : 204 -> 212
~ -[DUDefinitionValue _HTMLDefinitionForType:] : 208 -> 212
~ -[DUDefinitionValue description] : 132 -> 140
~ -[DUDefinitionValue setRawAsset:] : 12 -> 64
~ -[DUDefinitionDictionary initWithAsset:] : 324 -> 344
~ -[DUDefinitionDictionary setAssetToUpgrade:] : 12 -> 64
~ -[DUDefinitionDictionary localizedLanguageName] : 352 -> 380
~ -[DUDefinitionDictionary localizedSortName] : 96 -> 104
~ -[DUDefinitionDictionary localizedDictionaryName] : 336 -> 368
~ +[DUDefinitionDictionary displayNameForLanguageIdentifier:context:] : 124 -> 128
~ ___67+[DUDefinitionDictionary displayNameForLanguageIdentifier:context:]_block_invoke : 188 -> 204
~ -[DUDefinitionDictionary _hasDefinitionForTerm:] : 144 -> 152
~ -[DUDefinitionDictionary setActivated:] : 92 -> 100
~ -[DUDefinitionDictionary description] : 188 -> 200
~ -[DUDictionaryManager init] : 120 -> 124
~ -[DUDictionaryManager _definitionValuesForTerm:] : 384 -> 388
~ -[DUDictionaryManager _availableDictionaryAssets] : 200 -> 208
~ -[DUDictionaryManager _allAvailableDefinitionDictionaries] : 1304 -> 1356
~ ___58-[DUDictionaryManager _allAvailableDefinitionDictionaries]_block_invoke : 108 -> 104
~ ___58-[DUDictionaryManager _allAvailableDefinitionDictionaries]_block_invoke_2 : 60 -> 64
~ ___58-[DUDictionaryManager _allAvailableDefinitionDictionaries]_block_invoke_3 : 228 -> 244
~ -[DUDictionaryManager _compareOrderOfDictionary:withDictionary:] : 228 -> 232
~ -[DUDictionaryManager _migrateInstalledStateForNewDictionaries:] : 848 -> 872

```
