## DocumentCamera

> `/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`

```diff

-211.40.1.0.0
-  __TEXT.__text: 0xa3ccc
-  __TEXT.__objc_methlist: 0x97d8
-  __TEXT.__const: 0x1b74
-  __TEXT.__gcc_except_tab: 0x9578
+211.40.2.0.0
+  __TEXT.__text: 0xa43e8
+  __TEXT.__objc_methlist: 0x9838
+  __TEXT.__const: 0x1b84
+  __TEXT.__gcc_except_tab: 0x963c
   __TEXT.__cstring: 0x3cb0
-  __TEXT.__oslogstring: 0x1e01
+  __TEXT.__oslogstring: 0x1e81
   __TEXT.__ustring: 0x3a0
   __TEXT.__dlopen_cstrs: 0x2f6
   __TEXT.__constg_swiftt: 0xf04

   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_capture: 0x15c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x38e8
+  __TEXT.__unwind_info: 0x3930
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x62d8
+  __DATA_CONST.__objc_selrefs: 0x6310
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x278

   __DATA_CONST.__got: 0xaa8
   __AUTH_CONST.__const: 0x1338
   __AUTH_CONST.__cfstring: 0x3b20
-  __AUTH_CONST.__objc_const: 0x15238
+  __AUTH_CONST.__objc_const: 0x15280
   __AUTH_CONST.__objc_doubleobj: 0x100
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_arrayobj: 0x60

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4229
-  Symbols:   6479
-  CStrings:  788
+  Functions: 4236
+  Symbols:   6491
+  CStrings:  790
 
Symbols:
+ +[ICDocCamViewController documentInfoForSingleImageDelivery:]
+ +[ICDocCamViewController isQuadPlausibleForEmbeddedCapture:]
+ +[ICDocCamViewController quadByExtruding:byFraction:withinBounds:wasConstrained:]
+ -[ICDocCamImageQuad containsAngleOutOfValidThreshold:]
+ -[ICDocCamViewController notifyDelegateExtrusionIsConstrained]
+ -[VNDocumentCameraViewController_InProcess documentCameraControllerExtrusionIsConstrained:]
+ GCC_except_table232
+ GCC_except_table233
+ GCC_except_table234
+ GCC_except_table235
+ GCC_except_table242
+ GCC_except_table251
+ GCC_except_table255
+ GCC_except_table258
+ GCC_except_table268
+ GCC_except_table272
+ GCC_except_table274
+ GCC_except_table278
+ GCC_except_table282
+ GCC_except_table285
+ GCC_except_table295
+ GCC_except_table296
+ GCC_except_table298
+ GCC_except_table304
+ GCC_except_table313
+ GCC_except_table328
+ GCC_except_table331
+ GCC_except_table357
+ GCC_except_table358
+ GCC_except_table360
+ GCC_except_table361
+ GCC_except_table364
+ ___62-[ICDocCamViewController notifyDelegateExtrusionIsConstrained]_block_invoke
- GCC_except_table237
- GCC_except_table238
- GCC_except_table239
- GCC_except_table240
- GCC_except_table257
- GCC_except_table261
- GCC_except_table263
- GCC_except_table270
- GCC_except_table273
- GCC_except_table277
- GCC_except_table283
- GCC_except_table284
- GCC_except_table287
- GCC_except_table290
- GCC_except_table300
- GCC_except_table301
- GCC_except_table303
- GCC_except_table309
- GCC_except_table318
- GCC_except_table333
- GCC_except_table336
CStrings:
+ "Requested quad extrusion of %f does not fit within the image"
+ "The detected quad is not plausibly a document in perspective: %@"
```
