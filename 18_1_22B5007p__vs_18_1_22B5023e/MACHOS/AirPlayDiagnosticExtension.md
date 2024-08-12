## AirPlayDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/AirPlayDiagnosticExtension`

```diff

-800.68.1.0.0
-  __TEXT.__text: 0x3048
-  __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_stubs: 0xae0
-  __TEXT.__objc_methlist: 0x36c
-  __TEXT.__cstring: 0xa9b
-  __TEXT.__objc_classname: 0x6b
-  __TEXT.__objc_methname: 0x886
-  __TEXT.__objc_methtype: 0x1b4
+830.2.0.0.0
+  __TEXT.__text: 0x3d94
+  __TEXT.__auth_stubs: 0x400
+  __TEXT.__objc_stubs: 0xec0
+  __TEXT.__objc_methlist: 0x514
+  __TEXT.__cstring: 0xaab
+  __TEXT.__objc_classname: 0xa2
+  __TEXT.__objc_methname: 0xca2
+  __TEXT.__objc_methtype: 0x334
+  __TEXT.__gcc_except_tab: 0x180
   __TEXT.__const: 0x8
-  __TEXT.__gcc_except_tab: 0xcc
-  __TEXT.__unwind_info: 0x130
-  __DATA_CONST.__auth_got: 0x1e0
-  __DATA_CONST.__got: 0x118
+  __TEXT.__unwind_info: 0x178
+  __DATA_CONST.__auth_got: 0x210
+  __DATA_CONST.__got: 0x168
   __DATA_CONST.__const: 0x90
-  __DATA_CONST.__cfstring: 0x2a0
-  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__cfstring: 0x300
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x5f0
-  __DATA.__objc_selrefs: 0x2e8
-  __DATA.__objc_ivar: 0x44
-  __DATA.__objc_data: 0x140
-  __DATA.__data: 0x150
-  __DATA.__crash_info: 0x40
+  __DATA.__objc_const: 0x940
+  __DATA.__objc_selrefs: 0x430
+  __DATA.__objc_ivar: 0x6c
+  __DATA.__objc_data: 0x1e0
+  __DATA.__data: 0x1c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 71
-  Symbols:   112
-  CStrings:  241
+  Functions: 103
+  Symbols:   134
+  CStrings:  326
 
Symbols:
+ _FigCFDictionaryGetValue
+ _FigRoutingContextRemoteCopySystemRemotePoolContext
+ _NSOSStatusErrorDomain
+ _NSStringFromClass
+ _OBJC_CLASS_$_APDOperation
+ _OBJC_CLASS_$_APDOperationSystemRemotePoolAddEndpoint
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSOperation
+ _OBJC_CLASS_$_NSOperationQueue
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_METACLASS_$_APDOperation
+ _OBJC_METACLASS_$_APDOperationSystemRemotePoolAddEndpoint
+ _OBJC_METACLASS_$_NSOperation
+ _kFigRouteDiscovererProperty_AvailableRouteDescriptors
+ _kFigRoutingContextNotificationPayloadKey_RouteConfigUpdateID
+ _kFigRoutingContextNotificationPayloadKey_RouteConfigUpdateReason
+ _kFigRoutingContextNotificationPayloadValue_ConfigUpdateReasonEndedFailed
+ _kFigRoutingContextNotificationPayloadValue_ConfigUpdateReasonEndedSuccess
+ _kFigRoutingContextNotification_RouteConfigUpdated
+ _kFigRoutingContextSelectRouteOptionKey_ClientRouteRequestID
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_opt_class
- _FigEndpointDeactivate
- _kFigRouteDiscovererProperty_AvailableRoutes
- _objc_retain_x22
CStrings:
+ "\x12$\x11"
+ "\x13"
+ "%!@(MISSING)-%!@(MISSING)"
+ "-[APDOperationSystemRemotePoolAddEndpoint handleRouteConfigUpdated:]"
+ "-[APDOperationSystemRemotePoolAddEndpoint main]"
+ "@\"APDOperationSystemRemotePoolAddEndpoint\""
+ "@\"NSDictionary\""
+ "@\"NSError\""
+ "@\"NSOperationQueue\""
+ "@\"NSUUID\""
+ "@32@0:8^{OpaqueFigEndpoint=}16^{__CFDictionary=}24"
+ "@40@0:8^{OpaqueFigEndpoint=}16^{__CFDictionary=}24Q32"
+ "APDOperation"
+ "APDOperation"
+ "APDOperationSystemRemotePoolAddEndpoint"
+ "RouteName"
+ "T@\"APDOperationSystemRemotePoolAddEndpoint\",&,V_previousActivation"
+ "T@\"NSDictionary\",&,V_options"
+ "T@\"NSError\",&,V_error"
+ "T@\"NSMutableDictionary\",&,V_endpoints"
+ "T@\"NSOperationQueue\",&,V_operationQueue"
+ "T@\"NSURL\",&,V_runDirURL"
+ "T@\"NSUUID\",&,V_uuid"
+ "T@,&,V_result"
+ "TB,GisExecuting,V_executing"
+ "TB,GisFinished,V_finished"
+ "T^{OpaqueFigRouteDiscoverer=},V_discoverer"
+ "T^{OpaqueFigRoutingContext=},V_routingContext"
+ "T^{__CFDictionary=},V_descriptor"
+ "UUID"
+ "UUIDString"
+ "[%!@(MISSING)] ### Failed to get endpoint for descriptor %!'(MISSING)@"
+ "[%!@(MISSING)] Discovered [%!@(MISSING)]"
+ "[%!@(MISSING)] Endpoint [%!@(MISSING)] added to system remote pool"
+ "[%!@(MISSING)] Endpoint [%!@(MISSING)] error adding to system remote pool%!?(MISSING){end}: %!@(MISSING)"
+ "[%!@(MISSING)] ID %!@(MISSING)"
+ "[%!@(MISSING)] ID %!@(MISSING) received notification %!@(MISSING) %!@(MISSING)"
+ "^{OpaqueFigRouteDiscoverer=}16@0:8"
+ "^{OpaqueFigRoutingContext=}"
+ "^{OpaqueFigRoutingContext=}16@0:8"
+ "^{__CFDictionary=}"
+ "^{__CFDictionary=}16@0:8"
+ "_descriptor"
+ "_error"
+ "_executing"
+ "_finished"
+ "_operationQueue"
+ "_options"
+ "_previousActivation"
+ "_result"
+ "_routingContext"
+ "_uuid"
+ "addDependency:"
+ "addEntriesFromDictionary:"
+ "addOperation:"
+ "cancel"
+ "cancelAllOperations"
+ "descriptor"
+ "didChangeValueForKey:"
+ "discoveredEndpoint:descriptor:"
+ "discoverer"
+ "done"
+ "done:"
+ "endpoints"
+ "error"
+ "errorWithDomain:code:userInfo:"
+ "executing"
+ "findAllfiles:"
+ "finished"
+ "handleRouteConfigUpdated:"
+ "initWithEndpoint:descriptor:state:"
+ "isAsynchronous"
+ "isCancelled"
+ "isExecuting"
+ "isExecuting"
+ "isFinished"
+ "isFinished"
+ "main"
+ "operationQueue"
+ "options"
+ "previousActivation"
+ "removeObserver:"
+ "result"
+ "routingContext"
+ "runDirURL"
+ "setCompletionBlock:"
+ "setDescriptor:"
+ "setDiscoverer:"
+ "setEndpoints:"
+ "setError:"
+ "setErrorCode:"
+ "setExecuting:"
+ "setFinished:"
+ "setOperationQueue:"
+ "setOptions:"
+ "setPreviousActivation:"
+ "setResult:"
+ "setRoutingContext:"
+ "setRunDirURL:"
+ "setUuid:"
+ "start"
+ "userInfo"
+ "uuid"
+ "v24@0:8^{OpaqueFigRouteDiscoverer=}16"
+ "v24@0:8^{OpaqueFigRoutingContext=}16"
+ "v24@0:8^{__CFDictionary=}16"
+ "v8@?0"
+ "willChangeValueForKey:"
- "\x02\"!"
- "+[APDiagnosticsEndpoint discoveredEndpoint:]"
- "-[APDiagnosticsEndpoint activateWithOptions:completion:]"
- "-[APDiagnosticsEndpoint deactivate]"
- "@24@0:8^{OpaqueFigEndpoint=}16"
- "@32@0:8^{OpaqueFigEndpoint=}16Q24"
- "Error in client of APDiagnosticsEndpoint: -init unsupported, use -initWithEndpoint:state:"
- "TB,V_shouldDeactivate"
- "[%!@(MISSING)] Activate"
- "[%!@(MISSING)] Activation completed for endpoint [%!@(MISSING)] %!'(MISSING)@ with error %!m(MISSING)"
- "[%!@(MISSING)] Deactivating endpoint %!'(MISSING)@"
- "[%!@(MISSING)] Discovered"
- "_activateFinishedWithErr:"
- "_retrieveLogsFinishedWithErr:"
- "_shouldDeactivate"
- "activateWithOptions:completion:"
- "deactivate"
- "discoveredEndpoint:"
- "initWithEndpoint:state:"
- "lsDir:"
- "setShouldDeactivate:"
- "shouldDeactivate"
- "v36@?0@\"APDiagnosticsEndpoint\"8Q16Q24i32"

```
