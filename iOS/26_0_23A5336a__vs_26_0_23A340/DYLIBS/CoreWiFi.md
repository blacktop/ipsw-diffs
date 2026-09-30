## CoreWiFi

> `/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`

```diff

 976.113.0.0.0
-  __TEXT.__text: 0x166a84
-  __TEXT.__auth_stubs: 0x1280
-  __TEXT.__objc_methlist: 0xe3f4
-  __TEXT.__const: 0x798
+  __TEXT.__text: 0x16effc
+  __TEXT.__auth_stubs: 0x12b0
+  __TEXT.__objc_methlist: 0xe8cc
+  __TEXT.__const: 0x7a8
   __TEXT.__dlopen_cstrs: 0x891
-  __TEXT.__cstring: 0x1a701
-  __TEXT.__gcc_except_tab: 0x5fa8
-  __TEXT.__oslogstring: 0x15acc
+  __TEXT.__cstring: 0x1b51c
+  __TEXT.__gcc_except_tab: 0x6458
+  __TEXT.__oslogstring: 0x1750b
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x44c0
-  __TEXT.__objc_classname: 0xc2a
-  __TEXT.__objc_methname: 0x1ff79
-  __TEXT.__objc_methtype: 0x30e9
-  __TEXT.__objc_stubs: 0x17ca0
-  __DATA_CONST.__got: 0x708
-  __DATA_CONST.__const: 0x4410
-  __DATA_CONST.__objc_classlist: 0x318
+  __TEXT.__unwind_info: 0x45d0
+  __TEXT.__objc_classname: 0xc8f
+  __TEXT.__objc_methname: 0x21176
+  __TEXT.__objc_methtype: 0x31d1
+  __TEXT.__objc_stubs: 0x188c0
+  __DATA_CONST.__got: 0x768
+  __DATA_CONST.__const: 0x4538
+  __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0xf0
+  __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7080
+  __DATA_CONST.__objc_selrefs: 0x7388
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0x2c8
+  __DATA_CONST.__objc_superrefs: 0x2d8
   __DATA_CONST.__objc_arraydata: 0x18b0
-  __AUTH_CONST.__auth_got: 0x950
+  __AUTH_CONST.__auth_got: 0x968
   __AUTH_CONST.__const: 0x2440
-  __AUTH_CONST.__cfstring: 0x168c0
-  __AUTH_CONST.__objc_const: 0x12878
-  __AUTH_CONST.__objc_intobj: 0x3660
+  __AUTH_CONST.__cfstring: 0x16e60
+  __AUTH_CONST.__objc_const: 0x12fe8
+  __AUTH_CONST.__objc_intobj: 0x3690
   __AUTH_CONST.__objc_arrayobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x1e0
-  __AUTH.__objc_data: 0xaa0
+  __AUTH.__objc_data: 0xb40
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0xfe0
-  __DATA.__data: 0xb78
+  __DATA.__objc_ivar: 0x1058
+  __DATA.__data: 0xbd8
   __DATA.__bss: 0x150
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_ivar: 0x54

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
+  - /System/Library/PrivateFrameworks/Centauri.framework/Centauri
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/IO80211.framework/IO80211

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 735E26E6-1A33-39FA-A9C5-7A699D67F5F8
-  Functions: 5979
-  Symbols:   946
-  CStrings:  13226
+  UUID: 648D1013-C502-3689-B212-F41285ACD5E4
+  Functions: 6103
+  Symbols:   964
+  CStrings:  13623
 
Symbols:
+ _CENCastPowerTableVote
+ _CENPowerTableEvaluationNewAssetVersions
+ _CENPowerTableEvaluationNotification
+ _CENPowerTableEvaluationPreviousAssetVersions
+ _CENPowerTableEvaluationReadinessTimeout
+ _CENPowerTableEvaluationSessionIdentifier
+ _CENPowerTableEvaluationSessionState
+ _CENPowerTableEvaluationVotingTimeout
+ _CENSetPowerTableEvaluationReadiness
+ _NSLocalizedFailureReasonErrorKey
+ _OBJC_CLASS_$_CWFAssetPowerTableElectionManager
+ _OBJC_CLASS_$_CWFAssetPowerTableElector
+ _OBJC_CLASS_$_NSCondition
+ _OBJC_CLASS_$_NSDistributedNotificationCenter
+ _OBJC_METACLASS_$_CWFAssetPowerTableElectionManager
+ _OBJC_METACLASS_$_CWFAssetPowerTableElector
+ __dispatch_queue_attr_concurrent
+ _objc_moveWeak
CStrings:
+ "!"
+ "%d"
+ "%{public}s::%d:%s: CWFAssetPowerTableElector has gone away"
+ "%{public}s::%d:%s: CWFEventTypeDriverAvailable %@"
+ "%{public}s::%d:%s: CWFEventTypeInterfaceAdded %@"
+ "%{public}s::%d:%s: Call to delegate powerTableReadiness Failed"
+ "%{public}s::%d:%s: Call to delegate powerTableVote Failed"
+ "%{public}s::%d:%s: Calling performVersionFetch"
+ "%{public}s::%d:%s: Calling performVersionFetchBlockify again, duration until deadline %f"
+ "%{public}s::%d:%s: Calling performVersionFetchBlockify success"
+ "%{public}s::%d:%s: Calling powerTableReadiness WeCan: %d"
+ "%{public}s::%d:%s: Calling powerTableVote WeLike: %d"
+ "%{public}s::%d:%s: Calling retryingVersionFetchBlock dueDate %@ now %@"
+ "%{public}s::%d:%s: Done powerTableVote WeLike: %d call success: %d"
+ "%{public}s::%d:%s: ERROR failed to retrieve current PT Version, setting areWeReady = FALSE"
+ "%{public}s::%d:%s: ERROR failed to retrieve current PT Version, setting voteResult = FALSE"
+ "%{public}s::%d:%s: ERROR got notice of RequestingVotes when current state is %@ instead of %@ "
+ "%{public}s::%d:%s: ERROR got notice of RequestingVotes when current state is %@ instead of %@ - desc %@"
+ "%{public}s::%d:%s: ERROR got notice of StateStarting when current state is %@ instead of %@ "
+ "%{public}s::%d:%s: ERROR got notice of StateStarting when current state is %@ instead of %@ - desc %@"
+ "%{public}s::%d:%s: ERROR got state CENPowerTableEvaluationStateUninitialized, why would we get this??"
+ "%{public}s::%d:%s: ERROR performVersionFetchBlockify never succeeded, exiting"
+ "%{public}s::%d:%s: Election NSNotification %@"
+ "%{public}s::%d:%s: Error Session Creation Blocked by _maxSessionActiveInterval, sending powerTableReadiness FALSE - self desc: %@"
+ "%{public}s::%d:%s: Failed access userDefaults"
+ "%{public}s::%d:%s: Failed to alloc _apiQueue"
+ "%{public}s::%d:%s: Failed to alloc _coordinationQueue"
+ "%{public}s::%d:%s: Failed to alloc _signalQueue"
+ "%{public}s::%d:%s: Failed to alloc _waitingQueue"
+ "%{public}s::%d:%s: Failed to start monitoring for CWFEventTypeDriverAvailable event; error %{public}@"
+ "%{public}s::%d:%s: Failed to start monitoring for CWFEventTypeInterfaceAdded event; error %{public}@"
+ "%{public}s::%d:%s: Got unexpected Readiness Request with session %@ when existng session running %@ which was started at %@"
+ "%{public}s::%d:%s: Missing case"
+ "%{public}s::%d:%s: Recovered Missing _powerTableEvaluationState from persisted data %@"
+ "%{public}s::%d:%s: Recovered Missing _powerTableSession from persisted data %@"
+ "%{public}s::%d:%s: Recovered Missing _powerTableSessionStartDate from persisted data %@"
+ "%{public}s::%d:%s: SET _driverAvailEventOccurred %d"
+ "%{public}s::%d:%s: SET _interfaceAddedEventOccurred %d"
+ "%{public}s::%d:%s: Sending powerTableReadiness areWeReady %d"
+ "%{public}s::%d:%s: Sending powerTableVote voteResult %d for session %@"
+ "%{public}s::%d:%s: Session Created - Session %@ interval %f - self desc: %@"
+ "%{public}s::%d:%s: Session id %@ has expired past max interval of %f, recovering by removing stale session - error %@"
+ "%{public}s::%d:%s: Session id %@ has missing start date, recovering by removing session id - error %@"
+ "%{public}s::%d:%s: Session id %@ was recovered: desc %@"
+ "%{public}s::%d:%s: Skipping CWFEventTypeDriverAvailable"
+ "%{public}s::%d:%s: Skipping CWFEventTypeInterfaceAdded"
+ "%{public}s::%d:%s: Timed Out waiting to retrieve valid performVersionFetch"
+ "%{public}s::%d:%s: Wait done: _interfaceAddedEventOccurred %d _driverAvailEventOccurred %d"
+ "%{public}s::%d:%s: Wait for _condInterfaceAddedAfterEvaluationStart timed out at date %@"
+ "%{public}s::%d:%s: Wait for _readyToFetchLoadedPTCondition timed out at date %@"
+ "%{public}s::%d:%s: _interfaceAddedEventCondition %@ or _interfaceAddedEventOccurred %d Done"
+ "%{public}s::%d:%s: _readyToFetchLoadedPT FALSE, will block waiting for _readyToFetchLoadedPTCondition until date: %@"
+ "%{public}s::%d:%s: _readyToFetchLoadedPT TRUE, will fetch PT until date: %@"
+ "%{public}s::%d:%s: identifier has wrong type"
+ "%{public}s::%d:%s: identifier missing"
+ "%{public}s::%d:%s: identifier: %@ \nstate: %@ \nnewAssetVersions[CENPowerTableVoterWiFi] %@ newAssetVersions[CENPowerTableVoterBT] %@ \npreviousAssetVersions[CENPowerTableVoterWiFi] %@ previousAssetVersions[CENPowerTableVoterBT] %@"
+ "%{public}s::%d:%s: identifier: %@ state: %@ previous state: %@"
+ "%{public}s::%d:%s: init complete"
+ "%{public}s::%d:%s: inside strong retryingVersionFetchBlock"
+ "%{public}s::%d:%s: invalid state %ld"
+ "%{public}s::%d:%s: kPowerTable__max_session_active_interval to %@"
+ "%{public}s::%d:%s: kPowerTable_ignore_driver_availability is %@"
+ "%{public}s::%d:%s: kPowerTable_ignore_interface_up is %@"
+ "%{public}s::%d:%s: kPowerTable_ignore_readiness_input is %@"
+ "%{public}s::%d:%s: kPowerTable_ignore_readiness_input is set, bailing before processing input"
+ "%{public}s::%d:%s: kPowerTable_ignore_requesting_vote_input is %@"
+ "%{public}s::%d:%s: kPowerTable_ignore_requesting_vote_input is set, bailing before processing input"
+ "%{public}s::%d:%s: kPowerTable_ignore_start_input is %@"
+ "%{public}s::%d:%s: kPowerTable_ignore_start_input is set, bailing before processing input"
+ "%{public}s::%d:%s: kPowerTable_override_readiness_response to %@"
+ "%{public}s::%d:%s: kPowerTable_override_ver_fetch_success is %@"
+ "%{public}s::%d:%s: kPowerTable_override_vote_response to %@"
+ "%{public}s::%d:%s: new asset versions has wrong count %lu"
+ "%{public}s::%d:%s: new asset versions has wrong type"
+ "%{public}s::%d:%s: new asset versions missing"
+ "%{public}s::%d:%s: new asset versions[CENPowerTableVoterBT] has wrong type"
+ "%{public}s::%d:%s: new asset versions[CENPowerTableVoterWiFi] has wrong type"
+ "%{public}s::%d:%s: no strong retryingVersionFetchBlock"
+ "%{public}s::%d:%s: powerTableReadiness WeCan: %d call success %d"
+ "%{public}s::%d:%s: previous asset versions has wrong type"
+ "%{public}s::%d:%s: previous asset versions missing"
+ "%{public}s::%d:%s: previous bt asset version has wrong type"
+ "%{public}s::%d:%s: previous wifi asset version has wrong type"
+ "%{public}s::%d:%s: setEventHandler Event %@"
+ "%{public}s::%d:%s: setupInterfaceAddedAndDriverAvailMonitor complete"
+ "%{public}s::%d:%s: state has wrong type"
+ "%{public}s::%d:%s: state missing"
+ "%{public}s::%d:%s: unexpected notification %s"
+ "%{public}s::%d:%s: waitForInterfaceAdded completed _interfaceAddedEventOccurred %d _driverAvailEventOccurred %d"
+ "%{public}s::%d:%s: will call waitForInterfaceAdded to block until date: %@"
+ "+[CWFAssetPowerTableElector powerTableEvaluationStateAsString:]"
+ "-[CWFAssetPowerTableElector _handleCENPowerTableEvaluationNotification:]"
+ "-[CWFAssetPowerTableElector _handleCENPowerTableEvaluationNotification:]_block_invoke"
+ "-[CWFAssetPowerTableElector checkForExistingSessionAndRecover]"
+ "-[CWFAssetPowerTableElector dispatchWaitForInterfaceAddedThenBlockify:completion:]_block_invoke"
+ "-[CWFAssetPowerTableElector handleCENPowerTableEvaluationStateRequestingReadiness:dueInterval:]"
+ "-[CWFAssetPowerTableElector handleCENPowerTableEvaluationStateRequestingReadiness:dueInterval:]_block_invoke"
+ "-[CWFAssetPowerTableElector handleCENPowerTableEvaluationStateRequestingReadiness:dueInterval:]_block_invoke_2"
+ "-[CWFAssetPowerTableElector handleCENPowerTableEvaluationStateRequestingVotes:dueInterval:]"
+ "-[CWFAssetPowerTableElector handleCENPowerTableEvaluationStateRequestingVotes:dueInterval:]_block_invoke"
+ "-[CWFAssetPowerTableElector handleCENPowerTableEvaluationStateRequestingVotes:dueInterval:]_block_invoke_2"
+ "-[CWFAssetPowerTableElector handleCENPowerTableEvaluationStateStarting:]"
+ "-[CWFAssetPowerTableElector handleCENPowerTableEvaluationStateUninitialized]"
+ "-[CWFAssetPowerTableElector initWithNotificationCenter:]"
+ "-[CWFAssetPowerTableElector isSessionCurrentlyBlocking]"
+ "-[CWFAssetPowerTableElector isSessionCurrentlyBlocking]_block_invoke"
+ "-[CWFAssetPowerTableElector performPowerTableVersionRequestWithDeadline:]"
+ "-[CWFAssetPowerTableElector performPowerTableVersionRequestWithDeadline:]_block_invoke"
+ "-[CWFAssetPowerTableElector performVersionFetchBlockify:]"
+ "-[CWFAssetPowerTableElector performVersionFetchBlockify:]_block_invoke"
+ "-[CWFAssetPowerTableElector persist:forKey:]"
+ "-[CWFAssetPowerTableElector powerTableReadiness:]"
+ "-[CWFAssetPowerTableElector powerTableVote:]"
+ "-[CWFAssetPowerTableElector setupInterfaceAddedAndDriverAvailMonitor]"
+ "-[CWFAssetPowerTableElector setupInterfaceAddedAndDriverAvailMonitor]_block_invoke"
+ "-[CWFAssetPowerTableElector waitForInterfaceAdded:]"
+ "-[CWFAssetPowerTableElector waitForPowerTableBootedThenVoteInBlock:completion:]"
+ "2n"
+ "@\"<CWFAssetPowerTableElectorDelegate>\""
+ "@\"CWFAssetPowerTableElector\""
+ "@\"NSCondition\""
+ "@\"NSDistributedNotificationCenter\""
+ "@\"NSNotificationCenter\""
+ "Aborted"
+ "Accepted"
+ "B24@0:8@\"NSMutableDictionary\"16"
+ "B36@0:8@\"NSString\"16q24B32"
+ "B36@0:8@16q24B32"
+ "CWFAssetPowerTableElectionManager"
+ "CWFAssetPowerTableElector"
+ "CWFAssetPowerTableElectorDelegate"
+ "CWFPowerTableElectionExistingSessionPastMaxSessionInterval"
+ "CWFPowerTableElectionRxReadinessWhileExistingSessionPastMaxSessionInterval"
+ "CWFPowerTableElectionRxReadinessWithCorruptActiveSession"
+ "CWFPowerTableElectionTimedOutWaitingForPerformVersionFetch"
+ "CWFPowerTableElectionUnexpectedStateRequestingVotes"
+ "CWFPowerTableElectionUnexpectedStateStarting"
+ "Current Persistent Session Info: kPersistence_session_id_current %@, kPersistence_session_start_date_current %@"
+ "Current Process info: pid %d, powerTableEvaluationState %ld, _powerTableSession %@, _powerTableSessionStartDate %@"
+ "Detailed All Persistent Session Info: %@"
+ "Detailed Current Persistent Session Info: %@"
+ "NSNotification"
+ "NotFound"
+ "PTV_BINARY_FILENAME"
+ "PTV_TABLE_VERSION"
+ "Rejected"
+ "RequestingReadiness"
+ "RequestingVotes"
+ "T@\"<CWFAssetPowerTableElectorDelegate>\",W,N,V_delegate"
+ "T@\"CWFAssetPowerTableElector\",&,N,V__elector"
+ "T@\"CWFInterface\",&,N,V_wifiInterface"
+ "T@\"CWFInterface\",R,N"
+ "T@\"NSCondition\",&,N,V__condPowerTableFetched"
+ "T@\"NSCondition\",&,N,V__driverAvailEventCondition"
+ "T@\"NSCondition\",&,N,V__interfaceAddedEventCondition"
+ "T@\"NSCondition\",&,N,V__readyToFetchLoadedPTCondition"
+ "T@\"NSDate\",&,N,V__powerTableEvaluationStartDate"
+ "T@\"NSDate\",&,N,V__powerTableRequestingVotesStartDate"
+ "T@\"NSDate\",&,N,V__powerTableSessionStartDate"
+ "T@\"NSDistributedNotificationCenter\",&,N,V__distNotificationCenter"
+ "T@\"NSError\",&,N,V_error"
+ "T@\"NSNotificationCenter\",&,N,V__notificationCenter"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V__apiQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V__coordinationQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V__signalQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V__waitingQueue"
+ "T@\"NSString\",&,N,V__powerTableSession"
+ "TB,N,V__driverAvailEventOccurred"
+ "TB,N,V__interfaceAddedEventOccurred"
+ "TB,N,V__isInternalBuild"
+ "TB,N,V__powerTableFetched"
+ "TB,N,V__readyToFetchLoadedPT"
+ "Td,N,V__dateToBlockWaitingForDriverReload"
+ "Td,N,V__dateToFetchReloadedPowerTableForVoteAssesment"
+ "Td,N,V__maxSessionActiveInterval"
+ "Td,N,V__readinessTimeoutInterval"
+ "Td,N,V__votingTimeoutInterval"
+ "Ti,N,V__pid"
+ "Tq,N,V__powerTableEvaluationState"
+ "Uninitialized"
+ "__apiQueue"
+ "__condPowerTableFetched"
+ "__coordinationQueue"
+ "__dateToBlockWaitingForDriverReload"
+ "__dateToFetchReloadedPowerTableForVoteAssesment"
+ "__distNotificationCenter"
+ "__driverAvailEventCondition"
+ "__driverAvailEventOccurred"
+ "__elector"
+ "__interfaceAddedEventCondition"
+ "__interfaceAddedEventOccurred"
+ "__isInternalBuild"
+ "__maxSessionActiveInterval"
+ "__notificationCenter"
+ "__pid"
+ "__powerTableEvaluationStartDate"
+ "__powerTableEvaluationState"
+ "__powerTableFetched"
+ "__powerTableRequestingVotesStartDate"
+ "__powerTableSession"
+ "__powerTableSessionStartDate"
+ "__readinessTimeoutInterval"
+ "__readyToFetchLoadedPT"
+ "__readyToFetchLoadedPTCondition"
+ "__signalQueue"
+ "__votingTimeoutInterval"
+ "__waitingQueue"
+ "_apiQueue"
+ "_apiQueue retryingVersionFetchBlock"
+ "_condPowerTableFetched"
+ "_coordinationQueue"
+ "_coordinationQueue handleCENPowerTableEvaluationNotification"
+ "_dateToBlockWaitingForDriverReload"
+ "_dateToFetchReloadedPowerTableForVoteAssesment"
+ "_distNotificationCenter"
+ "_driverAvailEventCondition"
+ "_driverAvailEventOccurred"
+ "_elector"
+ "_handleCENPowerTableEvaluationNotification:"
+ "_interfaceAddedEventCondition"
+ "_interfaceAddedEventOccurred"
+ "_isInternalBuild"
+ "_maxSessionActiveInterval"
+ "_notificationCenter"
+ "_pid"
+ "_powerTableEvaluationStartDate"
+ "_powerTableEvaluationState"
+ "_powerTableFetched"
+ "_powerTableRequestingVotesStartDate"
+ "_powerTableSession"
+ "_powerTableSessionStartDate"
+ "_readinessTimeoutInterval"
+ "_readyToFetchLoadedPT"
+ "_readyToFetchLoadedPTCondition"
+ "_signalQueue"
+ "_signalQueue setEventHandler"
+ "_votingTimeoutInterval"
+ "_waitingQueue"
+ "_waitingQueue dispatchWaitForInterfaceAddedThenBlockify"
+ "_wifiInterface"
+ "checkForExistingSessionAndRecover"
+ "com.apple.wifi.CWFAssetPowerTableElector"
+ "com.apple.wifi.CWFAssetPowerTableWorker"
+ "com.apple.wifi.PowerTableSignalQueue"
+ "com.apple.wifi.PowerTableWaitingQueue"
+ "com.apple.wifi.powertable"
+ "dispatchWaitForInterfaceAddedThenBlockify:completion:"
+ "evaluation-start-date"
+ "getPersistedDict"
+ "getPersistedKey:"
+ "getSession:"
+ "getSession:forKey:"
+ "handleCENPowerTableEvaluationNotification:"
+ "handleCENPowerTableEvaluationStateAborted:"
+ "handleCENPowerTableEvaluationStateAccepted:"
+ "handleCENPowerTableEvaluationStateRejected:"
+ "handleCENPowerTableEvaluationStateRequestingReadiness:dueInterval:"
+ "handleCENPowerTableEvaluationStateRequestingVotes:dueInterval:"
+ "handleCENPowerTableEvaluationStateStarting:"
+ "handleCENPowerTableEvaluationStateUninitialized"
+ "ignore-driver-availability"
+ "ignore-interface-up"
+ "ignore-readiness-request"
+ "ignore-start-request"
+ "ignore-vote-request"
+ "initWithNotificationCenter:"
+ "isSessionCurrentlyBlocking"
+ "lock"
+ "max-session-active-interval"
+ "override-readiness-response"
+ "override-ver-fetch-success"
+ "override-vote-response"
+ "performPowerTableVersionRequestWithDeadline"
+ "performPowerTableVersionRequestWithDeadline:"
+ "performVersionFetch"
+ "performVersionFetch:"
+ "performVersionFetchBlockify:"
+ "persist:forKey:"
+ "persistSession:data:forKey:"
+ "persistentDomainForName:"
+ "pid-at-end"
+ "pid-at-start"
+ "powerTableEvaluationStateAsString:"
+ "powerTableEvaluationStringToState:"
+ "powerTableReadiness"
+ "powerTableReadiness:"
+ "powerTableReadiness:voter:vote:"
+ "powerTableVote"
+ "powerTableVote:"
+ "powerTableVote:voter:vote:"
+ "powertable-election-session-id"
+ "powertable-election-session-start-date"
+ "powertable-election-session-state"
+ "powertable-election-sessions-history"
+ "processTransitionToTerminalState:"
+ "pt-ver-final"
+ "pt-ver-initial"
+ "readiness-deadline-date"
+ "readiness-reply"
+ "removeObserver:"
+ "removePersistedKey:"
+ "session-end-date"
+ "session-id"
+ "setEventHandler Event"
+ "setPersistentDomain:forName:"
+ "setWifiInterface:"
+ "set_apiQueue:"
+ "set_condPowerTableFetched:"
+ "set_coordinationQueue:"
+ "set_dateToBlockWaitingForDriverReload:"
+ "set_dateToFetchReloadedPowerTableForVoteAssesment:"
+ "set_distNotificationCenter:"
+ "set_driverAvailEventCondition:"
+ "set_driverAvailEventOccurred:"
+ "set_elector:"
+ "set_interfaceAddedEventCondition:"
+ "set_interfaceAddedEventOccurred:"
+ "set_isInternalBuild:"
+ "set_maxSessionActiveInterval:"
+ "set_notificationCenter:"
+ "set_pid:"
+ "set_powerTableEvaluationStartDate:"
+ "set_powerTableEvaluationState:"
+ "set_powerTableFetched:"
+ "set_powerTableRequestingVotesStartDate:"
+ "set_powerTableSession:"
+ "set_powerTableSessionStartDate:"
+ "set_readinessTimeoutInterval:"
+ "set_readyToFetchLoadedPT:"
+ "set_readyToFetchLoadedPTCondition:"
+ "set_signalQueue:"
+ "set_votingTimeoutInterval:"
+ "set_waitingQueue:"
+ "setupInterfaceAddedAndDriverAvailMonitor"
+ "signal"
+ "unlock"
+ "v16@?0@\"NSNumber\"8"
+ "v28@?0B8@\"NSDictionary\"12@\"NSError\"20"
+ "v32@0:8@16d24"
+ "valueForKey:"
+ "vote-deadline-date"
+ "vote-reply"
+ "vote-start-date"
+ "wait _condPowerTableFetched"
+ "wait _interfaceAddedEventCondition"
+ "wait _readyToFetchLoadedPTCondition"
+ "waitForInterfaceAdded"
+ "waitForInterfaceAdded:"
+ "waitForPowerTableBootedThenVoteInBlock:completion:"
+ "waitUntilDate:"
+ "wifiInterface"
- "%{public}s::%d:%s: NO ELECTOR"
- "-[CWFAssetPowerTable init]"

```
