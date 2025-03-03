## CloudTelemetryService

> `/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService`

```diff

-2200.144.0.0.0
-  __TEXT.__text: 0x87b88
-  __TEXT.__auth_stubs: 0x2180
+2250.14.0.0.0
+  __TEXT.__text: 0x7f66c
+  __TEXT.__auth_stubs: 0x21b0
   __TEXT.__objc_stubs: 0x320
-  __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0x3bac
+  __TEXT.__objc_methlist: 0x194
+  __TEXT.__const: 0x45dc
   __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__cstring: 0x2fa0
+  __TEXT.__cstring: 0x2d60
   __TEXT.__objc_classname: 0x82
-  __TEXT.__objc_methname: 0x931
+  __TEXT.__objc_methname: 0x946
   __TEXT.__objc_methtype: 0x220
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__oslogstring: 0x19d7
-  __TEXT.__swift5_typeref: 0x1287
-  __TEXT.__constg_swiftt: 0x16d0
+  __TEXT.__oslogstring: 0x19e0
+  __TEXT.__swift5_typeref: 0x1261
+  __TEXT.__constg_swiftt: 0x1710
   __TEXT.__swift5_reflstr: 0xef5
-  __TEXT.__swift5_fieldmd: 0x1928
-  __TEXT.__swift5_capture: 0xa80
-  __TEXT.__swift5_builtin: 0x64
+  __TEXT.__swift5_fieldmd: 0x1978
+  __TEXT.__swift5_capture: 0x2d0
+  __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_assocty: 0x128
-  __TEXT.__swift5_proto: 0x3c4
-  __TEXT.__swift5_types: 0x1f4
+  __TEXT.__swift5_proto: 0x3e0
+  __TEXT.__swift5_types: 0x1fc
+  __TEXT.__swift_as_entry: 0x158
+  __TEXT.__swift_as_ret: 0x190
   __TEXT.__swift5_protos: 0x2c
-  __TEXT.__swift5_mpenum: 0x18
+  __TEXT.__swift5_mpenum: 0x20
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x2220
-  __TEXT.__eh_frame: 0x4cd8
-  __DATA_CONST.__auth_got: 0x10d0
-  __DATA_CONST.__got: 0x4d8
-  __DATA_CONST.__auth_ptr: 0x5b8
-  __DATA_CONST.__const: 0x4bc8
+  __TEXT.__unwind_info: 0x1dc8
+  __TEXT.__eh_frame: 0x50a8
+  __DATA_CONST.__auth_got: 0x10e8
+  __DATA_CONST.__got: 0x4f8
+  __DATA_CONST.__auth_ptr: 0x550
+  __DATA_CONST.__const: 0x39d0
   __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA.__objc_const: 0x1d10
-  __DATA.__objc_selrefs: 0x260
+  __DATA.__objc_const: 0x1aa0
+  __DATA.__objc_selrefs: 0x330
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x230
-  __DATA.__data: 0x27f0
-  __DATA.__bss: 0x62d0
+  __DATA.__data: 0x2890
+  __DATA.__bss: 0x66a0
   __DATA.__common: 0x270
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /System/Library/PrivateFrameworks/C2.framework/C2
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
+  - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2471
-  Symbols:   332
-  CStrings:  572
+  Functions: 2048
+  Symbols:   346
+  CStrings:  558
 
Symbols:
+ _OBJC_CLASS_$_OSASystemConfiguration
+ _objc_retain_x28
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
+ _swift_getExistentialTypeMetadata
- _swift_allocateGenericValueMetadata
- _swift_initEnumMetadataMultiPayload
- _swift_initEnumMetadataSinglePayload
- _swift_initStructMetadata
CStrings:
+ ", failed to decode json response"
+ "INSERT INTO session_cache (session_id, client_type, event_type, tc_allows_cellular, tc_allows_expensive, tc_bundle_id, sampling_factor, session_created) VALUES (?, ?, ?, ?, ?)"
+ "_automatedDeviceGroup"
+ "automatedDeviceGroup"
+ "com.apple.demo-settings"
+ "failed to download storebag data with status code "
+ "https://gateway.icloud.com/ctstorebagservice"
+ "storebag-internal"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Not enough bits to represent the passed value"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
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
