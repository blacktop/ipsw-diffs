## com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/Versions/A/XPCServices/com.apple.siri.embeddedspeech.xpc/Contents/MacOS/com.apple.siri.embeddedspeech`

```diff

-3403.7.3.0.0
-  __TEXT.__text: 0x258b8
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_stubs: 0x6080
-  __TEXT.__objc_methlist: 0x147c
+3404.82.3.0.0
+  __TEXT.__text: 0x25fe4
+  __TEXT.__auth_stubs: 0x660
+  __TEXT.__objc_stubs: 0x6320
+  __TEXT.__objc_methlist: 0x18ec
   __TEXT.__const: 0xf0
-  __TEXT.__gcc_except_tab: 0xce0
-  __TEXT.__cstring: 0x30c1
-  __TEXT.__objc_methname: 0x81ab
-  __TEXT.__oslogstring: 0x33c8
-  __TEXT.__objc_classname: 0x204
-  __TEXT.__objc_methtype: 0x173b
-  __TEXT.__unwind_info: 0x630
-  __DATA_CONST.__auth_got: 0x330
-  __DATA_CONST.__got: 0x550
+  __TEXT.__gcc_except_tab: 0xd18
+  __TEXT.__cstring: 0x3204
+  __TEXT.__objc_methname: 0x8397
+  __TEXT.__oslogstring: 0x34b3
+  __TEXT.__objc_classname: 0x206
+  __TEXT.__objc_methtype: 0x176f
+  __TEXT.__unwind_info: 0x628
+  __DATA_CONST.__auth_got: 0x340
+  __DATA_CONST.__got: 0x560
   __DATA_CONST.__const: 0x9e0
-  __DATA_CONST.__cfstring: 0x1c20
+  __DATA_CONST.__cfstring: 0x1d60
   __DATA_CONST.__objc_classlist: 0x88
-  __DATA_CONST.__objc_catlist: 0x18
+  __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2e58
-  __DATA.__objc_selrefs: 0x1be0
-  __DATA.__objc_ivar: 0x234
+  __DATA.__objc_const: 0x2698
+  __DATA.__objc_selrefs: 0x1d18
+  __DATA.__objc_ivar: 0x238
   __DATA.__objc_data: 0x550
   __DATA.__data: 0x268
   __DATA.__bss: 0x100

   - /System/Library/PrivateFrameworks/BiomePubSub.framework/Versions/A/BiomePubSub
   - /System/Library/PrivateFrameworks/BiomeStorage.framework/Versions/A/BiomeStorage
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams
+  - /System/Library/PrivateFrameworks/CascadeSets.framework/Versions/A/CascadeSets
   - /System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/Versions/A/CoreEmbeddedSpeechRecognition
   - /System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/Versions/A/EmbeddedAcousticRecognition
   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/Versions/A/IntelligencePlatformLibrary

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C7F500A0-486C-3298-A011-72C5479366CE
-  Functions: 528
-  Symbols:   282
-  CStrings:  2122
+  UUID: 679A02AD-788C-3048-88CF-1457C2E37835
+  Functions: 527
+  Symbols:   287
+  CStrings:  2169
 
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
- "%s Processed %tu items for (%@, %@)."
- "-[ESSpeechProfileBuilderConnection addVocabularyItems:isBoosted:completion:]"
- "Vv40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?B@\"NSError\">32"
- "\\unknown-first"
- "addVocabularyItems:isBoosted:completion:"

```
