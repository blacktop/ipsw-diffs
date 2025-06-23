## nexusd

> `/usr/libexec/nexusd`

```diff

-730.8.3.0.0
-  __TEXT.__text: 0x2884
+740.14.0.0.0
+  __TEXT.__text: 0x2890
   __TEXT.__auth_stubs: 0x680
   __TEXT.__objc_stubs: 0x500
   __TEXT.__objc_methlist: 0x214

   __DATA_CONST.__auth_got: 0x350
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x128
+  __DATA_CONST.__const: 0x168
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x430
   __DATA.__objc_selrefs: 0x180
-  __DATA.__objc_classrefs: 0x50
-  __DATA.__objc_superrefs: 0x8
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x90

   - /System/Library/PrivateFrameworks/NexusDaemon.framework/NexusDaemon
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: F306EB67-8273-3C9A-B456-749FCAD15DCE
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 91BD0BA0-2689-3C47-A667-99E99F2E0DCF
   Functions: 63
-  Symbols:   143
+  Symbols:   151
   CStrings:  173
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftsimd

```
