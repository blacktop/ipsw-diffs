## SoftwareUpdateServicesUIPlugin

> `/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/Plugins/SoftwareUpdateServicesUIPlugin.servicebundle/SoftwareUpdateServicesUIPlugin`

```diff

-227.0.0.0.0
-  __TEXT.__text: 0x40570
+229.0.0.0.0
+  __TEXT.__text: 0x40900
   __TEXT.__auth_stubs: 0x490
   __TEXT.__objc_stubs: 0x51c0
   __TEXT.__objc_methlist: 0x24c4
-  __TEXT.__cstring: 0x3ad5
-  __TEXT.__objc_methname: 0x5f48
-  __TEXT.__oslogstring: 0x40c4
+  __TEXT.__cstring: 0x3ad1
+  __TEXT.__objc_methname: 0x5f5c
+  __TEXT.__oslogstring: 0x4203
   __TEXT.__objc_classname: 0x77b
   __TEXT.__objc_methtype: 0x1230
   __TEXT.__gcc_except_tab: 0x140
   __TEXT.__const: 0x30
-  __TEXT.__unwind_info: 0x680
+  __TEXT.__unwind_info: 0x688
   __DATA_CONST.__auth_got: 0x258
   __DATA_CONST.__got: 0x408
   __DATA_CONST.__const: 0x5a30

   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0xe0
+  __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0x180
-  __DATA.__objc_const: 0x5418
+  __DATA.__objc_const: 0x5438
   __DATA.__objc_selrefs: 0x1738
-  __DATA.__objc_ivar: 0x268
+  __DATA.__objc_ivar: 0x26c
   __DATA.__objc_data: 0xdc0
   __DATA.__data: 0x7b0
   __DATA.__bss: 0x1a0

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 984
+  Functions: 986
   Symbols:   321
-  CStrings:  1957
+  CStrings:  1958
 
CStrings:
+ "%s: [DDM] Can't show DDM alert when there's no descriptor (from the SUDDMManager) for our %{public}@"
+ "%s: [DDM] Cannot show alert because of the invalid alert info %{public}@"
+ "%s: [DDM] Deciding conflict between classic flow (%{public}@) and DDM (%{public}@) alerts"
+ "%s: [DDM] Deciding no conflicts. Downloaded update (%{public}@) mismatches SUDDMManager-tracked update (%{public}@)"
+ "%s: [DDM] Declaration %{public}@ isn't relevant for %{public}@"
+ "%s: [DDM] Failed to install %{public}@; resume showing alert..."
+ "%s: [DDM] Finished to install irrelevant update %{public}@; resume showing alert... [should never print this... likely a bug...]"
+ "%s: [DDM] Finished to install relevant update %{public}@; disarming..."
+ "%s: [DDM] First init of SUSUIDDMController missing %{public}@ delegate"
+ "%s: [DDM] Next alert info: %{public}@"
+ "%s: [DDM] No previous declaration, new declaration: %{public}@"
+ "%s: [DDM] Owner decision: %{public}@"
+ "%s: [DDM] Replacing existing declaration: %{public}@ \nwith new declaration: %{public}@"
+ "%s: [DDM] Set passcode policy to SUPasscodePolicyTypeRequired for the enforced date %{public}@"
+ "%s: [DDM] Skipping. SUDDMManager descriptor (%{public}@) mismatches downloaded descriptor (%{public}@)"
+ "%s: [DDM] Started to install %{public}@; pause showing alert..."
+ "%s: [DDM] WARNING WARNING WARNING!!! We found a descriptor\n%{public}@\nfor declaration\n%{public}@\nbut we downloaded something else\n%{public}@\nDon't show the alert..."
+ "%s: [DDM] Will directly start installing after %{public}@ (interval: %lf)"
+ "%s: [DDM] result = %{public}@ (real enforce date: %{public}@; past due notifications cnt = %lu)"
+ "-[SUSUIDDMController _shouldTryToInstall]"
+ "_pastDueNotificationCnt"
+ "_shouldTryToInstall"
- "%s: [DDM] Can't show DDM alert when there's no descriptor (from the SUDDMManager) for our %@"
- "%s: [DDM] Cannot show alert because of the invalid alert info %@"
- "%s: [DDM] Deciding conflict between classic flow (%@) and DDM (%@) alerts"
- "%s: [DDM] Deciding no conflicts. Downloaded descriptor (%@) mismatches SUDDMManager descriptor (%@)"
- "%s: [DDM] Declaration %@ isn't relevant for %@"
- "%s: [DDM] Failed to install %@; resume showing alert..."
- "%s: [DDM] Finished to install irrelevant update %@; resume showing alert..."
- "%s: [DDM] Finished to install relevant update %@; disarming..."
- "%s: [DDM] First init of SUSUIDDMController missing %@ delegate"
- "%s: [DDM] Next alert info: %@"
- "%s: [DDM] No previous declaration, new declaration: %@"
- "%s: [DDM] Owner decision: %@"
- "%s: [DDM] Replacing existing declaration: %@ \nwith new declaration: %@"
- "%s: [DDM] Set passcode policy to SUPasscodePolicyTypeRequired for the enforced date %@"
- "%s: [DDM] Skipping. SUDDMManager descriptor (%@) mismatches downloaded descriptor (%@)"
- "%s: [DDM] Started to install %@; pause showing alert..."
- "%s: [DDM] WARNING WARNING WARNING!!! We found a descriptor\n%@\nfor declaration\n%@\nbut we downloaded something else\n%@\nDon't show the alert..."
- "%s: [DDM] Will directly start installing after %@ (interval: %lf)"
- "%s: [DDM] result = %@"
- "-[SUSUIDDMController _reallyShouldEnforceNow]"
- "_reallyShouldEnforceNow"

```
