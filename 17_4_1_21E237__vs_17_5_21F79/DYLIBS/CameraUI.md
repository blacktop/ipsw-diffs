## CameraUI

> `/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`

```diff

-4009.19.0.0.0
-  __TEXT.__text: 0x1df470
-  __TEXT.__auth_stubs: 0x20a0
-  __TEXT.__objc_methlist: 0x15388
+4011.3.0.0.0
+  __TEXT.__text: 0x1e1a58
+  __TEXT.__auth_stubs: 0x20c0
+  __TEXT.__objc_methlist: 0x15508
   __TEXT.__const: 0x2d58
-  __TEXT.__gcc_except_tab: 0x2404
-  __TEXT.__cstring: 0x12898
-  __TEXT.__oslogstring: 0x11e33
+  __TEXT.__gcc_except_tab: 0x2458
+  __TEXT.__cstring: 0x12c2b
+  __TEXT.__oslogstring: 0x11f5b
   __TEXT.__dlopen_cstrs: 0x310
   __TEXT.__ustring: 0x8
-  __TEXT.__objc_const_ax: 0xea20
-  __TEXT.__unwind_info: 0x8514
-  __TEXT.__objc_classname: 0x4a6e
-  __TEXT.__objc_methname: 0x80543
-  __TEXT.__objc_methtype: 0xd86f
-  __TEXT.__objc_stubs: 0x49f40
-  __DATA_CONST.__got: 0x1170
-  __DATA_CONST.__const: 0x6220
-  __DATA_CONST.__objc_classlist: 0xed0
+  __TEXT.__objc_const_ax: 0xeab0
+  __TEXT.__unwind_info: 0x8524
+  __TEXT.__objc_classname: 0x4b88
+  __TEXT.__objc_methname: 0x810a7
+  __TEXT.__objc_methtype: 0xdd4e
+  __TEXT.__objc_stubs: 0x4a5c0
+  __DATA_CONST.__got: 0x1188
+  __DATA_CONST.__const: 0x62e0
+  __DATA_CONST.__objc_classlist: 0xee8
   __DATA_CONST.__objc_catlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x5e8
+  __DATA_CONST.__objc_protolist: 0x618
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3bc20
-  __DATA_CONST.__objc_selrefs: 0x146e0
+  __DATA_CONST.__objc_const: 0x3c1c0
+  __DATA_CONST.__objc_selrefs: 0x148c8
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_classrefs: 0x1688
-  __DATA_CONST.__objc_superrefs: 0xc70
-  __DATA_CONST.__objc_arraydata: 0xcf0
-  __AUTH_CONST.__cfstring: 0x12b20
-  __AUTH_CONST.__objc_const: 0x9fc8
+  __DATA_CONST.__objc_classrefs: 0x16d0
+  __DATA_CONST.__objc_superrefs: 0xc78
+  __DATA_CONST.__objc_arraydata: 0xcf8
+  __AUTH_CONST.__cfstring: 0x12e60
+  __AUTH_CONST.__objc_const: 0xa0e8
   __AUTH_CONST.__objc_intobj: 0x15a8
   __AUTH_CONST.__objc_doubleobj: 0x500
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0xb28
-  __AUTH_CONST.__const: 0xaa0
+  __AUTH_CONST.__const: 0xac0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1060
-  __AUTH.__objc_data: 0x2648
-  __DATA.__objc_ivar: 0x31bc
+  __AUTH_CONST.__auth_got: 0x1070
+  __AUTH.__objc_data: 0x2508
+  __DATA.__objc_ivar: 0x31d8
   __DATA.__objc_const_ax: 0x0
-  __DATA.__data: 0x4778
-  __DATA.__bss: 0x1f0
-  __DATA_DIRTY.__objc_data: 0x6dd8
+  __DATA.__data: 0x49c0
+  __DATA.__bss: 0x200
+  __DATA_DIRTY.__objc_data: 0x7008
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x2b8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 13834
-  Symbols:   47162
-  CStrings:  22500
+  Functions: 13892
+  Symbols:   47407
+  CStrings:  22654
 
Symbols:
+ +[CAMDocumentScanFlowController isSupported]
+ +[CAMDocumentScanFlowController nameForDocumentWithDate:]
+ +[CAMPDFConverter _pdfPageOptionsForImageRef:]
+ +[CAMPDFConverter convertToPDFAndWrite:documentName:completionHandler:]
+ +[CAMPDFConverter convertToPDFAndWrite:documentName:completionHandler:].cold.1
+ +[CAMPDFConverter convertToPDFAndWrite:documentName:completionHandler:].cold.2
+ -[CAMCaptureCapabilities documentScanningMinimumConfidenceLevel]
+ -[CAMCaptureCapabilities isDocumentScanningSupported]
+ -[CAMCaptureCapabilities isFrontCameraOnRightEdge]
+ -[CAMDocumentScanFlowController .cxx_destruct]
+ -[CAMDocumentScanFlowController _asyncConvertToPDFAndWrite:completionHandler:]
+ -[CAMDocumentScanFlowController _handlePDFResults:]
+ -[CAMDocumentScanFlowController _handlePDFResults:].cold.1
+ -[CAMDocumentScanFlowController _pdfConversionQueue]
+ -[CAMDocumentScanFlowController _url]
+ -[CAMDocumentScanFlowController documentCameraViewController:didFailWithError:]
+ -[CAMDocumentScanFlowController documentCameraViewController:didFinishWithScan:]
+ -[CAMDocumentScanFlowController documentCameraViewControllerDidCancel:]
+ -[CAMDocumentScanFlowController documentFlowDelegate]
+ -[CAMDocumentScanFlowController documentPicker:didPickDocumentsAtURLs:]
+ -[CAMDocumentScanFlowController init]
+ -[CAMDocumentScanFlowController numberOfPreviewItemsInPreviewController:]
+ -[CAMDocumentScanFlowController previewController:editingModeForPreviewItem:]
+ -[CAMDocumentScanFlowController previewController:previewItemAtIndex:]
+ -[CAMDocumentScanFlowController setDocumentFlowDelegate:]
+ -[CAMDocumentScanFlowController set_url:]
+ -[CAMResetVideoMinFrameDurationOverrideCommand executeWithContext:]
+ -[CAMViewfinderViewController _dismissDocumentScanningButton]
+ -[CAMViewfinderViewController _handleDocumentScanningPillPress]
+ -[CAMViewfinderViewController _isDisplayingDocumentScanningButton]
+ -[CAMViewfinderViewController _isDisplayingMRCButton]
+ -[CAMViewfinderViewController _isDocumentInScene]
+ -[CAMViewfinderViewController _setDocumentInScene:]
+ -[CAMViewfinderViewController _shouldShowDocumentScanningButton]
+ -[CAMViewfinderViewController _updateDocumentScanningButtonIfNeeded]
+ -[CAMViewfinderViewController captureController:didChangeDocumentSceneConfidenceResults:]
+ -[CAMViewfinderViewController documentScanFlowControllerDidCancel:]
+ -[CAMViewfinderViewController documentScanFlowControllerDidFail:withError:]
+ -[CAMViewfinderViewController documentScanFlowControllerDidFinish:]
+ -[CUCaptureController _documentScanningChangedForKeyPath:ofObject:change:]
+ -[CUCaptureController _setupDocumentScanningMonitoring]
+ -[CUCaptureController _tearDownDocumentScanningMonitoring]
+ -[CUCaptureController documentSceneResultDelegate]
+ -[CUCaptureController setDocumentSceneResultDelegate:]
+ GCC_except_table1057
+ GCC_except_table1063
+ GCC_except_table1172
+ GCC_except_table1177
+ GCC_except_table1182
+ GCC_except_table186
+ GCC_except_table187
+ GCC_except_table198
+ GCC_except_table217
+ GCC_except_table225
+ GCC_except_table553
+ GCC_except_table555
+ GCC_except_table609
+ GCC_except_table768
+ GCC_except_table786
+ GCC_except_table839
+ GCC_except_table842
+ _CAMDocumentScanningResultsContext
+ _CGImageGetSizeAfterOrientation
+ _OBJC_CLASS_$_CAMDocumentScanFlowController
+ _OBJC_CLASS_$_CAMPDFConverter
+ _OBJC_CLASS_$_CAMResetVideoMinFrameDurationOverrideCommand
+ _OBJC_CLASS_$_PDFDocument
+ _OBJC_CLASS_$_PDFPage
+ _OBJC_CLASS_$_QLPreviewController
+ _OBJC_CLASS_$_UIAction
+ _OBJC_CLASS_$_UIDocumentPickerViewController
+ _OBJC_CLASS_$_VNDocumentCameraViewController
+ _OBJC_IVAR_$_CAMCaptureCapabilities._documentScanningMinimumConfidenceLevel
+ _OBJC_IVAR_$_CAMCaptureCapabilities._documentScanningSupported
+ _OBJC_IVAR_$_CAMCaptureCapabilities._frontCameraOnRightEdge
+ _OBJC_IVAR_$_CAMDocumentScanFlowController.__url
+ _OBJC_IVAR_$_CAMDocumentScanFlowController._documentFlowDelegate
+ _OBJC_IVAR_$_CAMViewfinderViewController.__documentInScene
+ _OBJC_IVAR_$_CUCaptureController._documentSceneResultDelegate
+ _OBJC_METACLASS_$_CAMDocumentScanFlowController
+ _OBJC_METACLASS_$_CAMPDFConverter
+ _OBJC_METACLASS_$_CAMResetVideoMinFrameDurationOverrideCommand
+ _PDFPageImageInitializationOptionMediaBox
+ _PDFPageImageInitializationOptionUpscaleIfSmaller
+ __OBJC_$_CLASS_METHODS_CAMDocumentScanFlowController
+ __OBJC_$_CLASS_METHODS_CAMPDFConverter
+ __OBJC_$_INSTANCE_METHODS_CAMDocumentScanFlowController
+ __OBJC_$_INSTANCE_METHODS_CAMResetVideoMinFrameDurationOverrideCommand
+ __OBJC_$_INSTANCE_VARIABLES_CAMDocumentScanFlowController
+ __OBJC_$_PROP_LIST_CAMDocumentScanFlowController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAMDocumentScanFlowControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAMDocumentSceneResultDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_QLPreviewControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIDocumentPickerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_VNDocumentCameraViewControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_QLPreviewControllerDataSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAMDocumentScanFlowControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAMDocumentSceneResultDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_QLPreviewControllerDataSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_QLPreviewControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIDocumentPickerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_VNDocumentCameraViewControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_CAMDocumentSceneResultDelegate
+ __OBJC_$_PROTOCOL_REFS_QLPreviewControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_UIDocumentPickerDelegate
+ __OBJC_$_PROTOCOL_REFS_VNDocumentCameraViewControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CAMDocumentScanFlowController
+ __OBJC_CLASS_RO_$_CAMDocumentScanFlowController
+ __OBJC_CLASS_RO_$_CAMPDFConverter
+ __OBJC_CLASS_RO_$_CAMResetVideoMinFrameDurationOverrideCommand
+ __OBJC_LABEL_PROTOCOL_$_CAMDocumentScanFlowControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_CAMDocumentSceneResultDelegate
+ __OBJC_LABEL_PROTOCOL_$_QLPreviewControllerDataSource
+ __OBJC_LABEL_PROTOCOL_$_QLPreviewControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_UIDocumentPickerDelegate
+ __OBJC_LABEL_PROTOCOL_$_VNDocumentCameraViewControllerDelegate
+ __OBJC_METACLASS_RO_$_CAMDocumentScanFlowController
+ __OBJC_METACLASS_RO_$_CAMPDFConverter
+ __OBJC_METACLASS_RO_$_CAMResetVideoMinFrameDurationOverrideCommand
+ __OBJC_PROTOCOL_$_CAMDocumentScanFlowControllerDelegate
+ __OBJC_PROTOCOL_$_CAMDocumentSceneResultDelegate
+ __OBJC_PROTOCOL_$_QLPreviewControllerDataSource
+ __OBJC_PROTOCOL_$_QLPreviewControllerDelegate
+ __OBJC_PROTOCOL_$_UIDocumentPickerDelegate
+ __OBJC_PROTOCOL_$_VNDocumentCameraViewControllerDelegate
+ ___51-[CAMDocumentScanFlowController _handlePDFResults:]_block_invoke
+ ___51-[CAMDocumentScanFlowController _handlePDFResults:]_block_invoke_2
+ ___52-[CAMDocumentScanFlowController _pdfConversionQueue]_block_invoke
+ ___63-[CAMViewfinderViewController _handleDocumentScanningPillPress]_block_invoke
+ ___63-[CAMViewfinderViewController _handleDocumentScanningPillPress]_block_invoke_2
+ ___63-[CAMViewfinderViewController _handleDocumentScanningPillPress]_block_invoke_3
+ ___63-[CAMViewfinderViewController _handleDocumentScanningPillPress]_block_invoke_4
+ ___63-[CAMViewfinderViewController _handleDocumentScanningPillPress]_block_invoke_5
+ ___71+[CAMPDFConverter convertToPDFAndWrite:documentName:completionHandler:]_block_invoke
+ ___72-[CAMViewfinderViewController _createPhysicalCaptureInteractionIfNeeded]_block_invoke.944
+ ___74-[CUCaptureController _documentScanningChangedForKeyPath:ofObject:change:]_block_invoke
+ ___78-[CAMDocumentScanFlowController _asyncConvertToPDFAndWrite:completionHandler:]_block_invoke
+ ___78-[CAMDocumentScanFlowController _asyncConvertToPDFAndWrite:completionHandler:]_block_invoke_2
+ ___78-[CAMDocumentScanFlowController _asyncConvertToPDFAndWrite:completionHandler:]_block_invoke_3
+ ___80-[CAMDocumentScanFlowController documentCameraViewController:didFinishWithScan:]_block_invoke
+ ___block_descriptor_40_e26_"PDFPage"16?0"UIImage"8l
+ ___block_descriptor_40_e8_32bs_e15_v16?0"NSURL"8ls32l8
+ ___block_descriptor_40_e8_32s_e18_v16?0"UIAction"8ls32l8
+ ___block_descriptor_40_e8_32w_e15_v16?0"NSURL"8lw32l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.1019
+ ___block_literal_global.1161
+ ___block_literal_global.27
+ ___block_literal_global.478
+ __pdfConversionQueue._conversionQueue
+ __pdfConversionQueue.onceToken
+ __unnamed_array_storage.342
+ __unnamed_array_storage.359
+ __unnamed_array_storage.362
+ __unnamed_array_storage.366
+ __unnamed_array_storage.390
+ __unnamed_array_storage.393
+ __unnamed_array_storage.3937
+ __unnamed_array_storage.3940
+ __unnamed_array_storage.3943
+ __unnamed_array_storage.398
+ __unnamed_array_storage.401
+ __unnamed_array_storage.406
+ __unnamed_array_storage.453
+ __unnamed_array_storage.456
+ __unnamed_array_storage.643
+ __unnamed_array_storage.662
+ __unnamed_array_storage.848
+ __unnamed_array_storage.851
+ __unnamed_array_storage.854
+ __unnamed_array_storage.857
+ _kCGPDFContextShouldOutputAllImagesAsJPEG
+ _objc_msgSend$URLByAppendingPathComponent:
+ _objc_msgSend$_asyncConvertToPDFAndWrite:completionHandler:
+ _objc_msgSend$_dismissDocumentScanningButton
+ _objc_msgSend$_documentScanningChangedForKeyPath:ofObject:change:
+ _objc_msgSend$_handlePDFResults:
+ _objc_msgSend$_isDisplayingDocumentScanningButton
+ _objc_msgSend$_isDisplayingMRCButton
+ _objc_msgSend$_isDocumentInScene
+ _objc_msgSend$_pdfConversionQueue
+ _objc_msgSend$_pdfPageOptionsForImageRef:
+ _objc_msgSend$_setDocumentInScene:
+ _objc_msgSend$_setupDocumentScanningMonitoring
+ _objc_msgSend$_shouldShowDocumentScanningButton
+ _objc_msgSend$_tearDownDocumentScanningMonitoring
+ _objc_msgSend$_updateDocumentScanningButtonIfNeeded
+ _objc_msgSend$_url
+ _objc_msgSend$actionWithTitle:image:identifier:handler:
+ _objc_msgSend$captureController:didChangeDocumentSceneConfidenceResults:
+ _objc_msgSend$convertToPDFAndWrite:documentName:completionHandler:
+ _objc_msgSend$dateFormatFromTemplate:options:locale:
+ _objc_msgSend$debugDescription
+ _objc_msgSend$documentFlowDelegate
+ _objc_msgSend$documentScanFlowControllerDidCancel:
+ _objc_msgSend$documentScanFlowControllerDidFail:withError:
+ _objc_msgSend$documentScanFlowControllerDidFinish:
+ _objc_msgSend$documentScanningMinimumConfidenceLevel
+ _objc_msgSend$documentSceneConfidence
+ _objc_msgSend$documentSceneResultDelegate
+ _objc_msgSend$imageOfPageAtIndex:
+ _objc_msgSend$initForExportingURLs:asCopy:
+ _objc_msgSend$initWithImage:options:
+ _objc_msgSend$initWithTitle:menu:
+ _objc_msgSend$insertPage:atIndex:
+ _objc_msgSend$isDocumentScanningSupported
+ _objc_msgSend$isFrontCameraOnRightEdge
+ _objc_msgSend$isSupported
+ _objc_msgSend$localizedStringFromDate:dateStyle:timeStyle:
+ _objc_msgSend$menuWithChildren:
+ _objc_msgSend$menuWithTitle:image:identifier:options:children:
+ _objc_msgSend$nameForDocumentWithDate:
+ _objc_msgSend$pageCount
+ _objc_msgSend$presentModalViewController:animated:
+ _objc_msgSend$setAttributes:
+ _objc_msgSend$setDocumentFlowDelegate:
+ _objc_msgSend$setDocumentSceneResultDelegate:
+ _objc_msgSend$setHidesBackButton:
+ _objc_msgSend$setModalTransitionStyle:
+ _objc_msgSend$setVideoMinFrameDurationOverride:
+ _objc_msgSend$setViewControllers:animated:
+ _objc_msgSend$set_url:
+ _objc_msgSend$temporaryDirectory
+ _objc_msgSend$writeToURL:withOptions:
+ _objc_retainAutoreleasedReturnValue
- GCC_except_table1042
- GCC_except_table1048
- GCC_except_table1157
- GCC_except_table1162
- GCC_except_table1167
- GCC_except_table182
- GCC_except_table183
- GCC_except_table194
- GCC_except_table210
- GCC_except_table538
- GCC_except_table540
- GCC_except_table594
- GCC_except_table753
- GCC_except_table771
- GCC_except_table824
- GCC_except_table827
- ___72-[CAMViewfinderViewController _createPhysicalCaptureInteractionIfNeeded]_block_invoke.932
- ___block_literal_global.1009
- ___block_literal_global.1151
- ___block_literal_global.24
- ___block_literal_global.466
- __unnamed_array_storage.330
- __unnamed_array_storage.341
- __unnamed_array_storage.344
- __unnamed_array_storage.360
- __unnamed_array_storage.381
- __unnamed_array_storage.384
- __unnamed_array_storage.3907
- __unnamed_array_storage.3910
- __unnamed_array_storage.3913
- __unnamed_array_storage.392
- __unnamed_array_storage.395
- __unnamed_array_storage.400
- __unnamed_array_storage.432
- __unnamed_array_storage.435
- __unnamed_array_storage.629
- __unnamed_array_storage.650
- __unnamed_array_storage.761
- __unnamed_array_storage.764
- __unnamed_array_storage.767
- __unnamed_array_storage.770
CStrings:
+ "\x01\xf0\xa1,\x13\x18"
+ "%@.pdf"
+ "/"
+ "@\"<CAMDocumentScanFlowControllerDelegate>\""
+ "@\"<CAMDocumentSceneResultDelegate>\""
+ "@\"<QLPreviewItem>\"32@0:8@\"QLPreviewController\"16q24"
+ "@\"PDFPage\"16@?0@\"UIImage\"8"
+ "@\"UIImage\"40@0:8@\"QLPreviewController\"16@\"<QLPreviewItem>\"24^{CGRect={CGPoint=dd}{CGSize=dd}}32"
+ "@\"UIView\"32@0:8@\"QLPreviewController\"16@\"<QLPreviewItem>\"24"
+ "@24@0:8^{CGImage=}16"
+ "@40@0:8@16@24^{CGRect={CGPoint=dd}{CGSize=dd}}32"
+ "B\x15\x1d\x12"
+ "B40@0:8@\"QLPreviewController\"16@\"NSURL\"24@\"<QLPreviewItem>\"32"
+ "CAMDocumentScanFlowController"
+ "CAMDocumentScanFlowControllerDelegate"
+ "CAMDocumentSceneResultDelegate"
+ "CAMFeatureDevelopmentDocumentScanningEnabled"
+ "CAMFeatureDevelopmentDocumentScanningMininumConfidenceLevel"
+ "CAMPDFConverter"
+ "CAMResetVideoMinFrameDurationOverrideCommand"
+ "CameraUI-DocumentScanning"
+ "DOCUMENT_SCANNING_DELETE"
+ "DOCUMENT_SCANNING_DONE"
+ "DOCUMENT_SCANNING_FILENAME"
+ "DOCUMENT_SCANNING_FILENAME_DATE_DELIMITER"
+ "DOCUMENT_SCANNING_FILENAME_FORMAT_STRING"
+ "DOCUMENT_SCANNING_FILENAME_TIME_DELIMITER"
+ "DOCUMENT_SCANNING_SAVE_TO_FILES"
+ "DOCUMENT_SCANNING_TITLE"
+ "Date component delimiter for filename. Cannot be slash (/) or colon (:)"
+ "Document Scanning component of the file name"
+ "Document scanner: error converting scanned images to PDF"
+ "Failed to create PDF page from image (image %lu/%lu of scanned document) with description: %{public}@"
+ "Failed to create directory for scanned PDF with error: %@"
+ "Failed to remove item (at path %@) prior to storing scanned PDF with error: %@"
+ "General format string for the file name. English format is SCREENSHOT_SAVE_FILE_NAME DATE at TIME"
+ "QLPreviewControllerDataSource"
+ "QLPreviewControllerDelegate"
+ "T@\"<CAMDocumentScanFlowControllerDelegate>\",W,N,V_documentFlowDelegate"
+ "T@\"<CAMDocumentSceneResultDelegate>\",W,N,V_documentSceneResultDelegate"
+ "T@\"NSURL\",&,N,V__url"
+ "TB,N,G_isDocumentInScene,S_setDocumentInScene:,V__documentInScene"
+ "TB,R,N,GisDocumentScanningSupported,V_documentScanningSupported"
+ "TB,R,N,GisFrontCameraOnRightEdge,V_frontCameraOnRightEdge"
+ "Tf,R,N,V_documentScanningMinimumConfidenceLevel"
+ "Time component delimiter for filename. Cannot be slash (/) or colon (:)"
+ "UIDocumentPickerDelegate"
+ "URLByAppendingPathComponent:"
+ "VNDocumentCameraViewControllerDelegate"
+ "__documentInScene"
+ "__url"
+ "_asyncConvertToPDFAndWrite:completionHandler:"
+ "_dismissDocumentScanningButton"
+ "_documentFlowDelegate"
+ "_documentInScene"
+ "_documentScanningChangedForKeyPath:ofObject:change:"
+ "_documentScanningMinimumConfidenceLevel"
+ "_documentScanningSupported"
+ "_documentSceneResultDelegate"
+ "_frontCameraOnRightEdge"
+ "_handleDocumentScanningPillPress"
+ "_handlePDFResults:"
+ "_isDisplayingDocumentScanningButton"
+ "_isDisplayingMRCButton"
+ "_isDocumentInScene"
+ "_pdfConversionQueue"
+ "_pdfPageOptionsForImageRef:"
+ "_setDocumentInScene:"
+ "_setupDocumentScanningMonitoring"
+ "_shouldShowDocumentScanningButton"
+ "_tearDownDocumentScanningMonitoring"
+ "_updateDocumentScanningButtonIfNeeded"
+ "actionWithTitle:image:identifier:handler:"
+ "captureController:didChangeDocumentSceneConfidenceResults:"
+ "com.apple.camera.pdf-conversion-queue"
+ "convertToPDFAndWrite:documentName:completionHandler:"
+ "currentCameraDevice.documentSceneConfidence"
+ "dateFormatFromTemplate:options:locale:"
+ "delete"
+ "destructive.options"
+ "doc.viewfinder"
+ "documentCameraViewController:didFailWithError:"
+ "documentCameraViewController:didFinishWithScan:"
+ "documentCameraViewControllerDidCancel:"
+ "documentFlowDelegate"
+ "documentPicker:didPickDocumentAtURL:"
+ "documentPicker:didPickDocumentsAtURLs:"
+ "documentPickerWasCancelled:"
+ "documentScanFlowControllerDidCancel:"
+ "documentScanFlowControllerDidFail:withError:"
+ "documentScanFlowControllerDidFinish:"
+ "documentScanningMinimumConfidenceLevel"
+ "documentScanningSupported"
+ "documentSceneConfidence"
+ "documentSceneResultDelegate"
+ "frontCameraOnRightEdge"
+ "imageOfPageAtIndex:"
+ "initForExportingURLs:asCopy:"
+ "initWithImage:options:"
+ "initWithRootViewController:"
+ "initWithTitle:menu:"
+ "insertPage:atIndex:"
+ "isDocumentScanningSupported"
+ "isFrontCameraOnRightEdge"
+ "isSupported"
+ "localizedStringFromDate:dateStyle:timeStyle:"
+ "menuWithChildren:"
+ "menuWithTitle:image:identifier:options:children:"
+ "nameForDocumentWithDate:"
+ "numberOfPreviewItemsInPreviewController:"
+ "pageCount"
+ "presentModalViewController:animated:"
+ "previewController:didSaveEditedCopyOfPreviewItem:atURL:"
+ "previewController:didUpdateContentsOfPreviewItem:"
+ "previewController:editingModeForPreviewItem:"
+ "previewController:frameForPreviewItem:inSourceView:"
+ "previewController:previewItemAtIndex:"
+ "previewController:shouldOpenURL:forPreviewItem:"
+ "previewController:transitionImageForPreviewItem:contentRect:"
+ "previewController:transitionViewForPreviewItem:"
+ "previewControllerDidDismiss:"
+ "previewControllerWillDismiss:"
+ "q24@0:8@\"QLPreviewController\"16"
+ "q32@0:8@\"QLPreviewController\"16@\"<QLPreviewItem>\"24"
+ "q32@0:8@16@24"
+ "save"
+ "setAttributes:"
+ "setDocumentFlowDelegate:"
+ "setDocumentSceneResultDelegate:"
+ "setHidesBackButton:"
+ "setModalTransitionStyle:"
+ "setVideoMinFrameDurationOverride:"
+ "setViewControllers:animated:"
+ "set_url:"
+ "square.and.arrow.down"
+ "temporaryDirectory"
+ "trash"
+ "v16@?0@\"NSURL\"8"
+ "v16@?0@\"UIAction\"8"
+ "v24@0:8@\"CAMDocumentScanFlowController\"16"
+ "v24@0:8@\"QLPreviewController\"16"
+ "v24@0:8@\"UIDocumentPickerViewController\"16"
+ "v24@0:8@\"VNDocumentCameraViewController\"16"
+ "v28@0:8@\"CUCaptureController\"16f24"
+ "v32@0:8@\"CAMDocumentScanFlowController\"16@\"NSError\"24"
+ "v32@0:8@\"QLPreviewController\"16@\"<QLPreviewItem>\"24"
+ "v32@0:8@\"UIDocumentPickerViewController\"16@\"NSArray\"24"
+ "v32@0:8@\"UIDocumentPickerViewController\"16@\"NSURL\"24"
+ "v32@0:8@\"VNDocumentCameraViewController\"16@\"NSError\"24"
+ "v32@0:8@\"VNDocumentCameraViewController\"16@\"VNDocumentCameraScan\"24"
+ "v40@0:8@\"QLPreviewController\"16@\"<QLPreviewItem>\"24@\"NSURL\"32"
+ "writeToURL:withOptions:"
+ "yyyy-MM-dd"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}40@0:8@\"QLPreviewController\"16@\"<QLPreviewItem>\"24^@32"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}40@0:8@16@24^@32"
+ "\xa2\xf0\xf0\xf0\xf0\xf0\xf0\xf0Q\xf0\xf0\xf0\xb3\x11"
+ "\xcf\x031\xf0\xe1!\x11?\x05/\r-2\x12\x14!B\x12\x1f\x011a"
+ "\xf0\xf0\xf0\xd1Rq\xf0\xf0!x"
- "\x01\xf0\x91,\x13\x18"
- "B\x15\x1c\x12"
- "\x92\xf0\xf0\xf0\xf0\xf0\xf0\xf0Q\xf0\xf0\xf0\xb3\x11"
- "\xbf\x031\xf0\xe1!\x11?\x05/\r-2\x12\x14!B\x12\x1f\x011a"
- "\xf0\xf0\xf0\xc1Rq\xf0\xf0!x"

```
