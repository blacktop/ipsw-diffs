## PassKitWrapperXPCServiceUI

> `filesystem/System/Library/Frameworks/PassKit.framework/XPCServices/PassKitWrapperXPCServiceUI.xpc/PassKitWrapperXPCServiceUI`

```diff

-1642.6.1.0.0
+1642.6.3.0.0
   __TEXT.__text: 0x6bf0
   __TEXT.__auth_stubs: 0xa40
   __TEXT.__objc_stubs: 0x5c0

   __DATA_CONST.__auth_got: 0x528
   __DATA_CONST.__got: 0x110
   __DATA_CONST.__auth_ptr: 0x158
-  __DATA_CONST.__const: 0x340
+  __DATA_CONST.__const: 0x348
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftAppleArchive.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EE2990C5-B30A-3A26-B34D-E3DA64F6AE42
+  UUID: 2B440C36-AFAE-3B87-81F7-ED284D85E48C
   Functions: 144
-  Symbols:   151
+  Symbols:   152
   CStrings:  136
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCallKit

```
