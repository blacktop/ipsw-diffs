## TVUIKit

> `/System/Library/PrivateFrameworks/TVUIKit.framework/TVUIKit`

```diff

-171.30.1.0.0
-  __TEXT.__text: 0xa61c
-  __TEXT.__auth_stubs: 0x550
+171.40.5.0.0
+  __TEXT.__text: 0xaf64
+  __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_methlist: 0x1284
   __TEXT.__const: 0x70
   __TEXT.__cstring: 0x91b
   __TEXT.__ustring: 0x4a
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__unwind_info: 0x368
+  __TEXT.__unwind_info: 0x3e0
   __TEXT.__objc_classname: 0x1b5
   __TEXT.__objc_methname: 0x473a
   __TEXT.__objc_methtype: 0x142f

   __DATA_CONST.__objc_selrefs: 0x1160
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x2b8
+  __AUTH_CONST.__auth_got: 0x2a0
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x1f40
   __AUTH_CONST.__objc_const: 0x1ba0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CB878D1C-9FE3-3871-A587-5EC46D283AA8
+  UUID: 65251FF6-BD21-38C3-AA74-7CD030F81634
   Functions: 319
-  Symbols:   1383
+  Symbols:   1380
   CStrings:  1379
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x27
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x4
- _objc_retain_x5
Functions:
~ +[TVUIKitUtilities TVUIKitBundle] : 68 -> 84
~ ___33+[TVUIKitUtilities TVUIKitBundle]_block_invoke : 72 -> 76
~ +[TVUIKitUtilities preferredGraphicsRenderFormat] : 148 -> 164
~ +[_TVContentRatingBadgeManager sharedInstance] : 68 -> 84
~ -[_TVContentRatingBadgeManager badgeForContentRating:drawUnknownRatingBadge:] : 140 -> 152
~ -[_TVContentRatingBadgeManager badgeForRatingLabel:inRatingSystem:drawUnknownRatingBadge:] : 372 -> 404
~ -[_TVContentRatingBadgeManager isTemplatedBadgeForContentRating:] : 72 -> 76
~ -[_TVContentRatingBadgeManager badgeDescriptors] : 2692 -> 2700
~ -[_TVContentRatingBadgeManager _badgeDescriptorForContentRating:] : 124 -> 136
~ -[_TVContentRatingBadgeManager _badgeDescriptorForRatingLabel:inRatingSystem:] : 144 -> 156
~ +[_TVContentRatingBadgeManager _badgeDescriptorLookupKeyWithRatingLabel:inRatingSystem:] : 184 -> 196
~ +[_TVContentRatingBadgeManager _cleanedRatingLabel:] : 172 -> 188
~ +[_TVContentRatingBadgeManager _addImageDescriptorToDictionary:ratingSystem:ratingLabel:resourceName:isTemplatedImage:] : 212 -> 208
~ +[_TVContentRatingBadgeManager _imageLookupKeyWithRatingLabel:inRatingSystem:] : 112 -> 120
~ -[_TVContentRatingBadgeManager setImageCache:] : 12 -> 64
~ -[_TVContentRatingBadgeManager setBadgeDescriptors:] : 12 -> 64
~ -[_TVContentRating initWithRatingSystem:ratingLabel:rank:ratingDescription:] : 180 -> 176
~ -[_TVContentRating initWithRatingSystemString:ratingLabel:rank:ratingDescription:] : 136 -> 132
~ -[_TVContentRating initWithStringRepresentation:] : 344 -> 368
~ -[_TVContentRating stringRepresentation] : 216 -> 220
~ -[_TVContentRating description] : 164 -> 176
~ -[_TVContentRating isEqual:] : 560 -> 604
~ -[_TVContentRating hash] : 120 -> 128
~ _TVUIKitLogObject : 68 -> 84
~ _TVUIKitLSMLogObject : 68 -> 84
~ -[NSMutableAttributedString(TVUIKitAdditions) tv_addLanguageAwareness:] : 2088 -> 2092
~ -[_TVContentRatingTextBadgeView initWithBaselineOffsetFromBottom:] : 424 -> 472
~ -[_TVContentRatingTextBadgeView initWithFrame:] : 112 -> 116
~ -[_TVContentRatingTextBadgeView contentRatingText] : 76 -> 84
~ +[_TVContentRatingTextBadgeView _badgeImageWithAttributedRatingText:andColor:] : 268 -> 288
~ -[_TVContentRatingTextBadgeView drawRect:] : 192 -> 200
~ -[_TVContentRatingTextBadgeView tintColorDidChange] : 108 -> 112
~ -[_TVContentRatingTextBadgeView _updateContentRatingAttributedText:] : 148 -> 156
~ -[_TVContentRatingTextBadgeView _intrinsicContentSize] : 96 -> 100
~ +[_TVContentRatingTextBadgeView _attributedRatingTextForText:color:] : 400 -> 412
~ +[_TVContentRatingTextBadgeView _badgeSizeForAttributedRatingText:] : 228 -> 240
~ +[_TVContentRatingTextBadgeView _drawBadgeWithAttributedRatingText:inContext:rect:color:] : 248 -> 256
~ -[_TVContentRatingTextBadgeView setContentGuide:] : 20 -> 80
~ +[_TVContentRatingSystemUtilities ratingSystemForString:] : 188 -> 208
~ +[_TVContentRatingSystemUtilities stringForRatingSystem:] : 124 -> 136
~ +[_TVContentRatingSystemUtilities _ratingSystemLookUpDictionary] : 68 -> 84
~ ___64+[_TVContentRatingSystemUtilities _ratingSystemLookUpDictionary]_block_invoke : 172 -> 176
~ +[_TVContentRatingSystemUtilities _ratingSystemStringLookUpDictionary] : 68 -> 84
~ ___70+[_TVContentRatingSystemUtilities _ratingSystemStringLookUpDictionary]_block_invoke : 180 -> 184
~ +[_TVContentRatingSystemUtilities _cleanedRatingSystem:] : 132 -> 144
~ -[_TVFocusableTextView initWithFrame:] : 908 -> 940
~ ___38-[_TVFocusableTextView initWithFrame:]_block_invoke : 260 -> 272
~ -[_TVFocusableTextView setDescriptionTextColor:] : 112 -> 128
~ -[_TVFocusableTextView setDescriptionTextHighlightColor:] : 112 -> 128
~ -[_TVFocusableTextView setBackgroundColor:] : 112 -> 128
~ -[_TVFocusableTextView setHighlightBackgroundColor:] : 112 -> 128
~ -[_TVFocusableTextView _updateBackgroundColors] : 320 -> 324
~ -[_TVFocusableTextView _updateTextColorsForFocusState:] : 392 -> 416
~ -[_TVFocusableTextView layoutSubviews] : 892 -> 912
~ -[_TVFocusableTextView didUpdateFocusInContext:withAnimationCoordinator:] : 96 -> 100
~ -[_TVFocusableTextView canBecomeFocused] : 148 -> 152
~ -[_TVFocusableTextView sizeThatFits:] : 248 -> 256
~ -[_TVFocusableTextView setDescriptionText:] : 556 -> 552
~ ___43-[_TVFocusableTextView setDescriptionText:]_block_invoke : 272 -> 280
~ ___43-[_TVFocusableTextView setDescriptionText:]_block_invoke_2 : 228 -> 236
~ -[_TVFocusableTextView setMaximumNumberOfLines:] : 108 -> 112
~ -[_TVFocusableTextView maximumNumberOfLines] : 68 -> 72
~ -[_TVFocusableTextView _recomputeTextSizeIfNeeded] : 244 -> 252
~ -[_TVFocusableTextView _moreLabelFrame] : 828 -> 852
~ -[_TVFocusableTextView tintColorDidChange] : 144 -> 152
~ -[_TVFocusableTextView gestureRecognizerShouldBegin:] : 116 -> 124
~ -[_TVFocusableTextView setMoreLabelTextColor:] : 20 -> 80
~ -[_TVFocusableTextView setMoreLabelText:] : 20 -> 80
~ -[_TVFocusableTextView setDescriptionTextView:] : 20 -> 80
~ -[_TVFocusableTextView setFloatingView:] : 20 -> 80
~ -[_TVFocusableTextView setBackgroundView:] : 20 -> 80
~ -[_TVFocusableTextView setSelectRecognizer:] : 20 -> 80
~ -[_TVFocusableTextView setPlayRecognizer:] : 20 -> 80
~ -[_TVFocusableTextView setMoreLabel:] : 20 -> 80
~ -[_TVCarouselView initWithFrame:] : 1264 -> 1336
~ -[_TVCarouselView setHeaderView:] : 160 -> 168
~ -[_TVCarouselView setShowsPageControl:] : 308 -> 324
~ -[_TVCarouselView _startContinuousScroll] : 328 -> 340
~ -[_TVCarouselView displayLinkDidFire:] : 352 -> 372
~ -[_TVCarouselView dealloc] : 112 -> 116
~ -[_TVCarouselView _collectionView] : 16 -> 64
~ -[_TVCarouselView _pageControlValueChanged:] : 104 -> 108
~ -[_TVCarouselView didMoveToWindow] : 112 -> 116
~ -[_TVCarouselView preferredFocusedView] : 16 -> 64
~ -[_TVCarouselView collectionView:numberOfItemsInSection:] : 212 -> 224
~ -[_TVCarouselView collectionView:cellForItemAtIndexPath:] : 220 -> 236
~ -[_TVCarouselView collectionView:willDisplayCell:forItemAtIndexPath:] : 368 -> 360
~ ___69-[_TVCarouselView collectionView:willDisplayCell:forItemAtIndexPath:]_block_invoke : 232 -> 256
~ ___74-[_TVCarouselView collectionView:didEndDisplayingCell:forItemAtIndexPath:]_block_invoke : 240 -> 264
~ -[_TVCarouselView shouldUpdateFocusInContext:] : 196 -> 200
~ -[_TVCarouselView scrollViewWillEndDragging:withVelocity:targetContentOffset:] : 420 -> 428
~ -[_TVCarouselView scrollViewDidScroll:] : 308 -> 312
~ -[_TVCarouselView _handlePlayGesture:] : 256 -> 268
~ -[_TVCarouselView _cellForItemAtIndex:] : 108 -> 116
~ -[_TVCarouselView focusedCell] : 84 -> 88
~ -[_TVCarouselView dequeueReusableCellWithReuseIdentifier:forIndex:] : 200 -> 208
~ -[_TVCarouselView indexForCell:] : 184 -> 200
~ -[_TVCarouselView reloadData] : 336 -> 356
~ -[_TVCarouselView setDelegate:] : 888 -> 892
~ -[_TVCarouselView _centerItemAtPageIndex:animated:] : 196 -> 212
~ -[_TVCarouselView _numberOfCells] : 96 -> 100
~ -[_TVCarouselView calculateChangeSetForFocusedIndex:newDataSourceMap:indexesToRemove:indexesToAdd:indexesToReload:] : 836 -> 872
~ -[_TVCarouselView _focusItemAtIndex:] : 492 -> 512
~ ___68-[_TVCarouselView _setContentOffsetForCollectionViewIndex:animated:]_block_invoke : 140 -> 148
~ -[_TVCarouselView _updateCarouselWithDataSource:indicesToRemove:indicesToAdd:indicesToReload:] : 276 -> 252
~ ___94-[_TVCarouselView _updateCarouselWithDataSource:indicesToRemove:indicesToAdd:indicesToReload:]_block_invoke : 252 -> 248
~ ___94-[_TVCarouselView _updateCarouselWithDataSource:indicesToRemove:indicesToAdd:indicesToReload:]_block_invoke_2 : 184 -> 228
~ -[_TVCarouselView _prepareIndexMap:] : 496 -> 524
~ -[_TVCarouselView _contentOffsetXForCollectionViewIndex:] : 216 -> 224
~ -[_TVCarouselView _updateContentOffsetForFocusedIndex:animated:] : 340 -> 348
~ ___64-[_TVCarouselView _updateContentOffsetForFocusedIndex:animated:]_block_invoke : 148 -> 156
~ ___64-[_TVCarouselView _updateContentOffsetForFocusedIndex:animated:]_block_invoke_2 : 92 -> 96
~ -[_TVCarouselView _animatePagedCenteringAnimated:animations:completion:] : 148 -> 144
~ -[_TVCarouselView _canScrollCarouselView] : 92 -> 96
~ -[_TVCarouselView _updateAutoScrollTimer] : 380 -> 392
~ ___40-[_TVCarouselView _startAutoScrollTimer]_block_invoke : 172 -> 180
~ -[_TVCarouselView _updateIdleModeLayoutAttributes] : 472 -> 488
~ -[_TVCarouselView _previousItemIndexForIndexPath:] : 228 -> 244
~ -[_TVCarouselView _itemIndexForIndexPath:] : 152 -> 164
~ -[_TVCarouselView _updatePageControl] : 452 -> 488
~ -[_TVCarouselView setCollectionToDatasourceIndexMap:] : 20 -> 80
~ -[_TVCarouselView setFocusGuide:] : 20 -> 80
~ -[_TVCarouselView setDisplayLink:] : 20 -> 80
~ -[_TVCarouselView setFirstFocusChangeInInterval:] : 20 -> 80
~ -[_TVCarouselView setPageControl:] : 20 -> 80
~ -[_TVCarouselCollectionViewLayout prepareLayout] : 444 -> 460
~ -[_TVCarouselCollectionViewLayout collectionViewContentSize] : 156 -> 160
~ -[_TVCarouselCollectionViewLayout layoutAttributesForElementsInRect:] : 436 -> 444
~ -[_TVCarouselCollectionViewLayout _expectedNumberOfCells] : 224 -> 232
~ -[_TVCarouselCollectionView _canScrollX] : 120 -> 124

```
