## dyld

> `/System/ExclaveKit/usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__AUTH_CONST.__const`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA_DIRTY.__all_image_info`

```diff

-27060.1.0.0.0
-  __TEXT.__text: 0x5bc38
+27062.0.0.0.0
+  __TEXT.__text: 0x5c5cc
   __TEXT.__const: 0x1c0a8
-  __TEXT.__cstring: 0xe51e
-  __TEXT.__unwind_info: 0x1e88
+  __TEXT.__cstring: 0xe679
+  __TEXT.__unwind_info: 0x1ea8
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__const: 0xaf0
+  __DATA_CONST.__const: 0xb30
   __AUTH_CONST.__const: 0x3ee8
   __AUTH.__data: 0x470
   __DATA.__data: 0x1448

   __DATA.__common: 0x550
   __DATA.__bss: 0xba408
   __DATA_DIRTY.__all_image_info: 0x170
-  Functions: 2746
-  Symbols:   2422
-  CStrings:  1461
+  Functions: 2756
+  Symbols:   2429
+  CStrings:  1468
 
Symbols:
+ _ZNK4objc19objc_headeropt_rw_t8isLoadedEj
+ __ZN4objc7lookup8EPKhmy
+ __ZNK4objc15ObjectHashTable13forEachObjectEPKcU13block_pointerFvytRbE
+ __ZNK4objc15StringHashTable11tryGetIndexEPKc
+ __ZNK4objc19objc_headeropt_rw_t8isLoadedEj
+ ____ZN5dyld44APIs25_dyld_for_each_objc_classEPKcNS_16ReadOnlyCallbackIU13block_pointerFvPvbPbEEE_block_invoke
+ ____ZN5dyld44APIs28_dyld_for_each_objc_protocolEPKcNS_16ReadOnlyCallbackIU13block_pointerFvPvbPbEEE_block_invoke
+ __tightbeam_tss_buffer
+ _tightbeam_tss_buffer
+ _tightbeam_tss_setup.ek_dyld_bufs
- __thread_local_ipc_buffer_payload_storage
- _thread_local_ipc_buffer_payload_storage
- _thread_local_ipc_buffer_payload_storage_static.ek_dyld_bufs
CStrings:
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/dyld_exclavekit/common/OptimizerObjC.h"
+ "27062"
+ "XRT_UNLIKELY(count != 0)"
+ "_dyld_get_objc_selector(%s) => %s\n"
+ "_dyld_get_objc_selector(%s) => nullptr\n"
+ "_dyld_is_objc_constant(%d, %p)\n"
+ "_dyld_is_preoptimized_objc_image_loaded(%d) : imageID is invalid\n"
+ "_dyld_is_preoptimized_objc_image_loaded(%d) : no dyld shared cache\n"
+ "_dyld_is_preoptimized_objc_image_loaded(%d) : no objC RW header\n"
+ "_tightbeam_tss_setup(): too many static threads"
+ "get"
+ "i < count"
+ "v28@?0Q8S16^B20"
- "27060.1"
- "_dyld_for_each_objc_class"
- "_dyld_for_each_objc_protocol"
- "_dyld_get_objc_selector"
- "_dyld_objc_class_count"
- "_thread_local_ipc_buffer_payload(): too many static threads"
```
