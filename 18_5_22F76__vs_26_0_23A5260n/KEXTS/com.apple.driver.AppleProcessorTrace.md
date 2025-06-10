## com.apple.driver.AppleProcessorTrace

> `com.apple.driver.AppleProcessorTrace`

```diff

-52.120.4.0.0
-  __TEXT.__cstring: 0x4355
-  __TEXT.__const: 0x398
-  __TEXT.__os_log: 0x1586
-  __TEXT_EXEC.__text: 0x21370
+78.0.7.0.0
+  __TEXT.__os_log: 0x1664
+  __TEXT.__cstring: 0x47e0
+  __TEXT.__const: 0x3b8
+  __TEXT_EXEC.__text: 0x246fc
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8
-  __DATA.__common: 0x380
-  __DATA_CONST.__auth_got: 0x308
+  __DATA.__data: 0xc4
+  __DATA.__common: 0x3a8
+  __DATA_CONST.__auth_got: 0x320
   __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__mod_init_func: 0xb0
-  __DATA_CONST.__mod_term_func: 0xb0
-  __DATA_CONST.__const: 0x83f8
-  __DATA_CONST.__kalloc_type: 0x580
-  __DATA_CONST.__kalloc_var: 0xa0
-  UUID: FF90E107-1045-370B-A319-2B3F1464C1FE
-  Functions: 1213
+  __DATA_CONST.__mod_init_func: 0xb8
+  __DATA_CONST.__mod_term_func: 0xb8
+  __DATA_CONST.__const: 0x8590
+  __DATA_CONST.__kalloc_type: 0x5c0
+  __DATA_CONST.__kalloc_var: 0xf0
+  UUID: 622CADDC-2167-394C-AAB8-A13181AFAEB0
+  Functions: 951
   Symbols:   0
-  CStrings:  417
+  CStrings:  431
 
CStrings:
+ "(config.buffer_size & ((128 << 10) - 1)) != 0"
+ "1"
+ "121111121222121211111112112"
+ "121111121222121211111112112211211"
+ "121111121222121211111112112211211211211"
+ "121111121222121211111112112211211211211211211211211211211211211"
+ "121111121222121211111112112211211211211211211211211211211211211211211211211211211"
+ "121111121222121211111112112211211211211211211211211211211211211211211211211211211211211211211211211211211211"
+ "12122"
+ "AppleProcessorTraceFracturedMemoryMap"
+ "FeatureFlags"
+ "OSSharedPtr<IOMemoryDescriptor> AppleProcessorTraceSession::getBufferPA()"
+ "OSSharedPtr<IOMemoryDescriptor> AppleProcessorTraceSession::getBufferVA()"
+ "Q24@?0^v8Q16"
+ "bounded_ptr<T>::operator+=(n): Calculating the number of bytes to add to the offset (n * sizeof(T)) would trigger an overflow"
+ "config.buffer_size < (16 << 20)"
+ "config.buffer_size > vm_map_kernel_max_simple_mappable_size()"
+ "config.delay_posting_chunk_fills"
+ "site.AppleProcessorTraceFracturedMemoryMap"
+ "virtual void AppleProcessorTraceT6040::defeatureCore(bool)"
+ "virtual void AppleProcessorTraceT8132::defeatureCore(bool)"
+ "virtual void AppleProcessorTraceT8140::defeatureCore(bool)"
+ "void AppleProcessorTraceSession::drainDirtyChunksAndAdviseThrottle()"
+ "void AppleProcessorTraceSession::transferFilledFreeChunksToDirtyQueue()"
- "12111112122212121111111112112"
- "12111112122212121111111112112211211"
- "12111112122212121111111112112211211211211"
- "12111112122212121111111112112211211211211211211211211211211211211"
- "12111112122212121111111112112211211211211211211211211211211211211211211211211211211"
- "12111112122212121111111112112211211211211211211211211211211211211211211211211211211211211211211211211211211211"
- "IOMemoryDescriptor *AppleProcessorTraceSession::getBufferPA()"
- "IOMemoryDescriptor *AppleProcessorTraceSession::getBufferVA()"
- "config.buffer_size < (1 << 24)"
- "void AppleProcessorTraceSession::drainDirtyChunks()"

```
