## com.apple.driver.ExclaveSEPManagerProxy

> `com.apple.driver.ExclaveSEPManagerProxy`

```diff

-928.40.6.0.0
+928.60.4.0.0
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x84f
-  __TEXT_EXEC.__text: 0x1d48
-  __TEXT_EXEC.__auth_stubs: 0x2b0
+  __TEXT.__cstring: 0x966
+  __TEXT_EXEC.__text: 0x21e4
+  __TEXT_EXEC.__auth_stubs: 0x2c0
   __DATA.__data: 0xc4
   __DATA.__common: 0x40
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
-  __DATA_CONST.__const: 0x6a0
+  __DATA_CONST.__const: 0x6f0
   __DATA_CONST.__kalloc_type: 0x40
-  __DATA_CONST.__auth_got: 0x158
+  __DATA_CONST.__auth_got: 0x160
   __DATA_CONST.__got: 0x28
-  Functions: 69
+  Functions: 75
   Symbols:   0
-  CStrings:  43
+  CStrings:  45
 
CStrings:
+ "!sleepThreadActive"
+ "121111121222121211111121112"
+ "ExclaveSEPManagerProxy: power off waiting for %u ms on %u power assertion(s), see ExclaveSEPManager log for holders\n"
+ "Powering down ExclaveSEPManager now\n"
+ "TB_ERROR_SUCCESS == exclavesepmanager_exclavesepmanagerproxyinterface_initiatepowertransition(&client, ps,^ (bool tb_ret) { ready_to_sleep = tb_ret; })"
+ "TB_ERROR_SUCCESS == exclavesepmanager_exclavesepmanagerproxyinterface_outboxnotemptyinterrupt(&client)"
+ "TB_ERROR_SUCCESS == exclavesepmanager_exclavesepmanagerproxyinterface_readytosleep(&client, ^ (bool ret) { ready = ret; })"
+ "TB_ERROR_SUCCESS == exclavesepmanager_exclavesepmanagerproxyinterface_reportpowerassertions(&client, ^ (uint32_t ret) { count = ret; })"
- "12111112122212121111112211"
- "Powering down ExclaveSEPManager now"
- "TB_ERROR_SUCCESS == exclavesepmanager_exclavesepmanagerproxyinterface_initiatepowertransition(&client, ps,^ (uint32_t tb_ret) { initiate_pt_ret = tb_ret; })"
- "TB_ERROR_SUCCESS == exclavesepmanager_exclavesepmanagerproxyinterface_outboxnotemptyinterrupt(&client, ^ (uint32_t ret) { message_count = ret; })"
- "message_count != __UINT32_MAX__"
- "outstanding_messages >= message_count"
```
