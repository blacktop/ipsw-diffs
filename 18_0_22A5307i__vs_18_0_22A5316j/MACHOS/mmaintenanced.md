## mmaintenanced

> `/usr/libexec/mmaintenanced`

```diff

-154.0.0.0.0
-  __TEXT.__text: 0x16458
-  __TEXT.__auth_stubs: 0xdf0
+155.0.0.0.0
+  __TEXT.__text: 0x17690
+  __TEXT.__auth_stubs: 0xf30
   __TEXT.__init_offsets: 0x8
   __TEXT.__const: 0x115a
-  __TEXT.__oslogstring: 0x1e43
-  __TEXT.__cstring: 0x1365
-  __TEXT.__gcc_except_tab: 0x794
-  __TEXT.__swift5_typeref: 0x23
-  __TEXT.__swift5_capture: 0x38
-  __TEXT.__unwind_info: 0x760
-  __TEXT.__eh_frame: 0xf0
-  __DATA_CONST.__auth_got: 0x700
-  __DATA_CONST.__got: 0x170
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xc58
+  __TEXT.__oslogstring: 0x1f33
+  __TEXT.__cstring: 0x1638
+  __TEXT.__gcc_except_tab: 0x758
+  __TEXT.__swift5_typeref: 0x39
+  __TEXT.__swift5_capture: 0x60
+  __TEXT.__unwind_info: 0x7d8
+  __TEXT.__eh_frame: 0x1a0
+  __DATA_CONST.__auth_got: 0x7a0
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__const: 0xcc8
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__data: 0xe60
+  __DATA.__data: 0xe80
   __DATA.__bss: 0x40
   __DATA.__common: 0x31
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 473
-  Symbols:   326
-  CStrings:  372
+  Functions: 502
+  Symbols:   353
+  CStrings:  391
 
Symbols:
+ _$s20ModelManagerServices9AssertionC10invalidateyyYaF
+ _$s20ModelManagerServices9AssertionC10invalidateyyYaFTu
+ _$s20ModelManagerServices9AssertionC6policy11descriptionACSS_SStYaKcfC
+ _$s20ModelManagerServices9AssertionC6policy11descriptionACSS_SStYaKcfCTu
+ _$s20ModelManagerServices9AssertionCMa
+ _$sSS8UTF8ViewV13_foreignCountSiyF
+ _$sSo13os_log_type_ta0A0E7defaultABvgZ
+ _$sSw10copyMemory4fromySW_tF
+ _$sSwys5UInt8VSicis
+ _$ss11_StringGutsV8copyUTF84intoSiSgSrys5UInt8VG_tF
+ _$ss11_StringGutsVN
+ _$ss13_StringObjectV10sharedUTF8SRys5UInt8VGvg
+ _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _$ss23_ContiguousArrayStorageCMn
+ _$ss5ErrorP10FoundationE20localizedDescriptionSSvg
+ _$ss5UInt8VMn
+ _$sypN
+ __swiftEmptyArrayStorage
+ _dispatch_retain
+ _malloc_size
+ _objc_release_x19
+ _swift_arrayDestroy
+ _swift_bridgeObjectRetain
+ _swift_errorRetain
+ _swift_getErrorValue
+ _swift_isUniquelyReferenced_nonNull_native
CStrings:
+ "Acquired MemoryMaintenance assertion in modelmanagerd"
+ "Failed to acquire MemoryMaintenance assertion in modelmanagerd: %!s(MISSING)"
+ "Fatal error"
+ "Hold models unloaded during ane memory validation"
+ "Insufficient space allocated to copy string contents"
+ "MemoryMaintenance"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "com.apple.MemoryMaintenance"
+ "invalid Collection: less than 'count' elements in collection"
+ "modelmanagerd model count query timeout, skipping ane abandonment check"
+ "modelmanagerd timeout in aquiring assertion, skipping ane abandonment check"
- "modelmanagerd timeout, skipping ane abandonment check"

```
