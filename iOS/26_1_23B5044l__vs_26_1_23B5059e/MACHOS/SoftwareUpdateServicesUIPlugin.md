## SoftwareUpdateServicesUIPlugin

> `/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/Plugins/SoftwareUpdateServicesUIPlugin.servicebundle/SoftwareUpdateServicesUIPlugin`

```diff

-251.40.7.0.0
-  __TEXT.__text: 0x43398
-  __TEXT.__auth_stubs: 0x490
-  __TEXT.__objc_stubs: 0x5560
-  __TEXT.__objc_methlist: 0x2b3c
-  __TEXT.__cstring: 0x3c35
-  __TEXT.__objc_methname: 0x60df
-  __TEXT.__oslogstring: 0x473b
-  __TEXT.__objc_classname: 0x77b
-  __TEXT.__objc_methtype: 0x1243
+251.40.17.0.0
+  __TEXT.__text: 0x415a0
+  __TEXT.__auth_stubs: 0x470
+  __TEXT.__objc_stubs: 0x5360
+  __TEXT.__objc_methlist: 0x2b24
+  __TEXT.__cstring: 0x3b99
+  __TEXT.__objc_methname: 0x5ee9
+  __TEXT.__oslogstring: 0x4587
+  __TEXT.__objc_classname: 0x74c
+  __TEXT.__objc_methtype: 0x1216
   __TEXT.__gcc_except_tab: 0x178
-  __TEXT.__unwind_info: 0x640
-  __DATA_CONST.__auth_got: 0x258
-  __DATA_CONST.__got: 0x460
-  __DATA_CONST.__const: 0x5df0
-  __DATA_CONST.__cfstring: 0x31e0
-  __DATA_CONST.__objc_classlist: 0x160
+  __TEXT.__unwind_info: 0x638
+  __DATA_CONST.__auth_got: 0x248
+  __DATA_CONST.__got: 0x448
+  __DATA_CONST.__const: 0x5aa0
+  __DATA_CONST.__cfstring: 0x3100
+  __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0x180
-  __DATA.__objc_const: 0x4920
-  __DATA.__objc_selrefs: 0x1950
-  __DATA.__objc_ivar: 0x260
-  __DATA.__objc_data: 0xdc0
-  __DATA.__data: 0x7b0
-  __DATA.__bss: 0x1b0
+  __DATA.__objc_const: 0x47c0
+  __DATA.__objc_selrefs: 0x18d0
+  __DATA.__objc_ivar: 0x248
+  __DATA.__objc_data: 0xd70
+  __DATA.__data: 0x7a0
+  __DATA.__bss: 0x1a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore
+  - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices
   - /System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/SoftwareUpdateServicesUI
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F0148EFA-5322-34C2-B8FC-2A1491DD10D9
-  Functions: 995
-  Symbols:   322
-  CStrings:  2398
+  UUID: 13992AF8-A41E-3BDE-B72A-754FC8E1ABD3
+  Functions: 987
+  Symbols:   315
+  CStrings:  2354
 
Symbols:
+ _OBJC_CLASS_$_SUCoreDevice
- _NSTemporaryDirectory
- _OBJC_CLASS_$_SUSUISoftwareUpdateRollbackDetectedAlertItem
- _OBJC_CLASS_$_UIColor
- _OBJC_CLASS_$_UIImage
- _OBJC_METACLASS_$_SUSUISoftwareUpdateRollbackDetectedAlertItem
- _SBUserNotificationIconImagePath
- _UIImagePNGRepresentation
- _kCFUserNotificationIconURLKey
CStrings:
+ " (%@)"
+ "Using custom graphic icon: %@"
+ "com.apple.graphic-icon.background-security-improvements"
+ "com.apple.graphic-icon.software-update-complete"
+ "graphicIcon"
+ "sharedDevice"
- "%s Preventing Rollback consent prompt due to user settings"
- "@\"SURollbackOptions\""
- "@56@0:8@16@24@32@40@?48"
- "SOFTWARE_UPDATE_ROLLBACK_DETECTED_ALERT_ACTION_REMOVE"
- "SOFTWARE_UPDATE_ROLLBACK_DETECTED_ALERT_BODY"
- "SOFTWARE_UPDATE_ROLLBACK_DETECTED_ALERT_TITLE"
- "SUSUISoftwareUpdateRollbackDetectedAlertItem"
- "T@\"SUManagerClient\",R,&,N,V_suClient"
- "UIImage generation failed, falling back to graphic icon definition"
- "URLForResource:withExtension:"
- "Using dynamically generated UIImage for software update notification"
- "Using existing bundle PNG gear_badge_checkmark_generated.png for software update notification"
- "[%{public}@] Passcode entry %@"
- "[%{public}@] Prompting for passcode before starting rollback."
- "[%{public}@] Prompting for passcode for rollback."
- "[%{public}@] Remove action taken."
- "_completion"
- "_options"
- "_promptForRollbackConentAndPasscode:withOptions:withCompletion:"
- "_removeButton"
- "_suClient"
- "bundleForClass:"
- "com.apple.graphic-icon.gear"
- "errorWithCode:"
- "failed"
- "fileURLWithPath:"
- "gear.badge.checkmark"
- "gear_badge_checkmark"
- "gear_badge_checkmark_temp.png"
- "imageWithTintColor:renderingMode:"
- "initWithRollback:options:controller:suClient:completion:"
- "path"
- "png"
- "presentRollbackConsentAlert:withOptions:withCompletion:"
- "preventRollbackPrompt"
- "promptForConsent"
- "promptForPasscode"
- "stringByAppendingPathComponent:"
- "suClient"
- "succeeded"
- "systemImageNamed:"
- "whiteColor"
- "writeToFile:atomically:"

```
