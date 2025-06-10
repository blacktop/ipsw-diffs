## com.apple.ExclaveKextClient

> `com.apple.ExclaveKextClient`

```diff

-427.120.2.0.0
-  __TEXT.__cstring: 0x64a
+442.0.0.0.0
+  __TEXT.__cstring: 0x6d5
   __TEXT.__const: 0x8
-  __TEXT_EXEC.__text: 0x1120
+  __TEXT_EXEC.__text: 0x1194
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__const: 0xd00
   __DATA_CONST.__kalloc_type: 0x80
   __DATA_CONST.__assert: 0x50
-  UUID: 7F869DA0-6D8A-3C5B-A35B-958F9A885393
+  UUID: C935F09E-6B49-3043-AD8C-37D755246529
   Functions: 66
   Symbols:   0
   CStrings:  28
CStrings:
+ "\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS) && \\\"tb_service_connection_message_configure_reply failed\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->add != ((void*)0)) && \\\"implementation for add is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->doasyncsignal != ((void*)0)) && \\\"implementation for doAsyncSignal is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->doasyncsignalwithkevent != ((void*)0)) && \\\"implementation for doAsyncSignalWithKevent is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->start != ((void*)0)) && \\\"implementation for Start is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
- "\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS) && \\\"tb_service_connection_message_configure_reply failed\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->add != NULL) && \\\"implementation for add is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->doasyncsignal != NULL) && \\\"implementation for doAsyncSignal is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->doasyncsignalwithkevent != NULL) && \\\"implementation for doAsyncSignalWithKevent is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->start != NULL) && \\\"implementation for Start is not present\\\"\" @%s:%d"

```
