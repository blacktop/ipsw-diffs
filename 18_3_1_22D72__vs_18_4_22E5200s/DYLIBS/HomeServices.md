## HomeServices

> `/System/Library/PrivateFrameworks/HomeServices.framework/HomeServices`

```diff

-254.4.1.0.0
-  __TEXT.__text: 0x43a6c
-  __TEXT.__auth_stubs: 0x18b0
-  __TEXT.__objc_methlist: 0x4c
-  __TEXT.__const: 0x2548
-  __TEXT.__cstring: 0x17a7
-  __TEXT.__constg_swiftt: 0x864
-  __TEXT.__swift5_typeref: 0x889
-  __TEXT.__swift5_fieldmd: 0xa8c
-  __TEXT.__swift5_types: 0xc8
-  __TEXT.__oslogstring: 0x1ac1
-  __TEXT.__swift5_proto: 0x1f4
-  __TEXT.__swift5_reflstr: 0x779
-  __TEXT.__swift5_protos: 0x4
+286.0.0.0.0
+  __TEXT.__text: 0x36f3c
+  __TEXT.__auth_stubs: 0x17a0
+  __TEXT.__objc_methlist: 0x154
+  __TEXT.__const: 0x2458
+  __TEXT.__cstring: 0x13e7
+  __TEXT.__constg_swiftt: 0x7e0
+  __TEXT.__swift5_typeref: 0x849
+  __TEXT.__swift5_fieldmd: 0x9bc
+  __TEXT.__swift5_types: 0xb4
+  __TEXT.__swift5_reflstr: 0x746
   __TEXT.__swift5_assocty: 0x1c8
+  __TEXT.__swift5_proto: 0x1f4
+  __TEXT.__swift_as_entry: 0x30
+  __TEXT.__swift_as_ret: 0x38
+  __TEXT.__oslogstring: 0x1a41
+  __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0xda8
-  __TEXT.__eh_frame: 0x1250
+  __TEXT.__unwind_info: 0xba0
+  __TEXT.__eh_frame: 0x11f8
   __TEXT.__objc_classname: 0x19
   __TEXT.__objc_methname: 0x6dc
   __TEXT.__objc_methtype: 0xad
-  __DATA_CONST.__got: 0x400
+  __DATA_CONST.__got: 0x3e0
   __DATA_CONST.__const: 0xd8
-  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x220
+  __DATA_CONST.__objc_selrefs: 0x2b8
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0xc58
-  __AUTH_CONST.__auth_ptr: 0x428
-  __AUTH_CONST.__const: 0x18d8
-  __AUTH_CONST.__objc_const: 0xc30
+  __AUTH_CONST.__auth_got: 0xbd0
+  __AUTH_CONST.__auth_ptr: 0x408
+  __AUTH_CONST.__const: 0x1620
+  __AUTH_CONST.__objc_const: 0x9b0
   __AUTH.__objc_data: 0xa0
-  __AUTH.__data: 0x720
-  __DATA.__data: 0x7b0
-  __DATA.__common: 0x1b0
+  __AUTH.__data: 0x550
+  __DATA.__data: 0x720
   __DATA.__bss: 0x3320
-  __DATA_DIRTY.__data: 0x718
+  __DATA.__common: 0x160
+  __DATA_DIRTY.__data: 0x740
   __DATA_DIRTY.__bss: 0xa00
-  __DATA_DIRTY.__common: 0xa8
+  __DATA_DIRTY.__common: 0xb0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1116
-  Symbols:   204
-  CStrings:  395
+  Functions: 958
+  Symbols:   210
+  CStrings:  365
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression
+ _objc_retain_x22
+ _objc_retain_x25
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_initStructMetadataWithLayoutString
+ _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_multiPayloadEnumGeneric_getEnumTag
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_retain_x26
- _objc_retain_x28
- _swift_initEnumMetadataMultiPayload
- _swift_initStaticObject
- _swift_initStructMetadata
- _swift_willThrowTypedImpl
CStrings:
+ "Invalid ISO 8601 duration string: "
+ "com.apple.wpc.energyservices.gridservices"
+ "{\n    \"serverUrl\": \"https://www.apple.com/v1/\",\n    \"energyServices\": {\n        \"configuration\": {\n            \"energyWindowRefreshInterval\": 3600,\n            \"supportedRegions\": [\"US\"]\n        },\n        \"serverURL\": \"https://www.apple.com\",\n        \"apiPath\": {\n            \"gridLookup\": \"/v1/getGrid\",\n            \"gridTileLookup\": \"v1/gridTileBoundaries\",\n            \"gridForecast\": \"/v1/gridSignal/getForecast\",\n            \"gridHistory\": \"/v1/gridSignal/getHistory\",\n            \"energyIntervals\": \"/v1/energyWindows\",\n            \"gridSignal\": \"/v1/energyKit/gridSignal\",\n            \"energyKitForecast\": \"/v1/energy-kit/guidance-forecast\",\n            \"energyKitHistorical\": \"/v1/energy-kit/guidance-historical\",\n            \"energyKitStats\": \"/v1/energy-kit/guidance-statistics\"\n        }\n    },\n    \"configuration\": {\n        \"cecEnabled\": true,\n        \"accountingEnabled\": true\n    },\n    \"version\": 1\n}"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "No grid information to save."
- "Saved computed grid for coordinate value."
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unable to ceil end half hour"
- "Unable to floor start half hour"
- "Unable to generate key for saving grid info."
- "Unable to get minute of day"
- "Unable to retrieve hour component"
- "Unable to truncante start time"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_TtC12HomeServices11TimeService"
- "com.apple.wpc.homeservices.energyservices"
- "invalid Collection: less than 'count' elements in collection"
- "{\n    \"serverUrl\": \"https://www.apple.com/v1/\",\n    \"energyServices\": {\n        \"configuration\": {\n            \"energyWindowRefreshInterval\": 3600,\n            \"supportedRegions\": [\"US\"]\n        },\n        \"serverURL\": \"https://www.apple.com\",\n        \"apiPath\": {\n            \"gridLookup\": \"/v1/getGrid\",\n            \"gridTileLookup\": \"v1/gridTileBoundaries\",\n            \"gridForecast\": \"/v1/gridSignal/getForecast\",\n            \"gridHistory\": \"/v1/gridSignal/getHistory\",\n            \"energyIntervals\": \"/v1/energyWindows\",\n            \"gridSignal\": \"/v1/energyKit/gridSignal\"\n        }\n    },\n    \"configuration\": {\n        \"cecEnabled\": true,\n        \"accountingEnabled\": true\n    },\n    \"version\": 1\n}"

```
