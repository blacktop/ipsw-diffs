## SoftwareUpdateServicesUIPlugin

> `/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/Plugins/SoftwareUpdateServicesUIPlugin.servicebundle/SoftwareUpdateServicesUIPlugin`

```diff

-251.40.17.0.0
-  __TEXT.__text: 0x415a0
-  __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_stubs: 0x5360
-  __TEXT.__objc_methlist: 0x2b24
-  __TEXT.__cstring: 0x3b99
-  __TEXT.__objc_methname: 0x5ee9
-  __TEXT.__oslogstring: 0x4587
+251.100.27.0.0
+  __TEXT.__text: 0x41d40
+  __TEXT.__auth_stubs: 0x460
+  __TEXT.__objc_stubs: 0x53e0
+  __TEXT.__objc_methlist: 0x2b44
+  __TEXT.__cstring: 0x3caa
+  __TEXT.__objc_methname: 0x5fb2
+  __TEXT.__oslogstring: 0x4680
   __TEXT.__objc_classname: 0x74c
-  __TEXT.__objc_methtype: 0x1216
+  __TEXT.__objc_methtype: 0x123f
   __TEXT.__gcc_except_tab: 0x178
-  __TEXT.__unwind_info: 0x638
-  __DATA_CONST.__auth_got: 0x248
-  __DATA_CONST.__got: 0x448
-  __DATA_CONST.__const: 0x5aa0
-  __DATA_CONST.__cfstring: 0x3100
+  __TEXT.__unwind_info: 0x648
+  __DATA_CONST.__auth_got: 0x240
+  __DATA_CONST.__got: 0x440
+  __DATA_CONST.__const: 0x5ac8
+  __DATA_CONST.__cfstring: 0x30e0
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80

   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0x180
-  __DATA.__objc_const: 0x47c0
-  __DATA.__objc_selrefs: 0x18d0
-  __DATA.__objc_ivar: 0x248
+  __DATA.__objc_const: 0x47e8
+  __DATA.__objc_selrefs: 0x1900
+  __DATA.__objc_ivar: 0x24c
   __DATA.__objc_data: 0xd70
   __DATA.__data: 0x7a0
-  __DATA.__bss: 0x1a0
+  __DATA.__bss: 0x1b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F4573459-C9EA-3522-B326-D6B4FF4BCB73
-  Functions: 987
-  Symbols:   315
-  CStrings:  2354
+  UUID: 8A1244EB-7538-347E-A8E3-CD798F8A5246
+  Functions: 990
+  Symbols:   314
+  CStrings:  2369
 
Symbols:
+ _kSUSUIBackgroundSecurityUpdateSettingsURL
- _MSURetrievePreviousUpdateState
- _OBJC_CLASS_$_SUPreferences
CStrings:
+ "%s New OS detected:%@"
+ "%s Splat Update detected"
+ "%s: UI Locked: %d, needsHomescreenForInstallAlert: %d, isShowingHomescreen: %d, inPreferences: %d, isClientInUserInteraction:%d, alert flow: %{public}@"
+ "%s: [DDM] [Install Alert] fgApp = %{public}@, and the device is not locked, presenting a notification (follow-up) ..."
+ "%s: waitForHomescreen: %d"
+ "-[SUSUISoftwareUpdateController _needsToWaitForHomescreenToAppear]"
+ "-[SUSUISoftwareUpdateController client:newOSBuildDetected:]"
+ "-[SUSUISoftwareUpdateController deviceBootedAfterSplatOnlyUpdate:]"
+ "Post-update controller not ready, queuing newOS notification with build: %@"
+ "Post-update controller not ready, queuing splat update notification"
+ "Processing pending newOSDetected notification with build: %@"
+ "Processing pending splatUpdate notification"
+ "SOFTWARE_UPDATE_INSTALL_ALERT_ENFORCED_SOON"
+ "_localizedStringForDate:"
+ "_pendingNewOSBuild"
+ "_processPendingPostUpdateNotification"
+ "client:newOSBuildDetected:"
+ "deleteKeepAliveFile"
+ "lastUpdateWasSuccessful"
+ "pending post update notification status: %d"
+ "postUpdateController failed to init"
+ "presentPostUpdateAlert"
+ "setDateStyle:"
+ "setLastUpdateWasSuccessful:"
+ "setTimeStyle:"
+ "settings-navigation://com.apple.Settings.PrivacyAndSecurity/BACKGROUND_SECURITY_IMPROVEMENTS"
+ "stringFromDate:"
+ "v32@0:8@\"SUManagerClient\"16@\"NSString\"24"
- "%s: [DDM] [Install Alert] fgApp = %{public}@, presenting a notification (follow-up) ..."
- "No"
- "Previous OTA attempt failed. MSUPreviousUpdateState: %d"
- "Previous OTA attempt was fake (hence succeeded)"
- "UI Locked: %@, needsHomescreenForInstallAlert: %@, isShowingHomescreen: %@, alert flow: %@"
- "UI not locked. inPreferences: %@, needsHomescreenForInstallAlert: %@, isShowingHomescreen: %@, isClientInUserInteraction:%@, alert flow: %@"
- "Yes"
- "_otaFailed"
- "prefs:root=General&path=About/SW_VERSION_SPECIFIER"
- "skipApply"
- "skipDownload"
- "startRunning"

```
