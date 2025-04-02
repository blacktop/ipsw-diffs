## Intents

> `/System/Library/Frameworks/Intents.framework/Intents`

```diff

-3506.0.1.0.0
+3601.0.0.0.0
   __TEXT.__text: 0x43ca3c
   __TEXT.__auth_stubs: 0xfd0
   __TEXT.__objc_methlist: 0x78b04
   __TEXT.__const: 0x1e10
   __TEXT.__dlopen_cstrs: 0xce9
   __TEXT.__gcc_except_tab: 0x220c
-  __TEXT.__oslogstring: 0x572f
-  __TEXT.__cstring: 0x473f4
+  __TEXT.__oslogstring: 0x5785
+  __TEXT.__cstring: 0x47415
   __TEXT.__ustring: 0x512
-  __TEXT.__unwind_info: 0x10d90
+  __TEXT.__unwind_info: 0x10d50
   __TEXT.__objc_classname: 0x12221
   __TEXT.__objc_methname: 0x69bfc
   __TEXT.__objc_methtype: 0xcd53

   - /usr/lib/libobjc.A.dylib
   Functions: 30607
   Symbols:   33916
-  CStrings:  28737
+  CStrings:  28738
 
CStrings:
+ "%s Error injecting image proxies into %{sensitive}@: %{public}@"
+ "%s No intent was provided in the interaction: %{sensitive}@"
+ "%s Not donating system intent because it does not have any valid parameter combinations: %{sensitive}@"
+ "Cannot donate interaction (%{sensitive}@) because intent (%@) has been deprecated"
+ "Cannot donate interaction because intent title is empty: %{sensitive}@ Please make sure that your intent definition includes the following shortcut type for %@: %@."
+ "Cannot donate interaction with nil identifier: %{sensitive}@"
- "%s No intent was provided in the interaction: %@"
- "%s Not donating system intent because it does not have any valid parameter combinations: %@"
- "Cannot donate interaction (%@) because intent (%@) has been deprecated"
- "Cannot donate interaction because intent title is empty: %@ Please make sure that your intent definition includes the following shortcut type for %@: %@."
- "Cannot donate interaction with nil identifier: %@"

```
