## DocumentCamera

> `/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`

```diff

-142.0.0.0.0
-  __TEXT.__text: 0x89e88
+145.0.0.0.0
+  __TEXT.__text: 0x8a174
   __TEXT.__auth_stubs: 0x1480
-  __TEXT.__objc_methlist: 0x7e94
+  __TEXT.__objc_methlist: 0x7ea4
   __TEXT.__const: 0x5c8
-  __TEXT.__gcc_except_tab: 0x81f8
-  __TEXT.__cstring: 0x3531
+  __TEXT.__gcc_except_tab: 0x827c
+  __TEXT.__cstring: 0x3571
   __TEXT.__oslogstring: 0x1a16
   __TEXT.__ustring: 0x3a8
   __TEXT.__dlopen_cstrs: 0x2f6
   __TEXT.__unwind_info: 0x28dc
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x1067
-  __TEXT.__objc_methname: 0x1acdf
+  __TEXT.__objc_methname: 0x1ad01
   __TEXT.__objc_methtype: 0x4057
   __TEXT.__objc_stubs: 0x129e0
   __DATA_CONST.__got: 0x490

   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x12b78
-  __DATA_CONST.__objc_selrefs: 0x58b8
+  __DATA_CONST.__objc_selrefs: 0x58c0
   __DATA_CONST.__objc_arraydata: 0x178
-  __AUTH_CONST.__cfstring: 0x3840
+  __AUTH_CONST.__cfstring: 0x38a0
+  __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x140
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_const: 0x0

   __DATA.__objc_ivar: 0x9ec
   __DATA.__data: 0xfa8
   __DATA.__bss: 0x238
-  __DATA_DIRTY.__const: 0x418
+  __DATA_DIRTY.__const: 0x3b8
   __DATA_DIRTY.__objc_const: 0x26f0
   __DATA_DIRTY.__objc_data: 0x1ef0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3436
-  Symbols:   12255
-  CStrings:  5454
+  Functions: 3438
+  Symbols:   12259
+  CStrings:  5458
 
Symbols:
+ -[VNDocumentCameraViewController_InProcess preferredContainerBackgroundStyle]
+ -[VNDocumentCameraViewController_ViewService preferredContainerBackgroundStyle]
+ ___49-[ICDocCamViewController snapStillImageWithMode:]_block_invoke.549
+ ___49-[ICDocCamViewController snapStillImageWithMode:]_block_invoke_2.550
+ ___55-[ICRemoteDocCamViewController sidecarRequestDidFinish]_block_invoke.66
+ ___55-[ICRemoteDocCamViewController sidecarRequestDidFinish]_block_invoke.66.cold.1
+ ___55-[ICRemoteDocCamViewController sidecarRequestDidFinish]_block_invoke.66.cold.2
+ ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke.524
+ ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke.524.cold.1
+ ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke.532
+ ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_2.525
+ ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_2.530
+ ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_3.526
+ ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_3.531
+ ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_3.531.cold.1
+ ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_4.527
+ ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_5.528
+ ___90-[ICDocCamViewController detectRectanglesAndSaveCapturedImage:metadata:completionHandler:]_block_invoke.536
+ ___90-[ICDocCamViewController detectRectanglesAndSaveCapturedImage:metadata:completionHandler:]_block_invoke_2.537
+ ___Block_byref_object_copy_.508
+ ___Block_byref_object_dispose_.509
+ ___block_literal_global.304
+ ___block_literal_global.371
+ ___block_literal_global.651
+ __unnamed_array_storage.401
+ __unnamed_array_storage.408
+ __unnamed_array_storage.411
+ __unnamed_array_storage.480
+ __unnamed_array_storage.677
- ___49-[ICDocCamViewController snapStillImageWithMode:]_block_invoke.546
- ___49-[ICDocCamViewController snapStillImageWithMode:]_block_invoke_2.547
- ___55-[ICRemoteDocCamViewController sidecarRequestDidFinish]_block_invoke.59
- ___55-[ICRemoteDocCamViewController sidecarRequestDidFinish]_block_invoke.59.cold.1
- ___55-[ICRemoteDocCamViewController sidecarRequestDidFinish]_block_invoke.59.cold.2
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke.521
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke.521.cold.1
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke.526
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_2.522
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_2.527
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_3.523
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_3.528
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_3.528.cold.1
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_4.524
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_5.525
- ___90-[ICDocCamViewController detectRectanglesAndSaveCapturedImage:metadata:completionHandler:]_block_invoke.533
- ___90-[ICDocCamViewController detectRectanglesAndSaveCapturedImage:metadata:completionHandler:]_block_invoke_2.534
- ___Block_byref_object_copy_.505
- ___Block_byref_object_dispose_.506
- ___block_literal_global.301
- ___block_literal_global.367
- ___block_literal_global.648
- __unnamed_array_storage.397
- __unnamed_array_storage.404
- __unnamed_array_storage.407
- __unnamed_array_storage.474
- __unnamed_array_storage.674
CStrings:
+ "character.cursor.ibeam"
+ "exclamationmark.triangle"
+ "ipad.and.iphone"
+ "preferredContainerBackgroundStyle"

```
