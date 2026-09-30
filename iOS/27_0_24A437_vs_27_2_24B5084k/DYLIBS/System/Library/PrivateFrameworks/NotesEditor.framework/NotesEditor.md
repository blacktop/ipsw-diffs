## NotesEditor

> `/System/Library/PrivateFrameworks/NotesEditor.framework/NotesEditor`

### Sections with Same Size but Changed Content

- `__TEXT.__ustring`

```diff

-3001.2.2.0.0
-  __TEXT.__text: 0x2f7844
+3001.40.8.100.1
+  __TEXT.__text: 0x2fbf48
   __TEXT.__delay_helper: 0x41c
-  __TEXT.__objc_methlist: 0x16d04
-  __TEXT.__const: 0xbdb4
-  __TEXT.__gcc_except_tab: 0x3dbc
-  __TEXT.__cstring: 0xb8db
-  __TEXT.__oslogstring: 0x6f3c
+  __TEXT.__objc_methlist: 0x17d2c
+  __TEXT.__const: 0xbea4
+  __TEXT.__gcc_except_tab: 0x3bcc
+  __TEXT.__cstring: 0xb93b
+  __TEXT.__oslogstring: 0x701c
   __TEXT.__ustring: 0x312
-  __TEXT.__constg_swiftt: 0x5c40
-  __TEXT.__swift5_typeref: 0x3632a
+  __TEXT.__constg_swiftt: 0x5c8c
+  __TEXT.__swift5_typeref: 0x36344
   __TEXT.__swift5_builtin: 0x26c
-  __TEXT.__swift5_reflstr: 0x5075
-  __TEXT.__swift5_fieldmd: 0x39b8
+  __TEXT.__swift5_reflstr: 0x50d5
+  __TEXT.__swift5_fieldmd: 0x39ec
   __TEXT.__swift5_assocty: 0x6f0
   __TEXT.__swift5_proto: 0x38c
-  __TEXT.__swift5_types: 0x310
-  __TEXT.__swift5_capture: 0x34f4
+  __TEXT.__swift5_types: 0x314
+  __TEXT.__swift5_capture: 0x35c4
   __TEXT.__swift5_protos: 0x48
-  __TEXT.__swift_as_entry: 0x184
-  __TEXT.__swift_as_cont: 0x38c
-  __TEXT.__swift_as_ret: 0x18c
+  __TEXT.__swift_as_entry: 0x190
+  __TEXT.__swift_as_cont: 0x3a0
+  __TEXT.__swift_as_ret: 0x198
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0xc688
-  __TEXT.__eh_frame: 0x5720
+  __TEXT.__unwind_info: 0xca48
+  __TEXT.__eh_frame: 0x58e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4770
-  __DATA_CONST.__objc_classlist: 0x748
+  __DATA_CONST.__const: 0x46d0
+  __DATA_CONST.__objc_classlist: 0x798
   __DATA_CONST.__objc_catlist: 0x188
-  __DATA_CONST.__objc_protolist: 0x588
+  __DATA_CONST.__objc_protolist: 0x590
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfb08
+  __DATA_CONST.__objc_selrefs: 0xfbb8
   __DATA_CONST.__objc_protorefs: 0x198
-  __DATA_CONST.__objc_superrefs: 0x408
+  __DATA_CONST.__objc_superrefs: 0x450
   __DATA_CONST.__objc_arraydata: 0x28
-  __DATA_CONST.__got: 0x3170
-  __AUTH_CONST.__const: 0xb918
-  __AUTH_CONST.__cfstring: 0x62a0
-  __AUTH_CONST.__objc_const: 0x208a8
-  __AUTH_CONST.__objc_intobj: 0x438
+  __DATA_CONST.__got: 0x31c0
+  __AUTH_CONST.__const: 0xbb58
+  __AUTH_CONST.__cfstring: 0x6260
+  __AUTH_CONST.__objc_const: 0x21ab0
+  __AUTH_CONST.__objc_intobj: 0x600
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH_CONST.__auth_got: 0x3a10
-  __AUTH.__objc_data: 0x5560
-  __AUTH.__data: 0x2ce0
-  __DATA.__objc_ivar: 0x1128
-  __DATA.__data: 0x881c
+  __AUTH_CONST.__auth_got: 0x39e8
+  __AUTH.__objc_data: 0x5880
+  __AUTH.__data: 0x2d10
+  __DATA.__objc_ivar: 0x1170
+  __DATA.__data: 0x888c
   __DATA.__objc_stublist: 0x10
   __DATA.__common: 0x1a0
   __DATA_DIRTY.__objc_data: 0x41e0
-  __DATA_DIRTY.__data: 0x1248
+  __DATA_DIRTY.__data: 0x1270
   __DATA_DIRTY.__bss: 0x1f10
   __DATA_DIRTY.__common: 0x1b8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 15752
-  Symbols:   20822
-  CStrings:  1907
+  Functions: 15956
+  Symbols:   21127
+  CStrings:  1900
 
Symbols:
+ +[ICNoteEditorFormattingController initialize]
+ +[ICNoteEditorPresentationCoordinator dismissChildPresentedViewControllersInPostOrder:animated:completion:]
+ -[ICBaseTextView(StyleRendering) drawBlockQuoteAndCleanup:pendingBlockQuoteLevelToDraw:pendingBlockQuoteRectToDraw:ioBlockQuoteIsRTL:ps:]
+ -[ICBaseTextView(StyleRendering) drawBlockQuoteLayerInRectForTK2:blockQuoteLevel:isMonostyled:isRTL:]
+ -[ICBaseTextView(StyleRendering) updateBlockQuoteLayerForParagraphStyle:inRange:ioPreviousBlockQuoteRect:ioBlockQuoteIsRTL:]
+ -[ICEditingTextView tintColorDidChange]
+ -[ICNoteEditorAnalytics .cxx_destruct]
+ -[ICNoteEditorAnalytics audioEventReporterLostSession:]
+ -[ICNoteEditorAnalytics audioEventReporter]
+ -[ICNoteEditorAnalytics environment]
+ -[ICNoteEditorAnalytics eventReporterLostSession:]
+ -[ICNoteEditorAnalytics eventReporter]
+ -[ICNoteEditorAnalytics findResultReporter]
+ -[ICNoteEditorAnalytics initWithEnvironment:subTrackerName:]
+ -[ICNoteEditorAnalytics setEnvironment:]
+ -[ICNoteEditorAnalytics setSubTrackerName:]
+ -[ICNoteEditorAnalytics subTrackerName]
+ -[ICNoteEditorAttachmentCoordinator .cxx_destruct]
+ -[ICNoteEditorAttachmentCoordinator addTable:]
+ -[ICNoteEditorAttachmentCoordinator attachFile:]
+ -[ICNoteEditorAttachmentCoordinator attachmentInsertionController:didAddAttachment:atRange:]
+ -[ICNoteEditorAttachmentCoordinator attachmentInsertionController:didAddInlineAttachment:atRange:textStorage:]
+ -[ICNoteEditorAttachmentCoordinator attachmentInsertionController:willAddAttachment:atRange:]
+ -[ICNoteEditorAttachmentCoordinator attachmentView:shouldPresentAttachment:]
+ -[ICNoteEditorAttachmentCoordinator attachmentView:shouldPresentNote:]
+ -[ICNoteEditorAttachmentCoordinator attachmentView:shouldRespondToPanGestureTouch:forAttachment:]
+ -[ICNoteEditorAttachmentCoordinator attachmentView:shouldShareAttachment:]
+ -[ICNoteEditorAttachmentCoordinator canPerformCreateImageWithSelection]
+ -[ICNoteEditorAttachmentCoordinator cleanupAfterAddImageAttachmentOperation]
+ -[ICNoteEditorAttachmentCoordinator createImage:]
+ -[ICNoteEditorAttachmentCoordinator documentPicker:didPickDocumentsAtURLs:]
+ -[ICNoteEditorAttachmentCoordinator environment]
+ -[ICNoteEditorAttachmentCoordinator getTableControllerFor:]
+ -[ICNoteEditorAttachmentCoordinator initWithEnvironment:]
+ -[ICNoteEditorAttachmentCoordinator insertDividerLine:]
+ -[ICNoteEditorAttachmentCoordinator insertSidecarItems:service:]
+ -[ICNoteEditorAttachmentCoordinator isDocumentCameraAvailable]
+ -[ICNoteEditorAttachmentCoordinator isPhotosLibraryAvailable]
+ -[ICNoteEditorAttachmentCoordinator notesQuickLookActivityItem:rectForPreviewItem:inView:previewController:]
+ -[ICNoteEditorAttachmentCoordinator notesQuickLookActivityItem:transitionViewForPreviewItem:previewController:]
+ -[ICNoteEditorAttachmentCoordinator paperTextAttachmentManager:beginTrackingUndoManager:]
+ -[ICNoteEditorAttachmentCoordinator paperTextAttachmentManager:endTrackingUndoManager:]
+ -[ICNoteEditorAttachmentCoordinator prepareSelectionForAddingAttachment]
+ -[ICNoteEditorAttachmentCoordinator presentAttachment:]
+ -[ICNoteEditorAttachmentCoordinator setEnvironment:]
+ -[ICNoteEditorAttachmentCoordinator showDocumentPicker]
+ -[ICNoteEditorAttachmentCoordinator showInsertAudio:]
+ -[ICNoteEditorAttachmentCoordinator showInsertUIForSourceType:sender:]
+ -[ICNoteEditorAttachmentCoordinator showInsertUIWithPreferredSourceType:]
+ -[ICNoteEditorAttachmentCoordinator showPhotoLibrary]
+ -[ICNoteEditorAttachmentCoordinator viewForAttachment:]
+ -[ICNoteEditorBarController .cxx_destruct]
+ -[ICNoteEditorBarController environment]
+ -[ICNoteEditorBarController initWithEnvironment:]
+ -[ICNoteEditorBarController navigationItemConfiguration]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:addChecklistFromBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:addNoteFromBarButtonItem:event:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:addTableFromBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:changeStyleFromBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:closeAuxiliaryWindowFromBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:deleteFromBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:didCompleteAnimationFromInlineSketchBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:doneEditingFromBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:inlineSketchFromBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:insertMediaWithSourceType:mediaBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:insertSidecarItemWithMenuItems:service:mediaBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:leftIndentWithSender:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:moveDownWithSender:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:moveFromBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:moveUpWithSender:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:openLinkEditorWithSender:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:quickNoteDidCancelFromBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:quickNoteDidSaveFromBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:quickNoteShowAllNotesFromBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:redoFromBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:rightIndentWithSender:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:setEmphasis:fromBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:setListStyle:withSender:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:setToolbarHidden:animated:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:shareFromBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:showPhotoLibraryFromBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:showWritingToolsFromBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:startEditingFromBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:toggleBIUS:fromBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:toggleBlockQuoteWithSender:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:toggleLockFromBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:toggleSidebarFromBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfiguration:undoFromBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfigurationChecklistAccessibilityValue:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfigurationCollaborationBarButtonItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfigurationContextualInputAccessoryView:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfigurationEmphasisAccessibilityCustomContentValue:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfigurationIndentationAccessibilityValue:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfigurationInputAccessoryToolbar:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfigurationInputAssistantItem:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfigurationIsStyleSheetShowing:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfigurationIsToolbarHidden:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfigurationPresentingSourceView:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfigurationPresentingViewController:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfigurationPresentingWindowScene:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfigurationStyleSelectorViewController:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfigurationTableAttachmentViewController:]
+ -[ICNoteEditorBarController noteEditorNavigationItemConfigurationToolbarItemSource:]
+ -[ICNoteEditorBarController setEnvironment:]
+ -[ICNoteEditorBarController setNavigationItemConfiguration:]
+ -[ICNoteEditorDocumentScanController .cxx_destruct]
+ -[ICNoteEditorDocumentScanController createdGalleryAttachmentUUID]
+ -[ICNoteEditorDocumentScanController documentCameraController:canAddImages:]
+ -[ICNoteEditorDocumentScanController documentCameraController:didFinishWithDocInfoCollection:imageCache:warnUser:]
+ -[ICNoteEditorDocumentScanController documentCameraController:didFinishWithDocInfoCollection:imageCache:warnUser:closeViewController:]
+ -[ICNoteEditorDocumentScanController documentCameraControllerCreateDataCryptorIfNecessary]
+ -[ICNoteEditorDocumentScanController documentCameraControllerDidCancel:]
+ -[ICNoteEditorDocumentScanController documentCameraControllerDidCancelWithPresentingViewController:]
+ -[ICNoteEditorDocumentScanController documentCameraControllerDidRetake:pageCount:]
+ -[ICNoteEditorDocumentScanController documentCameraPresentingViewController:didFinishWithInfoCollection:imageCache:warnUser:closeViewController:]
+ -[ICNoteEditorDocumentScanController environment]
+ -[ICNoteEditorDocumentScanController initWithEnvironment:]
+ -[ICNoteEditorDocumentScanController remoteDocumentCameraController:didFailWithError:]
+ -[ICNoteEditorDocumentScanController remoteDocumentCameraController:didFinishWithInfoCollection:]
+ -[ICNoteEditorDocumentScanController remoteDocumentCameraControllerDidCancel:]
+ -[ICNoteEditorDocumentScanController scanDataDelegateWithIdentifier:]
+ -[ICNoteEditorDocumentScanController setCreatedGalleryAttachmentUUID:]
+ -[ICNoteEditorDocumentScanController setEnvironment:]
+ -[ICNoteEditorDocumentScanController showDocumentCamera]
+ -[ICNoteEditorDrawingController .cxx_destruct]
+ -[ICNoteEditorDrawingController _scribbleInteraction:shouldBeginAtLocation:]
+ -[ICNoteEditorDrawingController _scribbleInteraction:willBeginWritingInElement:]
+ -[ICNoteEditorDrawingController cleanupAfterFingerDrawing]
+ -[ICNoteEditorDrawingController clearTextViewSelection]
+ -[ICNoteEditorDrawingController createInkPickerControllerIfNecessary]
+ -[ICNoteEditorDrawingController currentStrokeStartTouch]
+ -[ICNoteEditorDrawingController currentValidToolForNewDrawingOrNote]
+ -[ICNoteEditorDrawingController dateOfLastStrokeOrNewDrawing]
+ -[ICNoteEditorDrawingController dealloc]
+ -[ICNoteEditorDrawingController defaultInkColor]
+ -[ICNoteEditorDrawingController didDrawWithPencilWithoutPalette]
+ -[ICNoteEditorDrawingController drawingsForHandwritingDebug]
+ -[ICNoteEditorDrawingController ensureValidInkForNewDrawingOrNote]
+ -[ICNoteEditorDrawingController environment]
+ -[ICNoteEditorDrawingController handwritingDebugPresenter]
+ -[ICNoteEditorDrawingController handwritingDebugShouldClose]
+ -[ICNoteEditorDrawingController hideInkPicker]
+ -[ICNoteEditorDrawingController icasPalettePositionFromPKPalettePosition:]
+ -[ICNoteEditorDrawingController initWithEnvironment:]
+ -[ICNoteEditorDrawingController inkPalette:didChangeColor:]
+ -[ICNoteEditorDrawingController inkPalette:didChangePalettePositionStart:end:]
+ -[ICNoteEditorDrawingController inkPalette:didHideAnimated:]
+ -[ICNoteEditorDrawingController inkPalette:didPickTool:]
+ -[ICNoteEditorDrawingController inkPalette:didShowAnimated:]
+ -[ICNoteEditorDrawingController inkPalette:shouldResignFirstResponder:]
+ -[ICNoteEditorDrawingController inkPalette:willHideAnimated:]
+ -[ICNoteEditorDrawingController inkPalette:willShowAnimated:]
+ -[ICNoteEditorDrawingController inkPaletteButtonView:]
+ -[ICNoteEditorDrawingController inkPaletteController]
+ -[ICNoteEditorDrawingController inkPaletteDidToggleRuler:isRulerActive:]
+ -[ICNoteEditorDrawingController inkPaletteUndoManager:]
+ -[ICNoteEditorDrawingController inkPickerState]
+ -[ICNoteEditorDrawingController inlineDrawingAttachmentForPoint:]
+ -[ICNoteEditorDrawingController isDrawingStrokeWithPencil]
+ -[ICNoteEditorDrawingController isDrawingStroke]
+ -[ICNoteEditorDrawingController isInkPickerShowing]
+ -[ICNoteEditorDrawingController isNewInk:]
+ -[ICNoteEditorDrawingController isPencilModeTransitory]
+ -[ICNoteEditorDrawingController lastSavedInkingTool]
+ -[ICNoteEditorDrawingController noteHasAnyPencilKitDrawings]
+ -[ICNoteEditorDrawingController paletteResponder]
+ -[ICNoteEditorDrawingController radarTitleForHandwritingDebug]
+ -[ICNoteEditorDrawingController recentlyCreatedDrawingInNewNoteAsPartOfPencilDown]
+ -[ICNoteEditorDrawingController responderToMatch]
+ -[ICNoteEditorDrawingController rulerHostWantsSharedRuler]
+ -[ICNoteEditorDrawingController rulerHostingView]
+ -[ICNoteEditorDrawingController saveToolAsCurrentTool:]
+ -[ICNoteEditorDrawingController setCurrentStrokeStartTouch:]
+ -[ICNoteEditorDrawingController setDateOfLastStrokeOrNewDrawing:]
+ -[ICNoteEditorDrawingController setDidDrawWithPencilWithoutPalette:]
+ -[ICNoteEditorDrawingController setEnvironment:]
+ -[ICNoteEditorDrawingController setHandwritingDebugPresenter:]
+ -[ICNoteEditorDrawingController setInkPaletteController:]
+ -[ICNoteEditorDrawingController setInkPickerState:]
+ -[ICNoteEditorDrawingController setIsDrawingStroke:]
+ -[ICNoteEditorDrawingController setIsDrawingStrokeWithPencil:]
+ -[ICNoteEditorDrawingController setIsPencilModeTransitory:]
+ -[ICNoteEditorDrawingController setPaletteResponder:]
+ -[ICNoteEditorDrawingController setRecentlyCreatedDrawingInNewNoteAsPartOfPencilDown:]
+ -[ICNoteEditorDrawingController setRulerHostingView:]
+ -[ICNoteEditorDrawingController setShowInkPickerAfterViewAppears:]
+ -[ICNoteEditorDrawingController setWasEditingBeforeDrawing:]
+ -[ICNoteEditorDrawingController setupForFingerDrawing]
+ -[ICNoteEditorDrawingController shouldEnablePencilGestures]
+ -[ICNoteEditorDrawingController showDrawingUpdateAlert]
+ -[ICNoteEditorDrawingController showHandwritingDebug:]
+ -[ICNoteEditorDrawingController showInkPicker:]
+ -[ICNoteEditorDrawingController showInkPicker:animated:]
+ -[ICNoteEditorDrawingController showInkPickerAfterViewAppears]
+ -[ICNoteEditorDrawingController showInkPickerAndEndEditingIfNecessary]
+ -[ICNoteEditorDrawingController textView:canAddDrawingAtIndex:]
+ -[ICNoteEditorDrawingController textView:didRemoveDrawingAtIndex:]
+ -[ICNoteEditorDrawingController textView:isEndOfDocument:]
+ -[ICNoteEditorDrawingController textView:newAttachmentForFileType:]
+ -[ICNoteEditorDrawingController textView:upgradeDrawingAtIndex:itemProviders:insertionLocationInDrawing:]
+ -[ICNoteEditorDrawingController textView:willAddDrawingAtIndex:]
+ -[ICNoteEditorDrawingController textViewCanAddStroke:]
+ -[ICNoteEditorDrawingController textViewCanSelectDrawing:]
+ -[ICNoteEditorDrawingController textViewDidEndStroke:]
+ -[ICNoteEditorDrawingController textViewWillBeginStroke:forTouch:]
+ -[ICNoteEditorDrawingController toggleInkPickerAnimated:]
+ -[ICNoteEditorDrawingController undoablySwitchToPPK:]
+ -[ICNoteEditorDrawingController updateDrawingAttachmentsIfNeeded]
+ -[ICNoteEditorDrawingController updateDrawingAttachmentsInNote]
+ -[ICNoteEditorDrawingController updateInkPickerAndTextViewToTool:]
+ -[ICNoteEditorDrawingController updateInlineDrawingsPaletteVisibility]
+ -[ICNoteEditorDrawingController updatePencilKitPaperStyleType]
+ -[ICNoteEditorDrawingController updateUIEnabledStatePencilActive:]
+ -[ICNoteEditorDrawingController upgradeAllAttachmentsInNoteWithUpgradeHelper:]
+ -[ICNoteEditorDrawingController upgradeAllAttachmentsInNoteWithUpgradeHelper:forSydney:]
+ -[ICNoteEditorDrawingController upgradePencilKitDrawingsForNewInksPromptingIfNecessary]
+ -[ICNoteEditorDrawingController wasEditingBeforeDrawing]
+ -[ICNoteEditorFormattingController .cxx_destruct]
+ -[ICNoteEditorFormattingController addTodoListAtEndOfNote]
+ -[ICNoteEditorFormattingController canIndentByAmount:]
+ -[ICNoteEditorFormattingController canIndentLeft]
+ -[ICNoteEditorFormattingController canIndentRight]
+ -[ICNoteEditorFormattingController canMoveCheckedToBottom]
+ -[ICNoteEditorFormattingController canMoveSelectedListItemDown]
+ -[ICNoteEditorFormattingController canMoveSelectedListItemUp]
+ -[ICNoteEditorFormattingController canPerformTodoCheckAll]
+ -[ICNoteEditorFormattingController canPerformTodoUncheckAll]
+ -[ICNoteEditorFormattingController canPerformToggleToDoDone]
+ -[ICNoteEditorFormattingController canRemoveCheckedListItem]
+ -[ICNoteEditorFormattingController canSetListStyle]
+ -[ICNoteEditorFormattingController canSetParagraphStyle]
+ -[ICNoteEditorFormattingController canToggleTodoStyle]
+ -[ICNoteEditorFormattingController changeIndentationByIncreasing:sender:]
+ -[ICNoteEditorFormattingController changeStyle:]
+ -[ICNoteEditorFormattingController checkAll:]
+ -[ICNoteEditorFormattingController containsUnCheckedItems]
+ -[ICNoteEditorFormattingController createTodoListItem:]
+ -[ICNoteEditorFormattingController currentBIUSForStyleSelector]
+ -[ICNoteEditorFormattingController currentEmphasisType]
+ -[ICNoteEditorFormattingController currentStylesForStyleSelectorIgnoreTypingAttributes:]
+ -[ICNoteEditorFormattingController decreaseIndentation:]
+ -[ICNoteEditorFormattingController disableBoldface]
+ -[ICNoteEditorFormattingController disableItalics]
+ -[ICNoteEditorFormattingController disableStrikethrough]
+ -[ICNoteEditorFormattingController disableUnderline]
+ -[ICNoteEditorFormattingController enableBoldface]
+ -[ICNoteEditorFormattingController enableItalics]
+ -[ICNoteEditorFormattingController enableStrikethrough]
+ -[ICNoteEditorFormattingController enableUnderline]
+ -[ICNoteEditorFormattingController environment]
+ -[ICNoteEditorFormattingController ic_alignCenter:]
+ -[ICNoteEditorFormattingController ic_alignLeft:]
+ -[ICNoteEditorFormattingController ic_alignRight:]
+ -[ICNoteEditorFormattingController increaseIndentation:]
+ -[ICNoteEditorFormattingController indentAmountIncreasing:]
+ -[ICNoteEditorFormattingController indentLeft:]
+ -[ICNoteEditorFormattingController indentRight:]
+ -[ICNoteEditorFormattingController indentSelectionIfPossibleByAmount:]
+ -[ICNoteEditorFormattingController initWithEnvironment:]
+ -[ICNoteEditorFormattingController isBlockQuoteSet]
+ -[ICNoteEditorFormattingController isChecklistSelected]
+ -[ICNoteEditorFormattingController isLoadingStyleSelectorInputView]
+ -[ICNoteEditorFormattingController isOnlyBlockQuoteEnabled]
+ -[ICNoteEditorFormattingController isStyleSelectorInputViewShowing]
+ -[ICNoteEditorFormattingController moveCheckedToBottom:]
+ -[ICNoteEditorFormattingController moveSelectedListItemDown:]
+ -[ICNoteEditorFormattingController moveSelectedListItemUp:]
+ -[ICNoteEditorFormattingController noteFormattingControllerCreateIfNecessary]
+ -[ICNoteEditorFormattingController noteFormattingController]
+ -[ICNoteEditorFormattingController noteFormattingDidFinish:]
+ -[ICNoteEditorFormattingController noteFormattingNeedsUpdate:]
+ -[ICNoteEditorFormattingController noteFormattingTintColor]
+ -[ICNoteEditorFormattingController presentingViewControllerForStyleSelector:]
+ -[ICNoteEditorFormattingController removeChecked:]
+ -[ICNoteEditorFormattingController resetCurrentListTextStyleIfNecessaryWithSender:]
+ -[ICNoteEditorFormattingController setBodyStyle:]
+ -[ICNoteEditorFormattingController setBulletedListStyle:]
+ -[ICNoteEditorFormattingController setCurrentTextStyle:]
+ -[ICNoteEditorFormattingController setDashedListStyle:]
+ -[ICNoteEditorFormattingController setEmphasisType:sender:]
+ -[ICNoteEditorFormattingController setEnvironment:]
+ -[ICNoteEditorFormattingController setFixedWidthStyle:]
+ -[ICNoteEditorFormattingController setHeadingStyle:]
+ -[ICNoteEditorFormattingController setIsLoadingStyleSelectorInputView:]
+ -[ICNoteEditorFormattingController setNoteFormattingController:]
+ -[ICNoteEditorFormattingController setNumberedListStyle:]
+ -[ICNoteEditorFormattingController setSubheadingStyle:]
+ -[ICNoteEditorFormattingController setTextStyle:sender:]
+ -[ICNoteEditorFormattingController setTitleStyle:]
+ -[ICNoteEditorFormattingController showStyleSelector:animated:]
+ -[ICNoteEditorFormattingController showStyleSelector:animated:sender:]
+ -[ICNoteEditorFormattingController showStyleSelectorInputView:animated:doneEditing:]
+ -[ICNoteEditorFormattingController showStyleSelectorPopover:animated:sender:]
+ -[ICNoteEditorFormattingController styleSelector:didChangeIndentAmount:]
+ -[ICNoteEditorFormattingController styleSelector:didSelectStyle:]
+ -[ICNoteEditorFormattingController styleSelector:presentViewController:animated:completion:]
+ -[ICNoteEditorFormattingController styleSelector:toggleBIUS:]
+ -[ICNoteEditorFormattingController styleSelectorCanIndentLeft:]
+ -[ICNoteEditorFormattingController styleSelectorCanIndentRight:]
+ -[ICNoteEditorFormattingController styleSelectorDidCancel:]
+ -[ICNoteEditorFormattingController styleSelectorDidIndentLeft:]
+ -[ICNoteEditorFormattingController styleSelectorDidIndentRight:]
+ -[ICNoteEditorFormattingController styleSelectorDummyInputView]
+ -[ICNoteEditorFormattingController styleSelectorSelectionHasBlockQuote:]
+ -[ICNoteEditorFormattingController styleSelectorShouldDisableTextStyles:]
+ -[ICNoteEditorFormattingController styleSelectorShouldUseCompactTopInset:]
+ -[ICNoteEditorFormattingController styleSelectorToggleBlockQuote:]
+ -[ICNoteEditorFormattingController styleSelectorWillShowInlineMenu:]
+ -[ICNoteEditorFormattingController toggleBIUS:sender:]
+ -[ICNoteEditorFormattingController toggleBlockQuote:]
+ -[ICNoteEditorFormattingController toggleBoldface]
+ -[ICNoteEditorFormattingController toggleCurrentTextStyle:]
+ -[ICNoteEditorFormattingController toggleEmphasisWithType:]
+ -[ICNoteEditorFormattingController toggleEmphasis]
+ -[ICNoteEditorFormattingController toggleItalics]
+ -[ICNoteEditorFormattingController toggleStrikethrough]
+ -[ICNoteEditorFormattingController toggleToDoDone:]
+ -[ICNoteEditorFormattingController toggleTodoStyle:]
+ -[ICNoteEditorFormattingController toggleUnderline]
+ -[ICNoteEditorFormattingController uncheckAll:]
+ -[ICNoteEditorFormattingController updateStyleSelectorStateIfNeededIgnoreTypingAttributes:]
+ -[ICNoteEditorFormattingController useInputViewForStyleSelector]
+ -[ICNoteEditorInlineAttachmentController .cxx_destruct]
+ -[ICNoteEditorInlineAttachmentController canConvertToTag]
+ -[ICNoteEditorInlineAttachmentController configureChangeControllerForNote:]
+ -[ICNoteEditorInlineAttachmentController convertToTag:]
+ -[ICNoteEditorInlineAttachmentController environment]
+ -[ICNoteEditorInlineAttachmentController hashtagInsertedInNote:tokenContentIdentifier:viaAutoComplete:]
+ -[ICNoteEditorInlineAttachmentController hashtagViewController:insertFutureHashtagWithText:]
+ -[ICNoteEditorInlineAttachmentController hashtagViewController:insertHashtagWithText:]
+ -[ICNoteEditorInlineAttachmentController hashtagViewController:insertUnknownInlineAttachmentWithText:]
+ -[ICNoteEditorInlineAttachmentController initWithEnvironment:]
+ -[ICNoteEditorInlineAttachmentController inlineAttachmentChangeController]
+ -[ICNoteEditorInlineAttachmentController inlineAttachmentDeleted:]
+ -[ICNoteEditorInlineAttachmentController managedObjectContextChangeController:managedObjectIDsToUpdateForUpdatedManagedObjects:]
+ -[ICNoteEditorInlineAttachmentController managedObjectContextChangeController:performUpdatesForManagedObjectIDs:]
+ -[ICNoteEditorInlineAttachmentController managedObjectContextChangeControllerShouldUpdateImmediately:]
+ -[ICNoteEditorInlineAttachmentController mentionInsertedInNote:mentionID:participantID:viaAutoComplete:]
+ -[ICNoteEditorInlineAttachmentController refreshInlineAttachmentTextStyling]
+ -[ICNoteEditorInlineAttachmentController setEnvironment:]
+ -[ICNoteEditorInlineAttachmentController setInlineAttachmentChangeController:]
+ -[ICNoteEditorLockController .cxx_destruct]
+ -[ICNoteEditorLockController environment]
+ -[ICNoteEditorLockController initWithEnvironment:]
+ -[ICNoteEditorLockController setEnvironment:]
+ -[ICNoteEditorLockController showOrHideLockIconCoverViewControllerIfNeededIsBackgrounding:]
+ -[ICNoteEditorLockController showOrHidePasswordEntryViewControllerIfNeeded]
+ -[ICNoteEditorPresentationCoordinator .cxx_destruct]
+ -[ICNoteEditorPresentationCoordinator cleanupAfterBarSourcedPopoverPresentation]
+ -[ICNoteEditorPresentationCoordinator environment]
+ -[ICNoteEditorPresentationCoordinator hideAndDismissPresentedViewController]
+ -[ICNoteEditorPresentationCoordinator initWithEnvironment:]
+ -[ICNoteEditorPresentationCoordinator prepareForBarSourcedPopoverPresentation]
+ -[ICNoteEditorPresentationCoordinator prepareForPresentationOfViewControllerAnimated:]
+ -[ICNoteEditorPresentationCoordinator selectedTextRangeToRestoreAfterBarSourcedPopoverPresentation]
+ -[ICNoteEditorPresentationCoordinator setEnvironment:]
+ -[ICNoteEditorPresentationCoordinator setSelectedTextRangeToRestoreAfterBarSourcedPopoverPresentation:]
+ -[ICNoteEditorPresentationCoordinator setUserInteractionEnabled:]
+ -[ICNoteEditorState debugDescription]
+ -[ICNoteEditorState isAddingImageAttachment]
+ -[ICNoteEditorState isConvertToTag]
+ -[ICNoteEditorState isEditingNewNote]
+ -[ICNoteEditorState isInLiveWindowResize]
+ -[ICNoteEditorState isPerformingDeleteAnimation]
+ -[ICNoteEditorState isPreviewingAttachmentFromNote]
+ -[ICNoteEditorState isSelecting]
+ -[ICNoteEditorState isSettingEditing]
+ -[ICNoteEditorState isSettingSelection]
+ -[ICNoteEditorState isShowingChecklistItems]
+ -[ICNoteEditorState isShowingIndentationItems]
+ -[ICNoteEditorState isTogglingLock]
+ -[ICNoteEditorState setIsAddingImageAttachment:]
+ -[ICNoteEditorState setIsConvertToTag:]
+ -[ICNoteEditorState setIsEditingNewNote:]
+ -[ICNoteEditorState setIsInLiveWindowResize:]
+ -[ICNoteEditorState setIsPerformingDeleteAnimation:]
+ -[ICNoteEditorState setIsPreviewingAttachmentFromNote:]
+ -[ICNoteEditorState setIsSelecting:]
+ -[ICNoteEditorState setIsSettingEditing:]
+ -[ICNoteEditorState setIsSettingSelection:]
+ -[ICNoteEditorState setShowingChecklistItems:]
+ -[ICNoteEditorState setShowingIndentationItems:]
+ -[ICNoteEditorState setSuspendBarButtonUpdates:]
+ -[ICNoteEditorState setSuspendSelectedRangeUpdates:]
+ -[ICNoteEditorState setSuspendTapGestureRecognizer:]
+ -[ICNoteEditorState setTogglingLock:]
+ -[ICNoteEditorState suspendBarButtonUpdates]
+ -[ICNoteEditorState suspendSelectedRangeUpdates]
+ -[ICNoteEditorState suspendTapGestureRecognizer]
+ -[ICNoteEditorViewController analyticsHostWindow]
+ -[ICNoteEditorViewController analytics]
+ -[ICNoteEditorViewController attachmentCoordinator]
+ -[ICNoteEditorViewController barController]
+ -[ICNoteEditorViewController clearDidDrawWithPencilWithoutPalette]
+ -[ICNoteEditorViewController currentFirstResponder]
+ -[ICNoteEditorViewController currentSelectionIsCaretAtLineStart]
+ -[ICNoteEditorViewController dismissCurrentAttachmentPresenterAnimated:]
+ -[ICNoteEditorViewController documentScanController]
+ -[ICNoteEditorViewController drawingController]
+ -[ICNoteEditorViewController editorAddSubviewAboveAllViews:]
+ -[ICNoteEditorViewController editorDelegateRespondsToDidTapAttachment]
+ -[ICNoteEditorViewController editorHasCompactWidth]
+ -[ICNoteEditorViewController editorNavigationController]
+ -[ICNoteEditorViewController editorState]
+ -[ICNoteEditorViewController formattingController]
+ -[ICNoteEditorViewController formattingTextViewInputAccessoryView]
+ -[ICNoteEditorViewController hostViewController]
+ -[ICNoteEditorViewController inlineAttachmentController]
+ -[ICNoteEditorViewController isEndOfDocumentForTextPosition:inTextView:]
+ -[ICNoteEditorViewController isNoteFormattingViewControllerShowing]
+ -[ICNoteEditorViewController isStyleSelectorInputViewShowing]
+ -[ICNoteEditorViewController isWelcomeScreenVisible]
+ -[ICNoteEditorViewController lockController]
+ -[ICNoteEditorViewController notifyEditorDelegateDidTapAttachment:]
+ -[ICNoteEditorViewController presentAttachments:startingAtIndex:editable:]
+ -[ICNoteEditorViewController presentationCoordinator]
+ -[ICNoteEditorViewController setFormattingUpdatesSuspended:]
+ -[ICNoteEditorViewController setStyleSelectorAXFocusElementOnDismissal:]
+ -[ICNoteEditorViewController setToolbarHidden:animated:]
+ -[ICNoteEditorViewController textView:primaryActionForTextItem:defaultAction:]
+ -[ICNoteEditorViewController updateContentViewBezelsForPasswordEntry]
+ -[ICNoteEditorViewController updatePaperKitMessengerForAttachment:layoutManager:]
+ -[ICNoteEditorViewController updatePaperKitMessengerForAttachment:textLayoutManager:]
+ -[ICNoteEditorViewController visualAssetImportControllerIsShowing]
+ -[ICTK2NoteEditorViewController isEndOfDocumentForTextPosition:inTextView:]
+ -[ICTK2TextView _share:]
+ -[ICTK2TextView attributedTextInRange:]
+ -[ICTK2TextView ic_flattenedTextForSharingInRange:]
+ -[ICTK2TextView isReadingTextForSharing]
+ -[ICTK2TextView setIsReadingTextForSharing:]
+ -[ICTK2TextView textInRange:]
+ GCC_except_table107
+ GCC_except_table111
+ GCC_except_table116
+ GCC_except_table119
+ GCC_except_table121
+ GCC_except_table126
+ GCC_except_table141
+ GCC_except_table144
+ GCC_except_table163
+ GCC_except_table165
+ GCC_except_table174
+ GCC_except_table178
+ GCC_except_table227
+ GCC_except_table274
+ GCC_except_table280
+ GCC_except_table306
+ GCC_except_table308
+ GCC_except_table486
+ GCC_except_table52
+ GCC_except_table577
+ GCC_except_table66
+ GCC_except_table73
+ GCC_except_table82
+ GCC_except_table85
+ GCC_except_table88
+ GCC_except_table91
+ GCC_except_table95
+ GCC_except_table99
+ _ICNoteEditorViewControllerSystemPaperLinkBarVisibilityChangedNotification_block_invoke.disableWorkaroundFor150051673
+ _ICNoteEditorViewControllerSystemPaperLinkBarVisibilityChangedNotification_block_invoke.disableWorkaroundFor150051673_token
+ _OBJC_CLASS_$_ICNoteEditorAnalytics
+ _OBJC_CLASS_$_ICNoteEditorAttachmentCoordinator
+ _OBJC_CLASS_$_ICNoteEditorBarController
+ _OBJC_CLASS_$_ICNoteEditorDocumentScanController
+ _OBJC_CLASS_$_ICNoteEditorDrawingController
+ _OBJC_CLASS_$_ICNoteEditorFormattingController
+ _OBJC_CLASS_$_ICNoteEditorInlineAttachmentController
+ _OBJC_CLASS_$_ICNoteEditorLockController
+ _OBJC_CLASS_$_ICNoteEditorPresentationCoordinator
+ _OBJC_CLASS_$_ICNoteEditorState
+ _OBJC_IVAR_$_ICNoteEditorAnalytics._audioEventReporter
+ _OBJC_IVAR_$_ICNoteEditorAnalytics._environment
+ _OBJC_IVAR_$_ICNoteEditorAnalytics._eventReporter
+ _OBJC_IVAR_$_ICNoteEditorAnalytics._findResultReporter
+ _OBJC_IVAR_$_ICNoteEditorAnalytics._subTrackerName
+ _OBJC_IVAR_$_ICNoteEditorAttachmentCoordinator._environment
+ _OBJC_IVAR_$_ICNoteEditorBarController._environment
+ _OBJC_IVAR_$_ICNoteEditorBarController._navigationItemConfiguration
+ _OBJC_IVAR_$_ICNoteEditorDocumentScanController._createdGalleryAttachmentUUID
+ _OBJC_IVAR_$_ICNoteEditorDocumentScanController._environment
+ _OBJC_IVAR_$_ICNoteEditorDrawingController._currentStrokeStartTouch
+ _OBJC_IVAR_$_ICNoteEditorDrawingController._dateOfLastStrokeOrNewDrawing
+ _OBJC_IVAR_$_ICNoteEditorDrawingController._didDrawWithPencilWithoutPalette
+ _OBJC_IVAR_$_ICNoteEditorDrawingController._environment
+ _OBJC_IVAR_$_ICNoteEditorDrawingController._handwritingDebugPresenter
+ _OBJC_IVAR_$_ICNoteEditorDrawingController._inkPaletteController
+ _OBJC_IVAR_$_ICNoteEditorDrawingController._inkPickerState
+ _OBJC_IVAR_$_ICNoteEditorDrawingController._isDrawingStroke
+ _OBJC_IVAR_$_ICNoteEditorDrawingController._isDrawingStrokeWithPencil
+ _OBJC_IVAR_$_ICNoteEditorDrawingController._isPencilModeTransitory
+ _OBJC_IVAR_$_ICNoteEditorDrawingController._paletteResponder
+ _OBJC_IVAR_$_ICNoteEditorDrawingController._recentlyCreatedDrawingInNewNoteAsPartOfPencilDown
+ _OBJC_IVAR_$_ICNoteEditorDrawingController._rulerHostingView
+ _OBJC_IVAR_$_ICNoteEditorDrawingController._showInkPickerAfterViewAppears
+ _OBJC_IVAR_$_ICNoteEditorDrawingController._wasEditingBeforeDrawing
+ _OBJC_IVAR_$_ICNoteEditorFormattingController._environment
+ _OBJC_IVAR_$_ICNoteEditorFormattingController._isLoadingStyleSelectorInputView
+ _OBJC_IVAR_$_ICNoteEditorFormattingController._noteFormattingController
+ _OBJC_IVAR_$_ICNoteEditorFormattingController._styleSelectorDummyInputView
+ _OBJC_IVAR_$_ICNoteEditorInlineAttachmentController._environment
+ _OBJC_IVAR_$_ICNoteEditorInlineAttachmentController._inlineAttachmentChangeController
+ _OBJC_IVAR_$_ICNoteEditorLockController._environment
+ _OBJC_IVAR_$_ICNoteEditorPresentationCoordinator._environment
+ _OBJC_IVAR_$_ICNoteEditorPresentationCoordinator._selectedTextRangeToRestoreAfterBarSourcedPopoverPresentation
+ _OBJC_IVAR_$_ICNoteEditorState._isAddingImageAttachment
+ _OBJC_IVAR_$_ICNoteEditorState._isConvertToTag
+ _OBJC_IVAR_$_ICNoteEditorState._isEditingNewNote
+ _OBJC_IVAR_$_ICNoteEditorState._isInLiveWindowResize
+ _OBJC_IVAR_$_ICNoteEditorState._isPerformingDeleteAnimation
+ _OBJC_IVAR_$_ICNoteEditorState._isPreviewingAttachmentFromNote
+ _OBJC_IVAR_$_ICNoteEditorState._isSelecting
+ _OBJC_IVAR_$_ICNoteEditorState._isSettingEditing
+ _OBJC_IVAR_$_ICNoteEditorState._isSettingSelection
+ _OBJC_IVAR_$_ICNoteEditorState._showingChecklistItems
+ _OBJC_IVAR_$_ICNoteEditorState._showingIndentationItems
+ _OBJC_IVAR_$_ICNoteEditorState._suspendBarButtonUpdates
+ _OBJC_IVAR_$_ICNoteEditorState._suspendSelectedRangeUpdates
+ _OBJC_IVAR_$_ICNoteEditorState._suspendTapGestureRecognizer
+ _OBJC_IVAR_$_ICNoteEditorState._togglingLock
+ _OBJC_IVAR_$_ICNoteEditorViewController._analytics
+ _OBJC_IVAR_$_ICNoteEditorViewController._attachmentCoordinator
+ _OBJC_IVAR_$_ICNoteEditorViewController._barController
+ _OBJC_IVAR_$_ICNoteEditorViewController._documentScanController
+ _OBJC_IVAR_$_ICNoteEditorViewController._drawingController
+ _OBJC_IVAR_$_ICNoteEditorViewController._editorState
+ _OBJC_IVAR_$_ICNoteEditorViewController._formattingController
+ _OBJC_IVAR_$_ICNoteEditorViewController._inlineAttachmentController
+ _OBJC_IVAR_$_ICNoteEditorViewController._lockController
+ _OBJC_IVAR_$_ICNoteEditorViewController._presentationCoordinator
+ _OBJC_IVAR_$_ICTK2TextView._isReadingTextForSharing
+ _OBJC_METACLASS_$_ICNoteEditorAnalytics
+ _OBJC_METACLASS_$_ICNoteEditorAttachmentCoordinator
+ _OBJC_METACLASS_$_ICNoteEditorBarController
+ _OBJC_METACLASS_$_ICNoteEditorDocumentScanController
+ _OBJC_METACLASS_$_ICNoteEditorDrawingController
+ _OBJC_METACLASS_$_ICNoteEditorFormattingController
+ _OBJC_METACLASS_$_ICNoteEditorInlineAttachmentController
+ _OBJC_METACLASS_$_ICNoteEditorLockController
+ _OBJC_METACLASS_$_ICNoteEditorPresentationCoordinator
+ _OBJC_METACLASS_$_ICNoteEditorState
+ __OBJC_$_CLASS_METHODS_ICNoteEditorFormattingController
+ __OBJC_$_CLASS_METHODS_ICNoteEditorPresentationCoordinator
+ __OBJC_$_INSTANCE_METHODS_ICNoteEditorAnalytics
+ __OBJC_$_INSTANCE_METHODS_ICNoteEditorAttachmentCoordinator
+ __OBJC_$_INSTANCE_METHODS_ICNoteEditorBarController
+ __OBJC_$_INSTANCE_METHODS_ICNoteEditorDocumentScanController
+ __OBJC_$_INSTANCE_METHODS_ICNoteEditorDrawingController
+ __OBJC_$_INSTANCE_METHODS_ICNoteEditorFormattingController
+ __OBJC_$_INSTANCE_METHODS_ICNoteEditorInlineAttachmentController
+ __OBJC_$_INSTANCE_METHODS_ICNoteEditorLockController
+ __OBJC_$_INSTANCE_METHODS_ICNoteEditorPresentationCoordinator
+ __OBJC_$_INSTANCE_METHODS_ICNoteEditorState
+ __OBJC_$_INSTANCE_VARIABLES_ICNoteEditorAnalytics
+ __OBJC_$_INSTANCE_VARIABLES_ICNoteEditorAttachmentCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_ICNoteEditorBarController
+ __OBJC_$_INSTANCE_VARIABLES_ICNoteEditorDocumentScanController
+ __OBJC_$_INSTANCE_VARIABLES_ICNoteEditorDrawingController
+ __OBJC_$_INSTANCE_VARIABLES_ICNoteEditorFormattingController
+ __OBJC_$_INSTANCE_VARIABLES_ICNoteEditorInlineAttachmentController
+ __OBJC_$_INSTANCE_VARIABLES_ICNoteEditorLockController
+ __OBJC_$_INSTANCE_VARIABLES_ICNoteEditorPresentationCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_ICNoteEditorState
+ __OBJC_$_PROP_LIST_ICNoteEditorAnalytics
+ __OBJC_$_PROP_LIST_ICNoteEditorAttachmentCoordinator
+ __OBJC_$_PROP_LIST_ICNoteEditorBarController
+ __OBJC_$_PROP_LIST_ICNoteEditorDocumentScanController
+ __OBJC_$_PROP_LIST_ICNoteEditorDrawingController
+ __OBJC_$_PROP_LIST_ICNoteEditorEnvironment
+ __OBJC_$_PROP_LIST_ICNoteEditorFormattingController
+ __OBJC_$_PROP_LIST_ICNoteEditorInlineAttachmentController
+ __OBJC_$_PROP_LIST_ICNoteEditorLockController
+ __OBJC_$_PROP_LIST_ICNoteEditorPresentationCoordinator
+ __OBJC_$_PROP_LIST_ICNoteEditorState
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ICNoteEditorEnvironment
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ICNoteEditorEnvironment
+ __OBJC_$_PROTOCOL_REFS_ICNoteEditorEnvironment
+ __OBJC_CLASS_PROTOCOLS_$_ICNoteEditorAttachmentCoordinator
+ __OBJC_CLASS_PROTOCOLS_$_ICNoteEditorBarController
+ __OBJC_CLASS_PROTOCOLS_$_ICNoteEditorDocumentScanController
+ __OBJC_CLASS_PROTOCOLS_$_ICNoteEditorDrawingController
+ __OBJC_CLASS_PROTOCOLS_$_ICNoteEditorFormattingController
+ __OBJC_CLASS_PROTOCOLS_$_ICNoteEditorInlineAttachmentController
+ __OBJC_CLASS_RO_$_ICNoteEditorAnalytics
+ __OBJC_CLASS_RO_$_ICNoteEditorAttachmentCoordinator
+ __OBJC_CLASS_RO_$_ICNoteEditorBarController
+ __OBJC_CLASS_RO_$_ICNoteEditorDocumentScanController
+ __OBJC_CLASS_RO_$_ICNoteEditorDrawingController
+ __OBJC_CLASS_RO_$_ICNoteEditorFormattingController
+ __OBJC_CLASS_RO_$_ICNoteEditorInlineAttachmentController
+ __OBJC_CLASS_RO_$_ICNoteEditorLockController
+ __OBJC_CLASS_RO_$_ICNoteEditorPresentationCoordinator
+ __OBJC_CLASS_RO_$_ICNoteEditorState
+ __OBJC_LABEL_PROTOCOL_$_ICNoteEditorEnvironment
+ __OBJC_METACLASS_RO_$_ICNoteEditorAnalytics
+ __OBJC_METACLASS_RO_$_ICNoteEditorAttachmentCoordinator
+ __OBJC_METACLASS_RO_$_ICNoteEditorBarController
+ __OBJC_METACLASS_RO_$_ICNoteEditorDocumentScanController
+ __OBJC_METACLASS_RO_$_ICNoteEditorDrawingController
+ __OBJC_METACLASS_RO_$_ICNoteEditorFormattingController
+ __OBJC_METACLASS_RO_$_ICNoteEditorInlineAttachmentController
+ __OBJC_METACLASS_RO_$_ICNoteEditorLockController
+ __OBJC_METACLASS_RO_$_ICNoteEditorPresentationCoordinator
+ __OBJC_METACLASS_RO_$_ICNoteEditorState
+ __OBJC_PROTOCOL_$_ICNoteEditorEnvironment
+ ___100-[ICNoteEditorDocumentScanController documentCameraControllerDidCancelWithPresentingViewController:]_block_invoke
+ ___101-[ICNoteEditorBarController noteEditorNavigationItemConfiguration:showWritingToolsFromBarButtonItem:]_block_invoke
+ ___105-[ICNoteEditorBarController noteEditorNavigationItemConfiguration:closeAuxiliaryWindowFromBarButtonItem:]_block_invoke
+ ___105-[ICNoteEditorBarController noteEditorNavigationItemConfiguration:closeAuxiliaryWindowFromBarButtonItem:]_block_invoke_2
+ ___124-[ICBaseTextView(StyleRendering) updateBlockQuoteLayerForParagraphStyle:inRange:ioPreviousBlockQuoteRect:ioBlockQuoteIsRTL:]_block_invoke
+ ___128-[ICNoteEditorInlineAttachmentController managedObjectContextChangeController:managedObjectIDsToUpdateForUpdatedManagedObjects:]_block_invoke
+ ___145-[ICNoteEditorDocumentScanController documentCameraPresentingViewController:didFinishWithInfoCollection:imageCache:warnUser:closeViewController:]_block_invoke
+ ___145-[ICNoteEditorDocumentScanController documentCameraPresentingViewController:didFinishWithInfoCollection:imageCache:warnUser:closeViewController:]_block_invoke_2
+ ___145-[ICNoteEditorDocumentScanController documentCameraPresentingViewController:didFinishWithInfoCollection:imageCache:warnUser:closeViewController:]_block_invoke_3
+ ___145-[ICNoteEditorDocumentScanController documentCameraPresentingViewController:didFinishWithInfoCollection:imageCache:warnUser:closeViewController:]_block_invoke_4
+ ___27-[ICEditingTextView paste:]_block_invoke_3
+ ___51-[ICNoteEditorFormattingController isBlockQuoteSet]_block_invoke
+ ___51-[ICNoteEditorFormattingController toggleToDoDone:]_block_invoke
+ ___51-[ICNoteEditorFormattingController toggleToDoDone:]_block_invoke_2
+ ___55-[ICNoteEditorDrawingController showDrawingUpdateAlert]_block_invoke
+ ___55-[ICNoteEditorDrawingController showDrawingUpdateAlert]_block_invoke_2
+ ___55-[ICNoteEditorDrawingController showDrawingUpdateAlert]_block_invoke_3
+ ___56-[ICNoteEditorDrawingController inkPalette:didPickTool:]_block_invoke
+ ___56-[ICNoteEditorViewController setToolbarHidden:animated:]_block_invoke
+ ___60-[ICNoteEditorDrawingController inkPalette:didShowAnimated:]_block_invoke
+ ___60-[ICNoteEditorDrawingController noteHasAnyPencilKitDrawings]_block_invoke
+ ___63-[ICNoteEditorDrawingController updateDrawingAttachmentsInNote]_block_invoke
+ ___64-[ICNoteEditorAttachmentCoordinator insertSidecarItems:service:]_block_invoke
+ ___64-[ICNoteEditorAttachmentCoordinator insertSidecarItems:service:]_block_invoke_2
+ ___65-[ICNoteEditorDrawingController inlineDrawingAttachmentForPoint:]_block_invoke
+ ___70-[ICNoteEditorAttachmentCoordinator showInsertUIForSourceType:sender:]_block_invoke
+ ___70-[ICNoteEditorDrawingController updateInlineDrawingsPaletteVisibility]_block_invoke
+ ___70-[ICNoteEditorFormattingController indentSelectionIfPossibleByAmount:]_block_invoke
+ ___74-[ICNoteEditorAttachmentCoordinator attachmentView:shouldShareAttachment:]_block_invoke
+ ___75-[ICNoteEditorLockController showOrHidePasswordEntryViewControllerIfNeeded]_block_invoke
+ ___75-[ICNoteEditorLockController showOrHidePasswordEntryViewControllerIfNeeded]_block_invoke_2
+ ___75-[ICNoteEditorLockController showOrHidePasswordEntryViewControllerIfNeeded]_block_invoke_3
+ ___75-[ICNoteEditorLockController showOrHidePasswordEntryViewControllerIfNeeded]_block_invoke_4
+ ___76-[ICNoteEditorInlineAttachmentController refreshInlineAttachmentTextStyling]_block_invoke
+ ___76-[ICNoteEditorPresentationCoordinator hideAndDismissPresentedViewController]_block_invoke
+ ___78-[ICNoteEditorDrawingController inkPalette:didChangePalettePositionStart:end:]_block_invoke
+ ___78-[ICNoteEditorViewController textView:primaryActionForTextItem:defaultAction:]_block_invoke
+ ___83-[ICNoteEditorFormattingController resetCurrentListTextStyleIfNecessaryWithSender:]_block_invoke
+ ___84-[ICNoteEditorFormattingController showStyleSelectorInputView:animated:doneEditing:]_block_invoke
+ ___86-[ICNoteEditorPresentationCoordinator prepareForPresentationOfViewControllerAnimated:]_block_invoke
+ ___88-[ICNoteEditorDrawingController upgradeAllAttachmentsInNoteWithUpgradeHelper:forSydney:]_block_invoke
+ ___88-[ICNoteEditorDrawingController upgradeAllAttachmentsInNoteWithUpgradeHelper:forSydney:]_block_invoke_2
+ ___88-[ICNoteEditorDrawingController upgradeAllAttachmentsInNoteWithUpgradeHelper:forSydney:]_block_invoke_3
+ ___91-[ICNoteEditorLockController showOrHideLockIconCoverViewControllerIfNeededIsBackgrounding:]_block_invoke
+ ___91-[ICNoteEditorLockController showOrHideLockIconCoverViewControllerIfNeededIsBackgrounding:]_block_invoke_2
+ ___98-[ICNoteEditorBarController noteEditorNavigationItemConfiguration:addNoteFromBarButtonItem:event:]_block_invoke
+ ___98-[ICNoteEditorBarController noteEditorNavigationItemConfiguration:addNoteFromBarButtonItem:event:]_block_invoke_2
+ ___block_descriptor_56_e8_32s40s48s_e12_v24?0Q8^B16ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_72_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_88_e8_32s40r48r56r64r72r80r_e18_v40?0Q8Q16Q24^B32lr40l8s32l8r48l8r56l8r64l8r72l8r80l8
+ ___swift_closure_destructor.159Tm
+ ___swift_closure_destructor.210Tm
+ ___swift_closure_destructor.252Tm
+ ___swift_closure_destructor.258Tm
+ ___swift_closure_destructor.401Tm
+ ___swift_closure_destructor.82Tm
+ ___swift_memcpy49_8
+ _objc_msgSend$analytics
+ _objc_msgSend$analyticsHostWindow
+ _objc_msgSend$attachFile:
+ _objc_msgSend$attachmentCoordinator
+ _objc_msgSend$barController
+ _objc_msgSend$canPerformToggleToDoDone
+ _objc_msgSend$canSetListStyle
+ _objc_msgSend$canSetParagraphStyle
+ _objc_msgSend$canToggleTodoStyle
+ _objc_msgSend$checkAll:
+ _objc_msgSend$clearDidDrawWithPencilWithoutPalette
+ _objc_msgSend$configureChangeControllerForNote:
+ _objc_msgSend$convertToTag:
+ _objc_msgSend$currentFirstResponder
+ _objc_msgSend$currentSelectionIsCaretAtLineStart
+ _objc_msgSend$disableBoldface
+ _objc_msgSend$disableItalics
+ _objc_msgSend$disableStrikethrough
+ _objc_msgSend$disableUnderline
+ _objc_msgSend$dismissCurrentAttachmentPresenterAnimated:
+ _objc_msgSend$documentScanController
+ _objc_msgSend$drawBlockQuoteAndCleanup:pendingBlockQuoteLevelToDraw:pendingBlockQuoteRectToDraw:ioBlockQuoteIsRTL:ps:
+ _objc_msgSend$drawBlockQuoteLayerInRectForTK2:blockQuoteLevel:isMonostyled:isRTL:
+ _objc_msgSend$drawingController
+ _objc_msgSend$editorAddSubviewAboveAllViews:
+ _objc_msgSend$editorDelegateRespondsToDidTapAttachment
+ _objc_msgSend$editorHasCompactWidth
+ _objc_msgSend$editorNavigationController
+ _objc_msgSend$editorState
+ _objc_msgSend$enableBoldface
+ _objc_msgSend$enableItalics
+ _objc_msgSend$enableStrikethrough
+ _objc_msgSend$enableUnderline
+ _objc_msgSend$environment
+ _objc_msgSend$filteredAttributedSubstringFromRange:
+ _objc_msgSend$formattingController
+ _objc_msgSend$formattingTextViewInputAccessoryView
+ _objc_msgSend$hostViewController
+ _objc_msgSend$ic_alignCenter:
+ _objc_msgSend$ic_alignLeft:
+ _objc_msgSend$ic_alignRight:
+ _objc_msgSend$ic_flattenedTextForSharingInRange:
+ _objc_msgSend$ic_rangeIsCaretAtLineStart:
+ _objc_msgSend$ic_selectionContainsOnlyBlockAttachments
+ _objc_msgSend$initWithEnvironment:
+ _objc_msgSend$initWithEnvironment:subTrackerName:
+ _objc_msgSend$inlineAttachmentController
+ _objc_msgSend$insertDividerLine:
+ _objc_msgSend$isEndOfDocumentForTextPosition:inTextView:
+ _objc_msgSend$isNoteFormattingViewControllerShowing
+ _objc_msgSend$isReadingTextForSharing
+ _objc_msgSend$isStyleSelectorInputViewShowing
+ _objc_msgSend$lockController
+ _objc_msgSend$moveCheckedToBottom:
+ _objc_msgSend$navigationBarMinimization
+ _objc_msgSend$needsTranscription
+ _objc_msgSend$notifyEditorDelegateDidTapAttachment:
+ _objc_msgSend$predicateForSearchableNotesInContext:
+ _objc_msgSend$prepareForBarSourcedPopoverPresentation
+ _objc_msgSend$prepareForPresentationOfViewControllerAnimated:
+ _objc_msgSend$presentAttachment:
+ _objc_msgSend$presentAttachments:startingAtIndex:editable:
+ _objc_msgSend$presentationCoordinator
+ _objc_msgSend$removeChecked:
+ _objc_msgSend$setBodyStyle:
+ _objc_msgSend$setBulletedListStyle:
+ _objc_msgSend$setDashedListStyle:
+ _objc_msgSend$setFixedWidthStyle:
+ _objc_msgSend$setFormattingUpdatesSuspended:
+ _objc_msgSend$setHeadingStyle:
+ _objc_msgSend$setIsReadingTextForSharing:
+ _objc_msgSend$setMinimizationBehavior:
+ _objc_msgSend$setNumberedListStyle:
+ _objc_msgSend$setStyleSelectorAXFocusElementOnDismissal:
+ _objc_msgSend$setSubheadingStyle:
+ _objc_msgSend$setTitleStyle:
+ _objc_msgSend$showDocumentCamera
+ _objc_msgSend$showInsertAudio:
+ _objc_msgSend$subTrackerName
+ _objc_msgSend$suspendSelectedRangeUpdates
+ _objc_msgSend$toggleBoldface
+ _objc_msgSend$toggleCurrentTextStyle:
+ _objc_msgSend$toggleInkPickerAnimated:
+ _objc_msgSend$toggleItalics
+ _objc_msgSend$toggleStrikethrough
+ _objc_msgSend$toggleToDoDone:
+ _objc_msgSend$toggleUnderline
+ _objc_msgSend$trailingItemGroups
+ _objc_msgSend$uncheckAll:
+ _objc_msgSend$updateBlockQuoteLayerForParagraphStyle:inRange:ioPreviousBlockQuoteRect:ioBlockQuoteIsRTL:
+ _objc_msgSend$updateContentViewBezelsForPasswordEntry
+ _objc_msgSend$updatePaperKitMessengerForAttachment:textLayoutManager:
+ _objc_msgSend$visualAssetImportControllerIsShowing
+ _symbolic SDySi_____G 10Foundation16AttributedStringV11NotesSharedE43TranscriptParagraphAccessibilityInformationV
+ _symbolic _____ 11NotesEditor14TranscriptViewC26AccessibilityElementsState33_70FAB152AD64B0C479A9BB619ADB754CLLV
+ _symbolic _____Sg 11NotesEditor14TranscriptViewC26AccessibilityElementsState33_70FAB152AD64B0C479A9BB619ADB754CLLV
+ _type_layout_string 11NotesEditor14TranscriptViewC26AccessibilityElementsState33_70FAB152AD64B0C479A9BB619ADB754CLLV
- +[ICNoteEditorViewController dismissChildPresentedViewControllersInPostOrder:animated:completion:]
- -[ICBaseTextView(StyleRendering) drawBlockQuoteAndCleanup:pendingBlockQuoteLevelToDraw:pendingBlockQuoteRectToDraw:ps:]
- -[ICBaseTextView(StyleRendering) drawBlockQuoteLayerInRectForTK2:blockQuoteLevel:isMonostyled:]
- -[ICBaseTextView(StyleRendering) updateBlockQuoteLayerForParagraphStyle:inRange:ioPreviousBlockQuoteRect:]
- -[ICNoteEditorViewController _scribbleInteraction:shouldBeginAtLocation:]
- -[ICNoteEditorViewController _scribbleInteraction:willBeginWritingInElement:]
- -[ICNoteEditorViewController addSystemPaperAttachment]
- -[ICNoteEditorViewController attachmentInsertionController:didAddAttachment:atRange:]
- -[ICNoteEditorViewController attachmentInsertionController:didAddInlineAttachment:atRange:textStorage:]
- -[ICNoteEditorViewController attachmentInsertionController:willAddAttachment:atRange:]
- -[ICNoteEditorViewController attachmentView:shouldPresentAttachment:]
- -[ICNoteEditorViewController attachmentView:shouldPresentNote:]
- -[ICNoteEditorViewController attachmentView:shouldRespondToPanGestureTouch:forAttachment:]
- -[ICNoteEditorViewController attachmentView:shouldShareAttachment:]
- -[ICNoteEditorViewController audioEventReporterLostSession:]
- -[ICNoteEditorViewController cleanupAfterFingerDrawing]
- -[ICNoteEditorViewController clearTextViewSelection]
- -[ICNoteEditorViewController createdGalleryAttachmentUUID]
- -[ICNoteEditorViewController currentSelectionContainsListOrFixedWidth]
- -[ICNoteEditorViewController currentStrokeStartTouch]
- -[ICNoteEditorViewController currentValidToolForNewDrawingOrNote]
- -[ICNoteEditorViewController dateOfLastStrokeOrNewDrawing]
- -[ICNoteEditorViewController defaultInkColor]
- -[ICNoteEditorViewController didDrawWithPencilWithoutPalette]
- -[ICNoteEditorViewController documentCameraController:canAddImages:]
- -[ICNoteEditorViewController documentCameraController:didFinishWithDocInfoCollection:imageCache:warnUser:]
- -[ICNoteEditorViewController documentCameraController:didFinishWithDocInfoCollection:imageCache:warnUser:closeViewController:]
- -[ICNoteEditorViewController documentCameraControllerCreateDataCryptorIfNecessary]
- -[ICNoteEditorViewController documentCameraControllerDidCancel:]
- -[ICNoteEditorViewController documentCameraControllerDidCancelWithPresentingViewController:]
- -[ICNoteEditorViewController documentCameraControllerDidRetake:pageCount:]
- -[ICNoteEditorViewController documentCameraPresentingViewController:didFinishWithInfoCollection:imageCache:warnUser:closeViewController:]
- -[ICNoteEditorViewController documentPicker:didPickDocumentsAtURLs:]
- -[ICNoteEditorViewController drawingsForHandwritingDebug]
- -[ICNoteEditorViewController ensureValidInkForNewDrawingOrNote]
- -[ICNoteEditorViewController eventReporterLostSession:]
- -[ICNoteEditorViewController handwritingDebugPresenter]
- -[ICNoteEditorViewController handwritingDebugShouldClose]
- -[ICNoteEditorViewController hashtagInsertedInNote:tokenContentIdentifier:viaAutoComplete:]
- -[ICNoteEditorViewController hashtagViewController:insertFutureHashtagWithText:]
- -[ICNoteEditorViewController hashtagViewController:insertHashtagWithText:]
- -[ICNoteEditorViewController hashtagViewController:insertUnknownInlineAttachmentWithText:]
- -[ICNoteEditorViewController icasPalettePositionFromPKPalettePosition:]
- -[ICNoteEditorViewController inkPalette:didChangeColor:]
- -[ICNoteEditorViewController inkPalette:didChangePalettePositionStart:end:]
- -[ICNoteEditorViewController inkPalette:didHideAnimated:]
- -[ICNoteEditorViewController inkPalette:didPickTool:]
- -[ICNoteEditorViewController inkPalette:didShowAnimated:]
- -[ICNoteEditorViewController inkPalette:shouldResignFirstResponder:]
- -[ICNoteEditorViewController inkPalette:willHideAnimated:]
- -[ICNoteEditorViewController inkPalette:willShowAnimated:]
- -[ICNoteEditorViewController inkPaletteButtonView:]
- -[ICNoteEditorViewController inkPaletteDidToggleRuler:isRulerActive:]
- -[ICNoteEditorViewController inkPaletteUndoManager:]
- -[ICNoteEditorViewController inkPickerState]
- -[ICNoteEditorViewController inlineAttachmentChangeController]
- -[ICNoteEditorViewController inlineAttachmentDeleted:]
- -[ICNoteEditorViewController inlineDrawingAttachmentForPoint:]
- -[ICNoteEditorViewController isDocumentCameraAvailable]
- -[ICNoteEditorViewController isDrawingStrokeWithPencil]
- -[ICNoteEditorViewController isDrawingStroke]
- -[ICNoteEditorViewController isEditingNewNote]
- -[ICNoteEditorViewController isInLiveWindowResize]
- -[ICNoteEditorViewController isLoadingStyleSelectorInputView]
- -[ICNoteEditorViewController isNewInk:]
- -[ICNoteEditorViewController isPencilModeTransitory]
- -[ICNoteEditorViewController isPerformingDeleteAnimation]
- -[ICNoteEditorViewController isPhotosLibraryAvailable]
- -[ICNoteEditorViewController isSelecting]
- -[ICNoteEditorViewController isSettingEditing]
- -[ICNoteEditorViewController isSettingSelection]
- -[ICNoteEditorViewController isShowingChecklistItems]
- -[ICNoteEditorViewController isShowingIndentationItems]
- -[ICNoteEditorViewController isTogglingLock]
- -[ICNoteEditorViewController mentionInsertedInNote:mentionID:participantID:viaAutoComplete:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:addChecklistFromBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:addNoteFromBarButtonItem:event:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:addTableFromBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:changeStyleFromBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:closeAuxiliaryWindowFromBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:deleteFromBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:didCompleteAnimationFromInlineSketchBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:doneEditingFromBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:inlineSketchFromBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:insertMediaWithSourceType:mediaBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:insertSidecarItemWithMenuItems:service:mediaBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:leftIndentWithSender:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:moveDownWithSender:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:moveFromBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:moveUpWithSender:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:openLinkEditorWithSender:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:quickNoteDidCancelFromBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:quickNoteDidSaveFromBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:quickNoteShowAllNotesFromBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:redoFromBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:rightIndentWithSender:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:setEmphasis:fromBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:setListStyle:withSender:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:setToolbarHidden:animated:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:shareFromBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:showPhotoLibraryFromBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:showWritingToolsFromBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:startEditingFromBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:toggleBIUS:fromBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:toggleBlockQuoteWithSender:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:toggleLockFromBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:toggleSidebarFromBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfiguration:undoFromBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfigurationChecklistAccessibilityValue:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfigurationCollaborationBarButtonItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfigurationContextualInputAccessoryView:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfigurationEmphasisAccessibilityCustomContentValue:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfigurationIndentationAccessibilityValue:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfigurationInputAccessoryToolbar:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfigurationInputAssistantItem:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfigurationIsStyleSheetShowing:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfigurationIsToolbarHidden:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfigurationPresentingSourceView:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfigurationPresentingViewController:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfigurationPresentingWindowScene:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfigurationStyleSelectorViewController:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfigurationTableAttachmentViewController:]
- -[ICNoteEditorViewController noteEditorNavigationItemConfigurationToolbarItemSource:]
- -[ICNoteEditorViewController noteFormattingControllerCreateIfNecessary]
- -[ICNoteEditorViewController noteFormattingController]
- -[ICNoteEditorViewController noteFormattingDidFinish:]
- -[ICNoteEditorViewController noteFormattingNeedsUpdate:]
- -[ICNoteEditorViewController noteFormattingTintColor]
- -[ICNoteEditorViewController noteHasAnyPencilKitDrawings]
- -[ICNoteEditorViewController notesQuickLookActivityItem:rectForPreviewItem:inView:previewController:]
- -[ICNoteEditorViewController notesQuickLookActivityItem:transitionViewForPreviewItem:previewController:]
- -[ICNoteEditorViewController paletteResponder]
- -[ICNoteEditorViewController paperTextAttachmentManager:beginTrackingUndoManager:]
- -[ICNoteEditorViewController paperTextAttachmentManager:endTrackingUndoManager:]
- -[ICNoteEditorViewController presentingViewControllerForStyleSelector:]
- -[ICNoteEditorViewController radarTitleForHandwritingDebug]
- -[ICNoteEditorViewController recentlyCreatedDrawingInNewNoteAsPartOfPencilDown]
- -[ICNoteEditorViewController refreshInlineAttachmentTextStyling]
- -[ICNoteEditorViewController remoteDocumentCameraController:didFailWithError:]
- -[ICNoteEditorViewController remoteDocumentCameraController:didFinishWithInfoCollection:]
- -[ICNoteEditorViewController remoteDocumentCameraControllerDidCancel:]
- -[ICNoteEditorViewController resetCurrentListTextStyleIfNecessaryWithSender:]
- -[ICNoteEditorViewController responderToMatch]
- -[ICNoteEditorViewController rulerHostWantsSharedRuler]
- -[ICNoteEditorViewController rulerHostingView]
- -[ICNoteEditorViewController saveToolAsCurrentTool:]
- -[ICNoteEditorViewController scanDataDelegateWithIdentifier:]
- -[ICNoteEditorViewController selectedTextRangeToRestoreAfterBarSourcedPopoverPresentation]
- -[ICNoteEditorViewController setAudioEventReporter:]
- -[ICNoteEditorViewController setCreatedGalleryAttachmentUUID:]
- -[ICNoteEditorViewController setCurrentStrokeStartTouch:]
- -[ICNoteEditorViewController setDateOfLastStrokeOrNewDrawing:]
- -[ICNoteEditorViewController setDidDrawWithPencilWithoutPalette:]
- -[ICNoteEditorViewController setEmphasisType:sender:]
- -[ICNoteEditorViewController setEventReporter:]
- -[ICNoteEditorViewController setFindResultReporter:]
- -[ICNoteEditorViewController setHandwritingDebugPresenter:]
- -[ICNoteEditorViewController setInkPaletteController:]
- -[ICNoteEditorViewController setInkPickerState:]
- -[ICNoteEditorViewController setInlineAttachmentChangeController:]
- -[ICNoteEditorViewController setIsDrawingStroke:]
- -[ICNoteEditorViewController setIsDrawingStrokeWithPencil:]
- -[ICNoteEditorViewController setIsEditingNewNote:]
- -[ICNoteEditorViewController setIsInLiveWindowResize:]
- -[ICNoteEditorViewController setIsLoadingStyleSelectorInputView:]
- -[ICNoteEditorViewController setIsPencilModeTransitory:]
- -[ICNoteEditorViewController setIsPerformingDeleteAnimation:]
- -[ICNoteEditorViewController setIsSelecting:]
- -[ICNoteEditorViewController setIsSettingEditing:]
- -[ICNoteEditorViewController setIsSettingSelection:]
- -[ICNoteEditorViewController setNoteFormattingController:]
- -[ICNoteEditorViewController setPaletteResponder:]
- -[ICNoteEditorViewController setRecentlyCreatedDrawingInNewNoteAsPartOfPencilDown:]
- -[ICNoteEditorViewController setRulerHostingView:]
- -[ICNoteEditorViewController setSelectedTextRangeToRestoreAfterBarSourcedPopoverPresentation:]
- -[ICNoteEditorViewController setShouldOverscrollScrollState:]
- -[ICNoteEditorViewController setShowInkPickerAfterViewAppears:]
- -[ICNoteEditorViewController setShowingChecklistItems:]
- -[ICNoteEditorViewController setShowingIndentationItems:]
- -[ICNoteEditorViewController setStyleSelectorDummyInputView:]
- -[ICNoteEditorViewController setSuspendBarButtonUpdates:]
- -[ICNoteEditorViewController setSuspendSelectedRangeUpdates:]
- -[ICNoteEditorViewController setSuspendTapGestureRecognizer:]
- -[ICNoteEditorViewController setTextStyle:sender:]
- -[ICNoteEditorViewController setTogglingLock:]
- -[ICNoteEditorViewController setUserInteractionEnabled:]
- -[ICNoteEditorViewController setWasEditingBeforeDrawing:]
- -[ICNoteEditorViewController setWasWindowlessDuringTransitionToSize:]
- -[ICNoteEditorViewController setupForFingerDrawing]
- -[ICNoteEditorViewController shouldEnablePencilGestures]
- -[ICNoteEditorViewController shouldOverscrollScrollState]
- -[ICNoteEditorViewController showDocumentPicker]
- -[ICNoteEditorViewController showInkPickerAfterViewAppears]
- -[ICNoteEditorViewController showInkPickerAndEndEditingIfNecessary]
- -[ICNoteEditorViewController showOrHideLockIconCoverViewControllerIfNeededIsBackgrounding:]
- -[ICNoteEditorViewController showOrHidePasswordEntryViewControllerIfNeeded]
- -[ICNoteEditorViewController styleSelector:didChangeIndentAmount:]
- -[ICNoteEditorViewController styleSelector:didSelectStyle:]
- -[ICNoteEditorViewController styleSelector:presentViewController:animated:completion:]
- -[ICNoteEditorViewController styleSelector:toggleBIUS:]
- -[ICNoteEditorViewController styleSelectorCanIndentLeft:]
- -[ICNoteEditorViewController styleSelectorCanIndentRight:]
- -[ICNoteEditorViewController styleSelectorDidCancel:]
- -[ICNoteEditorViewController styleSelectorDidIndentLeft:]
- -[ICNoteEditorViewController styleSelectorDidIndentRight:]
- -[ICNoteEditorViewController styleSelectorDummyInputView]
- -[ICNoteEditorViewController styleSelectorInputViewShowing]
- -[ICNoteEditorViewController styleSelectorSelectionHasBlockQuote:]
- -[ICNoteEditorViewController styleSelectorShouldDisableTextStyles:]
- -[ICNoteEditorViewController styleSelectorShouldUseCompactTopInset:]
- -[ICNoteEditorViewController styleSelectorToggleBlockQuote:]
- -[ICNoteEditorViewController styleSelectorWillShowInlineMenu:]
- -[ICNoteEditorViewController suspendBarButtonUpdates]
- -[ICNoteEditorViewController suspendSelectedRangeUpdates]
- -[ICNoteEditorViewController suspendTapGestureRecognizer]
- -[ICNoteEditorViewController textView:canAddDrawingAtIndex:]
- -[ICNoteEditorViewController textView:didRemoveDrawingAtIndex:]
- -[ICNoteEditorViewController textView:newAttachmentForFileType:]
- -[ICNoteEditorViewController textView:shouldInteractWithURL:inRange:interaction:]
- -[ICNoteEditorViewController textView:upgradeDrawingAtIndex:itemProviders:insertionLocationInDrawing:]
- -[ICNoteEditorViewController textView:willAddDrawingAtIndex:]
- -[ICNoteEditorViewController textViewCanAddStroke:]
- -[ICNoteEditorViewController textViewCanSelectDrawing:]
- -[ICNoteEditorViewController textViewDidEndStroke:]
- -[ICNoteEditorViewController textViewWillBeginStroke:forTouch:]
- -[ICNoteEditorViewController undoablySwitchToPPK:]
- -[ICNoteEditorViewController updateDrawingAttachmentsInNote]
- -[ICNoteEditorViewController updateInlineDrawingsPaletteVisibility]
- -[ICNoteEditorViewController updateInlineDrawings]
- -[ICNoteEditorViewController updateUIEnabledStatePencilActive:]
- -[ICNoteEditorViewController upgradeAllAttachmentsInNoteWithUpgradeHelper:forSydney:]
- -[ICNoteEditorViewController upgradePencilKitDrawingsForNewInksPromptingIfNecessary]
- -[ICNoteEditorViewController useInputViewForStyleSelector]
- -[ICNoteEditorViewController wasEditingBeforeDrawing]
- -[ICNoteEditorViewController wasWindowlessDuringTransitionToSize]
- -[ICTK2NoteEditorViewController textView:isEndOfDocument:]
- -[ICTextView hideOverlappingAttachmentViewsIfNecessary]
- -[ICTextView needsHideOverlappingAttachmentViews]
- -[ICTextView previousContentSize]
- -[ICTextView setNeedsHideOverlappingAttachmentViews:]
- -[ICTextView setPreviousContentSize:]
- -[ICTextView shouldUpdateVisibleSupplementalViewsInLayoutSubviews]
- GCC_except_table105
- GCC_except_table112
- GCC_except_table120
- GCC_except_table130
- GCC_except_table145
- GCC_except_table148
- GCC_except_table167
- GCC_except_table170
- GCC_except_table183
- GCC_except_table219
- GCC_except_table269
- GCC_except_table317
- GCC_except_table323
- GCC_except_table352
- GCC_except_table354
- GCC_except_table357
- GCC_except_table36
- GCC_except_table405
- GCC_except_table44
- GCC_except_table51
- GCC_except_table548
- GCC_except_table579
- GCC_except_table584
- GCC_except_table610
- GCC_except_table63
- GCC_except_table649
- GCC_except_table682
- GCC_except_table694
- GCC_except_table724
- GCC_except_table725
- GCC_except_table742
- GCC_except_table75
- GCC_except_table83
- GCC_except_table92
- _ICCurrentInkDataDefaultsKey_block_invoke.disableWorkaroundFor150051673
- _ICCurrentInkDataDefaultsKey_block_invoke.disableWorkaroundFor150051673_token
- _ICInternalSettingsIsBlockQuoteEnabled
- _ICInternalSettingsIsCollapsibleSectionsEnabled
- _ICInternalSettingsIsEmphasisEnabled
- _ICInternalSettingsIsGraphingEnabled
- _ICInternalSettingsIsMathEnabled
- _ICInternalSettingsIsNotesMathEnabled
- _ICInternalSettingsIsPaperKitMathEnabled
- _ICInternalSettingsIsScrubbingEnabled
- _ICInternalSettingsIsTextKit2Enabled
- _NSProtocolFromString
- _NSTextEffectAttributeName
- _OBJC_IVAR_$_ICNoteEditorViewController._audioEventReporter
- _OBJC_IVAR_$_ICNoteEditorViewController._createdGalleryAttachmentUUID
- _OBJC_IVAR_$_ICNoteEditorViewController._currentStrokeStartTouch
- _OBJC_IVAR_$_ICNoteEditorViewController._dateOfLastStrokeOrNewDrawing
- _OBJC_IVAR_$_ICNoteEditorViewController._didDrawWithPencilWithoutPalette
- _OBJC_IVAR_$_ICNoteEditorViewController._eventReporter
- _OBJC_IVAR_$_ICNoteEditorViewController._findResultReporter
- _OBJC_IVAR_$_ICNoteEditorViewController._handwritingDebugPresenter
- _OBJC_IVAR_$_ICNoteEditorViewController._inkPaletteController
- _OBJC_IVAR_$_ICNoteEditorViewController._inkPickerState
- _OBJC_IVAR_$_ICNoteEditorViewController._inlineAttachmentChangeController
- _OBJC_IVAR_$_ICNoteEditorViewController._isAddingImageAttachment
- _OBJC_IVAR_$_ICNoteEditorViewController._isConvertToTag
- _OBJC_IVAR_$_ICNoteEditorViewController._isDrawingStroke
- _OBJC_IVAR_$_ICNoteEditorViewController._isDrawingStrokeWithPencil
- _OBJC_IVAR_$_ICNoteEditorViewController._isEditingNewNote
- _OBJC_IVAR_$_ICNoteEditorViewController._isInLiveWindowResize
- _OBJC_IVAR_$_ICNoteEditorViewController._isLoadingStyleSelectorInputView
- _OBJC_IVAR_$_ICNoteEditorViewController._isPencilModeTransitory
- _OBJC_IVAR_$_ICNoteEditorViewController._isPerformingDeleteAnimation
- _OBJC_IVAR_$_ICNoteEditorViewController._isPreviewingAttachmentFromNote
- _OBJC_IVAR_$_ICNoteEditorViewController._isSelecting
- _OBJC_IVAR_$_ICNoteEditorViewController._isSettingEditing
- _OBJC_IVAR_$_ICNoteEditorViewController._isSettingSelection
- _OBJC_IVAR_$_ICNoteEditorViewController._noteFormattingController
- _OBJC_IVAR_$_ICNoteEditorViewController._paletteResponder
- _OBJC_IVAR_$_ICNoteEditorViewController._recentlyCreatedDrawingInNewNoteAsPartOfPencilDown
- _OBJC_IVAR_$_ICNoteEditorViewController._rulerHostingView
- _OBJC_IVAR_$_ICNoteEditorViewController._selectedTextRangeToRestoreAfterBarSourcedPopoverPresentation
- _OBJC_IVAR_$_ICNoteEditorViewController._shouldOverscrollScrollState
- _OBJC_IVAR_$_ICNoteEditorViewController._showInkPickerAfterViewAppears
- _OBJC_IVAR_$_ICNoteEditorViewController._showingChecklistItems
- _OBJC_IVAR_$_ICNoteEditorViewController._showingIndentationItems
- _OBJC_IVAR_$_ICNoteEditorViewController._styleSelectorDummyInputView
- _OBJC_IVAR_$_ICNoteEditorViewController._suspendBarButtonUpdates
- _OBJC_IVAR_$_ICNoteEditorViewController._suspendSelectedRangeUpdates
- _OBJC_IVAR_$_ICNoteEditorViewController._suspendTapGestureRecognizer
- _OBJC_IVAR_$_ICNoteEditorViewController._togglingLock
- _OBJC_IVAR_$_ICNoteEditorViewController._wasEditingBeforeDrawing
- _OBJC_IVAR_$_ICNoteEditorViewController._wasWindowlessDuringTransitionToSize
- _OBJC_IVAR_$_ICTextView._needsHideOverlappingAttachmentViews
- _OBJC_IVAR_$_ICTextView._previousContentSize
- _OUTLINED_FUNCTION_6
- ___102-[ICNoteEditorViewController noteEditorNavigationItemConfiguration:showWritingToolsFromBarButtonItem:]_block_invoke
- ___105-[ICEditingTextView(DragAndDrop) textPasteConfigurationSupporting:combineItemAttributedStrings:forRange:]_block_invoke_4
- ___106-[ICBaseTextView(StyleRendering) updateBlockQuoteLayerForParagraphStyle:inRange:ioPreviousBlockQuoteRect:]_block_invoke
- ___106-[ICEditingTextView(DragAndDrop) textPasteConfigurationSupporting:performPasteOfAttributedString:toRange:]_block_invoke_3
- ___106-[ICEditingTextView(DragAndDrop) textPasteConfigurationSupporting:performPasteOfAttributedString:toRange:]_block_invoke_4
- ___106-[ICEditingTextView(DragAndDrop) textPasteConfigurationSupporting:performPasteOfAttributedString:toRange:]_block_invoke_5
- ___106-[ICEditingTextView(DragAndDrop) textPasteConfigurationSupporting:performPasteOfAttributedString:toRange:]_block_invoke_6
- ___106-[ICNoteEditorViewController noteEditorNavigationItemConfiguration:closeAuxiliaryWindowFromBarButtonItem:]_block_invoke
- ___106-[ICNoteEditorViewController noteEditorNavigationItemConfiguration:closeAuxiliaryWindowFromBarButtonItem:]_block_invoke_2
- ___116-[ICNoteEditorViewController managedObjectContextChangeController:managedObjectIDsToUpdateForUpdatedManagedObjects:]_block_invoke_2
- ___137-[ICNoteEditorViewController documentCameraPresentingViewController:didFinishWithInfoCollection:imageCache:warnUser:closeViewController:]_block_invoke
- ___137-[ICNoteEditorViewController documentCameraPresentingViewController:didFinishWithInfoCollection:imageCache:warnUser:closeViewController:]_block_invoke_2
- ___137-[ICNoteEditorViewController documentCameraPresentingViewController:didFinishWithInfoCollection:imageCache:warnUser:closeViewController:]_block_invoke_3
- ___137-[ICNoteEditorViewController documentCameraPresentingViewController:didFinishWithInfoCollection:imageCache:warnUser:closeViewController:]_block_invoke_4
- ___32-[ICTextView _updateContentSize]_block_invoke_2
- ___37-[ICTextView pressesBegan:withEvent:]_block_invoke_2
- ___40-[ICImageAttachmentView updateImageSize]_block_invoke
- ___45-[ICNoteEditorViewController isBlockQuoteSet]_block_invoke
- ___45-[ICNoteEditorViewController toggleToDoDone:]_block_invoke
- ___45-[ICNoteEditorViewController toggleToDoDone:]_block_invoke_2
- ___47-[ICNoteEditorViewController sceneDidActivate:]_block_invoke
- ___52-[ICNoteEditorViewController showDrawingUpdateAlert]_block_invoke
- ___52-[ICNoteEditorViewController showDrawingUpdateAlert]_block_invoke_2
- ___52-[ICNoteEditorViewController showDrawingUpdateAlert]_block_invoke_3
- ___52-[ICTextFindingResult framesForHighlightInTextView:]_block_invoke_2
- ___52-[ICTextFindingResult framesForHighlightInTextView:]_block_invoke_3
- ___53-[ICNoteEditorViewController inkPalette:didPickTool:]_block_invoke
- ___55-[ICTextView hideOverlappingAttachmentViewsIfNecessary]_block_invoke
- ___57-[ICNoteEditorViewController insertSidecarItems:service:]_block_invoke
- ___57-[ICNoteEditorViewController insertSidecarItems:service:]_block_invoke_2
- ___57-[ICNoteEditorViewController noteHasAnyPencilKitDrawings]_block_invoke
- ___60-[ICNoteEditorViewController setArchivedScrollStateToApply:]_block_invoke_2
- ___60-[ICNoteEditorViewController updateDrawingAttachmentsInNote]_block_invoke
- ___62-[ICNoteEditorViewController inlineDrawingAttachmentForPoint:]_block_invoke
- ___63-[ICNoteEditorViewController showInsertUIForSourceType:sender:]_block_invoke
- ___64-[ICNoteEditorViewController indentSelectionIfPossibleByAmount:]_block_invoke
- ___64-[ICNoteEditorViewController refreshInlineAttachmentTextStyling]_block_invoke
- ___67-[ICNoteEditorViewController attachmentView:shouldShareAttachment:]_block_invoke
- ___67-[ICNoteEditorViewController hideAndDismissPresentedViewController]_block_invoke
- ___67-[ICNoteEditorViewController updateInlineDrawingsPaletteVisibility]_block_invoke
- ___72-[ICNoteEditorNavigationItemConfiguration performInlineSketchAnimation:]_block_invoke
- ___72-[ICNoteEditorViewController presentViewController:animated:completion:]_block_invoke
- ___75-[ICNoteEditorViewController inkPalette:didChangePalettePositionStart:end:]_block_invoke
- ___75-[ICNoteEditorViewController showOrHidePasswordEntryViewControllerIfNeeded]_block_invoke
- ___75-[ICNoteEditorViewController showOrHidePasswordEntryViewControllerIfNeeded]_block_invoke_2
- ___75-[ICNoteEditorViewController showOrHidePasswordEntryViewControllerIfNeeded]_block_invoke_3
- ___75-[ICNoteEditorViewController showOrHidePasswordEntryViewControllerIfNeeded]_block_invoke_4
- ___77-[ICEditingTextView(ICAccessibility_iOS) _icaxLinePositionForPosition:start:]_block_invoke_3
- ___77-[ICNoteEditorViewController resetCurrentListTextStyleIfNecessaryWithSender:]_block_invoke
- ___78-[ICNoteEditorViewController showStyleSelectorInputView:animated:doneEditing:]_block_invoke
- ___85-[ICNoteEditorViewController upgradeAllAttachmentsInNoteWithUpgradeHelper:forSydney:]_block_invoke
- ___85-[ICNoteEditorViewController upgradeAllAttachmentsInNoteWithUpgradeHelper:forSydney:]_block_invoke_2
- ___85-[ICNoteEditorViewController upgradeAllAttachmentsInNoteWithUpgradeHelper:forSydney:]_block_invoke_3
- ___91-[ICNoteEditorViewController showOrHideLockIconCoverViewControllerIfNeededIsBackgrounding:]_block_invoke
- ___91-[ICNoteEditorViewController showOrHideLockIconCoverViewControllerIfNeededIsBackgrounding:]_block_invoke_2
- ___92-[ICNoteEditorViewController documentCameraControllerDidCancelWithPresentingViewController:]_block_invoke
- ___94-[ICNoteEditorViewController noteEditorNavigationItemConfiguration:setToolbarHidden:animated:]_block_invoke
- ___99-[ICEditingTextView(StyleAdditions) ic_enumerateTableAttachmentViewControllersInRanges:usingBlock:]_block_invoke_2
- ___99-[ICNoteEditorViewController noteEditorNavigationItemConfiguration:addNoteFromBarButtonItem:event:]_block_invoke
- ___99-[ICNoteEditorViewController noteEditorNavigationItemConfiguration:addNoteFromBarButtonItem:event:]_block_invoke_2
- ___block_descriptor_104_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_56_e8_32s40r_e113_v104?0{CGRect={CGPoint=dd}{CGSize=dd}}8{CGRect={CGPoint=dd}{CGSize=dd}}40"NSTextContainer"72{_NSRange=QQ}80^B96ls32l8r40l8
- ___block_descriptor_56_e8_32s_e45_v40?0"NSTextAttachment"8{_NSRange=QQ}16^B32ls32l8
- ___block_descriptor_72_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s_e43_v48?0{CGRect={CGPoint=dd}{CGSize=dd}}8^B40ls32l8
- ___block_descriptor_80_e8_32s40r48r56r64r72r_e18_v40?0Q8Q16Q24^B32lr40l8s32l8r48l8r56l8r64l8r72l8
- ___block_descriptor_80_e8_32s40s48r56r_e5_v8?0ls32l8s40l8r48l8r56l8
- ___block_descriptor_96_e8_32s40s_e113_v104?0{CGRect={CGPoint=dd}{CGSize=dd}}8{CGRect={CGPoint=dd}{CGSize=dd}}40"NSTextContainer"72{_NSRange=QQ}80^B96ls32l8s40l8
- ___swift_closure_destructor.155Tm
- ___swift_closure_destructor.206Tm
- ___swift_closure_destructor.248Tm
- ___swift_closure_destructor.254Tm
- ___swift_closure_destructor.393Tm
- ___swift_closure_destructor.79Tm
- __os_feature_enabled_impl
- _kICInternalSettingsDisableTextViewEmptyLastLineWorkaround
- _objc_msgSend$_isAnimatingScrollTest
- _objc_msgSend$addConstraintsForSafeAreaLayoutGuide:toContainer:
- _objc_msgSend$app_systemPaperInkPaletteButtonView:
- _objc_msgSend$attachmentContentSize
- _objc_msgSend$createTextViewUsingTextController:stylingTextUsingSeparateTextStorageForRendering:
- _objc_msgSend$currentSelectionContainsListOrFixedWidth
- _objc_msgSend$drawBlockQuoteAndCleanup:pendingBlockQuoteLevelToDraw:pendingBlockQuoteRectToDraw:ps:
- _objc_msgSend$drawBlockQuoteLayerInRectForTK2:blockQuoteLevel:isMonostyled:
- _objc_msgSend$ensureGlyphsForCharacterRange:
- _objc_msgSend$ensureLayoutForSurroundingPages
- _objc_msgSend$extraLineFragmentRect
- _objc_msgSend$finishedInit
- _objc_msgSend$glyphRangeForBoundingRectWithoutAdditionalLayout:inTextContainer:
- _objc_msgSend$hideOverlappingAttachmentViewsIfNecessary
- _objc_msgSend$ic_shouldEnableBlockQuoteForAttachmentsOnlySelection
- _objc_msgSend$ic_view
- _objc_msgSend$icaxTodoButtonForParagraphStyle:
- _objc_msgSend$inlineAttachmentChangeController
- _objc_msgSend$invalidateLayoutAfterAttachmentViewTypeChangeIfNecessary
- _objc_msgSend$isTextDragActive
- _objc_msgSend$needsHideOverlappingAttachmentViews
- _objc_msgSend$performAnimatedSortForTrackedParagraphs:expandedRange:textView:sortChecklistsBlock:
- _objc_msgSend$ppt_inkPickerDidShow
- _objc_msgSend$predicateForVisibleNotesIncludingTrash:includingSystemPaper:includingMathNotes:includingCallNotes:inContext:
- _objc_msgSend$previousContentSize
- _objc_msgSend$restoreAttributedString:
- _objc_msgSend$scrollView:didChangeContentOffset:
- _objc_msgSend$setAttributionSidebarWidth:isGestureActive:animated:currentVelocity:
- _objc_msgSend$setExtraLineFragmentRect:usedRect:textContainer:
- _objc_msgSend$setIsSettingLinkTextAttributes:
- _objc_msgSend$setNavigationItemConfiguration:
- _objc_msgSend$setNeedsHideOverlappingAttachmentViews:
- _objc_msgSend$setPreviousContentSize:
- _objc_msgSend$setShouldIgnoreCachedOriginUpdates:
- _objc_msgSend$setShouldOverscrollScrollState:
- _objc_msgSend$setTextController:
- _objc_msgSend$setWasWindowlessDuringTransitionToSize:
- _objc_msgSend$shouldOverscrollScrollState
- _objc_msgSend$shouldUpdateVisibleSupplementalViewsInLayoutSubviews
- _objc_msgSend$styleSelector:presentViewController:animated:completion:
- _objc_msgSend$styleSelectorInputViewShowing
- _objc_msgSend$todoButtonForTrackedParagraphIfExists:
- _objc_msgSend$updateAttachmentsSelectionStateInTextStorage:forSelectedRanges:layoutManager:textView:
- _objc_msgSend$updateBlockQuoteLayerForParagraphStyle:inRange:ioPreviousBlockQuoteRect:
- _objc_msgSend$updateInlineDrawingViews
- _objc_msgSend$viewForBaseTextAttachmentNoCreate:
- _objc_msgSend$wasWindowlessDuringTransitionToSize
CStrings:
+ "-[ICNoteEditorDocumentScanController documentCameraPresentingViewController:didFinishWithInfoCollection:imageCache:warnUser:closeViewController:]"
+ "<%@: %p; isEditingNewNote=%d; isSettingEditing=%d; isTogglingLock=%d; isSelecting=%d; isSettingSelection=%d; isPerformingDeleteAnimation=%d; isPreviewingAttachmentFromNote=%d; isInLiveWindowResize=%d; isAddingImageAttachment=%d; isConvertToTag=%d; suspendBarButtonUpdates=%d; suspendSelectedRangeUpdates=%d; suspendTapGestureRecognizer=%d; isShowingIndentationItems=%d; isShowingChecklistItems=%d>"
+ "Cannot add summary to note because no transcript is available {attachment: %s}"
+ "Cannot add summary to note because the attachment has no managed object context {attachment: %s}"
+ "Cannot add summary to note because the note is not editable {attachment: %s}"
+ "Could not transcribe audio before summarizing {attachment: %s, error: %@}"
+ "Edit Link (Link Editor header)"
+ "ICAllowNotificationsViewController"
+ "NotesEditor/LinkEditorViewController_iOS.swift"
- "((textContainer.layoutManager) != nil)"
- "((textContainer.layoutManager.textStorage) != nil)"
- "-[ICNoteEditorViewController documentCameraPresentingViewController:didFinishWithInfoCollection:imageCache:warnUser:closeViewController:]"
- "-[ICTextFindingResult framesForHighlightInTextView:]"
- "DisableInitialCursorSizeWorkaround"
- "Disabling animation for checklist sort of %d items"
- "ICAllowNotificationsWarmingSheet"
- "NotesEditor/LinkEditorViewController.swift"
- "Trying to find a transition view for %@, but the note editor's layout manager isn't an %@"
- "UIKit"
- "Unsupported use of TextKit1."
- "keyboard_oop"
- "textContainer.layoutManager"
- "textContainer.layoutManager.textStorage"
- "textViewController.attributionSidebarView.visibleWidth"
- "\x82Q\x81\x81\xf0\xf01\xf01"
```
