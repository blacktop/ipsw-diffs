## akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

-525.475.19.0.0
-  __TEXT.__text: 0x2dbb90
+525.575.4.0.0
+  __TEXT.__text: 0x2e02fc
   __TEXT.__auth_stubs: 0x2170
-  __TEXT.__objc_stubs: 0x1bba0
-  __TEXT.__objc_methlist: 0xbe34
-  __TEXT.__const: 0x6c70
-  __TEXT.__cstring: 0xaf75
-  __TEXT.__objc_classname: 0x28da
-  __TEXT.__gcc_except_tab: 0x3e24
-  __TEXT.__objc_methname: 0x26615
-  __TEXT.__objc_methtype: 0x7696
-  __TEXT.__oslogstring: 0x25507
+  __TEXT.__objc_stubs: 0x1be00
+  __TEXT.__objc_methlist: 0xc03c
+  __TEXT.__const: 0x6d60
+  __TEXT.__cstring: 0xb045
+  __TEXT.__objc_classname: 0x292a
+  __TEXT.__gcc_except_tab: 0x3eb8
+  __TEXT.__objc_methname: 0x26a65
+  __TEXT.__objc_methtype: 0x7732
+  __TEXT.__oslogstring: 0x25887
   __TEXT.__dlopen_cstrs: 0x15f
-  __TEXT.__swift5_typeref: 0x3071
-  __TEXT.__swift5_fieldmd: 0x15b4
-  __TEXT.__constg_swiftt: 0x2094
-  __TEXT.__swift5_reflstr: 0x11c1
+  __TEXT.__swift5_typeref: 0x3117
+  __TEXT.__swift5_fieldmd: 0x15ec
+  __TEXT.__constg_swiftt: 0x20d0
+  __TEXT.__swift5_reflstr: 0x1201
   __TEXT.__swift5_builtin: 0x140
   __TEXT.__swift5_assocty: 0x270
-  __TEXT.__swift5_capture: 0x1f68
-  __TEXT.__swift5_protos: 0x4c
+  __TEXT.__swift5_capture: 0x1fa8
   __TEXT.__swift5_proto: 0x2ec
-  __TEXT.__swift5_types: 0x1d4
-  __TEXT.__swift_as_entry: 0x534
-  __TEXT.__swift_as_ret: 0x6e8
+  __TEXT.__swift5_types: 0x1d8
+  __TEXT.__swift_as_entry: 0x53c
+  __TEXT.__swift_as_ret: 0x6f0
+  __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x6fd0
-  __TEXT.__eh_frame: 0xf410
+  __TEXT.__unwind_info: 0x7500
+  __TEXT.__eh_frame: 0xf590
   __DATA_CONST.__auth_got: 0x10c8
-  __DATA_CONST.__got: 0x19d8
-  __DATA_CONST.__auth_ptr: 0x670
-  __DATA_CONST.__const: 0x13360
-  __DATA_CONST.__cfstring: 0x7f40
-  __DATA_CONST.__objc_classlist: 0x7e8
+  __DATA_CONST.__got: 0x19f0
+  __DATA_CONST.__auth_ptr: 0x678
+  __DATA_CONST.__const: 0x13450
+  __DATA_CONST.__cfstring: 0x8000
+  __DATA_CONST.__objc_classlist: 0x800
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x378
+  __DATA_CONST.__objc_protolist: 0x380
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x168
-  __DATA_CONST.__objc_superrefs: 0x428
+  __DATA_CONST.__objc_protorefs: 0x170
+  __DATA_CONST.__objc_superrefs: 0x438
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_intobj: 0x360
   __DATA_CONST.__objc_arraydata: 0x370
   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__linkguard: 0x3e
-  __DATA.__objc_const: 0x29728
-  __DATA.__objc_selrefs: 0x80e0
-  __DATA.__objc_ivar: 0xacc
-  __DATA.__objc_data: 0x62e0
-  __DATA.__data: 0x4a78
-  __DATA.__bss: 0x57b0
-  __DATA.__common: 0x140
+  __DATA.__objc_const: 0x29908
+  __DATA.__objc_selrefs: 0x81c8
+  __DATA.__objc_ivar: 0xaf0
+  __DATA.__objc_data: 0x6448
+  __DATA.__data: 0x4ae8
+  __DATA.__bss: 0x57c0
+  __DATA.__common: 0x148
   - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E29D7C21-BDD9-3035-B3AE-69488511FD97
-  Functions: 9154
-  Symbols:   1526
-  CStrings:  11744
+  UUID: 841C6210-B170-3844-9B09-83751D338673
+  Functions: 9226
+  Symbols:   1529
+  CStrings:  11822
 
Symbols:
+ _AKURLBagKeyFetchUserEvents
+ _OBJC_CLASS_$_AKBasicServerResponse
+ _OBJC_CLASS_$_AKFailureInjectionConfig
CStrings:
+ "<AKADPFlowInfo: flowID=%@, altDSID=%{mask.hash}@, started=%@, completed=%@>"
+ "ADP cleanup liveness failed for altDSID=%{mask.hash}@: %@"
+ "ADP cleanup liveness succeeded for altDSID=%{mask.hash}@"
+ "ADP flow abandoned: flowID=%@, altDSID=%{mask.hash}@. Triggering cleanup liveness."
+ "AKADPFlowInfo"
+ "AKADPFlowTracker"
+ "AKBasicServerRequestService"
+ "AKBasicServerRequestServiceProtocol"
+ "Attempted to complete unknown ADP flow: flowID=%@"
+ "Beginning ADP flow tracking: flowID=%@, altDSID=%{mask.hash}@"
+ "Cancelling all ADP flow tracking"
+ "Cannot begin ADP flow tracking with empty flowID or altDSID"
+ "Cannot complete ADP flow tracking with empty flowID"
+ "Cannot trigger ADP cleanup liveness: no account found for altDSID=%{mask.hash}@, error=%@"
+ "Completing ADP flow: flowID=%@, success=%@"
+ "Internal access entitlement required but missing for performBasicServerRequest"
+ "Internal/Owner access entitlement required for ADP flow tracking!"
+ "Invalid flowID for completeADPFlowWithID"
+ "Invalid parameters for beginADPFlowWithID: flowID=%@, altDSID=%{mask.hash}@"
+ "Sending ADP flow cleanup liveness to IdMS"
+ "T@\"NSDate\",R,N,V_startTime"
+ "T@\"NSString\",R,C,N,V_flowID"
+ "TB,N,GisCompleted,V_completed"
+ "Td,N,V_abandonmentTimeout"
+ "_abandonmentTimeout"
+ "_activeFlows"
+ "_cancelTimerForFlowID:"
+ "_completed"
+ "_flowID"
+ "_flowQueue"
+ "_handleAbandonmentTimeoutForFlowID:altDSID:"
+ "_performBasicServerRequestWithContext:completion:"
+ "_scheduleAbandonmentCheckForFlowID:altDSID:"
+ "_startTime"
+ "_timers"
+ "_triggerCleanupLivenessForAltDSID:"
+ "abandonmentTimeout"
+ "activeFlowCount"
+ "adpFlowCleanup"
+ "authHandler"
+ "beginADPFlowWithID:altDSID:completion:"
+ "beginFlowWithID:altDSID:"
+ "cancelAllTracking"
+ "com.apple.authkit.adp-flow-tracker"
+ "completeADPFlowWithID:success:completion:"
+ "completeFlowWithID:success:"
+ "completed"
+ "expectedResponseFormat"
+ "failureInjectionConfig"
+ "failureInjectionHeadersForURL:completion:"
+ "flowID"
+ "headerRepresentationForRequestURL:"
+ "initWithFlowID:altDSID:"
+ "initWithHTTPResponse:data:"
+ "isCompleted"
+ "isFailureInjectionHeaderEnabled"
+ "isFlowAbandoned:"
+ "performBasicServerRequest:completion:"
+ "requestBody"
+ "requestBodyFormat"
+ "setAbandonmentTimeout:"
+ "setCompleted:"
+ "sharedTracker"
+ "startTime"
+ "v24@?0@\"AKBasicServerResponse\"8@\"NSError\"16"
+ "v32@0:8@\"AKBasicServerRequest\"16@?<v@?@\"AKBasicServerResponse\"@\"NSError\">24"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v36@0:8@\"NSString\"16B24@?<v@?@\"NSError\">28"

```
