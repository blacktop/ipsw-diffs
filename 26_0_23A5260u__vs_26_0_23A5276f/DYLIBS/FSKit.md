## FSKit

> `/System/Library/PrivateFrameworks/FSKit.framework/FSKit`

```diff

-737.0.2.0.1
-  __TEXT.__text: 0x3fb70
+737.0.10.0.0
+  __TEXT.__text: 0x401fc
   __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x49d4
+  __TEXT.__objc_methlist: 0x49c4
   __TEXT.__const: 0x390
-  __TEXT.__gcc_except_tab: 0xdd0
-  __TEXT.__cstring: 0x420f
-  __TEXT.__oslogstring: 0x2ec1
+  __TEXT.__gcc_except_tab: 0xdd8
+  __TEXT.__cstring: 0x429f
+  __TEXT.__oslogstring: 0x3007
   __TEXT.__swift5_typeref: 0x1d1
   __TEXT.__swift5_capture: 0x58
   __TEXT.__swift5_reflstr: 0x16

   __TEXT.__unwind_info: 0x12f0
   __TEXT.__eh_frame: 0x160
   __TEXT.__objc_classname: 0x8e7
-  __TEXT.__objc_methname: 0x99e0
+  __TEXT.__objc_methname: 0x9991
   __TEXT.__objc_methtype: 0x32db
   __TEXT.__objc_stubs: 0x56c0
   __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0x1358
+  __DATA_CONST.__const: 0x1338
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2480
+  __DATA_CONST.__objc_selrefs: 0x2470
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x6a0
   __AUTH_CONST.__const: 0x4e8
-  __AUTH_CONST.__cfstring: 0x22c0
+  __AUTH_CONST.__cfstring: 0x2300
   __AUTH_CONST.__objc_const: 0x7e70
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1040

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F8A62C69-C660-3BF2-A3D8-C9DDBED76BB8
-  Functions: 1985
-  Symbols:   6330
-  CStrings:  3307
+  UUID: 4A5FA78B-4DD5-3D1D-979A-00CF18401299
+  Functions: 1992
+  Symbols:   6336
+  CStrings:  3320
 
Symbols:
+ -[FSModuleHost(Project) loadEnabledList].cold.3
+ -[FSModuleHost(Project) loadEnabledList].cold.4
+ -[FSModuleHost(Project) loadProbeOrderList].cold.3
+ -[FSModuleHost(Project) loadProbeOrderList].cold.4
+ -[FSModuleHost(Project) saveEnabledList].cold.2
+ -[FSModuleHost(Project) saveProbeOrderList].cold.2
+ __FSKitLocalizedString
+ __FSKitLocalizedStringWithFormat
+ __OBJC_$_INSTANCE_METHODS_FSUnaryFileSystem
+ __OBJC_CLASS_PROTOCOLS_$_FSUnaryFileSystem(FSUnaryFileSystem_project)
- -[FSFileSystem wipeResource:reply:]
- -[FSUnaryFileSystem(Private) wipeResource:includingRanges:excludingRanges:replyHandler:]
- __OBJC_$_INSTANCE_METHODS_FSUnaryFileSystem(FSUnaryFileSystem_project|Private)
- __OBJC_CLASS_PROTOCOLS_$_FSUnaryFileSystem(FSUnaryFileSystem_project|Private)
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_FSKit
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_FSKit
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_FSKit
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_FSKit
CStrings:
+ "%s: Can't get enabled list URL, can't load enabled list"
+ "%s: Can't get enabled list URL, can't save enabled list"
+ "%s: Can't get probe order URL, can't load probe order"
+ "%s: Can't get probe order URL, can't save probe order"
+ "-[FSModuleHost(Project) loadEnabledList]"
+ "-[FSModuleHost(Project) loadProbeOrderList]"
+ "-[FSModuleHost(Project) saveEnabledList]"
+ "-[FSModuleHost(Project) saveProbeOrderList]"
+ "Couldn't find value for key %@ in %@ at %@"
+ "FSClientLocalizable"
+ "LOCALIZED_STRING_UNAVAILABLE"
+ "Load default enabled list"
+ "Loading the default probe order list"
+ "UnknownBundle"
+ "VolNameContainsInvalidChars"
+ "VolNameStartsWithSpace"
+ "VolNameTooLongAPFS"
+ "VolNameTooLongFAT"
+ "VolNameTooLongHFS"
- "Unknown bundle"
- "Volume name contains invalid characters"
- "Volume name exceeds 11 characters"
- "Volume name exceeds 255 characters"
- "Volume name exceeds 256 characters"
- "Volume name starts with a space"
- "wipeResource:includingRanges:excludingRanges:replyHandler:"
- "wipeResource:reply:"

```
