## powermetrics

> `/usr/bin/powermetrics`

```diff

-287.0.0.0.0
-  __TEXT.__text: 0xd5b0
-  __TEXT.__auth_stubs: 0x890
-  __TEXT.__const: 0x14c0
-  __TEXT.__cstring: 0x469c
+287.100.1.0.0
+  __TEXT.__text: 0xd85c
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__const: 0x1530
+  __TEXT.__cstring: 0x4688
+  __TEXT.__oslogstring: 0x1c
   __TEXT.__gcc_except_tab: 0x58
   __TEXT.__unwind_info: 0x290
-  __DATA_CONST.__auth_got: 0x450
-  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__auth_got: 0x460
+  __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xed0
   __DATA_CONST.__cfstring: 0x5a0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpmenergy.dylib
   - /usr/lib/libpmsample.dylib
-  UUID: 9E85F2F5-18AE-34A8-8C2D-8C8491B16EC1
+  UUID: BB13C1F0-ABD2-320D-9D51-BF070A74A3DB
   Functions: 204
-  Symbols:   157
+  Symbols:   160
   CStrings:  579
 
Symbols:
+ __os_log_default
+ __os_log_error_impl
+ _os_log_type_enabled
CStrings:
+ "task %{public}s is invalid\n"
- "task %s is invalid\n"

```
