## com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/XPCServices/com.apple.siri.embeddedspeech.xpc/com.apple.siri.embeddedspeech`

```diff

-3404.82.3.0.0
-  __TEXT.__text: 0x2d594
-  __TEXT.__auth_stubs: 0x920
-  __TEXT.__objc_stubs: 0x7420
-  __TEXT.__objc_methlist: 0x19ac
+3405.20.3.0.0
+  __TEXT.__text: 0x2dc04
+  __TEXT.__auth_stubs: 0x910
+  __TEXT.__objc_stubs: 0x75a0
+  __TEXT.__objc_methlist: 0x19c4
   __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x1b64
-  __TEXT.__cstring: 0x3fef
-  __TEXT.__objc_methname: 0x8fc2
-  __TEXT.__oslogstring: 0x411d
-  __TEXT.__objc_classname: 0x210
-  __TEXT.__objc_methtype: 0x1879
+  __TEXT.__gcc_except_tab: 0x1b44
+  __TEXT.__cstring: 0x4004
+  __TEXT.__objc_methname: 0x91b6
+  __TEXT.__oslogstring: 0x4257
+  __TEXT.__objc_classname: 0x212
+  __TEXT.__objc_methtype: 0x18d8
   __TEXT.__unwind_info: 0x6c0
-  __DATA_CONST.__auth_got: 0x4a0
-  __DATA_CONST.__got: 0x660
+  __DATA_CONST.__auth_got: 0x498
+  __DATA_CONST.__got: 0x6a0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xb48
-  __DATA_CONST.__cfstring: 0x2ae0
+  __DATA_CONST.__const: 0xb70
+  __DATA_CONST.__cfstring: 0x2b00
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x27f8
-  __DATA.__objc_selrefs: 0x20b8
-  __DATA.__objc_ivar: 0x250
+  __DATA.__objc_const: 0x2898
+  __DATA.__objc_selrefs: 0x2118
+  __DATA.__objc_ivar: 0x264
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x268
   __DATA.__bss: 0x140

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 541
-  Symbols:   365
-  CStrings:  2284
+  Functions: 543
+  Symbols:   372
+  CStrings:  2311
 
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
- "\t\x14"
- "+[ESUserData _processVocabularyItem:vocabularyWords:]"
- "Error during _EARUserProfile initialization"
- "URLWithString:"
- "Vv56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32q40@?<v@?B@\"NSError\">48"
- "Vv56@0:8@16@24@32q40@?48"
- "containerForPersona:"
- "setProfileConfigWithLanguage:profileDir:userId:dataProtectionClass:completion:"
- "switchToNewAssetsForAssetType:"

```
