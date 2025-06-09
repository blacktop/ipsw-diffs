## watchdogd

> `/usr/libexec/watchdogd`

```diff

-299.120.2.0.0
-  __TEXT.__text: 0xb5f8
-  __TEXT.__auth_stubs: 0xfa0
-  __TEXT.__objc_stubs: 0xb20
+321.0.0.0.0
+  __TEXT.__text: 0xc0b0
+  __TEXT.__auth_stubs: 0xff0
+  __TEXT.__objc_stubs: 0xc60
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x4b5f
+  __TEXT.__cstring: 0x4fef
   __TEXT.__oslogstring: 0x2a1
   __TEXT.__objc_classname: 0x1
   __TEXT.__gcc_except_tab: 0x5c
-  __TEXT.__objc_methname: 0x719
-  __TEXT.__unwind_info: 0x288
-  __DATA_CONST.__auth_got: 0x7e0
-  __DATA_CONST.__got: 0x1a8
+  __TEXT.__objc_methname: 0x7f3
+  __TEXT.__unwind_info: 0x2a0
+  __DATA_CONST.__auth_got: 0x808
+  __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x7c0
-  __DATA_CONST.__cfstring: 0x8e0
+  __DATA_CONST.__const: 0x830
+  __DATA_CONST.__cfstring: 0x960
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x318
+  __DATA_CONST.__objc_intobj: 0x360
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_selrefs: 0x2c8
-  __DATA.__data: 0x9cd8
-  __DATA.__bss: 0xae8
+  __DATA.__objc_selrefs: 0x318
+  __DATA.__data: 0xa3b8
+  __DATA.__bss: 0xb00
   __DATA.__common: 0x90
   __INFO_FILTER.__disable: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics
   - /System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement
+  - /System/Library/PrivateFrameworks/UnblockClient.framework/UnblockClient
+  - /System/Library/PrivateFrameworks/UnblockService.framework/UnblockService
   - /usr/lib/libEndpointSecurity.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: FE7BB1C7-9610-3558-8F5C-E1779F43C897
-  Functions: 194
-  Symbols:   312
-  CStrings:  688
+  UUID: D4D7DB70-15E1-3F07-9077-B4E990DAF27C
+  Functions: 202
+  Symbols:   320
+  CStrings:  736
 
Symbols:
+ _NSClassFromString
+ _OBJC_CLASS_$_CDStackshotReport
+ _OBJC_CLASS_$_CDSystemWatchdogStackshotReport
+ _OBJC_CLASS_$_UBStuckService
+ _OBJC_CLASS_$_UBUnblockClient
+ _OBJC_CLASS_$_UBUnblockService
+ __os_feature_enabled_impl
+ _dispatch_source_set_event_handler_f
+ _objc_retain_x22
+ _os_transaction_create
- _OBJC_CLASS_$_OSACrackShotReport
- _OBJC_CLASS_$_OSAStackShotReport
CStrings:
+ "%s : %s"
+ "-b"
+ "-d"
+ "-wdt_skip_reactive_unblock_action"
+ "/usr/local/libexec/watchdogtestunblock"
+ "EnableUnblockReactiveAction"
+ "Error occured when trying to recover process %d"
+ "Evaluate Healthiness Found Unresponsive Thread"
+ "Failed to bootstrap Unblock Service"
+ "Failed to capture stackshot"
+ "Identified issue %d for process %d with confidence %d, %s"
+ "No valid unblock requests, return"
+ "No valuable service could be found, return"
+ "OS_REASON_AUDIO"
+ "REALITYKIT"
+ "ROSETTA"
+ "Request unblock operation for:"
+ "Service not touched"
+ "Service recovered"
+ "Skip evaluating or taking action on service %s because failed to find blocked thread"
+ "Skip evaluating or taking action on service %s because failed to get PID"
+ "Skip evaluating or taking action on service %s because service being debugged"
+ "UBUnblockService"
+ "UBUnblockService is not available"
+ "UUIDString"
+ "Unable to identify recoverable action for process %d"
+ "Unblock reactive action returns error: %s"
+ "com.apple.watchdogd.unblock_diagnostics"
+ "com.apple.watchdogd.unblock_reactive_action"
+ "com.apple.watchdogtestd.listener"
+ "com.apple.watchdogtestunblock"
+ "com.apple.watchdogtestunblock.watchdog"
+ "detected setting for skipping unblock reactive action"
+ "initForPid:threadID:timeElapsed:incidentUUID:"
+ "initWithBytes:length:"
+ "initWithUUIDBytes:"
+ "issueType"
+ "recover:stackshotData:replyQueue:callback:"
+ "recoveryConfidence"
+ "recoveryStatus"
+ "setupAndActivate:"
+ "sharedInstance"
+ "v16@?0^{watchdog_service={?=^{watchdog_service}}QBB****iBBBBBi(?={ephemeral_service_data=*B^{watchdog_service}{?=^{watchdog_service}}}{controller_service_data={?=^{watchdog_service}}})I{watchdog_service_state=QQQQQQQ[16C]AiBii{watchdog_service_state_round=IiBB[1024c]Q[10Q][5[32c]]QBB[400c]}}}8"
+ "v24@?0@\"NSError\"8@\"NSArray\"16"
+ "v24@?0^{es_client_s=}8r^{?=I{timespec=qq}QQ^{?}Qi(?={?=[32C]}{?=i(?=iI[32C])})i(?={?=i^{?}[64C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}^{?}{?=Q*}[64C]}{?=B^{?}(?=[64C]{?=B})}{?=^{?}^{?}^{?}{?=Q*}Si[56C]}{?=i(?=^{?}{?=^{?}{?=Q*}S})[16C](?=[48C]{?=^{_acl}})}{?=[64C]}{?=^{?}{?=Q*}[64C]}{?=^{?}[64C]}{?=^{?}^{?}[64C]}{?=^{?}{?=Q*}(?=[64C]{?=^{?}^{?}iii})}{?=i[64C]}{?=^{?}^{?}^{?}{?=[8I]}[32C]}{?=^{?}{?=Q*}[64C]}{?=^{?}i[64C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}i[60C]}{?=^{?}i[60C]}{?=^{?}i[60C]}{?=^{?}i[60C]}{?={attrlist=SSIIIII}^{?}[64C]}{?=^{?}{?=Q*}[64C]}{?=I{?=Q*}Q{?=Q*}[40C]}{?={?=Q*}[64C]}{?={?=Q*}[64C]}{?=^{?}^{?}{?=Q*}[64C]}{?=^{?}[64C]}{?=^{?}{?=Q*}[64C]}{?=iiiQ^{?}[64C]}{?=^{statfs}i[60C]}{?=iQQ[64C]}{?=i^{?}[64C]}{?=^{?}ii[64C]}{?=^{?}i[64C]}{?=i[64C]}{?=i[64C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}^{?}[64C]}{?=^{statfs}Qi[52C]}{?=^{?}i(?=^{?}{?=^{?}{?=Q*}})[64C]}{?={attrlist=SSIIIII}^{?}[64C]}{?=^{?}i(?=^{_acl})[64C]}{?={attrlist=SSIIIII}^{?}[64C]}{?=^{?}{?=Q*}[64C]}{?=I^{?}[64C]}{?=S^{?}[64C]}{?=II^{?}[64C]}{?=[64C]}{?=I[64C]}{?=I[64C]}{?=I[64C]}{?=I[64C]}{?=II[64C]}{?=II[64C]}{?=i^{?}^{?}[56C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}{?=Q*}S[64C]}{?=^{?}iii[64C]}{?=^{?}^{?}[64C]}{?=^{statfs}[64C]}{?=^{?}{timespec=qq}{timespec=qq}[64C]}{?=^{?}[64C]}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?})^{?}Q[0Q]}16"
+ "watchdogd"
+ "watchdogd detected testing boot-args for daemon (controller: %d) (ephemeral: %d) (optin: %d) (exclave :%d) (unblock: %d)"
+ "watchdogtestunblock"
+ "wdt_unblock"
+ "wdt_unblock="
- "com.apple.mediaserverd"
- "com.apple.mediaserverd.coremedia.watchdog"
- "mediaserverd"
- "v16@?0^{watchdog_service={?=^{watchdog_service}}QBB****iBBBBBi(?={ephemeral_service_data=*B^{watchdog_service}{?=^{watchdog_service}}}{controller_service_data={?=^{watchdog_service}}})I{watchdog_service_state=QQQQQQQ[16C]AiBii{watchdog_service_state_round=IiBB[1024c]Q[5[32c]]QBB[400c]}}}8"
- "v24@?0^{es_client_s=}8r^{?=I{timespec=qq}QQ^{?}Qi(?={?=[32C]}{?=i(?=iI[32C])})i(?={?=i^{?}[64C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}^{?}{?=Q*}[64C]}{?=B^{?}(?=[64C]{?=B})}{?=^{?}^{?}^{?}{?=Q*}Si[56C]}{?=i(?=^{?}{?=^{?}{?=Q*}S})[16C](?=[48C]{?=^{_acl}})}{?=[64C]}{?=^{?}{?=Q*}[64C]}{?=^{?}[64C]}{?=^{?}^{?}[64C]}{?=^{?}{?=Q*}(?=[64C]{?=^{?}^{?}iii})}{?=i[64C]}{?=^{?}^{?}^{?}{?=[8I]}[32C]}{?=^{?}{?=Q*}[64C]}{?=^{?}i[64C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}i[60C]}{?=^{?}i[60C]}{?=^{?}i[60C]}{?=^{?}i[60C]}{?={attrlist=SSIIIII}^{?}[64C]}{?=^{?}{?=Q*}[64C]}{?=I{?=Q*}[64C]}{?={?=Q*}[64C]}{?={?=Q*}[64C]}{?=^{?}^{?}{?=Q*}[64C]}{?=^{?}[64C]}{?=^{?}{?=Q*}[64C]}{?=iiiQ^{?}[64C]}{?=^{statfs}i[60C]}{?=iQQ[64C]}{?=i^{?}[64C]}{?=^{?}ii[64C]}{?=^{?}i[64C]}{?=i[64C]}{?=i[64C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}^{?}[64C]}{?=^{statfs}Qi[52C]}{?=^{?}i(?=^{?}{?=^{?}{?=Q*}})[64C]}{?={attrlist=SSIIIII}^{?}[64C]}{?=^{?}i(?=^{_acl})[64C]}{?={attrlist=SSIIIII}^{?}[64C]}{?=^{?}{?=Q*}[64C]}{?=I^{?}[64C]}{?=S^{?}[64C]}{?=II^{?}[64C]}{?=[64C]}{?=I[64C]}{?=I[64C]}{?=I[64C]}{?=I[64C]}{?=II[64C]}{?=II[64C]}{?=i^{?}^{?}[56C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}{?=Q*}S[64C]}{?=^{?}iii[64C]}{?=^{?}^{?}[64C]}{?=^{statfs}[64C]}{?=^{?}{timespec=qq}{timespec=qq}[64C]}{?=^{?}[64C]}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?})^{?}Q[0Q]}16"
- "watchdogd detected testing boot-args for daemon (controller: %d) (ephemeral: %d) (optin: %d) (exclave :%d)"

```
