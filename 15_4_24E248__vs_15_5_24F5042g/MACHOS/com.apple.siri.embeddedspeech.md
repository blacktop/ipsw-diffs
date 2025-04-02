## com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/Versions/A/XPCServices/com.apple.siri.embeddedspeech.xpc/Contents/MacOS/com.apple.siri.embeddedspeech`

```diff

-3404.82.3.0.0
-  __TEXT.__text: 0x25fe4
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_stubs: 0x6320
-  __TEXT.__objc_methlist: 0x18ec
+3405.20.3.0.0
+  __TEXT.__text: 0x266d4
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_stubs: 0x6480
+  __TEXT.__objc_methlist: 0x1904
   __TEXT.__const: 0xf0
-  __TEXT.__gcc_except_tab: 0xd18
-  __TEXT.__cstring: 0x3204
-  __TEXT.__objc_methname: 0x8397
-  __TEXT.__oslogstring: 0x34b3
+  __TEXT.__gcc_except_tab: 0xcf8
+  __TEXT.__cstring: 0x3219
+  __TEXT.__objc_methname: 0x852e
+  __TEXT.__oslogstring: 0x35ed
   __TEXT.__objc_classname: 0x206
-  __TEXT.__objc_methtype: 0x176f
+  __TEXT.__objc_methtype: 0x17ce
   __TEXT.__unwind_info: 0x628
-  __DATA_CONST.__auth_got: 0x340
-  __DATA_CONST.__got: 0x560
-  __DATA_CONST.__const: 0x9e0
-  __DATA_CONST.__cfstring: 0x1d60
+  __DATA_CONST.__auth_got: 0x338
+  __DATA_CONST.__got: 0x5a0
+  __DATA_CONST.__const: 0xa10
+  __DATA_CONST.__cfstring: 0x1d80
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2698
-  __DATA.__objc_selrefs: 0x1d18
-  __DATA.__objc_ivar: 0x238
+  __DATA.__objc_const: 0x2738
+  __DATA.__objc_selrefs: 0x1d70
+  __DATA.__objc_ivar: 0x24c
   __DATA.__objc_data: 0x550
   __DATA.__data: 0x268
   __DATA.__bss: 0x100

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 527
-  Symbols:   287
-  CStrings:  1947
+  Functions: 529
+  Symbols:   294
+  CStrings:  1972
 
Symbols:
+ _NSTextCheckingCityKey
+ _NSTextCheckingCountryKey
+ _NSTextCheckingPhoneKey
+ _NSTextCheckingStateKey
+ _NSTextCheckingStreetKey
+ _NSTextCheckingZIPKey
+ _OBJC_CLASS_$_NSDataDetector
+ _OBJC_CLASS_$_NSMutableCharacterSet
+ _OBJC_CLASS_$_SFSpeechProfileContainer
- _OBJC_CLASS_$_SFSpeechProfileContainerManager
- _SFPersonaIdFromSiteURL
CStrings:
+ "\b"
+ "\n%"
+ "%s Failed to initialize NSDataDetector for NSTextCheckingTypes-based entity sanitization, skipping enrolling entities of impacted types."
+ "%s Failed to initialize _EARUserProfile, error: %@"
+ "%s No installed %@ asset for language: %@"
+ "%s Using model from %@ asset for %@ at path: %@"
+ "%s Using model override at path: %@"
+ "-[ESUserData _processVocabularyItem:vocabularyWords:]"
+ "-[ESUserData _textDatatypeDetector]"
+ "@\"CESREntityCleanupConfig\""
+ "@\"NSDataDetector\""
+ "@\"SFSpeechProfileContainer\""
+ "Vv68@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40q48B56@?<v@?B@\"NSError\">60"
+ "Vv68@0:8@16@24@32@40q48B56@?60"
+ "\\NT-location"
+ "\\location-first"
+ "_container"
+ "_entityCleanupConfig"
+ "_isInUserVault"
+ "_personaId"
+ "_sanitizeTextForDatatypes:detector:"
+ "_textDatatypeDetector"
+ "addressComponents"
+ "dataDetectorWithTypes:error:"
+ "enableDatatypeCleanupFromNonAppEntities"
+ "entityCleanupConfig"
+ "formUnionWithCharacterSet:"
+ "initWithConfig:language:overrides:textNormalizationModelRoot:sdapiOverrides:emptyVoc:pgVoc:paramsetHolder:isJit:error:"
+ "initWithPersona:"
+ "matchesInString:options:range:"
+ "replaceOccurrencesOfString:withString:options:range:"
+ "resultType"
+ "setProfileConfigWithLanguage:profileDir:userId:personaId:dataProtectionClass:isInUserVault:completion:"
+ "setString:"
+ "stringWithString:"
+ "whitespaceAndNewlineCharacterSet"
- "\x06"
- "\t\x14"
- "+[ESUserData _processVocabularyItem:vocabularyWords:]"
- "Error during _EARUserProfile initialization"
- "URLWithString:"
- "Vv56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32q40@?<v@?B@\"NSError\">48"
- "Vv56@0:8@16@24@32q40@?48"
- "containerForPersona:"
- "initWithConfiguration:language:overrides:sdapiOverrides:emptyVoc:pgVoc:paramsetHolder:isJit:"
- "setProfileConfigWithLanguage:profileDir:userId:dataProtectionClass:completion:"
- "switchToNewAssetsForAssetType:"

```
