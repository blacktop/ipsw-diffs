## TextUnderstanding

> `/System/Library/PrivateFrameworks/TextUnderstanding.framework/TextUnderstanding`

```diff

-192.0.0.0.0
-  __TEXT.__text: 0x12b590
-  __TEXT.__objc_methlist: 0x20
-  __TEXT.__const: 0x28528
-  __TEXT.__swift5_typeref: 0x74ff
-  __TEXT.__cstring: 0x2d78
-  __TEXT.__constg_swiftt: 0x5c34
-  __TEXT.__swift5_reflstr: 0x3c90
-  __TEXT.__swift5_fieldmd: 0x8484
-  __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_proto: 0x27a0
-  __TEXT.__swift5_types: 0xa64
-  __TEXT.__swift5_mpenum: 0x130
-  __TEXT.__swift5_assocty: 0x3d8
-  __TEXT.__oslogstring: 0xce5
+195.2.0.0.0
+  __TEXT.__text: 0x1581c0
+  __TEXT.__objc_methlist: 0x2c
+  __TEXT.__const: 0x2e108
+  __TEXT.__swift5_typeref: 0x84f1
+  __TEXT.__cstring: 0x32dc
+  __TEXT.__constg_swiftt: 0x6920
+  __TEXT.__swift5_reflstr: 0x42e0
+  __TEXT.__swift5_fieldmd: 0x9604
+  __TEXT.__swift5_builtin: 0xc8
+  __TEXT.__swift5_proto: 0x2db0
+  __TEXT.__swift5_types: 0xbe8
+  __TEXT.__swift5_mpenum: 0x128
+  __TEXT.__swift5_assocty: 0x438
+  __TEXT.__oslogstring: 0x11b5
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__swift5_capture: 0x280
-  __TEXT.__swift_as_entry: 0xc
-  __TEXT.__swift_as_ret: 0x8
-  __TEXT.__swift_as_cont: 0x1c
-  __TEXT.__unwind_info: 0x9a50
-  __TEXT.__eh_frame: 0x6130
+  __TEXT.__swift_as_entry: 0x18
+  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__swift_as_cont: 0x40
+  __TEXT.__swift5_capture: 0x290
+  __TEXT.__unwind_info: 0xb100
+  __TEXT.__eh_frame: 0x74c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x260
+  __DATA_CONST.__objc_selrefs: 0x268
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xfba8
-  __AUTH_CONST.__objc_const: 0x7b0
-  __AUTH_CONST.__auth_got: 0xc18
-  __AUTH.__data: 0x80
-  __DATA.__data: 0x4008
-  __DATA_DIRTY.__data: 0x4fb8
-  __DATA_DIRTY.__bss: 0x19a00
+  __AUTH_CONST.__const: 0x12260
+  __AUTH_CONST.__objc_const: 0x7b8
+  __AUTH_CONST.__auth_got: 0xd40
+  __AUTH.__data: 0x298
+  __DATA.__data: 0x4ed0
+  __DATA_DIRTY.__data: 0x53e0
+  __DATA_DIRTY.__bss: 0x1a980
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13159
-  Symbols:   169
-  CStrings:  402
+  Functions: 15137
+  Symbols:   172
+  CStrings:  459
 
Symbols:
+ __os_signpost_emit_with_name_impl
+ _swift_allocBox
+ _swift_release_x9
CStrings:
+ "<Document.Kind compactedConversations>"
+ "<Document.Kind conversation>"
+ "<Request.Kind compaction>"
+ "<Request.Kind smartResponses>"
+ "<Request.Kind summary>"
+ "<Request.Kind topics>"
+ "ExclaveKit compaction failed"
+ "ExclaveKitService.process()"
+ "ExclaveKitService: Conclave.service failed: %@"
+ "ExclaveKitService: Conclave.service for speakerIdentificationClient failed: %@"
+ "ExclaveKitService: Conclave.service for transcriptionClient failed: %@"
+ "ExclaveKitService: failed to decode compaction text for audio segment %s"
+ "ExclaveKitService: missing compaction in result for audio segment %s"
+ "ExclaveKitService: process called for audio segment %s"
+ "ExclaveKitService: process completed for audio segment %s with compaction text length %{private}ld, safetyError %s"
+ "ExclaveKitService: reset called for audio segment %s"
+ "ExclaveKitService: sanitizeCompaction failed: %@"
+ "ExclaveKitService: starting conclave..."
+ "ExclaveKitService: successfully created Tightbeam client"
+ "ExclaveKitService: tightbeamClient.process failed for audio segment %s: %@"
+ "ExclaveKitService: tightbeamClient.process returned for audio segment %s"
+ "ExclaveKitService: tightbeamClient.reset failed: %@"
+ "Invalid key value while decoding result type for handleSpeakerIdentificationSnippet"
+ "Invalid key value while decoding result type for handleTranscriptionSnippet"
+ "Invalid key value while decoding result type for initialize"
+ "Invalid key value while decoding result type for process"
+ "Invalid key value while decoding result type for reset"
+ "TextProcessingService: sanitizeCompaction called"
+ "TextProcessingService: sanitizeCompaction failed with unknown error: %@"
+ "TextProcessingService: sanitizeCompaction failed: %@"
+ "[Error] Interval already ended"
+ "acousticConditions"
+ "activeSessionTypes"
+ "administrativeArea"
+ "audioSegmentDuration"
+ "call"
+ "com.apple.textunderstanding.service"
+ "compacted conversations"
+ "compactedConversations"
+ "disallowedTopics"
+ "failedCompactionRatioCheck"
+ "financial"
+ "inferredLocation"
+ "inputTranscriptCharacterCount"
+ "invalid rawValue for ErrorTB: "
+ "legal"
+ "medical"
+ "noneCharacterCount"
+ "nowPlaying"
+ "otherCharacterCount"
+ "outputDeviceType"
+ "pointOfInterestCategory"
+ "previousTopicEnd"
+ "previousTopicStart"
+ "speakerBreakdown"
+ "speakerIdentificationSnippets"
+ "transcriptionSnippets"
+ "wearerCharacterCount"
+ "workout"
- "com.apple.textComposition.OpenEndedExtract.SPI"
- "schemaName"
```
