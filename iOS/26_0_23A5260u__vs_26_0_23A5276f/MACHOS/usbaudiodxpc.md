## usbaudiodxpc

> `/System/Library/Audio/Plug-Ins/HAL/usbaudiodxpc.driver/usbaudiodxpc`

```diff

-802.17.0.0.0
-  __TEXT.__text: 0x2ac0
+802.30.0.0.0
+  __TEXT.__text: 0x2ae8
   __TEXT.__auth_stubs: 0x5f0
   __TEXT.__objc_methlist: 0x2c
   __TEXT.__const: 0x34

   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0xf8
   __DATA_CONST.__auth_got: 0x2f8
-  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x178
+  __DATA_CONST.__const: 0x158
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x130

   __DATA.__data: 0xb8
   __DATA.__bss: 0x8
   __DATA.__common: 0x8
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AudioServerDriver.framework/AudioServerDriver
   - /System/Library/PrivateFrameworks/IOKitten.framework/IOKitten

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: FE27A7C8-DE3E-38A0-99FA-83DAA5242905
+  UUID: 46F2F4CC-96E2-349C-B37C-F8B28A481340
   Functions: 47
-  Symbols:   88
+  Symbols:   85
   CStrings:  32
 
Symbols:
+ _OBJC_CLASS_$_NSDictionary
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
Functions:
~ sub_16cc -> sub_15fc : 1328 -> 1368

```
