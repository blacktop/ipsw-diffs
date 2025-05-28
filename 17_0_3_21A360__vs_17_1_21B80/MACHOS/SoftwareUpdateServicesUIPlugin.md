## SoftwareUpdateServicesUIPlugin

> `/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/Plugins/SoftwareUpdateServicesUIPlugin.servicebundle/SoftwareUpdateServicesUIPlugin`

```diff

-185.0.0.0.0
-  __TEXT.__text: 0x3f084
+192.40.1.0.0
+  __TEXT.__text: 0x3f440
   __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_stubs: 0x4ec0
-  __TEXT.__objc_methlist: 0x2544
-  __TEXT.__cstring: 0x35e1
-  __TEXT.__objc_methname: 0x5ddc
-  __TEXT.__oslogstring: 0x3c6b
+  __TEXT.__objc_stubs: 0x4ee0
+  __TEXT.__objc_methlist: 0x24e4
+  __TEXT.__cstring: 0x36a2
+  __TEXT.__objc_methname: 0x5c72
+  __TEXT.__oslogstring: 0x3e2f
   __TEXT.__objc_classname: 0x787
-  __TEXT.__objc_methtype: 0x1195
-  __TEXT.__gcc_except_tab: 0x12c
+  __TEXT.__objc_methtype: 0x1177
+  __TEXT.__gcc_except_tab: 0x118
   __TEXT.__const: 0x30
-  __TEXT.__unwind_info: 0x668
+  __TEXT.__unwind_info: 0x650
   __DATA_CONST.__auth_got: 0x250
   __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x4690
-  __DATA_CONST.__cfstring: 0x2c00
+  __DATA_CONST.__const: 0x46e0
+  __DATA_CONST.__cfstring: 0x2c60
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88

   __DATA_CONST.__objc_arraydata: 0xd8
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0x150
-  __DATA.__objc_const: 0x57c0
-  __DATA.__objc_selrefs: 0x1660
+  __DATA.__objc_const: 0x5738
+  __DATA.__objc_selrefs: 0x1680
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x358
-  __DATA.__objc_superrefs: 0xe8
-  __DATA.__objc_ivar: 0x270
+  __DATA.__objc_classrefs: 0x350
+  __DATA.__objc_superrefs: 0xe0
+  __DATA.__objc_ivar: 0x268
   __DATA.__objc_data: 0xe10
   __DATA.__data: 0x810
   __DATA.__bss: 0x1b0

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 988
+  Functions: 982
   Symbols:   321
-  CStrings:  1866
+  CStrings:  1880
 
CStrings:
+ "%s: [DDM] Directly install the update on a shared iPad"
+ "%s: [DDM] Failed to show the countdown; try to show a regular alert"
+ "%s: [DDM] Installing DDM update now (isSharedIpad = %d)"
+ "%s: [DDM] Overriding isSharedIPad to YES"
+ "%s: [DDM] Skipping. SUDDMManager descriptor (%@) mismatches downloaded descriptor (%@)"
+ "-[SUSUIDDMController installNow]"
+ "@\"SUAutoInstallForecast\""
+ "Auto install operation (%p) was attempted to be scheduled, but it was already expired or cancelled. Trying to fetch a new one."
+ "Enforced-install-countdown"
+ "Failed getting auto install forecast: %{public}@"
+ "Got new auto install forecast: (%@)"
+ "I will reboot later; don't reboot now!"
+ "IWillRebootLater"
+ "SUSUISoftwareUpdateInstallAlertStyleEnforcedCountdown"
+ "Try tonight forecast expired."
+ "[%@] DDM alert, don't schedule anything here"
+ "[%{public}@] forecast not valid: %{public}@"
+ "[Install Alert] Presenting %{public}@ with auto install operation forecast: %{public}@"
+ "_activateInstallLaterAlert:"
+ "_createInstallTonightForecastWithResult:"
+ "_doInstall:"
+ "_forecast"
+ "_isForecastExpired"
+ "_presentAuthenticationUIForInstallation:withInstallType:withInstallOperationForecast:"
+ "currentAutoInstallOperationForecast:"
+ "ddmInstallNow"
+ "initWithDescriptor:autoInstallForecast:forInstallTonight:canDeferInstallation:completionQueue:completionBlock:"
+ "initWithDescriptor:softwareUpdateController:tryTonightOperationForecast:"
+ "initWithDownload:style:softwareUpdateController:tryTonightInstallOperationForecast:installOptions:"
+ "install tonight scheduled"
+ "installNow"
+ "installTonight"
+ "isSharedIPad"
+ "issharedipad=%d"
+ "notification was canceled (alert = %@)"
+ "v16@?0@\"SUAutoInstallForecast\"8"
+ "v24@?0@\"SUAutoInstallForecast\"8@\"NSError\"16"
+ "v24@?0@\"SUDownload\"8@\"SUAutoInstallForecast\"16"
+ "v40@?0@\"SUDownload\"8@\"SUScanResults\"16@\"SUAutoInstallForecast\"24@\"SURollbackDescriptor\"32"
- "%s: [DDM] Installing DDM update now"
- "%s: [DDM] Skipping. Downloaded descriptor (%@) mismatches SUDDMManager descriptor (%@)"
- "@\"SUSUISoftwareUpdateInstallOperationLifeCycleHandler\""
- "T@\"SUAutoInstallOperation\",&,N,V_tryTonightOperation"
- "T@\"SUAutoInstallOperation\",R,W,N"
- "T@\"SUSUISoftwareUpdateInstallOperationLifeCycleHandler\",&,N,G_tryTonightOperationWrapper,S_setTryTonightOperationWrapper:,V_tryTonightOperationWrapper"
- "T@\"SUSUISoftwareUpdateInstallOperationLifeCycleHandler\",&,N,V_tryTonightOperationLifeCycleHandler"
- "Try tonight operation refreshed but still expired."
- "[%{public}@] Try tonight operation (%p) is no longer valid.  Refreshing it."
- "[%{public}@] operation not valid for scheduling: %{public}@"
- "[Install Alert] Presenting %{public}@ with auto install operation: %{public}@"
- "_presentAuthenticationUIForInstallation:withInstallType:withInstallOperation:"
- "_setTryTonightOperation:"
- "_setTryTonightOperationWrapper:"
- "_tryTonightOperationLifeCycleHandler"
- "_tryTonightOperationWrapper"
- "initWithDescriptor:autoInstallOperation:forInstallTonight:canDeferInstallation:completionQueue:completionBlock:"
- "initWithDescriptor:softwareUpdateController:tryTonightOperationLifeCycleHandler:"
- "initWithDownload:style:softwareUpdateController:tryTonightInstallOperation:installOptions:"
- "setTryTonightOperation:"
- "setTryTonightOperationLifeCycleHandler:"
- "tryTonightOperationLifeCycleHandler"
- "tryTonightOperationWrapper"
- "v24@?0@\"SUDownload\"8@\"SUAutoInstallOperation\"16"
- "v40@?0@\"SUDownload\"8@\"SUScanResults\"16@\"SUAutoInstallOperation\"24@\"SURollbackDescriptor\"32"

```
