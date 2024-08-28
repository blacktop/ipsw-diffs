## BuddyMigrator

> `/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator`

```diff

-5337.0.0.0.0
-  __TEXT.__text: 0xf2c8
-  __TEXT.__auth_stubs: 0x940
+5344.2.0.0.0
+  __TEXT.__text: 0xee9c
+  __TEXT.__auth_stubs: 0x880
   __TEXT.__objc_stubs: 0x19e0
-  __TEXT.__objc_methlist: 0x844
-  __TEXT.__const: 0x16c
+  __TEXT.__objc_methlist: 0x854
+  __TEXT.__const: 0x15c
   __TEXT.__gcc_except_tab: 0x218
-  __TEXT.__objc_methname: 0x2003
-  __TEXT.__cstring: 0xf11
-  __TEXT.__oslogstring: 0x15a8
+  __TEXT.__objc_methname: 0x2036
+  __TEXT.__cstring: 0xd01
+  __TEXT.__oslogstring: 0x1658
   __TEXT.__objc_classname: 0xf2
   __TEXT.__objc_methtype: 0x275
   __TEXT.__dlopen_cstrs: 0x166
-  __TEXT.__swift5_typeref: 0x2f4
-  __TEXT.__swift5_fieldmd: 0x100
-  __TEXT.__constg_swiftt: 0x1a8
+  __TEXT.__swift5_typeref: 0x304
+  __TEXT.__swift5_fieldmd: 0x10c
+  __TEXT.__constg_swiftt: 0x1c0
   __TEXT.__swift5_capture: 0x1b8
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_reflstr: 0xd1
-  __TEXT.__unwind_info: 0x500
-  __TEXT.__eh_frame: 0x768
-  __DATA_CONST.__auth_got: 0x4b0
-  __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__auth_ptr: 0x48
-  __DATA_CONST.__const: 0x880
-  __DATA_CONST.__cfstring: 0xa20
+  __TEXT.__unwind_info: 0x4f8
+  __TEXT.__eh_frame: 0x778
+  __DATA_CONST.__auth_got: 0x450
+  __DATA_CONST.__got: 0x2c8
+  __DATA_CONST.__auth_ptr: 0x38
+  __DATA_CONST.__const: 0x8b8
+  __DATA_CONST.__cfstring: 0xa00
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x16f8
-  __DATA.__objc_selrefs: 0x830
+  __DATA.__objc_const: 0x1720
+  __DATA.__objc_selrefs: 0x838
   __DATA.__objc_ivar: 0xa8
-  __DATA.__objc_data: 0x778
-  __DATA.__data: 0x3d8
+  __DATA.__objc_data: 0x7b0
+  __DATA.__data: 0x3f8
   __DATA.__bss: 0x60
   __DATA.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices
+  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
+  - /System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 367
-  Symbols:   306
-  CStrings:  677
+  Functions: 365
+  Symbols:   307
+  CStrings:  670
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ _OBJC_CLASS_$_UNNotificationOnboarding
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftFileProvider
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftDataDetection
- _memcpy
- _swift_bridgeObjectRetain
- __swiftEmptyArrayStorage
- _malloc_size
- _memmove
- _swift_deallocPartialClassInstance
- _swift_isUniquelyReferenced_nonNull_native
CStrings:
+ "Summarization seen status: %!{(MISSING)bool}d"
+ "shouldShowExperience:forClient:"
+ "Checking intelligence on device availability status: %!{(MISSING)bool}d"
+ "Local availability check"
+ "initWithFeatureFlags:availabilityProvider:stateProvider:preferences:"
+ "Failed to determine intelligence status. Error: %!@(MISSING)"
+ "initWithFeatureFlags:preferences:"
+ "BuddyMigrator.IntelligenceAvailabilityProvider"
+ "Intelligence availablility status: %!{(MISSING)bool}d"
+ "Invalid bag configuration"
+ "Intelligence status: %!{(MISSING)bool}d"
+ "Did see intelligence in a previous buddy run"
+ "Checking intelligence status"
+ "shouldShowForSummarization"
+ "@48@0:8@16@24@32@40"
- "initWithFeatureFlags:"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "Swift/ContiguousArrayBuffer.swift"
- "Should show intelligence: %!{(MISSING)bool}d"
- "@40@0:8@16@24@32"
- "Intelligence state: %!s(MISSING)"
- "Swift/UnsafePointer.swift"
- "isEnabledWithCompletionHandler:"
- "Swift/StringUTF8View.swift"
- "UnsafeMutableBufferPointer with negative count"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Fatal error"
- "Checking if intelligence is available: %!{(MISSING)bool}d"
- "Insufficient space allocated to copy string contents"
- "UnsafeMutablePointer.initialize overlapping range"
- "invalid Collection: less than 'count' elements in collection"
- "Unexpectedly found nil while unwrapping an Optional value"
- "initWithFeatureFlags:availabilityProvider:stateProvider:"
- "Intelligence is already enabled."
- "Failed to determine intelligence status. Abort!"
- "Swift/StringTesting.swift"

```
