## SMSPreferences

> `/System/Library/PreferenceBundles/SMSPreferences.bundle/SMSPreferences`

```diff

-1537.100.1.2.1
+1539.100.2.0.0
   __TEXT.__text: 0x2458
   __TEXT.__auth_stubs: 0x460
   __TEXT.__objc_stubs: 0x20

   __DATA_CONST.__auth_got: 0x238
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0xd8
-  __DATA_CONST.__const: 0x3f8
+  __DATA_CONST.__const: 0x400
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftAppleArchive.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B85B1B69-E92B-3FC2-B48C-7FE21ECB8ABB
+  UUID: F312E73B-CC4A-33AD-B021-00F9AC649B09
   Functions: 71
-  Symbols:   96
+  Symbols:   97
   CStrings:  41
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCallKit

```
