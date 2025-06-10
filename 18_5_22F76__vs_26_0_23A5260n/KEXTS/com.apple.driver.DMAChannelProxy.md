## com.apple.driver.DMAChannelProxy

> `com.apple.driver.DMAChannelProxy`

```diff

-450.4.0.0.0
+500.80.0.0.0
   __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x555
-  __TEXT_EXEC.__text: 0x2888
+  __TEXT.__cstring: 0x5bd
+  __TEXT_EXEC.__text: 0x28e8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0xcd0
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: BC358CB0-4645-3ACD-925C-948E41FF460B
-  Functions: 116
+  UUID: 0C69EA7D-6508-3357-AFE7-AF5F1D094F2A
+  Functions: 115
   Symbols:   0
   CStrings:  28
 
CStrings:
+ "\"TB_ASSERT: \" \"(cmp.encoded) && \\\"completion block must be called before returning\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \\\"unexpected tb_error_t returned\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->enqueuedescriptor != ((void*)0)) && \\\"implementation for enqueueDescriptor is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->stoptransfer != ((void*)0)) && \\\"implementation for stopTransfer is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
- "\"TB_ASSERT: \" \"(cmp.encoded) && \\\"completion block must be called before returning\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \\\"unexpected tb_error_t returned\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->enqueuedescriptor != NULL) && \\\"implementation for enqueueDescriptor is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->stoptransfer != NULL) && \\\"implementation for stopTransfer is not present\\\"\" @%s:%d"

```
