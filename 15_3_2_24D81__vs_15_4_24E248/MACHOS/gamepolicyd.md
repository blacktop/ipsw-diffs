## gamepolicyd

> `/usr/libexec/gamepolicyd`

```diff

-2.2.1.0.0
-  __TEXT.__text: 0x56860
-  __TEXT.__auth_stubs: 0x19e0
+2.4.2.0.0
+  __TEXT.__text: 0x54188
+  __TEXT.__auth_stubs: 0x19a0
   __TEXT.__objc_stubs: 0x360
-  __TEXT.__objc_methlist: 0x408
-  __TEXT.__const: 0x17e0
-  __TEXT.__cstring: 0x3222
+  __TEXT.__objc_methlist: 0x764
+  __TEXT.__const: 0x1810
+  __TEXT.__cstring: 0x2f32
   __TEXT.__objc_methname: 0x11b3
   __TEXT.__oslogstring: 0x1615
-  __TEXT.__gcc_except_tab: 0x58
+  __TEXT.__gcc_except_tab: 0x6c
   __TEXT.__objc_classname: 0x131
   __TEXT.__objc_methtype: 0x2ea
-  __TEXT.__swift5_typeref: 0xe84
+  __TEXT.__swift5_typeref: 0xe8c
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x1db0
   __TEXT.__swift5_builtin: 0x3c

   __TEXT.__swift5_types: 0xc4
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_capture: 0x56c
-  __TEXT.__unwind_info: 0xe48
-  __TEXT.__eh_frame: 0xd2c
-  __DATA_CONST.__auth_got: 0xd00
+  __TEXT.__swift_as_entry: 0x38
+  __TEXT.__swift_as_ret: 0x44
+  __TEXT.__unwind_info: 0xde0
+  __TEXT.__eh_frame: 0xd1c
+  __DATA_CONST.__auth_got: 0xce0
   __DATA_CONST.__got: 0x3d8
-  __DATA_CONST.__auth_ptr: 0x3e0
-  __DATA_CONST.__const: 0x1db8
+  __DATA_CONST.__auth_ptr: 0x3e8
+  __DATA_CONST.__const: 0x1de8
   __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x3728
-  __DATA.__objc_selrefs: 0x590
+  __DATA.__objc_const: 0x3448
+  __DATA.__objc_selrefs: 0x630
   __DATA.__objc_ivar: 0x2c
-  __DATA.__objc_data: 0xcf0
-  __DATA.__data: 0x3498
+  __DATA.__objc_data: 0x9b8
+  __DATA.__data: 0x34a0
   __DATA.__bss: 0x16a0
   __DATA.__common: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 15DD8078-7204-3173-9DB8-102EDEF72B06
-  Functions: 1305
-  Symbols:   621
-  CStrings:  781
+  UUID: FEF137E6-B249-37EF-AE71-510E64C1D75C
+  Functions: 1278
+  Symbols:   616
+  CStrings:  763
 
Symbols:
+ _$ss10_HashTableV11startBucketAB0D0Vvg
- _$s10Foundation3URLVMn
- _$sSa12_endMutationyyFyXl_Ts5
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
CStrings:
+ "Responsible process = %{public, name=responsibleProcess}s"
+ "Signpost ID is process ID\nBundle ID = %{public, name=bundleIdentifier}s\nRequires Performance Gaming Tier = %{public, name=requiresPerformanceGamingTier}d\nSupports SEM = %{public, name=supportsSEM}d\nSupports Model Manager Assertion = %{public, name=supportsModelManagerAssertion}d\nRequires Model Manager Assertion = %{public, name=requiresModelManagerAssertion}d"
+ "TrackedProcessLifetime"
+ "com.apple.GameOverlayUIInternal"
+ "com.apple.GameOverlayViewService"
- "Bundle ID = %{public, name=bundleId}%s\n\nRequires Performance Gaming Tier = %{public, name=requiresPerformanceGamingTier}%d\n\nSupports SEM = %{public, name=supportsSEM}d\n\nSupports Model Manager Assertion = %{public, name=supportsModelManagerAssertion}d\n\nRequires Model Manager Assertion %{public, name=requiresModelManagerAssertion}d"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "GameSession"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
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
