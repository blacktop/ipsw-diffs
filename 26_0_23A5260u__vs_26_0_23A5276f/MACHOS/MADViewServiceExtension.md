## MADViewServiceExtension

> `/System/Library/ExtensionKit/Extensions/MADViewServiceExtension.appex/MADViewServiceExtension`

```diff

 3.0.10.0.0
-  __TEXT.__text: 0x57d0
-  __TEXT.__auth_stubs: 0x9c0
+  __TEXT.__text: 0x5740
+  __TEXT.__auth_stubs: 0x9d0
   __TEXT.__swift5_entry: 0x8
   __TEXT.__const: 0x424
   __TEXT.__constg_swiftt: 0x1dc

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x20
   __TEXT.__swift5_capture: 0x58
-  __TEXT.__oslogstring: 0xcc
+  __TEXT.__oslogstring: 0x3c
   __TEXT.__objc_methname: 0xd3
   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__cstring: 0xa3
-  __TEXT.__unwind_info: 0x1f0
+  __TEXT.__cstring: 0x133
+  __TEXT.__unwind_info: 0x1f8
   __TEXT.__eh_frame: 0x118
-  __DATA_CONST.__auth_got: 0x4e0
+  __DATA_CONST.__auth_got: 0x4e8
   __DATA_CONST.__got: 0x180
   __DATA_CONST.__auth_ptr: 0x218
-  __DATA_CONST.__const: 0x3b8
+  __DATA_CONST.__const: 0x398
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
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
-  UUID: 7CDEA722-3938-38DE-AA62-3BD299166B5D
+  UUID: 581CC92D-69E0-33E4-820E-51FA402BF253
   Functions: 148
-  Symbols:   112
+  Symbols:   108
   CStrings:  18
 
Symbols:
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."
- "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."

```
