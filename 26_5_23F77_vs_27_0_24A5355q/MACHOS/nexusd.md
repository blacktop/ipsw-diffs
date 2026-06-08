## nexusd

> `/usr/libexec/nexusd`

```diff

-830.22.0.0.0
-  __TEXT.__text: 0x658
-  __TEXT.__auth_stubs: 0x240
+900.25.0.0.0
+  __TEXT.__text: 0x650
+  __TEXT.__auth_stubs: 0x260
   __TEXT.__cstring: 0x1d
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_typeref: 0xa
   __TEXT.__const: 0xa
   __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0x120
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x130
+  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__auth_ptr: 0x10
   __DATA.__data: 0x20
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 6CD43652-FD55-3612-9A59-2D9B3713F3BE
+  UUID: 4654911A-BBA9-35EB-8EE5-B81CC1C01365
   Functions: 7
-  Symbols:   55
+  Symbols:   57
   CStrings:  2
 
Symbols:
+ _swift_release_x20
+ _swift_release_x22
+ _swift_release_x8
- _swift_release
Functions:
~ sub_100000c78 : 1048 -> 1040

```
