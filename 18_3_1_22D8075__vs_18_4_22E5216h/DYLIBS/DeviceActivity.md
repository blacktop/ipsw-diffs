## DeviceActivity

> `/System/Library/Frameworks/DeviceActivity.framework/DeviceActivity`

```diff

-377.3.2.0.0
-  __TEXT.__text: 0x95590
-  __TEXT.__auth_stubs: 0x1670
-  __TEXT.__objc_methlist: 0x184
-  __TEXT.__const: 0x3192
-  __TEXT.__cstring: 0x11fb
-  __TEXT.__swift5_typeref: 0x1274
+377.4.6.0.0
+  __TEXT.__text: 0x88f80
+  __TEXT.__auth_stubs: 0x16d0
+  __TEXT.__objc_methlist: 0x300
+  __TEXT.__const: 0x2fe2
+  __TEXT.__cstring: 0xeab
+  __TEXT.__swift5_typeref: 0x12d8
   __TEXT.__swift5_fieldmd: 0xe48
   __TEXT.__constg_swiftt: 0xc78
   __TEXT.__swift5_builtin: 0x78

   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_proto: 0x2b4
   __TEXT.__swift5_types: 0xf8
-  __TEXT.__swift5_capture: 0x390
-  __TEXT.__oslogstring: 0x120b
-  __TEXT.__unwind_info: 0x1c18
-  __TEXT.__eh_frame: 0x2b98
+  __TEXT.__swift5_capture: 0x430
+  __TEXT.__oslogstring: 0x121b
+  __TEXT.__swift_as_entry: 0x24
+  __TEXT.__swift_as_ret: 0x38
+  __TEXT.__unwind_info: 0x1a38
+  __TEXT.__eh_frame: 0x2e18
   __TEXT.__objc_classname: 0x52
-  __TEXT.__objc_methname: 0x162b
+  __TEXT.__objc_methname: 0x1639
   __TEXT.__objc_methtype: 0x51d
-  __DATA_CONST.__got: 0x4f0
-  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__got: 0x528
+  __DATA_CONST.__const: 0x148
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x600
+  __DATA_CONST.__objc_selrefs: 0x668
   __DATA_CONST.__objc_protorefs: 0x28
-  __AUTH_CONST.__auth_got: 0xb38
-  __AUTH_CONST.__auth_ptr: 0x558
-  __AUTH_CONST.__const: 0x2200
+  __AUTH_CONST.__auth_got: 0xb68
+  __AUTH_CONST.__auth_ptr: 0x570
+  __AUTH_CONST.__const: 0x2528
   __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__objc_const: 0x8c8
-  __AUTH.__objc_data: 0x38
-  __DATA.__data: 0xb80
+  __AUTH_CONST.__objc_const: 0x640
+  __DATA.__data: 0xc50
   __DATA.__bss: 0x3c80
-  __DATA.__common: 0x88
+  __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x350
   __DATA_DIRTY.__data: 0xfb0
   __DATA_DIRTY.__bss: 0x1280

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
-  Functions: 2398
-  Symbols:   327
-  CStrings:  447
+  Functions: 2274
+  Symbols:   363
+  CStrings:  429
 
Symbols:
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _dispatch_sync
+ _objc_retain_x4
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_getExistentialTypeMetadata
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_release_x9
- _swift_allocateGenericValueMetadata
- _swift_initEnumMetadataMultiPayload
- _swift_initStructMetadata
CStrings:
+ "Skipping refresh because query interval has invalid bounds using local start date: %{public}s, thirty days ago: %{public}s, now: %{public}s"
+ "Skipping refresh because query start: %{public}s, is out of bounds: %{public}s - %{public}s"
+ "applicationID"
+ "com.apple.DeviceActivity.EventStreams.testBiomeQueue"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Local start date is in the future; skipping refresh"
- "Start of query: %{public}s is after the current date: %{public}s"
- "Start of query: %{public}s is before thirty days ago: %{public}s"
- "Swift/Array.swift"
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
