## Diagnostics Reporter

> `/System/Library/CoreServices/Diagnostics Reporter.app/Contents/MacOS/Diagnostics Reporter`

```diff

-727.80.2.0.0
-  __TEXT.__text: 0x16288
-  __TEXT.__auth_stubs: 0xfc0
-  __TEXT.__objc_methlist: 0x150
-  __TEXT.__cstring: 0xed4
-  __TEXT.__const: 0x814
-  __TEXT.__swift5_typeref: 0x7e0
+758.100.43.0.0
+  __TEXT.__text: 0x185e8
+  __TEXT.__auth_stubs: 0xf70
+  __TEXT.__objc_methlist: 0x500
+  __TEXT.__cstring: 0xb84
+  __TEXT.__const: 0x8b4
   __TEXT.__objc_methname: 0xdbd
-  __TEXT.__oslogstring: 0x46c
+  __TEXT.__oslogstring: 0x4dc
+  __TEXT.__swift5_typeref: 0x7c2
   __TEXT.__swift5_capture: 0x50
-  __TEXT.__swift5_fieldmd: 0x2f0
+  __TEXT.__swift5_fieldmd: 0x308
   __TEXT.__constg_swiftt: 0x4cc
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_reflstr: 0x1c3
+  __TEXT.__swift5_reflstr: 0x1ec
   __TEXT.__swift5_types: 0x4c
   __TEXT.__objc_classname: 0x2f
   __TEXT.__objc_methtype: 0x43e
-  __TEXT.__swift5_assocty: 0x68
+  __TEXT.__swift5_assocty: 0x98
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_proto: 0x58
+  __TEXT.__swift5_proto: 0x60
   __TEXT.__unwind_info: 0x578
   __TEXT.__eh_frame: 0x4b0
-  __DATA_CONST.__auth_got: 0x7e0
+  __DATA_CONST.__auth_got: 0x7b8
   __DATA_CONST.__got: 0x228
   __DATA_CONST.__auth_ptr: 0x390
-  __DATA_CONST.__const: 0x600
+  __DATA_CONST.__const: 0x6d0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA.__objc_const: 0xe58
-  __DATA.__objc_selrefs: 0x268
-  __DATA.__objc_data: 0x418
-  __DATA.__data: 0x858
-  __DATA.__bss: 0x900
-  __DATA.__common: 0xa0
+  __DATA.__objc_const: 0x808
+  __DATA.__objc_selrefs: 0x460
+  __DATA.__objc_data: 0x360
+  __DATA.__data: 0x8a8
+  __DATA.__bss: 0xa00
+  __DATA.__common: 0x40
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftQuickLookUI.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_errno.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: B349E7E2-9D03-3E6F-AD01-A3C4200398F7
-  Functions: 413
-  Symbols:   440
-  CStrings:  314
+  UUID: 5FD1C3EB-E3EC-34AA-A797-D47B582E449F
+  Functions: 426
+  Symbols:   437
+  CStrings:  301
 
Symbols:
+ _$ss20__StaticArrayStorageCN
+ _$ss21_findStringSwitchCase5cases6stringSiSays06StaticB0VG_SStF
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftDataDetection
- _$sSa12_endMutationyyFyXl_Ts5
- _$sSs8UTF8ViewVys5UInt8VSS5IndexVcig
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- __swift_FORCE_LOAD_$_swiftWebKit
CStrings:
+ "ALE"
+ "Cannot initialize CrashLog of type %s without a fileURL"
+ "Display"
+ "Failed to resolve symlink: %{public}s"
+ "Host"
+ "Standard"
+ "SystemWatchdog"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Must take zero or more splits"
- "Range requires lowerBound <= upperBound"
- "Swift/Collection.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Range.swift"
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
