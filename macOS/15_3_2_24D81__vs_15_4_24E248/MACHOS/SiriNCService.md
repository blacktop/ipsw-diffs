## SiriNCService

> `/System/Library/CoreServices/Siri.app/Contents/XPCServices/SiriNCService.xpc/Contents/MacOS/SiriNCService`

```diff

-3403.4.1.14.2
-  __TEXT.__text: 0x1105c
-  __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_stubs: 0x3640
-  __TEXT.__objc_methlist: 0xe3c
-  __TEXT.__const: 0x90
+3404.72.1.14.4
+  __TEXT.__text: 0x114b8
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__objc_stubs: 0x3720
+  __TEXT.__objc_methlist: 0x1508
+  __TEXT.__const: 0x80
   __TEXT.__objc_classname: 0x343
-  __TEXT.__objc_methname: 0x44ed
-  __TEXT.__objc_methtype: 0xfa4
-  __TEXT.__cstring: 0x174d
-  __TEXT.__oslogstring: 0xfce
-  __TEXT.__gcc_except_tab: 0x270
-  __TEXT.__unwind_info: 0x490
-  __DATA_CONST.__auth_got: 0x2d8
-  __DATA_CONST.__got: 0x348
+  __TEXT.__objc_methname: 0x462d
+  __TEXT.__objc_methtype: 0x101f
+  __TEXT.__cstring: 0x1790
+  __TEXT.__oslogstring: 0x1007
+  __TEXT.__gcc_except_tab: 0x27c
+  __TEXT.__unwind_info: 0x4b8
+  __DATA_CONST.__auth_got: 0x2e8
+  __DATA_CONST.__got: 0x360
   __DATA_CONST.__const: 0x700
   __DATA_CONST.__cfstring: 0xa00
   __DATA_CONST.__objc_classlist: 0x58

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x48
-  __DATA.__objc_const: 0x3600
-  __DATA.__objc_selrefs: 0x10e8
-  __DATA.__objc_ivar: 0x110
+  __DATA.__objc_const: 0x2ab0
+  __DATA.__objc_selrefs: 0x1280
+  __DATA.__objc_ivar: 0x114
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x780
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/SAObjects.framework/Versions/A/SAObjects
   - /System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/Versions/A/SiriCrossDeviceArbitration
   - /System/Library/PrivateFrameworks/SiriFoundation.framework/Versions/A/SiriFoundation
+  - /System/Library/PrivateFrameworks/SiriSharedUI.framework/Versions/A/SiriSharedUI
   - /System/Library/PrivateFrameworks/SiriUI.framework/Versions/A/SiriUI
   - /System/Library/PrivateFrameworks/SiriUIFoundation.framework/Versions/A/SiriUIFoundation
   - /System/Library/PrivateFrameworks/SpeechObjects.framework/Versions/A/Frameworks/DictationServices.framework/Versions/A/DictationServices
   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 04507754-5B6E-3EE9-9003-C53E81F075AD
-  Functions: 407
-  Symbols:   238
-  CStrings:  1197
+  UUID: A28794EA-824E-361E-A12F-B635E3D59DB8
+  Functions: 421
+  Symbols:   243
+  CStrings:  1214
 
Symbols:
+ _AFLanguageCodeDidChangeNotification
+ _OBJC_CLASS_$_SiriUIReplayWindowController
+ _SRUIFConstructLaunchContextForLaunchEnded
+ _SiriSharedUIGenerativeAssistantOnboardingNotifierWillDismissAssistantNotification
+ _SiriUIRequestSourceGetSISchemaInvocationSource
CStrings:
+ "%s Handling AppleLocale update to newLocaleIdentifier=%@"
+ "-[SiriNCAlertViewController _localeChanged:]"
+ "T{CGSize=dd},N,V_notificationCenterWindowSize"
+ "_notificationCenterWindowSize"
+ "closeReplayUtility"
+ "emitInstrumentation:"
+ "jit_enablement_window"
+ "notificationCenterWindowSize"
+ "pauseOutsideOfContentDismissal:"
+ "setNotificationCenterWindowSize:"
+ "shared"
+ "siriViewControllerTextInputDidClearMarkedText:"
+ "siriViewControllerTextInputDidInsertMarkedText:"
+ "windowSizeForRemoteViewBridgeService:"
+ "{CGSize=\"width\"d\"height\"d}"
+ "{CGSize=dd}16@0:8"
+ "{CGSize=dd}24@0:8@\"RemoteViewBridgeServiceViewService\"16"
+ "{CGSize=dd}24@0:8@16"
- "cancelRequestAndStopAttending"

```
