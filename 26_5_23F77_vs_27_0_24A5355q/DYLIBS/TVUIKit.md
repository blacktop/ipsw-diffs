## TVUIKit

> `/System/Library/PrivateFrameworks/TVUIKit.framework/TVUIKit`

```diff

-171.50.2.0.0
-  __TEXT.__text: 0xaf64
-  __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_methlist: 0x1284
+182.0.0.0.0
+  __TEXT.__text: 0xa9e8
+  __TEXT.__objc_methlist: 0x1294
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x91b
+  __TEXT.__cstring: 0x935
   __TEXT.__ustring: 0x4a
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__unwind_info: 0x3e0
-  __TEXT.__objc_classname: 0x1b5
-  __TEXT.__objc_methname: 0x473a
-  __TEXT.__objc_methtype: 0x142f
-  __TEXT.__objc_stubs: 0x2be0
-  __DATA_CONST.__got: 0x220
+  __TEXT.__unwind_info: 0x360
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xb88
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__objc_selrefs: 0x1160
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x2a0
+  __DATA_CONST.__got: 0x220
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x1f40
   __AUTH_CONST.__objc_const: 0x1ba0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x12c
   __DATA.__data: 0x240

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 35D7AD8F-A163-3F98-8F35-3D66E0A15D7E
-  Functions: 319
-  Symbols:   1380
-  CStrings:  1379
+  UUID: B43D8F8F-14CF-3B1A-A9E2-8D52FA91F4E2
+  Functions: 320
+  Symbols:   1386
+  CStrings:  504
 
Symbols:
+ -[_TVCarouselView _focusedCell]
+ ___block_literal_global.13
+ ___block_literal_global.15
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_focusedCell
+ _objc_msgSend$focusedCell
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x4
+ _objc_retain_x5
- ___block_literal_global.14
- ___block_literal_global.16
- _objc_msgSend$focusedView
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
Functions:
~ +[TVUIKitUtilities TVUIKitBundle] : 84 -> 68
~ ___33+[TVUIKitUtilities TVUIKitBundle]_block_invoke : 76 -> 72
~ +[TVUIKitUtilities preferredGraphicsRenderFormat] : 164 -> 148
~ +[_TVContentRatingBadgeManager sharedInstance] : 84 -> 68
~ -[_TVContentRatingBadgeManager badgeForContentRating:drawUnknownRatingBadge:] : 152 -> 140
~ -[_TVContentRatingBadgeManager badgeForRatingLabel:inRatingSystem:drawUnknownRatingBadge:] : 404 -> 372
~ -[_TVContentRatingBadgeManager isTemplatedBadgeForContentRating:] : 76 -> 72
~ -[_TVContentRatingBadgeManager badgeDescriptors] : 2700 -> 2692
~ -[_TVContentRatingBadgeManager _badgeDescriptorForContentRating:] : 136 -> 124
~ -[_TVContentRatingBadgeManager _badgeDescriptorForRatingLabel:inRatingSystem:] : 156 -> 144
~ +[_TVContentRatingBadgeManager _badgeDescriptorLookupKeyWithRatingLabel:inRatingSystem:] : 196 -> 184
~ +[_TVContentRatingBadgeManager _cleanedRatingLabel:] : 188 -> 172
~ +[_TVContentRatingBadgeManager _addImageDescriptorToDictionary:ratingSystem:ratingLabel:resourceName:isTemplatedImage:] : 208 -> 212
~ +[_TVContentRatingBadgeManager _imageLookupKeyWithRatingLabel:inRatingSystem:] : 120 -> 112
~ -[_TVContentRatingBadgeManager setImageCache:] : 64 -> 12
~ -[_TVContentRatingBadgeManager setBadgeDescriptors:] : 64 -> 12
~ -[_TVContentRating initWithRatingSystem:ratingLabel:rank:ratingDescription:] : 176 -> 180
~ -[_TVContentRating initWithRatingSystemString:ratingLabel:rank:ratingDescription:] : 132 -> 136
~ -[_TVContentRating initWithStringRepresentation:] : 368 -> 344
~ -[_TVContentRating stringRepresentation] : 220 -> 216
~ -[_TVContentRating description] : 176 -> 164
~ -[_TVContentRating isEqual:] : 604 -> 560
~ -[_TVContentRating hash] : 128 -> 120
~ _TVUIKitLogObject : 84 -> 68
~ _TVUIKitLSMLogObject : 84 -> 68
~ -[NSMutableAttributedString(TVUIKitAdditions) tv_addLanguageAwareness:] : 2092 -> 2080
~ _AMPCFStringGetCharacterAtIndex : 436 -> 452
~ -[_TVContentRatingTextBadgeView initWithBaselineOffsetFromBottom:] : 472 -> 428
~ -[_TVContentRatingTextBadgeView initWithFrame:] : 116 -> 112
~ -[_TVContentRatingTextBadgeView contentRatingText] : 84 -> 76
~ -[_TVContentRatingTextBadgeView setContentRatingAttributedText:] : 112 -> 116
~ +[_TVContentRatingTextBadgeView _badgeImageWithAttributedRatingText:andColor:] : 288 -> 268
~ -[_TVContentRatingTextBadgeView drawRect:] : 200 -> 192
~ -[_TVContentRatingTextBadgeView firstBaselineAnchor] : 96 -> 88
~ -[_TVContentRatingTextBadgeView tintColorDidChange] : 112 -> 108
~ -[_TVContentRatingTextBadgeView _updateContentRatingAttributedText:] : 156 -> 148
~ -[_TVContentRatingTextBadgeView _intrinsicContentSize] : 100 -> 96
~ +[_TVContentRatingTextBadgeView _attributedRatingTextForText:color:] : 412 -> 400
~ +[_TVContentRatingTextBadgeView _badgeSizeForAttributedRatingText:] : 240 -> 228
~ +[_TVContentRatingTextBadgeView _drawBadgeWithAttributedRatingText:inContext:rect:color:] : 256 -> 248
~ -[_TVContentRatingTextBadgeView contentRatingAttributedText] : 16 -> 20
~ -[_TVContentRatingTextBadgeView contentGuide] : 16 -> 20
~ -[_TVContentRatingTextBadgeView setContentGuide:] : 80 -> 20
~ +[_TVContentRatingSystemUtilities ratingSystemForString:] : 208 -> 188
~ +[_TVContentRatingSystemUtilities stringForRatingSystem:] : 136 -> 124
~ +[_TVContentRatingSystemUtilities _ratingSystemLookUpDictionary] : 84 -> 68
~ ___64+[_TVContentRatingSystemUtilities _ratingSystemLookUpDictionary]_block_invoke : 176 -> 172
~ +[_TVContentRatingSystemUtilities _ratingSystemStringLookUpDictionary] : 84 -> 68
~ ___70+[_TVContentRatingSystemUtilities _ratingSystemStringLookUpDictionary]_block_invoke : 184 -> 180
~ +[_TVContentRatingSystemUtilities _cleanedRatingSystem:] : 144 -> 132
~ -[_TVFocusableTextView initWithFrame:] : 940 -> 948
~ ___38-[_TVFocusableTextView initWithFrame:]_block_invoke : 272 -> 260
~ -[_TVFocusableTextView setDescriptionTextColor:] : 128 -> 116
~ -[_TVFocusableTextView setDescriptionTextHighlightColor:] : 128 -> 116
~ -[_TVFocusableTextView setDescriptionTextAlignment:] : 32 -> 36
~ -[_TVFocusableTextView setBackgroundColor:] : 128 -> 116
~ -[_TVFocusableTextView setHighlightBackgroundColor:] : 128 -> 116
~ -[_TVFocusableTextView setFocusSizeIncrease:] : 48 -> 56
~ -[_TVFocusableTextView setPadding:] : 152 -> 156
~ -[_TVFocusableTextView setAlwaysShowBackground:] : 32 -> 36
~ -[_TVFocusableTextView _updateBackgroundColors] : 324 -> 344
~ -[_TVFocusableTextView _updateTextColorsIfNeeded] : 72 -> 76
~ -[_TVFocusableTextView _updateTextColorsForFocusState:] : 416 -> 412
~ -[_TVFocusableTextView layoutSubviews] : 912 -> 940
~ -[_TVFocusableTextView didUpdateFocusInContext:withAnimationCoordinator:] : 100 -> 96
~ -[_TVFocusableTextView sizeThatFits:] : 256 -> 268
~ -[_TVFocusableTextView setDescriptionText:] : 552 -> 564
~ ___43-[_TVFocusableTextView setDescriptionText:]_block_invoke : 280 -> 272
~ ___43-[_TVFocusableTextView setDescriptionText:]_block_invoke_2 : 236 -> 228
~ -[_TVFocusableTextView descriptionText] : 16 -> 20
~ -[_TVFocusableTextView setTrackHorizontal:] : 72 -> 80
~ -[_TVFocusableTextView _setNeedsTextSizeComputation] : 20 -> 24
~ -[_TVFocusableTextView _recomputeTextSizeIfNeeded] : 252 -> 256
~ -[_TVFocusableTextView _moreLabelExclusionPathFrame] : 168 -> 176
~ -[_TVFocusableTextView _moreLabelFrame] : 852 -> 844
~ -[_TVFocusableTextView pressesBegan:withEvent:] : 200 -> 204
~ -[_TVFocusableTextView tintColorDidChange] : 152 -> 148
~ -[_TVFocusableTextView gestureRecognizerShouldBegin:] : 124 -> 116
~ -[_TVFocusableTextView floatingContentView:isTransitioningFromState:toState:] : 56 -> 64
~ -[_TVFocusableTextView _selectButtonAction:] : 36 -> 40
~ -[_TVFocusableTextView _playButtonAction:] : 36 -> 40
~ -[_TVFocusableTextView descriptionTextColor] : 16 -> 20
~ -[_TVFocusableTextView descriptionTextHighlightColor] : 16 -> 20
~ -[_TVFocusableTextView descriptionTextAlignment] : 16 -> 20
~ -[_TVFocusableTextView highlightBackgroundColor] : 16 -> 20
~ -[_TVFocusableTextView isTextTruncating] : 16 -> 20
~ -[_TVFocusableTextView setTextTruncating:] : 16 -> 20
~ -[_TVFocusableTextView moreHighlightPadding] : 16 -> 20
~ -[_TVFocusableTextView setMoreHighlightPadding:] : 16 -> 20
~ -[_TVFocusableTextView moreLabelOnNewLine] : 16 -> 20
~ -[_TVFocusableTextView setMoreLabelOnNewLine:] : 16 -> 20
~ -[_TVFocusableTextView moreLabelTextColor] : 16 -> 20
~ -[_TVFocusableTextView setMoreLabelTextColor:] : 80 -> 20
~ -[_TVFocusableTextView moreLabelText] : 16 -> 20
~ -[_TVFocusableTextView setMoreLabelText:] : 80 -> 20
~ -[_TVFocusableTextView trackHorizontal] : 16 -> 20
~ -[_TVFocusableTextView alwaysShowBackground] : 16 -> 20
~ -[_TVFocusableTextView focusSizeIncrease] : 16 -> 20
~ -[_TVFocusableTextView isAlwaysFocusable] : 16 -> 20
~ -[_TVFocusableTextView setAlwaysFocusable:] : 16 -> 20
~ -[_TVFocusableTextView disableFocus] : 16 -> 20
~ -[_TVFocusableTextView setDisableFocus:] : 16 -> 20
~ -[_TVFocusableTextView selectionHandler] : 16 -> 20
~ -[_TVFocusableTextView playHandler] : 16 -> 20
~ -[_TVFocusableTextView descriptionTextView] : 16 -> 20
~ -[_TVFocusableTextView setDescriptionTextView:] : 80 -> 20
~ -[_TVFocusableTextView floatingView] : 16 -> 20
~ -[_TVFocusableTextView setFloatingView:] : 80 -> 20
~ -[_TVFocusableTextView backgroundView] : 16 -> 20
~ -[_TVFocusableTextView setBackgroundView:] : 80 -> 20
~ -[_TVFocusableTextView selectRecognizer] : 16 -> 20
~ -[_TVFocusableTextView setSelectRecognizer:] : 80 -> 20
~ -[_TVFocusableTextView playRecognizer] : 16 -> 20
~ -[_TVFocusableTextView setPlayRecognizer:] : 80 -> 20
~ -[_TVFocusableTextView moreLabel] : 16 -> 20
~ -[_TVFocusableTextView setMoreLabel:] : 80 -> 20
~ -[_TVFocusableTextView moreLabelTapGestureRecognizer] : 16 -> 20
~ -[_TVFocusableTextView needsTextSizeComputation] : 16 -> 20
~ -[_TVFocusableTextView setNeedsTextSizeComputation:] : 16 -> 20
~ -[_TVCarouselView initWithFrame:] : 1336 -> 1304
~ -[_TVCarouselView tv_setShowcaseFactor:] : 16 -> 20
~ -[_TVCarouselView setHeaderView:] : 168 -> 164
~ -[_TVCarouselView setScrollMode:] : 68 -> 76
~ -[_TVCarouselView setShowsPageControl:] : 324 -> 312
~ -[_TVCarouselView layoutSubviews] : 264 -> 272
~ -[_TVCarouselView _startContinuousScroll] : 340 -> 336
~ -[_TVCarouselView displayLinkDidFire:] : 372 -> 352
~ -[_TVCarouselView dealloc] : 116 -> 112
~ -[_TVCarouselView _collectionView] : 64 -> 20
~ -[_TVCarouselView _pageControlValueChanged:] : 108 -> 104
~ -[_TVCarouselView didMoveToWindow] : 116 -> 112
~ -[_TVCarouselView preferredFocusedView] : 64 -> 20
~ -[_TVCarouselView setSemanticContentAttribute:] : 92 -> 96
~ -[_TVCarouselView collectionView:numberOfItemsInSection:] : 224 -> 220
~ -[_TVCarouselView collectionView:cellForItemAtIndexPath:] : 236 -> 224
~ -[_TVCarouselView collectionView:shouldHighlightItemAtIndexPath:] : 140 -> 144
~ -[_TVCarouselView collectionView:didHighlightItemAtIndexPath:] : 152 -> 156
~ -[_TVCarouselView collectionView:didUnhighlightItemAtIndexPath:] : 152 -> 156
~ -[_TVCarouselView collectionView:shouldSelectItemAtIndexPath:] : 140 -> 144
~ -[_TVCarouselView collectionView:shouldDeselectItemAtIndexPath:] : 140 -> 144
~ -[_TVCarouselView collectionView:didSelectItemAtIndexPath:] : 152 -> 156
~ -[_TVCarouselView collectionView:didDeselectItemAtIndexPath:] : 152 -> 156
~ -[_TVCarouselView collectionView:willDisplayCell:forItemAtIndexPath:] : 360 -> 372
~ ___69-[_TVCarouselView collectionView:willDisplayCell:forItemAtIndexPath:]_block_invoke : 256 -> 236
~ ___74-[_TVCarouselView collectionView:didEndDisplayingCell:forItemAtIndexPath:]_block_invoke : 264 -> 244
~ -[_TVCarouselView shouldUpdateFocusInContext:] : 200 -> 208
~ -[_TVCarouselView scrollViewWillEndDragging:withVelocity:targetContentOffset:] : 428 -> 424
~ -[_TVCarouselView _handlePlayGesture:] : 268 -> 232
~ -[_TVCarouselView _cellForItemAtIndex:] : 116 -> 112
~ -[_TVCarouselView indexForCell:] : 200 -> 188
~ -[_TVCarouselView registerClass:forCellWithReuseIdentifier:] : 16 -> 20
~ -[_TVCarouselView registerNib:forCellWithReuseIdentifier:] : 16 -> 20
~ -[_TVCarouselView reloadData] : 356 -> 348
~ -[_TVCarouselView setInteritemSpacing:animated:] : 44 -> 48
~ -[_TVCarouselView setAutoscrollInterval:] : 64 -> 68
~ -[_TVCarouselView setUnitScrollDuration:] : 64 -> 68
~ -[_TVCarouselView setDelegate:] : 892 -> 888
~ -[_TVCarouselView visibleCells] : 16 -> 20
~ -[_TVCarouselView _centerItemAtPageIndex:animated:] : 212 -> 196
~ -[_TVCarouselView _centerCollectionViewCellIndex] : 48 -> 52
~ -[_TVCarouselView _numberOfCells] : 100 -> 104
~ -[_TVCarouselView calculateChangeSetForFocusedIndex:newDataSourceMap:indexesToRemove:indexesToAdd:indexesToReload:] : 872 -> 828
~ -[_TVCarouselView _focusItemAtIndex:] : 512 -> 496
~ ___68-[_TVCarouselView _setContentOffsetForCollectionViewIndex:animated:]_block_invoke : 148 -> 140
~ -[_TVCarouselView _updateCarouselWithDataSource:indicesToRemove:indicesToAdd:indicesToReload:] : 252 -> 276
~ ___94-[_TVCarouselView _updateCarouselWithDataSource:indicesToRemove:indicesToAdd:indicesToReload:]_block_invoke : 248 -> 236
~ ___94-[_TVCarouselView _updateCarouselWithDataSource:indicesToRemove:indicesToAdd:indicesToReload:]_block_invoke_2 : 228 -> 188
~ -[_TVCarouselView _prepareIndexMap:] : 524 -> 500
~ -[_TVCarouselView _contentOffsetXForCollectionViewIndex:] : 224 -> 220
~ -[_TVCarouselView _updateCollectionViewLayoutAnimated:] : 204 -> 220
~ -[_TVCarouselView _updateContentOffsetForFocusedIndex:animated:] : 348 -> 352
~ ___64-[_TVCarouselView _updateContentOffsetForFocusedIndex:animated:]_block_invoke : 156 -> 148
~ -[_TVCarouselView _animatePagedCenteringAnimated:animations:completion:] : 144 -> 148
~ -[_TVCarouselView _updateAutoScrollTimer] : 392 -> 332
~ -[_TVCarouselView _startAutoScrollTimer] : 324 -> 332
~ ___40-[_TVCarouselView _startAutoScrollTimer]_block_invoke : 180 -> 172
~ -[_TVCarouselView _stopAutoScrollTimer] : 260 -> 264
~ -[_TVCarouselView _updateIdleModeLayoutAttributes] : 488 -> 404
~ -[_TVCarouselView _previousItemIndexForIndexPath:] : 244 -> 232
~ -[_TVCarouselView _itemIndexForIndexPath:] : 164 -> 152
~ -[_TVCarouselView _updatePageControl] : 488 -> 456
+ -[_TVCarouselView _focusedCell]
~ -[_TVCarouselView interitemSpacing] : 16 -> 20
~ -[_TVCarouselView scrollMode] : 16 -> 20
~ -[_TVCarouselView autoscrollInterval] : 16 -> 20
~ -[_TVCarouselView unitScrollDuration] : 16 -> 20
~ -[_TVCarouselView headerView] : 16 -> 20
~ -[_TVCarouselView showcaseFactor] : 16 -> 20
~ -[_TVCarouselView setShowcaseFactor:] : 16 -> 20
~ -[_TVCarouselView shouldScaleOnIdleFocus] : 16 -> 20
~ -[_TVCarouselView setShouldScaleOnIdleFocus:] : 16 -> 20
~ -[_TVCarouselView showsPageControl] : 16 -> 20
~ -[_TVCarouselView pageControlMargin] : 16 -> 20
~ -[_TVCarouselView setPageControlMargin:] : 16 -> 20
~ -[_TVCarouselView collectionToDatasourceIndexMap] : 16 -> 20
~ -[_TVCarouselView setCollectionToDatasourceIndexMap:] : 80 -> 20
~ -[_TVCarouselView focusGuide] : 16 -> 20
~ -[_TVCarouselView setFocusGuide:] : 80 -> 20
~ -[_TVCarouselView displayLink] : 16 -> 20
~ -[_TVCarouselView setDisplayLink:] : 80 -> 20
~ -[_TVCarouselView previousDisplayLinkTimestamp] : 16 -> 20
~ -[_TVCarouselView setPreviousDisplayLinkTimestamp:] : 16 -> 20
~ -[_TVCarouselView offsetChangePerSecond] : 16 -> 20
~ -[_TVCarouselView setOffsetChangePerSecond:] : 16 -> 20
~ -[_TVCarouselView firstFocusChangeInInterval] : 16 -> 20
~ -[_TVCarouselView setFirstFocusChangeInInterval:] : 80 -> 20
~ -[_TVCarouselView pageControl] : 16 -> 20
~ -[_TVCarouselView setPageControl:] : 80 -> 20
~ -[_TVCarouselView focusThrottleTimeInterval] : 16 -> 20
~ -[_TVCarouselView setFocusThrottleTimeInterval:] : 16 -> 20
~ -[_TVCarouselCollectionViewLayout prepareLayout] : 460 -> 448
~ -[_TVCarouselCollectionViewLayout collectionViewContentSize] : 160 -> 156
~ -[_TVCarouselCollectionViewLayout layoutAttributesForItemAtIndexPath:] : 16 -> 20
~ -[_TVCarouselCollectionViewLayout _expectedNumberOfCells] : 232 -> 224
~ -[_TVCarouselCollectionViewLayout minimumInteritemSpacing] : 16 -> 20
~ -[_TVCarouselCollectionViewLayout setMinimumInteritemSpacing:] : 16 -> 20
~ -[_TVCarouselCollectionView _canScrollX] : 124 -> 120
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<TVCarouselViewDataSource>\""
- "@\"<TVCarouselViewDelegate>\""
- "@\"CADisplayLink\""
- "@\"NSArray\"24@0:8@\"UICollectionView\"16"
- "@\"NSAttributedString\""
- "@\"NSCache\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSIndexPath\""
- "@\"NSIndexPath\"24@0:8@\"UICollectionView\"16"
- "@\"NSIndexPath\"40@0:8@\"UICollectionView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "@\"NSIndexPath\"40@0:8@\"UICollectionView\"16@\"NSString\"24q32"
- "@\"NSIndexPath\"48@0:8@\"UICollectionView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32@\"NSIndexPath\"40"
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"UICollectionReusableView\"40@0:8@\"UICollectionView\"16@\"NSString\"24@\"NSIndexPath\"32"
- "@\"UICollectionViewCell\"32@0:8@\"UICollectionView\"16@\"NSIndexPath\"24"
- "@\"UICollectionViewTransitionLayout\"40@0:8@\"UICollectionView\"16@\"UICollectionViewLayout\"24@\"UICollectionViewLayout\"32"
- "@\"UIColor\""
- "@\"UIContextMenuConfiguration\"48@0:8@\"UICollectionView\"16@\"NSArray\"24{CGPoint=dd}32"
- "@\"UIContextMenuConfiguration\"48@0:8@\"UICollectionView\"16@\"NSIndexPath\"24{CGPoint=dd}32"
- "@\"UIFocusGuide\""
- "@\"UILabel\""
- "@\"UILayoutGuide\""
- "@\"UIPageControl\""
- "@\"UITapGestureRecognizer\""
- "@\"UITargetedPreview\"32@0:8@\"UICollectionView\"16@\"UIContextMenuConfiguration\"24"
- "@\"UITargetedPreview\"40@0:8@\"UICollectionView\"16@\"UIContextMenuConfiguration\"24@\"NSIndexPath\"32"
- "@\"UITextView\""
- "@\"UIView\""
- "@\"UIView\"24@0:8@\"UIScrollView\"16"
- "@\"UIVisualEffectView\""
- "@\"UIWindowSceneActivationConfiguration\"48@0:8@\"UICollectionView\"16@\"NSIndexPath\"24{CGPoint=dd}32"
- "@\"_TVCarouselCollectionView\""
- "@\"_UIFloatingContentView\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8d16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@28@0:8q16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@32@0:8@16q24"
- "@36@0:8@16q24B32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24q32"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24Q32@40"
- "@48@0:8@16@24{CGPoint=dd}32"
- "@48@0:8q16@24Q32@40"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"UIGestureRecognizer\"16"
- "B24@0:8@\"UIScrollView\"16"
- "B24@0:8@16"
- "B24@0:8q16"
- "B32@0:8@\"UICollectionView\"16@\"NSIndexPath\"24"
- "B32@0:8@\"UICollectionView\"16@\"UICollectionViewFocusUpdateContext\"24"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UIEvent\"24"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UIGestureRecognizer\"24"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UIPress\"24"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UITouch\"24"
- "B32@0:8@16@24"
- "B40@0:8@\"UICollectionView\"16@\"NSIndexPath\"24@\"<UISpringLoadedInteractionContext>\"32"
- "B40@0:8@16@24@32"
- "B48@0:8@\"UICollectionView\"16:24@\"NSIndexPath\"32@40"
- "B48@0:8@16:24@32@40"
- "B48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "NSObject"
- "Q"
- "Q16@0:8"
- "Q24@0:8@16"
- "T#,R"
- "T@\"<TVCarouselViewDataSource>\",W,N,V_dataSource"
- "T@\"<TVCarouselViewDelegate>\",W,N,V_delegate"
- "T@\"CADisplayLink\",&,N,V_displayLink"
- "T@\"NSArray\",R,C,N"
- "T@\"NSAttributedString\",&,N"
- "T@\"NSAttributedString\",C,N,V_contentRatingAttributedText"
- "T@\"NSCache\",&,N,V_imageCache"
- "T@\"NSDate\",&,N,V_firstFocusChangeInInterval"
- "T@\"NSDictionary\",&,N,V_badgeDescriptors"
- "T@\"NSDictionary\",&,N,V_collectionToDatasourceIndexMap"
- "T@\"NSString\",&,N,V_moreLabelText"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_ratingDescription"
- "T@\"NSString\",R,C,N,V_ratingLabel"
- "T@\"NSString\",R,C,N,V_resourceName"
- "T@\"UIColor\",&,N,V_descriptionTextColor"
- "T@\"UIColor\",&,N,V_descriptionTextHighlightColor"
- "T@\"UIColor\",&,N,V_highlightBackgroundColor"
- "T@\"UIColor\",&,N,V_moreLabelTextColor"
- "T@\"UIFocusGuide\",&,N,V_focusGuide"
- "T@\"UILabel\",&,N,V_moreLabel"
- "T@\"UILayoutGuide\",&,N,V_contentGuide"
- "T@\"UIPageControl\",&,N,V_pageControl"
- "T@\"UITapGestureRecognizer\",&,N,V_playRecognizer"
- "T@\"UITapGestureRecognizer\",&,N,V_selectRecognizer"
- "T@\"UITapGestureRecognizer\",R,N,V_moreLabelTapGestureRecognizer"
- "T@\"UITextView\",&,N,V_descriptionTextView"
- "T@\"UIView\",&,N,V_headerView"
- "T@\"UIVisualEffectView\",&,N,V_backgroundView"
- "T@\"_UIFloatingContentView\",&,N,V_floatingView"
- "T@?,C,N,V_playHandler"
- "T@?,C,N,V_selectionHandler"
- "TB,N,GisAlwaysFocusable,V_alwaysFocusable"
- "TB,N,GisTextTruncating,V_textTruncating"
- "TB,N,V_alwaysShowBackground"
- "TB,N,V_cachesImages"
- "TB,N,V_disableFocus"
- "TB,N,V_moreLabelOnNewLine"
- "TB,N,V_needsTextSizeComputation"
- "TB,N,V_shouldScaleOnIdleFocus"
- "TB,N,V_showsPageControl"
- "TB,N,V_trackHorizontal"
- "TB,R,N,GisExplicitContent"
- "TB,R,N,GisTemplatedImage,V_templatedImage"
- "TQ,N"
- "TQ,N,V_focusSizeIncrease"
- "TQ,N,V_scrollMode"
- "TQ,R"
- "TQ,R,N,V_rank"
- "TVUIKitAdditions"
- "TVUIKitBundle"
- "TVUIKitUtilities"
- "Td,N,V_autoscrollInterval"
- "Td,N,V_focusThrottleTimeInterval"
- "Td,N,V_interitemSpacing"
- "Td,N,V_minimumInteritemSpacing"
- "Td,N,V_moreHighlightPadding"
- "Td,N,V_offsetChangePerSecond"
- "Td,N,V_pageControlMargin"
- "Td,N,V_previousDisplayLinkTimestamp"
- "Td,N,V_showcaseFactor"
- "Td,N,V_unitScrollDuration"
- "Tq,N,V_descriptionTextAlignment"
- "Tq,R,N"
- "Tq,R,N,V_ratingSystem"
- "T{CGPoint=dd},N,V_focusDirection"
- "T{CGPoint=dd},N,V_targetContentOffset"
- "T{CGSize=dd},N,V_itemSize"
- "T{UIEdgeInsets=dddd},N,V_padding"
- "UICollectionViewDataSource"
- "UICollectionViewDelegate"
- "UIGestureRecognizerDelegate"
- "UIScrollViewDelegate"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TVCarouselCollectionView"
- "_TVCarouselCollectionViewLayout"
- "_TVCarouselView"
- "_TVContentRating"
- "_TVContentRatingBadgeDescriptor"
- "_TVContentRatingBadgeManager"
- "_TVContentRatingSystemUtilities"
- "_TVContentRatingTextBadgeView"
- "_TVFocusableTextView"
- "_UIFloatingContentViewDelegate"
- "_accessibilityHigherContrastTintColorForColor:"
- "_accessibilityReducedMotionNotification:"
- "_addImageDescriptorToDictionary:ratingSystem:ratingLabel:resourceName:isTemplatedImage:"
- "_alwaysFocusable"
- "_alwaysShowBackground"
- "_animatePagedCenteringAnimated:animations:completion:"
- "_applicationDidBecomeActiveNotification:"
- "_applicationDidEnterBackgroundNotification:"
- "_attributedRatingTextForText:color:"
- "_autoScrollTimer"
- "_autoscrollInterval"
- "_auxilliaryTextView"
- "_backgroundColor"
- "_backgroundView"
- "_badgeDescriptorForContentRating:"
- "_badgeDescriptorForRatingLabel:inRatingSystem:"
- "_badgeDescriptorLookupKeyWithRatingLabel:inRatingSystem:"
- "_badgeDescriptors"
- "_badgeImageWithAttributedRatingText:andColor:"
- "_badgeSizeForAttributedRatingText:"
- "_cachesImages"
- "_canScrollCarouselView"
- "_canScrollX"
- "_carouselViewFlags"
- "_cellForItemAtIndex:"
- "_centerCollectionViewCellIndex"
- "_centerItemAtPageIndex:animated:"
- "_centeringAnimationDuration"
- "_cleanedRatingLabel:"
- "_cleanedRatingSystem:"
- "_collectionToDatasourceIndexMap"
- "_collectionView"
- "_collectionViewLayoutItemSize"
- "_contentGuide"
- "_contentOffsetXForCollectionViewIndex:"
- "_contentRatingAttributedText"
- "_dataSource"
- "_delegate"
- "_descriptionTextAlignment"
- "_descriptionTextColor"
- "_descriptionTextHighlightColor"
- "_descriptionTextView"
- "_disableFocus"
- "_displayLink"
- "_drawBadgeWithAttributedRatingText:inContext:rect:color:"
- "_expectedNumberOfCells"
- "_firstFocusChangeInInterval"
- "_flags"
- "_floatingView"
- "_focusDirection"
- "_focusGuide"
- "_focusItemAtIndex:"
- "_focusSizeIncrease"
- "_focusThrottleTimeInterval"
- "_focusedIndexPath"
- "_handlePlayGesture:"
- "_headerView"
- "_highlightBackgroundColor"
- "_imageCache"
- "_imageForUnknownRatingLabel:"
- "_imageLookupKeyWithRatingLabel:inRatingSystem:"
- "_indexToDeque"
- "_interitemSpacing"
- "_intrinsicContentSize"
- "_isNaturallyRTL"
- "_isRatingSystemForMovies:"
- "_isRatingSystemForMusic:"
- "_isRatingSystemForTV:"
- "_itemIndexForIndexPath:"
- "_itemSize"
- "_layoutAttributesByIndexPath"
- "_minimumInteritemSpacing"
- "_moreHighlightPadding"
- "_moreLabel"
- "_moreLabelExclusionPathFrame"
- "_moreLabelFrame"
- "_moreLabelOnNewLine"
- "_moreLabelTapGestureRecognizer"
- "_moreLabelText"
- "_moreLabelTextColor"
- "_needsTextSizeComputation"
- "_numFocusChangesInInterval"
- "_numberOfCells"
- "_numberOfRealItemsForDataSource"
- "_offsetChangePerSecond"
- "_originalSelectionDuration"
- "_originalUnselectionDuration"
- "_padding"
- "_paddingEdgeInsets"
- "_pageControl"
- "_pageControlMargin"
- "_pageControlValueChanged:"
- "_playButtonAction:"
- "_playHandler"
- "_playRecognizer"
- "_prepareIndexMap:"
- "_previousCollectionToDatasourceIndexMap"
- "_previousDisplayLinkTimestamp"
- "_previousItemIndexForIndexPath:"
- "_rank"
- "_ratingDescription"
- "_ratingLabel"
- "_ratingSystem"
- "_ratingSystemLookUpDictionary"
- "_ratingSystemStringLookUpDictionary"
- "_recomputeTextSizeIfNeeded"
- "_resourceName"
- "_scrollMode"
- "_selectButtonAction:"
- "_selectRecognizer"
- "_selectionHandler"
- "_setContentOffsetForCollectionViewIndex:"
- "_setContentOffsetForCollectionViewIndex:animated:"
- "_setIdleModeLayoutAttributes:"
- "_setNeedsTextSizeComputation"
- "_setVisibleRectEdgeInsets:"
- "_setWantsUnderlineForAccessibilityButtonShapesEnabled:"
- "_shouldScaleOnIdleFocus"
- "_showcaseFactor"
- "_showsPageControl"
- "_startAutoScrollTimer"
- "_startContinuousScroll"
- "_stopAutoScrollTimer"
- "_stopContinuousScroll"
- "_targetContentOffset"
- "_templatedImage"
- "_textTruncating"
- "_trackHorizontal"
- "_unitScrollDuration"
- "_updateAutoScrollTimer"
- "_updateBackgroundColors"
- "_updateCarouselWithDataSource:indicesToRemove:indicesToAdd:indicesToReload:"
- "_updateCollectionViewLayout"
- "_updateCollectionViewLayoutAnimated:"
- "_updateContentForNewCenterIndex:"
- "_updateContentOffsetForFocusedIndex:animated:"
- "_updateContentRatingAttributedText:"
- "_updateIdleModeLayoutAttributes"
- "_updatePageControl"
- "_updateTextColorsForFocusState:"
- "_updateTextColorsIfNeeded"
- "_vibrantEffectView"
- "activateConstraints:"
- "addAttribute:value:range:"
- "addCoordinatedAnimations:completion:"
- "addGestureRecognizer:"
- "addLayoutGuide:"
- "addLayoutManager:"
- "addObject:"
- "addObserver:selector:name:object:"
- "addSubview:"
- "addTarget:action:forControlEvents:"
- "addTextContainer:"
- "addToRunLoop:forMode:"
- "allKeysForObject:"
- "allValues"
- "alpha"
- "alwaysFocusable"
- "alwaysShowBackground"
- "animateWithDuration:delay:options:animations:completion:"
- "anyObject"
- "appendFormat:"
- "appendString:"
- "applicationState"
- "array"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "attribute:atIndex:effectiveRange:"
- "attributedText"
- "attributesAtIndex:effectiveRange:"
- "autorelease"
- "autoscrollInterval"
- "backgroundView"
- "badgeDescriptors"
- "badgeForContentRating:drawUnknownRatingBadge:"
- "badgeForRatingLabel:inRatingSystem:drawUnknownRatingBadge:"
- "baseWritingDirection"
- "bezierPathWithRect:"
- "bezierPathWithRoundedRect:cornerRadius:"
- "blackColor"
- "bottomAnchor"
- "boundingRectWithSize:options:context:"
- "boundingRectWithWidth:lines:"
- "bounds"
- "bundleWithIdentifier:"
- "cachesImages"
- "calculateChangeSetForFocusedIndex:newDataSourceMap:indexesToRemove:indexesToAdd:indexesToReload:"
- "canBecomeFocused"
- "carouselView:cellForItemAtIndex:"
- "carouselView:didCenterItemAtIndex:"
- "carouselView:didDeselectItemAtIndex:"
- "carouselView:didEndDisplayingCell:forItemAtIndex:"
- "carouselView:didEndDisplayingItemAtIndex:"
- "carouselView:didFocusItemAtIndex:"
- "carouselView:didHighlightItemAtIndex:"
- "carouselView:didPlayItemAtIndex:"
- "carouselView:didSelectItemAtIndex:"
- "carouselView:didUnhighlightItemAtIndex:"
- "carouselView:shouldDeselectItemAtIndex:"
- "carouselView:shouldHighlightItemAtIndex:"
- "carouselView:shouldSelectItemAtIndex:"
- "carouselView:willDisplayCell:forItemAtIndex:"
- "carouselView:willDisplayItemAtIndex:"
- "carouselViewDidScroll:"
- "cellForItemAtIndexPath:"
- "center"
- "centerItemAtPageIndex:"
- "characterSetWithCharactersInString:"
- "class"
- "clearColor"
- "collectionToDatasourceIndexMap"
- "collectionView"
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
- "collectionViewContentSize"
- "collectionViewDidEndMultipleSelectionInteraction:"
- "collectionViewLayout"
- "colorWithAlphaComponent:"
- "componentsSeparatedByCharactersInSet:"
- "conformsToProtocol:"
- "constraintEqualToAnchor:"
- "constraintEqualToAnchor:constant:"
- "containsObject:"
- "contentGuide"
- "contentOffset"
- "contentRatingAttributedText"
- "contentRatingText"
- "contentView"
- "controlState"
- "copy"
- "cornerRadius"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentDevice"
- "currentMode"
- "currentPage"
- "currentRunLoop"
- "d"
- "d16@0:8"
- "d24@0:8q16"
- "dataSource"
- "date"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "defaultParagraphStyle"
- "delegate"
- "deleteItemsAtIndexPaths:"
- "dequeueReusableCellWithReuseIdentifier:forIndex:"
- "dequeueReusableCellWithReuseIdentifier:forIndexPath:"
- "descender"
- "description"
- "descriptionText"
- "descriptionTextAlignment"
- "descriptionTextColor"
- "descriptionTextHighlightColor"
- "descriptionTextView"
- "dictionaryWithCapacity:"
- "dictionaryWithObjects:forKeys:count:"
- "didMoveToWindow"
- "didUpdateFocusInContext:withAnimationCoordinator:"
- "disableFocus"
- "displayLink"
- "displayLinkDidFire:"
- "displayLinkWithTarget:selector:"
- "doesNotRecognizeSelector:"
- "drawAtPoint:"
- "drawRect:"
- "enumerateAttribute:inRange:options:usingBlock:"
- "enumerateLineFragmentsForGlyphRange:usingBlock:"
- "explicitContent"
- "firstBaselineAnchor"
- "firstFocusChangeInInterval"
- "firstObject"
- "floatingContentView:didFinishTransitioningToState:"
- "floatingContentView:isTransitioningFromState:toState:"
- "floatingView"
- "focusDirection"
- "focusGuide"
- "focusSizeIncrease"
- "focusThrottleTimeInterval"
- "focusedCell"
- "focusedView"
- "font"
- "formatForTraitCollection:"
- "frame"
- "gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:"
- "gestureRecognizer:shouldReceiveEvent:"
- "gestureRecognizer:shouldReceivePress:"
- "gestureRecognizer:shouldReceiveTouch:"
- "gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:"
- "gestureRecognizer:shouldRequireFailureOfGestureRecognizer:"
- "gestureRecognizerShouldBegin:"
- "hash"
- "headerView"
- "highlightBackgroundColor"
- "imageCache"
- "imageNamed:inBundle:"
- "imageWithRenderingMode:"
- "indexForCell:"
- "indexForPreferredCenteredViewInCarouselView:"
- "indexPathForCell:"
- "indexPathForItem:inSection:"
- "indexPathForPreferredFocusedViewInCollectionView:"
- "indexTitlesForCollectionView:"
- "init"
- "initWithAttributedString:"
- "initWithBaselineOffsetFromBottom:"
- "initWithFrame:"
- "initWithFrame:collectionViewLayout:"
- "initWithRatingSystem:explicitContent:"
- "initWithRatingSystem:ratingLabel:rank:ratingDescription:"
- "initWithRatingSystemString:ratingLabel:rank:ratingDescription:"
- "initWithResourceName:isTemplatedImage:"
- "initWithSize:"
- "initWithString:attributes:"
- "initWithStringRepresentation:"
- "initWithTarget:action:"
- "insertItemsAtIndexPaths:"
- "integerValue"
- "interactionState"
- "interitemSpacing"
- "intrinsicContentSize"
- "invalidate"
- "invalidateIntrinsicContentSize"
- "isAlwaysFocusable"
- "isDescendantOfView:"
- "isEqual:"
- "isEqualToString:"
- "isExplicitContent"
- "isFocused"
- "isJ42"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isTemplatedBadgeForContentRating:"
- "isTemplatedImage"
- "isTextTruncating"
- "isUserInteractionEnabled"
- "item"
- "itemSize"
- "lastBaselineAnchor"
- "layer"
- "layoutAttributesForCellWithIndexPath:"
- "layoutAttributesForElementsInRect:"
- "layoutAttributesForItemAtIndexPath:"
- "layoutBelowIfNeeded"
- "layoutSubviews"
- "leading"
- "leadingAnchor"
- "leftAnchor"
- "length"
- "lowercaseString"
- "mainScreen"
- "maximumNumberOfLines"
- "minimumInteritemSpacing"
- "minusSet:"
- "moreHighlightPadding"
- "moreLabel"
- "moreLabelOnNewLine"
- "moreLabelTapGestureRecognizer"
- "moreLabelText"
- "moreLabelTextColor"
- "mutableCopy"
- "needsTextSizeComputation"
- "new"
- "nextFocusedView"
- "numberOfGlyphs"
- "numberOfItemsInCarouselView:"
- "numberOfItemsInSection:"
- "numberOfSectionsInCollectionView:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectAtIndex:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "offsetChangePerSecond"
- "padding"
- "pageControl"
- "pageControlMargin"
- "performBatchUpdates:completion:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performWithoutAnimation:"
- "playHandler"
- "playRecognizer"
- "preferredFocusedView"
- "preferredFontForTextStyle:"
- "preferredGraphicsRenderFormat"
- "prepareLayout"
- "pressesBegan:withEvent:"
- "previousDisplayLinkTimestamp"
- "q16@0:8"
- "q24@0:8@\"UICollectionView\"16"
- "q24@0:8@16"
- "q24@0:8q16"
- "q32@0:8@\"UICollectionView\"16q24"
- "q32@0:8@16q24"
- "raise:format:"
- "rank"
- "ratingDescription"
- "ratingLabel"
- "ratingSystem"
- "ratingSystemForString:"
- "ratingSystemKind"
- "ratingSystemKindForRatingSystem:"
- "ratingSystemString"
- "registerClass:forCellWithReuseIdentifier:"
- "registerNib:forCellWithReuseIdentifier:"
- "release"
- "reloadData"
- "reloadItemsAtIndexPaths:"
- "removeAttribute:range:"
- "removeFromSuperview"
- "removeObserver:"
- "replaceCharactersInRange:withString:"
- "resourceName"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "rightAnchor"
- "scale"
- "scrollMode"
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
- "selectRecognizer"
- "selectionHandler"
- "self"
- "set"
- "setActive:"
- "setAdjustsFontForContentSizeCategory:"
- "setAlignment:"
- "setAllowedPressTypes:"
- "setAlpha:"
- "setAlwaysFocusable:"
- "setAlwaysShowBackground:"
- "setAttributedText:"
- "setAutoresizingMask:"
- "setAutoscrollInterval:"
- "setBackgroundColor:"
- "setBackgroundColor:forState:"
- "setBackgroundView:"
- "setBadgeDescriptors:"
- "setBaseWritingDirection:"
- "setCachesImages:"
- "setClipsToBounds:"
- "setCollectionToDatasourceIndexMap:"
- "setCollectionViewLayout:animated:"
- "setContentGuide:"
- "setContentMotionRotation:translation:"
- "setContentOffset:animated:"
- "setContentRatingAttributedText:"
- "setContentRatingText:"
- "setControlState:animated:"
- "setCornerRadius:"
- "setCountLimit:"
- "setCurrentPage:"
- "setDataSource:"
- "setDelegate:"
- "setDescriptionText:"
- "setDescriptionTextAlignment:"
- "setDescriptionTextColor:"
- "setDescriptionTextHighlightColor:"
- "setDescriptionTextView:"
- "setDisableFocus:"
- "setDisplayLink:"
- "setEditable:"
- "setExclusionPaths:"
- "setFirstFocusChangeInInterval:"
- "setFloatingContentDelegate:"
- "setFloatingView:"
- "setFocusDirection:"
- "setFocusGuide:"
- "setFocusSizeIncrease:"
- "setFocusThrottleTimeInterval:"
- "setFocusedSizeIncrease:"
- "setFont:"
- "setFrame:"
- "setHeaderView:"
- "setHidden:"
- "setHidesForSinglePage:"
- "setHighlightBackgroundColor:"
- "setImageCache:"
- "setInteritemSpacing:"
- "setInteritemSpacing:animated:"
- "setItemSize:"
- "setLineBreakMode:"
- "setLineWidth:"
- "setMaximumNumberOfLines:"
- "setMinimumInteritemSpacing:"
- "setMoreHighlightPadding:"
- "setMoreLabel:"
- "setMoreLabelOnNewLine:"
- "setMoreLabelText:"
- "setMoreLabelTextColor:"
- "setName:"
- "setNeedsDisplay"
- "setNeedsFocusUpdate"
- "setNeedsLayout"
- "setNeedsTextSizeComputation:"
- "setNumberOfPages:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOffsetChangePerSecond:"
- "setOpaque:"
- "setPadding:"
- "setPageControl:"
- "setPageControlMargin:"
- "setPlayHandler:"
- "setPlayRecognizer:"
- "setPreferredFocusEnvironments:"
- "setPreviousDisplayLinkTimestamp:"
- "setScrollEnabled:"
- "setScrollMode:"
- "setSelectRecognizer:"
- "setSelectable:"
- "setSelected:animated:"
- "setSelected:animated:withAnimationCoordinator:"
- "setSelectionHandler:"
- "setSemanticContentAttribute:"
- "setShouldScaleOnIdleFocus:"
- "setShowcaseFactor:"
- "setShowsHorizontalScrollIndicator:"
- "setShowsPageControl:"
- "setShowsVerticalScrollIndicator:"
- "setTargetContentOffset:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setTextContainerInset:"
- "setTextTruncating:"
- "setTrackHorizontal:"
- "setTransform:"
- "setUnitScrollDuration:"
- "setUserInteractionEnabled:"
- "setWithArray:"
- "setZIndex:"
- "sharedApplication"
- "sharedInstance"
- "shouldInvalidateLayoutForBoundsChange:"
- "shouldScaleOnIdleFocus"
- "shouldUpdateFocusInContext:"
- "showcaseFactor"
- "showsPageControl"
- "sizeForNumberOfPages:"
- "sizeThatFits:"
- "sizeToFit"
- "state"
- "string"
- "stringByAppendingString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringForRatingSystem:"
- "stringRepresentation"
- "stringWithFormat:"
- "stroke"
- "superclass"
- "systemFontOfSize:weight:"
- "systemMidGrayColor"
- "targetContentOffset"
- "targetTimestamp"
- "templatedImage"
- "text"
- "textContainer"
- "textContainerInset"
- "textTruncating"
- "timeIntervalSinceDate:"
- "timestamp"
- "tintAdjustmentMode"
- "tintColor"
- "tintColorDidChange"
- "topAnchor"
- "trackHorizontal"
- "trailingAnchor"
- "traitCollection"
- "tv_addLanguageAwareness:"
- "tv_paragraphStyleWithBaseWritingDirection:"
- "tv_setShowcaseFactor:"
- "type"
- "unitScrollDuration"
- "unsignedIntegerValue"
- "userInterfaceIdiom"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"UICollectionView\"16"
- "v24@0:8@\"UIScrollView\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8B16B20"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@\"UIScrollView\"16B24"
- "v28@0:8@16B24"
- "v28@0:8d16B24"
- "v28@0:8q16B24"
- "v32@0:8#16@24"
- "v32@0:8@\"UICollectionView\"16@\"NSIndexPath\"24"
- "v32@0:8@\"UIScrollView\"16@\"UIView\"24"
- "v32@0:8@\"_UIFloatingContentView\"16Q24"
- "v32@0:8@16@24"
- "v32@0:8@16Q24"
- "v32@0:8B16B20@24"
- "v32@0:8{CGPoint=dd}16"
- "v32@0:8{CGSize=dd}16"
- "v36@0:8B16@?20@?28"
- "v40@0:8@\"UICollectionView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UICollectionView\"16@\"UICollectionViewCell\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UICollectionView\"16@\"UICollectionViewFocusUpdateContext\"24@\"UIFocusAnimationCoordinator\"32"
- "v40@0:8@\"UICollectionView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionAnimating>\"32"
- "v40@0:8@\"UICollectionView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionCommitAnimating>\"32"
- "v40@0:8@\"UIScrollView\"16@\"UIView\"24d32"
- "v40@0:8@\"_UIFloatingContentView\"16Q24Q32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24d32"
- "v40@0:8@16Q24Q32"
- "v48@0:8@\"UICollectionView\"16:24@\"NSIndexPath\"32@40"
- "v48@0:8@\"UICollectionView\"16@\"UICollectionReusableView\"24@\"NSString\"32@\"NSIndexPath\"40"
- "v48@0:8@\"UIScrollView\"16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v48@0:8@16:24@32@40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "v48@0:8{UIEdgeInsets=dddd}16"
- "v52@0:8@16q24@32@40B48"
- "v56@0:8q16@24N^@32N^@40N^@48"
- "v72@0:8@16^{CGContext=}24{CGRect={CGPoint=dd}{CGSize=dd}}32@64"
- "viewForZoomingInScrollView:"
- "visibleCells"
- "visualEffectContainerView"
- "window"
- "zone"
- "{?=\"delegateWasNonNil\"b1\"delegateShouldHighlightItemAtIndex\"b1\"delegateDidHighlightItemAtIndex\"b1\"delegateDidUnhighlightItemAtIndex\"b1\"delegateShouldSelectItemAtIndex\"b1\"delegateShouldDeselectItemAtIndex\"b1\"delegateDidSelectItemAtIndex\"b1\"delegateDidDeselectItemAtIndex\"b1\"delegateWillDisplayCellForItemAtIndex\"b1\"delegateDidEndDisplayingCellForItemAtIndex\"b1\"delegateCarouselViewDidScroll\"b1\"delegateDidFocusItemAtIndex\"b1\"delegateDidPlayItemAtIndex\"b1\"delegateWillDisplayItemAtIndex\"b1\"delegateDidEndDisplayingItemAtIndex\"b1\"delegateIndexForPreferredCenteredView\"b1\"delegateDidCenterItemAtIndex\"b1}"
- "{?=\"layoutUpdateInProgress\"B\"firstLayoutPass\"B}"
- "{CGPoint=\"x\"d\"y\"d}"
- "{CGPoint=dd}16@0:8"
- "{CGPoint=dd}40@0:8@\"UICollectionView\"16{CGPoint=dd}24"
- "{CGPoint=dd}40@0:8@16{CGPoint=dd}24"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGRect={CGPoint=dd}{CGSize=dd}}32@0:8d16Q24"
- "{CGSize=\"width\"d\"height\"d}"
- "{CGSize=dd}16@0:8"
- "{CGSize=dd}24@0:8@16"
- "{CGSize=dd}32@0:8{CGSize=dd}16"
- "{UIEdgeInsets=\"top\"d\"left\"d\"bottom\"d\"right\"d}"
- "{UIEdgeInsets=dddd}16@0:8"

```
