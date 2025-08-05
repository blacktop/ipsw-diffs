## BluetoothSettings

> `/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings`

```diff

-450.40.0.0.0
-  __TEXT.__text: 0x22b04
+450.43.0.0.0
+  __TEXT.__text: 0x22b14
   __TEXT.__auth_stubs: 0xcd0
   __TEXT.__objc_methlist: 0x18ec
   __TEXT.__cstring: 0x1801

   __TEXT.__objc_methtype: 0x106e
   __TEXT.__objc_stubs: 0x4380
   __DATA_CONST.__got: 0x5f8
-  __DATA_CONST.__const: 0x578
+  __DATA_CONST.__const: 0x580
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78

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
-  UUID: 95BE0F1A-C47A-37CD-B837-EC12BEA5C040
+  UUID: 094B8B27-79A8-3590-9278-DA5E1EA8873B
   Functions: 640
-  Symbols:   2298
+  Symbols:   2300
   CStrings:  1715
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_BluetoothSettings
Functions:
~ -[BTSDevicesController fetchDADevices] : 520 -> 536

```
