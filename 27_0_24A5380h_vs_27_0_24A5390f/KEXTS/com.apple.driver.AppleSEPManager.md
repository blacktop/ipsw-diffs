## com.apple.driver.AppleSEPManager

> `com.apple.driver.AppleSEPManager`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-928.0.0.0.0
-  __TEXT.__cstring: 0x11527
+928.0.2.0.0
+  __TEXT.__cstring: 0x1178f
   __TEXT.__const: 0xded8
-  __TEXT_EXEC.__text: 0x41f24
-  __TEXT_EXEC.__auth_stubs: 0xb00
+  __TEXT_EXEC.__text: 0x42e78
+  __TEXT_EXEC.__auth_stubs: 0xb20
   __DATA.__data: 0x168
   __DATA.__common: 0xc48
   __DATA.__bss: 0x4e

   __DATA_CONST.__const: 0x9fc0
   __DATA_CONST.__kalloc_type: 0xe00
   __DATA_CONST.__kalloc_var: 0x50
-  __DATA_CONST.__auth_got: 0x580
+  __DATA_CONST.__auth_got: 0x590
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x38
-  Functions: 2519
+  Functions: 2544
   Symbols:   0
-  CStrings:  1473
+  CStrings:  1493
 
CStrings:
+ "%s: SEP CoreAnalytics: Failed to send CA event %d\n"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleSEPManager/AppleSEPCommon.h"
+ "AppleSEPCommon.h"
+ "KdbgScope::~KdbgScope()"
+ "analytics.version == 1"
+ "begin_code & TRACE_FUNCTION_BEGIN"
+ "code_begin & TRACE_FUNCTION_BEGIN"
+ "code_end & TRACE_FUNCTION_END"
+ "com.apple.applesepos.storage.stats"
+ "dictData[0]"
+ "dictKey[0]"
+ "eventName"
+ "eventPayload"
+ "in_msg_p->length == sizeof(xart_analytics_t)"
+ "pwn"
+ "top_ < kMaxDepth"
+ "top_ > 0"
+ "void AppleSEPManager::_report_sandcat_pwn(uint32_t)"
+ "void KdbgScope::pop(uint32_t)"
+ "void KdbgScope::push(uint32_t)"
```
