## PDFKit

> `/System/Library/Frameworks/PDFKit.framework/Versions/A/PDFKit`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-1537.0.0.0.0
-  __TEXT.__text: 0xe2784
-  __TEXT.__objc_methlist: 0xc870
-  __TEXT.__const: 0x9c4
-  __TEXT.__gcc_except_tab: 0x84d8
+1537.1.4.0.0
+  __TEXT.__text: 0xe3a0c
+  __TEXT.__objc_methlist: 0xc9d0
+  __TEXT.__const: 0x9b4
+  __TEXT.__gcc_except_tab: 0x8410
   __TEXT.__cstring: 0x8074
   __TEXT.__dlopen_cstrs: 0x257
   __TEXT.__ustring: 0xc2

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x43d0
+  __TEXT.__unwind_info: 0x4420
   __TEXT.__eh_frame: 0x128
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7938
+  __DATA_CONST.__objc_selrefs: 0x7a40
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x378
   __DATA_CONST.__objc_arraydata: 0x1d0
   __DATA_CONST.__got: 0xdd0
   __AUTH_CONST.__const: 0x2308
   __AUTH_CONST.__cfstring: 0x8880
-  __AUTH_CONST.__objc_const: 0x11870
+  __AUTH_CONST.__objc_const: 0x119e0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x5e8

   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__objc_data: 0x19a0
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0xe78
+  __DATA.__objc_ivar: 0xe9c
   __DATA.__data: 0x1310
   __DATA.__bss: 0x630
   __DATA_DIRTY.__objc_data: 0x1c20

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4486
-  Symbols:   11793
+  Functions: 4509
+  Symbols:   11857
   CStrings:  1426
 
Symbols:
+ -[PDFAccessibilityNodeContent _contentRelativeRange:]
+ -[PDFAccessibilityNodeContent _getParentTextOffset]
+ -[PDFAccessibilityNodeContent _isParentTextOffsetCalculated]
+ -[PDFAccessibilityNodeContent _parentRelativeRange:]
+ -[PDFAccessibilityNodeContent _parentTextOffset]
+ -[PDFAccessibilityNodeContent set_isParentTextOffsetCalculated:]
+ -[PDFAccessibilityNodeContent set_parentTextOffset:]
+ -[PDFKitTextView _beginEditingSession]
+ -[PDFKitTextView _commitStringToModel:]
+ -[PDFKitTextView _replacementOverflowsWidget:inRange:forTextView:]
+ -[PDFKitTextView textDidBeginEditing:]
+ -[PDFKitTextView textView:shouldChangeTextInRange:replacementString:]
+ -[PDFView _alignArrivingPageViews:goingToNextPage:]
+ -[PDFView _beginTouchPageSwipeWithTranslation:gesture:]
+ -[PDFView _completePageTransitionWithSuccess:]
+ -[PDFView _detachPageViewInPlace:]
+ -[PDFView _finishInFlightPageTransitionImmediately]
+ -[PDFView _finishTouchPageSwipeForGesture:state:]
+ -[PDFView _pageTransitionTravelDistance]
+ -[PDFView _readingOriginForPageFrame:visibleRect:steppingBack:]
+ -[PDFView _reattachPageViewInPlace:]
+ -[PDFView _scrollForPassedThroughTouchDrag:]
+ -[PDFView _scrollToReadingStartOfCurrentPageComingFromPage:]
+ -[PDFView _shouldHandleScannerResultAtPagePoint:onPage:]
+ -[PDFView _touchDragShouldTurnPage:]
+ -[PDFView _updatePageTransitionWithAmount:]
+ -[PDFView _updateTouchPageSwipeForChangedGesture:]
+ -[PDFView isAtPageTurnEdgeForHorizontalScroll:goingToNextPage:]
+ GCC_except_table325
+ GCC_except_table332
+ GCC_except_table377
+ GCC_except_table385
+ OBJC_IVAR_$_PDFAccessibilityNodeContent.__isParentTextOffsetCalculated
+ OBJC_IVAR_$_PDFAccessibilityNodeContent.__parentTextOffset
+ OBJC_IVAR_$_PDFKitTextViewPrivate.isCommittingOwnEdit
+ OBJC_IVAR_$_PDFKitTextViewPrivate.preEditValue
+ OBJC_IVAR_$_PDFKitTextViewPrivate.sessionUndoRegistered
+ OBJC_IVAR_$_PDFViewPrivate.isPassingTouchDragToScrollView
+ OBJC_IVAR_$_PDFViewPrivate.pageTransitionGeneration
+ OBJC_IVAR_$_PDFViewPrivate.pageTransitionSucceeded
+ OBJC_IVAR_$_PDFViewPrivate.suppressScrollOffsetRestoreOnResize
+ OBJC_IVAR_$_PDFViewPrivate.touchPassThroughStartOrigin
+ OBJC_IVAR_$_PDFViewPrivate.touchSwipeTranslationOffset
+ __49-[PDFView _finishTouchPageSwipeForGesture:state:]_block_invoke
+ ___49-[PDFView _finishTouchPageSwipeForGesture:state:]_block_invoke
+ ___block_descriptor_49_e8_32w_e5_v8?0l
+ ___block_descriptor_66_e8_32w_e18_v36?0d8Q16B24^B28l
+ _objc_msgSend$_alignArrivingPageViews:goingToNextPage:
+ _objc_msgSend$_beginEditingSession
+ _objc_msgSend$_beginTouchPageSwipeWithTranslation:gesture:
+ _objc_msgSend$_commitStringToModel:
+ _objc_msgSend$_completePageTransitionWithSuccess:
+ _objc_msgSend$_contentRelativeRange:
+ _objc_msgSend$_detachPageViewInPlace:
+ _objc_msgSend$_finishInFlightPageTransitionImmediately
+ _objc_msgSend$_finishTouchPageSwipeForGesture:state:
+ _objc_msgSend$_getParentTextOffset
+ _objc_msgSend$_isParentTextOffsetCalculated
+ _objc_msgSend$_pageTransitionTravelDistance
+ _objc_msgSend$_parentRelativeRange:
+ _objc_msgSend$_parentTextOffset
+ _objc_msgSend$_readingOriginForPageFrame:visibleRect:steppingBack:
+ _objc_msgSend$_reattachPageViewInPlace:
+ _objc_msgSend$_replacementOverflowsWidget:inRange:forTextView:
+ _objc_msgSend$_scrollForPassedThroughTouchDrag:
+ _objc_msgSend$_scrollToReadingStartOfCurrentPageComingFromPage:
+ _objc_msgSend$_shouldHandleScannerResultAtPagePoint:onPage:
+ _objc_msgSend$_touchDragShouldTurnPage:
+ _objc_msgSend$_updatePageTransitionWithAmount:
+ _objc_msgSend$_updateTouchPageSwipeForChangedGesture:
+ _objc_msgSend$centerXAnchor
+ _objc_msgSend$constraintGreaterThanOrEqualToAnchor:
+ _objc_msgSend$constraintLessThanOrEqualToAnchor:
+ _objc_msgSend$isAtPageTurnEdgeForHorizontalScroll:goingToNextPage:
+ _objc_msgSend$setPriority:
+ _objc_msgSend$set_isParentTextOffsetCalculated:
+ _objc_msgSend$set_parentTextOffset:
+ _objc_msgSend$stringByReplacingCharactersInRange:withString:
+ _objc_msgSend$textContainerInset
- +[PDFAccessibilityNode _accessibilityElementForNode:]
- GCC_except_table320
- GCC_except_table327
- GCC_except_table366
- GCC_except_table371
- OBJC_IVAR_$_PDFViewPrivate.originalCurrentPageViewFrames
- OBJC_IVAR_$_PDFViewPrivate.originalTopPageViewFrames
- __32-[PDFView handleTouchPageSwipe:]_block_invoke
- ___32-[PDFView handleTouchPageSwipe:]_block_invoke
- ___block_descriptor_89_e8_32s40s48s56w_e5_v8?0l
- ___block_descriptor_98_e8_32s40s48s56s64w_e18_v36?0d8Q16B24^B28l
- ___copy_helper_block_e8_32s40s48s56s64w
- ___copy_helper_block_e8_32s40s48s56w
- ___destroy_helper_block_e8_32s40s48s56s64w
- ___destroy_helper_block_e8_32s40s48s56w
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/System/Library/Frameworks/CoreGraphics.framework/PrivateHeaders/CGBuf.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/System/Library/Frameworks/CoreGraphics.framework/PrivateHeaders/CGBuf.h"
```
