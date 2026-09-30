## com.apple.EXBrightKext

> `com.apple.EXBrightKext`

```diff

-1902.120.21.0.1
-  __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x2118
-  __TEXT_EXEC.__text: 0xd5b0
+2079.0.9.502.1
+  __TEXT.__const: 0xf8
+  __TEXT.__cstring: 0x3037
+  __TEXT_EXEC.__text: 0xfeb4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
-  __DATA.__common: 0x68
+  __DATA.__common: 0x90
   __DATA.__bss: 0x2
-  __DATA_CONST.__auth_got: 0x290
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__mod_init_func: 0x10
-  __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x17e8
-  __DATA_CONST.__kalloc_type: 0x80
-  UUID: 4E227307-E2B7-3EF6-ACCE-2A808658A388
-  Functions: 333
+  __DATA_CONST.__auth_got: 0x2b0
+  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__mod_init_func: 0x18
+  __DATA_CONST.__mod_term_func: 0x18
+  __DATA_CONST.__const: 0x18f0
+  __DATA_CONST.__kalloc_type: 0xc0
+  UUID: 43F1DCC1-BC0A-306F-A0DD-52E15815EA08
+  Functions: 389
   Symbols:   0
-  CStrings:  141
+  CStrings:  185
 
CStrings:
+ "\"TB_ASSERT: \" \"(cmp.encoded) && \\\"completion block must be called before returning\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \\\"unexpected tb_error_t returned\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS) && \\\"failed to wrap packed buffer\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->calibrateambientlightsensors != ((void*)0)) && \\\"implementation for calibrateAmbientLightSensors is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->calibratextalk != ((void*)0)) && \\\"implementation for calibrateXTalk is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->calibratextalkfromblob != ((void*)0)) && \\\"implementation for calibrateXTalkFromBlob is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->configureupcallnotification != ((void*)0)) && \\\"implementation for configureUpcallNotification is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->getlastxtalkestimates != ((void*)0)) && \\\"implementation for getLastXTalkEstimates is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->getpilbrightness != ((void*)0)) && \\\"implementation for getPILBrightness is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->getpilenablementstate != ((void*)0)) && \\\"implementation for getPILEnablementState is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->getsildebug != ((void*)0)) && \\\"implementation for getSILDebug is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->getsoftboundarystate != ((void*)0)) && \\\"implementation for getSoftBoundaryState is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->overridepanelbrightness != ((void*)0)) && \\\"implementation for overridePanelBrightness is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->overridesensortemperature != ((void*)0)) && \\\"implementation for overrideSensorTemperature is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->overridesoftboundaryhint != ((void*)0)) && \\\"implementation for overrideSoftBoundaryHint is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->processalssamplesandfetchmib != ((void*)0)) && \\\"implementation for processALSSamplesAndFetchMIB is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->setarbitraryalscalibration != ((void*)0)) && \\\"implementation for setArbitraryALSCalibration is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->setindicatorstate != ((void*)0)) && \\\"implementation for setIndicatorState is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->setuibrightness != ((void*)0)) && \\\"implementation for setUIBrightness is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->start != ((void*)0)) && \\\"implementation for Start is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(u8__v_decode(msg, &calibration) == TB_ERROR_SUCCESS) && \\\"failed to decode type: UInt8\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(vErr == TB_ERROR_SUCCESS) && \\\"tb_message_subrange failed\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "12111112122212121111111211111112112212111111112"
+ "121112121212122"
+ "EXBrightALSCalibrationInterest"
+ "EXBrightCalibrationLoader"
+ "EXBrightUserspaceForwardedFDRBundles"
+ "I24@?0{exbrightkextinterfacedebug_exbrightalsarbitrarycalibrationresponse__opt_s=B{exbrightkextinterfacedebug_exbrightalsarbitrarycalibrationresponse_s=CII}}8"
+ "I52@?0{exbrightkextinterface_exbrightalscalibrationresults__opt_s=B{exbrightkextinterface_exbrightalscalibrationresults_s=[3{exbrightkextinterface_exbrightalscalibrationresult_s=IIB}]C}}8"
+ "I56@?0{exbrightkextinterfacedebug_softboundarydebugstate__opt_s=B{exbrightkextinterfacedebug_softboundarydebugstate_s=BBffff{exbrightkextinterfacedebug_exbrightrgbfactorstb_s=fff}{exbrightkextinterfacedebug_exbrightrgbfactorstb_s=fff}}}8"
+ "[%s] A new ALS calibration path will be used on this product!\n"
+ "[%s] EXBright calibration: alsPlacement=%u alsOrientation=%u success=%d\n"
+ "[%s] [%s] calibrationSize = %lu calibrationResponseSize = %u\n"
+ "[%s] [CL] Calibration process will start in %ums (_alsCalibrationCnt=%d)\n"
+ "[%s] [CL] Registered a new ALS calibration client with placement=%u and orientation=%u (_alsCalibrationClientsCnt=%d).\n"
+ "[%s] [CL] Sending calibration info to ALS client (i=%u, alsPlacement=%u, alsOrientation=%u, calibrated=%u)\n"
+ "[%s] [CL] Starting calibration process! (_alsCalibrationClientsCnt=%u, _expectedALSCalibrationClientsCnt=%u)\n"
+ "[%s] [CL] [%s] The calibration process has already finished!\n"
+ "[%s] [CL] [%s] Wating for ALS companion drivers (_alsCalibrationClientsCnt=%d)\n"
+ "[%s] [CL] [ERR] Bad input!\n"
+ "[%s] [CL] [ERR] Calibration failed (err=%u)\n"
+ "[%s] [CL] [ERR] Calibration process failed: EXBright returned nil!\n"
+ "[%s] [CL] [ERR] Could not add timer for calibration to the workloop, res: %d\n"
+ "[%s] [CL] [ERR] Could not create a timer for calibration.\n"
+ "[%s] [CL] [ERR] Init failed!\n"
+ "[%s] [CL] [ERR] No ALS is configured in EDT.\n"
+ "[%s] [CL] [ERR] No calibration result for ALS with placement=%u and orientation=%u (i=%u)\n"
+ "[%s] [CL] [ERR] This is *bad*! A client with placement=%u and orientation=%u already exists!\n"
+ "[%s] [CL] [ERR] This is *bad*! Cannot register another client. There are more clients than expected (_alsCalibrationClientsCnt=%d, _expectedALSCalibrationClientsCnt=%d).\n"
+ "[%s] [CL] [ERR] [%s] Calibration process has already started!\n"
+ "[%s] [CL] [ERR] [%s] Late! Calibration process has already started!\n"
+ "[%s] [CL] [ERR] [%s] Not configured!\n"
+ "[%s] [CL] _expectedALSCalibrationClientsCnt = %u _waitTillUserspaceForwardsFDRBundles=%d\n"
+ "[%s] [ERR] Calibration process failed: EXBright returned nil!\n"
+ "[%s] [ERR] Received '%s' but calibration loader is missing.\n"
+ "[%s] [ERR] Received calibration interest but calibration loader is missing.\n"
+ "[%s] [ERR] [%s] Incorrect buffer size (got=%d needed=%lu).\n"
+ "[%s] [ERR] [%s] Received nullptr!\n"
+ "als-new-calibration-path"
+ "als-types"
+ "alsCalibrationTimerCallback"
+ "calibration-source"
+ "registerALSCalibrationClient"
+ "registerALSCalibrationClient_block_invoke"
+ "setArbitraryALSCalibration"
+ "setArbitraryALSCalibration_block_invoke_2"
+ "site.EXBrightCalibrationLoader"
+ "userspaceForwardedFDRBundles"
+ "userspaceForwardedFDRBundles_block_invoke"
+ "v24@?0{exbrightkextinterfacedebug_exbrightalsarbitrarycalibrationresponse__opt_s=B{exbrightkextinterfacedebug_exbrightalsarbitrarycalibrationresponse_s=CII}}8"
+ "v52@?0{exbrightkextinterface_exbrightalscalibrationresults__opt_s=B{exbrightkextinterface_exbrightalscalibrationresults_s=[3{exbrightkextinterface_exbrightalscalibrationresult_s=IIB}]C}}8"
+ "v56@?0{exbrightkextinterfacedebug_softboundarydebugstate__opt_s=B{exbrightkextinterfacedebug_softboundarydebugstate_s=BBffff{exbrightkextinterfacedebug_exbrightrgbfactorstb_s=fff}{exbrightkextinterfacedebug_exbrightrgbfactorstb_s=fff}}}8"
- "\"TB_ASSERT: \" \"(cmp.encoded) && \\\"completion block must be called before returning\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \\\"unexpected tb_error_t returned\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS) && \\\"failed to wrap packed buffer\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->calibrateambientlightsensor != NULL) && \\\"implementation for calibrateAmbientLightSensor is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->calibrateambientlightsensors != NULL) && \\\"implementation for calibrateAmbientLightSensors is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->calibratextalk != NULL) && \\\"implementation for calibrateXTalk is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->calibratextalkfromblob != NULL) && \\\"implementation for calibrateXTalkFromBlob is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->configureupcallnotification != NULL) && \\\"implementation for configureUpcallNotification is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->getlastxtalkestimates != NULL) && \\\"implementation for getLastXTalkEstimates is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->getpilbrightness != NULL) && \\\"implementation for getPILBrightness is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->getpilenablementstate != NULL) && \\\"implementation for getPILEnablementState is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->getsildebug != NULL) && \\\"implementation for getSILDebug is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->getsoftboundarystate != NULL) && \\\"implementation for getSoftBoundaryState is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->overridepanelbrightness != NULL) && \\\"implementation for overridePanelBrightness is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->overridesensortemperature != NULL) && \\\"implementation for overrideSensorTemperature is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->overridesoftboundaryhint != NULL) && \\\"implementation for overrideSoftBoundaryHint is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->processalssamplesandfetchmib != NULL) && \\\"implementation for processALSSamplesAndFetchMIB is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->setindicatorstate != NULL) && \\\"implementation for setIndicatorState is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->setuibrightness != NULL) && \\\"implementation for setUIBrightness is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->start != NULL) && \\\"implementation for Start is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(u8__v_decode(msg, &calibration) == TB_ERROR_SUCCESS) && \\\"failed to decode type: UInt8\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(vErr == TB_ERROR_SUCCESS) && \\\"tb_message_subrange failed\\\"\" @%s:%d"
- "121111121222121211111112111111121122121111111"
- "I36@?0{exbrightkextinterfacedebug_softboundarydebugstate__opt_s=B{exbrightkextinterfacedebug_softboundarydebugstate_s=BBfffff}}8"
- "[%s] EXBright ALS-%d calibrated: %d\n"
- "[%s] EXBright calibrated: %d\n"
- "[%s] calibrate ALS%d, size = %lu\n"
- "v36@?0{exbrightkextinterfacedebug_softboundarydebugstate__opt_s=B{exbrightkextinterfacedebug_softboundarydebugstate_s=BBfffff}}8"

```
