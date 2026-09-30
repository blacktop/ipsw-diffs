## usbaudiodxpc

> `/System/Library/Audio/Plug-Ins/HAL/usbaudiodxpc.driver/usbaudiodxpc`

```diff

-802.45.0.0.0
+802.55.0.0.0
   __TEXT.__text: 0x2c38
   __TEXT.__auth_stubs: 0x600
   __TEXT.__objc_methlist: 0x2c

   __DATA_CONST.__auth_got: 0x300
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x158
+  __DATA_CONST.__const: 0x168
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x130

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: C4628EB1-9A05-3E63-85D5-736606FFE4D6
+  UUID: CDBD2E8F-32E6-34C1-9D60-D45059443F1B
   Functions: 47
-  Symbols:   85
+  Symbols:   87
   CStrings:  33
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private

```
