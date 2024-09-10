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
+ __dispatch_queue_attr_concurrent
+ _OBJC_CLASS_$_ASTInstructionalPrompt
+ _kBrunorTagResponseTicket
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_CRLocalization
+ _OBJC_CLASS_$_CRUserDefaults
+ _OBJC_CLASS_$_ASTSuiteResult
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$_ASTRepairSessionProvider
+ _os_variant_has_internal_content
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_CRBootIntentHelper
+ _OBJC_CLASS_$_ASTTestResult
+ _OBJC_CLASS_$_ASTSuite
+ _OBJC_CLASS_$_CRRepairHistory
CStrings:
+ "8185_Staged"
+ "Boot intent not set, check for unsealed data"
+ "updateProperties"
+ "-[CRRepairSession sendTestResult:withCompletion:]"
+ "deviceSupportsRepairBootIntent"
+ "getRepairTicket:"
+ "completeTestSuite:description:"
+ "T@\"NSString\",&,N,V_name"
+ "com.apple.private.corerepair.control-boot-intent"
+ "Get osBootHash failed"
+ "T@\"ASTSuiteResult\",&,N,V_suiteResult"
+ "_testId"
+ "CR_TERMS_CONDITIONS"
+ "Test result is not for the running test"
+ "CRTestSequencer"
+ "setLastTestStatusCode:"
+ "dictionaryForKey:"
+ "MPU"
+ "hasMesaDelta"
+ "initWithDelegate:"
+ "@\"NSObject<OS_dispatch_semaphore>\""
+ "ASTRepairSessionProvider is not linked on current platform"
+ "MSRk"
+ "START_SUITE"
+ "v40@0:8@16q24@32"
+ "\x16\x11"
+ "9010"
+ "patchItem"
+ "testSequence"
+ "-[CRRepairSession requestAsset:withCompletion:]"
+ "Cancelling test: %!@(MISSING)"
+ "Get Brunor ticket failed"
+ "CAMERA_CALIBRATION_INSTRUCTIONS_3"
+ "Get prebootPath failed"
+ "verifyFDRData %!p(MISSING) %!z(MISSING)u\n"
+ "setRunningSemaphore:"
+ "_testContext"
+ "Failed to verify psd3, pearlStatus: %!d(MISSING)"
+ "prpcSign:outSignature:outDeviceNonce:outError:"
+ "initWithId:suiteNameLocalizedString:suiteDescriptionLocalizedString:estimatedCompletionTimeLocalizedString:primaryAssetLocator:secondaryAssetLocator:"
+ "PrCL"
+ "Test sequencer completed"
+ "setPatchItems:"
+ "https://ig.apple.com"
+ "CRTest_8276"
+ "_lastRunTestIndex"
+ "T@\"NSNumber\",&,N,V_lastRunTestId"
+ "rik"
+ "IPHONE COMP RCAM"
+ "preflightRIK"
+ "setName:"
+ "_suiteResult"
+ "8185_Update"
+ "T@\"NSNumber\",&,N,V_testId"
+ "ASTRepairProtocol"
+ "setPrCL:"
+ "setTestSequence:"
+ "https://diagnostics-mdn1.apple.com"
+ "-[CRRepairSession startWithCompletionHandler:]"
+ "https://skl.apple.com"
+ "https://gg.apple.com"
+ "_runningSemaphore"
+ "serialNumber"
+ "Checking test: %!@(MISSING)"
+ "handleResult:"
+ "scope"
+ "8262"
+ "doRetry"
+ "T@\"NSDictionary\",&,N,V_overrides"
+ "ignoreStagedData"
+ "testIdentifer"
+ "v24@?0@\"NSNumber\"8@\"NSString\"16"
+ "SerialNumber"
+ "sessionTimeOut"
+ "setTestSequencerQueue:"
+ "6002"
+ "_overrides"
+ "isSSRBootIntentSet"
+ "_patchItems"
+ "CAMERA_CALIBRATION_INSTRUCTIONS_4"
+ "testContext"
+ "CAMERA_CALIBRATION_INSTRUCTIONS_2"
+ "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_runningSemaphore"
+ "Failed to read asset %!@(MISSING): %!@(MISSING)"
+ "CAMERA_CALIBRATION_CONTINUE_BUTTON_TITLE"
+ "CRTest_8185_Patch"
+ "T@\"NSNumber\",&,N,V_lastTestStatusCode"
+ "T@\"NSNumber\",&,N,V_statusCode"
+ "Verify PSD3 failed"
+ "stringByAppendingPathComponent:"
+ "started"
+ "-[CRRepairSession requestSuitesAvailableWithCompletionHandler:]"
+ "9006"
+ "T@\"NSString\",&,N,V_PrCL"
+ "-[CRRepairSession requestTermsAndConditionsWithCompletion:]"
+ "LiDAR not supported"
+ "deviceInfoDict: %!@(MISSING)"
+ "CRJasperTest"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "setSuiteId:"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"NSNumber\"@\"NSString\"@\"NSString\"@\"NSError\">24"
+ "T@\"NSString\",&,N,V_serialNumber"
+ "CRTest"
+ "com.apple.private.corerepair.diagnostics-delegate"
+ "verifyFDRData -> %!d(MISSING)\n"
+ "7004"
+ "CRTest_9010"
+ "CONTINUE"
+ "start"
+ "testSequencerQueue"
+ "persistedBootIntentReason"
+ "T@\"NSNumber\",&,N,V_suiteId"
+ "_testSequencerQueue"
+ "_started"
+ "setBootIntentAndRebootToCheckerboardWithLocale:reply:"
+ "setSerialNumber:"
+ "startListening"
+ "IPHONE COMP CAMERA"
+ "_PrCL"
+ "8340"
+ "SavageUpdaterExecCommand failed: %!@(MISSING)"
+ "Verify psd3 successfully"
+ "Invalid test result"
+ "TB,N,V_doRetry"
+ "startWithCompletionHandler:"
+ "CRTest_8259"
+ "Repair Assistant"
+ "8185"
+ "endpointURLs"
+ "IPHONE COMP BATTERY"
+ "supportLiDAR"
+ "_name"
+ "-[CRRepairSession endWithCompletionHandler:]"
+ "T@\"NSString\",&,N,V_rik"
+ "powerCycleSensor:"
+ "_lastRunTestId"
+ "perform next stage: %!@(MISSING)"
+ "T@\"CRTestContext\",&,N,V_testContext"
+ "Test sequencer is already running"
+ "8259"
+ "isEqualToNumber:"
+ "prpc"
+ "lastTestStatusCode"
+ "testId"
+ "CRTest_8185_Staged"
+ "CRTest_8185_Update"
+ "ping:"
+ "setSuiteResult:"
+ "NvMR"
+ "requestSuitesAvailableWithCompletionHandler:"
+ "testStatusCode"
+ "CAMERA_CALIBRATION_INTRO_TITLE"
+ "supportHarvestPearl"
+ "\x04"
+ "Set exportedObject as a CRBootIntentHelper instance"
+ "updateTestSuiteProgress:"
+ "CAMERA_CALIBRATION_INSTRUCTIONS_TITLE"
+ "suiteId"
+ "hasMesa"
+ "suiteResult"
+ "CRTest_8340"
+ "Received a connection com.apple.corerepair.intentControl !"
+ "CAMERA_CALIBRATION_CANCEL_BUTTON_TITLE"
+ "psd3"
+ "Running test: %!@(MISSING)"
+ "supportPeCoNet"
+ "CAMERA_CALIBRATION_INTRO_BODY_2"
+ "_statusCode"
+ "CAMERA_CALIBRATION_INTRO_BODY_1"
+ "setDoRetry:"
+ "CANCEL"
+ "answer %!@(MISSING)"
+ "SSR not supported"
+ "No running test found"
+ "setStatusCode:"
+ "_suiteId"
+ "[CRDiagnostics][%!s(MISSING)]"
+ "_testSequence"
+ "https://humb.apple.com"
+ "_partSPC"
+ "promptContinue:withContext:"
+ "CoreRepairBootIntentProtocol"
+ "https://sklaxm.apple.com"
+ "preflightPartSPC"
+ "overrides"
+ "v24@0:8q16"
+ "initWithCapacity:"
+ "v24@0:8@?<v@?B@\"NSData\"@\"NSError\">16"
+ "TB,V_started"
+ "enableStagedSeal"
+ "powerCycleSensor failed with error: %!@(MISSING)"
+ "sendTestResult:withCompletion:"
+ "setRik:"
+ "decodeObjectOfClasses:forKey:"
+ "@\"CRTestContext\""
+ "CRRepairSession"
+ "partSPC"
+ "runningSemaphore"
+ "T@\"CRTestSequencer\",&,N,V_testSequencer"
+ "_serialNumber"
+ "T@\"NSMutableArray\",&,N,V_testSequence"
+ "testResult:%!@(MISSING)"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "8343"
+ "T@\"ASTRepairSessionProvider\",&,N,V_delegate"
+ "setPartSPC:"
+ "T@\"NSMutableArray\",&,N,V_patchItems"
+ "JpCl"
+ "clearBootIntent:"
+ "_rik"
+ "Updating Brunor ..."
+ "@\"CRTestSequencer\""
+ "SSR suite"
+ "requestTermsAndConditionsWithCompletion:"
+ "verifyPSD3"
+ "SavageUpdater failed with error: %!@(MISSING)"
+ "componentsJoinedByString:"
+ "setLastRunTestId:"
+ "LiDARCalibrationIllustration_Pan.svg"
+ "8264"
+ "lastRunTestId"
+ "dataWithContentsOfFile:options:error:"
+ "IPHONE COMP FACEID"
+ "CRTest_9006"
+ "parameters"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "-[CRRepairSession requestSuiteStart:withCompletionHandler:]"
+ "_lastTestStatusCode"
+ "sceneErrorWarningThreshold"
+ "@\"ASTSuiteResult\""
+ "requestSuiteResult:withCompletion:"
+ "KGBSerialNumber"
+ "arrayWithObject:"
+ "initTestSequence"
+ "CRTest_7004"
+ "initWithID:type:iconLocator:localizedTitle:localizedSubtitle:imageLocators:instructions:instructionsStyle:options:"
+ "CRTest_8343"
+ "_doRetry"
+ "getBrunorTicketForBrunorFWUpdateWithOptions:BrunorTicket:auth:error:"
+ "CRTest_6002"
+ "Failed to create SavageUpdater: %!@(MISSING)"
+ "@\"ASTRepairSessionProvider\""
+ "IPAD FRONT CAMERA"
+ "dataLength > 0"
+ "localizedDescription"
+ "-[CRRepairSession requestSuiteResult:withCompletion:]"
+ "com.apple.corerepair.testSequencerQueue"
+ "updateBrunorDATFirmware"
+ "lidar-scanner"
+ "_resultData"
+ "Create optionsDict failed"
+ "v32@0:8@\"ASTTestResult\"16@?<v@?@\"NSError\">24"
+ "setTestContext:"
+ "PeCoNet not supported"
+ "IPAD REAR CAMERA"
+ "sceneErrorTimeOut"
+ "shouldRun:"
+ "\x14"
+ "CRTest_8262"
+ "setTestSequencer:"
+ "enabled"
+ "9008"
+ "CRTest_8268"
+ "Get Yonkers ticket failed"
+ "HV7WDiidgMf7lwAu++Lk5w"
+ "initWithServiceName:entitlements:"
+ "lastRunTestIndex"
+ "Cancelling test"
+ "isDataClassSupported:"
+ "setObject:atIndexedSubscript:"
+ "Tq,N,V_lastRunTestIndex"
+ "com.apple.corerepaird.test"
+ "CRTest_8185"
+ "CRTest_9008"
+ "setLastRunTestIndex:"
+ "Update streaming DAT file failed"
+ "requestAsset:withCompletion:"
+ "com.apple.CheckerBoard"
+ "com.apple.corerepair.testSequencer"
+ "noMovementAttitudeChangeMinThreshold"
+ "userNotMovingTimeout"
+ "clearRepairBackup:"
+ "updateBrunorDATFirmwareWithReply:"
+ "/System/Library/PrivateFrameworks/CoreRepairCore.framework"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_testSequencerQueue"
+ "setResultData:"
+ "v32@0:8@\"NSString\"16@?<v@?@\"ASTSuiteResult\"@\"NSError\">24"
+ "LiDARCalibrationIllustration_Setup.svg"
+ "hop0"
+ "-[CRRepairSession ping:]"
+ "8268"
+ "q16@0:8"
+ "T@\"NSArray\",&,N,V_partSPC"
+ "SavageUpdater work done. LoopCounter = %!d(MISSING)."
+ "run:withContext:"
+ "needRequestURL"
+ "objectForKey:"
+ "8185_Patch"
+ "setOverrides:"
+ "Failed to get local psd3, error: %!@(MISSING)"
+ "Updating Yonkers ..."
+ "CRTest_8264"
+ "IPHONE COMP DISPLAY"
+ "com.apple.corerepair.diagnostics-controller"
+ "patchItems"
+ "Retrying test index: %!l(MISSING)d"
+ "setStarted:"
+ "https://gs.apple.com"
+ "delegate"
+ "-[PreferencesDelegate listener:shouldAcceptNewConnection:]"
+ "showInstructionalPrompt:withConfirmation:"
+ "requestSuiteStart:withCompletionHandler:"
+ "verifyPSD3WithReply:"
+ "q"
+ "skipStageEAN"
+ "testSequencer"
+ "startTest:parameters:"
+ "T@\"NSDictionary\",&,N,V_resultData"
+ "No test result"
+ "setReceiver:"
+ "_testSequencer"
+ "updaterOptions: %!@(MISSING) updaterLoopCount: %!d(MISSING)"
+ "setTestId:"
+ "CAMERA_CALIBRATION_INSTRUCTIONS_1"
+ "8276"
+ "Create updaterOptions failed"
+ "dictionaryWithContentsOfFile:"
+ "localizedStringWithKey:"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
+ "/var/mobile/Library/Preferences/%!@(MISSING).plist"
+ "Get customAMAuthInstallRef failed"
+ "endWithCompletionHandler:"
+ "FSCl"
+ "CRTestContext"
+ "update:testIndex:testResult:"
+ "resultData"

```
