## PodcastsWidget

> `/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsWidget.appex/PodcastsWidget`

```diff

-4025.110.94.1.0
+4025.100.100.0.0
   __TEXT.__text: 0x2b74
   __TEXT.__auth_stubs: 0x370
   __TEXT.__objc_stubs: 0xd20

   __DATA_CONST.__auth_got: 0x1c8
   __DATA_CONST.__got: 0x128
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x1d8
+  __DATA_CONST.__const: 0x1e0
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x10

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - @rpath/PodcastsActions.framework/PodcastsActions
   - @rpath/ShelfKit.framework/ShelfKit
-  UUID: A3133AF6-7558-3052-AD62-EDF5D2A972F0
+  UUID: DF8AC22E-B416-3A2E-AC34-7CD20D681F81
   Functions: 63
-  Symbols:   128
+  Symbols:   129
   CStrings:  160
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private

```
