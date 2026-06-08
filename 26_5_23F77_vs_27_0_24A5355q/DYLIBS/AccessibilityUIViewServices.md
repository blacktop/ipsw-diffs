## AccessibilityUIViewServices

> `/System/Library/PrivateFrameworks/AccessibilityUIViewServices.framework/AccessibilityUIViewServices`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x798
-  __TEXT.__auth_stubs: 0xb0
+3229.1.6.0.0
+  __TEXT.__text: 0x720
   __TEXT.__objc_methlist: 0x194
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x142
-  __TEXT.__unwind_info: 0xb8
-  __TEXT.__objc_classname: 0xd9
-  __TEXT.__objc_methname: 0x6f
-  __TEXT.__objc_methtype: 0x8
-  __TEXT.__objc_stubs: 0x60
-  __DATA_CONST.__got: 0x18
+  __TEXT.__unwind_info: 0xa0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x20
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x60
+  __DATA_CONST.__got: 0x18
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x480
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x280
   __DATA.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 98ACAB5B-618F-3B53-8C52-EB091F055989
+  UUID: 15C8AD33-8CBF-3E72-A426-1DAE7955921B
   Functions: 25
   Symbols:   134
-  CStrings:  32
+  CStrings:  18
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _sharedInstance.onceToken.21
+ _sharedInstance.onceToken.36
+ _sharedInstance.onceToken.51
+ _sharedInstance.onceToken.6
+ _sharedInstance.onceToken.77
+ _sharedInstance.onceToken.92
+ _sharedInstance.sharedInstance.22
+ _sharedInstance.sharedInstance.37
+ _sharedInstance.sharedInstance.52
+ _sharedInstance.sharedInstance.7
+ _sharedInstance.sharedInstance.78
+ _sharedInstance.sharedInstance.93
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[AXVSVoiceOverImageExplorerService sharedInstance] : 176 -> 160
~ +[AXVSAudiographService sharedInstance] : 176 -> 160
~ +[AXCACCorrectionsService sharedInstance] : 176 -> 160
~ +[AXVSVoiceOverQuickSettingsService sharedInstance] : 176 -> 160
~ +[AXVSVoiceOverItemChooserService sharedInstance] : 176 -> 160
~ -[AXVSBaseService sb_alertDefinition] : 144 -> 136
~ +[AXVSOnboardingService sharedInstance] : 176 -> 160
~ +[AXCACCustomCommandEditorService sharedInstance] : 176 -> 160
CStrings:
- "@16@0:8"
- "AXCACCorrectionsService"
- "AXCACCustomCommandEditorService"
- "AXVSAudiographService"
- "AXVSBaseService"
- "AXVSOnboardingService"
- "AXVSVoiceOverImageExplorerService"
- "AXVSVoiceOverItemChooserService"
- "AXVSVoiceOverQuickSettingsService"
- "initWithServiceName:viewControllerClassName:"
- "sb_alertDefinition"
- "sb_initialClassName"
- "serviceName"
- "sharedInstance"

```
