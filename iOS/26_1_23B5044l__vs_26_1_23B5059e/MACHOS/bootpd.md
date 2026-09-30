## bootpd

> `/usr/libexec/bootpd`

```diff

-529.0.0.0.0
-  __TEXT.__text: 0x10e7c
+531.0.0.0.0
+  __TEXT.__text: 0x1120c
   __TEXT.__auth_stubs: 0x970
   __TEXT.__const: 0xe8
   __TEXT.__cstring: 0x1ed1
-  __TEXT.__oslogstring: 0x114f
-  __TEXT.__unwind_info: 0x2e8
+  __TEXT.__oslogstring: 0x11a2
+  __TEXT.__unwind_info: 0x2f0
   __DATA_CONST.__auth_got: 0x4b8
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x18

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libresolv.9.dylib
-  UUID: 090C7447-E03A-3117-A533-340CEC7A651A
-  Functions: 201
+  UUID: 49A7D47A-9DD9-3160-A0F4-B351A176A392
+  Functions: 203
   Symbols:   197
-  CStrings:  745
+  CStrings:  747
 
CStrings:
+ "%s re-using flags 0x%x (generation %qu)\n"
+ "%s: SIOCGIFGENERATIONID failed status, %s"

```
