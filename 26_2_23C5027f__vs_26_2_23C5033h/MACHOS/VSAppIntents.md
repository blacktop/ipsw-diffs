## VSAppIntents

> `/System/Library/ExtensionKit/Extensions/VSAppIntents.appex/VSAppIntents`

```diff

-593.10.1.0.0
+593.20.1.0.0
   __TEXT.__text: 0x5790
   __TEXT.__auth_stubs: 0x740
   __TEXT.__const: 0x878

   __DATA_CONST.__auth_got: 0x3a0
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__auth_ptr: 0x428
-  __DATA_CONST.__const: 0x168
+  __DATA_CONST.__const: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x48
   __DATA.__data: 0x238

   - /System/Library/PrivateFrameworks/VideoSubscriberAccountUI.framework/VideoSubscriberAccountUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6C7E5F41-A185-3006-9CCC-06AF270FD4F3
+  UUID: E6D755C2-E5D8-35BE-8BDA-489475462271
   Functions: 162
-  Symbols:   85
+  Symbols:   89
   CStrings:  34
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMedia

```
