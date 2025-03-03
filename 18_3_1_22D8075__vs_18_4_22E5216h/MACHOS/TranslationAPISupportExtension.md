## TranslationAPISupportExtension

> `/System/Library/ExtensionKit/Extensions/TranslationAPISupportExtension.appex/TranslationAPISupportExtension`

```diff

-300.2.0.0.0
-  __TEXT.__text: 0x1c10c
-  __TEXT.__auth_stubs: 0x1120
-  __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0xb98
-  __TEXT.__swift5_typeref: 0x13e1
-  __TEXT.__cstring: 0x912
+300.8.0.0.0
+  __TEXT.__text: 0x1a520
+  __TEXT.__auth_stubs: 0x10d0
+  __TEXT.__objc_methlist: 0x1b4
+  __TEXT.__const: 0xc18
+  __TEXT.__swift5_typeref: 0x140d
+  __TEXT.__cstring: 0x612
   __TEXT.__objc_methname: 0x43e
   __TEXT.__swift5_reflstr: 0x22f
   __TEXT.__swift5_assocty: 0xc0

   __TEXT.__swift5_protos: 0x8
   __TEXT.__objc_classname: 0x25
   __TEXT.__objc_methtype: 0x152
+  __TEXT.__swift_as_entry: 0x14
+  __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x730
-  __TEXT.__eh_frame: 0x5c8
-  __DATA_CONST.__auth_got: 0x890
+  __TEXT.__unwind_info: 0x6f0
+  __TEXT.__eh_frame: 0x5f8
+  __DATA_CONST.__auth_got: 0x868
   __DATA_CONST.__got: 0x2d0
   __DATA_CONST.__auth_ptr: 0x3b8
-  __DATA_CONST.__const: 0x738
+  __DATA_CONST.__const: 0x758
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA.__objc_const: 0x710
-  __DATA.__objc_selrefs: 0xf8
-  __DATA.__objc_data: 0x438
+  __DATA.__objc_const: 0x4e8
+  __DATA.__objc_selrefs: 0x1a0
+  __DATA.__objc_data: 0x3d8
   __DATA.__data: 0x9d8
   __DATA.__bss: 0x890
   __DATA.__common: 0x38

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 565
-  Symbols:   164
-  CStrings:  152
+  Functions: 553
+  Symbols:   169
+  CStrings:  136
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftIntents
+ _objc_release_x28
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_release_x9
- _objc_retain_x1
- _objc_retain_x26
- _swift_allocateGenericValueMetadata
- _swift_initStructMetadata
CStrings:
- "Can't construct Array with count < 0"
- "Insufficient space allocated to copy string contents"
- "Swift/Array.swift"
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
- "invalid Collection: less than 'count' elements in collection"

```
