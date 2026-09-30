## Safety

> `/System/Library/Health/FeedItemPlugins/Safety.healthplugin/Safety`

```diff

-5200.1.9.1.2
+5200.1.15.1.2
   __TEXT.__text: 0x8204c
   __TEXT.__auth_stubs: 0x27d0
   __TEXT.__objc_methlist: 0x58c

   __TEXT.__objc_methname: 0x23ee
   __TEXT.__objc_methtype: 0x444
   __DATA_CONST.__got: 0x9b8
-  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__const: 0x128
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_catlist2: 0x28
   __DATA_CONST.__objc_protolist: 0xd0

   __DATA_CONST.__objc_selrefs: 0x9f8
   __DATA_CONST.__objc_protorefs: 0x68
   __AUTH_CONST.__auth_got: 0x13e8
-  __AUTH_CONST.__auth_ptr: 0xb08
+  __AUTH_CONST.__auth_ptr: 0xae8
   __AUTH_CONST.__const: 0x2148
   __AUTH_CONST.__objc_const: 0x3508
   __AUTH.__objc_data: 0x17c0

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 2203
-  Symbols:   278
+  Symbols:   279
   CStrings:  997
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
