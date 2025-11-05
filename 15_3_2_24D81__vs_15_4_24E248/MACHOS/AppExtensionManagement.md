## AppExtensionManagement

> `/System/Library/ExtensionKit/Extensions/AppExtensionManagement.appex/Contents/MacOS/AppExtensionManagement`

```diff

-202.4.0.0.0
+212.4.0.0.0
   __TEXT.__text: 0x1c4
   __TEXT.__auth_stubs: 0x60
   __TEXT.__swift5_entry: 0x8

   __DATA_CONST.__auth_got: 0x30
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0xd8
+  __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x18
   __DATA.__bss: 0x100

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 8C8AFC63-748B-3B5E-A347-37AF2E33EEFF
+  UUID: 4FFB9C37-68F4-3C69-83FB-26500DCCB40F
   Functions: 9
-  Symbols:   29
+  Symbols:   30
   CStrings:  0
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftDataDetection

```
