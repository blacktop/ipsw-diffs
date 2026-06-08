## MarkupUI

> `/System/Library/PrivateFrameworks/MarkupUI.framework/MarkupUI`

```diff

-560.4.2.0.0
-  __TEXT.__text: 0x2aacc
-  __TEXT.__auth_stubs: 0xfe0
-  __TEXT.__objc_methlist: 0x3d4c
+577.0.0.0.0
+  __TEXT.__text: 0x28cc8
+  __TEXT.__objc_methlist: 0x3d64
   __TEXT.__const: 0x120
-  __TEXT.__gcc_except_tab: 0x5b4
-  __TEXT.__cstring: 0x299a
+  __TEXT.__gcc_except_tab: 0x5c0
+  __TEXT.__cstring: 0x29c4
   __TEXT.__dlopen_cstrs: 0x112
-  __TEXT.__unwind_info: 0xb70
-  __TEXT.__objc_classname: 0x610
-  __TEXT.__objc_methname: 0xbf16
-  __TEXT.__objc_methtype: 0x292f
-  __TEXT.__objc_stubs: 0x9340
-  __DATA_CONST.__got: 0x6c0
+  __TEXT.__unwind_info: 0xad8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x8c0
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d80
+  __DATA_CONST.__objc_selrefs: 0x2d90
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x800
+  __DATA_CONST.__got: 0x6c0
   __AUTH_CONST.__const: 0x130
   __AUTH_CONST.__cfstring: 0x2620
-  __AUTH_CONST.__objc_const: 0x4a30
+  __AUTH_CONST.__objc_const: 0x4a40
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x910
   __DATA.__objc_ivar: 0x288
   __DATA.__data: 0xa58

   - /System/Library/PrivateFrameworks/VisionKitCore.framework/VisionKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 687BF69F-64B6-3007-89FC-B2FB35D3F5B0
+  UUID: 618936F7-2381-30A8-8F74-38FC7E817797
   Functions: 1018
-  Symbols:   4338
-  CStrings:  2902
+  Symbols:   4342
+  CStrings:  700
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x6
- _objc_retain_x10
Functions:
~ -[MUImageReader readArchivedModelDataFromImageData:] : 108 -> 104
~ -[MUImageReader readArchivedModelDataFromImageURL:] : 108 -> 104
~ -[MUImageReader readAnnotationsFromArchivedModelData:toController:] : 92 -> 88
~ -[MUImageReader _readAnnotationsFromDataProvider:] : 380 -> 356
~ -[MUImageReader readBaseImageFromData:baseWasValid:] : 140 -> 132
~ -[MUImageReader readBaseImageFromImageAtURL:baseWasValid:] : 140 -> 132
~ -[MUImageReader _readBaseImageFromDataProvider:providerSource:baseWasValid:] : 1136 -> 1100
~ +[MUImageReader hasPrivateImageMetadata:] : 348 -> 340
~ ___41+[MUImageReader hasPrivateImageMetadata:]_block_invoke : 180 -> 176
~ +[MUImageReader cleanImageMetadataFromData:] : 696 -> 656
~ ___44+[MUImageReader cleanImageMetadataFromData:]_block_invoke : 188 -> 184
~ -[MUImageReader _readDataFromTagAtPath:inMetadata:] : 188 -> 192
~ -[MUDocumentPickerViewController presentationControllerDidDismiss:] : 120 -> 116
~ -[MUQuickLookContentEditorViewController init] : 116 -> 112
~ -[MUQuickLookContentEditorViewController _updatePeekSize] : 308 -> 292
~ +[MUQuickLookContentEditorViewController suggestedContentSizeForURL:] : 316 -> 308
~ +[MUQuickLookContentEditorViewController suggestedContentSizeForData:] : 316 -> 308
~ +[MUQuickLookContentEditorViewController _suggestedContentSizeForPDF:] : 132 -> 128
~ -[MUQuickLookContentEditorViewController loadWithData:archivedModelData:placeholderImage:completionHandler:] : 124 -> 120
~ -[MUQuickLookContentEditorViewController loadWithURL:archivedModelData:placeholderImage:completionHandler:] : 124 -> 120
~ -[MUQuickLookContentEditorViewController _handleLoadingWithCompletion:] : 300 -> 288
~ -[MUQuickLookContentEditorViewController _canShowWhileLocked] : 104 -> 100
~ -[MUQuickLookContentEditorViewController traitCollectionDidChange:] : 332 -> 320
~ -[MUQuickLookContentEditorViewController willTransitionToTraitCollection:withTransitionCoordinator:] : 240 -> 244
~ -[MUQuickLookContentEditorViewController PDFView:allowsFormFillingMode:forPage:] : 148 -> 144
~ -[MUQuickLookContentEditorViewController annotationController:detectedEditOfType:] : 252 -> 232
~ -[MUQuickLookContentEditorViewController contentControllerDidUnlockDocument:] : 120 -> 116
~ -[MUQuickLookContentEditorViewController setAnnotationEditingEnabled:] : 128 -> 124
~ -[MUQuickLookContentEditorViewController transitioningView] : 92 -> 84
~ -[MUQuickLookContentEditorViewController documentIsLocked] : 76 -> 72
~ -[MUQuickLookContentEditorViewController canEncryptDocument] : 100 -> 96
~ -[MUQuickLookContentEditorViewController presentationMode] : 16 -> 20
~ -[MUQuickLookContentEditorViewController flattenImageForAnalysis] : 204 -> 200
~ -[MUQuickLookContentEditorViewController updateForFullScreen:animated:] : 292 -> 288
~ -[MUQuickLookContentEditorViewController shouldHideMarkupOverlays:animated:] : 136 -> 132
~ -[MUQuickLookContentEditorViewController findInteraction] : 108 -> 100
~ -[MUQuickLookContentEditorViewController acceptSingleTouch:] : 124 -> 120
~ -[MUQuickLookContentEditorViewController updateThumbnailView] : 88 -> 84
~ -[MUQuickLookContentEditorViewController isInteractionActive] : 60 -> 56
~ -[MUQuickLookContentEditorViewController hasResultsForVisualSearch] : 60 -> 56
~ -[MUQuickLookContentEditorViewController infoButtonTapped] : 68 -> 64
~ -[MUQuickLookContentEditorViewController canEditContent] : 104 -> 100
~ -[MUQuickLookContentEditorViewController allowsEditing] : 104 -> 100
~ -[MUQuickLookContentEditorViewController getMenuElementsForPage:] : 2180 -> 2132
~ -[MUQuickLookContentEditorViewController convertToPDFAndWrite:completionHandler:] : 264 -> 272
~ -[MUQuickLookContentEditorViewController documentCameraViewControllerDidCancel:] : 200 -> 192
~ -[MUQuickLookContentEditorViewController documentCameraViewController:didFinishWithScan:] : 240 -> 248
~ ___89-[MUQuickLookContentEditorViewController documentCameraViewController:didFinishWithScan:]_block_invoke_3 : 140 -> 136
~ -[MUQuickLookContentEditorViewController sharedSerialPagesEditionQueue] : 84 -> 68
~ ___71-[MUQuickLookContentEditorViewController sharedSerialPagesEditionQueue]_block_invoke : 140 -> 132
~ -[MUQuickLookContentEditorViewController pdfPageOptionsForImageRef:withPreviousPage:] : 260 -> 252
~ -[MUQuickLookContentEditorViewController insertPages:atIndexes:inDocument:] : 500 -> 476
~ -[MUQuickLookContentEditorViewController documentPicker:didPickDocumentsAtURLs:] : 176 -> 160
~ -[MUQuickLookContentEditorViewController documentPickerWasCancelled:] : 280 -> 268
~ -[MUQuickLookContentEditorViewController find:] : 160 -> 148
~ -[MUQuickLookContentEditorViewController findPrevious:] : 160 -> 148
~ -[MUQuickLookContentEditorViewController findNext:] : 160 -> 148
~ -[MUQuickLookContentEditorViewController isVisualSearchEnabled] : 60 -> 56
~ -[MUQuickLookContentEditorViewController filledInfoButtonGlyphName] : 84 -> 76
~ -[MUQuickLookContentEditorViewController infoButtonGlyphName] : 84 -> 76
~ -[MUQuickLookContentEditorViewController stopImageAnalysis] : 68 -> 64
~ -[MUQuickLookContentEditorViewController shouldHighlightTextAndDDAfterNextAnalysis] : 60 -> 56
~ -[MUQuickLookContentEditorViewController setShouldHighlightTextAndDDAfterNextAnalysis:] : 84 -> 80
~ -[MUQuickLookContentEditorViewController shouldEnterVisualSearchAfterNextAnalysis] : 60 -> 56
~ -[MUQuickLookContentEditorViewController setShouldEnterVisualSearchAfterNextAnalysis:] : 84 -> 80
~ -[MUQuickLookContentEditorViewController shouldUpliftSubjectAfterNextAnalysis] : 60 -> 56
~ -[MUQuickLookContentEditorViewController setShouldUpliftSubjectAfterNextAnalysis:] : 84 -> 80
~ -[MUQuickLookContentEditorViewController imageForAnalysis] : 156 -> 144
~ -[MUQuickLookContentEditorViewController clientPreviewOptions] : 84 -> 76
~ -[MUQuickLookContentEditorViewController imageAnalyzerWantsUpdateInfoButtonWithAnimation:] : 92 -> 88
~ -[MUQuickLookContentEditorViewController imageAnalysisInteractionWillPresentVisualSearchController] : 88 -> 84
~ -[MUQuickLookContentEditorViewController imageAnalysisInteractionDidDismissVisualSearchController] : 88 -> 84
~ -[MUQuickLookContentEditorViewController _editedImageAnalysisQueue] : 84 -> 68
~ ___67-[MUQuickLookContentEditorViewController _editedImageAnalysisQueue]_block_invoke : 140 -> 132
~ -[MUQuickLookContentEditorViewController _adjustImageInteractionForScrollEvent:] : 104 -> 100
~ -[MUQuickLookContentEditorViewController _setupAndStartImageAnalysisIfNeeded] : 280 -> 268
~ -[MUQuickLookContentEditorViewController _imageAnalysisOverlayAcceptSingleTouch:] : 248 -> 240
~ -[MUQuickLookContentEditorViewController _insertPagesFromProvidedPDFDocument:toPDFDocument:atPageIndex:] : 700 -> 668
~ -[MUQuickLookContentEditorViewController _insertPagesFromFileURLs:afterPage:] : 352 -> 344
~ ___77-[MUQuickLookContentEditorViewController _insertPagesFromFileURLs:afterPage:]_block_invoke : 512 -> 520
~ -[MUQuickLookContentEditorViewController _insertFileAtURL:type:afterPage:completionHandler:] : 540 -> 544
~ -[MUQuickLookContentEditorViewController _insertPDFDocumentWithURL:afterPage:completionHandler:] : 288 -> 296
~ ___96-[MUQuickLookContentEditorViewController _insertPDFDocumentWithURL:afterPage:completionHandler:]_block_invoke : 160 -> 156
~ -[MUQuickLookContentEditorViewController _insertImageWithURL:afterPage:completionHandler:] : 616 -> 604
~ ___90-[MUQuickLookContentEditorViewController _insertImageWithURL:afterPage:completionHandler:]_block_invoke : 252 -> 240
~ -[MUQuickLookContentEditorViewController _convertToPDFAndWrite:completionHandler:] : 1056 -> 996
~ -[MUQuickLookContentEditorViewController _detectedEditEnablingMarkup:] : 152 -> 148
~ -[MUQuickLookContentEditorViewController _loadSourceContentWithCompletion:] : 192 -> 196
~ ___75-[MUQuickLookContentEditorViewController _loadSourceContentWithCompletion:]_block_invoke : 128 -> 124
~ -[MUQuickLookContentEditorViewController _setAsPDFViewDelegatePrivateIfNecessary] : 268 -> 260
~ -[MUQuickLookContentEditorViewController _resetOriginalDelegate] : 140 -> 136
~ -[MUQuickLookContentEditorViewController _updateAnalysisButtonsContainerConstraints] : 188 -> 168
~ -[MUQuickLookContentEditorViewController _updateThumbnailViewWithTraitCollection:] : 360 -> 348
~ -[MUQuickLookContentEditorViewController _flattenImageForAnalysis] : 256 -> 252
~ ___66-[MUQuickLookContentEditorViewController _flattenImageForAnalysis]_block_invoke : 72 -> 68
~ -[MUQuickLookContentEditorViewController _setPresentationModeForImageContent:] : 216 -> 212
~ -[MUQuickLookContentEditorViewController _setPresentationModeForPDFContent:] : 384 -> 360
~ -[MUQuickLookContentEditorViewController _registerActionNotEnablingMarkup:] : 168 -> 160
~ -[MUQuickLookContentEditorViewController _rotatePage:clockwise:] : 376 -> 344
~ -[MUQuickLookContentEditorViewController _insertBlankPageAfterPage:] : 376 -> 372
~ ___68-[MUQuickLookContentEditorViewController _insertBlankPageAfterPage:]_block_invoke : 100 -> 96
~ ___71-[MUQuickLookContentEditorViewController _insertPageFromFileAfterPage:]_block_invoke : 264 -> 260
~ -[MUQuickLookContentEditorViewController _insertPage:atIndex:] : 116 -> 112
~ -[MUQuickLookContentEditorViewController _insertBlankPage:atIndex:] : 400 -> 372
~ -[MUQuickLookContentEditorViewController _insertDeletedPage:atIndex:] : 400 -> 372
~ -[MUQuickLookContentEditorViewController _deletePage:] : 188 -> 180
~ -[MUQuickLookContentEditorViewController _deletePages:inDocument:] : 724 -> 684
~ ___66-[MUQuickLookContentEditorViewController _deletePages:inDocument:]_block_invoke : 132 -> 128
~ -[MUQuickLookContentEditorViewController supportedUTTypes] : 84 -> 68
~ ___58-[MUQuickLookContentEditorViewController supportedUTTypes]_block_invoke : 144 -> 140
~ ___65-[MUQuickLookContentEditorViewController _presentDocumentPicker:]_block_invoke : 244 -> 236
~ -[MUQuickLookContentEditorViewController _presentDocumentScannerAfterPage:] : 500 -> 508
~ ___75-[MUQuickLookContentEditorViewController _presentDocumentScannerAfterPage:]_block_invoke : 740 -> 700
~ ___75-[MUQuickLookContentEditorViewController _presentDocumentScannerAfterPage:]_block_invoke_2 : 172 -> 168
~ ___75-[MUQuickLookContentEditorViewController _presentDocumentScannerAfterPage:]_block_invoke_3 : 276 -> 260
~ -[MUQuickLookContentEditorViewController _hasPDFContent] : 80 -> 76
~ -[MUQuickLookContentEditorViewController _hasImageContent] : 80 -> 76
~ -[MUQuickLookContentEditorViewController importHandler] : 16 -> 20
~ -[MUQuickLookContentEditorViewController scanPDFHandler] : 16 -> 20
~ -[MUQuickLookContentEditorViewController scanImageToPDFConversionHandler] : 16 -> 20
~ -[MUQuickLookContentEditorViewController actionsNotEnablingMarkup] : 16 -> 20
~ -[MUQuickLookContentEditorViewController setActionsNotEnablingMarkup:] : 80 -> 20
~ -[MUQuickLookContentEditorViewController imageAnalysisManager] : 16 -> 20
~ -[MUQuickLookContentEditorViewController setImageAnalysisManager:] : 80 -> 20
~ -[MUQuickLookContentEditorViewController latestImageForAnalysis] : 16 -> 20
~ -[MUQuickLookContentEditorViewController setLatestImageForAnalysis:] : 80 -> 20
~ -[MUQuickLookContentEditorViewController didAppearOnce] : 20 -> 24
~ -[MUQuickLookContentEditorViewController setDidAppearOnce:] : 16 -> 20
~ -[MUQuickLookContentEditorViewController delegateRespondsToDetectedFormInContent] : 20 -> 24
~ -[MUQuickLookContentEditorViewController setDelegateRespondsToDetectedFormInContent:] : 16 -> 20
~ -[MUQuickLookContentEditorViewController formDetectedInDocument] : 20 -> 24
~ -[MUQuickLookContentEditorViewController setFormDetectedInDocument:] : 16 -> 20
~ -[MUQuickLookContentEditorViewController pdfViewDelegateProxy] : 16 -> 20
~ -[MUQuickLookContentEditorViewController setPdfViewDelegateProxy:] : 80 -> 20
~ +[MUCGPDFPopupAnnotationAdaptor _concreteAKAnnotationWithCGPDFAnnotation:ofPage:] : 236 -> 228
~ +[MUCGPDFPopupAnnotationAdaptor _concreteDictionaryRepresentationOfAKAnnotation:forPage:] : 468 -> 452
~ +[MUCGPDFLineAnnotationAdaptor _concreteDictionaryRepresentationOfAKAnnotation:forPage:] : 888 -> 864
~ -[MUDelegateProxy methodSignatureForSelector:] : 172 -> 164
~ +[QuickLookContentEditorBannerConfiguration configurationWithImage:title:subtitle:primaryAction:dismissAction:] : 200 -> 216
~ -[QuickLookContentEditorBannerConfiguration setImage:] : 64 -> 12
~ -[QuickLookContentEditorBannerConfiguration setPrimaryAction:] : 64 -> 12
~ -[QuickLookContentEditorBannerConfiguration setDismissAction:] : 64 -> 12
~ -[MarkupViewController _commonInit] : 420 -> 444
~ -[MarkupViewController _canShowWhileLocked] : 104 -> 100
~ -[MarkupViewController documentDidCloseTeardown] : 820 -> 748
~ -[MarkupViewController viewDidLoad] : 616 -> 556
~ -[MarkupViewController viewWillAppear:] : 132 -> 124
~ -[MarkupViewController viewDidAppear:] : 260 -> 256
~ -[MarkupViewController canBecomeFirstResponder] : 172 -> 168
~ -[MarkupViewController viewDidLayoutSubviews] : 112 -> 108
~ -[MarkupViewController sketchOverlayInsets] : 172 -> 164
~ -[MarkupViewController traitCollectionDidChange:] : 276 -> 260
~ -[MarkupViewController preferredStatusBarStyle] : 64 -> 60
~ ___41-[MarkupViewController _useLegacyToolbar]_block_invoke : 116 -> 108
~ -[MarkupViewController _setLegacyToolbarHidden:animated:] : 428 -> 408
~ ___57-[MarkupViewController _setLegacyToolbarHidden:animated:]_block_invoke : 104 -> 100
~ ___57-[MarkupViewController _setLegacyToolbarHidden:animated:]_block_invoke_2 : 100 -> 96
~ -[MarkupViewController setToolbarHidden:animated:] : 428 -> 408
~ -[MarkupViewController setToolbarPosition:] : 116 -> 120
~ -[MarkupViewController setShowThumbnailViewForMultipage:] : 156 -> 152
~ -[MarkupViewController setFixedThumbnailView:] : 172 -> 164
~ -[MarkupViewController fixedThumbnailView] : 136 -> 128
~ -[MarkupViewController isTouchInThumbnailView:] : 156 -> 148
~ -[MarkupViewController setFileURL:withArchivedModelData:placeholderImage:] : 244 -> 260
~ -[MarkupViewController _setFileURL:withArchivedModelData:withCompletion:] : 356 -> 368
~ ___73-[MarkupViewController _setFileURL:withArchivedModelData:withCompletion:]_block_invoke : 72 -> 16
~ -[MarkupViewController setImage:withArchivedModelData:placeholderImage:] : 332 -> 340
~ -[MarkupViewController setData:withArchivedModelData:placeholderImage:] : 332 -> 340
~ -[MarkupViewController outputContentType] : 332 -> 336
~ -[MarkupViewController outputType] : 84 -> 76
~ -[MarkupViewController writeToURL:embeddingSourceImageAndEditModel:options:error:] : 204 -> 200
~ -[MarkupViewController dataRepresentationEmbeddingSourceImageAndEditModel:error:] : 432 -> 396
~ __MUWriteOutputToTemp : 236 -> 224
~ -[MarkupViewController dataRepresentationEmbeddingSourceImageAndEditModel:withDestinationType:error:] : 432 -> 396
~ -[MarkupViewController createArchivedModelData] : 132 -> 124
~ -[MarkupViewController finalizeCrop] : 120 -> 124
~ -[MarkupViewController cancel:] : 632 -> 592
~ -[MarkupViewController _cancel] : 200 -> 188
~ -[MarkupViewController validateRedo:] : 92 -> 88
~ -[MarkupViewController validateUndo:] : 92 -> 88
~ -[MarkupViewController undo:] : 100 -> 96
~ -[MarkupViewController redo:] : 100 -> 96
~ -[MarkupViewController revert] : 188 -> 172
~ -[MarkupViewController _writeToDataConsumer:embedSourceImageAndEditModel:options:error:] : 704 -> 668
~ -[MarkupViewController _updateAndLoadSourceContent:withArchivedModelData:withCompletion:] : 276 -> 280
~ ___89-[MarkupViewController _updateAndLoadSourceContent:withArchivedModelData:withCompletion:]_block_invoke : 548 -> 516
~ -[MarkupViewController _loadSourceContentWithCompletion:] : 848 -> 800
~ ___57-[MarkupViewController _loadSourceContentWithCompletion:]_block_invoke : 188 -> 176
~ -[MarkupViewController allEditingDisabled] : 60 -> 56
~ -[MarkupViewController setAllEditingDisabled:] : 84 -> 80
~ -[MarkupViewController setAnnotationEditingEnabled:] : 156 -> 148
~ -[MarkupViewController setFormFillingEnabled:didUseBanner:] : 168 -> 156
~ -[MarkupViewController restoreToolModeForContentType] : 212 -> 204
~ -[MarkupViewController annotationEditingEnabled] : 60 -> 56
~ -[MarkupViewController formFillingEnabled] : 60 -> 56
~ -[MarkupViewController _saveEditing:] : 1176 -> 1124
~ -[MarkupViewController setSourceContent:withArchivedModelData:] : 2236 -> 2100
~ -[MarkupViewController _pdfView] : 160 -> 148
~ -[MarkupViewController _pdfDocument] : 160 -> 148
~ -[MarkupViewController thumbnailViewStyle] : 136 -> 128
~ -[MarkupViewController setThumbnailViewStyle:] : 172 -> 164
~ -[MarkupViewController allowsThumbnailViewPageReordering] : 136 -> 128
~ -[MarkupViewController setAllowsThumbnailViewPageReordering:] : 172 -> 164
~ -[MarkupViewController contentViewScrollView] : 84 -> 76
~ -[MarkupViewController imageViewCombinedContentView] : 124 -> 116
~ -[MarkupViewController currentPDFPageIndex] : 136 -> 128
~ -[MarkupViewController setCurrentPDFPageIndex:] : 256 -> 236
~ -[MarkupViewController filteredToolbarItemsForItems:fromController:] : 56 -> 8
~ -[MarkupViewController setForcesPDFViewTopAlignment:] : 192 -> 188
~ -[MarkupViewController setShowShareButtonInToolbar:] : 116 -> 112
~ -[MarkupViewController annotationController] : 84 -> 76
~ +[MarkupViewController _maxImageDimensionInView] : 132 -> 124
~ -[MarkupViewController _setupInitialBaseModelScaleFactorWithScreenSize:windowDecorationSize:] : 164 -> 156
~ -[MarkupViewController _shouldShowUndoRedoButtonsInNavigationBar] : 120 -> 112
~ -[MarkupViewController _updateundoBarButtonWithController:] : 684 -> 628
~ -[MarkupViewController _presentPlaceholderImage] : 544 -> 488
~ -[MarkupViewController _cleanupPlaceholderImage] : 92 -> 88
~ -[MarkupViewController _startObservingAnnotationController] : 188 -> 180
~ -[MarkupViewController _stopObservingAnnotationController] : 184 -> 176
~ -[MarkupViewController observeValueForKeyPath:ofObject:change:context:] : 456 -> 436
~ -[MarkupViewController _installContentViewControllerForUTI:] : 1064 -> 1008
~ -[MarkupViewController _setupAnnotationController] : 1384 -> 1248
~ -[MarkupViewController _createCancelDoneNavBar] : 1040 -> 956
~ -[MarkupViewController adjustContentInsetsForBars] : 848 -> 780
~ -[MarkupViewController _updateConstraintsForBarPosition:] : 780 -> 688
~ -[MarkupViewController _updateAppearanceForTraitCollection:] : 472 -> 420
~ -[MarkupViewController setNavBar:] : 128 -> 116
~ -[MarkupViewController _updateNavBarProperties] : 300 -> 276
~ -[MarkupViewController setBackgroundColor:] : 204 -> 192
~ -[MarkupViewController backgroundColor] : 64 -> 20
~ -[MarkupViewController _effectiveBackgroundColor] : 200 -> 176
~ -[MarkupViewController toolbarItemTintColor] : 64 -> 20
~ -[MarkupViewController setToolbarItemTintColor:] : 216 -> 204
~ -[MarkupViewController _effectiveToolbarItemTintColor] : 164 -> 144
~ -[MarkupViewController toolbarTintColor] : 64 -> 20
~ -[MarkupViewController setToolbarTintColor:] : 216 -> 204
~ -[MarkupViewController _effectiveToolbarTintColor] : 160 -> 148
~ -[MarkupViewController navBarTitleColor] : 64 -> 20
~ -[MarkupViewController setNavBarTitleColor:] : 280 -> 272
~ -[MarkupViewController _effectiveNavBarTitleColor] : 200 -> 176
~ -[MarkupViewController delete:] : 152 -> 140
~ -[MarkupViewController duplicate:] : 152 -> 140
~ -[MarkupViewController editTextAnnotation:] : 152 -> 140
~ -[MarkupViewController motionEnded:withEvent:] : 1312 -> 1276
~ -[MarkupViewController _showTextStyleOptions:] : 152 -> 140
~ -[MarkupViewController canPerformAction:withSender:] : 308 -> 292
~ -[MarkupViewController positionSketchOverlay:forContentViewController:] : 596 -> 560
~ -[MarkupViewController annotationControllerOfContentViewController:willSetToolbarItems:] : 408 -> 380
~ -[MarkupViewController contentViewController:shouldHandleURL:] : 124 -> 120
~ -[MarkupViewController annotationController:detectedEditOfType:] : 120 -> 116
~ -[MarkupViewController controllerWillShowSignatureCaptureView:] : 20 -> 24
~ -[MarkupViewController controllerWillDismissSignatureCaptureView:] : 16 -> 20
~ -[MarkupViewController controllerWillShowSignatureManagerView:] : 20 -> 24
~ -[MarkupViewController controllerWillDismissSignatureManagerView:] : 16 -> 20
~ -[MarkupViewController toolbar] : 124 -> 112
~ -[MarkupViewController _toolbarShareButtonTapped:] : 112 -> 108
~ -[MarkupViewController toolbarController:positionForBar:] : 16 -> 20
~ -[MarkupViewController getMenuElementsForPage:] : 144 -> 136
~ -[MarkupViewController akUndoManager] : 16 -> 20
~ -[MarkupViewController setAkUndoManager:] : 80 -> 20
~ -[MarkupViewController allowShakeToUndo] : 16 -> 20
~ -[MarkupViewController setAllowShakeToUndo:] : 16 -> 20
~ -[MarkupViewController centersIgnoringContentInsets] : 16 -> 20
~ -[MarkupViewController setCentersIgnoringContentInsets:] : 16 -> 20
~ -[MarkupViewController encryptPrivateMetadata] : 20 -> 24
~ -[MarkupViewController setEncryptPrivateMetadata:] : 16 -> 20
~ -[MarkupViewController forcesPDFViewTopAlignment] : 16 -> 20
~ -[MarkupViewController hostProcessBundleIdentifier] : 16 -> 20
~ -[MarkupViewController inkStyle] : 16 -> 20
~ -[MarkupViewController setInkStyle:] : 16 -> 20
~ -[MarkupViewController navBar] : 16 -> 20
~ -[MarkupViewController isNavigationModeHorizontal] : 16 -> 20
~ -[MarkupViewController isShapeDetectionEnabled] : 16 -> 20
~ -[MarkupViewController showShareButtonInToolbar] : 16 -> 20
~ -[MarkupViewController showThumbnailViewForMultipage] : 16 -> 20
~ -[MarkupViewController isThumbnailViewHidden] : 16 -> 20
~ -[MarkupViewController isToolbarHidden] : 16 -> 20
~ -[MarkupViewController toolbarPosition] : 16 -> 20
~ -[MarkupViewController needToPerformFullTeardown] : 20 -> 24
~ -[MarkupViewController setNeedToPerformFullTeardown:] : 16 -> 20
~ -[MarkupViewController needToPerformDocumentClosedTeardown] : 20 -> 24
~ -[MarkupViewController setNeedToPerformDocumentClosedTeardown:] : 16 -> 20
~ -[MarkupViewController isObservingAKCurrentPageIndex] : 20 -> 24
~ -[MarkupViewController setObservingAKCurrentPageIndex:] : 16 -> 20
~ -[MarkupViewController sourceContent] : 16 -> 20
~ -[MarkupViewController setSourceContent:] : 80 -> 20
~ -[MarkupViewController initialContentScale] : 16 -> 20
~ -[MarkupViewController setInitialContentScale:] : 16 -> 20
~ -[MarkupViewController setToolbar:] : 80 -> 20
~ -[MarkupViewController navItem] : 16 -> 20
~ -[MarkupViewController setNavItem:] : 80 -> 20
~ -[MarkupViewController alreadyLoggedSavingForThisDocument] : 16 -> 20
~ -[MarkupViewController setAlreadyLoggedSavingForThisDocument:] : 16 -> 20
~ -[MarkupViewController needsToolPickerVisibleWhenAnnotationControllerIsAvailable] : 16 -> 20
~ -[MarkupViewController setNeedsToolPickerVisibleWhenAnnotationControllerIsAvailable:] : 16 -> 20
~ -[MarkupViewController preferredFileDisplayName] : 16 -> 20
~ -[MarkupViewController useFancyTransition] : 20 -> 24
~ -[MarkupViewController setUseFancyTransition:] : 16 -> 20
~ -[MarkupViewController isAnimatingMarkupExtensionTransition] : 20 -> 24
~ -[MarkupViewController setIsAnimatingMarkupExtensionTransition:] : 16 -> 20
~ -[MarkupViewController userDidCancel] : 20 -> 24
~ -[MarkupViewController setUserDidCancel:] : 16 -> 20
~ -[MarkupViewController showAsFormSheet] : 20 -> 24
~ -[MarkupViewController setShowAsFormSheet:] : 16 -> 20
~ -[MarkupViewController originalImageDescription] : 16 -> 20
~ +[MUImageDownsamplingUtilities _sourceContentType:] : 92 -> 88
~ +[MUImageDownsamplingUtilities _newImageSourceWithSourceContent:] : 128 -> 124
~ +[MUImageDownsamplingUtilities _shouldFlattenEXIFOrientation:andDownsample:sourceContent:] : 424 -> 420
~ _maxImageArea : 92 -> 88
~ +[MUImageDownsamplingUtilities _flattenEXIFOrientation:withDownsampling:sourceContent:withContentType:] : 864 -> 828
~ +[MUImageDownsamplingUtilities _flattenRotation:withDownsampling:sourceImage:] : 340 -> 332
~ +[MUImageDownsamplingUtilities _flattenEXIFOrientationForHEICData:] : 804 -> 792
~ +[MUImageDownsamplingUtilities _flattenEXIFOrientationOfImage:toDestination:] : 508 -> 500
~ +[MUImageDownsamplingUtilities _uniqueTemporaryDirectory] : 372 -> 340
~ +[MUImageDownsamplingUtilities _preferredFileDisplayNameForSourceContent:] : 232 -> 212
~ +[MUPDFUtilities createPDFDateString:] : 276 -> 260
~ __dictionaryApplierFunction : 468 -> 452
~ __objectFromPDFObject : 596 -> 572
~ -[MUImageContentViewController initWithSourceContent:archivedDataModel:delegate:] : 380 -> 388
~ -[MUImageContentViewController imageForAnalysis] : 84 -> 76
~ -[MUImageContentViewController viewDidLoad] : 1288 -> 1188
~ -[MUImageContentViewController visibleContentRect] : 140 -> 132
~ -[MUImageContentViewController visibleContentRectInCoordinateSpace:] : 164 -> 156
~ -[MUImageContentViewController contentSnapshot] : 88 -> 80
~ -[MUImageContentViewController setup] : 1092 -> 968
~ -[MUImageContentViewController teardown] : 680 -> 616
~ -[MUImageContentViewController loadContentWithCompletionBlock:] : 108 -> 104
~ -[MUImageContentViewController setEdgeInsets:] : 240 -> 232
~ -[MUImageContentViewController _installOverlayOfController:forPageAtIndex:] : 436 -> 420
~ -[MUImageContentViewController _uninstallOverlayOfController:forPageAtIndex:] : 136 -> 124
~ -[MUImageContentViewController uninstallAllAnnotationControllerOverlays] : 208 -> 196
~ -[MUImageContentViewController canEditContent] : 100 -> 92
~ -[MUImageContentViewController _setImage:withCompletionHandler:] : 784 -> 788
~ ___64-[MUImageContentViewController _setImage:withCompletionHandler:]_block_invoke : 592 -> 568
~ ___64-[MUImageContentViewController _setImage:withCompletionHandler:]_block_invoke_2 : 132 -> 124
~ -[MUImageContentViewController viewDidLayoutSubviews] : 452 -> 444
~ ___53-[MUImageContentViewController viewDidLayoutSubviews]_block_invoke : 112 -> 116
~ -[MUImageContentViewController _setupScrollViewForImageOfScaledSize:] : 276 -> 260
~ -[MUImageContentViewController _downsampleImageForDisplay:fromImageSource:withCompletionHandler:] : 836 -> 816
~ ___97-[MUImageContentViewController _downsampleImageForDisplay:fromImageSource:withCompletionHandler:]_block_invoke : 792 -> 768
~ -[MUImageContentViewController _zoomToFitZoomFactorIncludingScrollViewEdgeInsets] : 144 -> 148
~ -[MUImageContentViewController _zoomToFitZoomFactorInBounds:] : 168 -> 172
~ -[MUImageContentViewController _doubleTap:] : 312 -> 316
~ -[MUImageContentViewController _zoomRectForScale:withCenter:] : 132 -> 128
~ -[MUImageContentViewController _imageIsSmallerThanView] : 108 -> 116
~ ___83-[MUImageContentViewController viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke : 140 -> 136
~ -[MUImageContentViewController _prepareToRotate] : 224 -> 232
~ -[MUImageContentViewController _recoverFromRotation] : 348 -> 364
~ -[MUImageContentViewController _updateMinMaxZoomFactor] : 188 -> 204
~ -[MUImageContentViewController _annotationRectInOverlay:pageIndex:] : 324 -> 316
~ -[MUImageContentViewController _annotationWillBeginEditing:] : 124 -> 116
~ -[MUImageContentViewController _pageIndexForAnnotation:] : 188 -> 168
~ -[MUImageContentViewController _keyboardWillShow:] : 108 -> 104
~ -[MUImageContentViewController _keyboardWillHide:] : 96 -> 92
~ -[MUImageContentViewController _adjustScrollViewForKeyboardNotification:] : 600 -> 552
~ -[MUImageContentViewController adjustScrollViewToAccomodateKeyboardStartingFrame:endingFrame:annotationFrame:inOverlayView:withAnimationDuration:curve:] : 980 -> 972
~ -[MUImageContentViewController scrollViewWillBeginDragging:] : 192 -> 180
~ -[MUImageContentViewController scrollViewWillBeginZooming:withView:] : 244 -> 240
~ -[MUImageContentViewController scrollViewDidScroll:] : 188 -> 176
~ -[MUImageContentViewController scrollViewDidZoom:] : 188 -> 176
~ -[MUImageContentViewController scrollViewShouldScrollToTop:] : 180 -> 172
~ -[MUImageContentViewController convertPoint:fromModelToOverlayWithPageIndex:forAnnotationController:] : 160 -> 152
~ -[MUImageContentViewController maxPageRectWithPageIndex:forAnnotationController:] : 124 -> 120
~ -[MUImageContentViewController newContentSnapshotPDFDataIncludingAdornments:atScale:inRect:onOverlayAtPageIndex:forAnnotationController:] : 1056 -> 1040
~ -[MUImageContentViewController undoManagerForAnnotationController:] : 92 -> 84
~ -[MUImageContentViewController popoverPresentingViewControllerForAnnotationController:] : 116 -> 108
~ -[MUImageContentViewController installDrawingGestureRecognizer:forPageAtIndex:forAnnotationController:] : 100 -> 96
~ -[MUImageContentViewController uninstallDrawingGestureRecognizer:forPageAtIndex:forAnnotationController:] : 96 -> 88
~ -[MUImageContentViewController updateDrawingGestureRecognizer:forPageAtIndex:withPriority:forAnnotationController:] : 1012 -> 988
~ -[MUImageContentViewController modelBaseScaleFactorOfPageAtIndex:forAnnotationController:] : 92 -> 88
~ -[MUImageContentViewController controller:willSetToolbarItems:] : 120 -> 112
~ -[MUImageContentViewController positionSketchOverlay:forAnnotationController:] : 104 -> 100
~ -[MUImageContentViewController layerContainingQuickBackgroundForLoupeOnOverlayAtPageIndex:forAnnotationController:] : 84 -> 76
~ -[MUImageContentViewController controllerDidEnterToolMode:] : 144 -> 132
~ -[MUImageContentViewController controllerDidExitToolMode:] : 144 -> 132
~ -[MUImageContentViewController editDetectedForAnnotationController:] : 100 -> 96
~ -[MUImageContentViewController editCheckpointReachedForAnnotationController:] : 100 -> 96
~ -[MUImageContentViewController penStrokeCompletedForAnnotationController:] : 100 -> 96
~ -[MUImageContentViewController controllerWillShowSignatureCaptureView:] : 100 -> 96
~ -[MUImageContentViewController controllerWillDismissSignatureCaptureView:] : 100 -> 96
~ -[MUImageContentViewController controllerWillShowSignatureManagerView:] : 100 -> 96
~ -[MUImageContentViewController controllerWillDismissSignatureManagerView:] : 100 -> 96
~ -[MUImageContentViewController originalImageDescription] : 120 -> 112
~ -[MUImageContentViewController enableHDRAnnotations] : 112 -> 108
~ -[MUImageContentViewController centersIgnoringContentInsets] : 16 -> 20
~ -[MUImageContentViewController setCentersIgnoringContentInsets:] : 16 -> 20
~ -[MUImageContentViewController tentativePlaceholderImage] : 16 -> 20
~ -[MUImageContentViewController setTentativePlaceholderImage:] : 80 -> 20
~ -[MUImageContentViewController maxImageDimension] : 16 -> 20
~ -[MUImageContentViewController setMaxImageDimension:] : 16 -> 20
~ -[MUImageContentViewController combinedContentView] : 16 -> 20
~ -[MUImageContentViewController setCombinedContentView:] : 80 -> 20
~ -[MUImageContentViewController inkStyle] : 16 -> 20
~ -[MUImageContentViewController scrollView] : 16 -> 20
~ -[MUImageContentViewController setScrollView:] : 80 -> 20
~ -[MUImageContentViewController imageView] : 16 -> 20
~ -[MUImageContentViewController setImageView:] : 80 -> 20
~ -[MUImageContentViewController downsampledImageScale] : 16 -> 20
~ -[MUImageContentViewController setDownsampledImageScale:] : 16 -> 20
~ -[MUImageContentViewController usePlaceholderAsDisplayImageIfPossible] : 16 -> 20
~ -[MUImageContentViewController setUsePlaceholderAsDisplayImageIfPossible:] : 16 -> 20
~ -[MUImageContentViewController inDoubleTapZoom] : 16 -> 20
~ -[MUImageContentViewController setInDoubleTapZoom:] : 16 -> 20
~ -[MUImageContentViewController didSetup] : 20 -> 24
~ -[MUImageContentViewController setDidSetup:] : 16 -> 20
~ -[MUImageContentViewController firstLoadZoomToFit] : 16 -> 20
~ -[MUImageContentViewController setFirstLoadZoomToFit:] : 16 -> 20
~ -[MUImageContentViewController zoomToFitRestoreValue] : 16 -> 20
~ -[MUImageContentViewController setZoomToFitRestoreValue:] : 16 -> 20
~ +[UIImage(UIImage_MarkupAppIcon) mu_markupAppIcon] : 128 -> 120
~ +[MUPDFAnnotationAdaptorHelper migrateAppearanceStreamFromCGPDFAnnotationDict:toAKAnnotation:compensatingForPageRotation:] : 1064 -> 1052
~ +[MUPDFAnnotationAdaptorHelper migrateAKStrokedAnnotationPropertiesTo:fromAnnotationDictionary:ofPDFPage:] : 268 -> 264
~ +[MUPDFAnnotationAdaptorHelper migrateAKFilledAnnotationPropertiesTo:fromAnnotationDictionary:ofPDFPage:] : 132 -> 128
~ +[MUPDFAnnotationAdaptorHelper migrateAKTextAnnotationPropertiesTo:fromAnnotationDictionary:ofPDFPage:] : 704 -> 696
~ +[MUPDFAnnotationAdaptorHelper getRGBColorForKey:fromAnnotationDictionary:] : 108 -> 104
~ +[MUPDFAnnotationAdaptorHelper getFullFieldNameFromAnnotationDictionary:] : 496 -> 492
~ +[MUPDFAnnotationAdaptorHelper readDefaultAppearanceStringFromPDFDictionary:ofPage:toDictionary:] : 212 -> 204
~ +[MUPDFAnnotationAdaptorHelper readQuaddingFromPDFDictionary:toDictionary:] : 228 -> 216
~ +[MUPDFAnnotationAdaptorHelper addBoundsOfAnnotation:forPage:toDictionary:] : 496 -> 476
~ +[MUPDFAnnotationAdaptorHelper addModificationDateOfAnnotation:toDictionary:] : 160 -> 152
~ +[MUPDFAnnotationAdaptorHelper addFlagsOfAnnotation:toDictionary:] : 120 -> 116
~ +[MUPDFAnnotationAdaptorHelper addContentsStringOfAnnotation:toDictionary:] : 320 -> 304
~ +[MUPDFAnnotationAdaptorHelper addTextOfAnnotation:toDictionary:forKey:canUsePlaceholder:] : 208 -> 196
~ +[MUPDFAnnotationAdaptorHelper addString:toDictionary:forKey:] : 188 -> 192
~ +[MUPDFAnnotationAdaptorHelper addBorderStyleOfAnnotation:toDictionary:] : 476 -> 460
~ +[MUPDFAnnotationAdaptorHelper addRGBColor:forKey:toDictionary:] : 356 -> 340
~ +[MUPDFAnnotationAdaptorHelper addAppearanceStreamOfAnnotation:forPage:toDictionary:] : 536 -> 524
~ +[MUPDFAnnotationAdaptorHelper addDefaultAppearanceStreamOfAnnotation:toDictionary:] : 1136 -> 1116
~ ___84+[MUPDFAnnotationAdaptorHelper addDefaultAppearanceStreamOfAnnotation:toDictionary:]_block_invoke : 208 -> 188
~ +[MUPDFAnnotationAdaptorHelper addQuaddingOfAnnotation:toDictionary:] : 260 -> 248
~ +[MUPDFAnnotationAdaptorHelper newAKAnnotationFromCGPDFAnnotation:] : 492 -> 480
~ +[MUPDFAnnotationAdaptorHelper addAKAnnotation:toAnnotationDictionary:] : 448 -> 424
~ +[MUPDFAnnotationAdaptorHelper _colorFromPDFArray:] : 428 -> 424
~ +[MUPDFAnnotationAdaptorHelper _getFontFromAppearanceString:ofPDFPage:] : 804 -> 776
~ +[MUPDFAnnotationAdaptorHelper _getColorFromAppearanceString:] : 144 -> 136
~ +[MUPDFAnnotationAdaptorHelper _tokenizeAppearanceString:] : 260 -> 252
~ +[MUPDFAnnotationAdaptorHelper _pointSizeFromAppearanceTokens:] : 200 -> 188
~ +[MUPDFAnnotationAdaptorHelper _fontNameFromAppearanceTokens:] : 276 -> 256
~ +[MUPDFAnnotationAdaptorHelper _colorFromAppearanceTokens:] : 468 -> 432
~ +[MUPDFAnnotationAdaptorHelper _shouldUseAKAnnotation:toRepresentCGPDFAnnotation:] : 784 -> 756
~ __dictionaryForPDFDictionary : 236 -> 232
~ __iterateDictionaryValueCallback : 276 -> 252
~ __objectForCGPDFObjectRefAndVisitedSet : 584 -> 552
~ __arrayForPDFArray : 268 -> 260
~ +[MUCGPDFSquareAnnotationAdaptor _concreteDictionaryRepresentationOfAKAnnotation:forPage:] : 416 -> 404
~ -[MUImageAnalysisManager initWithDelegate:presentingView:] : 168 -> 172
~ -[MUImageAnalysisManager _setupImageAnalysis] : 284 -> 260
~ -[MUImageAnalysisManager dealloc] : 104 -> 100
~ -[MUImageAnalysisManager _setupAnalysisButtonsContainerInView:] : 2740 -> 2476
~ -[MUImageAnalysisManager image] : 84 -> 76
~ -[MUImageAnalysisManager imageAnalyzer] : 164 -> 148
~ -[MUImageAnalysisManager _updateAnalysisButtonWithAnimation:] : 292 -> 280
~ -[MUImageAnalysisManager _updateAnalysisButtonContainerWithAnimation:] : 540 -> 512
~ ___70-[MUImageAnalysisManager _updateAnalysisButtonContainerWithAnimation:]_block_invoke : 124 -> 120
~ -[MUImageAnalysisManager _activateInteractionTypes:] : 108 -> 104
~ -[MUImageAnalysisManager setupAnalysisButtonsContainer] : 140 -> 136
~ -[MUImageAnalysisManager imageAnalysisQueue] : 84 -> 68
~ ___44-[MUImageAnalysisManager imageAnalysisQueue]_block_invoke : 140 -> 132
~ -[MUImageAnalysisManager startImageAnalysis] : 328 -> 308
~ -[MUImageAnalysisManager _startImageAnalysisWithRequest:] : 308 -> 304
~ ___57-[MUImageAnalysisManager _startImageAnalysisWithRequest:]_block_invoke : 264 -> 260
~ ___57-[MUImageAnalysisManager _startImageAnalysisWithRequest:]_block_invoke_2 : 328 -> 336
~ -[MUImageAnalysisManager _handleImageAnalysis:error:] : 332 -> 328
~ ___53-[MUImageAnalysisManager _handleImageAnalysis:error:]_block_invoke : 76 -> 72
~ -[MUImageAnalysisManager _updateInfoButtonWithAnimation:] : 120 -> 116
~ -[MUImageAnalysisManager updateBottomRightContainerPositionForImageView:view:] : 352 -> 316
~ -[MUImageAnalysisManager updateForFullScreen:animated:] : 428 -> 420
~ ___55-[MUImageAnalysisManager updateForFullScreen:animated:]_block_invoke : 124 -> 120
~ -[MUImageAnalysisManager stopImageAnalysis] : 188 -> 172
~ -[MUImageAnalysisManager cancelAllRequests] : 96 -> 92
~ -[MUImageAnalysisManager hasAnalysis] : 76 -> 68
~ -[MUImageAnalysisManager addInteractionIfNeeded] : 188 -> 172
~ -[MUImageAnalysisManager enableMarkupMode:] : 272 -> 256
~ -[MUImageAnalysisManager isInteractionActive] : 168 -> 152
~ -[MUImageAnalysisManager hasResultsForVisualSearch] : 100 -> 92
~ -[MUImageAnalysisManager isVisualSearchEnabled] : 76 -> 72
~ -[MUImageAnalysisManager infoButtonGlyphName] : 220 -> 200
~ -[MUImageAnalysisManager filledInfoButtonGlyphName] : 220 -> 200
~ -[MUImageAnalysisManager isTextSelectionEnabled] : 88 -> 84
~ -[MUImageAnalysisManager isImageSubjectHighlightingEnabled] : 76 -> 72
~ -[MUImageAnalysisManager shouldHideInteraction:animated:] : 300 -> 276
~ -[MUImageAnalysisManager dataDetectorExistsAtPoint:] : 84 -> 80
~ -[MUImageAnalysisManager textExistsAtPoint:] : 84 -> 80
~ -[MUImageAnalysisManager imageSubjectExistsAtPoint:] : 84 -> 80
~ -[MUImageAnalysisManager visualSearchExistsAtPoint:] : 84 -> 80
~ -[MUImageAnalysisManager actionInfoItemExistsAtPoint:] : 84 -> 80
~ -[MUImageAnalysisManager hasActiveTextSelection] : 60 -> 56
~ -[MUImageAnalysisManager adjustImageInteractionForScrollView:] : 300 -> 288
~ -[MUImageAnalysisManager imageAnalysisInteraction:shouldBeginAtPoint:forAnalysisType:] : 184 -> 180
~ -[MUImageAnalysisManager imageAnalysisPopoverWillAppear] : 112 -> 108
~ -[MUImageAnalysisManager imageAnalysisPopoverDidDisappear] : 112 -> 108
~ -[MUImageAnalysisManager imageAnalysisInteraction:prepareForCalloutAction:competion:] : 208 -> 200
~ -[MUImageAnalysisManager presentingViewControllerForImageAnalysisInteraction:] : 116 -> 108
~ -[MUImageAnalysisManager setImageInteraction:] : 64 -> 12
~ -[MUImageAnalysisManager setImageAnalyzer:] : 64 -> 12
~ -[MUImageAnalysisManager setVisualSearchViewContainer:] : 64 -> 12
~ -[MUImageAnalysisManager setAnalysisButtonContainer:] : 64 -> 12
~ -[MUImageAnalysisManager setBottomRightButtonsContainer:] : 64 -> 12
~ -[MUImageAnalysisManager setBottomRightButtonsContainerRightConstraint:] : 64 -> 12
~ -[MUImageAnalysisManager setBottomRightButtonsContainerBottomConstraint:] : 64 -> 12
~ +[MUCGPDFFreeTextAnnotationAdaptor _concreteDictionaryRepresentationOfAKAnnotation:forPage:] : 316 -> 312
~ +[MUCGPDFCircleAnnotationAdaptor _concreteDictionaryRepresentationOfAKAnnotation:forPage:] : 416 -> 404
~ ___56-[NSDictionary(Foundation_Extensions) muDeepMutableCopy]_block_invoke : 296 -> 292
~ -[_MUBaseImage initWithBaseImage:allowHDR:] : 836 -> 820
~ +[MUImageWriter outputTypesSupportingHDR] : 168 -> 160
~ -[MUImageWriter _renderImageForBaseImage:controller:wantsHDR:opaque:] : 296 -> 280
~ -[MUImageWriter writeUsingBaseImage:withAnnotationsFromController:asImageOfType:toConsumer:embedSourceImageAndAnnotationsAsMetadata:encryptPrivateMetadata:error:] : 2572 -> 2472
~ -[MUImageWriter addGainMapImageToImageDestination:sdrImage:hdrImage:imageMetadata:imageOptions:] : 672 -> 648
~ -[MUImageWriter encodedModelFromAnnotationsController:encrypt:] : 184 -> 164
~ +[MURemoteViewController serviceViewControllerInterface] : 236 -> 228
~ +[MURemoteViewController exportedInterface] : 252 -> 240
~ -[MURemoteViewController serviceDidFinishwithResults:andSandboxExtension:] : 196 -> 188
~ -[MURemoteViewController beginDismissWithInfo:] : 136 -> 132
~ -[MURemoteViewController finishedWithResultsCompletionBlock] : 16 -> 20
~ -[MURemoteViewController sandboxExtensionHandle] : 16 -> 20
~ -[MURemoteViewController setSandboxExtensionHandle:] : 16 -> 20
~ -[MURemoteViewController shouldResignFirstResponder] : 20 -> 24
~ -[MURemoteViewController setShouldResignFirstResponder:] : 16 -> 20
~ _akMedian : 268 -> 272
~ -[MUPDFContentViewController initWithPDFDocument:delegate:] : 188 -> 196
~ -[MUPDFContentViewController allowsThumbnailViewPageReordering] : 76 -> 72
~ -[MUPDFContentViewController viewDidLoad] : 128 -> 120
~ -[MUPDFContentViewController viewDidLayoutSubviews] : 348 -> 320
~ -[MUPDFContentViewController teardown] : 160 -> 156
~ -[MUPDFContentViewController loadContentWithCompletionBlock:] : 156 -> 152
~ -[MUPDFContentViewController idealContentSizeForScreenSize:windowDecorationSize:] : 468 -> 460
~ -[MUPDFContentViewController contentViewScrollView] : 84 -> 76
~ -[MUPDFContentViewController PDFView:shouldHandleLink:] : 124 -> 120
~ -[MUPDFContentViewController shouldShowAnnotationsOfType:] : 96 -> 92
~ -[MUPDFContentViewController documentCanBeEdited:] : 172 -> 164
~ -[MUPDFContentViewController menuElementsForPage:] : 144 -> 136
~ -[MUPDFContentViewController canShowPageViewLabel] : 128 -> 120
~ -[MUPDFContentViewController controller:willSetToolbarItems:] : 152 -> 140
~ -[MUPDFContentViewController positionSketchOverlay:forAnnotationController:] : 124 -> 120
~ -[MUPDFContentViewController annotationController:detectedEditOfType:] : 116 -> 112
~ -[MUPDFContentViewController editCheckpointReachedForAnnotationController:] : 100 -> 96
~ -[MUPDFContentViewController penStrokeCompletedForAnnotationController:] : 100 -> 96
~ -[MUPDFContentViewController controllerWillShowSignatureCaptureView:] : 100 -> 96
~ -[MUPDFContentViewController controllerWillDismissSignatureCaptureView:] : 100 -> 96
~ -[MUPDFContentViewController controllerWillShowSignatureManagerView:] : 100 -> 96
~ -[MUPDFContentViewController controllerWillDismissSignatureManagerView:] : 100 -> 96
~ -[MUPDFContentViewController setEdgeInsets:] : 376 -> 368
~ -[MUPDFContentViewController pageCount] : 60 -> 56
~ -[MUPDFContentViewController setFixedThumbnailView:] : 84 -> 88
~ -[MUPDFContentViewController setShowsThumbnailView:] : 1300 -> 1220
~ ___52-[MUPDFContentViewController setShowsThumbnailView:]_block_invoke_2 : 176 -> 168
~ -[MUPDFContentViewController setNavigationModeHorizontal:] : 128 -> 132
~ -[MUPDFContentViewController _updatePDFViewDisplayMode] : 184 -> 172
~ -[MUPDFContentViewController _boundingPathMayHaveChangedForView:relativeToBoundsOriginOnly:] : 184 -> 176
~ -[MUPDFContentViewController _thumbnailViewWidth] : 172 -> 168
~ -[MUPDFContentViewController _thumbnailViewCellSize] : 132 -> 136
~ -[MUPDFContentViewController _updateThumbnailViewHolderBackgroundColor] : 696 -> 648
~ -[MUPDFContentViewController _updateThumbnailViewHolderVisibility] : 140 -> 136
~ -[MUPDFContentViewController removeThumbnailViewHolderConstraints] : 188 -> 176
~ -[MUPDFContentViewController _updateThumbnailViewHolderConstraints] : 1836 -> 1696
~ -[MUPDFContentViewController _updateThumbnailViewAppearance] : 460 -> 424
~ -[MUPDFContentViewController documentUnlockedWithPassword] : 140 -> 128
~ -[MUPDFContentViewController _createPDFView] : 1716 -> 1620
~ -[MUPDFContentViewController _teardownPDFViewIfNecessary] : 544 -> 508
~ -[MUPDFContentViewController pdfViewDidChangeCurrentPage:] : 228 -> 212
~ -[MUPDFContentViewController pdfScrollViewWillBeginDragging:] : 216 -> 208
~ -[MUPDFContentViewController pdfDocumentDidUnlock:] : 472 -> 456
~ -[MUPDFContentViewController _updateThumbnailView] : 88 -> 84
~ -[MUPDFContentViewController pageLabelViewTapped:] : 112 -> 120
~ -[MUPDFContentViewController edgeSwipeGestureRecognized:] : 100 -> 104
~ -[MUPDFContentViewController _removePageLabelViewConstraints] : 172 -> 176
~ -[MUPDFContentViewController _updatePageNumberOverlayToPage:animate:] : 916 -> 860
~ ___69-[MUPDFContentViewController _updatePageNumberOverlayToPage:animate:]_block_invoke : 72 -> 68
~ -[MUPDFContentViewController canEditContent] : 116 -> 112
~ -[MUPDFContentViewController acceptSingleTouch:] : 216 -> 208
~ -[MUPDFContentViewController _pageLabelExistAtPoint:] : 268 -> 244
~ -[MUPDFContentViewController _thumbnailViewExistAtPoint:] : 104 -> 100
~ -[MUPDFContentViewController thumbnailViewStyle] : 16 -> 20
~ -[MUPDFContentViewController setThumbnailViewStyle:] : 576 -> 528
~ -[MUPDFContentViewController isTouchInThumbnailView:] : 176 -> 172
~ -[MUPDFContentViewController visibleContentRect] : 140 -> 132
~ -[MUPDFContentViewController visibleContentRectInCoordinateSpace:] : 284 -> 268
~ -[MUPDFContentViewController contentSnapshot] : 336 -> 304
~ -[MUPDFContentViewController highlight:] : 120 -> 116
~ -[MUPDFContentViewController canPerformAction:withSender:] : 304 -> 296
~ -[MUPDFContentViewController _prepareToRotate] : 68 -> 64
~ -[MUPDFContentViewController _recoverFromRotation] : 460 -> 444
~ -[MUPDFContentViewController _medianSizeForCurrentDocumentInPDFViewWithGetter:] : 368 -> 364
~ -[MUPDFContentViewController _updateMinMaxZoomFactor] : 140 -> 132
~ -[MUPDFContentViewController _userChangedScrollViewMagnificationNotification:] : 228 -> 216
~ -[MUPDFContentViewController traitCollectionDidChange:] : 196 -> 184
~ -[MUPDFContentViewController _compensatingAffineTransformForPage:] : 312 -> 308
~ -[MUPDFContentViewController find:] : 100 -> 92
~ -[MUPDFContentViewController findNext:] : 96 -> 88
~ -[MUPDFContentViewController findPrevious:] : 96 -> 88
~ -[MUPDFContentViewController showsThumbnailView] : 16 -> 20
~ -[MUPDFContentViewController fixedThumbnailView] : 16 -> 20
~ -[MUPDFContentViewController navigationModeHorizontal] : 16 -> 20
~ -[MUPDFContentViewController forcesPDFViewTopAlignment] : 16 -> 20
~ -[MUPDFContentViewController shouldShowThumbnailView] : 16 -> 20
~ -[MUPDFContentViewController setShouldShowThumbnailView:] : 16 -> 20
~ -[MUPDFContentViewController inkStyle] : 16 -> 20
~ -[MUPDFContentViewController constraintsAreHorizontal] : 20 -> 24
~ -[MUPDFContentViewController setConstraintsAreHorizontal:] : 16 -> 20
~ -[MUPDFContentViewController viewIsTransitioningBetweenSizes] : 20 -> 24
~ -[MUPDFContentViewController setViewIsTransitioningBetweenSizes:] : 16 -> 20
~ -[MUPDFContentViewController viewTransitionPreviousScale] : 16 -> 20
~ -[MUPDFContentViewController setViewTransitionPreviousScale:] : 16 -> 20
~ -[MUPDFContentViewController viewTransitionPreviousAutoscalingState] : 20 -> 24
~ -[MUPDFContentViewController setViewTransitionPreviousAutoscalingState:] : 16 -> 20
~ -[MUPDFContentViewController didSetup] : 20 -> 24
~ -[MUPDFContentViewController setDidSetup:] : 16 -> 20
~ -[MUImageScrollView _centerContentIfNecessaryAdjustingContentOffset:] : 176 -> 172
~ -[MUImageScrollView centerContentIgnoringInsets] : 176 -> 168
~ -[MUPDFPageLabelView initWithFrame:] : 1316 -> 1212
~ +[MUPDFPageLabelView sidebarAttributedString] : 84 -> 68
~ ___45+[MUPDFPageLabelView sidebarAttributedString]_block_invoke : 244 -> 232
~ -[MUPDFPageLabelView isTimerInstalled] : 24 -> 28
~ -[MUPDFPageLabelView showNowInSuperView:withText:] : 216 -> 228
~ -[MUPDFPageLabelView resetFadeOutTimer] : 176 -> 172
~ ___29-[MUPDFPageLabelView fadeOut]_block_invoke : 92 -> 100
~ -[MUPDFPageLabelView currentPageIndex] : 16 -> 20
~ -[MUPDFPageLabelView setCurrentPageIndex:] : 16 -> 20
~ +[MUCGPDFMarkupAnnotationAdaptor _concreteAKAnnotationWithCGPDFAnnotation:ofPage:] : 720 -> 708
~ +[MUCGPDFMarkupAnnotationAdaptor _concreteDictionaryRepresentationOfAKAnnotation:forPage:] : 964 -> 920
~ +[MUStatistics logFileTypeOpened:byProcess:] : 280 -> 292
~ ___44+[MUStatistics logFileTypeOpened:byProcess:]_block_invoke : 148 -> 144
~ +[MUStatistics logFileTypeSaved:byProcess:] : 280 -> 292
~ ___43+[MUStatistics logFileTypeSaved:byProcess:]_block_invoke : 148 -> 144
~ +[MUPayloadEncryption sharedInstance] : 176 -> 160
~ -[MUPayloadEncryption encryptData:] : 508 -> 500
~ -[MUPayloadEncryption decryptData:] : 396 -> 392
~ -[MUPayloadEncryption initializeKey] : 1128 -> 1092
~ +[MUCGPDFAnnotationAdaptor supportedAnnotationTypes] : 84 -> 68
~ ___52+[MUCGPDFAnnotationAdaptor supportedAnnotationTypes]_block_invoke : 176 -> 172
~ +[MUCGPDFAnnotationAdaptor newAKAnnotationWithCGPDFAnnotation:ofPage:] : 512 -> 504
~ +[MUCGPDFAnnotationAdaptor newPlaceholderAKAnnotationWithCGPDFAnnotation:ofPage:] : 192 -> 188
~ +[MUCGPDFAnnotationAdaptor pdfDictionaryRepresentationOfAKAnnotation:forPage:] : 1364 -> 1276
~ +[MUCGPDFTextWidgetAnnotationAdaptor _concreteAKAnnotationWithCGPDFAnnotation:ofPage:] : 872 -> 864
~ +[MUCGPDFTextWidgetAnnotationAdaptor _concreteDictionaryRepresentationOfAKAnnotation:forPage:] : 560 -> 556
~ +[MUCGPDFStampAnnotationAdaptor _concreteDictionaryRepresentationOfAKAnnotation:forPage:] : 268 -> 264
CStrings:
- "#16@0:8"
- "#24@0:8@\"NSString\"16"
- "#24@0:8@16"
- ".cxx_destruct"
- "@"
- "@\"<MUContentViewControllerDelegate>\""
- "@\"<MUImageAnalysisManagerDelegate>\""
- "@\"<MarkupViewControllerDelegate>\""
- "@\"<MarkupViewControllerDelegate>\"16@0:8"
- "@\"<QuickLookContentEditorDelegate>\"16@0:8"
- "@\"<UIScrollViewDelegate>\""
- "@\"AKController\""
- "@\"AKController\"16@0:8"
- "@\"AKPageController\""
- "@\"AKRectAnnotation\""
- "@\"AKToolbarView\""
- "@\"CALayer\"32@0:8Q16@\"AKController\"24"
- "@\"MUDelegateProxy<PDFViewDelegatePrivate>\""
- "@\"MUImageAnalysisManager\""
- "@\"MUPDFPageLabelView\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSArray\"24@0:8@\"PDFPage\"16"
- "@\"NSArray\"24@0:8@\"PDFSelection\"16"
- "@\"NSArray\"24@0:8@\"VKCImageAnalysisInteraction\"16"
- "@\"NSArray\"32@0:8@\"AKController\"16@\"NSArray\"24"
- "@\"NSArray\"32@0:8@\"MUContentViewController\"16@\"NSArray\"24"
- "@\"NSArray\"32@0:8@\"NSArray\"16@\"PDFPage\"24"
- "@\"NSArray\"40@0:8@\"NSIndexSet\"16Q24@\"AKController\"32"
- "@\"NSAttributedString\"32@0:8@\"VKCImageAnalysisInteraction\"16@\"NSAttributedString\"24"
- "@\"NSData\""
- "@\"NSData\"16@0:8"
- "@\"NSData\"24@0:8@\"NSData\"16"
- "@\"NSData\"24@0:8^@16"
- "@\"NSData\"28@0:8B16^@20"
- "@\"NSData\"76@0:8B16d20{CGRect={CGPoint=dd}{CGSize=dd}}28Q60@\"AKController\"68"
- "@\"NSDictionary\"16@0:8"
- "@\"NSDictionary\"24@0:8@\"VKCImageAnalysisInteraction\"16"
- "@\"NSIndexSet\"32@0:8Q16@\"AKController\"24"
- "@\"NSIndexSet\"40@0:8@\"NSArray\"16Q24@\"AKController\"32"
- "@\"NSLayoutConstraint\""
- "@\"NSMutableSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8d16"
- "@\"NSString\"32@0:8@\"VKCImageAnalysisInteraction\"16@\"NSString\"24"
- "@\"NSTimer\""
- "@\"NSUndoManager\""
- "@\"NSUndoManager\"16@0:8"
- "@\"NSUndoManager\"24@0:8@\"AKController\"16"
- "@\"NSUndoManager\"24@0:8@\"MUContentViewController\"16"
- "@\"PDFDocument\""
- "@\"PDFDocument\"16@0:8"
- "@\"PDFPage\""
- "@\"PDFThumbnailView\""
- "@\"PDFView\""
- "@\"PDFView\"16@0:8"
- "@\"UIAction\""
- "@\"UIBarButtonItem\""
- "@\"UIBlurEffect\""
- "@\"UIColor\""
- "@\"UIColor\"16@0:8"
- "@\"UIFindInteraction\"16@0:8"
- "@\"UIImage\""
- "@\"UIImage\"16@0:8"
- "@\"UIImage\"24@0:8@\"VKCImageAnalysisInteraction\"16"
- "@\"UIImageView\""
- "@\"UILabel\""
- "@\"UINavigationBar\""
- "@\"UINavigationBar\"16@0:8"
- "@\"UINavigationItem\""
- "@\"UIScreenEdgePanGestureRecognizer\""
- "@\"UIScrollView\""
- "@\"UIScrollView\"16@0:8"
- "@\"UITapGestureRecognizer\""
- "@\"UIView\""
- "@\"UIView\"16@0:8"
- "@\"UIView\"24@0:8@\"UIScrollView\"16"
- "@\"UIView\"24@0:8@\"VKCImageAnalysisInteraction\"16"
- "@\"UIViewController\"16@0:8"
- "@\"UIViewController\"24@0:8@\"AKController\"16"
- "@\"UIViewController\"24@0:8@\"VKCImageAnalysisInteraction\"16"
- "@\"UIViewController\"32@0:8@\"UIPresentationController\"16q24"
- "@\"UIViewController<MUContentViewControllerProtocol>\""
- "@\"UIViewController<MUContentViewControllerProtocol>\"16@0:8"
- "@\"UIVisualEffectView\""
- "@\"UTType\"16@0:8"
- "@\"VKCImageAnalysisInteraction\""
- "@\"VKCImageAnalyzer\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@24@0:8^{CGDataProvider=}16"
- "@24@0:8^{CGPDFAnnotation=}16"
- "@24@0:8^{CGPDFArray=}16"
- "@24@0:8^{CGPDFDictionary=}16"
- "@24@0:8^{CGPDFForm=}16"
- "@24@0:8^{CGPDFString=}16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8d16"
- "@28@0:8@16B24"
- "@28@0:8B16^@20"
- "@32@0:8:16@24"
- "@32@0:8@16:24"
- "@32@0:8@16@24"
- "@32@0:8@16^B24"
- "@32@0:8@16^{CGImageMetadata=}24"
- "@32@0:8@16^{CGPDFPage=}24"
- "@32@0:8@16q24"
- "@32@0:8B16B20@24"
- "@32@0:8Q16@24"
- "@32@0:8^{CGImage=}16@24"
- "@32@0:8^{CGPDFAnnotation=}16^{CGPDFPage=}24"
- "@32@0:8^{CGPDFString=}16^{CGPDFPage=}24"
- "@32@0:8r*16^{CGPDFDictionary=}24"
- "@36@0:8B16@20^@28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16Q24@32"
- "@40@0:8B16B20@24@32"
- "@40@0:8^{CGDataProvider=}16@24^B32"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@56@0:8@16@24@32@40@48"
- "@76@0:8B16d20{CGRect={CGPoint=dd}{CGSize=dd}}28Q60@68"
- "@?"
- "@?16@0:8"
- "AKControllerDelegateProtocol"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"AKController\"16"
- "B24@0:8@\"NSData\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"UIPresentationController\"16"
- "B24@0:8@\"UIScrollView\"16"
- "B24@0:8@\"UITouch\"16"
- "B24@0:8@\"VKCImageAnalysisInteraction\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B32@0:8:16@24"
- "B32@0:8@\"AKAnnotation\"16@\"AKController\"24"
- "B32@0:8@\"AKController\"16q24"
- "B32@0:8@\"MUPDFContentViewController\"16@\"NSURL\"24"
- "B32@0:8@\"NSURL\"16^@24"
- "B32@0:8@\"UINavigationBar\"16@\"UINavigationItem\"24"
- "B32@0:8@\"VKCImageAnalysisInteraction\"16@24"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B32@0:8@16^{CGPDFAnnotation=}24"
- "B32@0:8@16q24"
- "B32@0:8{CGPoint=dd}16"
- "B32@0:8{CGSize=dd}16"
- "B36@0:8@\"NSURL\"16B24^@28"
- "B36@0:8@16B24^@28"
- "B36@0:8^{CGDataConsumer=}16B24^@28"
- "B40@0:8@\"AKController\"16@\"AKAnnotation\"24@\"AKPageModelController\"32"
- "B40@0:8@\"NSURL\"16@\"NSDictionary\"24^@32"
- "B40@0:8@16@24@32"
- "B40@0:8@16@24^@32"
- "B44@0:8@16B24@28^@36"
- "B44@0:8^{CGDataConsumer=}16B24@28^@36"
- "B48@0:8@\"VKCImageAnalysisInteraction\"16{CGPoint=dd}24Q40"
- "B48@0:8@16{CGPoint=dd}24Q40"
- "B48@0:8{CGPoint=dd}16Q32@\"AKController\"40"
- "B48@0:8{CGPoint=dd}16Q32@40"
- "B48@0:8{CGSize=dd}16{CGSize=dd}32"
- "B64@0:8@16@24@32^{CGDataConsumer=}40B48B52^@56"
- "B64@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16Q48@\"AKController\"56"
- "B64@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16Q48@56"
- "B80@0:8@\"VKCImageAnalysisInteraction\"16@\"NSArray\"24{CGRect={CGPoint=dd}{CGSize=dd}}32@\"NSString\"64@\"NSAttributedString\"72"
- "B80@0:8@16@24{CGRect={CGPoint=dd}{CGSize=dd}}32@64@72"
- "CGColor"
- "CGImage"
- "CGRectValue"
- "EnableAnnotationKit"
- "Foundation_Extensions"
- "MUCGPDFAnnotationAdaptor"
- "MUCGPDFCircleAnnotationAdaptor"
- "MUCGPDFFormWrapper"
- "MUCGPDFFreeTextAnnotationAdaptor"
- "MUCGPDFLineAnnotationAdaptor"
- "MUCGPDFMarkupAnnotationAdaptor"
- "MUCGPDFPopupAnnotationAdaptor"
- "MUCGPDFSquareAnnotationAdaptor"
- "MUCGPDFStampAnnotationAdaptor"
- "MUCGPDFTextWidgetAnnotationAdaptor"
- "MUContentViewController"
- "MUContentViewControllerDelegate"
- "MUContentViewControllerProtocol"
- "MUDelegateProxy"
- "MUDocumentPickerViewController"
- "MUExtensionViewProtocol"
- "MUImageAnalysisManager"
- "MUImageAnalysisManagerDelegate"
- "MUImageContentViewController"
- "MUImageDownsamplingUtilities"
- "MUImageReader"
- "MUImageScrollView"
- "MUImageWriter"
- "MUPDFAnnotationAdaptorHelper"
- "MUPDFPageLabelView"
- "MUPDFUtilities"
- "MUPDFView"
- "MURemoteViewController"
- "MURemoteViewProtocol"
- "MUStatistics"
- "MarkupViewControllerPrivateProtocol"
- "MarkupViewControllerProtocol"
- "NSCopying"
- "NSMutableCopying"
- "NSObject"
- "PDFAKControllerDelegateProtocol"
- "PDFDocumentDelegate"
- "PDFThumbnailContextMenuDelegate"
- "PDFView:allowsFormFillingMode:forPage:"
- "PDFView:allowsFormFillingMode:withAutofill:forPage:"
- "PDFView:allowsFormFillingMode:withRecognitionConfidence:forPage:"
- "PDFView:shouldHandleLink:"
- "PDFViewDelegate"
- "PDFViewDelegatePrivate"
- "PDFViewOpenPDF:forRemoteGoToAction:"
- "PDFViewParentViewController"
- "PDFViewPerformFind:"
- "PDFViewPerformGoToPage:"
- "PDFViewWillClickOnLink:withURL:"
- "PKRulerHostingDelegate"
- "Q16@0:8"
- "Q24@0:8@\"VKCImageAnalysisInteraction\"16"
- "Q24@0:8@16"
- "Q24@0:8^{CGPDFPage=}16"
- "Q32@0:8^{CGPDFDictionary=}16^{CGPDFArray=}24"
- "Q40@0:8@16@24Q32"
- "QuickLookContentEditor"
- "QuickLookContentEditorBannerConfiguration"
- "T#,R"
- "T@\"<MUContentViewControllerDelegate>\",W,V_delegate"
- "T@\"<MUImageAnalysisManagerDelegate>\",W,N,V_delegate"
- "T@\"<MUImageScrollViewDelegate>\",W,D,N"
- "T@\"<MarkupViewControllerDelegate>\",W,N"
- "T@\"<MarkupViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<QuickLookContentEditorDelegate>\",W,N"
- "T@\"<UIScrollViewDelegate>\",W,V_scrollViewDelegate"
- "T@\"AKController\",&,V_annotationController"
- "T@\"AKController\",R,N"
- "T@\"AKPageController\",W,N,V_pageController"
- "T@\"AKRectAnnotation\",W,N,V_editingAnnotaiton"
- "T@\"AKToolbarView\",&,V_modernToolbar"
- "T@\"MUDelegateProxy<PDFViewDelegatePrivate>\",&,N,V_pdfViewDelegateProxy"
- "T@\"MUImageAnalysisManager\",&,N,V_imageAnalysisManager"
- "T@\"NSArray\",&,V_sourceContentReplacedAnnotationMaps"
- "T@\"NSArray\",&,V_thumbnailViewHolderConstraints"
- "T@\"NSArray\",?,&"
- "T@\"NSData\",&,V_archivedModelData"
- "T@\"NSDictionary\",?,R,N"
- "T@\"NSLayoutConstraint\",&,N,V_bottomRightButtonsContainerBottomConstraint"
- "T@\"NSLayoutConstraint\",&,N,V_bottomRightButtonsContainerRightConstraint"
- "T@\"NSLayoutConstraint\",&,V_pdfViewLeadingConstraint"
- "T@\"NSLayoutConstraint\",&,V_thumbnailViewHolderRevealConstraint"
- "T@\"NSLayoutConstraint\",&,V_thumbnailViewHolderWidthConstraint"
- "T@\"NSLayoutConstraint\",&,V_thumbnailViewLeadingConstraint"
- "T@\"NSLayoutConstraint\",&,V_toolbarBottomConstraint"
- "T@\"NSLayoutConstraint\",&,V_toolbarTopAttachedConstraint"
- "T@\"NSLayoutConstraint\",&,V_toolbarTopConstraint"
- "T@\"NSMutableSet\",&,N,V_actionsNotEnablingMarkup"
- "T@\"NSString\",&,V_sourceContentType"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",?,R,C,N"
- "T@\"NSString\",C,N"
- "T@\"NSString\",C,N,V_hostProcessBundleIdentifier"
- "T@\"NSString\",C,N,V_originalImageDescription"
- "T@\"NSString\",C,N,V_preferredFileDisplayName"
- "T@\"NSString\",C,N,V_subtitle"
- "T@\"NSString\",C,N,V_title"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSUndoManager\",&,N"
- "T@\"NSUndoManager\",&,N,V_akUndoManager"
- "T@\"PDFDocument\",R"
- "T@\"PDFDocument\",R,V_pdfDocument"
- "T@\"PDFPage\",W,V_viewTransitionPageToCenter"
- "T@\"PDFThumbnailView\",&,V_thumbnailView"
- "T@\"PDFView\",&,V_pdfView"
- "T@\"PDFView\",R"
- "T@\"UIAction\",&,N,V_dismissAction"
- "T@\"UIAction\",&,N,V_primaryAction"
- "T@\"UIBarButtonItem\",&,V_cancelButton"
- "T@\"UIBarButtonItem\",&,V_doneButton"
- "T@\"UIColor\",C"
- "T@\"UIFindInteraction\",R,N"
- "T@\"UIImage\",&,N,V_image"
- "T@\"UIImage\",&,N,V_latestImageForAnalysis"
- "T@\"UIImage\",&,N,V_tentativePlaceholderImage"
- "T@\"UIImage\",&,V_placeholderImage"
- "T@\"UIImage\",R,N"
- "T@\"UIImageView\",&,N,V_imageView"
- "T@\"UIImageView\",&,V_placeholderImageView"
- "T@\"UINavigationBar\",&,N"
- "T@\"UINavigationBar\",&,N,V_navBar"
- "T@\"UINavigationItem\",&,N,V_navItem"
- "T@\"UIScrollView\",&,N,V_scrollView"
- "T@\"UIScrollView\",R,N"
- "T@\"UITapGestureRecognizer\",&,V_localDoubleTapRecognizer"
- "T@\"UIView\",&,N,V_analysisButtonContainer"
- "T@\"UIView\",&,N,V_bottomRightButtonsContainer"
- "T@\"UIView\",&,N,V_combinedContentView"
- "T@\"UIView\",&,N,V_toolbar"
- "T@\"UIView\",&,N,V_visualSearchViewContainer"
- "T@\"UIView\",&,V_contentContainerView"
- "T@\"UIView\",&,V_scrollerBackgroundView"
- "T@\"UIView\",&,V_thumbnailViewHolder"
- "T@\"UIView\",&,V_transitionDimmingView"
- "T@\"UIView\",&,V_whiteView"
- "T@\"UIView\",R,N"
- "T@\"UIView\",R,W"
- "T@\"UIView\",R,W,N"
- "T@\"UIView\",W,N,V_presentingView"
- "T@\"UIViewController<MUContentViewControllerProtocol>\",&,V_contentViewController"
- "T@\"UIViewController<MUContentViewControllerProtocol>\",R"
- "T@\"UTType\",R,N"
- "T@\"VKCImageAnalysisInteraction\",&,N,V_imageInteraction"
- "T@\"VKCImageAnalyzer\",&,N,V_imageAnalyzer"
- "T@,&,N,V_sourceContent"
- "T@,&,V_digestedSourceContent"
- "T@,&,V_sourceContent"
- "T@,W,V_firstDelegate"
- "T@,W,V_secondDelegate"
- "T@?,C,N,V_finishedWithResultsCompletionBlock"
- "T@?,C,N,V_importHandler"
- "T@?,C,N,V_scanImageToPDFConversionHandler"
- "T@?,C,N,V_scanPDFHandler"
- "T@?,C,V_loadCompletionBlock"
- "TB"
- "TB,?,N"
- "TB,?,R,N"
- "TB,GisObservingAKCurrentPageIndex,V_observingAKCurrentPageIndex"
- "TB,N"
- "TB,N,GisNavigationModeHorizontal"
- "TB,N,GisNavigationModeHorizontal,V_navigationModeHorizontal"
- "TB,N,GisShapeDetectionEnabled"
- "TB,N,GisShapeDetectionEnabled,V_shapeDetectionEnabled"
- "TB,N,GisThumbnailViewHidden"
- "TB,N,GisThumbnailViewHidden,V_thumbnailViewHidden"
- "TB,N,GisToolbarHidden"
- "TB,N,GisToolbarHidden,V_toolbarHidden"
- "TB,N,V_allowShakeToUndo"
- "TB,N,V_alreadyLoggedSavingForThisDocument"
- "TB,N,V_centersIgnoringContentInsets"
- "TB,N,V_firstLoadZoomToFit"
- "TB,N,V_fixedThumbnailView"
- "TB,N,V_forcesPDFViewTopAlignment"
- "TB,N,V_inDoubleTapZoom"
- "TB,N,V_navigationModeHorizontal"
- "TB,N,V_needsToolPickerVisibleWhenAnnotationControllerIsAvailable"
- "TB,N,V_pencilAlwaysDraws"
- "TB,N,V_shouldEnterVisualSearchAfterNextAnalysis"
- "TB,N,V_shouldHighlightTextAndDDAfterNextAnalysis"
- "TB,N,V_shouldShowThumbnailView"
- "TB,N,V_shouldUpliftSubjectAfterNextAnalysis"
- "TB,N,V_showShareButtonInToolbar"
- "TB,N,V_showThumbnailViewForMultipage"
- "TB,N,V_showsThumbnailView"
- "TB,N,V_usePlaceholderAsDisplayImageIfPossible"
- "TB,N,V_zoomToFitRestoreValue"
- "TB,R"
- "TB,R,N"
- "TB,R,N,GisTimerInstalled"
- "TB,R,N,V_opaque"
- "TB,V_constraintsAreHorizontal"
- "TB,V_delegateRespondsToDetectedFormInContent"
- "TB,V_didAppearOnce"
- "TB,V_didSetup"
- "TB,V_encryptPrivateMetadata"
- "TB,V_formDetectedInDocument"
- "TB,V_isAnimatingMarkupExtensionTransition"
- "TB,V_isFullScreen"
- "TB,V_isImageAnalysisPopoverPresented"
- "TB,V_needToPerformDocumentClosedTeardown"
- "TB,V_needToPerformFullTeardown"
- "TB,V_shouldResignFirstResponder"
- "TB,V_showAsFormSheet"
- "TB,V_useFancyTransition"
- "TB,V_userDidCancel"
- "TB,V_viewIsTransitioningBetweenSizes"
- "TB,V_viewTransitionPreviousAutoscalingState"
- "TQ"
- "TQ,?,R"
- "TQ,N"
- "TQ,N,V_inkStyle"
- "TQ,N,V_presentationMode"
- "TQ,N,VcurrentPageIndex"
- "TQ,R"
- "TQ,V_inkStyle"
- "T^{CGImage=},R,N,V_hdrImage"
- "T^{CGImage=},R,N,V_sdrImage"
- "T^{CGImageMetadata=},R,N,V_imageMetadata"
- "T^{CGImageSource=},R,N,V_imageSourceRef"
- "T^{CGPDFForm=},R"
- "T^{__CFDictionary=},R,N,V_imageOptions"
- "Td,R,N,V_headroom"
- "Td,V_downsampledImageScale"
- "Td,V_initialContentScale"
- "Td,V_maxImageDimension"
- "Td,V_viewTransitionPreviousScale"
- "Ti,V_imageAnalysisRequestId"
- "Tq,N"
- "Tq,N,V_toolbarPosition"
- "Tq,R,N"
- "Tq,V_sandboxExtensionHandle"
- "T{CGPoint=dd},V_viewTransitionPointOnPageToCenter"
- "T{CGSize=dd},R"
- "T{CGSize=dd},V_sourceImagePixelSize"
- "T{UIEdgeInsets=dddd},N"
- "T{UIEdgeInsets=dddd},N,V_cachedThumnailViewInsets"
- "T{UIEdgeInsets=dddd},N,V_edgeInsets"
- "UIAdaptivePresentationControllerDelegate"
- "UIBarPositioningDelegate"
- "UIDocumentPickerDelegate"
- "UIImage_MarkupAppIcon"
- "UINavigationBarDelegate"
- "UIScrollViewDelegate"
- "UIToolbarDelegate"
- "URLByAppendingPathComponent:"
- "URLByAppendingPathExtension:"
- "UTF8String"
- "UUID"
- "UUIDString"
- "VKCImageAnalysisInteractionDelegate"
- "VNDocumentCameraViewControllerDelegate"
- "Vv16@0:8"
- "[16C]"
- "^{CGImage=}"
- "^{CGImage=}16@0:8"
- "^{CGImage=}40@0:8@16@24B32B36"
- "^{CGImageMetadata=}"
- "^{CGImageMetadata=}16@0:8"
- "^{CGImageSource=}"
- "^{CGImageSource=}16@0:8"
- "^{CGImageSource=}24@0:8@16"
- "^{CGPDFForm=}"
- "^{CGPDFForm=}16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__CFDictionary=}"
- "^{__CFDictionary=}16@0:8"
- "_MUBaseImage"
- "_UIViewBoundingPathChangeObserver"
- "_acceptsFailureRequirements"
- "_actionsNotEnablingMarkup"
- "_activateInteractionTypes:"
- "_addBoundingPathChangeObserver:"
- "_adjustImageInteractionForScrollEvent:"
- "_adjustScrollViewForKeyboardNotification:"
- "_akUndoManager"
- "_allowShakeToUndo"
- "_allowsThumbnailViewPageReordering"
- "_alreadyLoggedSavingForThisDocument"
- "_analysisButtonContainer"
- "_animateUsingDefaultTimingWithOptions:animations:completion:"
- "_annotationController"
- "_annotationDidEndEditing:"
- "_annotationRectInOverlay:pageIndex:"
- "_annotationWillBeginEditing:"
- "_archivedModelData"
- "_backgroundColor"
- "_bailFailedAnimateEnterMarkup"
- "_baseInsetsForAccessoryOnEdge:hasCustomClientInsets:accessorySize:additionalInsetFromEdge:"
- "_blurEffect"
- "_blurView"
- "_bottomRightButtonsContainer"
- "_bottomRightButtonsContainerBottomConstraint"
- "_bottomRightButtonsContainerRightConstraint"
- "_boundingPathMayHaveChangedForView:relativeToBoundsOriginOnly:"
- "_cachedThumnailViewInsets"
- "_canShowWhileLocked"
- "_cancel"
- "_cancelButton"
- "_centerContentIfNecessaryAdjustingContentOffset:"
- "_centersIgnoringContentInsets"
- "_cleanupPlaceholderImage"
- "_colorFromAppearanceTokens:"
- "_colorFromPDFArray:"
- "_combinedContentView"
- "_commonInit"
- "_compensatingAffineTransformForPage:"
- "_concreteAKAnnotationWithCGPDFAnnotation:ofPage:"
- "_concreteDictionaryRepresentationOfAKAnnotation:forPage:"
- "_constraintsAreHorizontal"
- "_contentContainerView"
- "_contentScrollInset"
- "_contentViewController"
- "_convertToPDFAndWrite:completionHandler:"
- "_createCancelDoneNavBar"
- "_createPDFView"
- "_defaultInteractionTypes"
- "_delegate"
- "_delegateRespondsToDetectedFormInContent"
- "_deletePage:"
- "_deletePages:inDocument:"
- "_detectedEditEnablingMarkup:"
- "_didAppearOnce"
- "_didSetup"
- "_digestedSourceContent"
- "_dismissAction"
- "_doneButton"
- "_doubleTap:"
- "_downsampleImageForDisplay:fromImageSource:withCompletionHandler:"
- "_downsampledImageScale"
- "_edgeInsets"
- "_edgePanGestureRecognizer"
- "_editedImageAnalysisQueue"
- "_editingAnnotaiton"
- "_effectiveBackgroundColor"
- "_effectiveNavBarTitleColor"
- "_effectiveToolbarItemTintColor"
- "_effectiveToolbarTintColor"
- "_encryptPrivateMetadata"
- "_fadeOutDelay"
- "_fadeOutDuration"
- "_finishedWithResultsCompletionBlock"
- "_firstDelegate"
- "_firstLoadZoomToFit"
- "_fixedThumbnailView"
- "_flattenEXIFOrientation:withDownsampling:sourceContent:withContentType:"
- "_flattenEXIFOrientationForHEICData:"
- "_flattenEXIFOrientationOfImage:toDestination:"
- "_flattenImageForAnalysis"
- "_flattenRotation:withDownsampling:sourceImage:"
- "_fontNameFromAppearanceTokens:"
- "_forcesPDFViewTopAlignment"
- "_formDetectedInDocument"
- "_getColorFromAppearanceString:"
- "_getFontFromAppearanceString:ofPDFPage:"
- "_handleImageAnalysis:error:"
- "_handleLoadingWithCompletion:"
- "_hasImageContent"
- "_hasPDFContent"
- "_haveKey"
- "_hdrImage"
- "_headroom"
- "_hostApplicationBundleIdentifier"
- "_hostProcessBundleIdentifier"
- "_image"
- "_imageAnalysisManager"
- "_imageAnalysisOverlayAcceptSingleTouch:"
- "_imageAnalysisRequestId"
- "_imageAnalyzer"
- "_imageInteraction"
- "_imageIsSize:isSmallerThanSize:"
- "_imageIsSmallerThanView"
- "_imageMetadata"
- "_imageOptions"
- "_imageSourceRef"
- "_imageView"
- "_importHandler"
- "_inDoubleTapZoom"
- "_initialContentScale"
- "_inkStyle"
- "_insertBlankPage:atIndex:"
- "_insertBlankPageAfterPage:"
- "_insertDeletedPage:atIndex:"
- "_insertFileAtURL:type:afterPage:completionHandler:"
- "_insertImageWithURL:afterPage:completionHandler:"
- "_insertPDFDocumentWithURL:afterPage:completionHandler:"
- "_insertPage:atIndex:"
- "_insertPageFromFileAfterPage:"
- "_insertPagesFromFileURLs:afterPage:"
- "_insertPagesFromProvidedPDFDocument:toPDFDocument:atPageIndex:"
- "_insertPagesFromScannerAfterPage:"
- "_installContentViewControllerForUTI:"
- "_installOverlayOfController:forPageAtIndex:"
- "_isAnimatingMarkupExtensionTransition"
- "_isFullScreen"
- "_isImageAnalysisPopoverPresented"
- "_isInLowMemoryEnvironment"
- "_isPointerTouch"
- "_key"
- "_keyInitialized"
- "_keyboardWillHide:"
- "_keyboardWillShow:"
- "_label"
- "_latestImageForAnalysis"
- "_loadCompletionBlock"
- "_loadSourceContentWithCompletion:"
- "_localDoubleTapRecognizer"
- "_markupBlackColor"
- "_maxDimensionOfSize:fittingToArea:"
- "_maxImageDimension"
- "_maxImageDimensionInView"
- "_maximumContentOffset"
- "_medianSizeForCurrentDocumentInPDFViewWithGetter:"
- "_minimumContentOffset"
- "_modernToolbar"
- "_navBar"
- "_navBarTitleColor"
- "_navItem"
- "_navigationModeHorizontal"
- "_needToPerformDocumentClosedTeardown"
- "_needToPerformFullTeardown"
- "_needsToolPickerVisibleWhenAnnotationControllerIsAvailable"
- "_newImageSourceWithSourceContent:"
- "_notifyDidChangeShowingSignaturesUI"
- "_observingAKCurrentPageIndex"
- "_opaque"
- "_originalImageDescription"
- "_pageController"
- "_pageIndexForAnnotation:"
- "_pageLabelExistAtPoint:"
- "_pageLabelView"
- "_pageLabelViewTapGestureRecognizer"
- "_pdfDocument"
- "_pdfForm"
- "_pdfView"
- "_pdfViewDelegateProxy"
- "_pdfViewLeadingConstraint"
- "_pencilAlwaysDraws"
- "_placeholderCanBeUsedForBaseImageOfSize:"
- "_placeholderImage"
- "_placeholderImageView"
- "_pointSizeFromAppearanceTokens:"
- "_pointToCenterAfterRotation"
- "_preferredFileDisplayName"
- "_preferredFileDisplayNameForSourceContent:"
- "_prepareToRotate"
- "_presentDocumentPicker:"
- "_presentDocumentScannerAfterPage:"
- "_presentPlaceholderImage"
- "_presentationMode"
- "_presentationModeAllowsEditing"
- "_presentationModeAllowsMarkupOverlays"
- "_presentingView"
- "_primaryAction"
- "_privateImageMetadataDescriptors"
- "_readAnnotationsFromDataProvider:"
- "_readBaseImageFromDataProvider:providerSource:baseWasValid:"
- "_readDataFromTagAtPath:inMetadata:"
- "_recoverFromRotation"
- "_registerActionNotEnablingMarkup:"
- "_remoteViewControllerProxy"
- "_removeBoundingPathChangeObserver:"
- "_removePageLabelViewConstraints"
- "_renderImageForBaseImage:controller:wantsHDR:opaque:"
- "_resetOriginalDelegate"
- "_rotatePage:clockwise:"
- "_sandboxExtensionHandle"
- "_saveEditing:"
- "_scanImageToPDFConversionHandler"
- "_scanPDFHandler"
- "_scrollViewDelegate"
- "_scrollerBackgroundView"
- "_sdrImage"
- "_secondDelegate"
- "_setAsPDFViewDelegatePrivateIfNecessary"
- "_setContentScrollInset:"
- "_setContinuousCornerRadius:"
- "_setData:withArchivedModelData:withCompletion:"
- "_setFileURL:withArchivedModelData:withCompletion:"
- "_setImage:withCompletionHandler:"
- "_setIndicatorInsetAdjustmentBehavior:"
- "_setLegacyToolbarHidden:animated:"
- "_setPresentationModeForImageContent:"
- "_setPresentationModeForPDFContent:"
- "_setThumbnailViewHidden:"
- "_setupAnalysisButtonsContainerInView:"
- "_setupAndStartImageAnalysisIfNeeded"
- "_setupAnnotationController"
- "_setupImageAnalysis"
- "_setupInitialBaseModelScaleFactorWithScreenSize:windowDecorationSize:"
- "_setupNotificationsObservation"
- "_setupScrollViewForImageOfScaledSize:"
- "_shapeDetectionEnabled"
- "_shouldEnterVisualSearchAfterNextAnalysis"
- "_shouldFlattenEXIFOrientation:andDownsample:sourceContent:"
- "_shouldHighlightTextAndDDAfterNextAnalysis"
- "_shouldResignFirstResponder"
- "_shouldShowMarkupOverlays"
- "_shouldShowThumbnailView"
- "_shouldShowUndoRedoButtonsInNavigationBar"
- "_shouldUpliftSubjectAfterNextAnalysis"
- "_shouldUseAKAnnotation:toRepresentCGPDFAnnotation:"
- "_showAsFormSheet"
- "_showShareButtonInToolbar"
- "_showTextStyleOptions:"
- "_showThumbnailViewForMultipage"
- "_showingSignaturesUI"
- "_showsThumbnailView"
- "_sizeFittingArea:withSize:"
- "_sourceContent"
- "_sourceContentReplacedAnnotationMaps"
- "_sourceContentType"
- "_sourceContentType:"
- "_sourceImageMayContainBaseImageAndModel"
- "_sourceImagePixelSize"
- "_startImageAnalysisWithRequest:"
- "_startObservingAnnotationController"
- "_stopObservingAnnotationController"
- "_stringByTrimmingDotDirectories"
- "_subtitle"
- "_suggestedContentSizeForImageSource:"
- "_suggestedContentSizeForPDF:"
- "_teardownPDFViewIfNecessary"
- "_tentativePlaceholderImage"
- "_thumbnailView"
- "_thumbnailViewCellSize"
- "_thumbnailViewExistAtPoint:"
- "_thumbnailViewHidden"
- "_thumbnailViewHolder"
- "_thumbnailViewHolderConstraints"
- "_thumbnailViewHolderRevealConstraint"
- "_thumbnailViewHolderWidthConstraint"
- "_thumbnailViewLeadingConstraint"
- "_thumbnailViewStyle"
- "_thumbnailViewWidth"
- "_timer"
- "_title"
- "_tokenizeAppearanceString:"
- "_toolbar"
- "_toolbarBottomConstraint"
- "_toolbarHidden"
- "_toolbarItemTintColor"
- "_toolbarPosition"
- "_toolbarShareButtonTapped:"
- "_toolbarTintColor"
- "_toolbarTopAttachedConstraint"
- "_toolbarTopConstraint"
- "_transitionDimmingView"
- "_uninstallOverlayOfController:forPageAtIndex:"
- "_uniqueTemporaryDirectory"
- "_updateAnalysisButtonContainerWithAnimation:"
- "_updateAnalysisButtonWithAnimation:"
- "_updateAnalysisButtonsContainerConstraints"
- "_updateAndLoadSourceContent:withArchivedModelData:withCompletion:"
- "_updateAppearanceForTraitCollection:"
- "_updateCachedThumbnailViewInsetsDidChangeLeftOrRight"
- "_updateConstraintsForBarPosition:"
- "_updateInfoButtonWithAnimation:"
- "_updateMinMaxZoomFactor"
- "_updateNavBarProperties"
- "_updatePDFViewDisplayMode"
- "_updatePageNumberOverlayToPage:animate:"
- "_updatePeekSize"
- "_updateThumbnailView"
- "_updateThumbnailViewAppearance"
- "_updateThumbnailViewHolderBackgroundColor"
- "_updateThumbnailViewHolderConstraints"
- "_updateThumbnailViewHolderVisibility"
- "_updateThumbnailViewWithTraitCollection:"
- "_updateundoBarButtonWithController:"
- "_useFancyTransition"
- "_useLegacyToolbar"
- "_usePlaceholderAsDisplayImageIfPossible"
- "_userChangedScrollViewMagnificationNotification:"
- "_userDidCancel"
- "_viewIsTransitioningBetweenSizes"
- "_viewTransitionPageToCenter"
- "_viewTransitionPointOnPageToCenter"
- "_viewTransitionPreviousAutoscalingState"
- "_viewTransitionPreviousScale"
- "_visualSearchViewContainer"
- "_wasZoomToFit"
- "_whiteView"
- "_writeToDataConsumer:embedSourceImageAndEditModel:error:"
- "_writeToDataConsumer:embedSourceImageAndEditModel:options:error:"
- "_zoomRectForScale:withCenter:"
- "_zoomToFitRestoreValue"
- "_zoomToFitZoomFactor"
- "_zoomToFitZoomFactorInBounds:"
- "_zoomToFitZoomFactorIncludingScrollViewEdgeInsets"
- "acceptSingleTouch:"
- "actionInfoItemExistsAtPoint:"
- "actionWithTitle:image:identifier:handler:"
- "actionWithTitle:style:handler:"
- "actionsNotEnablingMarkup"
- "activateConstraints:"
- "activateVisualSearchInteraction"
- "activeInteractionTypes"
- "actualOrPlaceholderTextOfAnnotation:"
- "adaptivePresentationStyleForPresentationController:"
- "adaptivePresentationStyleForPresentationController:traitCollection:"
- "addAKAnnotation:toAnnotationDictionary:"
- "addAction:"
- "addAppearanceStreamOfAnnotation:forPage:toDictionary:"
- "addBorderStyleOfAnnotation:toDictionary:"
- "addBoundsOfAnnotation:forPage:toDictionary:"
- "addChildViewController:"
- "addConstraint:"
- "addConstraints:"
- "addContentsStringOfAnnotation:toDictionary:"
- "addDefaultAppearanceStreamOfAnnotation:toDictionary:"
- "addEntriesFromDictionary:"
- "addFlagsOfAnnotation:toDictionary:"
- "addGainMapImageToImageDestination:sdrImage:hdrImage:imageMetadata:imageOptions:"
- "addGestureRecognizer:"
- "addHDRImageToImageDestination:hdrImage:imageMetadata:imageOptions:"
- "addInteraction:"
- "addInteractionIfNeeded"
- "addModificationDateOfAnnotation:toDictionary:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:forKeyPath:options:context:"
- "addObserver:selector:name:object:"
- "addQuaddingOfAnnotation:toDictionary:"
- "addRGBColor:forKey:toDictionary:"
- "addString:toDictionary:forKey:"
- "addSubview:"
- "addTextLabelOfAnnotation:toDictionary:"
- "addTextOfAnnotation:toDictionary:forKey:canUsePlaceholder:"
- "additionalEditMenuElementsForSelection:"
- "adjustAnnotationBoundsToFitText:"
- "adjustContentInsetsForBars"
- "adjustImageInteractionForScrollView:"
- "adjustScrollViewToAccomodateKeyboardStartingFrame:endingFrame:annotationFrame:inOverlayView:withAnimationDuration:curve:"
- "adjustedSourceImageSize"
- "akColorWithSRGBRed:green:blue:alpha:"
- "akColorWithWhite:alpha:"
- "akController"
- "akToolbarButtonItemType"
- "akUndoManager"
- "alertControllerWithTitle:message:preferredStyle:"
- "alignment"
- "allEditingDisabled"
- "allObjects"
- "allowShakeToUndo"
- "allowsDocumentAssembly"
- "allowsDocumentChanges"
- "allowsEditing"
- "allowsPageReordering"
- "allowsThumbnailViewPageReordering"
- "alpha"
- "alreadyLoggedSavingForThisDocument"
- "analysis"
- "analysisButton"
- "analysisButtonContainer"
- "animateAlongsideTransition:completion:"
- "animateExitWithInfo:"
- "animateWithDuration:animations:"
- "animateWithDuration:animations:completion:"
- "animateWithDuration:delay:options:animations:completion:"
- "animationDuration"
- "annotationController"
- "annotationController:detectedEditOfType:"
- "annotationControllerOfContentViewController:willSetToolbarItems:"
- "annotationEditingEnabled"
- "annotationHeadroom"
- "annotationText"
- "annotationWithData:"
- "annotations"
- "appendAttributedString:"
- "appendData:"
- "archivedModelData"
- "archivedPageModelControllers"
- "array"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "arrowHeadStyle"
- "attribute:atIndex:effectiveRange:"
- "attributeController"
- "attributedStringWithAttachment:"
- "autoScaleFactor"
- "autoScales"
- "autorelease"
- "backgroundColor"
- "base64EncodedDataWithOptions:"
- "base64EncodedStringWithOptions:"
- "becomeFirstResponder"
- "begin"
- "beginAppearanceTransition:animated:"
- "beginDismissWithInfo:"
- "beginLogging:documentType:"
- "beginPDFViewRotation"
- "blackColor"
- "boldSystemFontOfSize:"
- "boolForKey:"
- "boolValue"
- "bottomAnchor"
- "bottomRightButtonsContainer"
- "bottomRightButtonsContainerBottomConstraint"
- "bottomRightButtonsContainerRightConstraint"
- "bounds"
- "boundsForBox:"
- "bringSubviewToFront:"
- "bundleForClass:"
- "bundleIdentifier"
- "bundleWithIdentifier:"
- "bytes"
- "cStringUsingEncoding:"
- "cachedThumnailViewInsets"
- "calendarWithIdentifier:"
- "canBecomeFirstResponder"
- "canConnectToStylus"
- "canEditContent"
- "canEditPDF"
- "canEncryptDocument"
- "canPerformAction:withSender:"
- "canResignFirstResponder"
- "canShowPageViewLabel"
- "canUndo"
- "cancel:"
- "cancelAllRequests"
- "cancelButton"
- "cancelRequestWithError:"
- "centerContentIgnoringInsets"
- "centersIgnoringContentInsets"
- "characterAtIndex:"
- "characterIndexesForQuadPoints:onPageAtIndex:forAnnotationController:"
- "childAnnotation"
- "class"
- "classForAnnotationType:"
- "classForPage"
- "cleanImageMetadataFromData:"
- "clearColor"
- "clearHighlightableSelectionForAnnotationController:"
- "clearTimer"
- "clientPreviewOptions"
- "code"
- "color"
- "colorUsingSRGBColorSpace"
- "colorWithCGColor:"
- "colorWithRed:green:blue:alpha:"
- "colorWithWhite:alpha:"
- "combinedContentView"
- "commit"
- "commitEditing"
- "completeRequestReturningItems:completionHandler:"
- "configurationWithImage:title:subtitle:primaryAction:dismissAction:"
- "conformsToAKFilledAnnotationProtocol"
- "conformsToAKStrokedAnnotationProtocol"
- "conformsToAKTextAnnotationProtocol"
- "conformsToProtocol:"
- "conformsToType:"
- "constant"
- "constraintEqualToAnchor:"
- "constraintEqualToAnchor:constant:"
- "constraintEqualToConstant:"
- "constraintGreaterThanOrEqualToAnchor:constant:"
- "constraintLessThanOrEqualToAnchor:"
- "constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:"
- "constraintsAreHorizontal"
- "constraintsWithVisualFormat:options:metrics:views:"
- "containsObject:"
- "containsString:"
- "contentContainerView"
- "contentControllerDidUnlockDocument:"
- "contentImageForImageAnalysisInteraction:"
- "contentInset"
- "contentSize"
- "contentSnapshot"
- "contentViewController"
- "contentViewController:shouldHandleURL:"
- "contentViewForImageAnalysisInteraction:"
- "contentViewScrollView"
- "contents"
- "contentsRectForImageAnalysisInteraction:"
- "controller:didChangeToPDFPageIndex:"
- "controller:didPlaceSingleShotAnnotation:onPageModelController:"
- "controller:performActionForMode:fromSender:withAttribute:onPageAtIndex:"
- "controller:setFormFillingEnabled:"
- "controller:shouldOpenLinkAtURL:"
- "controller:shouldPlaceSingleShotAnnotation:onProposedPageModelController:"
- "controller:willPlaceSingleShotAnnotation:onProposedPageModelController:"
- "controller:willSetToolbarItems:"
- "controllerCanBecomeFirstResponder:"
- "controllerCanShowWhileLocked:"
- "controllerDidChangeContent:"
- "controllerDidDismissPopover:"
- "controllerDidEnterToolMode:"
- "controllerDidExitToolMode:"
- "controllerShouldDetectFormElements:"
- "controllerWantsToShowShareSheet:"
- "controllerWillDismissSignatureCaptureView:"
- "controllerWillDismissSignatureManagerView:"
- "controllerWillEnterToolMode:"
- "controllerWillExitToolMode:"
- "controllerWillShowSignatureCaptureView:"
- "controllerWillShowSignatureManagerView:"
- "controllerWithDelegate:"
- "convertPoint:fromModelToOverlayWithPageIndex:forAnnotationController:"
- "convertPoint:fromOverlayToModelWithPageIndex:forAnnotationController:"
- "convertPoint:fromView:"
- "convertPoint:toView:"
- "convertRect:fromView:"
- "convertRect:toCoordinateSpace:"
- "convertRect:toView:"
- "convertToPDFAndWrite:completionHandler:"
- "coordinateReadingItemAtURL:options:error:byAccessor:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createArchivedModelData"
- "createDictionaryFromPDFDictionary:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "createPDFDateString:"
- "currentDevice"
- "currentPage"
- "customEdgeInsets"
- "customPlaceholderText"
- "customSketchOverlayInsets"
- "d"
- "d16@0:8"
- "d24@0:8@16"
- "d32@0:8Q16@\"AKController\"24"
- "d32@0:8Q16@\"MUContentViewController\"24"
- "d32@0:8Q16@24"
- "d40@0:8{CGSize=dd}16d32"
- "d48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "darkGrayColor"
- "data"
- "dataDetectorDetectionControllerDidDismissAction:"
- "dataDetectorDetectionControllerWillPresentAction:"
- "dataDetectorExistsAtPoint:"
- "dataRepresentation"
- "dataRepresentationEmbeddingSourceImageAndEditModel:error:"
- "dataRepresentationEmbeddingSourceImageAndEditModel:withDestinationType:error:"
- "dataRepresentationWithError:"
- "dataWithBytes:length:"
- "dataWithCapacity:"
- "date"
- "dateWithTimeIntervalSinceNow:"
- "dealloc"
- "debugDescription"
- "decryptData:"
- "defaultCenter"
- "defaultFormat"
- "defaultManager"
- "defaultMaxHDRGain"
- "defaultMetrics"
- "defaultParagraphStyle"
- "defaultToolTag"
- "delegate"
- "delegateRespondsToDetectedFormInContent"
- "delete:"
- "description"
- "deselectAllAnnotations"
- "dictionary"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "didAppearOnce"
- "didChangeValueForKey:"
- "didMatchString:"
- "didMoveToParentViewController:"
- "didReceiveMemoryWarning"
- "didSetup"
- "digestedSourceContent"
- "disableActions"
- "dismissAction"
- "dismissPresentedPopoversAnimated:"
- "dismissViewControllerAnimated:completion:"
- "displayBox"
- "displayMode"
- "document"
- "documentCameraViewController:didFailWithError:"
- "documentCameraViewController:didFinishWithScan:"
- "documentCameraViewControllerDidCancel:"
- "documentCanBeEdited:"
- "documentDidBeginDocumentFind:"
- "documentDidBeginPageFind:"
- "documentDidCloseTeardown"
- "documentDidEndDocumentFind:"
- "documentDidEndPageFind:"
- "documentDidFindMatch:"
- "documentDidUnlock:"
- "documentIsLocked"
- "documentPicker:didPickDocumentAtURL:"
- "documentPicker:didPickDocumentsAtURLs:"
- "documentPickerWasCancelled:"
- "documentScrollView"
- "documentUnlockedWithPassword"
- "domain"
- "done:"
- "doneButton"
- "doubleTapGestureRecognizer"
- "downsampledImageScale"
- "drawInRect:"
- "drawingBounds"
- "duplicate:"
- "edgeInsets"
- "edgeSwipeGestureRecognized:"
- "editCheckpointReachedForAnnotationController:"
- "editDetectedForAnnotationController:"
- "editTextAnnotation:"
- "editingAnnotaiton"
- "editor:detectedFormInContent:"
- "editor:didDismissViewControllerWithAnimation:"
- "editor:needsScreenEdgePanGestureRecognition:"
- "editor:needsToUpdateChromeWithAnimation:"
- "editor:willPresentViewControllerWithAnimation:"
- "editorCanShowWhileLocked:"
- "editorDidChangeContent:enablingMarkup:"
- "editorDidUnlockDocument:"
- "editorShouldAllowEditingContents:"
- "effectWithStyle:"
- "effectiveUserInterfaceLayoutDirection"
- "enableHDRAnnotations"
- "enableMarkupMode:"
- "encodedModelFromAnnotationsController:encrypt:"
- "encryptData:"
- "encryptPrivateMetadata"
- "endAnnotationEditing"
- "endAppearanceTransition"
- "endLogging"
- "endPDFViewRotation"
- "endPoint"
- "enumerateFontAttributesOfAttributedString:usingBlock:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "exifOrientationOfPage:"
- "exportedInterface"
- "extensionContext"
- "fadeOut"
- "feedbackMetadataForImageAnalysisInteraction:"
- "feedbackOptionsForImageAnalysisInteraction:"
- "feedbackTypeForImageAnalysisInteraction:"
- "fieldName"
- "fileExistsAtPath:"
- "filePathURL"
- "fileURLWithPath:"
- "fillColor"
- "filledInfoButtonGlyphName"
- "filteredToolbarItemsForItems:fromController:"
- "finalizeCrop"
- "find:"
- "findInteraction"
- "findNext"
- "findNext:"
- "findPrevious"
- "findPrevious:"
- "finishedWithResultsCompletionBlock"
- "firstDelegate"
- "firstLoadZoomToFit"
- "firstObject"
- "fixedThumbnailView"
- "flattenImageForAnalysis"
- "flattenRotationTransformForPage:outMediaBox:outCropBox:"
- "floatValue"
- "floatingAttributeToolbarContainer"
- "fontName"
- "fontWithName:size:"
- "forceHideRuler"
- "forcesPDFViewTopAlignment"
- "formDetectedInDocument"
- "formFillingEnabled"
- "forwardInvocation:"
- "forwardingTargetForSelector:"
- "frame"
- "fullTeardown"
- "gestureRecognizers"
- "getBytes:length:"
- "getFullFieldNameFromAnnotationDictionary:"
- "getMenuElementsForPage:"
- "getRGBColorForKey:fromAnnotationDictionary:"
- "getRed:green:blue:alpha:"
- "getResourceValue:forKey:error:"
- "getTextStringForKey:fromAnnotationDictionary:"
- "goToPage:"
- "handleBackTabInTextEditorForAnnotation:forAnnotationController:"
- "handleTabInTextEditorForAnnotation:forAnnotationController:"
- "handleTextSuggestion:forAnnotationController:completionHandler:"
- "hasActiveTextSelection"
- "hasActiveTextSelectionDidChangeForImageAnalysisInteraction:"
- "hasAnalysis"
- "hasHighlightableSelectionForAnnotationController:"
- "hasPrivateImageMetadata:"
- "hasResultsForAnalysisTypes:"
- "hasResultsForVisualSearch"
- "hash"
- "hdrImage"
- "headroom"
- "heightAnchor"
- "heightIncludingAdditionalVisibleBars"
- "hideBanner"
- "highlight:"
- "highlightSelectableItems"
- "highlightableSelectionCharacterIndexesOnPageAtIndex:forAnnotationController:"
- "horizontalSizeClass"
- "hostProcessBundleIdentifier"
- "i16@0:8"
- "idealContentSizeForScreenSize:windowDecorationSize:"
- "identifier"
- "image"
- "imageAnalysisInteraction:didRequestLiveTextButtonSelectedState:"
- "imageAnalysisInteraction:didTapVisualSearchIndicatorWithNormalizedBoundingBox:"
- "imageAnalysisInteraction:highlightSelectedItemsValueDidChange:"
- "imageAnalysisInteraction:imageAnalysisBarItemPressed:"
- "imageAnalysisInteraction:imageAnalysisButtonPressed:"
- "imageAnalysisInteraction:isDraggingVisualIntelligenceSheetDidChange:"
- "imageAnalysisInteraction:livePhotoShouldPlay:"
- "imageAnalysisInteraction:liveTextButtonDidChangeToVisible:"
- "imageAnalysisInteraction:prepareForCalloutAction:competion:"
- "imageAnalysisInteraction:shouldBeginAtPoint:forAnalysisType:"
- "imageAnalysisInteraction:shouldHandleShareWithRanges:boundingRect:selectedText:selectedAttributedText:"
- "imageAnalysisInteraction:shouldShowLookupForItemFromCallout:"
- "imageAnalysisInteraction:updateAttributedStringForCopy:"
- "imageAnalysisInteraction:updateStringForCopy:"
- "imageAnalysisInteraction:visualIntelligenceVluEnabledDidChange:"
- "imageAnalysisInteractionDidBeginSubjectAnalysis:"
- "imageAnalysisInteractionDidCompleteSubjectAnalysis:"
- "imageAnalysisInteractionDidDismissVisualSearchController"
- "imageAnalysisInteractionDidDismissVisualSearchController:"
- "imageAnalysisInteractionSubjectInteractionInProgressDidChange:"
- "imageAnalysisInteractionWillPresentVisualSearchController"
- "imageAnalysisManager"
- "imageAnalysisPopoverDidDisappear"
- "imageAnalysisPopoverWillAppear"
- "imageAnalysisQueue"
- "imageAnalysisRequestId"
- "imageAnalysisView"
- "imageAnalyzer"
- "imageAnalyzerWantsUpdateInfoButtonWithAnimation:"
- "imageAnalyzerWantsUpdateOverlayViews"
- "imageDescriptionFromSourceContent:"
- "imageForAnalysis"
- "imageInteraction"
- "imageMetadata"
- "imageNamed:inBundle:compatibleWithTraitCollection:"
- "imageOfPageAtIndex:"
- "imageOptions"
- "imageOrientation"
- "imageSourceRef"
- "imageSubjectExistsAtPoint:"
- "imageView"
- "imageViewCombinedContentView"
- "imageWithActions:"
- "imageWithCGImage:"
- "imageWithData:"
- "importHandler"
- "inDoubleTapZoom"
- "indexForPage:"
- "indexOfDictionary:inArray:"
- "indexOfObject:"
- "indexOfObjectPassingTest:"
- "infoButtonGlyphName"
- "infoButtonTapped"
- "init"
- "initForOpeningContentTypes:asCopy:"
- "initWithAttributedString:"
- "initWithBarButtonSystemItem:target:action:"
- "initWithBase64EncodedData:options:"
- "initWithBase64EncodedString:options:"
- "initWithBaseImage:allowHDR:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithData:"
- "initWithDelegate:presentingView:"
- "initWithEffect:"
- "initWithFilePresenter:"
- "initWithForm:"
- "initWithFrame:"
- "initWithFrame:style:"
- "initWithImage:options:"
- "initWithImage:requestType:"
- "initWithNibName:bundle:"
- "initWithNibName:bundle:delegate:"
- "initWithPDFDocument:delegate:"
- "initWithSize:format:"
- "initWithSourceContent:archivedDataModel:delegate:"
- "initWithString:"
- "initWithTarget:action:"
- "initWithTitle:"
- "initWithURL:"
- "initialContentScale"
- "initializeKey"
- "inkStyle"
- "insertPage:atIndex:"
- "insertPages:atIndexes:inDocument:"
- "insertSubview:above:"
- "insertSubview:atIndex:"
- "insertSubview:belowSubview:"
- "installDrawingGestureRecognizer:forPageAtIndex:forAnnotationController:"
- "instancesRespondToSelector:"
- "interactions"
- "interfaceWithProtocol:"
- "invalidate"
- "invokeWithTarget:"
- "isAnalysisOngoing"
- "isAnimatingMarkupExtensionTransition"
- "isBannerVisible"
- "isDashed"
- "isDescendantOfView:"
- "isEncrypted"
- "isEqual:"
- "isEqualToDictionary:"
- "isEqualToString:"
- "isFirstResponder"
- "isFullScreen"
- "isHighDynamicRange"
- "isImageAnalysisPopoverPresented"
- "isImageSubjectHighlightingEnabled"
- "isInFormFillingMode"
- "isInteractionActive"
- "isKindOfClass:"
- "isLocked"
- "isMainThread"
- "isMemberOfClass:"
- "isNavigationModeHorizontal"
- "isObservingAKCurrentPageIndex"
- "isOverlayViewLoadedAtIndex:"
- "isProxy"
- "isShapeDetectionEnabled"
- "isShowingLivePhotoForImageAnalysisInteraction:"
- "isSupported"
- "isTextSelectionEnabled"
- "isThumbnailViewHidden"
- "isTimerInstalled"
- "isToolbarHidden"
- "isTouchInThumbnailView:"
- "isUsedOnDarkBackground"
- "isViewLoaded"
- "isVisualIntelligenceSheetPresentedDidChangeForImageAnalysisInteraction:"
- "isVisualSearchEnabled"
- "isZooming"
- "lastPathComponent"
- "latestImageForAnalysis"
- "layer"
- "layerContainingQuickBackgroundForLoupeOnOverlayAtPageIndex:forAnnotationController:"
- "layoutIfNeeded"
- "layoutSubviews"
- "leadingAnchor"
- "legacyDoodleController"
- "length"
- "loadCompletionBlock"
- "loadContentWithCompletionBlock:"
- "loadWithData:archivedModelData:placeholderImage:completionHandler:"
- "loadWithURL:archivedModelData:placeholderImage:completionHandler:"
- "localDoubleTapRecognizer"
- "localizedStringForKey:value:table:"
- "locationInView:"
- "logFileTypeOpened:byProcess:"
- "logFileTypeSaved:byProcess:"
- "longLongValue"
- "lowercaseString"
- "mainBundle"
- "mainScreen"
- "mapTableWithKeyOptions:valueOptions:"
- "markupBarButtonItemWithTarget:action:"
- "markupViewController:didChangeShowingSignaturesUI:"
- "maxImageDimension"
- "maxPageRectWithPageIndex:forAnnotationController:"
- "maximumZoomScale"
- "menuElementsForPage:"
- "menuItems:forPage:"
- "methodSignatureForSelector:"
- "migrateAKFilledAnnotationPropertiesTo:fromAnnotationDictionary:ofPDFPage:"
- "migrateAKRectangularShapeAnnotationPropertiesTo:fromAnnotationDictionary:ofPDFPage:"
- "migrateAKStrokedAnnotationPropertiesTo:fromAnnotationDictionary:ofPDFPage:"
- "migrateAKTextAnnotationPropertiesTo:fromAnnotationDictionary:ofPDFPage:"
- "migrateAppearanceStreamFromCGPDFAnnotationDict:toAKAnnotation:compensatingForPageRotation:"
- "minimumZoomScale"
- "minusSet:"
- "modelBaseScaleFactorOfPageAtIndex:forAnnotationController:"
- "modelBaseScaleFactorOfPageAtIndex:forContentViewController:"
- "modelController"
- "modernToolbar"
- "modernToolbarView"
- "modifiedImageDescription"
- "motionEnded:withEvent:"
- "muDeepMutableCopy"
- "mu_markupAppIcon"
- "mutableArrayValueForKey:"
- "mutableBytes"
- "mutableCopy"
- "mutableCopyWithZone:"
- "nativeBounds"
- "nativeScale"
- "navBarTitleColor"
- "navItem"
- "navigationBar:didPopItem:"
- "navigationBar:didPushItem:"
- "navigationBar:shouldPopItem:"
- "navigationBar:shouldPushItem:"
- "navigationBarNSToolbarSection:"
- "navigationItem"
- "navigationModeHorizontal"
- "needToPerformDocumentClosedTeardown"
- "needToPerformFullTeardown"
- "needsToolPickerVisibleWhenAnnotationControllerIsAvailable"
- "newAKAnnotationFromCGPDFAnnotation:"
- "newAKAnnotationWithCGPDFAnnotation:ofPage:"
- "newContentSnapshotPDFDataIncludingAdornments:atScale:inRect:onOverlayAtPageIndex:forAnnotationController:"
- "newPlaceholderAKAnnotationWithCGPDFAnnotation:ofPage:"
- "newTextStorageOriginalFontSavvyWithString:attributes:"
- "normalizedRotationAngleOfPage:"
- "null"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithLong:"
- "numberWithUnsignedChar:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "object"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observeValueForKeyPath:ofObject:change:context:"
- "observingAKCurrentPageIndex"
- "opaque"
- "orientation"
- "originalExifOrientation"
- "originalImageDescription"
- "originalModelBaseScaleFactor"
- "outputContentType"
- "outputType"
- "outputTypesSupportingHDR"
- "overlayViewAtIndex:"
- "pageAtIndex:"
- "pageController"
- "pageCount"
- "pageLabelView"
- "pageLabelViewSideConstraint"
- "pageLabelViewTapped:"
- "pageLabelViewTopConstraint"
- "pageModelControllerForAnnotation:"
- "pageRef"
- "pageViewForPageAtIndex:"
- "panGestureRecognizer"
- "parentViewController"
- "passwordUsedForUnlocking"
- "path"
- "pdfDictionaryRepresentationOfAKAnnotation:forPage:"
- "pdfDocument"
- "pdfDocumentDidUnlock:"
- "pdfForm"
- "pdfPageOptionsForImageRef:withPreviousPage:"
- "pdfScrollViewWillBeginDragging:"
- "pdfViewContentInset"
- "pdfViewDelegateProxy"
- "pdfViewDidChangeCurrentPage:"
- "pdfViewLeadingConstraint"
- "penStrokeCompletedForAnnotationController:"
- "pencilAlwaysDraws"
- "performActionForSender:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performWithoutAnimation:"
- "pinchGestureRecognizer"
- "placeAuxiliaryView:forAnnotationController:"
- "placeholderImage"
- "placeholderImageView"
- "pointSize"
- "popoverPresentationController"
- "popoverPresentingViewControllerForAnnotationController:"
- "populateFromArchivedPageModelControllers:"
- "positionForBar:"
- "positionSketchOverlay:forAnnotationController:"
- "positionSketchOverlay:forContentViewController:"
- "postNotificationName:object:"
- "preferredContentSizeCategory"
- "preferredFileDisplayName"
- "preferredFilenameExtension"
- "preferredStatusBarStyle"
- "prepareOverlayAtIndex:"
- "prepareWithInvocationTarget:"
- "presentFindNavigatorShowingReplace:"
- "presentViewController:animated:completion:"
- "presentationController"
- "presentationController:prepareAdaptivePresentationController:"
- "presentationController:viewControllerForAdaptivePresentationStyle:"
- "presentationController:willPresentWithAdaptiveStyle:transitionCoordinator:"
- "presentationControllerDidAttemptToDismiss:"
- "presentationControllerDidDismiss:"
- "presentationControllerShouldDismiss:"
- "presentationControllerWillDismiss:"
- "presentationMode"
- "presentingView"
- "presentingViewControllerForImageAnalysisInteraction:"
- "pressGestureRecognizer"
- "primaryAction"
- "processRequest:progressHandler:completionHandler:"
- "promisedFeedbackAttachementsForImageAnalysisInteraction:"
- "q"
- "q16@0:8"
- "q24@0:8@\"<UIBarPositioning>\"16"
- "q24@0:8@\"UINavigationBar\"16"
- "q24@0:8@\"UIPresentationController\"16"
- "q24@0:8@16"
- "q24@0:8^{CGPDFPage=}16"
- "q32@0:8@\"UIPresentationController\"16@\"UITraitCollection\"24"
- "q32@0:8@16@24"
- "quadPoints"
- "quadPointsForCharacterIndexes:onPageAtIndex:forAnnotationController:"
- "quadrilateralValue"
- "quickActionProcessingCompleteForImageAnalysisInteraction:"
- "readAnnotationsFromArchivedModelData:toController:"
- "readArchivedModelDataFromImageData:"
- "readArchivedModelDataFromImageURL:"
- "readBaseImageFromData:baseWasValid:"
- "readBaseImageFromImageAtURL:baseWasValid:"
- "readDefaultAppearanceStringFromPDFDictionary:ofPage:toDictionary:"
- "readQuaddingFromPDFDictionary:toDictionary:"
- "rectangle"
- "redo:"
- "redoActionName"
- "registerItemForTypeIdentifier:loadHandler:"
- "release"
- "relinquishOverlayAtIndex:"
- "removeAllActions"
- "removeAuxiliaryView:forAnnotationController:"
- "removeConstraints:"
- "removeFailureRequirement:"
- "removeFromParentViewController"
- "removeFromSuperview"
- "removeGestureRecognizer:"
- "removeInteraction:"
- "removeItemAtPath:error:"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObjectIdenticalTo:"
- "removeObserver:"
- "removeObserver:forKeyPath:context:"
- "removeObserver:name:object:"
- "removePageAtIndex:"
- "removeThumbnailViewHolderConstraints"
- "renderAnnotation:inContext:"
- "renderAnnotationsOnImage:wantsHDR:opaque:withTransform:shouldApplyCropRect:forPreview:"
- "replaceOccurrencesOfString:withString:options:range:"
- "requestPermissionForController:toPerformActionFromSender:"
- "requireGestureRecognizerToFail:"
- "resetFadeOutTimer"
- "resetPageLabelFadeOutTimer"
- "resetToDefaultToolMode"
- "respondsToSelector:"
- "restoreStrokeColorToSystemDefault"
- "restoreToolModeForContentType"
- "retain"
- "retainCount"
- "reverseObjectEnumerator"
- "revert"
- "rightAnchor"
- "rightBarButtonItems"
- "rotateLeft:"
- "rotateRight:"
- "rotation"
- "rotationGestureRecognizer"
- "rowSizeForPage:"
- "rulerHostWantsSharedRuler"
- "rulerHostingStringFromPixels:"
- "rulerHostingView"
- "safeAreaInsets"
- "safeAreaLayoutGuide"
- "sandboxExtensionHandle"
- "scaleFactor"
- "scaledValueForValue:compatibleWithTraitCollection:"
- "scanImageToPDFConversionHandler"
- "scanPDFHandler"
- "scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:"
- "scrollRectToVisible:animated:"
- "scrollView"
- "scrollViewDelegate"
- "scrollViewDidChangeAdjustedContentInset:"
- "scrollViewDidEndDecelerating:"
- "scrollViewDidEndDragging:willDecelerate:"
- "scrollViewDidEndScrollingAnimation:"
- "scrollViewDidEndZooming:withView:atScale:"
- "scrollViewDidScroll:"
- "scrollViewDidScrollToTop:"
- "scrollViewDidZoom:"
- "scrollViewDidZoomToUnitRect:"
- "scrollViewShouldScrollToTop:"
- "scrollViewWillBeginDecelerating:"
- "scrollViewWillBeginDragging:"
- "scrollViewWillBeginZooming:withView:"
- "scrollViewWillEndDragging:withVelocity:targetContentOffset:"
- "scrollerBackgroundView"
- "sdrImage"
- "secondDelegate"
- "secondItem"
- "selector"
- "self"
- "serviceDidFinishwithResults:andSandboxExtension:"
- "serviceViewControllerInterface"
- "serviceViewControllerProxy"
- "set"
- "setActionInfoViewHidden:animated:"
- "setActionName:"
- "setActionsNotEnablingMarkup:"
- "setActive:"
- "setActiveInteractionTypes:"
- "setAkUndoManager:"
- "setAlignment:"
- "setAllEditingDisabled:"
- "setAllowShakeToUndo:"
- "setAllowsGroupOpacity:"
- "setAllowsMultipleSelection:"
- "setAllowsNativeRenderingOfHighlightableSelection:forAnnotationController:"
- "setAllowsPageReordering:"
- "setAllowsThumbnailViewPageReordering:"
- "setAlpha:"
- "setAlreadyLoggedSavingForThisDocument:"
- "setAnalysis:"
- "setAnalysisButtonContainer:"
- "setAnchorPoint:"
- "setAnnotationController:"
- "setAnnotationEditingEnabled:"
- "setAnnotationText:"
- "setAppearanceOverride:"
- "setArchivedModelData:"
- "setArrowHeadStyle:"
- "setAttachments:"
- "setAttributedText:"
- "setAttributes:"
- "setAutoScales:"
- "setAutomaticallyShowVisualSearchResults:"
- "setAutoresizingMask:"
- "setBackgroundColor:"
- "setBarButtonItem:"
- "setBarTintColor:"
- "setBorderColor:"
- "setBorderWidth:"
- "setBottomRightButtonsContainer:"
- "setBottomRightButtonsContainerBottomConstraint:"
- "setBottomRightButtonsContainerRightConstraint:"
- "setBounds:forBox:"
- "setCachedThumnailViewInsets:"
- "setCalendar:"
- "setCallbackQueue:"
- "setCancelButton:"
- "setCentersIgnoringContentInsets:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setCoalescesDoodles:"
- "setColor:"
- "setCombinedContentView:"
- "setConstant:"
- "setConstraintsAreHorizontal:"
- "setContentContainerView:"
- "setContentHuggingPriority:forAxis:"
- "setContentInset:"
- "setContentInsetAdjustmentBehavior:"
- "setContentOffset:"
- "setContentSize:"
- "setContentViewController:"
- "setContents:"
- "setContentsHidden:"
- "setContentsHidden:animated:"
- "setCurrentPDFPageIndex:"
- "setCurrentPageIndex:"
- "setCustomPlaceholderText:"
- "setDashed:"
- "setData:"
- "setData:withArchivedModelData:"
- "setData:withArchivedModelData:placeholderImage:"
- "setDateFormat:"
- "setDecelerationRate:"
- "setDelegate:"
- "setDelegateRespondsToDetectedFormInContent:"
- "setDidAppearOnce:"
- "setDidSetup:"
- "setDigestedSourceContent:"
- "setDisableActions:"
- "setDismissAction:"
- "setDisplayBox:"
- "setDisplayDirection:"
- "setDisplayMode:"
- "setDocument:"
- "setDocument:waitDuration:"
- "setDoneButton:"
- "setDownsampledImageScale:"
- "setEdgeInsets:"
- "setEdges:"
- "setEditingAnnotaiton:"
- "setEditsDisableAppearanceOverride:"
- "setEffect:"
- "setEnabled:"
- "setEncryptPrivateMetadata:"
- "setEndPoint:"
- "setFieldName:"
- "setFileURL:"
- "setFileURL:withArchivedModelData:"
- "setFileURL:withArchivedModelData:placeholderImage:"
- "setFillColor:"
- "setFindInteractionEnabled:"
- "setFinishedWithResultsCompletionBlock:"
- "setFireDate:"
- "setFirstDelegate:"
- "setFirstLoadZoomToFit:"
- "setFixedThumbnailView:"
- "setFont:"
- "setForcesPDFViewTopAlignment:"
- "setForcesTopAlignment:"
- "setFormDetectedInDocument:"
- "setFormFillingEnabled:"
- "setFormFillingEnabled:didUseBanner:"
- "setFrame:"
- "setHidden:"
- "setHighlightSelectableItems:"
- "setHostProcessBundleIdentifier:"
- "setImage:"
- "setImage:withArchivedModelData:"
- "setImage:withArchivedModelData:placeholderImage:"
- "setImageAnalysisManager:"
- "setImageAnalysisRequestId:"
- "setImageAnalyzer:"
- "setImageInteraction:"
- "setImageURL:"
- "setImageView:"
- "setImportHandler:"
- "setInDoubleTapZoom:"
- "setInFormFillingMode:"
- "setInitialContentScale:"
- "setInkStyle:"
- "setIsAnimatingMarkupExtensionTransition:"
- "setIsFullScreen:"
- "setIsImageAnalysisPopoverPresented:"
- "setIsUsedOnDarkBackground:"
- "setItems:"
- "setKeyboardDismissMode:"
- "setLatestImageForAnalysis:"
- "setLayoutMode:"
- "setLeftBarButtonItems:"
- "setLength:"
- "setLoadCompletionBlock:"
- "setLocalDoubleTapRecognizer:"
- "setMaxHDRGain:"
- "setMaxImageDimension:"
- "setMaximumZoomScale:"
- "setMidPoint:"
- "setMinimumNumberOfTouches:"
- "setMinimumZoomScale:"
- "setModalPresentationStyle:"
- "setModernToolbar:"
- "setNavBar:"
- "setNavBarTitleColor:"
- "setNavItem:"
- "setNavigationModeHorizontal:"
- "setNeedToPerformDocumentClosedTeardown:"
- "setNeedToPerformFullTeardown:"
- "setNeedsLayout"
- "setNeedsStatusBarAppearanceUpdate"
- "setNeedsToolPickerVisibleWhenAnnotationControllerIsAvailable:"
- "setNeedsUpdateConstraints"
- "setNumberOfTapsRequired:"
- "setObject:atIndexedSubscript:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setObservingAKCurrentPageIndex:"
- "setOpaque:"
- "setOriginalExifOrientation:"
- "setOriginalImageDescription:"
- "setOriginalModelBaseScaleFactor:"
- "setOverlayShouldPixelate:"
- "setPDFAKControllerDelegate:"
- "setPDFView:"
- "setPageController:"
- "setPageURL:"
- "setPdfView:"
- "setPdfViewDelegateProxy:"
- "setPdfViewLeadingConstraint:"
- "setPencilAlwaysDraws:"
- "setPermittedArrowDirections:"
- "setPlaceholderImage:"
- "setPlaceholderImageView:"
- "setPreferDoodle:"
- "setPreferredFileDisplayName:"
- "setPreferredImageDynamicRange:"
- "setPresentationMode:"
- "setPresentingView:"
- "setPreservesCenterDuringRotation:"
- "setPrimaryAction:"
- "setPriority:"
- "setQuadPoints:"
- "setRectangle:"
- "setRightBarButtonItem:"
- "setRightBarButtonItems:"
- "setRotation:"
- "setRulerHostingDelegate:"
- "setSandboxExtensionHandle:"
- "setScale:"
- "setScaleFactor:"
- "setScanImageToPDFConversionHandler:"
- "setScanPDFHandler:"
- "setScrollEnabled:"
- "setScrollIndicatorInsets:"
- "setScrollView:"
- "setScrollViewDelegate:"
- "setScrollerBackgroundView:"
- "setSecondDelegate:"
- "setSelectNewlyCreatedAnnotations:"
- "setShapeDetectionEnabled:"
- "setShareButtonAction:"
- "setShareButtonHidden:"
- "setShareButtonTarget:"
- "setShouldEnterVisualSearchAfterNextAnalysis:"
- "setShouldHighlightTextAndDDAfterNextAnalysis:"
- "setShouldResignFirstResponder:"
- "setShouldShowThumbnailView:"
- "setShouldUpliftSubjectAfterNextAnalysis:"
- "setShouldUsePlaceholderText:"
- "setShowAsFormSheet:"
- "setShowShareButtonInToolbar:"
- "setShowThumbnailViewForMultipage:"
- "setShowsThumbnailView:"
- "setSourceContent:"
- "setSourceContent:withArchivedModelData:"
- "setSourceContentReplacedAnnotationMaps:"
- "setSourceContentType:"
- "setSourceImagePixelSize:"
- "setStartPoint:"
- "setStrokeColor:"
- "setStrokeWidth:"
- "setStyle:"
- "setSubjectHighlightActive:"
- "setSubtitle:"
- "setTag:"
- "setTentativePlaceholderImage:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setTextIsFixedHeight:"
- "setTextIsFixedWidth:"
- "setThumbnailContextMenuDelegate:"
- "setThumbnailSize:"
- "setThumbnailView:"
- "setThumbnailViewHidden:"
- "setThumbnailViewHolder:"
- "setThumbnailViewHolderConstraints:"
- "setThumbnailViewHolderRevealConstraint:"
- "setThumbnailViewHolderWidthConstraint:"
- "setThumbnailViewLeadingConstraint:"
- "setThumbnailViewStyle:"
- "setTimeZone:"
- "setTintColor:"
- "setTitle:"
- "setTitleTextAttributes:"
- "setToolbar:"
- "setToolbarBottomConstraint:"
- "setToolbarHidden:"
- "setToolbarHidden:animated:"
- "setToolbarItemTintColor:"
- "setToolbarPosition:"
- "setToolbarTintColor:"
- "setToolbarTopAttachedConstraint:"
- "setToolbarTopConstraint:"
- "setTransform:"
- "setTransitionDimmingView:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setTypingAttributes:"
- "setUndoManagerForBarButtons:"
- "setUndoRedoButtonsHidden:"
- "setUseFancyTransition:"
- "setUseHighVisibilityDefaultInks:"
- "setUsePlaceholderAsDisplayImageIfPossible:"
- "setUserDidCancel:"
- "setUserInteractionEnabled:"
- "setValue:forKey:"
- "setViewIsTransitioningBetweenSizes:"
- "setViewTransitionPageToCenter:"
- "setViewTransitionPointOnPageToCenter:"
- "setViewTransitionPreviousAutoscalingState:"
- "setViewTransitionPreviousScale:"
- "setVisible:forFirstResponder:"
- "setVisualSearchViewContainer:"
- "setWhiteView:"
- "setWithArray:"
- "setWithObjects:"
- "setZoomScale:"
- "setZoomScale:animated:"
- "setZoomToFitRestoreValue:"
- "setup"
- "setupAnalysisButtonsContainer"
- "setupAndStartImageAnalysisIfNeeded"
- "shapeDetectionEnabled"
- "sharedInstance"
- "sharedMenuController"
- "sharedSerialPagesEditionQueue"
- "shouldAcceptTouch:ofGestureRecognizer:"
- "shouldAddTabControlsToTextEditorForAnnotation:forAnnotationController:"
- "shouldEnterVisualSearchAfterNextAnalysis"
- "shouldHideInteraction:animated:"
- "shouldHideMarkupOverlays:animated:"
- "shouldHighlightTextAndDDAfterNextAnalysis"
- "shouldPlaceFormElementAtPoint:onOverlayAtPageIndex:forAnnotationController:"
- "shouldPlaceProposedFormElementAtRect:onOverlayAtPageIndex:forAnnotationController:"
- "shouldResignFirstResponder"
- "shouldShowAnnotationsOfType:"
- "shouldShowThumbnailView"
- "shouldStartImageAnalysisForPresentationMode:"
- "shouldUpliftSubjectAfterNextAnalysis"
- "showAsFormSheet"
- "showAttributeInspector:"
- "showBannerWithConfiguration:"
- "showBannerWithConfiguration:primaryAction:dismissAction:"
- "showNowInSuperView:withText:"
- "showShareButtonInToolbar"
- "showThumbnailViewForMultipage"
- "showsThumbnailView"
- "sidebarAttributedString"
- "size"
- "sizeThatFits:"
- "sketchOverlayInsets"
- "snapshotViewAfterScreenUpdates:"
- "sourceContent"
- "sourceContentReplacedAnnotationMaps"
- "sourceContentType"
- "sourceImagePixelSize"
- "standardUserDefaults"
- "startImageAnalysis"
- "startPoint"
- "state"
- "stopImageAnalysis"
- "string"
- "stringByAppendingPathComponent:"
- "stringByAppendingPathExtension:"
- "stringByDeletingPathExtension"
- "stringFromDate:"
- "stringWithCString:encoding:"
- "stringWithFormat:"
- "stringWithString:"
- "stringWithUTF8String:"
- "strokeColor"
- "strokeColorIsEqualTo:"
- "strokeWidth"
- "style"
- "substringWithRange:"
- "subtitle"
- "subviews"
- "suggestedContentSizeForData:"
- "suggestedContentSizeForURL:"
- "superclass"
- "superview"
- "supportedAnnotationTypes"
- "supportedOutputTypes"
- "supportedUTTypes"
- "supportsFormFill"
- "supportsImageDescriptionEditing"
- "systemBlueColor"
- "systemImageNamed:"
- "tapGestureRecognizer"
- "teardown"
- "temporaryDirectory"
- "tentativePlaceholderImage"
- "textAttachmentWithImage:"
- "textExistsAtPoint:"
- "textSelectionDidChangeForImageAnalysisInteraction:"
- "thumbnailViewHidden"
- "thumbnailViewHolder"
- "thumbnailViewHolderConstraints"
- "thumbnailViewHolderRevealConstraint"
- "thumbnailViewHolderWidthConstraint"
- "thumbnailViewLeadingConstraint"
- "thumbnailViewStyle"
- "timeZoneWithName:"
- "timerInstalled"
- "tintColor"
- "title"
- "toolMode"
- "toolPicker"
- "toolbar"
- "toolbarBottomConstraint"
- "toolbarButtonItemOfType:"
- "toolbarController:positionForBar:"
- "toolbarHidden"
- "toolbarItemTintColor"
- "toolbarPosition"
- "toolbarTintColor"
- "toolbarTopAttachedConstraint"
- "toolbarTopConstraint"
- "toolbarView"
- "toolbarViewController"
- "topAnchor"
- "trailingAnchor"
- "traitCollection"
- "traitCollectionDidChange:"
- "transitionDimmingView"
- "transitioningView"
- "typeWithIdentifier:"
- "undo"
- "undo:"
- "undoActionName"
- "undoManager"
- "undoManagerForAnnotationController:"
- "undoManagerForContentViewController:"
- "uninstallAllAnnotationControllerOverlays"
- "uninstallDrawingGestureRecognizer:forPageAtIndex:forAnnotationController:"
- "unsignedIntegerValue"
- "updateBottomRightContainerPositionForImageView:view:"
- "updateConstraints"
- "updateDrawingGestureRecognizer:forPageAtIndex:withPriority:forAnnotationController:"
- "updateForFullScreen:animated:"
- "updateOverlayViewAtIndex:"
- "updateThumbnailView"
- "useFancyTransition"
- "useNewFullscreenPalette"
- "usePageViewController:withViewOptions:"
- "usePlaceholderAsDisplayImageIfPossible"
- "userDidCancel"
- "userInfo"
- "userInterfaceIdiom"
- "v136@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48{CGRect={CGPoint=dd}{CGSize=dd}}80@112d120q128"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"<MarkupViewControllerDelegate>\"16"
- "v24@0:8@\"<QuickLookContentEditorDelegate>\"16"
- "v24@0:8@\"AKController\"16"
- "v24@0:8@\"MUPDFContentViewController\"16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSData\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSNotification\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"NSURL\"16"
- "v24@0:8@\"NSUndoManager\"16"
- "v24@0:8@\"PDFSelection\"16"
- "v24@0:8@\"PDFView\"16"
- "v24@0:8@\"QuickLookContentEditorBannerConfiguration\"16"
- "v24@0:8@\"UIDocumentPickerViewController\"16"
- "v24@0:8@\"UIImage\"16"
- "v24@0:8@\"UINavigationBar\"16"
- "v24@0:8@\"UIPresentationController\"16"
- "v24@0:8@\"UIScrollView\"16"
- "v24@0:8@\"VKCImageAnalysisInteraction\"16"
- "v24@0:8@\"VNDocumentCameraViewController\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8B16B20"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@\"AKController\"16B24"
- "v28@0:8@\"UIScrollView\"16B24"
- "v28@0:8@\"UIView\"16B24"
- "v28@0:8@\"VKCImageAnalysisInteraction\"16B24"
- "v28@0:8@16B24"
- "v28@0:8B16@\"AKController\"20"
- "v28@0:8B16@20"
- "v28@0:8Q16B24"
- "v32@0:8@\"AKController\"16Q24"
- "v32@0:8@\"NSData\"16@\"NSData\"24"
- "v32@0:8@\"NSURL\"16@\"NSData\"24"
- "v32@0:8@\"NSURL\"16@\"NSString\"24"
- "v32@0:8@\"PDFView\"16@\"NSURL\"24"
- "v32@0:8@\"PDFView\"16@\"PDFActionRemoteGoTo\"24"
- "v32@0:8@\"UIDocumentPickerViewController\"16@\"NSArray\"24"
- "v32@0:8@\"UIDocumentPickerViewController\"16@\"NSURL\"24"
- "v32@0:8@\"UIImage\"16@\"NSData\"24"
- "v32@0:8@\"UINavigationBar\"16@\"UINavigationItem\"24"
- "v32@0:8@\"UIPresentationController\"16@\"UIPresentationController\"24"
- "v32@0:8@\"UIScrollView\"16@\"UIView\"24"
- "v32@0:8@\"UIView\"16@\"AKController\"24"
- "v32@0:8@\"UIView\"16@\"MUContentViewController\"24"
- "v32@0:8@\"VKCImageAnalysisInteraction\"16@\"NSURL\"24"
- "v32@0:8@\"VKCImageAnalysisInteraction\"16@\"UIBarButtonItem\"24"
- "v32@0:8@\"VKCImageAnalysisInteraction\"16@\"UIButton\"24"
- "v32@0:8@\"VNDocumentCameraViewController\"16@\"NSError\"24"
- "v32@0:8@\"VNDocumentCameraViewController\"16@\"VNDocumentCameraScan\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8@16^{__CFDictionary=}24"
- "v32@0:8^{CGPDFDictionary=}16@24"
- "v32@0:8q16@24"
- "v32@0:8{CGPoint=dd}16"
- "v32@0:8{CGSize=dd}16"
- "v36@0:8@\"PDFView\"16B24@\"PDFPage\"28"
- "v36@0:8@16B24@28"
- "v40@0:8@\"<MUBannerConfiguration>\"16@\"UIAction\"24@\"UIAction\"32"
- "v40@0:8@\"AKController\"16@\"AKAnnotation\"24@\"AKPageModelController\"32"
- "v40@0:8@\"AKController\"16@\"AKAnnotation\"24^@32"
- "v40@0:8@\"NSData\"16@\"NSData\"24@\"UIImage\"32"
- "v40@0:8@\"NSURL\"16@\"NSData\"24@\"UIImage\"32"
- "v40@0:8@\"PDFView\"16B24B28@\"PDFPage\"32"
- "v40@0:8@\"UIAutoFillTextSuggestion\"16@\"AKController\"24@?<v@?@\"NSSet\">32"
- "v40@0:8@\"UIGestureRecognizer\"16Q24@\"AKController\"32"
- "v40@0:8@\"UIImage\"16@\"NSData\"24@\"UIImage\"32"
- "v40@0:8@\"UIPresentationController\"16q24@\"<UIViewControllerTransitionCoordinator>\"32"
- "v40@0:8@\"UIScrollView\"16@\"UIView\"24d32"
- "v40@0:8@\"VKCImageAnalysisInteraction\"16:24@?<v@?>32"
- "v40@0:8@16:24@?32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@24^@32"
- "v40@0:8@16@24d32"
- "v40@0:8@16B24B28@32"
- "v40@0:8@16Q24@32"
- "v40@0:8@16^{CGPDFDictionary=}24^{CGPDFPage=}32"
- "v40@0:8@16^{CGPDFPage=}24@32"
- "v40@0:8@16q24@32"
- "v40@0:8^B16^B24@32"
- "v40@0:8^{CGImage=}16^{CGImageSource=}24@?32"
- "v40@0:8^{CGPDFDictionary=}16@24Q32"
- "v40@0:8^{CGPDFDictionary=}16^{CGPDFPage=}24@32"
- "v40@0:8{CGSize=dd}16@32"
- "v44@0:8@\"PDFView\"16B24Q28@\"PDFPage\"36"
- "v44@0:8@\"UIGestureRecognizer\"16Q24B32@\"AKController\"36"
- "v44@0:8@16@24@32B40"
- "v44@0:8@16B24Q28@36"
- "v44@0:8@16Q24B32@36"
- "v48@0:8@\"NSData\"16@\"NSData\"24@\"UIImage\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSURL\"16@\"NSData\"24@\"UIImage\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"UIScrollView\"16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24@32^v40"
- "v48@0:8@16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v48@0:8^{CGImageDestination=}16^{CGImage=}24^{CGImageMetadata=}32@40"
- "v48@0:8{CGSize=dd}16{CGSize=dd}32"
- "v48@0:8{UIEdgeInsets=dddd}16"
- "v56@0:8@\"AKController\"16Q24q32q40Q48"
- "v56@0:8@\"VKCImageAnalysisInteraction\"16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "v56@0:8@16Q24q32q40Q48"
- "v56@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "v56@0:8^{CGImageDestination=}16^{CGImage=}24^{CGImage=}32^{CGImageMetadata=}40@48"
- "validateDelete:"
- "validateDuplicate:"
- "validateEditTextAnnotation:"
- "validateRedo:"
- "validateSender:"
- "validateShowAttributeInspector:"
- "validateUndo:"
- "valueForKey:"
- "valueWithCGRect:"
- "valueWithQuadrilateral:"
- "videoPreviewAvailableForImageAnalysisInteraction:"
- "view"
- "viewDidAppear:"
- "viewDidLayoutSubviews"
- "viewDidLoad"
- "viewForZoomingInScrollView:"
- "viewIsTransitioningBetweenSizes"
- "viewSafeAreaInsetsDidChange"
- "viewTransitionPageToCenter"
- "viewTransitionPointOnPageToCenter"
- "viewTransitionPreviousAutoscalingState"
- "viewTransitionPreviousScale"
- "viewWillAppear:"
- "viewWillDisappear:"
- "viewWillLayoutSubviews"
- "viewWillTransitionToSize:withTransitionCoordinator:"
- "visibleContentRect"
- "visibleContentRectInCoordinateSpace:"
- "visibleHeightOfAttributeBar"
- "visiblePages"
- "visibleRectOfOverlayAtPageIndex:forAnnotationController:"
- "visualSearchCornerView"
- "visualSearchExistsAtPoint:"
- "visualSearchResultItems"
- "visualSearchViewContainer"
- "whiteColor"
- "whiteView"
- "widthAnchor"
- "willBeginLoadingNewDocument"
- "willChangeValueForKey:"
- "willMoveToParentViewController:"
- "willTransitionToTraitCollection:withTransitionCoordinator:"
- "window"
- "writeFeedbackAttachementForImageAnalysisInteraction:to:"
- "writeToConsumer:withOptions:"
- "writeToFile:atomically:"
- "writeToURL:embeddingSourceImageAndEditModel:error:"
- "writeToURL:embeddingSourceImageAndEditModel:options:error:"
- "writeToURL:error:"
- "writeToURL:options:error:"
- "writeToURL:withOptions:"
- "writeUsingBaseImage:withAnnotationsFromController:asImageOfType:toConsumer:embedSourceImageAndAnnotationsAsMetadata:encryptPrivateMetadata:error:"
- "zone"
- "zoomScale"
- "zoomToFitRestoreValue"
- "zoomToRect:animated:"
- "{CGAffineTransform=dddddd}24@0:8@16"
- "{CGAffineTransform=dddddd}40@0:8^{CGPDFPage=}16^{CGRect={CGPoint=dd}{CGSize=dd}}24^{CGRect={CGPoint=dd}{CGSize=dd}}32"
- "{CGPoint=\"x\"d\"y\"d}"
- "{CGPoint=dd}16@0:8"
- "{CGPoint=dd}48@0:8{CGPoint=dd}16Q32@\"AKController\"40"
- "{CGPoint=dd}48@0:8{CGPoint=dd}16Q32@40"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8@\"<UICoordinateSpace>\"16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8@\"VKCImageAnalysisInteraction\"16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8@16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}32@0:8@16Q24"
- "{CGRect={CGPoint=dd}{CGSize=dd}}32@0:8Q16@\"AKController\"24"
- "{CGRect={CGPoint=dd}{CGSize=dd}}32@0:8Q16@24"
- "{CGRect={CGPoint=dd}{CGSize=dd}}40@0:8d16{CGPoint=dd}24"
- "{CGSize=\"width\"d\"height\"d}"
- "{CGSize=dd}16@0:8"
- "{CGSize=dd}24@0:8@\"NSData\"16"
- "{CGSize=dd}24@0:8@\"NSURL\"16"
- "{CGSize=dd}24@0:8@16"
- "{CGSize=dd}24@0:8@?16"
- "{CGSize=dd}24@0:8^{CGImageSource=}16"
- "{CGSize=dd}40@0:8d16{CGSize=dd}24"
- "{CGSize=dd}48@0:8{CGSize=dd}16{CGSize=dd}32"
- "{UIEdgeInsets=\"top\"d\"left\"d\"bottom\"d\"right\"d}"
- "{UIEdgeInsets=dddd}16@0:8"

```
