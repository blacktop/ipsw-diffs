## Intents

> `/System/Library/Frameworks/Intents.framework/Versions/A/Intents`

```diff

-3506.0.1.0.0
+3601.0.0.0.0
   __TEXT.__text: 0x4b04a8
   __TEXT.__auth_stubs: 0xd30
   __TEXT.__objc_methlist: 0x7a9b4
   __TEXT.__const: 0x1dc8
   __TEXT.__dlopen_cstrs: 0xb0a
   __TEXT.__gcc_except_tab: 0x1fa4
-  __TEXT.__oslogstring: 0x527a
-  __TEXT.__cstring: 0x4bace
+  __TEXT.__oslogstring: 0x52d0
+  __TEXT.__cstring: 0x4baef
   __TEXT.__ustring: 0x512
   __TEXT.__unwind_info: 0xf588
   __TEXT.__objc_classname: 0x12514

   - /usr/lib/libobjc.A.dylib
   Functions: 31117
   Symbols:   59851
-  CStrings:  29194
+  CStrings:  29195
 
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
