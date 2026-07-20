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

-1355.42.0.0.0
-  __TEXT.__os_log: 0x4680
+1355.44.0.0.0
+  __TEXT.__os_log: 0x47bc
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x2082
-  __TEXT_EXEC.__text: 0x27ecc
+  __TEXT.__cstring: 0x2084
+  __TEXT_EXEC.__text: 0x2809c
   __TEXT_EXEC.__auth_stubs: 0x750
   __DATA.__data: 0xc4
   __DATA.__common: 0x308

   __DATA_CONST.__got: 0xd8
   Functions: 880
   Symbols:   0
-  CStrings:  671
+  CStrings:  677
 
Functions:
~ __ZN9CCLogPipe13freeResourcesEv : 496 -> 288
~ __ZN9CCLogPipe25initWithOwnerNameCapacityEP9IOServicePKcS3_PK13CCPipeOptions : 1744 -> 1944
~ __ZN9CCLogPipe7mapPipeEy : 860 -> 968
~ __ZN9CCLogPipe19getMemoryDescriptorEy : 152 -> 516
CStrings:
+ "%s::%s() ring buffer allocation is deferred\n"
+ "%s::%s(): Log Size must be non-zero Owner:%s Pipe:%s\n"
+ "%s::%s(): Pipe size resolved to zero Owner:%s Pipe:%s\n"
+ "?"
+ "CCLogPipe::getMemoryDescriptor mapPipe(0) failed rv:0x%x map:%p owner:%s pipe:%s"
+ "CCLogPipe::getMemoryDescriptor mapPipe(1) failed rv:0x%x map:%p owner:%s pipe:%s"
```
