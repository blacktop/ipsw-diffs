## corerepaird

> `/usr/libexec/corerepaird`

```diff

-645.42.2.0.0
-  __TEXT.__text: 0x393f0
-  __TEXT.__auth_stubs: 0xf80
-  __TEXT.__objc_stubs: 0x3500
-  __TEXT.__objc_methlist: 0x3130
-  __TEXT.__cstring: 0x5c2a
-  __TEXT.__oslogstring: 0x14a1
+645.60.42.502.1
+  __TEXT.__text: 0x33c4c
+  __TEXT.__auth_stubs: 0xf40
+  __TEXT.__objc_stubs: 0x2dc0
+  __TEXT.__objc_methlist: 0x2b48
+  __TEXT.__oslogstring: 0x12c0
+  __TEXT.__cstring: 0x54cd
   __TEXT.__const: 0x3940
-  __TEXT.__objc_methname: 0x3edd
-  __TEXT.__objc_classname: 0xcd0
-  __TEXT.__objc_methtype: 0xcc2
-  __TEXT.__gcc_except_tab: 0x260
-  __TEXT.__unwind_info: 0xe48
-  __DATA_CONST.__auth_got: 0x7d0
-  __DATA_CONST.__got: 0x3d0
+  __TEXT.__objc_methname: 0x37b2
+  __TEXT.__objc_classname: 0xbb2
+  __TEXT.__objc_methtype: 0xb5e
+  __TEXT.__gcc_except_tab: 0x278
+  __TEXT.__unwind_info: 0xd50
+  __DATA_CONST.__auth_got: 0x7b0
+  __DATA_CONST.__got: 0x390
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0xea8
-  __DATA_CONST.__cfstring: 0x6260
-  __DATA_CONST.__objc_classlist: 0x2f0
+  __DATA_CONST.__const: 0xe58
+  __DATA_CONST.__cfstring: 0x58c0
+  __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x68
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_classrefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x2b8
-  __DATA_CONST.__objc_arraydata: 0x80
-  __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA_CONST.__objc_intobj: 0x330
-  __DATA_CONST.__objc_doubleobj: 0x20
+  __DATA_CONST.__objc_superrefs: 0x218
+  __DATA_CONST.__objc_intobj: 0xc0
+  __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x6b68
-  __DATA.__objc_selrefs: 0x10f0
-  __DATA.__objc_ivar: 0x390
-  __DATA.__objc_data: 0x1d60
-  __DATA.__data: 0xae8
+  __DATA.__objc_const: 0x5be8
+  __DATA.__objc_selrefs: 0xf30
+  __DATA.__objc_ivar: 0x354
+  __DATA.__objc_data: 0x1720
+  __DATA.__data: 0xa88
   __DATA.__bss: 0xa8
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libz.1.dylib
   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
-  Functions: 1257
-  Symbols:   345
-  CStrings:  2410
+  Functions: 1141
+  Symbols:   331
+  CStrings:  2196
 
Symbols:
+ _DeviceIdentityCreateClientCertificateRequest
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_CLASS_$_NSURLSession
+ _OBJC_CLASS_$_NSURLSessionConfiguration
- _DeviceIdentityIssueClientCertificateWithCompletion
- _OBJC_CLASS_$_ASTInstructionalPrompt
- _OBJC_CLASS_$_ASTRepairSessionProvider
- _OBJC_CLASS_$_ASTSuite
- _OBJC_CLASS_$_ASTSuiteResult
- _OBJC_CLASS_$_ASTTestResult
- _OBJC_CLASS_$_CRLocalization
- _OBJC_CLASS_$_CRRepairHistory
- _OBJC_CLASS_$_CRUserDefaults
- _OBJC_CLASS_$_NSConstantArray
- _OBJC_CLASS_$_NSConstantDoubleNumber
- _SecCertificateGetBytePtr
- _SecCertificateGetLength
- __dispatch_queue_attr_concurrent
- _dispatch_get_global_queue
- _kMAOptionsSOCKSProxyHost
- _kMAOptionsSOCKSProxyPort
- _os_variant_has_internal_content
CStrings:
+ "%!@(MISSING) - %!@(MISSING)"
+ "-----BEGIN CERTIFICATE-----(.+?)-----END CERTIFICATE-----\n"
+ "3kmXfug8VcxLI5yEmsqQKw"
+ "@40@0:8@16@24^@32"
+ "@48@0:8@16@24@32^@40"
+ "Empty configuration"
+ "Empty session"
+ "Failed to create regex: %!@(MISSING)"
+ "Failed to find version info"
+ "Failed to get url request, error: %!@(MISSING)"
+ "Failed to request BAA: %!@(MISSING)"
+ "HTTP Error: %!@(MISSING)"
+ "HTTP Request Header: %!@(MISSING)"
+ "HTTP Request: %!@(MISSING)"
+ "HTTP Response Header: %!@(MISSING)"
+ "HTTP Response: %!@(MISSING)"
+ "HTTP Status: %!d(MISSING)"
+ "No User-Agent"
+ "Original Headers: %!@(MISSING)"
+ "Request BAA failed with status: %!d(MISSING) error: %!@(MISSING)"
+ "Request BAA timeout"
+ "SOCKSEnable"
+ "User-Agent"
+ "^.*\\(MobileActivation-.*?\\)"
+ "_extractCertsFromResponse:"
+ "_getVersionInfo:"
+ "_httpSendRequest:proxySettings:withError:"
+ "allHTTPHeaderFields"
+ "allHeaderFields"
+ "corerepaird-CB"
+ "corerepaird-SB"
+ "dataTaskWithRequest:completionHandler:"
+ "enumerateMatchesInString:options:range:usingBlock:"
+ "ephemeralSessionConfiguration"
+ "firstMatchInString:options:range:"
+ "initWithBase64EncodedString:options:"
+ "libauthinstall_device-1033.60.13"
+ "range"
+ "rangeAtIndex:"
+ "regularExpressionWithPattern:options:error:"
+ "requestBAACertificates:apticket:proxySettings:withError:"
+ "sessionWithConfiguration:"
+ "setConnectionProxyDictionary:"
+ "setValue:forHTTPHeaderField:"
+ "substringWithRange:"
+ "v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24"
+ "v32@?0@\"NSTextCheckingResult\"8Q16^B24"
- "\x04"
- "\x14"
- "-[CRRepairSession endWithCompletionHandler:]"
- "-[CRRepairSession ping:]"
- "-[CRRepairSession requestAsset:withCompletion:]"
- "-[CRRepairSession requestSuiteResult:withCompletion:]"
- "-[CRRepairSession requestSuiteStart:withCompletionHandler:]"
- "-[CRRepairSession requestSuitesAvailableWithCompletionHandler:]"
- "-[CRRepairSession requestTermsAndConditionsWithCompletion:]"
- "-[CRRepairSession sendTestResult:withCompletion:]"
- "-[CRRepairSession startWithCompletionHandler:]"
- "/System/Library/PrivateFrameworks/CoreRepairCore.framework"
- "/var/mobile/Library/Preferences/%!@(MISSING).plist"
- "6002"
- "7004"
- "8185"
- "8185_Patch"
- "8185_Staged"
- "8185_Update"
- "8259"
- "8262"
- "8262 failed with statusCode: %!@(MISSING), continue to run the following testIDs"
- "8264"
- "8268"
- "8276"
- "8340"
- "8343"
- "9006"
- "9008"
- "9010"
- "@\"ASTRepairSessionProvider\""
- "@\"ASTSuiteResult\""
- "@\"CRTestContext\""
- "@\"CRTestSequencer\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "ASTRepairProtocol"
- "ASTRepairSessionProvider is not linked on current platform"
- "Boot intent not set, check for unsealed data"
- "CAMERA_CALIBRATION_CANCEL_BUTTON_TITLE"
- "CAMERA_CALIBRATION_CONTINUE_BUTTON_TITLE"
- "CAMERA_CALIBRATION_INSTRUCTIONS_1"
- "CAMERA_CALIBRATION_INSTRUCTIONS_2"
- "CAMERA_CALIBRATION_INSTRUCTIONS_3"
- "CAMERA_CALIBRATION_INSTRUCTIONS_4"
- "CAMERA_CALIBRATION_INSTRUCTIONS_TITLE"
- "CAMERA_CALIBRATION_INTRO_BODY_1"
- "CAMERA_CALIBRATION_INTRO_BODY_2"
- "CAMERA_CALIBRATION_INTRO_TITLE"
- "CANCEL"
- "CONTINUE"
- "CRJasperTest"
- "CRRepairSession"
- "CRTest"
- "CRTestSequencer"
- "CRTest_6002"
- "CRTest_7004"
- "CRTest_8185"
- "CRTest_8185_Patch"
- "CRTest_8185_Staged"
- "CRTest_8185_Update"
- "CRTest_8259"
- "CRTest_8262"
- "CRTest_8264"
- "CRTest_8268"
- "CRTest_8276"
- "CRTest_8340"
- "CRTest_8343"
- "CRTest_9006"
- "CRTest_9008"
- "CRTest_9010"
- "CR_TERMS_CONDITIONS"
- "Cancelling test"
- "Cancelling test: %!@(MISSING)"
- "Checking test: %!@(MISSING)"
- "DeviceIdentityIssueClientCertificateWithCompletion failed with no certificates"
- "DeviceIdentityIssueClientCertificateWithCompletion failed: %!@(MISSING)"
- "DeviceIdentityIssueClientCertificateWithCompletion timeout"
- "FSCl"
- "Failed to read asset %!@(MISSING): %!@(MISSING)"
- "HV7WDiidgMf7lwAu++Lk5w"
- "IPAD FRONT CAMERA"
- "IPAD REAR CAMERA"
- "IPAD TOUCH ID"
- "IPHONE COMP BATTERY"
- "IPHONE COMP CAMERA"
- "IPHONE COMP DISPLAY"
- "IPHONE COMP FACEID"
- "IPHONE COMP RCAM"
- "Invalid test result"
- "JpCl"
- "KGBSerialNumber"
- "LiDAR not supported"
- "LiDARCalibrationIllustration_Pan.svg"
- "LiDARCalibrationIllustration_Setup.svg"
- "MPU"
- "MSRk"
- "No running test found"
- "No test result"
- "NvMR"
- "PeCoNet not supported"
- "Repair Assistant"
- "Request BAA failed"
- "Retrying test index: %!l(MISSING)d"
- "Running test: %!@(MISSING)"
- "SSR not supported"
- "SSR suite"
- "START_SUITE"
- "T@\"ASTRepairSessionProvider\",&,N,V_delegate"
- "T@\"ASTSuiteResult\",&,N,V_suiteResult"
- "T@\"CRTestContext\",&,N,V_testContext"
- "T@\"CRTestSequencer\",&,N,V_testSequencer"
- "T@\"NSDictionary\",&,N,V_overrides"
- "T@\"NSDictionary\",&,N,V_resultData"
- "T@\"NSMutableArray\",&,N,V_testSequence"
- "T@\"NSNumber\",&,N,V_statusCode"
- "T@\"NSNumber\",&,N,V_suiteId"
- "T@\"NSNumber\",&,N,V_testId"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_testSequencerQueue"
- "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_runningSemaphore"
- "T@\"NSString\",&,N,V_name"
- "TB,V_started"
- "Test result is not for the running test"
- "Test sequencer completed"
- "Test sequencer is already running"
- "[CRDiagnostics][%!s(MISSING)]"
- "_name"
- "_overrides"
- "_resultData"
- "_runningSemaphore"
- "_started"
- "_statusCode"
- "_suiteId"
- "_suiteResult"
- "_testContext"
- "_testId"
- "_testSequence"
- "_testSequencer"
- "_testSequencerQueue"
- "answer %!@(MISSING)"
- "arrayWithObject:"
- "cert_%!d(MISSING): %!@(MISSING)"
- "com.apple.CheckerBoard"
- "com.apple.corerepair.diagnostics-controller"
- "com.apple.corerepair.testSequencer"
- "com.apple.corerepair.testSequencerQueue"
- "com.apple.corerepaird.test"
- "com.apple.private.corerepair.diagnostics-delegate"
- "completeTestSuite:description:"
- "componentsJoinedByString:"
- "dataWithContentsOfFile:options:error:"
- "decodeObjectOfClasses:forKey:"
- "delegate"
- "deviceSupportsRepairBootIntent"
- "dictionaryForKey:"
- "dictionaryWithContentsOfFile:"
- "enableStagedSeal"
- "enabled"
- "endWithCompletionHandler:"
- "endpointURLs"
- "handleResult:"
- "hasMesa"
- "hasMesaDelta"
- "hop0"
- "https://gg.apple.com"
- "https://gs.apple.com"
- "https://humb.apple.com"
- "https://ig.apple.com"
- "https://skl.apple.com"
- "https://sklaxm.apple.com"
- "ignoreStagedData"
- "initTestSequence"
- "initWithCapacity:"
- "initWithDelegate:"
- "initWithID:type:iconLocator:localizedTitle:localizedSubtitle:imageLocators:instructions:instructionsStyle:options:"
- "initWithId:suiteNameLocalizedString:suiteDescriptionLocalizedString:estimatedCompletionTimeLocalizedString:primaryAssetLocator:secondaryAssetLocator:"
- "initWithServiceName:entitlements:"
- "isDataClassSupported:"
- "isEqualToNumber:"
- "isSSRBootIntentSet"
- "libauthinstall_device-1033.40.4"
- "lidar-scanner"
- "localizedDescription"
- "localizedStringWithKey:"
- "needRequestURL"
- "noMovementAttitudeChangeMinThreshold"
- "objectForKey:"
- "overrides"
- "parameters"
- "patchItem"
- "persistedBootIntentReason"
- "ping:"
- "preflightPartSPC"
- "preflightRIK"
- "promptContinue:withContext:"
- "requestAsset:withCompletion:"
- "requestBAACertificates:apticket:proxySettings:"
- "requestSuiteResult:withCompletion:"
- "requestSuiteStart:withCompletionHandler:"
- "requestSuitesAvailableWithCompletionHandler:"
- "requestTermsAndConditionsWithCompletion:"
- "resultData"
- "run:withContext:"
- "runningSemaphore"
- "sceneErrorTimeOut"
- "sceneErrorWarningThreshold"
- "scope"
- "sendTestResult:withCompletion:"
- "sessionTimeOut"
- "setName:"
- "setObject:atIndexedSubscript:"
- "setOverrides:"
- "setReceiver:"
- "setResultData:"
- "setRunningSemaphore:"
- "setStarted:"
- "setStatusCode:"
- "setSuiteId:"
- "setSuiteResult:"
- "setTestContext:"
- "setTestId:"
- "setTestSequence:"
- "setTestSequencer:"
- "setTestSequencerQueue:"
- "shouldRun:"
- "showInstructionalPrompt:withConfirmation:"
- "skipStageEAN"
- "start"
- "startListening"
- "startTest:parameters:"
- "startWithCompletionHandler:"
- "started"
- "stringByAppendingPathComponent:"
- "suiteId"
- "suiteResult"
- "supportHarvestPearl"
- "supportLiDAR"
- "supportPeCoNet"
- "testContext"
- "testId"
- "testIdentifer"
- "testResult:%!@(MISSING)"
- "testSequence"
- "testSequencer"
- "testSequencerQueue"
- "testStatusCode"
- "update:testIndex:testResult:"
- "updateProperties"
- "updateTestSuiteProgress:"
- "userNotMovingTimeout"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@?0@\"NSNumber\"8@\"NSString\"16"
- "v32@0:8@\"ASTTestResult\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSNumber\"16@?<v@?@\"NSNumber\"@\"NSString\"@\"NSString\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"ASTSuiteResult\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v32@?0^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}8@\"NSArray\"16@\"NSError\"24"
- "v40@0:8@16q24@32"

```
