## Fitness

> `/System/Library/PrivateFrameworks/Fitness.framework/Fitness`

```diff

-2026.2.3.0.0
+2026.2.5.0.0
   __TEXT.__text: 0x4afdc
   __TEXT.__auth_stubs: 0x14f0
-  __TEXT.__objc_methlist: 0x2a3c
+  __TEXT.__objc_methlist: 0x2a4c
   __TEXT.__const: 0x1ae0
   __TEXT.__oslogstring: 0x27e6
   __TEXT.__cstring: 0x5ec3

   __TEXT.__unwind_info: 0x14f8
   __TEXT.__eh_frame: 0x218
   __TEXT.__objc_classname: 0x503
-  __TEXT.__objc_methname: 0x9365
+  __TEXT.__objc_methname: 0x9384
   __TEXT.__objc_methtype: 0xfce
   __TEXT.__objc_stubs: 0x6080
   __DATA_CONST.__got: 0x6a8
-  __DATA_CONST.__const: 0x1290
+  __DATA_CONST.__const: 0x12b8
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2288
+  __DATA_CONST.__objc_selrefs: 0x2290
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x1100
   __AUTH_CONST.__auth_got: 0xa88
   __AUTH_CONST.__const: 0x24b0
   __AUTH_CONST.__cfstring: 0x5120
-  __AUTH_CONST.__objc_const: 0x45b8
+  __AUTH_CONST.__objc_const: 0x45c0
   __AUTH_CONST.__objc_intobj: 0xdb0
   __AUTH_CONST.__objc_arrayobj: 0x9a8
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 707203B1-8278-3BAC-B7B5-A2D2CAD6278D
+  UUID: 03CC3D9F-BAE3-3365-BB23-1F62EB4C0FB5
   Functions: 1917
-  Symbols:   4611
-  CStrings:  3317
+  Symbols:   4621
+  CStrings:  3318
 
Symbols:
+ ___38-[FIUnitManager _updatePreferredUnits]_block_invoke.360
+ ___52-[FIBluetoothSensorLookup _queueCheckForPeripherals]_block_invoke.329
+ ___68+[FIAppStoreAvailability _isSupportedDeviceAvailableWithCompletion:]_block_invoke.347
+ ___68+[FIAppStoreAvailability _isSupportedDeviceAvailableWithCompletion:]_block_invoke.347.cold.1
+ ___68+[FIAppStoreAvailability _isSupportedDeviceAvailableWithCompletion:]_block_invoke.349
+ ___82-[FIMindfulnessSessionDataProvider _createMindfulnessSessionsQueryWithRetryCount:]_block_invoke.314
+ ___block_literal_global.313
+ ___block_literal_global.315
+ ___block_literal_global.321
+ ___block_literal_global.335
+ ___block_literal_global.337
+ ___block_literal_global.339
+ ___block_literal_global.341
+ ___block_literal_global.352
+ ___block_literal_global.363
+ ___block_literal_global.366
+ ___block_literal_global.368
+ ___block_literal_global.373
+ ___block_literal_global.378
+ ___block_literal_global.399
+ ___block_literal_global.402
+ ___block_literal_global.405
+ ___block_literal_global.407
+ ___block_literal_global.428
+ ___block_literal_global.432
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAVFoundation_$_Fitness
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_Fitness
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_Fitness
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_Fitness
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftCoreMedia_$_Fitness
- ___38-[FIUnitManager _updatePreferredUnits]_block_invoke.351
- ___52-[FIBluetoothSensorLookup _queueCheckForPeripherals]_block_invoke.320
- ___68+[FIAppStoreAvailability _isSupportedDeviceAvailableWithCompletion:]_block_invoke.338
- ___68+[FIAppStoreAvailability _isSupportedDeviceAvailableWithCompletion:]_block_invoke.338.cold.1
- ___68+[FIAppStoreAvailability _isSupportedDeviceAvailableWithCompletion:]_block_invoke.340
- ___82-[FIMindfulnessSessionDataProvider _createMindfulnessSessionsQueryWithRetryCount:]_block_invoke.305
- ___block_literal_global.297
- ___block_literal_global.304
- ___block_literal_global.312
- ___block_literal_global.323
- ___block_literal_global.326
- ___block_literal_global.328
- ___block_literal_global.330
- ___block_literal_global.334
- ___block_literal_global.354
- ___block_literal_global.357
- ___block_literal_global.359
- ___block_literal_global.364
- ___block_literal_global.369
- ___block_literal_global.390
- ___block_literal_global.393
- ___block_literal_global.396
- ___block_literal_global.398
- ___block_literal_global.419
- ___block_literal_global.423
CStrings:
+ "applicationsDidUpdateMetadata:"

```
