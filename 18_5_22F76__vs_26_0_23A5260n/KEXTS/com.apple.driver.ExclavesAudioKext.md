## com.apple.driver.ExclavesAudioKext

> `com.apple.driver.ExclavesAudioKext`

```diff

-240.34.0.0.0
+300.56.0.0.0
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x2e46
+  __TEXT.__cstring: 0x3024
   __TEXT.__os_log: 0x55a
-  __TEXT_EXEC.__text: 0xa8dc
+  __TEXT_EXEC.__text: 0xd66c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xd8

   __DATA_CONST.__got: 0x30
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
-  __DATA_CONST.__const: 0xb08
+  __DATA_CONST.__const: 0xf08
   __DATA_CONST.__kalloc_type: 0x140
-  UUID: 7E9629D5-0A62-3A2A-A2BD-1006E991B9B6
-  Functions: 321
+  UUID: 5B2C1D8A-E669-3840-816F-857F992967E4
+  Functions: 426
   Symbols:   0
   CStrings:  111
 
CStrings:
+ "\"TB_ASSERT: \" \"(cmp.encoded) && \\\"completion block must be called before returning\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \\\"unexpected tb_error_t returned\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(exclavesaudiodrivers_streamdescriptionselectortb__decode(msg, &inSelector) == TB_ERROR_SUCCESS) && \\\"failed to decode type: ExclavesAudioDrivers.StreamDescriptionSelectorTB\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->enableinjection != ((void*)0)) && \\\"implementation for enableInjection is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->getstreamdescription != ((void*)0)) && \\\"implementation for getStreamDescription is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->mapdmabuffer != ((void*)0)) && \\\"implementation for mapDMABuffer is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->readinput != ((void*)0)) && \\\"implementation for readInput is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->selectphysicalstreamdescription != ((void*)0)) && \\\"implementation for selectPhysicalStreamDescription is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->setupclientio != ((void*)0)) && \\\"implementation for setupClientIO is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->setupio != ((void*)0)) && \\\"implementation for setupIO is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->sleep != ((void*)0)) && \\\"implementation for sleep is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->teardownclientio != ((void*)0)) && \\\"implementation for teardownClientIO is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->teardownio != ((void*)0)) && \\\"implementation for teardownIO is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->wake != ((void*)0)) && \\\"implementation for wake is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "/Library/Caches/com.apple.xbs/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Driver/InputStream/ExclavesAudioProxyInputStreamDriverInterface.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Driver/InputStream/ExclavesAudioProxyInputStreamDriverTightbeam.cpp"
+ "ExclavesAudioProxyInputStreamDriverInterface"
+ "ExclavesAudioProxyInputStreamDriverTightbeam"
+ "site.ExclavesAudioProxyInputStreamDriverInterface"
+ "site.ExclavesAudioProxyInputStreamDriverTightbeam"
- "\"TB_ASSERT: \" \"(cmp.encoded) && \\\"completion block must be called before returning\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \\\"unexpected tb_error_t returned\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(exclavesaudiodrivers_streamdescriptionselectortb__decode(msg, &inSelector) == TB_ERROR_SUCCESS) && \\\"failed to decode type: ExclavesAudioDrivers.StreamDescriptionSelectorTB\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->enableinjection != NULL) && \\\"implementation for enableInjection is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->getstreamdescription != NULL) && \\\"implementation for getStreamDescription is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->mapdmabuffer != NULL) && \\\"implementation for mapDMABuffer is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->readinput != NULL) && \\\"implementation for readInput is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->selectphysicalstreamdescription != NULL) && \\\"implementation for selectPhysicalStreamDescription is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->setupclientio != NULL) && \\\"implementation for setupClientIO is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->setupio != NULL) && \\\"implementation for setupIO is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->sleep != NULL) && \\\"implementation for sleep is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->teardownclientio != NULL) && \\\"implementation for teardownClientIO is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->teardownio != NULL) && \\\"implementation for teardownIO is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->wake != NULL) && \\\"implementation for wake is not present\\\"\" @%s:%d"
- "/Library/Caches/com.apple.xbs/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Driver/ExclavesAudioProxyDriverInterface.cpp"
- "/Library/Caches/com.apple.xbs/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Driver/ExclavesAudioProxyDriverTightbeam.cpp"
- "ExclavesAudioProxyDriverInterface"
- "ExclavesAudioProxyDriverTightbeam"
- "site.ExclavesAudioProxyDriverInterface"
- "site.ExclavesAudioProxyDriverTightbeam"

```
