## GraphKit

> `/System/Library/PrivateFrameworks/GraphKit.framework/Versions/A/GraphKit`

```diff

 31.0.0.0.0
-  __TEXT.__text: 0x283e0
+  __TEXT.__text: 0x28118
   __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0x16a4
-  __TEXT.__const: 0x3f8
-  __TEXT.__cstring: 0x3593
-  __TEXT.__unwind_info: 0x5e8
+  __TEXT.__objc_methlist: 0x16dc
+  __TEXT.__const: 0x410
+  __TEXT.__cstring: 0x357d
+  __TEXT.__unwind_info: 0x5d8
   __TEXT.__objc_classname: 0xc6
   __TEXT.__objc_methname: 0x2cba
   __TEXT.__objc_methtype: 0x6cc

   __DATA_CONST.__objc_superrefs: 0x70
   __AUTH_CONST.__auth_got: 0x280
   __AUTH_CONST.__const: 0x18
-  __AUTH_CONST.__cfstring: 0x2fe0
-  __AUTH_CONST.__objc_const: 0x1e68
+  __AUTH_CONST.__cfstring: 0x2fc0
+  __AUTH_CONST.__objc_const: 0x1e10
   __AUTH.__objc_data: 0x460
   __DATA.__objc_ivar: 0x1fc
   __DATA.__data: 0x8d0

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3B4C077D-D56F-3330-B157-BE505B15D93D
-  Functions: 467
+  UUID: 03498E5F-53AF-3623-8613-22AFB65F4356
+  Functions: 465
   Symbols:   1636
-  CStrings:  1540
+  CStrings:  1538
 
Symbols:
+ zoomToRect:.samuraiPizzaCats.277
- zoomToRect:.samuraiPizzaCats.280
Functions:
~ -[GRChartView setProperty:forKey:] : 528 -> 540
~ -[GRChartView setNeedsToReloadData:inRange:] : 352 -> 328
~ -[GRChartView setDelegate:] : 272 -> 260
~ -[GRChartView canvasRectForDataSetAtIndex:] : 628 -> 608
~ -[GRChartView computeLayout] : 820 -> 828
~ -[GRChartView delayedRedraw:] : 140 -> 136
~ -[GRChartView drawRect:] : 2644 -> 2628
~ -[GRChartView acceptsFirstResponder] : 172 -> 176
~ -[GRChartView canBecomeKeyView] : 172 -> 176
~ -[GRChartView addDataSets:loadData:] : 124 -> 116
~ -[GRChartView _setZoomX:Y:] : 752 -> 728
~ -[GRChartView _zoomToPercent:] : 1140 -> 1132
~ -[GRChartView zoomToRect:] : 1148 -> 1144
~ -[GRChartView sizeSelectionRectangle] : 588 -> 584
~ -[GRChartView flagsChanged:] : 360 -> 356
~ -[GRChartView resetCursorRects] : 360 -> 356
~ -[GRChartView mouseDragged:] : 564 -> 568
~ -[GRAxes setDelegate:] : 132 -> 120
~ -[GRAxes didSetProperty:forKey:replacingOldValue:andShouldReload:andRelayout:andRedisplay:] : 1284 -> 1276
~ -[GRAxes chart:propertyChangedForKey:from:to:] : 352 -> 364
~ -[GRAxes dataSet:propertyChangedForKey:from:to:] : 296 -> 308
~ -[GRAxes setProperty:forKey:] : 400 -> 412
~ -[GRAxes legendRect] : 3084 -> 3056
~ -[GRAxes computeLayout] : 876 -> 880
~ -[GRAxes setNeedsLayout:] : 60 -> 56
~ +[GRPieAxes initialize] : 444 -> 440
~ -[GRAreaDataSet drawDataSetRect:] : 6120 -> 6020
~ -[GRColumnDataSet drawDataSetRect:] : 7604 -> 7656
~ -[GRDataSet setProperty:forKey:andRefresh:] : 464 -> 476
~ -[GRDataSet chart:propertyChangedForKey:from:to:] : 220 -> 232
~ -[GRDataSet setDataSource:] : 124 -> 116
~ -[GRDataSet setDelegate:] : 188 -> 176
~ -[GRDataSet _setSelectedRangeWithoutChangingAnchorPoint:] : 164 -> 168
~ -[GRPieDataSet reloadDataInRange:] : 1320 -> 1328
~ -[GRPieDataSet drawDataSetRect:] : 1552 -> 1548
~ +[GRLineDataSet initialize] : 1724 -> 1720
~ -[GRLineDataSet drawDataSetRect:] : 6672 -> 6548
- sub_1a6d0
~ -[GRXYDataSet supportsRangesOnAxis:] : 144 -> 148
~ -[GRXYDataSet xIntervalAtIndex:] : 148 -> 164
~ -[GRXYDataSet yValueAtIndex:] : 144 -> 156
~ -[GRXYDataSet setSelectedRange:] : 864 -> 868
~ -[GRXYDataSet reloadDataInRange:] : 4252 -> 4344
~ -[GRXYAxes initWithOwner:] : 248 -> 240
~ -[GRXYAxes initWithCoder:] : 304 -> 296
~ -[GRXYAxes _extraMarginSpaceLeft:right:top:bottom:] : 2388 -> 2344
~ _boundsOfRotatedSize : 212 -> 200
~ __labelOffset : 508 -> 492
~ -[GRXYAxes computeUnitsForAxis:] : 13156 -> 12872
~ -[GRXYAxes drawGridRect:forAxis:] : 3096 -> 3100
~ -[GRXYAxes drawAxisRect:forAxis:] : 9664 -> 9464
~ -[GRSliderScroller _layoutScroller] : 624 -> 664
~ -[GRSliderScroller setFrameOrigin:] : 192 -> 184
~ -[GRSliderScroller setFrameSize:] : 196 -> 192
~ -[GRGradientColor _updateColorFunction] : 596 -> 608
~ -[GRGradientColor fillBezierPath:withBounds:] : 576 -> 580
- sub_29b04
CStrings:
- "Unversioned directory"

```
