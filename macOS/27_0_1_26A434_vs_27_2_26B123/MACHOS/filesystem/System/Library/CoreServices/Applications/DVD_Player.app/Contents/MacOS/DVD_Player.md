## DVD Player

> `/System/Library/CoreServices/Applications/DVD Player.app/Contents/MacOS/DVD Player`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`

```diff

-282.5.0.0.0
-  __TEXT.__text: 0xdec8
-  __TEXT.__auth_stubs: 0x8f0
-  __TEXT.__objc_stubs: 0x3940
-  __TEXT.__objc_methlist: 0x164c
+292.2.0.0.0
+  __TEXT.__text: 0xea28
+  __TEXT.__auth_stubs: 0x920
+  __TEXT.__objc_stubs: 0x3d20
+  __TEXT.__objc_methlist: 0x1764
   __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__cstring: 0x1125
-  __TEXT.__objc_methname: 0x4b7b
-  __TEXT.__objc_classname: 0x2c7
-  __TEXT.__objc_methtype: 0xf40
-  __TEXT.__unwind_info: 0x548
-  __DATA_CONST.__const: 0x380
-  __DATA_CONST.__cfstring: 0x14a0
+  __TEXT.__gcc_except_tab: 0x8c
+  __TEXT.__cstring: 0x1156
+  __TEXT.__objc_methname: 0x5003
+  __TEXT.__objc_classname: 0x2e3
+  __TEXT.__objc_methtype: 0x1041
+  __TEXT.__unwind_info: 0x588
+  __DATA_CONST.__const: 0x3f0
+  __DATA_CONST.__cfstring: 0x14c0
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_intobj: 0xa8
-  __DATA_CONST.__auth_got: 0x488
-  __DATA_CONST.__got: 0x300
-  __DATA.__objc_const: 0x2ca8
-  __DATA.__objc_selrefs: 0x1508
-  __DATA.__objc_ivar: 0x260
+  __DATA_CONST.__auth_got: 0x4a0
+  __DATA_CONST.__got: 0x330
+  __DATA.__objc_const: 0x2d98
+  __DATA.__objc_selrefs: 0x1638
+  __DATA.__objc_ivar: 0x274
   __DATA.__objc_data: 0x5a0
-  __DATA.__data: 0x300
+  __DATA.__data: 0x360
   __DATA.__bss: 0x14
   - /System/Library/Frameworks/AVKit.framework/Versions/A/AVKit
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /System/Library/PrivateFrameworks/MediaRemote.framework/Versions/A/MediaRemote
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 362
-  Symbols:   260
-  CStrings:  1256
+  Functions: 383
+  Symbols:   269
+  CStrings:  1307
 
Symbols:
+ _DVDSleep
+ _DVDWakeUp
+ _NSWorkspaceDidWakeNotification
+ _NSWorkspaceWillSleepNotification
+ _OBJC_CLASS_$_NSClickGestureRecognizer
+ _OBJC_CLASS_$_NSControl
+ _OBJC_CLASS_$_NSPanGestureRecognizer
+ _OBJC_CLASS_$_NSTrackingArea
+ _dispatch_async
CStrings:
+ "@\"NSClickGestureRecognizer\""
+ "@\"NSPanGestureRecognizer\""
+ "B24@0:8@\"NSGestureRecognizer\"16"
+ "B32@0:8@\"NSGestureRecognizer\"16@\"NSEvent\"24"
+ "B32@0:8@\"NSGestureRecognizer\"16@\"NSGestureRecognizer\"24"
+ "B32@0:8@\"NSGestureRecognizer\"16@\"NSTouch\"24"
+ "NSGestureRecognizerDelegate"
+ "TB,N,GisMoving,V_moving"
+ "TB,N,GwasMoved,V_moved"
+ "[5d]"
+ "_armHudAutoHideTimerIfNeeded"
+ "_beginHudInteraction"
+ "_clickGestureRecognizer"
+ "_deviceMounted: ignoring non-removable volume %@"
+ "_endHudInteraction"
+ "_fireHudAutoHideTimer:"
+ "_handleClickGesture:"
+ "_handleHudMoveGesture:"
+ "_hudAutoHideTimer"
+ "_hudInteractionCount"
+ "_hudMoveGestureLocationOnScreen:"
+ "_hudMoveGestureRecognizer"
+ "_hudMoveMaxX"
+ "_hudMoveMaxY"
+ "_hudMoveMinX"
+ "_hudMoveMinY"
+ "_hudMoveRecentXSamples"
+ "_hudMoveRecentYSamples"
+ "_hudMoveStartingFrameOrigin"
+ "_hudMoveStartingLocationOnScreen"
+ "_isRemovableVolumeAtPath:"
+ "_registerHudInteractionTrackingFor:"
+ "addGestureRecognizer:"
+ "addTarget:action:forControlEvents:"
+ "addTrackingArea:"
+ "convertPoint:fromView:"
+ "convertPointFromScreen:"
+ "convertPointToScreen:"
+ "gestureRecognizer:shouldAttemptToRecognizeWithEvent:"
+ "gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:"
+ "gestureRecognizer:shouldReceiveTouch:"
+ "gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:"
+ "gestureRecognizer:shouldRequireFailureOfGestureRecognizer:"
+ "gestureRecognizerShouldBegin:"
+ "hideHud"
+ "hitTest:"
+ "hudDragDidBegin"
+ "hudDragDidEnd"
+ "hudPanel"
+ "initWithRect:options:owner:userInfo:"
+ "initWithTarget:action:"
+ "isHudBeingDragged"
+ "isHudControlBeingTracked"
+ "isMouseOverHUD"
+ "locationInView:"
+ "mouseEntered:"
+ "mouseExited:"
+ "setAllowedTouchTypes:"
+ "setDelaysPrimaryMouseButtonEvents:"
+ "setDelaysSecondaryMouseButtonEvents:"
+ "setMoved:"
+ "setMoving:"
+ "setNumberOfTouchesRequired:"
+ "showHud"
+ "state"
+ "superview"
+ "toggleHudVisibility"
+ "window"
+ "{CGPoint=dd}24@0:8@16"
- "TB,R,GisMoving,V_moving"
- "TB,R,GwasMoved,V_moved"
- "_fireHudVisibilityTimer:"
- "_hudVisibilityTimer"
- "_isMouseDown"
- "_isValidMedia:"
- "_maxX"
- "_maxY"
- "_minX"
- "_minY"
- "_moveStartingPoint"
- "isMouseOverHUD:"
- "mouseDown:"
- "mouseDownOverDVD:"
- "mouseDragged:"
- "mouseUp:"
- "q!"
- "\x81"
```
