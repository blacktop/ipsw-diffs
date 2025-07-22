## DPSubmissionService

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/XPCServices/DPSubmissionService.xpc/DPSubmissionService`

```diff

-684.0.20.0.2
-  __TEXT.__text: 0x4e4fc
-  __TEXT.__auth_stubs: 0x1100
+684.0.23.0.2
+  __TEXT.__text: 0x4e3d0
+  __TEXT.__auth_stubs: 0x10b0
   __TEXT.__objc_stubs: 0x2fe0
   __TEXT.__objc_methlist: 0x1344
   __TEXT.__const: 0x4078
   __TEXT.__cstring: 0x2b70
-  __TEXT.__objc_methname: 0x3c10
+  __TEXT.__objc_methname: 0x3c1f
   __TEXT.__objc_classname: 0x31a
   __TEXT.__objc_methtype: 0xa1a
   __TEXT.__oslogstring: 0x127e

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__unwind_info: 0x1c78
   __TEXT.__eh_frame: 0x41a0
-  __DATA_CONST.__auth_got: 0x890
-  __DATA_CONST.__got: 0x548
+  __DATA_CONST.__auth_got: 0x868
+  __DATA_CONST.__got: 0x550
   __DATA_CONST.__auth_ptr: 0x2a8
-  __DATA_CONST.__const: 0x2f98
+  __DATA_CONST.__const: 0x2f78
   __DATA_CONST.__cfstring: 0x1720
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8

   - /System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A52ACB38-43A9-3AA1-BC57-04254816EBA9
+  UUID: 6A5FF693-FC9F-37C1-9D84-C1A5D29B5EEC
   Functions: 2305
   Symbols:   360
   CStrings:  1326
Symbols:
+ _kDPMetadataDediscoTaskConfigVDAFConfig
+ _kDPMetadataVDAFConfigPreambleBlockSize
+ _kDPMetadataVDAFConfigPreambleNumKeptBlocks
+ _objc_retain_x5
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftCoreAudio
- __swift_FORCE_LOAD_$_swiftCoreMIDI
- __swift_FORCE_LOAD_$_swiftCoreMedia
Functions:
~ sub_100004fcc -> sub_100004eac : 1964 -> 2096
~ sub_10001506c -> sub_100014fd0 : 264 -> 224
~ sub_10001c298 -> sub_10001c1d4 : 1192 -> 800
CStrings:
+ "@44@0:8I16I20I24@28^@36"
+ "encodedPreambleField32HmacSha256Aes128VDAFConfigWithLength:blockSize:numKeptBlocks:encodedDPConfig:error:"
- "@48@0:8@16@24q32^@40"
- "encodedPreambleField32HmacSha256Aes128VDAFConfigWithMetaData:encodedDPConfig:length:error:"

```
