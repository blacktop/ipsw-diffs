## AccessibilityUIViewServices

> `/System/Library/PrivateFrameworks/AccessibilityUIViewServices.framework/AccessibilityUIViewServices`

```diff

-3191.7.24.0.0
-  __TEXT.__text: 0x720
+3191.19.0.0.0
+  __TEXT.__text: 0x798
   __TEXT.__auth_stubs: 0xb0
   __TEXT.__objc_methlist: 0x194
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x142
-  __TEXT.__unwind_info: 0xa0
+  __TEXT.__unwind_info: 0xb8
   __TEXT.__objc_classname: 0xd9
   __TEXT.__objc_methname: 0x6f
   __TEXT.__objc_methtype: 0x8

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 66831C3F-E352-3D0C-8952-DB689A9ACFF8
+  UUID: AE0F888C-1729-37CC-803B-8F4CB5EAD2F2
   Functions: 25
   Symbols:   134
   CStrings:  32
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
Functions:
~ +[AXVSVoiceOverImageExplorerService sharedInstance] : 160 -> 176
~ +[AXVSAudiographService sharedInstance] : 160 -> 176
~ +[AXCACCorrectionsService sharedInstance] : 160 -> 176
~ +[AXVSVoiceOverQuickSettingsService sharedInstance] : 160 -> 176
~ +[AXVSVoiceOverItemChooserService sharedInstance] : 160 -> 176
~ -[AXVSBaseService sb_alertDefinition] : 136 -> 144
~ +[AXVSOnboardingService sharedInstance] : 160 -> 176
~ +[AXCACCustomCommandEditorService sharedInstance] : 160 -> 176

```
