## corerepaird

> `/usr/libexec/corerepaird`

```diff

-645.42.1.0.0
-  __TEXT.__text: 0x32b1c
-  __TEXT.__auth_stubs: 0xf60
-  __TEXT.__objc_stubs: 0x2aa0
-  __TEXT.__objc_methlist: 0x2a30
-  __TEXT.__oslogstring: 0x1203
-  __TEXT.__cstring: 0x5361
+645.42.2.0.0
+  __TEXT.__text: 0x393f0
+  __TEXT.__auth_stubs: 0xf80
+  __TEXT.__objc_stubs: 0x3500
+  __TEXT.__objc_methlist: 0x3130
+  __TEXT.__cstring: 0x5c2a
+  __TEXT.__oslogstring: 0x14a1
   __TEXT.__const: 0x3940
-  __TEXT.__objc_methname: 0x32ff
-  __TEXT.__objc_classname: 0xb84
-  __TEXT.__objc_methtype: 0xab8
-  __TEXT.__gcc_except_tab: 0x208
-  __TEXT.__unwind_info: 0xd30
-  __DATA_CONST.__auth_got: 0x7c0
-  __DATA_CONST.__got: 0x380
+  __TEXT.__objc_methname: 0x3edd
+  __TEXT.__objc_classname: 0xcd0
+  __TEXT.__objc_methtype: 0xcc2
+  __TEXT.__gcc_except_tab: 0x260
+  __TEXT.__unwind_info: 0xe48
+  __DATA_CONST.__auth_got: 0x7d0
+  __DATA_CONST.__got: 0x3d0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0xe30
-  __DATA_CONST.__cfstring: 0x5740
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
+  __DATA_CONST.__objc_arraydata: 0x80
+  __DATA_CONST.__objc_arrayobj: 0x60
+  __DATA_CONST.__objc_intobj: 0x330
+  __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x5910
-  __DATA.__objc_selrefs: 0xe10
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
-  Functions: 1113
-  Symbols:   331
-  CStrings:  2100
+  Functions: 1257
+  Symbols:   345
+  CStrings:  2410
 
Symbols:
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_ASTInstructionalPrompt
+ _OBJC_CLASS_$_ASTRepairSessionProvider
+ _OBJC_CLASS_$_ASTSuite
+ _OBJC_CLASS_$_ASTSuiteResult
+ _OBJC_CLASS_$_ASTTestResult
+ _OBJC_CLASS_$_CRBootIntentHelper
+ _OBJC_CLASS_$_CRLocalization
+ _OBJC_CLASS_$_CRRepairHistory
+ _OBJC_CLASS_$_CRUserDefaults
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ __dispatch_queue_attr_concurrent
+ _os_variant_has_internal_content
CStrings:
+ "\x04"
+ "\x14"
+ "\x16\x11"
+ "-[CRRepairSession endWithCompletionHandler:]"
+ "-[CRRepairSession ping:]"
+ "-[CRRepairSession requestAsset:withCompletion:]"
+ "-[CRRepairSession requestSuiteResult:withCompletion:]"
+ "-[CRRepairSession requestSuiteStart:withCompletionHandler:]"
+ "-[CRRepairSession requestSuitesAvailableWithCompletionHandler:]"
+ "-[CRRepairSession requestTermsAndConditionsWithCompletion:]"
+ "-[CRRepairSession sendTestResult:withCompletion:]"
+ "-[CRRepairSession startWithCompletionHandler:]"
+ "-[PreferencesDelegate listener:shouldAcceptNewConnection:]"
+ "/System/Library/PrivateFrameworks/CoreRepairCore.framework"
+ "/var/mobile/Library/Preferences/%!@(MISSING).plist"
+ "6002"
+ "7004"
+ "8185"
+ "8185_Patch"
+ "8185_Staged"
+ "8185_Update"
+ "8259"
+ "8262"
+ "8262 failed with statusCode: %!@(MISSING), continue to run the following testIDs"
+ "8264"
+ "8268"
+ "8276"
+ "8340"
+ "8343"
+ "9006"
+ "9008"
+ "9010"
+ "@\"ASTRepairSessionProvider\""
+ "@\"ASTSuiteResult\""
+ "@\"CRTestContext\""
+ "@\"CRTestSequencer\""
+ "@\"NSObject<OS_dispatch_semaphore>\""
+ "ASTRepairProtocol"
+ "ASTRepairSessionProvider is not linked on current platform"
+ "Boot intent not set, check for unsealed data"
+ "CAMERA_CALIBRATION_CANCEL_BUTTON_TITLE"
+ "CAMERA_CALIBRATION_CONTINUE_BUTTON_TITLE"
+ "CAMERA_CALIBRATION_INSTRUCTIONS_1"
+ "CAMERA_CALIBRATION_INSTRUCTIONS_2"
+ "CAMERA_CALIBRATION_INSTRUCTIONS_3"
+ "CAMERA_CALIBRATION_INSTRUCTIONS_4"
+ "CAMERA_CALIBRATION_INSTRUCTIONS_TITLE"
+ "CAMERA_CALIBRATION_INTRO_BODY_1"
+ "CAMERA_CALIBRATION_INTRO_BODY_2"
+ "CAMERA_CALIBRATION_INTRO_TITLE"
+ "CANCEL"
+ "CONTINUE"
+ "CRJasperTest"
+ "CRRepairSession"
+ "CRTest"
+ "CRTestContext"
+ "CRTestSequencer"
+ "CRTest_6002"
+ "CRTest_7004"
+ "CRTest_8185"
+ "CRTest_8185_Patch"
+ "CRTest_8185_Staged"
+ "CRTest_8185_Update"
+ "CRTest_8259"
+ "CRTest_8262"
+ "CRTest_8264"
+ "CRTest_8268"
+ "CRTest_8276"
+ "CRTest_8340"
+ "CRTest_8343"
+ "CRTest_9006"
+ "CRTest_9008"
+ "CRTest_9010"
+ "CR_TERMS_CONDITIONS"
+ "Cancelling test"
+ "Cancelling test: %!@(MISSING)"
+ "Checking test: %!@(MISSING)"
+ "CoreRepairBootIntentProtocol"
+ "FSCl"
+ "Failed to read asset %!@(MISSING): %!@(MISSING)"
+ "HV7WDiidgMf7lwAu++Lk5w"
+ "IPAD FRONT CAMERA"
+ "IPAD REAR CAMERA"
+ "IPAD TOUCH ID"
+ "IPHONE COMP BATTERY"
+ "IPHONE COMP CAMERA"
+ "IPHONE COMP DISPLAY"
+ "IPHONE COMP FACEID"
+ "IPHONE COMP RCAM"
+ "Invalid test result"
+ "JpCl"
+ "KGBSerialNumber"
+ "LiDAR not supported"
+ "LiDARCalibrationIllustration_Pan.svg"
+ "LiDARCalibrationIllustration_Setup.svg"
+ "MPU"
+ "MSRk"
+ "No running test found"
+ "No test result"
+ "NvMR"
+ "PeCoNet not supported"
+ "PrCL"
+ "Received a connection com.apple.corerepair.intentControl !"
+ "Repair Assistant"
+ "Retrying test index: %!l(MISSING)d"
+ "Running test: %!@(MISSING)"
+ "SSR not supported"
+ "SSR suite"
+ "START_SUITE"
+ "SerialNumber"
+ "Set exportedObject as a CRBootIntentHelper instance"
+ "T@\"ASTRepairSessionProvider\",&,N,V_delegate"
+ "T@\"ASTSuiteResult\",&,N,V_suiteResult"
+ "T@\"CRTestContext\",&,N,V_testContext"
+ "T@\"CRTestSequencer\",&,N,V_testSequencer"
+ "T@\"NSArray\",&,N,V_partSPC"
+ "T@\"NSDictionary\",&,N,V_overrides"
+ "T@\"NSDictionary\",&,N,V_resultData"
+ "T@\"NSMutableArray\",&,N,V_patchItems"
+ "T@\"NSMutableArray\",&,N,V_testSequence"
+ "T@\"NSNumber\",&,N,V_lastRunTestId"
+ "T@\"NSNumber\",&,N,V_lastTestStatusCode"
+ "T@\"NSNumber\",&,N,V_statusCode"
+ "T@\"NSNumber\",&,N,V_suiteId"
+ "T@\"NSNumber\",&,N,V_testId"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_testSequencerQueue"
+ "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_runningSemaphore"
+ "T@\"NSString\",&,N,V_PrCL"
+ "T@\"NSString\",&,N,V_name"
+ "T@\"NSString\",&,N,V_rik"
+ "T@\"NSString\",&,N,V_serialNumber"
+ "TB,N,V_doRetry"
+ "TB,V_started"
+ "Test result is not for the running test"
+ "Test sequencer completed"
+ "Test sequencer is already running"
+ "Tq,N,V_lastRunTestIndex"
+ "[CRDiagnostics][%!s(MISSING)]"
+ "_PrCL"
+ "_doRetry"
+ "_lastRunTestId"
+ "_lastRunTestIndex"
+ "_lastTestStatusCode"
+ "_name"
+ "_overrides"
+ "_partSPC"
+ "_patchItems"
+ "_resultData"
+ "_rik"
+ "_runningSemaphore"
+ "_serialNumber"
+ "_started"
+ "_statusCode"
+ "_suiteId"
+ "_suiteResult"
+ "_testContext"
+ "_testId"
+ "_testSequence"
+ "_testSequencer"
+ "_testSequencerQueue"
+ "answer %!@(MISSING)"
+ "arrayWithObject:"
+ "clearBootIntent:"
+ "clearRepairBackup:"
+ "com.apple.CheckerBoard"
+ "com.apple.corerepair.diagnostics-controller"
+ "com.apple.corerepair.testSequencer"
+ "com.apple.corerepair.testSequencerQueue"
+ "com.apple.corerepaird.test"
+ "com.apple.private.corerepair.control-boot-intent"
+ "com.apple.private.corerepair.diagnostics-delegate"
+ "completeTestSuite:description:"
+ "componentsJoinedByString:"
+ "dataWithContentsOfFile:options:error:"
+ "decodeObjectOfClasses:forKey:"
+ "delegate"
+ "deviceSupportsRepairBootIntent"
+ "dictionaryForKey:"
+ "dictionaryWithContentsOfFile:"
+ "doRetry"
+ "enableStagedSeal"
+ "enabled"
+ "endWithCompletionHandler:"
+ "endpointURLs"
+ "getRepairTicket:"
+ "handleResult:"
+ "hasMesa"
+ "hasMesaDelta"
+ "hop0"
+ "https://gg.apple.com"
+ "https://gs.apple.com"
+ "https://humb.apple.com"
+ "https://ig.apple.com"
+ "https://skl.apple.com"
+ "https://sklaxm.apple.com"
+ "ignoreStagedData"
+ "initTestSequence"
+ "initWithCapacity:"
+ "initWithDelegate:"
+ "initWithID:type:iconLocator:localizedTitle:localizedSubtitle:imageLocators:instructions:instructionsStyle:options:"
+ "initWithId:suiteNameLocalizedString:suiteDescriptionLocalizedString:estimatedCompletionTimeLocalizedString:primaryAssetLocator:secondaryAssetLocator:"
+ "initWithServiceName:entitlements:"
+ "isDataClassSupported:"
+ "isEqualToNumber:"
+ "isSSRBootIntentSet"
+ "lastRunTestId"
+ "lastRunTestIndex"
+ "lastTestStatusCode"
+ "lidar-scanner"
+ "localizedDescription"
+ "localizedStringWithKey:"
+ "needRequestURL"
+ "noMovementAttitudeChangeMinThreshold"
+ "objectForKey:"
+ "overrides"
+ "parameters"
+ "partSPC"
+ "patchItem"
+ "patchItems"
+ "persistedBootIntentReason"
+ "ping:"
+ "preflightPartSPC"
+ "preflightRIK"
+ "promptContinue:withContext:"
+ "q"
+ "q16@0:8"
+ "requestAsset:withCompletion:"
+ "requestSuiteResult:withCompletion:"
+ "requestSuiteStart:withCompletionHandler:"
+ "requestSuitesAvailableWithCompletionHandler:"
+ "requestTermsAndConditionsWithCompletion:"
+ "resultData"
+ "rik"
+ "run:withContext:"
+ "runningSemaphore"
+ "sceneErrorTimeOut"
+ "sceneErrorWarningThreshold"
+ "scope"
+ "sendTestResult:withCompletion:"
+ "serialNumber"
+ "sessionTimeOut"
+ "setBootIntentAndRebootToCheckerboardWithLocale:reply:"
+ "setDoRetry:"
+ "setLastRunTestId:"
+ "setLastRunTestIndex:"
+ "setLastTestStatusCode:"
+ "setName:"
+ "setObject:atIndexedSubscript:"
+ "setOverrides:"
+ "setPartSPC:"
+ "setPatchItems:"
+ "setPrCL:"
+ "setReceiver:"
+ "setResultData:"
+ "setRik:"
+ "setRunningSemaphore:"
+ "setSerialNumber:"
+ "setStarted:"
+ "setStatusCode:"
+ "setSuiteId:"
+ "setSuiteResult:"
+ "setTestContext:"
+ "setTestId:"
+ "setTestSequence:"
+ "setTestSequencer:"
+ "setTestSequencerQueue:"
+ "shouldRun:"
+ "showInstructionalPrompt:withConfirmation:"
+ "skipStageEAN"
+ "start"
+ "startListening"
+ "startTest:parameters:"
+ "startWithCompletionHandler:"
+ "started"
+ "stringByAppendingPathComponent:"
+ "suiteId"
+ "suiteResult"
+ "supportHarvestPearl"
+ "supportLiDAR"
+ "supportPeCoNet"
+ "testContext"
+ "testId"
+ "testIdentifer"
+ "testResult:%!@(MISSING)"
+ "testSequence"
+ "testSequencer"
+ "testSequencerQueue"
+ "testStatusCode"
+ "update:testIndex:testResult:"
+ "updateProperties"
+ "updateTestSuiteProgress:"
+ "userNotMovingTimeout"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "v24@0:8@?<v@?B@\"NSData\"@\"NSError\">16"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v24@0:8q16"
+ "v24@?0@\"NSNumber\"8@\"NSString\"16"
+ "v32@0:8@\"ASTTestResult\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"NSNumber\"@\"NSString\"@\"NSString\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"ASTSuiteResult\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
+ "v40@0:8@16q24@32"

```
