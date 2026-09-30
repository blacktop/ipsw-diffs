## BiometricKitUI

> `/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`

```diff

 684.100.0.0.0
-  __TEXT.__text: 0x70534
-  __TEXT.__objc_methlist: 0x72c0
+  __TEXT.__text: 0x70b1c
+  __TEXT.__objc_methlist: 0x72e0
   __TEXT.__const: 0xd44
   __TEXT.__gcc_except_tab: 0xde4
-  __TEXT.__cstring: 0x2fd6
-  __TEXT.__oslogstring: 0x6853
+  __TEXT.__cstring: 0x3026
+  __TEXT.__oslogstring: 0x6963
   __TEXT.__dlopen_cstrs: 0x292
   __TEXT.__swift5_typeref: 0x2c2
   __TEXT.__swift5_capture: 0x114

   __TEXT.__swift5_proto: 0x20
   __TEXT.__swift5_types: 0x34
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1ac0
+  __TEXT.__unwind_info: 0x1ac8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x48d8
+  __DATA_CONST.__objc_selrefs: 0x4918
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0x188
   __DATA_CONST.__got: 0x880
   __AUTH_CONST.__const: 0xc50
-  __AUTH_CONST.__cfstring: 0x33a0
+  __AUTH_CONST.__cfstring: 0x3400
   __AUTH_CONST.__objc_const: 0x10720
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0xc0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2868
-  Symbols:   6374
-  CStrings:  1068
+  Functions: 2875
+  Symbols:   6386
+  CStrings:  1078
 
Symbols:
+ -[BKUIPearlVideoCaptureSession configureFaceIDCoexistenceForCamera:]
+ -[BKUIPearlVideoCaptureSession enableFaceIDCoexistenceForCamera:]
+ -[BKUIPearlVideoCaptureSession findCoexistenceSupportedFormatForCamera:]
+ _objc_msgSend$configureFaceIDCoexistenceForCamera:
+ _objc_msgSend$enableFaceIDCoexistenceForCamera:
+ _objc_msgSend$excessiveLight
+ _objc_msgSend$faceIDCoexistenceSupported
+ _objc_msgSend$findCoexistenceSupportedFormatForCamera:
+ _objc_msgSend$inadequateLight
+ _objc_msgSend$isFaceIDCoexistenceSupported
+ _objc_msgSend$setActiveFormatForCamera:format:
+ _objc_msgSend$setFaceIDCoexistenceEnabled:
CStrings:
+ "Coexistence: Cannot enable coexistence for nil camera"
+ "Coexistence: Cannot find format for nil camera"
+ "Coexistence: Enabling for: %@"
+ "Coexistence: Failed to find a supported format"
+ "Coexistence: Failed to lock camera for configuration: %@"
+ "Coexistence: Unsupported"
+ "Pearl-rgbCamera"
+ "Too little light"
+ "Too much light from backlit Sun"
+ "jindo_coexistence"
```
