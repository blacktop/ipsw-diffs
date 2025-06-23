## com.apple.driver.AppleProcessorTrace

> `com.apple.driver.AppleProcessorTrace`

```diff

-78.0.7.0.0
-  __TEXT.__os_log: 0x1664
-  __TEXT.__cstring: 0x47e0
+78.0.11.0.0
+  __TEXT.__os_log: 0x1596
+  __TEXT.__cstring: 0x46b1
   __TEXT.__const: 0x3b8
-  __TEXT_EXEC.__text: 0x246fc
+  __TEXT_EXEC.__text: 0x243e0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x3a8
-  __DATA_CONST.__auth_got: 0x320
+  __DATA_CONST.__auth_got: 0x328
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__mod_init_func: 0xb8
   __DATA_CONST.__mod_term_func: 0xb8
-  __DATA_CONST.__const: 0x8590
+  __DATA_CONST.__const: 0x8558
   __DATA_CONST.__kalloc_type: 0x5c0
   __DATA_CONST.__kalloc_var: 0xf0
-  UUID: 622CADDC-2167-394C-AAB8-A13181AFAEB0
-  Functions: 951
+  UUID: AC65286E-30B9-3D0A-B7A4-9E4EFA41DCAA
+  Functions: 954
   Symbols:   0
-  CStrings:  431
+  CStrings:  421
 
CStrings:
+ "121121212122121322132111"
+ "AppleProcessorTrace::buffer size %lx\n"
+ "_traceableTaskToken == nullptr"
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
- "nb_pages"
- "void AppleProcessorTraceVirtualBufferMemoryDescriptor::retype()"
- "void AppleProcessorTraceVirtualBufferMemoryDescriptor::unretype()"

```
