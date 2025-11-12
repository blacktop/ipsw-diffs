## VideoSubscriberAccountSettings

> `/System/Library/PreferenceBundles/VideoSubscriberAccountSettings.bundle/VideoSubscriberAccountSettings`

```diff

-593.10.1.0.0
+593.20.1.0.0
   __TEXT.__text: 0x9ff8
   __TEXT.__auth_stubs: 0x6f0
   __TEXT.__objc_stubs: 0x2860

   __DATA_CONST.__auth_got: 0x388
   __DATA_CONST.__got: 0x2f0
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA_CONST.__const: 0x6c0
+  __DATA_CONST.__const: 0x6d0
   __DATA_CONST.__cfstring: 0x740
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x50

   - /System/Library/PrivateFrameworks/VideosUI.framework/VideosUI
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
-  UUID: BB94C588-B147-31CF-824E-5B2A820A74C9
+  UUID: 31D8C693-36C9-3E90-95A8-A46E344BA9BF
   Functions: 282
-  Symbols:   225
+  Symbols:   227
   CStrings:  744
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCompression

```
