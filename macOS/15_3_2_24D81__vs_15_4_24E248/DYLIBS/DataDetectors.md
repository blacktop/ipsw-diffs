## DataDetectors

> `/System/Library/PrivateFrameworks/DataDetectors.framework/Versions/A/DataDetectors`

```diff

 463.0.0.0.0
-  __TEXT.__text: 0x24ce4
+  __TEXT.__text: 0x255e0
   __TEXT.__auth_stubs: 0xd60
   __TEXT.__delay_helper: 0x244
-  __TEXT.__objc_methlist: 0x20a8
-  __TEXT.__const: 0x140
+  __TEXT.__objc_methlist: 0x279c
+  __TEXT.__const: 0x120
   __TEXT.__cstring: 0x1f02
   __TEXT.__oslogstring: 0x1053
-  __TEXT.__gcc_except_tab: 0x114
-  __TEXT.__unwind_info: 0x838
+  __TEXT.__gcc_except_tab: 0x110
+  __TEXT.__unwind_info: 0x8d8
   __TEXT.__objc_classname: 0x553
   __TEXT.__objc_methname: 0x67ce
   __TEXT.__objc_methtype: 0x1ce5

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c08
+  __DATA_CONST.__objc_selrefs: 0x1ea0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xe8
   __AUTH_CONST.__auth_got: 0x6c0
   __AUTH_CONST.__const: 0x370
   __AUTH_CONST.__cfstring: 0x27a0
-  __AUTH_CONST.__objc_const: 0x5240
+  __AUTH_CONST.__objc_const: 0x4528
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x2f4

   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 899C588D-9452-31E0-A63F-D16FECC2F17D
-  Functions: 807
-  Symbols:   2721
+  UUID: 5B3E5002-F206-39D0-AE8F-734717CBBE25
+  Functions: 862
+  Symbols:   2777
   CStrings:  2326
 
Symbols:
+ +[DDActionsManager sharedManager].cold.1
+ -[DDActionsManager actionsForType:].cold.1
+ -[DDActionsManager actionsForType:].cold.2
+ -[DDActionsManager hasActionsForResult:actionContext:].cold.1
+ -[DDActionsManager menuItemsForTextCheckingResult:actionContext:].cold.1
+ -[DDActionsManager setUIElement:isInUse:].cold.1
+ -[DDBasicHighlightsView _finishSetup].cold.1
+ -[DDBasicHighlightsView drawAtPoint:inContext:].cold.2
+ -[DDBasicHighlightsView drawRect:].cold.2
+ -[DDDataDetectorsViewHost updateViewController].cold.4
+ -[DDDetectorManager2 _highligtsOverlayForController:highlightRequest:].cold.1
+ -[DDDetectorManager2 _highligtsOverlayForController:highlightRequest:].cold.2
+ -[DDDetectorManager2 _removeReferenceToHLOverlayForIdentifier:].cold.1
+ -[DDDetectorManager2 controllerWithIdentifierDidAppear:].cold.2
+ -[DDDetectorManager2 controllerWithIdentifierWillDisappear:].cold.1
+ -[DDDetectorManager2 controllerWithIdentifierWillGoAway:].cold.1
+ -[DDDetectorManager2 dealloc].cold.1
+ -[DDDetectorManager2 scanCompleted:].cold.4
+ -[DDDetectorManager2 scanCompleted:].cold.5
+ -[DDOperation _scanDone].cold.2
+ -[DDPhoneNumber appendDataFromResult:].cold.1
+ -[DDPhoneNumber setFacetimeMenuItem:].cold.1
+ -[DDRange initWithDOMRange:].cold.1
+ -[DDWK2Overlay _addMultiViewForObject:withArrow:availableViews:].cold.1
+ -[DDWK2Overlay mouseEntered:].cold.1
+ -[NSString(dd_additions) dd_stringByAppendingURLParameter:value:first:keepEmpty:].cold.1
+ -[WKDOMTextIterator(DDExtensions) dd_doUrlificationForQuery:forResults:referenceDate:document:DOMWasModified:relevantResults:knownHighlights:URLificationBlock:].cold.1
+ -[WKDOMTextIterator(DDExtensions) dd_doUrlificationForQuery:forResults:referenceDate:document:DOMWasModified:relevantResults:knownHighlights:URLificationBlock:].cold.2
+ -[WKDOMTextIterator(DDExtensions) dd_doUrlificationForQuery:forResults:referenceDate:document:DOMWasModified:relevantResults:knownHighlights:URLificationBlock:].cold.3
+ -[WKDOMTextIterator(DDExtensions) dd_doUrlificationForQuery:forResults:referenceDate:document:DOMWasModified:relevantResults:knownHighlights:URLificationBlock:].cold.4
+ -[WKDOMTextIterator(DDExtensions) dd_doUrlificationForQuery:forResults:referenceDate:document:DOMWasModified:relevantResults:knownHighlights:URLificationBlock:].cold.5
+ -[WKDOMTextIterator(DDExtensions) dd_doUrlificationForQuery:forResults:referenceDate:document:DOMWasModified:relevantResults:knownHighlights:URLificationBlock:].cold.6
+ -[WKDOMTextIterator(DDExtensions) dd_doUrlificationForQuery:forResults:referenceDate:document:DOMWasModified:relevantResults:knownHighlights:URLificationBlock:].cold.7
+ -[WKDOMTextIterator(DDExtensions) dd_doUrlificationForQuery:forResults:referenceDate:document:DOMWasModified:relevantResults:knownHighlights:URLificationBlock:].cold.8
+ -[WKDOMTextIterator(DDExtensions) dd_newQueryStopRange:].cold.1
+ DDActionLogHandle.cold.1
+ DDHighlightGetLayerWithContext.cold.1
+ DDHighlightGetLayerWithContext.cold.2
+ DDHighlightGetLayerWithContext.cold.3
+ DDHighlightGetLayerWithContext.cold.4
+ DDHighlightGetNumberOfShapePoints.cold.1
+ DDHighlightGetNumberOfShapePoints.cold.2
+ DDHighlightGetNumberOfShapes.cold.1
+ DDHighlightGetShapePointAtCircularIndex.cold.1
+ DDHighlightGetShapePointAtCircularIndex.cold.2
+ DDHighlightGetShapePointAtCircularIndex.cold.3
+ DDHighlightGetShapeSmallestEdgeIndex.cold.1
+ DDHighlightGetShapeSmallestEdgeSize.cold.1
+ DDHighlightGetTrackingRects.cold.1
+ DDHighlightSimplifyPolygon.cold.1
+ DDHighlightUpdateGeometry.cold.1
+ DDMapsGetBestAddressForResults.cold.3
+ DDMapsURLStringForAddressResult.cold.1
+ DDServiceLogHandle.cold.1
+ DDUILogHandle.cold.1
+ dd_can_connect_to_service.cold.1
+ dd_phoneNumberResultCanBeRdarLink.cold.1
+ dd_send_showdate_request.cold.1
- _OUTLINED_FUNCTION_2
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DataDetectors/Sources/Actions/DDActionsManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DataDetectors/Sources/Drawing/DDDottedHighlightDrawing.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DataDetectors/Sources/Utilities/DDWebUtils.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DataDetectors/Sources/Actions/DDActionsManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DataDetectors/Sources/Drawing/DDDottedHighlightDrawing.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DataDetectors/Sources/Utilities/DDWebUtils.m"

```
