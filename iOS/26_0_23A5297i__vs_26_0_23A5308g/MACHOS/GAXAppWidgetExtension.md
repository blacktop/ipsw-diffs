## GAXAppWidgetExtension

> `/Applications/GAXApp.app/PlugIns/GAXAppWidgetExtension.appex/GAXAppWidgetExtension`

```diff

-1023.0.0.0.0
+1025.0.0.0.0
   __TEXT.__text: 0x2b30
   __TEXT.__auth_stubs: 0x4d0
   __TEXT.__const: 0x264

   __DATA_CONST.__auth_got: 0x268
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__auth_ptr: 0x180
-  __DATA_CONST.__const: 0x178
+  __DATA_CONST.__const: 0x180
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x120

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AEFE2EFC-D3F9-3A87-B464-3966D0082F91
+  UUID: 4ED8583C-37C7-3FF7-BB0A-AEAAD54F3343
   Functions: 82
-  Symbols:   89
+  Symbols:   90
   CStrings:  25
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private

```
