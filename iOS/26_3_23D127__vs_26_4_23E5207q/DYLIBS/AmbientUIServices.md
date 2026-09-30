## AmbientUIServices

> `/System/Library/PrivateFrameworks/AmbientUIServices.framework/AmbientUIServices`

```diff

-81.0.0.0.0
-  __TEXT.__text: 0x8ac
-  __TEXT.__auth_stubs: 0x170
+81.4.1.0.0
+  __TEXT.__text: 0x914
+  __TEXT.__auth_stubs: 0x150
   __TEXT.__objc_methlist: 0x2ac
   __TEXT.__const: 0x48
   __TEXT.__cstring: 0xb6

   __DATA_CONST.__objc_selrefs: 0x1a0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xc0
+  __AUTH_CONST.__auth_got: 0xb0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x638

   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EA8C2D35-57FE-33B2-BA60-D4FC738C9EE2
+  UUID: B6986A59-79F7-3CD0-9509-58FB47E0CC49
   Functions: 27
-  Symbols:   181
+  Symbols:   179
   CStrings:  114
 
Symbols:
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ -[UITraitCollection(AmbientPresentation) isAmbientPresented] : 80 -> 84
~ +[AMUIAmbientPresentationSceneExtension settingsExtensions] : 128 -> 132
~ +[AMUIAmbientPresentationSceneExtension clientComponents] : 128 -> 132
~ -[AMUIAmbientPresentationSceneClientComponent setScene:] : 272 -> 260
~ -[AMUIAmbientPresentationSceneClientComponent dealloc] : 116 -> 120
~ -[AMUIAmbientPresentationSceneClientComponent scene:didUpdateSettings:] : 332 -> 348
~ ___71-[AMUIAmbientPresentationSceneClientComponent scene:didUpdateSettings:]_block_invoke : 164 -> 152
~ -[AMUIAmbientPresentationSceneClientComponent _isAmbientPresentedForScene:] : 88 -> 92
~ -[AMUIAmbientPresentationSceneClientComponent _ambientDisplayStyleForScene:] : 88 -> 92
~ -[AMUIAmbientPresentationSceneClientComponent _updateAmbientTraitsForWindowScene:] : 240 -> 260
~ _AMUIServicesLogGeneral : 68 -> 84
~ +[AMUIAmbientPresentationSettingsExtension protocol] : 12 -> 60
~ -[UITraitCollection(AmbientPresentation) ambientDisplayStyle] : 76 -> 80

```
