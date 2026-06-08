## MLRuntime

> `/System/Library/PrivateFrameworks/MLRuntime.framework/MLRuntime`

```diff

-111.1.0.0.0
-  __TEXT.__text: 0x6a64
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_methlist: 0x968
+113.0.0.0.0
+  __TEXT.__text: 0x611c
+  __TEXT.__objc_methlist: 0x958
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x5fe
+  __TEXT.__cstring: 0x5bd
   __TEXT.__oslogstring: 0x470
   __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__unwind_info: 0x258
-  __TEXT.__objc_classname: 0x244
-  __TEXT.__objc_methname: 0x16f7
-  __TEXT.__objc_methtype: 0x446
-  __TEXT.__objc_stubs: 0x10e0
-  __DATA_CONST.__got: 0x170
-  __DATA_CONST.__const: 0x178
+  __TEXT.__unwind_info: 0x238
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x150
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x668
+  __DATA_CONST.__objc_selrefs: 0x660
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x1c8
+  __DATA_CONST.__got: 0x168
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x7c0
+  __AUTH_CONST.__cfstring: 0x760
   __AUTH_CONST.__objc_const: 0x13a8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x320
   __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x420

   - /System/Library/PrivateFrameworks/TrialProto.framework/TrialProto
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 88C4C24B-31C2-3ABB-B848-1E9F9074B633
-  Functions: 200
-  Symbols:   897
-  CStrings:  503
+  UUID: 95068F7D-F084-35F1-AE87-9AF3EE2B9C73
+  Functions: 190
+  Symbols:   870
+  CStrings:  154
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x24
+ _objc_retain_x5
+ _objc_retain_x8
- -[MLRTrialDediscoTaskResult initWithJSONResult:identifier:]
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- ___59-[MLRServiceClient donateJSONResult:identifier:completion:]_block_invoke
- ___59-[MLRServiceClient donateJSONResult:identifier:completion:]_block_invoke_2
- ___59-[MLRServiceClient donateJSONResult:identifier:completion:]_block_invoke_3
- ___block_descriptor_56_e8_32s40s48bs_e26_v16?0"<DESFullService>"8ls32l8s40l8s48l8
- _objc_msgSend$donateJSONResult:identifier:completion:
- _objc_msgSend$initWithJSONResult:namespaceName:factorName:additionalKeyVariables:
- _objc_msgSend$performOnRemoteObjectWithBlock:errorHandler:
- _objc_retain_x28
CStrings:
+ "donateJSONResult:identifier:completion is deprecated."
- "#16@0:8"
- ".cxx_destruct"
- "@\"<MLROnDemandTaskPerforming>\""
- "@\"<PKModularService>\"16@0:8"
- "@\"<PKModularService>\"24@0:8@\"NSDictionary\"16"
- "@\"MLRTaskAttachments\""
- "@\"MLRTaskParameters\""
- "@\"MLRTaskResult\"32@0:8@\"MLRTask\"16^@24"
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"TRIClient\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24^@32"
- "@48@0:8@16@24@32@40"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSXPCConnection\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B28@0:8@16B24"
- "B32@0:8@16^@24"
- "B56@0:8@16@24@32@40^@48"
- "DediscoUploadPrototype"
- "JSONObjectWithData:options:error:"
- "JSONResult must be not be nil."
- "MLRDonationManager"
- "MLRExtensionHostProtocol"
- "MLRExtensionPrincipalClass"
- "MLRExtensionRemoteContext"
- "MLRExtensionRemoteProtocol"
- "MLRExtensionService_Subsystem"
- "MLROnDemandConnectionHandler"
- "MLROnDemandPlugin"
- "MLROnDemandRemoteProtocol"
- "MLROnDemandTaskPerforming"
- "MLRSandboxExtensionRequest"
- "MLRServiceClient"
- "MLRTask"
- "MLRTaskAttachments"
- "MLRTaskParameters"
- "MLRTaskResult"
- "MLRTrialDediscoRecipe"
- "MLRTrialDediscoTaskResult"
- "MLRTrialTask"
- "MLRTrialTaskResult"
- "MLRuntime"
- "NSCoding"
- "NSExtensionRequestHandling"
- "NSObject"
- "NSSecureCoding"
- "PKModularService"
- "PPM_DIRECT_UPLOAD"
- "Q"
- "Q16@0:8"
- "Q32@0:8@16Q24"
- "T#,R"
- "T@\"<MLROnDemandTaskPerforming>\",&,N,V_pluginPrincipal"
- "T@\"MLRTaskAttachments\",R,C,N,V_attachments"
- "T@\"MLRTaskParameters\",R,N,V_parameters"
- "T@\"NSArray\",R,C,N,V_URLs"
- "T@\"NSArray\",R,C,N,V_attachmentURLs"
- "T@\"NSData\",R,N,V_vector"
- "T@\"NSDictionary\",R,C,N"
- "T@\"NSDictionary\",R,C,N,V_additionalKeyVariables"
- "T@\"NSDictionary\",R,C,N,V_recipeUserInfo"
- "T@\"NSDictionary\",R,N,V_JSONResult"
- "T@\"NSDictionary\",R,N,V_dediscoTaskConfig"
- "T@\"NSDictionary\",R,N,V_dpConfig"
- "T@\"NSDictionary\",R,N,V_encodingSchema"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_namespaceName"
- "T@\"NSString\",R,C,N,V_recipeFactorName"
- "T@\"NSString\",R,N,V_baseKeyFormat"
- "T@\"NSXPCConnection\",W,N,V_xpcConnection"
- "T@\"TRIClient\",R,N,V_triClient"
- "T@,R"
- "TB,R"
- "TB,R,N,V_requireWrite"
- "TQ,R"
- "TQ,R,N,V_count"
- "URLByResolvingSymlinksInPath"
- "URLByStandardizingPath"
- "URLs"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_EXConnectionHandler"
- "_EXMainConnectionHandler"
- "_JSONResult"
- "_URLs"
- "_additionalKeyVariables"
- "_attachmentURLs"
- "_attachments"
- "_baseKeyFormat"
- "_connection"
- "_count"
- "_createXPCConnection:error:"
- "_dediscoTaskConfig"
- "_dpConfig"
- "_encodingSchema"
- "_extensionAuxiliaryHostProtocol"
- "_extensionAuxiliaryVendorProtocol"
- "_locateWithExtensionID:"
- "_namespaceName"
- "_numberValueForKey:"
- "_parameters"
- "_performTask:forPluginID:isSynchronous:completionHandler:"
- "_pluginPrincipal"
- "_queue"
- "_recipeFactorName"
- "_recipeUserInfo"
- "_requireWrite"
- "_startListening:"
- "_stopQueue"
- "_taskExecutionQueue"
- "_triClient"
- "_vector"
- "_xpcConnection"
- "addEntriesFromDictionary:"
- "addObject:"
- "additionalKeyVariables"
- "appendFormat:"
- "appendString:"
- "array"
- "arrayWithObjects:count:"
- "attachmentURLsForBasename:"
- "autorelease"
- "baseKeyFormat"
- "baseKeyFromFormat:variables:"
- "beginRequestWithExtensionContext:"
- "beginUsing:withBundle:"
- "boolValue"
- "boolValueForKey:defaultValue:"
- "bundleIdentifier"
- "cStringUsingEncoding:"
- "characterAtIndex:"
- "characterSetWithCharactersInString:"
- "class"
- "code"
- "communicationsFailed:"
- "conformsToProtocol:"
- "copy"
- "coreChannel"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d32@0:8@16d24"
- "dataWithContentsOfURL:options:error:"
- "dealloc"
- "debugDescription"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "dediscoTaskConfig"
- "defaultManager"
- "description"
- "dictionary"
- "dictionaryRepresentation"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "domain"
- "donateJSONResult:identifier:completion:"
- "doubleValue"
- "doubleValueForKey:defaultValue:"
- "dpConfig"
- "encodeAndUploadToDediscoWithIdentifier:measurements:withEncodingSchemas:metadata:completion:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endUsing:"
- "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
- "errorWithDomain:code:userInfo:"
- "exceptionWithName:reason:userInfo:"
- "executeQuery:"
- "experimentIdentifiersWithNamespaceName:"
- "extensionPointIdentifierQuery:"
- "f28@0:8@16f24"
- "fileExistsAtPath:"
- "fileURLWithPath:isDirectory:"
- "fileValue"
- "firstObject"
- "floatValue"
- "floatValueForKey:defaultValue:"
- "hasDirectoryPath"
- "hasOnDemandLaunchEntitlement:"
- "hasPath"
- "hasSuffix:"
- "hash"
- "identifier must be not be nil."
- "init"
- "initForPlugInKit"
- "initForPlugInKitWithOptions:"
- "initWithAssetURL:configOverride:error:"
- "initWithCoder:"
- "initWithConnection:"
- "initWithContentsOfURL:error:"
- "initWithDESRecipe:"
- "initWithDomain:code:userInfo:"
- "initWithInputItems:listenerEndpoint:contextUUID:"
- "initWithInputItems:listenerEndpoint:contextUUID:plugin:"
- "initWithJSONResult:"
- "initWithJSONResult:identifier:"
- "initWithJSONResult:namespaceName:factorName:additionalKeyVariables:"
- "initWithJSONResult:unprivatizedVector:"
- "initWithMachServiceName:options:"
- "initWithParameters:attachments:"
- "initWithParametersDict:"
- "initWithPrincipalObject:"
- "initWithTriClient:"
- "initWithURL:error:"
- "initWithURLs:"
- "initWithURLs:requireWrite:"
- "integerValue"
- "integerValueForKey:defaultValue:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isValidJSONObject:"
- "lastPathComponent"
- "length"
- "levelForFactor:withNamespaceName:"
- "localizedDescription"
- "mainBundle"
- "makeXPCConnectionWithError:"
- "mlrDediscoMetadata"
- "mlr_boolValueForKey:defaultValue:"
- "mlr_clientWithMLRTask:"
- "mlr_dictionaryValueForKey:"
- "mlr_doubleValueForKey:defaultValue:"
- "mlr_floatValueForKey:defaultValue:"
- "mlr_integerValueForKey:defaultValue:"
- "mlr_namespaceNameWithMLRTask:"
- "mlr_stringValueForKey:defaultValue:"
- "mlr_unsignedIntegerValueForKey:defaultValue:"
- "mutableCopy"
- "namespaceName"
- "numberWithInt:"
- "objectForKeyedSubscript:"
- "onDemandPluginIDs"
- "path"
- "performOnRemoteObjectWithBlock:errorHandler:"
- "performOnRemoteObjectWithBlock:isSynchronous:errorHandler:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performSynchronouslyOnRemoteObjectWithBlock:errorHandler:"
- "performTask:completionHandler:"
- "performTask:error:"
- "performTask:forPluginID:completionHandler:"
- "performTaskInternal:completionHandler:"
- "pluginPrincipal"
- "principalObject"
- "processInfo"
- "q32@0:8@16q24"
- "queue"
- "rangeOfCharacterFromSet:options:range:"
- "recipeFactorName"
- "record:data:encodingSchema:metadata:errorOut:"
- "recordSetForTask:"
- "refresh"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "requireWrite"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "sendEventErrorForBundleID:error:"
- "sendEventEvaluationForBundleID:evaluationID:duration:deferred:success:error:downloadedAttachmentCount:"
- "sendEventEvaluationSessionFinishForBundleID:success:"
- "sendEventEvaluationSessionStartForBundleID:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setObject:forKeyedSubscript:"
- "setPluginPrincipal:"
- "setQueue:"
- "setRemoteObjectInterface:"
- "setWithObjects:"
- "setXpcConnection:"
- "sharedConnection"
- "sharedInstance"
- "shouldAcceptXPCConnection:"
- "string"
- "stringValueForKey:defaultValue:"
- "stringWithFormat:"
- "submitForTask:error:"
- "submitWithTRIClient:error:"
- "substringWithRange:"
- "superclass"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "synchronouslyPerformTask:forPluginID:error:"
- "systemUptime"
- "triClient"
- "underlyingErrors"
- "unsignedIntegerValue"
- "unsignedIntegerValueForKey:defaultValue:"
- "v16@0:8"
- "v16@?0@\"<DESFullService>\"8"
- "v24@0:8@\"<PKSubsystemServicePersonality>\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSExtensionContext\"16"
- "v24@0:8@16"
- "v32@0:8@\"<PKSubsystemServicePersonality>\"16@\"NSBundle\"24"
- "v32@0:8@\"MLRTask\"16@?<v@?@\"MLRTaskResult\"@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@?16@?24"
- "v36@0:8@?16B24@?28"
- "v40@0:8@16@24@?32"
- "v44@0:8@16@24B32@?36"
- "v56@0:8@16@24@32@40@?48"
- "variablesFromTrialClient:"
- "xpcConnection"
- "zone"

```
