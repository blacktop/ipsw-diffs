## FreeformWidgetKitExtension

> `/private/var/staged_system_apps/Freeform.app/PlugIns/FreeformWidgetKitExtension.appex/FreeformWidgetKitExtension`

```diff

-630.40.7.0.0
+630.60.4.0.3
   __TEXT.__text: 0x1aa50
   __TEXT.__auth_stubs: 0xa20
   __TEXT.__objc_stubs: 0xe0

   __DATA_CONST.__auth_got: 0x518
   __DATA_CONST.__got: 0x240
   __DATA_CONST.__auth_ptr: 0x7b8
-  __DATA_CONST.__const: 0xb60
+  __DATA_CONST.__const: 0xb70
   __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
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
-  UUID: 98B92DFF-9EFE-3FC1-880C-F98C4DBD1025
+  UUID: A6CEBCD0-ADEA-3B61-9B10-1C773F70F534
   Functions: 873
-  Symbols:   112
+  Symbols:   114
   CStrings:  151
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCallKit
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private

```
