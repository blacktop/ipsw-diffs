## com.apple.Terminal

> `/System/Library/Accessibility/BundlesBase/com.apple.Terminal.axbundle/Versions/A/com.apple.Terminal`

```diff

-287.6.0.0.0
-  __TEXT.__text: 0x2618
+287.6.4.0.0
+  __TEXT.__text: 0x2630
   __TEXT.__auth_stubs: 0x1a0
   __TEXT.__objc_stubs: 0x820
   __TEXT.__objc_methlist: 0x1d4

   __TEXT.__const: 0x30
   __TEXT.__gcc_except_tab: 0x104
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x1a0
+  __TEXT.__unwind_info: 0x1a8
   __DATA_CONST.__auth_got: 0xe0
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9F8A93F2-39A9-3F16-A894-B1C1FBBF1EA5
-  Functions: 68
-  Symbols:   243
+  UUID: D3C06A95-7035-39AC-93B6-D9F7B6BAC2C2
+  Functions: 69
+  Symbols:   244
   CStrings:  182
 
Symbols:
+ axcTerminalLog.cold.1
Functions:
~ +[TTKeyMappingsControllerAccessibility accessibilitySetupExistingObjects] : 540 -> 544
~ -[TTKeyMappingsControllerAccessibility _axcInitAccessibility] : 480 -> 488
~ -[TTViewAccessibility accessibilityNumberOfCharacters] : 652 -> 656
~ -[TTViewAccessibility _axcLogicalScreen] : 332 -> 336
~ _axcTerminalLog : 84 -> 68

```
