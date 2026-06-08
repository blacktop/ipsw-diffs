## SymptomDiagnosticReporter

> `/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter`

```diff

-411.120.4.0.0
-  __TEXT.__text: 0x85b0
-  __TEXT.__auth_stubs: 0x3f0
+460.0.0.0.0
+  __TEXT.__text: 0x81f8
   __TEXT.__objc_methlist: 0x56c
   __TEXT.__const: 0xac
   __TEXT.__gcc_except_tab: 0xbc
-  __TEXT.__cstring: 0x13ed
+  __TEXT.__cstring: 0x13db
   __TEXT.__oslogstring: 0xf79
-  __TEXT.__unwind_info: 0x2c8
-  __TEXT.__objc_classname: 0x57
-  __TEXT.__objc_methname: 0x1338
-  __TEXT.__objc_methtype: 0x6b0
-  __TEXT.__objc_stubs: 0xb00
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__unwind_info: 0x2b0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xa38
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b8
+  __DATA_CONST.__objc_selrefs: 0x4b0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0x518
-  __AUTH_CONST.__auth_got: 0x208
+  __DATA_CONST.__objc_arraydata: 0x510
+  __DATA_CONST.__got: 0xa0
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x2320
+  __AUTH_CONST.__cfstring: 0x22e0
   __AUTH_CONST.__objc_const: 0x380
-  __AUTH_CONST.__objc_arrayobj: 0x408
+  __AUTH_CONST.__objc_arrayobj: 0x3f0
   __AUTH_CONST.__objc_dictobj: 0x4d8
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0xc0
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 939E9354-BDED-3F1D-85F6-00646497EEB5
-  Functions: 195
-  Symbols:   825
-  CStrings:  859
+  UUID: 06F1FF74-16C9-3A6E-A58C-2BCC1AB308BB
+  Functions: 191
+  Symbols:   824
+  CStrings:  626
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x25
+ _objc_retain_x27
+ _objc_retain_x4
+ _objc_retain_x8
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _objc_msgSend$isEqualToString:
- _objc_retainAutoreleasedReturnValue
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<SDRDiagnosticReporterDelegate>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24d32"
- "@48@0:8@16Q24Q32Q40"
- "@56@0:8@16@24@32@40@48"
- "@64@0:8@16@24@32@40@48@56"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "B32@0:8@16@?24"
- "B40@0:8@16@24@?32"
- "B48@0:8@16@24@32@?40"
- "B48@0:8@16d24@32@?40"
- "B56@0:8@16d24@32@40@?48"
- "B60@0:8@16d24@32@40B48@?52"
- "B64@0:8@16d24@32@40@48@?56"
- "B68@0:8@16d24@32@40@48B56@?60"
- "B80@0:8@16@24d32d40@48@56@64@?72"
- "CaseDampeningExceptions"
- "DiagnosticsServiceInterface"
- "NSObject"
- "Q16@0:8"
- "SDRDiagnosticReporter"
- "T#,R"
- "T@\"<SDRDiagnosticReporterDelegate>\",W,N,V_delegate"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "UTF8String"
- "Vv16@0:8"
- "WiFi Watchdog"
- "^{_NSZone=}16@0:8"
- "_connection"
- "_delegate"
- "_payloadAugmentedWithSandboxExtensionTokensDict:"
- "_queue"
- "actionsDictionary:withIDSDestinations:validFor:"
- "addEntriesFromDictionary:"
- "addObjectsFromArray:"
- "addSignatureContentForSession:key:content:reply:"
- "addToSession:event:payload:reply:"
- "addToSession:events:payload:reply:"
- "allObjects"
- "allowDampeningExceptionFor:"
- "arrayWithObjects:count:"
- "autorelease"
- "boolValue"
- "buildDiagnosticIncidentEventForCaseSignature:handledResult:dampeningResult:closureType:"
- "cancelSession:"
- "caseSummariesListCallbackWithResult:service:caseSummaryType:count:container:reply:"
- "casesListCallbackWithResult:service:identifier:count:container:reply:"
- "checkSignatureValidity:"
- "class"
- "cloudKitUploadDecisionForCaseIdentifiers:reply:"
- "commonPreflightChecksForSignature:payload:callback:"
- "conformsToProtocol:"
- "containsObject:"
- "containsString:"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
- "countByEnumeratingWithState:objects:count:"
- "date"
- "dealloc"
- "debugDescription"
- "defaultManager"
- "delegate"
- "description"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "doubleValue"
- "endSession:"
- "errorWithDomain:code:userInfo:"
- "fileURLWithPath:"
- "getAllDiagnosticCasesWithReply:"
- "getAutoBugCaptureConfiguration:"
- "getCasesListFromIdentifier:count:reply:"
- "getDiagnosticCaseSummariesOfType:reply:"
- "getDiagnosticCaseSummariesWithIdentifiers:reply:"
- "getDiagnosticPayloadsForSignatures:reply:"
- "getExpertSystemsStatus:"
- "getSessionStatisticsWithReply:"
- "groupCaseIdentifierForSignature:reply:"
- "hasPrefix:"
- "hasSuffix:"
- "hash"
- "homeKitResidentDevicesIDSIdentifiersWithReply:"
- "i24@0:8@16"
- "init"
- "initWithDictionary:"
- "initWithMachServiceName:options:"
- "initWithObjectsAndKeys:"
- "initWithQueue:"
- "initialize"
- "intValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isABCEnabled"
- "isEqual:"
- "isEqualToString:"
- "isException:containedInString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isString:inExceptionList:"
- "lastObject"
- "length"
- "listCaseSummariesOfType:fromIdentifier:count:reply:"
- "listCaseSummariesWithIdentifiers:reply:"
- "mutableCopy"
- "newXPCConnection"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectForKeyedSubscript:"
- "parseCaseTriggerResponse:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "proxima"
- "purgeAutoBugCaptureFilesWithSubPaths:reply:"
- "queue"
- "rangeOfString:"
- "release"
- "remoteObjectProxy"
- "remoteObjectProxyWithErrorHandler:"
- "reporterConnectionInterrupted:"
- "reporterConnectionInvalidated:"
- "requestGroupCaseIdentifierForSignature:reply:"
- "resetAPIRateLimit"
- "resetAllWithReply:"
- "resetDailyCaseLimit"
- "resetDiagnosticCaseStorageWithReply:"
- "resetDiagnosticCaseUsageWithReply:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setBasebandChipset:"
- "setDelegate:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setLoggingHandle:"
- "setNPIDevice:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setProductType:"
- "setRemoteObjectInterface:"
- "setWiFiChipset:"
- "setupXPCInterface"
- "signatureWithDomain:type:subType:detectedProcess:triggerThresholdValues:"
- "signatureWithDomain:type:subType:originatingProcess:triggerThreshold:"
- "signatureWithDomain:type:subType:subtypeContext:detectedProcess:triggerThresholdValues:"
- "snapshotWithSignature:delay:events:payload:actions:reply:"
- "snapshotWithSignature:delay:events:payload:actions:wantsRemoteCase:reply:"
- "snapshotWithSignature:delay:events:payload:reply:"
- "snapshotWithSignature:delay:events:payload:wantsRemoteCase:reply:"
- "snapshotWithSignature:duration:event:payload:reply:"
- "snapshotWithSignature:duration:events:payload:actions:reply:"
- "snapshotWithSignature:duration:events:payload:actions:wantsRemoteCase:reply:"
- "snapshotWithSignature:duration:events:payload:reply:"
- "snapshotWithSignature:duration:events:payload:wantsRemoteCase:reply:"
- "snapshotWithSignature:duration:payload:reply:"
- "snapshotWithSignature:withIDSDestinations:validFor:delay:events:payload:actions:reply:"
- "snapshotWithSignature:withIDSDestinations:validFor:duration:events:payload:actions:reply:"
- "startSessionWithSignature:duration:event:payload:reply:"
- "startSessionWithSignature:duration:events:payload:actions:reply:"
- "startSessionWithSignature:duration:events:payload:actions:wantsRemoteCase:reply:"
- "startSessionWithSignature:duration:events:payload:reply:"
- "startSessionWithSignature:duration:events:payload:wantsRemoteCase:reply:"
- "startSessionWithSignature:duration:payload:reply:"
- "startSessionWithSignature:withIDSDestinations:validFor:duration:events:payload:actions:reply:"
- "stringWithUTF8String:"
- "submitDiagnosticIncidentEventForCaseSignature:handledResult:dampeningResult:closureType:"
- "submitRecentCaseSummariesWithCount:reply:"
- "submitRecentCaseSummariesWithIdentifiers:reply:"
- "substringWithRange:"
- "superclass"
- "timeIntervalSince1970"
- "triggerRemoteSessionForSignature:caseGroupID:reply:"
- "triggerRemoteSessionForSignature:groupIdentifier:reply:"
- "uploadCasesWithIdentifiersToCloudKit:"
- "uploadRecentCases:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\">16"
- "v24@0:8@?<v@?@\"NSDictionary\">16"
- "v24@0:8Q16"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\">24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSString\">24"
- "v32@0:8@\"NSArray\"16@?<v@?B>24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@16@?24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?@\"NSString\">24"
- "v40@0:8@\"NSDictionary\"16@\"NSString\"24@?<v@?@\"NSDictionary\">32"
- "v40@0:8@\"NSString\"16Q24@?<v@?@\"NSArray\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@?32"
- "v48@0:8@\"NSString\"16@\"NSArray\"24@\"NSDictionary\"32@?<v@?@\"NSDictionary\">40"
- "v48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSDictionary\"32@?<v@?@\"NSDictionary\">40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSDictionary\">40"
- "v48@0:8@\"NSString\"16@\"NSString\"24Q32@?<v@?@\"NSArray\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24Q32@?40"
- "v48@0:8@16Q24Q32Q40"
- "v64@0:8@16@24@32Q40@48@?56"
- "v68@0:8@\"NSDictionary\"16Q24@\"NSArray\"32@\"NSDictionary\"40@\"NSDictionary\"48B56@?<v@?@\"NSDictionary\">60"
- "v68@0:8@16Q24@32@40@48B56@?60"
- "zone"

```
