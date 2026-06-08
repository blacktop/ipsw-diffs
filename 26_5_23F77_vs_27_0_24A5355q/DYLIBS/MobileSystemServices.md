## MobileSystemServices

> `/System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices`

```diff

 24.0.0.0.0
-  __TEXT.__text: 0x32d0
-  __TEXT.__auth_stubs: 0x880
+  __TEXT.__text: 0x30e0
   __TEXT.__objc_methlist: 0x274
   __TEXT.__const: 0x820
-  __TEXT.__cstring: 0xbc5
-  __TEXT.__unwind_info: 0x140
-  __TEXT.__objc_classname: 0x2f
-  __TEXT.__objc_methname: 0x82e
-  __TEXT.__objc_methtype: 0x20b
-  __TEXT.__objc_stubs: 0x600
-  __DATA_CONST.__got: 0xe0
+  __TEXT.__cstring: 0xbc7
+  __TEXT.__unwind_info: 0x100
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x250
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x288
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x448
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x6a0
   __AUTH_CONST.__objc_const: 0x3f0
+  __AUTH_CONST.__auth_got: 0x468
   __DATA.__objc_ivar: 0x28
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E3AF9000-7632-315D-90A2-D0958AA6F1A5
+  UUID: 0F81FAA4-8F04-3CD6-B35E-D6862224606C
   Functions: 65
-  Symbols:   377
-  CStrings:  294
+  Symbols:   381
+  CStrings:  153
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_retain_x9
- _objc_retainAutoreleasedReturnValue
Functions:
~ _MOLogWriteV -> _MOLogWrite : 712 -> 44
~ _MOLogWrite -> _MOLogWriteV : 44 -> 712
~ -[MOSplunkLogger _onQueue_loadConfiguration] : 368 -> 352
~ ___44-[MOSplunkLogger _onQueue_loadConfiguration]_block_invoke : 816 -> 780
~ -[MOSplunkLogger uploadEventsWithCompletion:] : 284 -> 280
~ ___45-[MOSplunkLogger uploadEventsWithCompletion:]_block_invoke_2 : 900 -> 872
~ ___45-[MOSplunkLogger uploadEventsWithCompletion:]_block_invoke_3 : 404 -> 396
~ -[MOSplunkLogger logEventNamed:value:] : 348 -> 340
~ ___38-[MOSplunkLogger logEventNamed:value:]_block_invoke : 216 -> 204
~ -[MOSplunkLogger URLSession:didReceiveChallenge:completionHandler:] : 476 -> 460
~ -[MOSplunkLogger setPath:] : 64 -> 12
~ -[MOSplunkLogger setEvents:] : 64 -> 12
~ -[MOSplunkLogger setQueue:] : 64 -> 12
~ -[MOSplunkLogger setVersion:] : 64 -> 12
~ -[MOSplunkLogger setSplunkUploadURL:] : 64 -> 12
~ -[MOSplunkLogger setConfigurationURL:] : 64 -> 12
~ -[MOSplunkLogger setSplunkTopic:] : 64 -> 12
~ -[MOSplunkLogger setSamplingPercentage:] : 64 -> 12
~ ___MOLogWriteV_block_invoke : 844 -> 892
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSMutableArray\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@52@0:8@16@24@32@40B48"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "JSONObjectWithData:options:error:"
- "MOSplunkLogger"
- "NSObject"
- "NSURLSessionDelegate"
- "Q16@0:8"
- "T#,R"
- "T@\"NSMutableArray\",&,N,V_events"
- "T@\"NSNumber\",&,N,V_samplingPercentage"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSString\",&,N,V_path"
- "T@\"NSString\",&,N,V_splunkTopic"
- "T@\"NSString\",&,N,V_version"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSURL\",&,N,V_configurationURL"
- "T@\"NSURL\",&,N,V_splunkUploadURL"
- "TB,N,V_allowInvalidCert"
- "TQ,R"
- "Td,N,V_lastSuccessfulConfigurationLoad"
- "URLByAppendingPathComponent:"
- "URLSession:didBecomeInvalidWithError:"
- "URLSession:didReceiveChallenge:completionHandler:"
- "URLSessionDidFinishEventsForBackgroundURLSession:"
- "URLWithString:"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_allowInvalidCert"
- "_configurationURL"
- "_events"
- "_lastSuccessfulConfigurationLoad"
- "_onQueue_loadConfiguration"
- "_path"
- "_queue"
- "_samplingPercentage"
- "_splunkTopic"
- "_splunkUploadURL"
- "_version"
- "addObject:"
- "allowInvalidCert"
- "authenticationMethod"
- "autorelease"
- "class"
- "configurationURL"
- "conformsToProtocol:"
- "count"
- "credentialForTrust:"
- "d"
- "d16@0:8"
- "dataTaskWithRequest:completionHandler:"
- "dataTaskWithURL:completionHandler:"
- "dataWithJSONObject:options:error:"
- "debugDescription"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "ephemeralSessionConfiguration"
- "floatValue"
- "hash"
- "init"
- "initWithName:configurationURL:splunkTopic:version:allowInvalidCert:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lastSuccessfulConfigurationLoad"
- "logEventNamed:value:"
- "mutableCopy"
- "numberWithUnsignedLongLong:"
- "objectForKeyedSubscript:"
- "path"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "previousFailureCount"
- "protectionSpace"
- "queue"
- "release"
- "removeAllObjects"
- "removeObjectAtIndex:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "serverTrust"
- "sessionWithConfiguration:delegate:delegateQueue:"
- "setAllowInvalidCert:"
- "setConfigurationURL:"
- "setEvents:"
- "setHTTPBody:"
- "setHTTPMethod:"
- "setLastSuccessfulConfigurationLoad:"
- "setObject:forKeyedSubscript:"
- "setPath:"
- "setQueue:"
- "setSamplingPercentage:"
- "setSplunkTopic:"
- "setSplunkUploadURL:"
- "setURL:"
- "setVersion:"
- "splunkTopic"
- "splunkUploadURL"
- "statusCode"
- "stringWithFormat:"
- "superclass"
- "timeIntervalSinceReferenceDate"
- "uploadEventsWithCompletion:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSURLSession\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8d16"
- "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
- "v32@0:8@16@24"
- "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
- "v40@0:8@16@24@?32"
- "version"
- "zone"

```
