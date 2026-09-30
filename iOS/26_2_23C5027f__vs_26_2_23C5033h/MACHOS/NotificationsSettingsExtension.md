## NotificationsSettingsExtension

> `/System/Library/ExtensionKit/Extensions/NotificationsSettingsExtension.appex/NotificationsSettingsExtension`

```diff

-270.2.5.0.0
+270.2.6.0.0
   __TEXT.__text: 0x652c
   __TEXT.__auth_stubs: 0x530
   __TEXT.__cstring: 0x1444

   __DATA_CONST.__auth_got: 0x298
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__auth_ptr: 0x3e8
-  __DATA_CONST.__const: 0x2e8
+  __DATA_CONST.__const: 0x2f8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x1a8
   __DATA.__bss: 0xc08

   - /System/Library/Frameworks/WidgetKit.framework/WidgetKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7C65547C-440A-35F4-BFC5-316E1FCDF414
+  UUID: 4C03D50F-7472-3AD7-9675-91AEFA814D3A
   Functions: 159
-  Symbols:   49
+  Symbols:   51
   CStrings:  93
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCompression

```
