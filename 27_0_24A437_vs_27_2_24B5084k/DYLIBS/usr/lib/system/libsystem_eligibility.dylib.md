## libsystem_eligibility.dylib

> `/usr/lib/system/libsystem_eligibility.dylib`

```diff

-446.2.3.0.0
-  __TEXT.__text: 0x416c
-  __TEXT.__const: 0x760
-  __TEXT.__cstring: 0x57e1
+446.40.34.502.1
+  __TEXT.__text: 0x4244
+  __TEXT.__const: 0x768
+  __TEXT.__cstring: 0x5815
   __TEXT.__oslogstring: 0x39b
-  __TEXT.__unwind_info: 0xe8
+  __TEXT.__unwind_info: 0xf8
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xf08
   __DATA_CONST.__got: 0x0

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 28
-  Symbols:   78
-  CStrings:  549
+  Functions: 32
+  Symbols:   82
+  CStrings:  551
 
Symbols:
+ _eligibility_xpc_create_set_input_message
+ _os_eligibility_reset_all_inputs
+ _os_eligibility_reset_input
+ _os_eligibility_set_input_forced
CStrings:
+ "OS_ELIGIBILITY_INPUT_CELLULAR_CAPABLE_DEVICE"
+ "forced"
```
