## AppleServiceToolkit

> `/System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit`

```diff

 175.0.0.0.0
-  __TEXT.__text: 0x23fa4
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_methlist: 0x298c
-  __TEXT.__const: 0x15c
-  __TEXT.__cstring: 0x1cf9
-  __TEXT.__oslogstring: 0x14ee
-  __TEXT.__gcc_except_tab: 0xe74
-  __TEXT.__unwind_info: 0xa70
-  __TEXT.__objc_classname: 0x5d2
-  __TEXT.__objc_methname: 0x680c
-  __TEXT.__objc_methtype: 0x15fd
-  __TEXT.__objc_stubs: 0x4fc0
-  __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__const: 0x880
-  __DATA_CONST.__objc_classlist: 0x1b0
+  __TEXT.__text: 0x2b41c
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__objc_methlist: 0x2f24
+  __TEXT.__const: 0x164
+  __TEXT.__cstring: 0x2855
+  __TEXT.__oslogstring: 0x1e81
+  __TEXT.__gcc_except_tab: 0x10b4
+  __TEXT.__unwind_info: 0xbd8
+  __TEXT.__objc_classname: 0x72d
+  __TEXT.__objc_methname: 0x739e
+  __TEXT.__objc_methtype: 0x1a94
+  __TEXT.__objc_stubs: 0x5840
+  __DATA_CONST.__got: 0x350
+  __DATA_CONST.__const: 0xad8
+  __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x90
+  __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1850
-  __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x160
+  __DATA_CONST.__objc_selrefs: 0x1aa8
+  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x108
-  __AUTH_CONST.__auth_got: 0x3a0
+  __AUTH_CONST.__auth_got: 0x3a8
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x27c0
-  __AUTH_CONST.__objc_const: 0x61b0
+  __AUTH_CONST.__cfstring: 0x2960
+  __AUTH_CONST.__objc_const: 0x6dd8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0xf78
-  __DATA.__objc_ivar: 0x324
-  __DATA.__data: 0x6d0
-  __DATA.__bss: 0x138
-  __DATA_DIRTY.__objc_data: 0x168
+  __AUTH.__objc_data: 0x11a8
+  __DATA.__objc_ivar: 0x37c
+  __DATA.__data: 0x7f8
+  __DATA.__bss: 0x140
+  __DATA_DIRTY.__objc_data: 0x1b8
   __DATA_DIRTY.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1017
-  Symbols:   1384
-  CStrings:  1971
+  Functions: 1182
+  Symbols:   1584
+  CStrings:  2222
 
Symbols:
+ _OBJC_CLASS_$_ASTRepairSession
+ _OBJC_METACLASS_$_ASTSelfServiceDestination
+ _OBJC_CLASS_$_ASTConnectionArchiveSelfServiceSession
+ _OBJC_CLASS_$_NSXPCListener
+ _OBJC_METACLASS_$_ASTRepairSession
+ _OBJC_METACLASS_$_ASTConnectionArchiveSelfServiceSession
+ _OBJC_CLASS_$_ASTConnectionRetrieveInstructionalPromptDetails
+ _OBJC_CLASS_$_ASTConnectionRetrieveSelfServiceSuites
+ _kASTEndpointRetrieveInstructionalPromptDetails
+ _OBJC_CLASS_$_ASTConnectionRetrieveSelfServiceSuiteResults
+ _OBJC_CLASS_$_ASTSelfServiceDestination
+ _OBJC_METACLASS_$_ASTConnectionRetrieveInstructionalPromptDetails
+ _kASTEndpointArchiveSelfServiceSession
+ _kASTEndpointRetrieveSelfServiceSuiteResults
+ _OBJC_METACLASS_$_ASTConnectionRetrieveSelfServiceSuiteResults
+ _OBJC_METACLASS_$_ASTConnectionRetrieveSelfServiceSuites
+ _OBJC_METACLASS_$_ASTRepairSessionProvider
+ _kASTEndpointSelectSelfServiceSuite
+ _OBJC_CLASS_$_ASTRepairSessionProvider
+ _OBJC_CLASS_$_ASTConnectionSelectSelfServiceSuite
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_METACLASS_$_ASTConnectionSelectSelfServiceSuite
+ __dispatch_queue_attr_concurrent
+ _kASTEndpointRetrieveSelfServiceSuites
+ _objc_retain_x9
CStrings:
+ "suiteId"
+ "ping:"
+ "setEndpoint:"
+ "AST2 has no suites to run"
+ "[ASTSessionRepairProvider] Establishing connection..."
+ "showInstructionalPrompt:withConfirmation:"
+ "initWithInstructionID:type:language:locale:"
+ "-[ASTRepairSessionProvider cancelSuite]"
+ "setClientConnection:"
+ "ASTRepairDelegateProtocol"
+ "Wrong session phase (%!l(MISSING)d), skipping requesting the suites"
+ "serviceName"
+ "setListenerConnection:"
+ "v24@0:8@\"NSData\"16"
+ "ASTConnectionRetrieveSelfServiceSuiteResults"
+ "https://idiagnostics-uat.apple.com/%!@(MISSING)/v1.6/"
+ "suspend"
+ "-[ASTRepairSessionProvider estimatedTimeRemainingForTest:completion:]"
+ "v32@0:8@\"NSNumber\"16@\"NSDictionary\"24"
+ "[ASTRepairSession] %!s(MISSING)"
+ "!Q"
+ "-[ASTRepairSession requestSuitesAvailableWithCompletionHandler:]"
+ "initWithServiceName:"
+ "ASTConnectionArchiveSelfServiceSession"
+ "@\"<ASTRepairProtocol>\""
+ "https://idiagnostics-stage1.apple.com/%!@(MISSING)/v1.6/"
+ "_remoteRepairServer"
+ "v32@0:8@\"NSString\"16@\"NSString\"24"
+ "setSuitesAvailable:"
+ "_serviceName"
+ "-[ASTRepairSession requestSuiteSummary:completionHandler:]"
+ "@\"NSSet\""
+ "v40@?0@\"NSNumber\"8@\"NSString\"16@\"NSString\"24@\"NSError\"32"
+ "initWithSuiteID:"
+ "https://idiagnostics-prod2-rno.apple.com/%!@(MISSING)/v1.6/"
+ "-[ASTRepairSession updateTestSuiteImage:]"
+ "Requesting suite summary with a bad diagnostic event id"
+ "-[ASTRepairSessionProvider ping:]"
+ "Switching to the server session"
+ "sessionExistsForIdentities:ticketNumber:timeout:completion:"
+ "initWithMachServiceName:options:"
+ "requestAsset:withCompletion:"
+ "ASTConnectionRetrieveSelfServiceSuites"
+ "\x02\x15"
+ "entitlements"
+ "v40@?0@\"NSArray\"8@\"NSArray\"16@\"NSArray\"24@\"NSError\"32"
+ "https://idiagnostics-it2.apple.com/%!@(MISSING)/v1.6/"
+ "archive/session"
+ "Unexpected instructional prompt type: %!@(MISSING)"
+ "[SHOW INSTRUCTIONS] (%!@(MISSING))"
+ "_receiver"
+ "-[ASTRepairSessionProvider startTest:parameters:]"
+ "_entitlements"
+ "Running ASTSession in repair session only mode.."
+ "ASTRepairSessionProvider"
+ "completeTestSuite:description:"
+ "setRemoteObjectInterface:"
+ "-[ASTRepairSessionProvider requestAsset:withCompletion:]"
+ "estimatedTimeRemainingForTest:completion:"
+ "https://idiagnostics-mdn1.apple.com/%!@(MISSING)/v1.6/"
+ "-[ASTRepairSession estimatedTimeRemainingForTest:completion:]"
+ "_suites"
+ "[ASTRepairSession] Unable to write data: %!@(MISSING)"
+ "listenerConnection"
+ "setSuites:"
+ "suitesAvailable"
+ "updateTestSuiteProgress:"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "v32@0:8@\"NSString\"16@?<v@?@\"ASTSuiteResult\"@\"NSError\">24"
+ "-[ASTRepairSessionProvider updateTestSuiteProgress:]"
+ "receiver"
+ "-[ASTRepairSession updateTestSuiteProgress:]"
+ "_isGuided"
+ "endWithCompletionHandler:"
+ "Invalidating the active session"
+ "v32@0:8@\"ASTInstructionalPrompt\"16@?<v@?@\"NSNumber\"@\"NSString\">24"
+ "1.6"
+ "T@\"NSArray\",&,N,V_entitlements"
+ "[ASTSessionInfo queuedSuiteType: %!@(MISSING), isGuided: %!d(MISSING)]"
+ "initWithEndpoint:suites:"
+ "initWithDiagnosticEventID:"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "select/suite"
+ "startListening"
+ "Connection manager is nil"
+ "https://idiagnostics-prod2.apple.com/%!@(MISSING)/v1.6/"
+ "Running ASTSession in server session only mode.."
+ "T@\"ASTRepairSession\",&,N,V_repairSession"
+ "com.apple.Diagnostics.ServiceAliveCheckQueue"
+ "https://idiagnostics-reno.apple.com/%!@(MISSING)/v1.6/"
+ "repairAliveCheckQueue"
+ "-[ASTRepairSessionProvider completeTestSuite:description:]"
+ "https://idiagnostics-staging.apple.com/%!@(MISSING)/v1.6/"
+ "-[ASTMaterializedConnectionManager requestSessionArchiveWithSessionID:withPayloadSigner:allowsCellularAccess:completionHandler:]"
+ "NSXPCListenerDelegate"
+ "retrieve/suites"
+ "T@\"<ASTRepairProtocol>\",&,N,V_clientConnection"
+ "cancelSuite"
+ "sendTestResult:withCompletion:"
+ "[ASTRepairSession] Unable to start the connection: %!@(MISSING)"
+ "[ASTConnectionManager] Diagnostic event ID has a wrong format"
+ "-[ASTMaterializedConnectionManager requestInstructionalPromptDetailsWithInstructionID:type:withPayloadSigner:language:locale:allowsCellularAccess:completionHandler:]"
+ "setRepairSession:"
+ "setListener:"
+ "-[ASTRepairSessionProvider endWithCompletionHandler:]"
+ "initWithDelegate:"
+ "Bad instructional prompt data, identifier: %!@(MISSING), reference: %!@(MISSING), type: %!@(MISSING)"
+ "requestSuiteStart:withCompletionHandler:"
+ "[ASTSessionRepairProvider] %!s(MISSING)"
+ "setEntitlements:"
+ "[ASTSessionRepairProvider] Connection %!@(MISSING) broke with error %!@(MISSING)"
+ "v16@?0q8"
+ "_serviceCheckQueue"
+ "retrieve/instruction/details"
+ "repairSession"
+ "-[ASTRepairSessionProvider requestSuitesAvailableWithCompletionHandler:]"
+ "-[ASTRepairSessionProvider establishConnectionWithCompletionHandler:]"
+ "T@\"<ASTRepairProtocol>\",W,N,V_receiver"
+ "-[ASTRepairSessionProvider startListening]"
+ "-[ASTRepairSessionProvider updateTestSuiteImage:]"
+ "[ASTRepairSession] %!s(MISSING), suiteName: %!@(MISSING)"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "locale"
+ "-[ASTRepairSession showInstructionalPrompt:withConfirmation:]"
+ "https://idiagnostics-it1.apple.com/%!@(MISSING)/v1.6/"
+ "-[ASTRepairSession completeTestSuite:description:]"
+ "establishConnectionWithCompletionHandler:"
+ "retrieve/results"
+ "_listener"
+ "[ASTRepairSession] Starting..."
+ "v68@0:8@\"NSNumber\"16@\"NSString\"24@?<@\"NSData\"@?@\"NSData\"^@>32@\"NSString\"40@\"NSString\"48B56@?<v@?@\"NSArray\"@\"NSArray\"@\"NSArray\"@\"NSError\">60"
+ "interfaceWithProtocol:"
+ "initWithServiceName:entitlements:"
+ "[ASTSessionRepairProvider] Connection established!"
+ "localeIdentifier"
+ "T@\"NSSet\",&,N,V_suitesAvailable"
+ "-[ASTRepairSession requestSuiteStart:completionHandler:]"
+ "requestInstructionalPromptDetailsWithInstructionID:type:withPayloadSigner:language:locale:allowsCellularAccess:completionHandler:"
+ "setReceiver:"
+ "v68@0:8@16@24@?32@40@48B56@?60"
+ "requestSuiteResult:withCompletion:"
+ "setRepairAliveCheckQueue:"
+ "v40@0:8@\"ASTSession\"16@\"NSArray\"24@?<v@?q>32"
+ "primary"
+ "https://idiagnostics-qa.apple.com/%!@(MISSING)/v1.6/"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_serviceCheckQueue"
+ "https://idiagnostics-prod2-mdn.apple.com/%!@(MISSING)/v1.6/"
+ "T@\"NSXPCListener\",&,N,V_listener"
+ "requestSelfServiceSuiteResultsWithDiagnosticEventID:withPayloadSigner:allowsCellularAccess:completionHandler:"
+ "serviceCheckQueue"
+ "_clientConnection"
+ "@\"NSXPCConnection\""
+ "Error requesting the AST2 suites available: %!@(MISSING)"
+ "[ASTConnectionManager] Failed to retrieve suite run results, deid: %!@(MISSING), error %!@(MISSING)"
+ "-[ASTRepairSessionProvider requestSuiteResult:withCompletion:]"
+ "v24@0:8@\"NSNumber\"16"
+ "-[ASTMaterializedConnectionManager postSelectSelfServiceSuite:withPayloadSigner:allowsCellularAccess:completionHandler:]"
+ "v24@?0@\"NSNumber\"8@\"NSString\"16"
+ "@\"ASTRepairSession\""
+ "_configCode"
+ "[ASTSessionRepairProvider] New connection %!@(MISSING) requested for %!@(MISSING)"
+ "-[ASTRepairSession sendTestResult:error:]"
+ "v44@0:8@\"NSNumber\"16@?<@\"NSData\"@?@\"NSData\"^@>24B32@?<v@?@\"NSNumber\"@\"NSString\"@\"NSString\"@\"NSError\">36"
+ "downloadAsset:fileHandle:completionHandler:"
+ "@\"NSXPCListener\""
+ "T@\"NSString\",&,N,V_serviceName"
+ "https://idiagnostics-acstage-ause1.apple.com/%!@(MISSING)/v1.6/"
+ "[ASTConnectionManager] Bad instructional prompt details response"
+ "[ASTConnectionManager] Failed to retrieve prompt details results, error %!@(MISSING)"
+ "[ASTRepairSession] Unable to establish the connection: %!@(MISSING)"
+ "-[ASTRepairSession end]"
+ "startTest:parameters:"
+ "startWithCompletionHandler:"
+ "timeEstimateStr"
+ "[ASTRepairSession] %!s(MISSING), progress: %!@(MISSING)"
+ "truncateAtOffset:error:"
+ "https://idiagnostics-it.apple.com/%!@(MISSING)/v1.6/"
+ "-[ASTMaterializedConnectionManager requestSelfServiceSuitesAvailableWithConfigCode:withPayloadSigner:allowsCellularAccess:completionHandler:]"
+ "-[ASTRepairSessionProvider listener:shouldAcceptNewConnection:]"
+ "[ASTSessionRepairProvider] Unknown error while creating connection.."
+ "Guided session was detected."
+ "setExportedObject:"
+ "ASTRepairProtocol"
+ "progressForTest:completion:"
+ "_repairAliveCheckQueue"
+ "[ASTRepairSession] Unable to retrieve the asset: %!@(MISSING)"
+ "[ASTRepairSession] %!s(MISSING), testId: %!@(MISSING)"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"NSNumber\">24"
+ "T@\"NSArray\",&,N,V_suites"
+ "-[ASTRepairSessionProvider startWithCompletionHandler:]"
+ "Error requesting the repair suites available: %!@(MISSING)"
+ "_listenerConnection"
+ "initWithMachServiceName:"
+ "updateTestSuiteImage:"
+ "ASTRepairSession"
+ "[ASTConnectionManager] Self service session failed to archive with error %!@(MISSING)"
+ "_repairSession"
+ "ASTSelfServiceDestination"
+ "[ASTRepairSession] %!s(MISSING), testId: %!@(MISSING), parameters: %!@(MISSING)"
+ "[ASTConnectionManager] Self service session failed to retrieve the suites available for config: %!@(MISSING), error: %!@(MISSING)"
+ "_suitesAvailable"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"NSNumber\"@\"NSString\"@\"NSString\"@\"NSError\">24"
+ "-[ASTRepairSession startTest:parameters:]"
+ "T@\"NSXPCConnection\",&,N,V_connection"
+ "https://idiagnostics.apple.com/%!@(MISSING)/v1.6/"
+ "v24@?0@\"ASTSuiteResult\"8@\"NSError\"16"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_repairAliveCheckQueue"
+ "-[ASTRepairSession progressForTest:completion:]"
+ "Provider is nil, make sure to establish a session."
+ "T@\"<ASTRepairDelegateProtocol>\",W,N,V_delegate"
+ "postSelectSelfServiceSuite:withPayloadSigner:allowsCellularAccess:completionHandler:"
+ "-[ASTMaterializedConnectionManager requestSelfServiceSuiteResultsWithDiagnosticEventID:withPayloadSigner:allowsCellularAccess:completionHandler:]"
+ "sessionExistsForIdentities:ticketNumber:completion:"
+ "Tq,N,V_endpoint"
+ "[ASTSessionRepairProvider] Connection %!@(MISSING) established with remote runner service"
+ "-[ASTRepairSessionProvider requestSuiteStart:withCompletionHandler:]"
+ "setExportedInterface:"
+ "Error occurred trying to truncate file: %!@(MISSING)"
+ "[ASTConnectionManager] %!s(MISSING)"
+ "listener:shouldAcceptNewConnection:"
+ "\x014"
+ "T@\"<ASTRepairProtocol>\",&,V_remoteRepairServer"
+ "Bad instructional prompt instructionID: %!@(MISSING), reference: %!@(MISSING) or answer: %!@(MISSING)"
+ "T@\"NSString\",&,N,V_configCode"
+ "setServiceName:"
+ "https://idiagnostics-nwk1.apple.com/%!@(MISSING)/v1.6/"
+ "v44@0:8@\"NSString\"16@?<@\"NSData\"@?@\"NSData\"^@>24B32@?<v@?@\"NSArray\"@\"NSError\">36"
+ "-[ASTRepairSessionProvider showInstructionalPrompt:withConfirmation:]"
+ "TB,R,N,V_isGuided"
+ "Repaird returned suites to run: %!@(MISSING)"
+ "T@\"<ASTRepairDelegateProtocol>\",&,N,V_listenerConnection"
+ "com.apple.corerepair.diagnostics-controller"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "remoteRepairServer"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "v32@0:8@\"ASTTestResult\"16@?<v@?@\"NSError\">24"
+ "ASTConnectionSelectSelfServiceSuite"
+ "requestSelfServiceSuitesAvailableWithConfigCode:withPayloadSigner:allowsCellularAccess:completionHandler:"
+ "@32@0:8q16@24"
+ "valueForEntitlement:"
+ "setServiceCheckQueue:"
+ "[ASTConnectionManager] Self service session failed to archive"
+ "setRemoteRepairServer:"
+ "Repaird has no suites to run"
+ "_showInstructionalPromptWithData:"
+ "-[ASTRepairSessionProvider sendTestResult:withCompletion:]"
+ "AST returned suites to run: %!@(MISSING)"
+ "-[ASTRepairSession cancelSuite]"
+ "https://idiagnostics-uat1.apple.com/%!@(MISSING)/v1.6/"
+ "language"
+ "clientConnection"
+ "initWithConfigCode:"
+ "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
+ "writeData:error:"
+ "_endpoint"
+ "@\"<ASTRepairDelegateProtocol>\""
+ "Switching to the repair session"
+ "listener"
+ "-[ASTRepairSessionProvider progressForTest:completion:]"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "https://idiagnostics-it4-ause1.apple.com/%!@(MISSING)/v1.6/"
+ "v44@0:8@\"NSString\"16@?<@\"NSData\"@?@\"NSData\"^@>24B32@?<v@?@\"ASTSuiteResult\"@\"NSError\">36"
+ "Requesting suites with a bad config code"
+ "isGuided"
+ "[ASTConnectionManager] Failed to select suite with ID: %!@(MISSING), error %!@(MISSING)"
+ "ASTConnectionRetrieveInstructionalPromptDetails"
+ "activate"
+ "secondary"
+ "[ASTSessionRepairProvider] Failed entitlements check, invalidating connection"
- "https://idiagnostics-prod2-mdn.apple.com/%!@(MISSING)/v1.5/"
- "1.5"
- "https://idiagnostics-qa.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-it1.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-staging.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-uat.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-stage1.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-uat1.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-it4-ause1.apple.com/%!@(MISSING)/v1.5/"
- "\x013"
- "https://idiagnostics-prod2-rno.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-nwk1.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-reno.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-it2.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-acstage-ause1.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-it.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-prod2.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-mdn1.apple.com/%!@(MISSING)/v1.5/"
- "[ASTSessionInfo queuedSuiteType: %!@(MISSING)]"

```
