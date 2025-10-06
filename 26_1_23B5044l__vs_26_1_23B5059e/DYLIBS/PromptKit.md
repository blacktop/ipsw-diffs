## PromptKit

> `/System/Library/PrivateFrameworks/PromptKit.framework/PromptKit`

```diff

-209.12.0.0.0
-  __TEXT.__text: 0xc8b44
-  __TEXT.__auth_stubs: 0x12d0
-  __TEXT.__const: 0x16a04
-  __TEXT.__swift5_typeref: 0x406b
-  __TEXT.__cstring: 0x1f02
-  __TEXT.__swift5_reflstr: 0x1643
-  __TEXT.__swift5_assocty: 0x588
-  __TEXT.__constg_swiftt: 0x2f20
-  __TEXT.__swift5_fieldmd: 0x3998
-  __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_capture: 0x64
+209.18.2.0.0
+  __TEXT.__text: 0xe7c48
+  __TEXT.__auth_stubs: 0x1440
+  __TEXT.__const: 0x193b4
+  __TEXT.__swift5_typeref: 0x4617
+  __TEXT.__cstring: 0x2412
+  __TEXT.__swift5_reflstr: 0x1b43
+  __TEXT.__swift5_assocty: 0x708
+  __TEXT.__constg_swiftt: 0x33fc
+  __TEXT.__swift5_fieldmd: 0x4310
+  __TEXT.__swift5_builtin: 0x64
+  __TEXT.__swift5_capture: 0xa8
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__swift5_proto: 0x169c
-  __TEXT.__swift5_types: 0x4ec
-  __TEXT.__swift_as_entry: 0x24
-  __TEXT.__swift_as_ret: 0x14
-  __TEXT.__swift5_mpenum: 0x30
-  __TEXT.__unwind_info: 0x46b0
-  __TEXT.__eh_frame: 0x7ee0
+  __TEXT.__swift5_proto: 0x18d8
+  __TEXT.__swift5_types: 0x57c
+  __TEXT.__swift_as_entry: 0x38
+  __TEXT.__swift_as_ret: 0x28
+  __TEXT.__swift5_mpenum: 0x38
+  __TEXT.__oslogstring: 0x2a9
+  __TEXT.__unwind_info: 0x50e8
+  __TEXT.__eh_frame: 0x9258
   __TEXT.__objc_methname: 0xe6
-  __DATA_CONST.__got: 0x340
-  __DATA_CONST.__const: 0x98
+  __DATA_CONST.__got: 0x3a0
+  __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x968
-  __AUTH_CONST.__const: 0x5d68
-  __AUTH.__data: 0x4b18
-  __DATA.__data: 0x3bc8
-  __DATA.__bss: 0x25580
-  __DATA.__common: 0xa10
-  __DATA_DIRTY.__data: 0xb60
-  __DATA_DIRTY.__bss: 0x4a80
+  __AUTH_CONST.__auth_got: 0xa20
+  __AUTH_CONST.__const: 0x6748
+  __AUTH.__data: 0x5030
+  __DATA.__data: 0x3bf8
+  __DATA.__bss: 0x26570
+  __DATA.__common: 0xb78
+  __DATA_DIRTY.__data: 0x1808
+  __DATA_DIRTY.__bss: 0x7480
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
-  UUID: A8EAE1F2-9568-38B2-A1BF-EC5C5A509785
-  Functions: 7385
-  Symbols:   116
-  CStrings:  308
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 75BDCB0A-B71E-3A4D-938F-A67A047162EB
+  Functions: 8396
+  Symbols:   126
+  CStrings:  354
 
Symbols:
+ __os_log_impl
+ __swift_FORCE_LOAD_$_swiftos
+ _objc_release_x22
+ _objc_release_x28
+ _objc_retain_x20
+ _objc_retain_x22
+ _os_log_type_enabled
+ _swift_getObjectType
+ _swift_getTupleTypeMetadata2
+ _swift_slowDealloc
+ _swift_willThrowTypedImpl
- _objc_release_x27
CStrings:
+ "InferenceResponse"
+ "Received a file segment with index %ld, but there is already a segment for that index. This indicates a bug in the inference provider."
+ "Received an annotation for segment %ld, but that segment was not a text segment! This indicates a bug in the inference provider."
+ "Received an audio segment with index %ld, but there is already a segment for that index. This indicates a bug in the inference provider."
+ "Received an image segment with index %ld, but there is already a segment for that index. This indicates a bug in the inference provider."
+ "Segment %ld should have been a text segment, but wasn't! This indicates a bug in the inference provider."
+ "annotation"
+ "arguments_delta"
+ "candidate_annotation"
+ "candidate_audio"
+ "candidate_file"
+ "candidate_finish"
+ "candidate_identifier"
+ "candidate_image"
+ "candidate_moderation"
+ "candidate_text_delta"
+ "candidate_tool_call_delta"
+ "com.apple.GenerativeModels"
+ "finish_reason"
+ "function_name"
+ "metadata"
+ "metadata_data"
+ "model_information"
+ "output"
+ "prompt_moderation"
+ "promptkit.wireformat.CandidateAnnotationEvent"
+ "promptkit.wireformat.CandidateAudioEvent"
+ "promptkit.wireformat.CandidateFileEvent"
+ "promptkit.wireformat.CandidateFinishEvent"
+ "promptkit.wireformat.CandidateImageEvent"
+ "promptkit.wireformat.CandidateModerationEvent"
+ "promptkit.wireformat.CandidateTextDeltaEvent"
+ "promptkit.wireformat.CandidateToolCallDeltaEvent"
+ "promptkit.wireformat.InferenceResponseEvent"
+ "promptkit.wireformat.MetadataEvent"
+ "promptkit.wireformat.ModelInformationEvent"
+ "promptkit.wireformat.PromptModerationEvent"
+ "promptkit.wireformat.RenderedPromptEvent"
+ "promptkit.wireformat.UsageEvent"
+ "rendered_prompt"
+ "response_identifier"
+ "segment_index"
+ "text_delta"
+ "tool_call_identifier"
+ "user_info"
+ "value annotations "

```
