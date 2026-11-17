## com.apple.driver.AppleSEPManager

> `com.apple.driver.AppleSEPManager`

```diff

-928.60.4.0.0
-  __TEXT.__cstring: 0x11800
+928.60.5.0.0
+  __TEXT.__cstring: 0x11826
   __TEXT.__const: 0xdee2
-  __TEXT_EXEC.__text: 0x43adc
+  __TEXT_EXEC.__text: 0x43b90
   __TEXT_EXEC.__auth_stubs: 0xb20
   __DATA.__data: 0x168
   __DATA.__common: 0xc48

   __DATA_CONST.__auth_got: 0x590
   __DATA_CONST.__got: 0x148
   __DATA_CONST.__auth_ptr: 0x38
-  Functions: 2548
+  Functions: 2550
   Symbols:   0
-  CStrings:  1495
+  CStrings:  1497
 
CStrings:
+ "12111112122212121221122221111"
+ "_recv_ool_size <= sep_page_size * ds->getReceiveOolMaxPages()"
+ "_recv_ool_size > 0"
+ "_recv_ool_size >= sep_page_size * ds->getReceiveOolMinPages()"
+ "_send_ool_size <= sep_page_size * ds->getSendOolMaxPages()"
+ "_send_ool_size > 0"
+ "_send_ool_size >= sep_page_size * ds->getSendOolMinPages()"
- "1211111212221212122111111"
- "ool_size <= ds->getSepPageSize() * ds->getReceiveOolMaxPages()"
- "ool_size <= ds->getSepPageSize() * ds->getSendOolMaxPages()"
- "ool_size >= ds->getSepPageSize() * ds->getReceiveOolMinPages()"
- "ool_size >= ds->getSepPageSize() * ds->getSendOolMinPages()"
```
