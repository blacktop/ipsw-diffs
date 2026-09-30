## MobileTimer-Assistant

> `/System/Library/AccessibilityBundles/MobileTimer-Assistant.axbundle/MobileTimer-Assistant`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xd00
-  __TEXT.__auth_stubs: 0x1c0
+3005.16.0.0.0
+  __TEXT.__text: 0xdd8
+  __TEXT.__auth_stubs: 0x1a0
   __TEXT.__objc_methlist: 0x16c
   __TEXT.__cstring: 0x2fd
   __TEXT.__unwind_info: 0xb8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x138
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xe8
+  __AUTH_CONST.__auth_got: 0xd8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x440
   __AUTH_CONST.__objc_const: 0x510

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F3326532-C3AF-3760-8C74-286E167C04B8
+  UUID: 476BD2A5-6EE8-35BF-BEF4-B6EF6E648461
   Functions: 27
-  Symbols:   186
+  Symbols:   184
   CStrings:  130
 
Symbols:
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXTimerAssistantUIGlue accessibilityInitializeBundle] : 148 -> 152
~ ___55+[AXTimerAssistantUIGlue accessibilityInitializeBundle]_block_invoke : 424 -> 428
~ ___55+[AXTimerAssistantUIGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___55+[AXTimerAssistantUIGlue accessibilityInitializeBundle]_block_invoke_3 : 132 -> 140
~ _accessibilityLocalizedString : 176 -> 184
~ -[MobileTimerAssistantAlarmSnippetCellAccessibility accessibilityLabel] : 564 -> 620
~ -[MobileTimerAssistantAlarmSnippetCellAccessibility accessibilityTraits] : 156 -> 164
~ -[MobileTimerAssistantAlarmSnippetCellAccessibility accessibilityValue] : 116 -> 128
~ -[MobileTimerAssistantAlarmSnippetCellAccessibility accessibilityActivationPoint] : 104 -> 112
~ -[MobileTimerAssistantAlarmSnippetCellAccessibility init] : 156 -> 160
~ -[MobileTimerAssistantTimerSnippetCellAccessibility accessibilityLabel] : 228 -> 252
~ +[MobileTimerAssistantWorldClockSnippetCellAccessibility _accessibilityPerformValidations:] : 164 -> 172
~ -[MobileTimerAssistantWorldClockSnippetCellAccessibility accessibilityLabel] : 360 -> 400
~ -[MobileTimerAssistantWorldClockSnippetCellAccessibility accessibilityValue] : 140 -> 156
~ -[TimerSnippetTimeViewAccessibility updateDisplayWithTime:] : 228 -> 240

```
