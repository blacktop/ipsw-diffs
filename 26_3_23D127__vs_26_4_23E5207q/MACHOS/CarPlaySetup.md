## CarPlaySetup

> `/Applications/CarPlaySetup.app/CarPlaySetup`

```diff

-746.24.2.0.0
-  __TEXT.__text: 0x7d04
-  __TEXT.__auth_stubs: 0x390
+774.8.0.0.0
+  __TEXT.__text: 0x8180
+  __TEXT.__auth_stubs: 0x360
   __TEXT.__objc_stubs: 0x12a0
   __TEXT.__objc_methlist: 0xc34
   __TEXT.__const: 0x68
-  __TEXT.__oslogstring: 0xbe7
-  __TEXT.__objc_classname: 0x1b7
-  __TEXT.__objc_methname: 0x2b99
-  __TEXT.__objc_methtype: 0x115f
+  __TEXT.__objc_methname: 0x2bab
   __TEXT.__cstring: 0x1a9
-  __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__unwind_info: 0x240
-  __DATA_CONST.__auth_got: 0x1d8
+  __TEXT.__oslogstring: 0xc12
+  __TEXT.__objc_classname: 0x1b7
+  __TEXT.__objc_methtype: 0x1194
+  __TEXT.__gcc_except_tab: 0x58
+  __TEXT.__unwind_info: 0x258
+  __DATA_CONST.__auth_got: 0x1c0
   __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x400
+  __DATA_CONST.__const: 0x428
   __DATA_CONST.__cfstring: 0x160
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x50

   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6FE3B9EF-2853-36B6-B435-CF5060106B92
-  Functions: 188
-  Symbols:   121
-  CStrings:  566
+  UUID: 4B9C7A66-6BBE-3622-9F6B-BF7278050DB2
+  Functions: 190
+  Symbols:   118
+  CStrings:  569
 
Symbols:
+ _OBJC_CLASS_$_CARSetupOnboardingViewController
+ _objc_release_x25
+ _objc_retainAutoreleasedReturnValue
- _OBJC_CLASS_$_CARSetupAssetReadyViewController
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
CStrings:
+ "Onboarding prompt confirmed"
+ "dismissing generic card presentation"
+ "initWithFeatures:doneHandler:"
+ "present CarPlay Onboarding prompt for vehicle name: %@"
+ "presentOnboardingPromptForVehicleName:features:appClipIDs:confirmationHandler:"
+ "promptDirector:wantsToPresentOnboardingPromptForVehicleName:features:appClipIDs:confirmationHandler:"
+ "v48@0:8@\"NSString\"16Q24@\"NSArray\"32@?<v@?B>40"
+ "v48@0:8@16Q24@32@?40"
+ "v56@0:8@\"CARSetupPromptDirector\"16@\"NSString\"24Q32@\"NSArray\"40@?<v@?B>48"
+ "v56@0:8@16@24Q32@40@?48"
- "asset ready prompt confirmed"
- "initWithAppsView:doneHandler:"
- "present asset ready prompt for vehicle name: %@"
- "presentAssetReadyPromptForVehicleName:appClipIDs:confirmationHandler:"
- "promptDirector:wantsToPresentAssetReadyPromptForVehicleName:appClipIDs:confirmationHandler:"
- "v40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?>32"
- "v48@0:8@\"CARSetupPromptDirector\"16@\"NSString\"24@\"NSArray\"32@?<v@?>40"

```
