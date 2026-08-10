## CameraUI

> `/System/Library/AccessibilityBundles/CameraUI.axbundle/CameraUI`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3045.0.0.0.0
-  __TEXT.__text: 0x18528
-  __TEXT.__objc_methlist: 0x26a4
+3048.0.0.0.0
+  __TEXT.__text: 0x18c40
+  __TEXT.__objc_methlist: 0x2744
   __TEXT.__const: 0x160
-  __TEXT.__gcc_except_tab: 0x378
-  __TEXT.__cstring: 0x3474
+  __TEXT.__gcc_except_tab: 0x384
+  __TEXT.__cstring: 0x3542
   __TEXT.__oslogstring: 0x381
-  __TEXT.__unwind_info: 0x900
+  __TEXT.__unwind_info: 0x928
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xa98
-  __DATA_CONST.__objc_classlist: 0x3c0
+  __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1530
-  __DATA_CONST.__objc_superrefs: 0x158
+  __DATA_CONST.__objc_selrefs: 0x1598
+  __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x48
-  __DATA_CONST.__got: 0x2c0
+  __DATA_CONST.__got: 0x2d8
   __AUTH_CONST.__const: 0x580
-  __AUTH_CONST.__cfstring: 0x45a0
-  __AUTH_CONST.__objc_const: 0x5310
+  __AUTH_CONST.__cfstring: 0x46a0
+  __AUTH_CONST.__objc_const: 0x5430
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x320
+  __AUTH.__objc_data: 0x3c0
   __DATA.__objc_ivar: 0x11c
   __DATA.__data: 0xc0
   __DATA.__bss: 0x41

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 822
-  Symbols:   2400
-  CStrings:  616
+  Functions: 836
+  Symbols:   2438
+  CStrings:  624
 
Symbols:
+ +[CAMSmartStylePreviewViewAccessibility _accessibilityPerformValidations:]
+ +[CAMSmartStylePreviewViewAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[CAMSmartStylePreviewViewAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[CAMPanoramaViewAccessibility _accessibilityAllowOutOfBoundsHitTestAtPoint:withEvent:]
+ -[CAMPanoramaViewAccessibility accessibilityElements]
+ -[CAMSmartStylePreviewViewAccessibility _accessibilityShouldIncludeRowRangeInElementDescription]
+ -[CAMSmartStylePreviewViewAccessibility accessibilityLabel]
+ -[CAMSmartStylePreviewViewAccessibility accessibilityRowRange]
+ -[CAMSmartStylePreviewViewAccessibility accessibilityTraits]
+ -[CAMSmartStylePreviewViewAccessibility isAccessibilityElement]
+ -[CAMZoomControlAccessibility _axIsZoomLockedForTimelapseRecording]
+ -[CAMZoomControlAccessibility _axZoomControlsHidden]
+ -[CAMZoomControlAccessibility accessibilityElementsHidden]
+ GCC_except_table339
+ GCC_except_table368
+ GCC_except_table394
+ GCC_except_table483
+ GCC_except_table484
+ GCC_except_table485
+ GCC_except_table486
+ GCC_except_table500
+ GCC_except_table503
+ GCC_except_table509
+ GCC_except_table515
+ GCC_except_table528
+ GCC_except_table558
+ GCC_except_table570
+ GCC_except_table583
+ GCC_except_table616
+ GCC_except_table662
+ GCC_except_table676
+ GCC_except_table760
+ _NSClassFromString
+ _OBJC_CLASS_$_CAMSmartStylePreviewViewAccessibility
+ _OBJC_CLASS_$_NSMeasurement
+ _OBJC_CLASS_$_NSMeasurementFormatter
+ _OBJC_CLASS_$_NSUnitLength
+ _OBJC_CLASS_$___CAMSmartStylePreviewViewAccessibility_super
+ _OBJC_METACLASS_$_CAMSmartStylePreviewViewAccessibility
+ _OBJC_METACLASS_$___CAMSmartStylePreviewViewAccessibility_super
+ __OBJC_$_CLASS_METHODS_CAMSmartStylePreviewViewAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_CAMSmartStylePreviewViewAccessibility
+ __OBJC_CLASS_RO_$_CAMSmartStylePreviewViewAccessibility
+ __OBJC_CLASS_RO_$___CAMSmartStylePreviewViewAccessibility_super
+ __OBJC_METACLASS_RO_$_CAMSmartStylePreviewViewAccessibility
+ __OBJC_METACLASS_RO_$___CAMSmartStylePreviewViewAccessibility_super
+ ___141-[AXCameraVisionEngine _sceneDescriptionAnnouncementForVisionFeatures:previousAnnouncementLocation:locationForAnnouncement:announcementType:]_block_invoke_2
+ ___50-[AXCameraVisionEngine _resetAccessiblityElements]_block_invoke
+ _objc_msgSend$_axIsZoomLockedForTimelapseRecording
+ _objc_msgSend$_axZoomControlsHidden
+ _objc_msgSend$_performOnMainQueueWithBlock:
+ _objc_msgSend$indexOfObjectIdenticalTo:
+ _objc_msgSend$initWithDoubleValue:unit:
+ _objc_msgSend$millimeters
+ _objc_msgSend$numberFromString:
+ _objc_msgSend$setUnitOptions:
+ _objc_msgSend$setUnitStyle:
+ _objc_msgSend$stringFromMeasurement:
- -[CAMPanoramaViewAccessibility _accessibilityHitTest:withEvent:]
- GCC_except_table331
- GCC_except_table360
- GCC_except_table385
- GCC_except_table473
- GCC_except_table474
- GCC_except_table475
- GCC_except_table476
- GCC_except_table490
- GCC_except_table493
- GCC_except_table499
- GCC_except_table505
- GCC_except_table518
- GCC_except_table548
- GCC_except_table560
- GCC_except_table573
- GCC_except_table606
- GCC_except_table652
- GCC_except_table666
- GCC_except_table749
CStrings:
+ "CAMSmartStylePreviewGridView"
+ "CAMSmartStylePreviewView"
+ "CAMSmartStylePreviewViewAccessibility"
+ "_arrowView"
+ "disablingMultipleCaptureFeatures"
+ "isDisablingMultipleCaptureFeatures"
+ "isZoomContentVisible"
+ "style.preview"
```
