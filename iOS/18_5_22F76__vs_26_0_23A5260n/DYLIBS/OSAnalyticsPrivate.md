## OSAnalyticsPrivate

> `/System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/OSAnalyticsPrivate`

```diff

-758.120.5.0.0
-  __TEXT.__text: 0x157f4
-  __TEXT.__auth_stubs: 0x9b0
-  __TEXT.__objc_methlist: 0xcac
+912.0.0.0.0
+  __TEXT.__text: 0x164d8
+  __TEXT.__auth_stubs: 0x9e0
+  __TEXT.__objc_methlist: 0xe84
   __TEXT.__const: 0x110
   __TEXT.__gcc_except_tab: 0xd4
-  __TEXT.__cstring: 0x1217
-  __TEXT.__oslogstring: 0x2166
-  __TEXT.__unwind_info: 0x340
-  __TEXT.__objc_classname: 0x157
-  __TEXT.__objc_methname: 0x2890
-  __TEXT.__objc_methtype: 0xf0e
-  __TEXT.__objc_stubs: 0x22e0
-  __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0x3b0
-  __DATA_CONST.__objc_classlist: 0x68
+  __TEXT.__cstring: 0x13f7
+  __TEXT.__oslogstring: 0x2175
+  __TEXT.__unwind_info: 0x360
+  __TEXT.__objc_classname: 0x1ec
+  __TEXT.__objc_methname: 0x2d17
+  __TEXT.__objc_methtype: 0x1464
+  __TEXT.__objc_stubs: 0x2500
+  __DATA_CONST.__got: 0x250
+  __DATA_CONST.__const: 0x3c8
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb60
+  __DATA_CONST.__objc_selrefs: 0xc70
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0xf8
-  __AUTH_CONST.__auth_got: 0x4e8
-  __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x21e0
-  __AUTH_CONST.__objc_const: 0x2080
+  __AUTH_CONST.__auth_got: 0x500
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__cfstring: 0x2300
+  __AUTH_CONST.__objc_const: 0x2698
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __DATA.__objc_ivar: 0x184
-  __DATA.__data: 0x1e0
-  __DATA_DIRTY.__objc_data: 0x410
+  __DATA.__objc_ivar: 0x18c
+  __DATA.__data: 0x3c0
+  __DATA.__bss: 0x10
+  __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 215043D1-B380-317F-AAB7-EB973F369FB7
-  Functions: 285
-  Symbols:   1350
-  CStrings:  1414
+  UUID: 1C2E45EF-2855-34AB-83CD-BC515DBC8251
+  Functions: 300
+  Symbols:   1454
+  CStrings:  1501
 
Symbols:
+ +[OSADeviceRecoveryEnvHelper sharedInstance]
+ +[OSADeviceRecoveryEnvHelper sharedInstance].cold.1
+ +[OSASubmitter endpointToString:]
+ +[OSASubmitter submitToUAT]
+ +[OverrideMountPathRequest supportsSecureCoding]
+ -[OSADeviceRecoveryEnvHelper .cxx_destruct]
+ -[OSADeviceRecoveryEnvHelper overrideMountPath:]
+ -[OSADeviceRecoveryEnvHelper releaseSandboxExtensions]
+ -[OSAHttpSubmitter URLSession:dataTask:didReceiveData:]
+ -[OSAHttpSubmitter URLSession:dataTask:didReceiveData:].cold.1
+ -[OSAHttpSubmitter URLSession:dataTask:didReceiveResponse:completionHandler:]
+ -[OSAHttpSubmitter URLSession:dataTask:didReceiveResponse:completionHandler:].cold.1
+ -[OSAHttpSubmitter URLSession:task:didCompleteWithError:]
+ -[OSAHttpSubmitter URLSession:task:didCompleteWithError:].cold.1
+ -[OSAHttpSubmitter URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:]
+ -[OSAHttpSubmitter URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:].cold.1
+ -[OSAHttpSubmitter abort].cold.1
+ -[OSAHttpSubmitter cancelCurrentTask]
+ -[OSAHttpSubmitter cancelCurrentTask].cold.1
+ -[OSAHttpSubmitter init]
+ -[OSAHttpSubmitter postContent:withHeaders:toEndpoint:]
+ -[OSASubmitter postContent:withHeaders:toEndpoint:]
+ -[OverrideMountPathRequest .cxx_destruct]
+ -[OverrideMountPathRequest encodeWithCoder:]
+ -[OverrideMountPathRequest initWithCoder:]
+ -[OverrideMountPathRequest initWithSandboxExtensions:]
+ -[OverrideMountPathRequest sandboxExtensions]
+ OBJC_IVAR_$_OSASubmitter._requestURL
+ _NSURLErrorDomain
+ _OBJC_CLASS_$_NSURLSession
+ _OBJC_CLASS_$_NSURLSessionConfiguration
+ _OBJC_CLASS_$_OSADeviceRecoveryEnvHelper
+ _OBJC_CLASS_$_OverrideMountPathRequest
+ _OBJC_IVAR_$_OSADeviceRecoveryEnvHelper._sandboxExtensions
+ _OBJC_IVAR_$_OSAHttpSubmitter._dataTask
+ _OBJC_IVAR_$_OverrideMountPathRequest._sandboxExtensions
+ _OBJC_METACLASS_$_OSADeviceRecoveryEnvHelper
+ _OBJC_METACLASS_$_OverrideMountPathRequest
+ _OSASandboxConsumeExtensionNoRelease
+ __OBJC_$_CLASS_METHODS_OSADeviceRecoveryEnvHelper
+ __OBJC_$_CLASS_METHODS_OverrideMountPathRequest
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_CLASS_PROP_LIST_OverrideMountPathRequest
+ __OBJC_$_INSTANCE_METHODS_OSADeviceRecoveryEnvHelper
+ __OBJC_$_INSTANCE_METHODS_OverrideMountPathRequest
+ __OBJC_$_INSTANCE_VARIABLES_OSADeviceRecoveryEnvHelper
+ __OBJC_$_INSTANCE_VARIABLES_OverrideMountPathRequest
+ __OBJC_$_PROP_LIST_OSAHttpSubmitter
+ __OBJC_$_PROP_LIST_OverrideMountPathRequest
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSURLSessionDataDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSURLSessionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSURLSessionTaskDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSURLSessionDataDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSURLSessionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSURLSessionTaskDelegate
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_NSURLSessionDataDelegate
+ __OBJC_$_PROTOCOL_REFS_NSURLSessionDelegate
+ __OBJC_$_PROTOCOL_REFS_NSURLSessionTaskDelegate
+ __OBJC_CLASS_PROTOCOLS_$_OSAHttpSubmitter
+ __OBJC_CLASS_PROTOCOLS_$_OverrideMountPathRequest
+ __OBJC_CLASS_RO_$_OSADeviceRecoveryEnvHelper
+ __OBJC_CLASS_RO_$_OverrideMountPathRequest
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_LABEL_PROTOCOL_$_NSURLSessionDataDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSURLSessionDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSURLSessionTaskDelegate
+ __OBJC_METACLASS_RO_$_OSADeviceRecoveryEnvHelper
+ __OBJC_METACLASS_RO_$_OverrideMountPathRequest
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ __OBJC_PROTOCOL_$_NSURLSessionDataDelegate
+ __OBJC_PROTOCOL_$_NSURLSessionDelegate
+ __OBJC_PROTOCOL_$_NSURLSessionTaskDelegate
+ ___39-[PCCProxiedDevice handleMessage:from:]_block_invoke.125
+ ___42-[PCCProxyingDevice finishRequest:result:]_block_invoke.421
+ ___44+[OSADeviceRecoveryEnvHelper sharedInstance]_block_invoke
+ _kOSASubmissionDomain
+ _objc_msgSend$addSuiteNamed:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$cancelCurrentTask
+ _objc_msgSend$createRetiredDirectoriesForUser:
+ _objc_msgSend$dataTaskWithRequest:
+ _objc_msgSend$decodeArrayOfObjectsOfClass:forKey:
+ _objc_msgSend$defaultSessionConfiguration
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$endpointToString:
+ _objc_msgSend$finishTasksAndInvalidate
+ _objc_msgSend$initWithSandboxExtensions:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$isInDeviceRecoveryEnvironment
+ _objc_msgSend$longLongValue
+ _objc_msgSend$markFile:withKey:value:
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$overrideMountPath
+ _objc_msgSend$postContent:withHeaders:toEndpoint:
+ _objc_msgSend$recoveryModeReason
+ _objc_msgSend$releaseSandboxExtensions
+ _objc_msgSend$sandboxExtensions
+ _objc_msgSend$sessionWithConfiguration:delegate:delegateQueue:
+ _objc_msgSend$set_usesNWLoader:
+ _objc_msgSend$submitToUAT
+ _objc_retainAutoreleasedReturnValue
+ _sandbox_extension_release
+ _sharedInstance._sharedInstance
+ _sharedInstance.onceToken
- -[OSAHttpSubmitter cleanupConnectionAndDisable:]
- -[OSAHttpSubmitter connection:didFailWithError:]
- -[OSAHttpSubmitter connection:didReceiveData:]
- -[OSAHttpSubmitter connection:didReceiveResponse:]
- -[OSAHttpSubmitter connection:didSendBodyData:totalBytesWritten:totalBytesExpectedToWrite:]
- -[OSAHttpSubmitter connection:didSendBodyData:totalBytesWritten:totalBytesExpectedToWrite:].cold.1
- -[OSAHttpSubmitter connectionDidFinishLoading:]
- -[OSAHttpSubmitter initWithEndpoint:]
- -[OSAHttpSubmitter postContent:withHeaders:]
- -[OSAHttpSubmitter startConnection:]
- -[OSAHttpSubmitter submissionURL]
- -[OSASubmitter postContent:withHeaders:]
- -[OSASubmitter submissionURL]
- _OBJC_CLASS_$_NSURLConnection
- _OBJC_IVAR_$_OSAHttpSubmitter._connection
- _OBJC_IVAR_$_OSAHttpSubmitter._submissionURL
- ___39-[PCCProxiedDevice handleMessage:from:]_block_invoke.118
- ___42-[PCCProxyingDevice finishRequest:result:]_block_invoke.416
- _objc_msgSend$_initWithRequest:delegate:usesCache:maxContentLength:startImmediately:connectionProperties:
- _objc_msgSend$absoluteString
- _objc_msgSend$cleanupConnectionAndDisable:
- _objc_msgSend$performSelectorOnMainThread:withObject:waitUntilDone:
- _objc_msgSend$postContent:withHeaders:
- _objc_msgSend$start
- _objc_msgSend$submissionURL
CStrings:
+ "%s"
+ "-[OSAHttpSubmitter URLSession:dataTask:didReceiveData:]"
+ "-[OSAHttpSubmitter URLSession:dataTask:didReceiveResponse:completionHandler:]"
+ "-[OSAHttpSubmitter URLSession:task:didCompleteWithError:]"
+ "-[OSAHttpSubmitter abort]"
+ "-[OSAHttpSubmitter cancelCurrentTask]"
+ "1"
+ "@\"NSURLSessionDataTask\""
+ "@24@0:8@\"NSCoder\"16"
+ "DnUOverride"
+ "Failed to release sandbox extension: %s (%i)"
+ "NSCoding"
+ "NSSecureCoding"
+ "NSURLSessionDataDelegate"
+ "NSURLSessionDelegate"
+ "NSURLSessionTaskDelegate"
+ "OHTTP"
+ "OSADeviceRecoveryEnvHelper"
+ "OverrideMountPathRequest"
+ "Skipping group transfer from proxy-configured device with disablePushOnConnection set"
+ "T@\"NSArray\",R,V_sandboxExtensions"
+ "TB,R"
+ "UAT"
+ "UATSubmissionServer"
+ "URLSession:dataTask:didBecomeDownloadTask:"
+ "URLSession:dataTask:didBecomeStreamTask:"
+ "URLSession:dataTask:didReceiveData:"
+ "URLSession:dataTask:didReceiveResponse:completionHandler:"
+ "URLSession:dataTask:willCacheResponse:completionHandler:"
+ "URLSession:didBecomeInvalidWithError:"
+ "URLSession:didCreateTask:"
+ "URLSession:didReceiveChallenge:completionHandler:"
+ "URLSession:task:didCompleteWithError:"
+ "URLSession:task:didFinishCollectingMetrics:"
+ "URLSession:task:didReceiveChallenge:completionHandler:"
+ "URLSession:task:didReceiveInformationalResponse:"
+ "URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:"
+ "URLSession:task:needNewBodyStream:"
+ "URLSession:task:needNewBodyStreamFromOffset:completionHandler:"
+ "URLSession:task:willBeginDelayedRequest:completionHandler:"
+ "URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:"
+ "URLSession:taskIsWaitingForConnectivity:"
+ "URLSessionDidFinishEventsForBackgroundURLSession:"
+ "Unified"
+ "_dataTask"
+ "_requestURL"
+ "_sandboxExtensions"
+ "addSuiteNamed:"
+ "autoCleanupProxiedFiles"
+ "boolForKey:"
+ "ca1-ohttp"
+ "cancelCurrentTask"
+ "com.apple.osanalytics.factoryproxysync"
+ "createRetiredDirectoriesForUser:"
+ "dataTaskWithRequest:"
+ "decodeArrayOfObjectsOfClass:forKey:"
+ "defaultSessionConfiguration"
+ "disablePushOnConnection"
+ "dnu-override"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "endpoint"
+ "endpointToString:"
+ "failed"
+ "finishTasksAndInvalidate"
+ "https://gateway-oblivious.apple.com/iphonesubmissions/convert.jsp"
+ "initWithCoder:"
+ "initWithSandboxExtensions:"
+ "initWithSuiteName:"
+ "isInDeviceRecoveryEnvironment"
+ "longLongValue"
+ "markFile:withKey:value:"
+ "numberWithLongLong:"
+ "overrideMountPath"
+ "overrideMountPath:"
+ "partial success"
+ "postContent:withHeaders:toEndpoint:"
+ "recoveryModeReason"
+ "releaseSandboxExtensions"
+ "sandboxExtensions"
+ "sessionWithConfiguration:delegate:delegateQueue:"
+ "set_usesNWLoader:"
+ "submitToUAT"
+ "supportsSecureCoding"
+ "v24@0:8@\"NSCoder\"16"
+ "v24@0:8@\"NSURLSession\"16"
+ "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
+ "v32@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24"
+ "v36@0:8@16@24i32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSData\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionDownloadTask\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionStreamTask\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSError\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLSessionTaskMetrics\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@?<v@?@\"NSInputStream\">32"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSCachedURLResponse\"32@?<v@?@\"NSCachedURLResponse\">40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLResponse\"32@?<v@?q>40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLAuthenticationChallenge\"32@?<v@?q@\"NSURLCredential\">40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLRequest\"32@?<v@?q@\"NSURLRequest\">40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32@?<v@?@\"NSInputStream\">40"
+ "v48@0:8@16@24q32@?40"
+ "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32@\"NSURLRequest\"40@?<v@?@\"NSURLRequest\">48"
+ "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32q40q48"
+ "v56@0:8@16@24@32@40@?48"
+ "v56@0:8@16@24q32q40q48"
+ "x-dre-submission"
- "@\"NSURL\""
- "@\"NSURLConnection\""
- "ABORTED"
- "ABORTED - %@"
- "B32@0:8@16@?24"
- "B40@0:8@16@24@?32"
- "DoNotSubmit"
- "SUCCESS"
- "Skipping DoNotSubmit tagged report at %{public}@"
- "Submission aborted after %u jobs"
- "T@\"NSURL\",R"
- "Using debug/UAT submission URL: '%@'"
- "_connection"
- "_initWithRequest:delegate:usesCache:maxContentLength:startImmediately:connectionProperties:"
- "_submissionURL"
- "absoluteString"
- "cleanupConnectionAndDisable:"
- "connection:didFailWithError:"
- "connection:didReceiveData:"
- "connection:didReceiveResponse:"
- "connection:didSendBodyData:totalBytesWritten:totalBytesExpectedToWrite:"
- "connectionDidFinishLoading:"
- "empty"
- "other"
- "performSelectorOnMainThread:withObject:waitUntilDone:"
- "postContent:withHeaders:"
- "start"
- "startConnection:"
- "submissionURL"
- "v48@0:8@16q24q32q40"

```
