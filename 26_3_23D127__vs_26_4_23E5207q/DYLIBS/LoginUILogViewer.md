## LoginUILogViewer

> `/System/Library/PrivateFrameworks/LoginUILogViewer.framework/LoginUILogViewer`

```diff

-3019.0.0.0.0
-  __TEXT.__text: 0xcc2c
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0x1bb0
+3024.0.0.0.0
+  __TEXT.__text: 0xe620
+  __TEXT.__auth_stubs: 0x430
+  __TEXT.__objc_methlist: 0x1bb8
   __TEXT.__const: 0x188
-  __TEXT.__gcc_except_tab: 0x19c
+  __TEXT.__gcc_except_tab: 0x118
   __TEXT.__cstring: 0x3dc
-  __TEXT.__unwind_info: 0x400
+  __TEXT.__unwind_info: 0x580
   __TEXT.__objc_classname: 0x355
-  __TEXT.__objc_methname: 0x5822
-  __TEXT.__objc_methtype: 0x1e0e
-  __TEXT.__objc_stubs: 0x32a0
-  __DATA_CONST.__got: 0x1f8
+  __TEXT.__objc_methname: 0x583e
+  __TEXT.__objc_methtype: 0x1e35
+  __TEXT.__objc_stubs: 0x32e0
+  __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0x318
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1540
+  __DATA_CONST.__objc_selrefs: 0x1550
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__auth_got: 0x238
+  __AUTH_CONST.__auth_got: 0x228
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x820
   __AUTH_CONST.__objc_const: 0x2f10

   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 214CB0BC-3D8F-370D-829E-21965C6E0B8E
-  Functions: 387
-  Symbols:   1653
-  CStrings:  1212
+  UUID: D45151D7-AB0A-3CDE-ACEF-31C50E33F5B0
+  Functions: 388
+  Symbols:   1654
+  CStrings:  1215
 
Symbols:
+ -[LUILogViewerController _windowBounds]
+ _objc_msgSend$_windowBounds
+ _objc_msgSend$effectiveGeometry
+ _objc_msgSend$screen
+ _objc_retain_x28
- _OBJC_CLASS_$_UIScreen
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$mainScreen
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
Functions:
~ -[LUILogFilterPredicateCandidateCollectionViewCell _setupUI] : 112 -> 120
~ -[LUILogFilterPredicateCandidateCollectionViewCell setSelected:] : 212 -> 232
~ -[LUILogFilterPredicateCandidateCollectionViewCell layoutSubViews] : 136 -> 140
~ -[LUILogFilterPredicateCandidateCollectionViewCell _createTitleLabel] : 244 -> 252
~ -[LUILogScreenshotItem setScreenshotImage:] : 12 -> 64
~ -[LUILogScreenshotItem setScreenshotDate:] : 12 -> 64
~ -[LUILogViewerController setup] : 328 -> 348
~ ___31-[LUILogViewerController setup]_block_invoke : 88 -> 92
~ -[LUILogViewerController init] : 292 -> 300
~ -[LUILogViewerController _grabLogAndUpdateTextView] : 280 -> 304
~ ___51-[LUILogViewerController _grabLogAndUpdateTextView]_block_invoke : 352 -> 372
~ ___51-[LUILogViewerController _grabLogAndUpdateTextView]_block_invoke_2 : 180 -> 200
~ -[LUILogViewerController _getLogsFromDate:predicate:duplicateHandler:] : 732 -> 716
~ ___70-[LUILogViewerController _getLogsFromDate:predicate:duplicateHandler:]_block_invoke : 16 -> 72
~ ___70-[LUILogViewerController _getLogsFromDate:predicate:duplicateHandler:]_block_invoke_2 : 552 -> 616
~ -[LUILogViewerController _attributedLogStringFrom:fontSize:] : 1228 -> 1296
~ -[LUILogViewerController _startStreamLog] : 224 -> 232
~ -[LUILogViewerController _stopStreaming] : 92 -> 96
~ -[LUILogViewerController _updateLogFromLastTime] : 440 -> 476
~ ___48-[LUILogViewerController _updateLogFromLastTime]_block_invoke : 432 -> 448
~ ___48-[LUILogViewerController _updateLogFromLastTime]_block_invoke_3 : 268 -> 300
~ -[LUILogViewerController _cleanupLogs] : 264 -> 288
~ -[LUILogViewerController keyboardWillShow:] : 396 -> 368
~ -[LUILogViewerController keyboardWillHide:] : 132 -> 136
~ -[LUILogViewerController _presentLogViewerView] : 792 -> 860
~ ___47-[LUILogViewerController _presentLogViewerView]_block_invoke : 108 -> 112
~ ___47-[LUILogViewerController _presentLogViewerView]_block_invoke_2 : 156 -> 164
~ -[LUILogViewerController _dismissLogViewerView] : 700 -> 748
~ ___47-[LUILogViewerController _dismissLogViewerView]_block_invoke : 88 -> 92
~ ___47-[LUILogViewerController _dismissLogViewerView]_block_invoke_2 : 196 -> 208
~ -[LUILogViewerController showLogFilterPage] : 476 -> 512
~ ___43-[LUILogViewerController showLogFilterPage]_block_invoke : 180 -> 196
~ -[LUILogViewerController showLogContentPage] : 476 -> 512
~ ___44-[LUILogViewerController showLogContentPage]_block_invoke : 180 -> 196
~ -[LUILogViewerController _moveElementsToView:] : 380 -> 424
~ -[LUILogViewerController _increaseCurrentHighlightIndex] : 184 -> 196
~ -[LUILogViewerController _decreaseCurrentHighlightIndex] : 216 -> 232
~ -[LUILogViewerController _performSearch:] : 376 -> 400
~ -[LUILogViewerController _setupInitialHighlight] : 464 -> 524
~ ___48-[LUILogViewerController _setupInitialHighlight]_block_invoke : 228 -> 248
~ -[LUILogViewerController _updateHighlight] : 268 -> 300
~ -[LUILogViewerController _cleanupHighlight] : 532 -> 580
~ -[LUILogViewerController _searchRangeForDate:inText:] : 692 -> 756
~ -[LUILogViewerController assistiveTouch] : 272 -> 240
~ -[LUILogViewerController logViewerView] : 444 -> 416
~ -[LUILogViewerController pageViewController] : 296 -> 316
~ -[LUILogViewerController logContentViewController] : 96 -> 104
~ -[LUILogViewerController logFilterViewController] : 96 -> 104
~ -[LUILogViewerController panGesture] : 112 -> 120
~ -[LUILogViewerController observeValueForKeyPath:ofObject:change:context:] : 172 -> 180
~ ___36-[LUILogViewerController handlePan:]_block_invoke : 88 -> 92
~ -[LUILogViewerController gestureRecognizerShouldBegin:] : 140 -> 152
~ -[LUILogViewerController logViewerViewClearButtontapped:] : 160 -> 164
~ -[LUILogViewerController logViewerLeftCaretButtonTapped:] : 112 -> 116
~ -[LUILogViewerController logViewerRightCaretButtonTapped:] : 112 -> 116
~ -[LUILogViewerController pageViewController:didFinishAnimating:previousViewControllers:transitionCompleted:] : 208 -> 228
~ -[LUILogViewerController pageViewController:viewControllerAfterViewController:] : 184 -> 200
~ -[LUILogViewerController pageViewController:viewControllerBeforeViewController:] : 152 -> 164
~ -[LUILogViewerController orderedViewControllers] : 148 -> 176
~ ___48-[LUILogViewerController orderedViewControllers]_block_invoke : 172 -> 184
~ -[LUILogViewerController logFilterViewController:didAddPredicates:] : 188 -> 196
~ ___67-[LUILogViewerController logFilterViewController:didAddPredicates:]_block_invoke : 112 -> 120
~ -[LUILogViewerController logFilterViewControllerApplyButtonTapped:] : 164 -> 168
~ -[LUILogViewerController logContentViewController:didSelectLogOptionWithTimeInterval:] : 132 -> 136
~ -[LUILogViewerController logContentViewController:didSelectDateForLog:] : 244 -> 260
~ -[LUILogViewerController searchBarSearchButtonClicked:] : 168 -> 172
~ -[LUILogViewerController searchBarShouldBeginEditing:] : 116 -> 132
+ -[LUILogViewerController _windowBounds]
~ -[LUILogViewerController setLogViewerView:] : 12 -> 64
~ -[LUILogViewerController setAssistiveTouch:] : 12 -> 64
~ -[LUILogViewerController setLogContentViewController:] : 12 -> 64
~ -[LUILogViewerController setLogFilterViewController:] : 12 -> 64
~ -[LUILogViewerController setPageViewController:] : 12 -> 64
~ -[LUILogViewerController setPredicates:] : 12 -> 64
~ -[LUILogViewerController setLastLogDate:] : 12 -> 64
~ -[LUILogViewerController setFirstLogDate:] : 12 -> 64
~ -[LUILogViewerController setLogMinutesSet:] : 12 -> 64
~ -[LUILogViewerController setLogMinutesArray:] : 12 -> 64
~ -[LUILogViewerController setHighlightRanges:] : 12 -> 64
~ -[LUILogViewerController setPanGesture:] : 12 -> 64
~ -[LUILogLocatorView _setup] : 380 -> 412
~ -[LUILogLocatorView layoutSubviews] : 912 -> 1012
~ -[LUILogLocatorView _createScreenshotCollectionView] : 204 -> 212
~ -[LUILogLocatorView _createButtonWithImageName:] : 340 -> 372
~ -[LUILogLocatorView setUpArrowButton:] : 20 -> 80
~ -[LUILogLocatorView setDownArrowButton:] : 20 -> 80
~ -[LUILogLocatorView setScreenshotButton:] : 20 -> 80
~ -[LUILogLocatorView setScreenshotCollectionView:] : 20 -> 80
~ -[LUILogOptionsView _setup] : 84 -> 88
~ -[LUILogOptionsView layoutSubviews] : 288 -> 316
~ -[LUILogOptionsView _createButtonStackView] : 468 -> 492
~ -[LUILogOptionsView _createButtonWithTitle:] : 464 -> 508
~ -[LUILogOptionsView setButtonStackView:] : 20 -> 80
~ -[LUILogOptionsView setTenMinutesLogButton:] : 20 -> 80
~ -[LUILogOptionsView setHalfHourButton:] : 20 -> 80
~ -[LUILogOptionsView setHourButton:] : 20 -> 80
~ -[LUILogOptionsView setLastDayButton:] : 20 -> 80
~ -[LUILogOptionsView setStreamButton:] : 20 -> 80
~ -[LUILogContentViewController viewDidLoad] : 220 -> 228
~ -[LUILogContentViewController dealloc] : 140 -> 148
~ -[LUILogContentViewController loadView] : 448 -> 480
~ -[LUILogContentViewController viewWillLayoutSubviews] : 676 -> 772
~ -[LUILogContentViewController _setupButtonActions] : 496 -> 560
~ -[LUILogContentViewController _setupTextViewGesture] : 192 -> 204
~ -[LUILogContentViewController showLogOptionsView] : 136 -> 148
~ -[LUILogContentViewController showLogTextView] : 136 -> 148
~ -[LUILogContentViewController enableTimeConsumingOptions:] : 152 -> 168
~ -[LUILogContentViewController showSpinner:] : 88 -> 92
~ -[LUILogContentViewController _createLogTextView] : 188 -> 200
~ -[LUILogContentViewController _createLogLocatorView] : 128 -> 136
~ -[LUILogContentViewController _dateWithPercentage:] : 200 -> 220
~ -[LUILogContentViewController scrollIndicatorView] : 240 -> 264
~ -[LUILogContentViewController _generateScreenshotItem] : 276 -> 292
~ -[LUILogContentViewController _visibleRangeOfTextView:] : 296 -> 320
~ -[LUILogContentViewController logOptionButtonTapped:] : 392 -> 440
~ -[LUILogContentViewController screenshotButtonTapped:] : 140 -> 152
~ -[LUILogContentViewController upArrowButtonTapped:] : 72 -> 76
~ -[LUILogContentViewController downArrowButtonTapped:] : 132 -> 144
~ -[LUILogContentViewController handlePan:] : 860 -> 936
~ -[LUILogContentViewController gestureRecognizerShouldBegin:] : 260 -> 276
~ -[LUILogContentViewController observeValueForKeyPath:ofObject:change:context:] : 216 -> 232
~ -[LUILogContentViewController collectionView:numberOfItemsInSection:] : 56 -> 60
~ -[LUILogContentViewController collectionView:cellForItemAtIndexPath:] : 512 -> 536
~ ___69-[LUILogContentViewController collectionView:cellForItemAtIndexPath:]_block_invoke_2 : 148 -> 152
~ -[LUILogContentViewController collectionView:didSelectItemAtIndexPath:] : 204 -> 212
~ -[LUILogContentViewController setLogOptionsView:] : 20 -> 80
~ -[LUILogContentViewController setLogLocatorView:] : 20 -> 80
~ -[LUILogContentViewController setSpinner:] : 20 -> 80
~ -[LUILogContentViewController setScreenshotItems:] : 20 -> 80
~ -[LUILogContentViewController setTextViewHolderView:] : 20 -> 80
~ -[LUILogContentViewController setPanGesture:] : 20 -> 80
~ -[LUILogContentViewController setScrollIndicatorView:] : 20 -> 80
~ -[LUILogViewerView _setup] : 660 -> 704
~ -[LUILogViewerView layoutSubviews] : 296 -> 308
~ -[LUILogViewerView switchClearButtonTitle:] : 104 -> 108
~ -[LUILogViewerView highlightFilterButton:] : 92 -> 96
~ -[LUILogViewerView highlightLogButton:] : 92 -> 96
~ -[LUILogViewerView _highlightButton:highlight:] : 204 -> 212
~ -[LUILogViewerView resetSearchResultLabel] : 72 -> 76
~ -[LUILogViewerView updateSearchResultLabelWithTotalResult:currentIndex:] : 120 -> 128
~ -[LUILogViewerView _createButtonWithTitle:action:] : 208 -> 212
~ -[LUILogViewerView _createSearchBar] : 184 -> 188
~ -[LUILogViewerView _createSearchResultLabel] : 144 -> 148
~ -[LUILogViewerView closeButtonTapped:] : 80 -> 84
~ -[LUILogViewerView logButtonTapped:] : 80 -> 84
~ -[LUILogViewerView clearButtonTapped:] : 80 -> 84
~ -[LUILogViewerView filterButtonTapped:] : 80 -> 84
~ -[LUILogViewerView leftCaretButtonTapped:] : 80 -> 84
~ -[LUILogViewerView rightCaretButtonTapped:] : 80 -> 84
~ -[LUILogViewerView setContentHolderView:] : 20 -> 80
~ -[LUILogViewerView setFilterButton:] : 20 -> 80
~ -[LUILogViewerView setSearchBar:] : 20 -> 80
~ -[LUILogViewerView setCloseButton:] : 20 -> 80
~ -[LUILogViewerView setFilterView:] : 20 -> 80
~ -[LUILogViewerView setLogButton:] : 20 -> 80
~ -[LUILogViewerView setClearButton:] : 20 -> 80
~ -[LUILogViewerView setButtonStack:] : 20 -> 80
~ -[LUILogViewerView setSearchResultLabel:] : 20 -> 80
~ -[LUILogViewerView setLeftCaretButton:] : 20 -> 80
~ -[LUILogViewerView setRightCaretButton:] : 20 -> 80
~ -[LUILogFilterCurrentPredicateTableViewCell _setupUI] : 316 -> 344
~ -[LUILogFilterCurrentPredicateTableViewCell layoutSubviews] : 244 -> 256
~ -[LUILogFilterCurrentPredicateTableViewCell _createTitleLabel] : 236 -> 244
~ -[LUILogFilterCurrentPredicateTableViewCell _createDeleteButton] : 192 -> 208
~ -[LUILogFilterCurrentPredicateTableViewCell _deleteButtonTapped:] : 80 -> 84
~ _secondStringWithDate : 108 -> 112
~ -[LUILogViewerAssistiveTouch _setup] : 200 -> 216
~ -[LUILogViewerAssistiveTouch layoutSubviews] : 124 -> 128
~ -[LUILogFilterView _setup] : 832 -> 900
~ -[LUILogFilterView layoutSubviews] : 980 -> 1052
~ -[LUILogFilterView _createCurrentPredicateLabel] : 184 -> 192
~ -[LUILogFilterView _createEnterLabel] : 232 -> 240
~ -[LUILogFilterView _createPredicateTextField] : 532 -> 572
~ -[LUILogFilterView _createButtonWithTitle:] : 204 -> 208
~ -[LUILogFilterView _createCollectionView] : 152 -> 156
~ -[LUILogFilterView _createTableView] : 136 -> 140
~ -[LUILogFilterView _createSeparatorLine] : 100 -> 104
~ -[LUILogFilterView setExistingPredicatesTableView:] : 20 -> 80
~ -[LUILogFilterView setPredicatesKeyCandidateCollectionView:] : 20 -> 80
~ -[LUILogFilterView setPredicatesComparisonCandidateCollectionView:] : 20 -> 80
~ -[LUILogFilterView setPredicatesValueCandidateCollectionView:] : 20 -> 80
~ -[LUILogFilterView setHorizontalSeparatorLine:] : 20 -> 80
~ -[LUILogFilterView setVeriticalSeparatorLineFirst:] : 20 -> 80
~ -[LUILogFilterView setVeriticalSeparatorLineSecond:] : 20 -> 80
~ -[LUILogFilterView setCurrentPredicateLabel:] : 20 -> 80
~ -[LUILogFilterView setEnterPredicateStackView:] : 20 -> 80
~ -[LUILogFilterView setAddButton:] : 20 -> 80
~ -[LUILogFilterView setPredicateTextField:] : 20 -> 80
~ -[LUILogFilterView setApplyButton:] : 20 -> 80
~ -[LUILogFilterViewController viewDidLoad] : 144 -> 152
~ -[LUILogFilterViewController viewDidAppear:] : 260 -> 280
~ -[LUILogFilterViewController viewDidDisappear:] : 100 -> 104
~ -[LUILogFilterViewController viewWillLayoutSubviews] : 188 -> 212
~ -[LUILogFilterViewController viewDidMoveToWindow:shouldAppearOrDisappear:] : 152 -> 164
~ -[LUILogFilterViewController _setupTableView] : 216 -> 240
~ -[LUILogFilterViewController _setupCollectionView] : 568 -> 648
~ -[LUILogFilterViewController _setupButtons] : 172 -> 188
~ -[LUILogFilterViewController predicateDataUpdated] : 88 -> 96
~ -[LUILogFilterViewController predicateKeyCandidates] : 68 -> 84
~ -[LUILogFilterViewController predicateComparisonCandidates] : 68 -> 84
~ -[LUILogFilterViewController predicateValueCandidates] : 68 -> 84
~ -[LUILogFilterViewController predicateValueCandidatesSize] : 148 -> 176
~ ___58-[LUILogFilterViewController predicateValueCandidatesSize]_block_invoke : 108 -> 116
~ -[LUILogFilterViewController sizeArrayWithStrings:] : 564 -> 580
~ -[LUILogFilterViewController _updatePredicateText] : 600 -> 640
~ ___50-[LUILogFilterViewController _updatePredicateText]_block_invoke : 332 -> 368
~ ___50-[LUILogFilterViewController _updatePredicateText]_block_invoke_2 : 276 -> 288
~ -[LUILogFilterViewController _clearCellsSelection] : 540 -> 572
~ -[LUILogFilterViewController _clearPredicateInput] : 100 -> 108
~ -[LUILogFilterViewController _shakeInputView:] : 324 -> 340
~ -[LUILogFilterViewController addButtonTapped:] : 1008 -> 1148
~ -[LUILogFilterViewController applyButtonTapped:] : 80 -> 84
~ -[LUILogFilterViewController collectionView:cellForItemAtIndexPath:] : 488 -> 548
~ -[LUILogFilterViewController collectionView:numberOfItemsInSection:] : 256 -> 292
~ -[LUILogFilterViewController collectionView:layout:sizeForItemAtIndexPath:] : 220 -> 232
~ -[LUILogFilterViewController tableView:cellForRowAtIndexPath:] : 248 -> 272
~ -[LUILogFilterViewController numberOfSectionsInTableView:] : 92 -> 100
~ -[LUILogFilterViewController tableView:numberOfRowsInSection:] : 92 -> 100
~ -[LUILogFilterViewController tableView:viewForFooterInSection:] : 100 -> 104
~ -[LUILogFilterViewController predicateTableViewCellDeleteButtonTapped:] : 248 -> 276
~ -[LUILogFilterViewController keyboardWillShow:] : 144 -> 152
~ -[LUILogFilterViewController keyboardWillHide:] : 140 -> 148
~ -[LUILogFilterViewController setFilterView:] : 20 -> 80
~ -[LUILogScreenshotCollectionViewCell _setup] : 248 -> 272
~ -[LUILogScreenshotCollectionViewCell _createClearButton] : 148 -> 152
~ -[LUILogScreenshotCollectionViewCell _createScreenshotDateLabel] : 112 -> 116
~ -[LUILogScreenshotCollectionViewCell clearButtonTapped:] : 124 -> 132
CStrings:
+ "_windowBounds"
+ "effectiveGeometry"
+ "screen"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "mainScreen"

```
