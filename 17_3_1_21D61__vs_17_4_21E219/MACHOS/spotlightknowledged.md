## spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

-2274.13.3.0.0
-  __TEXT.__text: 0x75bb8
-  __TEXT.__auth_stubs: 0x1370
-  __TEXT.__objc_stubs: 0x7060
-  __TEXT.__objc_methlist: 0x3f8c
+2274.23.0.3.0
+  __TEXT.__text: 0x76280
+  __TEXT.__auth_stubs: 0x1340
+  __TEXT.__objc_stubs: 0x70c0
+  __TEXT.__objc_methlist: 0x3fe4
   __TEXT.__const: 0x408
   __TEXT.__oslogstring: 0x1b58
-  __TEXT.__gcc_except_tab: 0x61a0
-  __TEXT.__cstring: 0x34d5
-  __TEXT.__objc_methname: 0x789c
-  __TEXT.__objc_classname: 0x737
-  __TEXT.__objc_methtype: 0xab1
+  __TEXT.__gcc_except_tab: 0x61b4
+  __TEXT.__cstring: 0x3523
+  __TEXT.__objc_methname: 0x79b6
+  __TEXT.__objc_classname: 0x747
+  __TEXT.__objc_methtype: 0xacd
   __TEXT.__dlopen_cstrs: 0x11c
-  __TEXT.__unwind_info: 0x271c
+  __TEXT.__unwind_info: 0x2724
   __TEXT.__eh_frame: 0x74
-  __DATA_CONST.__auth_got: 0x9d0
-  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__auth_got: 0x9b8
+  __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x26a8
-  __DATA_CONST.__cfstring: 0x3e00
+  __DATA_CONST.__const: 0x26c8
+  __DATA_CONST.__cfstring: 0x3e80
   __DATA_CONST.__objc_classlist: 0x3f8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x490
+  __DATA_CONST.__objc_superrefs: 0x260
   __DATA_CONST.__objc_intobj: 0x1b0
   __DATA_CONST.__objc_arraydata: 0x7b0
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_arrayobj: 0x210
-  __DATA.__objc_const: 0x6780
-  __DATA.__objc_selrefs: 0x1f98
-  __DATA.__objc_classrefs: 0x490
-  __DATA.__objc_superrefs: 0x260
+  __DATA.__objc_const: 0x67a0
+  __DATA.__objc_selrefs: 0x1fd0
   __DATA.__objc_ivar: 0x2a4
   __DATA.__objc_data: 0x27b0
   __DATA.__data: 0x2d8
-  __DATA.__bss: 0x298
+  __DATA.__bss: 0x2b8
   __DATA.__common: 0xc010
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7754D2B9-2263-3428-A80E-24E0DB820D49
-  Functions: 2118
-  Symbols:   442
-  CStrings:  2835
+  UUID: 51A825BB-855E-3444-9053-D6E78E7EFE58
+  Functions: 2131
+  Symbols:   437
+  CStrings:  2854
 
Symbols:
+ _CFURLGetTypeID
- _NLTaggerCreate
- _SILanguageModelPurge
- _SILanguageModelRelease
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
- _kNLTagSchemeLemma
- _kNLTagSchemeTokenType
CStrings:
+ "\a\x15"
+ ", "
+ "@\"NSLocale\""
+ "B32@0:8@?16@?24"
+ "B48@0:8@16@24@?32@?40"
+ "Keyphraser"
+ "T@\"NSSet\",R,N,V_availableLanguages"
+ "TB,N,V_didProcessKeyphrases"
+ "TB,N,V_didProcessPeople"
+ "_availableLanguages"
+ "_currentLocale"
+ "_didProcessKeyphrases"
+ "_didProcessPeople"
+ "absoluteString"
+ "authorFromRecord:"
+ "didProcessKeyphrases"
+ "didProcessPeople"
+ "enumerateProcessedItemsFromRecord:referenceIdentifier:bundleIdentifier:protectionClass:includeKeyphrases:includePeople:processedItemBlock:cancelBlock:"
+ "generateKeyphrasesForRecord:processedItem:cancelBlock:"
+ "generateMegadomePeopleUsingBlock:cancelBlock:"
+ "generatePeopleForRecord:processedItem:processedItemBlock:cancelBlock:"
+ "loadKeyphraserWithCancelBlock:"
+ "loadPeopleExtractorWithCancelBlock:"
+ "processCSArchivesWithGroup:protectionClasses:includeKeyphrases:includePeople:shouldRemove:archiverNextPathBlock:processedPathBlock:processedItemBlock:errorLogBlock:cancelBlock:"
+ "processCSJournalsWithGroup:protectionClasses:includeKeyphrases:includePeople:shouldRemove:readerNextPathBlock:deletedReferencesBlock:processedPathBlock:processedItemBlock:errorLogBlock:cancelBlock:"
+ "processKeyphrases:load"
+ "processPeople:load"
+ "processPeopleFromRecord:megadome"
+ "runCSQueryWithGroup:queryContext:queryString:includeKeyphrases:includePeople:shouldArchive:archiverNextPathBlock:archiverNextPathNameBlock:processedPathBlock:processedBatchBlock:processedItemBlock:errorLogBlock:cancelBlock:"
+ "setDidProcessKeyphrases:"
+ "setDidProcessPeople:"
+ "stringValueFromRecord:key:"
- "\x031"
- "\f"
- "T@\"NSSet\",R,N"
- "^v"
- "^{_LanguageModel=}"
- "_languageModel"
- "_nameComponentsCache"
- "_nameFormatter"
- "_tagger"
- "displayNameForNameComponents:inString:"
- "enumerateInfoInString:usingBlock:"
- "enumerateMegadomePeopleUsingBlock:"
- "enumerateProcessedItemsFromRecord:referenceIdentifier:bundleIdentifier:protectionClass:includeTextContent:includePeople:processedItemBlock:cancelBlock:"
- "nameComponentsFromString:"
- "processCSArchivesWithGroup:protectionClasses:includeTextContent:includePeople:shouldRemove:archiverNextPathBlock:processedPathBlock:processedItemBlock:errorLogBlock:cancelBlock:"
- "processCSJournalsWithGroup:protectionClasses:includeTextContent:includePeople:shouldRemove:readerNextPathBlock:deletedReferencesBlock:processedPathBlock:processedItemBlock:errorLogBlock:cancelBlock:"
- "processKeyphrasesFromRecord:processedItem:cancelBlock:"
- "runCSQueryWithGroup:queryContext:queryString:includeTextContent:includePeople:shouldArchive:archiverNextPathBlock:archiverNextPathNameBlock:processedPathBlock:processedBatchBlock:processedItemBlock:errorLogBlock:cancelBlock:"

```
