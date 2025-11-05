## AccessibilityEvents

> `/System/Library/PrivateFrameworks/AccessibilitySupport.framework/Versions/A/Frameworks/AccessibilityEvents.framework/Versions/A/AccessibilityEvents`

```diff

-387.5.2.0.0
-  __TEXT.__text: 0x15dec
+387.7.3.0.0
+  __TEXT.__text: 0x15d74
   __TEXT.__auth_stubs: 0x900
-  __TEXT.__objc_methlist: 0x232c
+  __TEXT.__objc_methlist: 0x25f4
   __TEXT.__const: 0x190
   __TEXT.__cstring: 0xb70
   __TEXT.__oslogstring: 0x326
-  __TEXT.__gcc_except_tab: 0x2a4
+  __TEXT.__gcc_except_tab: 0x298
   __TEXT.__ustring: 0x7e
-  __TEXT.__unwind_info: 0x6b0
+  __TEXT.__unwind_info: 0x6a8
   __TEXT.__objc_classname: 0x3fa
   __TEXT.__objc_methname: 0x65ff
   __TEXT.__objc_methtype: 0x10a4

   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1658
+  __DATA_CONST.__objc_selrefs: 0x16e0
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x78
   __AUTH_CONST.__auth_got: 0x490
   __AUTH_CONST.__const: 0x4b0
   __AUTH_CONST.__cfstring: 0x1740
-  __AUTH_CONST.__objc_const: 0x7008
+  __AUTH_CONST.__objc_const: 0x6b20
   __AUTH_CONST.__objc_intobj: 0x12d8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /System/Library/PrivateFrameworks/MultitouchSupport.framework/Versions/A/MultitouchSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 31C6F330-68D3-3BF3-98E6-E0BE1730AF11
-  Functions: 849
-  Symbols:   2380
+  UUID: 1F18DA46-0F32-3D16-96BF-C58F0DE92E62
+  Functions: 858
+  Symbols:   2393
   CStrings:  1773
 
Symbols:
+ +[AXEEventTap _eventTapIDQueue].cold.1
+ +[AXEEventTapManager _cgPriorityStringForAXEPriority:].cold.1
+ +[AXEEventTapManager sharedTapManagerAtLevel:].cold.1
+ +[AXEKeyboard modifierFlagTable].cold.1
+ +[AXEPhysicalMouse _mouseHIDReportDescriptorData].cold.1
+ +[AXEVirtualKeyboard _cgEventFlagsForModifier:].cold.1
+ -[AXEEventTap _createEventTapThreadIfNeeded].cold.2
+ AXEFixedGlyphForMacKeyCode.cold.1
+ AXEGlyphForMacKeyCode.cold.1
+ AXEGlyphForPureModifierFlags.cold.1
+ AXEMacKeyCodeFromUSBKeyCode.cold.1
+ _AXEMacKeyCodeToUSBKeyCodeMapping.cold.1
+ _AXEPureModifierFlagsByMacKeyCode.cold.1

```
