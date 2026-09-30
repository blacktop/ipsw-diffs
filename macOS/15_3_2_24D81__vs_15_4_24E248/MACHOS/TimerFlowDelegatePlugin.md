## TimerFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/TimerFlowDelegatePlugin.bundle/Contents/MacOS/TimerFlowDelegatePlugin`

```diff

-3402.38.1.0.0
-  __TEXT.__text: 0x13683c
-  __TEXT.__auth_stubs: 0x3c80
-  __TEXT.__const: 0x4eb0
-  __TEXT.__cstring: 0x3cc5
-  __TEXT.__swift5_typeref: 0x1bfa
-  __TEXT.__constg_swiftt: 0x3c24
-  __TEXT.__swift5_reflstr: 0x14d3
-  __TEXT.__swift5_fieldmd: 0x1a64
+3404.19.1.0.0
+  __TEXT.__text: 0x164040
+  __TEXT.__auth_stubs: 0x3d30
+  __TEXT.__objc_methlist: 0x26c
+  __TEXT.__const: 0x4a30
+  __TEXT.__cstring: 0x3a15
+  __TEXT.__swift5_typeref: 0x1c04
+  __TEXT.__constg_swiftt: 0x3c8c
+  __TEXT.__swift5_reflstr: 0x1543
+  __TEXT.__swift5_fieldmd: 0x1ab0
   __TEXT.__swift5_capture: 0x1ec
   __TEXT.__swift5_proto: 0x308
-  __TEXT.__swift5_types: 0x1f4
+  __TEXT.__swift5_types: 0x1f8
   __TEXT.__objc_classname: 0xaf
   __TEXT.__objc_methname: 0x913
   __TEXT.__objc_methtype: 0x1a8
   __TEXT.__swift5_assocty: 0x698
-  __TEXT.__oslogstring: 0x9925
+  __TEXT.__oslogstring: 0x9a65
+  __TEXT.__swift_as_entry: 0x5a0
+  __TEXT.__swift_as_ret: 0x96c
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__unwind_info: 0x3cc8
-  __TEXT.__eh_frame: 0xd258
-  __DATA_CONST.__auth_got: 0x1e40
-  __DATA_CONST.__got: 0xb50
-  __DATA_CONST.__auth_ptr: 0x1020
+  __TEXT.__unwind_info: 0x3d58
+  __TEXT.__eh_frame: 0xd920
+  __DATA_CONST.__auth_got: 0x1e98
+  __DATA_CONST.__got: 0xb88
+  __DATA_CONST.__auth_ptr: 0x1030
   __DATA_CONST.__const: 0x2e38
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA.__objc_const: 0x23d0
-  __DATA.__objc_selrefs: 0x378
+  __DATA.__objc_const: 0x1f78
+  __DATA.__objc_selrefs: 0x4a8
   __DATA.__objc_data: 0x9b8
-  __DATA.__data: 0x5be8
-  __DATA.__common: 0x4e0
+  __DATA.__data: 0x5c90
   __DATA.__bss: 0x5810
+  __DATA.__common: 0x4a0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Intents.framework/Versions/A/Intents
   - /System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/AssistantServices
+  - /System/Library/PrivateFrameworks/IntelligenceFlow.framework/Versions/A/IntelligenceFlow
   - /System/Library/PrivateFrameworks/MediaServices.framework/Versions/A/MediaServices
   - /System/Library/PrivateFrameworks/MobileTimer.framework/Versions/A/MobileTimer
   - /System/Library/PrivateFrameworks/SAObjects.framework/Versions/A/SAObjects

   - /System/Library/PrivateFrameworks/SiriNaturalLanguageGeneration.framework/Versions/A/SiriNaturalLanguageGeneration
   - /System/Library/PrivateFrameworks/SiriOntology.framework/Versions/A/SiriOntology
   - /System/Library/PrivateFrameworks/SiriReferenceResolutionDataModel.framework/Versions/A/SiriReferenceResolutionDataModel
+  - /System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/Versions/A/SiriSuggestionsAPI
+  - /System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/Versions/A/SiriSuggestionsKit
   - /System/Library/PrivateFrameworks/SiriTasks.framework/Versions/A/SiriTasks
   - /System/Library/PrivateFrameworks/SiriTimeInternal.framework/Versions/A/SiriTimeInternal
   - /System/Library/PrivateFrameworks/SiriTimeTimerInternal.framework/Versions/A/SiriTimeTimerInternal

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMapKit.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 4EA8E0CC-5CC2-3487-A6FB-B8E06DBDC601
-  Functions: 3416
-  Symbols:   176
-  CStrings:  1108
+  UUID: 4D689B53-6402-3A4C-ABB9-153555B9B5EE
+  Functions: 3412
+  Symbols:   178
+  CStrings:  1098
 
Symbols:
+ _AFDeviceSupportsEchoCancellation
+ _OBJC_CLASS_$_AFClockTimer
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ _swift_getErrorValue
- __swift_FORCE_LOAD_$_swiftFileProvider
- _swift_initStaticObject
CStrings:
+ "CreateTimer - unable to parse %s to a UUID"
+ "Handling ifClientAction for intent: %s"
+ "SuggestionsProvider.submitIntentToSiriSuggestions caught error: %s"
+ "Timer domain Siri X code path hit: received ifClientAction parse."
+ "Timer domain unexpected client action toolId: %s"
+ "compactVoiceTriggerEnabled"
+ "supportsEchoCancellation"
- "Division by zero"
- "Division results in an overflow"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
