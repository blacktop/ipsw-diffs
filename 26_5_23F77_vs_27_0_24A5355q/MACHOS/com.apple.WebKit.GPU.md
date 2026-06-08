## com.apple.WebKit.GPU

> `/System/Library/ExtensionKit/Extensions/GPUExtension.appex/com.apple.WebKit.GPU`

```diff

-7624.2.5.10.4
+7625.1.18.10.4
   __TEXT.__text: 0x54c
   __TEXT.__auth_stubs: 0x110
   __TEXT.__objc_stubs: 0x40

   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0x90
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__auth_ptr: 0x70
+  __TEXT.__unwind_info: 0x90
   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x90
+  __DATA_CONST.__got: 0x20
+  __DATA_CONST.__auth_ptr: 0x70
   __DATA.__objc_const: 0x48
   __DATA.__objc_selrefs: 0x20
   __DATA.__objc_data: 0xb0

   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 089003AE-61F2-3EED-97F8-C3C2BCBD8098
+  UUID: E8BFE90C-FA02-3334-888E-BD090C89169B
   Functions: 16
   Symbols:   39
   CStrings:  8
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreLocation
- __swift_FORCE_LOAD_$_swiftCoreMedia
Functions:
~ sub_10000da40 : 52 -> 4
~ sub_10000da74 -> sub_10000da44 : 460 -> 104
~ sub_10000dc40 -> sub_10000daac : 104 -> 460
~ sub_10000dcac -> sub_10000dc7c : 4 -> 52
~ sub_10000dcb4 : 76 -> 4
~ sub_10000dd00 -> sub_10000dcb8 : 4 -> 76

```
