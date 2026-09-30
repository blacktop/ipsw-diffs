## asktod

> `/usr/libexec/asktod`

```diff

-41.225.0.0.0
-  __TEXT.__text: 0x368
-  __TEXT.__auth_stubs: 0x140
+41.226.0.0.0
+  __TEXT.__text: 0x4fc
+  __TEXT.__auth_stubs: 0x150
   __TEXT.__const: 0x32
   __TEXT.__objc_methname: 0x13
   __TEXT.__oslogstring: 0x3f
   __TEXT.__swift5_entry: 0x8
   __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0xa0
+  __TEXT.__eh_frame: 0x48
+  __DATA_CONST.__auth_got: 0xa8
   __DATA_CONST.__got: 0x8
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x10
-  __DATA.__data: 0x28
+  __DATA.__data: 0x10
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 36969682-FBE7-3994-90C5-1B6CD5042DF5
+  UUID: AB3CA53A-8843-33CD-9F5F-423F61098DF8
   Functions: 5
-  Symbols:   57
+  Symbols:   59
   CStrings:  4
 
Symbols:
+ ___chkstk_darwin
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ _swift_release
+ _swift_retain
- __swift_FORCE_LOAD_$_swiftFileProvider
- _swift_bridgeObjectRetain
Functions:
~ sub_1000035f0 -> sub_100001308 : 488 -> 548
~ sub_1000037d8 -> sub_10000152c : 56 -> 444
~ sub_100003810 -> sub_1000016e8 : 48 -> 56
~ sub_100003840 -> sub_100001720 : 180 -> 128

```
