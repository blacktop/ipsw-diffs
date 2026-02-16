## SoftwareUpdateServicesUI

> `/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/SoftwareUpdateServicesUI`

```diff

-251.40.17.0.0
-  __TEXT.__text: 0x986c
+251.100.27.0.0
+  __TEXT.__text: 0x992c
   __TEXT.__auth_stubs: 0x2d0
-  __TEXT.__objc_methlist: 0xb00
+  __TEXT.__objc_methlist: 0xb18
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0xf9c
+  __TEXT.__cstring: 0xfb4
   __TEXT.__oslogstring: 0x39c
   __TEXT.__gcc_except_tab: 0xd8
   __TEXT.__unwind_info: 0x140
   __TEXT.__objc_classname: 0x2a9
-  __TEXT.__objc_methname: 0x1d6d
+  __TEXT.__objc_methname: 0x1df6
   __TEXT.__objc_methtype: 0x4b8
   __TEXT.__objc_stubs: 0x15a0
   __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0x1e98
+  __DATA_CONST.__const: 0x1ea0
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x878
+  __DATA_CONST.__objc_selrefs: 0x888
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x50
   __AUTH_CONST.__auth_got: 0x178
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x13a0
-  __AUTH_CONST.__objc_const: 0x1a70
+  __AUTH_CONST.__cfstring: 0x13c0
+  __AUTH_CONST.__objc_const: 0x1aa0
   __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x98
+  __DATA.__objc_ivar: 0x9c
   __DATA.__data: 0x2b0
   __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0x140

   - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 938BED07-CAB7-3663-A818-EABECECA5236
-  Functions: 220
-  Symbols:   1869
-  CStrings:  781
+  UUID: 668AC6AF-4AD4-3D0D-BCDC-62A7D122E27C
+  Functions: 222
+  Symbols:   1875
+  CStrings:  787
 
Symbols:
+ -[SUSUIPreferences lastUpdateWasSuccessful]
+ -[SUSUIPreferences setLastUpdateWasSuccessful:]
+ _OBJC_IVAR_$_SUSUIPreferences._lastUpdateWasSuccessful
+ _kSUSUIPreferenceLastUpdateWasSuccessful
Functions:
~ -[SUSUIPreferences _loadPreferences] : 508 -> 544
+ -[SUSUIPreferences setLastUpdateWasSuccessful:]
+ -[SUSUIPreferences preventCountdownAlert]
CStrings:
+ "TB,N,SsetLastUpdateWasSuccessful:,V_lastUpdateWasSuccessful"
+ "_lastUpdateWasSuccessful"
+ "lastUpdateWasSuccessful"
+ "setLastUpdateWasSuccessful:"

```
