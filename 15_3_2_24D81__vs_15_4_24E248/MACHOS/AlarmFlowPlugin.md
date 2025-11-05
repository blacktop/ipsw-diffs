## AlarmFlowPlugin

> `/System/Library/Assistant/FlowDelegatePlugins/AlarmFlowPlugin.bundle/Contents/MacOS/AlarmFlowPlugin`

```diff

-3402.38.1.0.0
-  __TEXT.__text: 0x10c4a8
-  __TEXT.__auth_stubs: 0x3450
-  __TEXT.__objc_methlist: 0x14
-  __TEXT.__const: 0x3874
-  __TEXT.__cstring: 0x2d9d
-  __TEXT.__swift5_typeref: 0x177e
+3404.19.1.0.0
+  __TEXT.__text: 0x11fa2c
+  __TEXT.__auth_stubs: 0x34a0
+  __TEXT.__objc_methlist: 0x284
+  __TEXT.__const: 0x35b4
+  __TEXT.__cstring: 0x2a6d
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
-  __TEXT.__unwind_info: 0x2d80
-  __TEXT.__eh_frame: 0x9b28
-  __DATA_CONST.__auth_got: 0x1a28
-  __DATA_CONST.__got: 0xa90
-  __DATA_CONST.__auth_ptr: 0xef8
-  __DATA_CONST.__const: 0x1b38
+  __TEXT.__unwind_info: 0x2d70
+  __TEXT.__eh_frame: 0x9d18
+  __DATA_CONST.__auth_got: 0x1a50
+  __DATA_CONST.__got: 0xaa0
+  __DATA_CONST.__auth_ptr: 0xf60
+  __DATA_CONST.__const: 0x1bb0
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
+  __DATA.__data: 0x5258
   __DATA.__common: 0x490
   __DATA.__bss: 0x3580
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Intents.framework/Versions/A/Intents
   - /System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/AssistantServices
+  - /System/Library/PrivateFrameworks/IntelligenceFlow.framework/Versions/A/IntelligenceFlow
   - /System/Library/PrivateFrameworks/MobileTimer.framework/Versions/A/MobileTimer
   - /System/Library/PrivateFrameworks/SAObjects.framework/Versions/A/SAObjects
   - /System/Library/PrivateFrameworks/SiriAppResolution.framework/Versions/A/SiriAppResolution

   - /System/Library/PrivateFrameworks/SiriUtilities.framework/Versions/A/SiriUtilities
   - /System/Library/PrivateFrameworks/SiriVirtualDeviceResolution.framework/Versions/A/SiriVirtualDeviceResolution
   - /System/Library/PrivateFrameworks/SnippetKit.framework/Versions/A/SnippetKit
+  - /System/Library/PrivateFrameworks/ToolKit.framework/Versions/A/ToolKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

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
-  UUID: 3B7B77C3-B107-3058-B704-941B2C9B374D
-  Functions: 2639
-  Symbols:   153
-  CStrings:  937
+  UUID: A530C8D7-4956-3D44-A368-E50DEBCB2165
+  Functions: 2626
+  Symbols:   152
+  CStrings:  924
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ _swift_projectBox
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_storeStrong
- _swift_initStaticObject
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SiriTime/AlarmFlowPlugin/Flows/ChangeAlarmStatusFlow/ChangeAlarmStatus+HandledIntentStrategy.swift"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SiriTime/AlarmFlowPlugin/Flows/CustomFlows/UndoCreateAlarmFlow.swift"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SiriTime/AlarmFlowPlugin/Flows/UpdateAlarmFlow/UpdateAlarm+HandledIntentStrategy.swift"
+ "Alarm domain unexpected client action toolId: %s"
+ "Alarm domain: received ifClientAction parse."
+ "Handling ifClientAction for intent: %s"
+ "ifClientActionParse time: %s"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SiriTime/AlarmFlowPlugin/Flows/ChangeAlarmStatusFlow/ChangeAlarmStatus+HandledIntentStrategy.swift"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SiriTime/AlarmFlowPlugin/Flows/CustomFlows/UndoCreateAlarmFlow.swift"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SiriTime/AlarmFlowPlugin/Flows/UpdateAlarmFlow/UpdateAlarm+HandledIntentStrategy.swift"
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
