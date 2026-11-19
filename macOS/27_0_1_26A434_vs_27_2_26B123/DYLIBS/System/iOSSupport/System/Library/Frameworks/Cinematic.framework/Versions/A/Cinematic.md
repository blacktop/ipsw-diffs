## Cinematic

> `/System/iOSSupport/System/Library/Frameworks/Cinematic.framework/Versions/A/Cinematic`

```diff

-560.21.2.0.0
-  __TEXT.__text: 0x20d70
+560.40.5.0.0
+  __TEXT.__text: 0x21000
   __TEXT.__objc_methlist: 0x1194
-  __TEXT.__cstring: 0x5c1
+  __TEXT.__cstring: 0x5f1
   __TEXT.__const: 0xb08
-  __TEXT.__oslogstring: 0x1390
+  __TEXT.__oslogstring: 0x1447
   __TEXT.__gcc_except_tab: 0x9a0
   __TEXT.__constg_swiftt: 0x644
   __TEXT.__swift5_typeref: 0x3c2

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xab8
+  __DATA_CONST.__const: 0xae0
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfd0
+  __DATA_CONST.__objc_selrefs: 0xfc0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x68
-  __DATA_CONST.__got: 0x470
+  __DATA_CONST.__got: 0x468
   __AUTH_CONST.__const: 0x988
-  __AUTH_CONST.__cfstring: 0x1e0
+  __AUTH_CONST.__cfstring: 0x240
   __AUTH_CONST.__objc_const: 0x26f0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x120

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1020
-  Symbols:   1721
-  CStrings:  161
+  Functions: 1023
+  Symbols:   1719
+  CStrings:  168
 
Symbols:
+ -[CNAssetInfo initWithTracks:cinematicAssetInfo:]
+ ___block_descriptor_72_e8_32s40bs48r_e5_v8?0lr48l8s40l8s32l8
+ _objc_msgSend$initWithTracks:cinematicAssetInfo:
+ _objc_msgSend$loadWithAsset:changesDictionary:completion:
+ _objc_msgSend$preprocessed
- -[CNAssetInfo initWithTracks:]
- _OBJC_CLASS_$_PTCinematographyScriptOptions
- __62-[CNAssetInfo downloadResourcesWithTimeout:completionHandler:]_block_invoke_2
- _objc_msgSend$initWithTracks:
- _objc_msgSend$loadWithAsset:changesDictionary:disparityProvider:completion:
- _objc_msgSend$loadWithAsset:changesDictionary:options:completion:
- _objc_msgSend$setDisparityPrecompute:
CStrings:
+ "Calling download on asset that does not need downloading. Returning self"
+ "Calling download on asset that is not supported (%@)."
+ "DisparitySettings returned nil"
+ "_loadFromAsset: Error %@"
+ "code: %li"
+ "unsupported asset"
+ "unsupported device"
```
