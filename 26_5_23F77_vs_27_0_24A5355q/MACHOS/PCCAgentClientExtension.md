## PCCAgentClientExtension

> `/System/Library/ExtensionKit/Extensions/PCCAgentClientExtension.appex/PCCAgentClientExtension`

```diff

-16.100.10.0.0
-  __TEXT.__text: 0x1de34
-  __TEXT.__auth_stubs: 0xc10
+39.0.0.0.0
+  __TEXT.__text: 0x46bdc
+  __TEXT.__auth_stubs: 0x1cb0
   __TEXT.__objc_stubs: 0x120
-  __TEXT.__const: 0xa62
-  __TEXT.__swift5_typeref: 0x345
-  __TEXT.__swift5_reflstr: 0x17f
+  __TEXT.__const: 0x3c82
+  __TEXT.__constg_swiftt: 0xbb4
+  __TEXT.__swift5_typeref: 0xbb1
+  __TEXT.__swift5_reflstr: 0x8a8
+  __TEXT.__swift5_fieldmd: 0x13d4
+  __TEXT.__cstring: 0xc3e
+  __TEXT.__swift5_proto: 0x340
+  __TEXT.__swift5_types: 0x128
+  __TEXT.__oslogstring: 0x1892
   __TEXT.__swift5_assocty: 0x90
-  __TEXT.__constg_swiftt: 0x3e0
-  __TEXT.__swift5_fieldmd: 0x228
-  __TEXT.__swift5_proto: 0x4c
-  __TEXT.__swift5_types: 0x2c
-  __TEXT.__swift_as_entry: 0xa8
-  __TEXT.__swift_as_ret: 0x80
-  __TEXT.__cstring: 0x371
+  __TEXT.__swift_as_entry: 0xb0
+  __TEXT.__swift_as_ret: 0xb0
+  __TEXT.__swift_as_cont: 0x1a4
   __TEXT.__objc_classname: 0x20d
-  __TEXT.__objc_methname: 0x108
+  __TEXT.__objc_methname: 0x122
   __TEXT.__objc_methtype: 0x1
-  __TEXT.__oslogstring: 0x1132
-  __TEXT.__swift5_capture: 0xd0
+  __TEXT.__swift5_capture: 0x114
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x718
-  __TEXT.__eh_frame: 0x19e0
-  __DATA_CONST.__auth_got: 0x610
-  __DATA_CONST.__got: 0x1a8
-  __DATA_CONST.__auth_ptr: 0x240
-  __DATA_CONST.__const: 0x2a0
+  __TEXT.__unwind_info: 0x10a8
+  __TEXT.__eh_frame: 0x2968
+  __DATA_CONST.__const: 0x2620
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x6c0
+  __DATA_CONST.__auth_got: 0xe60
+  __DATA_CONST.__got: 0x558
+  __DATA_CONST.__auth_ptr: 0x468
+  __DATA.__objc_const: 0x6b8
   __DATA.__objc_selrefs: 0x48
-  __DATA.__objc_data: 0xe8
-  __DATA.__data: 0x9e0
-  __DATA.__bss: 0x880
+  __DATA.__objc_data: 0x138
+  __DATA.__data: 0x12d8
+  __DATA.__bss: 0x6700
   __DATA.__common: 0x18
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppleIntelligenceReporting.framework/AppleIntelligenceReporting
+  - /System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/GenerativeFunctionsInstrumentation
+  - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog
+  - /System/Library/PrivateFrameworks/ModelInterfaces.framework/ModelInterfaces
   - /System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices
   - /System/Library/PrivateFrameworks/PCCAgentClientCommon.framework/PCCAgentClientCommon
   - /System/Library/PrivateFrameworks/PrivateCloudCompute.framework/PrivateCloudCompute

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 62AA69A2-8E59-3BBE-8AE5-1A0B88F9868A
-  Functions: 348
-  Symbols:   115
-  CStrings:  129
+  UUID: 907B2D40-0979-3C7D-8BC7-B8DDDE5CE4D3
+  Functions: 1190
+  Symbols:   139
+  CStrings:  218
 
Symbols:
+ __os_signpost_emit_with_name_impl
+ __swiftEmptySetSingleton
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ _objc_release_x22
+ _objc_retain_x25
+ _objc_retain_x26
+ _swift_arrayInitWithCopy
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain_x19
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x8
- _objc_release_x28
- _objc_release_x9
- _objc_retain_x20
- _objc_retain_x21
CStrings:
+ "%s"
+ "%s connection closure completed. elapsed=%s"
+ "%s request %s, initiating immediate connection closure"
+ "%s:Connection not found, ignoring termination."
+ "' is not supported."
+ ": Unsupported model interface"
+ "ClientExtension response: %s"
+ "Component: %{public, signpost.description=attribute,public}s, Operation: %{public, signpost.description=attribute,public}s, ID: %{public, signpost.description=attribute,public}s, StartTime: %{public, signpost.description=attribute,public}llu, EndTime: %{public, signpost.description=attribute,public}llu"
+ "ConditioningImage"
+ "Connection yielded new response. response=%s"
+ "Created TieServiceRequest with vgGenerateRequest.vgOpaqueRequest, size="
+ "Creating the PrivateCloudCompute.TrustedRequest with workloadType: %s"
+ "Deserialized TieServiceRequest, type=%s"
+ "DirectManipulation"
+ "DrawingConditioner"
+ "Emitted FinalResponse.DebugInfo summary metrics"
+ "Emitted transparency report. requestID=%{public}s promptBytes=%{public}ld responseBytes=%{public}ld"
+ "EndToEndComponentMetrics"
+ "Expected vgGenerateResponse for VGF bundle ID but got: "
+ "Expected vgOpaqueResponse in VisualGenerateResponse but got: "
+ "FinalResponse.InferenceEnvironmentInfo"
+ "FinalResponse.InferenceMetrics"
+ "FinalResponse.PerfMetrics"
+ "FinalResponse.VisualGenerationEnvironmentInfo"
+ "FinalResponse.VisualGenerationMetrics"
+ "Ignoring EmptyResponse for one-shot request"
+ "Ignoring EmptyResponse for streaming request"
+ "Ignoring HeartbeatResponse for one-shot request"
+ "Ignoring HeartbeatResponse for streaming request"
+ "Inner stream completed after %ld responses"
+ "MessageBackground"
+ "MessagesBackground"
+ "Model interface '"
+ "PersonalizationImage"
+ "Received %s in DebugResponse"
+ "Received DebugResponse with no debug info type"
+ "Received FinalResponse, completionReason=%s"
+ "Received VLU response"
+ "Received echoAgent response (VLU/HKSV)"
+ "Received unknown debugInfoType in DebugResponse"
+ "SpatialReframing"
+ "Streaming consumer finished after processing %ld responses"
+ "Transparency input JSON: %{private}s"
+ "Transparency output JSON: %{private}s"
+ "VGF response received, continuing to wait for FinalResponse"
+ "VisualGenerationInference"
+ "activeAdapterIdentifier"
+ "boundingBoxCount"
+ "canPersonalizeFromConditioningImage"
+ "candidateKnowledgeIds"
+ "com.apple.PCCAgentClientExtension"
+ "com.apple.fm.service.hksvprocessing.v1"
+ "com.apple.fm.service.hksvprocessing_pro.v1"
+ "com.apple.fm.service.vlu.v1"
+ "containPreviousProcessing"
+ "convertFromTieServiceResponse - ERROR: Expected vgOpaqueResponse but got: "
+ "convertFromTieServiceResponse - Output: returning raw bytes, "
+ "convertFromTieServiceResponse: ERROR: Expected vgGenerateResponse but got: "
+ "convertFromTieServiceResponse: Found vgGenerateResponse, "
+ "convertFromTieServiceResponse: Processing VGF response, expecting vgGenerateResponse"
+ "convertFromTieServiceResponse: Returning TieServiceResponse as-is (no conversion)"
+ "convertFromTieServiceResponse: Serialized response size=%ld bytes"
+ "convertFromTieServiceResponse: bundleId="
+ "convertFromTieServiceResponse: found modelInterfaceName: %s"
+ "convertToTieServiceRequest: Converting to VisualGenerateRequest with vgOpaqueRequest"
+ "convertToTieServiceRequest: Input bundleId="
+ "convertToTieServiceRequest: Processing native TieServiceRequest (no conversion needed)"
+ "convertToTieServiceRequest: TieServiceRequest created, "
+ "convertToTieServiceRequest: found modelInterfaceName: %s"
+ "debiasingMetadataByteCount"
+ "desiredResolution"
+ "directManipulationOperation"
+ "domainPrediction"
+ "durationTimeScale"
+ "durationTimeValue"
+ "emojiHasBackground"
+ "fragmentSequenceNumber"
+ "generatedImageDimensions"
+ "generationControl"
+ "imageTransformsCount"
+ "imageVariationsCount"
+ "iterator"
+ "layoutConfiguration"
+ "modelPredictions"
+ "performBackgroundRemoval"
+ "performPostProcessingSafetyCheck"
+ "performPreProcessingSafetyCheck"
+ "performSafetyCheck"
+ "previousCaptions"
+ "previousEmbeddings"
+ "representationNumber"
+ "requestStream Error encountered: %@"
+ "requestStream making request"
+ "sessionID"
+ "stream"
+ "structuredLocales"
- "Inner connection stream completed normally after %ld responses"
- "One-shot connection closure completed. elapsed=%s"
- "One-shot request complete, initiating immediate connection closure"
- "Request failed with AppleIntelligenceError: %@"
- "Request failed: %s"
- "Successfully returned the new response. response=%s"
- "TODO(ruibm): ClientDataStream not yet implemented. rdar://155324195"

```
