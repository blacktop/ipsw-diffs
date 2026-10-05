## InvertColorsManager

> `/System/Library/AccessibilityBundles/InvertColorsManager.bundle/InvertColorsManager`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-3245.8.2.0.0
-  __TEXT.__text: 0x1f9c8
+3245.8.4.2.0
+  __TEXT.__text: 0x1fc5c
   __TEXT.__auth_stubs: 0x7f0
   __TEXT.__objc_stubs: 0x28c0
   __TEXT.__objc_methlist: 0x779c
-  __TEXT.__const: 0xc8
+  __TEXT.__const: 0xd0
   __TEXT.__dlopen_cstrs: 0x6a
   __TEXT.__gcc_except_tab: 0x1d8
   __TEXT.__objc_classname: 0xa17e
   __TEXT.__cstring: 0x8cc4
   __TEXT.__objc_methname: 0x2cfb
   __TEXT.__objc_methtype: 0x334
-  __TEXT.__oslogstring: 0xb76
+  __TEXT.__oslogstring: 0xdb4
   __TEXT.__unwind_info: 0x11c8
   __DATA_CONST.__const: 0x818
   __DATA_CONST.__cfstring: 0x8d00

   - /usr/lib/libobjc.A.dylib
   Functions: 1917
   Symbols:   1893
-  CStrings:  2137
+  CStrings:  2142
 
Functions:
~ sub_115a0 : 116 -> 308
~ sub_11614 -> sub_116d4 : 116 -> 212
~ sub_18840 -> sub_18960 : 116 -> 264
~ sub_188b4 -> sub_18a68 : 168 -> 392
CStrings:
+ "CAMSecureWindow: isInHostedDarkWindow=YES window=%@"
+ "CAMSecureWindow: locked + dark — opting OUT of own window-level dark invert, deferring to SB counter-invert. window=%@"
+ "CAMSecureWindow: supportsDarkWindowInvert=YES (screenLocked=%d darkModeActive=%d) window=%@"
+ "SBDeviceApplicationSceneView: _accessibilityLoadInvertColors shouldCounter=%d window=%@ windowClass=%@ invertColorsEnabled=%d isDarkWindow=%d supportsDarkWindowInvert=%d sceneView=%@"
+ "SBDeviceApplicationSceneView: _axShouldCounterCoverSheetDarkWindowInvert=%d globalSmartInvertDrivesDisplayFilter=%d window=%@"
```
