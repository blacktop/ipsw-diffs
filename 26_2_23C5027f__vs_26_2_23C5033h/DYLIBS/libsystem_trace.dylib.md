## libsystem_trace.dylib

> `/usr/lib/system/libsystem_trace.dylib`

```diff

-1815.60.3.0.0
-  __TEXT.__text: 0x1aad0
+1815.60.5.0.0
+  __TEXT.__text: 0x1ab84
   __TEXT.__auth_stubs: 0x1140
   __TEXT.__delay_stubs: 0x108
   __TEXT.__delay_helper: 0xa4

   - /usr/lib/system/libsystem_symptoms.dylib
   - /usr/lib/system/libunwind.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: E5549299-E2F0-391C-992E-4D1C8A28CE31
+  UUID: AFED4ABF-9B45-31B0-9CBE-8516409EEF29
   Functions: 369
   Symbols:   1087
   CStrings:  487
Symbols:
+ __os_metric_emit_value_impl
- __os_metric_emit_value
Functions:
~ __os_metric_uint64_op_impl : 652 -> 696
~ __os_metric_emit_value -> __os_metric_emit_value_impl : 1092 -> 1104
~ __os_metric_int64_op_impl : 664 -> 708
~ __os_metric_double_op_impl : 660 -> 716
~ __os_metric_reset_impl : 84 -> 108

```
