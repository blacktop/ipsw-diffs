## com.apple.driver.AppleSEPManager

> `com.apple.driver.AppleSEPManager`

```diff

-  __TEXT.__cstring: 0x11437
+  __TEXT.__cstring: 0x11527
   __TEXT.__const: 0xded8
-  __TEXT_EXEC.__text: 0x41bf8
+  __TEXT_EXEC.__text: 0x41f24
   __TEXT_EXEC.__auth_stubs: 0xb00
   __DATA.__data: 0x168
   __DATA.__common: 0xc48
   __DATA.__bss: 0x4e
   __DATA_CONST.__mod_init_func: 0xc0
   __DATA_CONST.__mod_term_func: 0xc0
-  __DATA_CONST.__const: 0x9f40
+  __DATA_CONST.__const: 0x9fc0
   __DATA_CONST.__kalloc_type: 0xe00
   __DATA_CONST.__kalloc_var: 0x50
   __DATA_CONST.__auth_got: 0x580
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x38
-  Functions: 2515
+  Functions: 2519
   Symbols:   0
-  CStrings:  1470
+  CStrings:  1473
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
CStrings:
+ "12111112122212121111111111111"
+ "PE_i_can_has_debugger(NULL)"
+ "decode_info != nullptr"
+ "static IOReturn AppleSEPUserClient::DispatchGetTraceRecordState(AppleSEPUserClient *, void *, IOExternalMethodArguments *)"
+ "target->_asep->cpu_trace_memory != nullptr"
+ "virtual IOReturn AppleSEPUserClient::clientMemoryForType(uint32_t, IOOptionBits *, IOMemoryDescriptor **)"
- "1211111212221212111111111111"
- "IOReturn AppleSEPControl::cmsgCPU_TRACE_GET_STREAM_FILL(uint32_t *)"
- "nullptr != fill"

```
