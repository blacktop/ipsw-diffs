## HearingAppPlugin

> `/System/Library/Health/FeedItemPlugins/HearingAppPlugin.healthplugin/HearingAppPlugin`

```diff

-5200.3.6.1.1
-  __TEXT.__text: 0x89a94
-  __TEXT.__auth_stubs: 0x36c0
-  __TEXT.__objc_methlist: 0x198
-  __TEXT.__const: 0x4194
-  __TEXT.__cstring: 0x4710
+5200.4.23.1.1
+  __TEXT.__text: 0x82920
+  __TEXT.__auth_stubs: 0x3650
+  __TEXT.__objc_methlist: 0x2e4
+  __TEXT.__const: 0x4364
+  __TEXT.__cstring: 0x4430
   __TEXT.__constg_swiftt: 0x21a4
   __TEXT.__swift5_typeref: 0x14bc
-  __TEXT.__swift5_reflstr: 0x13c4
+  __TEXT.__swift5_reflstr: 0x13b4
   __TEXT.__swift5_fieldmd: 0x1268
-  __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_assocty: 0x230
   __TEXT.__oslogstring: 0x17e3
   __TEXT.__swift5_capture: 0x4e8
+  __TEXT.__swift5_builtin: 0x78
+  __TEXT.__swift5_assocty: 0x230
   __TEXT.__swift5_proto: 0x308
   __TEXT.__swift5_types: 0x1a8
   __TEXT.__swift5_protos: 0x34
-  __TEXT.__unwind_info: 0x1c08
-  __TEXT.__eh_frame: 0xed0
+  __TEXT.__swift_as_entry: 0x44
+  __TEXT.__swift_as_ret: 0x50
+  __TEXT.__unwind_info: 0x1a08
+  __TEXT.__eh_frame: 0xe90
   __TEXT.__objc_classname: 0x4b
   __TEXT.__objc_methname: 0x1b18
   __TEXT.__objc_methtype: 0xd6
   __TEXT.__objc_stubs: 0x20
   __DATA_CONST.__got: 0xe48
-  __DATA_CONST.__const: 0x178
+  __DATA_CONST.__const: 0x168
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist2: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x838
+  __DATA_CONST.__objc_selrefs: 0x8d0
   __DATA_CONST.__objc_protorefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1b68
-  __AUTH_CONST.__auth_ptr: 0xd68
-  __AUTH_CONST.__const: 0x21d8
-  __AUTH_CONST.__objc_const: 0x25e8
-  __AUTH.__objc_data: 0x1350
-  __AUTH.__data: 0x1740
-  __DATA.__data: 0x1630
+  __AUTH_CONST.__auth_got: 0x1b30
+  __AUTH_CONST.__auth_ptr: 0xd90
+  __AUTH_CONST.__const: 0x2228
+  __AUTH_CONST.__objc_const: 0x23d8
+  __AUTH.__objc_data: 0x12a8
+  __AUTH.__data: 0x16d8
+  __DATA.__data: 0x15f8
   __DATA.__objc_stublist: 0x78
-  __DATA.__common: 0x1c8
-  __DATA.__bss: 0x3a20
-  __DATA_DIRTY.__objc_data: 0x428
-  __DATA_DIRTY.__data: 0xd58
-  __DATA_DIRTY.__bss: 0x1900
-  __DATA_DIRTY.__common: 0x140
+  __DATA.__common: 0x1a0
+  __DATA.__bss: 0x3820
+  __DATA_DIRTY.__objc_data: 0x490
+  __DATA_DIRTY.__data: 0xdb8
+  __DATA_DIRTY.__bss: 0x1b00
+  __DATA_DIRTY.__common: 0x150
   - /System/Library/Frameworks/Charts.framework/Charts
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftGLKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMapKit.dylib

   - /usr/lib/swift/libswiftSceneKit.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2449
-  Symbols:   320
-  CStrings:  828
+  Functions: 2282
+  Symbols:   323
+  CStrings:  812
 
Symbols:
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftWebKit
- _objc_release_x10
- _objc_release_x9
- _swift_initStructMetadata
CStrings:
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
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
