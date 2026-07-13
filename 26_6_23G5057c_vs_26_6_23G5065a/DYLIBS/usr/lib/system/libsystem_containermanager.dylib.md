## libsystem_containermanager.dylib

> `/usr/lib/system/libsystem_containermanager.dylib`

```diff

-  __TEXT.__text: 0x2da50
+  __TEXT.__text: 0x2db1c
   __TEXT.__auth_stubs: 0xb70
   __TEXT.__const: 0x290
   __TEXT.__cstring: 0x3a62
-  __TEXT.__oslogstring: 0x505d
+  __TEXT.__oslogstring: 0x50cb
   __TEXT.__unwind_info: 0x688
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x1c40

   - /usr/lib/system/libxpc.dylib
   Functions: 588
   Symbols:   1290
-  CStrings:  895
+  CStrings:  896
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Functions:
~ _container_traverse_directory : 4296 -> 4312
~ __container_traverse_parse_attr_buf : 3556 -> 3744
CStrings:
+ "@(#)VERSION:Container Manager: Jul  2 2026 23:50:00; MobileContainerManager_system-725.160.3~18/arm64e"
+ "Malformed attrlist on entry in [%s]; length (%u) exceeds remaining buffer (%zu); buffer = %p, buffer_end = %p"
- "@(#)VERSION:Container Manager: Jun 26 2026 15:59:50; MobileContainerManager_system-725.160.2~55/arm64e"

```
