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
+ _OBJC_CLASS_$_ASTConnectionRetrieveInstructionalPromptDetails
+ _OBJC_CLASS_$_ASTConnectionRetrieveSelfServiceSuites
+ _OBJC_CLASS_$_ASTConnectionSelectSelfServiceSuite
+ _kASTEndpointRetrieveSelfServiceSuites
+ _OBJC_CLASS_$_ASTConnectionArchiveSelfServiceSession
+ _OBJC_METACLASS_$_ASTRepairSessionProvider
+ _OBJC_METACLASS_$_ASTSelfServiceDestination
+ _objc_retain_x9
+ _OBJC_METACLASS_$_ASTConnectionArchiveSelfServiceSession
+ _OBJC_METACLASS_$_ASTConnectionRetrieveSelfServiceSuiteResults
+ __dispatch_queue_attr_concurrent
+ _kASTEndpointSelectSelfServiceSuite
+ _OBJC_METACLASS_$_ASTConnectionRetrieveSelfServiceSuites
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$_ASTRepairSessionProvider
+ _OBJC_CLASS_$_ASTConnectionRetrieveSelfServiceSuiteResults
+ _OBJC_CLASS_$_ASTRepairSession
+ _OBJC_METACLASS_$_ASTConnectionRetrieveInstructionalPromptDetails
+ _kASTEndpointRetrieveInstructionalPromptDetails
+ _OBJC_CLASS_$_NSXPCConnection
+ _kASTEndpointRetrieveSelfServiceSuiteResults
+ _kASTEndpointArchiveSelfServiceSession
+ _OBJC_CLASS_$_ASTSelfServiceDestination
+ _OBJC_METACLASS_$_ASTConnectionSelectSelfServiceSuite
+ _OBJC_METACLASS_$_ASTRepairSession
+ _OBJC_CLASS_$_NSXPCListener
CStrings:
+ "initWithServiceName:"
+ "select/suite"
+ "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
+ "v40@?0@\"NSArray\"8@\"NSArray\"16@\"NSArray\"24@\"NSError\"32"
+ "[ASTSessionRepairProvider] Failed entitlements check, invalidating connection"
+ "initWithMachServiceName:options:"
+ "setListenerConnection:"
+ "repairAliveCheckQueue"
+ "[ASTSessionRepairProvider] Connection %!@(MISSING) established with remote runner service"
+ "T@\"NSXPCConnection\",&,N,V_connection"
+ "Repaird returned suites to run: %!@(MISSING)"
+ "initWithDelegate:"
+ "-[ASTRepairSession showInstructionalPrompt:withConfirmation:]"
+ "initWithInstructionID:type:language:locale:"
+ "-[ASTRepairSessionProvider listener:shouldAcceptNewConnection:]"
+ "_remoteRepairServer"
+ "setRemoteObjectInterface:"
+ "downloadAsset:fileHandle:completionHandler:"
+ "https://idiagnostics-it1.apple.com/%!@(MISSING)/v1.6/"
+ "-[ASTMaterializedConnectionManager postSelectSelfServiceSuite:withPayloadSigner:allowsCellularAccess:completionHandler:]"
+ "[ASTRepairSession] Unable to start the connection: %!@(MISSING)"
+ "ASTConnectionArchiveSelfServiceSession"
+ "https://idiagnostics-nwk1.apple.com/%!@(MISSING)/v1.6/"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "writeData:error:"
+ "https://idiagnostics-it.apple.com/%!@(MISSING)/v1.6/"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"NSNumber\">24"
+ "interfaceWithProtocol:"
+ "_serviceName"
+ "archive/session"
+ "Bad instructional prompt data, identifier: %!@(MISSING), reference: %!@(MISSING), type: %!@(MISSING)"
+ "Guided session was detected."
+ "sessionExistsForIdentities:ticketNumber:timeout:completion:"
+ "Invalidating the active session"
+ "[ASTSessionRepairProvider] Connection established!"
+ "[ASTSessionRepairProvider] Establishing connection..."
+ "ASTRepairSessionProvider"
+ "estimatedTimeRemainingForTest:completion:"
+ "-[ASTRepairSession requestSuiteStart:completionHandler:]"
+ "-[ASTRepairSession estimatedTimeRemainingForTest:completion:]"
+ "T@\"<ASTRepairProtocol>\",&,N,V_clientConnection"
+ "[ASTRepairSession] %!s(MISSING)"
+ "_repairAliveCheckQueue"
+ "@\"ASTRepairSession\""
+ "T@\"NSSet\",&,N,V_suitesAvailable"
+ "-[ASTRepairSession sendTestResult:error:]"
+ "setEntitlements:"
+ "@\"<ASTRepairProtocol>\""
+ "[ASTSessionRepairProvider] Connection %!@(MISSING) broke with error %!@(MISSING)"
+ "T@\"NSXPCListener\",&,N,V_listener"
+ "language"
+ "setExportedObject:"
+ "v24@0:8@\"NSData\"16"
+ "-[ASTMaterializedConnectionManager requestSelfServiceSuiteResultsWithDiagnosticEventID:withPayloadSigner:allowsCellularAccess:completionHandler:]"
+ "AST returned suites to run: %!@(MISSING)"
+ "clientConnection"
+ "_configCode"
+ "@\"NSXPCConnection\""
+ "initWithConfigCode:"
+ "T@\"NSArray\",&,N,V_entitlements"
+ "T@\"<ASTRepairProtocol>\",W,N,V_receiver"
+ "requestSelfServiceSuitesAvailableWithConfigCode:withPayloadSigner:allowsCellularAccess:completionHandler:"
+ "-[ASTRepairSession completeTestSuite:description:]"
+ "suspend"
+ "listener"
+ "v24@?0@\"NSNumber\"8@\"NSString\"16"
+ "setEndpoint:"
+ "v24@?0@\"ASTSuiteResult\"8@\"NSError\"16"
+ "setClientConnection:"
+ "_repairSession"
+ "[ASTConnectionManager] Diagnostic event ID has a wrong format"
+ "locale"
+ "updateTestSuiteImage:"
+ "https://idiagnostics-qa.apple.com/%!@(MISSING)/v1.6/"
+ "requestInstructionalPromptDetailsWithInstructionID:type:withPayloadSigner:language:locale:allowsCellularAccess:completionHandler:"
+ "v40@?0@\"NSNumber\"8@\"NSString\"16@\"NSString\"24@\"NSError\"32"
+ "-[ASTRepairSessionProvider requestAsset:withCompletion:]"
+ "-[ASTRepairSessionProvider requestSuiteResult:withCompletion:]"
+ "timeEstimateStr"
+ "sessionExistsForIdentities:ticketNumber:completion:"
+ "Requesting suite summary with a bad diagnostic event id"
+ "setExportedInterface:"
+ "[ASTConnectionManager] Self service session failed to archive with error %!@(MISSING)"
+ "setSuitesAvailable:"
+ "entitlements"
+ "https://idiagnostics-reno.apple.com/%!@(MISSING)/v1.6/"
+ "Unexpected instructional prompt type: %!@(MISSING)"
+ "_entitlements"
+ "https://idiagnostics-mdn1.apple.com/%!@(MISSING)/v1.6/"
+ "establishConnectionWithCompletionHandler:"
+ "[ASTConnectionManager] %!s(MISSING)"
+ "https://idiagnostics-prod2-rno.apple.com/%!@(MISSING)/v1.6/"
+ "_suites"
+ "progressForTest:completion:"
+ "ASTConnectionRetrieveInstructionalPromptDetails"
+ "[SHOW INSTRUCTIONS] (%!@(MISSING))"
+ "v44@0:8@\"NSString\"16@?<@\"NSData\"@?@\"NSData\"^@>24B32@?<v@?@\"NSArray\"@\"NSError\">36"
+ "primary"
+ "startTest:parameters:"
+ "Connection manager is nil"
+ "NSXPCListenerDelegate"
+ "setReceiver:"
+ "!Q"
+ "Error requesting the AST2 suites available: %!@(MISSING)"
+ "T@\"<ASTRepairDelegateProtocol>\",&,N,V_listenerConnection"
+ "-[ASTRepairSession startTest:parameters:]"
+ "@\"NSXPCListener\""
+ "[ASTRepairSession] %!s(MISSING), suiteName: %!@(MISSING)"
+ "requestAsset:withCompletion:"
+ "sendTestResult:withCompletion:"
+ "Switching to the server session"
+ "[ASTConnectionManager] Self service session failed to retrieve the suites available for config: %!@(MISSING), error: %!@(MISSING)"
+ "[ASTRepairSession] Unable to establish the connection: %!@(MISSING)"
+ "https://idiagnostics-staging.apple.com/%!@(MISSING)/v1.6/"
+ "-[ASTRepairSessionProvider startTest:parameters:]"
+ "@\"<ASTRepairDelegateProtocol>\""
+ "Provider is nil, make sure to establish a session."
+ "-[ASTRepairSessionProvider updateTestSuiteProgress:]"
+ "[ASTConnectionManager] Self service session failed to archive"
+ "endWithCompletionHandler:"
+ "setRemoteRepairServer:"
+ "[ASTConnectionManager] Bad instructional prompt details response"
+ "serviceCheckQueue"
+ "-[ASTRepairSessionProvider ping:]"
+ "https://idiagnostics-it4-ause1.apple.com/%!@(MISSING)/v1.6/"
+ "initWithEndpoint:suites:"
+ "localeIdentifier"
+ "truncateAtOffset:error:"
+ "cancelSuite"
+ "initWithSuiteID:"
+ "v44@0:8@\"NSNumber\"16@?<@\"NSData\"@?@\"NSData\"^@>24B32@?<v@?@\"NSNumber\"@\"NSString\"@\"NSString\"@\"NSError\">36"
+ "v68@0:8@\"NSNumber\"16@\"NSString\"24@?<@\"NSData\"@?@\"NSData\"^@>32@\"NSString\"40@\"NSString\"48B56@?<v@?@\"NSArray\"@\"NSArray\"@\"NSArray\"@\"NSError\">60"
+ "https://idiagnostics-uat1.apple.com/%!@(MISSING)/v1.6/"
+ "initWithDiagnosticEventID:"
+ "startListening"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "retrieve/results"
+ "setRepairSession:"
+ "TB,R,N,V_isGuided"
+ "v32@0:8@\"NSNumber\"16@\"NSDictionary\"24"
+ "_listenerConnection"
+ "activate"
+ "Repaird has no suites to run"
+ "repairSession"
+ "AST2 has no suites to run"
+ "[ASTRepairSession] Starting..."
+ "Error requesting the repair suites available: %!@(MISSING)"
+ "-[ASTRepairSession requestSuitesAvailableWithCompletionHandler:]"
+ "[ASTConnectionManager] Failed to select suite with ID: %!@(MISSING), error %!@(MISSING)"
+ "ASTSelfServiceDestination"
+ "Switching to the repair session"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_serviceCheckQueue"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v16@?0q8"
+ "-[ASTMaterializedConnectionManager requestInstructionalPromptDetailsWithInstructionID:type:withPayloadSigner:language:locale:allowsCellularAccess:completionHandler:]"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "showInstructionalPrompt:withConfirmation:"
+ "_isGuided"
+ "[ASTSessionInfo queuedSuiteType: %!@(MISSING), isGuided: %!d(MISSING)]"
+ "retrieve/suites"
+ "-[ASTRepairSession updateTestSuiteProgress:]"
+ "updateTestSuiteProgress:"
+ "-[ASTRepairSessionProvider completeTestSuite:description:]"
+ "Error occurred trying to truncate file: %!@(MISSING)"
+ "com.apple.corerepair.diagnostics-controller"
+ "-[ASTRepairSessionProvider estimatedTimeRemainingForTest:completion:]"
+ "[ASTSessionRepairProvider] New connection %!@(MISSING) requested for %!@(MISSING)"
+ "Running ASTSession in repair session only mode.."
+ "valueForEntitlement:"
+ "T@\"NSString\",&,N,V_configCode"
+ "[ASTRepairSession] %!s(MISSING), testId: %!@(MISSING)"
+ "-[ASTRepairSession updateTestSuiteImage:]"
+ "@32@0:8q16@24"
+ "-[ASTRepairSessionProvider updateTestSuiteImage:]"
+ "https://idiagnostics.apple.com/%!@(MISSING)/v1.6/"
+ "T@\"ASTRepairSession\",&,N,V_repairSession"
+ "-[ASTRepairSession end]"
+ "v32@0:8@\"NSString\"16@\"NSString\"24"
+ "suiteId"
+ "startWithCompletionHandler:"
+ "ASTRepairSession"
+ "postSelectSelfServiceSuite:withPayloadSigner:allowsCellularAccess:completionHandler:"
+ "_listener"
+ "isGuided"
+ "ASTRepairProtocol"
+ "https://idiagnostics-stage1.apple.com/%!@(MISSING)/v1.6/"
+ "Running ASTSession in server session only mode.."
+ "-[ASTRepairSessionProvider sendTestResult:withCompletion:]"
+ "v68@0:8@16@24@?32@40@48B56@?60"
+ "setListener:"
+ "-[ASTRepairSessionProvider endWithCompletionHandler:]"
+ "receiver"
+ "ping:"
+ "listener:shouldAcceptNewConnection:"
+ "remoteRepairServer"
+ "v44@0:8@\"NSString\"16@?<@\"NSData\"@?@\"NSData\"^@>24B32@?<v@?@\"ASTSuiteResult\"@\"NSError\">36"
+ "\x02\x15"
+ "setSuites:"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"NSNumber\"@\"NSString\"@\"NSString\"@\"NSError\">24"
+ "https://idiagnostics-acstage-ause1.apple.com/%!@(MISSING)/v1.6/"
+ "ASTConnectionSelectSelfServiceSuite"
+ "[ASTRepairSession] %!s(MISSING), testId: %!@(MISSING), parameters: %!@(MISSING)"
+ "requestSuiteResult:withCompletion:"
+ "-[ASTRepairSession progressForTest:completion:]"
+ "-[ASTRepairSession cancelSuite]"
+ "[ASTSessionRepairProvider] Unknown error while creating connection.."
+ "_clientConnection"
+ "_showInstructionalPromptWithData:"
+ "retrieve/instruction/details"
+ "ASTRepairDelegateProtocol"
+ "serviceName"
+ "-[ASTRepairSessionProvider requestSuiteStart:withCompletionHandler:]"
+ "https://idiagnostics-uat.apple.com/%!@(MISSING)/v1.6/"
+ "T@\"<ASTRepairProtocol>\",&,V_remoteRepairServer"
+ "_suitesAvailable"
+ "Tq,N,V_endpoint"
+ "-[ASTRepairSessionProvider cancelSuite]"
+ "T@\"NSString\",&,N,V_serviceName"
+ "https://idiagnostics-prod2-mdn.apple.com/%!@(MISSING)/v1.6/"
+ "v24@0:8@\"NSNumber\"16"
+ "-[ASTRepairSessionProvider showInstructionalPrompt:withConfirmation:]"
+ "-[ASTMaterializedConnectionManager requestSelfServiceSuitesAvailableWithConfigCode:withPayloadSigner:allowsCellularAccess:completionHandler:]"
+ "-[ASTRepairSessionProvider startListening]"
+ "\x014"
+ "initWithServiceName:entitlements:"
+ "v32@0:8@\"ASTInstructionalPrompt\"16@?<v@?@\"NSNumber\"@\"NSString\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"ASTSuiteResult\"@\"NSError\">24"
+ "suitesAvailable"
+ "1.6"
+ "ASTConnectionRetrieveSelfServiceSuiteResults"
+ "setServiceCheckQueue:"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "Bad instructional prompt instructionID: %!@(MISSING), reference: %!@(MISSING) or answer: %!@(MISSING)"
+ "[ASTConnectionManager] Failed to retrieve suite run results, deid: %!@(MISSING), error %!@(MISSING)"
+ "secondary"
+ "[ASTSessionRepairProvider] %!s(MISSING)"
+ "requestSuiteStart:withCompletionHandler:"
+ "[ASTRepairSession] Unable to retrieve the asset: %!@(MISSING)"
+ "Wrong session phase (%!l(MISSING)d), skipping requesting the suites"
+ "-[ASTRepairSessionProvider startWithCompletionHandler:]"
+ "https://idiagnostics-it2.apple.com/%!@(MISSING)/v1.6/"
+ "v40@0:8@\"ASTSession\"16@\"NSArray\"24@?<v@?q>32"
+ "_serviceCheckQueue"
+ "ASTConnectionRetrieveSelfServiceSuites"
+ "com.apple.Diagnostics.ServiceAliveCheckQueue"
+ "https://idiagnostics-prod2.apple.com/%!@(MISSING)/v1.6/"
+ "setServiceName:"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "completeTestSuite:description:"
+ "[ASTRepairSession] %!s(MISSING), progress: %!@(MISSING)"
+ "-[ASTMaterializedConnectionManager requestSessionArchiveWithSessionID:withPayloadSigner:allowsCellularAccess:completionHandler:]"
+ "T@\"<ASTRepairDelegateProtocol>\",W,N,V_delegate"
+ "listenerConnection"
+ "_receiver"
+ "setRepairAliveCheckQueue:"
+ "[ASTRepairSession] Unable to write data: %!@(MISSING)"
+ "_endpoint"
+ "-[ASTRepairSessionProvider progressForTest:completion:]"
+ "-[ASTRepairSession requestSuiteSummary:completionHandler:]"
+ "requestSelfServiceSuiteResultsWithDiagnosticEventID:withPayloadSigner:allowsCellularAccess:completionHandler:"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_repairAliveCheckQueue"
+ "initWithMachServiceName:"
+ "@\"NSSet\""
+ "-[ASTRepairSessionProvider requestSuitesAvailableWithCompletionHandler:]"
+ "T@\"NSArray\",&,N,V_suites"
+ "Requesting suites with a bad config code"
+ "-[ASTRepairSessionProvider establishConnectionWithCompletionHandler:]"
+ "v32@0:8@\"ASTTestResult\"16@?<v@?@\"NSError\">24"
+ "[ASTConnectionManager] Failed to retrieve prompt details results, error %!@(MISSING)"
- "https://idiagnostics-qa.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-reno.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-uat.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-nwk1.apple.com/%!@(MISSING)/v1.5/"
- "[ASTSessionInfo queuedSuiteType: %!@(MISSING)]"
- "https://idiagnostics-prod2-rno.apple.com/%!@(MISSING)/v1.5/"
- "\x013"
- "1.5"
- "https://idiagnostics-it2.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-it4-ause1.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-prod2-mdn.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-staging.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-it.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-mdn1.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-acstage-ause1.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-uat1.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-stage1.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-it1.apple.com/%!@(MISSING)/v1.5/"
- "https://idiagnostics-prod2.apple.com/%!@(MISSING)/v1.5/"

```
