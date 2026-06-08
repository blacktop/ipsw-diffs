## LoginPerformanceKit

> `/System/Library/PrivateFrameworks/LoginPerformanceKit.framework/LoginPerformanceKit`

```diff

-3024.0.0.0.0
-  __TEXT.__text: 0x4ed4
-  __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_methlist: 0x358
-  __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0x224
-  __TEXT.__cstring: 0xca5
-  __TEXT.__oslogstring: 0x341
-  __TEXT.__unwind_info: 0x1c0
-  __TEXT.__objc_classname: 0xaf
-  __TEXT.__objc_methname: 0xed7
-  __TEXT.__objc_methtype: 0x15e
-  __TEXT.__objc_stubs: 0xf80
-  __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x378
+3030.0.0.0.0
+  __TEXT.__text: 0x4c30
+  __TEXT.__objc_methlist: 0x368
+  __TEXT.__const: 0xa8
+  __TEXT.__cstring: 0xd04
+  __TEXT.__gcc_except_tab: 0x1fc
+  __TEXT.__oslogstring: 0x353
+  __TEXT.__unwind_info: 0x1a8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x380
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x468
+  __DATA_CONST.__objc_selrefs: 0x470
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__got: 0x110
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x820
+  __AUTH_CONST.__cfstring: 0x8c0
   __AUTH_CONST.__objc_const: 0x760
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x38
   __DATA.__bss: 0x8

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E7E61B22-5317-3249-899E-35A6FB298701
-  Functions: 104
-  Symbols:   531
-  CStrings:  376
+  UUID: 64770947-3E72-3280-A0F9-BB79729626B0
+  Functions: 103
+  Symbols:   532
+  CStrings:  187
 
Symbols:
+ +[LPKPerformanceTestIntermediary _startUserSwitchTestForType:count:username:password:loginDelay:logoutDelay:isPerformanceTest:scheduleOnly:skipLogoutWhenCompletes:]
+ +[LPKPerformanceTestIntermediary scheduleUserSwitchTestForType:count:username:password:loginDelay:logoutDelay:skipLogoutWhenCompletes:]
+ -[LPKUserSwitchCycleController _loginAccount:password:localLoginOnly:isTemporarySession:delay:]
+ -[LPKUserSwitchCycleController startUserSwitchWithType:count:username:password:loginDelay:logoutDelay:scheduleOnly:]
+ GCC_except_table4
+ ___116-[LPKUserSwitchCycleController startUserSwitchWithType:count:username:password:loginDelay:logoutDelay:scheduleOnly:]_block_invoke
+ ___164+[LPKPerformanceTestIntermediary _startUserSwitchTestForType:count:username:password:loginDelay:logoutDelay:isPerformanceTest:scheduleOnly:skipLogoutWhenCompletes:]_block_invoke
+ ___164+[LPKPerformanceTestIntermediary _startUserSwitchTestForType:count:username:password:loginDelay:logoutDelay:isPerformanceTest:scheduleOnly:skipLogoutWhenCompletes:]_block_invoke_2
+ ___61-[LPKUserSwitchCycleController triggerTestUserSwitchIfNeeded]_block_invoke.55
+ ___95-[LPKUserSwitchCycleController _loginAccount:password:localLoginOnly:isTemporarySession:delay:]_block_invoke
+ ___95-[LPKUserSwitchCycleController _loginAccount:password:localLoginOnly:isTemporarySession:delay:]_block_invoke.58
+ ___95-[LPKUserSwitchCycleController _loginAccount:password:localLoginOnly:isTemporarySession:delay:]_block_invoke.58.cold.1
+ ___95-[LPKUserSwitchCycleController _loginAccount:password:localLoginOnly:isTemporarySession:delay:]_block_invoke.58.cold.2
+ ___95-[LPKUserSwitchCycleController _loginAccount:password:localLoginOnly:isTemporarySession:delay:]_block_invoke_2
+ ___block_descriptor_57_e8_32s40s48r_e20_v20?0B8"NSError"12lr48l8s32l8s40l8
+ ___block_descriptor_58_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_66_e8_32s40s48w_e20_v20?0B8"NSError"12lw48l8s32l8s40l8
+ ___block_descriptor_97_e8_32s40s48s56r_e20_v20?0B8"NSError"12ls32l8s40l8r56l8s48l8
+ ___block_literal_global.92
+ _kLocalUserSwitchTestSkipLogoutWhenCompletesKey
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_loginAccount:password:localLoginOnly:isTemporarySession:delay:
+ _objc_msgSend$_startUserSwitchTestForType:count:username:password:loginDelay:logoutDelay:isPerformanceTest:scheduleOnly:skipLogoutWhenCompletes:
+ _objc_msgSend$forceLoggingInAppleID:password:localLoginOnly:isTemporarySession:completionHandler:
+ _objc_msgSend$triggerLocalUserSwitchTestForType:count:username:password:loginDelay:logoutDelay:scheduleOnly:completionHandler:
+ _objc_retain_x23
+ _objc_retain_x25
+ _objc_retain_x3
+ _objc_retain_x4
- +[LPKPerformanceTestIntermediary _startUserSwitchTestForType:count:username:password:loginDelay:logoutDelay:isPerformanceTest:]
- -[LPKUserSwitchCycleController _loginAccount:password:localLoginOnly:delay:]
- -[LPKUserSwitchCycleController startUserSwitchWithType:count:username:password:loginDelay:logoutDelay:]
- GCC_except_table3
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- ___103-[LPKUserSwitchCycleController startUserSwitchWithType:count:username:password:loginDelay:logoutDelay:]_block_invoke
- ___127+[LPKPerformanceTestIntermediary _startUserSwitchTestForType:count:username:password:loginDelay:logoutDelay:isPerformanceTest:]_block_invoke
- ___127+[LPKPerformanceTestIntermediary _startUserSwitchTestForType:count:username:password:loginDelay:logoutDelay:isPerformanceTest:]_block_invoke_2
- ___61-[LPKUserSwitchCycleController triggerTestUserSwitchIfNeeded]_block_invoke.46
- ___76-[LPKUserSwitchCycleController _loginAccount:password:localLoginOnly:delay:]_block_invoke
- ___76-[LPKUserSwitchCycleController _loginAccount:password:localLoginOnly:delay:]_block_invoke.49
- ___76-[LPKUserSwitchCycleController _loginAccount:password:localLoginOnly:delay:]_block_invoke.49.cold.1
- ___76-[LPKUserSwitchCycleController _loginAccount:password:localLoginOnly:delay:]_block_invoke.49.cold.2
- ___76-[LPKUserSwitchCycleController _loginAccount:password:localLoginOnly:delay:]_block_invoke_2
- ___block_descriptor_56_e8_32s40s48r_e20_v20?0B8"NSError"12lr48l8s32l8s40l8
- ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_65_e8_32s40s48w_e20_v20?0B8"NSError"12lw48l8s32l8s40l8
- ___block_descriptor_96_e8_32s40s48s56r_e20_v20?0B8"NSError"12ls32l8s40l8r56l8s48l8
- ___block_literal_global.93
- _objc_msgSend$_loginAccount:password:localLoginOnly:delay:
- _objc_msgSend$_startUserSwitchTestForType:count:username:password:loginDelay:logoutDelay:isPerformanceTest:
- _objc_msgSend$forceLoggingInAppleID:password:localLoginOnly:completionHandler:
- _objc_msgSend$triggerLocalUserSwitchTestForType:count:username:password:loginDelay:logoutDelay:completionHandler:
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x28
CStrings:
+ "-[LPKUserSwitchCycleController _loginAccount:password:localLoginOnly:isTemporarySession:delay:]_block_invoke_2"
+ "LPKLocalUserSwitchTestSkipLogoutWhenCompletes"
+ "NO"
+ "Scheduling"
+ "Starting"
+ "Starting user switch cycle with type: %lu for %ld times, scheduleOnly: %@"
+ "Test states stored\n%@ login & logout for account: %@..."
+ "YES"
- "-[LPKUserSwitchCycleController _loginAccount:password:localLoginOnly:delay:]_block_invoke_2"
- ".cxx_destruct"
- "@\"<LPKUserSwitchCycleResponder>\""
- "@\"NSDate\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8q16@24"
- "@40@0:8@16Q24q32"
- "B"
- "B16@0:8"
- "B64@0:8Q16q24@32@40q48q56"
- "B68@0:8Q16q24@32@40q48q56B64"
- "JSONObjectWithData:options:error:"
- "LPKLoginEvent"
- "LPKLogoutEvent"
- "LPKPerfResultAnalyzer"
- "LPKPerfResultEntry"
- "LPKPerformanceTestIntermediary"
- "LPKSignpostEvent"
- "LPKUserSwitchCycleController"
- "LPKUserSwitchEvent"
- "Q16@0:8"
- "Starting user switch cycle with type: %lu for %ld times"
- "T@\"<LPKUserSwitchCycleResponder>\",W,N,V_delegate"
- "T@\"NSDate\",&,N,V_endDate"
- "T@\"NSDate\",&,N,V_startDate"
- "T@\"NSMutableArray\",&,N,V_entryValues"
- "T@\"NSMutableDictionary\",&,N,V_signposts"
- "T@\"NSString\",C,N,V_entryName"
- "T@\"NSString\",C,N,V_name"
- "T@\"NSString\",C,N,V_processName"
- "TB,N,V_needsReCalculation"
- "Td,N,V_duration"
- "Td,R,N,V_meanValue"
- "Td,R,N,V_medianValue"
- "Test states stored\nStarting login & logout for account: %@..."
- "UTF8String"
- "_abstractUserSwitchsFromTheEnd:userSwitches:"
- "_calculateDurationIfNeeded"
- "_clearOutLocalPerfTestDefaults"
- "_currentEnvironment"
- "_delegate"
- "_disableKtrace"
- "_dumpKtraceResult"
- "_duration"
- "_durationFromString:"
- "_enableKtrace"
- "_endDate"
- "_entryName"
- "_entryValues"
- "_fixTestStatesForRetry"
- "_generateSharedipadTraceHelperCommand"
- "_isLoginSession"
- "_loginAccount:password:localLoginOnly:delay:"
- "_meanValue"
- "_medianValue"
- "_name"
- "_needsReCalculation"
- "_perfResultsFromUserSwitches:"
- "_populateMigratorsData:"
- "_processName"
- "_reCalculateValuesIfNeeded"
- "_removeStoredValues"
- "_scheduleRetryWithTimeout:"
- "_setUserSwitchDestinationExpectation:retryIfFailed:completionHandler:"
- "_signposts"
- "_startDate"
- "_startUserSwitchTestForType:count:username:password:loginDelay:logoutDelay:isPerformanceTest:"
- "_triggerFastLogoutWithDelay:"
- "_triggerFullLogoutWithDelay:"
- "_updateLocalPerfTestCycleCount:"
- "_validateUserSwitchExpectation"
- "activateStreamFromDate:"
- "addEntryValue:"
- "addObject:"
- "allValues"
- "analyzePerformanceTestResult:type:count:"
- "appendString:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "boolValue"
- "clearKeys:completionHandler:"
- "code"
- "compare:"
- "componentsSeparatedByString:"
- "composedMessage"
- "containsString:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentUser"
- "d"
- "d16@0:8"
- "d24@0:8@16"
- "dataWithContentsOfFile:"
- "date"
- "dateFromString:"
- "dateWithTimeIntervalSince1970:"
- "defaultManager"
- "delegate"
- "deleteUser:completionHandler:"
- "dictionaryWithObjects:forKeys:count:"
- "disableRestrictionlessLoginWithCompletionHandler:"
- "domain"
- "doubleValue"
- "duration"
- "enableRestrictionlessLoginWithCompletionHandler:"
- "endDate"
- "endPerformanceTestAndDumpResults"
- "endUserSwitchTest"
- "entryName"
- "entryValues"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateMatchesInString:options:range:usingBlock:"
- "enumerateObjectsUsingBlock:"
- "fileExistsAtPath:"
- "firstObject"
- "forceLoggingInAppleID:password:localLoginOnly:completionHandler:"
- "init"
- "initWithDelegate:"
- "initWithSource:"
- "integerValue"
- "interruptLocalUserSwitchTest"
- "isEqualToString:"
- "isInternalBuild"
- "isLoginUser"
- "lastObject"
- "length"
- "localStore"
- "logErrorEventForTopic:reason:error:details:"
- "logoutWithLogoutType:completionHandler:"
- "meanValue"
- "medianValue"
- "name"
- "needsReCalculation"
- "numberOfRanges"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "performanceTestDidFinishSuccessfully"
- "performanceTestWillTerminate"
- "predicateWithFormat:"
- "prepareWithCompletionHandler:"
- "processName"
- "q16@0:8"
- "rangeAtIndex:"
- "regularExpressionWithPattern:options:error:"
- "retrieveValueForKey:"
- "saveKeyValuePairs:completionHandler:"
- "saveKeyValuePairs:error:"
- "setDateFormat:"
- "setDelegate:"
- "setDuration:"
- "setEndDate:"
- "setEntryName:"
- "setEntryValues:"
- "setEventHandler:"
- "setFilterPredicate:"
- "setFlags:"
- "setInvalidationHandler:"
- "setName:"
- "setNeedsReCalculation:"
- "setObject:forKeyedSubscript:"
- "setProcessName:"
- "setSignposts:"
- "setStartDate:"
- "setUsername:"
- "sharedController"
- "sharedManager"
- "sharedStorage"
- "signposts"
- "sortUsingComparator:"
- "sortedArrayUsingComparator:"
- "startDate"
- "startPerformanceTestForType:count:username:password:loginDelay:logoutDelay:"
- "startUserSwitchTestForType:count:username:password:loginDelay:logoutDelay:"
- "startUserSwitchWithType:count:username:password:loginDelay:logoutDelay:"
- "stringWithFormat:"
- "subarrayWithRange:"
- "substringToIndex:"
- "substringWithRange:"
- "timeIntervalSince1970"
- "timeIntervalSinceDate:"
- "triggerLocalUserSwitchTestForType:count:username:password:loginDelay:logoutDelay:completionHandler:"
- "triggerTestUserSwitchIfNeeded"
- "type"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "userExists:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v36@0:8Q16B24@?28"
- "v44@0:8@16@24B32d36"

```
