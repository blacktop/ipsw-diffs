## securityd

> `/usr/libexec/securityd`

```diff

-61901.40.47.0.1
-  __TEXT.__text: 0x259fac
-  __TEXT.__auth_stubs: 0x4290
-  __TEXT.__objc_stubs: 0x1c640
-  __TEXT.__objc_methlist: 0x15220
+61901.40.71.0.2
+  __TEXT.__text: 0x25bc78
+  __TEXT.__auth_stubs: 0x42b0
+  __TEXT.__objc_stubs: 0x1c7c0
+  __TEXT.__objc_methlist: 0x15348
   __TEXT.__const: 0x891
-  __TEXT.__objc_methname: 0x2c31e
-  __TEXT.__cstring: 0x20f0f
-  __TEXT.__oslogstring: 0x2d2ad
+  __TEXT.__objc_methname: 0x2c64d
+  __TEXT.__cstring: 0x20fe0
+  __TEXT.__oslogstring: 0x2d520
   __TEXT.__swift5_typeref: 0x37a
   __TEXT.__swift5_fieldmd: 0x120
   __TEXT.__constg_swiftt: 0x274

   __TEXT.__swift5_types: 0x20
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x3c
-  __TEXT.__gcc_except_tab: 0xb5e4
-  __TEXT.__objc_classname: 0x2360
-  __TEXT.__objc_methtype: 0xa48e
+  __TEXT.__gcc_except_tab: 0xb630
+  __TEXT.__objc_classname: 0x238d
+  __TEXT.__objc_methtype: 0xa586
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x6790
+  __TEXT.__unwind_info: 0x67b8
   __TEXT.__eh_frame: 0xa58
-  __DATA_CONST.__auth_got: 0x2158
-  __DATA_CONST.__got: 0x1340
+  __DATA_CONST.__auth_got: 0x2168
+  __DATA_CONST.__got: 0x1350
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x13fd8
-  __DATA_CONST.__cfstring: 0x1b1a0
-  __DATA_CONST.__objc_classlist: 0x8b8
+  __DATA_CONST.__const: 0x14180
+  __DATA_CONST.__cfstring: 0x1b300
+  __DATA_CONST.__objc_classlist: 0x8c0
   __DATA_CONST.__objc_catlist: 0x68
-  __DATA_CONST.__objc_protolist: 0x248
+  __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x7f8

   __DATA_CONST.__objc_arraydata: 0x3f8
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x360
-  __DATA.__objc_const: 0x22820
-  __DATA.__objc_selrefs: 0x92d0
-  __DATA.__objc_ivar: 0x19f4
-  __DATA.__objc_data: 0x5a28
-  __DATA.__data: 0x2320
+  __DATA.__objc_const: 0x22a30
+  __DATA.__objc_selrefs: 0x9360
+  __DATA.__objc_ivar: 0x1a10
+  __DATA.__objc_data: 0x5a78
+  __DATA.__data: 0x2380
   __DATA.__thread_vars: 0xc0
   __DATA.__thread_bss: 0x28
   __DATA.__bss: 0xe60

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: FAEA432F-3540-3B4F-ACBC-D9F219D52A14
-  Functions: 9610
-  Symbols:   1772
-  CStrings:  19524
+  UUID: 266BA62B-A4B8-3472-84F2-1EAD8B9C675F
+  Functions: 9635
+  Symbols:   1776
+  CStrings:  19595
 
Symbols:
+ _AKSEventsRegister
+ _AKSEventsUnregister
+ _kAKSInfoCacheFlowContext
+ _kSecurityRTCEventNameEscrowRepairOperationPasscodeChanged
+ _kSecurityRTCEventNameEscrowRepairOperationPasscodeUnlocked
- _KCSharingGroupsUpdatedNotification
CStrings:
+ "@\"<OTLAContextAdapter>\""
+ "@160@0:8@16@24@32@40@48@56@64@72@80#88#96#104#112@120@128@136@144@152"
+ "@184@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144#152#160#168@176"
+ "@204@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136#144#152@160@168B176B180B184@188@196"
+ "@56@0:8@16@24@32@40q48"
+ "B32@0:8q16^@24"
+ "B48@0:8@\"NSData\"16q24^@32^@40"
+ "B48@0:8@16q24^@32^@40"
+ "Failed to find saved group locally"
+ "Failed to save staged outgoing changes for group create/update request for %{public}@: %{public}@, %{public}@"
+ "Invite couldn't be found"
+ "OTLAContextActualAdapter"
+ "OTLAContextAdapter"
+ "T@\"<OTLAContextAdapter>\",&,V_laContextAdapter"
+ "T@\"<OTLAContextAdapter>\",R,V_laContextAdapter"
+ "T^{_AKSEvent=},V_aksEvent"
+ "Tq,N,V_escrowRepairAttemptVersion"
+ "Tq,V_contextType"
+ "^{_AKSEvent=}"
+ "^{_AKSEvent=}16@0:8"
+ "_aksEvent"
+ "_contextType"
+ "_escrowRepairAttemptVersion"
+ "_laContextAdapter"
+ "_persistEscrowRepairAttemptVersion:error:"
+ "acceptGroupInvite:startTime:completion:"
+ "aksEvent"
+ "cache flow enabled passcode changed"
+ "cache flow enabled passcode unlocked"
+ "cache flow enabled passcode validated"
+ "cache flow enabled unknown value: %@"
+ "clearLastEscrowRepairAttempt:"
+ "com.apple.security.kcsharing.groupsupdated"
+ "com.apple.security.keychain.sharing.groupOperation"
+ "contextType"
+ "create"
+ "decline"
+ "declineGroupInvite:startTime:completion:"
+ "discardPasscodeStashSecret:"
+ "enableWithPasscodeStashSecret:account:error:"
+ "enableWithSecureBackup:error:"
+ "enabling cache flow after discarding passcode stash"
+ "escrowRepairAttemptVersion"
+ "failed to clear last escrow repair attempt: %@"
+ "failed to discard passcode stash: %@"
+ "fetchAndUpdateParticipantsForGroup:share:isCreateOperation:startTime:completion:"
+ "hasEscrowRepairAttemptVersion"
+ "initForContainer:contextID:activeAccount:stateHolder:flagHandler:sosAdapter:octagonAdapter:accountsAdapter:authKitAdapter:personaAdapter:deviceInfoAdapter:secureBackupAdapter:laContextAdapter:ckksAccountSync:lockStateTracker:cuttlefishXPCWrapper:escrowRequestClass:notifierClass:flowID:deviceSessionID:permittedToSendMetrics:accountIsG:accountIsW:reachabilityTracker:escrowChecker:"
+ "initWithContainerName:contextID:activeAccount:cuttlefish:ckksAccountSync:sosAdapter:accountsAdapter:authKitAdapter:personaAdapter:tooManyPeersAdapter:tapToRadarAdapter:lockStateTracker:reachabilityTracker:accountStateTracker:deviceInformationAdapter:secureBackupAdapter:laContextAdapter:apsConnectionClass:escrowRequestClass:notifierClass:cdpd:"
+ "initWithDependencies:intendedState:errorState:followupHandler:contextType:"
+ "initWithSOSAdapter:accountsAdapter:authKitAdapter:tooManyPeersAdapter:tapToRadarAdapter:deviceInformationAdapter:secureBackupAdapter:laContextAdapter:personaAdapter:apsConnectionClass:escrowRequestClass:notifierClass:loggerClass:lockStateTracker:reachabilityTracker:cloudKitClassDependencies:cuttlefishXPCConnection:cdpd:"
+ "laContextAdapter"
+ "not in clique, discarding passcode stash"
+ "octagon-escrow-repair: failed to clear last escrow repair attempt: %@"
+ "octagon-escrow-repair: failed to enable with passcode stash secret: %@"
+ "octagon-escrow-repair: unsupported context type: %ld"
+ "participantCount"
+ "passcodeStashAvailable:"
+ "rate limit ignored due to version check"
+ "resetting last escrow repair attempt, ignored error: %@"
+ "setAksEvent:"
+ "setContextType:"
+ "setCredential:type:laContext:error:"
+ "setEscrowRepairAttemptVersion:"
+ "setHasEscrowRepairAttemptVersion:"
+ "setLaContextAdapter:"
+ "setPasscodeStashAvailableForArguments:aksEventContext:"
+ "shouldIgnoreError:"
+ "unsignedCharValue"
+ "v20@0:8C16"
+ "v20@?0i8^{__CFDictionary=}12"
+ "v24@0:8^{_AKSEvent=}16"
+ "v52@0:8@16@24B32Q36@?44"
+ "{?=\"epoch\"b1\"escrowRepairAttemptVersion\"b1\"lastEscrowRepairAttempted\"b1\"lastEscrowRepairTriggered\"b1\"lastHealthCheckup\"b1\"attemptedJoin\"b1\"cdpState\"b1\"icloudAccountState\"b1\"sendingMetricsPermitted\"b1\"trustState\"b1\"isInheritedAccount\"b1\"warmedEscrowCache\"b1\"warnedTooManyPeers\"b1}"
+ "\xf1a"
- "@152@0:8@16@24@32@40@48@56@64@72#80#88#96#104@112@120@128@136@144"
- "@176@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136#144#152#160@168"
- "@196@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128#136#144@152@160B168B172B176@180@188"
- "Failed to save staged outgoing changes for group create/update request for %{public}@: %{public}@"
- "com.apple.keystore.cache.enabled"
- "declineGroupInvite:completion:"
- "enableWithPasscodeStashSecret:account:"
- "fetchAndUpdateParticipantsForGroup:share:completion:"
- "initForContainer:contextID:activeAccount:stateHolder:flagHandler:sosAdapter:octagonAdapter:accountsAdapter:authKitAdapter:personaAdapter:deviceInfoAdapter:secureBackupAdapter:ckksAccountSync:lockStateTracker:cuttlefishXPCWrapper:escrowRequestClass:notifierClass:flowID:deviceSessionID:permittedToSendMetrics:accountIsG:accountIsW:reachabilityTracker:escrowChecker:"
- "initWithContainerName:contextID:activeAccount:cuttlefish:ckksAccountSync:sosAdapter:accountsAdapter:authKitAdapter:personaAdapter:tooManyPeersAdapter:tapToRadarAdapter:lockStateTracker:reachabilityTracker:accountStateTracker:deviceInformationAdapter:secureBackupAdapter:apsConnectionClass:escrowRequestClass:notifierClass:cdpd:"
- "initWithDependencies:intendedState:errorState:followupHandler:"
- "initWithSOSAdapter:accountsAdapter:authKitAdapter:tooManyPeersAdapter:tapToRadarAdapter:deviceInformationAdapter:secureBackupAdapter:personaAdapter:apsConnectionClass:escrowRequestClass:notifierClass:loggerClass:lockStateTracker:reachabilityTracker:cloudKitClassDependencies:cuttlefishXPCConnection:cdpd:"
- "passcodeStashAvailable"
- "setPasscodeStashAvailableForArguments:"
- "{?=\"epoch\"b1\"lastEscrowRepairAttempted\"b1\"lastEscrowRepairTriggered\"b1\"lastHealthCheckup\"b1\"attemptedJoin\"b1\"cdpState\"b1\"icloudAccountState\"b1\"sendingMetricsPermitted\"b1\"trustState\"b1\"isInheritedAccount\"b1\"warmedEscrowCache\"b1\"warnedTooManyPeers\"b1}"
- "\xe1a"

```
