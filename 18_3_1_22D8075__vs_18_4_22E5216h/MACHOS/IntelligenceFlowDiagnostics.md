## IntelligenceFlowDiagnostics

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/PlugIns/IntelligenceFlowDiagnostics.appex/IntelligenceFlowDiagnostics`

```diff

-137.12.0.0.0
-  __TEXT.__text: 0x76ec
-  __TEXT.__auth_stubs: 0x960
+197.0.6.0.0
+  __TEXT.__text: 0x8e54
+  __TEXT.__auth_stubs: 0xa00
   __TEXT.__objc_methlist: 0x2c
-  __TEXT.__cstring: 0x523
-  __TEXT.__const: 0x330
-  __TEXT.__constg_swiftt: 0x148
-  __TEXT.__swift5_typeref: 0x166
-  __TEXT.__swift5_reflstr: 0x13d
-  __TEXT.__swift5_fieldmd: 0x118
+  __TEXT.__const: 0x3c0
+  __TEXT.__cstring: 0x2c3
+  __TEXT.__swift5_typeref: 0x1b2
+  __TEXT.__constg_swiftt: 0x1ac
+  __TEXT.__swift5_reflstr: 0xd6
+  __TEXT.__swift5_fieldmd: 0x120
   __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x20
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__swift5_protos: 0x4
-  __TEXT.__objc_methname: 0x1ae
-  __TEXT.__swift5_capture: 0x38
-  __TEXT.__oslogstring: 0x322
-  __TEXT.__unwind_info: 0x248
-  __TEXT.__eh_frame: 0x2e0
-  __DATA_CONST.__auth_got: 0x4b0
-  __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__auth_ptr: 0xe0
-  __DATA_CONST.__const: 0x438
+  __TEXT.__objc_methname: 0x203
+  __TEXT.__swift5_protos: 0x8
+  __TEXT.__oslogstring: 0x4a2
+  __TEXT.__swift5_capture: 0x74
+  __TEXT.__unwind_info: 0x2a0
+  __TEXT.__eh_frame: 0x440
+  __DATA_CONST.__auth_got: 0x500
+  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__auth_ptr: 0x120
+  __DATA_CONST.__const: 0x490
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x70
-  __DATA.__objc_selrefs: 0xc0
+  __DATA.__objc_selrefs: 0xf0
   __DATA.__objc_data: 0xc0
-  __DATA.__data: 0x1c0
-  __DATA.__bss: 0x300
+  __DATA.__data: 0x270
+  __DATA.__bss: 0x280
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
+  - /System/Library/PrivateFrameworks/FeatureStore.framework/FeatureStore
   - /System/Library/PrivateFrameworks/IntelligenceFlowContext.framework/IntelligenceFlowContext
   - /System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/IntelligenceFlowPlannerSupport
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
+  - /System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 174
-  Symbols:   115
+  Functions: 185
+  Symbols:   127
   CStrings:  70
 
Symbols:
+ _OBJC_CLASS_$_NSFileHandle
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x22
+ _swift_allocBox
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_projectBox
- __swift_FORCE_LOAD_$_swiftFileProvider
- _swift_initStructMetadata
CStrings:
+ "AutomationJSONAttachment"
+ "BiomeEventAttachment"
+ "Datastream"
+ "Donation"
+ "Error serialising loaded replay record.\nerror=%@"
+ "IntelligenceEngine"
+ "IntelligenceFlow"
+ "IntelligenceFlow.interactionStore.json"
+ "IntelligenceFlow.requests.automation.json"
+ "IntelligenceFlowDiagnostics: AutomationJSONAttachment error: %@"
+ "Interaction"
+ "InteractionStoreAttachment: error during event processing: %@"
+ "InteractionStoreAttachment: failed to fully publish events: %s"
+ "InteractionStoreAttachment: file path: %s"
+ "InteractionStoreAttachment: finished writing to: %s"
+ "TranscriptAttachment: event has no data"
+ "closeAndReturnError:"
+ "data"
+ "fileHandleForWritingToURL:error:"
+ "setLastN:"
- "%s: failed to open stream"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "JSONObjectWithData:options:error:"
- "Sage"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "eventPayload"
- "invalid Collection: less than 'count' elements in collection"

```
