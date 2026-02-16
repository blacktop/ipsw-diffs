## siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

-4407.0.0.0.0
-  __TEXT.__text: 0xe8
-  __TEXT.__auth_stubs: 0xe0
+4524.1.0.0.0
+  __TEXT.__text: 0xd8
+  __TEXT.__auth_stubs: 0xd0
+  __TEXT.__objc_stubs: 0x40
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__objc_methname: 0x10
   __TEXT.__const: 0x2
+  __TEXT.__objc_methname: 0x10
   __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0x70
   __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0xc0
+  __DATA_CONST.__const: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__linkguard: 0x8
   __DATA.__objc_selrefs: 0x10

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3F953356-C66E-306D-A574-42936A7F3457
+  UUID: 6CCA11F6-B721-3A2C-8463-E7EE5AB8D761
   Functions: 2
-  Symbols:   43
+  Symbols:   45
   CStrings:  2
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCallKit
+ __swift_FORCE_LOAD_$_swiftVideoToolbox
Functions:
~ sub_100001088 -> sub_100001168 : 204 -> 188

```
