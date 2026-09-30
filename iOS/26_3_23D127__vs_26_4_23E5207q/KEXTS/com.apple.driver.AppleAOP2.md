## com.apple.driver.AppleAOP2

> `com.apple.driver.AppleAOP2`

```diff

-126.60.2.0.0
-  __TEXT.__cstring: 0x45
-  __TEXT_EXEC.__text: 0x694
+126.100.25.0.0
+  __TEXT.__cstring: 0xc08
+  __TEXT.__const: 0x8
+  __TEXT.__os_log: 0x1fc
+  __TEXT_EXEC.__text: 0x3550
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x188
-  __DATA.__common: 0x38
-  __DATA_CONST.__auth_got: 0x48
-  __DATA_CONST.__got: 0x18
-  __DATA_CONST.__mod_init_func: 0x8
-  __DATA_CONST.__mod_term_func: 0x8
-  __DATA_CONST.__const: 0x5f0
-  __DATA_CONST.__kalloc_type: 0x40
-  UUID: 0A3BA048-64CD-3BA4-AA88-DBAA13FF292C
-  Functions: 26
+  __DATA.__data: 0x248
+  __DATA.__common: 0x88
+  __DATA.__bss: 0x28
+  __DATA_CONST.__auth_got: 0x1d8
+  __DATA_CONST.__got: 0x48
+  __DATA_CONST.__mod_init_func: 0x18
+  __DATA_CONST.__mod_term_func: 0x18
+  __DATA_CONST.__const: 0x1308
+  __DATA_CONST.__kalloc_type: 0x140
+  UUID: FB2CC1CD-E7B4-3BDB-B8F5-C1EB9839D16D
+  Functions: 147
   Symbols:   0
-  CStrings:  3
+  CStrings:  54
 
CStrings:
+ "\"%s: command queueing is not supported\" @%s:%d"
+ "\"%s: ctx cannot be NULL\" @%s:%d"
+ "\"%s: ctx->cmdBuffer cannot be NULL\" @%s:%d"
+ "\"%s: wake transition failed\" @%s:%d"
+ "\"TB_ASSERT: \" \"(aop2kext_iopmassertionoptions__decode(msg, &options) == TB_ERROR_SUCCESS) && \\\"failed to decode type: AOP2Kext.IOPMAssertionOptions\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS) && \\\"tb_service_connection_message_configure_reply failed\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->assertlevel != ((void*)0)) && \\\"implementation for assertLevel is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->createiopmassertion != ((void*)0)) && \\\"implementation for createIOPMAssertion is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->deassertlevel != ((void*)0)) && \\\"implementation for deassertLevel is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->releaseiopmassertion != ((void*)0)) && \\\"implementation for releaseIOPMAssertion is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid error returned from assertLevel\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid error returned from createIOPMAssertion\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid error returned from deassertLevel\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid error returned from releaseIOPMAssertion\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from assertLevel\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from createIOPMAssertion\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from deassertLevel\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from releaseIOPMAssertion\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid value: unexpected bits, 0x%llx\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid value: unexpected case value, %llx\" @%s:%d"
+ "\"TB_FATAL: \" \"unrecognized selector: %llu\" @%s:%d"
+ "\"Thread call cannot be NULL\" @%s:%d"
+ "%s: AssertMacros: %s, %s file: %s, line: %d value:%x\n"
+ "/Library/Caches/com.apple.xbs/8130F003-40D2-42C3-BEA0-B17BEDB865B4/TemporaryDirectory.GhX8Hk/Sources/AppleAOP2/AppleAOP2Kext/src/Services/IOPMService/AppleAOP2IOPMService.cpp"
+ "112"
+ "12111112122212121111111111"
+ "12111112122212121111112"
+ "AOP2Kext_c.c"
+ "AppleAOP2IOPMService"
+ "AppleAOP2IOPMService.cpp"
+ "AppleAOP2KextTightbeamEndpoint"
+ "AppleAOP2KextTightbeamEndpoint.cpp"
+ "CFBundleIdentifier"
+ "I24@?0r^{aop2kext_iopmassertion=Q}8^(aop2kext_iopm_assertlevel__result={aop2kext_iopmerror=Q})16"
+ "I24@?0r^{aop2kext_iopmassertion=Q}8^(aop2kext_iopm_deassertlevel__result={aop2kext_iopmerror=Q})16"
+ "I24@?0r^{aop2kext_iopmassertion=Q}8^(aop2kext_iopm_releaseiopmassertion__result={aop2kext_iopmerror=Q})16"
+ "I24@?0r^{aop2kext_iopmassertionoptions=[64C]Q{aop2kext_iopmassertionlevel=Q}}8^(aop2kext_iopm_createiopmassertion__result={aop2kext_iopmerror=Q}{aop2kext_iopmassertion=Q})16"
+ "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[64c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
+ "_commandGate"
+ "_provider"
+ "_tb_ep_rev"
+ "_workloop"
+ "aop2kext_iopm__server_start_owned failed: 0x%x"
+ "com.apple.driver.AppleAOP2IOPMService"
+ "power state change failed %d"
+ "site.AppleAOP2IOPMService"
+ "site.AppleAOP2KextTightbeamEndpoint"
+ "site.commandHandlerCtx"
+ "status == 0 "
+ "success"
+ "v32@?0^v8*16Q24"

```
