## MediaPicker

> `/private/var/staged_system_apps/Music.app/PlugIns/MediaPicker.appex/MediaPicker`

```diff

-4023.110.8.0.0
-  __TEXT.__text: 0x299c
-  __TEXT.__auth_stubs: 0x600
+4023.210.9.0.0
+  __TEXT.__text: 0x29c4
+  __TEXT.__auth_stubs: 0x5f0
   __TEXT.__objc_methlist: 0x70
   __TEXT.__const: 0xd4
   __TEXT.__cstring: 0x2a3

   __TEXT.__objc_classname: 0x50
   __TEXT.__objc_methtype: 0x127
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0xe4
-  __DATA_CONST.__auth_got: 0x300
+  __TEXT.__unwind_info: 0xe0
+  __DATA_CONST.__auth_got: 0x2f8
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__const: 0x148
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftMetalKit.dylib
   - /usr/lib/swift/libswiftModelIO.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - @rpath/MusicApplication.framework/MusicApplication
   Functions: 43
-  Symbols:   116
+  Symbols:   117
   CStrings:  106
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftMapKit
CStrings:
+ "A non-playlist/album was picked while picksSingleCollectionEntity was true."
- "A non-playist/album was picked while picksSingleCollectionEntity was true."

```
