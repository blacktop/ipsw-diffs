## com.apple.plugin.IOgPTPPlugin

> `com.apple.plugin.IOgPTPPlugin`

```diff

-  __TEXT.__cstring: 0x6cc3
-  __TEXT.__os_log: 0x1c46f
+  __TEXT.__cstring: 0x6d31
+  __TEXT.__os_log: 0x1c585
   __TEXT.__const: 0x2d2
-  __TEXT_EXEC.__text: 0x6fcec
+  __TEXT_EXEC.__text: 0x70030
   __TEXT_EXEC.__auth_stubs: 0xe40
   __DATA.__data: 0xc8
   __DATA.__common: 0x5d8

   __DATA_CONST.__const: 0xea70
   __DATA_CONST.__kalloc_type: 0x980
   __DATA_CONST.__auth_got: 0x720
-  __DATA_CONST.__got: 0x1b0
-  Functions: 1637
+  __DATA_CONST.__got: 0x1b8
+  Functions: 1641
   Symbols:   0
-  CStrings:  1569
+  CStrings:  1577
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__auth_got : content changed
CStrings:
+ "121111121222121211111111111111111111211111111111111111111111"
+ "12111112122212121111111111111111222212121"
+ "Could not allocate number\n"
+ "IOTimeSyncNetworkPortUserClient: missing entitlement %s\n"
+ "IOTimeSyncgPTPManagerUserClient: missing entitlement %s\n"
+ "NULL == fIOTimeSyncgPTPManagerLock"
+ "com.apple.private.timesync.direct-userclient"
+ "fTimeSyncDomainLock != NULL"
+ "failed to allocate gPTP manager lock\n"
+ "super::start failed\n"
- "12111112122212121111111111111111111121111111111111111111111"
- "1211111212221212111111111111111222212121"

```
