## com.apple.driver.AudioSharedDARTMapperProxy

> `com.apple.driver.AudioSharedDARTMapperProxy`

```diff

-240.34.0.0.0
+300.56.0.0.0
   __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x7d1
+  __TEXT.__cstring: 0x856
   __TEXT.__os_log: 0xf8
-  __TEXT_EXEC.__text: 0x3954
+  __TEXT_EXEC.__text: 0x3974
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x38

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x730
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: EF0EDEAA-889E-3C18-90E0-22D4572BFC1F
+  UUID: 63887D90-DD49-3BDB-8002-03B913D0EDE4
   Functions: 118
   Symbols:   0
   CStrings:  29
CStrings:
+ "\"TB_ASSERT: \" \"(cmp.encoded) && \\\"completion block must be called before returning\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \\\"unexpected tb_error_t returned\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->resume != ((void*)0)) && \\\"implementation for resume is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->setupusecase != ((void*)0)) && \\\"implementation for setupUseCase is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->suspend != ((void*)0)) && \\\"implementation for suspend is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
- "\"TB_ASSERT: \" \"(cmp.encoded) && \\\"completion block must be called before returning\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \\\"unexpected tb_error_t returned\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->resume != NULL) && \\\"implementation for resume is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->setupusecase != NULL) && \\\"implementation for setupUseCase is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->suspend != NULL) && \\\"implementation for suspend is not present\\\"\" @%s:%d"

```
