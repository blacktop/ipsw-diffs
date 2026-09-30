## Cinematic

> `/System/Library/Frameworks/Cinematic.framework/Cinematic`

```diff

-484.0.0.0.0
-  __TEXT.__text: 0x12b28
-  __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_methlist: 0xdc4
+488.0.0.0.1
+  __TEXT.__text: 0x12c74
+  __TEXT.__auth_stubs: 0x920
+  __TEXT.__objc_methlist: 0xdcc
   __TEXT.__const: 0x960
-  __TEXT.__cstring: 0x617
-  __TEXT.__oslogstring: 0x6c6
+  __TEXT.__cstring: 0x637
+  __TEXT.__oslogstring: 0x6e2
   __TEXT.__gcc_except_tab: 0x25c
   __TEXT.__constg_swiftt: 0x5b0
   __TEXT.__swift5_typeref: 0x332

   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x7e0
+  __TEXT.__unwind_info: 0x7f0
   __TEXT.__eh_frame: 0x448
   __TEXT.__objc_classname: 0x18a
-  __TEXT.__objc_methname: 0x2777
+  __TEXT.__objc_methname: 0x2781
   __TEXT.__objc_methtype: 0x81e
-  __TEXT.__objc_stubs: 0x1dc0
+  __TEXT.__objc_stubs: 0x1de0
   __DATA_CONST.__got: 0x288
   __DATA_CONST.__const: 0x6e8
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xae8
+  __DATA_CONST.__objc_selrefs: 0xaf0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x498
-  __AUTH_CONST.__const: 0x6d0
-  __AUTH_CONST.__cfstring: 0x180
-  __AUTH_CONST.__objc_const: 0x1b10
+  __AUTH_CONST.__auth_got: 0x4a0
+  __AUTH_CONST.__const: 0x6f0
+  __AUTH_CONST.__cfstring: 0x1a0
+  __AUTH_CONST.__objc_const: 0x1b28
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_intobj: 0xa8

   __AUTH.__data: 0x840
   __DATA.__objc_ivar: 0x6c
   __DATA.__data: 0x2c8
-  __DATA.__bss: 0x730
+  __DATA.__bss: 0x740
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/Portrait.framework/Portrait
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7417CAA6-3D0D-3B34-B82D-3482A0D2B199
-  Functions: 724
-  Symbols:   1590
-  CStrings:  643
+  UUID: 4099CDF5-0C55-3820-BC89-01364A3AE55B
+  Functions: 729
+  Symbols:   1604
+  CStrings:  647
 
Symbols:
+ +[CNAssetSpatialAudioInfo isSupported]
+ +[CNAssetSpatialAudioInfo isSupported].cold.1
+ +[CNAssetSpatialAudioInfo loadFromAsset:completionHandler:].cold.2
+ _MGCopyAnswer
+ __OBJC_$_CLASS_PROP_LIST_CNAssetSpatialAudioInfo
+ ___38+[CNAssetSpatialAudioInfo isSupported]_block_invoke
+ ___59+[CNAssetSpatialAudioInfo loadFromAsset:completionHandler:]_block_invoke.11
+ ___59+[CNAssetSpatialAudioInfo loadFromAsset:completionHandler:]_block_invoke.11.cold.1
+ ___59+[CNAssetSpatialAudioInfo loadFromAsset:completionHandler:]_block_invoke.11.cold.2
+ ___block_literal_global.54
+ _isSupported.audioMixIsSupported
+ _isSupported.checkDeviceSupportsOnce
+ _objc_msgSend$boolValue
- ___59+[CNAssetSpatialAudioInfo loadFromAsset:completionHandler:]_block_invoke.6
- ___59+[CNAssetSpatialAudioInfo loadFromAsset:completionHandler:]_block_invoke.6.cold.1
- ___59+[CNAssetSpatialAudioInfo loadFromAsset:completionHandler:]_block_invoke.6.cold.2
CStrings:
+ "DeviceSupportsAudioMix"
+ "Error: unsupported platform"
+ "boolValue"

```
