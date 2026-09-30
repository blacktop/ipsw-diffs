## com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/XPCServices/com.apple.siri.embeddedspeech.xpc/com.apple.siri.embeddedspeech`

```diff

-3405.29.3.11.1
-  __TEXT.__text: 0x2dc04
+3500.97.2.1.1
+  __TEXT.__text: 0x2f130
   __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_stubs: 0x75a0
-  __TEXT.__objc_methlist: 0x19c4
+  __TEXT.__objc_stubs: 0x7a00
+  __TEXT.__objc_methlist: 0x1a04
   __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x1b44
-  __TEXT.__cstring: 0x4004
-  __TEXT.__objc_methname: 0x91b6
-  __TEXT.__oslogstring: 0x4257
-  __TEXT.__objc_classname: 0x212
-  __TEXT.__objc_methtype: 0x18d8
-  __TEXT.__unwind_info: 0x6c0
+  __TEXT.__gcc_except_tab: 0x1b4c
+  __TEXT.__cstring: 0x42b4
+  __TEXT.__objc_methname: 0x96e1
+  __TEXT.__oslogstring: 0x45c4
+  __TEXT.__objc_classname: 0x201
+  __TEXT.__objc_methtype: 0x1979
+  __TEXT.__ustring: 0x4
+  __TEXT.__unwind_info: 0x6c8
   __DATA_CONST.__auth_got: 0x498
-  __DATA_CONST.__got: 0x6a0
+  __DATA_CONST.__got: 0x6c0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xb70
-  __DATA_CONST.__cfstring: 0x2b00
-  __DATA_CONST.__objc_classlist: 0x90
+  __DATA_CONST.__cfstring: 0x2c80
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2898
-  __DATA.__objc_selrefs: 0x2118
-  __DATA.__objc_ivar: 0x264
-  __DATA.__objc_data: 0x5a0
+  __DATA.__objc_const: 0x2840
+  __DATA.__objc_selrefs: 0x2240
+  __DATA.__objc_ivar: 0x270
+  __DATA.__objc_data: 0x550
   __DATA.__data: 0x268
   __DATA.__bss: 0x140
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1DADED05-1225-3A98-B758-A8AFE80E5129
-  Functions: 543
-  Symbols:   372
-  CStrings:  2642
+  UUID: FE4046AC-706F-341C-8C57-6BDA81E3756F
+  Functions: 549
+  Symbols:   376
+  CStrings:  2729
 
Symbols:
+ _OBJC_CLASS_$_CCTypeIdentifierRegistry
+ _OBJC_CLASS_$_CESRVocabularyLabel
+ _OBJC_CLASS_$_EAREntityCleanup
+ _OBJC_CLASS_$__EAREntityTagger
CStrings:
+ "%s %@ at least one emoji."
+ "%s %@ at least one extracted entity."
+ "%s %@ at least one special character."
+ "%s Cleanup %@ enabled."
+ "%s Enrolled %ld extracted entities."
+ "%s Entity Cleanup: Apply Regex %@ enabled"
+ "%s Entity Cleanup: Emoji Removal %@ enabled for AppEntities"
+ "%s Entity Cleanup: Emoji Removal %@ enabled for Non-AppEntities"
+ "%s Entity Cleanup: Special Character Removal %@ enabled for AppEntities"
+ "%s Entity Cleanup: Special Character Removal %@ enabled for Non-AppEntities"
+ "%s Entity Extraction Limit: %ld"
+ "%s Extracted entity equals original string. Skipping."
+ "%s Extraction %@ enabled."
+ "%s Failed applying regex: %@"
+ "%s Failed to add extracted entity (type: %@) to vocabulary."
+ "%s GeoLM: geoLM region specific [%{private}@] asset exists on device, but not compatible."
+ "%s GeoLM: region specific [%{private}@] geo-config json file=%{public}@"
+ "%s GeoLM: region specific asset is not found for given language=%{public}@ regionId=%{private}@"
+ "%s No mapping found for extracted entity with tagName %@. Skipping."
+ "%s No mapping found for extracted entity with tagName: %@. Using default mapping."
+ "%s Set recognized text: %{private}@"
+ "+[ESUserData _fetchExtractedEntityMappingsForEntities:extractionVocabLabels:originalInputString:]"
+ "-[ESUserData _applyEntityCleanup:enableEmojiCleanup:enableSpecialCharacterCleanup:customRegex:]"
+ "-[ESUserData _performEntityExtractionAndAddToVocabWords:vocabularyWords:extractionVocabLabels:]_block_invoke"
+ "-[ESUserData _processContactItem:contactWords:vocabularyWords:]"
+ "-[ESUserData _processRadioItem:radioWords:]"
+ "-extracted"
+ "4d8033c8-b9f3-4168-ae10-e04ac69ae864"
+ "5d947328-fccf-4c7f-b772-a156ab177a0a"
+ "7e65308b-bea2-4201-9f02-4ae398303003"
+ "<%@: %p; components: %@; frequency: %d>"
+ "<%@: %p; firstPartyContactWords: %@; thirdPartyContactWords: %@; groupNameWords: %@; vocabularyWords: %@; radioWords: %@>"
+ "@\"CESRDirectDonationConfig\""
+ "@\"EAREntityCleanup\""
+ "@\"_EAREntityTagger\""
+ "@28@0:8S16@20"
+ "@40@0:8@16B24B28@32"
+ "DOES NOT HAVE"
+ "HAS"
+ "IS"
+ "IS NOT"
+ "T@\"NSSet\",R,C,N"
+ "_addVocabWord:vocabularyLabel:toVocabularyWords:"
+ "_applyEntityCleanup:enableEmojiCleanup:enableSpecialCharacterCleanup:customRegex:"
+ "_applyEntityCleanupToNonAppEntity:"
+ "_directDonationConfig"
+ "_entityCleaner"
+ "_entityTagger"
+ "_extractedEntityBudget"
+ "_extractedLabelForLabel:"
+ "_fetchAppEntityMappingForBundleId:appEntityConfig:assistantSchemas:entityType:"
+ "_fetchExtractedEntityMappingsForEntities:extractionVocabLabels:originalInputString:"
+ "_isEntityInExclusionList:bundleId:type:"
+ "_normalize:"
+ "_performEntityExtractionAndAddToVocabWords:vocabularyWords:extractionVocabLabels:"
+ "_processAppEntity:vocabularyWords:"
+ "_processContactItem:contactWords:vocabularyWords:"
+ "_processSingleVocabItem:fieldContent:vocabularyLabel:vocabularyWords:"
+ "_vocabularyLabelsForFieldType:directDonationConfig:"
+ "applyRegex"
+ "applyRegex:toString:"
+ "codepathIds"
+ "default"
+ "descriptionForTypeIdentifier:"
+ "directDonationConfig"
+ "enableEmojiCleanupFromAppEntities"
+ "enableEmojiCleanupFromNonAppEntities"
+ "enableEntityCleanup"
+ "enableEntityExtraction"
+ "enableSpecialCharacterCleanupFromAppEntities"
+ "enableSpecialCharacterCleanupFromNonAppEntities"
+ "entitiesExcludedFromEmojiCleanup"
+ "entitiesExcludedFromSpecialCharacterCleanup"
+ "entityContent"
+ "extractionVocabLabels"
+ "initWithLmeTemplate:lmeTag:"
+ "mappingForFieldTypeName:"
+ "overallEntityExtractionLimit"
+ "precomposedStringWithCanonicalMapping"
+ "primaryVocabLabel"
+ "removeDuplicateWhitespace:"
+ "removeEmojis:"
+ "removeSpecialCharacters:fromString:"
+ "specialCharactersToRemove"
+ "speechRecognizer:didProduceLoggableMultiUserPackages:"
+ "speechRecognizer:didRecognizeFinalResultMultiUserPackages:"
+ "stringByAppendingString:"
+ "tagEntitiesWithTagNamesIn:"
+ "unionSet:"
+ "v32@0:8@\"_EARSpeechRecognizer\"16@\"NSDictionary\"24"
+ "v32@?0@\"CESRVocabularyLabel\"8@\"NSOrderedSet\"16^B24"
+ "v32@?0@\"NSString\"8@\"CESRVocabularyLabel\"16^B24"
+ "v44@0:8S16@20@28@36"
+ "vocabularyLabel"
+ "\xa0"
- "%s GeoLM: geoLM region specific [%@] asset exists on device, but not compatible."
- "%s GeoLM: region specific [%@] geo-config json file=%@"
- "%s GeoLM: region specific asset is not found for given language=%@ regionId=%@"
- "%s Set recognized text: %@"
- "+[ESUserData _processContactItem:contactWords:]"
- "+[ESUserData _processRadioItem:radioWords:]"
- "@20@0:8S16"
- "ESVocabularyLabel"
- "T@\"NSString\",R,C,N,V_speechCategoryName"
- "T@\"NSString\",R,C,N,V_tagName"
- "_addVocabWord:vocabularyLabels:toVocabularyWords:"
- "_processAppEntityOrEnum:vocabularyWords:"
- "_processContactItem:contactWords:"
- "_speechCategoryName"
- "_tagName"
- "_vocabularyLabelsForFieldType:"
- "initWithSpeechCategoryName:tagName:"
- "speechCategoryName"
- "v32@?0@\"ESVocabularyLabel\"8@\"NSOrderedSet\"16^B24"

```
