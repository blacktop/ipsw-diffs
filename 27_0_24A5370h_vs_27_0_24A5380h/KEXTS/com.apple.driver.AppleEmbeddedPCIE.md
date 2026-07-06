## com.apple.driver.AppleEmbeddedPCIE

> `com.apple.driver.AppleEmbeddedPCIE`

```diff

-  __TEXT.__cstring: 0x7152
+  __TEXT.__cstring: 0x7277
   __TEXT.__os_log: 0x32dd
   __TEXT.__const: 0x178
-  __TEXT_EXEC.__text: 0x33898
+  __TEXT_EXEC.__text: 0x33e00
   __TEXT_EXEC.__auth_stubs: 0x930
   __DATA.__data: 0x3d8
   __DATA.__common: 0x188
   __DATA.__bss: 0x8
   __DATA_CONST.__mod_init_func: 0x40
   __DATA_CONST.__mod_term_func: 0x40
-  __DATA_CONST.__const: 0x2c98
-  __DATA_CONST.__kalloc_type: 0x280
+  __DATA_CONST.__const: 0x2cb8
+  __DATA_CONST.__kalloc_type: 0x300
   __DATA_CONST.__kalloc_var: 0x140
   __DATA_CONST.__auth_got: 0x498
   __DATA_CONST.__got: 0x190
-  Functions: 504
+  Functions: 507
   Symbols:   0
-  CStrings:  802
+  CStrings:  811
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
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
