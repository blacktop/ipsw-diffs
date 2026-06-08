## com.apple.driver.AppleProcessorTrace

> `com.apple.driver.AppleProcessorTrace`

```diff

-78.100.33.0.0
-  __TEXT.__os_log: 0x195e
+125.0.0.0.0
+  __TEXT.__os_log: 0x194f
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x52d0
-  __TEXT_EXEC.__text: 0x2fb60
+  __TEXT.__cstring: 0x5403
+  __TEXT_EXEC.__text: 0x33ca4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x6e8
-  __DATA_CONST.__auth_got: 0x3c0
-  __DATA_CONST.__got: 0xb0
   __DATA_CONST.__mod_init_func: 0xd0
   __DATA_CONST.__mod_term_func: 0xd0
-  __DATA_CONST.__const: 0x9c08
+  __DATA_CONST.__const: 0x9cf0
+  __DATA_CONST.__weak_auth_got: 0xb0
   __DATA_CONST.__kalloc_type: 0x680
   __DATA_CONST.__kalloc_var: 0xf0
-  UUID: 9A2BE757-F297-3D52-A60E-B2C2B23A26FB
-  Functions: 1143
+  __DATA_CONST.__auth_got: 0x310
+  __DATA_CONST.__got: 0xb0
+  UUID: 04ED7DC7-B49E-3321-B65A-D3CBE8D2397F
+  Functions: 1166
   Symbols:   0
-  CStrings:  492
+  CStrings:  494
 
CStrings:
+ "\"failed to find the PMGR block offset in EDT. Looked up under 'pmgr' and 'pmgr-child'.\" @%s:%d"
+ "(!isExceptionLevelDisabled(config, ExceptionLevel::EL2)) && (!caps.ProdTraceEL2)"
+ "121111121222121211111112112211211211"
+ "121111121222121211111112112211211211211211211"
+ "121111121222121211111112112211211211211211211211211211211211211211211211211211211"
+ "121111121222121211111112112211211211211211211211211211211211211211211211211211211211211211211"
+ "121111121222121211111112112211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211"
+ "12122111121121222222222222221122111212112111"
+ "AppleProcessorTraceACC8_9_10Src.hpp"
+ "AppleProcessorTraceUserClient::externalMethodGetSystemMetadata\n"
+ "pmgr-child"
+ "start_va == (volatile const char *)VATraceBufferMap->getVirtualAddress()"
+ "static IOReturn AppleProcessorTraceUserClient::externalMethodGetSystemMetadata(OSObject *, void *, IOExternalMethodArguments *)"
- "!isExceptionLevelDisabled(config, ExceptionLevel::EL2)"
- "\"failed to find the PMGR block offset in EDT. Looked up under 'pmgr' and 'cpmgr'.\" @%s:%d"
- "121111121222121211111112112211211"
- "121111121222121211111112112211211211211"
- "121111121222121211111112112211211211211211211211211211211211211"
- "121111121222121211111112112211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211"
- "1212211112112122222222222221122111212112111"
- "AppleProcessorTrace::resetBufferPA\n"
- "cpmgr"
- "start_va == (void*)VATraceBufferMap->getVirtualAddress()"
- "void AppleProcessorTraceSession::resetBufferPA()"

```
