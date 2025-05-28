## MediaRemoteUIService

> `/Applications/MediaRemoteUIService.app/MediaRemoteUIService`

```diff

-4023.110.7.0.0
+4023.210.1.0.0
   __TEXT.__text: 0x89a0
   __TEXT.__auth_stubs: 0xbf0
   __TEXT.__objc_stubs: 0xe0

   __DATA_CONST.__auth_got: 0x600
   __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x658
+  __DATA_CONST.__const: 0x668
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x68

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 220
-  Symbols:   368
+  Symbols:   370
   CStrings:  353
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCoreMedia

```
