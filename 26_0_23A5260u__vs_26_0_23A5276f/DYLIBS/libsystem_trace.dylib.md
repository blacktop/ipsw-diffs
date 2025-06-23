## libsystem_trace.dylib

> `/usr/lib/system/libsystem_trace.dylib`

```diff

-1815.0.0.0.0
-  __TEXT.__text: 0x1aa14
+1815.0.6.0.0
+  __TEXT.__text: 0x1aa78
   __TEXT.__auth_stubs: 0x1140
   __TEXT.__delay_stubs: 0x108
   __TEXT.__delay_helper: 0xa4
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xf4
   __TEXT.__const: 0x2a5
-  __TEXT.__cstring: 0x1b9b
+  __TEXT.__cstring: 0x1be3
   __TEXT.__gcc_except_tab: 0x64
   __TEXT.__oslogstring: 0x137
   __TEXT.__unwind_info: 0x4e8

   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x1c0
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x360
+  __DATA_DIRTY.__data: 0x368
   __DATA_DIRTY.__bss: 0x2d0
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/system/libcompiler_rt.dylib

   - /usr/lib/system/libsystem_symptoms.dylib
   - /usr/lib/system/libunwind.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: BD83AED3-5715-3656-A076-C6B27928263C
+  UUID: 86635457-3DD6-39E2-AA74-33A14ECFD377
   Functions: 368
   Symbols:   1086
-  CStrings:  485
+  CStrings:  486
 
Symbols:
+ ___block_descriptor_tmp.292
+ ___block_descriptor_tmp.3.488
+ ___block_descriptor_tmp.302
+ ___block_descriptor_tmp.35.304
+ ___block_descriptor_tmp.475
+ ___block_descriptor_tmp.509
+ ___block_literal_global.290
+ ___block_literal_global.367
+ ___block_literal_global.437
+ ___block_literal_global.487
+ ___block_literal_global.504
- ___block_descriptor_tmp.291
- ___block_descriptor_tmp.3.487
- ___block_descriptor_tmp.301
- ___block_descriptor_tmp.35.303
- ___block_descriptor_tmp.474
- ___block_descriptor_tmp.508
- ___block_literal_global.289
- ___block_literal_global.366
- ___block_literal_global.436
- ___block_literal_global.486
- ___block_literal_global.503
Functions:
~ __os_log_impl_flatten_and_send : 10796 -> 10816
~ __libtrace_fork_child : 392 -> 400
~ __os_trace_init_slow : 1236 -> 1248
~ _RTLogRingBufferIterateFrom : 280 -> 284
~ ___LIBTRACE_CLIENT_QUARANTINED_DUE_TO_HIGH_LOGGING_VOLUME__ : 108 -> 124
~ __os_metric_create_impl : 272 -> 312
CStrings:
+ "BUG IN CLIENT OF LIBTRACE: histogram cannot have greater than 128 bins."

```
