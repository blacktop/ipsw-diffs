## TimerFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/TimerFlowDelegatePlugin.bundle/TimerFlowDelegatePlugin`

```diff

-3402.38.1.0.0
-  __TEXT.__text: 0x13b1e0
-  __TEXT.__auth_stubs: 0x3f50
-  __TEXT.__const: 0x4ef0
-  __TEXT.__cstring: 0x3eb5
-  __TEXT.__swift5_typeref: 0x1c2e
+3404.17.1.0.0
+  __TEXT.__text: 0x135a94
+  __TEXT.__auth_stubs: 0x3eb0
+  __TEXT.__objc_methlist: 0x26c
+  __TEXT.__const: 0x4af0
+  __TEXT.__cstring: 0x3a15
+  __TEXT.__swift5_typeref: 0x1c04
   __TEXT.__constg_swiftt: 0x3c4c
   __TEXT.__swift5_reflstr: 0x1543
   __TEXT.__swift5_fieldmd: 0x1ab0

   __TEXT.__objc_methname: 0x931
   __TEXT.__objc_methtype: 0x1a8
   __TEXT.__swift5_assocty: 0x698
-  __TEXT.__oslogstring: 0x99b5
+  __TEXT.__oslogstring: 0x9a65
+  __TEXT.__swift_as_entry: 0x5a0
+  __TEXT.__swift_as_ret: 0x96c
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__unwind_info: 0x3d98
-  __TEXT.__eh_frame: 0xd650
-  __DATA_CONST.__auth_got: 0x1fa8
+  __TEXT.__unwind_info: 0x3ad8
+  __TEXT.__eh_frame: 0xd3b8
+  __DATA_CONST.__auth_got: 0x1f58
   __DATA_CONST.__got: 0xbb8
-  __DATA_CONST.__auth_ptr: 0x1030
-  __DATA_CONST.__const: 0x2e50
+  __DATA_CONST.__auth_ptr: 0x1018
+  __DATA_CONST.__const: 0x2e48
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA.__objc_const: 0x23d0
-  __DATA.__objc_selrefs: 0x380
+  __DATA.__objc_const: 0x1f78
+  __DATA.__objc_selrefs: 0x4b0
   __DATA.__objc_data: 0x9b8
-  __DATA.__data: 0x5d20
-  __DATA.__common: 0x4e8
+  __DATA.__data: 0x5cf0
   __DATA.__bss: 0x5810
+  __DATA.__common: 0x4a0
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
+  - /System/Library/PrivateFrameworks/IntelligenceFlow.framework/IntelligenceFlow
   - /System/Library/PrivateFrameworks/MediaServices.framework/MediaServices
   - /System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer
   - /System/Library/PrivateFrameworks/MobileTimerSupport.framework/MobileTimerSupport

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMapKit.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3484
-  Symbols:   205
-  CStrings:  1118
+  Functions: 3243
+  Symbols:   213
+  CStrings:  1099
 
Symbols:
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_generic_instantiateLayoutString
+ _swift_getExistentialTypeMetadata
+ _swift_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_initStructMetadataWithLayoutString
+ _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_multiPayloadEnumGeneric_getEnumTag
- __swift_FORCE_LOAD_$_swiftFileProvider
- _swift_allocateGenericValueMetadata
- _swift_initEnumMetadataMultiPayload
- _swift_initStaticObject
- _swift_initStructMetadata
CStrings:
+ "CreateTimer - unable to parse %s to a UUID"
+ "Handling ifClientAction for intent: %s"
+ "Timer domain Siri X code path hit: received ifClientAction parse."
+ "Timer domain unexpected client action toolId: %s"
- "CreateTimerIntentHandle has label. Adding to param dictionary"
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
- "sirikit.intents.custom.com.apple.siri.SiriTimeInternal.TimerIntentsExtension.CreateTimerIntent"
- "sirikit.intents.custom.com.apple.siri.SiriTimeInternal.TimerIntentsExtension.DismissTimerIntent"
- "sirikit.intents.custom.com.apple.siri.SiriTimeInternal.TimerIntentsExtension.SearchTimerIntent"
- "sirikit.intents.custom.com.apple.siri.SiriTimeInternal.TimerIntentsExtension.SetTimerAttributeIntent"
- "timerAndAlarmAction"

```
