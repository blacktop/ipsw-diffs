## LoginUILogViewer

> `/System/Library/PrivateFrameworks/LoginUILogViewer.framework/LoginUILogViewer`

```diff

-3024.0.0.0.0
-  __TEXT.__text: 0xe620
-  __TEXT.__auth_stubs: 0x430
+3030.0.0.0.0
+  __TEXT.__text: 0xcdd0
   __TEXT.__objc_methlist: 0x1bb8
   __TEXT.__const: 0x188
-  __TEXT.__gcc_except_tab: 0x118
-  __TEXT.__cstring: 0x3dc
-  __TEXT.__unwind_info: 0x580
-  __TEXT.__objc_classname: 0x355
-  __TEXT.__objc_methname: 0x583e
-  __TEXT.__objc_methtype: 0x1e35
-  __TEXT.__objc_stubs: 0x32e0
-  __DATA_CONST.__got: 0x1f0
+  __TEXT.__cstring: 0x3f7
+  __TEXT.__gcc_except_tab: 0x19c
+  __TEXT.__unwind_info: 0x410
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x318
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_selrefs: 0x1550
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__auth_got: 0x228
+  __DATA_CONST.__got: 0x1f0
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x820
   __AUTH_CONST.__objc_const: 0x2f10
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x410
   __DATA.__objc_ivar: 0x12c
   __DATA.__data: 0x660

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
+  - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3769F253-759E-3399-90A0-DE4CF590907E
+  UUID: 74DC4F72-BBA6-3513-824C-9CC34B90AA48
   Functions: 388
-  Symbols:   1654
-  CStrings:  1215
+  Symbols:   1656
+  CStrings:  143
 
Symbols:
+ ___block_literal_global.147
+ ___block_literal_global.158
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
- ___block_literal_global.148
- ___block_literal_global.159
- _objc_retain_x28
Functions:
~ -[LUILogFilterPredicateCandidateCollectionViewCell _setupUI] : 120 -> 116
~ -[LUILogFilterPredicateCandidateCollectionViewCell setSelected:] : 232 -> 212
~ -[LUILogFilterPredicateCandidateCollectionViewCell layoutSubViews] : 140 -> 136
~ -[LUILogFilterPredicateCandidateCollectionViewCell _createTitleLabel] : 252 -> 244
~ -[LUILogFilterPredicateCandidateCollectionViewCell titleLabel] : 16 -> 20
~ -[LUILogScreenshotItem setScreenshotImage:] : 64 -> 12
~ -[LUILogScreenshotItem setScreenshotDate:] : 64 -> 12
~ -[LUILogViewerController setup] : 348 -> 328
~ ___31-[LUILogViewerController setup]_block_invoke : 92 -> 88
~ -[LUILogViewerController init] : 300 -> 292
~ -[LUILogViewerController _grabLogAndUpdateTextView] : 304 -> 280
~ ___51-[LUILogViewerController _grabLogAndUpdateTextView]_block_invoke : 372 -> 352
~ ___51-[LUILogViewerController _grabLogAndUpdateTextView]_block_invoke_2 : 200 -> 180
~ -[LUILogViewerController _getLogsFromDate:predicate:duplicateHandler:] : 716 -> 732
~ ___70-[LUILogViewerController _getLogsFromDate:predicate:duplicateHandler:]_block_invoke : 72 -> 16
~ ___70-[LUILogViewerController _getLogsFromDate:predicate:duplicateHandler:]_block_invoke_2 : 616 -> 552
~ -[LUILogViewerController _attributedLogStringFrom:fontSize:] : 1296 -> 1216
~ -[LUILogViewerController _startStreamLog] : 232 -> 224
~ -[LUILogViewerController _stopStreaming] : 96 -> 92
~ -[LUILogViewerController _updateLogFromLastTime] : 476 -> 440
~ ___48-[LUILogViewerController _updateLogFromLastTime]_block_invoke : 448 -> 432
~ ___48-[LUILogViewerController _updateLogFromLastTime]_block_invoke_3 : 300 -> 268
~ -[LUILogViewerController _cleanupLogs] : 288 -> 264
~ -[LUILogViewerController keyboardWillShow:] : 368 -> 348
~ -[LUILogViewerController keyboardWillHide:] : 136 -> 132
~ -[LUILogViewerController _presentLogViewerView] : 860 -> 792
~ ___47-[LUILogViewerController _presentLogViewerView]_block_invoke : 112 -> 108
~ ___47-[LUILogViewerController _presentLogViewerView]_block_invoke_2 : 164 -> 156
~ -[LUILogViewerController _dismissLogViewerView] : 748 -> 700
~ ___47-[LUILogViewerController _dismissLogViewerView]_block_invoke : 92 -> 88
~ ___47-[LUILogViewerController _dismissLogViewerView]_block_invoke_2 : 208 -> 196
~ -[LUILogViewerController showLogFilterPage] : 512 -> 476
~ ___43-[LUILogViewerController showLogFilterPage]_block_invoke : 196 -> 180
~ -[LUILogViewerController showLogContentPage] : 512 -> 476
~ ___44-[LUILogViewerController showLogContentPage]_block_invoke : 196 -> 180
~ -[LUILogViewerController _moveElementsToView:] : 424 -> 380
~ -[LUILogViewerController _increaseCurrentHighlightIndex] : 196 -> 184
~ -[LUILogViewerController _decreaseCurrentHighlightIndex] : 232 -> 216
~ -[LUILogViewerController _performSearch:] : 400 -> 376
~ -[LUILogViewerController _setupInitialHighlight] : 524 -> 464
~ ___48-[LUILogViewerController _setupInitialHighlight]_block_invoke : 248 -> 228
~ -[LUILogViewerController _updateHighlight] : 300 -> 268
~ -[LUILogViewerController _cleanupHighlight] : 580 -> 536
~ -[LUILogViewerController _searchRangeForDate:inText:] : 756 -> 692
~ -[LUILogViewerController assistiveTouch] : 240 -> 228
~ -[LUILogViewerController logViewerView] : 416 -> 388
~ -[LUILogViewerController pageViewController] : 316 -> 296
~ -[LUILogViewerController logContentViewController] : 104 -> 96
~ -[LUILogViewerController logFilterViewController] : 104 -> 96
~ -[LUILogViewerController panGesture] : 120 -> 112
~ -[LUILogViewerController observeValueForKeyPath:ofObject:change:context:] : 180 -> 172
~ -[LUILogViewerController handlePan:] : 676 -> 640
~ ___36-[LUILogViewerController handlePan:]_block_invoke : 92 -> 88
~ -[LUILogViewerController gestureRecognizerShouldBegin:] : 152 -> 140
~ -[LUILogViewerController logViewerViewClearButtontapped:] : 164 -> 160
~ -[LUILogViewerController logViewerLeftCaretButtonTapped:] : 116 -> 112
~ -[LUILogViewerController logViewerRightCaretButtonTapped:] : 116 -> 112
~ -[LUILogViewerController pageViewController:didFinishAnimating:previousViewControllers:transitionCompleted:] : 228 -> 208
~ -[LUILogViewerController pageViewController:viewControllerAfterViewController:] : 200 -> 184
~ -[LUILogViewerController pageViewController:viewControllerBeforeViewController:] : 164 -> 152
~ -[LUILogViewerController orderedViewControllers] : 176 -> 148
~ ___48-[LUILogViewerController orderedViewControllers]_block_invoke : 184 -> 172
~ -[LUILogViewerController logFilterViewController:didAddPredicates:] : 196 -> 188
~ ___67-[LUILogViewerController logFilterViewController:didAddPredicates:]_block_invoke : 120 -> 112
~ -[LUILogViewerController logFilterViewControllerApplyButtonTapped:] : 168 -> 164
~ -[LUILogViewerController logContentViewController:didSelectLogOptionWithTimeInterval:] : 136 -> 132
~ -[LUILogViewerController logContentViewController:didSelectDateForLog:] : 260 -> 244
~ -[LUILogViewerController searchBarSearchButtonClicked:] : 172 -> 168
~ -[LUILogViewerController searchBarShouldBeginEditing:] : 132 -> 116
~ -[LUILogViewerController _windowBounds] : 204 -> 184
~ -[LUILogViewerController setLogViewerView:] : 64 -> 12
~ -[LUILogViewerController setAssistiveTouch:] : 64 -> 12
~ -[LUILogViewerController setLogContentViewController:] : 64 -> 12
~ -[LUILogViewerController setLogFilterViewController:] : 64 -> 12
~ -[LUILogViewerController setPageViewController:] : 64 -> 12
~ -[LUILogViewerController setPredicates:] : 64 -> 12
~ -[LUILogViewerController setLastLogDate:] : 64 -> 12
~ -[LUILogViewerController setFirstLogDate:] : 64 -> 12
~ -[LUILogViewerController setLogMinutesSet:] : 64 -> 12
~ -[LUILogViewerController setLogMinutesArray:] : 64 -> 12
~ -[LUILogViewerController setHighlightRanges:] : 64 -> 12
~ -[LUILogViewerController setPanGesture:] : 64 -> 12
~ -[LUILogLocatorView _setup] : 412 -> 396
~ -[LUILogLocatorView layoutSubviews] : 1012 -> 936
~ -[LUILogLocatorView handleOrientationChange:] : 116 -> 120
~ -[LUILogLocatorView _createScreenshotCollectionView] : 212 -> 204
~ -[LUILogLocatorView _createButtonWithImageName:] : 372 -> 340
~ -[LUILogLocatorView upArrowButton] : 16 -> 20
~ -[LUILogLocatorView setUpArrowButton:] : 80 -> 20
~ -[LUILogLocatorView downArrowButton] : 16 -> 20
~ -[LUILogLocatorView setDownArrowButton:] : 80 -> 20
~ -[LUILogLocatorView screenshotButton] : 16 -> 20
~ -[LUILogLocatorView setScreenshotButton:] : 80 -> 20
~ -[LUILogLocatorView screenshotCollectionView] : 16 -> 20
~ -[LUILogLocatorView setScreenshotCollectionView:] : 80 -> 20
~ -[LUILogOptionsView layoutSubviews] : 316 -> 288
~ -[LUILogOptionsView _createButtonStackView] : 492 -> 480
~ -[LUILogOptionsView _createButtonWithTitle:] : 508 -> 464
~ -[LUILogOptionsView buttonStackView] : 16 -> 20
~ -[LUILogOptionsView setButtonStackView:] : 80 -> 20
~ -[LUILogOptionsView tenMinutesLogButton] : 16 -> 20
~ -[LUILogOptionsView setTenMinutesLogButton:] : 80 -> 20
~ -[LUILogOptionsView halfHourButton] : 16 -> 20
~ -[LUILogOptionsView setHalfHourButton:] : 80 -> 20
~ -[LUILogOptionsView hourButton] : 16 -> 20
~ -[LUILogOptionsView setHourButton:] : 80 -> 20
~ -[LUILogOptionsView lastDayButton] : 16 -> 20
~ -[LUILogOptionsView setLastDayButton:] : 80 -> 20
~ -[LUILogOptionsView streamButton] : 16 -> 20
~ -[LUILogOptionsView setStreamButton:] : 80 -> 20
~ -[LUILogContentViewController viewDidLoad] : 228 -> 220
~ -[LUILogContentViewController dealloc] : 148 -> 140
~ -[LUILogContentViewController loadView] : 480 -> 468
~ -[LUILogContentViewController viewWillLayoutSubviews] : 772 -> 700
~ -[LUILogContentViewController _setupButtonActions] : 560 -> 496
~ -[LUILogContentViewController _setupTextViewGesture] : 204 -> 192
~ -[LUILogContentViewController showLogOptionsView] : 148 -> 136
~ -[LUILogContentViewController showLogTextView] : 148 -> 136
~ -[LUILogContentViewController enableTimeConsumingOptions:] : 168 -> 152
~ -[LUILogContentViewController showSpinner:] : 92 -> 88
~ -[LUILogContentViewController _createLogTextView] : 200 -> 188
~ -[LUILogContentViewController _createLogLocatorView] : 136 -> 128
~ -[LUILogContentViewController _dateWithPercentage:] : 220 -> 200
~ -[LUILogContentViewController scrollIndicatorView] : 264 -> 244
~ -[LUILogContentViewController _generateScreenshotItem] : 292 -> 276
~ -[LUILogContentViewController _visibleRangeOfTextView:] : 320 -> 296
~ -[LUILogContentViewController logOptionButtonTapped:] : 440 -> 392
~ -[LUILogContentViewController screenshotButtonTapped:] : 152 -> 140
~ -[LUILogContentViewController upArrowButtonTapped:] : 76 -> 72
~ -[LUILogContentViewController downArrowButtonTapped:] : 144 -> 132
~ -[LUILogContentViewController handlePan:] : 936 -> 860
~ -[LUILogContentViewController gestureRecognizerShouldBegin:] : 276 -> 256
~ -[LUILogContentViewController observeValueForKeyPath:ofObject:change:context:] : 232 -> 216
~ -[LUILogContentViewController collectionView:numberOfItemsInSection:] : 60 -> 56
~ -[LUILogContentViewController collectionView:cellForItemAtIndexPath:] : 536 -> 512
~ ___69-[LUILogContentViewController collectionView:cellForItemAtIndexPath:]_block_invoke_2 : 152 -> 148
~ -[LUILogContentViewController collectionView:didSelectItemAtIndexPath:] : 212 -> 204
~ -[LUILogContentViewController textView] : 16 -> 20
~ -[LUILogContentViewController logOptionsView] : 16 -> 20
~ -[LUILogContentViewController setLogOptionsView:] : 80 -> 20
~ -[LUILogContentViewController logLocatorView] : 16 -> 20
~ -[LUILogContentViewController setLogLocatorView:] : 80 -> 20
~ -[LUILogContentViewController spinner] : 16 -> 20
~ -[LUILogContentViewController setSpinner:] : 80 -> 20
~ -[LUILogContentViewController screenshotItems] : 16 -> 20
~ -[LUILogContentViewController setScreenshotItems:] : 80 -> 20
~ -[LUILogContentViewController textViewHolderView] : 16 -> 20
~ -[LUILogContentViewController setTextViewHolderView:] : 80 -> 20
~ -[LUILogContentViewController panGesture] : 16 -> 20
~ -[LUILogContentViewController setPanGesture:] : 80 -> 20
~ -[LUILogContentViewController setScrollIndicatorView:] : 80 -> 20
~ -[LUILogViewerView _setup] : 704 -> 700
~ -[LUILogViewerView layoutSubviews] : 308 -> 296
~ -[LUILogViewerView switchClearButtonTitle:] : 108 -> 104
~ -[LUILogViewerView highlightFilterButton:] : 96 -> 92
~ -[LUILogViewerView highlightLogButton:] : 96 -> 92
~ -[LUILogViewerView _highlightButton:highlight:] : 212 -> 204
~ -[LUILogViewerView resetSearchResultLabel] : 76 -> 72
~ -[LUILogViewerView updateSearchResultLabelWithTotalResult:currentIndex:] : 128 -> 120
~ -[LUILogViewerView _createButtonWithTitle:action:] : 212 -> 208
~ -[LUILogViewerView _createSearchBar] : 188 -> 184
~ -[LUILogViewerView _createSearchResultLabel] : 148 -> 144
~ -[LUILogViewerView closeButtonTapped:] : 84 -> 80
~ -[LUILogViewerView logButtonTapped:] : 84 -> 80
~ -[LUILogViewerView clearButtonTapped:] : 84 -> 80
~ -[LUILogViewerView filterButtonTapped:] : 84 -> 80
~ -[LUILogViewerView leftCaretButtonTapped:] : 84 -> 80
~ -[LUILogViewerView rightCaretButtonTapped:] : 84 -> 80
~ -[LUILogViewerView contentHolderView] : 16 -> 20
~ -[LUILogViewerView setContentHolderView:] : 80 -> 20
~ -[LUILogViewerView filterButton] : 16 -> 20
~ -[LUILogViewerView setFilterButton:] : 80 -> 20
~ -[LUILogViewerView searchBar] : 16 -> 20
~ -[LUILogViewerView setSearchBar:] : 80 -> 20
~ -[LUILogViewerView closeButton] : 16 -> 20
~ -[LUILogViewerView setCloseButton:] : 80 -> 20
~ -[LUILogViewerView filterView] : 16 -> 20
~ -[LUILogViewerView setFilterView:] : 80 -> 20
~ -[LUILogViewerView logButton] : 16 -> 20
~ -[LUILogViewerView setLogButton:] : 80 -> 20
~ -[LUILogViewerView clearButton] : 16 -> 20
~ -[LUILogViewerView setClearButton:] : 80 -> 20
~ -[LUILogViewerView buttonStack] : 16 -> 20
~ -[LUILogViewerView setButtonStack:] : 80 -> 20
~ -[LUILogViewerView searchResultLabel] : 16 -> 20
~ -[LUILogViewerView setSearchResultLabel:] : 80 -> 20
~ -[LUILogViewerView leftCaretButton] : 16 -> 20
~ -[LUILogViewerView setLeftCaretButton:] : 80 -> 20
~ -[LUILogViewerView rightCaretButton] : 16 -> 20
~ -[LUILogViewerView setRightCaretButton:] : 80 -> 20
~ -[LUILogFilterCurrentPredicateTableViewCell _setupUI] : 344 -> 324
~ -[LUILogFilterCurrentPredicateTableViewCell layoutSubviews] : 256 -> 244
~ -[LUILogFilterCurrentPredicateTableViewCell _createTitleLabel] : 244 -> 236
~ -[LUILogFilterCurrentPredicateTableViewCell _createDeleteButton] : 208 -> 192
~ -[LUILogFilterCurrentPredicateTableViewCell _deleteButtonTapped:] : 84 -> 80
~ -[LUILogFilterCurrentPredicateTableViewCell titleLabel] : 16 -> 20
~ -[LUILogFilterCurrentPredicateTableViewCell deleteButton] : 16 -> 20
~ _secondStringWithDate : 112 -> 108
~ -[LUILogViewerAssistiveTouch _setup] : 216 -> 200
~ -[LUILogViewerAssistiveTouch layoutSubviews] : 128 -> 124
~ -[LUILogFilterView _setup] : 900 -> 880
~ -[LUILogFilterView layoutSubviews] : 1052 -> 980
~ -[LUILogFilterView _createCurrentPredicateLabel] : 192 -> 184
~ -[LUILogFilterView _createEnterLabel] : 240 -> 232
~ -[LUILogFilterView _createPredicateTextField] : 572 -> 532
~ -[LUILogFilterView _createButtonWithTitle:] : 208 -> 204
~ -[LUILogFilterView _createCollectionView] : 156 -> 152
~ -[LUILogFilterView _createTableView] : 140 -> 136
~ -[LUILogFilterView _createSeparatorLine] : 104 -> 100
~ -[LUILogFilterView existingPredicatesTableView] : 16 -> 20
~ -[LUILogFilterView setExistingPredicatesTableView:] : 80 -> 20
~ -[LUILogFilterView predicatesKeyCandidateCollectionView] : 16 -> 20
~ -[LUILogFilterView setPredicatesKeyCandidateCollectionView:] : 80 -> 20
~ -[LUILogFilterView predicatesComparisonCandidateCollectionView] : 16 -> 20
~ -[LUILogFilterView setPredicatesComparisonCandidateCollectionView:] : 80 -> 20
~ -[LUILogFilterView predicatesValueCandidateCollectionView] : 16 -> 20
~ -[LUILogFilterView setPredicatesValueCandidateCollectionView:] : 80 -> 20
~ -[LUILogFilterView horizontalSeparatorLine] : 16 -> 20
~ -[LUILogFilterView setHorizontalSeparatorLine:] : 80 -> 20
~ -[LUILogFilterView veriticalSeparatorLineFirst] : 16 -> 20
~ -[LUILogFilterView setVeriticalSeparatorLineFirst:] : 80 -> 20
~ -[LUILogFilterView veriticalSeparatorLineSecond] : 16 -> 20
~ -[LUILogFilterView setVeriticalSeparatorLineSecond:] : 80 -> 20
~ -[LUILogFilterView currentPredicateLabel] : 16 -> 20
~ -[LUILogFilterView setCurrentPredicateLabel:] : 80 -> 20
~ -[LUILogFilterView enterPredicateStackView] : 16 -> 20
~ -[LUILogFilterView setEnterPredicateStackView:] : 80 -> 20
~ -[LUILogFilterView addButton] : 16 -> 20
~ -[LUILogFilterView setAddButton:] : 80 -> 20
~ -[LUILogFilterView predicateTextField] : 16 -> 20
~ -[LUILogFilterView setPredicateTextField:] : 80 -> 20
~ -[LUILogFilterView applyButton] : 16 -> 20
~ -[LUILogFilterView setApplyButton:] : 80 -> 20
~ -[LUILogFilterViewController viewDidLoad] : 152 -> 144
~ -[LUILogFilterViewController viewDidAppear:] : 280 -> 260
~ -[LUILogFilterViewController viewDidDisappear:] : 104 -> 100
~ -[LUILogFilterViewController viewWillLayoutSubviews] : 212 -> 188
~ -[LUILogFilterViewController viewDidMoveToWindow:shouldAppearOrDisappear:] : 164 -> 152
~ -[LUILogFilterViewController _setupTableView] : 240 -> 216
~ -[LUILogFilterViewController _setupCollectionView] : 648 -> 568
~ -[LUILogFilterViewController _setupButtons] : 188 -> 172
~ -[LUILogFilterViewController predicateDataUpdated] : 96 -> 88
~ -[LUILogFilterViewController predicateKeyCandidates] : 84 -> 68
~ -[LUILogFilterViewController predicateComparisonCandidates] : 84 -> 68
~ -[LUILogFilterViewController predicateValueCandidates] : 84 -> 68
~ -[LUILogFilterViewController predicateValueCandidatesSize] : 176 -> 148
~ ___58-[LUILogFilterViewController predicateValueCandidatesSize]_block_invoke : 116 -> 108
~ -[LUILogFilterViewController sizeArrayWithStrings:] : 580 -> 568
~ -[LUILogFilterViewController _updatePredicateText] : 640 -> 600
~ ___50-[LUILogFilterViewController _updatePredicateText]_block_invoke : 368 -> 332
~ ___50-[LUILogFilterViewController _updatePredicateText]_block_invoke_2 : 288 -> 276
~ -[LUILogFilterViewController _clearCellsSelection] : 572 -> 544
~ -[LUILogFilterViewController _clearPredicateInput] : 108 -> 100
~ -[LUILogFilterViewController _shakeInputView:] : 340 -> 324
~ -[LUILogFilterViewController addButtonTapped:] : 1148 -> 1008
~ -[LUILogFilterViewController applyButtonTapped:] : 84 -> 80
~ -[LUILogFilterViewController collectionView:cellForItemAtIndexPath:] : 548 -> 488
~ -[LUILogFilterViewController collectionView:numberOfItemsInSection:] : 292 -> 256
~ -[LUILogFilterViewController collectionView:layout:sizeForItemAtIndexPath:] : 232 -> 220
~ -[LUILogFilterViewController tableView:cellForRowAtIndexPath:] : 272 -> 248
~ -[LUILogFilterViewController numberOfSectionsInTableView:] : 100 -> 92
~ -[LUILogFilterViewController tableView:numberOfRowsInSection:] : 100 -> 92
~ -[LUILogFilterViewController tableView:viewForFooterInSection:] : 104 -> 100
~ -[LUILogFilterViewController predicateTableViewCellDeleteButtonTapped:] : 276 -> 248
~ -[LUILogFilterViewController keyboardWillShow:] : 152 -> 144
~ -[LUILogFilterViewController keyboardWillHide:] : 148 -> 140
~ -[LUILogFilterViewController filterView] : 16 -> 20
~ -[LUILogFilterViewController setFilterView:] : 80 -> 20
~ -[LUILogScreenshotCollectionViewCell _setup] : 272 -> 260
~ -[LUILogScreenshotCollectionViewCell layoutSubviews] : 228 -> 240
~ -[LUILogScreenshotCollectionViewCell _createClearButton] : 152 -> 148
~ -[LUILogScreenshotCollectionViewCell _createScreenshotDateLabel] : 116 -> 112
~ -[LUILogScreenshotCollectionViewCell clearButtonTapped:] : 132 -> 124
~ -[LUILogScreenshotCollectionViewCell screenshotImageView] : 16 -> 20
~ -[LUILogScreenshotCollectionViewCell screenshotDateLabel] : 16 -> 20
~ -[LUILogScreenshotCollectionViewCell clearButton] : 16 -> 20
~ -[LUILogScreenshotCollectionViewCell clearButtonAction] : 16 -> 20
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<LUILogContentViewControllerDelegate>\""
- "@\"<LUILogFilterCurrentPredicateTableViewCellDelegate>\""
- "@\"<LUILogFilterViewControllerDelegate>\""
- "@\"<LUILogViewerControllerDelegate>\""
- "@\"<LUILogViewerViewDelegate>\""
- "@\"LUILogContentViewController\""
- "@\"LUILogFilterView\""
- "@\"LUILogFilterViewController\""
- "@\"LUILogLocatorView\""
- "@\"LUILogOptionsView\""
- "@\"LUILogViewerAssistiveTouch\""
- "@\"LUILogViewerView\""
- "@\"NSArray\""
- "@\"NSArray\"24@0:8@\"LUILogFilterViewController\"16"
- "@\"NSArray\"24@0:8@\"UICollectionView\"16"
- "@\"NSArray\"24@0:8@\"UITableView\"16"
- "@\"NSArray\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSDate\""
- "@\"NSDate\"24@0:8@\"LUILogContentViewController\"16"
- "@\"NSIndexPath\"24@0:8@\"UICollectionView\"16"
- "@\"NSIndexPath\"24@0:8@\"UITableView\"16"
- "@\"NSIndexPath\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSIndexPath\"40@0:8@\"UICollectionView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "@\"NSIndexPath\"40@0:8@\"UICollectionView\"16@\"NSString\"24q32"
- "@\"NSIndexPath\"40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "@\"NSIndexPath\"48@0:8@\"UICollectionView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32@\"NSIndexPath\"40"
- "@\"NSMutableArray\""
- "@\"NSMutableSet\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSString\"32@0:8@\"UITableView\"16q24"
- "@\"UIActivityIndicatorView\""
- "@\"UIButton\""
- "@\"UICollectionReusableView\"40@0:8@\"UICollectionView\"16@\"NSString\"24@\"NSIndexPath\"32"
- "@\"UICollectionView\""
- "@\"UICollectionViewCell\"32@0:8@\"UICollectionView\"16@\"NSIndexPath\"24"
- "@\"UICollectionViewTransitionLayout\"40@0:8@\"UICollectionView\"16@\"UICollectionViewLayout\"24@\"UICollectionViewLayout\"32"
- "@\"UIContextMenuConfiguration\"48@0:8@\"UICollectionView\"16@\"NSArray\"24{CGPoint=dd}32"
- "@\"UIContextMenuConfiguration\"48@0:8@\"UICollectionView\"16@\"NSIndexPath\"24{CGPoint=dd}32"
- "@\"UIContextMenuConfiguration\"48@0:8@\"UITableView\"16@\"NSIndexPath\"24{CGPoint=dd}32"
- "@\"UIImage\""
- "@\"UIImageView\""
- "@\"UILabel\""
- "@\"UIMenu\"40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSArray\"32"
- "@\"UIMenu\"48@0:8@\"UITextField\"16{_NSRange=QQ}24@\"NSArray\"40"
- "@\"UIPageViewController\""
- "@\"UIPanGestureRecognizer\""
- "@\"UISearchBar\""
- "@\"UIStackView\""
- "@\"UISwipeActionsConfiguration\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"UITableView\""
- "@\"UITableViewCell\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"UITargetedPreview\"32@0:8@\"UICollectionView\"16@\"UIContextMenuConfiguration\"24"
- "@\"UITargetedPreview\"32@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24"
- "@\"UITargetedPreview\"40@0:8@\"UICollectionView\"16@\"UIContextMenuConfiguration\"24@\"NSIndexPath\"32"
- "@\"UITextField\""
- "@\"UITextView\""
- "@\"UIView\""
- "@\"UIView\"24@0:8@\"UIScrollView\"16"
- "@\"UIView\"32@0:8@\"UITableView\"16q24"
- "@\"UIViewController\"32@0:8@\"UIPageViewController\"16@\"UIViewController\"24"
- "@\"UIWindowSceneActivationConfiguration\"48@0:8@\"UICollectionView\"16@\"NSIndexPath\"24{CGPoint=dd}32"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8d16"
- "@32@0:8:16@24"
- "@32@0:8@16:24"
- "@32@0:8@16@24"
- "@32@0:8@16d24"
- "@32@0:8@16q24"
- "@32@0:8q16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24@?32"
- "@40@0:8@16@24q32"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24{CGPoint=dd}32"
- "@48@0:8@16{_NSRange=QQ}24@40"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"LUILogFilterViewController\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"UIGestureRecognizer\"16"
- "B24@0:8@\"UIScrollView\"16"
- "B24@0:8@\"UISearchBar\"16"
- "B24@0:8@\"UITextField\"16"
- "B24@0:8@16"
- "B32@0:8@\"UICollectionView\"16@\"NSIndexPath\"24"
- "B32@0:8@\"UICollectionView\"16@\"UICollectionViewFocusUpdateContext\"24"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UIEvent\"24"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UIGestureRecognizer\"24"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UIPress\"24"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UITouch\"24"
- "B32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "B32@0:8@\"UITableView\"16@\"UITableViewFocusUpdateContext\"24"
- "B32@0:8@16@24"
- "B40@0:8@\"UICollectionView\"16@\"NSIndexPath\"24@\"<UISpringLoadedInteractionContext>\"32"
- "B40@0:8@\"UISearchBar\"16@\"NSArray\"24@\"NSString\"32"
- "B40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"<UISpringLoadedInteractionContext>\"32"
- "B40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSString\"32"
- "B40@0:8@16@24@32"
- "B48@0:8@\"UICollectionView\"16:24@\"NSIndexPath\"32@40"
- "B48@0:8@\"UISearchBar\"16{_NSRange=QQ}24@\"NSString\"40"
- "B48@0:8@\"UITableView\"16:24@\"NSIndexPath\"32@40"
- "B48@0:8@\"UITextField\"16{_NSRange=QQ}24@\"NSString\"40"
- "B48@0:8@16:24@32@40"
- "B48@0:8@16{_NSRange=QQ}24@40"
- "CGColor"
- "CGRectValue"
- "LUILogContentViewController"
- "LUILogContentViewControllerDelegate"
- "LUILogFilterCurrentPredicateTableViewCell"
- "LUILogFilterCurrentPredicateTableViewCellDelegate"
- "LUILogFilterPredicateCandidateCollectionViewCell"
- "LUILogFilterView"
- "LUILogFilterViewController"
- "LUILogFilterViewControllerDelegate"
- "LUILogLocatorView"
- "LUILogOptionsView"
- "LUILogScreenshotCollectionViewCell"
- "LUILogScreenshotItem"
- "LUILogViewerAssistiveTouch"
- "LUILogViewerController"
- "LUILogViewerPageViewController"
- "LUILogViewerView"
- "LUILogViewerViewDelegate"
- "LogViewerColor"
- "NSObject"
- "Q16@0:8"
- "Q24@0:8@\"UIPageViewController\"16"
- "Q24@0:8@16"
- "T#,R"
- "T@\"<LUILogContentViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<LUILogFilterCurrentPredicateTableViewCellDelegate>\",W,N,V_delegate"
- "T@\"<LUILogFilterViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<LUILogViewerControllerDelegate>\",W,N,V_delegate"
- "T@\"<LUILogViewerViewDelegate>\",W,N,V_delegate"
- "T@\"LUILogContentViewController\",&,N,V_logContentViewController"
- "T@\"LUILogFilterView\",&,N,V_filterView"
- "T@\"LUILogFilterViewController\",&,N,V_logFilterViewController"
- "T@\"LUILogLocatorView\",&,N,V_logLocatorView"
- "T@\"LUILogOptionsView\",&,N,V_logOptionsView"
- "T@\"LUILogViewerAssistiveTouch\",&,N,V_assistiveTouch"
- "T@\"LUILogViewerView\",&,N,V_logViewerView"
- "T@\"NSArray\",&,N,V_highlightRanges"
- "T@\"NSArray\",&,N,V_predicates"
- "T@\"NSArray\",&,N,V_screenshotItems"
- "T@\"NSDate\",&,N,V_firstLogDate"
- "T@\"NSDate\",&,N,V_lastLogDate"
- "T@\"NSDate\",&,N,V_screenshotDate"
- "T@\"NSMutableArray\",&,N,V_logMinutesArray"
- "T@\"NSMutableSet\",&,N,V_logMinutesSet"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"UIActivityIndicatorView\",&,N,V_spinner"
- "T@\"UIButton\",&,N,V_addButton"
- "T@\"UIButton\",&,N,V_applyButton"
- "T@\"UIButton\",&,N,V_clearButton"
- "T@\"UIButton\",&,N,V_closeButton"
- "T@\"UIButton\",&,N,V_downArrowButton"
- "T@\"UIButton\",&,N,V_filterButton"
- "T@\"UIButton\",&,N,V_halfHourButton"
- "T@\"UIButton\",&,N,V_hourButton"
- "T@\"UIButton\",&,N,V_lastDayButton"
- "T@\"UIButton\",&,N,V_leftCaretButton"
- "T@\"UIButton\",&,N,V_logButton"
- "T@\"UIButton\",&,N,V_rightCaretButton"
- "T@\"UIButton\",&,N,V_screenshotButton"
- "T@\"UIButton\",&,N,V_streamButton"
- "T@\"UIButton\",&,N,V_tenMinutesLogButton"
- "T@\"UIButton\",&,N,V_upArrowButton"
- "T@\"UIButton\",R,N,V_clearButton"
- "T@\"UIButton\",R,N,V_deleteButton"
- "T@\"UICollectionView\",&,N,V_predicatesComparisonCandidateCollectionView"
- "T@\"UICollectionView\",&,N,V_predicatesKeyCandidateCollectionView"
- "T@\"UICollectionView\",&,N,V_predicatesValueCandidateCollectionView"
- "T@\"UICollectionView\",&,N,V_screenshotCollectionView"
- "T@\"UIImage\",&,N,V_screenshotImage"
- "T@\"UIImageView\",R,N,V_screenshotImageView"
- "T@\"UILabel\",&,N,V_currentPredicateLabel"
- "T@\"UILabel\",&,N,V_scrollIndicatorView"
- "T@\"UILabel\",&,N,V_searchResultLabel"
- "T@\"UILabel\",R,N,V_screenshotDateLabel"
- "T@\"UILabel\",R,N,V_titleLabel"
- "T@\"UIPageViewController\",&,N,V_pageViewController"
- "T@\"UIPanGestureRecognizer\",&,N,V_panGesture"
- "T@\"UISearchBar\",&,N,V_searchBar"
- "T@\"UIStackView\",&,N,V_buttonStack"
- "T@\"UIStackView\",&,N,V_buttonStackView"
- "T@\"UIStackView\",&,N,V_enterPredicateStackView"
- "T@\"UITableView\",&,N,V_existingPredicatesTableView"
- "T@\"UITextField\",&,N,V_predicateTextField"
- "T@\"UITextView\",R,N,V_textView"
- "T@\"UIView\",&,N,V_contentHolderView"
- "T@\"UIView\",&,N,V_filterView"
- "T@\"UIView\",&,N,V_horizontalSeparatorLine"
- "T@\"UIView\",&,N,V_textViewHolderView"
- "T@\"UIView\",&,N,V_veriticalSeparatorLineFirst"
- "T@\"UIView\",&,N,V_veriticalSeparatorLineSecond"
- "T@\"UIView\",W,N,V_baseView"
- "T@?,C,N,V_clearButtonAction"
- "TB,N,V_isFetchingLogs"
- "TB,N,V_isStreaming"
- "TB,N,V_outsideKeyboardIsShowing"
- "TQ,R"
- "Td,N,V_logInterval"
- "Tq,N,V_currentHighlightIndex"
- "T{_NSRange=QQ},N,V_visibleRange"
- "UIBarPositioningDelegate"
- "UICollectionViewDataSource"
- "UICollectionViewDelegate"
- "UICollectionViewDelegateFlowLayout"
- "UIGestureRecognizerDelegate"
- "UIPageViewControllerDataSource"
- "UIPageViewControllerDelegate"
- "UIScrollViewDelegate"
- "UISearchBarDelegate"
- "UITableViewDataSource"
- "UITableViewDelegate"
- "UITextFieldDelegate"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_addButton"
- "_applyButton"
- "_applyScreenShotAnimation"
- "_assistiveTouch"
- "_attributedLogStringFrom:fontSize:"
- "_baseView"
- "_buttonStack"
- "_buttonStackView"
- "_canShowWhileLocked"
- "_cleanupHighlight"
- "_cleanupLogs"
- "_clearButton"
- "_clearButtonAction"
- "_clearCellsSelection"
- "_clearPredicateInput"
- "_closeButton"
- "_contentHolderView"
- "_createButtonStackView"
- "_createButtonWithImageName:"
- "_createButtonWithTitle:"
- "_createButtonWithTitle:action:"
- "_createClearButton"
- "_createCloseButton"
- "_createCollectionView"
- "_createCurrentPredicateLabel"
- "_createDeleteButton"
- "_createElementStackViewWithElements:"
- "_createEnterLabel"
- "_createEnterPredicateStackViewWithSubViews:"
- "_createFilterButton"
- "_createLeftCaretButton"
- "_createLogButton"
- "_createLogLocatorView"
- "_createLogOptionsView"
- "_createLogTextView"
- "_createPredicateTextField"
- "_createRightCaretButton"
- "_createScreenshotCollectionView"
- "_createScreenshotDateLabel"
- "_createScreenshotImageView"
- "_createSearchBar"
- "_createSearchResultLabel"
- "_createSeparatorLine"
- "_createTableView"
- "_createTitleLabel"
- "_currentHighlightIndex"
- "_currentPredicateLabel"
- "_dateWithPercentage:"
- "_decreaseCurrentHighlightIndex"
- "_delegate"
- "_deleteButton"
- "_deleteButtonTapped:"
- "_dismissLogViewerView"
- "_downArrowButton"
- "_enterPredicateStackView"
- "_existingPredicatesTableView"
- "_filterButton"
- "_filterView"
- "_firstLogDate"
- "_generateScreenshotItem"
- "_getLogsFromDate:predicate:duplicateHandler:"
- "_grabLogAndUpdateTextView"
- "_halfHourButton"
- "_highlightButton:highlight:"
- "_highlightRanges"
- "_horizontalSeparatorLine"
- "_hourButton"
- "_increaseCurrentHighlightIndex"
- "_isFetchingLogs"
- "_isStreaming"
- "_lastDayButton"
- "_lastLogDate"
- "_leftCaretButton"
- "_logButton"
- "_logContentViewController"
- "_logFilterViewController"
- "_logInterval"
- "_logLocatorView"
- "_logMinutesArray"
- "_logMinutesSet"
- "_logOptionsView"
- "_logViewerView"
- "_moveElementsToView:"
- "_outsideKeyboardIsShowing"
- "_pageViewController"
- "_panGesture"
- "_performSearch:"
- "_placeholderLabel"
- "_predicateTextField"
- "_predicates"
- "_predicatesComparisonCandidateCollectionView"
- "_predicatesKeyCandidateCollectionView"
- "_predicatesValueCandidateCollectionView"
- "_presentLogViewerView"
- "_rightCaretButton"
- "_screenshotButton"
- "_screenshotCollectionView"
- "_screenshotDate"
- "_screenshotDateLabel"
- "_screenshotImage"
- "_screenshotImageView"
- "_screenshotItems"
- "_scrollIndicatorView"
- "_searchBar"
- "_searchRangeForDate:inText:"
- "_searchResultLabel"
- "_setForcesClearButtonHighContrastAppearance:"
- "_setup"
- "_setupButtonActions"
- "_setupButtons"
- "_setupCollectionView"
- "_setupInitialHighlight"
- "_setupTableView"
- "_setupTextViewGesture"
- "_setupUI"
- "_shakeInputView:"
- "_spinner"
- "_startStreamLog"
- "_stopStreaming"
- "_streamButton"
- "_tenMinutesLogButton"
- "_textView"
- "_textViewHolderView"
- "_titleLabel"
- "_upArrowButton"
- "_updateHighlight"
- "_updateLogFromLastTime"
- "_updatePredicateText"
- "_veriticalSeparatorLineFirst"
- "_veriticalSeparatorLineSecond"
- "_visibleRange"
- "_visibleRangeOfTextView:"
- "_windowBounds"
- "activateStreamFromDate:"
- "addAnimation:forKey:"
- "addAttribute:value:range:"
- "addButton"
- "addButtonTapped:"
- "addGestureRecognizer:"
- "addObject:"
- "addObserver:forKeyPath:options:context:"
- "addObserver:selector:name:object:"
- "addSubview:"
- "addTarget:action:forControlEvents:"
- "alpha"
- "animateWithDuration:delay:usingSpringWithDamping:initialSpringVelocity:options:animations:completion:"
- "animationWithKeyPath:"
- "appendAttributedString:"
- "appendString:"
- "applyButton"
- "applyButtonTapped:"
- "arrayByAddingObject:"
- "arrayByAddingObjectsFromArray:"
- "arrayWithObjects:count:"
- "assistiveTouch"
- "assistiveTouchButtonTapped:"
- "autorelease"
- "baseView"
- "becomeFirstResponder"
- "beginEditing"
- "beginningOfDocument"
- "blackColor"
- "boldSystemFontOfSize:"
- "boundingRectWithSize:options:attributes:context:"
- "bounds"
- "bringSubviewToFront:"
- "buttonStack"
- "buttonStackView"
- "center"
- "characterRangeAtPoint:"
- "class"
- "clearButton"
- "clearButtonAction"
- "clearButtonTapped:"
- "clearColor"
- "clearScreenshots"
- "closeButton"
- "closeButtonTapped:"
- "collectionView:canEditItemAtIndexPath:"
- "collectionView:canFocusItemAtIndexPath:"
- "collectionView:canMoveItemAtIndexPath:"
- "collectionView:canPerformAction:forItemAtIndexPath:withSender:"
- "collectionView:canPerformPrimaryActionForItemAtIndexPath:"
- "collectionView:cellForItemAtIndexPath:"
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
- "collectionView:indexPathForIndexTitle:atIndex:"
- "collectionView:layout:insetForSectionAtIndex:"
- "collectionView:layout:minimumInteritemSpacingForSectionAtIndex:"
- "collectionView:layout:minimumLineSpacingForSectionAtIndex:"
- "collectionView:layout:referenceSizeForFooterInSection:"
- "collectionView:layout:referenceSizeForHeaderInSection:"
- "collectionView:layout:sizeForItemAtIndexPath:"
- "collectionView:moveItemAtIndexPath:toIndexPath:"
- "collectionView:numberOfItemsInSection:"
- "collectionView:performAction:forItemAtIndexPath:withSender:"
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
- "collectionView:viewForSupplementaryElementOfKind:atIndexPath:"
- "collectionView:willDisplayCell:forItemAtIndexPath:"
- "collectionView:willDisplayContextMenuWithConfiguration:animator:"
- "collectionView:willDisplaySupplementaryView:forElementKind:atIndexPath:"
- "collectionView:willEndContextMenuInteractionWithConfiguration:animator:"
- "collectionView:willPerformPreviewActionForMenuWithConfiguration:animator:"
- "collectionViewDidEndMultipleSelectionInteraction:"
- "collectionViewLayout"
- "colorWithAlphaComponent:"
- "compare:"
- "composedMessage"
- "conformsToProtocol:"
- "constraintEqualToConstant:"
- "containsObject:"
- "containsString:"
- "contentHolderView"
- "contentOffset"
- "contentSize"
- "contentView"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentHighlightIndex"
- "currentPredicateLabel"
- "currentPredicates:"
- "d"
- "d16@0:8"
- "d32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "d32@0:8@\"UITableView\"16q24"
- "d32@0:8@16@24"
- "d32@0:8@16q24"
- "d40@0:8@\"UICollectionView\"16@\"UICollectionViewLayout\"24q32"
- "d40@0:8@16@24q32"
- "darkGrayColor"
- "date"
- "dateWithTimeInterval:sinceDate:"
- "dateWithTimeIntervalSinceNow:"
- "dateWithTimeIntervalSinceReferenceDate:"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "delegate"
- "deleteButton"
- "dequeueReusableCellWithIdentifier:"
- "dequeueReusableCellWithReuseIdentifier:forIndexPath:"
- "description"
- "deselectItemAtIndexPath:animated:"
- "dictionaryWithObjects:forKeys:count:"
- "doubleValue"
- "downArrowButton"
- "downArrowButtonTapped:"
- "effectiveGeometry"
- "enableTimeConsumingOptions:"
- "end"
- "endEditing"
- "endEditing:"
- "enterPredicateStackView"
- "enumerateObjectsUsingBlock:"
- "existingPredicatesTableView"
- "filterButton"
- "filterButtonTapped:"
- "filterView"
- "fire"
- "firstLogDate"
- "firstObject"
- "frame"
- "gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:"
- "gestureRecognizer:shouldReceiveEvent:"
- "gestureRecognizer:shouldReceivePress:"
- "gestureRecognizer:shouldReceiveTouch:"
- "gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:"
- "gestureRecognizer:shouldRequireFailureOfGestureRecognizer:"
- "gestureRecognizerShouldBegin:"
- "grayColor"
- "halfHourButton"
- "handleOrientationChange:"
- "handlePan:"
- "hash"
- "heightAnchor"
- "highlightFilterButton:"
- "highlightLogButton:"
- "highlightRanges"
- "horizontalSeparatorLine"
- "hourButton"
- "imageNamed:"
- "imageView"
- "imageWithRenderingMode:"
- "indexOfObject:"
- "indexPathForCell:"
- "indexPathForPreferredFocusedViewInCollectionView:"
- "indexPathForPreferredFocusedViewInTableView:"
- "indexPathsForSelectedItems"
- "indexTitlesForCollectionView:"
- "init"
- "initWithActivityIndicatorStyle:"
- "initWithArrangedSubviews:"
- "initWithFrame:"
- "initWithFrame:collectionViewLayout:"
- "initWithFrame:style:"
- "initWithRed:green:blue:alpha:"
- "initWithSource:"
- "initWithString:attributes:"
- "initWithStyle:reuseIdentifier:"
- "initWithTarget:action:"
- "initWithTransitionStyle:navigationOrientation:options:"
- "interfaceOrientation"
- "invalidate"
- "invalidateLayout"
- "isEqual:"
- "isEqualToString:"
- "isFetchingLogs"
- "isFirstResponder"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isStreaming"
- "keyboardWillHide:"
- "keyboardWillShow:"
- "lastDayButton"
- "lastLogDate"
- "layer"
- "layoutManager"
- "layoutSubViews"
- "layoutSubviews"
- "leftCaretButton"
- "leftCaretButtonTapped:"
- "length"
- "lengthOfBytesUsingEncoding:"
- "lightGrayColor"
- "loadView"
- "localStore"
- "locationInView:"
- "logButton"
- "logButtonTapped:"
- "logContentViewController"
- "logContentViewController:didSelectDateForLog:"
- "logContentViewController:didSelectLogOptionWithTimeInterval:"
- "logContentViewControllerLogEndDate:"
- "logContentViewControllerLogStartDate:"
- "logCyanColor"
- "logFilterViewController"
- "logFilterViewController:didAddPredicates:"
- "logFilterViewController:didDeletePredicate:"
- "logFilterViewControllerApplyButtonTapped:"
- "logFilterViewControllerShouldAllowTextEditing:"
- "logInterval"
- "logLocatorView"
- "logMinutesArray"
- "logMinutesSet"
- "logOptionButtonTapped:"
- "logOptionsView"
- "logPurpleColor"
- "logViewerControllerDidCloseLogViewer:"
- "logViewerControllerDidOpenLogViewer:"
- "logViewerFilterButtonTapped:"
- "logViewerLeftCaretButtonTapped:"
- "logViewerRightCaretButtonTapped:"
- "logViewerView"
- "logViewerViewClearButtontapped:"
- "logViewerViewCloseButtonTapped:"
- "logViewerViewLogButtonTapped:"
- "logYellowColor"
- "lowercaseString"
- "mutableCopy"
- "numberOfSectionsInCollectionView:"
- "numberOfSectionsInTableView:"
- "numberWithDouble:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "observeValueForKeyPath:ofObject:change:context:"
- "offsetFromPosition:toPosition:"
- "orPredicateWithSubpredicates:"
- "orderedViewControllers"
- "outsideKeyboardIsShowing"
- "pageViewController"
- "pageViewController:didFinishAnimating:previousViewControllers:transitionCompleted:"
- "pageViewController:spineLocationForInterfaceOrientation:"
- "pageViewController:viewControllerAfterViewController:"
- "pageViewController:viewControllerBeforeViewController:"
- "pageViewController:willTransitionToViewControllers:"
- "pageViewControllerPreferredInterfaceOrientationForPresentation:"
- "pageViewControllerSupportedInterfaceOrientations:"
- "panGesture"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "positionForBar:"
- "predicateComparisonCandidates"
- "predicateDataUpdated"
- "predicateFormat"
- "predicateKeyCandidates"
- "predicateTableViewCellDeleteButtonTapped:"
- "predicateTextField"
- "predicateValueCandidates"
- "predicateValueCandidatesSize"
- "predicateWithFormat:"
- "predicatesComparisonCandidateCollectionView"
- "predicatesKeyCandidateCollectionView"
- "predicatesValueCandidateCollectionView"
- "prepareWithCompletionHandler:"
- "presentationCountForPageViewController:"
- "presentationIndexForPageViewController:"
- "processIdentifier"
- "q"
- "q16@0:8"
- "q24@0:8@\"<UIBarPositioning>\"16"
- "q24@0:8@\"UICollectionView\"16"
- "q24@0:8@\"UIPageViewController\"16"
- "q24@0:8@\"UITableView\"16"
- "q24@0:8@16"
- "q32@0:8@\"UICollectionView\"16q24"
- "q32@0:8@\"UIPageViewController\"16q24"
- "q32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "q32@0:8@\"UITableView\"16q24"
- "q32@0:8@16@24"
- "q32@0:8@16q24"
- "q40@0:8@\"UITableView\"16@\"NSString\"24q32"
- "q40@0:8@16@24q32"
- "rangeOfString:"
- "rangeOfString:options:range:locale:"
- "rangeValue"
- "registerClass:forCellReuseIdentifier:"
- "registerClass:forCellWithReuseIdentifier:"
- "release"
- "reloadData"
- "removeAllObjects"
- "removeAttribute:range:"
- "removeFromSuperview"
- "removeGestureRecognizer:"
- "removeObject:"
- "removeObserver:"
- "removeObserver:forKeyPath:"
- "renderInContext:"
- "resetSearchResultLabel"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "rightCaretButton"
- "rightCaretButtonTapped:"
- "row"
- "scheduledTimerWithTimeInterval:repeats:block:"
- "screen"
- "screenshotButton"
- "screenshotButtonTapped:"
- "screenshotCollectionView"
- "screenshotDate"
- "screenshotDateLabel"
- "screenshotImage"
- "screenshotImageView"
- "screenshotItems"
- "scrollIndicatorView"
- "scrollRangeToVisible:"
- "scrollViewDidChangeAdjustedContentInset:"
- "scrollViewDidEndDecelerating:"
- "scrollViewDidEndDragging:willDecelerate:"
- "scrollViewDidEndScrollingAnimation:"
- "scrollViewDidEndZooming:withView:atScale:"
- "scrollViewDidScroll:"
- "scrollViewDidScrollToTop:"
- "scrollViewDidZoom:"
- "scrollViewShouldScrollToTop:"
- "scrollViewWillBeginDecelerating:"
- "scrollViewWillBeginDragging:"
- "scrollViewWillBeginZooming:withView:"
- "scrollViewWillEndDragging:withVelocity:targetContentOffset:"
- "searchBar"
- "searchBar:selectedScopeButtonIndexDidChange:"
- "searchBar:shouldChangeTextInRange:replacementText:"
- "searchBar:shouldChangeTextInRanges:replacementText:"
- "searchBar:textDidChange:"
- "searchBarBookmarkButtonClicked:"
- "searchBarCancelButtonClicked:"
- "searchBarResultsListButtonClicked:"
- "searchBarSearchButtonClicked:"
- "searchBarShouldBeginEditing:"
- "searchBarShouldEndEditing:"
- "searchBarTextDidBeginEditing:"
- "searchBarTextDidEndEditing:"
- "searchResultLabel"
- "section"
- "sectionIndexTitlesForTableView:"
- "self"
- "setActive:"
- "setAddButton:"
- "setAlignment:"
- "setAllowsMultipleSelection:"
- "setAllowsNonContiguousLayout:"
- "setAllowsSelection:"
- "setAlpha:"
- "setApplyButton:"
- "setAssistiveTouch:"
- "setAttributedText:"
- "setAutocapitalizationType:"
- "setAutocorrectionType:"
- "setAutoresizingMask:"
- "setAutoreverses:"
- "setAxis:"
- "setBackgroundColor:"
- "setBarTintColor:"
- "setBaseView:"
- "setBorderColor:"
- "setBorderWidth:"
- "setButtonStack:"
- "setButtonStackView:"
- "setCenter:"
- "setClearButton:"
- "setClearButtonAction:"
- "setClearButtonMode:"
- "setClipsToBounds:"
- "setCloseButton:"
- "setCollectionViewLayout:"
- "setContentCompressionResistancePriority:forAxis:"
- "setContentHolderView:"
- "setContentHuggingPriority:forAxis:"
- "setContentMode:"
- "setCornerRadius:"
- "setCurrentHighlightIndex:"
- "setCurrentPredicateLabel:"
- "setDataSource:"
- "setDateFormat:"
- "setDelegate:"
- "setDistribution:"
- "setDownArrowButton:"
- "setDuration:"
- "setEditable:"
- "setEnabled:"
- "setEnterPredicateStackView:"
- "setEventHandler:"
- "setExistingPredicatesTableView:"
- "setFilterButton:"
- "setFilterPredicate:"
- "setFilterView:"
- "setFirstLogDate:"
- "setFlags:"
- "setFont:"
- "setFrame:"
- "setFromValue:"
- "setHalfHourButton:"
- "setHighlightRanges:"
- "setHorizontalSeparatorLine:"
- "setHourButton:"
- "setImage:"
- "setImage:forState:"
- "setIndicatorStyle:"
- "setInvalidationHandler:"
- "setIsFetchingLogs:"
- "setIsStreaming:"
- "setLastDayButton:"
- "setLastLogDate:"
- "setLeftCaretButton:"
- "setLeftView:"
- "setLeftViewMode:"
- "setLogButton:"
- "setLogContentViewController:"
- "setLogFilterViewController:"
- "setLogInterval:"
- "setLogLocatorView:"
- "setLogMinutesArray:"
- "setLogMinutesSet:"
- "setLogOptionsView:"
- "setLogViewerView:"
- "setOutsideKeyboardIsShowing:"
- "setPageViewController:"
- "setPanGesture:"
- "setPlaceholder:"
- "setPredicateTextField:"
- "setPredicates:"
- "setPredicatesComparisonCandidateCollectionView:"
- "setPredicatesKeyCandidateCollectionView:"
- "setPredicatesValueCandidateCollectionView:"
- "setRepeatCount:"
- "setRightCaretButton:"
- "setScreenshotButton:"
- "setScreenshotCollectionView:"
- "setScreenshotDate:"
- "setScreenshotImage:"
- "setScreenshotItems:"
- "setScrollDirection:"
- "setScrollIndicatorView:"
- "setSearchBar:"
- "setSearchResultLabel:"
- "setSelected:"
- "setSelectedRange:"
- "setSmartQuotesType:"
- "setSpacing:"
- "setSpellCheckingType:"
- "setSpinner:"
- "setStreamButton:"
- "setTenMinutesLogButton:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setTextViewHolderView:"
- "setTintColor:"
- "setTitle:forState:"
- "setTitleColor:forState:"
- "setToValue:"
- "setTransform:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setUpArrowButton:"
- "setUserInteractionEnabled:"
- "setVeriticalSeparatorLineFirst:"
- "setVeriticalSeparatorLineSecond:"
- "setView:"
- "setViewControllers:direction:animated:completion:"
- "setVisibleRange:"
- "setZPosition:"
- "setup"
- "sharedApplication"
- "showLogContentPage"
- "showLogFilterPage"
- "showLogOptionsView"
- "showLogTextView"
- "showSpinner:"
- "sizeArrayWithStrings:"
- "sizeToFit"
- "sortedArrayUsingComparator:"
- "spinner"
- "start"
- "startAnimating"
- "state"
- "stopAnimating"
- "streamButton"
- "string"
- "stringFromDate:"
- "stringWithFormat:"
- "superclass"
- "superview"
- "switchClearButtonTitle:"
- "systemFontOfSize:"
- "systemFontOfSize:weight:"
- "tableView:accessoryButtonTappedForRowWithIndexPath:"
- "tableView:accessoryTypeForRowWithIndexPath:"
- "tableView:canEditRowAtIndexPath:"
- "tableView:canFocusRowAtIndexPath:"
- "tableView:canMoveRowAtIndexPath:"
- "tableView:canPerformAction:forRowAtIndexPath:withSender:"
- "tableView:canPerformPrimaryActionForRowAtIndexPath:"
- "tableView:cellForRowAtIndexPath:"
- "tableView:commitEditingStyle:forRowAtIndexPath:"
- "tableView:contextMenuConfigurationForRowAtIndexPath:point:"
- "tableView:didBeginMultipleSelectionInteractionAtIndexPath:"
- "tableView:didDeselectRowAtIndexPath:"
- "tableView:didEndDisplayingCell:forRowAtIndexPath:"
- "tableView:didEndDisplayingFooterView:forSection:"
- "tableView:didEndDisplayingHeaderView:forSection:"
- "tableView:didEndEditingRowAtIndexPath:"
- "tableView:didHighlightRowAtIndexPath:"
- "tableView:didSelectRowAtIndexPath:"
- "tableView:didUnhighlightRowAtIndexPath:"
- "tableView:didUpdateFocusInContext:withAnimationCoordinator:"
- "tableView:editActionsForRowAtIndexPath:"
- "tableView:editingStyleForRowAtIndexPath:"
- "tableView:estimatedHeightForFooterInSection:"
- "tableView:estimatedHeightForHeaderInSection:"
- "tableView:estimatedHeightForRowAtIndexPath:"
- "tableView:heightForFooterInSection:"
- "tableView:heightForHeaderInSection:"
- "tableView:heightForRowAtIndexPath:"
- "tableView:indentationLevelForRowAtIndexPath:"
- "tableView:leadingSwipeActionsConfigurationForRowAtIndexPath:"
- "tableView:moveRowAtIndexPath:toIndexPath:"
- "tableView:numberOfRowsInSection:"
- "tableView:performAction:forRowAtIndexPath:withSender:"
- "tableView:performPrimaryActionForRowAtIndexPath:"
- "tableView:previewForDismissingContextMenuWithConfiguration:"
- "tableView:previewForHighlightingContextMenuWithConfiguration:"
- "tableView:sectionForSectionIndexTitle:atIndex:"
- "tableView:selectionFollowsFocusForRowAtIndexPath:"
- "tableView:shouldBeginMultipleSelectionInteractionAtIndexPath:"
- "tableView:shouldHighlightRowAtIndexPath:"
- "tableView:shouldIndentWhileEditingRowAtIndexPath:"
- "tableView:shouldShowMenuForRowAtIndexPath:"
- "tableView:shouldSpringLoadRowAtIndexPath:withContext:"
- "tableView:shouldUpdateFocusInContext:"
- "tableView:targetIndexPathForMoveFromRowAtIndexPath:toProposedIndexPath:"
- "tableView:titleForDeleteConfirmationButtonForRowAtIndexPath:"
- "tableView:titleForFooterInSection:"
- "tableView:titleForHeaderInSection:"
- "tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:"
- "tableView:viewForFooterInSection:"
- "tableView:viewForHeaderInSection:"
- "tableView:willBeginEditingRowAtIndexPath:"
- "tableView:willDeselectRowAtIndexPath:"
- "tableView:willDisplayCell:forRowAtIndexPath:"
- "tableView:willDisplayContextMenuWithConfiguration:animator:"
- "tableView:willDisplayFooterView:forSection:"
- "tableView:willDisplayHeaderView:forSection:"
- "tableView:willEndContextMenuInteractionWithConfiguration:animator:"
- "tableView:willPerformPreviewActionForMenuWithConfiguration:animator:"
- "tableView:willSelectRowAtIndexPath:"
- "tableViewDidEndMultipleSelectionInteraction:"
- "tenMinutesLogButton"
- "text"
- "textField:editMenuForCharactersInRange:suggestedActions:"
- "textField:editMenuForCharactersInRanges:suggestedActions:"
- "textField:insertInputSuggestion:"
- "textField:shouldChangeCharactersInRange:replacementString:"
- "textField:shouldChangeCharactersInRanges:replacementString:"
- "textField:willDismissEditMenuWithAnimator:"
- "textField:willPresentEditMenuWithAnimator:"
- "textFieldDidBeginEditing:"
- "textFieldDidChangeSelection:"
- "textFieldDidEndEditing:"
- "textFieldDidEndEditing:reason:"
- "textFieldShouldBeginEditing:"
- "textFieldShouldClear:"
- "textFieldShouldEndEditing:"
- "textFieldShouldReturn:"
- "textStorage"
- "textView"
- "textViewHolderView"
- "timeIntervalSinceDate:"
- "timeIntervalSinceReferenceDate"
- "titleLabel"
- "translationInView:"
- "type"
- "unixDate"
- "upArrowButton"
- "upArrowButtonTapped:"
- "updateSearchResultLabelWithTotalResult:currentIndex:"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"LUILogFilterCurrentPredicateTableViewCell\"16"
- "v24@0:8@\"LUILogFilterViewController\"16"
- "v24@0:8@\"LUILogViewerView\"16"
- "v24@0:8@\"UICollectionView\"16"
- "v24@0:8@\"UIScrollView\"16"
- "v24@0:8@\"UISearchBar\"16"
- "v24@0:8@\"UITableView\"16"
- "v24@0:8@\"UITextField\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@\"UIScrollView\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"LUILogContentViewController\"16@\"NSDate\"24"
- "v32@0:8@\"LUILogContentViewController\"16d24"
- "v32@0:8@\"LUILogFilterViewController\"16@\"NSArray\"24"
- "v32@0:8@\"LUILogFilterViewController\"16@\"NSPredicate\"24"
- "v32@0:8@\"UICollectionView\"16@\"NSIndexPath\"24"
- "v32@0:8@\"UIPageViewController\"16@\"NSArray\"24"
- "v32@0:8@\"UIScrollView\"16@\"UIView\"24"
- "v32@0:8@\"UISearchBar\"16@\"NSString\"24"
- "v32@0:8@\"UISearchBar\"16q24"
- "v32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "v32@0:8@\"UITextField\"16@\"<UIEditMenuInteractionAnimating>\"24"
- "v32@0:8@\"UITextField\"16@\"UIInputSuggestion\"24"
- "v32@0:8@\"UITextField\"16q24"
- "v32@0:8@16@24"
- "v32@0:8@16d24"
- "v32@0:8@16q24"
- "v32@0:8Q16Q24"
- "v32@0:8{_NSRange=QQ}16"
- "v40@0:8@\"UICollectionView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UICollectionView\"16@\"UICollectionViewCell\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UICollectionView\"16@\"UICollectionViewFocusUpdateContext\"24@\"UIFocusAnimationCoordinator\"32"
- "v40@0:8@\"UICollectionView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionAnimating>\"32"
- "v40@0:8@\"UICollectionView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionCommitAnimating>\"32"
- "v40@0:8@\"UIPageViewController\"16B24@\"NSArray\"28B36"
- "v40@0:8@\"UIScrollView\"16@\"UIView\"24d32"
- "v40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionAnimating>\"32"
- "v40@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionCommitAnimating>\"32"
- "v40@0:8@\"UITableView\"16@\"UITableViewCell\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UITableView\"16@\"UITableViewFocusUpdateContext\"24@\"UIFocusAnimationCoordinator\"32"
- "v40@0:8@\"UITableView\"16@\"UIView\"24q32"
- "v40@0:8@\"UITableView\"16q24@\"NSIndexPath\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24d32"
- "v40@0:8@16@24q32"
- "v40@0:8@16B24@28B36"
- "v40@0:8@16q24@32"
- "v48@0:8@\"UICollectionView\"16:24@\"NSIndexPath\"32@40"
- "v48@0:8@\"UICollectionView\"16@\"UICollectionReusableView\"24@\"NSString\"32@\"NSIndexPath\"40"
- "v48@0:8@\"UIScrollView\"16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v48@0:8@\"UITableView\"16:24@\"NSIndexPath\"32@40"
- "v48@0:8@16:24@32@40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32^v40"
- "v48@0:8@16{CGPoint=dd}24N^{CGPoint=dd}40"
- "valueWithBytes:objCType:"
- "valueWithCGPoint:"
- "valueWithRange:"
- "velocityInView:"
- "veriticalSeparatorLineFirst"
- "veriticalSeparatorLineSecond"
- "view"
- "viewControllers"
- "viewDidAppear:"
- "viewDidDisappear:"
- "viewDidLoad"
- "viewDidMoveToWindow:shouldAppearOrDisappear:"
- "viewForZoomingInScrollView:"
- "viewWillLayoutSubviews"
- "visibleRange"
- "whiteColor"
- "widthAnchor"
- "window"
- "windowScene"
- "zone"
- "{CGPoint=dd}40@0:8@\"UICollectionView\"16{CGPoint=dd}24"
- "{CGPoint=dd}40@0:8@16{CGPoint=dd}24"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGSize=dd}40@0:8@\"UICollectionView\"16@\"UICollectionViewLayout\"24@\"NSIndexPath\"32"
- "{CGSize=dd}40@0:8@\"UICollectionView\"16@\"UICollectionViewLayout\"24q32"
- "{CGSize=dd}40@0:8@16@24@32"
- "{CGSize=dd}40@0:8@16@24q32"
- "{UIEdgeInsets=dddd}40@0:8@\"UICollectionView\"16@\"UICollectionViewLayout\"24q32"
- "{UIEdgeInsets=dddd}40@0:8@16@24q32"
- "{_NSRange=\"location\"Q\"length\"Q}"
- "{_NSRange=QQ}16@0:8"
- "{_NSRange=QQ}24@0:8@16"
- "{_NSRange=QQ}32@0:8@16@24"

```
