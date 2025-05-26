## libpmenergy.dylib

> `/usr/lib/libpmenergy.dylib`

```diff

-278.0.0.0.0
-  __TEXT.__text: 0x20bc
+281.0.0.0.0
+  __TEXT.__text: 0x2464
   __TEXT.__auth_stubs: 0x1e0
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x793
+  __TEXT.__cstring: 0x82b
   __TEXT.__unwind_info: 0x84
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0xe0

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  Functions: 41
-  Symbols:   42
-  CStrings:  91
+  Functions: 47
+  Symbols:   44
+  CStrings:  99
 
Symbols:
+ _pm_task_add_version
+ _pm_task_subtract_version
CStrings:
+ "current->cycles"
+ "current->instructions"
+ "current->pcycles"
+ "current->pinstructions"
+ "last->cycles"
+ "last->instructions"
+ "last->pcycles"
+ "last->pinstructions"
+ "pm_task_arithmetic_version"
- "pm_task_arithmetic"

```
