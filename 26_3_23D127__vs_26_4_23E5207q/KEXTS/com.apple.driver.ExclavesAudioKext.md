## com.apple.driver.ExclavesAudioKext

> `com.apple.driver.ExclavesAudioKext`

```diff

-300.59.0.0.0
-  __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x3024
-  __TEXT.__os_log: 0x55a
-  __TEXT_EXEC.__text: 0xd820
+340.22.0.0.0
+  __TEXT.__const: 0x58
+  __TEXT.__cstring: 0x4e30
+  __TEXT.__os_log: 0x8a5
+  __TEXT_EXEC.__text: 0x12a2c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0xd8
+  __DATA.__common: 0x128
   __DATA_CONST.__auth_got: 0x190
   __DATA_CONST.__got: 0x30
-  __DATA_CONST.__mod_init_func: 0x28
-  __DATA_CONST.__mod_term_func: 0x28
-  __DATA_CONST.__const: 0xf08
-  __DATA_CONST.__kalloc_type: 0x140
-  UUID: BF2CCDC7-B2A6-3981-8722-B89EB5ABE151
-  Functions: 426
+  __DATA_CONST.__mod_init_func: 0x38
+  __DATA_CONST.__mod_term_func: 0x38
+  __DATA_CONST.__const: 0x1488
+  __DATA_CONST.__kalloc_type: 0x1c0
+  UUID: 1B7ECD6E-A313-30EC-B594-942B8E5201EC
+  Functions: 608
   Symbols:   0
-  CStrings:  111
+  CStrings:  160
 
CStrings:
+ "\"TB_ASSERT: \" \"(server->writemixoutput != ((void*)0)) && \\\"implementation for writeMixOutput is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid error returned from writeMixOutput\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from enableInjection\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from getStreamDescription\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from mapDMABuffer\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from readInput\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from selectPhysicalStreamDescription\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from setupClientIO\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from setupIO\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from sleep\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from teardownClientIO\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from teardownIO\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from wake\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from writeMixOutput\" @%s:%d"
+ "/Library/Caches/com.apple.xbs/7DB8A0E5-4B39-41CE-9BAF-0F259C351B57/TemporaryDirectory.waZaIV/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Debug/ExclavesAudioProxyDebugInterface.cpp"
+ "/Library/Caches/com.apple.xbs/7DB8A0E5-4B39-41CE-9BAF-0F259C351B57/TemporaryDirectory.waZaIV/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Debug/ExclavesAudioProxyDebugTightbeam.cpp"
+ "/Library/Caches/com.apple.xbs/7DB8A0E5-4B39-41CE-9BAF-0F259C351B57/TemporaryDirectory.waZaIV/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Driver/InputStream/ExclavesAudioProxyInputStreamDriverInterface.cpp"
+ "/Library/Caches/com.apple.xbs/7DB8A0E5-4B39-41CE-9BAF-0F259C351B57/TemporaryDirectory.waZaIV/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Driver/InputStream/ExclavesAudioProxyInputStreamDriverTightbeam.cpp"
+ "/Library/Caches/com.apple.xbs/7DB8A0E5-4B39-41CE-9BAF-0F259C351B57/TemporaryDirectory.waZaIV/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Driver/OutputStream/ExclavesAudioProxyOutputStreamDriverInterface.cpp"
+ "/Library/Caches/com.apple.xbs/7DB8A0E5-4B39-41CE-9BAF-0F259C351B57/TemporaryDirectory.waZaIV/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Driver/OutputStream/ExclavesAudioProxyOutputStreamDriverTightbeam.cpp"
+ "/Library/Caches/com.apple.xbs/7DB8A0E5-4B39-41CE-9BAF-0F259C351B57/TemporaryDirectory.waZaIV/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Endpoint/ExclavesAudioProxyEndpoint.cpp"
+ "ExclavesAudioProxyOutputStreamDriverInterface"
+ "ExclavesAudioProxyOutputStreamDriverTightbeam"
+ "I24@?0{audiostreamdriver_audioinputstreamdriver_readinput__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8"
+ "I24@?0{audiostreamdriver_audioinputstreamdriver_setupclientio__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8"
+ "I24@?0{audiostreamdriver_audioinputstreamdriver_teardownclientio__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8"
+ "I24@?0{audiostreamdriver_audiooutputstreamdriver_writemixoutput__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8"
+ "I24@?0{audiostreamdriver_audiostreamdriver_mapdmabuffer__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8"
+ "I24@?0{audiostreamdriver_audiostreamdriver_selectphysicalstreamdescription__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8"
+ "I24@?0{audiostreamdriver_audiostreamdriver_setupio__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8"
+ "I24@?0{audiostreamdriver_audiostreamdriver_sleep__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8"
+ "I24@?0{audiostreamdriver_audiostreamdriver_teardownio__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8"
+ "I24@?0{audiostreamdriver_audiostreamdriver_wake__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8"
+ "I40@?0{audiostreamdriver_audiostreamdriver_getstreamdescription__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q}{exclavesaudiodrivers_exadstreamdescription_s=IIIICC})}8"
+ "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[64c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
+ "ret = ioReturnFromTBError( audiostreamdriver_audiostreamdriver__init(&client, mTightbeamEndpoint)) == 0 "
+ "ret = ioReturnFromTBError(audiostreamdriver_audiooutputstreamdriver_writemixoutput( &kECDevice, inSampleTime, inFrames, ^(audiostreamdriver_audiooutputstreamdriver_writemixoutput__result_s result) { if (!audiostreamdriver_audiooutputstreamdriver_writemixoutput__result_get_success( &result)) { auto failure = audiostreamdriver_audiooutputstreamdriver_writemixoutput__result_get_failure( &result); readOutputRet = ioReturnFromResult(failure); } })) == 0 "
+ "ret = ioReturnFromTBError(audiostreamdriver_audiostreamdriver_getstreamdescription( &kECDevice, ^(audiostreamdriver_audiostreamdriver_getstreamdescription__result_s result) { auto success = audiostreamdriver_audiostreamdriver_getstreamdescription__result_get_success( &result); if (success != nullptr) { ecStreamDescription = *success; } else { auto failure = audiostreamdriver_audiostreamdriver_getstreamdescription__result_get_failure( &result); getStreamDescriptionRet = ioReturnFromResult(failure); } })) == 0 "
+ "ret = ioReturnFromTBError(audiostreamdriver_audiostreamdriver_mapdmabuffer( &kECDevice, ^(audiostreamdriver_audiostreamdriver_mapdmabuffer__result_s result) { if (!audiostreamdriver_audiostreamdriver_mapdmabuffer__result_get_success(&result)) { auto failure = audiostreamdriver_audiostreamdriver_mapdmabuffer__result_get_failure(&result); setupIORet = ioReturnFromResult(failure); } })) == 0 "
+ "ret = ioReturnFromTBError(audiostreamdriver_audiostreamdriver_selectphysicalstreamdescription( &kECDevice, &selector, ^(audiostreamdriver_audiostreamdriver_selectphysicalstreamdescription__result_s result) { if (!audiostreamdriver_audiostreamdriver_selectphysicalstreamdescription__result_get_success( &result)) { auto failure = audiostreamdriver_audiostreamdriver_selectphysicalstreamdescription__result_get_failure( &result); selectPhysicalStreamDescriptionRet = ioReturnFromResult(failure); } })) == 0 "
+ "ret = ioReturnFromTBError(audiostreamdriver_audiostreamdriver_setupio( &kECDevice, ^(audiostreamdriver_audiostreamdriver_setupio__result_s result) { if (!audiostreamdriver_audiostreamdriver_setupio__result_get_success(&result)) { auto failure = audiostreamdriver_audiostreamdriver_setupio__result_get_failure(&result); setupIORet = ioReturnFromResult(failure); } })) == 0 "
+ "ret = ioReturnFromTBError(audiostreamdriver_audiostreamdriver_sleep( &kECDevice, ^(audiostreamdriver_audiostreamdriver_sleep__result_s result) { if (!audiostreamdriver_audiostreamdriver_sleep__result_get_success(&result)) { auto failure = audiostreamdriver_audiostreamdriver_sleep__result_get_failure(&result); sleepRet = ioReturnFromResult(failure); } })) == 0 "
+ "ret = ioReturnFromTBError(audiostreamdriver_audiostreamdriver_teardownio( &kECDevice, ^(audiostreamdriver_audiostreamdriver_teardownio__result_s result) { if (!audiostreamdriver_audiostreamdriver_teardownio__result_get_success(&result)) { auto failure = audiostreamdriver_audiostreamdriver_teardownio__result_get_failure(&result); teardownIORet = ioReturnFromResult(failure); } })) == 0 "
+ "ret = ioReturnFromTBError(audiostreamdriver_audiostreamdriver_wake( &kECDevice, ^(audiostreamdriver_audiostreamdriver_wake__result_s result) { if (!audiostreamdriver_audiostreamdriver_wake__result_get_success(&result)) { auto failure = audiostreamdriver_audiostreamdriver_wake__result_get_failure(&result); wakeRet = ioReturnFromResult(failure); } })) == 0 "
+ "ret = readOutputRet == 0 "
+ "site.ExclavesAudioProxyOutputStreamDriverInterface"
+ "site.ExclavesAudioProxyOutputStreamDriverTightbeam"
+ "v24@?0{audiostreamdriver_audiooutputstreamdriver_writemixoutput__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8"
+ "v24@?0{audiostreamdriver_audiostreamdriver_mapdmabuffer__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8"
+ "v24@?0{audiostreamdriver_audiostreamdriver_selectphysicalstreamdescription__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8"
+ "v24@?0{audiostreamdriver_audiostreamdriver_setupio__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8"
+ "v24@?0{audiostreamdriver_audiostreamdriver_sleep__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8"
+ "v24@?0{audiostreamdriver_audiostreamdriver_teardownio__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8"
+ "v24@?0{audiostreamdriver_audiostreamdriver_wake__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8"
+ "v40@?0{audiostreamdriver_audiostreamdriver_getstreamdescription__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q}{exclavesaudiodrivers_exadstreamdescription_s=IIIICC})}8"
- "/Library/Caches/com.apple.xbs/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Debug/ExclavesAudioProxyDebugInterface.cpp"
- "/Library/Caches/com.apple.xbs/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Debug/ExclavesAudioProxyDebugTightbeam.cpp"
- "/Library/Caches/com.apple.xbs/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Driver/InputStream/ExclavesAudioProxyInputStreamDriverInterface.cpp"
- "/Library/Caches/com.apple.xbs/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Driver/InputStream/ExclavesAudioProxyInputStreamDriverTightbeam.cpp"
- "/Library/Caches/com.apple.xbs/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Endpoint/ExclavesAudioProxyEndpoint.cpp"
- "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[41c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"

```
