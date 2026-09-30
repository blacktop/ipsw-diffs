## com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/XPCServices/com.apple.siri.embeddedspeech.xpc/com.apple.siri.embeddedspeech`

```diff

-3403.7.3.0.0
-  __TEXT.__text: 0x2cf18
-  __TEXT.__auth_stubs: 0x900
-  __TEXT.__objc_stubs: 0x7180
-  __TEXT.__objc_methlist: 0x152c
-  __TEXT.__const: 0x100
-  __TEXT.__gcc_except_tab: 0x1b28
-  __TEXT.__cstring: 0x3e8f
-  __TEXT.__objc_methname: 0x8dd6
-  __TEXT.__oslogstring: 0x4032
-  __TEXT.__objc_classname: 0x212
-  __TEXT.__objc_methtype: 0x1845
-  __TEXT.__unwind_info: 0x6c8
-  __DATA_CONST.__auth_got: 0x490
-  __DATA_CONST.__got: 0x650
+3404.71.4.1.1
+  __TEXT.__text: 0x2d58c
+  __TEXT.__auth_stubs: 0x920
+  __TEXT.__objc_stubs: 0x7420
+  __TEXT.__objc_methlist: 0x19ac
+  __TEXT.__const: 0x110
+  __TEXT.__gcc_except_tab: 0x1b64
+  __TEXT.__cstring: 0x3fef
+  __TEXT.__objc_methname: 0x8fc2
+  __TEXT.__oslogstring: 0x411d
+  __TEXT.__objc_classname: 0x210
+  __TEXT.__objc_methtype: 0x1879
+  __TEXT.__unwind_info: 0x6c0
+  __DATA_CONST.__auth_got: 0x4a0
+  __DATA_CONST.__got: 0x660
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xb48
-  __DATA_CONST.__cfstring: 0x2980
+  __DATA_CONST.__cfstring: 0x2ae0
   __DATA_CONST.__objc_classlist: 0x90
-  __DATA_CONST.__objc_catlist: 0x18
+  __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x78

   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2fd0
-  __DATA.__objc_selrefs: 0x1f80
-  __DATA.__objc_ivar: 0x24c
+  __DATA.__objc_const: 0x27f8
+  __DATA.__objc_selrefs: 0x20b8
+  __DATA.__objc_ivar: 0x250
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x268
   __DATA.__bss: 0x140

   - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
   - /System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
+  - /System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets
   - /System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition
   - /System/Library/PrivateFrameworks/DistributedEvaluation.framework/DistributedEvaluation
   - /System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 542
-  Symbols:   360
-  CStrings:  2247
+  Functions: 541
+  Symbols:   365
+  CStrings:  2284
 
Symbols:
+ _CCAssistantSchemaTypeAsString
+ _OBJC_CLASS_$_CCItemField
+ _OBJC_CLASS_$_CESRSpeechProfileConfig
+ _OBJC_CLASS_$_SFSpeechProfileContainerManager
+ _SFPersonaIdFromSiteURL
CStrings:
+ "%s Enrolled %tu items for (%@, %@)."
+ "%s Processed %ld App Entities, enrolled %ld."
+ "%s Siri/asr_speech_profile_app_entities feature flag disabled, App Entities will not be consumed."
+ "%s Siri/asr_speech_profile_app_entities feature flag enabled, App Entities will be consumed."
+ "-[ESSpeechProfileBuilderConnection addVocabularyItems:sourceBundleIds:isBoosted:completion:]"
+ "@\"CESRAppEntityConfig\""
+ "B40@0:8@16@24@32"
+ "URLWithString:"
+ "Vv48@0:8@\"NSArray\"16@\"NSArray\"24@\"NSArray\"32@?<v@?B@\"NSError\">40"
+ "\\appAudiobookAuthorFullName-first"
+ "\\appShortcutPhrase-first"
+ "\\health-medicationName-first"
+ "\\health-medicationNickname-first"
+ "\\home-serviceName-first"
+ "\\homeServiceArea-areaName-first"
+ "\\homeServiceArea-mapName-first"
+ "\\media-albumArtistFullName-first"
+ "\\podcast-authorFullName-first"
+ "\\podcast-playlist-first"
+ "\\radiostation-callSign-first"
+ "\\useraccountidentity-first"
+ "_appEntityConfig"
+ "_processAppEntityOrEnum:vocabularyWords:"
+ "addVocabularyItems:sourceBundleIds:isBoosted:completion:"
+ "appEntityConfig"
+ "appEntityFeatureFlagEnabled"
+ "appEntityMappingForAssistantSchemaType:"
+ "appEntityMappingForBundleId:appEntityName:"
+ "assistantDefinedSchemas"
+ "containerForPersona:"
+ "displayRepresentation"
+ "isFirstPartyBundleId:"
+ "lmeTag"
+ "lmeTemplate"
+ "overallAppEntityLimit"
+ "setSourceBundleId:"
+ "sourceBundleId"
+ "stringByTrimmingCharactersInSet:"
+ "stringValueTrimmingWhitespace"
+ "title"
+ "typeIdentifier"
+ "whitespaceCharacterSet"
- "\x05"
- "%s Processed %tu items for (%@, %@)."
- "-[ESSpeechProfileBuilderConnection addVocabularyItems:isBoosted:completion:]"
- "Vv40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?B@\"NSError\">32"
- "\\unknown-first"
- "addVocabularyItems:isBoosted:completion:"

```
