## Cinematic

> `/System/Library/Frameworks/Cinematic.framework/Versions/A/Cinematic`

```diff

-560.21.2.0.0
-  __TEXT.__text: 0x2189c
+560.40.3.0.0
+  __TEXT.__text: 0x21b70
   __TEXT.__objc_methlist: 0x1194
-  __TEXT.__cstring: 0x5a1
+  __TEXT.__cstring: 0x5d1
   __TEXT.__const: 0xb08
-  __TEXT.__oslogstring: 0x1390
+  __TEXT.__oslogstring: 0x1447
   __TEXT.__gcc_except_tab: 0x9a0
   __TEXT.__constg_swiftt: 0x644
   __TEXT.__swift5_typeref: 0x3c2

   __TEXT.__swift_as_cont: 0x80
   __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xf08
+  __TEXT.__unwind_info: 0xf10
   __TEXT.__eh_frame: 0x918
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x68
   __DATA_CONST.__got: 0x470
-  __AUTH_CONST.__const: 0x14a8
-  __AUTH_CONST.__cfstring: 0x1c0
+  __AUTH_CONST.__const: 0x14d8
+  __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0x26f0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x120

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1049
-  Symbols:   1710
-  CStrings:  160
+  Functions: 1052
+  Symbols:   1711
+  CStrings:  167
 
Symbols:
+ -[CNAssetInfo initWithTracks:cinematicAssetInfo:]
+ ___block_descriptor_72_e8_32s40bs48r_e5_v8?0l
+ _objc_msgSend$initWithTracks:cinematicAssetInfo:
+ _objc_msgSend$preprocessed
- -[CNAssetInfo initWithTracks:]
- __62-[CNAssetInfo downloadResourcesWithTimeout:completionHandler:]_block_invoke_2
- _objc_msgSend$initWithTracks:
CStrings:
+ "Calling download on asset that does not need downloading. Returning self"
+ "Calling download on asset that is not supported (%@)."
+ "DisparitySettings returned nil"
+ "_loadFromAsset: Error %@"
+ "code: %li"
+ "unsupported asset"
+ "unsupported device"
```
