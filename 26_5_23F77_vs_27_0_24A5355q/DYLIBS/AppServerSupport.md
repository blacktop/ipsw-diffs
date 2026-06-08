## AppServerSupport

> `/System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport`

```diff

-3102.120.13.0.0
-  __TEXT.__text: 0x6ef0
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__objc_methlist: 0x994
+3295.0.0.502.1
+  __TEXT.__text: 0x7d60
+  __TEXT.__objc_methlist: 0xb2c
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x52a
+  __TEXT.__cstring: 0x63c
   __TEXT.__oslogstring: 0xdd6
-  __TEXT.__unwind_info: 0x218
-  __TEXT.__objc_classname: 0xe7
-  __TEXT.__objc_methname: 0x18eb
-  __TEXT.__objc_methtype: 0x3b7
-  __TEXT.__objc_stubs: 0xa20
-  __DATA_CONST.__got: 0xc0
+  __TEXT.__unwind_info: 0x1f0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x68
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x10
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x610
+  __DATA_CONST.__objc_selrefs: 0x680
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x308
+  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__got: 0xc8
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x460
-  __AUTH_CONST.__objc_const: 0x1598
+  __AUTH_CONST.__cfstring: 0x580
+  __AUTH_CONST.__objc_const: 0x1840
   __AUTH_CONST.__objc_intobj: 0x18
-  __DATA.__objc_ivar: 0x100
-  __DATA.__data: 0xc0
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__objc_ivar: 0x120
+  __DATA.__data: 0x1e0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x280
-  __DATA_DIRTY.__bss: 0x18
+  __DATA_DIRTY.__objc_data: 0x2d0
+  __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3EA5FE3E-A610-3E1E-A303-E6C756AB4522
-  Functions: 231
-  Symbols:   873
-  CStrings:  585
+  UUID: FE8DCA43-D251-3A11-89F5-F13CB2FBFFDA
+  Functions: 200
+  Symbols:   805
+  CStrings:  221
 
Symbols:
+ +[OSLaunchdDeveloperToolsOptions supportsSecureCoding]
+ +[OSLaunchdDomain domainForBackgroundUser:]
+ -[OSLaunchdDeveloperToolsOptions addressSanitizer]
+ -[OSLaunchdDeveloperToolsOptions copyWithZone:]
+ -[OSLaunchdDeveloperToolsOptions description]
+ -[OSLaunchdDeveloperToolsOptions encodeWithCoder:]
+ -[OSLaunchdDeveloperToolsOptions initWithCoder:]
+ -[OSLaunchdDeveloperToolsOptions isEqual:]
+ -[OSLaunchdDeveloperToolsOptions mtAddressSanitizer]
+ -[OSLaunchdDeveloperToolsOptions setAddressSanitizer:]
+ -[OSLaunchdDeveloperToolsOptions setMtAddressSanitizer:]
+ -[OSLaunchdDeveloperToolsOptions setThreadSanitizer:]
+ -[OSLaunchdDeveloperToolsOptions setUndefinedBehaviorSanitizer:]
+ -[OSLaunchdDeveloperToolsOptions threadSanitizer]
+ -[OSLaunchdDeveloperToolsOptions toDictionary]
+ -[OSLaunchdDeveloperToolsOptions undefinedBehaviorSanitizer]
+ -[OSLaunchdDomain handle]
+ -[OSLaunchdDomain type]
+ -[OSLaunchdJobInstanceProperties developerToolsOptions]
+ -[OSLaunchdJobInstanceProperties setDeveloperToolsOptions:]
+ -[OSLaunchdJobInstanceProperties setSpawnConstraint:]
+ -[OSLaunchdJobInstanceProperties spawnConstraint]
+ -[OSLaunchdJobProperties conclave]
+ -[OSLaunchdJobProperties developerToolsOptions]
+ -[OSLaunchdJobProperties setConclave:]
+ -[OSLaunchdJobProperties setDeveloperToolsOptions:]
+ _OBJC_CLASS_$_OSLaunchdDeveloperToolsOptions
+ _OBJC_IVAR_$_OSLaunchdDeveloperToolsOptions._addressSanitizer
+ _OBJC_IVAR_$_OSLaunchdDeveloperToolsOptions._mtAddressSanitizer
+ _OBJC_IVAR_$_OSLaunchdDeveloperToolsOptions._threadSanitizer
+ _OBJC_IVAR_$_OSLaunchdDeveloperToolsOptions._undefinedBehaviorSanitizer
+ _OBJC_IVAR_$_OSLaunchdJobInstanceProperties._developerToolsOptions
+ _OBJC_IVAR_$_OSLaunchdJobInstanceProperties._spawnConstraint
+ _OBJC_IVAR_$_OSLaunchdJobProperties._conclave
+ _OBJC_IVAR_$_OSLaunchdJobProperties._developerToolsOptions
+ _OBJC_METACLASS_$_OSLaunchdDeveloperToolsOptions
+ __MergedGlobals
+ __OBJC_$_CLASS_METHODS_OSLaunchdDeveloperToolsOptions
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_CLASS_PROP_LIST_OSLaunchdDeveloperToolsOptions
+ __OBJC_$_INSTANCE_METHODS_OSLaunchdDeveloperToolsOptions
+ __OBJC_$_INSTANCE_VARIABLES_OSLaunchdDeveloperToolsOptions
+ __OBJC_$_PROP_LIST_OSLaunchdDeveloperToolsOptions
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_CLASS_PROTOCOLS_$_OSLaunchdDeveloperToolsOptions
+ __OBJC_CLASS_RO_$_OSLaunchdDeveloperToolsOptions
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_METACLASS_RO_$_OSLaunchdDeveloperToolsOptions
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ ___64-[OSLaunchdJob _setupMonitorSourceWithPort:onQueue:withHandler:]_block_invoke.88
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$developerToolsOptions
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$numberWithUnsignedChar:
+ _objc_msgSend$spawnConstraint
+ _objc_msgSend$toDictionary
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x24
+ _objc_retain_x3
- +[LASSProperties4RB _propertiesFromAttrs:].cold.1
- +[LASSProperties4RB _propertiesFromAttrs:].cold.2
- +[LASSProperties4RB propertiesForJob:error:].cold.1
- +[LASSProperties4RB propertiesForJob:error:].cold.2
- +[LASSProperties4RB propertiesForJob:error:].cold.3
- +[LASSProperties4RB propertiesForPid:error:].cold.1
- +[OSLaunchdJob _createJobFromReplyHandle:].cold.1
- +[OSLaunchdJob _handlesToJobs:].cold.1
- +[OSLaunchdJob _handlesToJobs:].cold.2
- +[OSLaunchdJob _submitExtension:overlay:domain:error:].cold.1
- +[OSLaunchdJob _submitExtension:overlay:domain:error:].cold.2
- +[OSLaunchdJob copyJobWithHandle:].cold.1
- +[OSLaunchdJob copyJobWithHandle:].cold.2
- +[OSLaunchdJob copyJobWithHandle:].cold.3
- +[OSLaunchdJob copyJobWithPid:].cold.1
- +[OSLaunchdJob copyJobsManagedBy:error:].cold.1
- +[OSLaunchdJob copyJobsManagedBy:error:].cold.2
- +[OSLaunchdJob jobInfoFromMessage:].cold.1
- +[OSLaunchdJob jobInfoFromMessage:].cold.2
- +[OSLaunchdJob jobInfoFromMessage:].cold.3
- +[OSLaunchdJob jobInfoFromMessage:].cold.4
- +[OSLaunchdJob jobStateFromMessage:].cold.1
- +[OSLaunchdJob submitAll:error:].cold.1
- -[OSLaunchdJob _initWithHandle:].cold.1
- -[OSLaunchdJob _newSubmitRequest].cold.1
- -[OSLaunchdJob _newSubmitRequest].cold.2
- -[OSLaunchdJob _populateHandle:].cold.1
- -[OSLaunchdJob _populateHandle:].cold.2
- -[OSLaunchdJob _setupMonitorSourceWithPort:onQueue:withHandler:].cold.1
- -[OSLaunchdJob _setupMonitorSourceWithPort:onQueue:withHandler:].cold.2
- -[OSLaunchdJob _setupMonitorSourceWithPort:onQueue:withHandler:].cold.3
- -[OSLaunchdJob _startMonitoringAfterSubmit:].cold.1
- -[OSLaunchdJob initWithPlist:domain:].cold.1
- -[OSLaunchdJob initWithPlist:domain:].cold.2
- -[OSLaunchdJob monitorOnQueue:withHandler:].cold.1
- -[OSLaunchdJob monitorOnQueue:withHandler:].cold.2
- -[OSLaunchdJob monitorOnQueue:withHandler:].cold.3
- -[OSLaunchdJob monitorOnQueue:withHandler:].cold.4
- -[OSLaunchdJob start:].cold.1
- -[OSLaunchdJob submit:].cold.1
- -[OSLaunchdJob submit:].cold.2
- -[OSLaunchdJob submit:].cold.3
- -[OSLaunchdJob submitAndStart:].cold.1
- -[OSLaunchdJob submitAndStart:].cold.2
- -[OSLaunchdJob submitAndStart:].cold.3
- -[OSLaunchdJob submitAndStart:].cold.4
- -[OSLaunchdJob submitAndStart:].cold.5
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:].cold.1
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:].cold.10
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:].cold.11
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:].cold.2
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:].cold.3
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:].cold.4
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:].cold.5
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:].cold.6
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:].cold.7
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:].cold.8
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:].cold.9
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- ___64-[OSLaunchdJob _setupMonitorSourceWithPort:onQueue:withHandler:]_block_invoke.98
- ___64-[OSLaunchdJob _setupMonitorSourceWithPort:onQueue:withHandler:]_block_invoke.98.cold.1
- ___64-[OSLaunchdJob _setupMonitorSourceWithPort:onQueue:withHandler:]_block_invoke.cold.1
- __lass_log.cold.1
- __lass_log.log
- __lass_log.once
- __os_launch_job_log.cold.1
- __os_launch_job_log.log
- __os_launch_job_log.once
- __xpc_mach_port_close_recv
- __xpc_mach_port_make_send_once
- _objc_msgSend$charValue
- _objc_msgSend$intValue
- _objc_msgSend$longValue
- _objc_msgSend$shortValue
- _objc_msgSend$unsignedCharValue
- _objc_msgSend$unsignedIntValue
- _objc_msgSend$unsignedLongLongValue
- _objc_msgSend$unsignedLongValue
- _objc_msgSend$unsignedShortValue
- _objc_retainAutoreleasedReturnValue
- _xpc_uint64_create
CStrings:
+ "<%@> addressSanitizer=%d threadSanitizer=%d mtAddressSanitizer=%d undefinedBehaviorSanitizer=%d"
+ "DeveloperTools"
+ "SanitizerFlags"
+ "_Conclave"
+ "_ProcessType"
+ "_SandboxContainer"
+ "addressSanitizer"
+ "developer-tools"
+ "mtAddressSanitizer"
+ "spawn-constraint"
+ "threadSanitizer"
+ "undefinedBehaviorSanitizer"
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSObject<OS_xpc_object>\"16@0:8"
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSUUID\""
- "@\"OSLaunchdDomain\""
- "@\"OSLaunchdJobExitStatus\""
- "@100@0:8@16@24i32@36@44I52B56B60B64@68q76@84B92i96"
- "@16@0:8"
- "@20@0:8I16"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@28@0:8i16Q20"
- "@28@0:8i16^@20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@32@0:8Q16^@24"
- "@32@0:8[16C]16@24"
- "@32@0:8[16C]16^@24"
- "@40@0:8:16@24@32"
- "@40@0:8[16C]16@24^@32"
- "@40@0:8i16I20Q24Q32"
- "@44@0:8I16@20Q28^@36"
- "@48@0:8@16@24@32^@40"
- "@48@0:8r*16@24@32^@40"
- "@68@0:8q16i24i28@32@40B48@52@60"
- "@?"
- "AppServiceSupportAdditions"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B32@0:8@16^@24"
- "I"
- "I16@0:8"
- "I24@0:8Q16"
- "LASSProperties4RB"
- "NSObject"
- "OSLaunchdDomain"
- "OSLaunchdError"
- "OSLaunchdJob"
- "OSLaunchdJobExitStatus"
- "OSLaunchdJobInfo"
- "OSLaunchdJobInstanceProperties"
- "OSLaunchdJobProperties"
- "Q"
- "Q16@0:8"
- "SandboxContainer"
- "T#,R"
- "T@\"NSArray\",C,N,V_managedByServices"
- "T@\"NSArray\",C,N,V_programArguments"
- "T@\"NSData\",C,N,V_lightweightCodeRequirement"
- "T@\"NSDictionary\",C,N,V_additionalProperties"
- "T@\"NSDictionary\",C,N,V_additionalSubServices"
- "T@\"NSDictionary\",C,N,V_arguments"
- "T@\"NSDictionary\",C,N,V_environmentVariables"
- "T@\"NSDictionary\",C,N,V_overlay"
- "T@\"NSDictionary\",C,N,V_spawnConstraint"
- "T@\"NSObject<OS_xpc_object>\",R,N,V_additionalProperties"
- "T@\"NSObject<OS_xpc_object>\",R,N,V_additionalPropertiesDictionary"
- "T@\"NSObject<OS_xpc_object>\",R,N,V_endpoints"
- "T@\"NSSet\",C,N,V_managedEndpointLaunchIdentifiers"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_personaString"
- "T@\"NSString\",C,N,V_processType"
- "T@\"NSString\",C,N,V_roleAccount"
- "T@\"NSString\",C,N,V_runLoopType"
- "T@\"NSString\",C,N,V_sandboxProfile"
- "T@\"NSString\",C,N,V_serviceType"
- "T@\"NSString\",C,N,V_uiApplicationClass"
- "T@\"NSString\",C,N,V_uiApplicationDelegateClass"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_program"
- "T@\"NSString\",R,N,V_label"
- "T@\"NSString\",R,N,V_path"
- "T@\"NSString\",R,N,V_program"
- "T@\"NSURL\",&,N,V_sandboxContainer"
- "T@\"NSUUID\",&,N,V_oneShotUUID"
- "T@\"NSUUID\",R,N,V_handle"
- "T@\"NSUUID\",R,N,V_instance"
- "T@\"OSLaunchdJobExitStatus\",R,N,V_lastExitStatus"
- "TB,N"
- "TB,N,V_abandonCoalition"
- "TB,N,V_joinExistingSession"
- "TB,N,V_omitSandboxParameters"
- "TB,N,V_watchdogTimeout"
- "TB,R,N,V_enablePressuredExit"
- "TB,R,N,V_enableTransactions"
- "TB,R,N,V_keepAlive"
- "TB,R,N,V_removing"
- "TB,R,N,V_runAtLoad"
- "TB,R,N,V_xpcBundle"
- "TI,N,V_enterprisePersona"
- "TI,N,V_platform"
- "TI,R,N,V_os_reason_namespace"
- "TI,R,N,V_processType"
- "TQ,R"
- "TQ,R,N,V_os_reason_code"
- "TQ,R,N,V_os_reason_flags"
- "Ti,R,N,V_hostPID"
- "Ti,R,N,V_lastSpawnError"
- "Ti,R,N,V_pid"
- "Ti,R,N,V_requestedJetsamPriority"
- "Ti,R,N,V_wait4Status"
- "Tq,R,N,V_serviceType"
- "Tq,R,N,V_state"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_OSXPCObjectRepresentable"
- "_OS_overlayDictionary:"
- "_OS_xpcObjectRepresentation"
- "_abandonCoalition"
- "_additionalProperties"
- "_additionalPropertiesDictionary"
- "_additionalSubServices"
- "_arguments"
- "_createDomainOptions2flags:"
- "_createJobFromReplyHandle:"
- "_domain"
- "_enablePressuredExit"
- "_enableTransactions"
- "_endpoints"
- "_enterprisePersona"
- "_environmentVariables"
- "_getPlist"
- "_handle"
- "_handlesToJobs:"
- "_hostPID"
- "_initWithHandle:"
- "_instance"
- "_joinExistingSession"
- "_keepAlive"
- "_label"
- "_lastExitStatus"
- "_lastSpawnError"
- "_lightweightCodeRequirement"
- "_managedByServices"
- "_managedEndpointLaunchIdentifiers"
- "_monitorNormalizeError:"
- "_monitor_handler"
- "_monitor_queue"
- "_monitor_source"
- "_newCreateInstanceRequest:properties:"
- "_newRequest"
- "_newSubmitRequest"
- "_omitSandboxParameters"
- "_oneShotUUID"
- "_os_reason_code"
- "_os_reason_flags"
- "_os_reason_namespace"
- "_overlay"
- "_path"
- "_personaString"
- "_pid"
- "_platform"
- "_plist"
- "_populateHandle:"
- "_processType"
- "_program"
- "_programArguments"
- "_propertiesFromAttrs:"
- "_removing"
- "_requestedJetsamPriority"
- "_roleAccount"
- "_runAtLoad"
- "_runLoopType"
- "_sandboxContainer"
- "_sandboxProfile"
- "_serviceType"
- "_setupMonitorSourceWithPort:onQueue:withHandler:"
- "_spawnConstraint"
- "_startMonitoringAfterSubmit:"
- "_state"
- "_submitExtension:overlay:domain:error:"
- "_type"
- "_uiApplicationClass"
- "_uiApplicationDelegateClass"
- "_wait4Status"
- "_watchdogTimeout"
- "_xpcBundle"
- "abandonCoalition"
- "addObject:"
- "additionalProperties"
- "additionalPropertiesDictionary"
- "additionalSubServices"
- "arguments"
- "arrayWithCapacity:"
- "autorelease"
- "boolValue"
- "bytes"
- "cancelMonitor"
- "charValue"
- "class"
- "conformsToProtocol:"
- "copy"
- "copyJobWithHandle:"
- "copyJobWithLabel:domain:"
- "copyJobWithPid:"
- "copyJobsLoadedByCoalition:error:"
- "copyJobsLoadedByJob:"
- "copyJobsManagedBy:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDomainForRoleAccount:sessionType:options:error:"
- "createInstance:error:"
- "createInstance:properties:error:"
- "createXPCError:"
- "currentDomain"
- "debugDescription"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "disableLogging_4watchdogd"
- "domainForAsid:"
- "domainForPid:"
- "domainForRoleAccountUser:"
- "domainForUser:"
- "enablePressuredExit"
- "enableTransactions"
- "endpoints"
- "enterprisePersona"
- "environmentVariables"
- "errorWithDomain:code:userInfo:"
- "fileSystemRepresentation"
- "getCurrentJobInfo"
- "getUUIDBytes:"
- "hash"
- "hostPID"
- "i16@0:8"
- "i20@0:8i16"
- "init"
- "initWithFormat:"
- "initWithLabel:instance:requestedJetsamPriority:additionalProperties:program:processType:keepAlive:runAtLoad:enableTransactions:endpoints:serviceType:path:xpcBundle:hostPID:"
- "initWithPlist:"
- "initWithPlist:domain:"
- "initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:"
- "initWithType:handle:"
- "initWithUUIDBytes:"
- "initWithWait4Status:os_reason_namespace:os_reason_code:os_reason_flags:"
- "initiateRemoval:"
- "intValue"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "jobInfoFromMessage:"
- "jobStateFromMessage:"
- "joinExistingSession"
- "keepAlive"
- "lastExitStatus"
- "lastSpawnError"
- "length"
- "lightweightCodeRequirement"
- "loginwindowDomain"
- "longLongValue"
- "longValue"
- "managedByServices"
- "managedEndpointLaunchIdentifiers"
- "monitorOnQueue:withHandler:"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedLong:"
- "objCType"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "omitSandboxParameters"
- "oneShotUUID"
- "os_reason_code"
- "os_reason_flags"
- "os_reason_namespace"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "personaString"
- "platform"
- "processSubmitReply:"
- "processType"
- "programArguments"
- "propertiesForJob:error:"
- "propertiesForPid:error:"
- "q"
- "q16@0:8"
- "q24@0:8@16"
- "release"
- "remove:"
- "requestedJetsamPriority"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "roleAccount"
- "runAtLoad"
- "runLoopType"
- "sandboxContainer"
- "sandboxProfile"
- "self"
- "serviceType"
- "setAbandonCoalition:"
- "setAdditionalProperties:"
- "setAdditionalSubServices:"
- "setArguments:"
- "setDisableLogging_4watchdogd:"
- "setEnterprisePersona:"
- "setEnvironmentVariables:"
- "setJoinExistingSession:"
- "setLightweightCodeRequirement:"
- "setManagedByServices:"
- "setManagedEndpointLaunchIdentifiers:"
- "setObject:forKeyedSubscript:"
- "setOmitSandboxParameters:"
- "setOneShotUUID:"
- "setOverlay:"
- "setPersonaString:"
- "setPlatform:"
- "setProcessType:"
- "setProgramArguments:"
- "setRoleAccount:"
- "setRunLoopType:"
- "setSandboxContainer:"
- "setSandboxProfile:"
- "setServiceType:"
- "setSpawnConstraint:"
- "setUiApplicationClass:"
- "setUiApplicationDelegateClass:"
- "setValue:forKey:"
- "setWatchdogTimeout:"
- "setupMonitorOnQueue:withHandler:reply:"
- "shortValue"
- "spawnConstraint"
- "start:"
- "state"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "submit:"
- "submitAll:error:"
- "submitAndStart:"
- "submitExtension:overlay:domain:error:"
- "submitExtensionAtURL:properties:domain:error:"
- "superclass"
- "systemDomain"
- "uiApplicationClass"
- "uiApplicationDelegateClass"
- "unpendLaunches:"
- "unsignedCharValue"
- "unsignedIntValue"
- "unsignedLongLongValue"
- "unsignedLongValue"
- "unsignedShortValue"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v24@0:8@16"
- "v32@0:8@16@?24"
- "v36@0:8I16@20@?28"
- "v40@0:8@16@?24@32"
- "valueForKey:"
- "wait4Status"
- "watchdogTimeout"
- "xpcBundle"
- "xpcOverlay"
- "zone"

```
