## Diagnostic-3939

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3939.appex/Diagnostic-3939`

```diff

 816.2.2.0.0
-  __TEXT.__text: 0x58c4
-  __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__objc_stubs: 0x1320
-  __TEXT.__objc_methlist: 0x788
-  __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x1b0
-  __TEXT.__cstring: 0x283
-  __TEXT.__objc_methname: 0x17e7
-  __TEXT.__oslogstring: 0x20a
-  __TEXT.__objc_classname: 0x13c
-  __TEXT.__objc_methtype: 0x4b6
-  __TEXT.__unwind_info: 0x1d0
-  __DATA_CONST.__auth_got: 0x268
-  __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x1e8
-  __DATA_CONST.__cfstring: 0x700
-  __DATA_CONST.__objc_classlist: 0x78
-  __DATA_CONST.__objc_protolist: 0x10
+  __TEXT.__text: 0x71b0
+  __TEXT.__auth_stubs: 0x510
+  __TEXT.__objc_stubs: 0x1820
+  __TEXT.__objc_methlist: 0x8b8
+  __TEXT.__const: 0x40
+  __TEXT.__gcc_except_tab: 0x23c
+  __TEXT.__cstring: 0x32c
+  __TEXT.__objc_methname: 0x1cc3
+  __TEXT.__oslogstring: 0x2fc
+  __TEXT.__objc_classname: 0x1ac
+  __TEXT.__objc_methtype: 0x578
+  __TEXT.__unwind_info: 0x228
+  __DATA_CONST.__auth_got: 0x298
+  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__const: 0x2f0
+  __DATA_CONST.__cfstring: 0x820
+  __DATA_CONST.__objc_classlist: 0x88
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__objc_intobj: 0x1f8
-  __DATA_CONST.__objc_doubleobj: 0x50
-  __DATA.__objc_const: 0x1550
-  __DATA.__objc_selrefs: 0x608
-  __DATA.__objc_ivar: 0xb4
-  __DATA.__objc_data: 0x4b0
-  __DATA.__data: 0xc0
+  __DATA_CONST.__objc_superrefs: 0x68
+  __DATA_CONST.__objc_intobj: 0x288
+  __DATA_CONST.__objc_doubleobj: 0x70
+  __DATA.__objc_const: 0x18f0
+  __DATA.__objc_selrefs: 0x750
+  __DATA.__objc_ivar: 0xd4
+  __DATA.__objc_data: 0x550
+  __DATA.__data: 0x180
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
+  - /System/Library/PrivateFrameworks/CheckerBoardServices.framework/CheckerBoardServices
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 177
-  Symbols:   156
-  CStrings:  468
+  Functions: 214
+  Symbols:   182
+  CStrings:  555
 
Symbols:
+ _CHHapticEventTypeHapticTransient
+ _CHHapticPatternKeyEventDuration
+ _OBJC_METACLASS_$_DATouchButtonParameters
+ _OBJC_CLASS_$__UIPhysicalButtonInteraction
+ _DAIdentifierCamera
+ _OBJC_METACLASS_$_DATouchButtonTargetEvent
+ _IOHIDEventConformsTo
+ _CHHapticPatternKeyPattern
+ _OBJC_CLASS_$__UIPhysicalButtonConfiguration
+ _IOHIDEventGetChildren
+ _OBJC_CLASS_$_CBSUtilities
+ _OBJC_CLASS_$_CHHapticEngine
+ _OBJC_CLASS_$_DATouchButtonParameters
+ _CHHapticPatternKeyTime
+ _IOHIDEventGetIntegerValue
+ _OBJC_CLASS_$_DATouchButtonTargetEvent
+ _IOHIDEventGetFloatValue
+ _DATypeTouchButton
+ __UIEventHIDGetChildForceStageEvent
+ _dispatch_get_global_queue
+ _IOHIDEventGetType
+ __UIEventHIDEnumerateChildren
+ _OBJC_CLASS_$_CHHapticPattern
+ _CHHapticPatternKeyEvent
+ _CHHapticPatternKeyEventType
+ _OBJC_CLASS_$_NSArray
CStrings:
+ "hapticEngine"
+ "numberWithFloat:"
+ "targetEvents"
+ "setupTouchButtonInteractions"
+ "startAtTime:error:"
+ "v16@?0q8"
+ "TouchButton"
+ "notifyWhenPlayersFinished:"
+ "T@\"NSNumber\",&,N,V_value"
+ "Haptic engine was reset"
+ "_UIPhysicalButtonInteractionDelegate"
+ "setResetHandler:"
+ "setStoppedHandler:"
+ "startAndReturnError:"
+ "v24@0:8^{__IOHIDEvent=}16"
+ "Camera"
+ "touch"
+ "createPlayerWithPattern:error:"
+ "isCancelled"
+ "_touchButtonParameters"
+ "playHaptic"
+ "touchButtonParameters"
+ "numberWithInteger:"
+ "Unable to play haptic with error: %!@(MISSING)"
+ "setValue:"
+ "value"
+ "DATouchButtonTargetEvent"
+ "Tq,N,V_eventType"
+ "_eventType"
+ "setTouchButtonParameters:"
+ "v32@?0^{__IOHIDEvent=}8Q16^B24"
+ "DAHIDEventMonitorDelegate"
+ "T@\"CHHapticEngine\",&,N,V_hapticEngine"
+ "integerValue"
+ "setTargetEvents:"
+ "@\"CHHapticEngine\""
+ "startWithCompletionHandler:"
+ "_isInputMonitoringPaused"
+ "v16@?0@\"NSError\"8"
+ "positionY"
+ "initWithConfigurations:delegate:"
+ "@\"DATouchButtonParameters\""
+ "Haptic engine stoped for reason %!l(MISSING)d"
+ "_cameraCaptureShutterConfigurationWithOptionsProvider:"
+ "setIsInputMonitoringPaused:"
+ "stopWithCompletionHandler:"
+ "setEventType:"
+ "Found touch sensitive button event %!@(MISSING)"
+ "TB,N,V_performHapticOnEvent"
+ "$\x14"
+ "initAndReturnError:"
+ "initWithDictionary:error:"
+ "isCheckerBoardActive"
+ "_value"
+ "enableTouchButtonEvents"
+ "Failed to initialize haptic engine with error: %!@(MISSING)"
+ "v40@0:8@\"_UIPhysicalButtonInteraction\"16@\"_UIPhysicalButtonAction\"24@\"NSArray\"32"
+ "dk_boolFromKey:defaultValue:failed:"
+ "setPerformHapticOnEvent:"
+ "T@\"DATouchButtonParameters\",&,N,V_touchButtonParameters"
+ "\t"
+ "performHapticOnEvent"
+ "DATouchButtonParameters"
+ "_targetEvents"
+ "isInputMonitoringPaused"
+ "_performHapticOnEvent"
+ "setHapticEngine:"
+ "T@\"NSArray\",&,N,V_targetEvents"
+ "_physicalButtonInteraction:handleAction:withActiveActions:"
+ "v24@0:8q16"
+ "TB,N,V_isInputMonitoringPaused"
+ "disableTouchButtonEvents"
+ "numberWithLong:"
+ "Failed to start haptic engine after reset with error: %!@(MISSING)"
+ "@\"NSNumber\""
+ "isFinished"
+ "v40@0:8@16@24@32"
+ "eventData"
+ "stage"
+ "addInteraction:"
+ "q16@?0@\"NSError\"8"
+ "arrayWithObjects:count:"
+ "_hapticEngine"
- "\b"
- "$\x13"

```
