## RunningBoardServices

> `/System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices`

```diff

-945.80.1.0.1
-  __TEXT.__text: 0x47b88
+961.100.17.0.0
+  __TEXT.__text: 0x48c94
   __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_methlist: 0x5348
+  __TEXT.__objc_methlist: 0x5880
   __TEXT.__const: 0x158
-  __TEXT.__cstring: 0x482f
+  __TEXT.__cstring: 0x4870
   __TEXT.__oslogstring: 0x28a9
-  __TEXT.__gcc_except_tab: 0x8f4
-  __TEXT.__unwind_info: 0x1470
+  __TEXT.__gcc_except_tab: 0x90c
+  __TEXT.__unwind_info: 0x15b8
   __TEXT.__objc_classname: 0xee7
-  __TEXT.__objc_methname: 0x7be0
+  __TEXT.__objc_methname: 0x7d55
   __TEXT.__objc_methtype: 0x1524
-  __TEXT.__objc_stubs: 0x4ae0
+  __TEXT.__objc_stubs: 0x4b00
   __DATA_CONST.__got: 0x4e0
-  __DATA_CONST.__const: 0x6d0
+  __DATA_CONST.__const: 0x6d8
   __DATA_CONST.__objc_classlist: 0x438
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c30
+  __DATA_CONST.__objc_selrefs: 0x1cd0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x640
   __AUTH_CONST.__const: 0xe60
-  __AUTH_CONST.__cfstring: 0x6080
-  __AUTH_CONST.__objc_const: 0xb3e8
+  __AUTH_CONST.__cfstring: 0x60c0
+  __AUTH_CONST.__objc_const: 0xab20
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xb40
-  __DATA.__objc_ivar: 0x5ac
+  __DATA.__objc_ivar: 0x5b4
   __DATA.__data: 0x620
   __DATA.__bss: 0x330
   __DATA_DIRTY.__objc_data: 0x1ef0

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/BaseBoard.framework/Versions/A/BaseBoard
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/UserManagement.framework/Versions/A/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C6A2DA05-DD7B-30D9-9C9B-3A0171803A5D
-  Functions: 2123
-  Symbols:   4748
-  CStrings:  3689
+  UUID: 6A3C0B76-D182-3E08-9211-586B3D78F4C1
+  Functions: 2272
+  Symbols:   4917
+  CStrings:  3703
 
Symbols:
+ +[RBSAuditToken tokenFromAuditTokenRef:].cold.1
+ +[RBSAuditToken tokenFromXPCConnection:].cold.1
+ +[RBSConnection connectionQueue].cold.1
+ +[RBSConnection handshakeQueue].cold.1
+ +[RBSConnection sharedInstance].cold.1
+ +[RBSEndowmentGrant grantWithNamespace:endowment:].cold.1
+ +[RBSMachPort portForPort:].cold.2
+ +[RBSProcessApplicationPredicate applicationPredicate].cold.1
+ +[RBSProcessBKSLegacyPredicate legacyPredicate].cold.1
+ +[RBSProcessHandle observeForImminentAssertionsExpiration:].cold.1
+ +[RBSProcessIdentity identityForAppViewServiceIdentifier:]
+ +[RBSProcessIdentity identityForXPCServiceExecutablePath:pid:auid:host:UUID:].cold.7
+ +[RBSProcessIdentity identityForXPCServiceExecutablePath:pid:auid:host:UUID:].cold.8
+ +[RBSProcessIdentity identityForXPCServiceIdentifier:hostInstance:UUID:persona:validationToken:variant:].cold.1
+ +[RBSProcessIdentity identityForXPCServiceIdentifier:hostInstance:UUID:persona:validationToken:variant:].cold.2
+ +[RBSProcessMonitor monitorWithPredicate:updateHandler:].cold.1
+ +[RBSProcessMonitor monitorWithPredicate:updateHandler:].cold.2
+ +[RBSProcessPredicate predicateMatching:].cold.1
+ +[RBSProcessStateUpdate updateWithState:previousState:exitEvent:].cold.1
+ +[RBSService saveEndowment:forKey:withError:].cold.1
+ +[RBSService saveEndowment:forKey:withError:].cold.2
+ +[RBSTarget currentProcess].cold.1
+ +[RBSTarget systemTarget].cold.1
+ +[RBSTarget targetWithEndpoint:].cold.1
+ +[RBSTarget targetWithEndpoint:].cold.2
+ +[RBSTarget targetWithPid:environmentIdentifier:].cold.1
+ +[RBSWorkloop sharedInstance].cold.1
+ +[RBSXPCMessage messageForMethod:arguments:].cold.1
+ +[RBSXPCServiceProcessIdentity shouldManageExtensionWithExtensionPoint:].cold.1
+ -[RBSAssertion _initWithServerValidatedDescriptor:service:].cold.1
+ -[RBSAssertion addObserver:].cold.1
+ -[RBSAssertion dealloc].cold.1
+ -[RBSAssertion initWithExplanation:target:attributes:].cold.1
+ -[RBSAssertion initWithExplanation:target:attributes:].cold.2
+ -[RBSAssertion removeObserver:].cold.1
+ -[RBSConnection _handleMessage:].cold.5
+ -[RBSConnection handleForPredicate:error:].cold.1
+ -[RBSConnection identifiersForStateCaptureSubsystems:].cold.1
+ -[RBSConnection preventLaunchPredicatesWithError:].cold.1
+ -[RBSConnection saveEndowment:withError:].cold.1
+ -[RBSConnection subscribeToProcessDeath:handler:].cold.1
+ -[RBSGPUAccessGrant _initWithRole:].cold.1
+ -[RBSIdentityAndRecordInfoProvider _initWithIdentity:record:].cold.1
+ -[RBSIdentityAndRecordInfoProvider _initWithIdentity:record:].cold.2
+ -[RBSInheritance _initWithNamespace:environment:encodedEndowment:originatingIdentifier:attributePath:].cold.1
+ -[RBSLaunchContext launchAssertionIdentifier]
+ -[RBSLaunchContext launchRequestIdentifierToMachNameMap]
+ -[RBSLaunchContext setLaunchAssertionIdentifier:]
+ -[RBSLaunchContext setLaunchRequestIdentifierToMachNameMap:]
+ -[RBSMacAppProcessIdentity _matchesIdentity:].cold.1
+ -[RBSMachEndpoint _initWithName:nonLaunching:port:].cold.1
+ -[RBSMachEndpoint _initWithName:nonLaunching:port:].cold.2
+ -[RBSMachEndpoint _initWithName:nonLaunching:port:].cold.3
+ -[RBSMachPort initWithCoder:].cold.1
+ -[RBSProcessBundle bundleInfoValueForKey:].cold.1
+ -[RBSProcessBundle bundleInfoValueForKey:].cold.2
+ -[RBSProcessBundleIdentifiersPredicate initWithIdentifiers:].cold.1
+ -[RBSProcessCollectionPredicateImpl initWithIdentifiers:].cold.1
+ -[RBSProcessHandle initWithInstance:auditToken:bundleData:manageFlags:beforeTranslocationBundlePath:executablePath:cache:].cold.1
+ -[RBSProcessHandle initWithInstance:auditToken:bundleData:manageFlags:beforeTranslocationBundlePath:executablePath:cache:].cold.2
+ -[RBSProcessHandle initWithRBSXPCCoder:].cold.2
+ -[RBSProcessHandlePredicateImpl initWithHandle:].cold.1
+ -[RBSProcessIdentifier initWithPid:].cold.1
+ -[RBSProcessIdentifierPredicate initWithIdentifier:].cold.1
+ -[RBSProcessIdentifiersPredicate initWithIdentifiers:].cold.1
+ -[RBSProcessIdentityPredicate isEqual:].cold.1
+ -[RBSProcessLimitations description].cold.1
+ -[RBSProcessMonitor setEvents:].cold.1
+ -[RBSProcessMonitor setPredicates:].cold.1
+ -[RBSProcessMonitor setPreventLaunchUpdateHandle:].cold.1
+ -[RBSProcessMonitor setServiceClass:].cold.1
+ -[RBSProcessMonitor setStateDescriptor:].cold.1
+ -[RBSProcessMonitor setUpdateHandler:].cold.1
+ -[RBSProcessMonitor updateConfiguration:].cold.4
+ -[RBSProcessMonitorConfiguration initWithRBSXPCCoder:].cold.3
+ -[RBSProcessPredicate initWithPredicate:].cold.1
+ -[RBSProcessState encodeWithRBSXPCCoder:].cold.1
+ -[RBSProcessStringPredicate initWithIdentifier:].cold.1
+ -[RBSTarget initWithRBSXPCCoder:].cold.2
+ -[RBSTerminateRequest initForAllManagedWithReason:service:].cold.1
+ -[RBSTerminateRequest initWithProcessIdentifier:context:].cold.1
+ -[RBSTerminateRequest initWithProcessIdentifier:context:].cold.2
+ -[RBSXPCCoder _removeValueForKey:].cold.1
+ -[RBSXPCCoder dealloc].cold.1
+ -[RBSXPCCoder encodeCollection:forKey:].cold.1
+ -[RBSXPCCoder encodeDictionary:forKey:].cold.1
+ -[RBSXPCCoder encodeObject:forKey:].cold.1
+ -[RBSXPCCoder encodeObject:forKey:].cold.2
+ -[RBSXPCCoder initWithMessage:].cold.1
+ -[RBSXPCMessage sendToConnection:replyQueue:completion:].cold.1
+ -[RBSXPCMessageReply send].cold.1
+ GCC_except_table0
+ GCC_except_table145
+ GCC_except_table146
+ OBJC_IVAR_$_RBSLaunchContext._launchAssertionIdentifier
+ OBJC_IVAR_$_RBSLaunchContext._launchRequestIdentifierToMachNameMap
+ RBSCreateDeserializedNSSecureEncodableObjectOfClassFromXPCDictionaryWithKey.cold.2
+ RBSCreateDeserializedNSSecureEncodableObjectOfClassFromXPCDictionaryWithKey.cold.3
+ RBSCurrentUserDirectory.cold.1
+ RBSSandboxCanAccessMachService.cold.1
+ RBSSerializeNSSecureEncodableObjectToXPCDictionaryWithKey.cold.1
+ RBSSystemRootDirectory.cold.1
+ RBSXPCDictionaryGetValue.cold.1
+ RBSXPCPackObject.cold.1
+ RBSandboxCanGetProcessInfo.cold.1
+ _BSXPCDecodeObjectForKey.cold.1
+ _BSXPCDecodeObjectFromContext.cold.14
+ _BSXPCEncodeDictionaryWithKey.cold.1
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _RBSAppViewServiceMachServiceName
+ _RBSAppViewServiceSessionVendingEntitlement
+ _RBSSandboxCanGetMachTaskName.cold.1
+ __27-[RBSConnection _handshake]_block_invoke.cold.6
+ __41-[RBSConnection registerServiceDelegate:]_block_invoke.cold.1
+ __44+[RBSXPCMessage messageForMethod:arguments:]_block_invoke.cold.1
+ __47-[RBSConnection async_willExpireAssertionsSoon]_block_invoke.cold.1
+ __56-[RBSXPCMessage sendToConnection:replyQueue:completion:]_block_invoke.114.cold.1
+ _assertionMap.cold.1
+ _objc_msgSend$substringToIndex:
+ _rbs_adapter_callout_queue.cold.1
+ _service.cold.1
+ rbs_adapter_log.cold.1
+ rbs_appnap_enabled_for_pid.cold.1
+ rbs_assertion_log.cold.1
+ rbs_best_effort_networking_log.cold.1
+ rbs_coder_log.cold.1
+ rbs_connection_log.cold.1
+ rbs_general_log.cold.1
+ rbs_jetsam_log.cold.1
+ rbs_job_log.cold.1
+ rbs_job_oversize_log.cold.1
+ rbs_message_log.cold.1
+ rbs_monitor_log.cold.1
+ rbs_power_log.cold.1
+ rbs_process_log.cold.1
+ rbs_resource_log.cold.1
+ rbs_shim_log.cold.1
+ rbs_sp_assertion_log.cold.1
+ rbs_sp_state_log.cold.1
+ rbs_sp_telemetry_log.cold.1
+ rbs_sp_therm_log.cold.1
+ rbs_state_log.cold.1
+ rbs_system_log.cold.1
+ rbs_test_log.cold.1
+ rbs_ttl_log.cold.1
- -[RBSConnection _handshake].cold.1
- -[RBSConnection _lock_connect].cold.1
- -[RBSConnection _lock_connect].cold.2
- -[RBSConnection _subscribeToProcessDeath:handler:].cold.1
- -[RBSConnection intendToExit:withStatus:].cold.1
- -[RBSConnection portForIdentifier:].cold.1
- -[RBSConnection processName:].cold.1
- -[RBSTerminateRequest initWithPredicate:context:allowLaunch:service:].cold.1
- GCC_except_table142
- GCC_except_table143
CStrings:
+ "T@\"NSDictionary\",C,N,V_launchRequestIdentifierToMachNameMap"
+ "T@\"RBSAssertionIdentifier\",&,N,V_launchAssertionIdentifier"
+ "_launchAssertionIdentifier"
+ "_launchRequestIdentifierToMachNameMap"
+ "com.apple.UIKit.vends-view-services"
+ "com.apple.uikit.viewservice."
+ "identityForAppViewServiceIdentifier:"
+ "launchAssertionIdentifier"
+ "launchRequestIdentifierToMachNameMap"
+ "setLaunchAssertionIdentifier:"
+ "setLaunchRequestIdentifierToMachNameMap:"
+ "substringToIndex:"

```
