## AAUIViewService

> `/Applications/AAUIViewService.app/AAUIViewService`

```diff

-520.480.0.0.0
-  __TEXT.__text: 0x47e4
+540.1.0.0.0
+  __TEXT.__text: 0x55a0
   __TEXT.__auth_stubs: 0x340
-  __TEXT.__objc_stubs: 0xe40
-  __TEXT.__objc_methlist: 0x76c
-  __TEXT.__objc_methname: 0x1b6c
-  __TEXT.__objc_classname: 0xa5
-  __TEXT.__objc_methtype: 0xa8f
-  __TEXT.__const: 0x30
-  __TEXT.__oslogstring: 0x97b
-  __TEXT.__cstring: 0x288
+  __TEXT.__objc_stubs: 0x11e0
+  __TEXT.__objc_methlist: 0x7fc
+  __TEXT.__objc_methname: 0x1efa
+  __TEXT.__objc_classname: 0xa6
+  __TEXT.__objc_methtype: 0xace
+  __TEXT.__const: 0x40
+  __TEXT.__oslogstring: 0xc32
+  __TEXT.__cstring: 0x3be
   __TEXT.__gcc_except_tab: 0x64
-  __TEXT.__unwind_info: 0x1a0
+  __TEXT.__unwind_info: 0x1c0
   __DATA_CONST.__auth_got: 0x1b0
-  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__const: 0x230
-  __DATA_CONST.__cfstring: 0x200
+  __DATA_CONST.__cfstring: 0x280
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0xab8
-  __DATA.__objc_selrefs: 0x6c8
-  __DATA.__objc_ivar: 0x28
+  __DATA.__objc_const: 0xb18
+  __DATA.__objc_selrefs: 0x7d8
+  __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x120
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI
   - /System/Library/PrivateFrameworks/ChatKit.framework/ChatKit
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
+  - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /usr/lib/libCTGreenTeaLogger.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F2A4B651-97B4-37D5-8CF9-6AB7B4AEE99F
-  Functions: 128
-  Symbols:   117
-  CStrings:  425
+  UUID: 2DDD1102-89EE-3AA5-8058-4AC72BCA8E33
+  Functions: 146
+  Symbols:   127
+  CStrings:  492
 
Symbols:
+ _OBJC_CLASS_$_AAAgeMigrationController
+ _OBJC_CLASS_$_AAAgeMisconfiguredPromptContext
+ _OBJC_CLASS_$_AAMisconfiguredAgePromptViewModel
+ _OBJC_CLASS_$_AAUIFeatureFlags
+ _OBJC_CLASS_$_OBBoldTrayButton
+ _OBJC_CLASS_$_OBLinkTrayButton
+ _OBJC_CLASS_$_OBWelcomeController
+ _OBJC_CLASS_$_UIBarButtonItem
+ _OBJC_CLASS_$_UIImage
+ _OBJC_CLASS_$_UINavigationController
CStrings:
+ "%s: Persisting user action: %d"
+ "%s: Something went wrong with saving error: %@"
+ "%s: User tapped on %i in misconfigured age prompt. Navigate to kb article"
+ "%s: User tapped on %i in misconfigured age prompt. cancel out"
+ "%s: User tapped on %i in misconfigured age prompt. dismiss"
+ "%s: User tapped on %i in misconfigured age prompt. going to settings..."
+ "%s: User tapped on %i."
+ "%s: age migration model is nil.."
+ "%s: hmmm, something went wrong"
+ "%s: saved was successful"
+ "-[AAUIRemoteViewController _persistUserHaveSeenAlertWithAction:]"
+ "-[AAUIRemoteViewController _persistUserHaveSeenAlertWithAction:]_block_invoke"
+ "-[AAUIRemoteViewController _userActionResponse:]"
+ "@\"<AAAgeMigrationPromptModelProtocol>\""
+ "Cancel"
+ "Showing misconfigured age prompt"
+ "T@\"<AAAgeMigrationPromptModelProtocol>\",&,N,V_ageMigrationPromptModel"
+ "Take user to KB article about changing birthday"
+ "Taking user to account personal information"
+ "Tq,N,V_viewServiceFlowType"
+ "Unsupported ViewModel... please file a radar to Apple Account | Experience. Model typed: %@"
+ "_ageMigrationPromptModel"
+ "_displayMisconfiguredAgePrompt"
+ "_goToAccountPersonalInformation"
+ "_goToKBArticleAboutChangingBirthday"
+ "_persistUserHaveSeenAlertWithAction:"
+ "_userActionResponse:"
+ "_viewServiceFlowType"
+ "addButton:"
+ "addTarget:action:forControlEvents:"
+ "ageMigrationPromptModel"
+ "altDSID"
+ "boldButton"
+ "bundleID"
+ "buttonTray"
+ "calendar.and.person"
+ "cancelTapped:"
+ "goToSettingsTapped:"
+ "https://support.apple.com/en-us/102473"
+ "initWithAltDSID:bundleID:"
+ "initWithRootViewController:"
+ "initWithTitle:detailText:icon:"
+ "initWithTitle:style:target:action:"
+ "isU13InferPromptEnabled"
+ "learnMoreTapped:"
+ "linkButton"
+ "message"
+ "misconfigure age prompt feature not enabled."
+ "navigationItem"
+ "prefs:root=APPLE_ACCOUNT&path=APPLE_ACCOUNT_CONTACT"
+ "primaryButtonText"
+ "q"
+ "saveUserAcknowledgeMisconfiguredAgedPromptWithContext:action:completion:"
+ "secondaryButtonText"
+ "setAgeMigrationPromptModel:"
+ "setLeftBarButtonItem:"
+ "setModalInPresentation:"
+ "setTitle:forState:"
+ "setViewServiceFlowType:"
+ "systemImageNamed:"
+ "title"
+ "v20@0:8i16"
+ "v24@0:8q16"
+ "viewServiceFlowType"
- "Showing invited as flow"

```
