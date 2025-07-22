## com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/XPCServices/com.apple.siri.embeddedspeech.xpc/com.apple.siri.embeddedspeech`

```diff

-3500.110.4.0.0
-  __TEXT.__text: 0x2f1a4
-  __TEXT.__auth_stubs: 0x920
-  __TEXT.__objc_stubs: 0x7a20
-  __TEXT.__objc_methlist: 0x1a04
+3500.115.2.0.0
+  __TEXT.__text: 0x2fc00
+  __TEXT.__auth_stubs: 0x940
+  __TEXT.__objc_stubs: 0x7d80
+  __TEXT.__objc_methlist: 0x1a44
   __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x1b4c
-  __TEXT.__cstring: 0x42b4
-  __TEXT.__objc_methname: 0x971f
-  __TEXT.__oslogstring: 0x45c4
+  __TEXT.__gcc_except_tab: 0x1c70
+  __TEXT.__cstring: 0x4328
+  __TEXT.__objc_methname: 0x9a85
+  __TEXT.__oslogstring: 0x476a
   __TEXT.__objc_classname: 0x201
-  __TEXT.__objc_methtype: 0x1979
+  __TEXT.__objc_methtype: 0x19bf
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x6c8
-  __DATA_CONST.__auth_got: 0x4a0
-  __DATA_CONST.__got: 0x6c0
+  __TEXT.__unwind_info: 0x6e8
+  __DATA_CONST.__auth_got: 0x4b0
+  __DATA_CONST.__got: 0x6d0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xb70
+  __DATA_CONST.__const: 0xb80
   __DATA_CONST.__cfstring: 0x2c80
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2840
-  __DATA.__objc_selrefs: 0x2248
-  __DATA.__objc_ivar: 0x270
+  __DATA.__objc_const: 0x2890
+  __DATA.__objc_selrefs: 0x2320
+  __DATA.__objc_ivar: 0x278
   __DATA.__objc_data: 0x550
   __DATA.__data: 0x268
   __DATA.__bss: 0x140

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 32BE2924-9241-3A60-8598-9F4472B883D1
-  Functions: 549
-  Symbols:   377
-  CStrings:  2730
+  UUID: DC49CEF6-BC6D-3617-8AB5-33DA18EED191
+  Functions: 556
+  Symbols:   381
+  CStrings:  2768
 
Symbols:
+ _OBJC_CLASS_$_CESRSpeechProfileMetrics
+ _OBJC_CLASS_$_CESRSpeechProfileSelfHelper
+ _objc_release_x2
+ _objc_retain_x9
CStrings:
+ "\n&"
+ "%s %@ cancelling instance %@; Connection interrupted."
+ "%s %@ cancelling instance %@; Connection invalidated."
+ "%s Entity Cleanup: %@ at least one emoji."
+ "%s Entity Cleanup: %@ at least one special character."
+ "%s Entity Cleanup: Cleanup %@ enabled."
+ "%s Entity Cleanup: Cleanup Ingestion %@ enabled."
+ "%s Entity Cleanup: Failed applying regex: %@"
+ "%s Entity Cleanup: Failed to initialize NSDataDetector for NSTextCheckingTypes-based entity sanitization, skipping enrolling entities of impacted types."
+ "%s Entity Extraction: %@ at least one extracted entity."
+ "%s Entity Extraction: Entity Extraction Limit is %ld"
+ "%s Entity Extraction: Extracted entity equals original string. Skipping."
+ "%s Entity Extraction: Extraction %@ enabled."
+ "%s Entity Extraction: Extraction Ingestion %@ enabled."
+ "%s Entity Extraction: Failed to add extracted entity (type: %@) to vocabulary."
+ "%s Entity Extraction: No mapping found for extracted entity with tagName %@. Skipping."
+ "%s Entity Extraction: No mapping found for extracted entity with tagName: %@. Using default mapping."
+ "%s Speech profile for %{public}@ updated successfully. Wrote %lu bytes to %{private}@"
+ "-[ESUserData logEntityCleanupConfig]"
+ "-[ESUserData logEntityExtractionConfig]"
+ "@\"CESRSpeechProfileMetrics\""
+ "@\"CESRSpeechProfileSelfHelper\""
+ "Q24@0:8@16"
+ "T@\"CESRSpeechProfileMetrics\",R,C,N,V_metrics"
+ "_metrics"
+ "_totalContactComponentsInSet:"
+ "isCleanupIngestionEnabled"
+ "isExtractionIngestionEnabled"
+ "isExtractionSetupSuccessful"
+ "logASRSpeechProfileUpdateEndedWithUserDataMetrics:"
+ "logASRSpeechProfileUpdateFailedWithReason:"
+ "logASRSpeechProfileUpdateStarted"
+ "logEntityCleanupConfig"
+ "logEntityExtractionConfig"
+ "numComponents"
+ "numEntitiesCleaned"
+ "numEntitiesContainingEmoji"
+ "numEntitiesContainingExtractions"
+ "numEntitiesContainingSpecialCharacters"
+ "numEntitiesExtracted"
+ "numEntitiesExtractionAttempted"
+ "setIsCleanupIngestionEnabled:"
+ "setIsExtractionIngestionEnabled:"
+ "setIsExtractionSetupSuccessful:"
+ "setNumEntitiesCleaned:"
+ "setNumEntitiesContainingEmoji:"
+ "setNumEntitiesContainingExtractions:"
+ "setNumEntitiesContainingSpecialCharacters:"
+ "setNumEntitiesExtracted:"
+ "setNumEntitiesExtractionAttempted:"
+ "setTotalNumEntitiesReceived:"
+ "totalNumEntitiesReceived"
+ "v32@?0@\"ESUserDataContactWord\"8Q16^B24"
- "\n%"
- "%s %@ at least one emoji."
- "%s %@ at least one extracted entity."
- "%s %@ at least one special character."
- "%s %@ cancelling instance %@"
- "%s Cleanup %@ enabled."
- "%s Entity Extraction Limit: %ld"
- "%s Extracted entity equals original string. Skipping."
- "%s Extraction %@ enabled."
- "%s Failed applying regex: %@"
- "%s Failed to add extracted entity (type: %@) to vocabulary."
- "%s Failed to initialize NSDataDetector for NSTextCheckingTypes-based entity sanitization, skipping enrolling entities of impacted types."
- "%s No mapping found for extracted entity with tagName %@. Skipping."
- "%s No mapping found for extracted entity with tagName: %@. Using default mapping."
- "%s Speech profile updated successfully. Wrote %lu bytes to %@"

```
