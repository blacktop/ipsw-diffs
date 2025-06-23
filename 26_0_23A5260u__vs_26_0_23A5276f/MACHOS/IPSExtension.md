## IPSExtension

> `/System/Library/PrivateFrameworks/OSAnalytics.framework/PlugIns/IPSExtension.appex/IPSExtension`

```diff

-912.0.0.0.0
+917.0.0.0.0
   __TEXT.__text: 0x1500
   __TEXT.__auth_stubs: 0x450
   __TEXT.__objc_stubs: 0x1c0

   __DATA_CONST.__auth_got: 0x230
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0x80
-  __DATA_CONST.__const: 0x1a8
+  __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10

   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftMetalKit.dylib
+  - /usr/lib/swift/libswiftModelIO.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8D839C84-4FFF-3A30-8BCC-0CAA808DC7D6
+  UUID: 4AAD0884-59A3-34F3-AFBC-BE571170A793
   Functions: 39
-  Symbols:   91
+  Symbols:   90
   CStrings:  74
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftMetalKit
+ __swift_FORCE_LOAD_$_swiftModelIO
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3

```
