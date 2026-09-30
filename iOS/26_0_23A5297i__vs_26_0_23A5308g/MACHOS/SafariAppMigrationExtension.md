## SafariAppMigrationExtension

> `/private/var/staged_system_apps/MobileSafari.app/Extensions/SafariAppMigrationExtension.appex/SafariAppMigrationExtension`

```diff

-7622.1.19.10.4
+7622.1.21.10.3
   __TEXT.__text: 0x13698
   __TEXT.__auth_stubs: 0x9f0
   __TEXT.__objc_stubs: 0x20

   __DATA_CONST.__auth_got: 0x500
   __DATA_CONST.__got: 0x188
   __DATA_CONST.__auth_ptr: 0x308
-  __DATA_CONST.__const: 0xd98
+  __DATA_CONST.__const: 0xda0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D20937E3-9F31-37CE-B8F9-CE3475193C3F
+  UUID: 1BAD48B6-C1A8-3CEF-B6CE-654B9219ED85
   Functions: 426
-  Symbols:   157
+  Symbols:   158
   CStrings:  150
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private

```
