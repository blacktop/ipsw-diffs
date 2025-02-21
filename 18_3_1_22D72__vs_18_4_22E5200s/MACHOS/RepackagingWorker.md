## RepackagingWorker

> `/System/Library/ExtensionKit/Extensions/RepackagingWorker.appex/RepackagingWorker`

```diff

-1.2.14.0.0
-  __TEXT.__text: 0x112d4
-  __TEXT.__auth_stubs: 0xc00
-  __TEXT.__const: 0xbda
-  __TEXT.__cstring: 0xa00
+1.4.8.0.0
+  __TEXT.__text: 0x1074c
+  __TEXT.__auth_stubs: 0xba0
+  __TEXT.__const: 0xd6a
+  __TEXT.__cstring: 0x7f8
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x2ac
-  __TEXT.__swift5_typeref: 0x4db
+  __TEXT.__swift5_typeref: 0x4f7
   __TEXT.__swift5_reflstr: 0x1dc
   __TEXT.__swift5_fieldmd: 0x2b0
   __TEXT.__swift5_assocty: 0x90

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0xa8
   __TEXT.__swift5_types: 0x50
+  __TEXT.__swift_as_entry: 0x24
+  __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift5_capture: 0x70
   __TEXT.__oslogstring: 0xc
-  __TEXT.__unwind_info: 0x588
-  __TEXT.__eh_frame: 0x780
-  __DATA_CONST.__auth_got: 0x600
-  __DATA_CONST.__got: 0x188
+  __TEXT.__unwind_info: 0x478
+  __TEXT.__eh_frame: 0x740
+  __DATA_CONST.__auth_got: 0x5d0
+  __DATA_CONST.__got: 0x190
   __DATA_CONST.__auth_ptr: 0x2d8
-  __DATA_CONST.__const: 0xb38
+  __DATA_CONST.__const: 0xb80
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0xb8
   __DATA.__objc_selrefs: 0x108
-  __DATA.__data: 0x400
+  __DATA.__data: 0x408
   __DATA.__bss: 0x1500
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 435
-  Symbols:   146
-  CStrings:  92
+  Functions: 376
+  Symbols:   151
+  CStrings:  79
 
Symbols:
+ _objc_retain_x27
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_initStructMetadataWithLayoutString
- _objc_release_x9
- _swift_initStructMetadata
- _swift_isUniquelyReferenced_nonNull_bridgeObject
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/LighthouseDataProcessor_AllPlatforms/RepackagingWorker/ExtensionPreferences.swift"
+ "/Library/Caches/com.apple.xbs/Sources/LighthouseDataProcessor_AllPlatforms/RepackagingWorker/ExtensionRecipe.swift"
+ "/Library/Caches/com.apple.xbs/Sources/LighthouseDataProcessor_AllPlatforms/RepackagingWorker/InstrumentationUploader.swift"
+ "/Library/Caches/com.apple.xbs/Sources/LighthouseDataProcessor_AllPlatforms/RepackagingWorker/RepackagingWorker.swift"
+ "/Library/Caches/com.apple.xbs/Sources/LighthouseDataProcessor_AllPlatforms/RepackagingWorker/SessionBuilderExtension.swift"
- "/Library/Caches/com.apple.xbs/Sources/LighthouseDataProcessor/RepackagingWorker/ExtensionPreferences.swift"
- "/Library/Caches/com.apple.xbs/Sources/LighthouseDataProcessor/RepackagingWorker/ExtensionRecipe.swift"
- "/Library/Caches/com.apple.xbs/Sources/LighthouseDataProcessor/RepackagingWorker/InstrumentationUploader.swift"
- "/Library/Caches/com.apple.xbs/Sources/LighthouseDataProcessor/RepackagingWorker/RepackagingWorker.swift"
- "/Library/Caches/com.apple.xbs/Sources/LighthouseDataProcessor/RepackagingWorker/SessionBuilderExtension.swift"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
