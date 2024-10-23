## ContactsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/ContactsAppIntentsExtension.appex/ContactsAppIntentsExtension`

```diff

-1274.1.0.0.0
+1380.0.0.0.0
   __TEXT.__text: 0x1f8
   __TEXT.__auth_stubs: 0x80
   __TEXT.__objc_stubs: 0x20

   __DATA_CONST.__auth_got: 0x48
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0xd8
+  __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftFileProvider.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 9
-  Symbols:   38
+  Symbols:   40
   CStrings:  3
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreMIDI

```
