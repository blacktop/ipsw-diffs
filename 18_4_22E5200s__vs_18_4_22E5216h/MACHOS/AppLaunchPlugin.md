## AppLaunchPlugin

> `/System/Library/Assistant/FlowDelegatePlugins/AppLaunchPlugin.bundle/AppLaunchPlugin`

```diff

-3404.8.1.0.0
+3404.14.1.0.0
   __TEXT.__text: 0x1dd4
   __TEXT.__auth_stubs: 0x450
   __TEXT.__const: 0x9a

   __DATA_CONST.__auth_got: 0x228
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__const: 0x128
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 44
-  Symbols:   79
+  Symbols:   80
   CStrings:  13
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAppleArchive

```
