## PFLCSLAppStore2

> `/System/Library/ExtensionKit/Extensions/PFLCSLAppStore2.appex/PFLCSLAppStore2`

```diff

-1.4.8.0.0
+1.4.9.0.0
   __TEXT.__text: 0x228fc
   __TEXT.__auth_stubs: 0x830
   __TEXT.__objc_stubs: 0x1a60

   __DATA_CONST.__auth_got: 0x428
   __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__auth_ptr: 0xf8
-  __DATA_CONST.__const: 0x118
+  __DATA_CONST.__const: 0x130
   __DATA_CONST.__cfstring: 0x1860
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x10

   - /System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib

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
-  UUID: 64A71F0B-9A61-30F5-9654-FF0EE49A934C
+  UUID: 86167602-F8B4-322C-A689-195F26061E50
   Functions: 211
-  Symbols:   515
+  Symbols:   518
   CStrings:  782
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMedia

```
