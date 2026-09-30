## SoftwareUpdateServicesUIPlugin

> `/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/Plugins/SoftwareUpdateServicesUIPlugin.servicebundle/SoftwareUpdateServicesUIPlugin`

```diff

-231.100.2.0.0
-  __TEXT.__text: 0x41a08
+244.0.0.502.1
+  __TEXT.__text: 0x41af8
   __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_stubs: 0x51c0
-  __TEXT.__objc_methlist: 0x2a8c
-  __TEXT.__cstring: 0x3b3c
-  __TEXT.__objc_methname: 0x5f5c
-  __TEXT.__oslogstring: 0x4203
+  __TEXT.__objc_stubs: 0x5220
+  __TEXT.__objc_methlist: 0x2ac4
+  __TEXT.__cstring: 0x3b96
+  __TEXT.__objc_methname: 0x5f8a
+  __TEXT.__oslogstring: 0x4315
   __TEXT.__objc_classname: 0x77b
-  __TEXT.__objc_methtype: 0x1230
-  __TEXT.__gcc_except_tab: 0x144
-  __TEXT.__unwind_info: 0x650
+  __TEXT.__objc_methtype: 0x121e
+  __TEXT.__gcc_except_tab: 0x160
+  __TEXT.__unwind_info: 0x648
   __DATA_CONST.__auth_got: 0x248
-  __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0x5cb8
-  __DATA_CONST.__cfstring: 0x3100
+  __DATA_CONST.__got: 0x410
+  __DATA_CONST.__const: 0x5ce0
+  __DATA_CONST.__cfstring: 0x3120
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80

   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0x180
-  __DATA.__objc_const: 0x49a0
-  __DATA.__objc_selrefs: 0x1898
+  __DATA.__objc_const: 0x49b0
+  __DATA.__objc_selrefs: 0x18c0
   __DATA.__objc_ivar: 0x26c
   __DATA.__objc_data: 0xdc0
   __DATA.__data: 0x7b0

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6656E2C7-F329-36E4-BE6E-D32243A1012D
-  Functions: 975
-  Symbols:   321
-  CStrings:  2340
+  UUID: 588D94C3-E5A7-3183-AB49-1CC3CE151086
+  Functions: 978
+  Symbols:   310
+  CStrings:  2351
 
Symbols:
- OBJC_IVAR_$_SUDescriptor._humanReadableUpdateName
- _SUSUIExtensionAlertCompletionActionInstall
- _SUSUIExtensionAlertCompletionActionKey
- _SUSUIExtensionAlertCompletionActionReboot
- _SUSUIExtensionAlertCountdownKey
- _SUSUIExtensionAlertHumanReadableUpdateNameKey
- _SUSUIExtensionAlertIgnorableConstraintsKey
- _SUSUIExtensionAlertIsAutoInstallKey
- _SUSUIExtensionAlertPluralText
- _SUSUIExtensionAlertSingularText
- _SUSUIExtensionAlertVerifyingText
CStrings:
+ "%s: Showing countdown alert"
+ "%s: User setting prevented presentation of SU installation countdown alert"
+ "%s: [Install Alert] Ignoring SU availability notification because a preference has disabled them."
+ "%s: [Install Alert] Presenting %{public}@ with auto install operation forecast: %{public}@"
+ "-[SUSUISoftwareUpdateController _showInstallAlertWithInstallOptions:]"
+ "Alert is already shown; not showing alert item for reason: %@"
+ "ContentCacheURLOverride"
+ "Failed to present the alert"
+ "Previous OTA attempt was fake (hence succeeded)"
+ "SOFTWARE_UPDATE_INSTALL_FAILURE_ACTION_DETAILS"
+ "TB,V_showingAlert"
+ "[%{public}@] Details action taken"
+ "_inSetupModeProvider"
+ "_otaFailed"
+ "_shouldShowPostUpdateAlert"
+ "follow up type: SUSUICommandLineToolFollowUpDDMUpdate currently not supported"
+ "follow up type: SUSUICommandLineToolFollowUpPostUpdate currently not supported"
+ "setShowingAlert:"
+ "showingAlert"
+ "startRunning"
- "@40@0:8@16@24@?32"
- "B8@?0"
- "Previous OTA attempt was fake"
- "SOFTWARE_UPDATE_INSTALL_FAILURE_ACTION_RETRY"
- "Showing alert already, not showing again"
- "Showing countdown alert"
- "User setting prevented presentation of SU installation countdown alert"
- "[Install Alert] Ignoring SU availability notification because a preference has disabled them."
- "[Install Alert] Presenting %{public}@ with auto install operation forecast: %{public}@"
- "_initWithLayoutStateMonitor:alertPresentationManager:inSetupModeProvider:"

```
