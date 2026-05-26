## NTKCustomization

> `/System/Library/AccessibilityBundles/NTKCustomization.axbundle/NTKCustomization`

```diff

-1001.19.0.0.0
-  __TEXT.__text: 0xfa20
-  __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_stubs: 0x1d40
-  __TEXT.__objc_methlist: 0x186c
+1001.20.0.0.0
+  __TEXT.__text: 0xfc8c
+  __TEXT.__auth_stubs: 0x5e0
+  __TEXT.__objc_stubs: 0x1da0
+  __TEXT.__objc_methlist: 0x18cc
   __TEXT.__objc_classname: 0x11c1
-  __TEXT.__cstring: 0x35e5
-  __TEXT.__objc_methname: 0x245a
-  __TEXT.__objc_methtype: 0x21d
+  __TEXT.__cstring: 0x3622
+  __TEXT.__objc_methname: 0x25cd
+  __TEXT.__objc_methtype: 0x228
   __TEXT.__const: 0xa8
   __TEXT.__gcc_except_tab: 0x368
-  __TEXT.__unwind_info: 0x638
-  __DATA_CONST.__auth_got: 0x2f0
-  __DATA_CONST.__got: 0x198
+  __TEXT.__unwind_info: 0x640
+  __DATA_CONST.__auth_got: 0x300
+  __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__const: 0x440
-  __DATA_CONST.__cfstring: 0x3d60
+  __DATA_CONST.__cfstring: 0x3da0
   __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA.__objc_const: 0x3e78
-  __DATA.__objc_selrefs: 0xa38
+  __DATA.__objc_selrefs: 0xa80
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x2260
   __DATA.__data: 0x1a8

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0EC62247-899D-340D-B2B9-23FEF0E0BBB8
-  Functions: 525
-  Symbols:   1535
-  CStrings:  1493
+  UUID: 23A06993-EC6E-3AA1-9A2D-90CAF17398B9
+  Functions: 533
+  Symbols:   1550
+  CStrings:  1507
 
Symbols:
+ -[NTKComplicationDisplayWrapperViewAccessibility _accessibilityAutoSpeakAction]
+ -[NTKComplicationDisplayWrapperViewAccessibility _accessibilityDisableAutoSpeak]
+ -[NTKComplicationDisplayWrapperViewAccessibility _accessibilityEnableAutoSpeak]
+ -[NTKComplicationDisplayWrapperViewAccessibility _accessibilitySelectedComplicationHasAutoSpeakEnabled]
+ -[NTKComplicationDisplayWrapperViewAccessibility _accessibilitySetAutoSpeakAction:]
+ -[NTKComplicationDisplayWrapperViewAccessibility _accessibilityShouldUseDescendantsForWatchAutoSpeak]
+ -[NTKComplicationDisplayWrapperViewAccessibility _accessibilityToggleAutoSpeak:]
+ -[NTKComplicationDisplayWrapperViewAccessibility accessibilityCustomActions]
+ _AXGuaranteedMutableArray
+ _OBJC_CLASS_$_AXSettings
+ _UIAccessibilitySpeakOrQueueIfNeeded
+ ___NTKComplicationDisplayWrapperViewAccessibility___accessibilityAutoSpeakAction
+ _objc_msgSend$_accessibilityToggleAutoSpeak:
+ _objc_msgSend$gizmoGetAutoSpeakEnabledForComplication:slot:face:
+ _objc_msgSend$gizmoSetAutoSpeakEnabledForComplication:slot:face:toggle:
CStrings:
+ "B20@0:8B16"
+ "_accessibilityAutoSpeakAction"
+ "_accessibilityDisableAutoSpeak"
+ "_accessibilityEnableAutoSpeak"
+ "_accessibilitySelectedComplicationHasAutoSpeakEnabled"
+ "_accessibilitySetAutoSpeakAction:"
+ "_accessibilityShouldUseDescendantsForWatchAutoSpeak"
+ "_accessibilityToggleAutoSpeak:"
+ "autospeak.disable.confirmation"
+ "autospeak.enable.confirmation"
+ "gizmoGetAutoSpeakEnabledForComplication:slot:face:"
+ "gizmoSetAutoSpeakEnabledForComplication:slot:face:toggle:"

```
