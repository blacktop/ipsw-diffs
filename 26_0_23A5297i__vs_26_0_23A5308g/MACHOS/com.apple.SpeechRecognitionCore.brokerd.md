## com.apple.SpeechRecognitionCore.brokerd

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/com.apple.SpeechRecognitionCore.brokerd`

```diff

-6.3.62.0.0
-  __TEXT.__text: 0x10e38
+6.3.64.0.0
+  __TEXT.__text: 0x10eb0
   __TEXT.__auth_stubs: 0xd40
   __TEXT.__objc_stubs: 0x13e0
   __TEXT.__init_offsets: 0x4

   __DATA_CONST.__auth_got: 0x6b8
   __DATA_CONST.__got: 0x218
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x918
+  __DATA_CONST.__const: 0x920
   __DATA_CONST.__cfstring: 0xf60
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C6D9846A-AD04-3CB3-A397-DC13A2C4BB53
+  UUID: 09CF723E-92F0-3B6A-90F9-770DADEBFA0A
   Functions: 253
-  Symbols:   303
+  Symbols:   304
   CStrings:  669
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
Functions:
~ __ZN16RDLanguageAssets33CopyInstalledAssetPathForLanguageEPK10__CFString : 264 -> 324
~ __ZN16RDLanguageAssets43CopyInstalledAssetSupportedTasksForLanguageEPK10__CFString : 336 -> 396

```
