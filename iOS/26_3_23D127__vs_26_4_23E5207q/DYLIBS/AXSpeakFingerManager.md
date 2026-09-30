## AXSpeakFingerManager

> `/System/Library/PrivateFrameworks/AXSpeakFingerManager.framework/AXSpeakFingerManager`

```diff

-3191.7.24.0.0
-  __TEXT.__text: 0x144c
+3191.19.0.0.0
+  __TEXT.__text: 0x1680
   __TEXT.__auth_stubs: 0x2d0
   __TEXT.__objc_methlist: 0x48c
   __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0x2c
   __TEXT.__cstring: 0x175
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0xd0
+  __TEXT.__unwind_info: 0x100
   __TEXT.__objc_classname: 0x52
   __TEXT.__objc_methname: 0x10fe
   __TEXT.__objc_methtype: 0x5e0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8FDBB225-7B90-3ABF-BEDF-77F1202B7607
+  UUID: 9EDBBD0E-B6C1-3AC7-BC5C-AB4490BD6193
   Functions: 48
   Symbols:   292
   CStrings:  274
Symbols:
+ _objc_release_x28
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x24
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_release_x27
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x8
Functions:
~ +[AXSpeakFingerManager sharedInstance] : 160 -> 176
~ -[AXSpeakFingerManager init] : 500 -> 508
~ -[AXSpeakFingerManager dealloc] : 144 -> 152
~ -[AXSpeakFingerManager speakElementAtLocation:] : 1592 -> 1676
~ -[AXSpeakFingerManager _updateFocusRingForWebElement:remove:] : 388 -> 400
~ -[AXSpeakFingerManager setCursorFrame:withPath:withContextId:element:forceRefresh:animated:] : 388 -> 400
~ -[AXSpeakFingerManager userManuallyExitedSpeakUnderFingerMode] : 368 -> 384
~ -[AXSpeakFingerManager _removeFocusRingForElement:] : 132 -> 140
~ -[AXSpeakFingerManager _speakFingerStateChanged] : 72 -> 76
~ -[AXSpeakFingerManager registerBlockForStateChange:] : 116 -> 120
~ -[AXSpeakFingerManager setElementsForUnitTests:] : 12 -> 64
~ -[AXSpeakFingerManager setStateUpdateBlocks:] : 12 -> 64
~ -[AXSpeakFingerManager setCurrentSpeakFingerElement:] : 12 -> 64
~ -[AXSpeakFingerManager setOrator:] : 12 -> 64
~ -[AXSpeakFingerManager setLastSpeakUnderFingerPhrase:] : 12 -> 64
~ -[AXSpeakFingerManager setHapticGenerator:] : 12 -> 64
~ -[AXSpeakFingerManager setSpringBoardActionHandlerId:] : 12 -> 64
~ _AXSpeakFingerBundle : 68 -> 84
~ ___AXSpeakFingerBundle_block_invoke : 92 -> 96
~ _AXSpeakFingerLocString : 112 -> 120

```
