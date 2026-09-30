## watchdogd

> `/usr/libexec/watchdogd`

```diff

-323.80.7.0.0
-  __TEXT.__text: 0xc0e0
+333.0.0.0.0
+  __TEXT.__text: 0xe120
   __TEXT.__auth_stubs: 0xff0
-  __TEXT.__objc_stubs: 0xc60
+  __TEXT.__objc_stubs: 0x1020
+  __TEXT.__objc_methlist: 0xc8
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x500b
+  __TEXT.__cstring: 0x5732
   __TEXT.__oslogstring: 0x2a1
-  __TEXT.__objc_classname: 0x1
-  __TEXT.__gcc_except_tab: 0x5c
-  __TEXT.__objc_methname: 0x7f3
-  __TEXT.__unwind_info: 0x2a8
+  __TEXT.__gcc_except_tab: 0x74
+  __TEXT.__objc_classname: 0x15
+  __TEXT.__objc_methname: 0xbb3
+  __TEXT.__objc_methtype: 0xa0
+  __TEXT.__unwind_info: 0x318
   __DATA_CONST.__auth_got: 0x808
-  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x830
-  __DATA_CONST.__cfstring: 0x980
+  __DATA_CONST.__const: 0x8f0
+  __DATA_CONST.__cfstring: 0x9c0
+  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x378
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_selrefs: 0x318
-  __DATA.__data: 0xa3b8
-  __DATA.__bss: 0xb00
+  __DATA.__objc_const: 0x1c0
+  __DATA.__objc_selrefs: 0x418
+  __DATA.__objc_ivar: 0x18
+  __DATA.__objc_data: 0x50
+  __DATA.__data: 0xa468
+  __DATA.__bss: 0xb08
   __DATA.__common: 0x90
   __INFO_FILTER.__disable: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: CE486802-3456-3FE6-8294-5A84A4CC58FF
-  Functions: 202
-  Symbols:   320
-  CStrings:  738
+  UUID: 3951B16C-1948-3E02-9502-86EAEBAF2FA8
+  Functions: 237
+  Symbols:   324
+  CStrings:  828
 
Symbols:
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_UBStuckServiceRecoveryResult
+ _OBJC_METACLASS_$_NSObject
+ _UBIssueTypeCopyDescription
+ _UBRecoveryConfidenceCopyDescription
+ _UBRecoveryStatusCopyDescription
+ __objc_empty_cache
+ _dispatch_assert_queue$V2
+ _objc_msgSendSuper2
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x28
+ _xpc_transaction_begin
+ _xpc_transaction_end
- _getpid
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x24
- _objc_retain_x3
- _objc_retain_x8
- _os_transaction_create
- _proc_set_dirty
CStrings:
+ "\n"
+ "\n\n%s"
+ "+[WDUnblockTracker addNewUnblockTracker:]"
+ "-[WDUnblockTracker reportEffectiveness]"
+ ".cxx_destruct"
+ "@\"NSDictionary\""
+ "@\"NSMutableSet\""
+ "@\"NSString\""
+ "@16@0:8"
+ "@32@0:8@16Q24"
+ "@44@0:8i16@20Q28@36"
+ "Already have unblock in flight"
+ "B"
+ "B16@0:8"
+ "Q"
+ "Q16@0:8"
+ "T@\"NSDictionary\",&,N,V_unblockRecoveryResults"
+ "T@\"NSMutableSet\",R,N,V_threadsStillBlocked"
+ "T@\"NSString\",R,N,V_launchdLabel"
+ "TB,N,V_watchdogTookAction"
+ "TQ,R,N,V_triggeredRoundID"
+ "Ti,R,N,V_pid"
+ "Unblock [%s]: %s round %llu : %s"
+ "Unblock [%s]: All unblock requests for %s round %llu were successful, but the service never recovered"
+ "Unblock [%s]: Already have unblock for %s round %llu"
+ "Unblock [%s]: Already reported Unblock tracker for %s round %llu took action"
+ "Unblock [%s]: Failed to capture stackshot"
+ "Unblock [%s]: Invalid thread (%llu) in result for %s round %llu %s [%d]"
+ "Unblock [%s]: No Unblock tracker for %s round %llu"
+ "Unblock [%s]: No recovery attempted for %s [%d] thread 0x%llx: %s (round %llu)"
+ "Unblock [%s]: No recovery attempted for %s blocking %s [%d] thread 0x%llx with confidence %s: did not terminate %s [%d] due to %s (round %llu)"
+ "Unblock [%s]: No valid unblock requests, return"
+ "Unblock [%s]: No valuable service could be found, return"
+ "Unblock [%s]: Recovery attempted for %s blocking %s [%d] thread 0x%llx with confidence %s: terminated %s [%d] (round %llu)"
+ "Unblock [%s]: Releasing all Unblock trackers"
+ "Unblock [%s]: Reporting effectiveness for unblock tracker for %s round %llu, and releasing"
+ "Unblock [%s]: Request unblock operation for:"
+ "Unblock [%s]: Skip evaluating or taking action on service %s round %llu because failed to find blocked thread"
+ "Unblock [%s]: Skip evaluating or taking action on service %s round %llu because failed to get PID"
+ "Unblock [%s]: Skip evaluating or taking action on service %s round %llu because service being debugged"
+ "Unblock [%s]: Unable to convert launchd label %s to NSString!"
+ "Unblock [%s]: Unable to convert launchd label to NSString, cannot track recovery results for service %s round %llu"
+ "Unblock [%s]: Unblock reactive action returned %lu results when expected %lu"
+ "Unblock [%s]: Unblock reactive action returned error: %s"
+ "Unblock [%s]: Unblock tracker for %s round %llu updated blocked threads %lu -> %lu (%s)"
+ "Unblock results no longer available for service %s"
+ "WDUnblockTracker"
+ "_launchdLabel"
+ "_pid"
+ "_threadsStillBlocked"
+ "_triggeredRoundID"
+ "_unblockRecoveryResults"
+ "_watchdogTookAction"
+ "addNewUnblockTracker:"
+ "allValues"
+ "appendString:"
+ "copy"
+ "copyHeaderDescription"
+ "existingUnblockTrackerForLaunchdLabel:triggeredRoundID:"
+ "headerDescription"
+ "i16@0:8"
+ "init"
+ "initWithObjects:"
+ "initWithPid:launchdLabel:triggeredRoundID:tids:"
+ "initWithUTF8String:"
+ "intersectSet:"
+ "launchdLabel"
+ "mutableCopy"
+ "name"
+ "numberWithUnsignedLongLong:"
+ "objectAtIndexedSubscript:"
+ "recoveryHadEffectiveness:"
+ "removeObjectAtIndex:"
+ "removeUnblockTrackerForLaunchdLabel:triggeredRoundID:"
+ "reportEffectiveness"
+ "selectedProcess"
+ "serviceProcessName"
+ "setObject:forKeyedSubscript:"
+ "setUnblockRecoveryResults:"
+ "setWatchdogTookAction:"
+ "take_unblock_action"
+ "take_unblock_action_block_invoke_2"
+ "threadID"
+ "threadsStillBlocked"
+ "triggeredRoundID"
+ "unblockRecoveryResults"
+ "unblock_recovery_copy_header_description"
+ "unblock_recovery_copy_header_description_block_invoke"
+ "unblock_recovery_ineffective"
+ "unblock_recovery_ineffective_block_invoke"
+ "unblock_recovery_release"
+ "unblock_recovery_release_block_invoke"
+ "unblock_recovery_reset_all_block_invoke"
+ "unblock_recovery_update_effectiveness"
+ "unblock_recovery_update_effectiveness_block_invoke"
+ "v16@0:8"
+ "v16@?0^{watchdog_service={?=^{watchdog_service}}QBB****iBBBBBi(?={ephemeral_service_data=*B^{watchdog_service}{?=^{watchdog_service}}}{controller_service_data={?=^{watchdog_service}}})I{watchdog_service_state=QQQQQQQQ[16C]AiBii{watchdog_service_state_round=IiBB[1024c]Q[10Q][5[32c]]QBB[400c]}}}8"
+ "v20@0:8B16"
+ "v24@0:8@16"
+ "v24@?0^{es_client_s=}8r^{?=I{timespec=qq}QQ^{?}Qi(?={?=[32C]}{?=i(?=iI[32C])})i(?={?=i^{?}[64C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}^{?}{?=Q*}[64C]}{?=B^{?}(?=[64C]{?=B})}{?=^{?}^{?}^{?}{?=Q*}Si[56C]}{?=i(?=^{?}{?=^{?}{?=Q*}S})[16C](?=[48C]{?=^{_acl}})}{?=[64C]}{?=^{?}{?=Q*}[64C]}{?=^{?}[64C]}{?=^{?}^{?}[64C]}{?=^{?}{?=Q*}(?=[64C]{?=^{?}^{?}iii})}{?=i[64C]}{?=^{?}^{?}^{?}{?=[8I]}[32C]}{?=^{?}{?=Q*}[64C]}{?=^{?}i[64C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}i[60C]}{?=^{?}i[60C]}{?=^{?}i[60C]}{?=^{?}i[60C]}{?={attrlist=SSIIIII}^{?}[64C]}{?=^{?}{?=Q*}[64C]}{?=I{?=Q*}Q{?=Q*}[40C]}{?={?=Q*}[64C]}{?={?=Q*}[64C]}{?=^{?}^{?}{?=Q*}[64C]}{?=^{?}[64C]}{?=^{?}{?=Q*}[64C]}{?=iiiQ^{?}[64C]}{?=^{statfs}i[60C]}{?=iQQ[64C]}{?=i^{?}[64C]}{?=^{?}ii[64C]}{?=^{?}i[64C]}{?=i[64C]}{?=i[64C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}^{?}[64C]}{?=^{statfs}Qi[52C]}{?=^{?}i(?=^{?}{?=^{?}{?=Q*}})[64C]}{?={attrlist=SSIIIII}^{?}[64C]}{?=^{?}i(?=^{_acl})[64C]}{?={attrlist=SSIIIII}^{?}[64C]}{?=^{?}{?=Q*}[64C]}{?=I^{?}[64C]}{?=S^{?}[64C]}{?=II^{?}[64C]}{?=[64C]}{?=I[64C]}{?=I[64C]}{?=I[64C]}{?=I[64C]}{?=II[64C]}{?=II[64C]}{?=i^{?}^{?}[56C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}{?=Q*}S[64C]}{?=^{?}iii[64C]}{?=^{?}^{?}[64C]}{?=^{statfs}[64C]}{?=^{?}{timespec=qq}{timespec=qq}[64C]}{?=^{?}[64C]}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{es_event_paste_t}^{es_event_listen_t}^{es_event_flow_t})^{?}Q[0Q]}16"
+ "v32@0:8@16Q24"
+ "watchdogTookAction"
+ "watchdogd is supposed to transit into active state"
+ "watchdogd is supposed to transit into idle state"
- "%s : %s"
- "Error occured when trying to recover process %d"
- "Failed to capture stackshot"
- "Identified issue %d for process %d with confidence %d, %s"
- "No valid unblock requests, return"
- "No valuable service could be found, return"
- "Request unblock operation for:"
- "Service not touched"
- "Service recovered"
- "Skip evaluating or taking action on service %s because failed to find blocked thread"
- "Skip evaluating or taking action on service %s because failed to get PID"
- "Skip evaluating or taking action on service %s because service being debugged"
- "Unable to identify recoverable action for process %d"
- "Unblock reactive action returns error: %s"
- "com.apple.watchdogd.unblock_reactive_action"
- "v16@?0^{watchdog_service={?=^{watchdog_service}}QBB****iBBBBBi(?={ephemeral_service_data=*B^{watchdog_service}{?=^{watchdog_service}}}{controller_service_data={?=^{watchdog_service}}})I{watchdog_service_state=QQQQQQQ[16C]AiBii{watchdog_service_state_round=IiBB[1024c]Q[10Q][5[32c]]QBB[400c]}}}8"
- "v24@?0^{es_client_s=}8r^{?=I{timespec=qq}QQ^{?}Qi(?={?=[32C]}{?=i(?=iI[32C])})i(?={?=i^{?}[64C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}^{?}{?=Q*}[64C]}{?=B^{?}(?=[64C]{?=B})}{?=^{?}^{?}^{?}{?=Q*}Si[56C]}{?=i(?=^{?}{?=^{?}{?=Q*}S})[16C](?=[48C]{?=^{_acl}})}{?=[64C]}{?=^{?}{?=Q*}[64C]}{?=^{?}[64C]}{?=^{?}^{?}[64C]}{?=^{?}{?=Q*}(?=[64C]{?=^{?}^{?}iii})}{?=i[64C]}{?=^{?}^{?}^{?}{?=[8I]}[32C]}{?=^{?}{?=Q*}[64C]}{?=^{?}i[64C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}i[60C]}{?=^{?}i[60C]}{?=^{?}i[60C]}{?=^{?}i[60C]}{?={attrlist=SSIIIII}^{?}[64C]}{?=^{?}{?=Q*}[64C]}{?=I{?=Q*}Q{?=Q*}[40C]}{?={?=Q*}[64C]}{?={?=Q*}[64C]}{?=^{?}^{?}{?=Q*}[64C]}{?=^{?}[64C]}{?=^{?}{?=Q*}[64C]}{?=iiiQ^{?}[64C]}{?=^{statfs}i[60C]}{?=iQQ[64C]}{?=i^{?}[64C]}{?=^{?}ii[64C]}{?=^{?}i[64C]}{?=i[64C]}{?=i[64C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}^{?}[64C]}{?=^{statfs}Qi[52C]}{?=^{?}i(?=^{?}{?=^{?}{?=Q*}})[64C]}{?={attrlist=SSIIIII}^{?}[64C]}{?=^{?}i(?=^{_acl})[64C]}{?={attrlist=SSIIIII}^{?}[64C]}{?=^{?}{?=Q*}[64C]}{?=I^{?}[64C]}{?=S^{?}[64C]}{?=II^{?}[64C]}{?=[64C]}{?=I[64C]}{?=I[64C]}{?=I[64C]}{?=I[64C]}{?=II[64C]}{?=II[64C]}{?=i^{?}^{?}[56C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}[64C]}{?=^{?}{?=Q*}S[64C]}{?=^{?}iii[64C]}{?=^{?}^{?}[64C]}{?=^{statfs}[64C]}{?=^{?}{timespec=qq}{timespec=qq}[64C]}{?=^{?}[64C]}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{?}^{es_event_paste_t})^{?}Q[0Q]}16"

```
