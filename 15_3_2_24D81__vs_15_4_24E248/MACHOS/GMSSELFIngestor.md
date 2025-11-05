## GMSSELFIngestor

> `/System/Library/ExtensionKit/Extensions/GMSSELFIngestor.appex/Contents/MacOS/GMSSELFIngestor`

```diff

-3403.9.4.0.0
-  __TEXT.__text: 0xf8fc
-  __TEXT.__auth_stubs: 0x9d0
-  __TEXT.__const: 0x218
-  __TEXT.__cstring: 0xc70
-  __TEXT.__swift5_typeref: 0x1dd
+3404.49.1.0.0
+  __TEXT.__text: 0x11d94
+  __TEXT.__auth_stubs: 0x9c0
+  __TEXT.__const: 0x238
+  __TEXT.__cstring: 0x46a
+  __TEXT.__swift5_typeref: 0x22f
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x178
-  __TEXT.__swift5_reflstr: 0x1d3
-  __TEXT.__swift5_fieldmd: 0x13c
+  __TEXT.__swift5_reflstr: 0x1e3
+  __TEXT.__swift5_fieldmd: 0x148
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__oslogstring: 0x8ea
-  __TEXT.__objc_methname: 0x273
+  __TEXT.__oslogstring: 0xb1a
+  __TEXT.__objc_methname: 0x296
   __TEXT.__swift5_capture: 0x14
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x1c8
+  __TEXT.__swift_as_entry: 0x8
+  __TEXT.__swift_as_ret: 0x4
+  __TEXT.__unwind_info: 0x1c0
   __TEXT.__eh_frame: 0xa8
-  __DATA_CONST.__auth_got: 0x4e8
-  __DATA_CONST.__got: 0x130
-  __DATA_CONST.__auth_ptr: 0x128
-  __DATA_CONST.__const: 0x1f0
+  __DATA_CONST.__auth_got: 0x4e0
+  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__auth_ptr: 0x130
+  __DATA_CONST.__const: 0x260
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x380
-  __DATA.__objc_selrefs: 0x118
+  __DATA.__objc_const: 0x3a0
+  __DATA.__objc_selrefs: 0x138
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x428
+  __DATA.__data: 0x450
   __DATA.__bss: 0x280
   __DATA.__common: 0xa0
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams
   - /System/Library/PrivateFrameworks/CollectionsInternal.framework/Versions/A/CollectionsInternal
   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/Versions/A/IntelligencePlatformLibrary
+  - /System/Library/PrivateFrameworks/LighthouseDataProcessor.framework/Versions/A/LighthouseDataProcessor
   - /System/Library/PrivateFrameworks/SiriAnalytics.framework/Versions/A/SiriAnalytics
   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/Versions/A/SiriInstrumentation
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: C1A69568-EC32-38A2-8F79-337D0973E22B
-  Functions: 118
-  Symbols:   97
-  CStrings:  159
+  UUID: 781B44DA-38EB-3479-A9C7-897398C211B6
+  Functions: 121
+  Symbols:   99
+  CStrings:  130
 
Symbols:
+ __swiftEmptyDictionarySingleton
+ _swift_allocBox
CStrings:
+ "End event modelManagerID %s"
+ "Failed event modelManagerID %s"
+ "Failed to compute latency for request %s"
+ "Failed to create event for request %s"
+ "GMS Error Domain is empty"
+ "GMS Error emitted, domain: %s,code: %s"
+ "GMS events type %s not matching event Filter"
+ "GMS events with modelManagerID %s not found in buffer"
+ "GMSClientRequestIdentifier set to: %s"
+ "GMSSELFIngestor.processEvent() event type: %s modelManagerID %s"
+ "ModelName: %s, modelVersion: %s"
+ "PartnerCloudRequestEvents %s: %s"
+ "PartnerCloudRequestEvents%s was set to nil."
+ "SELF EndEvent: %s"
+ "SELF FailEvent: %s"
+ "Should not log for this useCaseString: %s"
+ "StartEvent: %s"
+ "Unknown or missing useCase for request %s"
+ "UseCaseIdentifier missing for request %s"
+ "Usecase Identifier missing for request %s"
+ "Usecase set to: %d"
+ "com.apple.inferenceRequest.completePromptTemplate.start event modelManagerID %s"
+ "description"
+ "errorCode"
+ "errorDomainString"
+ "eventTypeFilter"
+ "isUserSignedIn"
+ "isUserSignedIn set to: %{bool}d"
+ "modelManagerID %s saved blackpowder.SignedInStatusEvent  %s %s"
+ "modelManagerID %s saved firstTokenEvent"
+ "modelManagerID %s saved modelInfoEvent %s %s"
+ "modelManagerID %s saved webSearchStatusEvent  %s %s"
+ "modelName"
+ "modelVersion"
+ "outputTokens: %lld, outputImages: %lld, timeToFirstToken: %f, timeToLastToken: %f"
+ "setErrorCode:"
+ "setErrorDomainString:"
+ "setImagePerSecond:"
+ "useCase"
- "Client request start event requestIdentifier%s"
- "DiffusionBase.AppleDiffusionPipeline.AppleDiffusionError"
- "EdgeKit.EKTransportMessageConnectionError"
- "End event requestIdentifier%s"
- "Extension.in.EdgeKit.EKStream.EKStreamError"
- "Failed event requestIdentifier%s"
- "Fatal error"
- "Foundation.GenericObjCError"
- "GMS events with requestIdentifier%s not found in buffer"
- "GMSSELFIngestor.processEvent() blackpowderSignedInStatusEvent"
- "GMSSELFIngestor.processEvent() event type: %s"
- "GMSSELFIngestor.processEvent() firstTokenEvent"
- "GMSSELFIngestor.processEvent() modelInfoEvent"
- "GMSSELFIngestor.processEvent() webSearchStatusEvent"
- "Insufficient space allocated to copy string contents"
- "Latency can't be computed for request %s"
- "ModelCatalog.CatalogErrors.AssetErrors"
- "ModelManagerServices.InferenceError"
- "NSCocoaErrorDomain"
- "NSPOSIXErrorDomain"
- "NSURLErrorDomain"
- "Negative error code (%lld) encountered for request %s, defaulting to 0"
- "Negative values encountered for request %s:\noutputTokens: %lld\noutputImages: %lld"
- "Not enough bits to represent the passed value"
- "OnDeviceInferenceAssetRepository"
- "PrivateCloudCompute.TrustedCloudComputeError"
- "Should not log for this useCaseString:%s"
- "Swift.CancellationError"
- "Swift.DecodingError"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "TGIAjaxAuthenticator"
- "TieCloudAppCore.RequestValidator.RequestError"
- "TieCommon.TieXPError"
- "TieInferenceCore.PromptTGPipeline.InternalError"
- "TokenGeneration.TokenGenerationError"
- "TokenGenerationCore"
- "TokenGenerationCore.ModelConfiguration.PromptTemplateError"
- "TokenGenerationInference"
- "TokenGenerationInference.DataSourceError"
- "TokenGenerationInference.TokenGenerationSamplingError"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "VisualGeneration.ImageChecker.Error"
- "XPC.XPCRichError"
- "com.apple.ExtensionKit"
- "com.apple.ModelManagerServices"
- "com.apple.PrivateMLClient"
- "com.apple.PrivateMLClientInferenceProvider"
- "com.apple.TokenGeneration"
- "com.apple.TokenGenerationInference.E5Runner"
- "com.apple.VisualGeneration"
- "com.apple.mm.executeRequest.begin"
- "invalid Collection: less than 'count' elements in collection"
- "setErrorDomain:"
- "setExternalPartner:"
- "setGmsErrorCode:"
- "setIsWebSearchUsed:"
- "setModelLocation:"
- "setModelParty:"

```
