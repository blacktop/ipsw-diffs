## CompanionStingSettings

> `/System/Library/AccessibilityBundles/CompanionStingSettings.axbundle/CompanionStingSettings`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x294
-  __TEXT.__auth_stubs: 0xb0
+3005.16.0.0.0
+  __TEXT.__text: 0x2b0
+  __TEXT.__auth_stubs: 0xa0
   __TEXT.__objc_methlist: 0x74
   __TEXT.__cstring: 0x14c
   __TEXT.__unwind_info: 0x78

   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x98
-  __AUTH_CONST.__auth_got: 0x60
+  __AUTH_CONST.__auth_got: 0x58
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E0AF8FB5-BE82-3510-AD80-57D05C7F62DB
+  UUID: 7FBB359C-5254-35C8-837D-2E729D966FCA
   Functions: 11
-  Symbols:   77
+  Symbols:   76
   CStrings:  51
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
Functions:
~ -[CSLPRFStingGesturePaneCellAccessibility accessibilityLabel] : 132 -> 144
~ +[AXCompanionStingSettingsGlue accessibilityInitializeBundle] : 148 -> 152
~ ___61+[AXCompanionStingSettingsGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ _accessibilityLocalizedString : 176 -> 184

```
