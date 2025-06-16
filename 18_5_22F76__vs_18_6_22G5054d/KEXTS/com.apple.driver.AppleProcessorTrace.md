## com.apple.driver.AppleProcessorTrace

> `com.apple.driver.AppleProcessorTrace`

```diff

-52.120.4.0.0
-  __TEXT.__cstring: 0x4355
+52.140.7.0.0
+  __TEXT.__cstring: 0x4237
   __TEXT.__const: 0x398
-  __TEXT.__os_log: 0x1586
-  __TEXT_EXEC.__text: 0x21370
+  __TEXT.__os_log: 0x1502
+  __TEXT_EXEC.__text: 0x20f60
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x380
-  __DATA_CONST.__auth_got: 0x308
+  __DATA_CONST.__auth_got: 0x310
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__mod_init_func: 0xb0
   __DATA_CONST.__mod_term_func: 0xb0
-  __DATA_CONST.__const: 0x83f8
+  __DATA_CONST.__const: 0x83c0
   __DATA_CONST.__kalloc_type: 0x580
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: FF90E107-1045-370B-A319-2B3F1464C1FE
-  Functions: 1213
+  UUID: C2490ED3-AFA5-3907-9CAB-A8A4584E834A
+  Functions: 1208
   Symbols:   0
-  CStrings:  417
+  CStrings:  407
 
CStrings:
+ "(config.buffer_size & ((128 << 10) - 1)) != 0"
+ "121121212122121322132111"
+ "AppleProcessorTrace::buffer size %lx\n"
+ "config.buffer_size < ( 16 << 20)"
- "!(physical_address & (PAGE_SIZE - 1))"
- "!(segment_length & (PAGE_SIZE - 1))"
- "!va_region_retyped"
- "12112121212212132213211121212"
- "AppleProcessorTrace::buffer size %llx\n"
- "AppleProcessorTrace::mapBufferVA : prepared\n"
- "AppleProcessorTraceVirtualBufferMemoryDescriptor.cpp"
- "AppleProcessorTraceVirtualBufferMemoryDescriptor::retype : retyping to traceable\n"
- "AppleProcessorTraceVirtualBufferMemoryDescriptor::unretype retype to normal.\n"
- "buffer_size == VATraceBuffer->getCapacity()"
- "config.buffer_size < (1 << 24)"
- "nb_pages"
- "void AppleProcessorTraceVirtualBufferMemoryDescriptor::retype()"
- "void AppleProcessorTraceVirtualBufferMemoryDescriptor::unretype()"

```
