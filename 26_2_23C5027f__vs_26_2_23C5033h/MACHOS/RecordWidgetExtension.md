## RecordWidgetExtension

> `/private/var/staged_system_apps/VoiceMemos.app/PlugIns/RecordWidgetExtension.appex/RecordWidgetExtension`

```diff

-1355.0.0.0.0
+1356.0.0.0.0
   __TEXT.__text: 0x2d38
   __TEXT.__auth_stubs: 0x560
   __TEXT.__objc_stubs: 0x100

   __DATA_CONST.__auth_got: 0x2b8
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__auth_ptr: 0x278
-  __DATA_CONST.__const: 0x210
+  __DATA_CONST.__const: 0x220
   __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

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
-  UUID: B09E86E5-7F5B-3A85-AD35-E9B24C52C8A1
+  UUID: BF4D4EC8-A2AF-3329-A576-72E48651A8E3
   Functions: 96
-  Symbols:   85
+  Symbols:   87
   CStrings:  53
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCompression

```
