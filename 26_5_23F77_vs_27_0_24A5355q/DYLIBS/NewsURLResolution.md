## NewsURLResolution

> `/System/Library/PrivateFrameworks/NewsURLResolution.framework/NewsURLResolution`

```diff

-5883.0.0.0.0
-  __TEXT.__text: 0x1d4c
-  __TEXT.__auth_stubs: 0x1e0
+5916.1.0.0.0
+  __TEXT.__text: 0x1c60
   __TEXT.__objc_methlist: 0x37c
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x5af
+  __TEXT.__cstring: 0x5b8
   __TEXT.__oslogstring: 0x44
   __TEXT.__unwind_info: 0xf0
-  __TEXT.__objc_classname: 0xda
-  __TEXT.__objc_methname: 0x73b
-  __TEXT.__objc_methtype: 0x21e
-  __TEXT.__objc_stubs: 0x4e0
-  __DATA_CONST.__got: 0x88
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x190
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_selrefs: 0x230
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xf8
+  __DATA_CONST.__got: 0x80
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0x6d8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x28
   __DATA.__data: 0x180

   - /System/Library/PrivateFrameworks/NewsTransport.framework/NewsTransport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4252F080-6A1B-3D59-B32E-196FDEF2E532
-  Functions: 66
-  Symbols:   307
-  CStrings:  173
+  UUID: B696D020-73E4-3322-B4D6-FE9093B01C8E
+  Functions: 65
+  Symbols:   302
+  CStrings:  41
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x22
+ _objc_retain_x8
- _OUTLINED_FUNCTION_5
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retain
- _objc_retainAutoreleasedReturnValue
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<NRBloomFilterInfoService>\""
- "@\"FCAsyncOnceOperation\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NTPBBloomFilterInfo\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@?"
- "@?16@0:8"
- "@?<v@?@\"NSURL\"@\"NSError\">16@0:8"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NDURLResolutionService"
- "NRAdditions"
- "NRBloomFilterInfoService"
- "NRNewsDaemonBloomFilterInfoService"
- "NRNewsURLResolutionOperation"
- "NRURLResolutionManager"
- "NRURLResolutionOperation"
- "NRWebURLResolutionOperation"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<NRBloomFilterInfoService>\",R,N,V_bloomFilterInfoService"
- "T@\"FCAsyncOnceOperation\",R,N,V_fetchOnceOperation"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSURL\",C,N,V_resultNewsURL"
- "T@\"NSURL\",C,N,V_resultWebURL"
- "T@\"NSURL\",R,C,N,V_newsURL"
- "T@\"NSURL\",R,C,N,V_webURL"
- "T@\"NTPBBloomFilterInfo\",C,N,V_bloomFilterInfo"
- "T@?,C,N"
- "T@?,C,N,V_resolutionCompletion"
- "TB,R,N"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_bloomFilterInfo"
- "_bloomFilterInfoService"
- "_fetchBloomFilterInfoWithCompletion:"
- "_fetchOnceOperation"
- "_newsURL"
- "_resolutionCompletion"
- "_resultNewsURL"
- "_resultWebURL"
- "_webURL"
- "autorelease"
- "bloomFilterInfo"
- "bloomFilterInfoService"
- "boolForKey:"
- "class"
- "conformsToProtocol:"
- "copy"
- "createResolutionOperationForNewsURL:"
- "createResolutionOperationForWebURL:"
- "debugDescription"
- "description"
- "errorWithDomain:code:userInfo:"
- "exceptionWithName:reason:userInfo:"
- "executeWithCompletionHandler:"
- "fc_fullBloomFilterInfo"
- "fc_isNewsURL"
- "fc_maybeContainsURL:"
- "fetchOnceOperation"
- "fetchWebURLBloomFilterInfoWithCompletion:"
- "finishedPerformingOperationWithError:"
- "hash"
- "init"
- "initWithBlock:"
- "initWithFormat:"
- "initWithMachServiceName:options:"
- "initWithNewsURL:"
- "initWithSuiteName:"
- "initWithWebURL:bloomFilterInfoService:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "newsURL"
- "nr_isNewsURL"
- "nr_isWebURL"
- "operationWillFinishWithError:"
- "performOperation"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "resolutionCompletion"
- "resolveNewsURL:withCompletion:"
- "resolveWebURL:withCompletion:"
- "respondsToSelector:"
- "resultNewsURL"
- "resultWebURL"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setBloomFilterInfo:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setRemoteObjectInterface:"
- "setResolutionCompletion:"
- "setResultNewsURL:"
- "setResultWebURL:"
- "setWithObject:"
- "sharedManager"
- "stringWithFormat:"
- "superclass"
- "userHasBundleSubscription"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSURL\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NTPBBloomFilterInfo\">16"
- "v24@0:8@?<v@?@\"NTPBBloomFilterInfo\"@\"NSError\">16"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSURL\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "validateOperation"
- "webURL"
- "zone"

```
