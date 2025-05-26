## RunningBoard

> `/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard`

```diff

-858.80.1.0.0
-  __TEXT.__text: 0x76b64
-  __TEXT.__auth_stubs: 0x1410
-  __TEXT.__objc_methlist: 0x4b90
+874.102.1.0.0
+  __TEXT.__text: 0x78c60
+  __TEXT.__auth_stubs: 0x1420
+  __TEXT.__objc_methlist: 0x4cd8
   __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0x669d
-  __TEXT.__oslogstring: 0xa6f9
-  __TEXT.__gcc_except_tab: 0x784
-  __TEXT.__unwind_info: 0x190c
-  __TEXT.__objc_classname: 0xe77
-  __TEXT.__objc_methname: 0xc45e
-  __TEXT.__objc_methtype: 0x2a4b
-  __TEXT.__objc_stubs: 0x93e0
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x14c0
-  __DATA_CONST.__objc_classlist: 0x340
-  __DATA_CONST.__objc_catlist: 0x150
+  __TEXT.__cstring: 0x6927
+  __TEXT.__oslogstring: 0xaa95
+  __TEXT.__gcc_except_tab: 0x7b4
+  __TEXT.__unwind_info: 0x1958
+  __TEXT.__objc_classname: 0xea8
+  __TEXT.__objc_methname: 0xc83e
+  __TEXT.__objc_methtype: 0x2a76
+  __TEXT.__objc_stubs: 0x9780
+  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__const: 0x1580
+  __DATA_CONST.__objc_classlist: 0x348
+  __DATA_CONST.__objc_catlist: 0x158
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xb100
-  __DATA_CONST.__objc_selrefs: 0x2918
-  __DATA_CONST.__objc_arraydata: 0x648
-  __AUTH_CONST.__cfstring: 0x5560
-  __AUTH_CONST.__const: 0x5a0
-  __AUTH_CONST.__objc_const: 0x3150
-  __AUTH_CONST.__objc_intobj: 0x210
+  __DATA_CONST.__objc_const: 0xb1b8
+  __DATA_CONST.__objc_selrefs: 0x2a00
+  __DATA_CONST.__objc_classrefs: 0x6a8
+  __DATA_CONST.__objc_superrefs: 0x280
+  __DATA_CONST.__objc_arraydata: 0x678
+  __AUTH_CONST.__cfstring: 0x56e0
+  __AUTH_CONST.__const: 0x5e0
+  __AUTH_CONST.__objc_const: 0x3220
+  __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__auth_ptr: 0x40
-  __AUTH_CONST.__objc_dictobj: 0x348
-  __AUTH_CONST.__objc_arrayobj: 0x150
-  __AUTH_CONST.__auth_got: 0xa18
+  __AUTH_CONST.__objc_dictobj: 0x370
+  __AUTH_CONST.__objc_arrayobj: 0x168
+  __AUTH_CONST.__auth_got: 0xa20
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_classrefs: 0x690
-  __DATA.__objc_superrefs: 0x278
-  __DATA.__objc_ivar: 0x97c
+  __DATA.__objc_ivar: 0x98c
   __DATA.__data: 0x1200
-  __DATA.__bss: 0x40
-  __DATA_DIRTY.__objc_data: 0x1ea0
+  __DATA.__bss: 0x50
+  __DATA_DIRTY.__objc_data: 0x1ef0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x230
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 2516
-  Symbols:   8739
-  CStrings:  4186
+  Functions: 2549
+  Symbols:   8863
+  CStrings:  4246
 
Symbols:
+ +[RBLaunchdProperties _instanceWithProperties:]
+ +[RBTargetExtensionPointRestriction domainRestrictionForDictionary:withError:]
+ -[RBLaunchdProperties _configureXPCServiceWithProperties:]
+ -[RBLaunchdProperties _initWithProperties:]
+ -[RBLaunchdProperties _initWithProperties:].cold.1
+ -[RBLaunchdProperties _initWithProperties:].cold.2
+ -[RBLaunchdProperties _initWithProperties:].cold.3
+ -[RBLaunchdProperties _initWithProperties:].cold.4
+ -[RBLaunchdProperties _initWithProperties:].cold.5
+ -[RBLaunchdProperties _initWithProperties:].cold.6
+ -[RBLaunchdProperties _parseEndpoints:withAdditionalProperties:]
+ -[RBLaunchdProperties managedEndpointByLaunchIdentifier]
+ -[RBMutableProcessState addEndowmentInfo:]
+ -[RBMutableProcessState removeAllEndowmentInfos]
+ -[RBMutableProcessState removeEndowmentInfo:]
+ -[RBProcess managedEndpointByLaunchIdentifier]
+ -[RBProcessManager _executeLaunchRequest:withError:]
+ -[RBProcessManager _lifecycleQueue_addProcessWithInstance:properties:].cold.3
+ -[RBProcessManager _lifecycleQueue_addProcessWithInstance:properties:].cold.4
+ -[RBProcessManager executeLaunchRequest:withCompletion:]
+ -[RBProcessState endowmentInfos]
+ -[RBSLaunchContext(RBLaunchChecks) _applicationRecordForLaunchCheck]
+ -[RBSLaunchContext(RBLaunchChecks) _applicationRecordForLaunchCheck].cold.1
+ -[RBSLaunchContext(RBLaunchChecks) _applicationRecordForLaunchCheck].cold.2
+ -[RBSLaunchContext(RBLaunchChecks) _applicationRecordForLaunchCheck].cold.3
+ -[RBSLaunchContext(RBLaunchChecks) _deviceIsEligibleForDomain:]
+ -[RBSLaunchContext(RBLaunchChecks) _deviceIsEligibleForDomain:].cold.1
+ -[RBSLaunchContext(RBLaunchChecks) _launchAllowedBySystemState:error:]
+ -[RBSLaunchContext(RBLaunchChecks) _needsEligibilityCheck]
+ -[RBSLaunchContext(RBLaunchChecks) _passesEligibilityCheck]
+ -[RBSLaunchContext(RBLaunchChecks) _passesEligibilityCheck].cold.1
+ -[RBSLaunchContext(RBLaunchChecks) _passesRegulatoryChecksWithError:]
+ -[RBSLaunchContext(RBLaunchChecks) _recordPassesEligibilityChecks:]
+ -[RBSLaunchContext(RBLaunchChecks) _requiresPreflightCheck]
+ -[RBSLaunchContext(RBLaunchChecks) _requiresPreflightCheck].cold.1
+ -[RBSLaunchContext(RBLaunchChecks) _requiresPreflightCheck].cold.2
+ -[RBSLaunchContext(RBLaunchChecks) _requiresPreflightCheck].cold.3
+ -[RBSLaunchContext(RBLaunchChecks) _requiresPreflightCheck].cold.4
+ -[RBSLaunchContext(RBLaunchChecks) _sharedPreflightManager]
+ -[RBTargetExtensionPointRestriction .cxx_destruct]
+ -[RBTargetExtensionPointRestriction _initWithExtensionPoint:]
+ -[RBTargetExtensionPointRestriction allEntitlements]
+ -[RBTargetExtensionPointRestriction allowsContext:withError:]
+ -[RBTargetExtensionPointRestriction copyWithZone:]
+ -[RBTargetExtensionPointRestriction description]
+ -[RBTargetExtensionPointRestriction hash]
+ -[RBTargetExtensionPointRestriction isEqual:]
+ GCC_except_table22
+ GCC_except_table33
+ GCC_except_table4
+ GCC_except_table42
+ GCC_except_table58
+ OBJC_IVAR_$_RBProcessState._endowmentInfos
+ _OBJC_CLASS_$_RBSMachEndpoint
+ _OBJC_CLASS_$_RBSProcessEndowmentInfo
+ _OBJC_CLASS_$_RBSSavedEndowment
+ _OBJC_CLASS_$_RBTargetExtensionPointRestriction
+ _OBJC_IVAR_$_RBLaunchdProperties._managedEndpointByLaunchIdentifier
+ _OBJC_IVAR_$_RBProcess._managedEndpointByLaunchIdentifier
+ _OBJC_IVAR_$_RBTargetExtensionPointRestriction._extensionPoint
+ _OBJC_METACLASS_$_RBTargetExtensionPointRestriction
+ _RBSServiceMessageManagedEndpointByLaunchIdentifierKey
+ __OBJC_$_CATEGORY_RBSLaunchContext_$_RBLaunchChecks
+ __OBJC_$_CLASS_METHODS_RBTargetExtensionPointRestriction
+ __OBJC_$_INSTANCE_METHODS_RBSLaunchContext(RBLaunchChecks)
+ __OBJC_$_INSTANCE_METHODS_RBTargetExtensionPointRestriction
+ __OBJC_$_INSTANCE_VARIABLES_RBTargetExtensionPointRestriction
+ __OBJC_$_PROP_LIST_RBBundleProperties.107
+ __OBJC_CLASS_RO_$_RBTargetExtensionPointRestriction
+ __OBJC_METACLASS_RO_$_RBTargetExtensionPointRestriction
+ ___104-[RBRequestManager _finishLaunchRequestAfterAssertionAcquisition:requestor:identifier:error:completion:]_block_invoke
+ ___37-[RBPrewarmManager _queue_runPrewarm]_block_invoke
+ ___52-[RBProcessManager _executeLaunchRequest:withError:]_block_invoke
+ ___57-[RBProcessMonitorObserver _lock_sendPendingStateUpdates]_block_invoke.108
+ ___57-[RBProcessMonitorObserver _lock_sendPendingStateUpdates]_block_invoke.108.cold.1
+ ___57-[RBProcessMonitorObserver _lock_sendPendingStateUpdates]_block_invoke.111
+ ___57-[RBProcessMonitorObserver _lock_sendPendingStateUpdates]_block_invoke.111.cold.1
+ ___58-[RBSLaunchContext(RBLaunchChecks) _needsEligibilityCheck]_block_invoke
+ ___59-[RBSLaunchContext(RBLaunchChecks) _sharedPreflightManager]_block_invoke
+ ___64-[RBLaunchdProperties _parseEndpoints:withAdditionalProperties:]_block_invoke
+ ___67-[RBSLaunchContext(RBLaunchChecks) _recordPassesEligibilityChecks:]_block_invoke
+ ___67-[RBSLaunchContext(RBLaunchChecks) _recordPassesEligibilityChecks:]_block_invoke.cold.1
+ ___70-[RBProcessManager _enqueueGuaranteedRunningLaunchForIdentity:atTime:]_block_invoke.134
+ ___70-[RBProcessManager _enqueueGuaranteedRunningLaunchForIdentity:atTime:]_block_invoke.cold.3
+ ___80-[RBRequestManager executeLaunchRequest:euid:requestor:entitlements:completion:]_block_invoke_2
+ ___block_descriptor_32_e55_v32?0"RBSProcessHandle"8"NSDictionary"16"NSError"24l
+ ___block_descriptor_40_e8_32bs_e55_v32?0"RBSProcessHandle"8"NSDictionary"16"NSError"24ls32l8
+ ___block_descriptor_56_e8_32s40s48r_e15_v32?0816^B24ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e37_B24?0r*8"NSObject<OS_xpc_object>"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e55_v32?0"RBSProcessHandle"8"NSDictionary"16"NSError"24ls56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e82_v40?0"RBSProcessHandle"8"RBSAssertionIdentifier"16"NSDictionary"24"NSError"32ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e5_v8?0ls32l8s40l8s48l8r64l8r72l8s56l8
+ ___block_literal_global.138
+ ___block_literal_global.140
+ ___block_literal_global.23
+ ___block_literal_global.262
+ ___block_literal_global.55
+ ___block_literal_global.91
+ __needsEligibilityCheck.allowed
+ __needsEligibilityCheck.onceToken
+ __unnamed_array_storage.19
+ __xpc_type_array
+ _domainRestrictionForDictionary:withError:.onceToken.244
+ _domainRestrictionForDictionary:withError:.onceToken.259
+ _domainRestrictionForDictionary:withError:.singleton.243
+ _domainRestrictionForDictionary:withError:.singleton.260
+ _objc_msgSend$_applicationRecordForLaunchCheck
+ _objc_msgSend$_configureXPCServiceWithProperties:
+ _objc_msgSend$_deviceIsEligibleForDomain:
+ _objc_msgSend$_executeLaunchRequest:withError:
+ _objc_msgSend$_initWithName:nonLaunching:port:
+ _objc_msgSend$_initWithNamespace:environment:encodedEndowment:
+ _objc_msgSend$_initWithProperties:
+ _objc_msgSend$_instanceWithProperties:
+ _objc_msgSend$_launchAllowedBySystemState:error:
+ _objc_msgSend$_needsEligibilityCheck
+ _objc_msgSend$_parseEndpoints:withAdditionalProperties:
+ _objc_msgSend$_passesEligibilityCheck
+ _objc_msgSend$_passesRegulatoryChecksWithError:
+ _objc_msgSend$_recordPassesEligibilityChecks:
+ _objc_msgSend$_requiresPreflightCheck
+ _objc_msgSend$addEndowmentInfo:
+ _objc_msgSend$decodeFromJob:
+ _objc_msgSend$encodeDictionary:forKey:
+ _objc_msgSend$endowmentInfos
+ _objc_msgSend$entitlements
+ _objc_msgSend$executeLaunchRequest:withCompletion:
+ _objc_msgSend$findApplicationRecordWithError:
+ _objc_msgSend$hostPID
+ _objc_msgSend$isMultiInstanceExtension
+ _objc_msgSend$managedEndpointByLaunchIdentifier
+ _objc_msgSend$managedEndpointLaunchIdentifiers
+ _objc_msgSend$objectForKey:ofClass:
+ _objc_msgSend$removeAllEndowmentInfos
+ _objc_msgSend$removeEndowmentInfo:
+ _objc_msgSend$requiredExistingProcess
+ _objc_msgSend$setEndowmentInfos:
+ _objc_msgSend$setManagedEndpointByLaunchIdentifier:
+ _objc_msgSend$setManagedEndpointLaunchIdentifiers:
+ _objc_msgSend$setRequiredExistingProcess:
+ _objc_msgSend$xpcBundle
+ _os_eligibility_get_domain_answer
+ _xpc_array_get_dictionary
+ _xpc_dictionary_apply
+ _xpc_dictionary_create_empty
+ _xpc_dictionary_get_count
- +[RBLaunchdProperties _instanceWithProperties:xpcProps:]
- +[RBLaunchdProperties propertiesForJob:].cold.2
- +[RBLaunchdProperties propertiesForJob:].cold.3
- +[RBLaunchdProperties propertiesForJob:].cold.4
- -[RBLaunchdProperties _configureXPCServiceWithProperties:HostPid:]
- -[RBLaunchdProperties _initWithProperties:xpcProps:]
- -[RBLaunchdProperties _initWithProperties:xpcProps:].cold.1
- -[RBLaunchdProperties _initWithProperties:xpcProps:].cold.2
- -[RBLaunchdProperties _initWithProperties:xpcProps:].cold.3
- -[RBLaunchdProperties _initWithProperties:xpcProps:].cold.4
- -[RBLaunchdProperties _initWithProperties:xpcProps:].cold.5
- -[RBLaunchdProperties _initWithProperties:xpcProps:].cold.6
- -[RBLaunchdProperties _initWithProperties:xpcProps:].cold.7
- -[RBProcessManager _preflightCheck:]
- -[RBProcessManager _preflightCheck:].cold.1
- -[RBProcessManager _preflightCheck:].cold.2
- -[RBProcessManager _preflightCheck:].cold.3
- -[RBProcessManager _preflightCheck:].cold.4
- -[RBProcessManager _sharedPreflightManager]
- -[RBProcessManager executeLaunchRequest:withError:]
- GCC_except_table10
- GCC_except_table23
- GCC_except_table32
- GCC_except_table48
- __OBJC_$_PROP_LIST_RBBundleProperties.106
- ___43-[RBProcessManager _sharedPreflightManager]_block_invoke
- ___51-[RBProcessManager executeLaunchRequest:withError:]_block_invoke
- ___57-[RBProcessMonitorObserver _lock_sendPendingStateUpdates]_block_invoke.107
- ___57-[RBProcessMonitorObserver _lock_sendPendingStateUpdates]_block_invoke.107.cold.1
- ___57-[RBProcessMonitorObserver _lock_sendPendingStateUpdates]_block_invoke.110
- ___57-[RBProcessMonitorObserver _lock_sendPendingStateUpdates]_block_invoke.110.cold.1
- ___70-[RBProcessManager _enqueueGuaranteedRunningLaunchForIdentity:atTime:]_block_invoke.89
- ___block_descriptor_56_e8_32s40s48s_e65_v32?0"RBSProcessHandle"8"RBSAssertionIdentifier"16"NSError"24ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8r56l8s48l8r64l8
- ___block_literal_global.230
- ___block_literal_global.39
- ___block_literal_global.93
- ___block_literal_global.95
- __launch_job_routine
- _domainRestrictionForDictionary:withError:.onceToken.228
- _domainRestrictionForDictionary:withError:.onceToken.243
- _domainRestrictionForDictionary:withError:.singleton.227
- _domainRestrictionForDictionary:withError:.singleton.244
- _launch_copy_properties_for_pid_4assertiond
- _launch_extension_property_host_pid
- _launch_extension_property_path
- _launch_extension_property_xpc_bundle
- _objc_msgSend$_configureXPCServiceWithProperties:HostPid:
- _objc_msgSend$_initWithProperties:xpcProps:
- _objc_msgSend$_instanceWithProperties:xpcProps:
- _objc_msgSend$_preflightCheck:
- _objc_msgSend$executeLaunchRequest:withError:
- _objc_msgSend$initWithDecodeFromJob:
- _xpc_dictionary_get_int64
- _xpc_dictionary_set_uuid
CStrings:
+ "\t1\""
+ "\x11\x12\x12\x15"
+ "\x14\x12!!'\x13"
+ " endowments:[\n\t"
+ "%{public}@ failed to encode identity"
+ "%{public}@ is already running as %{public}@ which doesn't match requiredExistingProcess of %@"
+ "%{public}@ is already running as %{public}@ which matches the requiredExistingProcess"
+ "%{public}@ is not RunningBoard jetsam managed."
+ "%{public}@: LaunchRequestEndpointIdentifiers entry (%s) is malformed (expect only true or string mappings) - ignoring %@"
+ "<%@| identity:%@ role:%@ gpuRole:%@ explicitJetsamBand:%d memoryLimit:%@(%@) flags:%hx guaranteedRunning:%@ legacyFinishTaskReason:%lu%@%@%@%@%@%@%@%@%@%@%@%@%@%@>"
+ "B24@0:8^@16"
+ "B24@?0r*8@\"NSObject<OS_xpc_object>\"16"
+ "Calculated state for %{public}@: %{public}@ (role: %{public}@) (endowments: %@) "
+ "Could not create LSApplicationRecord from bundleID %@: %@"
+ "Could not find LS record for %@"
+ "Could not get bundle ID from %{public}@"
+ "Failed GuaranteedRunning launch of %@"
+ "Failed GuaranteedRunning launch of %@ because of %@"
+ "Invalidating assertion <%{public}@> on acquisition for unmet conditions: %{public}@"
+ "Launch prevented due to device eligibility requirements"
+ "LaunchRequestEndpointIdentifiers"
+ "Not emitting 0xdead10cc error for process %@ suspended with locked system files because it is a Mac Catalyst app. Mac Catalyst apps should always be terminated on suspension, regardless of whether the app holds a shared file lock."
+ "Prior process for %@ is reporting a pid when we're not expecting it to (should be dead)."
+ "RBLaunchChecks"
+ "RBTargetExtensionPointRestriction"
+ "RBTargetExtensionPointRestriction doesn't specify extensionPoint or doesn't have right class for extensionPoint: %@"
+ "T@\"NSDictionary\",R,C,N,V_managedEndpointByLaunchIdentifier"
+ "T@\"NSDictionary\",R,N,V_managedEndpointByLaunchIdentifier"
+ "T@\"NSSet\",R,C,N,V_endowmentInfos"
+ "T@\"NSString\",?,R,C"
+ "TargetExtensionPoint"
+ "The process was already running as expected."
+ "The running process did not match the expected."
+ "We already have a process %@ with this identifier: %@, were two launches for the same process executed?"
+ "XPCServiceEndpointPort"
+ "_applicationRecordForLaunchCheck"
+ "_configureXPCServiceWithProperties:"
+ "_deviceIsEligibleForDomain:"
+ "_endowmentInfos"
+ "_executeLaunchRequest:withError:"
+ "_initWithName:nonLaunching:port:"
+ "_initWithNamespace:environment:encodedEndowment:"
+ "_initWithProperties:"
+ "_instanceWithProperties:"
+ "_launchAllowedBySystemState:error:"
+ "_managedEndpointByLaunchIdentifier"
+ "_needsEligibilityCheck"
+ "_parseEndpoints:withAdditionalProperties:"
+ "_passesEligibilityCheck"
+ "_passesRegulatoryChecksWithError:"
+ "_recordPassesEligibilityChecks:"
+ "_requiresPreflightCheck"
+ "addEndowmentInfo:"
+ "com.apple.SafariViewService"
+ "com.apple.developer.embedded-web-browser-engine"
+ "com.apple.developer.web-browser-engine.host"
+ "completion"
+ "decodeFromJob:"
+ "device is ineligible for domain %@"
+ "encodeDictionary:forKey:"
+ "endowmentInfos"
+ "executeLaunchRequest:error:"
+ "executeLaunchRequest:withCompletion:"
+ "failure getting eligibility info for domain %qu: %s"
+ "findApplicationRecordWithError:"
+ "hostPID"
+ "isMultiInstanceExtension"
+ "launch request %{public}@ from %{public}@ failed but still created an assertion (%{public}@) : error=%{public}@"
+ "managedEndpointByLaunchIdentifier"
+ "managedEndpointLaunchIdentifiers"
+ "no job for endpoint %@ from looked up handle=%@"
+ "objectForKey:ofClass:"
+ "removeAllEndowmentInfos"
+ "removeEndowmentInfo:"
+ "requiredExistingProcess"
+ "setEndowmentInfos:"
+ "setManagedEndpointByLaunchIdentifier:"
+ "setManagedEndpointLaunchIdentifiers:"
+ "setRequiredExistingProcess:"
+ "target doesn't have extensionPoint %@"
+ "target isn't extension"
+ "unable to find LSApplicationRecord for identity %@: %@"
+ "v32@0:8@\"RBSLaunchRequest\"16@?<v@?@\"RBSProcessHandle\"@\"NSDictionary\"@\"NSError\">24"
+ "v32@?0@\"RBSProcessHandle\"8@\"NSDictionary\"16@\"NSError\"24"
+ "v40@?0@\"RBSProcessHandle\"8@\"RBSAssertionIdentifier\"16@\"NSDictionary\"24@\"NSError\"32"
+ "v52@0:8@\"RBSLaunchRequest\"16I24@\"RBProcess\"28@\"<RBEntitlementPossessing>\"36@?<v@?@\"RBSProcessHandle\"@\"RBSAssertionIdentifier\"@\"NSDictionary\"@\"NSError\">44"
+ "xpcBundle"
- "\t1!"
- "\x11\x12\x12\x14"
- "\x14\x12!!'\x12"
- "<%@| identity:%@ role:%@ gpuRole:%@ explicitJetsamBand:%d memoryLimit:%@(%@) flags:%hx guaranteedRunning:%@ legacyFinishTaskReason:%lu%@%@%@%@%@%@%@%@%@%@%@>"
- "@\"RBSProcessHandle\"32@0:8@\"RBSLaunchRequest\"16o^@24"
- "@28@0:8@16i24"
- "Calculated state for %{public}@: %{public}@ (role: %{public}@)"
- "Failed GuaranteedRunning launch of %@ (handle %@)"
- "Failed GuaranteedRunning launch of %@ (handle %@) because of %@"
- "INvalidating assertion on acquisition for unmet conditions: %{public}@"
- "_configureXPCServiceWithProperties:HostPid:"
- "_initWithProperties:xpcProps:"
- "_instanceWithProperties:xpcProps:"
- "_parseAdditionalProperties no additionalProperties"
- "_preflightCheck:"
- "adding additional launch properties to %@: %@"
- "assertion failure: \"job != ((void *)0)\" -> %lld"
- "assertion failure: \"job.handle != ((void *)0)\" -> %lld"
- "assertion failure: \"xpcProps != ((void*)0)\" -> %lld"
- "attrs"
- "could not copy properties for job: %@ (%s)"
- "executeLaunchRequest:identifier:error:"
- "executeLaunchRequest:withError:"
- "initWithDecodeFromJob:"
- "job-handle"
- "no job found for endpoint %@"
- "v32@?0@\"RBSProcessHandle\"8@\"RBSAssertionIdentifier\"16@\"NSError\"24"
- "v52@0:8@\"RBSLaunchRequest\"16I24@\"RBProcess\"28@\"<RBEntitlementPossessing>\"36@?<v@?@\"RBSProcessHandle\"@\"RBSAssertionIdentifier\"@\"NSError\">44"

```
