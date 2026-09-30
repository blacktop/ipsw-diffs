## callintelligenced

> `/System/Library/PrivateFrameworks/CallIntelligence.framework/callintelligenced`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA.__objc_selrefs`

```diff

-145.100.7.0.0
+147.100.5.0.0
   __TEXT.__text: 0xaa8
   __TEXT.__auth_stubs: 0x170
   __TEXT.__objc_stubs: 0x40

   __TEXT.__objc_methname: 0x10
   __TEXT.__unwind_info: 0x98
   __TEXT.__eh_frame: 0xb0
-  __DATA_CONST.__const: 0xd8
+  __DATA_CONST.__const: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0xc0
   __DATA_CONST.__got: 0x38

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/CallIntelligence.framework/Versions/A/CallIntelligence
+  - /System/Library/PrivateFrameworks/CallIntelligenceRuntime.framework/Versions/A/CallIntelligenceRuntime
   - /System/Library/PrivateFrameworks/CallsXPC.framework/Versions/A/CallsXPC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMediaIO.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 15
-  Symbols:   51
+  Symbols:   57
   CStrings:  2
 
Symbols:
+ _$s23CallIntelligenceRuntime6DaemonC5startyyYaKF
+ _$s23CallIntelligenceRuntime6DaemonC5startyyYaKFTu
+ _$s23CallIntelligenceRuntime6DaemonCACycfc
+ _$s23CallIntelligenceRuntime6DaemonCMa
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreMediaIO
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftOSLog
- _$s16CallIntelligence6DaemonC5startyyYaKF
- _$s16CallIntelligence6DaemonC5startyyYaKFTu
- _$s16CallIntelligence6DaemonCACycfc
- _$s16CallIntelligence6DaemonCMa
```
