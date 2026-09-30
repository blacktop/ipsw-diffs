## com.apple.driver.AppleEmbeddedPCIE

> `com.apple.driver.AppleEmbeddedPCIE`

```diff

-  __TEXT.__cstring: 0x7152
+  __TEXT.__cstring: 0x7277
   __TEXT.__os_log: 0x32dd
   __TEXT.__const: 0x178
-  __TEXT_EXEC.__text: 0x34048
+  __TEXT_EXEC.__text: 0x345b0
   __TEXT_EXEC.__auth_stubs: 0x930
   __DATA.__data: 0x3d8
   __DATA.__common: 0x188
   __DATA.__bss: 0x8
   __DATA_CONST.__mod_init_func: 0x40
   __DATA_CONST.__mod_term_func: 0x40
-  __DATA_CONST.__const: 0x4558
-  __DATA_CONST.__kalloc_type: 0x280
+  __DATA_CONST.__const: 0x4578
+  __DATA_CONST.__kalloc_type: 0x300
   __DATA_CONST.__kalloc_var: 0x140
   __DATA_CONST.__auth_got: 0x498
   __DATA_CONST.__got: 0x190
-  Functions: 504
-  Symbols:   1382
-  CStrings:  802
+  Functions: 507
+  Symbols:   1388
+  CStrings:  811
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ __ZN27AppleEmbeddedPCIEUserClient11extLockPortEP25IOExternalMethodArguments
+ __ZN27AppleEmbeddedPCIEUserClient18lockPortThreadCallEPv
+ __ZZN27AppleEmbeddedPCIEUserClient11extLockPortEP25IOExternalMethodArgumentsE20kalloc_type_view_754
+ __ZZN27AppleEmbeddedPCIEUserClient18lockPortThreadCallEPvE20kalloc_type_view_803
+ ____ZN27AppleEmbeddedPCIEUserClient18lockPortThreadCallEPv_block_invoke
CStrings:
+ "1121"
+ "AppleEmbeddedPCIEUserClient.cpp"
+ "IOReturn AppleEmbeddedPCIEUserClient::extLockPort(IOExternalMethodArguments *)"
+ "[%s()] duration argument must not exceed %u seconds\n"
+ "extLockPort"
+ "site.struct lockPortData"
+ "threadData != NULL"
+ "threadData->lock"
+ "thread_call_enter1(threadCall, threadData) != TRUE"

```
