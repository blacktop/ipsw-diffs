## com.apple.driver.IOPAudioVoiceTriggerDevice

> `com.apple.driver.IOPAudioVoiceTriggerDevice`

```diff

-440.4.0.0.0
-  __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x2c29
-  __TEXT.__os_log: 0x16f1
-  __TEXT_EXEC.__text: 0xafb0
+500.14.0.0.0
+  __TEXT.__const: 0x98
+  __TEXT.__cstring: 0x2d80
+  __TEXT.__os_log: 0x1726
+  __TEXT_EXEC.__text: 0xb0d0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xf8
   __DATA.__common: 0x88

   __DATA_CONST.__got: 0x60
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x1780
+  __DATA_CONST.__const: 0x1750
   __DATA_CONST.__kalloc_type: 0xc0
-  UUID: 335BB092-15C7-374C-9098-2AE30141B393
-  Functions: 258
+  UUID: A309E52B-DB65-3F86-A279-7F1C13C22C0D
+  Functions: 260
   Symbols:   0
-  CStrings:  232
+  CStrings:  235
 
CStrings:
+ "\"TB_ASSERT: \" \"(aopvoicetriggersecure_voicetriggerlanguagemodeltb__decode(msg, &inLanguageModel) == TB_ERROR_SUCCESS) && \\\"failed to decode type: AOPVoiceTriggerSecure.VoiceTriggerLanguageModelTB\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(cmp.encoded) && \\\"completion block must be called before returning\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \\\"unexpected tb_error_t returned\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS) && \\\"failed to wrap packed buffer\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->configuretriggernotification != ((void*)0)) && \\\"implementation for configureTriggerNotification is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->debuggetsecuredata != ((void*)0)) && \\\"implementation for debugGetSecureData is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->debugsirilanguagemodel != ((void*)0)) && \\\"implementation for debugSiriLanguageModel is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->getnonsecuredata != ((void*)0)) && \\\"implementation for getNonSecureData is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(vErr == TB_ERROR_SUCCESS) && \\\"tb_message_subrange failed\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "20:37:17"
+ "May 30 2025"
+ "expression \"%s\" FAILED, %s(), line %d, status: 0x%x\n"
+ "getNodeInterface()->setNodeProperty(channelMaskDescriptor)"
- "\"TB_ASSERT: \" \"(aopvoicetriggersecure_voicetriggerlanguagemodeltb__decode(msg, &inLanguageModel) == TB_ERROR_SUCCESS) && \\\"failed to decode type: AOPVoiceTriggerSecure.VoiceTriggerLanguageModelTB\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(cmp.encoded) && \\\"completion block must be called before returning\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \\\"unexpected tb_error_t returned\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS) && \\\"failed to wrap packed buffer\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->configuretriggernotification != NULL) && \\\"implementation for configureTriggerNotification is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->debuggetsecuredata != NULL) && \\\"implementation for debugGetSecureData is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->debugsirilanguagemodel != NULL) && \\\"implementation for debugSiriLanguageModel is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->getnonsecuredata != NULL) && \\\"implementation for getNonSecureData is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(vErr == TB_ERROR_SUCCESS) && \\\"tb_message_subrange failed\\\"\" @%s:%d"
- "18:27:20"
- "Apr 27 2025"

```
