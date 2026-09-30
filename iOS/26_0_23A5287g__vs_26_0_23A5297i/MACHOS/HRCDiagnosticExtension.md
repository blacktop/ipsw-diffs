## HRCDiagnosticExtension

> `/System/Library/PrivateFrameworks/HeartRateCoordinator.framework/PlugIns/HRCDiagnosticExtension.appex/HRCDiagnosticExtension`

```diff

-19.0.0.0.0
-  __TEXT.__text: 0x2fc4
+21.0.0.0.0
+  __TEXT.__text: 0x30b4
   __TEXT.__auth_stubs: 0x500
   __TEXT.__objc_stubs: 0x300
   __TEXT.__objc_methlist: 0x74
   __TEXT.__const: 0x166
-  __TEXT.__gcc_except_tab: 0x420
+  __TEXT.__gcc_except_tab: 0x444
   __TEXT.__cstring: 0x256
-  __TEXT.__oslogstring: 0x562
+  __TEXT.__oslogstring: 0x574
   __TEXT.__objc_classname: 0x17
   __TEXT.__objc_methname: 0x26a
   __TEXT.__objc_methtype: 0x5e

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A8B11450-427F-3315-A23A-D1CD67BB2B0D
+  UUID: 1572D921-0B37-357D-BF2E-0FE8DD35F5D8
   Functions: 76
   Symbols:   115
-  CStrings:  96
+  CStrings:  97
 
Symbols:
+ _objc_retain_x23
- _objc_retain_x22
Functions:
~ sub_100000fc4 : 128 -> 332
~ sub_100001044 -> sub_100001110 : 1028 -> 1064
CStrings:
+ "Unexpected calling host: %{public}@"
+ "initial limited logging state found in defaults: %{public,BOOL}d"
- "initial limited logging state already in defaults, skipping setup: %{public,BOOL}d"

```
