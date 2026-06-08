## AppExtensionManagement

> `/System/Library/ExtensionKit/Extensions/AppExtensionManagement.appex/AppExtensionManagement`

```diff

-264.4.9.0.0
+289.1.0.0.0
   __TEXT.__text: 0x1c8
   __TEXT.__auth_stubs: 0x70
   __TEXT.__swift5_entry: 0x8

   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0x70
+  __DATA_CONST.__const: 0xb0
+  __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x38
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x48
-  __DATA_CONST.__const: 0xb0
-  __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x18
   __DATA.__bss: 0x100
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7E15DD45-C1F2-3B8E-9797-3339B14A9A31
+  UUID: 29D0EA0C-6FE9-393C-B2C4-C5A9D9DFAADE
   Functions: 10
   Symbols:   24
   CStrings:  0
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreLocation
- __swift_FORCE_LOAD_$_swiftCoreMedia

```
