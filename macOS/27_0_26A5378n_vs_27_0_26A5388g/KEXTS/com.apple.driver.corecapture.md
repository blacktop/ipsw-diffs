## com.apple.driver.corecapture

> `com.apple.driver.corecapture`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-1345.39.0.0.0
-  __TEXT.__os_log: 0x4733
+1345.42.0.0.0
+  __TEXT.__os_log: 0x486f
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x20df
-  __TEXT_EXEC.__text: 0x29028
+  __TEXT.__cstring: 0x20e1
+  __TEXT_EXEC.__text: 0x29218
   __TEXT_EXEC.__auth_stubs: 0x790
   __DATA.__data: 0xc5
   __DATA.__common: 0x308

   __DATA_CONST.__auth_got: 0x3c8
   __DATA_CONST.__got: 0xd8
   Functions: 879
-  Symbols:   1973
-  CStrings:  679
+  Symbols:   1978
+  CStrings:  685
 
Symbols:
+ __ZZN9CCLogPipe13freeResourcesEvE20kalloc_type_view_531
+ __ZZN9CCLogPipe18freeScratchBuffersEvE21kalloc_type_view_1598
+ __ZZN9CCLogPipe18initScratchBuffersEmmE21kalloc_type_view_1563
+ __ZZN9CCLogPipe19getMemoryDescriptorEyE11_os_log_fmt_0
+ __ZZN9CCLogPipe19getMemoryDescriptorEyE11_os_log_fmt_1
+ __ZZN9CCLogPipe25initWithOwnerNameCapacityEP9IOServicePKcS3_PK13CCPipeOptionsE11_os_log_fmt_9
+ __ZZN9CCLogPipe25initWithOwnerNameCapacityEP9IOServicePKcS3_PK13CCPipeOptionsE11_os_log_fmt__10_
+ __ZZN9CCLogPipe25initWithOwnerNameCapacityEP9IOServicePKcS3_PK13CCPipeOptionsE20kalloc_type_view_213
+ __ZZN9CCLogPipe25initWithOwnerNameCapacityEP9IOServicePKcS3_PK13CCPipeOptionsE20kalloc_type_view_253
+ __ZZN9CCLogPipe4freeEvE20kalloc_type_view_512
+ __ZZN9CCLogPipe7mapPipeEyE11_os_log_fmt_0
- __ZZN9CCLogPipe13freeResourcesEvE20kalloc_type_view_524
- __ZZN9CCLogPipe18freeScratchBuffersEvE21kalloc_type_view_1546
- __ZZN9CCLogPipe18initScratchBuffersEmmE21kalloc_type_view_1511
- __ZZN9CCLogPipe25initWithOwnerNameCapacityEP9IOServicePKcS3_PK13CCPipeOptionsE20kalloc_type_view_201
- __ZZN9CCLogPipe25initWithOwnerNameCapacityEP9IOServicePKcS3_PK13CCPipeOptionsE20kalloc_type_view_241
- __ZZN9CCLogPipe4freeEvE20kalloc_type_view_500
Functions:
~ __ZN9CCLogPipe13freeResourcesEv : 496 -> 288
~ __ZN9CCLogPipe25initWithOwnerNameCapacityEP9IOServicePKcS3_PK13CCPipeOptions : 1744 -> 1944
~ __ZN9CCLogPipe7mapPipeEy : 860 -> 968
~ __ZN9CCLogPipe19getMemoryDescriptorEy : 152 -> 548
CStrings:
+ "%s::%s() ring buffer allocation is deferred\n"
+ "%s::%s(): Log Size must be non-zero Owner:%s Pipe:%s\n"
+ "%s::%s(): Pipe size resolved to zero Owner:%s Pipe:%s\n"
+ "?"
+ "CCLogPipe::getMemoryDescriptor mapPipe(0) failed rv:0x%x map:%p owner:%s pipe:%s"
+ "CCLogPipe::getMemoryDescriptor mapPipe(1) failed rv:0x%x map:%p owner:%s pipe:%s"
```
