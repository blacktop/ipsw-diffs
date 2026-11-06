## libsystem_trace.dylib

> `/usr/lib/system/libsystem_trace.dylib`

```diff

-1966.1.1.0.0
-  __TEXT.__text: 0x1bdb8
+1966.40.15.0.2
+  __TEXT.__text: 0x1c134
   __TEXT.__delay_stubs: 0x180
   __TEXT.__delay_helper: 0xa4
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xf4
   __TEXT.__const: 0x2c0
-  __TEXT.__cstring: 0x1cfa
+  __TEXT.__cstring: 0x1dc1
   __TEXT.__gcc_except_tab: 0x68
   __TEXT.__oslogstring: 0x137
   __TEXT.__unwind_info: 0x528

   __DATA.__objc_ivar: 0x34
   __DATA.__data: 0xe4
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x238
+  __DATA.__bss: 0x210
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x368
-  __DATA_DIRTY.__bss: 0x2d0
+  __DATA_DIRTY.__bss: 0x2f8
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libcorecrypto.dylib

   - /usr/lib/system/libxpc.dylib
   Functions: 394
   Symbols:   918
-  CStrings:  428
+  CStrings:  432
 
Functions:
~ __os_log_impl_flatten_and_send : 8604 -> 8612
~ _os_metric_dimensions_create : 124 -> 128
~ __os_metric_create_impl : 312 -> 596
~ __os_metric_uint64_op_impl : 700 -> 844
~ __os_metric_int64_op_impl : 708 -> 864
~ __os_metric_double_op_impl : 716 -> 896
~ __os_metric_reset_data : 228 -> 284
~ __os_metric_emit_value_impl : 1140 -> 1200
CStrings:
+ "BUG IN CLIENT OF LIBTRACE: custom histogram cannot have greater than (128 / 2) bins."
+ "_os_metric_get_bin_count"
+ "md->type == _OS_METRIC_TYPE_HISTOGRAM"
+ "metric->metadata.type == _OS_METRIC_TYPE_HISTOGRAM"
```
