## ABMHelper

> `/System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper`

```diff

-1209.0.0.0.0
-  __TEXT.__text: 0x13d6e4
+1211.0.0.0.0
+  __TEXT.__text: 0x13d2d0
   __TEXT.__auth_stubs: 0x24f0
   __TEXT.__init_offsets: 0xc0
   __TEXT.__objc_methlist: 0x14
-  __TEXT.__gcc_except_tab: 0x18af8
+  __TEXT.__gcc_except_tab: 0x18b4c
   __TEXT.__const: 0x6032
   __TEXT.__cstring: 0x68c8
-  __TEXT.__oslogstring: 0x8aca
-  __TEXT.__unwind_info: 0x5c18
+  __TEXT.__oslogstring: 0x89a3
+  __TEXT.__unwind_info: 0x5c48
   __TEXT.__objc_classname: 0x16
   __TEXT.__objc_methname: 0x5e6
   __TEXT.__objc_methtype: 0x28

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 3499
-  Symbols:   4789
-  CStrings:  2035
+  Functions: 3504
+  Symbols:   4793
+  CStrings:  2031
 
Symbols:
+ __ZN3sys20isBootSessionChangedEv
+ __ZN3sys21updateBootSessionUUIDEv
+ __ZN8INTTrace21sendFlushRequest_syncEv
CStrings:
+ "#I AP reboot detected, resetting trace properties"
- "#N New boot instance (%!s(MISSING)) for DIAG Trace, resetting trace mode and ownership"
- "#N New boot instance (%!s(MISSING)) for INT Trace, resetting trace mode and ownership"
- "#N prefs boot session uuid: %!s(MISSING), current boot session uuid: %!s(MISSING), reset mode on AP boot: %!s(MISSING)"
- "Failed to get boot session uuid from preferences"
- "Failed to set boot session uuid in pref from %!s(MISSING) -> %!s(MISSING)"

```
