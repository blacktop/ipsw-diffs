## PDFKit

> `/System/Library/Frameworks/PDFKit.framework/PDFKit`

```diff

-1451.5.3.0.0
-  __TEXT.__text: 0xc2078
-  __TEXT.__auth_stubs: 0x2bf0
-  __TEXT.__objc_methlist: 0xaa34
+1527.0.0.0.0
+  __TEXT.__text: 0xba9d4
+  __TEXT.__objc_methlist: 0xaffc
   __TEXT.__const: 0x964
-  __TEXT.__cstring: 0x7244
-  __TEXT.__gcc_except_tab: 0x3a88
+  __TEXT.__cstring: 0x76c4
+  __TEXT.__gcc_except_tab: 0x40ac
   __TEXT.__dlopen_cstrs: 0x201
   __TEXT.__ustring: 0xb4
   __TEXT.__oslogstring: 0x1a

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x31e0
-  __TEXT.__eh_frame: 0xf0
-  __TEXT.__objc_classname: 0x1165
-  __TEXT.__objc_methname: 0x1967e
-  __TEXT.__objc_methtype: 0x6b5d
-  __TEXT.__objc_stubs: 0x15340
-  __DATA_CONST.__got: 0xa90
-  __DATA_CONST.__const: 0x20a0
-  __DATA_CONST.__objc_classlist: 0x458
-  __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x168
+  __TEXT.__unwind_info: 0x32d8
+  __TEXT.__eh_frame: 0x128
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x2280
+  __DATA_CONST.__objc_classlist: 0x408
+  __DATA_CONST.__objc_catlist: 0x38
+  __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d88
-  __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x298
-  __DATA_CONST.__objc_arraydata: 0x158
-  __AUTH_CONST.__auth_got: 0x1610
+  __DATA_CONST.__weak_got: 0x8
+  __DATA_CONST.__objc_selrefs: 0x70e0
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0x2b0
+  __DATA_CONST.__objc_arraydata: 0xe8
+  __DATA_CONST.__got: 0xa58
   __AUTH_CONST.__const: 0x9d8
-  __AUTH_CONST.__cfstring: 0x7d00
-  __AUTH_CONST.__objc_const: 0xf268
+  __AUTH_CONST.__cfstring: 0x7720
+  __AUTH_CONST.__objc_const: 0xf070
+  __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__objc_intobj: 0x330
-  __AUTH_CONST.__objc_dictobj: 0x168
+  __AUTH_CONST.__objc_intobj: 0x2e8
+  __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0xe0
-  __AUTH.__objc_data: 0x28f0
+  __AUTH_CONST.__auth_got: 0x1758
+  __AUTH.__objc_data: 0x25d0
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0xcd8
-  __DATA.__data: 0x1190
-  __DATA.__bss: 0x7a0
+  __DATA.__objc_ivar: 0xc6c
+  __DATA.__data: 0x13c8
+  __DATA.__bss: 0x870
   __DATA_DIRTY.__objc_data: 0x230
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5006F7CC-D5BC-3D96-98FE-6DB50E907CF1
-  Functions: 3685
-  Symbols:   13941
-  CStrings:  7553
+  UUID: F09862B0-111B-3E74-97E0-69CDCED9E49E
+  Functions: 3742
+  Symbols:   14103
+  CStrings:  2185
 
Symbols:
+ +[PDFAKAnnotationSerializationHelper _computeIdentityHashForCGPDFDictionary:]
+ +[PDFAKAnnotationSerializationHelper _identityHashMatchesForDictionary:]
+ +[PDFAKAnnotationSerializationHelper addAKAnnotation:toCGPDFAnnotationDictionary:]
+ +[PDFCGPDFUtilities CGPDFObjectFromValue:]
+ +[PDFCGPDFUtilities CGPDFStringFromDate:]
+ +[PDFCGPDFUtilities _createCGPDFObjectFromValue:visitedNodes:]
+ +[PDFCGPDFUtilities cgNameStringFromPDFNameString:]
+ +[PDFCGPDFUtilities cgNameStringFromPDFNameString:].cold.1
+ +[PDFCGPDFUtilities dictionaryFromCGPDFDictionary:]
+ +[PDFTextInputView selectionForTextRange:pdfView:]
+ +[UIGestureRecognizer(Blocks) recognizerWithActionBlock:]
+ -[PDFAnnotation _setDictionaryValue:forKey:]
+ -[PDFAnnotation addAKAnnotationToCGPDFDictionary:]
+ -[PDFAnnotation allowsLossyImageCompression]
+ -[PDFAnnotation ensureCGPDFAnnotation]
+ -[PDFAnnotation registerAsDirtyForChangeOfKey:]
+ -[PDFAnnotation registerAsDirtyForChangeOfKey:].cold.1
+ -[PDFAnnotation updateAppearanceStream]
+ -[PDFAnnotationManager .cxx_destruct]
+ -[PDFAnnotationManager _activateAKAnnotation:]
+ -[PDFAnnotationManager _activateAnnotationInternal:]
+ -[PDFAnnotationManager _activatePDFKitAnnotation:]
+ -[PDFAnnotationManager _addControlForAnnotation:]
+ -[PDFAnnotationManager _clearIncompatibleSelection:]
+ -[PDFAnnotationManager _configureAnnotationForPromotion:]
+ -[PDFAnnotationManager _deactivateAnnotationInternal:]
+ -[PDFAnnotationManager _findNextActivatableAnnotationFromPage:fromAnnotation:direction:withCompletion:]
+ -[PDFAnnotationManager _findNextActivatableAnnotationOnPage:fromAnnotation:direction:]
+ -[PDFAnnotationManager _handleButtonHit:]
+ -[PDFAnnotationManager _handleLinkAnnotation:atLocation:]
+ -[PDFAnnotationManager _handleMarkupAnnotation:atLocation:]
+ -[PDFAnnotationManager _handleWidgetAnnotation:]
+ -[PDFAnnotationManager _hideActiveMenus]
+ -[PDFAnnotationManager _pageViewForAnnotation:]
+ -[PDFAnnotationManager _postActiveAnnotationChangedNotification]
+ -[PDFAnnotationManager _postAnnotationHitNotification:]
+ -[PDFAnnotationManager _postAnnotationWillHitNotification:]
+ -[PDFAnnotationManager _removeControlForAnnotation:]
+ -[PDFAnnotationManager _scrollToAnnotation:]
+ -[PDFAnnotationManager _setButtonState:forAnnotation:]
+ -[PDFAnnotationManager _showMenuForMarkupAnnotation:]
+ -[PDFAnnotationManager _undoRadioButtonChange:withState:formValue:]
+ -[PDFAnnotationManager activateAnnotation:]
+ -[PDFAnnotationManager activateNextAnnotationInDirection:completion:]
+ -[PDFAnnotationManager activeAnnotation]
+ -[PDFAnnotationManager activeControls]
+ -[PDFAnnotationManager deactivateAnnotation:]
+ -[PDFAnnotationManager deactivateCurrentAnnotation]
+ -[PDFAnnotationManager dealloc]
+ -[PDFAnnotationManager documentDidChange:]
+ -[PDFAnnotationManager handleInteractionWithAnnotation:atLocation:]
+ -[PDFAnnotationManager handleLongPressOnAnnotation:state:location:]
+ -[PDFAnnotationManager initWithPDFView:]
+ -[PDFAnnotationManager isFindingNextAnnotation]
+ -[PDFAnnotationManager pdfView]
+ -[PDFAnnotationManager prepareForDeallocation]
+ -[PDFAnnotationManager promoteAllDetectedAnnotationsOnPage:]
+ -[PDFAnnotationManager promoteAnnotations:onPage:]
+ -[PDFAnnotationManager setActiveAnnotation:]
+ -[PDFAnnotationManager setActiveControls:]
+ -[PDFAnnotationManager setIsFindingNextAnnotation:]
+ -[PDFAnnotationManager setPdfView:]
+ -[PDFChoiceWidgetComboBoxAdapter .cxx_destruct]
+ -[PDFChoiceWidgetComboBoxAdapter annotationChanged:]
+ -[PDFChoiceWidgetComboBoxAdapter annotation]
+ -[PDFChoiceWidgetComboBoxAdapter choices]
+ -[PDFChoiceWidgetComboBoxAdapter comboBox]
+ -[PDFChoiceWidgetComboBoxAdapter dealloc]
+ -[PDFChoiceWidgetComboBoxAdapter dismissalHandler]
+ -[PDFChoiceWidgetComboBoxAdapter initWithAnnotation:comboBoxControl:]
+ -[PDFChoiceWidgetComboBoxAdapter numberOfComponentsInPickerView:]
+ -[PDFChoiceWidgetComboBoxAdapter pickerView:didSelectRow:inComponent:]
+ -[PDFChoiceWidgetComboBoxAdapter pickerView:numberOfRowsInComponent:]
+ -[PDFChoiceWidgetComboBoxAdapter pickerView:titleForRow:forComponent:]
+ -[PDFChoiceWidgetComboBoxAdapter selectionHandler]
+ -[PDFChoiceWidgetComboBoxAdapter setChoices:]
+ -[PDFChoiceWidgetComboBoxAdapter setDismissalHandler:]
+ -[PDFChoiceWidgetComboBoxAdapter setSelectionHandler:]
+ -[PDFChoiceWidgetComboBoxAdapter textField]
+ -[PDFChoiceWidgetComboBoxAdapter updateAnnotationWithStringValue:]
+ -[PDFChoiceWidgetListBoxAdapter .cxx_destruct]
+ -[PDFChoiceWidgetListBoxAdapter annotationChanged:]
+ -[PDFChoiceWidgetListBoxAdapter annotation]
+ -[PDFChoiceWidgetListBoxAdapter choices]
+ -[PDFChoiceWidgetListBoxAdapter dealloc]
+ -[PDFChoiceWidgetListBoxAdapter initWithAnnotation:tableView:]
+ -[PDFChoiceWidgetListBoxAdapter numberOfSectionsInTableView:]
+ -[PDFChoiceWidgetListBoxAdapter selectionHandler]
+ -[PDFChoiceWidgetListBoxAdapter setChoices:]
+ -[PDFChoiceWidgetListBoxAdapter setSelectionHandler:]
+ -[PDFChoiceWidgetListBoxAdapter tableView:cellForRowAtIndexPath:]
+ -[PDFChoiceWidgetListBoxAdapter tableView:didSelectRowAtIndexPath:]
+ -[PDFChoiceWidgetListBoxAdapter tableView:numberOfRowsInSection:]
+ -[PDFChoiceWidgetListBoxAdapter tableView]
+ -[PDFChoiceWidgetListBoxAdapter updateAnnotationWithStringValue:]
+ -[PDFDocument _processDirtyAnnots]
+ -[PDFDocument _shouldGenerateAppearanceForAnnotation:]
+ -[PDFDocument canSaveWithMutablePDFUsingOptions:]
+ -[PDFDocument flushPendingAKAnnotationData]
+ -[PDFDocument flushPendingAppearanceUpdates]
+ -[PDFDocument registerDirtyAnnotation:]
+ -[PDFDocumentViewController _convertPoint:fromPage:inPDFPageViewController:]
+ -[PDFDocumentViewController _convertPoint:toPage:inPDFPageViewController:]
+ -[PDFDocumentViewController _distanceFromPoint:toPageView:]
+ -[PDFDocumentViewController _enforceAutoScaleFactorIfNeeded]
+ -[PDFDocumentViewController _point:isInPage:]
+ -[PDFDocumentViewController _updateBackgroundImageOfPage:inPageViewController:isSecondPage:]
+ -[PDFDocumentViewController _updatePageImageAtIndex:isSecondPage:inPageViewController:]
+ -[PDFDocumentViewController activePageView]
+ -[PDFDocumentViewController clearAllDecoratedFoundText]
+ -[PDFDocumentViewController compareFoundRange:toRange:inDocument:]
+ -[PDFDocumentViewController decorateFoundTextRange:inDocument:usingStyle:]
+ -[PDFDocumentViewController facingPage]
+ -[PDFDocumentViewController findPageViewControllerForPage:]
+ -[PDFDocumentViewController forceDimmingViewVisible]
+ -[PDFDocumentViewController foundRangesForPage:]
+ -[PDFDocumentViewController highlightedFoundRange]
+ -[PDFDocumentViewController pageViewControllers]
+ -[PDFDocumentViewController pdfViewSafeAreaInsetsDidChange]
+ -[PDFDocumentViewController performTextSearchWithQueryString:usingOptions:resultAggregator:]
+ -[PDFDocumentViewController selectedTextRange]
+ -[PDFKitPopupContentView .cxx_destruct]
+ -[PDFKitPopupContentView initWithAnnotation:initialContents:]
+ -[PDFKitPopupContentView setupViewsWithAnnotation:initialContents:]
+ -[PDFKitPopupContentView textView]
+ -[PDFKitPopupViewController .cxx_destruct]
+ -[PDFKitPopupViewController _handlePopupClose]
+ -[PDFKitPopupViewController _positioningRectInPageView]
+ -[PDFKitPopupViewController _updateParentContents]
+ -[PDFKitPopupViewController cancelled]
+ -[PDFKitPopupViewController contents]
+ -[PDFKitPopupViewController dismiss]
+ -[PDFKitPopupViewController doneButton:]
+ -[PDFKitPopupViewController initWithParentAnnotation:owningPageView:owningPDFView:positioningRect:]
+ -[PDFKitPopupViewController loadView]
+ -[PDFKitPopupViewController localUndoManager]
+ -[PDFKitPopupViewController originalPdfViewNextResponder]
+ -[PDFKitPopupViewController pageView]
+ -[PDFKitPopupViewController parentAnnotation]
+ -[PDFKitPopupViewController pdfView]
+ -[PDFKitPopupViewController popoverPresentationController:willRepositionPopoverToRect:inView:]
+ -[PDFKitPopupViewController popoverPresentationControllerDidDismissPopover:]
+ -[PDFKitPopupViewController popupContentView]
+ -[PDFKitPopupViewController popupPresentingViewController]
+ -[PDFKitPopupViewController positioningRect]
+ -[PDFKitPopupViewController prepareForPopoverPresentation:]
+ -[PDFKitPopupViewController present]
+ -[PDFKitPopupViewController savedFirstResponder]
+ -[PDFKitPopupViewController setCancelled:]
+ -[PDFKitPopupViewController setContents:]
+ -[PDFKitPopupViewController setLocalUndoManager:]
+ -[PDFKitPopupViewController setOriginalPdfViewNextResponder:]
+ -[PDFKitPopupViewController setPageView:]
+ -[PDFKitPopupViewController setParentAnnotation:]
+ -[PDFKitPopupViewController setPdfView:]
+ -[PDFKitPopupViewController setPopupContentView:]
+ -[PDFKitPopupViewController setPopupPresentingViewController:]
+ -[PDFKitPopupViewController setPositioningRect:]
+ -[PDFKitPopupViewController setSavedFirstResponder:]
+ -[PDFKitPopupViewController textViewDidChange:]
+ -[PDFKitPopupViewController textView]
+ -[PDFKitPopupViewController undoManager]
+ -[PDFKitPopupViewController viewDidAppear:]
+ -[PDFKitPopupViewController viewDidLoad]
+ -[PDFKitTextView annotationChanged:]
+ -[PDFKitTextView dealloc]
+ -[PDFOverlayViewsController pdfView:willAddPageViewController:]
+ -[PDFOverlayViewsController pdfView:willRemovePageViewController:]
+ -[PDFPage _setBounds:forBox:]
+ -[PDFPage addAnnotationsObserver:]
+ -[PDFPage appendXObject:]
+ -[PDFPage enumerateObserversRespondingToSelector:withBlock:]
+ -[PDFPage fetchPageLayoutWithCompletion:]
+ -[PDFPage pdfScannerResultAtPoint:onPageLayer:waitForScan:]
+ -[PDFPage removeAnnotationsObserver:]
+ -[PDFPageArrangementView hitTest:withEvent:]
+ -[PDFPageArrangementView initWithFrame:firstPageView:secondPageView:]
+ -[PDFPageLayer addPageDebugLayerEffect:]
+ -[PDFPageLayer removePageDebugLayerEffect:]
+ -[PDFPageLayerEffect pageLayer]
+ -[PDFPageLayerMarkupAnnotationEffect calculateLayerGeometryForQuad:markupType:bounds:position:angle:]
+ -[PDFPageView _annotationManager]
+ -[PDFPageView annotationController]
+ -[PDFPageView setStringValue:onChoiceWidgetAnnotation:]
+ -[PDFPageViewAnnotationController _addPDFAnnotationChoiceWidget:]
+ -[PDFPageViewAnnotationController _addPDFAnnotationSignatureWidget:]
+ -[PDFPageViewAnnotationController _addPDFAnnotationTextWidget:]
+ -[PDFPageViewAnnotationController _addPDFAnnotationViews]
+ -[PDFPageViewAnnotationController _addPopupForAnnotation:positioningRect:]
+ -[PDFPageViewAnnotationController _addViewForAnnotation:]
+ -[PDFPageViewAnnotationController _allowsFormFieldEntry]
+ -[PDFPageViewAnnotationController _calculateMarkerViewGeometryFromQuads:onLeft:frame:angle:]
+ -[PDFPageViewAnnotationController _createPopupMarkerForAnnotation:]
+ -[PDFPageViewAnnotationController _formChanged:]
+ -[PDFPageViewAnnotationController _removeViewForAnnotation:]
+ -[PDFPageViewAnnotationController _rotationTransformForPageView]
+ -[PDFPageViewAnnotationController _updateWidgetControl:forBounds:]
+ -[PDFPageViewAnnotationController activeControls]
+ -[PDFPageViewAnnotationController annotationViews]
+ -[PDFPageViewAnnotationController choiceWidgetComboBoxAdapter]
+ -[PDFPageViewAnnotationController choiceWidgetListBoxAdapter]
+ -[PDFPageViewAnnotationController createControlForAnnotation:]
+ -[PDFPageViewAnnotationController destroyControlForAnnotation:]
+ -[PDFPageViewAnnotationController formChangedObservation]
+ -[PDFPageViewAnnotationController page:didAddAnnotation:]
+ -[PDFPageViewAnnotationController page:didRemoveAnnotation:]
+ -[PDFPageViewAnnotationController pageView]
+ -[PDFPageViewAnnotationController page]
+ -[PDFPageViewAnnotationController pdfView]
+ -[PDFPageViewAnnotationController setActiveControls:]
+ -[PDFPageViewAnnotationController setAnnotationViews:]
+ -[PDFPageViewAnnotationController setChoiceWidgetComboBoxAdapter:]
+ -[PDFPageViewAnnotationController setChoiceWidgetListBoxAdapter:]
+ -[PDFPageViewAnnotationController setFormChangedObservation:]
+ -[PDFPageViewAnnotationController setPage:]
+ -[PDFPageViewAnnotationController setPageView:]
+ -[PDFPageViewAnnotationController setPdfView:]
+ -[PDFPageViewController _buildPDFPageViews]
+ -[PDFPageViewController _foundRangesForPages]
+ -[PDFPageViewController _pageFrameForPageInAutoScaleFactorCalculation:inPDFView:]
+ -[PDFPageViewController _updateAnnotationsForPage:pageView:]
+ -[PDFPageViewController _updatePageContainerViewSearchState]
+ -[PDFPageViewController pageViewForPage:]
+ -[PDFPageViewController pageViewsContainerView]
+ -[PDFPageViewController searchDelegate]
+ -[PDFPageViewController secondPDFPage]
+ -[PDFPageViewController secondPageView]
+ -[PDFPageViewController setSearchDelegate:]
+ -[PDFPageViewController setSecondBackgroundImage:atBackgroundQuality:]
+ -[PDFPageViewController setSecondPDFPage:]
+ -[PDFRenderingProperties fontAntiAliasingFlags]
+ -[PDFRenderingProperties setFontAntiAliasingFlags:]
+ -[PDFTableCellSelection isPointInHandle:whichHandle:hitRadius:]
+ -[PDFTextInputView canInteractAtPoint:]
+ -[PDFTextInputView disableDimmingViewAnimation]
+ -[PDFTextInputView forceDimmingViewVisible]
+ -[PDFTextInputView setDisableDimmingViewAnimation:]
+ -[PDFTextInputView setForceDimmingViewVisible:]
+ -[PDFTextInputView(SharedTextDataSource) _beginningOfDocument]
+ -[PDFTextInputView(SharedTextDataSource) _comparePosition:toPosition:]
+ -[PDFTextInputView(SharedTextDataSource) _endOfDocument]
+ -[PDFTextInputView(SharedTextDataSource) _offsetFromPosition:toPosition:]
+ -[PDFTextInputView(SharedTextDataSource) _positionFromPosition:inDirection:offset:]
+ -[PDFTextInputView(SharedTextDataSource) _positionFromPosition:offset:]
+ -[PDFTextInputView(SharedTextDataSource) _textRangeFromPosition:toPosition:]
+ -[PDFTextInputView(UITextInput) _allowAnimatedUpdateSelectionRectViews]
+ -[PDFTextInputView(UITextInput) _closestPositionToPoint:withinRange:]
+ -[PDFTextInputView(UITextInput) baseWritingDirectionForPosition:inDirection:]
+ -[PDFTextInputView(UITextInput) beginningOfDocument]
+ -[PDFTextInputView(UITextInput) caretRectForPosition:]
+ -[PDFTextInputView(UITextInput) characterRangeAtPoint:]
+ -[PDFTextInputView(UITextInput) characterRangeByExtendingPosition:inDirection:]
+ -[PDFTextInputView(UITextInput) closestPositionToPoint:]
+ -[PDFTextInputView(UITextInput) closestPositionToPoint:withinRange:]
+ -[PDFTextInputView(UITextInput) comparePosition:toPosition:]
+ -[PDFTextInputView(UITextInput) deleteBackward]
+ -[PDFTextInputView(UITextInput) editMenuForTextRange:suggestedActions:]
+ -[PDFTextInputView(UITextInput) endOfDocument]
+ -[PDFTextInputView(UITextInput) firstRectForRange:]
+ -[PDFTextInputView(UITextInput) hasText]
+ -[PDFTextInputView(UITextInput) inputDelegate]
+ -[PDFTextInputView(UITextInput) insertText:]
+ -[PDFTextInputView(UITextInput) isSecureTextEntry]
+ -[PDFTextInputView(UITextInput) markedTextRange]
+ -[PDFTextInputView(UITextInput) markedTextStyle]
+ -[PDFTextInputView(UITextInput) offsetFromPosition:toPosition:]
+ -[PDFTextInputView(UITextInput) positionFromPosition:inDirection:offset:]
+ -[PDFTextInputView(UITextInput) positionFromPosition:offset:]
+ -[PDFTextInputView(UITextInput) positionWithinRange:farthestInDirection:]
+ -[PDFTextInputView(UITextInput) replaceRange:withText:]
+ -[PDFTextInputView(UITextInput) selectionRectsForRange:]
+ -[PDFTextInputView(UITextInput) setBaseWritingDirection:forRange:]
+ -[PDFTextInputView(UITextInput) setInputDelegate:]
+ -[PDFTextInputView(UITextInput) setMarkedText:selectedRange:]
+ -[PDFTextInputView(UITextInput) setMarkedTextStyle:]
+ -[PDFTextInputView(UITextInput) setTokenizer:]
+ -[PDFTextInputView(UITextInput) textInRange:]
+ -[PDFTextInputView(UITextInput) textRangeFromPosition:toPosition:]
+ -[PDFTextInputView(UITextInput) tokenizer]
+ -[PDFTextInputView(UITextInput) unmarkText]
+ -[PDFTextInputView(UITextInteractionDelegate) interactionShouldBegin:atPoint:]
+ -[PDFTextInputView(UITextLinkInteraction) linkRegionsConstrainedToLineAtPoint:]
+ -[PDFTextInputView(UITextSearching) _setDimmingViewVisible:animated:]
+ -[PDFTextInputView(UITextSearching) _setupSearchHighlightView]
+ -[PDFTextInputView(UITextSearching) _targetedPreviewForRange:]
+ -[PDFTextInputView(UITextSearching) clearAllDecoratedFoundText]
+ -[PDFTextInputView(UITextSearching) compareFoundRange:toRange:inDocument:]
+ -[PDFTextInputView(UITextSearching) decorateFoundTextRange:inDocument:usingStyle:]
+ -[PDFTextInputView(UITextSearching) layoutSubviews]
+ -[PDFTextInputView(UITextSearching) performTextSearchWithQueryString:usingOptions:resultAggregator:]
+ -[PDFTextInputView(UITextSearching) updateSearchStateWithFoundRanges:highlightedRange:forceDimming:]
+ -[PDFTextPosition compare:]
+ -[PDFTextPosition hash]
+ -[PDFTextPosition isEqual:]
+ -[PDFView _activeScrollView]
+ -[PDFView _gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:]
+ -[PDFView _gestureRecognizer:shouldReceiveTouch:]
+ -[PDFView _gestureRecognizer:shouldReceiveTouch:event:]
+ -[PDFView _gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:]
+ -[PDFView _gestureRecognizer:shouldRequireFailureOfGestureRecognizer:]
+ -[PDFView _gestureRecognizerShouldBegin:]
+ -[PDFView _usingGestureRecognizers]
+ -[PDFView activateAnnotation:]
+ -[PDFView callPageViewControllerCreationDelegateMethod:]
+ -[PDFView callPageViewControllerRemovalDelegateMethod:]
+ -[PDFView deactivateAnnotation:]
+ -[PDFView drawPageLayout:]
+ -[PDFView pageViewControllerForPage:]
+ -[PDFView safeAreaInsetsDidChange]
+ -[PDFView updatePageLayout]
+ -[PDFView windowDidChangeScreen:]
+ -[PDFViewController annotationManager]
+ -[PDFViewController choiceWidgetComboBoxAdapter]
+ -[PDFViewController setAnnotationManager:]
+ -[PDFViewController setChoiceWidgetComboBoxAdapter:]
+ -[PDFViewController showMarkupStyleMenuForMarkupAnnotation:]
+ -[UIGestureRecognizer(Blocks) initWithActionBlock:]
+ -[UIView(ViewExtensions) PDFKitUserInterfaceLayoutDirection]
+ -[_GestureActionHandler .cxx_destruct]
+ -[_GestureActionHandler block]
+ -[_GestureActionHandler handleAction:]
+ -[_GestureActionHandler initWithBlock:]
+ -[_GestureActionHandler setBlock:]
+ GCC_except_table102
+ GCC_except_table104
+ GCC_except_table119
+ GCC_except_table121
+ GCC_except_table130
+ GCC_except_table145
+ GCC_except_table146
+ GCC_except_table158
+ GCC_except_table160
+ GCC_except_table171
+ GCC_except_table177
+ GCC_except_table179
+ GCC_except_table250
+ GCC_except_table327
+ GCC_except_table33
+ GCC_except_table333
+ GCC_except_table34
+ GCC_except_table45
+ GCC_except_table52
+ GCC_except_table68
+ GCC_except_table69
+ GCC_except_table73
+ GCC_except_table74
+ GCC_except_table78
+ GCC_except_table98
+ _CATransform3DMakeRotation
+ _CC_SHA256_Final
+ _CC_SHA256_Init
+ _CC_SHA256_Update
+ _CFAutorelease
+ _CFRunLoopGetCurrent
+ _CFRunLoopGetMain
+ _CFRunLoopPerformBlock
+ _CFRunLoopWakeUp
+ _CGPDFAnnotationCreateWithCGPDFDictionary
+ _CGPDFArrayAppendObject
+ _CGPDFArrayCreate
+ _CGPDFDictionaryContainsKey
+ _CGPDFDictionaryCreate
+ _CGPDFDictionaryCreateCopy
+ _CGPDFDictionaryRelease
+ _CGPDFDictionaryRemoveObject
+ _CGPDFDictionarySetObject
+ _CGPDFDocumentWriteToDataConsumer
+ _CGPDFObjectCreateWithArray
+ _CGPDFObjectCreateWithBoolean
+ _CGPDFObjectCreateWithDictionary
+ _CGPDFObjectCreateWithInteger
+ _CGPDFObjectCreateWithName
+ _CGPDFObjectCreateWithReal
+ _CGPDFObjectCreateWithString
+ _CGPDFObjectRelease
+ _CGPDFPageAddAnnotationAppearance
+ _CGPDFPageAppendXObject
+ _CGPDFPageCopyPageLayoutIfAvailable
+ _CGPDFPageInsertAnnotationAtIndex
+ _CGPDFStreamCreateWithBlock
+ _CGPDFStreamCreateWithDisplayList
+ _CGPDFStringCreateWithBytes
+ _CGPDFStringCreateWithCFString
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_NSRecursiveLock
+ _OBJC_CLASS_$_NSTextContentStorage
+ _OBJC_CLASS_$_NSTextLayoutManager
+ _OBJC_CLASS_$_NSUndoManager
+ _OBJC_CLASS_$_PDFAnnotationManager
+ _OBJC_CLASS_$_PDFChoiceWidgetComboBoxAdapter
+ _OBJC_CLASS_$_PDFChoiceWidgetListBoxAdapter
+ _OBJC_CLASS_$_PDFKitPopupContentView
+ _OBJC_CLASS_$_PDFKitPopupViewController
+ _OBJC_CLASS_$_PDFPageArrangementView
+ _OBJC_CLASS_$_UIGestureRecognizer
+ _OBJC_CLASS_$_UINavigationBarAppearance
+ _OBJC_CLASS_$__GestureActionHandler
+ _OBJC_IVAR_$_PDFAnnotation._allowsLossyImageCompression
+ _OBJC_IVAR_$_PDFAnnotation._cgAnnotationLock
+ _OBJC_IVAR_$_PDFAnnotation._initializingDictionary
+ _OBJC_IVAR_$_PDFAnnotationManager._activeAnnotation
+ _OBJC_IVAR_$_PDFAnnotationManager._activeControls
+ _OBJC_IVAR_$_PDFAnnotationManager._isFindingNextAnnotation
+ _OBJC_IVAR_$_PDFAnnotationManager._pdfView
+ _OBJC_IVAR_$_PDFChoiceWidgetComboBoxAdapter._annotation
+ _OBJC_IVAR_$_PDFChoiceWidgetComboBoxAdapter._choices
+ _OBJC_IVAR_$_PDFChoiceWidgetComboBoxAdapter._comboBox
+ _OBJC_IVAR_$_PDFChoiceWidgetComboBoxAdapter._dismissalHandler
+ _OBJC_IVAR_$_PDFChoiceWidgetComboBoxAdapter._selectionHandler
+ _OBJC_IVAR_$_PDFChoiceWidgetComboBoxAdapter._textField
+ _OBJC_IVAR_$_PDFChoiceWidgetListBoxAdapter._annotation
+ _OBJC_IVAR_$_PDFChoiceWidgetListBoxAdapter._choices
+ _OBJC_IVAR_$_PDFChoiceWidgetListBoxAdapter._selectionHandler
+ _OBJC_IVAR_$_PDFChoiceWidgetListBoxAdapter._tableView
+ _OBJC_IVAR_$_PDFDocument._dirtyAKAnnots
+ _OBJC_IVAR_$_PDFDocument._dirtyAnnots
+ _OBJC_IVAR_$_PDFDocument._dirtyAnnotsAccessLock
+ _OBJC_IVAR_$_PDFDocument._dirtyAnnotsCoalescingTimer
+ _OBJC_IVAR_$_PDFDocument._dirtyAnnotsWorkQueue
+ _OBJC_IVAR_$_PDFDocumentViewControllerPrivate.activeSearch
+ _OBJC_IVAR_$_PDFDocumentViewControllerPrivate.foundTextRangesByPageIndex
+ _OBJC_IVAR_$_PDFDocumentViewControllerPrivate.highlightedFoundRange
+ _OBJC_IVAR_$_PDFFormFieldPrivateVars.sourceDictionary
+ _OBJC_IVAR_$_PDFKitPopupContentView._textView
+ _OBJC_IVAR_$_PDFKitPopupViewController._cancelled
+ _OBJC_IVAR_$_PDFKitPopupViewController._contents
+ _OBJC_IVAR_$_PDFKitPopupViewController._localUndoManager
+ _OBJC_IVAR_$_PDFKitPopupViewController._originalPdfViewNextResponder
+ _OBJC_IVAR_$_PDFKitPopupViewController._pageView
+ _OBJC_IVAR_$_PDFKitPopupViewController._parentAnnotation
+ _OBJC_IVAR_$_PDFKitPopupViewController._pdfView
+ _OBJC_IVAR_$_PDFKitPopupViewController._popupContentView
+ _OBJC_IVAR_$_PDFKitPopupViewController._popupPresentingViewController
+ _OBJC_IVAR_$_PDFKitPopupViewController._positioningRect
+ _OBJC_IVAR_$_PDFKitPopupViewController._savedFirstResponder
+ _OBJC_IVAR_$_PDFPage._annotationsOnceToken
+ _OBJC_IVAR_$_PDFPage._privateObservers
+ _OBJC_IVAR_$_PDFPageLayer._debugEffectsLayer
+ _OBJC_IVAR_$_PDFPageLayer._debugPageLayerEffects
+ _OBJC_IVAR_$_PDFPageViewAnnotationController._activeControls
+ _OBJC_IVAR_$_PDFPageViewAnnotationController._annotationViews
+ _OBJC_IVAR_$_PDFPageViewAnnotationController._choiceWidgetComboBoxAdapter
+ _OBJC_IVAR_$_PDFPageViewAnnotationController._choiceWidgetListBoxAdapter
+ _OBJC_IVAR_$_PDFPageViewAnnotationController._formChangedObservation
+ _OBJC_IVAR_$_PDFPageViewAnnotationController._page
+ _OBJC_IVAR_$_PDFPageViewAnnotationController._pageView
+ _OBJC_IVAR_$_PDFPageViewAnnotationController._pdfView
+ _OBJC_IVAR_$_PDFPageViewController._searchDelegate
+ _OBJC_IVAR_$_PDFPageViewControllerPrivate.secondBackgroundImage
+ _OBJC_IVAR_$_PDFPageViewControllerPrivate.secondBackgroundImageQuality
+ _OBJC_IVAR_$_PDFPageViewControllerPrivate.secondPage
+ _OBJC_IVAR_$_PDFPageViewControllerPrivate.secondPageView
+ _OBJC_IVAR_$_PDFRenderingProperties._fontAntiAliasingFlags
+ _OBJC_IVAR_$_PDFScrollView._boundsUpdateTimer
+ _OBJC_IVAR_$_PDFScrollView._document
+ _OBJC_IVAR_$_PDFScrollView._documentView
+ _OBJC_IVAR_$_PDFScrollView._forcesTopAlignment
+ _OBJC_IVAR_$_PDFScrollView._isZooming
+ _OBJC_IVAR_$_PDFScrollView._oldBounds
+ _OBJC_IVAR_$_PDFScrollView._oldMagnification
+ _OBJC_IVAR_$_PDFScrollView._pageSyncDate
+ _OBJC_IVAR_$_PDFScrollView._pdfView
+ _OBJC_IVAR_$_PDFScrollView._scheduledPageSync
+ _OBJC_IVAR_$_PDFTextInputView._disableDimmingViewAnimation
+ _OBJC_IVAR_$_PDFTextInputView._forceDimmingViewVisible
+ _OBJC_IVAR_$_PDFViewController._annotationManager
+ _OBJC_IVAR_$_PDFViewController._choiceWidgetComboBoxAdapter
+ _OBJC_IVAR_$_PDFViewControllerPrivate.tableCellDragInitialEndPoint
+ _OBJC_IVAR_$_PDFViewControllerPrivate.tableCellDragIsHandleDrag
+ _OBJC_IVAR_$_PDFViewControllerPrivate.tableCellDragPassedHysteresisX
+ _OBJC_IVAR_$_PDFViewControllerPrivate.tableCellDragPassedHysteresisY
+ _OBJC_IVAR_$_PDFViewControllerPrivate.tableCellDragStartPage
+ _OBJC_IVAR_$_PDFViewControllerPrivate.tableCellDragStartPoint
+ _OBJC_IVAR_$_PDFViewControllerPrivate.tableCellGestureIsTouch
+ _OBJC_IVAR_$__GestureActionHandler._block
+ _OBJC_METACLASS_$_PDFAnnotationManager
+ _OBJC_METACLASS_$_PDFChoiceWidgetComboBoxAdapter
+ _OBJC_METACLASS_$_PDFChoiceWidgetListBoxAdapter
+ _OBJC_METACLASS_$_PDFKitPopupContentView
+ _OBJC_METACLASS_$_PDFKitPopupViewController
+ _OBJC_METACLASS_$_PDFPageArrangementView
+ _OBJC_METACLASS_$_UIStackView
+ _OBJC_METACLASS_$__GestureActionHandler
+ _PDFAnnotationChangedAnnotationKeyUserInfoKey
+ _PDFAnnotationDidSetValueForAnnotationKey
+ _PDFCGVectorFromPoints
+ _PDFKitGestureNameAnnotationLongPress
+ _PDFKitGestureNameAnnotationPan
+ _PDFKitGestureNameAnnotationPopupTap
+ _PDFKitGestureNameAnnotationPress
+ _PDFKitGestureNameAnnotationTap
+ _PDFKitGestureNameDeepPress
+ _PDFKitGestureNameFormFillingDoubleTap
+ _PDFKitGestureNameScannerResult
+ _PDFKitGestureNameTableCellDrag
+ _PDFKitGestureNameTableCellTap
+ _PDFKitGestureNameTouchPageSwipe
+ _UIFontTextStyleBody
+ __OBJC_$_CATEGORY_CLASS_METHODS_UIGestureRecognizer_$_Blocks
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UIGestureRecognizer_$_Blocks
+ __OBJC_$_CATEGORY_UIGestureRecognizer_$_Blocks
+ __OBJC_$_CLASS_METHODS_PDFCGPDFUtilities
+ __OBJC_$_CLASS_METHODS_PDFTextInputView
+ __OBJC_$_INSTANCE_METHODS_PDFAnnotationManager
+ __OBJC_$_INSTANCE_METHODS_PDFChoiceWidgetComboBoxAdapter
+ __OBJC_$_INSTANCE_METHODS_PDFChoiceWidgetListBoxAdapter
+ __OBJC_$_INSTANCE_METHODS_PDFKitPopupContentView
+ __OBJC_$_INSTANCE_METHODS_PDFKitPopupViewController
+ __OBJC_$_INSTANCE_METHODS_PDFPageArrangementView
+ __OBJC_$_INSTANCE_METHODS_PDFTextInputView(SharedTextDataSource|UITextInteractionDelegate|UITextInput|UITextLinkInteraction|UITextSearching)
+ __OBJC_$_INSTANCE_METHODS__GestureActionHandler
+ __OBJC_$_INSTANCE_VARIABLES_PDFAnnotationManager
+ __OBJC_$_INSTANCE_VARIABLES_PDFChoiceWidgetComboBoxAdapter
+ __OBJC_$_INSTANCE_VARIABLES_PDFChoiceWidgetListBoxAdapter
+ __OBJC_$_INSTANCE_VARIABLES_PDFKitPopupContentView
+ __OBJC_$_INSTANCE_VARIABLES_PDFKitPopupViewController
+ __OBJC_$_INSTANCE_VARIABLES__GestureActionHandler
+ __OBJC_$_PROP_LIST_PDFAnnotationManager
+ __OBJC_$_PROP_LIST_PDFChoiceWidgetComboBoxAdapter
+ __OBJC_$_PROP_LIST_PDFChoiceWidgetListBoxAdapter
+ __OBJC_$_PROP_LIST_PDFKitPopupContentView
+ __OBJC_$_PROP_LIST_PDFKitPopupViewController
+ __OBJC_$_PROP_LIST_PDFPageViewAnnotationController
+ __OBJC_$_PROP_LIST_PDFTextRange
+ __OBJC_$_PROP_LIST__GestureActionHandler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PDFPageObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIAdaptivePresentationControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIPickerViewDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIPopoverPresentationControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UITableViewDataSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UITableViewDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PDFPageLayerDebugEffectManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UIPickerViewDataSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UITableViewDataSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PDFPageLayerDebugEffectManager
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PDFPageObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIAdaptivePresentationControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIPickerViewDataSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIPickerViewDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIPopoverPresentationControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UITableViewDataSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UITableViewDelegate
+ __OBJC_$_PROTOCOL_REFS_PDFPageLayerDebugEffectManager
+ __OBJC_$_PROTOCOL_REFS_PDFPageObserver
+ __OBJC_$_PROTOCOL_REFS_UIAdaptivePresentationControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_UIPickerViewDataSource
+ __OBJC_$_PROTOCOL_REFS_UIPickerViewDelegate
+ __OBJC_$_PROTOCOL_REFS_UIPopoverPresentationControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_UITableViewDataSource
+ __OBJC_$_PROTOCOL_REFS_UITableViewDelegate
+ __OBJC_CLASS_PROTOCOLS_$_PDFChoiceWidgetComboBoxAdapter
+ __OBJC_CLASS_PROTOCOLS_$_PDFChoiceWidgetListBoxAdapter
+ __OBJC_CLASS_PROTOCOLS_$_PDFKitPopupViewController
+ __OBJC_CLASS_PROTOCOLS_$_PDFPageViewAnnotationController
+ __OBJC_CLASS_PROTOCOLS_$_PDFTextInputView(SharedTextDataSource|UITextInteractionDelegate|UITextInput|UITextLinkInteraction|UITextSearching)
+ __OBJC_CLASS_RO_$_PDFAnnotationManager
+ __OBJC_CLASS_RO_$_PDFChoiceWidgetComboBoxAdapter
+ __OBJC_CLASS_RO_$_PDFChoiceWidgetListBoxAdapter
+ __OBJC_CLASS_RO_$_PDFKitPopupContentView
+ __OBJC_CLASS_RO_$_PDFKitPopupViewController
+ __OBJC_CLASS_RO_$_PDFPageArrangementView
+ __OBJC_CLASS_RO_$__GestureActionHandler
+ __OBJC_LABEL_PROTOCOL_$_PDFPageLayerDebugEffectManager
+ __OBJC_LABEL_PROTOCOL_$_PDFPageObserver
+ __OBJC_LABEL_PROTOCOL_$_UIAdaptivePresentationControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_UIPickerViewDataSource
+ __OBJC_LABEL_PROTOCOL_$_UIPickerViewDelegate
+ __OBJC_LABEL_PROTOCOL_$_UIPopoverPresentationControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_UITableViewDataSource
+ __OBJC_LABEL_PROTOCOL_$_UITableViewDelegate
+ __OBJC_METACLASS_RO_$_PDFAnnotationManager
+ __OBJC_METACLASS_RO_$_PDFChoiceWidgetComboBoxAdapter
+ __OBJC_METACLASS_RO_$_PDFChoiceWidgetListBoxAdapter
+ __OBJC_METACLASS_RO_$_PDFKitPopupContentView
+ __OBJC_METACLASS_RO_$_PDFKitPopupViewController
+ __OBJC_METACLASS_RO_$_PDFPageArrangementView
+ __OBJC_METACLASS_RO_$__GestureActionHandler
+ __OBJC_PROTOCOL_$_PDFPageLayerDebugEffectManager
+ __OBJC_PROTOCOL_$_PDFPageObserver
+ __OBJC_PROTOCOL_$_UIAdaptivePresentationControllerDelegate
+ __OBJC_PROTOCOL_$_UIPickerViewDataSource
+ __OBJC_PROTOCOL_$_UIPickerViewDelegate
+ __OBJC_PROTOCOL_$_UIPopoverPresentationControllerDelegate
+ __OBJC_PROTOCOL_$_UITableViewDataSource
+ __OBJC_PROTOCOL_$_UITableViewDelegate
+ __ZN10applesauce2CF9ObjectRefIP11CGPDFStreamED2Ev
+ __ZN10applesauce2CF9ObjectRefIP11CGPDFStringED2Ev
+ __ZN10applesauce2CF9ObjectRefIP12CGColorSpaceED2Ev
+ __ZNKSt3__111__copy_implclB9foe220100IPU8__strongP20PDFDetectedFormFieldS5_S5_Li0EEENS_4pairIT_T1_EES7_T0_S8_
+ __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB9foe220100IP18PDFDetectedFormRowS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
+ __ZNKSt3__120__move_backward_implINS_17_ClassicAlgPolicyEEclB9foe220100IP18PDFDetectedFormRowS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI18PDFDetectedFormRowEEPS2_EclB9foe220100Ev
+ __ZNKSt9type_infoeqB9foe220100ERKS_
+ __ZNSt12length_errorC1B9foe220100EPKc
+ __ZNSt3__110__function12__value_funcIFvP12CGPDFScannerEEC2B9foe220100EOS5_
+ __ZNSt3__110__function12__value_funcIFvP12CGPDFScannerEED2B9foe220100Ev
+ __ZNSt3__110unique_ptrI12CGPDFScannerNS_8functionIFvPS1_EEEE5resetB9foe220100ES3_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIdN10applesauce2CF9ObjectRefIPK8__CTFontEEEEPvEENS_22__tree_node_destructorINS_9allocatorISC_EEEEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIdU8__strongP13PDFAnnotationEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrINS_11__tree_nodeImPvEENS_6__treeImNS_4lessImEENS_9allocatorImEEE14__tree_deleterEE5resetB9foe220100EPS3_
+ __ZNSt3__112__destroy_atB9foe220100INS_4pairIKdN10applesauce2CF9ObjectRefIPK8__CTFontEEEEEEvPT_
+ __ZNSt3__114__split_bufferI18PDFDetectedFormRowRNS_9allocatorIS1_EEE5clearB9foe220100Ev
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorI14ParsedWordDataEENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorI18PDFDetectedFormRowEENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorI6CGRectEENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorIPK18CGDisplayListEntryEENS_16allocator_traitsIS5_EEEENS_19__allocation_resultINT0_7pointerENS9_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorIU8__strongP20PDFDetectedFormFieldEENS_16allocator_traitsIS5_EEEENS_19__allocation_resultINT0_7pointerENS9_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorIdEENS_16allocator_traitsIS2_EEEENS_19__allocation_resultINT0_7pointerENS6_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorImEENS_16allocator_traitsIS2_EEEENS_19__allocation_resultINT0_7pointerENS6_9size_typeEEERT_m
+ __ZNSt3__120__throw_length_errorB9foe220100EPKc
+ __ZNSt3__123__lower_bound_bisectingB9foe220100INS_17_ClassicAlgPolicyENS_11__wrap_iterIPU8__strongP20PDFDetectedFormFieldEES5_NS_10__identityEZN18PDFDetectedFormRow11insertFieldES4_EUlS4_S4_E_EET0_SB_RKT1_NS_15iterator_traitsISB_E15difference_typeERT3_RT2_
+ __ZNSt3__125__throw_bad_function_callB9foe220100Ev
+ __ZNSt3__127__tree_balance_after_insertB9foe220100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI18PDFDetectedFormRowEEPS3_EEED2B9foe220100Ev
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__134__uninitialized_allocator_relocateB9foe220100INS_9allocatorI18PDFDetectedFormRowEEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__13mapIdN10applesauce2CF9ObjectRefIPK8__CTFontEENS_4lessIdEENS_9allocatorINS_4pairIKdS7_EEEEE7emplaceB9foe220100IJRdRS7_EEENSB_INS_14__map_iteratorINS_15__tree_iteratorINS_12__value_typeIdS7_EEPNS_11__tree_nodeISM_PvEElEEEEbEEDpOT_
+ __ZNSt3__13mapIdU8__strongP13PDFAnnotationNS_4lessIdEENS_9allocatorINS_4pairIKdS3_EEEEEixERS8_
+ __ZNSt3__13setIdNS_4lessIdEENS_9allocatorIdEEE6insertB9foe220100ERKd
+ __ZNSt3__13setImNS_4lessImEENS_9allocatorImEEE6insertB9foe220100EOm
+ __ZNSt3__13setImNS_4lessImEENS_9allocatorImEEE6insertB9foe220100ERKm
+ __ZNSt3__14pairIKdN10applesauce2CF9ObjectRefIPK8__CTFontEEEC2B9foe220100IRdRS8_Li0EEEOT_OT0_
+ __ZNSt3__16__treeINS_12__value_typeIdN10applesauce2CF9ObjectRefIPK8__CTFontEEEENS_19__map_value_compareIdNS_4pairIKdS8_EENS_4lessIdEEEENS_9allocatorISD_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS9_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIdN10applesauce2CF9ObjectRefIPK8__CTFontEEEENS_19__map_value_compareIdNS_4pairIKdS8_EENS_4lessIdEEEENS_9allocatorISD_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSO_SO_
+ __ZNSt3__16__treeINS_12__value_typeIdN10applesauce2CF9ObjectRefIPK8__CTFontEEEENS_19__map_value_compareIdNS_4pairIKdS8_EENS_4lessIdEEEENS_9allocatorISD_EEE7destroyEPNS_11__tree_nodeIS9_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIdU8__strongP13PDFAnnotationEENS_19__map_value_compareIdNS_4pairIKdS4_EENS_4lessIdEEEENS_9allocatorIS9_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS5_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIdU8__strongP13PDFAnnotationEENS_19__map_value_compareIdNS_4pairIKdS4_EENS_4lessIdEEEENS_9allocatorIS9_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSK_SK_
+ __ZNSt3__16__treeINS_12__value_typeIdU8__strongP13PDFAnnotationEENS_19__map_value_compareIdNS_4pairIKdS4_EENS_4lessIdEEEENS_9allocatorIS9_EEE7destroyEPNS_11__tree_nodeIS5_PvEE
+ __ZNSt3__16__treeIdNS_4lessIdEENS_9allocatorIdEEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIdPvEE
+ __ZNSt3__16__treeImNS_4lessImEENS_9allocatorImEEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeImPvEE
+ __ZNSt3__16__treeImNS_4lessImEENS_9allocatorImEEE21__construct_from_treeB9foe220100IZNS5_21__copy_construct_treeB9foe220100EPNS_11__tree_nodeImPvEEEUlRKmE_EESA_SA_T_
+ __ZNSt3__16__treeImNS_4lessImEENS_9allocatorImEEEC2ERKS5_
+ __ZNSt3__16vectorI14ParsedWordDataNS_9allocatorIS1_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorI14ParsedWordDataNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI14ParsedWordDataNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRU8__strongP8NSStringRdSA_SA_SA_SA_RbR13PDFQuadPointsEEEPS1_DpOT_
+ __ZNSt3__16vectorI18PDFDetectedFormRowNS_9allocatorIS1_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorI18PDFDetectedFormRowNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI18PDFDetectedFormRowNS_9allocatorIS1_EEE30__emplace_back_assume_capacityB9foe220100IJS1_EEEvDpOT_
+ __ZNSt3__16vectorI6CGRectNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIPK18CGDisplayListEntryNS_9allocatorIS3_EEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorIPK18CGDisplayListEntryNS_9allocatorIS3_EEE16__init_with_sizeB9foe220100IPS3_S8_EEvT_T0_m
+ __ZNSt3__16vectorIPK18CGDisplayListEntryNS_9allocatorIS3_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIPK18CGDisplayListEntryNS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE16__init_with_sizeB9foe220100IPS3_S8_EEvT_T0_m
+ __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE18__assign_with_sizeB9foe220100INS_17_ClassicAlgPolicyEPS3_S9_EEvT0_T1_l
+ __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE24__emplace_back_slow_pathIJdEEEPdDpOT_
+ __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__19__advanceB9foe220100INS_21__tree_const_iteratorIdPNS_11__tree_nodeIdPvEElEEEEvRT_NS_15iterator_traitsIS7_E15difference_typeENS_26bidirectional_iterator_tagE
+ __ZSt28__throw_bad_array_new_lengthB9foe220100v
+ __ZZNSt3__16vectorI14ParsedWordDataNS_9allocatorIS1_EEE12emplace_backIJRU8__strongP8NSStringRdSA_SA_SA_SA_RbR13PDFQuadPointsEEERS1_DpOT_ENKUlvE0_clEv
+ ___103-[PDFAnnotationManager _findNextActivatableAnnotationFromPage:fromAnnotation:direction:withCompletion:]_block_invoke
+ ___103-[PDFAnnotationManager _findNextActivatableAnnotationFromPage:fromAnnotation:direction:withCompletion:]_block_invoke.71
+ ___103-[PDFAnnotationManager _findNextActivatableAnnotationFromPage:fromAnnotation:direction:withCompletion:]_block_invoke_2
+ ___103-[PDFAnnotationManager _findNextActivatableAnnotationFromPage:fromAnnotation:direction:withCompletion:]_block_invoke_3
+ ___103-[PDFAnnotationManager _findNextActivatableAnnotationFromPage:fromAnnotation:direction:withCompletion:]_block_invoke_4
+ ___21-[PDFPage _scanData:]_block_invoke
+ ___26-[PDFDocument _commonInit]_block_invoke
+ ___32-[PDFPage lazilyLoadAnnotations]_block_invoke
+ ___33-[PDFPage areaOfInterestAtPoint:]_block_invoke
+ ___34-[PDFView areaOfInterestForPoint:]_block_invoke
+ ___36-[PDFDocumentView _updateVisibility]_block_invoke.138
+ ___36-[PDFKitPopupViewController dismiss]_block_invoke
+ ___36-[PDFPage insertAnnotation:atIndex:]_block_invoke
+ ___36-[PDFPage removeAnnotation:atIndex:]_block_invoke
+ ___39-[PDFAnnotation updateAppearanceStream]_block_invoke
+ ___40-[PDFPageViewController removeAKOverlay]_block_invoke
+ ___40-[PDFPageViewController viewWillAppear:]_block_invoke
+ ___41-[PDFPage fetchPageLayoutWithCompletion:]_block_invoke
+ ___41-[PDFPage fetchPageLayoutWithCompletion:]_block_invoke_2
+ ___41-[PDFPage fetchPageLayoutWithCompletion:]_block_invoke_3
+ ___44-[PDFDocument flushPendingAppearanceUpdates]_block_invoke
+ ___47-[PDFAnnotation registerAsDirtyForChangeOfKey:]_block_invoke
+ ___51+[PDFCGPDFUtilities cgNameStringFromPDFNameString:]_block_invoke
+ ___51+[PDFCGPDFUtilities dictionaryFromCGPDFDictionary:]_block_invoke
+ ___54-[PDFAnnotationManager _setButtonState:forAnnotation:]_block_invoke
+ ___54-[PDFAnnotationManager _setButtonState:forAnnotation:]_block_invoke_2
+ ___54-[PDFAnnotationManager _setButtonState:forAnnotation:]_block_invoke_3
+ ___57-[PDFAnnotationManager _handleLinkAnnotation:atLocation:]_block_invoke
+ ___57-[PDFPageViewAnnotationController _addPDFAnnotationViews]_block_invoke
+ ___57-[PDFPageViewAnnotationController _addPDFAnnotationViews]_block_invoke_2
+ ___57-[PDFPageViewAnnotationController page:didAddAnnotation:]_block_invoke
+ ___59-[PDFDocumentViewController pdfViewSafeAreaInsetsDidChange]_block_invoke
+ ___59-[PDFPage pdfScannerResultAtPoint:onPageLayer:waitForScan:]_block_invoke
+ ___60-[PDFPageViewAnnotationController page:didRemoveAnnotation:]_block_invoke
+ ___62+[PDFCGPDFUtilities _createCGPDFObjectFromValue:visitedNodes:]_block_invoke
+ ___62-[PDFTextInputView(UITextSearching) _setupSearchHighlightView]_block_invoke
+ ___62-[PDFTextInputView(UITextSearching) _targetedPreviewForRange:]_block_invoke
+ ___64-[PDFDocumentViewController backgroundImageForPage:withQuality:]_block_invoke
+ ___65-[PDFPageViewAnnotationController _addPDFAnnotationChoiceWidget:]_block_invoke
+ ___65-[PDFPageViewAnnotationController _addPDFAnnotationChoiceWidget:]_block_invoke_2
+ ___65-[PDFPageViewAnnotationController _addPDFAnnotationChoiceWidget:]_block_invoke_3
+ ___67-[PDFAnnotationManager _undoRadioButtonChange:withState:formValue:]_block_invoke
+ ___67-[PDFPageViewAnnotationController _createPopupMarkerForAnnotation:]_block_invoke
+ ___69-[PDFAnnotationManager activateNextAnnotationInDirection:completion:]_block_invoke
+ ___69-[PDFTextInputView(UITextSearching) _setDimmingViewVisible:animated:]_block_invoke
+ ___69-[PDFTextInputView(UITextSearching) _setDimmingViewVisible:animated:]_block_invoke_2
+ ___69-[PDFTextInputView(UITextSearching) _setDimmingViewVisible:animated:]_block_invoke_3
+ ___71-[PDFTextInputView(UITextInput) editMenuForTextRange:suggestedActions:]_block_invoke
+ ___80-[PDFDocumentViewController recieveBackgroundImage:atBackgroundQuality:forPage:]_block_invoke
+ ___82-[PDFTextInputView(UITextSearching) decorateFoundTextRange:inDocument:usingStyle:]_block_invoke
+ ___83-[PDFViewController _findNextActivatableAnnotationOnPage:fromAnnotation:direction:]_block_invoke.105
+ ___86-[PDFAnnotationManager _findNextActivatableAnnotationOnPage:fromAnnotation:direction:]_block_invoke
+ ___Block_byref_object_copy_.357
+ ___Block_byref_object_copy_.48
+ ___Block_byref_object_copy_.69
+ ___Block_byref_object_dispose_.358
+ ___Block_byref_object_dispose_.49
+ ___Block_byref_object_dispose_.70
+ ___PDFMainRunLoopPerformBlockInModes_block_invoke
+ ____digestDictionaryForIdentityHash_block_invoke
+ ___block_descriptor_104_e8_32s_e20_v16?0^{CGContext=}8ls32l8
+ ___block_descriptor_40_e8_32s_e24_v24?0"PDFPageView"8Q16ls32l8
+ ___block_descriptor_40_e8_32s_e33_v24?0"PDFPageView"8"PDFPage"16ls32l8
+ ___block_descriptor_40_e8_32w_e24_v16?0"NSNotification"8lw32l8
+ ___block_descriptor_41_e8_32s_e30_B32?0r*8^{CGPDFObject=}16^v24ls32l8
+ ___block_descriptor_48_e8_32bs40w_e23_v16?0"PDFAnnotation"8lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_48_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e23_v16?0"PDFAnnotation"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e18_v16?0"NSString"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e27_v16?0"<PDFPageObserver>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e36_v24?0"NSString"8"PDFAnnotation"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e30_v16?0"PDFAnnotationManager"8ls32l8
+ ___block_descriptor_56_e8_32s40r_e21_B16?0"PDFPageView"8ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48w_e17_v16?0"NSArray"8lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48w_e18_v16?0"NSString"8lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e30_v16?0"PDFAnnotationManager"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s_e25_v32?0"NSString"816^B24ls32l8
+ ___block_descriptor_64_e8_32s40s48s56w_e18_v16?0"UIAction"8lw56l8s32l8s40l8s48l8
+ ___block_descriptor_68_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s64l8s56l8
+ ___block_descriptor_80_e8_32s40w_e32_v16?0"UITapGestureRecognizer"8lw40l8s32l8
+ ___block_descriptor_88_e8_32s40s48s56bs64r72r_e5_v8?0lr64l8s32l8s56l8s40l8s48l8r72l8
+ ___block_literal_global.1001
+ ___block_literal_global.1003
+ ___block_literal_global.1023
+ ___block_literal_global.1025
+ ___block_literal_global.1036
+ ___block_literal_global.109
+ ___block_literal_global.116
+ ___block_literal_global.119
+ ___block_literal_global.122
+ ___block_literal_global.136
+ ___block_literal_global.161
+ ___block_literal_global.178
+ ___block_literal_global.180
+ ___block_literal_global.182
+ ___block_literal_global.205
+ ___block_literal_global.211
+ ___block_literal_global.212
+ ___block_literal_global.319
+ ___block_literal_global.365
+ ___block_literal_global.52
+ ___block_literal_global.528
+ ___block_literal_global.530
+ ___block_literal_global.567
+ ___block_literal_global.592
+ ___block_literal_global.72
+ ___block_literal_global.91
+ ___block_literal_global.940
+ ___block_literal_global.942
+ ___block_literal_global.944
+ ___block_literal_global.952
+ ___block_literal_global.954
+ ___block_literal_global.956
+ ___block_literal_global.964
+ ___block_literal_global.994
+ ___block_literal_global.996
+ ___block_literal_global.998
+ ___swift_closure_destructor
+ __digestDictionaryForIdentityHash
+ __digestObjectForIdentityHash
+ __dispatch_source_type_timer
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_PDFKit
+ _cgNameStringFromPDFNameString:.kPDFNameEscapeTable
+ _cgNameStringFromPDFNameString:.onceToken
+ _dispatch_get_global_queue
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _kCFRunLoopCommonModes
+ _kCGPDFContentStreamOptionAllowLossyImageCompressionKey
+ _kCGPDFDocumentWriteOptionSaveTextFromOCR
+ _kGestureActionHandlerKey
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$CGPDFObjectFromValue:
+ _objc_msgSend$CGPDFStringFromDate:
+ _objc_msgSend$PDFKitUserInterfaceLayoutDirection
+ _objc_msgSend$_activateAKAnnotation:
+ _objc_msgSend$_activateAnnotationInternal:
+ _objc_msgSend$_activatePDFKitAnnotation:
+ _objc_msgSend$_activeScrollView
+ _objc_msgSend$_addPDFAnnotationViews
+ _objc_msgSend$_addPopupForAnnotation:positioningRect:
+ _objc_msgSend$_addViewForAnnotation:
+ _objc_msgSend$_annotationManager
+ _objc_msgSend$_beginningOfDocument
+ _objc_msgSend$_buildPDFPageViews
+ _objc_msgSend$_calculateMarkerViewGeometryFromQuads:onLeft:frame:angle:
+ _objc_msgSend$_clearIncompatibleSelection:
+ _objc_msgSend$_comparePosition:toPosition:
+ _objc_msgSend$_computeIdentityHashForCGPDFDictionary:
+ _objc_msgSend$_configureAnnotationForPromotion:
+ _objc_msgSend$_convertPoint:fromPage:inPDFPageViewController:
+ _objc_msgSend$_convertPoint:toPage:inPDFPageViewController:
+ _objc_msgSend$_createCGPDFObjectFromValue:visitedNodes:
+ _objc_msgSend$_createPopupMarkerForAnnotation:
+ _objc_msgSend$_deactivateAnnotationInternal:
+ _objc_msgSend$_distanceFromPoint:toPageView:
+ _objc_msgSend$_endOfDocument
+ _objc_msgSend$_enforceAutoScaleFactorIfNeeded
+ _objc_msgSend$_findNextActivatableAnnotationFromPage:fromAnnotation:direction:withCompletion:
+ _objc_msgSend$_formChanged:
+ _objc_msgSend$_foundRangesForPages
+ _objc_msgSend$_gestureRecognizer:shouldReceiveTouch:event:
+ _objc_msgSend$_handleLinkAnnotation:atLocation:
+ _objc_msgSend$_handleMarkupAnnotation:atLocation:
+ _objc_msgSend$_handlePopupClose
+ _objc_msgSend$_handleWidgetAnnotation:
+ _objc_msgSend$_hideActiveMenus
+ _objc_msgSend$_identityHashMatchesForDictionary:
+ _objc_msgSend$_offsetFromPosition:toPosition:
+ _objc_msgSend$_pageFrameForPageInAutoScaleFactorCalculation:inPDFView:
+ _objc_msgSend$_point:isInPage:
+ _objc_msgSend$_positionFromPosition:inDirection:offset:
+ _objc_msgSend$_positioningRectInPageView
+ _objc_msgSend$_postActiveAnnotationChangedNotification
+ _objc_msgSend$_processDirtyAnnots
+ _objc_msgSend$_removeControlForAnnotation:
+ _objc_msgSend$_removeViewForAnnotation:
+ _objc_msgSend$_scrollToAnnotation:
+ _objc_msgSend$_setBounds:forBox:
+ _objc_msgSend$_setButtonState:forAnnotation:
+ _objc_msgSend$_setDictionaryValue:forKey:
+ _objc_msgSend$_setDimmingViewVisible:animated:
+ _objc_msgSend$_setupSearchHighlightView
+ _objc_msgSend$_shouldGenerateAppearanceForAnnotation:
+ _objc_msgSend$_showMenuForMarkupAnnotation:
+ _objc_msgSend$_textRangeFromPosition:toPosition:
+ _objc_msgSend$_undoRadioButtonChange:withState:formValue:
+ _objc_msgSend$_updateAnnotationsForPage:pageView:
+ _objc_msgSend$_updateBackgroundImageOfPage:inPageViewController:isSecondPage:
+ _objc_msgSend$_updatePageContainerViewSearchState
+ _objc_msgSend$_updatePageImageAtIndex:isSecondPage:inPageViewController:
+ _objc_msgSend$activateNextAnnotationInDirection:completion:
+ _objc_msgSend$activeControls
+ _objc_msgSend$activePageView
+ _objc_msgSend$addAKAnnotation:toCGPDFAnnotationDictionary:
+ _objc_msgSend$addAKAnnotationToCGPDFDictionary:
+ _objc_msgSend$addAnnotationsObserver:
+ _objc_msgSend$addArrangedSubview:
+ _objc_msgSend$addTextLayoutManager:
+ _objc_msgSend$allowsLossyImageCompression
+ _objc_msgSend$annotationController
+ _objc_msgSend$annotationManager
+ _objc_msgSend$annotationViews
+ _objc_msgSend$appendXObject:
+ _objc_msgSend$arrayByAddingObject:
+ _objc_msgSend$calculateLayerGeometryForQuad:markupType:bounds:position:angle:
+ _objc_msgSend$callPageViewControllerCreationDelegateMethod:
+ _objc_msgSend$callPageViewControllerRemovalDelegateMethod:
+ _objc_msgSend$canInteractAtPoint:
+ _objc_msgSend$canSaveWithMutablePDFUsingOptions:
+ _objc_msgSend$cancelled
+ _objc_msgSend$cgNameStringFromPDFNameString:
+ _objc_msgSend$choiceWidgetComboBoxAdapter
+ _objc_msgSend$choiceWidgetListBoxAdapter
+ _objc_msgSend$clearAllDecoratedFoundText
+ _objc_msgSend$comboBox
+ _objc_msgSend$configurationByApplyingConfiguration:
+ _objc_msgSend$configurationWithPaletteColors:
+ _objc_msgSend$configurationWithPointSize:weight:
+ _objc_msgSend$createAKAnnotation
+ _objc_msgSend$createControlForAnnotation:
+ _objc_msgSend$deactivateAnnotation:
+ _objc_msgSend$deactivateCurrentAnnotation
+ _objc_msgSend$decorateFoundTextRange:inDocument:usingStyle:
+ _objc_msgSend$deselectRowAtIndexPath:animated:
+ _objc_msgSend$destroyControlForAnnotation:
+ _objc_msgSend$dictionaryFromCGPDFDictionary:
+ _objc_msgSend$disableDimmingViewAnimation
+ _objc_msgSend$dismiss
+ _objc_msgSend$dismissFindNavigator
+ _objc_msgSend$effectiveUserInterfaceLayoutDirection
+ _objc_msgSend$ensureCGPDFAnnotation
+ _objc_msgSend$enumerateObserversRespondingToSelector:withBlock:
+ _objc_msgSend$facingPage
+ _objc_msgSend$fetchPageLayoutWithCompletion:
+ _objc_msgSend$findPageViewControllerForPage:
+ _objc_msgSend$flushPendingAKAnnotationData
+ _objc_msgSend$flushPendingAppearanceUpdates
+ _objc_msgSend$forceDimmingViewVisible
+ _objc_msgSend$foundRangesForPage:
+ _objc_msgSend$handleInteractionWithAnnotation:atLocation:
+ _objc_msgSend$highlightedFoundRange
+ _objc_msgSend$indexPathsForSelectedRows
+ _objc_msgSend$initWithActionBlock:
+ _objc_msgSend$initWithAnnotation:comboBoxControl:
+ _objc_msgSend$initWithAnnotation:initialContents:
+ _objc_msgSend$initWithAnnotation:tableView:
+ _objc_msgSend$initWithBlock:
+ _objc_msgSend$initWithBytes:length:encoding:
+ _objc_msgSend$initWithFrame:firstPageView:secondPageView:
+ _objc_msgSend$initWithLocaleIdentifier:
+ _objc_msgSend$initWithOptions:capacity:
+ _objc_msgSend$initWithParentAnnotation:owningPageView:owningPDFView:positioningRect:
+ _objc_msgSend$initWithPrimaryAction:
+ _objc_msgSend$insertSubview:atIndex:
+ _objc_msgSend$installGesturesInView:
+ _objc_msgSend$isFindingNextAnnotation
+ _objc_msgSend$isPointInHandle:whichHandle:hitRadius:
+ _objc_msgSend$layoutFrame
+ _objc_msgSend$layoutMarginsGuide
+ _objc_msgSend$localUndoManager
+ _objc_msgSend$navigationBar
+ _objc_msgSend$page:didAddAnnotation:
+ _objc_msgSend$page:didRemoveAnnotation:
+ _objc_msgSend$pageViewControllers
+ _objc_msgSend$pageViewForPage:
+ _objc_msgSend$parentAnnotation
+ _objc_msgSend$pdfScannerResultAtPoint:onPageLayer:waitForScan:
+ _objc_msgSend$pdfView:willAddPageViewController:
+ _objc_msgSend$pdfView:willRemovePageViewController:
+ _objc_msgSend$pdfViewSafeAreaInsetsDidChange
+ _objc_msgSend$performSelector:
+ _objc_msgSend$popupContentView
+ _objc_msgSend$positioningRect
+ _objc_msgSend$preferredFontForTextStyle:
+ _objc_msgSend$prepareForDeallocation
+ _objc_msgSend$present
+ _objc_msgSend$presentingViewController
+ _objc_msgSend$promoteAllDetectedAnnotationsOnPage:
+ _objc_msgSend$promoteAnnotations:onPage:
+ _objc_msgSend$recognizerWithActionBlock:
+ _objc_msgSend$registerAsDirtyForChangeOfKey:
+ _objc_msgSend$registerDirtyAnnotation:
+ _objc_msgSend$registerUndoWithTarget:handler:
+ _objc_msgSend$removeGesturesFromView
+ _objc_msgSend$rightBarButtonItem
+ _objc_msgSend$savedFirstResponder
+ _objc_msgSend$searchDelegate
+ _objc_msgSend$secondPDFPage
+ _objc_msgSend$secondPageView
+ _objc_msgSend$secondsFromGMTForDate:
+ _objc_msgSend$selectRow:inComponent:animated:
+ _objc_msgSend$selectedTextRange
+ _objc_msgSend$selectionForTextRange:pdfView:
+ _objc_msgSend$selectionHandler
+ _objc_msgSend$separatorColor
+ _objc_msgSend$set
+ _objc_msgSend$setBlock:
+ _objc_msgSend$setChoiceWidgetComboBoxAdapter:
+ _objc_msgSend$setChoiceWidgetListBoxAdapter:
+ _objc_msgSend$setContentInsetAdjustmentBehavior:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setDisableDimmingViewAnimation:
+ _objc_msgSend$setFindInteractionEnabled:
+ _objc_msgSend$setForceDimmingViewVisible:
+ _objc_msgSend$setFormChangedObservation:
+ _objc_msgSend$setIsFindingNextAnnotation:
+ _objc_msgSend$setLocalUndoManager:
+ _objc_msgSend$setLocale:
+ _objc_msgSend$setPopupContentView:
+ _objc_msgSend$setPopupPresentingViewController:
+ _objc_msgSend$setSavedFirstResponder:
+ _objc_msgSend$setScrollEdgeAppearance:
+ _objc_msgSend$setSearchDelegate:
+ _objc_msgSend$setSecondBackgroundImage:atBackgroundQuality:
+ _objc_msgSend$setSecondPDFPage:
+ _objc_msgSend$setSelectionHandler:
+ _objc_msgSend$setStandardAppearance:
+ _objc_msgSend$setStringValue:onChoiceWidgetAnnotation:
+ _objc_msgSend$setTextContainer:
+ _objc_msgSend$setTimeZone:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$setupViewsWithAnnotation:initialContents:
+ _objc_msgSend$showMarkupStyleMenuForMarkupAnnotation:
+ _objc_msgSend$sortUsingSelector:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$tableView
+ _objc_msgSend$textField
+ _objc_msgSend$updateAnnotationWithStringValue:
+ _objc_msgSend$updateAppearanceStream
+ _objc_msgSend$updateSearchStateWithFoundRanges:highlightedRange:forceDimming:
+ _objc_msgSend$valueWithNonretainedObject:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x6
+ _objc_retain_x9
+ _registerAsDirtyForChangeOfKey:.appearanceKeys
+ _registerAsDirtyForChangeOfKey:.onceToken
+ _strlen
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x25
+ _swift_release_x8
+ _swift_retain_x2
+ _swift_retain_x21
- +[PDFDocument standardDocumentAttributes]
- +[PDFDocument standardDocumentAttributes].cold.1
- +[PDFExtensionContext _extensionAuxiliaryHostProtocol]
- +[PDFExtensionContext _extensionAuxiliaryVendorProtocol]
- +[PDFExtensionContext initialize]
- +[PDFExtensionViewController _exportedInterface]
- +[PDFExtensionViewController _remoteViewControllerInterface]
- +[PDFHostExtensionContext _extensionAuxiliaryHostProtocol]
- +[PDFHostExtensionContext _extensionAuxiliaryVendorProtocol]
- +[PDFHostViewController backgroundColor]
- +[PDFHostViewController createHostView:forExtensionIdentifier:]
- +[PDFHostViewController exportedInterface]
- +[PDFHostViewController loadExtension:]
- +[PDFHostViewController serviceViewControllerInterface]
- +[PDFHostViewController setUseIOSurfaceForTiles:]
- +[PDFHostViewController useIOSurfaceForTiles]
- +[XPCExtensionInterface extensionInterface]
- +[XPCExtensionInterface extensionInterface].cold.1
- +[XPCExtensionInterface hostInterface]
- +[XPCExtensionInterface hostInterface].cold.1
- -[PDFAKPageOverlayViewProvider overlayViewInstalledForPage:]
- -[PDFAKPageOverlayViewProvider overlayViewWillBeUninstalledForPage:]
- -[PDFAnnotation addToPageView]
- -[PDFAnnotation removeFromPageView]
- -[PDFDocumentViewController _convertPoint:fromPDFPageViewController:]
- -[PDFDocumentViewController _convertPoint:toPDFPageViewController:]
- -[PDFExtensionContext .cxx_destruct]
- -[PDFExtensionContext extensionViewController]
- -[PDFExtensionContext hostToExtension:]
- -[PDFExtensionContext setExtensionViewController:]
- -[PDFExtensionTopView canBecomeFirstResponder]
- -[PDFExtensionTopView hitTest:withEvent:]
- -[PDFExtensionTopView pointInside:withEvent:]
- -[PDFExtensionViewController .cxx_destruct]
- -[PDFExtensionViewController _annotationHitNotification:]
- -[PDFExtensionViewController _annotationLongPressNotification:]
- -[PDFExtensionViewController _goToDestination:]
- -[PDFExtensionViewController _goToPage:]
- -[PDFExtensionViewController _pageChangedNotification:]
- -[PDFExtensionViewController _pdfViewZoomToRect:]
- -[PDFExtensionViewController _selectionChangedNotification:]
- -[PDFExtensionViewController _selectionPointsChangedNotification:]
- -[PDFExtensionViewController _setupDocumentViewSize]
- -[PDFExtensionViewController _textSelectionDidCopyNotification:]
- -[PDFExtensionViewController _textSelectionShowTextSelectionMenu:]
- -[PDFExtensionViewController _updateDocumentIsLocked]
- -[PDFExtensionViewController _updatePageCount]
- -[PDFExtensionViewController _updateTextSelectionPoints]
- -[PDFExtensionViewController _zoomToRect:]
- -[PDFExtensionViewController cancelFindStringWithHighlightsCleared:]
- -[PDFExtensionViewController cancelFindString]
- -[PDFExtensionViewController clearSearchHighlights]
- -[PDFExtensionViewController copy]
- -[PDFExtensionViewController didMatchString:]
- -[PDFExtensionViewController documentDidEndDocumentFind:]
- -[PDFExtensionViewController findString:withOptions:]
- -[PDFExtensionViewController focusOnSearchResultAtIndex:]
- -[PDFExtensionViewController goToPageIndex:]
- -[PDFExtensionViewController handleGesture:state:location:locationOfFirstTouch:isIndirectTouch:]
- -[PDFExtensionViewController init]
- -[PDFExtensionViewController pointerRegionForLocation:]
- -[PDFExtensionViewController selectAll]
- -[PDFExtensionViewController setDocumentData:]
- -[PDFExtensionViewController setMaximumZoomScale:]
- -[PDFExtensionViewController setMinimumZoomScale:]
- -[PDFExtensionViewController setupPDFView]
- -[PDFExtensionViewController snapshotViewRect:forWidth:afterScreenUpdates:]
- -[PDFExtensionViewController unlockWithPassword:]
- -[PDFExtensionViewController updatePDFViewLayout:scrollViewFrame:safeAreaInsets:zoomScale:]
- -[PDFExtensionViewController viewDidLoad]
- -[PDFExtensionViewControllerPrivate .cxx_destruct]
- -[PDFHostExtensionContext .cxx_destruct]
- -[PDFHostExtensionContext extensionSnapshotToHost:scale:]
- -[PDFHostExtensionContext extensionToHost:]
- -[PDFHostExtensionContext hostViewController]
- -[PDFHostExtensionContext setHostViewController:]
- -[PDFHostViewController .cxx_destruct]
- -[PDFHostViewController _appendPasswordUI]
- -[PDFHostViewController _documentViewSize]
- -[PDFHostViewController _endPDFViewRotationAnimated:withUpdate:]
- -[PDFHostViewController _gestureInit]
- -[PDFHostViewController _hostScrollViewZoomScale]
- -[PDFHostViewController _insetBoundsInDocument]
- -[PDFHostViewController _isTouchingLollipopAtLocationOfFirstTouch:]
- -[PDFHostViewController _pdfViewInsets]
- -[PDFHostViewController _pdfViewSafeAreaInsets]
- -[PDFHostViewController _pointerInteraction:regionForRequest:defaultRegion:completion:]
- -[PDFHostViewController _resetPDFHostViewControllerViews]
- -[PDFHostViewController _setMaximumZoomScale:]
- -[PDFHostViewController _setMinimumZoomScale:]
- -[PDFHostViewController _setupExtensionInterruptionBlock]
- -[PDFHostViewController _typeForGestureRecognizer:]
- -[PDFHostViewController beginPDFViewRotation]
- -[PDFHostViewController canPerformAction:withSender:]
- -[PDFHostViewController cancelFindStringWithHighlightsCleared:]
- -[PDFHostViewController cancelFindString]
- -[PDFHostViewController clearSearchHighlights]
- -[PDFHostViewController completePointerInteractionRegionForRequest:]
- -[PDFHostViewController copy:]
- -[PDFHostViewController currentPageIndex]
- -[PDFHostViewController dealloc]
- -[PDFHostViewController didCopy:]
- -[PDFHostViewController didLongPressPageIndex:atLocation:withAnnotationRect:]
- -[PDFHostViewController didLongPressURL:atLocation:withAnnotationRect:]
- -[PDFHostViewController documentIsLocked:]
- -[PDFHostViewController endPDFViewRotationWithContentInset:]
- -[PDFHostViewController endPDFViewRotation]
- -[PDFHostViewController findString:withOptions:]
- -[PDFHostViewController findStringUpdate:done:]
- -[PDFHostViewController focusOnSearchResultAtIndex:]
- -[PDFHostViewController gestureRecognizer:shouldReceiveTouch:]
- -[PDFHostViewController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:]
- -[PDFHostViewController gestureRecognizerShouldBegin:]
- -[PDFHostViewController goToDestination:point:]
- -[PDFHostViewController goToPageIndex:]
- -[PDFHostViewController goToPageIndex:pageFrame:]
- -[PDFHostViewController goToPageIndex:withViewFrustum:]
- -[PDFHostViewController goToURL:atLocation:]
- -[PDFHostViewController handleGesture:]
- -[PDFHostViewController killExtensionProcess]
- -[PDFHostViewController maximumZoomScale]
- -[PDFHostViewController minimumZoomScale]
- -[PDFHostViewController observeValueForKeyPath:ofObject:change:context:]
- -[PDFHostViewController pageCount]
- -[PDFHostViewController pageNumberIndicator]
- -[PDFHostViewController pointerInteraction:styleForRegion:]
- -[PDFHostViewController recievedSnapshotViewRect:]
- -[PDFHostViewController selectAll:]
- -[PDFHostViewController setDelegate:]
- -[PDFHostViewController setDocumentData:withScrollView:]
- -[PDFHostViewController setHasSelection:]
- -[PDFHostViewController setTextSelectionPoints:right:]
- -[PDFHostViewController setupDocumentViewSize:]
- -[PDFHostViewController setup]
- -[PDFHostViewController showSelectionRect:]
- -[PDFHostViewController showTextSelectionMenu:selectionRect:]
- -[PDFHostViewController snapshotViewRect:snapshotWidth:afterScreenUpdates:withResult:]
- -[PDFHostViewController updateAutoScaleFactor]
- -[PDFHostViewController updateCurrentPageIndex:]
- -[PDFHostViewController updateDocumentIsLocked:]
- -[PDFHostViewController updateDocumentViewSize]
- -[PDFHostViewController updatePDFViewLayout]
- -[PDFHostViewController updatePageCount:]
- -[PDFHostViewController userDidEnterPassword:forPasswordViewController:]
- -[PDFHostViewController viewDidLayoutSubviews]
- -[PDFHostViewController zoomToRect:]
- -[PDFHostViewControllerPrivate .cxx_destruct]
- -[PDFKitPopupView .cxx_destruct]
- -[PDFKitPopupView _popoverControllerSourceRect]
- -[PDFKitPopupView _presentPopupView]
- -[PDFKitPopupView _presentPopupView_iOS]
- -[PDFKitPopupView _presentViewController:]
- -[PDFKitPopupView _removeControlForAnnotation]
- -[PDFKitPopupView _setupPopupView]
- -[PDFKitPopupView _updateParentContents]
- -[PDFKitPopupView becomeFirstResponder]
- -[PDFKitPopupView doneButton:]
- -[PDFKitPopupView initWithParentAnnotation:owningPageView:owningPDFView:]
- -[PDFKitPopupView popoverPresentationController:willRepositionPopoverToRect:inView:]
- -[PDFKitPopupView popoverPresentationControllerDidDismissPopover:]
- -[PDFKitPopupView prepareForPopoverPresentation:]
- -[PDFKitPopupView removeFromSuperview]
- -[PDFKitPopupView textViewDidChange:]
- -[PDFKitPopupView textView]
- -[PDFKitPopupViewPrivate .cxx_destruct]
- -[PDFOverlayViewsController _setupGestureRecognizersForView:andDocument:]
- -[PDFOverlayViewsController _teardownGestureRecognizersForView:andDocument:]
- -[PDFPage _buildPageLayout]
- -[PDFPage fetchPageLayoutWithCompletion:deliveredOnQueue:]
- -[PDFPage pageLayoutIfAvail]
- -[PDFPage pageLayout]
- -[PDFPage setExtraContentStream:steamDocument:]
- -[PDFPageLabelView .cxx_destruct]
- -[PDFPageLabelView _startFade]
- -[PDFPageLabelView initWithFrame:]
- -[PDFPageLabelView setCurrentPageNumber:forPageCount:]
- -[PDFPageLabelView updateEffect]
- -[PDFPageLabelViewPrivate .cxx_destruct]
- -[PDFPageView _addPDFAnnotation:]
- -[PDFPageView _addPDFAnnotationChoiceWidget:]
- -[PDFPageView _addPDFAnnotationSignatureWidget:]
- -[PDFPageView _addPDFAnnotationTextWidget:]
- -[PDFPageView _allowsFormFieldEntry]
- -[PDFPageView _choiceWidgetDone]
- -[PDFPageView _didRotatePageNotification:]
- -[PDFPageView _formChanged:]
- -[PDFPageView _rotateActiveAnnotation]
- -[PDFPageView _rotationTransformForPageView]
- -[PDFPageView _setuppageAnnotationEffects]
- -[PDFPageView _updateWidgetControl:forBounds:]
- -[PDFPageView activeAnnotation]
- -[PDFPageView addAnnotation:]
- -[PDFPageView addControlForAnnotation:]
- -[PDFPageView numberOfComponentsInPickerView:]
- -[PDFPageView numberOfSectionsInTableView:]
- -[PDFPageView pickerView:didSelectRow:inComponent:]
- -[PDFPageView pickerView:numberOfRowsInComponent:]
- -[PDFPageView pickerView:viewForRow:forComponent:reusingView:]
- -[PDFPageView removeAnnotation:]
- -[PDFPageView removeControlForAnnotation:]
- -[PDFPageView setStringValue:onChoiceWidgetAnnotation:withTableView:]
- -[PDFPageView setStringValue:onChoiceWidgetAnnotation:withTextField:]
- -[PDFPageView setStringValue:onTextWidgetAnnotation:withTextView:]
- -[PDFPageView tableView:cellForRowAtIndexPath:]
- -[PDFPageView tableView:didSelectRowAtIndexPath:]
- -[PDFPageView tableView:numberOfRowsInSection:]
- -[PDFPageViewAnnotationController _addPopupForAnnotation:]
- -[PDFPageViewAnnotationController activeAnnotation]
- -[PDFPageViewAnnotationController addControlForAnnotation:]
- -[PDFPageViewAnnotationController removeControlForAnnotation:]
- -[PDFPageViewAnnotationControllerPrivate .cxx_destruct]
- -[PDFPageViewController _buildPDFPageView]
- -[PDFRenderingProperties isUsingPDFExtensionView]
- -[PDFRenderingProperties setIsUsingPDFExtensionView:]
- -[PDFScrollView setContentInset:]
- -[PDFScrollViewPrivate .cxx_destruct]
- -[PDFSelection copyAsTextSelection]
- -[PDFTextInputView _allowAnimatedUpdateSelectionRectViews]
- -[PDFTextInputView _closestPositionToPoint:withinRange:]
- -[PDFTextInputView _setDimmingViewVisible:]
- -[PDFTextInputView _targetedPreviewForRange:]
- -[PDFTextInputView baseWritingDirectionForPosition:inDirection:]
- -[PDFTextInputView beginningOfDocument]
- -[PDFTextInputView caretRectForPosition:]
- -[PDFTextInputView characterRangeAtPoint:]
- -[PDFTextInputView characterRangeByExtendingPosition:inDirection:]
- -[PDFTextInputView clearAllDecoratedFoundText]
- -[PDFTextInputView closestPositionToPoint:]
- -[PDFTextInputView closestPositionToPoint:withinRange:]
- -[PDFTextInputView compareFoundRange:toRange:inDocument:]
- -[PDFTextInputView comparePosition:toPosition:]
- -[PDFTextInputView decorateFoundTextRange:inDocument:usingStyle:]
- -[PDFTextInputView deleteBackward]
- -[PDFTextInputView editMenuForTextRange:suggestedActions:]
- -[PDFTextInputView endOfDocument]
- -[PDFTextInputView firstRectForRange:]
- -[PDFTextInputView hasText]
- -[PDFTextInputView inputDelegate]
- -[PDFTextInputView insertText:]
- -[PDFTextInputView interactionShouldBegin:atPoint:]
- -[PDFTextInputView isSecureTextEntry]
- -[PDFTextInputView layoutSubviews]
- -[PDFTextInputView linkRegionsConstrainedToLineAtPoint:]
- -[PDFTextInputView markedTextRange]
- -[PDFTextInputView markedTextStyle]
- -[PDFTextInputView offsetFromPosition:toPosition:]
- -[PDFTextInputView performTextSearchWithQueryString:usingOptions:resultAggregator:]
- -[PDFTextInputView positionFromPosition:inDirection:offset:]
- -[PDFTextInputView positionFromPosition:offset:]
- -[PDFTextInputView positionWithinRange:farthestInDirection:]
- -[PDFTextInputView replaceRange:withText:]
- -[PDFTextInputView selectionRectsForRange:]
- -[PDFTextInputView setBaseWritingDirection:forRange:]
- -[PDFTextInputView setInputDelegate:]
- -[PDFTextInputView setMarkedText:selectedRange:]
- -[PDFTextInputView setMarkedTextStyle:]
- -[PDFTextInputView setTokenizer:]
- -[PDFTextInputView textInRange:]
- -[PDFTextInputView textRangeFromPosition:toPosition:]
- -[PDFTextInputView tokenizer]
- -[PDFTextInputView unmarkText]
- -[PDFView activeAnnotation]
- -[PDFView drawNodeBoundingBoxesType:enableDrawing:]
- -[PDFView drawTextBoundingBoxesType:enableDrawing:]
- -[PDFView extensionViewBoundsInDocument]
- -[PDFView extensionViewZoomScale]
- -[PDFView gestureRecognizer:shouldReceiveTouch:]
- -[PDFView gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:]
- -[PDFView gestureRecognizerShouldBegin:]
- -[PDFView hitTestForSubviewsOfView:atLocation:withEvent:]
- -[PDFView interactWithAnnotation:]
- -[PDFView pdfDocumentViewSize]
- -[PDFView removeControlForAnnotation:]
- -[PDFView setActiveAnnotation:]
- -[PDFView setIsUsingPDFExtensionView:]
- -[PDFView setScrollViewScrollEnabled:]
- -[PDFView updateNodeBoundingBoxes]
- -[PDFView updatePDFViewLayout:scrollViewFrame:zoomScale:]
- -[PDFViewController _addControlForAnnotation:]
- -[PDFViewController _annotationHit:atLocation:]
- -[PDFViewController _doButtonHit:]
- -[PDFViewController _handleButtonHit:]
- -[PDFViewController activateAnnotation:]
- -[PDFViewController activeAnnotation]
- -[PDFViewController addDetectedAnnotation:toPage:]
- -[PDFViewController interactWithAnnotation:]
- -[PDFViewController populateAnnotationsFromDetectedAnnotationsOnPage:]
- -[PDFViewController removeControlForAnnotation:]
- -[PDFViewController setActiveAnnotation:]
- -[PDFViewController showMarkupStyleMenuForMarkupAnnotation]
- -[PageSignature .cxx_destruct]
- -[SelectionRectInfo .cxx_destruct]
- GCC_except_table101
- GCC_except_table109
- GCC_except_table110
- GCC_except_table111
- GCC_except_table116
- GCC_except_table122
- GCC_except_table123
- GCC_except_table141
- GCC_except_table147
- GCC_except_table161
- GCC_except_table163
- GCC_except_table174
- GCC_except_table178
- GCC_except_table180
- GCC_except_table182
- GCC_except_table244
- GCC_except_table322
- GCC_except_table328
- GCC_except_table61
- GCC_except_table71
- GCC_except_table76
- _CGContextDrawImage
- _CGIOSurfaceContextCreate
- _CGImageCreate
- _CGImageCreateFromIOSurface
- _CGPDFContextAddInfoEntry
- _CGPDFDictionaryCreateNSDictionary
- _CGPDFDictionaryEnumerateKeysAndValues
- _CGPDFDocumentCopyPage
- _CGPDFPageSetExtraContentStream
- _IOSurfacePropertyKeyBytesPerElement
- _IOSurfacePropertyKeyHeight
- _IOSurfacePropertyKeyPixelFormat
- _IOSurfacePropertyKeyWidth
- _OBJC_CLASS_$_CAFilter
- _OBJC_CLASS_$_IOSurface
- _OBJC_CLASS_$_NSExtension
- _OBJC_CLASS_$_NSExtensionContext
- _OBJC_CLASS_$_NSLayoutManager
- _OBJC_CLASS_$_NSXPCInterface
- _OBJC_CLASS_$_PDFDocumentContentView
- _OBJC_CLASS_$_PDFExtensionContext
- _OBJC_CLASS_$_PDFExtensionTopView
- _OBJC_CLASS_$_PDFExtensionViewController
- _OBJC_CLASS_$_PDFExtensionViewControllerPrivate
- _OBJC_CLASS_$_PDFHostExtensionContext
- _OBJC_CLASS_$_PDFHostViewController
- _OBJC_CLASS_$_PDFHostViewControllerPrivate
- _OBJC_CLASS_$_PDFKitPopupView
- _OBJC_CLASS_$_PDFKitPopupViewPrivate
- _OBJC_CLASS_$_PDFPageLabelView
- _OBJC_CLASS_$_PDFPageLabelViewPrivate
- _OBJC_CLASS_$_PDFPageViewAnnotationControllerPrivate
- _OBJC_CLASS_$_PDFScrollViewPrivate
- _OBJC_CLASS_$_PageSignature
- _OBJC_CLASS_$_SelectionRectInfo
- _OBJC_CLASS_$_UILabel
- _OBJC_CLASS_$_UIMenuController
- _OBJC_CLASS_$_UIPointerRegion
- _OBJC_CLASS_$_XPCExtensionInterface
- _OBJC_CLASS_$__UIBackdropView
- _OBJC_CLASS_$__UIBackdropViewSettings
- _OBJC_CLASS_$__UIRemoteViewController
- _OBJC_IVAR_$_PDFDocument._auxiliaryAttributes
- _OBJC_IVAR_$_PDFDocumentViewPrivate.contentView
- _OBJC_IVAR_$_PDFExtensionContext._extensionViewController
- _OBJC_IVAR_$_PDFExtensionViewController._private
- _OBJC_IVAR_$_PDFExtensionViewControllerPrivate.bottomRightSelectionPoint
- _OBJC_IVAR_$_PDFExtensionViewControllerPrivate.currentGestureState
- _OBJC_IVAR_$_PDFExtensionViewControllerPrivate.didCancelActiveSearch
- _OBJC_IVAR_$_PDFExtensionViewControllerPrivate.documentViewSize
- _OBJC_IVAR_$_PDFExtensionViewControllerPrivate.hasSelection
- _OBJC_IVAR_$_PDFExtensionViewControllerPrivate.hostProxy
- _OBJC_IVAR_$_PDFExtensionViewControllerPrivate.pdfView
- _OBJC_IVAR_$_PDFExtensionViewControllerPrivate.searchResults
- _OBJC_IVAR_$_PDFExtensionViewControllerPrivate.searchSelection
- _OBJC_IVAR_$_PDFExtensionViewControllerPrivate.searchString
- _OBJC_IVAR_$_PDFExtensionViewControllerPrivate.topLeftSelectionPoint
- _OBJC_IVAR_$_PDFHostExtensionContext._hostViewController
- _OBJC_IVAR_$_PDFHostViewController._private
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.bottomRightSelectionPoint
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.contentInset
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.currentPageIndex
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.documentViewCenter
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.documentViewSize
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.doubleTapGestureRecognizer
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.extension
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.extensionProxy
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.hasSelection
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.horizontalScaleFactor
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.hostScrollView
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.hostScrollViewObserverIsActive
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.hostViewControllerDelegate
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.insetBoundsInDocument
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.isUnlocked
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.longPressGestureRecognizer
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.maxScaleFactor
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.minScaleFactor
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.pageCount
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.pageLabelView
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.panGestureRecognizer
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.password
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.passwordViewController
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.pdfPointerCompletionHandler
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.pdfSafeAreaInsets
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.pdfViewIsRotating
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.pdfViewNeedsUpdate
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.pointerInteraction
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.recentGestureIsIndirectTouch
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.scrollViewFrame
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.snapshotCompletion
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.tapGestureRecognizer
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.topLeftSelectionPoint
- _OBJC_IVAR_$_PDFHostViewControllerPrivate.topView
- _OBJC_IVAR_$_PDFKitPopupView._private
- _OBJC_IVAR_$_PDFKitPopupViewPrivate.contents
- _OBJC_IVAR_$_PDFKitPopupViewPrivate.deviceIsiPad
- _OBJC_IVAR_$_PDFKitPopupViewPrivate.deviceIsiPhone
- _OBJC_IVAR_$_PDFKitPopupViewPrivate.pageView
- _OBJC_IVAR_$_PDFKitPopupViewPrivate.parentAnnotation
- _OBJC_IVAR_$_PDFKitPopupViewPrivate.popupController
- _OBJC_IVAR_$_PDFKitPopupViewPrivate.popupTextView
- _OBJC_IVAR_$_PDFKitPopupViewPrivate.popupTextViewUndoManager
- _OBJC_IVAR_$_PDFKitPopupViewPrivate.savedFirstResponder
- _OBJC_IVAR_$_PDFKitPopupViewPrivate.view
- _OBJC_IVAR_$_PDFPage._builtLayout
- _OBJC_IVAR_$_PDFPage._layout
- _OBJC_IVAR_$_PDFPage._layoutLock
- _OBJC_IVAR_$_PDFPage._lock_getAnnotations
- _OBJC_IVAR_$_PDFPageLabelView._private
- _OBJC_IVAR_$_PDFPageLabelViewPrivate.backdropView
- _OBJC_IVAR_$_PDFPageLabelViewPrivate.label
- _OBJC_IVAR_$_PDFPageLabelViewPrivate.visibilityTimer
- _OBJC_IVAR_$_PDFPageViewAnnotationController._private
- _OBJC_IVAR_$_PDFPageViewAnnotationControllerPrivate.activeAnnotation
- _OBJC_IVAR_$_PDFPageViewAnnotationControllerPrivate.activeControls
- _OBJC_IVAR_$_PDFPageViewAnnotationControllerPrivate.page
- _OBJC_IVAR_$_PDFPageViewAnnotationControllerPrivate.pageView
- _OBJC_IVAR_$_PDFPageViewAnnotationControllerPrivate.view
- _OBJC_IVAR_$_PDFPageViewPrivate.activeAnnotation
- _OBJC_IVAR_$_PDFPageViewPrivate.activeControls
- _OBJC_IVAR_$_PDFPageViewPrivate.activeTextStorage
- _OBJC_IVAR_$_PDFPageViewPrivate.pageAnnotationEffects
- _OBJC_IVAR_$_PDFPageViewPrivate.pageSignatures
- _OBJC_IVAR_$_PDFRenderingProperties._isUsingPDFExtensionView
- _OBJC_IVAR_$_PDFScrollView._private
- _OBJC_IVAR_$_PDFScrollViewPrivate.boundsUpdateTimer
- _OBJC_IVAR_$_PDFScrollViewPrivate.document
- _OBJC_IVAR_$_PDFScrollViewPrivate.documentView
- _OBJC_IVAR_$_PDFScrollViewPrivate.forcesTopAlignment
- _OBJC_IVAR_$_PDFScrollViewPrivate.isZooming
- _OBJC_IVAR_$_PDFScrollViewPrivate.oldBounds
- _OBJC_IVAR_$_PDFScrollViewPrivate.oldMagnification
- _OBJC_IVAR_$_PDFScrollViewPrivate.pageSyncDate
- _OBJC_IVAR_$_PDFScrollViewPrivate.pdfView
- _OBJC_IVAR_$_PDFScrollViewPrivate.scheduledPageSync
- _OBJC_IVAR_$_PDFViewControllerPrivate.activeAnnotation
- _OBJC_IVAR_$_PDFViewControllerPrivate.didPostPDFExtensionViewAnnotationLongPress
- _OBJC_IVAR_$_PDFViewControllerPrivate.longPressGestureStartTime
- _OBJC_IVAR_$_PDFViewPrivate.extensionViewBoundsInDocument
- _OBJC_IVAR_$_PDFViewPrivate.extensionViewFrame
- _OBJC_IVAR_$_PDFViewPrivate.extensionViewZoomScale
- _OBJC_IVAR_$_PageSignature.annotation
- _OBJC_IVAR_$_PageSignature.signatureLayer
- _OBJC_IVAR_$_SelectionRectInfo.rect
- _OBJC_IVAR_$_SelectionRectInfo.selection
- _OBJC_IVAR_$_SelectionRectInfo.transform
- _OBJC_IVAR_$_SelectionRectInfo.type
- _OBJC_METACLASS_$_NSExtensionContext
- _OBJC_METACLASS_$_PDFDocumentContentView
- _OBJC_METACLASS_$_PDFExtensionContext
- _OBJC_METACLASS_$_PDFExtensionTopView
- _OBJC_METACLASS_$_PDFExtensionViewController
- _OBJC_METACLASS_$_PDFExtensionViewControllerPrivate
- _OBJC_METACLASS_$_PDFHostExtensionContext
- _OBJC_METACLASS_$_PDFHostViewController
- _OBJC_METACLASS_$_PDFHostViewControllerPrivate
- _OBJC_METACLASS_$_PDFKitPopupView
- _OBJC_METACLASS_$_PDFKitPopupViewPrivate
- _OBJC_METACLASS_$_PDFPageLabelView
- _OBJC_METACLASS_$_PDFPageLabelViewPrivate
- _OBJC_METACLASS_$_PDFPageViewAnnotationControllerPrivate
- _OBJC_METACLASS_$_PDFScrollViewPrivate
- _OBJC_METACLASS_$_PageSignature
- _OBJC_METACLASS_$_SelectionRectInfo
- _OBJC_METACLASS_$_XPCExtensionInterface
- _OBJC_METACLASS_$__UIRemoteViewController
- _PDFEdgeInsetsEqualToInsets
- _PDFKitDeviceIsiPhone
- _PDFKitDeviceIsiPhone.cold.1
- _PDFKitDeviceIsiPhone.deviceIsiPhone
- _PDFKitDeviceIsiPhone.onceToken
- __CFPrefsSetDirectModeEnabled
- __CFPrefsSetReadOnly
- __OBJC_$_CLASS_METHODS_PDFExtensionContext
- __OBJC_$_CLASS_METHODS_PDFExtensionViewController
- __OBJC_$_CLASS_METHODS_PDFHostExtensionContext
- __OBJC_$_CLASS_METHODS_PDFHostViewController
- __OBJC_$_CLASS_METHODS_XPCExtensionInterface
- __OBJC_$_CLASS_PROP_LIST_PDFHostViewController
- __OBJC_$_INSTANCE_METHODS_PDFExtensionContext
- __OBJC_$_INSTANCE_METHODS_PDFExtensionTopView
- __OBJC_$_INSTANCE_METHODS_PDFExtensionViewController
- __OBJC_$_INSTANCE_METHODS_PDFExtensionViewControllerPrivate
- __OBJC_$_INSTANCE_METHODS_PDFHostExtensionContext
- __OBJC_$_INSTANCE_METHODS_PDFHostViewController
- __OBJC_$_INSTANCE_METHODS_PDFHostViewControllerPrivate
- __OBJC_$_INSTANCE_METHODS_PDFKitPopupView
- __OBJC_$_INSTANCE_METHODS_PDFKitPopupViewPrivate
- __OBJC_$_INSTANCE_METHODS_PDFPageLabelView
- __OBJC_$_INSTANCE_METHODS_PDFPageLabelViewPrivate
- __OBJC_$_INSTANCE_METHODS_PDFPageViewAnnotationControllerPrivate
- __OBJC_$_INSTANCE_METHODS_PDFScrollViewPrivate
- __OBJC_$_INSTANCE_METHODS_PDFTextInputView
- __OBJC_$_INSTANCE_METHODS_PageSignature
- __OBJC_$_INSTANCE_METHODS_SelectionRectInfo
- __OBJC_$_INSTANCE_VARIABLES_PDFExtensionContext
- __OBJC_$_INSTANCE_VARIABLES_PDFExtensionViewController
- __OBJC_$_INSTANCE_VARIABLES_PDFExtensionViewControllerPrivate
- __OBJC_$_INSTANCE_VARIABLES_PDFHostExtensionContext
- __OBJC_$_INSTANCE_VARIABLES_PDFHostViewController
- __OBJC_$_INSTANCE_VARIABLES_PDFHostViewControllerPrivate
- __OBJC_$_INSTANCE_VARIABLES_PDFKitPopupView
- __OBJC_$_INSTANCE_VARIABLES_PDFKitPopupViewPrivate
- __OBJC_$_INSTANCE_VARIABLES_PDFPageLabelView
- __OBJC_$_INSTANCE_VARIABLES_PDFPageLabelViewPrivate
- __OBJC_$_INSTANCE_VARIABLES_PDFPageViewAnnotationControllerPrivate
- __OBJC_$_INSTANCE_VARIABLES_PDFScrollViewPrivate
- __OBJC_$_INSTANCE_VARIABLES_PageSignature
- __OBJC_$_INSTANCE_VARIABLES_SelectionRectInfo
- __OBJC_$_PROP_LIST_PDFExtensionContext
- __OBJC_$_PROP_LIST_PDFHostExtensionContext
- __OBJC_$_PROP_LIST_PDFHostViewController
- __OBJC_$_PROP_LIST_PDFKitPopupView
- __OBJC_$_PROP_LIST_PDFTextInputView
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PDFExtensionProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PDFHostProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_PDFExtensionProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_PDFHostProtocol
- __OBJC_$_PROTOCOL_REFS_PDFExtensionProtocol
- __OBJC_$_PROTOCOL_REFS_PDFHostProtocol
- __OBJC_CLASS_PROTOCOLS_$_PDFExtensionContext
- __OBJC_CLASS_PROTOCOLS_$_PDFHostExtensionContext
- __OBJC_CLASS_PROTOCOLS_$_PDFHostViewController
- __OBJC_CLASS_PROTOCOLS_$_PDFKitPopupView
- __OBJC_CLASS_PROTOCOLS_$_PDFTextInputView
- __OBJC_CLASS_RO_$_PDFDocumentContentView
- __OBJC_CLASS_RO_$_PDFExtensionContext
- __OBJC_CLASS_RO_$_PDFExtensionTopView
- __OBJC_CLASS_RO_$_PDFExtensionViewController
- __OBJC_CLASS_RO_$_PDFExtensionViewControllerPrivate
- __OBJC_CLASS_RO_$_PDFHostExtensionContext
- __OBJC_CLASS_RO_$_PDFHostViewController
- __OBJC_CLASS_RO_$_PDFHostViewControllerPrivate
- __OBJC_CLASS_RO_$_PDFKitPopupView
- __OBJC_CLASS_RO_$_PDFKitPopupViewPrivate
- __OBJC_CLASS_RO_$_PDFPageLabelView
- __OBJC_CLASS_RO_$_PDFPageLabelViewPrivate
- __OBJC_CLASS_RO_$_PDFPageViewAnnotationControllerPrivate
- __OBJC_CLASS_RO_$_PDFScrollViewPrivate
- __OBJC_CLASS_RO_$_PageSignature
- __OBJC_CLASS_RO_$_SelectionRectInfo
- __OBJC_CLASS_RO_$_XPCExtensionInterface
- __OBJC_LABEL_PROTOCOL_$_PDFExtensionProtocol
- __OBJC_LABEL_PROTOCOL_$_PDFHostProtocol
- __OBJC_METACLASS_RO_$_PDFDocumentContentView
- __OBJC_METACLASS_RO_$_PDFExtensionContext
- __OBJC_METACLASS_RO_$_PDFExtensionTopView
- __OBJC_METACLASS_RO_$_PDFExtensionViewController
- __OBJC_METACLASS_RO_$_PDFExtensionViewControllerPrivate
- __OBJC_METACLASS_RO_$_PDFHostExtensionContext
- __OBJC_METACLASS_RO_$_PDFHostViewController
- __OBJC_METACLASS_RO_$_PDFHostViewControllerPrivate
- __OBJC_METACLASS_RO_$_PDFKitPopupView
- __OBJC_METACLASS_RO_$_PDFKitPopupViewPrivate
- __OBJC_METACLASS_RO_$_PDFPageLabelView
- __OBJC_METACLASS_RO_$_PDFPageLabelViewPrivate
- __OBJC_METACLASS_RO_$_PDFPageViewAnnotationControllerPrivate
- __OBJC_METACLASS_RO_$_PDFScrollViewPrivate
- __OBJC_METACLASS_RO_$_PageSignature
- __OBJC_METACLASS_RO_$_SelectionRectInfo
- __OBJC_METACLASS_RO_$_XPCExtensionInterface
- __OBJC_PROTOCOL_$_PDFExtensionProtocol
- __OBJC_PROTOCOL_$_PDFHostProtocol
- __OBJC_PROTOCOL_REFERENCE_$_PDFExtensionProtocol
- __OBJC_PROTOCOL_REFERENCE_$_PDFHostProtocol
- __ZN10applesauce2CF9ObjectRefIP12CGColorSpaceED1Ev
- __ZN10applesauce2CF9ObjectRefIP14CGDataProviderED1Ev
- __ZN10applesauce2CF9ObjectRefIP7CGImageED2Ev
- __ZN10applesauce2CF9ObjectRefIPK8__CFDataED2Ev
- __ZNKSt3__111__copy_implclB9nqe210106IPU8__strongP20PDFDetectedFormFieldS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
- __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB9nqe210106IP18PDFDetectedFormRowS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
- __ZNKSt3__120__move_backward_implINS_17_ClassicAlgPolicyEEclB9nqe210106IP18PDFDetectedFormRowS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI18PDFDetectedFormRowEEPS2_EclB9nqe210106Ev
- __ZNKSt9type_infoeqB9nqe210106ERKS_
- __ZNSt12length_errorC1B9nqe210106EPKc
- __ZNSt3__110__function12__value_funcIFvP12CGPDFScannerEEC2B9nqe210106EOS5_
- __ZNSt3__110__function12__value_funcIFvP12CGPDFScannerEED2B9nqe210106Ev
- __ZNSt3__110unique_ptrI12CGPDFScannerNS_8functionIFvPS1_EEEE5resetB9nqe210106ES3_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIdN10applesauce2CF9ObjectRefIPK8__CTFontEEEEPvEENS_22__tree_node_destructorINS_9allocatorISC_EEEEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIdU8__strongP13PDFAnnotationEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEED1B9nqe210106Ev
- __ZNSt3__112__destroy_atB9nqe210106INS_4pairIKdN10applesauce2CF9ObjectRefIPK8__CTFontEEEELi0EEEvPT_
- __ZNSt3__114__split_bufferI18PDFDetectedFormRowRNS_9allocatorIS1_EEE5clearB9nqe210106Ev
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorI14ParsedWordDataEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorI18PDFDetectedFormRowEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorI6CGRectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIPK18CGDisplayListEntryEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIU8__strongP20PDFDetectedFormFieldEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorImEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119piecewise_constructE
- __ZNSt3__120__throw_length_errorB9nqe210106EPKc
- __ZNSt3__123__lower_bound_bisectingB9nqe210106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPU8__strongP20PDFDetectedFormFieldEES5_NS_10__identityEZN18PDFDetectedFormRow11insertFieldES4_EUlS4_S4_E_EET0_SB_RKT1_NS_15iterator_traitsISB_E15difference_typeERT3_RT2_
- __ZNSt3__125__throw_bad_function_callB9nqe210106Ev
- __ZNSt3__127__tree_balance_after_insertB9nqe210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI18PDFDetectedFormRowEEPS3_EEED2B9nqe210106Ev
- __ZNSt3__134__uninitialized_allocator_relocateB9nqe210106INS_9allocatorI18PDFDetectedFormRowEEPS2_EEvRT_T0_S7_S7_
- __ZNSt3__13setImNS_4lessImEENS_9allocatorImEEE6insertB9nqe210106INS_21__tree_const_iteratorImPNS_11__tree_nodeImPvEElEEEEvT_SD_
- __ZNSt3__13setImNS_4lessImEENS_9allocatorImEEEC2B9nqe210106ERKS5_
- __ZNSt3__14pairIKdN10applesauce2CF9ObjectRefIPK8__CTFontEEEC2B9nqe210106IRdRS8_Li0EEEOT_OT0_
- __ZNSt3__16__treeINS_12__value_typeIdN10applesauce2CF9ObjectRefIPK8__CTFontEEEENS_19__map_value_compareIdNS_4pairIKdS8_EENS_4lessIdEELb1EEENS_9allocatorISD_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSO_SO_
- __ZNSt3__16__treeINS_12__value_typeIdN10applesauce2CF9ObjectRefIPK8__CTFontEEEENS_19__map_value_compareIdNS_4pairIKdS8_EENS_4lessIdEELb1EEENS_9allocatorISD_EEE25__emplace_unique_key_argsIdJRdRS8_EEENSB_INS_15__tree_iteratorIS9_PNS_11__tree_nodeIS9_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeINS_12__value_typeIdN10applesauce2CF9ObjectRefIPK8__CTFontEEEENS_19__map_value_compareIdNS_4pairIKdS8_EENS_4lessIdEELb1EEENS_9allocatorISD_EEE7destroyEPNS_11__tree_nodeIS9_PvEE
- __ZNSt3__16__treeINS_12__value_typeIdU8__strongP13PDFAnnotationEENS_19__map_value_compareIdNS_4pairIKdS4_EENS_4lessIdEELb1EEENS_9allocatorIS9_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSK_SK_
- __ZNSt3__16__treeINS_12__value_typeIdU8__strongP13PDFAnnotationEENS_19__map_value_compareIdNS_4pairIKdS4_EENS_4lessIdEELb1EEENS_9allocatorIS9_EEE25__emplace_unique_key_argsIdJRKNS_21piecewise_construct_tENS_5tupleIJRS8_EEENSK_IJEEEEEENS7_INS_15__tree_iteratorIS5_PNS_11__tree_nodeIS5_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeINS_12__value_typeIdU8__strongP13PDFAnnotationEENS_19__map_value_compareIdNS_4pairIKdS4_EENS_4lessIdEELb1EEENS_9allocatorIS9_EEE7destroyEPNS_11__tree_nodeIS5_PvEE
- __ZNSt3__16__treeIdNS_4lessIdEENS_9allocatorIdEEE25__emplace_unique_key_argsIdJRKdEEENS_4pairINS_15__tree_iteratorIdPNS_11__tree_nodeIdPvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeImNS_4lessImEENS_9allocatorImEEE12__find_equalImEERPNS_16__tree_node_baseIPvEENS_21__tree_const_iteratorImPNS_11__tree_nodeImS8_EElEERPNS_15__tree_end_nodeISA_EESB_RKT_
- __ZNSt3__16__treeImNS_4lessImEENS_9allocatorImEEE25__emplace_unique_key_argsImJRKmEEENS_4pairINS_15__tree_iteratorImPNS_11__tree_nodeImPvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeImNS_4lessImEENS_9allocatorImEEE25__emplace_unique_key_argsImJmEEENS_4pairINS_15__tree_iteratorImPNS_11__tree_nodeImPvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeImNS_4lessImEENS_9allocatorImEEE30__emplace_hint_unique_key_argsImJRKmEEENS_4pairINS_15__tree_iteratorImPNS_11__tree_nodeImPvEElEEbEENS_21__tree_const_iteratorImSE_lEERKT_DpOT0_
- __ZNSt3__16vectorI14ParsedWordDataNS_9allocatorIS1_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorI14ParsedWordDataNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI18PDFDetectedFormRowNS_9allocatorIS1_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorI18PDFDetectedFormRowNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI18PDFDetectedFormRowNS_9allocatorIS1_EEE30__emplace_back_assume_capacityB9nqe210106IJS1_EEEvDpOT_
- __ZNSt3__16vectorI6CGRectNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI6CGRectNS_9allocatorIS1_EEE8__appendEm
- __ZNSt3__16vectorI6CGRectNS_9allocatorIS1_EEE8__appendEmRKS1_
- __ZNSt3__16vectorIPK18CGDisplayListEntryNS_9allocatorIS3_EEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorIPK18CGDisplayListEntryNS_9allocatorIS3_EEE16__init_with_sizeB9nqe210106IPS3_S8_EEvT_T0_m
- __ZNSt3__16vectorIPK18CGDisplayListEntryNS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE16__init_with_sizeB9nqe210106IPS3_S8_EEvT_T0_m
- __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE18__assign_with_sizeB9nqe210106IPS3_S8_EEvT_T0_l
- __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIdNS_9allocatorIdEEE9push_backB9nqe210106EOd
- __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__19__advanceB9nqe210106INS_21__tree_const_iteratorIdPNS_11__tree_nodeIdPvEElEEEEvRT_NS_15iterator_traitsIS7_E15difference_typeENS_26bidirectional_iterator_tagE
- __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- ___16-[PDFView copy:]_block_invoke
- ___28-[PDFPage pageLayoutIfAvail]_block_invoke
- ___30-[PDFPageLabelView _startFade]_block_invoke
- ___32-[PDFPageLabelView updateEffect]_block_invoke
- ___33-[PDFDocument documentAttributes]_block_invoke
- ___36-[PDFDocumentView _updateVisibility]_block_invoke.158
- ___37-[PDFDocument setDocumentAttributes:]_block_invoke_2
- ___38+[XPCExtensionInterface hostInterface]_block_invoke
- ___39+[PDFHostViewController loadExtension:]_block_invoke
- ___39-[PDFExtensionContext hostToExtension:]_block_invoke
- ___41+[PDFDocument standardDocumentAttributes]_block_invoke
- ___42-[PDFPageView _setuppageAnnotationEffects]_block_invoke
- ___43+[XPCExtensionInterface extensionInterface]_block_invoke
- ___43-[PDFDocument writeToConsumer:withOptions:]_block_invoke.324
- ___43-[PDFHostExtensionContext extensionToHost:]_block_invoke
- ___43-[PDFTextInputView _setDimmingViewVisible:]_block_invoke
- ___43-[PDFTextInputView _setDimmingViewVisible:]_block_invoke_2
- ___43-[PDFTextInputView _setDimmingViewVisible:]_block_invoke_3
- ___44-[PDFPageLayerMarkupAnnotationEffect update]_block_invoke
- ___45-[PDFTextInputView _targetedPreviewForRange:]_block_invoke
- ___47-[PDFViewController _annotationHit:atLocation:]_block_invoke
- ___57-[PDFHostExtensionContext extensionSnapshotToHost:scale:]_block_invoke
- ___57-[PDFHostViewController _setupExtensionInterruptionBlock]_block_invoke
- ___57-[PDFHostViewController _setupExtensionInterruptionBlock]_block_invoke_2
- ___57-[PDFView hitTestForSubviewsOfView:atLocation:withEvent:]_block_invoke
- ___58-[PDFPage fetchPageLayoutWithCompletion:deliveredOnQueue:]_block_invoke
- ___58-[PDFPage fetchPageLayoutWithCompletion:deliveredOnQueue:]_block_invoke_2
- ___58-[PDFTextInputView editMenuForTextRange:suggestedActions:]_block_invoke
- ___59-[PDFViewController activateNextAnnotation:withCompletion:]_block_invoke
- ___59-[PDFViewController activateNextAnnotation:withCompletion:]_block_invoke_2
- ___63+[PDFHostViewController createHostView:forExtensionIdentifier:]_block_invoke
- ___65-[PDFTextInputView decorateFoundTextRange:inDocument:usingStyle:]_block_invoke
- ___65-[PDFTextInputView decorateFoundTextRange:inDocument:usingStyle:]_block_invoke_2
- ___83-[PDFViewController _findNextActivatableAnnotationOnPage:fromAnnotation:direction:]_block_invoke.112
- ___Block_byref_object_copy_.367
- ___Block_byref_object_copy_.49
- ___Block_byref_object_dispose_.368
- ___Block_byref_object_dispose_.50
- ___CGPDFDictionaryCreateNSDictionary_block_invoke
- ___PDFKitDeviceIsiPhone_block_invoke
- ___UpdateRectTransformDictionary_block_invoke
- ___UpdateRectTransformDictionary_block_invoke_2
- ___block_descriptor_40_e33_v32?0"NSValue"8"CALayer"16^B24l
- ___block_descriptor_40_e8_32s_e15_v32?0816^B24ls32l8
- ___block_descriptor_40_e8_32s_e17_v16?0"NSArray"8ls32l8
- ___block_descriptor_40_e8_32s_e26_B24?0r*8^{CGPDFObject=}16ls32l8
- ___block_descriptor_40_e8_32s_e33_v32?0"NSValue"8"CALayer"16^B24ls32l8
- ___block_descriptor_40_e8_32w_e16_v16?0"NSUUID"8lw32l8
- ___block_descriptor_40_e8_32w_e18_v16?0"UIAction"8lw32l8
- ___block_descriptor_48_e8_32s40bs_e54_v32?0"<NSCopying>"8"UIViewController"16"NSError"24ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e15_v32?0816^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s_e36_"CALayer"16?0"SelectionRectInfo"8ls32l8
- ___block_descriptor_56_e8_32s40bs48w_e23_v16?0"PDFAnnotation"8ls32l8w48l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e36_v24?0"NSString"8"PDFAnnotation"16ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48bs56w_e5_v8?0ls32l8s40l8w56l8s48l8
- ___block_descriptor_72_e8_32s40s48r_e23_v32?0"UIView"8Q16^B24ls32l8s40l8r48l8
- ___block_literal_global.1013
- ___block_literal_global.1015
- ___block_literal_global.1018
- ___block_literal_global.117
- ___block_literal_global.120
- ___block_literal_global.121
- ___block_literal_global.123
- ___block_literal_global.184
- ___block_literal_global.187
- ___block_literal_global.189
- ___block_literal_global.191
- ___block_literal_global.213
- ___block_literal_global.215
- ___block_literal_global.219
- ___block_literal_global.317
- ___block_literal_global.324
- ___block_literal_global.366
- ___block_literal_global.45
- ___block_literal_global.53
- ___block_literal_global.537
- ___block_literal_global.540
- ___block_literal_global.542
- ___block_literal_global.583
- ___block_literal_global.73
- ___block_literal_global.77
- ___block_literal_global.929
- ___block_literal_global.931
- ___block_literal_global.933
- ___block_literal_global.941
- ___block_literal_global.943
- ___block_literal_global.945
- ___block_literal_global.953
- ___block_literal_global.983
- ___block_literal_global.985
- ___block_literal_global.987
- ___block_literal_global.991
- ___block_literal_global.993
- _extensionInterface.onceToken
- _extensionInterface.sExtensionInterface
- _hostInterface.onceToken
- _hostInterface.sHostInterface
- _kCAFilterPlusD
- _kCGColorSpaceSRGB
- _loadExtension:.extension
- _loadExtension:.onceToken
- _objc_autorelease
- _objc_msgSend$URLWithString:
- _objc_msgSend$_addPDFAnnotation:
- _objc_msgSend$_addPopupForAnnotation:
- _objc_msgSend$_annotationHit:atLocation:
- _objc_msgSend$_appendPasswordUI
- _objc_msgSend$_auxiliaryConnection
- _objc_msgSend$_buildPDFPageView
- _objc_msgSend$_buildPageLayout
- _objc_msgSend$_convertPoint:fromPDFPageViewController:
- _objc_msgSend$_convertPoint:toPDFPageViewController:
- _objc_msgSend$_dataOwnerForCopy
- _objc_msgSend$_doButtonHit:
- _objc_msgSend$_documentViewSize
- _objc_msgSend$_endPDFViewRotationAnimated:withUpdate:
- _objc_msgSend$_extensionContextForUUID:
- _objc_msgSend$_gestureInit
- _objc_msgSend$_hostScrollViewZoomScale
- _objc_msgSend$_insetBoundsInDocument
- _objc_msgSend$_isTouchingLollipopAtLocationOfFirstTouch:
- _objc_msgSend$_kill:
- _objc_msgSend$_maximumBeamSnappingLength
- _objc_msgSend$_pdfViewInsets
- _objc_msgSend$_pdfViewSafeAreaInsets
- _objc_msgSend$_popoverControllerSourceRect
- _objc_msgSend$_presentPopupView
- _objc_msgSend$_presentPopupView_iOS
- _objc_msgSend$_presentViewController:
- _objc_msgSend$_removeControlForAnnotation
- _objc_msgSend$_resetPDFHostViewControllerViews
- _objc_msgSend$_setCornerRadius:
- _objc_msgSend$_setDimmingViewVisible:
- _objc_msgSend$_setHysteresis:
- _objc_msgSend$_setMaximumZoomScale:
- _objc_msgSend$_setMinimumZoomScale:
- _objc_msgSend$_setupDocumentViewSize
- _objc_msgSend$_setupExtensionInterruptionBlock
- _objc_msgSend$_setupPopupView
- _objc_msgSend$_setuppageAnnotationEffects
- _objc_msgSend$_shouldReplaceStringOnAnnotation:withTextView:
- _objc_msgSend$_typeForGestureRecognizer:
- _objc_msgSend$_updateDocumentIsLocked
- _objc_msgSend$_updateNoteLayer
- _objc_msgSend$_updatePageCount
- _objc_msgSend$_updateTextSelectionPoints
- _objc_msgSend$_zoomToRect:
- _objc_msgSend$addControlForAnnotation:
- _objc_msgSend$addDetectedAnnotation:toPage:
- _objc_msgSend$addLayoutManager:
- _objc_msgSend$addTextContainer:
- _objc_msgSend$addToPageView
- _objc_msgSend$beginFindString:withOptions:
- _objc_msgSend$beginPDFViewRotation
- _objc_msgSend$boldSystemFontOfSize:
- _objc_msgSend$cancelFindStringWithHighlightsCleared:
- _objc_msgSend$clearSearchHighlights
- _objc_msgSend$completePointerInteractionRegionForRequest:
- _objc_msgSend$completeRequestReturningItems:completionHandler:
- _objc_msgSend$contentInsetAdjustmentBehavior
- _objc_msgSend$copy:
- _objc_msgSend$copyAsTextSelection
- _objc_msgSend$didCopy:
- _objc_msgSend$didLongPressPageIndex:atLocation:withAnnotationRect:
- _objc_msgSend$didLongPressURL:atLocation:withAnnotationRect:
- _objc_msgSend$displayGamut
- _objc_msgSend$displayScale
- _objc_msgSend$documentIsLocked:
- _objc_msgSend$endPDFViewRotation
- _objc_msgSend$extensionContext
- _objc_msgSend$extensionInterface
- _objc_msgSend$extensionSnapshotToHost:scale:
- _objc_msgSend$extensionToHost:
- _objc_msgSend$extensionViewBoundsInDocument
- _objc_msgSend$extensionViewController
- _objc_msgSend$extensionViewZoomScale
- _objc_msgSend$extensionWithIdentifier:error:
- _objc_msgSend$fetchPageLayoutWithCompletion:deliveredOnQueue:
- _objc_msgSend$filterWithType:
- _objc_msgSend$findString:withOptions:
- _objc_msgSend$findStringUpdate:done:
- _objc_msgSend$focusOnSearchResultAtIndex:
- _objc_msgSend$goToDestination:point:
- _objc_msgSend$goToPageIndex:
- _objc_msgSend$goToPageIndex:pageFrame:
- _objc_msgSend$goToURL:atLocation:
- _objc_msgSend$handleGesture:
- _objc_msgSend$handleGesture:state:location:locationOfFirstTouch:isIndirectTouch:
- _objc_msgSend$hideActiveMenus
- _objc_msgSend$hideMenu
- _objc_msgSend$hitTest:withEvent:
- _objc_msgSend$hitTestForSubviewsOfView:atLocation:withEvent:
- _objc_msgSend$hostInterface
- _objc_msgSend$hostToExtension:
- _objc_msgSend$hostViewController
- _objc_msgSend$initWithCGImage:scale:orientation:
- _objc_msgSend$initWithData:
- _objc_msgSend$initWithParentAnnotation:owningPageView:owningPDFView:
- _objc_msgSend$initWithProperties:
- _objc_msgSend$initWithSettings:
- _objc_msgSend$instantiateViewControllerWithInputItems:connectionHandler:
- _objc_msgSend$interactWithAnnotation:
- _objc_msgSend$interfaceWithProtocol:
- _objc_msgSend$isUsingPDFExtensionView
- _objc_msgSend$killExtensionProcess
- _objc_msgSend$loadExtension:
- _objc_msgSend$location
- _objc_msgSend$locationOfFirstTouchInView:
- _objc_msgSend$lockWithOptions:seed:
- _objc_msgSend$menuWithChildren:
- _objc_msgSend$pageLayout
- _objc_msgSend$pageLayoutIfAvail
- _objc_msgSend$pdfDocumentViewSize
- _objc_msgSend$pdfHostViewController:didLongPressPageIndex:atLocation:
- _objc_msgSend$pdfHostViewController:didLongPressPageIndex:atLocation:withAnnotationRect:
- _objc_msgSend$pdfHostViewController:didLongPressURL:atLocation:
- _objc_msgSend$pdfHostViewController:didLongPressURL:atLocation:withAnnotationRect:
- _objc_msgSend$pdfHostViewController:documentDidUnlockWithPassword:
- _objc_msgSend$pdfHostViewController:findStringUpdate:done:
- _objc_msgSend$pdfHostViewController:goToPageIndex:
- _objc_msgSend$pdfHostViewController:goToPageIndex:withViewFrustum:
- _objc_msgSend$pdfHostViewController:goToURL:
- _objc_msgSend$pdfHostViewController:goToURL:atLocation:
- _objc_msgSend$pdfHostViewController:updateCurrentPageIndex:
- _objc_msgSend$pdfHostViewController:updatePageCount:
- _objc_msgSend$pdfHostViewControllerDocumentDidRequestPassword:
- _objc_msgSend$pdfHostViewControllerExtensionProcessDidCrash:
- _objc_msgSend$pointerRegionForLocation:
- _objc_msgSend$populateAnnotationsFromDetectedAnnotationsOnPage:
- _objc_msgSend$positionFromPosition:inDirection:offset:
- _objc_msgSend$recievedSnapshotViewRect:
- _objc_msgSend$regionWithRect:identifier:
- _objc_msgSend$registerUndoWithTarget:selector:object:
- _objc_msgSend$remoteObjectProxy
- _objc_msgSend$removeControlForAnnotation:
- _objc_msgSend$removeFromPageView
- _objc_msgSend$renderInContext:
- _objc_msgSend$selectAll
- _objc_msgSend$selectAll:
- _objc_msgSend$setAdjustsFontSizeToFitWidth:
- _objc_msgSend$setAllowsGroupOpacity:
- _objc_msgSend$setCurrentPageNumber:forPageCount:
- _objc_msgSend$setDocumentData:
- _objc_msgSend$setDocumentMargins:
- _objc_msgSend$setExtensionViewController:
- _objc_msgSend$setExtraContentStream:steamDocument:
- _objc_msgSend$setHasSelection:
- _objc_msgSend$setHighlightedSelections:
- _objc_msgSend$setHostViewController:
- _objc_msgSend$setIsUsingPDFExtensionView:
- _objc_msgSend$setOpaque:
- _objc_msgSend$setRequestInterruptionBlock:
- _objc_msgSend$setScale:
- _objc_msgSend$setStringValue:onChoiceWidgetAnnotation:withTableView:
- _objc_msgSend$setStringValue:onChoiceWidgetAnnotation:withTextField:
- _objc_msgSend$setStringValue:onTextWidgetAnnotation:withTextView:
- _objc_msgSend$setTextSelectionPoints:right:
- _objc_msgSend$setUseIOSurfaceForTiles:
- _objc_msgSend$settingsForPrivateStyle:
- _objc_msgSend$setup
- _objc_msgSend$setupDocumentViewSize:
- _objc_msgSend$setupPDFView
- _objc_msgSend$sharedMenuController
- _objc_msgSend$showMarkupStyleMenuForMarkupAnnotation
- _objc_msgSend$showMenuForMarkupAnnotation:
- _objc_msgSend$showMenuFromView:rect:
- _objc_msgSend$showSelectionRect:
- _objc_msgSend$showTextSelectionMenu:selectionRect:
- _objc_msgSend$snapshotViewRect:forWidth:afterScreenUpdates:
- _objc_msgSend$standardDocumentAttributes
- _objc_msgSend$tableView:didSelectRowAtIndexPath:
- _objc_msgSend$timeIntervalSinceReferenceDate
- _objc_msgSend$unlockWithOptions:seed:
- _objc_msgSend$updateAutoScaleFactor
- _objc_msgSend$updateCurrentPageIndex:
- _objc_msgSend$updateDocumentIsLocked:
- _objc_msgSend$updateDocumentViewSize
- _objc_msgSend$updateEffect
- _objc_msgSend$updatePDFViewLayout
- _objc_msgSend$updatePDFViewLayout:scrollViewFrame:safeAreaInsets:zoomScale:
- _objc_msgSend$updatePDFViewLayout:scrollViewFrame:zoomScale:
- _objc_msgSend$updatePageCount:
- _objc_msgSend$zoomToRect:
- _objc_msgSend$zoomToRect:animated:
- _standardDocumentAttributes.onceToken
- _standardDocumentAttributes.standardAttributes
CStrings:
+ "#%02X"
+ "%02x"
+ "%c"
+ "%s: Calling CGPDFPageInsertAnnotationAtIndex(): annotationDict:  : %@"
+ "%s: Found invalid _cgAnnotation %p (no backing dictionary). Releasing."
+ "%s: cgAnnotation is NULL! Not inserting."
+ "+"
+ "-"
+ "-[PDFAnnotation ensureCGPDFAnnotation]"
+ "-[PDFPage insertAnnotation:atIndex:]"
+ "/AppleInternal/Library/BuildRoots/4~CQDKugCEviD0n23jDL0UhvNSIBpKzXg3fVCjF6Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/System/Library/Frameworks/CoreGraphics.framework/PrivateHeaders/CGBuf.h"
+ "/AppleInternal/Library/BuildRoots/4~CQDKugCEviD0n23jDL0UhvNSIBpKzXg3fVCjF6Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQDKugCEviD0n23jDL0UhvNSIBpKzXg3fVCjF6Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1156: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQDKugCEviD0n23jDL0UhvNSIBpKzXg3fVCjF6Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:413: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/BE"
+ "/DS"
+ "/OC"
+ "/RD"
+ "/Vertices"
+ "5"
+ "AAPL:AKIdentityHash"
+ "AAPL:Hash"
+ "AAPL:PaperKit"
+ "AIGC"
+ "B!"
+ "B16@?0@\"PDFPageView\"8"
+ "CGPDFStreamCreateWithDisplayList failed for displayList: %@"
+ "Cannot convert point, pageIndex is OOB for layout. range: (idx=%lu size=%zu)"
+ "CoreGraphics"
+ "D:%@%@%02ld'%02ld'"
+ "D:%@Z00'00'"
+ "E1!"
+ "Error: Cycle detected while converting value to CGPDFObject. Skipping value."
+ "HasExtendedColorDisplay"
+ "MutablePDF"
+ "PDFAnnotationChangedAnnotationKeyUserInfoKey"
+ "PDFAnnotationDidSetValueForAnnotationKey"
+ "PDFKit warning: quadPoints array has odd number of elements (%lu), expected pairs of coordinates"
+ "PDFViewActiveAnnotationChangedNotification"
+ "Q1"
+ "Unexpected object type in quadPoints array: %@"
+ "ViewLayout"
+ "calculateIconPlacementInfoFromQuads: failed"
+ "com.apple.PDFKit.AnnotationAppearanceQueue"
+ "com.apple.PDFKit.AnnotationLongPress"
+ "com.apple.PDFKit.AnnotationPan"
+ "com.apple.PDFKit.AnnotationPopupTap"
+ "com.apple.PDFKit.AnnotationPress"
+ "com.apple.PDFKit.AnnotationTap"
+ "com.apple.PDFKit.DeepPress"
+ "com.apple.PDFKit.DoubleTap"
+ "com.apple.PDFKit.FormFillingDoubleTap"
+ "com.apple.PDFKit.LongPress"
+ "com.apple.PDFKit.ScannerResult"
+ "com.apple.PDFKit.TableCellDrag"
+ "com.apple.PDFKit.TableCellTap"
+ "com.apple.PDFKit.Tap"
+ "com.apple.PDFKit.TouchPageSwipe"
+ "com.apple.iBooks"
+ "convertPoint:toPage: called with page from foreign document (%p vs %p)"
+ "debugEffectsLayer"
+ "en_US_POSIX"
+ "text.bubble.fill"
+ "v16@?0@\"<PDFPageObserver>\"8"
+ "v16@?0@\"NSString\"8"
+ "v16@?0@\"PDFAnnotationManager\"8"
+ "v16@?0@\"UITapGestureRecognizer\"8"
+ "v24@?0@\"PDFPageView\"8@\"PDFPage\"16"
+ "v24@?0@\"PDFPageView\"8Q16"
+ "v32@?0@\"NSString\"8@16^B24"
+ "yyyyMMddHHmmss"
- "#16@0:8"
- "#24@0:8@16"
- "#24@0:8^{CGPDFDictionary=}16"
- "%d of %d"
- ".cxx_construct"
- ".cxx_destruct"
- "/AppleInternal/Library/BuildRoots/4~CNqTugDeA3-nwofOoaEHP9o3PKTxNhKjLVpdP2g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/System/Library/Frameworks/CoreGraphics.framework/PrivateHeaders/CGBuf.h"
- "@"
- "@\"<CAAction>\"32@0:8@\"CALayer\"16@\"NSString\"24"
- "@\"<NSCopying>\""
- "@\"<NSObject><NSCopying>\"16@0:8"
- "@\"<PDFAKControllerDelegateProtocol>\""
- "@\"<PDFDocumentPageChangeDelegate>\""
- "@\"<PDFExtensionProtocol>\""
- "@\"<PDFHostProtocol>\""
- "@\"<PDFHostViewControllerDelegate>\""
- "@\"<PDFPageBackgroundManagerDelegate>\""
- "@\"<PDFPageLayerInterface>\""
- "@\"<PDFPageOverlayViewProvider>\""
- "@\"<PDFTextInputDelegate>\""
- "@\"<PDFThumbnailContextMenuDelegate>\""
- "@\"<PDFThumbnailDataSourceDelegate>\""
- "@\"<PDFThumbnailIconsViewProtocol>\"16@0:8"
- "@\"<PDFTilePoolDelegate>\""
- "@\"<PDFViewDelegate>\""
- "@\"<UITextInputDelegate>\""
- "@\"<UITextInputDelegate>\"16@0:8"
- "@\"<UITextInputTokenizer>\""
- "@\"<UITextInputTokenizer>\"16@0:8"
- "@\"<UITextSearchAggregator>\""
- "@\"AKAnnotation\""
- "@\"AKAnnotation\"16@0:8"
- "@\"AKController\""
- "@\"AKInkAnnotation\""
- "@\"AKPageModelController\""
- "@\"AKRectAnnotation\""
- "@\"AKToolbarView\""
- "@\"CALayer\""
- "@\"CALayer\"16@?0@\"SelectionRectInfo\"8"
- "@\"CALayer\"32@0:8Q16@\"AKController\"24"
- "@\"CALayer<PDFPageLayerInterface>\""
- "@\"CRNormalizedQuad\"16@0:8"
- "@\"DDScannerResult\""
- "@\"NSArray\""
- "@\"NSArray\"24@0:8@\"UITextRange\"16"
- "@\"NSArray\"32@0:8@\"AKController\"16@\"NSArray\"24"
- "@\"NSArray\"40@0:8@\"NSIndexSet\"16Q24@\"AKController\"32"
- "@\"NSArray\"40@0:8@\"UICollectionView\"16@\"<UIDragSession>\"24@\"NSIndexPath\"32"
- "@\"NSArray\"40@0:8@\"UITextView\"16{_NSRange=QQ}24"
- "@\"NSArray\"56@0:8@\"UICollectionView\"16@\"<UIDragSession>\"24@\"NSIndexPath\"32{CGPoint=dd}40"
- "@\"NSAttributedString\""
- "@\"NSAttributedString\"24@0:8@\"UITextRange\"16"
- "@\"NSCache\""
- "@\"NSData\"76@0:8B16d20{CGRect={CGPoint=dd}{CGSize=dd}}28Q60@\"AKController\"68"
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSDictionary\"32@0:8@\"UITextPosition\"16q24"
- "@\"NSExtension\""
- "@\"NSHashTable\""
- "@\"NSIndexPath\"24@0:8@\"UICollectionView\"16"
- "@\"NSIndexPath\"40@0:8@\"UICollectionView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "@\"NSIndexPath\"48@0:8@\"UICollectionView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32@\"NSIndexPath\"40"
- "@\"NSIndexSet\""
- "@\"NSIndexSet\"32@0:8Q16@\"AKController\"24"
- "@\"NSIndexSet\"40@0:8@\"NSArray\"16Q24@\"AKController\"32"
- "@\"NSInvocation\""
- "@\"NSLayoutConstraint\""
- "@\"NSLock\""
- "@\"NSMapTable\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableIndexSet\""
- "@\"NSMutableSet\""
- "@\"NSObject\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSObject<PDFPageLayerGeometryInterface>\""
- "@\"NSObject<PDFPageLayerGeometryInterface>\"16@0:8"
- "@\"NSObject<PDFPasswordViewControllerDelegate>\""
- "@\"NSOrderedSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"UITextRange\"16"
- "@\"NSString\"24@0:8d16"
- "@\"NSTextStorage\""
- "@\"NSTextStorage\"16@0:8"
- "@\"NSTimer\""
- "@\"NSURL\""
- "@\"NSUUID\""
- "@\"NSUndoManager\""
- "@\"NSUndoManager\"24@0:8@\"AKController\"16"
- "@\"PDFAKAnnotationAdaptor\""
- "@\"PDFAKAnnotationAdaptorPrivate\""
- "@\"PDFAKDocumentAdaptor\""
- "@\"PDFAKPageAdaptor\""
- "@\"PDFAKPageAdaptorPrivate\""
- "@\"PDFAKPageOverlayViewProvider\""
- "@\"PDFAccessibilityNode\""
- "@\"PDFAction\""
- "@\"PDFActionGoToPrivateVars\""
- "@\"PDFActionNamedPrivateVars\""
- "@\"PDFActionPrivate\""
- "@\"PDFActionRemoteGoToPrivateVars\""
- "@\"PDFActionResetFormPrivateVars\""
- "@\"PDFActionURLPrivateVars\""
- "@\"PDFAnnotation\""
- "@\"PDFAnnotationChangePrivate\""
- "@\"PDFAnnotationFreeTextPrivateVars\""
- "@\"PDFAnnotationPointerTrackingView\""
- "@\"PDFAppearanceCharacteristicsPrivate\""
- "@\"PDFBorderPrivateVars\""
- "@\"PDFCoachMarkManager\""
- "@\"PDFCoachMarkManagerPrivate\""
- "@\"PDFDestination\""
- "@\"PDFDestinationPrivate\""
- "@\"PDFDetectedForm\""
- "@\"PDFDetectedFormField\""
- "@\"PDFDocument\""
- "@\"PDFDocument\"16@0:8"
- "@\"PDFDocumentContentView\""
- "@\"PDFDocumentView\""
- "@\"PDFDocumentViewController\""
- "@\"PDFDocumentViewControllerPrivate\""
- "@\"PDFDocumentViewPrivate\""
- "@\"PDFExtensionTopView\""
- "@\"PDFExtensionViewController\""
- "@\"PDFExtensionViewControllerPrivate\""
- "@\"PDFForm\""
- "@\"PDFFormFieldPrivateVars\""
- "@\"PDFFormPrivateVars\""
- "@\"PDFHighlightDetectedFormFieldsEffectLayer\""
- "@\"PDFHostViewController\""
- "@\"PDFHostViewControllerPrivate\""
- "@\"PDFKitPopupViewPrivate\""
- "@\"PDFKitTextViewPrivate\""
- "@\"PDFOutline\""
- "@\"PDFOutlinePrivate\""
- "@\"PDFOverlayViewsController\""
- "@\"PDFPage\""
- "@\"PDFPage\"16@0:8"
- "@\"PDFPageBackgroundManager\""
- "@\"PDFPageIconLayer\""
- "@\"PDFPageLabelView\""
- "@\"PDFPageLabelViewPrivate\""
- "@\"PDFPageLayer\""
- "@\"PDFPageLayerEffect\""
- "@\"PDFPageLayerEffect\"24@0:8@\"NSUUID\"16"
- "@\"PDFPageLayerEffectPrivate\""
- "@\"PDFPageRangePrivate\""
- "@\"PDFPageView\""
- "@\"PDFPageViewAnnotationController\""
- "@\"PDFPageViewAnnotationControllerPrivate\""
- "@\"PDFPageViewController\""
- "@\"PDFPageViewControllerPrivate\""
- "@\"PDFPageViewPrivate\""
- "@\"PDFPanGestureRecognizer\""
- "@\"PDFPasswordViewController\""
- "@\"PDFPointerRegionPrivate\""
- "@\"PDFRenderingProperties\""
- "@\"PDFRenderingProperties\"16@0:8"
- "@\"PDFRevealManagerPrivate\""
- "@\"PDFScannerResult\""
- "@\"PDFScannerResultPrivate\""
- "@\"PDFScrollView\""
- "@\"PDFScrollViewPrivate\""
- "@\"PDFSelection\""
- "@\"PDFTableCellSelection\""
- "@\"PDFTextInputView\""
- "@\"PDFTextPosition\""
- "@\"PDFTextSearchAggregator\""
- "@\"PDFTextWidgetTextView\""
- "@\"PDFThumbnailView\""
- "@\"PDFTilePoolPrivate\""
- "@\"PDFTileSurface\""
- "@\"PDFTimer\""
- "@\"PDFTimerPrivate\""
- "@\"PDFView\""
- "@\"PDFView\"16@0:8"
- "@\"PDFViewController\""
- "@\"PDFViewControllerPrivate\""
- "@\"PDFViewDebugFlags\""
- "@\"PDFViewLayout\""
- "@\"PDFViewLayoutPrivate\""
- "@\"PDFViewPrivate\""
- "@\"PKDrawing\""
- "@\"RVPresenter\""
- "@\"UIAction\"40@0:8@\"UITextView\"16@\"UITextItem\"24@\"UIAction\"32"
- "@\"UIButton\""
- "@\"UICollectionView\""
- "@\"UICollectionViewDiffableDataSource\""
- "@\"UICollectionViewDropProposal\"40@0:8@\"UICollectionView\"16@\"<UIDropSession>\"24@\"NSIndexPath\"32"
- "@\"UICollectionViewTransitionLayout\"40@0:8@\"UICollectionView\"16@\"UICollectionViewLayout\"24@\"UICollectionViewLayout\"32"
- "@\"UIColor\""
- "@\"UIColor\"16@0:8"
- "@\"UIColor\"24@0:8@\"AKAnnotationRendererOptions\"16"
- "@\"UIContextMenuConfiguration\"40@0:8@\"UIContextMenuInteraction\"16{CGPoint=dd}24"
- "@\"UIContextMenuConfiguration\"48@0:8@\"UICollectionView\"16@\"NSArray\"24{CGPoint=dd}32"
- "@\"UIContextMenuConfiguration\"48@0:8@\"UICollectionView\"16@\"NSIndexPath\"24{CGPoint=dd}32"
- "@\"UIConversationContext\"16@0:8"
- "@\"UIDocumentPasswordView\""
- "@\"UIDragInteraction\""
- "@\"UIDragPreviewParameters\"32@0:8@\"UICollectionView\"16@\"NSIndexPath\"24"
- "@\"UIEditMenuInteraction\""
- "@\"UIFindInteraction\""
- "@\"UIFindSession\"32@0:8@\"UIFindInteraction\"16@\"UIView\"24"
- "@\"UIImage\""
- "@\"UIImage\"32@0:8@\"PDFPage\"16^i24"
- "@\"UIImageView\""
- "@\"UILabel\""
- "@\"UILongPressGestureRecognizer\""
- "@\"UIMenu\"32@0:8@\"UITextRange\"16@\"NSArray\"24"
- "@\"UIMenu\"40@0:8@\"UIEditMenuInteraction\"16@\"UIEditMenuConfiguration\"24@\"NSArray\"32"
- "@\"UIMenu\"40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSArray\"32"
- "@\"UIMenu\"48@0:8@\"UITextView\"16{_NSRange=QQ}24@\"NSArray\"40"
- "@\"UIPointerInteraction\""
- "@\"UIPointerRegion\"40@0:8@\"UIPointerInteraction\"16@\"UIPointerRegionRequest\"24@\"UIPointerRegion\"32"
- "@\"UIPointerStyle\"32@0:8@\"UIPointerInteraction\"16@\"UIPointerRegion\"24"
- "@\"UIScrollView\""
- "@\"UITapGestureRecognizer\""
- "@\"UITargetedPreview\"32@0:8@\"UICollectionView\"16@\"UIContextMenuConfiguration\"24"
- "@\"UITargetedPreview\"32@0:8@\"UIContextMenuInteraction\"16@\"UIContextMenuConfiguration\"24"
- "@\"UITargetedPreview\"40@0:8@\"UICollectionView\"16@\"UIContextMenuConfiguration\"24@\"NSIndexPath\"32"
- "@\"UITargetedPreview\"40@0:8@\"UIContextMenuInteraction\"16@\"UIContextMenuConfiguration\"24@\"<NSCopying>\"32"
- "@\"UITextHighlightView\""
- "@\"UITextInputPasswordRules\"16@0:8"
- "@\"UITextInteraction\""
- "@\"UITextItemMenuConfiguration\"40@0:8@\"UITextView\"16@\"UITextItem\"24@\"UIMenu\"32"
- "@\"UITextPlaceholder\"32@0:8{CGSize=dd}16"
- "@\"UITextPosition\"16@0:8"
- "@\"UITextPosition\"32@0:8@\"UITextPosition\"16q24"
- "@\"UITextPosition\"32@0:8@\"UITextRange\"16q24"
- "@\"UITextPosition\"32@0:8{CGPoint=dd}16"
- "@\"UITextPosition\"40@0:8@\"UITextPosition\"16q24q32"
- "@\"UITextPosition\"40@0:8{CGPoint=dd}16@\"UITextRange\"32"
- "@\"UITextRange\""
- "@\"UITextRange\"16@0:8"
- "@\"UITextRange\"32@0:8@\"UITextPosition\"16@\"UITextPosition\"24"
- "@\"UITextRange\"32@0:8@\"UITextPosition\"16q24"
- "@\"UITextRange\"32@0:8{CGPoint=dd}16"
- "@\"UITextSearchingDimmingView\""
- "@\"UITextView\""
- "@\"UITraitCollection\""
- "@\"UIView\""
- "@\"UIView\"16@0:8"
- "@\"UIView\"24@0:8@\"UIScrollView\"16"
- "@\"UIView\"32@0:8@\"PDFView\"16@\"PDFPage\"24"
- "@\"UIView<PDFThumbnailCollectionViewInterface>\""
- "@\"UIViewController\""
- "@\"UIViewController\"24@0:8@\"AKController\"16"
- "@\"UIViewController\"32@0:8@\"UIPageViewController\"16@\"UIViewController\"24"
- "@\"UIWindowSceneActivationConfiguration\"48@0:8@\"UICollectionView\"16@\"NSIndexPath\"24{CGPoint=dd}32"
- "@\"VKImageAnalyzer\""
- "@\"_UIBackdropView\""
- "@100@0:8{CGPoint=dd}16{CGPoint=dd}32i48{?=qq}52{CGRect={CGPoint=dd}{CGSize=dd}}68"
- "@116@0:8@16{CGPoint=dd}24@40{CGPoint=dd}48i64{?=qq}68{CGRect={CGPoint=dd}{CGSize=dd}}84"
- "@116@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48{CGAffineTransform=dddddd}56d104i112"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@\"PDFThumbnailView\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8Q16"
- "@24@0:8^v16"
- "@24@0:8^{CGDataProvider=}16"
- "@24@0:8^{CGImageSource=}16"
- "@24@0:8^{CGPDFDictionary=}16"
- "@24@0:8^{CGPDFDocument=}16"
- "@24@0:8^{CGPDFPage=}16"
- "@24@0:8^{CGPDFString=}16"
- "@24@0:8^{CGPDFTaggedNode=}16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8d16"
- "@24@0:8q16"
- "@28@0:8^{CGPDFFont=}16f24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@32@0:8@16^i24"
- "@32@0:8@16^{CGPDFDictionary=}24"
- "@32@0:8@16q24"
- "@32@0:8@?16@24"
- "@32@0:8Q16@24"
- "@32@0:8Q16^i24"
- "@32@0:8^{CGColor=}16d24"
- "@32@0:8^{CGImage=}16@24"
- "@32@0:8^{CGPDFAnnotation=}16@24"
- "@32@0:8^{CGPDFAnnotation=}16^{CGPDFDictionary=}24"
- "@32@0:8^{CGPDFDictionary=}16@24"
- "@32@0:8^{CGPDFDictionary=}16q24"
- "@32@0:8^{CGPDFPageLayoutTable=}16@24"
- "@32@0:8^{CGPDFSelection=}16d24"
- "@32@0:8q16@24"
- "@32@0:8{CGPoint=dd}16"
- "@32@0:8{CGSize=dd}16"
- "@32@0:8{_NSRange=QQ}16"
- "@36@0:8@16i24@28"
- "@36@0:8{CGPoint=dd}16B32"
- "@36@0:8{CGPoint=dd}16i32"
- "@36@0:8{_NSRange=QQ}16B32"
- "@40@0:8:16@24@32"
- "@40@0:8@\"PDFPage\"16@\"NSObject<PDFPageLayerGeometryInterface>\"24@\"PDFRenderingProperties\"32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24Q32"
- "@40@0:8@16@24q32"
- "@40@0:8@16Q24@32"
- "@40@0:8@16Q24q32"
- "@40@0:8@16^{CGPDFAnnotation=}24^{CGPDFDictionary=}32"
- "@40@0:8@16^{CGPDFStream=}24^{CGPDFDictionary=}32"
- "@40@0:8@16q24@32"
- "@40@0:8@16q24q32"
- "@40@0:8@16{CGPoint=dd}24"
- "@40@0:8@16{_NSRange=QQ}24"
- "@40@0:8^{CGPDFDictionary=}16@24@32"
- "@40@0:8^{CGPDFObject=}16^{__CFSet=}24^B32"
- "@40@0:8^{CGPoint=dd}16{CGPoint=dd}24"
- "@40@0:8^{__CFData=}16@24@32"
- "@40@0:8d16:24@32"
- "@40@0:8{CGPoint=dd}16@32"
- "@40@0:8{CGSize=dd}16q32"
- "@44@0:8@16^{CGPDFAnnotation=}24^{CGPDFDictionary=}32B40"
- "@44@0:8{CGSize=dd}16q32B40"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24Q32@?40"
- "@48@0:8@16@24{CGPoint=dd}32"
- "@48@0:8@16Q24@32Q40"
- "@48@0:8@16q24q32@40"
- "@48@0:8@16{CGPoint=dd}24@40"
- "@48@0:8@16{_NSRange=QQ}24@40"
- "@48@0:8Q16{CGPoint=dd}24@40"
- "@48@0:8{CGPoint=dd}16{CGPoint=dd}32"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@48@0:8{CGSize=dd}16q32@40"
- "@48@0:8{CGSize=dd}16q32B40B44"
- "@52@0:8{CGPoint=dd}16{CGPoint=dd}32i48"
- "@56@0:8@16@24@32{CGPoint=dd}40"
- "@56@0:8@16Q24q32@40@48"
- "@56@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "@56@0:8Q16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "@56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48"
- "@56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16q48"
- "@64@0:8@16{CGPoint=dd}24@40{CGPoint=dd}48"
- "@64@0:8Q16{CGRect={CGPoint=dd}{CGSize=dd}}24q56"
- "@64@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48@56"
- "@68@0:8@16{CGPoint=dd}24@40{CGPoint=dd}48i64"
- "@72@0:8@16{CGPoint=dd}24@40{CGPoint=dd}48Q64"
- "@72@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48@56@64"
- "@76@0:8B16d20{CGRect={CGPoint=dd}{CGSize=dd}}28Q60@68"
- "@80@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48@56@64Q72"
- "@80@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48"
- "@?"
- "@?16@0:8"
- "@?<v@?@\"CALayer\">16@0:8"
- "AB"
- "AKChildAnnotationProtocol"
- "AKControllerDelegateProtocol"
- "AKParentAnnotationProtocol"
- "AKSignaturesControllerDelegate"
- "AKTextAnnotationProtocol"
- "Aixt/MEN2O2B7f+8m4TxUA"
- "B104@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24@56@64q72i80B84^{CGContext=}88@96"
- "B16@0:8"
- "B20@0:8B16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"AKController\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"UIGestureRecognizer\"16"
- "B24@0:8@\"UIScrollView\"16"
- "B24@0:8@\"UITextView\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B24@0:8^{CGDataConsumer=}16"
- "B24@0:8^{CGPDFArray=}16"
- "B24@0:8^{CGPDFDictionary=}16"
- "B24@0:8^{CGPDFPage=}16"
- "B24@0:8^{CGPath=}16"
- "B24@0:8^{__CFDictionary=}16"
- "B24@?0r*8^{CGPDFObject=}16"
- "B28@0:8B16@20"
- "B28@0:8Q16B24"
- "B32@0:8:16@24"
- "B32@0:8@\"AKAnnotation\"16@\"AKController\"24"
- "B32@0:8@\"AKController\"16q24"
- "B32@0:8@\"NSString\"16@\"PDFPasswordViewController\"24"
- "B32@0:8@\"UICollectionView\"16@\"<UIDragSession>\"24"
- "B32@0:8@\"UICollectionView\"16@\"<UIDropSession>\"24"
- "B32@0:8@\"UICollectionView\"16@\"NSIndexPath\"24"
- "B32@0:8@\"UICollectionView\"16@\"UICollectionViewFocusUpdateContext\"24"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UIEvent\"24"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UIGestureRecognizer\"24"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UIPress\"24"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UITouch\"24"
- "B32@0:8@\"UITextRange\"16@\"NSString\"24"
- "B32@0:8@16:24"
- "B32@0:8@16@24"
- "B32@0:8@16Q24"
- "B32@0:8@16^{CGPDFDictionary=}24"
- "B32@0:8@16q24"
- "B32@0:8Q16^i24"
- "B32@0:8^Q16^i24"
- "B32@0:8^{CGDataConsumer=}16@24"
- "B32@0:8{CGPoint=dd}16"
- "B36@0:8@16@24B32"
- "B40@0:8@\"AKController\"16@\"AKAnnotation\"24@\"AKPageModelController\"32"
- "B40@0:8@\"UICollectionView\"16@\"NSIndexPath\"24@\"<UISpringLoadedInteractionContext>\"32"
- "B40@0:8@\"UITextInteraction\"16{CGPoint=dd}24"
- "B40@0:8@\"UITextRange\"16@\"<NSObject><NSCopying>\"24@\"NSString\"32"
- "B40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSString\"32"
- "B40@0:8@16@24@32"
- "B40@0:8@16{CGPoint=dd}24"
- "B40@0:8Q16@24@32"
- "B40@0:8{CGPoint=dd}16@32"
- "B40@0:8{CGPoint=dd}16Q32"
- "B40@0:8{CGPoint=dd}16^q32"
- "B48@0:8@\"UICollectionView\"16:24@\"NSIndexPath\"32@40"
- "B48@0:8@\"UITextView\"16@\"NSTextAttachment\"24{_NSRange=QQ}32"
- "B48@0:8@\"UITextView\"16@\"NSURL\"24{_NSRange=QQ}32"
- "B48@0:8@\"UITextView\"16{_NSRange=QQ}24@\"NSString\"40"
- "B48@0:8@16:24@32@40"
- "B48@0:8@16@24{_NSRange=QQ}32"
- "B48@0:8@16^{__CVBuffer=}24@32q40"
- "B48@0:8@16{_NSRange=QQ}24@40"
- "B48@0:8{CGPoint=dd}16Q32@\"AKController\"40"
- "B48@0:8{CGPoint=dd}16Q32@40"
- "B48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "B56@0:8@\"UITextView\"16@\"NSTextAttachment\"24{_NSRange=QQ}32q48"
- "B56@0:8@\"UITextView\"16@\"NSURL\"24{_NSRange=QQ}32q48"
- "B56@0:8@16@24{_NSRange=QQ}32q48"
- "B56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48"
- "B64@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24@56"
- "B64@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16Q48@\"AKController\"56"
- "B64@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16Q48@56"
- "CALayerDelegate"
- "CGColor"
- "CGContext"
- "CGImage"
- "CGPDFAnnotation"
- "CGPath"
- "CGPointValue"
- "CGRectValue"
- "CRDirectionalRegion"
- "CRFormFieldProviding"
- "CRRegion"
- "DisableAnnotationKit"
- "EnableAnnotationKit"
- "Error - undefined state in [PDFViewController _doButtonHit]"
- "FindFirstResponder"
- "I16@0:8"
- "MarkupTypeForMarkupStyle:"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "PDFAKAnnotationAdaptor"
- "PDFAKAnnotationAdaptorPrivate"
- "PDFAKAnnotationSerializationHelper"
- "PDFAKControllerDelegate"
- "PDFAKPageAdaptor"
- "PDFAKPageAdaptorPrivate"
- "PDFAKPageOverlayViewProvider"
- "PDFAction"
- "PDFActionGoTo"
- "PDFActionGoToPrivateVars"
- "PDFActionNamed"
- "PDFActionNamedPrivateVars"
- "PDFActionPrivate"
- "PDFActionRemoteGoTo"
- "PDFActionRemoteGoToPrivateVars"
- "PDFActionResetForm"
- "PDFActionResetFormPrivateVars"
- "PDFActionURL"
- "PDFActionURLPrivateVars"
- "PDFAnnotationCGPDFObject"
- "PDFAnnotationChange"
- "PDFAnnotationChangePrivate"
- "PDFAnnotationDrawing"
- "PDFAnnotationEditMenuConfiguration"
- "PDFAnnotationFreeText"
- "PDFAnnotationFreeTextPrivateVars"
- "PDFAnnotationKeysForRedactionDiscoverability"
- "PDFAnnotationKeysWithStringValues"
- "PDFAnnotationPKDrawing"
- "PDFAnnotationPointerTrackingView"
- "PDFAnnotationUtilities"
- "PDFAppearanceCharacteristics"
- "PDFAppearanceCharacteristicsPrivate"
- "PDFBlockQueuePair"
- "PDFBorder"
- "PDFBorderPrivateVars"
- "PDFCGPDFUtilities"
- "PDFCoachMark"
- "PDFCoachMarkManager"
- "PDFCoachMarkManagerPrivate"
- "PDFDestination"
- "PDFDestinationPrivate"
- "PDFDetectedForm"
- "PDFDetectedFormField"
- "PDFDocumentAsyncFindDelegate"
- "PDFDocumentContentView"
- "PDFDocumentPageChangeDelegate"
- "PDFDocumentView"
- "PDFDocumentViewController"
- "PDFDocumentViewControllerPrivate"
- "PDFDocumentViewPrivate"
- "PDFExtensionContext"
- "PDFExtensionProtocol"
- "PDFExtensionTopView"
- "PDFExtensionViewAnnotationLongPress"
- "PDFExtensionViewController"
- "PDFExtensionViewControllerPrivate"
- "PDFExtensionViewGoToDestination"
- "PDFExtensionViewGoToPage"
- "PDFExtensionViewZoomToRect"
- "PDFExtensions"
- "PDFForm"
- "PDFFormField"
- "PDFFormFieldBackgroundColor"
- "PDFFormFieldPrivateVars"
- "PDFFormPrivateVars"
- "PDFHighlightDetectedFormFieldsEffectLayer"
- "PDFHostExtensionContext"
- "PDFHostProtocol"
- "PDFHostViewController"
- "PDFHostViewController failed to initialize."
- "PDFHostViewController failed to load extension \"%@\". error: %@"
- "PDFHostViewController proxy failed to initialize."
- "PDFHostViewController.contentInsetPropertyObservationContext"
- "PDFHostViewControllerPrivate"
- "PDFIconCollectionViewCell_iOS"
- "PDFKVOObserver"
- "PDFKitAnnotationKeys"
- "PDFKitAnnotationUndoManagerDisplayNames"
- "PDFKitAppearanceDictionaryArray"
- "PDFKitBorderStyleArray"
- "PDFKitDebug"
- "PDFKitDebugging"
- "PDFKitDocumentVisibleRectIncludingContentInsets"
- "PDFKitDumpToFile"
- "PDFKitEnclosingScrollView"
- "PDFKitFieldTypeArray"
- "PDFKitHandleBackTabInTextWidget:"
- "PDFKitHandleTabInTextWidget:"
- "PDFKitHighlightingModeArray"
- "PDFKitPDFPointValue"
- "PDFKitPDFRectValue"
- "PDFKitPopupView"
- "PDFKitPopupViewPrivate"
- "PDFKitSignatureView"
- "PDFKitSubtypeArray"
- "PDFKitTextView"
- "PDFKitTextViewPrivate"
- "PDFKitUIFontExtensions"
- "PDFKitUIViewExtensions"
- "PDFKitValueWithPDFPoint:"
- "PDFKitValueWithPDFRect:"
- "PDFLayout"
- "PDFMarkupColors"
- "PDFMarkupMenuUtilities"
- "PDFMarkupStyleLabels"
- "PDFMarkupStyleView"
- "PDFOutline"
- "PDFOutlinePrivate"
- "PDFOverlayViewsController"
- "PDFOverlayViewsController_ios"
- "PDFPage"
- "PDFPageAnalyzer"
- "PDFPageAnalyzerV2"
- "PDFPageBackgroundManager"
- "PDFPageBackgroundManagerDelegate"
- "PDFPageDrawProgressCallback"
- "PDFPageEvaluator"
- "PDFPageIconLayer"
- "PDFPageLabelView"
- "PDFPageLabelViewPrivate"
- "PDFPageLayer"
- "PDFPageLayerAnnotationEffect"
- "PDFPageLayerEffect"
- "PDFPageLayerEffectPrivate"
- "PDFPageLayerInterface"
- "PDFPageLayerMarkupAnnotationEffect"
- "PDFPageLayerNoteEffect"
- "PDFPageLayerSelectionEffect"
- "PDFPageLayerTile"
- "PDFPageOverlayViewProvider"
- "PDFPageOverlayViewProviderPrivate"
- "PDFPageRange"
- "PDFPageRangePrivate"
- "PDFPageView"
- "PDFPageViewAnnotationController"
- "PDFPageViewAnnotationControllerPrivate"
- "PDFPageViewController"
- "PDFPageViewControllerPrivate"
- "PDFPageViewPrivate"
- "PDFPanGestureRecognizer"
- "PDFPasswordViewController"
- "PDFPasswordViewControllerDelegate"
- "PDFPointerRegion"
- "PDFPointerRegionPrivate"
- "PDFRVDocumentContextForPage:"
- "PDFRVPresenter"
- "PDFRVPresentingContextAtPoint:"
- "PDFRenderingProperties"
- "PDFRevealManager"
- "PDFRevealManagerPrivate"
- "PDFScannerResult"
- "PDFScannerResultPrivate"
- "PDFScrollView"
- "PDFScrollViewPrivate"
- "PDFSelection"
- "PDFSelectionLayer"
- "PDFSimplePageLayer"
- "PDFTableCellSelection"
- "PDFTextBorderColorForMarkupStyle:"
- "PDFTextBorderColors"
- "PDFTextColorForMarkupStyle:"
- "PDFTextColors"
- "PDFTextInputDelegate"
- "PDFTextInputView"
- "PDFTextLogicalPosition"
- "PDFTextPosition"
- "PDFTextRange"
- "PDFTextSearchAggregator"
- "PDFTextSelectionDidCopy"
- "PDFTextSelectionRect"
- "PDFTextSelectionShowTextSelectionMenu"
- "PDFTextWidgetTextView"
- "PDFThumbnailCollectionViewInterface"
- "PDFThumbnailIconsViewProtocol"
- "PDFThumbnailView"
- "PDFTilePool"
- "PDFTilePoolDelegate"
- "PDFTilePoolPrivate"
- "PDFTileSurface"
- "PDFTimer"
- "PDFTimerPrivate"
- "PDFView:allowsFormFillingMode:forPage:"
- "PDFView:allowsFormFillingMode:withAutofill:forPage:"
- "PDFView:allowsFormFillingMode:withRecognitionConfidence:forPage:"
- "PDFViewController"
- "PDFViewControllerPrivate"
- "PDFViewDebugFlags"
- "PDFViewLayout"
- "PDFViewLayoutPrivate"
- "PDFViewOpenPDF:forRemoteGoToAction:"
- "PDFViewOrderVisiblePageDrawing:"
- "PDFViewParentViewController"
- "PDFViewPerformFind:"
- "PDFViewPerformGoToPage:"
- "PDFViewPrivate"
- "PDFViewWillChangeScaleFactor:toScale:"
- "PDFViewWillClickOnLink:withURL:"
- "PDFWeakWrapper"
- "PKRulerHostingDelegate"
- "PageSignature"
- "PresentableStringForAnnotationKey:"
- "Q16@0:8"
- "Q24@0:8@\"UIPageViewController\"16"
- "Q24@0:8@16"
- "Q32@0:8@16Q24"
- "Q40@0:8@16q24Q32"
- "R1"
- "SelectionRectInfo"
- "SubtypeForPDFMarkupStyle:"
- "T#,R"
- "T#,R,N"
- "T@\"<NSObject><NSCopying>\",?,R"
- "T@\"<PDFAKControllerDelegateProtocol>\",W,N"
- "T@\"<PDFDocumentDelegate>\",W,N"
- "T@\"<PDFPageOverlayViewProvider>\",W,N,V_pageOverlayViewProvider"
- "T@\"<PDFPageOverlayViewProvider>\",W,V_viewProvider"
- "T@\"<PDFThumbnailContextMenuDelegate>\",W,N,VthumbnailContextMenuDelegate"
- "T@\"<PDFThumbnailDataSourceDelegate>\",W,N,V_thumbnailDataSourceDelegate"
- "T@\"<PDFThumbnailIconsViewProtocol>\",R,N"
- "T@\"<PDFViewDelegate>\",W,N"
- "T@\"<UITextInputDelegate>\",W,N"
- "T@\"<UITextInputTokenizer>\",R,N"
- "T@\"<UITextSearchAggregator>\",R,N,V_aggregator"
- "T@\"AKAnnotation\",R,N"
- "T@\"AKAnnotation\",W"
- "T@\"AKController\",R,N"
- "T@\"AKModelController\",R,N"
- "T@\"AKPageModelController\",R,N"
- "T@\"CRNormalizedQuad\",R"
- "T@\"NSArray\",C,N"
- "T@\"NSArray\",R,N"
- "T@\"NSAttributedString\",R,N"
- "T@\"NSData\",R,N"
- "T@\"NSDate\",C,N"
- "T@\"NSDictionary\",C"
- "T@\"NSDictionary\",C,N"
- "T@\"NSDictionary\",R,C,N"
- "T@\"NSObject<OS_dispatch_queue>\",R,N"
- "T@\"NSObject<OS_dispatch_queue>\",R,V_queue"
- "T@\"NSString\""
- "T@\"NSString\",?,C,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",?,R,C,N"
- "T@\"NSString\",C,N"
- "T@\"NSString\",C,N,V_keyPath"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_searchString"
- "T@\"NSString\",R,N"
- "T@\"NSTextStorage\",&"
- "T@\"NSURL\",C,N"
- "T@\"NSURL\",R,N"
- "T@\"PDFAction\",&,N"
- "T@\"PDFAnnotation\",&,N"
- "T@\"PDFAnnotation\",&,V_annotation"
- "T@\"PDFAnnotation\",R,&,N"
- "T@\"PDFAnnotation\",R,N,V_annotation"
- "T@\"PDFAnnotation\",R,W,N"
- "T@\"PDFBorder\",&,N"
- "T@\"PDFDestination\",&,N"
- "T@\"PDFDestination\",R,N"
- "T@\"PDFDetectedForm\",&,N"
- "T@\"PDFDocument\",&,N"
- "T@\"PDFDocument\",R,W,N"
- "T@\"PDFDocument\",W,N"
- "T@\"PDFDocument\",W,N,V_document"
- "T@\"PDFDocument\",W,V_pdfDocument"
- "T@\"PDFExtensionViewController\",W,N,V_extensionViewController"
- "T@\"PDFHostViewController\",W,N,V_hostViewController"
- "T@\"PDFOutline\",&,N"
- "T@\"PDFOutline\",R,N"
- "T@\"PDFPage\",&,N,V_page"
- "T@\"PDFPage\",&,V_page"
- "T@\"PDFPage\",R,N"
- "T@\"PDFPage\",R,W,N"
- "T@\"PDFPage\",R,W,V_page"
- "T@\"PDFPage\",W,N"
- "T@\"PDFPage\",W,N,V_page"
- "T@\"PDFPageAnalyzer\",R,N"
- "T@\"PDFPageView\",&,V_pdfPageView"
- "T@\"PDFRenderingProperties\",&,V_renderingProperties"
- "T@\"PDFRenderingProperties\",R"
- "T@\"PDFSelection\",&,N"
- "T@\"PDFSelection\",&,V_selection"
- "T@\"PDFSelection\",R,N"
- "T@\"PDFTableCellSelection\",R"
- "T@\"PDFView\",&,V_pdfView"
- "T@\"PDFView\",W,N"
- "T@\"PDFView\",W,N,SsetPDFView:"
- "T@\"PDFView\",W,V_pdfView"
- "T@\"PKDrawing\",&,N,V_drawing"
- "T@\"UIButton\",&,N,V_actionsButton"
- "T@\"UIColor\",&"
- "T@\"UIColor\",&,N"
- "T@\"UIColor\",&,N,V_darkModePageBackgroundColor"
- "T@\"UIColor\",C"
- "T@\"UIColor\",C,N"
- "T@\"UIColor\",R,N"
- "T@\"UIConversationContext\",?,&,N"
- "T@\"UIFindInteraction\",R,N"
- "T@\"UIFont\",C,N"
- "T@\"UIImageView\",&,N,V_imageView"
- "T@\"UITextInputPasswordRules\",?,C,N"
- "T@\"UITextPosition\",R,N"
- "T@\"UITextRange\",C"
- "T@\"UITextRange\",R"
- "T@\"UITextRange\",R,N"
- "T@\"UITraitCollection\",&,N,V_traitCollection"
- "T@\"UIView\",&,V_view"
- "T@\"UIView\",?,R,N"
- "T@\"UIView\",R,N"
- "T@,?,R,N"
- "T@,W,N"
- "T@,W,N,V_observedObject"
- "T@,W,V_object"
- "T@?,C,N"
- "T@?,C,N,V_block"
- "T@?,C,N,V_iconConfigurationHandler"
- "T@?,R,V_block"
- "TB"
- "TB,?"
- "TB,?,N"
- "TB,?,N,GisSecureTextEntry"
- "TB,?,R"
- "TB,?,R,N"
- "TB,?,R,N,GisEditable"
- "TB,D,N"
- "TB,GisHighlighted"
- "TB,GisOverlayViewInstalled,V_overlayViewInstalled"
- "TB,N"
- "TB,N,GhasComb"
- "TB,N,GisBookmarked"
- "TB,N,GisFindInteractionEnabled,V_findInteractionEnabled"
- "TB,N,GisHighlighted"
- "TB,N,GisInMarkupMode,V_inMarkupMode"
- "TB,N,GisListChoice"
- "TB,N,GisMultiline"
- "TB,N,GisOpen"
- "TB,N,GisReadOnly"
- "TB,N,GisSelected,V_selected"
- "TB,N,SenablePageShadows:"
- "TB,N,V_didForcePress"
- "TB,N,V_prefersIconOverlaySelection"
- "TB,N,V_prefersOverlaySelection"
- "TB,N,V_touchesDidHavePressure"
- "TB,R,GisActivatableTextField"
- "TB,R,GisSolariumEnabled"
- "TB,R,N"
- "TB,R,N,GisDarkMode"
- "TB,R,N,GisSuspiciousURL"
- "TB,R,N,GisTextFromOCR"
- "TB,V_containsLargeImage"
- "TB,V_containsText"
- "TQ"
- "TQ,?"
- "TQ,?,R"
- "TQ,N"
- "TQ,R"
- "TQ,R,N"
- "TQ,R,V_pageNumber"
- "T^{CGColorSpace=},N"
- "T^{CGDisplayList=},&,V_effectLayerOCRContent"
- "T^{CGPDFContentStream=},R,V_contentStream"
- "T^{CGPDFDocument=},R,N"
- "T^{CGPDFPage=},R,N"
- "T^{CGPDFPageLayoutTable=},N"
- "T^{CGPDFRState=},R,V_rstate"
- "Tc,N,GisCandidateForFormDetection"
- "Tc,N,GisCandidateForOCR"
- "Td,?"
- "Td,N"
- "Td,N,V_iconScale"
- "Td,R"
- "Td,R,N"
- "Td,V_segmentWidth"
- "Ti,R,N"
- "TileRenderRequest"
- "Tq,?"
- "Tq,?,N"
- "Tq,N"
- "Tq,N,V_appearanceStyle"
- "Tq,N,V_offset"
- "Tq,N,V_startCellIndex"
- "Tq,R,N"
- "Tq,R,V_displayBox"
- "Tq,R,V_offset"
- "Tq,V_index"
- "Tq,V_kind"
- "Tq,V_numberOfSegments"
- "T{CAColorMatrix=ffffffffffffffffffff},R"
- "T{CGMatrixFilter=ffffffffffffffffffff},R"
- "T{CGPoint=dd},N"
- "T{CGPoint=dd},N,V_locationOfFirstTouch"
- "T{CGPoint=dd},R,N"
- "T{CGPoint=dd},V_startPoint"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},V_rect"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},V_rootViewFrame"
- "T{CGSize=dd},N"
- "T{UIEdgeInsets=dddd},N"
- "UICollectionViewDelegate"
- "UICollectionViewDragDelegate"
- "UICollectionViewDropDelegate"
- "UIContextMenuInteractionDelegate"
- "UIDocumentPasswordViewDelegate"
- "UIEditMenuInteractionDelegate"
- "UIFindInteractionDelegate"
- "UIGestureRecognizerDelegate"
- "UIKeyInput"
- "UIPageViewControllerDataSource"
- "UIPageViewControllerDelegate"
- "UIPointerInteractionDelegate"
- "UIScrollViewDelegate"
- "UIScrollViewExtensions"
- "UITextInput"
- "UITextInputTraits"
- "UITextInteractionDelegate"
- "UITextSearching"
- "UITextViewDelegate"
- "URL"
- "URLByAppendingPathComponent:"
- "URLWithString:"
- "UTF8String"
- "UUIDString"
- "Unsuported \"extensionToHost:\" function recieved: \"%@\""
- "Unsuported \"hostToExtension:\" function recieved: \"%@\""
- "ViewExtensions"
- "Vv16@0:8"
- "Vv24@0:8@\"NSDictionary\"16"
- "Vv24@0:8@16"
- "Vv32@0:8@\"IOSurface\"16d24"
- "Vv32@0:8@16d24"
- "XPCExtensionInterface"
- "[3@\"NSMutableDictionary\"]"
- "^^{CGPath}"
- "^^{CGPath}16@0:8"
- "^^{CGPath}24@0:8@16"
- "^d"
- "^v"
- "^v32@0:8@16@24"
- "^{CGColor=}"
- "^{CGColor=}16@0:8"
- "^{CGColorSpace=}"
- "^{CGColorSpace=}16@0:8"
- "^{CGContext=}32@0:8@16@24"
- "^{CGDisplayList=}"
- "^{CGDisplayList=}16@0:8"
- "^{CGDisplayList=}20@0:8B16"
- "^{CGDisplayList=}20@0:8i16"
- "^{CGImage=}"
- "^{CGImage=}112@0:8q16{PDFSizeIntegral=QQ}24d40{CGPoint=dd}48^{CGColorSpace=}64@72B80B84B88B92@96@104"
- "^{CGPDFAnnotation=}"
- "^{CGPDFAnnotation=}16@0:8"
- "^{CGPDFAnnotation=}24@0:8@16"
- "^{CGPDFArray=}"
- "^{CGPDFContentStream=}"
- "^{CGPDFContentStream=}16@0:8"
- "^{CGPDFDictionary=}"
- "^{CGPDFDictionary=}16@0:8"
- "^{CGPDFDocument=}"
- "^{CGPDFDocument=}16@0:8"
- "^{CGPDFForm=}"
- "^{CGPDFForm=}16@0:8"
- "^{CGPDFForm=}20@0:8i16"
- "^{CGPDFGState=}"
- "^{CGPDFName=}32@0:8^v16^{__CFString=}24"
- "^{CGPDFOperatorTable=}"
- "^{CGPDFOperatorTable=}16@0:8"
- "^{CGPDFPage=}"
- "^{CGPDFPage=}16@0:8"
- "^{CGPDFPage=}32@0:8^{CGImage=}16@24"
- "^{CGPDFPageLayout=}"
- "^{CGPDFPageLayout=}16@0:8"
- "^{CGPDFPageLayoutTable=}"
- "^{CGPDFPageLayoutTable=}16@0:8"
- "^{CGPDFRState=}"
- "^{CGPDFRState=}16@0:8"
- "^{CGPDFSelection=}24@0:8@16"
- "^{CGPDFString=}"
- "^{CGPDFString=}16@0:8"
- "^{CGPath=}"
- "^{CGPath=}16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__CFArray=}"
- "^{__CFArray=}16@0:8"
- "^{__CFData=}28@0:8@16B24"
- "^{__CFDictionary=}"
- "^{__CFDictionary=}16@0:8"
- "^{__CFDictionary=}32@0:8@16@24"
- "^{__CVBuffer=}32@0:8@16q24"
- "^{__DDHighlight=}"
- "^{__DDHighlight=}16@0:8"
- "^{__IOSurface=}"
- "_PDFAnnotationDictionary"
- "_PDFAnnotationKeyMapping"
- "_PDFMarkupColorForColor:"
- "_PDFTextColorForColor:"
- "_PDFViewParentViewController"
- "_SASLSanitize:"
- "_TtC6PDFKitP33_92DE75AC7A13714BF383CEB737D314A519ResourceBundleClass"
- "_accessPermissions"
- "_accessibilityNode"
- "_accessibilityPageElements"
- "_accessibilityPageElementsParent"
- "_accessibilityTypeString"
- "_actionsButton"
- "_activeIcon"
- "_activePageIndex"
- "_activeSearch"
- "_addAKAnnotationToDictionary:"
- "_addActionToDictionaryRef:"
- "_addActionWithTitle:style:handler:shouldDismissHandler:"
- "_addBox:toDictionary:offset:"
- "_addControlForAnnotation:"
- "_addDestinationToDictionaryRef:"
- "_addEncryptionFromOptions:"
- "_addFormElementsFromAnalysis:bounds:toPage:"
- "_addFormElementsUsingDetectorToPage:displayBox:"
- "_addPDFAnnotation:"
- "_addPDFAnnotationChoiceWidget:"
- "_addPDFAnnotationSignatureWidget:"
- "_addPDFAnnotationTextWidget:"
- "_addPopupForAnnotation:"
- "_addRect:withColor:backgroundColor:labelText:itemIndex:"
- "_addTableFromAnalysis:bounds:toPDFPage:"
- "_addTextFromAnalysis:ofImage:bounds:toPage:"
- "_addUnknownPropertiesToDictionaryRef:"
- "_addWidgetAnnotationToLookupDictionary:"
- "_addedSublayers"
- "_adjustScrollViewForKeyboardNotification:"
- "_adjustScrollViewWithAnimationProperties:delta:"
- "_aggregator"
- "_akAnnotationAdaptor"
- "_akAnnotationForCopying"
- "_akAnnotationInstanceForPDFAnnotationSubtype:withOptionalWidgetFieldType:"
- "_akAnnotationSubclassForWidgetFieldType:"
- "_akController"
- "_akDidSetupRealPageModelController"
- "_akDocumentAdaptor"
- "_akInkAnnotation"
- "_akPageAdaptor"
- "_akPageOverlayViewProvider"
- "_akToolbarView"
- "_allowAnimatedUpdateSelectionRectViews"
- "_allowUpdate"
- "_allowsCommenting"
- "_allowsContentAccessibility"
- "_allowsCopying"
- "_allowsDocumentAssembly"
- "_allowsDocumentChanges"
- "_allowsFormFieldEntry"
- "_allowsPrinting"
- "_analyzerCallbackQueue"
- "_animationProperties"
- "_annotation"
- "_annotationAllowsCommenting:"
- "_annotationAtGestureLocation:"
- "_annotationChanges"
- "_annotationClassHasSeniority:"
- "_annotationEditingAllowed"
- "_annotationHit:atLocation:"
- "_annotationHitLongPress:gestureState:location:"
- "_annotationHitNotification:"
- "_annotationLongPressNotification:"
- "_annotations"
- "_annotationsForSelection:"
- "_annotationsWereAdded:"
- "_annotationsWereRemoved:"
- "_appearanceStyle"
- "_appendPasswordUI"
- "_appendedAttributes"
- "_applyScale:toView:"
- "_artBox"
- "_asyncSearchQueue"
- "_attributedString"
- "_attributes"
- "_autoFillTextContentType"
- "_autofillEntryType"
- "_auxiliaryAttributes"
- "_auxiliaryConnection"
- "_backgroundColor"
- "_backgroundImageCache"
- "_backgroundOnePixelView"
- "_beginObservingScrollViewMagnification"
- "_bleedBox"
- "_block"
- "_bookmarked"
- "_bookmarkedPages"
- "_bookmarksCatalog"
- "_boolValueForAnnotationFlag:withDefaultValue:"
- "_boolValueForWidgetFieldFlag:"
- "_buildPDFPageView"
- "_buildPageLayout"
- "_builtLayout"
- "_cache"
- "_cachedAppearances"
- "_cachedAppearancesLock"
- "_cachedOverlayViewForPage:"
- "_calculatePDFAnnotationLayerOutsetForAction:"
- "_callCompletionBlock:onQueue:analysis:error:foundTable:"
- "_callOverlayViewForPage:"
- "_callWillEndDisplayingOverlayViewForPage:"
- "_canEditDocument"
- "_canSaveWithEncryption"
- "_candidateForFormDetection"
- "_candidateForOCR"
- "_centerAlign"
- "_cgAnnotation"
- "_cgPaths"
- "_cgSelections"
- "_changedAnnotations"
- "_childArray"
- "_childDictionaryReferencesParent:"
- "_choiceWidgetDone"
- "_classForActionDictionary:"
- "_classifyRect:"
- "_cleanCoachMarks"
- "_cleanup"
- "_clear"
- "_closeTextEditingMenu"
- "_closestPositionToPoint:withinRange:"
- "_collectGlyphEntriesInDisplayList:medianGlyphHeight:"
- "_collectionView"
- "_collectionView:dataOwnerForDragSession:atIndexPath:"
- "_color"
- "_colorFromColorOrArray:"
- "_colorWidgetBackgrounds"
- "_colorizeTileEdgesForRequest:context:tileSize:"
- "_commitTextFromTextView:"
- "_commonInit"
- "_commonInitWithStyle:"
- "_commonResetForm:inclusive:"
- "_compensatingAffineTransformForPage:"
- "_computeEdgeInsetsForQuad:inImage:background:glyphCount:"
- "_configureIcons"
- "_constructingDictionaryRef"
- "_containsLargeImage"
- "_containsText"
- "_contentInset"
- "_contentLayer"
- "_contentRect"
- "_contentScrollInset"
- "_contentStream"
- "_contentsScale"
- "_control"
- "_convertCFStringToCGPDFName:forKey:"
- "_convertPoint:fromPDFPageViewController:"
- "_convertPoint:toPDFPageViewController:"
- "_convertPoint:toPageView:"
- "_convertWriteOptions:"
- "_createArrayForCGRect:"
- "_createArrayForColor:"
- "_createAttributedString"
- "_createCGPDFAnnotationForAnnotation:"
- "_createContextForTileSurface:ofRequest:"
- "_createDisplayListCompletionBlocks"
- "_createDisplayListTrackingGlyphs:"
- "_createDocumentWithDataProvider:"
- "_createInfoDictionary"
- "_createPageRefFromImage:andOptions:"
- "_createPageView:"
- "_createRetainedDisplayList"
- "_createTileSurfaceForRequest:"
- "_createdWithHighLatencyDataProvider"
- "_creatingDisplayList"
- "_cropBox"
- "_cs"
- "_currentPageIndex"
- "_darkMode"
- "_darkModePageBackgroundColor"
- "_dataDetectorsEnabled"
- "_dataDetectorsLock"
- "_dataFromXMP:withRootPath:keys:"
- "_dataOwnerForCopy"
- "_dataSource"
- "_delayedModelBaseScaleFactorCalculation"
- "_delegate"
- "_detectedAnnotationWithBounds:intersectsAnnotationOnPage:"
- "_detectedAnnotations"
- "_detectedForm"
- "_detectedFormField"
- "_detectedFormFieldPage"
- "_detectedFormFieldsRecognitionConfidence"
- "_deviceColorSpace"
- "_dictionaryRef"
- "_didChangeBounds"
- "_didChangeZoomFactor:"
- "_didForcePress"
- "_didPerformFormDetection"
- "_didPerformOCR"
- "_didRemoveValueForAnnotationKey:"
- "_didRotatePageNotification:"
- "_didSetValue:forAnnotationKey:"
- "_dimmingViewVisible"
- "_displayBox"
- "_displayList"
- "_displayListMutex"
- "_displaysAnnotations"
- "_displaysMarkups"
- "_doButtonHit:"
- "_doNotQueryScaleFactor"
- "_document"
- "_documentCatalogMetadata"
- "_documentCatalogMetadataForRootPath:withKeys:"
- "_documentChanged"
- "_documentDelegate"
- "_documentHasBurnInAnnotations"
- "_documentHasPageWithApplicationData"
- "_documentIndex"
- "_documentRedactionCount"
- "_documentURL"
- "_documentViewSize"
- "_documentWasUnlocked"
- "_downAppearance"
- "_downOffAppearance"
- "_dragDataOwner"
- "_dragInteraction:dataOwnerForSession:"
- "_dragItemsAtLocationInView:"
- "_drawAnnotationWithBox:inContext:"
- "_drawAnnotationsWithBox:inContext:"
- "_drawBookmarkInContext:"
- "_drawPageImage:forQuality:"
- "_drawQuads"
- "_drawTextFromAnalysis:ofImage:intoContext:withBounds:"
- "_drawing"
- "_drawingRectForLineStyle:from:to:borderWidth:"
- "_dumpLayer"
- "_editingAnnotaiton"
- "_effectLayerOCRContent"
- "_effectsLayer"
- "_enableAccessibilityDrawing"
- "_enableBackgroundImages"
- "_enablePageShadows"
- "_enableRoundPageCorners"
- "_enableTileEdgeColoring"
- "_enableTileUpdates"
- "_encodedLayerTree"
- "_end"
- "_endPDFViewRotationAnimated:withUpdate:"
- "_endPoint"
- "_ensureOverlayViewController"
- "_execute"
- "_expectedQualityIndexForPageIndex:forQuality:"
- "_exportedInterface"
- "_extensionAuxiliaryHostProtocol"
- "_extensionAuxiliaryVendorProtocol"
- "_extensionContextForUUID:"
- "_extensionViewController"
- "_fieldCount"
- "_fieldNamedUnlocked:"
- "_findCharIndex"
- "_findInstance"
- "_findInteractionEnabled"
- "_findModel"
- "_findNextActivatableAnnotationOnPage:fromAnnotation:direction:"
- "_findOptions"
- "_findPageIndex"
- "_findPageIndexNeedingUpdate:forQuality:"
- "_findResults"
- "_findString:fromSelection:withOptions:"
- "_findStrings"
- "_findVisiblePages"
- "_finding"
- "_firstChild"
- "_forceBreaks"
- "_forceTileUpdate"
- "_forcedUpdateTimer"
- "_formChanged:"
- "_formContentType"
- "_formData"
- "_formDataLoaded"
- "_formDetectionEnabled"
- "_formFieldButton"
- "_formFieldButtonHideKeyboardNotification"
- "_formFieldButtonShowKeyboardNotification"
- "_formFieldGroups"
- "_formFillingQueue"
- "_foundTextRanges"
- "_frameSize"
- "_generateFormFieldName"
- "_generateRects"
- "_generationCount"
- "_geometryInterface"
- "_gestureInit"
- "_getBooleanProperty:forKey:withDefault:"
- "_getDocumentAKController"
- "_getDocumentID:"
- "_getFullFieldNameFromDictionary:"
- "_getIndexSetIntersectionBetween:and:"
- "_getNearestOutline:forDestination:"
- "_getPagePoint:forGestureLocation:"
- "_goToDestination:"
- "_goToPage:"
- "_goToPage:animated:withBackgroundUpdate:"
- "_greekingThreshold"
- "_gstate"
- "_handleButtonHit:"
- "_handleFormFillingEventAtLocation:"
- "_handlePageRefChangeWithOldRotation:oldMediaBox:"
- "_hasTileWithFrameInLayer:"
- "_hidePDFMarkupMenuView"
- "_hideTextSelectionMenu"
- "_hideTileLayer:"
- "_highlightedTextRange"
- "_hostScrollViewZoomScale"
- "_hostViewController"
- "_iconConfigurationHandler"
- "_iconScale"
- "_icons"
- "_iconsLayoutIconCount"
- "_iconsLayoutSize"
- "_iconsView"
- "_imageAnalyzer"
- "_imageScale"
- "_imageView"
- "_imageViewHeightConstraint"
- "_imageViewWidthConstraint"
- "_inMarkupMode"
- "_index"
- "_indexSet:touchesIndexSet:"
- "_initPageCornerRadiusForMagnification:"
- "_initialBookmarkedPageIndices"
- "_insertFieldRect:ofKind:"
- "_insertFileAtURL:type:atIndex:completionHandler:"
- "_insertImageWithURL:atIndex:completionHandler:"
- "_insertPDFDocumentWithURL:atIndex:completionHandler:"
- "_insertPagesFromProvidedPDFDocument:atPageIndex:"
- "_insetBoundsInDocument"
- "_installOverlayForPageView:ofPage:atIndex:"
- "_intelligenceCollectContentIn:collector:"
- "_internalPDFAnnotationDictionary"
- "_internalSetAutoScaleFactor"
- "_internalSetScaleFactor:"
- "_interpolationQuality"
- "_invalidateAppearanceStreamForAnnotation:withKey:andNewValue:"
- "_isActive"
- "_isAutofillNewContextStart"
- "_isCancled"
- "_isCommonlyMappedToNothing:"
- "_isDetectedCheckbox"
- "_isDetectedSignature"
- "_isEncrypted"
- "_isEndingRect"
- "_isForcingUpdate"
- "_isFullyConstructed"
- "_isHighlighted"
- "_isNonAsciiSpace:"
- "_isPointerTouch"
- "_isRectangular"
- "_isRedacted"
- "_isSelected"
- "_isSignatureWidget"
- "_isStartingRect"
- "_isTextMarkupRedaction"
- "_isTile:occludedByTiles:"
- "_isTiling"
- "_isTornDown"
- "_isTouchingLollipopAtLocationOfFirstTouch:"
- "_isTransparent"
- "_isUnlocked"
- "_isUsingPDFExtensionView"
- "_isValidAnnotationKey:"
- "_isWorking"
- "_keyPath"
- "_keyboardWillHide:"
- "_keyboardWillShow:"
- "_kill:"
- "_kind"
- "_label"
- "_labelText"
- "_largePotWithSystemImageNamed:"
- "_lastChild"
- "_lastFindCharIndex"
- "_lastFindPageIndex"
- "_lastLayerFrameInRootView"
- "_lastLayoutZoomFactor"
- "_lastZoomChange"
- "_layerTileToRootViewBounds:"
- "_layout"
- "_layoutLock"
- "_layoutMode"
- "_lazilyLoadChildren"
- "_limitedSearch"
- "_lineWidthThreshold"
- "_loadDocument:"
- "_loadedAnnotations"
- "_locationOfFirstTouch"
- "_lock_accessAnnotations"
- "_lock_getAnnotations"
- "_loggingEnabled"
- "_lp_userVisibleStringUsesEncodedHost"
- "_majorVersion"
- "_markupAnnotationsForExactIndexSet:"
- "_maximumBeamSnappingLength"
- "_mediaBox"
- "_minorVersion"
- "_modelBaseScaleFactor"
- "_namedDestination:forNameDictionary:"
- "_needsUpdate"
- "_newCGImageWithBox:bitmapSize:scale:offset:colorSpace:backgroundColor:withRotation:withAntialiasing:withAnnotations:withBookmark:withOptions:withDelegate:"
- "_next"
- "_normalAppearance"
- "_normalOffAppearance"
- "_normalizedToPageTransformForPageWithBounds:"
- "_notifyAKAdaptorPagePlaceholder:wasReplacedWithPage:atIndex:"
- "_notifyPropertyChanged:"
- "_numberOfSegments"
- "_object"
- "_observedObject"
- "_observedPageIndices"
- "_offset"
- "_oldBoundsForBox"
- "_oldPageRotation"
- "_openDescendantCount"
- "_outline"
- "_overlay"
- "_overlayView"
- "_overlayViewController"
- "_overlayViewInstalled"
- "_ownerPassword"
- "_page"
- "_pageArea"
- "_pageBackgroundColor"
- "_pageBackgroundColorHint"
- "_pageBackgroundManager"
- "_pageBounds"
- "_pageChangeDelegate"
- "_pageChangedNotification:"
- "_pageChangedPageRef:"
- "_pageColor"
- "_pageCount"
- "_pageDictionaryIndices"
- "_pageDidRotate:"
- "_pageImage"
- "_pageImageOptions"
- "_pageIndex"
- "_pageIndices"
- "_pageLayerEffects"
- "_pageLayerForPage:"
- "_pageLayerVisibleRect"
- "_pageLock"
- "_pageNumber"
- "_pageOverlayViewProvider"
- "_pageRanges"
- "_pageRotationChanged:"
- "_pageToOverlayMap"
- "_pageViewController:nextViewController:forViewController:"
- "_pageViewControllerCreate:"
- "_pageViewForAnnotation:"
- "_pageViewHeight:"
- "_pages"
- "_pagesChanged"
- "_pagesOrderedSet"
- "_parent"
- "_pasteActionIfAvailableAfterPage:"
- "_pathLock"
- "_pdfAKControllerDelegate"
- "_pdfAKControllerDelegateForDeferredSetup"
- "_pdfAnnotationInstanceForAKAnnotation:"
- "_pdfAnnotationUUID"
- "_pdfDocument"
- "_pdfDocumentDidUnlock:"
- "_pdfPageView"
- "_pdfSelectionUUID"
- "_pdfView"
- "_pdfViewDidChangeScale:"
- "_pdfViewDidLayout:"
- "_pdfViewInsets"
- "_pdfViewSafeAreaInsets"
- "_pdfViewZoomToRect:"
- "_performAsDataOwner:block:"
- "_performDoubleTapAtLocation:"
- "_performGestureType:state:location:locationOfFirstTouch:forTouchType:"
- "_permission"
- "_persistentApplicationData"
- "_pixelAlignPageFrameOrigin:"
- "_pointOutsetFrom:startPoint1:startPoint2:lineWidth:"
- "_pointerInteraction:regionForRequest:defaultRegion:completion:"
- "_pointerIsOverAnnotation"
- "_popoverControllerSourceRect"
- "_popup"
- "_popupDictionary"
- "_popupDrawCloseWidget"
- "_popupDrawText"
- "_postAnnotationHitNotification:"
- "_postAnnotationWillHitNotification:"
- "_postAnnotationsChangedNotificationCoalesced"
- "_prefersIconOverlaySelection"
- "_prefersOverlaySelection"
- "_preloadingPageIndexes"
- "_presentPopupView"
- "_presentPopupView_iOS"
- "_presentViewController:"
- "_pressure"
- "_previous"
- "_printDictionary:atDepth:"
- "_printRectsArray:"
- "_private"
- "_private2"
- "_propagateNotesForIndexSet:"
- "_quadPoints"
- "_quadPointsIndexSet"
- "_quadPointsPath"
- "_queue"
- "_ranDataDetectors"
- "_ratioConstraint"
- "_rawPageAtIndex:"
- "_reAddPageOverlaysStartingAtIndex:"
- "_rect"
- "_reflectNewPageOn"
- "_releaseBackgroundImage"
- "_releaseDictionaryRef"
- "_releaseDisplayList"
- "_releaseDocument"
- "_releaseDocumentViewController"
- "_releasePageLayerEffects"
- "_releaseScrollView"
- "_releaseTiles"
- "_reloadPage:"
- "_remoteViewControllerInterface"
- "_removeChildAtIndex:"
- "_removeControlForAnnotation"
- "_removePDFView"
- "_removePageOverlaysStartingAtIndex:"
- "_removePasswordView"
- "_removeWidgetAnnotationFromLookupDictionary:"
- "_renderTileForRequest:"
- "_renderingProperties"
- "_renderingPropertyUpdate:"
- "_requestedOCR"
- "_requestedPages"
- "_requestedPagesMutex"
- "_requestedTiling"
- "_resetAnimationProperties"
- "_resetPDFHostViewControllerViews"
- "_resizeDisplayView:"
- "_respondsToClassForAnnotationClass"
- "_respondsToClassForAnnotationType"
- "_respondsToClassForPage"
- "_respondsToDidBeginDocumentFind"
- "_respondsToDidBeginPageFind"
- "_respondsToDidEndDocumentFind"
- "_respondsToDidEndPageFind"
- "_respondsToDidFindMatch"
- "_respondsToDidMatchString"
- "_respondsToDidReceiveAnalysis"
- "_respondsToDidUnlock"
- "_respondsToHandleTabFrom"
- "_respondsToPrintJobTitle"
- "_respondsToShouldReadAKInkAnnotations"
- "_restoreLinePoints"
- "_restorePropertiesAfterSetBounds"
- "_restoreQuadPoints"
- "_rolloverAppearance"
- "_rolloverOffAppearance"
- "_rootViewFrame"
- "_rotateActiveAnnotation"
- "_rotation"
- "_rotationTransformForPageView"
- "_rows"
- "_rstate"
- "_rvItemAtPoint:"
- "_sanitizeAnnotationArray:"
- "_sanitizeAnnotationDictionary:"
- "_sanitizeValue:forKey:"
- "_saveAppearance"
- "_savePropertiesBeforeSetBounds"
- "_scaleFactor"
- "_scaleFromLayerTransforms"
- "_scanData:"
- "_scanned"
- "_scannerResults"
- "_scheduleDelayedModelBaseScaleFactorCalculation"
- "_scrollByPage:"
- "_scrollHorizontalBy:"
- "_scrollOriginForPageTopLeft:"
- "_scrollVerticalBy:"
- "_scrollViewRecognizersForPageAtIndex:"
- "_searchDimmingView"
- "_searchHighlightView"
- "_searchString"
- "_segmentWidth"
- "_selectAndScrollToCurrentPageIfNeeded"
- "_selected"
- "_selection"
- "_selectionChangedNotification:"
- "_selectionForMarkupAnnotation"
- "_selectionForTextRange:"
- "_selectionPointsChangedNotification:"
- "_selfDidResize:"
- "_setAlignment:"
- "_setArray:forAnnotationKey:"
- "_setAttributedMessage:"
- "_setAttributedString:"
- "_setAttributedStringForAnnotation:stringValue:textView:"
- "_setAutoScrollEnabled:"
- "_setBoolValue:forAnnotationFlag:"
- "_setBoolValue:forWidgetFieldFlag:"
- "_setContentScrollInset:"
- "_setCornerRadius:"
- "_setDashFromArray:"
- "_setDictionary:forAnnotationKey:"
- "_setDimmingViewVisible:"
- "_setDocumentCatalogMetadata:withNSpace:prefix:rootPath:"
- "_setEnablePageShadows:"
- "_setFont:"
- "_setFontColor:"
- "_setHysteresis:"
- "_setInteger:forAnnotationKey:"
- "_setMaximumZoomScale:"
- "_setMenuProvider:"
- "_setMinimumZoomScale:"
- "_setNextAction:forDocument:forPage:"
- "_setNextActions:"
- "_setNextActions:forDocument:forPage:"
- "_setParent:"
- "_setSignatureWidgetAsKeyboardFocused:"
- "_setString:"
- "_setString:forAnnotationKey:"
- "_setStyleFromDictionary:"
- "_setVarious:forAnnotationKey:"
- "_setup"
- "_setupBookmarkLayer"
- "_setupDocument:"
- "_setupDocumentViewController"
- "_setupDocumentViewSize"
- "_setupExtensionInterruptionBlock"
- "_setupGestureRecognizerDependencies"
- "_setupGestureRecognizersForView:andDocument:"
- "_setupPasswordView"
- "_setupPopupView"
- "_setupRotationNotificationObservationForPageAtIndex:"
- "_setupScrollView"
- "_setupTopLevelView"
- "_setuppageAnnotationEffects"
- "_shadowLayer1"
- "_shadowLayer2"
- "_shiftImagesAtIndex:downwards:"
- "_shiftPagesAtIndex:downwards:"
- "_shouldAntiAlias"
- "_shouldBurnIn"
- "_shouldExport"
- "_shouldHandleAnnotationAtLocation:forGestureType:"
- "_shouldHideInteractiveBackgroundColor"
- "_shouldReadAppearanceStreams"
- "_shouldReplaceStringOnAnnotation:withTextView:"
- "_shouldReportAnalytics"
- "_shouldUpdateMarkupWithStyle:onPage:forIndexSet:"
- "_shouldUseAKAnnotation:toRepresentCGPDFDictionary:"
- "_showFormFillingButton:"
- "_signatureAnnotationForRendering"
- "_sourceDictionary"
- "_srcDictionaryRef"
- "_start"
- "_startCellIndex"
- "_startFade"
- "_startObservingAnnotation"
- "_startObservingPageModel"
- "_startPoint"
- "_stopObservingAnnotation"
- "_stopObservingPageModel"
- "_style"
- "_subclassOverridesPageAtIndex"
- "_subtractRectB:fromRectA:"
- "_suggestedLineHeight"
- "_suppressAppearanceStreamText"
- "_syncAction:"
- "_syncAdditionalAction:"
- "_syncAnnotationTextForAnnotation:withKey:andNewValue:"
- "_syncAppearanceDictionaryUpdatingEditsDisableAppearanceOverride:"
- "_syncAppearanceState:"
- "_syncAppleExtras:"
- "_syncArrowHeadStyleForAnnotation:withKey:andNewValue:"
- "_syncAuthorForAnnotation:withKey:andNewValue:"
- "_syncBorder:"
- "_syncBorderStyle:"
- "_syncBoundingRectangleForAnnotation:withKey:andNewValue:"
- "_syncChildAnnotationForAnnotation:withKey:andNewValue:"
- "_syncColor:"
- "_syncColorForAnnotation:withKey:andNewValue:"
- "_syncContents:"
- "_syncContentsForAnnotation:withKey:andNewValue:"
- "_syncCornerRadiusForAnnotation:withKey:andNewValue:"
- "_syncDashedForAnnotation:withKey:andNewValue:"
- "_syncDate:"
- "_syncDefaultAppearance:"
- "_syncDestination:"
- "_syncEndPointForAnnotation:withKey:andNewValue:"
- "_syncEverythingToAKAnnotation"
- "_syncEverythingToPDFAnnotation"
- "_syncFlags:"
- "_syncHighlightingMode:"
- "_syncIconName:"
- "_syncInkPathForAnnotation:withKey:andNewValue:"
- "_syncInklist:"
- "_syncInteriorColor:"
- "_syncLineEndingStyles:"
- "_syncLinePoints:"
- "_syncModificationDateForAnnotation:withKey:andNewValue:"
- "_syncName:"
- "_syncOpen:"
- "_syncPage:"
- "_syncPageIndexToScrollView"
- "_syncParent:"
- "_syncPopup:"
- "_syncQuadding:"
- "_syncRect:"
- "_syncStartPointForAnnotation:withKey:andNewValue:"
- "_syncStrokeWidthForAnnotation:withKey:andNewValue:"
- "_syncSubtype:"
- "_syncTextLabel:"
- "_syncWidgetAppearance:"
- "_syncWidgetDefaultValue:"
- "_syncWidgetFieldFlags:"
- "_syncWidgetFieldType:"
- "_syncWidgetMaxLen:"
- "_syncWidgetOptions:"
- "_syncWidgetTextLabelUI:"
- "_syncWidgetValue:"
- "_table"
- "_targetedPreviewForRange:"
- "_teardown"
- "_teardownGestureRecognizersForView:andDocument:"
- "_teardownRotationNotificationObservationForPageAtIndex:"
- "_testPixelsFromPoint:toPoint:compare:"
- "_text"
- "_textExtractionQueue"
- "_textForValue:"
- "_textFromOCR"
- "_textInputDelegate"
- "_textInputTokenizer"
- "_textInteraction"
- "_textPathInsets"
- "_textSelectionDidCopyNotification:"
- "_textSelectionRange"
- "_textSelectionShowTextSelectionMenu:"
- "_textWidgetDone"
- "_thumbnailDataSourceDelegate"
- "_thumbnailSize"
- "_thumbnailView"
- "_tileLayerHidden"
- "_tileRefresh"
- "_tileUpdateComplete"
- "_tiles"
- "_tilesLayer"
- "_touchesDidHavePressure"
- "_traitCollection"
- "_transformFromPageToPageView:"
- "_transformFromPageViewToPage:"
- "_trimBox"
- "_typeForGestureRecognizer:"
- "_uiDocPasswordView"
- "_unboundAutoScaleFactorForPage:"
- "_unboundAutoScaleFactorForPageWithSize:"
- "_uninstallAllOverlays"
- "_uninstallOverlayForPageView:ofPage:atIndex:"
- "_update"
- "_updateActionsButtonVisibilityAtIndexPath:"
- "_updateAnnotationVisibility:"
- "_updateAnnotations"
- "_updateBackgroundColor"
- "_updateBookmarksForPages"
- "_updateCurrentPageUsingViewCenter"
- "_updateCurrentPageViewController:"
- "_updateDashPatternRaw"
- "_updateDashedPatternForStrokeWidth:isDashed:"
- "_updateDocumentIsLocked"
- "_updateGeometry"
- "_updateLayerEffect:withPageTransform:"
- "_updateLayout"
- "_updateNoteLayer"
- "_updatePDFScrollViewMinimumNumberOfTouches"
- "_updatePageCount"
- "_updateParentContents"
- "_updatePasswordView"
- "_updateScaleFactor"
- "_updateScrubber"
- "_updateScrubberAtViewLocation:"
- "_updateScrubberForPageIndex:goToPage:"
- "_updateTextSelectionPoints"
- "_updateTiles"
- "_updateUI"
- "_updateVisibility"
- "_updateVisibilityDelegateForVisiblePageView:atIndex:"
- "_updateWidgetControl:forBounds:"
- "_userInterfaceStyle"
- "_userPassword"
- "_view"
- "_viewDidMoveToSuperviewCommon"
- "_viewProvider"
- "_visibilityDelegateIndex"
- "_widgetAnnotationLookup"
- "_widgetAnnotationLookupLock"
- "_widgetOnStateString"
- "_willForceUpdate"
- "_workQueue"
- "_workloadSemaphore"
- "_writeAppendMode:"
- "_writeToConsumer:"
- "_xmpNameSpace"
- "_xmpPrefix"
- "_xmpRootPath"
- "_zoomChangeScheduled"
- "_zoomGenerationDelay"
- "_zoomToRect:"
- "absoluteString"
- "acceptSingleTouch:"
- "accessibilityElementsWithPlugin:"
- "accessibilityHitTest:withPlugin:"
- "accessibilityLabel"
- "accessibilityNode"
- "accessibilityParent"
- "accessibilityTitleUIElement"
- "action"
- "actionForLayer:forKey:"
- "actionWithActionDictionary:forDocument:forPage:"
- "actionWithHandler:"
- "actionWithTitle:image:identifier:handler:"
- "actionWithTitle:style:handler:"
- "actionsButton"
- "activatableTextField"
- "activateAnnotation:"
- "activateBackground:"
- "activateConstraints:"
- "activateNextAnnotation:withCompletion:"
- "activeControls"
- "activeMarkupStyle"
- "activePageView"
- "activeTextStorage"
- "activeTileCount"
- "addAKAnnotation:toAnnotationDictionary:"
- "addAction:"
- "addAction:forControlEvents:"
- "addActionToDictionaryRef:"
- "addAdditionalActionsToDictionaryRef:"
- "addAlternateFieldNameToDictionaryRef:"
- "addAnimation:forKey:"
- "addAnnotation:"
- "addAnnotation:withUndo:"
- "addAnnotationFormField:"
- "addAppearanceCharacteristicsToDictionaryRef:"
- "addAppearanceForKey:toDictionaryRef:"
- "addAttribute:value:range:"
- "addBezierPath:"
- "addBookmark"
- "addBorderStyleToDictionaryRef:"
- "addBorderToDictionaryRef:"
- "addCGSelection:forPage:"
- "addCharactersInString:"
- "addColor:forKey:toDictionaryRef:"
- "addContentsToDictionaryRef:"
- "addControl"
- "addControlForAnnotation:"
- "addCurveToPoint:controlPoint1:controlPoint2:"
- "addDefaultAppearanceDictionaryRef:"
- "addDefaultFieldValueToDictionaryRef:"
- "addDestinationToDictionaryRef:"
- "addDetectedAnnotation:toPage:"
- "addDetectedAnnotations:"
- "addDictionaryValueToDictionaryRef:"
- "addDisplayList:toPage:"
- "addEntriesFromDictionary:"
- "addFieldFlagsToDictionaryRef:"
- "addFieldNameToDictionaryRef:"
- "addFieldTypeToDictionaryRef:"
- "addFieldValueToDictionaryRef:"
- "addFieldsToDictionaryRef:"
- "addFlagsToDictionaryRef:"
- "addFormField:"
- "addFormFieldGroup:"
- "addFormFieldsFromVisionDocument:documentImage:toPage:withBox:"
- "addGestureRecognizer:"
- "addHighlightingModeToDictionaryRef:"
- "addIndex:"
- "addIndexes:"
- "addIndexesInRange:"
- "addInkListToDictionaryRef:"
- "addInteraction:"
- "addLayoutManager:"
- "addLineEndingStylesToDictionaryRef:"
- "addLineToDictionaryRef:"
- "addLineToPoint:"
- "addMarkupWithStyle:forIndexSet:"
- "addMarkupWithStyle:fromSelection:"
- "addMaxLenToDictionaryRef:"
- "addModificationDateToDictionaryRef:"
- "addNameDefaultValueToDictionaryRef:"
- "addNameToDictionaryRef:"
- "addNameValueToDictionaryRef:"
- "addNeedsAppearanceToDictionaryRef:"
- "addNormalAndDownAppearanceToDictionaryRef:"
- "addNormalAndDownAppearanceWithStateToDictionaryRef:"
- "addNormalAppearanceToDictionaryRef:"
- "addNormalAppearanceWithStateToDictionaryRef:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:forKeyPath:options:context:"
- "addObserver:selector:name:object:"
- "addObserverForName:object:queue:usingBlock:"
- "addOpenToDictionaryRef:"
- "addOperation:"
- "addOperationWithBlock:"
- "addOptionsToDictionaryRef:"
- "addPageLayerEffect:"
- "addPageReferenceToDictionaryRef:"
- "addPopupToDictionaryRef:"
- "addQuadPointsToDictionaryRef:"
- "addQuaddingToDictionaryRef:"
- "addRect:forKey:toDictionaryRef:"
- "addRedactionFromRectangularSelectionWithRect:"
- "addSearchSelection:"
- "addSelection:"
- "addSelectionCore:normalize:"
- "addSelectionCore:normalize:withClampedRange:"
- "addSelectionNoNormalize:"
- "addSelectionRange:page:normalize:"
- "addSelections:"
- "addStringDefaultValueToDictionaryRef:"
- "addStringValueToDictionaryRef:"
- "addSublayer:"
- "addSubview:"
- "addTablesFromVisionDocument:documentImage:toPage:withBox:"
- "addTextContainer:"
- "addTextFieldWithConfigurationHandler:"
- "addTextFromVisionDocument:documentImage:toPage:withBox:"
- "addTextLabelToDictionaryRef:"
- "addTimer:forMode:"
- "addToPageView"
- "addedAnnotation:forFormField:"
- "additionalEditMenuElementsForMarkupAnnotation:"
- "additionalEditMenuElementsForSelection:"
- "adjustScrollViewForKeyboardNotification:"
- "adjustScrollViewToAccomodateKeyboardStartingFrame:endingFrame:annotationFrame:withAnimationDuration:curve:"
- "adjustedContentInset"
- "adjustedPageCornerRadiusForPageSize:magnification:"
- "adjustedRectForBox:withAnnotation:"
- "afterScreenUpdates"
- "aggregator"
- "akAnnotation"
- "akAnnotationAdaptor"
- "akAnnotationEditingEnabled"
- "akAnnotationFromCGPDFAnnotation:andDictionary:"
- "akAnnotationIsSelected"
- "akController"
- "akDidSetupRealPageModelController"
- "akDocumentAdaptor"
- "akDocumentModelController"
- "akMainController"
- "akPageAdaptor"
- "akPageModelController"
- "akRedoToolbarItem"
- "akToolbarView"
- "akToolbarViewItemTintColor"
- "akToolbarViewTintColor"
- "akUndoToolbarItem"
- "alertControllerWithTitle:message:preferredStyle:"
- "alignment"
- "allKeys"
- "allLines"
- "allObjects"
- "allValues"
- "allocWithZone:"
- "allowedWritingToolsResultOptions"
- "allowsDarkAppearanceContent"
- "allowsKeyedCoding"
- "allowsMarkupAnnotationEditing"
- "allowsNumberPadPopover"
- "allowsPageReordering"
- "allowsToggleToOff"
- "allowsUndo"
- "alternateFieldName"
- "analyzePage:analysisTypes:completionQueue:completionBlock:"
- "analyzePage:withBox:requestTypes:"
- "animateWithCompletion:"
- "animateWithDuration:animations:"
- "animateWithDuration:animations:completion:"
- "animateWithDuration:delay:options:animations:completion:"
- "animationWithKeyPath:"
- "annotationAdaptorWithPDFAnnotation:andCGPDFAnnotation:andPDFDictionary:"
- "annotationAdaptorWithPDFAnnotation:andCGPDFAnnotation:andPDFDictionary:updatePDFAnnotationIfNeeded:"
- "annotationAtPoint:"
- "annotationAtRect:"
- "annotationChanges"
- "annotationController"
- "annotationController:detectedEditOfType:"
- "annotationDidEndEditing:"
- "annotationEditingEnabled"
- "annotationForDetectedFormField:"
- "annotationKeyValues"
- "annotationOver"
- "annotationPageLayerEffectIsFlipped"
- "annotationRect"
- "annotationSubclassForPopup"
- "annotationSubclassForSubtype:"
- "annotationSubclassForType:"
- "annotationWillBeginEditing:"
- "annotationWithData:"
- "annotationWithUUID:"
- "annotationsChangedOnPage:"
- "annotationsForFieldName:"
- "annotationsIfAvail"
- "anyObject"
- "appearString"
- "appearance:"
- "appearanceCharacteristicsKeyValues"
- "appearanceOverride"
- "appearanceStyle"
- "appendAttributedString:"
- "appendFormat:"
- "appendItemsWithIdentifiers:intoSectionWithIdentifier:"
- "appendSectionsWithIdentifiers:"
- "appendString:"
- "applicationDataWithName:"
- "applySnapshot:animatingDifferences:"
- "applySnapshot:animatingDifferences:completion:"
- "applySnapshotWithAnimation:"
- "applyTileLayoutScale:"
- "areaOfInterestAtPoint:"
- "areaOfInterestForMouse:"
- "areaOfInterestForPoint:"
- "array"
- "arrayByAddingObjectsFromArray:"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObject:"
- "arrayWithObjects:"
- "arrayWithObjects:count:"
- "asDestination"
- "ascender"
- "associatePDFAnnotation:withAKAnnotation:"
- "associatedIndex"
- "asyncFindString:withDelegate:onQueue:"
- "asyncFindStrings:withDelegate:onQueue:"
- "asyncFindStrings:withOptions:withDelegate:onQueue:"
- "asyncWorkQueue"
- "attribute:atIndex:effectiveRange:"
- "attributedString"
- "attributedStringScaled:"
- "attributedTextInRange:"
- "attributes"
- "autoFillContentType"
- "autoFillContentTypeForCRContentType:"
- "autoFillDidInsertWithExplicitInvocationMode:"
- "autoFillTextContentType"
- "autoScale"
- "autoScaleFactor"
- "autoScaleFactorForPage:"
- "autoScaleFactorForPageWithSize:"
- "autoScales"
- "autocapitalizationType"
- "autocorrectionType"
- "autofillEntryType"
- "autofillNewContextStart"
- "autorelease"
- "backdropView"
- "backgroundColor"
- "backgroundImage"
- "backgroundImageForPage:withQuality:"
- "backgroundImageForPageIndex:withFoundQuality:"
- "backgroundImageLock"
- "backgroundImageQuality"
- "backgroundImagesEnabled"
- "backgroundQuality"
- "barTintColor"
- "base64EncodedStringWithOptions:"
- "baseURLForDocument:"
- "baseWritingDirectionForPosition:inDirection:"
- "beamWithPreferredLength:axis:"
- "becomeFirstResponder"
- "begin"
- "beginBatchPageChanges"
- "beginFindString:withOptions:"
- "beginFindStrings:withOptions:"
- "beginFloatingCursorAtPoint:"
- "beginIgnoringInteractionEvents"
- "beginPDFViewRotation"
- "beginningOfDocument"
- "bezierPath"
- "bezierPathWithRect:"
- "bezierPathWithRoundedRect:cornerRadius:"
- "blackColor"
- "blendedSelectionLayer"
- "block"
- "blockOperationWithBlock:"
- "blockQueuePairWithBlock:andQueue:"
- "blockingWaitDuration"
- "blocksWithTypes:inRegion:"
- "blueColor"
- "boldSystemFontOfSize:"
- "bookmarkLayer"
- "bookmarkSize"
- "bookmarked"
- "bookmarkedPages"
- "bookmarksChanged"
- "boolForKey:"
- "boolValue"
- "border"
- "borderColor"
- "borderKeyValues"
- "bottom"
- "bottomAnchor"
- "bottomLeft"
- "bottomRight"
- "boundingBox"
- "boundingQuad"
- "boundingRectWithSize:options:attributes:context:"
- "boundingRectWithSize:options:context:"
- "boundsArrayForPage:"
- "boundsForBox:"
- "boundsForPage:"
- "boundsForPageAtIndex:"
- "boundsInDocument"
- "boundsUpdateTimer"
- "bringSubviewToFront:"
- "bundleIdentifier"
- "bundleWithIdentifier:"
- "buttonType"
- "buttonWidgetState"
- "buttonWidgetStateString"
- "buttonWithConfiguration:primaryAction:"
- "c"
- "c16@0:8"
- "cStringUsingEncoding:"
- "cacheAppearances"
- "cacheKeyForPage:"
- "cachedAppearance:"
- "cachedContinuousSizeDisplayDirection"
- "cachedImageForPage:displayBox:thumbnailView:"
- "callDelegateDidReceiveAnalysis:forPage:"
- "callDelegateHandleTabFrom:direction:"
- "callPageVisibilityDelegateMethod:forPageView:atPageIndex:"
- "callPageVisibilityDelegateMethodForOverlayAdaptorOnly:forPageView:atPageIndex:"
- "callShouldReadAKInkAnnotations"
- "canBeMergedWith:"
- "canBecomeFirstResponder"
- "canGoBack"
- "canGoForward"
- "canGoToFirstPage"
- "canGoToLastPage"
- "canGoToNextPage"
- "canGoToPreviousPage"
- "canOpenURL:"
- "canPerformAction:withSender:"
- "canSaveWithAppendModeUsingOptions:"
- "canSaveWithTextFromOCR"
- "canUndo"
- "canZoomIn"
- "canZoomOut"
- "cancel"
- "cancelFind"
- "cancelFindString"
- "cancelFindStringWithHighlightsCleared"
- "cancelFindStringWithHighlightsCleared:"
- "cancelPreviousPerformRequestsWithTarget:selector:object:"
- "candidateForFormDetection"
- "candidateForOCR"
- "caption"
- "caretRectForPosition:"
- "caretTransformForPosition:"
- "caseInsensitiveCompare:"
- "cellForItemAtIndexPath:"
- "center"
- "centerAlign"
- "centerPointOfVisibleRectOfPage:"
- "centerXAnchor"
- "centerYAnchor"
- "cfValue"
- "cgImageRef"
- "cgPathArray"
- "cgSelectionForPage:"
- "cgSelectionPages"
- "cgSelections"
- "changeTimestamp"
- "changedAnnotation:"
- "changedAnnotations"
- "changedBoundsForBoxNotification:"
- "characterAtIndex:"
- "characterBoundsAtIndex:"
- "characterIndexAtPoint:"
- "characterIndexNearestPoint:"
- "characterIndexesForQuadPoints:onPageAtIndex:forAnnotationController:"
- "characterOffsetOfPosition:withinRange:"
- "characterRangeAtPoint:"
- "characterRangeByExtendingPosition:inDirection:"
- "checkResourceIsReachableAndReturnError:"
- "childAtIndex:"
- "children"
- "childrenLoaded"
- "choices"
- "class"
- "classForAnnotationType:"
- "classForPage"
- "cleanupFind"
- "clearAllDecoratedFoundText"
- "clearAnnotationChanges"
- "clearColor"
- "clearDictionaryRef"
- "clearFormData"
- "clearHighlightableSelectionForAnnotationController:"
- "clearHighlights"
- "clearPasswordField"
- "clearSearchHighlights"
- "clearSelection"
- "clearTiles"
- "clientHints"
- "closePath"
- "closestPositionToPoint:"
- "closestPositionToPoint:withinRange:"
- "coachMarkManager"
- "coachMarks"
- "code"
- "colRange"
- "collectionView:canEditItemAtIndexPath:"
- "collectionView:canFocusItemAtIndexPath:"
- "collectionView:canHandleDropSession:"
- "collectionView:canPerformAction:forItemAtIndexPath:withSender:"
- "collectionView:canPerformPrimaryActionForItemAtIndexPath:"
- "collectionView:contextMenuConfiguration:dismissalPreviewForItemAtIndexPath:"
- "collectionView:contextMenuConfiguration:highlightPreviewForItemAtIndexPath:"
- "collectionView:contextMenuConfigurationForItemAtIndexPath:point:"
- "collectionView:contextMenuConfigurationForItemsAtIndexPaths:point:"
- "collectionView:didBeginMultipleSelectionInteractionAtIndexPath:"
- "collectionView:didDeselectItemAtIndexPath:"
- "collectionView:didEndDisplayingCell:forItemAtIndexPath:"
- "collectionView:didEndDisplayingSupplementaryView:forElementOfKind:atIndexPath:"
- "collectionView:didHighlightItemAtIndexPath:"
- "collectionView:didSelectItemAtIndexPath:"
- "collectionView:didUnhighlightItemAtIndexPath:"
- "collectionView:didUpdateFocusInContext:withAnimationCoordinator:"
- "collectionView:dragPreviewParametersForItemAtIndexPath:"
- "collectionView:dragSessionAllowsMoveOperation:"
- "collectionView:dragSessionDidEnd:"
- "collectionView:dragSessionIsRestrictedToDraggingApplication:"
- "collectionView:dragSessionWillBegin:"
- "collectionView:dropPreviewParametersForItemAtIndexPath:"
- "collectionView:dropSessionDidEnd:"
- "collectionView:dropSessionDidEnter:"
- "collectionView:dropSessionDidExit:"
- "collectionView:dropSessionDidUpdate:withDestinationIndexPath:"
- "collectionView:itemsForAddingToDragSession:atIndexPath:point:"
- "collectionView:itemsForBeginningDragSession:atIndexPath:"
- "collectionView:performAction:forItemAtIndexPath:withSender:"
- "collectionView:performDropWithCoordinator:"
- "collectionView:performPrimaryActionForItemAtIndexPath:"
- "collectionView:previewForDismissingContextMenuWithConfiguration:"
- "collectionView:previewForHighlightingContextMenuWithConfiguration:"
- "collectionView:sceneActivationConfigurationForItemAtIndexPath:point:"
- "collectionView:selectionFollowsFocusForItemAtIndexPath:"
- "collectionView:shouldBeginMultipleSelectionInteractionAtIndexPath:"
- "collectionView:shouldDeselectItemAtIndexPath:"
- "collectionView:shouldHighlightItemAtIndexPath:"
- "collectionView:shouldSelectItemAtIndexPath:"
- "collectionView:shouldShowMenuForItemAtIndexPath:"
- "collectionView:shouldSpringLoadItemAtIndexPath:withContext:"
- "collectionView:shouldUpdateFocusInContext:"
- "collectionView:targetContentOffsetForProposedContentOffset:"
- "collectionView:targetIndexPathForMoveFromItemAtIndexPath:toProposedIndexPath:"
- "collectionView:targetIndexPathForMoveOfItemFromOriginalIndexPath:atCurrentIndexPath:toProposedIndexPath:"
- "collectionView:transitionLayoutForOldLayout:newLayout:"
- "collectionView:willDisplayCell:forItemAtIndexPath:"
- "collectionView:willDisplayContextMenuWithConfiguration:animator:"
- "collectionView:willDisplaySupplementaryView:forElementKind:atIndexPath:"
- "collectionView:willEndContextMenuInteractionWithConfiguration:animator:"
- "collectionView:willPerformPreviewActionForMenuWithConfiguration:animator:"
- "collectionViewDidEndMultipleSelectionInteraction:"
- "collectionViewLayout"
- "colorFromAppearanceTokens:"
- "colorWidgetBackgrounds"
- "colorWidgetBackgrounds:"
- "colorWithAlphaComponent:"
- "colorWithCGColor:"
- "colorWithRed:green:blue:alpha:"
- "colorWithWhite:alpha:"
- "columnAtPoint:"
- "columnAtPointIfAvailable:"
- "columnFrameAtPoint:"
- "com.apple.PDFKit.PDFExtensionView"
- "comb"
- "commit"
- "commitEditing"
- "commonCreateDictionaryRef"
- "commonCreateDictionaryRef:"
- "commonInit"
- "compare:"
- "compareFoundRange:toRange:inDocument:"
- "compareOrderFromDocument:toDocument:"
- "comparePosition:toPosition:"
- "completePointerInteractionRegionForRequest:"
- "completeRequestReturningItems:completionHandler:"
- "componentsSeparatedByString:"
- "compositingFilterWithRenderingProperties:"
- "configurationWithIdentifier:previewProvider:actionProvider:"
- "configurationWithIdentifier:sourcePoint:"
- "configurationWithScale:"
- "configureCell:withPage:indexPath:"
- "conformsToProtocol:"
- "constant"
- "constrainedScrollToPoint:"
- "constraintEqualToAnchor:"
- "constraintEqualToAnchor:constant:"
- "constraintEqualToAnchor:multiplier:constant:"
- "constraintEqualToConstant:"
- "containsAnnotation:"
- "containsDetectedFormFields"
- "containsEnd"
- "containsFormFields"
- "containsFormFieldsWithContentType"
- "containsIndex:"
- "containsIndexes:"
- "containsIndexesInRange:"
- "containsLargeImage"
- "containsObject:"
- "containsPoint:"
- "containsPoint:onPage:"
- "containsPoint:onPageLayer:"
- "containsStart"
- "containsString:"
- "containsText"
- "containsValueForKey:"
- "contentInset"
- "contentInsetAdjustmentBehavior"
- "contentOffset"
- "contentRect"
- "contentSize"
- "contentSizeWithCurrentPage:"
- "contentSnapshot"
- "contentStream"
- "contentType"
- "contentView"
- "contentsLocked"
- "contextMenuForBackgroundAtLocation:"
- "contextMenuForPage:"
- "contextMenuInteraction:configuration:dismissalPreviewForItemWithIdentifier:"
- "contextMenuInteraction:configuration:highlightPreviewForItemWithIdentifier:"
- "contextMenuInteraction:configurationForMenuAtLocation:"
- "contextMenuInteraction:previewForDismissingMenuWithConfiguration:"
- "contextMenuInteraction:previewForHighlightingMenuWithConfiguration:"
- "contextMenuInteraction:willDisplayMenuForConfiguration:animator:"
- "contextMenuInteraction:willEndForConfiguration:animator:"
- "contextMenuInteraction:willPerformPreviewActionForMenuWithConfiguration:animator:"
- "control"
- "controlType"
- "controller"
- "controller:didPlaceSingleShotAnnotation:onPageModelController:"
- "controller:performActionForMode:fromSender:withAttribute:onPageAtIndex:"
- "controller:setFormFillingEnabled:"
- "controller:shouldPlaceSingleShotAnnotation:onProposedPageModelController:"
- "controller:willPlaceSingleShotAnnotation:onProposedPageModelController:"
- "controller:willSetToolbarItems:"
- "controllerDidDismissPopover:"
- "controllerDidEnterToolMode:"
- "controllerDidExitToolMode:"
- "controllerShouldDetectFormElements:"
- "controllerWillDismissSignatureCaptureView:"
- "controllerWillDismissSignatureManagerView:"
- "controllerWillEnterToolMode:"
- "controllerWillExitToolMode:"
- "controllerWillShowSignatureCaptureView:"
- "controllerWillShowSignatureManagerView:"
- "controllerWithDelegate:"
- "conversationContext"
- "convertPoint:fromModelToOverlayWithPageIndex:forAnnotationController:"
- "convertPoint:fromOverlayToModelWithPageIndex:forAnnotationController:"
- "convertPoint:fromPage:"
- "convertPoint:fromPage:forScaleFactor:"
- "convertPoint:fromView:"
- "convertPoint:toPage:"
- "convertPoint:toPage:forScaleFactor:"
- "convertPoint:toView:"
- "convertPointToPageView:"
- "convertRect:fromLayer:"
- "convertRect:fromPage:"
- "convertRect:fromPage:forScaleFactor:"
- "convertRect:fromView:"
- "convertRect:toCoordinateSpace:"
- "convertRect:toLayer:"
- "convertRect:toPage:"
- "convertRect:toView:"
- "convertRectToPageView:"
- "convertRectToRootView:fromPageLayer:"
- "convertRootViewRect:toPageLayer:"
- "convertToFitMaximumHeight:"
- "copy:"
- "copyAsTextSelection"
- "copyDisplayList"
- "copyItemAtURL:toURL:error:"
- "copyPage:"
- "copyWithZone:"
- "coreFindString:"
- "coreFindStrings:"
- "coreResult"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createAKAnnotation"
- "createArrayRef"
- "createAttributedStringForCGSelection:scaled:"
- "createAttributedStringForTextWidget"
- "createCGPathArrayWithBezierPaths:"
- "createCoachMarkForPage:atFrame:"
- "createDefaultAppearanceStringWithFont:fontColor:"
- "createDetectedTextFieldWithBounds:font:textContentType:page:"
- "createDictionaryRef"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createDisplayListForFormDetection"
- "createFlashEffectForPDFLinkAnnotation:withLayer:forType:"
- "createHostView:forExtensionIdentifier:"
- "createLigtherColor:withIntensity:"
- "createOperatorTable"
- "createPDFAnnotationLayerEffectForAnnotation:withLayer:"
- "createPDFCoachmarkLayerEffectsWithFrame:withLayer:"
- "createPDFMarkupLayerEffectsForAnnotation:withLayer:"
- "createPDFNoteLayerEffectForAnnotation:withLayer:"
- "createPDFSelectionLayerEffectsForSelections:withLayer:"
- "createPageViewForPageAtIndex:withFrame:"
- "createPillBezier:inContext:"
- "createPixelBufferForPage:withBox:"
- "createRedactionPath"
- "createWithPKDrawing:bounds:"
- "createdWithWithHighLatencyDataProvider"
- "creationTime"
- "cropAnnotation"
- "cropApplied"
- "currentDestination"
- "currentDevice"
- "currentExifOrientationForPageAtIndex:"
- "currentGestureState"
- "currentModelBaseScaleFactorForPageAtIndex:"
- "currentPage"
- "currentPageChanged:"
- "currentPageIndex"
- "currentPoint"
- "currentSelection"
- "currentThread"
- "cyanColor"
- "d"
- "d16@0:8"
- "d24@0:8@16"
- "d32@0:8@16d24"
- "d32@0:8Q16@\"AKController\"24"
- "d32@0:8Q16@24"
- "d32@0:8{CGSize=dd}16"
- "d40@0:8{CGSize=dd}16d32"
- "darkGrayColor"
- "darkModeBackgroundColor"
- "darkModePageBackgroundColor"
- "dashCount"
- "dashCountRaw"
- "dashPattern"
- "dashPatternRaw"
- "data"
- "dataDetectorResults"
- "dataDetectorsEnabled"
- "dataFromRange:documentAttributes:error:"
- "dataRepresentation"
- "dataRepresentationWithOptions:"
- "dataSource"
- "dataWithBytes:length:"
- "datasourceQueue"
- "date"
- "ddResult"
- "dealloc"
- "debugDescription"
- "debugFlags"
- "debugQuickLookObject"
- "decodeBoolForKey:"
- "decodeFloatForKey:"
- "decodeIntForKey:"
- "decodeIntegerForKey:"
- "decodeObject"
- "decodeObjectOfClass:forKey:"
- "decodeUnknownAnnotationProperties"
- "decodeValueOfObjCType:at:"
- "decodeValueOfObjCType:at:size:"
- "decomposedStringWithCompatibilityMapping"
- "decorateFoundTextRange:inDocument:usingStyle:"
- "decrementRedactionCount"
- "defaultActiveColor"
- "defaultActiveColorTable"
- "defaultCenter"
- "defaultContextMenuForPage:"
- "defaultDAStringRef"
- "defaultGutterWidth"
- "defaultInactiveColor"
- "defaultManager"
- "defaultParagraphStyle"
- "defaultQueue"
- "defaultStringValue"
- "defaultStringValueForFieldNamed:"
- "delegate"
- "delegateKnowsDisplayAsBook"
- "delegateKnowsDisplayBox"
- "delegateKnowsDisplayMode"
- "delegateKnowsDisplayRTL"
- "delegateKnowsDisplaysDirection"
- "delegateKnowsDocumentMargins"
- "delegateKnowsIsUsingPageViewController"
- "delegateKnowsMargins"
- "delegateOrdersPageDrawing"
- "delegateRespondsToAllowFormFilling"
- "delegateRespondsToAllowFormFillingWithAutoFill"
- "delegateRespondsToAllowFormFillingWithConfidence"
- "delegateWillScale"
- "deleteAnnotation"
- "deleteBackward"
- "dequeueNotificationsMatching:coalesceMask:"
- "dequeueReusableCellWithIdentifier:"
- "dequeueReusableCellWithReuseIdentifier:forIndexPath:"
- "descender"
- "description"
- "deselectAllAnnotations"
- "destination"
- "destinationHistory"
- "destinationIndexPath"
- "detectedAnnotations"
- "detectedFieldRegionsExcludingFields:updateExcludedFields:"
- "detectedForm"
- "detectedFormFieldAtIndex:"
- "detectedFormFieldBoundingBoxesLayer"
- "detectedFormFieldDefaultFontName"
- "detectedFormFieldDefaultFontSize"
- "detectedFormFieldForAnnotation:"
- "detectedFormFieldNearestPoint:"
- "detectedFormFieldsRecognitionConfidence"
- "determineCurrentPage"
- "deviceColorSpace"
- "deviceIsiPad"
- "deviceIsiPhone"
- "dictationRecognitionFailed"
- "dictationRecordingDidEnd"
- "dictionary"
- "dictionaryRef"
- "dictionaryRefExcludingParentOrPopup"
- "dictionaryWithCapacity:"
- "dictionaryWithDictionary:"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "didBeginEditingPassword:inView:"
- "didCancelActiveSearch"
- "didChangeBounds"
- "didChangeValueForKey:"
- "didCopy"
- "didCopy:"
- "didDismissWritingTools"
- "didEndEditingPassword:inView:"
- "didForcePress"
- "didInsertPage:atIndex:"
- "didInsertPageAtIndex:"
- "didLongPressLink"
- "didLongPressPageIndex:atLocation:withAnnotationRect:"
- "didLongPressURL:atLocation:withAnnotationRect:"
- "didMatchString:"
- "didMoveToSuperview"
- "didMoveToWindow"
- "didPerformFormDetection"
- "didPerformOCR"
- "didPostPDFExtensionViewAnnotationLongPress"
- "didRemovePage:atIndex:"
- "didRemovePageAtIndex:"
- "didRemoveValueForAnnotationKey:"
- "didReplaceAllValuesWithNewDictionary:andOldDictionary:"
- "didRotatePageNotification:"
- "didSetValue:forAnnotationKey:"
- "didSwapPage:atIndex:forPage:atIndex:"
- "didSwapPageAtIndex:withIndex:"
- "difference"
- "digitalSignature"
- "disableUndoManagerForAK"
- "disableUndoRegistration"
- "dismissMenu"
- "dismissViewControllerAnimated:completion:"
- "display"
- "displayBox"
- "displayDirection"
- "displayGamut"
- "displayLayer:"
- "displayListCreationQueue"
- "displayMode"
- "displayName"
- "displayScale"
- "displayScaleOnPageLayer:"
- "displaySignaturePopoverOnSender:"
- "displaysAnnotations"
- "displaysAsBook"
- "displaysBookmarksForPages"
- "displaysPageBreaks"
- "displaysRTL"
- "document"
- "documentAnalysisEnabled"
- "documentAttributes"
- "documentCanBeEdited:"
- "documentChanged"
- "documentChanged:"
- "documentDidBeginDocumentFind:"
- "documentDidBeginPageFind:"
- "documentDidEndDocumentFind:"
- "documentDidEndPageFind:"
- "documentDidFindMatch:"
- "documentDidUnlock:"
- "documentIsLocked"
- "documentIsLocked:"
- "documentMargins"
- "documentMutated:"
- "documentRef"
- "documentScrollView"
- "documentURL"
- "documentUnlocked:"
- "documentView"
- "documentViewCenter"
- "documentViewCenterBeforeRotation"
- "documentViewController"
- "documentViewSize"
- "documentWasUnlocked"
- "done"
- "doneButton:"
- "doubleTapGestureRecognizer"
- "doubleValue"
- "downCaption"
- "dragInteraction"
- "dragInteraction:itemsForAddingToSession:withTouchAtPoint:"
- "dragInteraction:itemsForBeginningSession:"
- "dragInteraction:previewForLiftingItem:session:"
- "dragInteractionEnabled"
- "dragItem"
- "drawAccessibilityTags:"
- "drawAnnotationsWithBox:inContext:passingTest:"
- "drawAppearance:ofAnnotation:withBox:inContext:"
- "drawAppearance:ofAnnotation:withBox:inContext:scaleProportional:"
- "drawAppearance:ofAnnotation:withBox:inContext:scaleProportional:suppressTextRendering:"
- "drawAppearance:withBox:inContext:"
- "drawAppearance:withBox:inContext:inRect:scaleProportional:"
- "drawAppearance:withBox:inContext:inRect:scaleProportional:suppressTextRendering:"
- "drawAppearance:withBox:inContext:scaleProportional:"
- "drawArrowFrom:to:open:inContext:withBorder:"
- "drawAtPoint:"
- "drawBulletAtPoint:shape:inContext:withBorder:"
- "drawCachedAppearance:withBox:inContext:inRect:scaleProportional:"
- "drawCheckBox:inContext:withState:withBackgroundColor:withBorderColor:withFontColor:isHighlighted:"
- "drawComboBox:inContext:withAnnotation:withStringValue:withFont:withFontColor:"
- "drawCommentIconInRect:withColor:inContext:"
- "drawCommonCommentNoteIconToContext:color:rect:"
- "drawDetectedAnnotationBounds:"
- "drawDisclosureBox:inContext:"
- "drawForPage:active:"
- "drawForPage:withBox:active:"
- "drawForPage:withBox:active:inContext:"
- "drawHelpIconInRect:withColor:inContext:"
- "drawInContext:"
- "drawInContext:withBounds:withPopupAnnotation:"
- "drawInRect:"
- "drawInRect:inContext:"
- "drawInsertIconInRect:withColor:inContext:"
- "drawKeyIconInRect:withColor:inContext:"
- "drawLayer:inContext:"
- "drawListBox:inContext:withAnnotation:withOptions:withStringValue:withFont:withFontColor:"
- "drawNewParagraphIconInRect:withColor:inContext:"
- "drawNodeBoundingBoxesType:enableDrawing:"
- "drawNoteAsSelected:rect:"
- "drawNoteIconInRect:withColor:inContext:"
- "drawNoteInContext:withParentAnnotation:"
- "drawOCRQuads:"
- "drawPage:toContext:"
- "drawPagePost:toContext:"
- "drawParagraphIconInRect:withColor:inContext:"
- "drawProgressCallback"
- "drawPushButton:inContext:withBackgroundColor:withCaption:withFont:withFontColor:isHighlighted:"
- "drawRadioButton:inContext:withState:withBackgroundColor:withBorderColor:withFontColor:isHighlighted:"
- "drawTextBoundingBoxesType:enableDrawing:"
- "drawTextPreciseBoundingBoxes:"
- "drawTextSelectionBoundingBoxes:"
- "drawWithBox:"
- "drawWithBox:inContext:"
- "drawWithBox:inContext:isThumbnail:"
- "drawWithBox:inContext:withAKAnnotation:forAnnotation:"
- "drawWithBox:inContext:withAnnotation:"
- "drawWithBox:inContext:withButtonWidgetAnnotation:"
- "drawWithBox:inContext:withChoiceWidgetAnnotation:"
- "drawWithBox:inContext:withCircleAnnotation:"
- "drawWithBox:inContext:withFreeTextAnnotation:"
- "drawWithBox:inContext:withInkAnnotation:"
- "drawWithBox:inContext:withLineAnnotation:"
- "drawWithBox:inContext:withLinkAnnotation:"
- "drawWithBox:inContext:withMarkupAnnotation:"
- "drawWithBox:inContext:withOptions:"
- "drawWithBox:inContext:withPopupAnnotation:"
- "drawWithBox:inContext:withRedactAnnotation:"
- "drawWithBox:inContext:withSignatureWidgetAnnotation:"
- "drawWithBox:inContext:withSquareAnnotation:"
- "drawWithBox:inContext:withStampAnnotation:"
- "drawWithBox:inContext:withTextAnnotation:"
- "drawWithBox:inContext:withTextWidgetAnnotation:"
- "drawWithBox:inContext:withUnknownAnnotation:"
- "drawWithBox:toContext:"
- "drawWithRect:options:context:"
- "drawingBounds"
- "editCheckpointReachedForAnnotationController:"
- "editDetectedForAnnotationController:"
- "editMenuForTextRange:suggestedActions:"
- "editMenuInteraction"
- "editMenuInteraction:menuForConfiguration:suggestedActions:"
- "editMenuInteraction:targetRectForConfiguration:"
- "editMenuInteraction:willDismissMenuForConfiguration:animator:"
- "editMenuInteraction:willPresentMenuForConfiguration:animator:"
- "editNoteForAnnotation:"
- "editTextAnnotation:selectAllText:"
- "editable"
- "effectLayerOCRContent"
- "effectTimeLeft"
- "elementWithViewProvider:"
- "enableBackgroundImages"
- "enableBackgroundImages:"
- "enableDataDetectors"
- "enableDocumentMRUMode:"
- "enableHighlightDetectedFormFields:"
- "enableLimitedSearch"
- "enablePageShadows"
- "enablePageShadows:"
- "enableRoundPageCorners"
- "enableTileUpdates"
- "enableUndoManagerForAK:"
- "enableUndoRegistration"
- "enablesReturnKeyAutomatically"
- "enablesTileUpdates"
- "encodeBool:forKey:"
- "encodeConditionalObject:forKey:"
- "encodeDouble:forKey:"
- "encodeFloat:forKey:"
- "encodeInt:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeValueOfObjCType:at:"
- "encodeWithCoder:"
- "end"
- "endBatchPageChanges"
- "endEditing:"
- "endEditingTextAnnotation"
- "endFloatingCursor"
- "endIgnoringInteractionEvents"
- "endLineStyle"
- "endOfDocument"
- "endPDFViewRotation"
- "endPDFViewRotationWithContentInset:"
- "enforceAutoScaleFactor"
- "enqueueNotification:postingStyle:"
- "ensureDisplayList"
- "enumerateApplicationDataUsingBlock:"
- "enumerateAttribute:inRange:options:usingBlock:"
- "enumerateAttributesInRange:options:usingBlock:"
- "enumerateIndexesUsingBlock:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsAtIndexes:options:usingBlock:"
- "enumerateObjectsUsingBlock:"
- "enumerateObjectsWithOptions:usingBlock:"
- "enumerateRangesUsingBlock:"
- "enumerateRectsAndTransformsForPage:usingBlock:"
- "environment"
- "errorWithDomain:code:userInfo:"
- "exchangeObjectAtIndex:withObjectAtIndex:"
- "exchangePageAtIndex:withPageAtIndex:"
- "exportedInterface"
- "extendSelectionAtEnd:"
- "extendSelectionAtStart:"
- "extendSelectionForLineBoundaries"
- "extendedBoundsForAction:"
- "extendedRootViewBounds"
- "extension"
- "extensionContext"
- "extensionInterface"
- "extensionProxy"
- "extensionSnapshotToHost:scale:"
- "extensionToHost:"
- "extensionViewBoundsInDocument"
- "extensionViewController"
- "extensionViewFrame"
- "extensionViewZoomScale"
- "extensionWithIdentifier:error:"
- "facingPageForPage:"
- "fadeAwayWithCompletion:"
- "fetchAnnotationFromTaggedNodeRef:"
- "fetchAnnotationsWithCompletion:deliveredOnQueue:"
- "fetchPageLayoutWithCompletion:deliveredOnQueue:"
- "fieldArray"
- "fieldName"
- "fieldNamed:"
- "fieldNames"
- "fieldSource"
- "fieldType"
- "fieldValue"
- "fields"
- "fieldsIncludedAreCleared"
- "fileExistsAtPath:"
- "fileURLWithPath:"
- "fill"
- "fillOval:color:context:"
- "fillRect:color:context:"
- "filledButtonConfiguration"
- "filterWithType:"
- "find:"
- "findFirstResponder"
- "findInteraction"
- "findInteraction:didBeginFindSession:"
- "findInteraction:didEndFindSession:"
- "findInteraction:sessionForView:"
- "findInteractionEnabled"
- "findNext"
- "findNext:"
- "findNextActivatableAnnotationFromPage:fromAnnotation:direction:withCompletion:"
- "findOnPage"
- "findPageViewControllerForPageIndex:"
- "findPageWithCGPDFDictionaryPageRef:"
- "findPrevious"
- "findPrevious:"
- "findString"
- "findString:fromSelection:withOptions:"
- "findString:withOptions:"
- "findStringPerPage:fromSelection:withOptions:"
- "findStringUpdate"
- "findStringUpdate:done:"
- "findStrings:withinSelection:withOptions:"
- "finishedSearching"
- "firstCharCenter"
- "firstIndex"
- "firstObject"
- "firstPage"
- "firstRectForRange:"
- "firstResponder"
- "firstSpanBoundsForPage:"
- "firstVisiblePage"
- "flags"
- "flipsTileContents"
- "floatValue"
- "focusOnColumnAtPoint:"
- "focusOnPasswordField"
- "focusOnSearchResultAtIndex"
- "focusOnSearchResultAtIndex:"
- "font"
- "fontColor"
- "fontName"
- "fontNameFromAppearanceTokens:"
- "fontWithDescriptor:size:"
- "fontWithName:size:"
- "fontWithPDFFont:size:"
- "fontWithSize:"
- "force"
- "forceBreaks"
- "forceSetBackgroundImage:forPageIndex:"
- "forceTileRefresh"
- "forceTileUpdate"
- "forceUpdateActivePageIndex:withMaxDuration:"
- "forcesTopAlignment"
- "foregroundColor"
- "foregroundColorForOptions:"
- "foregroundColorHDR"
- "foregroundColorSDR"
- "formContentType"
- "formData"
- "formFieldGroupForAnnotation:"
- "formFillingQueue"
- "formFillingUpdatesAnnotationOnEveryTextChange"
- "formLock"
- "formRegionsExcluding:updateExcludedFields:"
- "formValue"
- "format"
- "formness"
- "foundRange:forSearchString:inDocument:"
- "foundResults:forDocument:"
- "foundResults:forPage:"
- "frame"
- "frameForDictationResultPlaceholder:"
- "fromPage"
- "function"
- "functionalDisplayMode"
- "gcCreateAttributesForFont:color:"
- "gcCreateBoxDictionary"
- "generalPasteboard"
- "generateInternalDocumentGeometry"
- "generationID"
- "geometryInterface"
- "gestureInit"
- "gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:"
- "gestureRecognizer:shouldReceiveEvent:"
- "gestureRecognizer:shouldReceivePress:"
- "gestureRecognizer:shouldReceiveTouch:"
- "gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:"
- "gestureRecognizer:shouldRequireFailureOfGestureRecognizer:"
- "gestureRecognizerShouldBegin:"
- "gestureRecognizers"
- "gestureType"
- "getAKTextView"
- "getActiveAnnotation"
- "getAnnotations"
- "getAppearancesFromDictionary:ofType:"
- "getCRDocumentOutputRegion"
- "getCROutputRegion"
- "getChildren"
- "getColorFromAppearanceNSString:"
- "getColorFromAppearanceString:"
- "getDisplayListWithCompletion:onQueue:"
- "getDrawingTransformForBox:"
- "getFontFromAppearanceNSString:"
- "getFontFromAppearanceString:"
- "getPDFAnnotationAssociatedWith:"
- "getPDFKeyMappingDictionary"
- "getProperNameStringFromString:"
- "getRed:green:blue:alpha:"
- "getResourceValue:forKey:error:"
- "getSelectedAnnotations"
- "goBack:"
- "goForward:"
- "goToDestination"
- "goToDestination:"
- "goToDestination:point:"
- "goToDestinationNoPush:"
- "goToFirstPage:"
- "goToLastPage:"
- "goToNextPage:"
- "goToPage"
- "goToPage:"
- "goToPage:animated:"
- "goToPage:direction:animated:"
- "goToPageIndex"
- "goToPageIndex:"
- "goToPageIndex:pageFrame:"
- "goToPageIndex:withViewFrustum:"
- "goToPageNoPush:"
- "goToPageNoPush:animated:"
- "goToPageWithoutBackgroundUpdate:"
- "goToPreviousPage:"
- "goToRect:onPage:"
- "goToSelection:"
- "goToURL"
- "goToURL:atLocation:"
- "grayColor"
- "greekingThreshold"
- "greenColor"
- "groupTableViewBackgroundColor"
- "gutterWide"
- "gutterWidth"
- "hCornerRadius"
- "handleAnalysisCompletionOfPage:resultTypes:"
- "handleBackTab"
- "handleBackTabInDetectedFormField"
- "handleBackTabInTextEditorForAnnotation:forAnnotationController:"
- "handleBackTabInTextWidget:"
- "handleGesture"
- "handleGesture:"
- "handleGesture:state:location:"
- "handleGesture:state:location:locationOfFirstTouch:isIndirectTouch:"
- "handlePageOrderedCollectionDifference:"
- "handleTab"
- "handleTabInDetectedFormField"
- "handleTabInTextEditorForAnnotation:forAnnotationController:"
- "handleTabInTextWidget:"
- "handleTextSuggestion:completionHandler:"
- "handleTextSuggestion:forAnnotationController:completionHandler:"
- "handledByPDFKit"
- "handledByPDFKitCheckAKEnabled:"
- "hasActionsForResult"
- "hasActiveDrag"
- "hasAppearanceStream"
- "hasArtBox"
- "hasBackgroundImage"
- "hasBleedBox"
- "hasBoundedHeight"
- "hasBoundedWidth"
- "hasChanges"
- "hasComb"
- "hasContent"
- "hasCropBox"
- "hasHighLatencyDataProvider"
- "hasHighlightableSelectionForAnnotationController:"
- "hasItemConformingToTypeIdentifier:"
- "hasItemsConformingToTypeIdentifiers:"
- "hasPopups"
- "hasPrefix:"
- "hasRunActionsForResult"
- "hasSelection"
- "hasStartedWork"
- "hasText"
- "hasTrimBox"
- "hash"
- "hashTableWithOptions:"
- "heightAnchor"
- "hideActiveMenus"
- "hideMenu"
- "hideTileLayer:"
- "highlight:"
- "highlightDetectedFormFields:"
- "highlightPDFRedactions:"
- "highlightRange"
- "highlightRedaction:"
- "highlightRef"
- "highlightableSelectionCharacterIndexesOnPageAtIndex:forAnnotationController:"
- "highlighted"
- "highlightedSelections"
- "highlights"
- "hintScrollDirectionHorizontal:andVertical:"
- "historyIndex"
- "hitTest:withEvent:"
- "hitTestForSubviewsOfView:atLocation:withEvent:"
- "horizontalCornerRadius"
- "horizontalScaleFactor"
- "horizontalScaleFactorBeforeRotation"
- "horizontalSizeClass"
- "host"
- "hostInterface"
- "hostProxy"
- "hostScrollView"
- "hostScrollViewObserverIsActive"
- "hostToExtension:"
- "hostViewController"
- "hostViewControllerDelegate"
- "html"
- "htmlData"
- "i16@0:8"
- "icon"
- "iconConfigurationHandler"
- "iconScale"
- "iconType"
- "identifier"
- "ignoreChangedBoundsForBoxNotification"
- "imageDrawingOperationQueue"
- "imageNamed:inBundle:compatibleWithTraitCollection:"
- "imageOfSize:forBox:withOptions:"
- "imageView"
- "imageWithActions:"
- "imageWithRenderingMode:"
- "imageWithTintColor:renderingMode:"
- "inFormFillingMode"
- "inMarkupMode"
- "included"
- "incrementRedactionCount"
- "index"
- "indexForPage:"
- "indexOfFirstCharacterOnPage:"
- "indexOfItemIdentifier:"
- "indexOfLastCharacterOnPage:"
- "indexOfObject:"
- "indexOfObject:inSortedRange:options:usingComparator:"
- "indexOfObjectIdenticalTo:"
- "indexOfObjectPassingTest:"
- "indexOfSectionIdentifier:"
- "indexPathForItem:inSection:"
- "indexPathForItemAtPoint:"
- "indexPathForPreferredFocusedViewInCollectionView:"
- "indexPathForRow:inSection:"
- "indexPathsForSelectedItems"
- "indexSet"
- "indexSetForQuadPoints"
- "indexSetWithIndexesInRange:"
- "indexesPassingTest:"
- "infoDictionary"
- "inhibitAutoScroll"
- "init"
- "initCommonWithBounds:"
- "initFromPos:toPos:"
- "initFromThumbnailView:"
- "initPageCornerRadiusForMagnification:"
- "initWithActionDictionary:forDocument:forPage:"
- "initWithAddedAnnotation:"
- "initWithAnnotation:"
- "initWithAnnotation:pdfPageView:pdfView:"
- "initWithAnnotationDictionary:forControlType:"
- "initWithAnnotationDictionary:forPage:"
- "initWithArrangedSubviews:"
- "initWithArray:"
- "initWithAttributedString:"
- "initWithBarButtonItems:representativeItem:"
- "initWithBarButtonSystemItem:target:action:"
- "initWithBase64EncodedString:options:"
- "initWithBlock:andQueue:"
- "initWithBounds:forType:withProperties:"
- "initWithCFObject:"
- "initWithCGImage:"
- "initWithCGImage:options:"
- "initWithCGImage:scale:orientation:"
- "initWithCGPDFAnnotation:forPage:"
- "initWithCString:encoding:"
- "initWithCVPixelBuffer:options:session:"
- "initWithCapacity:"
- "initWithChangedAnnotation:"
- "initWithCoder:"
- "initWithCollectionView:cellProvider:"
- "initWithContainer:center:"
- "initWithDDResult:"
- "initWithDDScannerResult:foundOnPage:"
- "initWithData:"
- "initWithData:encoding:"
- "initWithDelegate:"
- "initWithDelegate:andRenderingProperties:"
- "initWithDestination:"
- "initWithDictionary:"
- "initWithDictionary:forDocument:"
- "initWithDictionary:forDocument:parent:"
- "initWithDictionary:forPage:"
- "initWithDocument:"
- "initWithDocumentName:"
- "initWithDropOperation:"
- "initWithDropOperation:intent:"
- "initWithFormDictionary:"
- "initWithFormat:arguments:"
- "initWithFrame:"
- "initWithFrame:annotation:"
- "initWithFrame:collectionViewLayout:"
- "initWithFrame:forPageLayer:withRenderingTransform:tileContentsScale:generationID:"
- "initWithFrame:style:"
- "initWithFrame:textContainer:"
- "initWithHandler:"
- "initWithImage:"
- "initWithImage:options:"
- "initWithImage:requestType:"
- "initWithImage:style:target:action:"
- "initWithImageSource:"
- "initWithIndexSet:"
- "initWithIndexesInRange:"
- "initWithItemProvider:"
- "initWithKeyOptions:valueOptions:capacity:"
- "initWithName:"
- "initWithNibName:bundle:"
- "initWithNormalizedBoundingBox:size:"
- "initWithObject:keyPath:options:block:"
- "initWithObjects:"
- "initWithOffset:onPage:"
- "initWithPDFAnnotation:andAKAnnotation:"
- "initWithPDFDocument:andView:"
- "initWithPDFDocument:pdfView:andAKController:"
- "initWithPDFPage:"
- "initWithPDFPage:pageModelController:"
- "initWithPDFPageLayer:"
- "initWithPDFPageView:"
- "initWithPDFRenderingProperties:"
- "initWithPDFView:"
- "initWithPDFView:pageIndex:navigationOrientation:withRenderingProperties:andOptions:"
- "initWithPKDrawing:bounds:"
- "initWithPage:"
- "initWithPage:atPoint:"
- "initWithPage:displayBox:"
- "initWithPage:geometryInterface:andRenderingProperties:"
- "initWithPage:offset:"
- "initWithPage:range:"
- "initWithPageIndex:atPoint:fileURL:"
- "initWithPageNumber:pageRect:rotation:"
- "initWithPageRef:"
- "initWithParent:"
- "initWithParent:stream:resources:"
- "initWithParentAnnotation:owningPageView:owningPDFView:"
- "initWithPreviewProvider:"
- "initWithProperties:"
- "initWithProvider:"
- "initWithRect:andKind:"
- "initWithRect:identifier:"
- "initWithRect:onPage:"
- "initWithRemovedAnnotation:"
- "initWithReorderedAndChangedAnnotation:"
- "initWithReorderedAnnotation:"
- "initWithRootViewController:"
- "initWithScannerType:passiveIntent:"
- "initWithSearchString:aggregator:"
- "initWithSearchableObject:"
- "initWithSelector:forTarget:"
- "initWithSessionDelegate:"
- "initWithSettings:"
- "initWithSize:"
- "initWithString:"
- "initWithString:attributes:"
- "initWithString:range:"
- "initWithString:relativeToURL:"
- "initWithStyle:"
- "initWithStyle:reuseIdentifier:"
- "initWithTable:onPage:"
- "initWithTarget:action:"
- "initWithText:selectedRange:"
- "initWithTextInput:"
- "initWithTextLineRects:"
- "initWithThrottleDelay:forSelector:forTarget:"
- "initWithTitle:style:target:action:"
- "initWithTopLeft:topRight:bottomLeft:bottomRight:"
- "initWithTransitionStyle:navigationOrientation:options:"
- "initWithURL:"
- "initWithUTF8String:"
- "initWithView:"
- "initWithView:parameters:target:"
- "initialize"
- "initializeExifAndScaleOnAnnotation:"
- "inlinePredictionType"
- "inputAssistantItem"
- "inputDelegate"
- "insertAdaptiveImageGlyph:replacementRange:"
- "insertAnnotation:atIndex:"
- "insertAttributedText:"
- "insertChild:atIndex:"
- "insertDictationResult:"
- "insertDictationResultPlaceholder"
- "insertFileAtURL:atIndex:completionHandler:"
- "insertFormFieldAtBestLocationNearPoint:onPage:"
- "insertFormFieldAtDefaultLocation"
- "insertFormFieldWithBounds:onPage:"
- "insertInputSuggestion:"
- "insertObject:atIndex:"
- "insertObjects:atIndexes:"
- "insertPage:atIndex:"
- "insertPages:atIndexes:"
- "insertSublayer:above:"
- "insertSublayer:atIndex:"
- "insertSublayer:below:"
- "insertSubview:aboveSubview:"
- "insertText:"
- "insertText:alternatives:style:"
- "insertTextPlaceholderWithSize:"
- "insertTextSuggestion:completionHandler:"
- "insetBoundsInDocument"
- "installDrawingGestureRecognizer:forPageAtIndex:forAnnotationController:"
- "instanceForPlatformWithPDFView:"
- "instanceMethodForSelector:"
- "instantiateViewControllerWithInputItems:connectionHandler:"
- "intValue"
- "integerValue"
- "integralDrawingBounds"
- "interactWithAnnotation:"
- "interactionDidEnd:"
- "interactionShouldBegin:atPoint:"
- "interactionWillBegin:"
- "interactions"
- "interactiveBackgroundColor"
- "interfaceWithProtocol:"
- "interiorColor"
- "internalForceAnnotationRefresh"
- "internalForceTileRefresh"
- "interpolationQuality"
- "intersectSet:"
- "intersectsWithRedactionPath"
- "invalidate"
- "invalidateAppearanceStream"
- "invalidateContentView"
- "invalidateDictionaryRef"
- "invalidateInternalDocumentGeometry"
- "invalidateIntrinsicContentSize"
- "invertedSet"
- "invocationWithMethodSignature:"
- "invoke"
- "ioSurfaceRef"
- "isActivatableTextField"
- "isAnnotationEditingEnabled"
- "isAppearanceStreamEmpty"
- "isAutofillNewContextStart"
- "isBookmarked"
- "isCandidateForFormDetection"
- "isCandidateForOCR"
- "isCreatedByCalendar:"
- "isDarkMode"
- "isDashed"
- "isDetectedCheckbox"
- "isDetectedSignature"
- "isDetectedTextField"
- "isDocumentAnalysisEnabled"
- "isDragging"
- "isEditable"
- "isEditingText"
- "isEmpty"
- "isEncrypted"
- "isEqual:"
- "isEqualToDictionary:"
- "isEqualToIndexSet:"
- "isEqualToSelection:"
- "isEqualToString:"
- "isExcludingAKAnnotationRenderingForThisThread"
- "isFileURL"
- "isFindInteractionEnabled"
- "isFindNavigatorVisible"
- "isFinding"
- "isFirstResponder"
- "isFormDetectionEnabled"
- "isFormField"
- "isFullyConstructed"
- "isHandlingEditDetected"
- "isHidden"
- "isHighlighted"
- "isInFormFillingMode"
- "isInMarkupMode"
- "isIndirectTouch"
- "isInvisible"
- "isKindOfClass:"
- "isLinearized"
- "isListChoice"
- "isLocked"
- "isMainThread"
- "isMarkupAnnotation"
- "isMarkupAnnotationSubtype"
- "isMemberOfClass:"
- "isMultiline"
- "isNativeRotationDrawingEnabledForThisThread"
- "isNoteAnnotation"
- "isObservingAKAnnotation"
- "isObservingPageModel"
- "isOpen"
- "isOverLinkAnnotation:"
- "isOverlayViewInstalled"
- "isOverlayViewLoadedAtIndex:"
- "isPageCandidateForOCR"
- "isPageCandidateForOCR:"
- "isPageCandidateForOCR:completion:"
- "isPasswordField"
- "isPerformingUndo"
- "isPointInHandle:whichHandle:"
- "isProxy"
- "isReadOnly"
- "isReadOnlyAnnotation"
- "isRectVisible:onPage:"
- "isRedaction"
- "isRequested"
- "isSecureTextEntry"
- "isSelected"
- "isSignature"
- "isSignatureMarker"
- "isSignatureWidget"
- "isSolariumEnabled"
- "isStandaloneGraphic"
- "isSuspiciousURL"
- "isSyncingFromAKAnnotation"
- "isSyncingFromAKPageModel"
- "isSyncingFromPDFAnnotation"
- "isSyncingFromPDFPage"
- "isSynthesizedFormField"
- "isTableCellSelection"
- "isTextFormField"
- "isTextFromOCR"
- "isTextMarkupAnnotation"
- "isTextMarkupOrNoteAnnotation"
- "isTextSelectionEnabled"
- "isTextWidget"
- "isTornDown"
- "isTransparent"
- "isUndoRegistrationEnabled"
- "isUnlocked"
- "isUpdateQueued"
- "isUpdatingSelectionMarkups"
- "isUsingPDFExtensionView"
- "isUsingPageViewController"
- "isValidPassword:"
- "isVertical"
- "isVisible"
- "isWidgetOrMarkupAnnotation"
- "isWorking"
- "isZooming"
- "item"
- "itemIdentifierForIndexPath:"
- "itemProvider"
- "itemProvider:registerDataRepresentationForPage:draggedPages:"
- "itemProvider:registerFileRepresentationForPage:draggedPages:"
- "itemProviders"
- "items"
- "itemsForDragWithSession:atIndexPath:"
- "keyCommandWithInput:modifierFlags:action:"
- "keyCommands"
- "keyEnumerator"
- "keyPath"
- "keyPathsForValuesAffectingValueForKey:"
- "keyboardAppearance"
- "keyboardType"
- "keysForValuesToObserveForUndo"
- "killExtensionProcess"
- "kind"
- "label"
- "labelRegion"
- "labelText"
- "largeColorPotForColor:"
- "largeStrikeOutPot"
- "largeUnderlinePot"
- "lastAnnotationChange"
- "lastFocusState"
- "lastHorizontalScrollDirection"
- "lastIndex"
- "lastObject"
- "lastPage"
- "lastPageIndex"
- "lastPathComponent"
- "lastSpanBoundsForPage:"
- "lastVerticalScrollDirection"
- "lastVisiblePage"
- "layer"
- "layerContainingQuickBackgroundForLoupeOnOverlayAtPageIndex:forAnnotationController:"
- "layerEffect"
- "layerEffectTransform"
- "layerWillDraw:"
- "layoutComponents"
- "layoutDirection"
- "layoutDocumentView"
- "layoutIfNeeded"
- "layoutMode"
- "layoutSublayers"
- "layoutSublayersOfLayer:"
- "layoutSubviews"
- "lazilyLoadAnnotations"
- "leading"
- "leadingAnchor"
- "left"
- "leftMostCharCenter"
- "length"
- "lightGrayColor"
- "lineStyleFromName:"
- "lineWidth"
- "lineWidthThreshold"
- "linearizedRangesForPage:"
- "linkRegionsConstrainedToLineAtPoint:"
- "listChoice"
- "loadExtension:"
- "loadFileRepresentationForTypeIdentifier:completionHandler:"
- "loadImageWithPage:displayBox:thumbnailView:completionHandler:"
- "localDragSession"
- "localObject"
- "localTimeZone"
- "localizedCaseInsensitiveContainsString:"
- "localizedStringForKey:value:table:"
- "localizedStringFromNumber:numberStyle:"
- "locationInView:"
- "locationOfFirstTouch"
- "locationOfFirstTouchInView:"
- "lock"
- "lockWithOptions:seed:"
- "longPressGestureRecognizer"
- "longPressGestureStartTime"
- "lowercaseLetterCharacterSet"
- "lowercaseString"
- "mainBundle"
- "mainQueue"
- "mainRunLoop"
- "mainScreen"
- "mainScreenBounds"
- "mainScreenScale"
- "majorVersion"
- "makeDatasource"
- "makeObjectsPerformSelector:"
- "mapTableWithKeyOptions:valueOptions:"
- "markedTextRange"
- "markedTextStyle"
- "markupAnnotationsForIndexSet:"
- "markupEffectLayers"
- "markupStyle"
- "markupType"
- "marqueeEffect"
- "mathExpressionCompletionType"
- "matrix"
- "maxCharacterCount"
- "maxPageRectWithPageIndex:forAnnotationController:"
- "maxScale"
- "maxScaleFactor"
- "maxX"
- "maxY"
- "maximumLength"
- "maximumNumberOfCharacters"
- "maximumPossibleForce"
- "maximumZoomScale"
- "menuElementsForPage:"
- "menuWithChildren:"
- "menuWithTitle:children:"
- "menuWithTitle:image:identifier:options:children:"
- "methodForSelector:"
- "methodInvocation"
- "methodSignatureForSelector:"
- "minScale"
- "minScaleFactor"
- "minX"
- "minY"
- "minimumZoomScale"
- "minorVersion"
- "minusSet:"
- "modelBaseScaleFactorOfPageAtIndex:forAnnotationController:"
- "modelController"
- "modernToolbarView"
- "monospacedSystemFontOfSize:weight:"
- "mouseDownAction"
- "mouseUpAction"
- "movePage:toIndex:"
- "movePageWithTransaction:"
- "moveToPoint:"
- "multiline"
- "mutableArrayValueForKey:"
- "mutableCopy"
- "mutableCopyWithZone:"
- "mutableSetValueForKey:"
- "nameForLineStyle:"
- "namedDestination:"
- "navigationItem"
- "newContentSnapshotPDFDataIncludingAdornments:atScale:inRect:onOverlayAtPageIndex:forAnnotationController:"
- "newPDFAnnotationFromAKAnnotation:"
- "newXMPFromData:preserveExistingXMPMetadata:"
- "newlineCharacterSet"
- "nextActions"
- "nextPage"
- "nextResponder"
- "normalize"
- "normalizeFindOptions:"
- "normalizedBoundsForBox:ofPageAtIndex:"
- "normalizedBoundsForPageAtIndex:"
- "normalizedPageBounds:"
- "normalizedToCIImageTransformForImageWithSize:"
- "normalizedToPageTransformForPageWithBounds:"
- "noteBounds"
- "noteContainsPoint:"
- "noteLayer"
- "notificationWithName:object:"
- "notificationWithName:object:userInfo:"
- "now"
- "null"
- "numFound"
- "numberOfCharacters"
- "numberOfChildren"
- "numberOfComponentsInPickerView:"
- "numberOfItems"
- "numberOfItemsInSection:"
- "numberOfSectionsInCollectionView:"
- "numberOfSectionsInTableView:"
- "numberOfSegments"
- "numberOfTapsRequired"
- "numberOfTextRangesOnPage:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithLong:"
- "numberWithUnsignedChar:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLong:"
- "objCType"
- "object"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectEnumerator"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observeValueForKeyPath:ofObject:change:context:"
- "observedObject"
- "offset"
- "offsetFromPosition:toPosition:"
- "oldBounds"
- "oldMagnification"
- "op_Do:"
- "op_Q:"
- "op_TJ:"
- "op_Tj:"
- "op_cm:"
- "op_doublequote:"
- "op_q:"
- "op_singlequote:"
- "opaqueSelectionLayer"
- "open"
- "openURL:options:completionHandler:"
- "options"
- "orangeColor"
- "orderedSetWithArray:"
- "originalExifOrientation"
- "originalFrame"
- "originalImageDescription"
- "originalModelBaseScaleFactor"
- "outlineItemForSelection:"
- "outlineRoot"
- "overlayViewAtIndex:"
- "overlayViewInstalled"
- "overlayViewInstalledForPage:"
- "overlayViewWillBeUninstalledForPage:"
- "pageAfter:"
- "pageAnnotationChanges"
- "pageAnnotationEffects"
- "pageAtIndex:"
- "pageBackgroundColor"
- "pageBackgroundColorHint"
- "pageBackgroundManager"
- "pageBefore:"
- "pageBreakMargins"
- "pageChanged:"
- "pageClass"
- "pageColor"
- "pageCornerRadius"
- "pageCount"
- "pageForPoint:nearest:"
- "pageFrame"
- "pageFrames"
- "pageIfExists"
- "pageIndexForAnnotation:"
- "pageLabelView"
- "pageLayer"
- "pageLayerDidAppear:"
- "pageLayerEffectForID:"
- "pageLayerWillRemove:"
- "pageLayout"
- "pageLayoutBounds"
- "pageLayoutIfAvail"
- "pageLayoutLock"
- "pageMargins"
- "pageModelControllerForAnnotation:"
- "pageNearestPoint:currentPage:"
- "pageNumber"
- "pageNumberIndicator"
- "pageOverlayViewProvider"
- "pagePreloadQueue"
- "pageRef"
- "pageShadowMetrics"
- "pageShadowsEnabled"
- "pageSignatures"
- "pageSurface"
- "pageSyncDate"
- "pageSyncTimer"
- "pageView"
- "pageViewContainerView"
- "pageViewController:didFinishAnimating:previousViewControllers:transitionCompleted:"
- "pageViewController:spineLocationForInterfaceOrientation:"
- "pageViewController:viewControllerAfterViewController:"
- "pageViewController:viewControllerBeforeViewController:"
- "pageViewController:willTransitionToViewControllers:"
- "pageViewControllerOptions"
- "pageViewControllerPreferredInterfaceOrientationForPresentation:"
- "pageViewControllerSaysPageChanged:"
- "pageViewControllerSupportedInterfaceOrientations:"
- "pageViewForPageAtIndex:"
- "pageViewSizeForPage:"
- "pageViews"
- "pages"
- "panGestureRecognizer"
- "parent"
- "parentAnnotation"
- "parentViewController"
- "passwordField"
- "passwordRules"
- "passwordUsedForUnlocking"
- "passwordViewController"
- "pasteAfterPage:"
- "pathIntersectsWithRedactionPath:"
- "pathLock"
- "paths"
- "pdfAnnotation"
- "pdfAnnotationUUID"
- "pdfDocument"
- "pdfDocument:detectedAnnotations:forPage:"
- "pdfDocument:didExchangePage:atIndex:withPage:atIndex:"
- "pdfDocument:didInsertPage:atIndex:"
- "pdfDocument:didReceiveAnalysis:forPage:"
- "pdfDocument:didRemovePage:atIndex:"
- "pdfDocument:didReplacePagePlaceholder:atIndex:withPage:"
- "pdfDocument:handleTabFrom:direction:"
- "pdfDocument:loadedAnnotations:forPage:"
- "pdfDocumentAppendModeActiveForThisThread"
- "pdfDocumentDidRemoveAllPagesOrPlaceholders:"
- "pdfDocumentView"
- "pdfDocumentViewSize"
- "pdfHostViewController:didLongPressPageIndex:atLocation:"
- "pdfHostViewController:didLongPressPageIndex:atLocation:withAnnotationRect:"
- "pdfHostViewController:didLongPressURL:atLocation:"
- "pdfHostViewController:didLongPressURL:atLocation:withAnnotationRect:"
- "pdfHostViewController:documentDidUnlockWithPassword:"
- "pdfHostViewController:findStringUpdate:done:"
- "pdfHostViewController:goToPageIndex:"
- "pdfHostViewController:goToPageIndex:withViewFrustum:"
- "pdfHostViewController:goToURL:"
- "pdfHostViewController:goToURL:atLocation:"
- "pdfHostViewController:updateCurrentPageIndex:"
- "pdfHostViewController:updatePageCount:"
- "pdfHostViewControllerDocumentDidRequestPassword:"
- "pdfHostViewControllerExtensionProcessDidCrash:"
- "pdfKitDocumentScrollView"
- "pdfKitIndexOfFirstCharacterOnPage:"
- "pdfKitIndexOfLastCharacterOnPage:"
- "pdfPage"
- "pdfPage:didAddAnnotation:"
- "pdfPage:didRemoveAnnotation:"
- "pdfPageView"
- "pdfPageWasRotated:"
- "pdfPointerCompletionHandler"
- "pdfResult"
- "pdfSafeAreaInsets"
- "pdfScannerResultAtPoint:"
- "pdfScannerResultAtPoint:onPageLayer:"
- "pdfSelectionUUID"
- "pdfView"
- "pdfView:didAddView:forPage:atIndex:"
- "pdfView:didRemoveView:forPage:atIndex:"
- "pdfView:didSetDocument:"
- "pdfView:overlayViewForPage:"
- "pdfView:willAddView:forPage:atIndex:"
- "pdfView:willDisplayOverlayView:forPage:"
- "pdfView:willEndDisplayingOverlayView:forPage:"
- "pdfView:willRemoveView:forPage:atIndex:"
- "pdfView:willSetDocument:"
- "pdfViewContentInset"
- "pdfViewDidChangePage:"
- "pdfViewDidChangeScale:"
- "pdfViewIsRotating"
- "pdfViewNeedsUpdate"
- "penStrokeCompletedForAnnotationController:"
- "performAction:"
- "performActionForSender:"
- "performBeep"
- "performOverlayAdaptorPageVisibilityTrueUpAfterSettingDocument"
- "performRequests:error:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:afterDelay:"
- "performSelector:withObject:afterDelay:inModes:"
- "performSelector:withObject:withObject:"
- "performSelectorOnMainThread:withObject:waitUntilDone:"
- "performTextSearchWithQueryString:usingOptions:resultAggregator:"
- "persistentDomainForName:"
- "pickerView:didSelectRow:inComponent:"
- "pickerView:numberOfRowsInComponent:"
- "pickerView:viewForRow:forComponent:reusingView:"
- "pinchGestureRecognizer"
- "placeAuxiliaryView:forAnnotationController:"
- "plainButtonConfiguration"
- "playEffect:"
- "point"
- "pointInside:withEvent:"
- "pointIsOnButton:"
- "pointIsOnButton:onPageLayer:"
- "pointSize"
- "pointSizeFromAppearanceTokens:"
- "pointerInteraction"
- "pointerInteraction:regionForRequest:defaultRegion:"
- "pointerInteraction:styleForRegion:"
- "pointerInteraction:willEnterRegion:animator:"
- "pointerInteraction:willExitRegion:animator:"
- "pointerIsOverAnnotation"
- "pointerRegionForLocation"
- "pointerRegionForLocation:"
- "pointerTrackingView"
- "popoverPresentationController"
- "popoverPresentationController:willRepositionPopoverToRect:inView:"
- "popoverPresentationControllerDidDismissPopover:"
- "popoverPresentingViewControllerForAnnotationController:"
- "populateAnnotationsFromDetectedAnnotationsOnPage:"
- "populateFormFieldsWithAutoFillSuggestion:completionHandler:"
- "popup"
- "popupController"
- "popupDictionary"
- "popupDrawsCloseWidget"
- "popupDrawsText"
- "popupTextView"
- "popupTextViewUndoManager"
- "positionFromPosition:inDirection:offset:"
- "positionFromPosition:offset:"
- "positionInternalViews:"
- "positionSketchOverlay:forAnnotationController:"
- "positionWithinRange:atCharacterOffset:"
- "positionWithinRange:farthestInDirection:"
- "positioningRectForCandidatePicker"
- "postAnnotationsChangedNotification"
- "postNotificationName:object:"
- "postNotificationName:object:userInfo:"
- "postPageDidChangeBoundsNotification"
- "postPageDidRotateNotification"
- "precomposedStringWithCanonicalMapping"
- "preferredInsertionOrder"
- "preferredPreviewParametersForTextLineRects:"
- "prefersIconOverlaySelection"
- "prefersOverlaySelection"
- "preloadDataOfPagesInRange:onQueue:completion:"
- "prepareForPopoverPresentation:"
- "prepareForReuse"
- "prepareOverlayAtIndex:"
- "prepareWithInvocationTarget:"
- "presentEditMenuWithConfiguration:"
- "presentFindNavigatorShowingReplace:"
- "presentInvalidPasswordAlertWithParentViewController:"
- "presentRedactionDiscoverabilityAlertWithOldValue:forAnnotationKey:"
- "presentSignaturesViewController"
- "presentViewController:animated:completion:"
- "presentationCountForPageViewController:"
- "presentationIndexForPageViewController:"
- "presentedViewController"
- "pressGestureRecognizer"
- "previewForCollectionView:contextMenuInteraction:"
- "previewForCollectionView:indexPath:"
- "previewRangeAtIndex:onPage:"
- "previewRotatePage:"
- "previewRotateShiftPages:"
- "previousPage"
- "printActivePageAnnotations"
- "printActivePageText"
- "printDictionaryKeyValues"
- "priority"
- "processIdentifier"
- "processInfo"
- "processName"
- "processRequest:progressHandler:completionHandler:"
- "proposedFormFieldBoundsNearestPoint:onPage:completionBlock:"
- "proposedFormRegionForPoint:existingFields:formSize:"
- "purgeAll"
- "purgePageLayout"
- "purpleColor"
- "pushDestination:"
- "q16@0:8"
- "q24@0:8@\"UIPageViewController\"16"
- "q24@0:8@16"
- "q24@0:8Q16"
- "q32@0:8@\"<NSObject><NSCopying>\"16@\"<NSObject><NSCopying>\"24"
- "q32@0:8@\"UIPageViewController\"16q24"
- "q32@0:8@\"UITextPosition\"16@\"UITextPosition\"24"
- "q32@0:8@\"UITextPosition\"16@\"UITextRange\"24"
- "q32@0:8@\"UITextPosition\"16q24"
- "q32@0:8@16@24"
- "q32@0:8@16q24"
- "q32@0:8{CGPoint=dd}16"
- "q40@0:8@\"UITextRange\"16@\"UITextRange\"24@\"<NSObject><NSCopying>\"32"
- "q40@0:8@16@24@32"
- "q48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "quad"
- "quadPointsForCharacterIndexes:onPageAtIndex:forAnnotationController:"
- "quadPointsPath"
- "quadrilateralPoints"
- "queue"
- "r^d16@0:8"
- "r^{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8Q16"
- "radiosInUnison"
- "raise:format:"
- "range"
- "rangeAtIndex:"
- "rangeAtIndex:onPage:"
- "rangeCount"
- "rangeOfCharacterFromSet:"
- "rangeOfCharacterFromSet:options:"
- "rangeOfComposedCharacterSequenceAtIndex:"
- "rangeOfString:options:range:"
- "readOnly"
- "recentGestureIsIndirectTouch"
- "recieveBackgroundImage:atBackgroundQuality:forPage:"
- "recievePDFTileSurface:"
- "recievedSnapshotViewRect:"
- "recognitionConfidence"
- "reconfigureItemsWithIdentifiers:"
- "rect"
- "rectIntersectsWithRedactionPath:"
- "rects"
- "redColor"
- "redo"
- "redo:"
- "redoActionName"
- "regionIdentifier"
- "regionRect"
- "regionWithRect:identifier:"
- "registerClass:forCellWithReuseIdentifier:"
- "registerDataRepresentationForTypeIdentifier:visibility:loadHandler:"
- "registerFileRepresentationForTypeIdentifier:fileOptions:visibility:loadHandler:"
- "registerForTraitChanges:withHandler:"
- "registerObject:visibility:"
- "registerUndoWithTarget:selector:object:"
- "release"
- "releaseCGPathArray"
- "releasePDFTileSurface:"
- "releaseSurface"
- "relinquishOverlayAtIndex:"
- "reloadData"
- "remoteObjectProxy"
- "removals"
- "removeAKAnnotationAdaptor"
- "removeAKOverlay"
- "removeAllActionsWithTarget:"
- "removeAllAppearanceStreams"
- "removeAllObjects"
- "removeAnnotation:"
- "removeAnnotation:atIndex:"
- "removeAnnotation:withUndo:"
- "removeAuxiliaryView:forAnnotationController:"
- "removeBezierPath:"
- "removeBookmark"
- "removeConstraint:"
- "removeControlForAnnotation:"
- "removeDictationResultPlaceholder:willInsertResult:"
- "removeFailureRequirement:"
- "removeFormFieldWithFieldName:"
- "removeFromDetectedAnnotations:"
- "removeFromPageView"
- "removeFromParent"
- "removeFromParentViewController"
- "removeFromSuperlayer"
- "removeFromSuperview"
- "removeGestureRecognizer:"
- "removeIndex:"
- "removeIndexes:"
- "removeInteraction:"
- "removeItemAtPath:error:"
- "removeItemAtURL:error:"
- "removeLastObject"
- "removeNoteForAnnotation:"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObjectsForKeys:"
- "removeObjectsInArray:"
- "removeObjectsInRange:"
- "removeObserver:"
- "removeObserver:forKeyPath:"
- "removeObserver:forKeyPath:context:"
- "removeObserver:name:object:"
- "removePageAtIndex:"
- "removePageLayerEffectForID:"
- "removePageViewForPageAtIndex:"
- "removePages:"
- "removeTextPlaceholder:"
- "removeValueForAnnotationKey:"
- "renderAnnotation:inContext:"
- "renderInContext:"
- "renderString:forRect:font:color:alignment:rotation:breaks:context:withAnnotation:"
- "renderingProperties"
- "renderingTransform"
- "reorderingHandlers"
- "replaceAllOccurrencesOfQueryString:usingOptions:withText:"
- "replaceAnnotation:withAnnotation:"
- "replaceFoundTextInRange:inDocument:withText:"
- "replaceItemAtURL:withItemAtURL:backupItemName:options:resultingItemURL:error:"
- "replaceObjectAtIndex:withObject:"
- "replaceOccurrencesOfString:withString:options:range:"
- "replaceRange:withAttributedText:"
- "replaceRange:withText:"
- "replaceTextWidgetWithString:"
- "requestPDFTileSurfaceForTarget:forPage:withRenderingProperties:atZoomFactor:frame:transform:tag:"
- "requestPermissionForController:toPerformActionFromSender:"
- "requestedOCR"
- "requireGestureRecognizerToFail:"
- "requirePasswordsIfNeededUsingPresentingViewController:completion:"
- "reset"
- "resetAccessibilityTree"
- "resetChangedAnnotations"
- "resetFormExcludingFields:"
- "resetFormFields:"
- "resetFormForFields:"
- "resetPageAnnotationChanges"
- "resetToDefaultToolMode"
- "resignFirstResponder"
- "resolvedColor:"
- "resolvedColorWithTraitCollection:"
- "respondsToSelector:"
- "restoreOriginalTileLayout"
- "resultIsPastDate"
- "results"
- "retain"
- "retainCount"
- "returnKeyType"
- "reverseObjectEnumerator"
- "revert"
- "right"
- "rightMostCharCenter"
- "rolloverCaption"
- "rootViewBounds"
- "rootViewController"
- "rootViewFrame"
- "rotateByAngle:"
- "rotateLeft:"
- "rotateRight:"
- "rotationGestureRecognizer"
- "row"
- "rowRange"
- "rowSizeForPage:"
- "rstate"
- "rtfData"
- "rtfdData"
- "rulerHostWantsSharedRuler"
- "rulerHostingStringFromPixels:"
- "rulerHostingView"
- "rvItemAtPoint:"
- "rvItemAtPoint:onPageLayer:"
- "rvItemWithPDFScannerResult:"
- "rvPresenter"
- "safeAreaInsets"
- "safeAreaLayoutGuide"
- "saveBitmapFiles"
- "saveOriginalTileLayout"
- "savedFirstResponder"
- "savedSafeAreaInsets"
- "savesAppearanceStream"
- "scale"
- "scaleCircumstance"
- "scaleFactor"
- "scaleFactorForSizeToFit"
- "scalePageLayerEffects:"
- "scaleProportional"
- "scaledFontForTextWidget"
- "scaling"
- "scan"
- "scanString:range:configuration:"
- "scannedAnnotationAtPoint:"
- "scheduledFindOnPage:"
- "scheduledPageSync"
- "scheme"
- "scrollRangeToVisible:inDocument:"
- "scrollRectToVisible:animated:"
- "scrollSelectionToVisible:"
- "scrollToItemAtIndexPath:atScrollPosition:animated:"
- "scrollView"
- "scrollViewDidChangeAdjustedContentInset:"
- "scrollViewDidEndDecelerating:"
- "scrollViewDidEndDragging:willDecelerate:"
- "scrollViewDidEndScrollingAnimation:"
- "scrollViewDidEndZooming:withView:atScale:"
- "scrollViewDidScroll:"
- "scrollViewDidScrollToTop:"
- "scrollViewDidZoom:"
- "scrollViewFrame"
- "scrollViewMinimumNumberOfTouches"
- "scrollViewObservation"
- "scrollViewSaysPageMayHaveChanged:"
- "scrollViewShouldScrollToTop:"
- "scrollViewWillBeginDecelerating:"
- "scrollViewWillBeginDragging:"
- "scrollViewWillBeginZooming:withView:"
- "scrollViewWillEndDragging:withVelocity:targetContentOffset:"
- "searchIndex"
- "searchLayer"
- "searchResults"
- "searchSelection"
- "searchString"
- "secondaryInit"
- "secondarySystemBackgroundColor"
- "secondarySystemFillColor"
- "secureTextEntry"
- "segmentWidth"
- "selectAll"
- "selectAll:"
- "selectAnnotation:byExtendingSelection:"
- "selectAnnotationsAtIndexes:byExtendingSelection:"
- "selectItemAtIndexPath:animated:scrollPosition:"
- "selectRowAtIndexPath:animated:scrollPosition:"
- "selected"
- "selectedPages"
- "selectedRange"
- "selectedTextRange"
- "selectedTextSearchDocument"
- "selectionAffinity"
- "selectionDidChange:"
- "selectionEffectLayers"
- "selectionForAll"
- "selectionForCharacterAtPoint:"
- "selectionForCodeRange:"
- "selectionForEntireDocument"
- "selectionForLineAtPoint:"
- "selectionForRange:"
- "selectionForRangeCommon:isCodeRange:"
- "selectionForRect:"
- "selectionForTableRect:"
- "selectionForWordAtPoint:"
- "selectionFromPage:atCharacterIndex:toPage:atCharacterIndex:"
- "selectionFromPage:atPoint:toPage:atPoint:"
- "selectionFromPage:atPoint:toPage:atPoint:type:"
- "selectionFromPage:atPoint:toPage:atPoint:type:withClampedRange:withCellRect:"
- "selectionFromPage:atPoint:toPage:atPoint:withGranularity:"
- "selectionFromPoint:toPoint:"
- "selectionFromPoint:toPoint:type:"
- "selectionFromPoint:toPoint:type:withClampedRange:withCellRect:"
- "selectionFromPointToBottom:type:"
- "selectionFromTopToPoint:type:"
- "selectionRect"
- "selectionRectsForRange:"
- "selectionWillChange:"
- "selections"
- "selectionsByLine"
- "self"
- "serviceViewControllerInterface"
- "setAKDidSetupRealPageModelController:"
- "setAccessibilityIdentifier:"
- "setAccessibilityLabel:"
- "setAccessibilityNode:"
- "setAction:"
- "setActionName:"
- "setActions:"
- "setActionsButton:"
- "setActive:"
- "setActiveAnnotation:"
- "setActiveMarkupStyle:"
- "setAdjustsFontSizeToFitWidth:"
- "setAffineTransform:"
- "setAkAnnotationEditingEnabled:"
- "setAkToolbarViewItemTintColor:"
- "setAkToolbarViewTintColor:"
- "setAlignment:"
- "setAlignmentMode:"
- "setAllowedTouchTypes:"
- "setAllowedWritingToolsResultOptions:"
- "setAllowsDarkAppearanceContent:"
- "setAllowsEdgeAntialiasing:"
- "setAllowsEditingTextAttributes:"
- "setAllowsGroupBlending:"
- "setAllowsGroupOpacity:"
- "setAllowsMarkupAnnotationEditing:"
- "setAllowsNativeRenderingOfHighlightableSelection:forAnnotationController:"
- "setAllowsNumberPadPopover:"
- "setAllowsPageReordering:"
- "setAllowsToggleToOff:"
- "setAllowsUndo:"
- "setAlpha:"
- "setAlternateFieldName:"
- "setAnchorPoint:"
- "setAnnotation:"
- "setAnnotationController:"
- "setAnnotationEditingEnabled:"
- "setAnnotationPageLayerEffectIsFlipped:"
- "setAnnotationText:"
- "setAppearance:forType:"
- "setAppearanceOverride:"
- "setAppearanceStyle:"
- "setApplicationData:withName:"
- "setArrowHeadStyle:"
- "setAttributedMarkedText:selectedRange:"
- "setAttributedText:"
- "setAttributes:"
- "setAttributes:range:"
- "setAuthor:"
- "setAutoFillTextContentType:"
- "setAutoScales:"
- "setAutocapitalizationType:"
- "setAutocorrectionType:"
- "setAutofillEntryType:"
- "setAutofillNewContextStart:"
- "setAutoresizesSubviews:"
- "setAutoresizingMask:"
- "setAxis:"
- "setBackgroundColor:"
- "setBackgroundImage:atBackgroundQuality:"
- "setBackgroundImage:forPage:"
- "setBarTintColor:"
- "setBaseWritingDirection:forRange:"
- "setBeginTime:"
- "setBlock:"
- "setBookmarked:"
- "setBookmarked:atPageIndex:"
- "setBookmarked:updateBookmarks:"
- "setBorder:"
- "setBorderCharacteristicsFromArray:"
- "setBorderColor:"
- "setBorderWidth:"
- "setBounces:"
- "setBounds:forBox:"
- "setBoundsWithUndo:"
- "setButtonPressed:"
- "setButtonSize:"
- "setButtonType:"
- "setButtonWidgetState:"
- "setButtonWidgetStateString:"
- "setByAddingObjectsFromArray:"
- "setCGPDFAnnotation:"
- "setCGPathArray:"
- "setCallbackQueue:"
- "setCanReorderItemHandler:"
- "setCandidateForFormDetection:"
- "setCandidateForOCR:"
- "setCaption:"
- "setCenter:"
- "setChildAnnotation:"
- "setChoices:"
- "setClientHints:"
- "setClipsToBounds:"
- "setCollectionViewLayout:"
- "setColor:"
- "setColorWidgetBackgrounds:"
- "setColors:"
- "setComb:"
- "setCompletionBlock:"
- "setCompositingFilter:"
- "setConfiguration:"
- "setConstant:"
- "setContainsLargeImage:"
- "setContainsText:"
- "setContentInset:"
- "setContentMode:"
- "setContentOffset:"
- "setContentOffset:animated:"
- "setContentScaleFactor:"
- "setContentSize:"
- "setContents:"
- "setContents:withUndo:"
- "setContentsFormat:"
- "setContentsGravity:"
- "setContentsLocked:"
- "setContentsOpaque:"
- "setContentsRect:"
- "setContentsScale:"
- "setControl:"
- "setControlType:"
- "setConversationContext:"
- "setCornerCurve:"
- "setCornerRadius:"
- "setCornerStyle:"
- "setCurrentPageIndex:"
- "setCurrentPageIndex:withNotification:"
- "setCurrentPageNumber:forPageCount:"
- "setCurrentSelection:"
- "setCurrentSelection:animate:"
- "setCurrentSelection:updateTextInput:"
- "setDarkModeBackgroundColor:"
- "setDarkModePageBackgroundColor:"
- "setDashPattern:"
- "setDashed:"
- "setDataSource:"
- "setDefaultStringValue:"
- "setDelegate:"
- "setDestination:"
- "setDetectedForm:"
- "setDetectedFormFieldsRecognitionConfidence:"
- "setDeviceColorSpace:"
- "setDictionaryRef:"
- "setDidForcePress:"
- "setDidPerformFormDetection:"
- "setDidPerformOCR:"
- "setDidReorderHandler:"
- "setDirectionalLockEnabled:"
- "setDisableActions:"
- "setDisplayBox:"
- "setDisplayDirection:"
- "setDisplayMode:"
- "setDisplaysAnnotations:"
- "setDisplaysAsBook:"
- "setDisplaysBookmarksForPages:"
- "setDisplaysMarkupAnnotations:"
- "setDisplaysPageBreaks:"
- "setDisplaysRTL:"
- "setDistribution:"
- "setDocument:"
- "setDocument:waitDuration:"
- "setDocument:withInitialPageIndex:"
- "setDocumentAnalysisEnabled:"
- "setDocumentAttributes:"
- "setDocumentData"
- "setDocumentData:"
- "setDocumentData:withScrollView:"
- "setDocumentHasBurnInAnnotations:"
- "setDocumentMargins:"
- "setDownCaption:"
- "setDragDelegate:"
- "setDragInteractionEnabled:"
- "setDrawing:"
- "setDrawsAsynchronously:"
- "setDropDelegate:"
- "setDuration:"
- "setEdgeAntialiasingMask:"
- "setEditsDisableAppearanceOverride:"
- "setEffectLayerOCRContent:"
- "setEnableBackgroundImages:"
- "setEnableDataDetectors:"
- "setEnablePageShadows:"
- "setEnableRoundPageCorners:"
- "setEnableTileUpdates:"
- "setEnabled:"
- "setEnablesReturnKeyAutomatically:"
- "setEndLineStyle:"
- "setEndPoint:"
- "setEstimatedItemSize:"
- "setExcludingAKAnnotationRenderingForThisThread:"
- "setExtensionViewController:"
- "setExtraContentStream:steamDocument:"
- "setFieldName:"
- "setFieldType:"
- "setFields:"
- "setFieldsIncludedAreCleared:"
- "setFill"
- "setFillColor:"
- "setFillMode:"
- "setFindInteractionEnabled:"
- "setFont:"
- "setFontColor:"
- "setFontSize:"
- "setForExport:"
- "setForceBreaks:"
- "setForcesTopAlignment:"
- "setForegroundColor:"
- "setForegroundColorHDR:"
- "setForegroundColorSDR:"
- "setFormContentType:"
- "setFormData:"
- "setFormDetectionEnabled:"
- "setFormFillingEnabled:"
- "setFormFillingUpdatesAnnotationOnEveryTextChange:"
- "setFrame:"
- "setFromValue:"
- "setGeometryFlipped:"
- "setGreekingThreshold:"
- "setGutterWidth:"
- "setHasHighLatencyDataProvider:"
- "setHasPageWithApplicationData:"
- "setHasSelection"
- "setHasSelection:"
- "setHidden:"
- "setHighlightRef:"
- "setHighlighted:"
- "setHighlightedSelections:"
- "setHorizontalCornerRadius:"
- "setHostViewController:"
- "setIconConfigurationHandler:"
- "setIconScale:"
- "setIconType:"
- "setIdentifier:"
- "setImage:"
- "setImage:forState:"
- "setImageView:"
- "setInFormFillingMode:"
- "setInMarkupMode:"
- "setIndex:"
- "setInlinePredictionType:"
- "setInputAccessoryView:"
- "setInputDelegate:"
- "setInputView:"
- "setInteriorColor:"
- "setInterpolationQuality:"
- "setInvisible:"
- "setIsDetectedCheckbox:"
- "setIsDetectedSignature:"
- "setIsEditingText:"
- "setIsEndingRect:"
- "setIsFormField:"
- "setIsFullyConstructed:"
- "setIsHandlingEditDetected:"
- "setIsHighlighted:"
- "setIsOpaque:"
- "setIsOpen:"
- "setIsSelected:"
- "setIsSignatureWidget:"
- "setIsStartingRect:"
- "setIsTextSelection"
- "setIsTransparent:"
- "setIsUsingPDFExtensionView:"
- "setItemProviders:"
- "setItems:"
- "setKeyPath:"
- "setKeyboardAppearance:"
- "setKeyboardType:"
- "setKind:"
- "setLabel:"
- "setLabelText:"
- "setLayoutMargins:"
- "setLayoutMarginsRelativeArrangement:"
- "setLayoutMode:"
- "setLeadingBarButtonGroups:"
- "setLineBreakMode:"
- "setLineDash:count:phase:"
- "setLineFragmentPadding:"
- "setLineWidth:"
- "setLineWidthThreshold:"
- "setListChoice:"
- "setLocalObject:"
- "setLocationOfFirstTouch:"
- "setLocked:"
- "setMagnificationFilter:"
- "setMarkedText:selectedRange:"
- "setMarkedTextStyle:"
- "setMarkupStyle:"
- "setMarkupStyle:forAnnotation:"
- "setMarkupStyle:forSelection:clearSelection:"
- "setMarkupType:"
- "setMasksToBounds:"
- "setMathExpressionCompletionType:"
- "setMaxConcurrentOperationCount:"
- "setMaxScaleFactor:"
- "setMaximumLength:"
- "setMaximumNumberOfCharacters:"
- "setMaximumZoomScale"
- "setMaximumZoomScale:"
- "setMenu:"
- "setMenuElementRepresentation:"
- "setMidPoint:"
- "setMinScaleFactor:"
- "setMinScaleFactor:withMaxScaleFactor:"
- "setMinificationFilter:"
- "setMinimumLineSpacing:"
- "setMinimumNumberOfTouches:"
- "setMinimumZoomScale"
- "setMinimumZoomScale:"
- "setModalPresentationStyle:"
- "setModificationDate:"
- "setMouseDownAction:"
- "setMouseUpAction:"
- "setMultiline:"
- "setName:"
- "setNativeRotationDrawingEnabledForThisThread:"
- "setNeedsDisplay"
- "setNeedsDisplayInRect:"
- "setNeedsLayout"
- "setNeedsTilesUpdate"
- "setNeedsUpdate"
- "setNewPageVisibilityDelegate:withOldDelegate:"
- "setNumberOfSegments:"
- "setNumberOfTapsRequired:"
- "setObject:"
- "setObject:atIndexedSubscript:"
- "setObject:forKey:"
- "setObject:forKey:cost:"
- "setObject:forKeyedSubscript:"
- "setObservedObject:"
- "setOffset:"
- "setOpaque:"
- "setOpen:"
- "setOriginalExifOrientation:"
- "setOriginalModelBaseScaleFactor:"
- "setOutlineRoot:"
- "setOverlayViewInstalled:"
- "setPDFAKControllerDelegate:"
- "setPDFAnnotationDictionary:"
- "setPDFAnnotationUUID:"
- "setPDFDocumentAppendModeActiveForThisThread:"
- "setPDFPage:"
- "setPDFView:"
- "setPage:"
- "setPageBreakMargins:"
- "setPageChangeDelegate:"
- "setPageColor:"
- "setPageFrame:"
- "setPageIndex:"
- "setPageOverlayViewProvider:"
- "setPageRef:"
- "setParent:"
- "setParentAnnotation:"
- "setPasswordDelegate:"
- "setPasswordRules:"
- "setPdfDocument:"
- "setPdfPageView:"
- "setPdfView:"
- "setPermittedArrowDirections:"
- "setPlaceholder:"
- "setPoint:"
- "setPointerIsOverAnnotation:"
- "setPopup:"
- "setPopupDrawsCloseWidget:"
- "setPopupDrawsText:"
- "setPopupInternal:scanPage:"
- "setPosition:"
- "setPreferredContentSize:"
- "setPreferredSymbolConfigurationForImage:"
- "setPrefersIconOverlaySelection:"
- "setPrefersOverlaySelection:"
- "setPresentationContext:"
- "setPresentingViewController:"
- "setPriority:"
- "setQuadPointsForIndexSet:withUndo:"
- "setQuadrilateralPoints:"
- "setQualityOfService:"
- "setRadiosInUnison:"
- "setRange:"
- "setReadOnly:"
- "setReadOnlyAnnotation:"
- "setRecognitionLevel:"
- "setRect:"
- "setRectangle:"
- "setRemovedOnCompletion:"
- "setRenderingProperties:"
- "setRepeatCount:"
- "setRepresentedObject:"
- "setRequestInterruptionBlock:"
- "setReturnKeyType:"
- "setRightBarButtonItem:"
- "setRolloverCaption:"
- "setRootViewFrame:"
- "setRotation:"
- "setRowHeight:"
- "setRulerHostingDelegate:"
- "setSavesAppearanceStream:"
- "setScale:"
- "setScaleFactor:"
- "setScaleFactor:anchorPoint:"
- "setScrollDirection:"
- "setScrollEnabled:"
- "setScrollViewScrollEnabled:"
- "setSearchSelections:"
- "setSectionInset:"
- "setSecureTextEntry:"
- "setSegmentWidth:"
- "setSelected:"
- "setSelectedRange:"
- "setSelectedTextRange:"
- "setSelection:"
- "setSelectionAffinity:"
- "setSelections:"
- "setSelector:"
- "setSeparatorInset:"
- "setSet:"
- "setShadowColor:"
- "setShadowOffset:"
- "setShadowOpacity:"
- "setShadowPath:"
- "setShadowRadius:"
- "setShareButtonHidden:"
- "setShouldAntiAlias:"
- "setShouldBurnIn:"
- "setShouldDisplay:"
- "setShouldHideAnnotationsForThisThread:"
- "setShouldHideInteractiveBackgroundColor:"
- "setShouldNotRotate:"
- "setShouldNotZoom:"
- "setShouldPrint:"
- "setShouldReportAnalytics:"
- "setShouldToggleNoView:"
- "setShouldUsePlaceholderText:"
- "setShowsAnnotations:"
- "setShowsHorizontalScrollIndicator:"
- "setShowsMenuAsPrimaryAction:"
- "setShowsScrollIndicators:"
- "setShowsVerticalScrollIndicator:"
- "setSignatureAnnotationForRendering:"
- "setSmartDashesType:"
- "setSmartInsertDeleteType:"
- "setSmartQuotesType:"
- "setSourceRect:"
- "setSourceView:"
- "setSpacing:"
- "setSpellCheckingType:"
- "setSpotlightSuggestionsEnabled:"
- "setStampName:"
- "setStartCellIndex:"
- "setStartLineStyle:"
- "setStartPoint:"
- "setState:onButtonWidgetAnnotation:"
- "setString:"
- "setStringValue:"
- "setStringValue:forFieldNamed:postFormChangeNotification:"
- "setStringValue:onChoiceWidgetAnnotation:withTableView:"
- "setStringValue:onChoiceWidgetAnnotation:withTextField:"
- "setStringValue:onTextAnnotation:"
- "setStringValue:onTextWidgetAnnotation:"
- "setStringValue:onTextWidgetAnnotation:withTextView:"
- "setStrokeColor:"
- "setStrokeWidth:"
- "setStyle:"
- "setSuggestedLineHeight:"
- "setSupportsAdaptiveImageGlyph:"
- "setTable:"
- "setTag:"
- "setTarget:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setTextContainerInset:"
- "setTextContentType:"
- "setTextInput:"
- "setTextIsClipped:"
- "setTextIsFixedHeight:"
- "setTextIsFixedWidth:"
- "setTextRects:"
- "setTextSelectionEnabled:"
- "setTextSelectionPoints"
- "setTextSelectionPoints:right:"
- "setThumbnailContextMenuDelegate:"
- "setThumbnailDataSourceDelegate:"
- "setThumbnailHeight:"
- "setThumbnailSize:"
- "setThumbnailWidth:"
- "setTileSurfaceType:"
- "setTintColor:"
- "setToValue:"
- "setTokenizer:"
- "setTouchesDidHavePressure:"
- "setTrailingBarButtonGroups:"
- "setTraitCollection:"
- "setTransform:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setType:"
- "setTypingAttributes:"
- "setURL:"
- "setUseIOSurfaceForTiles"
- "setUseIOSurfaceForTiles:"
- "setUserInteractionEnabled:"
- "setUserName:"
- "setUsesFormFieldDetection:"
- "setValue:forKey:"
- "setValue:forKeyPath:"
- "setValues:"
- "setVerticalCornerRadius:"
- "setView:"
- "setViewControllers:direction:animated:completion:"
- "setViewProvider:"
- "setVisibilityDelegateIndex:"
- "setVisiblePath:"
- "setWidgetControlType:"
- "setWidgetDefaultStringValue:"
- "setWidgetFieldType:"
- "setWidgetOnStateString:"
- "setWidgetStringValue:"
- "setWithArray:"
- "setWriteDefaultValue:"
- "setWritingToolsBehavior:"
- "setZPosition:"
- "setZoom:"
- "setZoomScale:"
- "setZoomScale:animated:"
- "set_wantsFormFieldDetection:"
- "settingsForPrivateStyle:"
- "setup"
- "setupAKAnnotationAdaptorIfNecessary"
- "setupAKDocumentAdaptorIfNecessaryWithView:"
- "setupAKPageAdaptorIfNecessary"
- "setupDocumentViewSize"
- "setupDocumentViewSize:"
- "setupDrawColor:forContext:"
- "setupGestureRecognizersForView:"
- "setupNotifications"
- "setupPDFView"
- "setupSubviews"
- "sharedApplication"
- "sharedInstance"
- "sharedMenuController"
- "sharedPool"
- "shouldAcceptTouch:ofGestureRecognizer:"
- "shouldAddTabControlsToTextEditorForAnnotation:forAnnotationController:"
- "shouldAntiAlias"
- "shouldBurnIn"
- "shouldChangeTextInRange:replacementText:"
- "shouldComb"
- "shouldDisplay"
- "shouldDisplayActionButtonForPage:"
- "shouldExport"
- "shouldHideAnnotationsForThisThread"
- "shouldNotRotate"
- "shouldNotZoom"
- "shouldPlaceFormElementAtPoint:onOverlayAtPageIndex:forAnnotationController:"
- "shouldPlaceProposedFormElementAtRect:onOverlayAtPageIndex:forAnnotationController:"
- "shouldPrint"
- "shouldReadAKInkAnnotations"
- "shouldRegisterUndo"
- "shouldReplaceFoundTextInRange:inDocument:withText:"
- "shouldReportAnalytics"
- "shouldRotateContent"
- "shouldToggleNoView"
- "shouldUsePlaceholderText"
- "shouldVerticallyFlipOverlayViews"
- "showActiveMenus"
- "showMarkupMenu:"
- "showMarkupStyleMenuForMarkupAnnotation"
- "showMenuForMarkupAnnotation:"
- "showMenuFromView:rect:"
- "showSelectionRect"
- "showSelectionRect:"
- "showTextSelectionMenu"
- "showTextSelectionMenu:selectionRect:"
- "showsAnnotations"
- "showsHorizontalScrollIndicator"
- "showsScrollIndicators"
- "showsVerticalScrollIndicator"
- "sideLength"
- "signatureAnnotationForRendering"
- "signatureLayer"
- "signaturesController"
- "signaturesController:didSelectSignatureWithAnnotation:"
- "singlePageContinuousSize"
- "size"
- "sizeToFit"
- "sizeWithAttributes:"
- "smallColorPotForColor:withAccessibilityLabel:"
- "smallStrikeOutPot"
- "smallSystemFontSize"
- "smallUnderlinePot"
- "smartDashesType"
- "smartInsertDeleteType"
- "smartInvertCAColorMatrix"
- "smartInvertCGMatrixFilter"
- "smartQuotesType"
- "snapshot"
- "snapshotCompletion"
- "snapshotViewRect"
- "snapshotViewRect:forWidth:afterScreenUpdates:"
- "snapshotViewRect:snapshotWidth:afterScreenUpdates:withResult:"
- "solariumEnabled"
- "sortUsingComparator:"
- "sortUsingFunction:context:"
- "sortWithOptions:usingComparator:"
- "sortedArrayUsingComparator:"
- "sortedArrayWithOptions:usingComparator:"
- "sourceDictionary"
- "spanBoundsForPage:atPoint:"
- "spellCheckingType"
- "srcDictionary"
- "stampName"
- "standardDocumentAttributes"
- "standardUserDefaults"
- "standardizedURL"
- "start"
- "startAccessingSecurityScopedResource"
- "startCellIndex"
- "startEditingTextWidgetAnnotation:"
- "startLineStyle"
- "stopAccessingSecurityScopedResource"
- "stopScan:"
- "string"
- "stringByAppendingFormat:"
- "stringByAppendingPathComponent:"
- "stringByAppendingString:"
- "stringByApplyingTransform:reverse:"
- "stringByDeletingLastPathComponent"
- "stringByRemovingPercentEncoding"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringByTrimmingCharactersInSet:"
- "stringByTrimmingTrailingCharactersInSet:forString:"
- "stringCompareOptions"
- "stringValue"
- "stringValueForFieldNamed:"
- "stringWithCString:encoding:"
- "stringWithCapacity:"
- "stringWithCharacters:length:"
- "stringWithFormat:"
- "stringWithString:"
- "stringWithUTF8String:"
- "stroke"
- "strokeOval:color:context:"
- "strokeRect:color:context:"
- "strongToStrongObjectsMapTable"
- "style"
- "styleMask"
- "styleWithShape:constrainedAxes:"
- "subarrayWithRange:"
- "substringFromIndex:"
- "substringToIndex:"
- "substringWithRange:"
- "subviews"
- "suggestedLineHeight"
- "superclass"
- "superview"
- "supportedUTTypes"
- "supportsAdaptiveImageGlyph"
- "supportsFormFill"
- "supportsImageDescriptionEditing"
- "supportsTextReplacement"
- "suppressAppearanceStreamText"
- "surfaceType"
- "surfaces"
- "surfacesLock"
- "suspiciousURL"
- "syncPageIndexToScrollView"
- "systemBackgroundColor"
- "systemBlueColor"
- "systemFontOfSize:"
- "systemFontSize"
- "systemGreenColor"
- "systemImageNamed:"
- "systemImageNamed:withConfiguration:"
- "systemPointerStyle"
- "systemRedColor"
- "systemUptime"
- "table"
- "tableCellSelection"
- "tableCellSelectionRect"
- "tableSelectionFromPoint:toPoint:"
- "tableView:cellForRowAtIndexPath:"
- "tableView:didSelectRowAtIndexPath:"
- "tableView:numberOfRowsInSection:"
- "tag"
- "takeBackgroundColorFrom:"
- "takePasswordFrom:"
- "tapGestureRecognizer"
- "target"
- "targetBackingScaleFactor"
- "teardown"
- "teardownGestureRecognizersForView:"
- "temporaryDirectory"
- "tertiarySystemBackgroundColor"
- "text"
- "textContainer"
- "textContentType"
- "textDidChange:"
- "textEditorController"
- "textExtractionQueue"
- "textFields"
- "textFromOCR"
- "textInRange:"
- "textInputView"
- "textInset"
- "textInteractionsForSet:"
- "textIsClipped"
- "textIsFixedHeight"
- "textIsFixedWidth"
- "textLabel"
- "textMarkupString"
- "textPositionFromPage:atCharacterIndex:offset:"
- "textRangeFromPosition:toPosition:"
- "textRangeFromSelection:"
- "textSelectionEnabled"
- "textSelectionMenu"
- "textStylingAtPosition:inDirection:"
- "textView"
- "textView:didBeginFormattingWithViewController:"
- "textView:didEndFormattingWithViewController:"
- "textView:doCommandBySelector:"
- "textView:editMenuForTextInRange:suggestedActions:"
- "textView:editMenuForTextInRanges:suggestedActions:"
- "textView:insertInputSuggestion:"
- "textView:menuConfigurationForTextItem:defaultMenu:"
- "textView:primaryActionForTextItem:defaultAction:"
- "textView:shouldChangeTextInRange:replacementText:"
- "textView:shouldChangeTextInRanges:replacementText:"
- "textView:shouldInteractWithTextAttachment:inRange:"
- "textView:shouldInteractWithTextAttachment:inRange:interaction:"
- "textView:shouldInteractWithURL:inRange:"
- "textView:shouldInteractWithURL:inRange:interaction:"
- "textView:textItemMenuWillDisplayForTextItem:animator:"
- "textView:textItemMenuWillEndForTextItem:animator:"
- "textView:willBeginFormattingWithViewController:"
- "textView:willDismissEditMenuWithAnimator:"
- "textView:willEndFormattingWithViewController:"
- "textView:willPresentEditMenuWithAnimator:"
- "textView:writingToolsIgnoredRangesInEnclosingRange:"
- "textViewDidBeginEditing:"
- "textViewDidChange:"
- "textViewDidChangeSelection:"
- "textViewDidEndEditing:"
- "textViewShouldBeginEditing:"
- "textViewShouldEndEditing:"
- "textViewWritingToolsDidEnd:"
- "textViewWritingToolsWillBegin:"
- "textWillChange:"
- "threadDictionary"
- "thumbnailContextMenuDelegate"
- "thumbnailDataSourceDelegate"
- "thumbnailIconsView"
- "thumbnailOfSize:forBox:"
- "thumbnailOfSize:forBox:withBookmark:"
- "thumbnailOfSize:forBox:withBookmark:withAnnotations:"
- "thumbnailSize"
- "thumbnailSizeForPage:"
- "thumbnailSizeForPage:displayBox:"
- "thumbnailSizeForPage:displayBox:thumbnailView:"
- "tileContentsScale"
- "tileDrawingComplete:"
- "tileFrame"
- "tileId"
- "tilePadding"
- "tileSize"
- "tileSurfacePadding"
- "tileSurfaceSize"
- "tileSurfaceType"
- "tilesSyncTimer"
- "timeInterval"
- "timeIntervalSince1970"
- "timeIntervalSinceDate:"
- "timeIntervalSinceNow"
- "timeIntervalSinceReferenceDate"
- "timer"
- "timerWithTimeInterval:target:selector:userInfo:repeats:"
- "tintColor"
- "title"
- "toPage"
- "tokenizeAppearanceString:"
- "tokenizer"
- "toolController"
- "toolTip"
- "toolTipNoLabel"
- "toolbarButtonItemOfType:"
- "toolbarView"
- "toolbarViewController"
- "top"
- "topAnchor"
- "topLeft"
- "topLevelView"
- "topRight"
- "topView"
- "touchesBegan:withEvent:"
- "touchesDidHavePressure"
- "touchesMoved:withEvent:"
- "trailingAnchor"
- "traitCollectionWithUserInterfaceStyle:"
- "transformContext:forBox:"
- "transformForBox:"
- "twoUpContinousSize"
- "type"
- "typeForGestureRecognizer:"
- "typeWithIdentifier:"
- "uiControl"
- "undo"
- "undo:"
- "undoActionName"
- "undoManager"
- "undoManagerForAnnotationController:"
- "undoNestedGroup"
- "uninstallDrawingGestureRecognizer:forPageAtIndex:forAnnotationController:"
- "unlock"
- "unlockWithOptions:seed:"
- "unlockWithPassword"
- "unlockWithPassword:"
- "unmarkText"
- "unobscuredContentRect"
- "unsignedIntegerValue"
- "unsignedLongValue"
- "update"
- "updateAccessibilityTags"
- "updateActivePageIndex:"
- "updateAnnotation:"
- "updateAnnotationEffect"
- "updateAsPageIndex:forDocument:"
- "updateAspectConstraintWithSize:"
- "updateAutoScaleFactor"
- "updateBookmark"
- "updateBookmarksInPDFDocument"
- "updateCacheForPage:withImage:"
- "updateColor:"
- "updateCornerBorderStyle"
- "updateCurrentPageIndex"
- "updateCurrentPageIndex:"
- "updateDocumentIsLocked"
- "updateDocumentIsLocked:"
- "updateDocumentViewSize"
- "updateDrawingGestureRecognizer:forPageAtIndex:withPriority:forAnnotationController:"
- "updateEffect"
- "updateFloatingCursorAtPoint:"
- "updateForTextAttributeChange"
- "updateFormData"
- "updateGestureRecognizerDependencies"
- "updateIconsImages"
- "updateImageForCell:atIndexPath:"
- "updateImageForCell:indexPath:page:"
- "updateLayout"
- "updateNodeBoundingBoxes"
- "updateNotificationsForDocument"
- "updateOverlay"
- "updatePDFViewLayout"
- "updatePDFViewLayout:scrollViewFrame:safeAreaInsets:zoomScale:"
- "updatePDFViewLayout:scrollViewFrame:zoomScale:"
- "updatePageCount"
- "updatePageCount:"
- "updatePageLayerEffectForID:"
- "updatePageLayerEffects"
- "updateScrollViews"
- "updateSelectionLayersWithFocusState:"
- "updateTextSelectionGraphics"
- "updateUserNameFromAKControllerforAnnotation:"
- "updateVisibility"
- "updateVisibleLayers"
- "urlString"
- "urlificationRange"
- "useIOSurfaceForTiles"
- "useLegacyImageHandling"
- "usePageViewController:withViewOptions:"
- "userDidEnterPassword:forPasswordView:"
- "userDidEnterPassword:forPasswordViewController:"
- "userInfo"
- "userInterfaceIdiom"
- "userInterfaceStyle"
- "userName"
- "uuid"
- "v120@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48{UIEdgeInsets=dddd}80d112"
- "v128@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48{CGRect={CGPoint=dd}{CGSize=dd}}80d112q120"
- "v132@0:8@16@24@32d40{CGRect={CGPoint=dd}{CGSize=dd}}48{CGAffineTransform=dddddd}80i128"
- "v16@0:8"
- "v16@?0@\"NSUUID\"8"
- "v20@0:8B16"
- "v20@0:8c16"
- "v20@0:8i16"
- "v24@0:8@\"<UIEditMenuInteractionAnimating>\"16"
- "v24@0:8@\"<UITextInputDelegate>\"16"
- "v24@0:8@\"AKAnnotation\"16"
- "v24@0:8@\"AKController\"16"
- "v24@0:8@\"CALayer\"16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSAttributedString\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSNotification\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"NSTextStorage\"16"
- "v24@0:8@\"NSUUID\"16"
- "v24@0:8@\"PDFPageLayerEffect\"16"
- "v24@0:8@\"PDFTileSurface\"16"
- "v24@0:8@\"PDFView\"16"
- "v24@0:8@\"UICollectionView\"16"
- "v24@0:8@\"UIColor\"16"
- "v24@0:8@\"UIConversationContext\"16"
- "v24@0:8@\"UIInputSuggestion\"16"
- "v24@0:8@\"UIScrollView\"16"
- "v24@0:8@\"UITextInputPasswordRules\"16"
- "v24@0:8@\"UITextInteraction\"16"
- "v24@0:8@\"UITextPlaceholder\"16"
- "v24@0:8@\"UITextRange\"16"
- "v24@0:8@\"UITextView\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"CALayer\">16"
- "v24@0:8B16B20"
- "v24@0:8Q16"
- "v24@0:8^^{CGPath}16"
- "v24@0:8^{CGColorSpace=}16"
- "v24@0:8^{CGContext=}16"
- "v24@0:8^{CGDataProvider=}16"
- "v24@0:8^{CGDisplayList=}16"
- "v24@0:8^{CGPDFAnnotation=}16"
- "v24@0:8^{CGPDFArray=}16"
- "v24@0:8^{CGPDFDictionary=}16"
- "v24@0:8^{CGPDFDocument=}16"
- "v24@0:8^{CGPDFPageLayoutTable=}16"
- "v24@0:8^{CGPDFScanner=}16"
- "v24@0:8^{__CFArray=}16"
- "v24@0:8^{__CFDictionary=}16"
- "v24@0:8^{__DDHighlight=}16"
- "v24@0:8d16"
- "v24@0:8i16B20"
- "v24@0:8q16"
- "v28@0:8@\"AKController\"16B24"
- "v28@0:8@\"UIScrollView\"16B24"
- "v28@0:8@16B24"
- "v28@0:8@16i24"
- "v28@0:8B16@\"AKController\"20"
- "v28@0:8B16@20"
- "v28@0:8B16Q20"
- "v28@0:8Q16B24"
- "v28@0:8Q16i24"
- "v28@0:8^{CGPDFDictionary=}16i24"
- "v28@0:8^{CGPDFForm=}16i24"
- "v28@0:8d16B24"
- "v28@0:8i16@20"
- "v32@0:8@\"AKSignaturesController\"16@\"AKSignatureAnnotation\"24"
- "v32@0:8@\"CALayer\"16^{CGContext=}24"
- "v32@0:8@\"NSAdaptiveImageGlyph\"16@\"UITextRange\"24"
- "v32@0:8@\"NSArray\"16@\"PDFDocument\"24"
- "v32@0:8@\"NSArray\"16@\"PDFPage\"24"
- "v32@0:8@\"NSString\"16@\"UIDocumentPasswordView\"24"
- "v32@0:8@\"PDFPage\"16Q24"
- "v32@0:8@\"UICollectionView\"16@\"<UICollectionViewDropCoordinator>\"24"
- "v32@0:8@\"UICollectionView\"16@\"<UIDragSession>\"24"
- "v32@0:8@\"UICollectionView\"16@\"<UIDropSession>\"24"
- "v32@0:8@\"UICollectionView\"16@\"NSIndexPath\"24"
- "v32@0:8@\"UIFindInteraction\"16@\"UIFindSession\"24"
- "v32@0:8@\"UIPageViewController\"16@\"NSArray\"24"
- "v32@0:8@\"UIScrollView\"16@\"UIView\"24"
- "v32@0:8@\"UITextField\"16@\"UIDocumentPasswordView\"24"
- "v32@0:8@\"UITextRange\"16@\"<NSObject><NSCopying>\"24"
- "v32@0:8@\"UITextRange\"16@\"NSAttributedString\"24"
- "v32@0:8@\"UITextRange\"16@\"NSString\"24"
- "v32@0:8@\"UITextView\"16@\"<UIEditMenuInteractionAnimating>\"24"
- "v32@0:8@\"UITextView\"16@\"UIInputSuggestion\"24"
- "v32@0:8@\"UITextView\"16@\"UITextFormattingViewController\"24"
- "v32@0:8@\"UIView\"16@\"AKController\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16B24B28"
- "v32@0:8@16Q24"
- "v32@0:8@16^{CGContext=}24"
- "v32@0:8@16^{__CFDictionary=}24"
- "v32@0:8@16d24"
- "v32@0:8@16q24"
- "v32@0:8@?16@24"
- "v32@0:8Q16@24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16Q24"
- "v32@0:8Q16d24"
- "v32@0:8^{CGContext=}16@24"
- "v32@0:8^{CGContext=}16q24"
- "v32@0:8^{CGDisplayList=}16@24"
- "v32@0:8^{CGPDFSelection=}16@24"
- "v32@0:8^{CGPDFStream=}16^{CGPDFDocument=}24"
- "v32@0:8^{__CFString=}16^{__CFDictionary=}24"
- "v32@0:8d16@24"
- "v32@0:8d16d24"
- "v32@0:8q16@\"UITextRange\"24"
- "v32@0:8q16@24"
- "v32@0:8q16^{CGContext=}24"
- "v32@0:8r^{CGRect={CGPoint=dd}{CGSize=dd}}16q24"
- "v32@0:8{CGPoint=dd}16"
- "v32@0:8{CGSize=dd}16"
- "v32@0:8{_NSRange=QQ}16"
- "v32@?0@\"<NSCopying>\"8@\"UIViewController\"16@\"NSError\"24"
- "v32@?0@\"NSValue\"8@\"CALayer\"16^B24"
- "v32@?0@\"UIView\"8Q16^B24"
- "v36@0:8@\"UIImage\"16i24@\"PDFPage\"28"
- "v36@0:8@16@24B32"
- "v36@0:8@16^{CGContext=}24i32"
- "v36@0:8@16i24@28"
- "v36@0:8@16q24B32"
- "v36@0:8Q16@24B32"
- "v36@0:8i16@20Q28"
- "v36@0:8q16^{CGContext=}24B32"
- "v40@0:8@\"AKController\"16@\"AKAnnotation\"24@\"AKPageModelController\"32"
- "v40@0:8@\"AKController\"16@\"AKAnnotation\"24^@32"
- "v40@0:8@\"NSAttributedString\"16{_NSRange=QQ}24"
- "v40@0:8@\"NSString\"16@\"NSArray\"24q32"
- "v40@0:8@\"NSString\"16@\"UITextSearchOptions\"24@\"<UITextSearchAggregator>\"32"
- "v40@0:8@\"NSString\"16@\"UITextSearchOptions\"24@\"NSString\"32"
- "v40@0:8@\"NSString\"16{_NSRange=QQ}24"
- "v40@0:8@\"PDFView\"16@\"UIView\"24@\"PDFPage\"32"
- "v40@0:8@\"UIAutoFillTextSuggestion\"16@\"AKController\"24@?<v@?@\"NSSet\">32"
- "v40@0:8@\"UICollectionView\"16@\"UICollectionViewCell\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UICollectionView\"16@\"UICollectionViewFocusUpdateContext\"24@\"UIFocusAnimationCoordinator\"32"
- "v40@0:8@\"UICollectionView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionAnimating>\"32"
- "v40@0:8@\"UICollectionView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionCommitAnimating>\"32"
- "v40@0:8@\"UIContextMenuInteraction\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionAnimating>\"32"
- "v40@0:8@\"UIContextMenuInteraction\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionCommitAnimating>\"32"
- "v40@0:8@\"UIEditMenuInteraction\"16@\"UIEditMenuConfiguration\"24@\"<UIEditMenuInteractionAnimating>\"32"
- "v40@0:8@\"UIGestureRecognizer\"16Q24@\"AKController\"32"
- "v40@0:8@\"UIPageViewController\"16B24@\"NSArray\"28B36"
- "v40@0:8@\"UIPointerInteraction\"16@\"UIPointerRegion\"24@\"<UIPointerInteractionAnimating>\"32"
- "v40@0:8@\"UIScrollView\"16@\"UIView\"24d32"
- "v40@0:8@\"UITextRange\"16@\"<NSObject><NSCopying>\"24@\"NSString\"32"
- "v40@0:8@\"UITextRange\"16@\"<NSObject><NSCopying>\"24q32"
- "v40@0:8@\"UITextView\"16@\"UITextItem\"24@\"<UIContextMenuInteractionAnimating>\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@24Q32"
- "v40@0:8@16@24^@32"
- "v40@0:8@16@24d32"
- "v40@0:8@16@24q32"
- "v40@0:8@16B24@28B36"
- "v40@0:8@16N^{CGRect={CGPoint=dd}{CGSize=dd}}24N^@32"
- "v40@0:8@16Q24@32"
- "v40@0:8@16Q24@?32"
- "v40@0:8@16^{__CFString=}24^{__CFDictionary=}32"
- "v40@0:8@16i24B28^{CGContext=}32"
- "v40@0:8@16q24q32"
- "v40@0:8@16{CGPoint=dd}24"
- "v40@0:8@16{_NSRange=QQ}24"
- "v40@0:8^{CGPDFArray=}16@24@32"
- "v40@0:8^{CGPDFDictionary=}16@24@32"
- "v40@0:8^{CGPDFForm=}16q24^{CGContext=}32"
- "v40@0:8d16{CGPoint=dd}24"
- "v40@0:8q16^{CGContext=}24@32"
- "v40@0:8q16^{CGContext=}24@?32"
- "v40@0:8q16{CGPoint=dd}24"
- "v40@0:8{CGPoint=dd}16@32"
- "v44@0:8@\"UIGestureRecognizer\"16Q24B32@\"AKController\"36"
- "v44@0:8@16B24{?=qq}28"
- "v44@0:8@16Q24B32@36"
- "v44@0:8^{CGPDFForm=}16q24^{CGContext=}32B40"
- "v44@0:8i16@20q28^{CGContext=}36"
- "v44@0:8i16^{__CFDictionary=}20{CGPoint=dd}28"
- "v44@0:8{_NSRange=QQ}16@32B40"
- "v48@0:8@\"PDFPage\"16Q24@\"PDFPage\"32Q40"
- "v48@0:8@\"UICollectionView\"16:24@\"NSIndexPath\"32@40"
- "v48@0:8@\"UICollectionView\"16@\"UICollectionReusableView\"24@\"NSString\"32@\"NSIndexPath\"40"
- "v48@0:8@\"UIScrollView\"16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v48@0:8@16:24@32@40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24@32Q40"
- "v48@0:8@16@24@32^v40"
- "v48@0:8@16@24Q32@40"
- "v48@0:8@16@24Q32@?40"
- "v48@0:8@16Q24@32@40"
- "v48@0:8@16Q24@32@?40"
- "v48@0:8@16Q24@32Q40"
- "v48@0:8@16q24@32@?40"
- "v48@0:8@16q24{CGPoint=dd}32"
- "v48@0:8@16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v48@0:8Q16q24{CGPoint=dd}32"
- "v48@0:8i16@20q28^{CGContext=}36B44"
- "v48@0:8q16^{CGContext=}24@32@40"
- "v48@0:8{CGPoint=dd}16@32@?40"
- "v48@0:8{CGPoint=dd}16{CGPoint=dd}32"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "v48@0:8{UIEdgeInsets=dddd}16"
- "v48@0:8{_NSRange=QQ}16@32@?40"
- "v52@0:8@?16@24@32@40B48"
- "v52@0:8B16{CGRect={CGPoint=dd}{CGSize=dd}}20"
- "v52@0:8i16@20q28^{CGContext=}36B44B48"
- "v52@0:8{CGPoint=dd}16i32^{CGContext=}36@44"
- "v56@0:8@\"AKController\"16Q24q32q40Q48"
- "v56@0:8@16@24Q32@40Q48"
- "v56@0:8@16Q24q32q40Q48"
- "v56@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "v56@0:8^{CGContext=}16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "v56@0:8q16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "v56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48"
- "v56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16^{CGContext=}48"
- "v56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16q48"
- "v60@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16d48B56"
- "v64@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24@56"
- "v64@0:8^{CGContext=}16@24{CGRect={CGPoint=dd}{CGSize=dd}}32"
- "v64@0:8^{CGContext=}16{CGRect={CGPoint=dd}{CGSize=dd}}24@56"
- "v64@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48^{CGContext=}56"
- "v64@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16^{__CFString=}48^{__CFDictionary=}56"
- "v68@0:8@16^{CGContext=}24@32@40@48@56B64"
- "v68@0:8@16^{CGContext=}24q32@40@48@56B64"
- "v68@0:8Q16q24{CGPoint=dd}32{CGPoint=dd}48B64"
- "v68@0:8{CGPoint=dd}16{CGPoint=dd}32B48^{CGContext=}52@60"
- "v68@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48B56@?60"
- "v72@0:8@16@24^{CGContext=}32{CGRect={CGPoint=dd}{CGSize=dd}}40"
- "v72@0:8@16@24{CGRect={CGPoint=dd}{CGSize=dd}}32@64"
- "v72@0:8@16{CGAffineTransform=dddddd}24"
- "v72@0:8@16{CGPoint=dd}24{CGRect={CGPoint=dd}{CGSize=dd}}40"
- "v72@0:8q16{CGPoint=dd}24{CGRect={CGPoint=dd}{CGSize=dd}}40"
- "v72@0:8{TextAnnotationAnimationProperties={CGRect={CGPoint=dd}{CGSize=dd}}dd}16d64"
- "v76@0:8^{CGDisplayList=}16q24^{CGContext=}32{CGRect={CGPoint=dd}{CGSize=dd}}40B72"
- "v76@0:8^{CGPDFForm=}16q24^{CGContext=}32{CGRect={CGPoint=dd}{CGSize=dd}}40B72"
- "v80@0:8^{CGPDFForm=}16q24^{CGContext=}32{CGRect={CGPoint=dd}{CGSize=dd}}40B72B76"
- "v88@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16^{CGContext=}48@56@64@72@80"
- "v88@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48d80"
- "v96@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16^{CGContext=}48@56@64@72@80@88"
- "vCornerRadius"
- "validateRedo:"
- "validateUndo:"
- "value"
- "valueForAnnotationKey:"
- "valueForCGPDFObject:visitedSet:isInternalObject:"
- "valueForKey:"
- "valueWithCATransform3D:"
- "valueWithCGMatrixFilter:"
- "valueWithCGPoint:"
- "valueWithCGRect:"
- "valueWithPointer:"
- "valueWithRange:"
- "valueWithRect:"
- "valueWithWeakObject:"
- "values"
- "verticalCornerRadius"
- "view"
- "viewControllers"
- "viewDidAppear:"
- "viewDidDisappear:"
- "viewDidLayoutSubviews"
- "viewDidLoad"
- "viewForPage:"
- "viewForZoomingInScrollView:"
- "viewIfLoaded"
- "viewLayout"
- "viewMarquee"
- "viewPreferenceRightToLeft"
- "viewProvider"
- "viewWillAppear:"
- "viewWillDisappear:"
- "viewWillLayoutSubviews"
- "visibilityDelegateIndex"
- "visibilityTimer"
- "visible"
- "visibleAnnotations"
- "visiblePageRangeInBounds:currentPage:"
- "visiblePageViews"
- "visiblePages"
- "visiblePagesChanged:"
- "visiblePagesInBounds:currentPage:"
- "visibleRect"
- "visibleRectForPageView:"
- "visibleRectOfOverlayAtPageIndex:forAnnotationController:"
- "wantsForceUpdate"
- "weakObjectValue"
- "weakPageViewControllers"
- "weakPageViewControllersLock"
- "weakWrapperWithObject:"
- "webArchive"
- "whiteColor"
- "whitespaceAndNewlineCharacterSet"
- "whitespaceCharacterSet"
- "widgetControlType"
- "widgetDefaultStringValue"
- "widgetFieldType"
- "widgetOnStateString"
- "widgetStringValue"
- "width"
- "widthAnchor"
- "willChangeValueForKey:"
- "willDismissEditMenuWithAnimator:"
- "willEndStartLiveResize"
- "willForceUpdate"
- "willHighlightFoundTextRange:inDocument:"
- "willInsertPage:atIndex:"
- "willMoveToSuperview:"
- "willPresentEditMenuWithAnimator:"
- "willPresentWritingTools"
- "willRemovePage:atIndex:"
- "willStartLiveResize"
- "willSwapPage:atIndex:forPage:atIndex:"
- "window"
- "windowDidBecomeKey:"
- "windowDidResignKey:"
- "workQueue"
- "workQueueThrottle"
- "writeDefaultValue"
- "writePDFDocumentFromPages:completionHandler:"
- "writeToConsumer:withOptions:"
- "writeToFile:"
- "writeToFile:atomically:"
- "writeToFile:withOptions:"
- "writeToURL:"
- "writeToURL:withOptions:"
- "writingDirection"
- "writingToolsBehavior"
- "yellowColor"
- "zone"
- "zoom"
- "zoomFactor"
- "zoomIn:"
- "zoomIncrement"
- "zoomOut:"
- "zoomScale"
- "zoomToRect"
- "zoomToRect:"
- "zoomToRect:animated:"
- "{?=\"pagesAdded\"B\"blankPagesAdded\"B\"pagesRemoved\"B\"pagesExchanged\"B}"
- "{?={CGPoint=dd}{CGPoint=dd}}20@0:8i16"
- "{CAColorMatrix=ffffffffffffffffffff}16@0:8"
- "{CGAffineTransform=\"a\"d\"b\"d\"c\"d\"d\"d\"tx\"d\"ty\"d}"
- "{CGAffineTransform=dddddd}16@0:8"
- "{CGAffineTransform=dddddd}24@0:8@\"UITextPosition\"16"
- "{CGAffineTransform=dddddd}24@0:8@16"
- "{CGAffineTransform=dddddd}24@0:8q16"
- "{CGAffineTransform=dddddd}32@0:8{CGSize=dd}16"
- "{CGAffineTransform=dddddd}48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "{CGMatrixFilter=ffffffffffffffffffff}16@0:8"
- "{CGPoint=\"x\"d\"y\"d}"
- "{CGPoint=dd}16@0:8"
- "{CGPoint=dd}24@0:8@16"
- "{CGPoint=dd}32@0:8{CGPoint=dd}16"
- "{CGPoint=dd}40@0:8@\"UICollectionView\"16{CGPoint=dd}24"
- "{CGPoint=dd}40@0:8@16{CGPoint=dd}24"
- "{CGPoint=dd}40@0:8{CGPoint=dd}16@32"
- "{CGPoint=dd}48@0:8{CGPoint=dd}16@32d40"
- "{CGPoint=dd}48@0:8{CGPoint=dd}16Q32@\"AKController\"40"
- "{CGPoint=dd}48@0:8{CGPoint=dd}16Q32@40"
- "{CGPoint=dd}48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "{CGPoint=dd}56@0:8{CGPoint=dd}16{CGPoint=dd}32@?48"
- "{CGPoint=dd}72@0:8{CGPoint=dd}16{CGPoint=dd}32{CGPoint=dd}48d64"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGRect={CGPoint=dd}{CGSize=dd}}20@0:8i16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8@\"UITextPosition\"16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8@\"UITextRange\"16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8@16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8Q16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8q16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}32@0:8@\"UIEditMenuInteraction\"16@\"UIEditMenuConfiguration\"24"
- "{CGRect={CGPoint=dd}{CGSize=dd}}32@0:8@16@24"
- "{CGRect={CGPoint=dd}{CGSize=dd}}32@0:8Q16@\"AKController\"24"
- "{CGRect={CGPoint=dd}{CGSize=dd}}32@0:8Q16@24"
- "{CGRect={CGPoint=dd}{CGSize=dd}}32@0:8q16@24"
- "{CGRect={CGPoint=dd}{CGSize=dd}}32@0:8q16Q24"
- "{CGRect={CGPoint=dd}{CGSize=dd}}32@0:8{CGPoint=dd}16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}40@0:8@16{CGPoint=dd}24"
- "{CGRect={CGPoint=dd}{CGSize=dd}}48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48"
- "{CGRect={CGPoint=dd}{CGSize=dd}}64@0:8q16{CGPoint=dd}24{CGPoint=dd}40d56"
- "{CGRect={CGPoint=dd}{CGSize=dd}}64@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48d56"
- "{CGSize=\"width\"d\"height\"d}"
- "{CGSize=dd}16@0:8"
- "{CGSize=dd}24@0:8@16"
- "{CGSize=dd}32@0:8@16q24"
- "{CGSize=dd}40@0:8@16q24@32"
- "{CGVector=dd}16@0:8"
- "{TextAnnotationAnimationProperties=\"visibleTextViewRectInScrollView\"{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}\"animationDuration\"d\"originDelta\"d}"
- "{UIEdgeInsets=\"top\"d\"left\"d\"bottom\"d\"right\"d}"
- "{UIEdgeInsets=dddd}16@0:8"
- "{UIEdgeInsets=dddd}44@0:8@16^{CGImage=}24C32Q36"
- "{_NSRange=\"location\"Q\"length\"Q}"
- "{_NSRange=QQ}16@0:8"
- "{_NSRange=QQ}32@0:8Q16@24"
- "{_NSRange=QQ}56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48"
- "{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{pdf_unfair_mutex=\"m_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}}"
- "{vector<CGRect, std::allocator<CGRect>>=\"__begin_\"^{CGRect}\"__end_\"^{CGRect}\"\"{?=\"__cap_\"^{CGRect}}}"
- "{vector<PDFDetectedFormRow, std::allocator<PDFDetectedFormRow>>=\"__begin_\"^{PDFDetectedFormRow}\"__end_\"^{PDFDetectedFormRow}\"\"{?=\"__cap_\"^{PDFDetectedFormRow}}}"
- "{vector<const CGDisplayListEntry *, std::allocator<const CGDisplayListEntry *>>=^^{CGDisplayListEntry}^^{CGDisplayListEntry}{?=^^{CGDisplayListEntry}}}32@0:8^{CGDisplayList=}16^d24"

```
