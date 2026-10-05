## com.apple.driver.AppleCamera

> `com.apple.driver.AppleCamera`

```diff

-20.105.6.0.0
+20.106.4.0.0
   __TEXT.__const: 0xa290
-  __TEXT.__cstring: 0x1a571
-  __TEXT.__os_log: 0x1613c
-  __TEXT_EXEC.__text: 0xa0bc4
+  __TEXT.__cstring: 0x1a5e7
+  __TEXT.__os_log: 0x16179
+  __TEXT_EXEC.__text: 0xa1024
   __TEXT_EXEC.__auth_stubs: 0x1160
   __DATA.__data: 0x2a8
   __DATA.__common: 0x540
   __DATA_CONST.__mod_init_func: 0x98
   __DATA_CONST.__mod_term_func: 0x58
-  __DATA_CONST.__const: 0x164a8
+  __DATA_CONST.__const: 0x164d8
   __DATA_CONST.__kalloc_type: 0x13c0
   __DATA_CONST.__kalloc_var: 0xa50
   __DATA_CONST.__auth_got: 0x8b0
   __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__auth_ptr: 0x18
-  Functions: 1856
+  Functions: 1864
   Symbols:   0
-  CStrings:  2551
+  CStrings:  2554
 
CStrings:
+ "AppleCamera:%s - ISP_CacheChannelConfigs command completed: res=0x%08X\n"
+ "AppleCamera:%s - Memory allocation fail on pChannels[%d] configs, allocation size=%d\n"
+ "AppleCamera:%s - channel %d has %zu configs, driver supports %d\n"
+ "ISP_CacheChannelConfigs"
+ "ISP_CopyChannelConfigCache_gated"
- "AppleCamera:%s - CISP_CMD_CH_INFO_GET command completed: res=0x%08X\n"
- "AppleCamera:%s - memory allocation fail on pChannels[%d].fSensorConfigs, allocation size=%d\n"
```
