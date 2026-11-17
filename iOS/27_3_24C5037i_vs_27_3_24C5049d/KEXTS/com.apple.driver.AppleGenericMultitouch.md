## com.apple.driver.AppleGenericMultitouch

> `com.apple.driver.AppleGenericMultitouch`

```diff

-30.0.0.0.0
-  __TEXT.__cstring: 0x6d1b
+31.0.0.0.0
+  __TEXT.__cstring: 0x6d73
   __TEXT.__const: 0x236
-  __TEXT.__os_log: 0x2b8c
-  __TEXT_EXEC.__text: 0xa5b8
+  __TEXT.__os_log: 0x2bb4
+  __TEXT_EXEC.__text: 0xa644
   __TEXT_EXEC.__auth_stubs: 0x380
   __DATA.__data: 0xd4
   __DATA.__common: 0xa8

   __DATA_CONST.__kalloc_type: 0x200
   __DATA_CONST.__auth_got: 0x1c0
   __DATA_CONST.__got: 0xc8
-  Functions: 247
+  Functions: 248
   Symbols:   0
-  CStrings:  326
+  CStrings:  327
 
CStrings:
+ "[Decider] Boot arg masks: agm-authentic present=%u 0x%x, agm-trusted present=%u 0x%x\n%s line %d"
+ "[Decider] No auth/trust boot args present\n%s line %d"
+ "[Helper %u] Interface %u: agm-authentic=0x%x, bit 0x%x -> %u\n%s line %d"
+ "[Helper %u] Interface %u: agm-trusted=0x%x, bit 0x%x -> %u\n%s line %d"
+ "void AppleGenericMultitouchDeciderHelper::applyAuthenticBootArg(uint32_t)"
+ "void AppleGenericMultitouchDeciderHelper::applyTrustedBootArg(uint32_t)"
- "[Decider] Checking boot args for all helpers\n%s line %d"
- "[Helper %u] Checking boot args for interface %u\n%s line %d"
- "[Helper %u] Interface %u: Found boot arg agm-authentic=%u\n%s line %d"
- "[Helper %u] Interface %u: Found boot arg agm-trusted=%u\n%s line %d"
- "void AppleGenericMultitouchDeciderHelper::checkBootArgs()"
```
