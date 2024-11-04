## libapp_launch_measurement.dylib

> `/usr/lib/libapp_launch_measurement.dylib`

```diff

-23.0.0.0.0
-  __TEXT.__text: 0x3ff4
-  __TEXT.__auth_stubs: 0x460
+25.0.0.0.0
+  __TEXT.__text: 0x40ec
+  __TEXT.__auth_stubs: 0x470
   __TEXT.__const: 0x88
   __TEXT.__cstring: 0x45b
-  __TEXT.__oslogstring: 0x897
-  __TEXT.__unwind_info: 0x160
+  __TEXT.__oslogstring: 0x91d
+  __TEXT.__unwind_info: 0x148
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x230
-  __AUTH_CONST.__auth_got: 0x230
+  __AUTH_CONST.__auth_got: 0x238
   __AUTH_CONST.__const: 0x100
   __DATA.__bss: 0xc0
   __DATA_DIRTY.__data: 0x1

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   Functions: 97
-  Symbols:   171
-  CStrings:  94
+  Symbols:   172
+  CStrings:  96
 
Symbols:
+ _kdebug_trace
+ _os_variant_has_internal_content
- _os_variant_has_internal_diagnostics
CStrings:
+ "ApplicationLaunchPageInCount"
+ "IsForeground=%!{(MISSING)public, signpost.telemetry:number1}d PageInCount=%!{(MISSING)public, signpost.telemetry:number2}llu"

```
