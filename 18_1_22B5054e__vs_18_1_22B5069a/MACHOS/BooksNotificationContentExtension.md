## BooksNotificationContentExtension

> `/private/var/staged_system_apps/Books.app/PlugIns/BooksNotificationContentExtension.appex/BooksNotificationContentExtension`

```diff

-6264.0.0.0.0
+6269.0.0.0.0
   __TEXT.__text: 0x2de8
   __TEXT.__auth_stubs: 0x420
   __TEXT.__objc_stubs: 0xda0

   __DATA_CONST.__auth_got: 0x218
   __DATA_CONST.__got: 0x168
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x3b8
+  __DATA_CONST.__const: 0x3c0
   __DATA_CONST.__cfstring: 0x340
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - @rpath/JSApp.framework/JSApp
   - @rpath/TemplateUI.framework/TemplateUI
   Functions: 66
-  Symbols:   172
+  Symbols:   173
   CStrings:  259
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
