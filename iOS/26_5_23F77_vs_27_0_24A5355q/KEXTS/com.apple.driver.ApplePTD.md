## com.apple.driver.ApplePTD

> `com.apple.driver.ApplePTD`

```diff

-30.0.0.0.0
-  __TEXT.__cstring: 0x1aa9 sha256:953267a54d8f58a6eb116ecd0fa14d8e69cd6828a94b85559a9b763f22f89d51
+47.0.0.502.1
+  __TEXT.__cstring: 0x1d85 sha256:e84e9a7274abb1db9ff1f5ead97840db4e6393aa3b474ca0f87c844e8356c9ed
   __TEXT.__const: 0x20 sha256:f1e0c5785a018e50c1d633174cd4b4d7dbf43b6f6138c468887431448a6b55cc
-  __TEXT_EXEC.__text: 0x872c sha256:80898f4fa4de211244a5677baefd67e92f1a84db1f7e91360c41e6fb6273fd3b
+  __TEXT_EXEC.__text: 0x8d8c sha256:2618ef35e7d23ef21759c52fabf0891f1b11d6f513aea2b2795a00bbc82e9e93
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc4 sha256:619568600f534009f8aa57ec56c582701bc5f967bb37ea6ddebc9869f8726523
-  __DATA.__common: 0xf8 sha256:b3ab6982980fddf460a2f47adb428475ce9afa89092fd034499d017a35993f05
-  __DATA_CONST.__auth_got: 0x168 sha256:a94f4bd20459ebb47d60ba6c1c9297e15c6fd653bab28b8c7bf264a9171a1f9a
-  __DATA_CONST.__got: 0x88 sha256:bff4d0639929ab9b4dd745c5c259f53b40ee277a8c03cfb0c4a47deedaabf24e
-  __DATA_CONST.__mod_init_func: 0x18 sha256:487313285ad24c43552a441a14c1ec0e735cbe1263d5fe28aaf0adfcba2011ac
-  __DATA_CONST.__mod_term_func: 0x18 sha256:511e6b52abc7a0aa50abfac69c7e7f8d0892dc55fa9da483225d61509210e901
-  __DATA_CONST.__const: 0xf68 sha256:e683202aa7d9ca7472dafa34685eb350fbd4693da5ba9062498d33c7942bb0a0
-  __DATA_CONST.__kalloc_type: 0x100 sha256:ef3310ee26f1e57c7cd53114b103726fdcc8c8f3696db259f95db252df4dc324
-  __DATA_CONST.__kalloc_var: 0x1e0 sha256:2508fec4a15d589939034abcd000a7616738b38fae3d10b9784bc727f9a4df03
-  UUID: 988277B9-0FFF-3BD9-A840-13914C5ADBF5
-  Functions: 237
+  __DATA.__data: 0xc4 sha256:69ab06ed43959019a558fa1868b9d404ff129bb3ee0d81136d1b5400ac2a8e7a
+  __DATA.__common: 0x120 sha256:2d5565fb483d8ea4525a7a9229677d1038ad34b6e22c8d5152e1d7f7b9817597
+  __DATA_CONST.__mod_init_func: 0x20 sha256:14b86ac6b5db3f37d996d40090f837ecdd89f146bbdfa4d060bb943c3c94e502
+  __DATA_CONST.__mod_term_func: 0x20 sha256:9ab07de63a3abb095d668ffc37f37dbc491108e19bed514e40e523185aafa198
+  __DATA_CONST.__const: 0x10d0 sha256:723dcc795c7cfc4724c334e53d9a3e8ecbf1a967e893cfc1457f12c6ea00ef31
+  __DATA_CONST.__kalloc_type: 0x140 sha256:4bd6240a52d9ee62e45adad9dec40aaaf545961b457431ec985b33212aea3bf1
+  __DATA_CONST.__kalloc_var: 0x1e0 sha256:aa56d50c42dbc98cc2f10af4e3e7e29e0086a12fb0629685a242c8e1d33ba555
+  __DATA_CONST.__auth_got: 0x188 sha256:7040cdf59a28b2aeedff05a12d4946014dacb861d5e9baf91d37491185f9ba05
+  __DATA_CONST.__got: 0xa0 sha256:2820aa3a0317012309843a5f9e13f0c12a0a473bd1bdded849c1a6b1e0c735c8
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
