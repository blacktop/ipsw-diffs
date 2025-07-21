## SoftwareUpdateServicesUI

> `/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/SoftwareUpdateServicesUI`

```diff

-231.140.1.0.0
-  __TEXT.__text: 0x995c
+231.140.1.0.1
+  __TEXT.__text: 0x99a0
   __TEXT.__auth_stubs: 0x2d0
-  __TEXT.__objc_methlist: 0xb00
+  __TEXT.__objc_methlist: 0xb10
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0xf63
+  __TEXT.__cstring: 0xf84
   __TEXT.__oslogstring: 0x39c
   __TEXT.__gcc_except_tab: 0xd8
   __TEXT.__unwind_info: 0x140
   __TEXT.__objc_classname: 0x2a9
-  __TEXT.__objc_methname: 0x1a81
+  __TEXT.__objc_methname: 0x1aee
   __TEXT.__objc_methtype: 0x4b8
   __TEXT.__objc_stubs: 0x11a0
   __DATA_CONST.__got: 0x258
-  __DATA_CONST.__const: 0x1e08
+  __DATA_CONST.__const: 0x1e10
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x778
+  __DATA_CONST.__objc_selrefs: 0x780
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x50
   __AUTH_CONST.__auth_got: 0x178
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x1360
-  __AUTH_CONST.__objc_const: 0x1a70
+  __AUTH_CONST.__cfstring: 0x1380
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
-  UUID: 725D915C-D824-31A7-9DD3-50437AE93A56
-  Functions: 220
-  Symbols:   1852
-  CStrings:  745
+  UUID: 23B59BA5-1349-3C0C-9BDD-325E2FD0DE7B
+  Functions: 221
+  Symbols:   1856
+  CStrings:  750
 
Symbols:
+ -[SUSUIPreferences useMobileInboxUpdaterRebootDelay]
+ _OBJC_IVAR_$_SUSUIPreferences._useMobileInboxUpdaterRebootDelay
+ _kSUSUIPreferenceUseMobileInboxUpdaterRebootDelay
Functions (modified):
~ -[SUSUIPreferences _loadPreferences] : 508 -> 544

Functions (added):
+ -[SUSUIPreferences useMobileInboxUpdaterRebootDelay]
CStrings:
+ "TB,R,N,V_useMobileInboxUpdaterRebootDelay"
+ "_useMobileInboxUpdaterRebootDelay"
+ "useMobileInboxUpdaterRebootDelay"

```
