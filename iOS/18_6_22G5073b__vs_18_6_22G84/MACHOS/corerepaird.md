## corerepaird

> `/usr/libexec/corerepaird`

```diff

 696.140.2.0.0
-  __TEXT.__text: 0x12f8
-  __TEXT.__auth_stubs: 0x1c0
-  __TEXT.__objc_stubs: 0x2e0
-  __TEXT.__objc_methlist: 0x37c
-  __TEXT.__oslogstring: 0x1f2
-  __TEXT.__cstring: 0x1ec
-  __TEXT.__const: 0x10
-  __TEXT.__objc_classname: 0xdf
-  __TEXT.__objc_methname: 0x6ca
-  __TEXT.__objc_methtype: 0x3af
-  __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0xe8
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x120
-  __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x30
+  __TEXT.__text: 0x77e8
+  __TEXT.__auth_stubs: 0x310
+  __TEXT.__objc_stubs: 0xea0
+  __TEXT.__objc_methlist: 0xa24
+  __TEXT.__cstring: 0xaa3
+  __TEXT.__oslogstring: 0x45e
+  __TEXT.__const: 0x38
+  __TEXT.__objc_classname: 0x217
+  __TEXT.__objc_methname: 0x11a1
+  __TEXT.__objc_methtype: 0x5aa
+  __TEXT.__gcc_except_tab: 0x58
+  __TEXT.__unwind_info: 0x1b8
+  __DATA_CONST.__auth_got: 0x198
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__const: 0xb8
+  __DATA_CONST.__cfstring: 0xce0
+  __DATA_CONST.__objc_classlist: 0xc8
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x740
-  __DATA.__objc_selrefs: 0x250
-  __DATA.__objc_ivar: 0x24
-  __DATA.__objc_data: 0x190
-  __DATA.__data: 0x268
+  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_arraydata: 0x78
+  __DATA_CONST.__objc_arrayobj: 0x60
+  __DATA_CONST.__objc_intobj: 0x288
+  __DATA_CONST.__objc_doubleobj: 0x20
+  __DATA.__objc_const: 0x1640
+  __DATA.__objc_selrefs: 0x540
+  __DATA.__objc_ivar: 0x60
+  __DATA.__objc_data: 0x7d0
+  __DATA.__data: 0x388
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libz.1.dylib
   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
-  UUID: 3D8B3B95-3C5A-3A0C-9DAB-5DC0C6D74443
-  Functions: 37
-  Symbols:   56
-  CStrings:  184
+  UUID: A357FB6A-BF35-31D8-80A2-B2094D983616
+  Functions: 164
+  Symbols:   93
+  CStrings:  571
 
Symbols:
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_ASTInstructionalPrompt
+ _OBJC_CLASS_$_ASTRepairSessionProvider
+ _OBJC_CLASS_$_ASTSuite
+ _OBJC_CLASS_$_ASTSuiteResult
+ _OBJC_CLASS_$_ASTTestResult
+ _OBJC_CLASS_$_CRFDRUtils
+ _OBJC_CLASS_$_CRLocalization
+ _OBJC_CLASS_$_CRRepairHistory
+ _OBJC_CLASS_$_CRUserDefaults
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$_NSMutableDictionary
+ __Block_object_dispose
+ __NSConcreteStackBlock
+ __Unwind_Resume
+ ___kCFBooleanTrue
+ ___objc_personality_v0
+ __dispatch_queue_attr_concurrent
+ __os_log_error_impl
+ _dispatch_async
+ _dispatch_queue_create
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _objc_enumerationMutation
+ _objc_release
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x9
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x4
+ _objc_retain_x8
+ _os_transaction_create
+ _os_variant_has_internal_content
CStrings:
+ ""
+ ","
+ "-[CRRepairSession endWithCompletionHandler:]"
+ "-[CRRepairSession ping:]"
+ "-[CRRepairSession requestAsset:withCompletion:]"
+ "-[CRRepairSession requestSuiteResult:withCompletion:]"
+ "-[CRRepairSession requestSuiteStart:withCompletionHandler:]"
+ "-[CRRepairSession requestSuitesAvailableWithCompletionHandler:]"
+ "-[CRRepairSession requestTermsAndConditionsWithCompletion:]"
+ "-[CRRepairSession sendTestResult:withCompletion:]"
+ "-[CRRepairSession startWithCompletionHandler:]"
+ "/System/Library/PrivateFrameworks/CoreRepairCore.framework"
+ "/var/mobile/Library/Preferences/%@.plist"
+ "6002"
+ "7004"
+ "8185"
+ "8185_Patch"
+ "8185_Staged"
+ "8185_Update"
+ "8259"
+ "8262"
+ "8262 failed with statusCode: %@, continue to run the following testIDs"
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
+ "@\"NSDictionary\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@\"NSObject<OS_dispatch_semaphore>\""
+ "@24@0:8@\"NSCoder\"16"
+ "@24@0:8@16"
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
+ "Cancelling test: %@"
+ "Checking test: %@"
+ "FSC2"
+ "FSCl"
+ "Failed to get delta components: %@"
+ "Failed to read asset %@: %@"
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
+ "NSCoding"
+ "NSSecureCoding"
+ "No delta components found"
+ "No running test found"
+ "No test result"
+ "NvMR"
+ "PeCoNet not supported"
+ "Repair Assistant"
+ "Retrying test index: %ld"
+ "Running test: %@"
+ "SSR not supported"
+ "SSR suite"
+ "START_SUITE"
+ "T@\"ASTRepairSessionProvider\",&,N,V_delegate"
+ "T@\"ASTSuiteResult\",&,N,V_suiteResult"
+ "T@\"CRTestContext\",&,N,V_testContext"
+ "T@\"CRTestSequencer\",&,N,V_testSequencer"
+ "T@\"NSDictionary\",&,N,V_overrides"
+ "T@\"NSDictionary\",&,N,V_resultData"
+ "T@\"NSMutableArray\",&,N,V_testSequence"
+ "T@\"NSNumber\",&,N,V_statusCode"
+ "T@\"NSNumber\",&,N,V_suiteId"
+ "T@\"NSNumber\",&,N,V_testId"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_testSequencerQueue"
+ "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_runningSemaphore"
+ "T@\"NSString\",&,N,V_name"
+ "TB,R"
+ "TB,V_started"
+ "Test result is not for the running test"
+ "Test sequencer completed"
+ "Test sequencer is already running"
+ "[CRDiagnostics][%s]"
+ "_delegate"
+ "_name"
+ "_overrides"
+ "_resultData"
+ "_runningSemaphore"
+ "_started"
+ "_statusCode"
+ "_suiteId"
+ "_suiteResult"
+ "_testContext"
+ "_testId"
+ "_testSequence"
+ "_testSequencer"
+ "_testSequencerQueue"
+ "addEntriesFromDictionary:"
+ "addObject:"
+ "answer %@"
+ "arrayWithObject:"
+ "arrayWithObjects:count:"
+ "com.apple.CheckerBoard"
+ "com.apple.corerepair.diagnostics-controller"
+ "com.apple.corerepair.testSequencer"
+ "com.apple.corerepair.testSequencerQueue"
+ "com.apple.corerepaird"
+ "com.apple.corerepaird.test"
+ "com.apple.private.corerepair.diagnostics-delegate"
+ "completeTestSuite:description:"
+ "componentsJoinedByString:"
+ "containsObject:"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "data"
+ "dataWithContentsOfFile:options:error:"
+ "decodeObjectOfClasses:forKey:"
+ "delegate"
+ "deviceSupportsRepairBootIntent"
+ "dictionaryForKey:"
+ "dictionaryWithContentsOfFile:"
+ "dictionaryWithObjects:forKeys:count:"
+ "enableStagedSeal"
+ "enabled"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "endWithCompletionHandler:"
+ "endpointURLs"
+ "findUnsealedDataWithError:"
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
+ "i"
+ "ignoreStagedData"
+ "initTestSequence"
+ "initWithCapacity:"
+ "initWithCoder:"
+ "initWithDelegate:"
+ "initWithID:type:iconLocator:localizedTitle:localizedSubtitle:imageLocators:instructions:instructionsStyle:options:"
+ "initWithId:suiteNameLocalizedString:suiteDescriptionLocalizedString:estimatedCompletionTimeLocalizedString:primaryAssetLocator:secondaryAssetLocator:"
+ "initWithServiceName:entitlements:"
+ "initWithSuiteName:"
+ "ipad"
+ "ipad.rear.camera.badge.scope"
+ "iphone.rear.camera.badge.scope"
+ "isDataClassSupported:"
+ "isEqualToNumber:"
+ "isEqualToString:"
+ "isSSRBootIntentSet"
+ "keyBlob"
+ "lidar-scanner"
+ "localizedDescription"
+ "localizedStringWithKey:"
+ "name"
+ "needRequestURL"
+ "noMovementAttitudeChangeMinThreshold"
+ "numberWithInteger:"
+ "objectAtIndexedSubscript:"
+ "objectForKey:"
+ "objectForKeyedSubscript:"
+ "overrides"
+ "parameters"
+ "patchItem"
+ "persistedBootIntentReason"
+ "ping:"
+ "preflightPartSPC"
+ "preflightRIK"
+ "promptContinue:withContext:"
+ "psd3"
+ "requestAsset:withCompletion:"
+ "requestSuiteResult:withCompletion:"
+ "requestSuiteStart:withCompletionHandler:"
+ "requestSuitesAvailableWithCompletionHandler:"
+ "requestTermsAndConditionsWithCompletion:"
+ "resultData"
+ "run:withContext:"
+ "runningSemaphore"
+ "sceneErrorTimeOut"
+ "sceneErrorWarningThreshold"
+ "sendTestResult:withCompletion:"
+ "sessionTimeOut"
+ "setName:"
+ "setObject:atIndexedSubscript:"
+ "setObject:forKeyedSubscript:"
+ "setOverrides:"
+ "setReceiver:"
+ "setResultData:"
+ "setRunningSemaphore:"
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
+ "statusCode"
+ "stringByAppendingPathComponent:"
+ "stringWithFormat:"
+ "suiteId"
+ "suiteResult"
+ "supportHarvestPearl"
+ "supportLiDAR"
+ "supportPeCoNet"
+ "supportsSecureCoding"
+ "testContext"
+ "testId"
+ "testIdentifier"
+ "testResult:%@"
+ "testSequence"
+ "testSequencer"
+ "testSequencerQueue"
+ "testStatusCode"
+ "update:testIndex:testResult:"
+ "updateProperties"
+ "updateTestSuiteProgress:"
+ "userNotMovingTimeout"
+ "v24@0:8@\"NSCoder\"16"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "v24@?0@\"NSNumber\"8@\"NSString\"16"
+ "v32@0:8@\"ASTTestResult\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"NSNumber\"@\"NSString\"@\"NSString\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"ASTSuiteResult\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "v32@0:8@16@24"
+ "v40@0:8@16q24@32"

```
