## gamepolicyd

> `/usr/libexec/gamepolicyd`

```diff

-2.2.1.0.0
-  __TEXT.__text: 0x27fc8
-  __TEXT.__auth_stubs: 0x1070
+2.4.1.0.0
+  __TEXT.__text: 0x2ffa8
+  __TEXT.__auth_stubs: 0x1020
   __TEXT.__objc_stubs: 0x20
-  __TEXT.__objc_methlist: 0x1b4
-  __TEXT.__const: 0xff4
-  __TEXT.__objc_methname: 0xc84
+  __TEXT.__objc_methlist: 0x574
+  __TEXT.__const: 0x1084
+  __TEXT.__objc_methname: 0xc92
   __TEXT.__objc_classname: 0xd5
   __TEXT.__objc_methtype: 0x2ed
-  __TEXT.__cstring: 0x26cb
-  __TEXT.__swift5_typeref: 0x8b5
+  __TEXT.__cstring: 0x255b
+  __TEXT.__swift5_typeref: 0x8bb
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x11ec
-  __TEXT.__swift5_reflstr: 0xd5c
-  __TEXT.__swift5_fieldmd: 0x92c
+  __TEXT.__swift5_reflstr: 0xdcc
+  __TEXT.__swift5_fieldmd: 0x968
   __TEXT.__swift5_proto: 0x8c
   __TEXT.__swift5_types: 0x78
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_capture: 0x358
   __TEXT.__oslogstring: 0x958
-  __TEXT.__unwind_info: 0x7a0
+  __TEXT.__swift_as_entry: 0x38
+  __TEXT.__swift_as_ret: 0x30
+  __TEXT.__unwind_info: 0x708
   __TEXT.__eh_frame: 0x700
-  __DATA_CONST.__auth_got: 0x840
-  __DATA_CONST.__got: 0x268
-  __DATA_CONST.__auth_ptr: 0x278
+  __DATA_CONST.__auth_got: 0x818
+  __DATA_CONST.__got: 0x278
+  __DATA_CONST.__auth_ptr: 0x280
   __DATA_CONST.__const: 0xf00
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA.__objc_const: 0x2630
-  __DATA.__objc_selrefs: 0x3c0
-  __DATA.__objc_data: 0x868
-  __DATA.__data: 0x1f20
+  __DATA.__objc_const: 0x22f0
+  __DATA.__objc_selrefs: 0x488
+  __DATA.__objc_data: 0x580
+  __DATA.__data: 0x1f30
   __DATA.__common: 0x70
   __DATA.__bss: 0xe00
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 674
-  Symbols:   412
-  CStrings:  492
+  Functions: 661
+  Symbols:   415
+  CStrings:  484
 
Symbols:
+ _$ss6UInt64VMn
+ _$ss6UInt64VN
+ _$ss6UInt64Vs7CVarArgsWP
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _$sSa12_endMutationyyFyXl_Ts5
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
CStrings:
+ "JettisonCameraS2REnabled"
+ "ModelManagerGameAssertionHeld"
+ "Policy = %{public, name=policy}s"
+ "Signpost ID is process ID\nBundle ID = %{public, name=bundleIdentifier}s\nGenre ID = %{public, name=genreIdentifier}lld\nHas Game Genre ID = %{public, name=hasGameGenre}d\nSupports Game mode = %{public, name=supportsGameMode}d\nRequires Performance Gaming Tier = %{public, name=requiresPerformanceGamingTier}d\nRequires Increased Memory Limit = %{public, name=requiresIncreasedMemoryLimit}d\nRequires Increased Debug Memory Limit = %{public, name=requiresIncreasedDebugMemoryLimit}d\nSupports SEM = %{public, name=supportsSEM}d\nSupports Model Manager Assertion = %{public, name=supportsModelManagerAssertion}d\nRequires Model Manager Assertion = %{public, name=requiresModelManagerAssertion}d\nSupports Camera Jettison S2R = %{public, name=supportsCameraJettisonS2R}d"
+ "TrackedProcessForeground"
+ "TrackedProcessLifetime"
+ "bundleVersion"
+ "hasGameGenreId"
+ "requiresIncreasedDebugMemoryLimit"
+ "requiresIncreasedMemoryLimit"
- "Bundle ID = %{public, name=bundleId}%s\n\nRequires Performance Gaming Tier = %{public, name=requiresPerformanceGamingTier}%d\n\nRequires Increased Memory Limit = %{public, name=requiresIncreasedMemoryLimit}d\n\nRequires Increased Debug Memory Limit = %{public, name=requiresIncreasedDebugMemoryLimit}d\n\nSupports SEM = %{public, name=supportsSEM}d\n\nSupports Model Manager Assertion = %{public, name=supportsModelManagerAssertion}d\n\nRequires Model Manager Assertion %{public, name=requiresModelManagerAssertion}d\n\nSupports Camera Jettison S2R %{public, name=supportsCameraJettisonS2R}d"
- "GameSession"
- "Insufficient space allocated to copy string contents"
- "JettisonCameraS2R: Disabled"
- "JettisonCameraS2R: Enabled"
- "Negative value is not representable"
- "Swift/ContiguousArrayBuffer.swift"
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
