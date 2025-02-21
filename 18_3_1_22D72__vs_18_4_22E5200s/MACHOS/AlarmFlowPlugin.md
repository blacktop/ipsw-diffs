## AlarmFlowPlugin

> `/System/Library/Assistant/FlowDelegatePlugins/AlarmFlowPlugin.bundle/AlarmFlowPlugin`

```diff

-3402.38.1.0.0
-  __TEXT.__text: 0x10a39c
-  __TEXT.__auth_stubs: 0x35e0
-  __TEXT.__objc_methlist: 0x14
-  __TEXT.__const: 0x3874
-  __TEXT.__cstring: 0x2cbd
-  __TEXT.__swift5_typeref: 0x177e
+3404.17.1.0.0
+  __TEXT.__text: 0xf5b08
+  __TEXT.__auth_stubs: 0x3630
+  __TEXT.__objc_methlist: 0x284
+  __TEXT.__const: 0x3504
+  __TEXT.__cstring: 0x299d
+  __TEXT.__swift5_typeref: 0x1796
   __TEXT.__objc_methname: 0x9a3
   __TEXT.__objc_classname: 0xaf
   __TEXT.__objc_methtype: 0x1a8
-  __TEXT.__constg_swiftt: 0x2f88
+  __TEXT.__swift_as_entry: 0x46c
+  __TEXT.__swift_as_ret: 0x670
+  __TEXT.__constg_swiftt: 0x2f80
   __TEXT.__swift5_fieldmd: 0x1944
   __TEXT.__swift5_types: 0x18c
-  __TEXT.__oslogstring: 0x6ec5
+  __TEXT.__oslogstring: 0x6f85
   __TEXT.__swift5_protos: 0x40
   __TEXT.__swift5_proto: 0x1f4
   __TEXT.__swift5_reflstr: 0x1783
   __TEXT.__swift5_assocty: 0x500
   __TEXT.__swift5_capture: 0x114
-  __TEXT.__unwind_info: 0x2da8
-  __TEXT.__eh_frame: 0x9b28
-  __DATA_CONST.__auth_got: 0x1af0
-  __DATA_CONST.__got: 0xa90
-  __DATA_CONST.__auth_ptr: 0xf50
-  __DATA_CONST.__const: 0x1b50
+  __TEXT.__unwind_info: 0x2b50
+  __TEXT.__eh_frame: 0x99e0
+  __DATA_CONST.__auth_got: 0x1b18
+  __DATA_CONST.__got: 0xac8
+  __DATA_CONST.__auth_ptr: 0xf58
+  __DATA_CONST.__const: 0x1bc0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA.__objc_const: 0x21c0
-  __DATA.__objc_selrefs: 0x3b0
+  __DATA.__objc_const: 0x1d68
+  __DATA.__objc_selrefs: 0x4d8
   __DATA.__objc_data: 0xa08
-  __DATA.__data: 0x52d8
+  __DATA.__data: 0x5298
   __DATA.__common: 0x490
   __DATA.__bss: 0x3580
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
+  - /System/Library/PrivateFrameworks/IntelligenceFlow.framework/IntelligenceFlow
   - /System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer
   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects
   - /System/Library/PrivateFrameworks/SiriAppResolution.framework/SiriAppResolution

   - /System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities
   - /System/Library/PrivateFrameworks/SiriVirtualDeviceResolution.framework/SiriVirtualDeviceResolution
   - /System/Library/PrivateFrameworks/SnippetKit.framework/SnippetKit
+  - /System/Library/PrivateFrameworks/ToolKit.framework/ToolKit
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

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
-  Functions: 2639
-  Symbols:   181
-  CStrings:  937
+  Functions: 2444
+  Symbols:   185
+  CStrings:  924
 
Symbols:
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_getExistentialTypeMetadata
+ _swift_initStructMetadataWithLayoutString
+ _swift_projectBox
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_release_x9
- _objc_storeStrong
- _swift_allocateGenericValueMetadata
- _swift_initStaticObject
- _swift_initStructMetadata
CStrings:
+ "Alarm domain unexpected client action toolId: %s"
+ "Alarm domain: received ifClientAction parse."
+ "Handling ifClientAction for intent: %s"
+ "ifClientActionParse time: %s"
- "Division by zero"
- "Division results in an overflow"
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
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
