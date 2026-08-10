## com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/XPCServices/com.apple.siri.embeddedspeech.xpc/com.apple.siri.embeddedspeech`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3600.70.32.0.0
-  __TEXT.__text: 0x33468
-  __TEXT.__auth_stubs: 0x960
-  __TEXT.__objc_stubs: 0x83c0
-  __TEXT.__objc_methlist: 0x1cec
+3600.70.47.0.0
+  __TEXT.__text: 0x33cdc
+  __TEXT.__auth_stubs: 0x970
+  __TEXT.__objc_stubs: 0x8500
+  __TEXT.__objc_methlist: 0x1cfc
   __TEXT.__const: 0x100
-  __TEXT.__gcc_except_tab: 0x1b80
-  __TEXT.__cstring: 0x4e02
-  __TEXT.__objc_methname: 0xa51c
-  __TEXT.__oslogstring: 0x4b37
+  __TEXT.__gcc_except_tab: 0x1b84
+  __TEXT.__cstring: 0x4e7f
+  __TEXT.__objc_methname: 0xa6dc
+  __TEXT.__oslogstring: 0x4b76
   __TEXT.__objc_classname: 0x297
-  __TEXT.__objc_methtype: 0x1c0a
-  __TEXT.__unwind_info: 0x790
-  __DATA_CONST.__const: 0xce0
+  __TEXT.__objc_methtype: 0x1c1a
+  __TEXT.__unwind_info: 0x798
+  __DATA_CONST.__const: 0xd00
   __DATA_CONST.__cfstring: 0x2e00
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA_CONST.__objc_intobj: 0xf0
+  __DATA_CONST.__objc_intobj: 0x240
   __DATA_CONST.__objc_floatobj: 0x20
   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x4c0
-  __DATA_CONST.__got: 0x858
+  __DATA_CONST.__auth_got: 0x4c8
+  __DATA_CONST.__got: 0x868
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x3200
-  __DATA.__objc_selrefs: 0x24d8
-  __DATA.__objc_ivar: 0x2f8
+  __DATA.__objc_const: 0x3260
+  __DATA.__objc_selrefs: 0x2528
+  __DATA.__objc_ivar: 0x304
   __DATA.__objc_data: 0x7d0
   __DATA.__data: 0x328
-  __DATA.__bss: 0x148
+  __DATA.__bss: 0x158
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 609
-  Symbols:   425
-  CStrings:  2550
+  Functions: 611
+  Symbols:   428
+  CStrings:  2564
 
Symbols:
+ _OBJC_CLASS_$_CCASRRankedEntityTermMetaContent
+ _OBJC_CLASS_$_CCItemInstance
+ ___udivti3
CStrings:
+ "%s No Cascade field type mapping for contact component key: %@"
+ "+[ESContactItemProcessor recordEnrolledContactEntitiesInMetrics:firstPartyContacts:thirdPartyContacts:groupNames:]"
+ "-[ESSpeechProfileBuilderConnection beginWithCategoriesAndVersions:trigger:completion:]"
+ "@84@0:8@16@24B32@36@44@52@60@68@76"
+ "S"
+ "Vv40@0:8@\"NSDictionary\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
+ "_speechProfileMetrics"
+ "addEnrolledEntitiesCount:forCascadeFieldType:"
+ "addEnrolledEntityForCascadeFieldType:"
+ "beginWithCategoriesAndVersions:trigger:completion:"
+ "initWithEntityCleanupConfig:entityCleanupHandler:speechProfileMetrics:"
+ "initWithEntityCleanupHandler:entityCleanupConfig:speechProfileMetrics:"
+ "initWithEntityCleanupHandler:entityExtractionHandler:enableDatatypeCleanupFromNonAppEntities:appEntityConfig:extractedEntityBudget:entitiesExtractedPerCategory:applicableSpeechCategories:entityCleanupConfig:speechProfileMetrics:"
+ "interactionOnlyRanking"
+ "logASRSpeechProfileUpdateStartedWithTrigger:"
+ "metaContent"
+ "numEnrolledEntitiesPerCascadeFieldType"
+ "rank"
+ "recordEnrolledContactEntitiesInMetrics:firstPartyContacts:thirdPartyContacts:groupNames:"
+ "setSpeechProfileSize:"
+ "unsignedShortValue"
- "-[ESSpeechProfileBuilderConnection beginWithCategoriesAndVersions:completion:]"
- "@76@0:8@16@24B32@36@44@52@60@68"
- "Vv32@0:8@\"NSDictionary\"16@?<v@?B@\"NSError\">24"
- "beginWithCategoriesAndVersions:completion:"
- "initWithEntityCleanupConfig:entityCleanupHandler:"
- "initWithEntityCleanupHandler:entityExtractionHandler:enableDatatypeCleanupFromNonAppEntities:appEntityConfig:extractedEntityBudget:entitiesExtractedPerCategory:applicableSpeechCategories:entityCleanupConfig:"
- "logASRSpeechProfileUpdateStarted"
```
