## MusicSettings

> `/System/Library/AccessibilityBundles/MusicSettings.axbundle/MusicSettings`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x5a8
-  __TEXT.__auth_stubs: 0x140
+3005.16.0.0.0
+  __TEXT.__text: 0x5d0
+  __TEXT.__auth_stubs: 0x130
   __TEXT.__objc_methlist: 0xc4
   __TEXT.__cstring: 0xf3
   __TEXT.__const: 0x8

   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xf0
-  __AUTH_CONST.__auth_got: 0xb0
+  __AUTH_CONST.__auth_got: 0xa8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ECA0AC33-BC6C-3879-ADDC-819A7A5EDD17
+  UUID: BCC73918-4190-3F3D-ADF0-650822FC31DC
   Functions: 19
-  Symbols:   114
+  Symbols:   113
   CStrings:  62
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
Functions:
~ _accessibilityMusicSettingsLocalizedString : 176 -> 184
~ +[AXMusicSettingsGlue accessibilityInitializeBundle] : 164 -> 168
~ ___52+[AXMusicSettingsGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ -[MusicCrossFadeDurationCellAccessibility accessibilityValue] : 148 -> 160
~ -[MusicCrossFadeDurationCellAccessibility _axIncrementSlider:] : 404 -> 408
~ -[MusicCrossFadeDurationCellAccessibility _axSlider] : 160 -> 168

```
