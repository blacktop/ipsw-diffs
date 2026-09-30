## ciphermld

> `/usr/libexec/ciphermld`

```diff

-239.80.5.0.0
+270.0.0.0.2
   __TEXT.__text: 0x290
   __TEXT.__auth_stubs: 0x150
   __TEXT.__const: 0x3a

   __DATA_CONST.__auth_got: 0xa8
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xa8
+  __DATA_CONST.__const: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x10
   __DATA.__common: 0x8

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 1
-  Symbols:   46
+  Symbols:   48
   CStrings:  8
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftOSLog

```
