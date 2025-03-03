## AppStoreEvalLighthouseWorker

> `/System/Library/ExtensionKit/Extensions/AppStoreEvalLighthouseWorker.appex/AppStoreEvalLighthouseWorker`

```diff

-1.3.26.0.0
-  __TEXT.__text: 0x170ec
-  __TEXT.__auth_stubs: 0xae0
-  __TEXT.__const: 0x626
-  __TEXT.__cstring: 0x73e
+1.3.31.0.0
+  __TEXT.__text: 0x1869c
+  __TEXT.__auth_stubs: 0xb90
+  __TEXT.__const: 0x686
+  __TEXT.__cstring: 0x50e
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_typeref: 0x38d
+  __TEXT.__swift5_typeref: 0x3af
   __TEXT.__constg_swiftt: 0xc8
-  __TEXT.__swift5_reflstr: 0x3dc
-  __TEXT.__swift5_fieldmd: 0x194
+  __TEXT.__swift5_reflstr: 0x48c
+  __TEXT.__swift5_fieldmd: 0x20c
   __TEXT.__swift5_assocty: 0x90
-  __TEXT.__swift5_capture: 0x610
-  __TEXT.__oslogstring: 0x644
-  __TEXT.__objc_methname: 0x245
+  __TEXT.__swift5_capture: 0x620
+  __TEXT.__objc_methname: 0x263
+  __TEXT.__oslogstring: 0x7f4
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x50
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x348
-  __TEXT.__eh_frame: 0x340
-  __DATA_CONST.__auth_got: 0x570
-  __DATA_CONST.__got: 0x108
-  __DATA_CONST.__auth_ptr: 0x2c8
-  __DATA_CONST.__const: 0x13d0
+  __TEXT.__swift_as_entry: 0x14
+  __TEXT.__swift_as_ret: 0x1c
+  __TEXT.__unwind_info: 0x308
+  __TEXT.__eh_frame: 0x348
+  __DATA_CONST.__auth_got: 0x5c8
+  __DATA_CONST.__got: 0x128
+  __DATA_CONST.__auth_ptr: 0x2d8
+  __DATA_CONST.__const: 0x1468
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0xa0
-  __DATA.__data: 0x230
+  __DATA.__objc_selrefs: 0xb0
+  __DATA.__data: 0x248
   __DATA.__bss: 0xa60
-  __DATA.__common: 0x28
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 411
-  Symbols:   114
+  Functions: 406
+  Symbols:   121
   CStrings:  105
 
Symbols:
+ _objc_retain_x22
+ _objc_retain_x26
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_release_n
+ _swift_stdlib_random
- _objc_retain_x23
- _objc_retain_x28
- _os_variant_has_internal_diagnostics
- _swift_initStructMetadata
CStrings:
+ "%s is not selected due to sampling. Exit early."
+ "Device region is %s"
+ "Device region is %s, but expected %s. Exiting early."
+ "Device region is %s, which is excluded by %s. Exiting early."
+ "Excluded regions are %s"
+ "Expected regions are %s"
+ "Failed to parse recipeAsString into dictionary: %s"
+ "Sampled probability as %ld. If less than sampling rate, then selected"
+ "Sampling is %ld"
+ "Sampling is %ld, but expected [1, 1000]. Exiting early."
+ "deviceRegionIsExcluded"
+ "deviceRegionNotInExpectedList"
+ "notSelectedInSampling"
+ "objectForKey:"
+ "samplingRateInvalid"
+ "setBool:forKey:"
- "Failed to parse recipeString into dictionary: %s"
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
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "com.apple.AppleMediaDiscoveryFramework"
- "invalid Collection: less than 'count' elements in collection"

```
