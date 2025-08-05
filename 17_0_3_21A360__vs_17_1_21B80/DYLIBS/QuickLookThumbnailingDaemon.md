## QuickLookThumbnailingDaemon

> `/System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/QuickLookThumbnailingDaemon`

```diff

-185.0.0.0.0
-  __TEXT.__text: 0x3ed7c
+186.2.2.0.0
+  __TEXT.__text: 0x3efd8
   __TEXT.__auth_stubs: 0x12a0
-  __TEXT.__objc_methlist: 0x2c84
+  __TEXT.__objc_methlist: 0x2ccc
   __TEXT.__const: 0x1c8
   __TEXT.__gcc_except_tab: 0xa60
-  __TEXT.__cstring: 0x3ca6
+  __TEXT.__cstring: 0x3cb0
   __TEXT.__oslogstring: 0x5206
   __TEXT.__dof_QuickLook: 0xb22
   __TEXT.__unwind_info: 0xf94
   __TEXT.__objc_classname: 0x49d
-  __TEXT.__objc_methname: 0x9314
-  __TEXT.__objc_methtype: 0x1a51
-  __TEXT.__objc_stubs: 0x71c0
+  __TEXT.__objc_methname: 0x944c
+  __TEXT.__objc_methtype: 0x1a40
+  __TEXT.__objc_stubs: 0x7220
   __DATA_CONST.__got: 0x250
   __DATA_CONST.__const: 0x1110
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x38d0
-  __DATA_CONST.__objc_selrefs: 0x2158
+  __DATA_CONST.__objc_const: 0x3930
+  __DATA_CONST.__objc_selrefs: 0x2188
   __AUTH_CONST.__cfstring: 0x1b00
   __AUTH_CONST.__objc_const: 0xe70
   __AUTH_CONST.__const: 0x1f8

   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x308
   __DATA.__objc_superrefs: 0xe0
-  __DATA.__objc_ivar: 0x430
+  __DATA.__objc_ivar: 0x438
   __DATA.__data: 0x248
   __DATA.__bss: 0x41
   __DATA_DIRTY.__objc_data: 0x8c0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 87CFB4F4-84E4-3173-AF09-CC54E80EC3BF
-  Functions: 1635
-  Symbols:   5387
-  CStrings:  2789
+  UUID: 4F987195-0FF2-3F51-972C-39FB38BB02BD
+  Functions: 1641
+  Symbols:   5404
+  CStrings:  2798
 
Symbols:
+ -[QLPreviewThumbnailGenerator initWithGeneratorRequest:lowQuality:thumbnailItem:]
+ -[QLServerThread _addThumbnailRequestBatchToQueue:completionHandler:]
+ -[QLServerThread _addThumbnailRequestBatchToQueue:completionHandler:].cold.1
+ -[QLServerThread generateSuccessiveThumbnailRepresentationsForGeneratorRequests:completionHandler:]
+ -[QLServerThread generateSuccessiveThumbnailRepresentationsForGeneratorRequests:completionHandler:].cold.1
+ -[QLTGeneratorThumbnailRequest clientApplicationIdentifier]
+ -[QLTGeneratorThumbnailRequest clientApprovedForAllFiles]
+ -[QLTGeneratorThumbnailRequest initWithRequest:generationHandler:]
+ -[QLTGeneratorThumbnailRequest setBatchDispatchGroup:]
+ -[QLTGeneratorThumbnailRequest setClientApplicationIdentifier:]
+ -[QLTGeneratorThumbnailRequest setClientApprovedForAllFiles:]
+ GCC_except_table24
+ GCC_except_table28
+ GCC_except_table63
+ _OBJC_IVAR_$_QLTGeneratorThumbnailRequest._clientApplicationIdentifier
+ _OBJC_IVAR_$_QLTGeneratorThumbnailRequest._clientApprovedForAllFiles
+ ___69-[QLServerThread _addThumbnailRequestBatchToQueue:completionHandler:]_block_invoke
+ ___99-[QLServerThread generateSuccessiveThumbnailRepresentationsForGeneratorRequests:completionHandler:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48bs_e42_v24?0"QLPlatformImage"8"NSDictionary"16ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e34_v16?0"CGRemotePDFDocumentProxy"8ls32l8s40l8s56l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56bs_e43_v40?0^{CGImage=}8{CGSize=dd}16"NSError"32ls32l8s40l8s56l8s48l8
+ _objc_msgSend$_addThumbnailRequestBatchToQueue:completionHandler:
+ _objc_msgSend$clientApplicationIdentifier
+ _objc_msgSend$generateSuccessiveThumbnailRepresentationsForGeneratorRequests:completionHandler:
+ _objc_msgSend$initWithGeneratorRequest:lowQuality:thumbnailItem:
+ _objc_msgSend$initWithRequest:generationHandler:
+ _objc_msgSend$setBatchDispatchGroup:
- -[QLPreviewThumbnailGenerator initWithGenerationRequest:lowQuality:thumbnailItem:]
- -[QLServerThread _addThumbnailRequestBatchToQueue:generationHandler:completionHandler:]
- -[QLServerThread _addThumbnailRequestBatchToQueue:generationHandler:completionHandler:].cold.1
- -[QLServerThread generateSuccessiveThumbnailRepresentationsForRequests:generationHandler:completionHandler:].cold.1
- -[QLTGeneratorThumbnailRequest initWithRequest:generationHandler:batchDispatchGroup:]
- GCC_except_table27
- GCC_except_table30
- GCC_except_table62
- ___108-[QLServerThread generateSuccessiveThumbnailRepresentationsForRequests:generationHandler:completionHandler:]_block_invoke
- ___87-[QLServerThread _addThumbnailRequestBatchToQueue:generationHandler:completionHandler:]_block_invoke
- ___block_descriptor_48_e8_32s40bs_e42_v24?0"QLPlatformImage"8"NSDictionary"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e34_v16?0"CGRemotePDFDocumentProxy"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48bs_e43_v40?0^{CGImage=}8{CGSize=dd}16"NSError"32ls32l8s40l8s48l8
- _objc_msgSend$_addThumbnailRequestBatchToQueue:generationHandler:completionHandler:
- _objc_msgSend$initWithGenerationRequest:lowQuality:thumbnailItem:
- _objc_msgSend$initWithRequest:generationHandler:batchDispatchGroup:
CStrings:
+ "\x158"
+ "<%@: %@, url: %@, item: %@, ht:%lu bt:%lu %@ client:%@>"
+ "T@\"NSObject<OS_dispatch_group>\",&,N,V_batchDispatchGroup"
+ "T@\"NSString\",&,V_clientApplicationIdentifier"
+ "T@\"QLTGeneratorThumbnailRequest\",&,V_request"
+ "TB,V_clientApprovedForAllFiles"
+ "_addThumbnailRequestBatchToQueue:completionHandler:"
+ "_clientApplicationIdentifier"
+ "_clientApprovedForAllFiles"
+ "clientApplicationIdentifier"
+ "clientApprovedForAllFiles"
+ "generateSuccessiveThumbnailRepresentationsForGeneratorRequests:completionHandler:"
+ "initWithGeneratorRequest:lowQuality:thumbnailItem:"
+ "initWithRequest:generationHandler:"
+ "setBatchDispatchGroup:"
+ "setClientApplicationIdentifier:"
+ "setClientApprovedForAllFiles:"
- "\x157"
- "<%@: %@, url: %@, item: %@, ht:%lu bt:%lu %@>"
- "@40@0:8@16@24@32"
- "T@\"NSObject<OS_dispatch_group>\",R,N,V_batchDispatchGroup"
- "T@\"QLThumbnailGenerationRequest\",&,V_request"
- "_addThumbnailRequestBatchToQueue:generationHandler:completionHandler:"
- "initWithGenerationRequest:lowQuality:thumbnailItem:"
- "initWithRequest:generationHandler:batchDispatchGroup:"

```
