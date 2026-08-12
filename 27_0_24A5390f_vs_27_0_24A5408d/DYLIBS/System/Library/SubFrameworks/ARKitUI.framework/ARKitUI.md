## ARKitUI

> `/System/Library/SubFrameworks/ARKitUI.framework/ARKitUI`

```diff

-781.0.4.0.0
-  __TEXT.__text: 0x2b150
-  __TEXT.__objc_methlist: 0x2910
-  __TEXT.__const: 0x948
-  __TEXT.__oslogstring: 0x18d2
+781.0.7.0.0
+  __TEXT.__text: 0x2b478
+  __TEXT.__objc_methlist: 0x2950
+  __TEXT.__const: 0x938
   __TEXT.__cstring: 0xdb4
+  __TEXT.__oslogstring: 0x1830
   __TEXT.__gcc_except_tab: 0xcd8
-  __TEXT.__unwind_info: 0xc10
+  __TEXT.__unwind_info: 0xc18
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2248
+  __DATA_CONST.__objc_selrefs: 0x2288
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__got: 0x590
   __AUTH_CONST.__const: 0x3a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 972
-  Symbols:   3032
-  CStrings:  234
+  Functions: 979
+  Symbols:   3047
+  CStrings:  230
 
Symbols:
+ -[ARCoachingAnimationView buildRendererForGoal:glyph:]
+ -[ARCoachingAnimationView startCoachingAnimation:camera:]
+ -[ARCoachingAnimationView teardownRenderer]
+ -[ARSCNView _abandonStuckRotationGateIfNeeded]
+ -[ARSCNView _removeRotationSnapshot]
+ -[ARSCNView _windowDidRotate:]
+ _ARCoachingLoadDeviceGlyphWithName
+ _ARDeviceName
+ ___46-[ARSCNView _abandonStuckRotationGateIfNeeded]_block_invoke
+ ___54-[ARCoachingAnimationView buildRendererForGoal:glyph:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ _objc_msgSend$_abandonStuckRotationGateIfNeeded
+ _objc_msgSend$_removeRotationSnapshot
+ _objc_msgSend$buildRendererForGoal:glyph:
+ _objc_msgSend$layoutIfNeeded
+ _objc_msgSend$performWithoutAnimation:
+ _objc_msgSend$setNeedsLayout
+ _objc_msgSend$startCoachingAnimation:camera:
+ _objc_msgSend$teardownRenderer
- -[ARCoachingAnimationView startCoachingAnimation:]
- ___50-[ARCoachingAnimationView startCoachingAnimation:]_block_invoke
- ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
- _objc_msgSend$startCoachingAnimation:
CStrings:
+ "%{public}@ <%p>: Loading coaching glyph %@ for %@"
- "Loading glyph for iPad with home button"
- "Loading glyph for iPad without home button"
- "Loading glyph for iPhone device with home button"
- "Loading glyph for iPhone device with notch"
- "Loading glyph for iPhone with island"
```
