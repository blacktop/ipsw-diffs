## SoftwareUpdateServicesUIPlugin

> `/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/Plugins/SoftwareUpdateServicesUIPlugin.servicebundle/SoftwareUpdateServicesUIPlugin`

```diff

-244.0.0.502.1
-  __TEXT.__text: 0x41af8
+248.0.0.0.0
+  __TEXT.__text: 0x422d4
   __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_stubs: 0x5220
-  __TEXT.__objc_methlist: 0x2ac4
-  __TEXT.__cstring: 0x3b96
-  __TEXT.__objc_methname: 0x5f8a
-  __TEXT.__oslogstring: 0x4315
+  __TEXT.__objc_stubs: 0x5340
+  __TEXT.__objc_methlist: 0x2aec
+  __TEXT.__cstring: 0x3b34
+  __TEXT.__objc_methname: 0x5ff6
+  __TEXT.__oslogstring: 0x4473
   __TEXT.__objc_classname: 0x77b
-  __TEXT.__objc_methtype: 0x121e
+  __TEXT.__objc_methtype: 0x1255
   __TEXT.__gcc_except_tab: 0x160
-  __TEXT.__unwind_info: 0x648
+  __TEXT.__unwind_info: 0x638
   __DATA_CONST.__auth_got: 0x248
   __DATA_CONST.__got: 0x410
-  __DATA_CONST.__const: 0x5ce0
+  __DATA_CONST.__const: 0x5d18
   __DATA_CONST.__cfstring: 0x3120
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0x180
-  __DATA.__objc_const: 0x49b0
-  __DATA.__objc_selrefs: 0x18c0
+  __DATA.__objc_const: 0x4988
+  __DATA.__objc_selrefs: 0x18e0
   __DATA.__objc_ivar: 0x26c
   __DATA.__objc_data: 0xdc0
   __DATA.__data: 0x7b0
-  __DATA.__bss: 0x1a0
+  __DATA.__bss: 0x1a8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 588D94C3-E5A7-3183-AB49-1CC3CE151086
-  Functions: 978
+  UUID: 558E101A-A488-34E3-8B28-4655BD303334
+  Functions: 983
   Symbols:   310
-  CStrings:  2351
+  CStrings:  2359
 
CStrings:
+ "\n"
+ "%s: [DDM] Current alert info: %{public}@"
+ "%s: [DDM] Failed to show DDM available alert."
+ "%s: [DDM] Failed to show DDM install alert."
+ "%s: [DDM] New global settings: %{public}@"
+ "%s: [DDM] Old global settings: %{public}@"
+ "%s: [DDM] Replacing existing declaration: %{public}@\nwith new declaration: %{public}@"
+ "%s: [DDM] This notification (%ld) is disabled by global settings; alerts will start one hour before the deadline."
+ "%s: notifications disabled by global settings"
+ "-[SUSUIDDMController _presentDDMAvailableAlert]"
+ "-[SUSUIDDMController _presentDDMInstallAlert]"
+ "-[SUSUIDDMController setGlobalSettings:]_block_invoke"
+ "@\"SUCoreDDMDeclarationGlobalSettings\""
+ "@32@0:8@16d24"
+ "Error retrieving autoInstallOperation: %@"
+ "Found autoInstallOperation:%@, canceling it"
+ "Ignoring SU availability notification because disabled by global settings"
+ "No autoInstallOperation"
+ "T@\"SUSUIDDMController\",R,N,V_ddmController"
+ "[AutoDownloadNotify] Disabled by global settings"
+ "[InstallWithoutCountdown] Disabled by global settings"
+ "_globalSettings"
+ "_indexForNextAlertInScheduling:forEnforcedDate:"
+ "_localizedStringForDate:RelativeToDate:"
+ "_presentDDMAvailableAlert"
+ "_presentDDMInstallAlert"
+ "_scheduleNextDDMAlertWithTimer"
+ "_scheduledAlertsForEnforcedInstallDate:"
+ "_schedulingUnitForEnforcedDate:withInterval:"
+ "_showDDMAlert"
+ "ddmController"
+ "enableGlobalNotifications"
+ "localizedStringForKey:"
+ "notificationsDisabledByGlobalSettings"
+ "objectAtIndexedSubscript:"
+ "q32@0:8@16@24"
+ "setGlobalSettings:"
- "\t"
- "%s: [DDM] Checking if we have a declaration to consider"
- "%s: [DDM] Failed to/Didn't show DDM alert."
- "%s: [DDM] First init of SUSUIDDMController missing %{public}@ delegate"
- "%s: [DDM] First init of SUSUIDDMController missing queue"
- "%s: [DDM] Found declaration: %@"
- "%s: [DDM] No declaration found"
- "%s: [DDM] Replacing existing declaration: %{public}@ \nwith new declaration: %{public}@"
- "%s: [DDM] was called"
- "-[SUSUIDDMController initWithSUSUIController:withQueue:]"
- "-[SUSUIDDMController installNow]"
- "-[SUSUISoftwareUpdateController _initializeState]"
- "-[SUSUISoftwareUpdateController _initializeState]_block_invoke"
- "@24@0:8d16"
- "T@\"NSArray\",&,V_scheduling"
- "TB,R,V_pendingUnlockToShowAlert"
- "Tq,V_schedulingIndex"
- "_localizedRelativeEnforcedDateRelativeTo:"
- "_pendingUnlockToShowAlert"
- "_schedulingUnitWithIntervalFromEnforcedDate:"
- "getDDMDeclarationWithHandler:"
- "getInitIfNeededDDMController"
- "pendingUnlockToShowAlert"
- "scheduling"
- "schedulingIndex"
- "setScheduling:"
- "setSchedulingIndex:"
- "sharedInstance:withQueue:"
- "v24@?0@\"SUCoreDDMDeclaration\"8@\"NSError\"16"

```
