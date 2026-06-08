## com.apple.driver.ApplePTD

> `com.apple.driver.ApplePTD`

```diff

-30.0.0.0.0
-  __TEXT.__cstring: 0x1aa9
+47.0.0.502.1
+  __TEXT.__cstring: 0x1d85
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x872c
+  __TEXT_EXEC.__text: 0x8d8c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
-  __DATA.__common: 0xf8
-  __DATA_CONST.__auth_got: 0x168
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__mod_init_func: 0x18
-  __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0xf68
-  __DATA_CONST.__kalloc_type: 0x100
+  __DATA.__common: 0x120
+  __DATA_CONST.__mod_init_func: 0x20
+  __DATA_CONST.__mod_term_func: 0x20
+  __DATA_CONST.__const: 0x10d0
+  __DATA_CONST.__kalloc_type: 0x140
   __DATA_CONST.__kalloc_var: 0x1e0
-  UUID: 988277B9-0FFF-3BD9-A840-13914C5ADBF5
-  Functions: 237
+  __DATA_CONST.__auth_got: 0x188
+  __DATA_CONST.__got: 0xa0
+  UUID: 793FFC36-BBBC-3859-99F6-007D5270EDAF
+  Functions: 270
   Symbols:   0
-  CStrings:  198
+  CStrings:  219
 
CStrings:
+ "%s: EntriesCount %d\n"
+ "%s: common start complete\n"
+ "%s: full path is %s\n"
+ "%s: getPath failed, len=%d\n"
+ "%s: logging at level >= 1\n"
+ "%s: logging at level >= 2\n"
+ "%s: registerInterrupt source %d, id %x, irq %d, irq entry %d\n"
+ "%s: start complete\n"
+ "%s: starting\n"
+ "%s: terminating\n"
+ "12111112122212121111111111111112222222211112"
+ "12121112"
+ "ApplePTDAccessorConcrete::ApplePTDAccessorConcrete(ApplePTD *)"
+ "ApplePTDCommon"
+ "ApplePTDCommon.cpp"
+ "Finding ptd_id=0x%x, _ptdTableRows=%u\n"
+ "IOReturn ApplePTDCommon::_ptdFindAndCheckEntry(ptd_data_entry_t *, ptd_function_args_t *)"
+ "IOReturn ApplePTDCommon::_ptdInsertEntry(ptd_data_entry_t *)"
+ "IOReturn ApplePTDCommon::_ptdLookupLength(uint32_t, uint32_t *)"
+ "IOReturn ApplePTDCommon::_ptdLookupMultiple(ptd_data_entry_t *, uint32_t)"
+ "IOReturn ApplePTDCommon::_ptdReadMultiple(ptd_function_args_t *, uint32_t, bool, const ApplePTDAccessor &)"
+ "IOReturn ApplePTDCommon::appleARMFunctionNew(void *, void *)"
+ "IOReturn ApplePTDCommon::ptdDoCmdOp(ptd_cmd_t, uintptr_t, const ApplePTDAccessor &)"
+ "IOReturn ApplePTDCommon::ptdDoMultiCmdOp(ptd_cmd_t, uintptr_t, uint64_t, const ApplePTDAccessor &)"
+ "IOReturn ApplePTDCommon::ptdEntryStruct(OSDictionary *, ptd_data_entry_t *)"
+ "No ptd entries populated!\n"
+ "_name"
+ "bool ApplePTDCommon::init(const char *)"
+ "bool ApplePTDCommon::start(IOService *, IOService *)"
+ "common->start(provider, this)"
+ "p"
+ "site.ApplePTDCommon"
+ "static SInt32 ApplePTDCommon::_ptdSortFunction(const OSMetaClassBase *, const OSMetaClassBase *, void *)"
+ "super::start(provider)"
+ "virtual IOReturn ApplePTD::registerInterrupt(IOService *, const int, void *, IOInterruptHandler, void *)"
- "%s: started\n"
- "%s:EntriesCount %d\n"
- "12111112122212121111111111111122222222111112112"
- "IOReturn ApplePTD::_ptdEntryStruct(OSDictionary *, ptd_data_entry_t *)"
- "IOReturn ApplePTD::_ptdFindAndCheckEntry(ptd_data_entry_t *, ptd_function_args_t *)"
- "IOReturn ApplePTD::_ptdInsertEntry(ptd_data_entry_t *)"
- "IOReturn ApplePTD::_ptdLookupLength(uint32_t, uint32_t *)"
- "IOReturn ApplePTD::_ptdLookupMultiple(ptd_data_entry_t *, uint32_t)"
- "IOReturn ApplePTD::_ptdReadMultiple(ptd_function_args_t *, uint32_t, bool)"
- "OSDictionary *ApplePTD::_ptdFindEntry(uint32_t)"
- "result"
- "static SInt32 ApplePTD::_ptdSortFunction(const OSMetaClassBase *, const OSMetaClassBase *, void *)"
- "virtual IOReturn ApplePTD::callPlatformFunction(const OSSymbol *, bool, void *, void *, void *, void *)"
- "virtual IOReturn ApplePTD::registerInterrupt(IOService *, int, void *, IOInterruptHandler, void *)"

```
