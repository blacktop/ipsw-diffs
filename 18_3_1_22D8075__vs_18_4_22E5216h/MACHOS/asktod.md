## asktod

> `/usr/libexec/asktod`

```diff

-41.225.0.0.0
-  __TEXT.__text: 0x35c
-  __TEXT.__auth_stubs: 0x150
+41.226.0.0.0
+  __TEXT.__text: 0x4f0
+  __TEXT.__auth_stubs: 0x160
   __TEXT.__const: 0x32
   __TEXT.__objc_methname: 0x13
   __TEXT.__oslogstring: 0x3f
   __TEXT.__swift5_entry: 0x8
   __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0xa8
+  __TEXT.__eh_frame: 0x48
+  __DATA_CONST.__auth_got: 0xb0
   __DATA_CONST.__got: 0x8
-  __DATA_CONST.__const: 0x118
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x10
-  __DATA.__data: 0x28
+  __DATA.__data: 0x10
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 5
-  Symbols:   59
+  Symbols:   60
   CStrings:  4
 
Symbols:
+ ___chkstk_darwin
+ _objc_release_x23
+ _swift_release
+ _swift_retain
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_release_x19
- _swift_bridgeObjectRetain

```
