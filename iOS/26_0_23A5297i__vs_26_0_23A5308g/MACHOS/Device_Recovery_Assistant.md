## Device Recovery Assistant

> `/Applications/Device Recovery Assistant.app/Device Recovery Assistant`

```diff

-88.0.0.0.4
-  __TEXT.__text: 0x106b0
+95.0.0.0.1
+  __TEXT.__text: 0x10b58
   __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_stubs: 0x3880
-  __TEXT.__objc_methlist: 0x1d48
+  __TEXT.__objc_stubs: 0x3a40
+  __TEXT.__objc_methlist: 0x1da0
   __TEXT.__const: 0x38
-  __TEXT.__objc_methname: 0x5b8f
-  __TEXT.__cstring: 0x1d99
-  __TEXT.__oslogstring: 0x2233
-  __TEXT.__objc_classname: 0x437
-  __TEXT.__objc_methtype: 0x207f
+  __TEXT.__objc_methname: 0x5cf1
+  __TEXT.__oslogstring: 0x22d2
+  __TEXT.__cstring: 0x1e41
+  __TEXT.__objc_classname: 0x439
+  __TEXT.__objc_methtype: 0x20c9
   __TEXT.__gcc_except_tab: 0x64
-  __TEXT.__unwind_info: 0x430
+  __TEXT.__unwind_info: 0x410
   __DATA_CONST.__auth_got: 0x328
-  __DATA_CONST.__got: 0x340
-  __DATA_CONST.__const: 0x6e8
-  __DATA_CONST.__cfstring: 0xbc0
+  __DATA_CONST.__got: 0x348
+  __DATA_CONST.__const: 0x718
+  __DATA_CONST.__cfstring: 0xc00
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA.__objc_const: 0x3748
-  __DATA.__objc_selrefs: 0x1698
-  __DATA.__objc_ivar: 0x104
+  __DATA.__objc_const: 0x3778
+  __DATA.__objc_selrefs: 0x1710
+  __DATA.__objc_ivar: 0x108
   __DATA.__objc_data: 0x6e0
   __DATA.__data: 0x978
   __DATA.__bss: 0x78

   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport
   - /System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter
-  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 78F68DCB-04BD-3964-9DA3-8D8F8A7F3DC7
-  Functions: 443
-  Symbols:   226
-  CStrings:  1592
+  UUID: 1CE4235D-E9AB-364C-AD76-CAF701210B5C
+  Functions: 449
+  Symbols:   227
+  CStrings:  1621
 
Symbols:
+ _OBJC_CLASS_$_BSPlatform
+ _OBJC_CLASS_$_NSUserDefaults
+ _UISDeviceContextDeviceClassKey
+ _UISDeviceContextHomeButtonTypeKey
- _OBJC_CLASS_$_MCProfileConnection
- _OBJC_CLASS_$_UIMutableApplicationSceneSettings
- _UIEdgeInsetsZero
CStrings:
+ "%{public}s: Language from mainOS is = %{public}@"
+ "%{public}s: Next button pressed. Calling didAuthenticate on delegate."
+ "%{public}s: Restarting DRE shell to pickup language change."
+ "%{public}s: Setting preferred language to: %{public}@"
+ "-[PasscodeViewController nextButtonPressed:]"
+ "-[SceneDelegate languageViewController:didChooseLanguageCodeWithRegion:]"
+ "@\"NSLocale\""
+ "@\"UIBarButtonItem\""
+ "NEXT_BUTTON_TITLE"
+ "T@\"NSLocale\",&,N,V_systemLocale"
+ "T@\"UIBarButtonItem\",&,V_nextItem"
+ "T@\"UIBarButtonItem\",&,V_spinnerItem"
+ "TB,D,N"
+ "_additionalSafeAreaInsets"
+ "_initializationContextWithDefaultSceneToken:"
+ "_newApplicationInitializationContext"
+ "_nextItem"
+ "_referenceBounds"
+ "_spinnerItem"
+ "_systemLocale"
+ "createInitialAppScene"
+ "deviceClass"
+ "dre-main-view"
+ "homeButtonType"
+ "languageCode"
+ "languageViewController:didChooseLanguageCodeWithRegion:"
+ "main"
+ "mainOSLanguageCode"
+ "nextButtonPressed:"
+ "nextItem"
+ "numberWithInt:"
+ "numberWithInteger:"
+ "passcode"
+ "persistentIdentifier"
+ "preferredLanguageCode"
+ "readSupportedLanguages"
+ "registerDefaults:"
+ "sceneIdentityTokenForIdentifier:workspaceIdentifier:"
+ "setDefaultSceneToken:"
+ "setDeviceInfoValue:forKey:"
+ "setDeviceOrientationEventsEnabled:"
+ "setNextItem:"
+ "setObject:forKey:"
+ "setSpinnerItem:"
+ "setSystemLocale:"
+ "spinnerItem"
+ "standardUserDefaults"
+ "stringForKey:"
+ "systemLocale"
+ "updateSettings:"
+ "v16@?0@\"<FBSceneManagerSceneCreating>\"8"
+ "v32@0:8@\"LanguageViewController\"16@\"NSString\"24"
+ "{UIEdgeInsets=dddd}16@0:8"
- "%{public}s: Did select language %{public}@ with guessed region %{public}@"
- "@\"FBScene\""
- "@44@0:8@16@24B32d36"
- "DREMainScene"
- "T@\"FBScene\",&,V_inputScene"
- "T@\"FBScene\",&,V_mainScene"
- "TB,N"
- "_inputScene"
- "_mainScene"
- "configureParameters:"
- "createSceneWithIdentifier:specification:isForeground:level:"
- "inputScene"
- "languageFromLanguage:byReplacingRegion:"
- "languageViewControllerDidChooseLanguage:"
- "mainScene"
- "readSsupportedLanguages"
- "regionCode"
- "setInputScene:"
- "setLocaleAfterLanguageChange:"
- "setMainScene:"
- "setSafeAreaInsetsPortrait:"
- "setStatusBarDisabled:"
- "setUnderLock:"
- "sharedConnection"
- "updateSettingsWithBlock:"
- "v16@?0@\"FBSMutableSceneParameters\"8"

```
