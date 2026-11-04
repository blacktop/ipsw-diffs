## com.apple.driver.ApplePTD

> `com.apple.driver.ApplePTD`

```diff

-50.40.4.0.0
-  __TEXT.__cstring: 0x1d85
+50.60.5.0.0
+  __TEXT.__cstring: 0x20e3
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x8e04
+  __TEXT_EXEC.__text: 0xa814
   __TEXT_EXEC.__auth_stubs: 0x310
   __DATA.__data: 0xc4
   __DATA.__common: 0x120
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x10d0
+  __DATA_CONST.__const: 0x1178
   __DATA_CONST.__kalloc_type: 0x140
   __DATA_CONST.__kalloc_var: 0x1e0
   __DATA_CONST.__auth_got: 0x188
   __DATA_CONST.__got: 0xa0
-  Functions: 270
+  Functions: 291
   Symbols:   0
-  CStrings:  219
+  CStrings:  243
 
CStrings:
+ "%s: DumpVector src %d (%d)\n"
+ "%s: EnableVector src %d en %d (%d)\n"
+ "%s: TestVector src %d loops %d (%d)\n"
+ "%s: client %p provider %p\n"
+ "%s: client not supported!\n"
+ "%s: cmd %d ptd_id 0x%x (%d)\n"
+ "%s: cmd %d ptd_id 0x%x vers 0x%x (%d)\n"
+ "%s: kApplePTDUserClientMethodGetAllPTD\n"
+ "%s: kApplePTDUserClientMethodLookupPTD\n"
+ "%s: no provider found for client!!!!\n"
+ "%s: pData %p len %u\n"
+ "%s: ptd_id 0x%x offset 0x%x entries 0x%x pData %p len %d\n"
+ "%s: ptd_id 0x%x pData %p len %d\n"
+ "%s: smc interface %p\n"
+ "%s: smc rd ptd_id 0x%x (%d)\n"
+ "%s: smc wr ptd_id 0x%x (%d)\n"
+ "%s: waitForMatchingService timed out for target %d\n"
+ "121111121222121211111111111111112222222211112"
+ "AppleBTM"
+ "AppleCLPC"
+ "ApplePTDAccessorLocal::ApplePTDAccessorLocal(ApplePTD *)"
+ "GetUserClientProvider"
+ "entries == 0 || (msgOut && metaOut)"
+ "entries == 0 || msgIn"
+ "virtual IOReturn ApplePTD::dumpInterrupt(IOService *, int)"
+ "virtual IOReturn ApplePTD::readViaSMC(uint32_t, uint8_t, uint8_t, bool, uint64_t *, uint64_t *)"
+ "virtual IOReturn ApplePTD::writeViaSMC(uint32_t, uint8_t, uint8_t, uint64_t *)"
- "12111112122212121111111111111112222222211112"
- "ApplePTDAccessorConcrete::ApplePTDAccessorConcrete(ApplePTD *)"
- "IOReturn ApplePTD::dumpInterrupt(IOService *, int)"
```
