## CPMS

> `/System/Library/PrivateFrameworks/CPMS.framework/CPMS`

```diff

-1035.100.47.0.0
-  __TEXT.__text: 0x6420
-  __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x3ec
-  __TEXT.__const: 0x8c
-  __TEXT.__gcc_except_tab: 0x14c
-  __TEXT.__cstring: 0x97b
-  __TEXT.__oslogstring: 0xaad
-  __TEXT.__ustring: 0x1a6
-  __TEXT.__unwind_info: 0x1c8
-  __TEXT.__objc_classname: 0x50
-  __TEXT.__objc_methname: 0x942
-  __TEXT.__objc_methtype: 0x3d0
-  __TEXT.__objc_stubs: 0x720
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x170
+1177.0.0.502.4
+  __TEXT.__text: 0x8b20
+  __TEXT.__objc_methlist: 0x4ac
+  __TEXT.__const: 0x9c
+  __TEXT.__gcc_except_tab: 0x170
+  __TEXT.__cstring: 0xc75
+  __TEXT.__oslogstring: 0x1137
+  __TEXT.__ustring: 0x220
+  __TEXT.__unwind_info: 0x1f0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1a8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x310
+  __DATA_CONST.__objc_selrefs: 0x390
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x240
+  __DATA_CONST.__got: 0x90
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0xf60
-  __AUTH_CONST.__objc_const: 0x580
+  __AUTH_CONST.__cfstring: 0x1120
+  __AUTH_CONST.__objc_const: 0x660
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_ivar: 0x30
+  __AUTH_CONST.__auth_got: 0x270
+  __DATA.__objc_ivar: 0x40
   __DATA.__data: 0xc0
   __DATA.__common: 0x1
   __DATA.__bss: 0x10

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9CF8D579-AE75-3630-82F3-A282DBFB206A
-  Functions: 133
-  Symbols:   522
-  CStrings:  505
+  UUID: A6B47FD3-6317-3C50-9163-6FE8C5AA9D6F
+  Functions: 181
+  Symbols:   645
+  CStrings:  396
 
Symbols:
+ -[CPMSAgent acknowledgePowerBudget:error:]
+ -[CPMSAgent acknowledgePowerBudget:error:].cold.1
+ -[CPMSAgent acknowledgePowerBudget:error:].cold.2
+ -[CPMSAgent acknowledgePowerBudget:error:].cold.3
+ -[CPMSAgent acknowledgePowerBudget:error:].cold.4
+ -[CPMSAgent acknowledgePowerBudget:error:].cold.5
+ -[CPMSAgent acknowledgePowerBudget:error:].cold.6
+ -[CPMSAgent acknowledgePowerBudget:error:].cold.7
+ -[CPMSAgent acknowledgePowerBudget:error:].cold.8
+ -[CPMSAgent acknowledgePowerBudget:error:].cold.9
+ -[CPMSAgent copyPowerBudgetForRequest:error:]
+ -[CPMSAgent copyPowerBudgetForRequest:error:].cold.1
+ -[CPMSAgent copyPowerBudgetForRequest:error:].cold.2
+ -[CPMSAgent copyPowerBudgetForRequest:error:].cold.3
+ -[CPMSAgent copyPowerBudgetForRequest:error:].cold.4
+ -[CPMSAgent copyPowerBudgetForRequest:error:].cold.5
+ -[CPMSAgent copyPowerBudgetForRequest:error:].cold.6
+ -[CPMSAgent copyPowerBudgetForRequest:error:].cold.7
+ -[CPMSAgent copyPowerBudgetForRequest:error:].cold.8
+ -[CPMSAgent copyPowerBudgetForRequest:error:].cold.9
+ -[CPMSAgent getClientMinMaxPowerPolicy:error:]
+ -[CPMSAgent getClientMinMaxPowerPolicy:error:].cold.1
+ -[CPMSAgent init].cold.5
+ -[CPMSAgent multiClientGroups]
+ -[CPMSAgent registerClientWithDescription:clientIdToDescriptionMap:]
+ -[CPMSAgent registerClientWithDescription:clientIdToDescriptionMap:].cold.1
+ -[CPMSAgent registerClientWithDescription:clientIdToDescriptionMap:].cold.2
+ -[CPMSAgent registerClientWithDescription:clientIdToDescriptionMap:].cold.3
+ -[CPMSAgent registerClientWithDescription:clientIdToDescriptionMap:].cold.4
+ -[CPMSAgent registerClientWithDescription:clientIdToDescriptionMap:].cold.5
+ -[CPMSAgent registerClientWithDescription:clientIdToDescriptionMap:].cold.6
+ -[CPMSAgent registerClientWithDescription:clientIdToDescriptionMap:].cold.7
+ -[CPMSAgent sanityCheckClientDescription:].cold.20
+ -[CPMSAgent sanityCheckClientDescription:].cold.21
+ -[CPMSAgent setMultiClientGroups:]
+ -[CPMSClientDescription isMultiClientEnabled]
+ -[CPMSClientDescription multiClientGroupID]
+ -[CPMSClientDescription multiClientNotificationCallback]
+ -[CPMSClientDescription setIsMultiClientEnabled:]
+ -[CPMSClientDescription setMultiClientGroupID:]
+ -[CPMSClientDescription setMultiClientNotificationCallback:]
+ GCC_except_table13
+ GCC_except_table23
+ GCC_except_table26
+ _OBJC_IVAR_$_CPMSAgent._multiClientGroups
+ _OBJC_IVAR_$_CPMSClientDescription._isMultiClientEnabled
+ _OBJC_IVAR_$_CPMSClientDescription._multiClientGroupID
+ _OBJC_IVAR_$_CPMSClientDescription._multiClientNotificationCallback
+ _PPMCallbackHandler.cold.5
+ _PPMCallbackHandler.cold.6
+ _PPMCallbackHandler.cold.7
+ _PPMCallbackHandler.cold.8
+ _PPMCallbackHandler.cold.9
+ ___block_literal_global.53
+ ___block_literal_global.58
+ _getAllocatedPowerBudgetParams
+ _getAllocatedPowerBudgetParams.cold.1
+ _getAllocatedPowerBudgetParams.cold.2
+ _getClientAllocatedBudget
+ _getClientAllocatedBudget.cold.1
+ _getClientAllocatedBudget.cold.2
+ _getClientState
+ _getClientState.cold.1
+ _kCPMSMaxPolicyPower
+ _kCPMSMinPolicyPower
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$array
+ _objc_msgSend$integerValue
+ _objc_msgSend$isMultiClientEnabled
+ _objc_msgSend$multiClientGroupID
+ _objc_msgSend$multiClientGroups
+ _objc_msgSend$multiClientNotificationCallback
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$setMultiClientGroupID:
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_retain_x8
+ _setAckClientBudgetParams
+ _setAckClientBudgetParams.cold.1
+ _setAckClientBudgetParams.cold.2
+ _setPowerRequestBudgetParams
+ _setPowerRequestBudgetParams.cold.1
+ _setPowerRequestBudgetParams.cold.2
- -[CPMSAgent acknowledgePowerBudget:forClientId:error:].cold.3
- -[CPMSAgent acknowledgePowerBudget:forClientId:error:].cold.4
- -[CPMSAgent copyPowerBudgetForRequest:forClient:withPowerProfile:error:].cold.4
- -[CPMSAgent copyPowerBudgetForRequest:forClient:withPowerProfile:error:].cold.5
- GCC_except_table17
- GCC_except_table19
- GCC_except_table82
- GCC_except_table83
- GCC_except_table84
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- ___block_literal_global.41
- ___block_literal_global.52
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
CStrings:
+ "$"
+ "<Error> Ack failure for CPMS, userclient return 0x%08x\n"
+ "<Error> Invalid Input arguments\n"
+ "<Error> Invalid client=%lu passed\n"
+ "<Error> Invalid input args\n"
+ "<Error> Invalid input argument \n"
+ "<Error> Invalid input parameters for %s"
+ "<Error> Key in clientIdToBudget is not NSNumber"
+ "<Error> Key in clientIdToRequestedBudget is not NSNumber"
+ "<Error> Multiclient Array alloc failed\n"
+ "<Error> Nil clientIdToDescriptionMap object\n"
+ "<Error> Nil multi-client notification callback\n"
+ "<Error> allocation ptr is null in %s"
+ "<Error> budget in clientIdToBudget is not NSDictionary for key=%u"
+ "<Error> cID ptr is null in %s"
+ "<Error> failed to setAckClientBudgetParams\n"
+ "<Error> getAllocatedPowerBudgetParams call failed"
+ "<Error> getClientMinMaxPowerPolicy call to PPM failed with error %d"
+ "<Error> getClientState failed for clientId %lu ret 0x%08x"
+ "<Error> groups ptr is null in %s"
+ "<Error> index for ppmClientDesc exceeds MAX_USER_MULTI_CLIENT_PER_GROUP\n"
+ "<Error> index is greater than MAX_USER_MULTI_CLIENT_PER_GROUP"
+ "<Error> input budget is null for key=%u"
+ "<Error> input clientIdToBudget is null"
+ "<Error> input clientIdToRequestedBudget is null"
+ "<Error> invalid numberOfTimeScales=%d in allocatedBudget\n"
+ "<Error> multiClientIds ptr is null in %s"
+ "<Error> numTimeScales greater than CPMSPPMTimeScaleCount for clientId=%u level=%d\n"
+ "<Error> requestedBudget in clientIdToRequestedBudget is not NSDictionary for key=%u"
+ "<Error> requestedBudget is Null for key=%u"
+ "<Error> setPowerRequestBudget call failed"
+ "<Info> CPMS clientId %ld requested budget %{public}s granted budget %{public}s"
+ "<Notice> Ack from CPMS clientId %ld. Budgets: %{public}s"
+ "<Notice> Sending budget notification for CPMS clientId %lu"
+ "<Notice> Sending multi client budget notification for CPMS clientId %lu"
+ "BatteryIndex"
+ "EstimatedR0123 (Ω)"
+ "EstimatedR4 (Ω)"
+ "ForceBatteryModelFallback"
+ "ImpedanceRCFreq1 (rad/s)"
+ "ImpedanceRCFreq2 (rad/s)"
+ "ImpedanceRCFreq3 (rad/s)"
+ "ImpedanceRCFreq4 (rad/s)"
+ "SSS FilteredResidualScore"
+ "SSS FilteredTempDiff (°C)"
+ "SSS Flag"
+ "SSS FusionFactor"
+ "SSS Pb (W)"
+ "SSS PredictedVoltageDroop (V)"
+ "SystemStressSignal"
+ "assertion failure: Ack failure for CPMS, userclient return 0x%08x\n"
+ "assertion failure: Nil clientIdToDescriptionMap object\n"
+ "assertion failure: Nil multi-client notification callback\n"
+ "assertion failure: failed to setAckClientBudgetParams\n"
+ "cpms_maxPwr"
+ "cpms_minPwr"
+ "dummy2"
+ "inductive"
+ "rtmu"
+ "systemStressLevel"
+ "void PPMCallbackHandler(void *, io_service_t, uint32_t, void *)"
+ "void getClientAllocatedBudget(CPMSClientDescription *__strong, CPMSAgent *__strong, NSMutableDictionary *__strong, CPMSPPMClientState *)"
+ "void getMultiClientAllocatedBudget(NSSet *__strong, CPMSClientDescription *__strong, NSMutableDictionary *__strong, CPMSAgent *__strong, CPMSPPMClientState *)"
- "#"
- "#16@0:8"
- ".cxx_destruct"
- "<Info> Sending budget notification for CPMS clientId %lu"
- "@\"NSDictionary\""
- "@\"NSDictionary\"32@0:8q16^@24"
- "@\"NSDictionary\"40@0:8@\"NSDictionary\"16q24^@32"
- "@\"NSDictionary\"48@0:8@\"NSDictionary\"16q24@\"NSDictionary\"32^@40"
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@20@0:8c16"
- "@24@0:8:16"
- "@24@0:8^i16"
- "@24@0:8^{CPMSPPMControlStateSnapshot=Q[7f]ifffff[22{CPMSPPMPowerBudget=CC[3{CPMSPPMPowerLevelScalar=cI}]}][22{CPMSPPMPowerBudget=CC[3{CPMSPPMPowerLevelScalar=cI}]}][8I]C[3i]ICIBfQQQQ[8f]iiiB}16"
- "@24@0:8^{CPMSPPMPowerBudget=CC[3{CPMSPPMPowerLevelScalar=cI}]}16"
- "@32@0:8:16@24"
- "@32@0:8q16^@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16q24^@32"
- "@48@0:8@16q24@32^@40"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8q16"
- "B32@0:8@\"CPMSClientDescription\"16^@24"
- "B32@0:8@16^@24"
- "B40@0:8@\"NSDictionary\"16q24^@32"
- "B40@0:8@16q24^@32"
- "C24@0:8q16"
- "CPMSAgent"
- "CPMSAgentProtocol"
- "CPMSClientDescription"
- "CPMSClientIdToPPMClientId:"
- "CPMSPowerTimeScaleToPPMIndex:"
- "CPMSStateReader"
- "I"
- "I16@0:8"
- "ImpedanceRCFreq1 (Hz)"
- "ImpedanceRCFreq2 (Hz)"
- "ImpedanceRCFreq3 (Hz)"
- "ImpedanceRCFreq4 (Hz)"
- "NSObject"
- "PPMIndexToCPMSPowerTimeScale:"
- "Q16@0:8"
- "T#,R"
- "T@\"NSDictionary\",&,N,V_powerLevels"
- "T@\"NSMutableSet\",&,V_clientSet"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@?,C,N,V_getCurrentPower"
- "T@?,C,N,V_notificationCallback"
- "TB,N,V_isContinuous"
- "TI,N,V_powerBudgetUpdateMinimumPeriod"
- "TI,V_connect"
- "TQ,R"
- "Tq,N,V_clientId"
- "UTF8String"
- "Vv16@0:8"
- "^{IONotificationPort=}"
- "^{_NSZone=}16@0:8"
- "_clientId"
- "_clientSet"
- "_connect"
- "_getCurrentPower"
- "_isContinuous"
- "_notificationCallback"
- "_notificationPort"
- "_notificationQueue"
- "_powerBudgetUpdateMinimumPeriod"
- "_powerLevels"
- "_ppmService"
- "_timeScalesSet"
- "acknowledgePowerBudget:forClientId:error:"
- "addObject:"
- "anyObject"
- "assertion failure: Ack called on unregistered CPMS clientId %lu\n"
- "autorelease"
- "c24@0:8@16"
- "cStringUsingEncoding:"
- "class"
- "clientId"
- "clientSet"
- "conformsToProtocol:"
- "connect"
- "containsObject:"
- "copy"
- "copyCPMSControlStateSnapshots"
- "copyCPMSPmaxState:"
- "copyDefaultPowerProfileForClient:error:"
- "copyPowerBudgetForRequest:forClient:error:"
- "copyPowerBudgetForRequest:forClient:withPowerProfile:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dateWithTimeIntervalSince1970:"
- "dealloc"
- "debugDescription"
- "description"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "errorWithDomain:code:userInfo:"
- "filteredSetUsingPredicate:"
- "getCPMSControlStateSnapshotDictionary:"
- "getCurrentPower"
- "getPowerBudgetDictionary:"
- "hasPrefix:"
- "hash"
- "init"
- "initWithCapacity:"
- "initWithObjectsAndKeys:"
- "intValue"
- "isCPMSSupported"
- "isCPMSSupportedForAnyClient"
- "isCPMSSupportedForClient:"
- "isClientIdValid:"
- "isContinuous"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isThermalOnlyDevice"
- "log"
- "notificationCallback"
- "numberWithBool:"
- "numberWithChar:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithUnsignedChar:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedLongLong:"
- "objectAtIndex:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "powerBudgetUpdateMinimumPeriod"
- "powerLevels"
- "predicateWithFormat:"
- "q"
- "q16@0:8"
- "registerClientWithDescription:error:"
- "registerForNotifications"
- "release"
- "requestPowerBudget:forClient:error:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "sanityCheckClientDescription:"
- "self"
- "setClientId:"
- "setClientSet:"
- "setConnect:"
- "setGetCurrentPower:"
- "setIsContinuous:"
- "setNotificationCallback:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPowerBudgetUpdateMinimumPeriod:"
- "setPowerLevels:"
- "setWithObjects:"
- "sharedCPMSAgent"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "timescaleDisplayName:"
- "unsignedIntValue"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8q16"
- "valueForKey:"
- "zone"

```
