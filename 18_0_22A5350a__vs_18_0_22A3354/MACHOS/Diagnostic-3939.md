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
+ __UIEventHIDEnumerateChildren
+ _OBJC_CLASS_$_CHHapticEngine
+ _OBJC_CLASS_$_DATouchButtonParameters
+ _OBJC_CLASS_$_NSArray
+ _CHHapticEventTypeHapticTransient
+ _OBJC_CLASS_$_DATouchButtonTargetEvent
+ _OBJC_CLASS_$__UIPhysicalButtonConfiguration
+ _IOHIDEventGetType
+ _CHHapticPatternKeyEvent
+ _IOHIDEventGetFloatValue
+ _CHHapticPatternKeyTime
+ _OBJC_METACLASS_$_DATouchButtonParameters
+ _OBJC_CLASS_$__UIPhysicalButtonInteraction
+ _OBJC_METACLASS_$_DATouchButtonTargetEvent
+ __UIEventHIDGetChildForceStageEvent
+ _IOHIDEventGetChildren
+ _CHHapticPatternKeyPattern
+ _OBJC_CLASS_$_CBSUtilities
+ _OBJC_CLASS_$_CHHapticPattern
+ _DAIdentifierCamera
+ _IOHIDEventGetIntegerValue
+ _CHHapticPatternKeyEventType
+ _dispatch_get_global_queue
+ _IOHIDEventConformsTo
+ _CHHapticPatternKeyEventDuration
+ _DATypeTouchButton
CStrings:
+ "Found touch sensitive button event %!@(MISSING)"
+ "v16@?0@\"NSError\"8"
+ "v24@0:8q16"
+ "T@\"CHHapticEngine\",&,N,V_hapticEngine"
+ "@\"NSNumber\""
+ "TB,N,V_isInputMonitoringPaused"
+ "dk_boolFromKey:defaultValue:failed:"
+ "isFinished"
+ "enableTouchButtonEvents"
+ "_eventType"
+ "notifyWhenPlayersFinished:"
+ "DATouchButtonParameters"
+ "isCheckerBoardActive"
+ "_cameraCaptureShutterConfigurationWithOptionsProvider:"
+ "Haptic engine was reset"
+ "setEventType:"
+ "Tq,N,V_eventType"
+ "setResetHandler:"
+ "_isInputMonitoringPaused"
+ "initWithConfigurations:delegate:"
+ "isCancelled"
+ "@\"CHHapticEngine\""
+ "integerValue"
+ "v32@?0^{__IOHIDEvent=}8Q16^B24"
+ "setStoppedHandler:"
+ "value"
+ "T@\"NSArray\",&,N,V_targetEvents"
+ "_touchButtonParameters"
+ "setupTouchButtonInteractions"
+ "\t"
+ "numberWithLong:"
+ "$\x14"
+ "stage"
+ "startAtTime:error:"
+ "positionY"
+ "targetEvents"
+ "v40@0:8@\"_UIPhysicalButtonInteraction\"16@\"_UIPhysicalButtonAction\"24@\"NSArray\"32"
+ "v40@0:8@16@24@32"
+ "q16@?0@\"NSError\"8"
+ "v16@?0q8"
+ "setValue:"
+ "setTargetEvents:"
+ "Haptic engine stoped for reason %!l(MISSING)d"
+ "Unable to play haptic with error: %!@(MISSING)"
+ "numberWithInteger:"
+ "addInteraction:"
+ "Failed to initialize haptic engine with error: %!@(MISSING)"
+ "createPlayerWithPattern:error:"
+ "playHaptic"
+ "hapticEngine"
+ "setIsInputMonitoringPaused:"
+ "startAndReturnError:"
+ "setTouchButtonParameters:"
+ "startWithCompletionHandler:"
+ "stopWithCompletionHandler:"
+ "_UIPhysicalButtonInteractionDelegate"
+ "Camera"
+ "_hapticEngine"
+ "touch"
+ "arrayWithObjects:count:"
+ "T@\"DATouchButtonParameters\",&,N,V_touchButtonParameters"
+ "isInputMonitoringPaused"
+ "touchButtonParameters"
+ "_targetEvents"
+ "@\"DATouchButtonParameters\""
+ "Failed to start haptic engine after reset with error: %!@(MISSING)"
+ "_performHapticOnEvent"
+ "initAndReturnError:"
+ "T@\"NSNumber\",&,N,V_value"
+ "TouchButton"
+ "disableTouchButtonEvents"
+ "TB,N,V_performHapticOnEvent"
+ "initWithDictionary:error:"
+ "setHapticEngine:"
+ "v24@0:8^{__IOHIDEvent=}16"
+ "_physicalButtonInteraction:handleAction:withActiveActions:"
+ "performHapticOnEvent"
+ "DATouchButtonTargetEvent"
+ "numberWithFloat:"
+ "DAHIDEventMonitorDelegate"
+ "setPerformHapticOnEvent:"
+ "_value"
+ "eventData"
- "\b"
- "$\x13"

```
