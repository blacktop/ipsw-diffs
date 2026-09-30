## SleepWidgetExtension

> `/Applications/SleepWidgetContainer.app/PlugIns/SleepWidgetExtension.appex/SleepWidgetExtension`

```diff

-5200.1.9.1.2
+5200.1.15.1.2
   __TEXT.__text: 0x4e4
   __TEXT.__auth_stubs: 0xd0
   __TEXT.__swift5_entry: 0x8

   __DATA_CONST.__auth_got: 0x68
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x50
-  __DATA_CONST.__const: 0x160
+  __DATA_CONST.__const: 0x168
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 13
-  Symbols:   54
+  Symbols:   55
   CStrings:  1
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
