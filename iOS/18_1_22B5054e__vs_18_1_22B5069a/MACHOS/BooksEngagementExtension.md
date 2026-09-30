## BooksEngagementExtension

> `/private/var/staged_system_apps/Books.app/PlugIns/BooksEngagementExtension.appex/BooksEngagementExtension`

```diff

-6264.0.0.0.0
+6269.0.0.0.0
   __TEXT.__text: 0x9764
   __TEXT.__auth_stubs: 0x770
   __TEXT.__objc_methlist: 0x44

   __DATA_CONST.__auth_got: 0x3b8
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__auth_ptr: 0x140
-  __DATA_CONST.__const: 0x708
+  __DATA_CONST.__const: 0x710
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftunistd.dylib
   - @rpath/EngagementCollector.framework/EngagementCollector
   Functions: 220
-  Symbols:   91
+  Symbols:   92
   CStrings:  102
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
