## DocumentCamera

> `/System/iOSSupport/System/Library/PrivateFrameworks/DocumentCamera.framework/Versions/A/DocumentCamera`

```diff

 185.0.0.0.0
-  __TEXT.__text: 0x89f1c
+  __TEXT.__text: 0x89c2c
   __TEXT.__auth_stubs: 0x1480
-  __TEXT.__objc_methlist: 0x7db4
-  __TEXT.__const: 0x620
-  __TEXT.__gcc_except_tab: 0x8b10
+  __TEXT.__objc_methlist: 0x8b98
+  __TEXT.__const: 0x610
+  __TEXT.__gcc_except_tab: 0x8b14
   __TEXT.__cstring: 0x360f
   __TEXT.__oslogstring: 0x1b9e
   __TEXT.__ustring: 0x3a0
   __TEXT.__dlopen_cstrs: 0x2f6
-  __TEXT.__unwind_info: 0x2870
+  __TEXT.__unwind_info: 0x28b0
   __TEXT.__objc_classname: 0x101b
-  __TEXT.__objc_methname: 0x1aacc
-  __TEXT.__objc_methtype: 0x4010
+  __TEXT.__objc_methname: 0x1aaed
+  __TEXT.__objc_methtype: 0x403e
   __TEXT.__objc_stubs: 0x12940
   __DATA_CONST.__got: 0x8c8
   __DATA_CONST.__const: 0x1668

   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5880
+  __DATA_CONST.__objc_selrefs: 0x5bd8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x268

   __AUTH_CONST.__auth_got: 0xa58
   __AUTH_CONST.__const: 0x438
   __AUTH_CONST.__cfstring: 0x3900
-  __AUTH_CONST.__objc_const: 0x14ad8
+  __AUTH_CONST.__objc_const: 0x13198
   __AUTH_CONST.__objc_doubleobj: 0x130
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_arrayobj: 0xf0

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5F76B913-BAF6-382E-98CD-E476E0ADAC4E
-  Functions: 3362
-  Symbols:   8778
-  CStrings:  5878
+  UUID: 3AF7658F-4361-3695-9A08-2AE937DB3A88
+  Functions: 3373
+  Symbols:   8799
+  CStrings:  5880
 
Symbols:
+ +[DCDispatchAfterHandler appLifeCycleHandler].cold.2
+ +[DCDocCamPDFGenerator fileQueue].cold.1
+ +[DCDocCamPDFGenerator rootPDFFolderPath].cold.1
+ +[DCDocCamPDFGenerator syncGeneratorQueue].cold.1
+ +[DCImageAnalyzerManager sharedInstance].cold.1
+ +[DCLRUCache cacheCollection].cold.1
+ +[DCScannedDocument scannedDocumentsFolderURL].cold.1
+ +[ICDocCamImageFilters imageFilterNames].cold.1
+ +[ICDocCamImageFilters nonLocalizedImageFilterNames].cold.1
+ +[VNDocumentCameraScan scannedDocumentsFolderURL].cold.1
+ -[ICDocCamImageQuadEditorController presentFromResponder:].cold.1
+ -[ICDocCamViewController preWarmFilters].cold.1
+ -[ICDocCamViewController useDocumentSegmentation].cold.1
+ -[NSString(DC) dc_whitespaceAndNewlineCoalescedString].cold.1
+ DCTSUCGColorCreateDeviceGray.cold.1
+ DCTSUCGColorCreateDeviceRGB.cold.1
+ DCTSUCreateRGBABitmapContext.cold.1
+ DCTSUDeviceCMYKColorSpace.cold.1
+ DCTSUDeviceGrayColorSpace.cold.1
+ DCTSUDeviceRGBColorSpace.cold.1
+ __61-[DCImageAnalyzerManager analysisForImage:completionHandler:]_block_invoke.155
+ __61-[DCImageAnalyzerManager analysisForImage:completionHandler:]_block_invoke.156
+ __61-[DCImageAnalyzerManager analysisForImage:completionHandler:]_block_invoke.156.cold.1
+ __61-[DCImageAnalyzerManager analysisForImage:completionHandler:]_block_invoke.157
+ __block_literal_global.690
- __61-[DCImageAnalyzerManager analysisForImage:completionHandler:]_block_invoke.41
- __61-[DCImageAnalyzerManager analysisForImage:completionHandler:]_block_invoke.42
- __61-[DCImageAnalyzerManager analysisForImage:completionHandler:]_block_invoke.42.cold.1
- __61-[DCImageAnalyzerManager analysisForImage:completionHandler:]_block_invoke.43
- __block_literal_global.576
CStrings:
+ "textField:insertInputSuggestion:"
+ "v32@0:8@\"UITextField\"16@\"UIInputSuggestion\"24"

```
