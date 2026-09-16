## libsystem_trace.dylib

> `/usr/lib/system/libsystem_trace.dylib`

```diff

-1966.2.1.0.0
-  __TEXT.__text: 0x1b500
+1966.40.15.502.2
+  __TEXT.__text: 0x1b880
   __TEXT.__delay_stubs: 0x180
   __TEXT.__delay_helper: 0xa4
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xf4
-  __TEXT.__const: 0x2b0
-  __TEXT.__cstring: 0x1c6b
+  __TEXT.__const: 0x2c0
+  __TEXT.__cstring: 0x1d32
   __TEXT.__gcc_except_tab: 0x64
   __TEXT.__oslogstring: 0x137
   __TEXT.__unwind_info: 0x658

   - /usr/lib/system/libxpc.dylib
   Functions: 382
   Symbols:   902
-  CStrings:  420
+  CStrings:  424
 
Functions:
~ __os_log_impl_flatten_and_send : 8564 -> 8572
~ _os_metric_dimensions_create : 124 -> 128
~ __os_metric_create_impl : 312 -> 596
~ __os_metric_uint64_op_impl : 684 -> 832
~ __os_metric_int64_op_impl : 696 -> 852
~ __os_metric_double_op_impl : 704 -> 884
~ __os_metric_reset_data : 216 -> 272
~ __os_metric_emit_value_impl : 1128 -> 1188
CStrings:
+ "BUG IN CLIENT OF LIBTRACE: custom histogram cannot have greater than (128 / 2) bins."
+ "_os_metric_get_bin_count"
+ "md->type == _OS_METRIC_TYPE_HISTOGRAM"
+ "metric->metadata.type == _OS_METRIC_TYPE_HISTOGRAM"
```
