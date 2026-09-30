## gamepolicyd

> `/usr/libexec/gamepolicyd`

```diff

-2.2.1.0.0
-  __TEXT.__text: 0x2fc04
-  __TEXT.__auth_stubs: 0x1010
+2.4.1.0.0
+  __TEXT.__text: 0x2ffa8
+  __TEXT.__auth_stubs: 0x1020
   __TEXT.__objc_stubs: 0x20
   __TEXT.__objc_methlist: 0x574
-  __TEXT.__const: 0x1044
-  __TEXT.__objc_methname: 0xc84
+  __TEXT.__const: 0x1084
+  __TEXT.__objc_methname: 0xc92
   __TEXT.__objc_classname: 0xd5
   __TEXT.__objc_methtype: 0x2ed
-  __TEXT.__cstring: 0x23cb
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

   __TEXT.__swift_as_ret: 0x30
   __TEXT.__unwind_info: 0x708
   __TEXT.__eh_frame: 0x700
-  __DATA_CONST.__auth_got: 0x810
-  __DATA_CONST.__got: 0x268
-  __DATA_CONST.__auth_ptr: 0x268
+  __DATA_CONST.__auth_got: 0x818
+  __DATA_CONST.__got: 0x278
+  __DATA_CONST.__auth_ptr: 0x280
   __DATA_CONST.__const: 0xf00
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA.__objc_const: 0x2250
-  __DATA.__objc_selrefs: 0x480
+  __DATA.__objc_const: 0x22f0
+  __DATA.__objc_selrefs: 0x488
   __DATA.__objc_data: 0x580
   __DATA.__data: 0x1f30
   __DATA.__common: 0x70

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 661
-  Symbols:   411
-  CStrings:  476
+  Symbols:   415
+  CStrings:  484
 
Symbols:
+ _$ss6UInt64VMn
+ _$ss6UInt64VN
+ _$ss6UInt64Vs7CVarArgsWP
+ _objc_retain_x26
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initializeBufferWithCopyOfBuffer
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
- "JettisonCameraS2R: Disabled"
- "JettisonCameraS2R: Enabled"

```
