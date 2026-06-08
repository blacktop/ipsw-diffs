## com.apple.driver.ExclavesAudioKext

> `com.apple.driver.ExclavesAudioKext`

```diff

-340.22.0.0.0
+400.57.1.0.0
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x4e30
-  __TEXT.__os_log: 0x8a5
-  __TEXT_EXEC.__text: 0x12a2c
+  __TEXT.__cstring: 0x52c4
+  __TEXT.__os_log: 0x97e
+  __TEXT_EXEC.__text: 0x16a84
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0x128
-  __DATA_CONST.__auth_got: 0x190
+  __DATA.__common: 0x178
+  __DATA_CONST.__mod_init_func: 0x48
+  __DATA_CONST.__mod_term_func: 0x48
+  __DATA_CONST.__const: 0x1778
+  __DATA_CONST.__kalloc_type: 0x240
+  __DATA_CONST.__auth_got: 0x1b0
   __DATA_CONST.__got: 0x30
-  __DATA_CONST.__mod_init_func: 0x38
-  __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x1488
-  __DATA_CONST.__kalloc_type: 0x1c0
-  UUID: 4278FD9A-C147-37D5-8C3C-EC5BD82B16BB
-  Functions: 608
+  UUID: 39913736-B226-31E4-AC38-E828B98D573A
+  Functions: 702
   Symbols:   0
-  CStrings:  160
+  CStrings:  175
 
CStrings:
+ "\"TB_ASSERT: \" \"(exclavesaudiodrivers_exadstreamdescriptionselector__decode(msg, &inSelector) == TB_ERROR_SUCCESS) && \\\"failed to decode type: ExclavesAudioDrivers.ExADStreamDescriptionSelector\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->enablealtsource != ((void*)0)) && \\\"implementation for enableAltSource is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid error returned from %s\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from enableAltSource\" @%s:%d"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Debug/InputStream/ExclavesAudioProxyDebugInterface.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Debug/InputStream/ExclavesAudioProxyDebugTightbeam.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Debug/OutputStream/ExclavesAudioProxyOutputStreamDebugInterface.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Debug/OutputStream/ExclavesAudioProxyOutputStreamDebugTightbeam.cpp"
+ "ExclavesAudioProxyOutputStreamDebugInterface"
+ "ExclavesAudioProxyOutputStreamDebugTightbeam"
+ "I24@?0{audiodriverdebug_audiooutputstreamdebug_enablealtsource__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8"
+ "I32@?0{audiostreamdriver_audiostreamdriver_getstreamdescription__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q}{exclavesaudiodrivers_exadstreamdescription_s=IIISCC})}8"
+ "I32@?0{exclavesaudiodrivers_audiodriver_getstreamdescription__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q}{exclavesaudiodrivers_exadstreamdescription_s=IIISCC})}8"
+ "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[97c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
+ "enableAltSource"
+ "enableInjection"
+ "getStreamDescription"
+ "mapDMABuffer"
+ "readInput"
+ "ret = enableAltSourceIORet == 0 "
+ "ret = ioReturnFromTBError( audiodriverdebug_audiooutputstreamdebug__init(&client, mTightbeamEndpoint)) == 0 "
+ "ret = ioReturnFromTBError(audiodriverdebug_audiooutputstreamdebug_enablealtsource( &kECDevice, inEnable, ^(audiodriverdebug_audiooutputstreamdebug_enablealtsource__result_s result) { if (!audiodriverdebug_audiooutputstreamdebug_enablealtsource__result_get_success( &result)) { auto failure = audiodriverdebug_audiooutputstreamdebug_enablealtsource__result_get_failure( &result); enableAltSourceIORet = ioReturnFromResult(failure); } })) == 0 "
+ "selectPhysicalStreamDescription"
+ "setupClientIO"
+ "setupIO"
+ "site.ExclavesAudioProxyOutputStreamDebugInterface"
+ "site.ExclavesAudioProxyOutputStreamDebugTightbeam"
+ "sleep"
+ "teardownClientIO"
+ "teardownIO"
+ "v24@?0{audiodriverdebug_audiooutputstreamdebug_enablealtsource__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8"
+ "v32@?0{audiostreamdriver_audiostreamdriver_getstreamdescription__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q}{exclavesaudiodrivers_exadstreamdescription_s=IIISCC})}8"
+ "v32@?0{exclavesaudiodrivers_audiodriver_getstreamdescription__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q}{exclavesaudiodrivers_exadstreamdescription_s=IIISCC})}8"
+ "wake"
+ "writeMixOutput"
- "\"TB_ASSERT: \" \"(exclavesaudiodrivers_streamdescriptionselectortb__decode(msg, &inSelector) == TB_ERROR_SUCCESS) && \\\"failed to decode type: ExclavesAudioDrivers.StreamDescriptionSelectorTB\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
- "\"TB_FATAL: \" \"invalid error returned from enableInjection\" @%s:%d"
- "\"TB_FATAL: \" \"invalid error returned from getStreamDescription\" @%s:%d"
- "\"TB_FATAL: \" \"invalid error returned from mapDMABuffer\" @%s:%d"
- "\"TB_FATAL: \" \"invalid error returned from readInput\" @%s:%d"
- "\"TB_FATAL: \" \"invalid error returned from selectPhysicalStreamDescription\" @%s:%d"
- "\"TB_FATAL: \" \"invalid error returned from setupClientIO\" @%s:%d"
- "\"TB_FATAL: \" \"invalid error returned from setupIO\" @%s:%d"
- "\"TB_FATAL: \" \"invalid error returned from sleep\" @%s:%d"
- "\"TB_FATAL: \" \"invalid error returned from teardownClientIO\" @%s:%d"
- "\"TB_FATAL: \" \"invalid error returned from teardownIO\" @%s:%d"
- "\"TB_FATAL: \" \"invalid error returned from wake\" @%s:%d"
- "\"TB_FATAL: \" \"invalid error returned from writeMixOutput\" @%s:%d"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Debug/ExclavesAudioProxyDebugInterface.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Debug/ExclavesAudioProxyDebugTightbeam.cpp"
- "I40@?0{audiostreamdriver_audiostreamdriver_getstreamdescription__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q}{exclavesaudiodrivers_exadstreamdescription_s=IIIICC})}8"
- "I40@?0{exclavesaudiodrivers_audiodriver_getstreamdescription__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q}{exclavesaudiodrivers_exadstreamdescription_s=IIIICC})}8"
- "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[64c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
- "v40@?0{audiostreamdriver_audiostreamdriver_getstreamdescription__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q}{exclavesaudiodrivers_exadstreamdescription_s=IIIICC})}8"
- "v40@?0{exclavesaudiodrivers_audiodriver_getstreamdescription__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q}{exclavesaudiodrivers_exadstreamdescription_s=IIIICC})}8"

```
