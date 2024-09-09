## corerepaird

> `/usr/libexec/corerepaird`

```diff

 625.2.2.0.0
-  __TEXT.__text: 0x314d0
-  __TEXT.__auth_stubs: 0xf60
-  __TEXT.__objc_stubs: 0x2a00
-  __TEXT.__objc_methlist: 0x2a00
-  __TEXT.__oslogstring: 0xf6e
-  __TEXT.__cstring: 0x5313
+  __TEXT.__text: 0x39298
+  __TEXT.__auth_stubs: 0xf80
+  __TEXT.__objc_stubs: 0x3500
+  __TEXT.__objc_methlist: 0x3120
+  __TEXT.__cstring: 0x5c3e
+  __TEXT.__oslogstring: 0x145a
   __TEXT.__const: 0x3940
-  __TEXT.__objc_methname: 0x321f
-  __TEXT.__objc_classname: 0xb84
-  __TEXT.__objc_methtype: 0xab8
-  __TEXT.__gcc_except_tab: 0x208
-  __TEXT.__unwind_info: 0xd20
-  __DATA_CONST.__auth_got: 0x7c0
-  __DATA_CONST.__got: 0x378
+  __TEXT.__objc_methname: 0x3edd
+  __TEXT.__objc_classname: 0xcd0
+  __TEXT.__objc_methtype: 0xcc2
+  __TEXT.__gcc_except_tab: 0x260
+  __TEXT.__unwind_info: 0xe40
+  __DATA_CONST.__auth_got: 0x7d0
+  __DATA_CONST.__got: 0x3d0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0xe30
-  __DATA_CONST.__cfstring: 0x56c0
-  __DATA_CONST.__objc_classlist: 0x248
+  __DATA_CONST.__const: 0xea8
+  __DATA_CONST.__cfstring: 0x6260
+  __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x58
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_classrefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x210
-  __DATA_CONST.__objc_intobj: 0xa8
-  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_superrefs: 0x2b8
+  __DATA_CONST.__objc_arraydata: 0x88
+  __DATA_CONST.__objc_arrayobj: 0x60
+  __DATA_CONST.__objc_intobj: 0x330
+  __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x58d0
-  __DATA.__objc_selrefs: 0xdd8
-  __DATA.__objc_ivar: 0x330
-  __DATA.__objc_data: 0x16d0
-  __DATA.__data: 0xa20
+  __DATA.__objc_const: 0x6b68
+  __DATA.__objc_selrefs: 0x10f0
+  __DATA.__objc_ivar: 0x390
+  __DATA.__objc_data: 0x1d60
+  __DATA.__data: 0xae8
   __DATA.__bss: 0xa8
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libz.1.dylib
   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
-  Functions: 1091
-  Symbols:   330
-  CStrings:  2065
+  Functions: 1255
+  Symbols:   345
+  CStrings:  2409
 
Symbols:
+ _OBJC_CLASS_$_CRUserDefaults
+ _OBJC_CLASS_$_ASTSuiteResult
+ _OBJC_CLASS_$_CRBootIntentHelper
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_ASTInstructionalPrompt
+ _os_variant_has_internal_content
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$_ASTRepairSessionProvider
+ _OBJC_CLASS_$_ASTSuite
+ _OBJC_CLASS_$_ASTTestResult
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_CRLocalization
+ _OBJC_CLASS_$_CRRepairHistory
+ _kBrunorTagResponseTicket
+ __dispatch_queue_attr_concurrent
CStrings:
+ "supportLiDAR"
+ "T@\"NSString\",&,N,V_serialNumber"
+ "IPHONE COMP FACEID"
+ "https://ig.apple.com"
+ "preflightPartSPC"
+ "updateProperties"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
+ "started"
+ "PeCoNet not supported"
+ "Cancelling test"
+ "CRTest_8340"
+ "@\"ASTSuiteResult\""
+ "CRTest_8268"
+ "isEqualToNumber:"
+ "T@\"NSMutableArray\",&,N,V_patchItems"
+ "\x16\x11"
+ "LiDARCalibrationIllustration_Setup.svg"
+ "clearBootIntent:"
+ "testSequencerQueue"
+ "-[CRRepairSession requestAsset:withCompletion:]"
+ "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_runningSemaphore"
+ "lastRunTestId"
+ "verifyPSD3"
+ "patchItem"
+ "Test result is not for the running test"
+ "initWithId:suiteNameLocalizedString:suiteDescriptionLocalizedString:estimatedCompletionTimeLocalizedString:primaryAssetLocator:secondaryAssetLocator:"
+ "skipStageEAN"
+ "_rik"
+ "7004"
+ "@\"ASTRepairSessionProvider\""
+ "CAMERA_CALIBRATION_INSTRUCTIONS_4"
+ "arrayWithObject:"
+ "sceneErrorTimeOut"
+ "showInstructionalPrompt:withConfirmation:"
+ "com.apple.corerepair.testSequencer"
+ "8276"
+ "-[CRRepairSession requestTermsAndConditionsWithCompletion:]"
+ "CAMERA_CALIBRATION_INSTRUCTIONS_3"
+ "decodeObjectOfClasses:forKey:"
+ "Verify PSD3 failed"
+ "_name"
+ "IPHONE COMP CAMERA"
+ "com.apple.corerepair.diagnostics-controller"
+ "IPHONE COMP RCAM"
+ "8262"
+ "https://humb.apple.com"
+ "setTestSequence:"
+ "testContext"
+ "T@\"NSString\",&,N,V_PrCL"
+ "MPU"
+ "CRTest_7004"
+ "_statusCode"
+ "@\"NSObject<OS_dispatch_semaphore>\""
+ "No running test found"
+ "componentsJoinedByString:"
+ "CAMERA_CALIBRATION_CONTINUE_BUTTON_TITLE"
+ "requestAsset:withCompletion:"
+ "patchItems"
+ "startTest:parameters:"
+ "updateBrunorDATFirmware"
+ "SavageUpdaterExecCommand failed: %!@(MISSING)"
+ "setStarted:"
+ "perform next stage: %!@(MISSING)"
+ "T@\"NSNumber\",&,N,V_suiteId"
+ "powerCycleSensor failed with error: %!@(MISSING)"
+ "localizedStringWithKey:"
+ "v32@0:8@\"ASTTestResult\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@16q24@32"
+ "setSerialNumber:"
+ "dictionaryWithContentsOfFile:"
+ "getRepairTicket:"
+ "8185_Update"
+ "psd3"
+ "runningSemaphore"
+ "CRTest_8264"
+ "hasMesa"
+ "promptContinue:withContext:"
+ "_lastRunTestIndex"
+ "requestTermsAndConditionsWithCompletion:"
+ "testResult:%!@(MISSING)"
+ "_testContext"
+ "setResultData:"
+ "TB,V_started"
+ "CRTest_8262"
+ "sessionTimeOut"
+ "Retrying test index: %!l(MISSING)d"
+ "deviceInfoDict: %!@(MISSING)"
+ "T@\"CRTestSequencer\",&,N,V_testSequencer"
+ "dataLength > 0"
+ "CAMERA_CALIBRATION_INTRO_TITLE"
+ "Update streaming DAT file failed"
+ "Get customAMAuthInstallRef failed"
+ "dictionaryForKey:"
+ "ASTRepairProtocol"
+ "lidar-scanner"
+ "update:testIndex:testResult:"
+ "CRTest_8185_Patch"
+ "T@\"NSDictionary\",&,N,V_overrides"
+ "start"
+ "setTestId:"
+ "testId"
+ "CRTest_8259"
+ "initTestSequence"
+ "T@\"NSString\",&,N,V_name"
+ "CRTestContext"
+ "endWithCompletionHandler:"
+ "com.apple.corerepaird.test"
+ "localizedDescription"
+ "HV7WDiidgMf7lwAu++Lk5w"
+ "Failed to create SavageUpdater: %!@(MISSING)"
+ "updaterOptions: %!@(MISSING) updaterLoopCount: %!d(MISSING)"
+ "-[CRRepairSession startWithCompletionHandler:]"
+ "Checking test: %!@(MISSING)"
+ "initWithDelegate:"
+ "setSuiteResult:"
+ "-[CRRepairSession requestSuitesAvailableWithCompletionHandler:]"
+ "CAMERA_CALIBRATION_INSTRUCTIONS_TITLE"
+ "handleResult:"
+ "_doRetry"
+ "-[CRRepairSession requestSuiteStart:withCompletionHandler:]"
+ "supportPeCoNet"
+ "lastTestStatusCode"
+ "IPHONE COMP BATTERY"
+ "testIdentifer"
+ "https://gs.apple.com"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "CRTest_8185"
+ "initWithID:type:iconLocator:localizedTitle:localizedSubtitle:imageLocators:instructions:instructionsStyle:options:"
+ "needRequestURL"
+ "[CRDiagnostics][%!s(MISSING)]"
+ "stringByAppendingPathComponent:"
+ "T@\"NSArray\",&,N,V_partSPC"
+ "T@\"NSMutableArray\",&,N,V_testSequence"
+ "LiDAR not supported"
+ "Failed to read asset %!@(MISSING): %!@(MISSING)"
+ "IPAD REAR CAMERA"
+ "6002"
+ "setLastTestStatusCode:"
+ "8340"
+ "CR_TERMS_CONDITIONS"
+ "lastRunTestIndex"
+ "setLastRunTestIndex:"
+ "setBootIntentAndRebootToCheckerboardWithLocale:reply:"
+ "v24@?0@\"NSNumber\"8@\"NSString\"16"
+ "9008"
+ "enabled"
+ "preflightRIK"
+ "\x14"
+ "setTestSequencer:"
+ "8268"
+ "verifyFDRData -> %!d(MISSING)\n"
+ "_overrides"
+ "enableStagedSeal"
+ "9006"
+ "hasMesaDelta"
+ "com.apple.private.corerepair.diagnostics-delegate"
+ "testSequence"
+ "_patchItems"
+ "-[CRRepairSession endWithCompletionHandler:]"
+ "9010"
+ "shouldRun:"
+ "_partSPC"
+ "getBrunorTicketForBrunorFWUpdateWithOptions:BrunorTicket:auth:error:"
+ "START_SUITE"
+ "SavageUpdater work done. LoopCounter = %!d(MISSING)."
+ "Test sequencer is already running"
+ "doRetry"
+ "NvMR"
+ "com.apple.private.corerepair.control-boot-intent"
+ "objectForKey:"
+ "Verify psd3 successfully"
+ "-[CRRepairSession ping:]"
+ "Test sequencer completed"
+ "CRTest_8185_Update"
+ "_suiteResult"
+ "answer %!@(MISSING)"
+ "v24@0:8q16"
+ "@\"CRTestSequencer\""
+ "run:withContext:"
+ "_PrCL"
+ "Failed to get local psd3, error: %!@(MISSING)"
+ "prpcSign:outSignature:outDeviceNonce:outError:"
+ "v32@0:8@\"NSString\"16@?<v@?@\"ASTSuiteResult\"@\"NSError\">24"
+ "rik"
+ "CAMERA_CALIBRATION_INTRO_BODY_1"
+ "CRTest"
+ "Set exportedObject as a CRBootIntentHelper instance"
+ "ASTRepairSessionProvider is not linked on current platform"
+ "T@\"NSNumber\",&,N,V_testId"
+ "setTestSequencerQueue:"
+ "startWithCompletionHandler:"
+ "serialNumber"
+ "deviceSupportsRepairBootIntent"
+ "q16@0:8"
+ "setDoRetry:"
+ "setPatchItems:"
+ "https://gg.apple.com"
+ "powerCycleSensor:"
+ "setTestContext:"
+ "CRJasperTest"
+ "com.apple.CheckerBoard"
+ "-[CRRepairSession sendTestResult:withCompletion:]"
+ "T@\"NSNumber\",&,N,V_statusCode"
+ "Invalid test result"
+ "JpCl"
+ "startListening"
+ "Create optionsDict failed"
+ "requestSuitesAvailableWithCompletionHandler:"
+ "T@\"CRTestContext\",&,N,V_testContext"
+ "testSequencer"
+ "testStatusCode"
+ "8185"
+ "PrCL"
+ "T@\"NSNumber\",&,N,V_lastRunTestId"
+ "CRTest_9006"
+ "CRTest_9010"
+ "sendTestResult:withCompletion:"
+ "CRTest_9008"
+ "CoreRepairBootIntentProtocol"
+ "Get Brunor ticket failed"
+ "persistedBootIntentReason"
+ "setReceiver:"
+ "KGBSerialNumber"
+ "setRik:"
+ "Running test: %!@(MISSING)"
+ "_testId"
+ "\x04"
+ "T@\"ASTSuiteResult\",&,N,V_suiteResult"
+ "resultData"
+ "Updating Yonkers ..."
+ "CAMERA_CALIBRATION_INSTRUCTIONS_2"
+ "suiteResult"
+ "com.apple.corerepair.testSequencerQueue"
+ "setPrCL:"
+ "CRTest_8185_Staged"
+ "delegate"
+ "endpointURLs"
+ "Create updaterOptions failed"
+ "-[CRRepairSession requestSuiteResult:withCompletion:]"
+ "scope"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"NSNumber\"@\"NSString\"@\"NSString\"@\"NSError\">24"
+ "https://sklaxm.apple.com"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "noMovementAttitudeChangeMinThreshold"
+ "T@\"ASTRepairSessionProvider\",&,N,V_delegate"
+ "isSSRBootIntentSet"
+ "_serialNumber"
+ "Get Yonkers ticket failed"
+ "clearRepairBackup:"
+ "_started"
+ "initWithServiceName:entitlements:"
+ "8185_Staged"
+ "requestSuiteResult:withCompletion:"
+ "CRRepairSession"
+ "_testSequencer"
+ "8343"
+ "SavageUpdater failed with error: %!@(MISSING)"
+ "q"
+ "setPartSPC:"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_testSequencerQueue"
+ "LiDARCalibrationIllustration_Pan.svg"
+ "MSRk"
+ "partSPC"
+ "IPHONE COMP DISPLAY"
+ "setName:"
+ "dataWithContentsOfFile:options:error:"
+ "requestSuiteStart:withCompletionHandler:"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "setOverrides:"
+ "updateBrunorDATFirmwareWithReply:"
+ "Boot intent not set, check for unsealed data"
+ "userNotMovingTimeout"
+ "verifyFDRData %!p(MISSING) %!z(MISSING)u\n"
+ "_lastRunTestId"
+ "FSCl"
+ "Failed to verify psd3, pearlStatus: %!d(MISSING)"
+ "prpc"
+ "@\"CRTestContext\""
+ "suiteId"
+ "_runningSemaphore"
+ "supportHarvestPearl"
+ "setRunningSemaphore:"
+ "CAMERA_CALIBRATION_CANCEL_BUTTON_TITLE"
+ "TB,N,V_doRetry"
+ "Get prebootPath failed"
+ "CAMERA_CALIBRATION_INTRO_BODY_2"
+ "Updating Brunor ..."
+ "CANCEL"
+ "SerialNumber"
+ "setObject:atIndexedSubscript:"
+ "hop0"
+ "_lastTestStatusCode"
+ "setLastRunTestId:"
+ "Cancelling test: %!@(MISSING)"
+ "_suiteId"
+ "/var/mobile/Library/Preferences/%!@(MISSING).plist"
+ "8264"
+ "https://skl.apple.com"
+ "sceneErrorWarningThreshold"
+ "SSR suite"
+ "_resultData"
+ "Received a connection com.apple.corerepair.intentControl !"
+ "https://diagnostics-mdn1.apple.com"
+ "v24@0:8@?<v@?B@\"NSData\"@\"NSError\">16"
+ "CRTest_8276"
+ "CRTest_8343"
+ "T@\"NSNumber\",&,N,V_lastTestStatusCode"
+ "isDataClassSupported:"
+ "verifyPSD3WithReply:"
+ "updateTestSuiteProgress:"
+ "8185_Patch"
+ "ping:"
+ "CONTINUE"
+ "_testSequencerQueue"
+ "IPAD FRONT CAMERA"
+ "No test result"
+ "ignoreStagedData"
+ "setSuiteId:"
+ "-[PreferencesDelegate listener:shouldAcceptNewConnection:]"
+ "T@\"NSDictionary\",&,N,V_resultData"
+ "parameters"
+ "Tq,N,V_lastRunTestIndex"
+ "CAMERA_CALIBRATION_INSTRUCTIONS_1"
+ "Get osBootHash failed"
+ "overrides"
+ "T@\"NSString\",&,N,V_rik"
+ "_testSequence"
+ "Repair Assistant"
+ "CRTestSequencer"
+ "SSR not supported"
+ "setStatusCode:"
+ "initWithCapacity:"
+ "completeTestSuite:description:"
+ "/System/Library/PrivateFrameworks/CoreRepairCore.framework"
+ "8259"
+ "CRTest_6002"

```
