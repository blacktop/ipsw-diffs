## audioanalyticsd

> `/usr/libexec/audioanalyticsd`

```diff

-223.103.0.0.0
+223.107.0.0.0
   __TEXT.__text: 0x348c8
   __TEXT.__auth_stubs: 0x14a0
   __TEXT.__objc_methlist: 0xbc

   __TEXT.__eh_frame: 0x598
   __DATA_CONST.__auth_got: 0xa50
   __DATA_CONST.__got: 0x400
-  __DATA_CONST.__auth_ptr: 0x2c0
-  __DATA_CONST.__const: 0x11a8
+  __DATA_CONST.__auth_ptr: 0x2d0
+  __DATA_CONST.__const: 0x11b0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 707
-  Symbols:   512
+  Symbols:   513
   CStrings:  119
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers

```
