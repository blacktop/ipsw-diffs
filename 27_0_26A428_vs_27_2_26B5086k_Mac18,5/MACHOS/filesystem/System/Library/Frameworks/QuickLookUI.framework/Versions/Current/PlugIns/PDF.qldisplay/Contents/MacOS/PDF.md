## PDF

> `/System/Library/Frameworks/QuickLookUI.framework/Versions/Current/PlugIns/PDF.qldisplay/Contents/MacOS/PDF`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`

```diff

-1114.0.0.0.0
-  __TEXT.__text: 0x8e88
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_stubs: 0x25c0
-  __TEXT.__objc_methlist: 0xea0
+1114.1.1.0.0
+  __TEXT.__text: 0x9b38
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_stubs: 0x28c0
+  __TEXT.__objc_methlist: 0x1020
   __TEXT.__const: 0x68
-  __TEXT.__objc_methname: 0x2590
-  __TEXT.__cstring: 0x394
+  __TEXT.__objc_methname: 0x2acb
+  __TEXT.__cstring: 0x3fe
   __TEXT.__ustring: 0xfe
-  __TEXT.__objc_classname: 0xf7
-  __TEXT.__objc_methtype: 0x875
+  __TEXT.__objc_classname: 0x13a
+  __TEXT.__objc_methtype: 0x9e0
   __TEXT.__gcc_except_tab: 0xb0
   __TEXT.__oslogstring: 0x1c3
-  __TEXT.__unwind_info: 0x4a0
+  __TEXT.__unwind_info: 0x4e0
   __DATA_CONST.__const: 0x1f0
-  __DATA_CONST.__cfstring: 0x4a0
-  __DATA_CONST.__objc_classlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__cfstring: 0x4e0
+  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x390
-  __DATA_CONST.__got: 0x260
-  __DATA.__objc_const: 0x1510
-  __DATA.__objc_selrefs: 0xc40
-  __DATA.__objc_ivar: 0x114
-  __DATA.__objc_data: 0x320
-  __DATA.__data: 0x120
+  __DATA_CONST.__auth_got: 0x398
+  __DATA_CONST.__got: 0x278
+  __DATA.__objc_const: 0x1750
+  __DATA.__objc_selrefs: 0xd58
+  __DATA.__objc_ivar: 0x12c
+  __DATA.__objc_data: 0x370
+  __DATA.__data: 0x180
   __DATA.__common: 0x8
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/QuickLookSupport.framework/Versions/A/QuickLookSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 311
-  Symbols:   206
-  CStrings:  660
+  Functions: 335
+  Symbols:   212
+  CStrings:  719
 
Symbols:
+ _NSZeroPoint
+ _OBJC_CLASS_$_NSMagnificationGestureRecognizer
+ _OBJC_CLASS_$_NSPanGestureRecognizer
+ _OBJC_CLASS_$_QLSidecarSwipeGestureRecognizer
+ _OBJC_METACLASS_$_NSPanGestureRecognizer
+ _objc_setProperty_nonatomic
CStrings:
+ "@\"NSMagnificationGestureRecognizer\""
+ "@\"QLPDFTouchCountingPanGestureRecognizer\""
+ "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "B24@0:8@\"NSGestureRecognizer\"16"
+ "B28@0:8d16B24"
+ "B32@0:8@\"NSGestureRecognizer\"16@\"NSEvent\"24"
+ "B32@0:8@\"NSGestureRecognizer\"16@\"NSGestureRecognizer\"24"
+ "B32@0:8@\"NSGestureRecognizer\"16@\"NSTouch\"24"
+ "B32@0:8@16@24"
+ "B32@0:8d16d24"
+ "B40@0:8d16{CGPoint=dd}24"
+ "NSGestureRecognizerDelegate"
+ "QLPDFContainerView.sidecarMagnificationGestureRecognizer"
+ "QLPDFContainerView.sidecarSwipeGestureRecognizer"
+ "QLPDFTouchCountingPanGestureRecognizer"
+ "T@\"NSMagnificationGestureRecognizer\",&,N,V_sidecarMagnificationGestureRecognizer"
+ "T@\"QLPDFTouchCountingPanGestureRecognizer\",&,N,V_sidecarSwipeGestureRecognizer"
+ "Td,N,V_sidecarLastMagnification"
+ "_activeTouchIdentities"
+ "_applyMagnification:atLayerPoint:"
+ "_lastPanTranslation"
+ "_panZoomedContentByDeltaX:deltaY:"
+ "_peakTouchCount"
+ "_setupGestures"
+ "_sidecarLastMagnification"
+ "_sidecarMagnificationGestureRecognizer"
+ "_sidecarSwipeGestureRecognizer"
+ "_slidePagesByDelta:horizontalPreferred:"
+ "addGestureRecognizer:"
+ "gestureRecognizer:shouldAttemptToRecognizeWithEvent:"
+ "gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:"
+ "gestureRecognizer:shouldReceiveTouch:"
+ "gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:"
+ "gestureRecognizer:shouldRequireFailureOfGestureRecognizer:"
+ "gestureRecognizerShouldBegin:"
+ "identity"
+ "initWithTarget:action:"
+ "locationInView:"
+ "magnifyByIncrement:atLayerPoint:"
+ "magnifyWithGesture:"
+ "panWithGesture:"
+ "ql_pdf_peakTouchCount"
+ "removeAllObjects"
+ "reset"
+ "setAllowedTouchTypes:"
+ "setButtonMask:"
+ "setEnabled:"
+ "setSidecarLastMagnification:"
+ "setSidecarMagnificationGestureRecognizer:"
+ "setSidecarSwipeGestureRecognizer:"
+ "sidecarLastMagnification"
+ "sidecarMagnificationGestureRecognizer"
+ "sidecarSwipeGestureRecognizer"
+ "state"
+ "touchesBeganWithEvent:"
+ "touchesCancelledWithEvent:"
+ "touchesEndedWithEvent:"
+ "touchesMatchingPhase:inView:"
+ "translationInView:"
```
