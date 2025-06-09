## audioclocksyncd

> `/usr/libexec/audioclocksyncd`

```diff

-1340.12.0.0.0
-  __TEXT.__text: 0x26f5c
-  __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_stubs: 0x3fa0
-  __TEXT.__objc_methlist: 0x2948
-  __TEXT.__const: 0xd0
-  __TEXT.__oslogstring: 0x26b0
-  __TEXT.__cstring: 0x237e
-  __TEXT.__gcc_except_tab: 0x4f0
-  __TEXT.__objc_methname: 0x6e49
-  __TEXT.__objc_classname: 0x40a
-  __TEXT.__objc_methtype: 0xcc5
-  __TEXT.__unwind_info: 0x8c8
-  __DATA_CONST.__auth_got: 0x300
-  __DATA_CONST.__got: 0x158
-  __DATA_CONST.__const: 0xab8
-  __DATA_CONST.__cfstring: 0x2000
-  __DATA_CONST.__objc_classlist: 0x140
+1400.53.0.0.0
+  __TEXT.__text: 0x30914
+  __TEXT.__auth_stubs: 0x930
+  __TEXT.__objc_stubs: 0x4c80
+  __TEXT.__objc_methlist: 0x3018
+  __TEXT.__const: 0x170
+  __TEXT.__oslogstring: 0x3541
+  __TEXT.__cstring: 0x27cf
+  __TEXT.__gcc_except_tab: 0x1194
+  __TEXT.__objc_methname: 0x8179
+  __TEXT.__objc_classname: 0x45c
+  __TEXT.__objc_methtype: 0x14fc
+  __TEXT.__unwind_info: 0xca0
+  __DATA_CONST.__auth_got: 0x4b0
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__const: 0xca0
+  __DATA_CONST.__cfstring: 0x2420
+  __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x160
-  __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x4ec0
-  __DATA.__objc_selrefs: 0x1570
-  __DATA.__objc_ivar: 0x400
-  __DATA.__objc_data: 0xc80
+  __DATA_CONST.__objc_superrefs: 0x178
+  __DATA_CONST.__objc_intobj: 0x48
+  __DATA.__objc_const: 0x5810
+  __DATA.__objc_selrefs: 0x19a8
+  __DATA.__objc_ivar: 0x494
+  __DATA.__objc_data: 0xdc0
   __DATA.__data: 0x360
-  __DATA.__bss: 0x108
-  __DATA.__common: 0x10
+  __DATA.__bss: 0x138
+  __DATA.__common: 0x4
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/AppleMSG.framework/AppleMSG
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/IOKitten.framework/IOKitten
+  - /System/Library/PrivateFrameworks/MSGExternalSync.framework/MSGExternalSync
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0C75B2E6-B396-39B8-83A6-CC6271D6F912
-  Functions: 1039
-  Symbols:   137
-  CStrings:  1987
+  UUID: F82FBAA7-1CDE-31BD-B786-516E980A5668
+  Functions: 1272
+  Symbols:   202
+  CStrings:  2396
 
Symbols:
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$_NSXPCConnection
+ __Z19alignToExternalSyncP19external_sync_inputP20external_sync_output
+ __Z19load_current_statusv
+ __Z29externalSyncShouldStopRunningv
+ __ZN13MSGController11openServiceEb
+ __ZN13MSGController13SyncGetStatusEjRb
+ __ZN13MSGController14getNextNFramesEhhyPyRy
+ __ZN13MSGController16IsMSGSystemReadyERby
+ __ZN13MSGController21getCurrentMasterFrameERyS0_S0_
+ __ZN13MSGController21registerForTimingInfoEjyRhb
+ __ZN13MSGController23unregisterForTimingInfoEh
+ __ZN13MSGControllerC1Ebb
+ __ZN13MSGControllerD1Ev
+ __ZNKSt3__119__shared_weak_count13__get_deleterERKSt9type_info
+ __ZNSt11logic_errorC2EPKc
+ __ZNSt12length_errorD1Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE21__grow_by_and_replaceEmmmmmmPKc
+ __ZNSt3__119__shared_weak_count14__release_weakEv
+ __ZNSt3__119__shared_weak_countD2Ev
+ __ZNSt3__16chrono12steady_clock3nowEv
+ __ZSt9terminatev
+ __ZTINSt3__119__shared_weak_countE
+ __ZTISt12length_error
+ __ZTISt9exception
+ __ZTVN10__cxxabiv120__si_class_type_infoE
+ __ZTVSt12length_error
+ __ZdlPv
+ __ZdlPvSt19__type_descriptor_t
+ __ZnwmSt19__type_descriptor_t
+ ___cxa_allocate_exception
+ ___cxa_begin_catch
+ ___cxa_end_catch
+ ___cxa_free_exception
+ ___cxa_throw
+ ___error
+ __dispatch_queue_attr_concurrent
+ __os_feature_enabled_impl
+ _clock_gettime
+ _dispatch_group_async
+ _dispatch_group_create
+ _dispatch_group_wait
+ _mach_get_times
+ _mach_thread_self
+ _mach_wait_until
+ _memmove
+ _nanosleep
+ _objc_copyCppObjectAtomic
+ _objc_copyStruct
+ _objc_getProperty
+ _objc_retain_x25
+ _objc_retain_x6
+ _objc_setProperty_atomic
+ _proc_name
+ _proc_pidinfo
+ _pthread_cond_broadcast
+ _pthread_cond_timedwait_relative_np
+ _pthread_mutex_lock
+ _pthread_mutex_unlock
+ _sched_yield
+ _strlen
+ _thread_info
+ _thread_policy_set
CStrings:
+ "%llu"
+ "%s_SyncId_"
+ "%u"
+ ", "
+ ".cxx_construct"
+ "/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/MSG/TSDMSGClockSession.mm"
+ "1"
+ "1400.53"
+ "@\"NSDictionary\"8@?0"
+ "@\"NSObject<OS_dispatch_group>\""
+ "@\"TSDMSGClockSession\""
+ "@20@0:8I16"
+ "@32@0:8r^{?=II{?=QQ}{?=QQ}QQQ*}16@?24"
+ "@44@0:8I16{?=QQ}20^@36"
+ "@52@0:8I16{?=QQ}20Q36^@44"
+ "@?"
+ "@?16@0:8"
+ "Added MSG clock with:\nsyncId: %u\nnominal machInterval: %llu\nnominal syncDuration: (%llu/%llu)"
+ "Added cross-timestamp: (%llu : %llu), syncId: %u\n"
+ "Attempted to decrement a clock session reference count of zero"
+ "B20@0:8i16"
+ "B24@0:8I16B20"
+ "B24@0:8I16i20"
+ "B24@0:8^{?={TSReplayTimestampsHeader=qQQ[13Q][16c]}^{TSReplayTimestampsTimestamp}}16"
+ "B32@0:8I16i20^@24"
+ "B36@0:8q16B24^@28"
+ "B44@0:8^Q16q24B32^@36"
+ "Bad pulse times offset calculated. desiredFrame: %llu, latestFrame: %llu, offset: %llu\n"
+ "Calculated future frame#: %llu, time: %llu\n"
+ "ClockSessionRefCounter"
+ "Deregistered stale clock session for pid: %i\n"
+ "Exception thrown in MSG.framework: %s"
+ "Exception thrown in MSG.framework: %s\n"
+ "Exception thrown while getting syncId status: %s"
+ "Exception thrown while running MSG clock thread: %s, syncId: %u"
+ "Failed to add MSG clock"
+ "Failed to add MSG clock cross-timestamp for syncId: %u\n"
+ "Failed to calculate MAT offset because MCT < MAT. MCT: %llu, MAT: %llu\n"
+ "Failed to calculate MAT offset from MCT. Error: %i\n"
+ "Failed to deregister stale clock session for pid: %i\n"
+ "Failed to get TSDClockManager instance"
+ "Failed to get TSDClockManager singleton"
+ "Failed to get persistent clock id from user id: %@, error: 0x%x\n"
+ "Failed to get sync status from MSG framework, status: %x"
+ "Failed to get thread information. Error: %i\n"
+ "Failed to get tracking info: 0x%x for syncId: %u\n"
+ "Failed to get tracking info: 0x%x, syncId: %u\n"
+ "Failed to get user clock from ID: 0x%llx\n"
+ "Failed to getNextNFrames, error: 0x%x"
+ "Failed to register for timing info: 0x%x, syncId: %u\n"
+ "Failed to remove MSG clock"
+ "Failed to set thread scheduling policy. Error: %i\n"
+ "Failed to unregister for syncId timing info: 0x%x, syncId: %u\n"
+ "Future frame time of 0 detected for frame: %llu!"
+ "Handling external sync MSG notification: %@"
+ "I24@0:8I16i20"
+ "I36@0:8r^{?=II{?=QQ}{?=QQ}QQQ*}16i24@?28"
+ "LocalClockSourceFromNTP"
+ "LockState"
+ "MAT/MCT offset greater than INT64_MAX. MCT: %llu, MAT: %llu\n"
+ "MSG clock session is already running. Ignoring start request.\n"
+ "MSG clock session is not running. Ignoring stop request.\n"
+ "MSG clock thread exited because of an error, restarting in %u ms.\n"
+ "MSG clock thread exiting for syncId: %u\n"
+ "MSG clock thread starting for syncId: %u\n"
+ "MSG service shutdown sessions for pid: %i due to IPC disconnect\n"
+ "MSG service unavailable"
+ "MSGService: startExternalSync: syncId: %u, triggerId: %u, nominalDuration: (%llu/%llu), syncMultiplier: (%llu/%llu), extTriggerToleranceNs: %llu, toleranceSyncOutputNs: %llu, timeoutNs: %llu, processId: %i, result :%i\n"
+ "MSGService: stopAllClockSessionsForProcess: processId: %i\n"
+ "MSGService: stopAllExternalSyncsForProcess: processId: %i\n"
+ "MSGService: stopExternalSync: triggerId: %u, processId: %i\n"
+ "No ref count for process"
+ "No registered session for syncId: %u\n"
+ "Nominal sync duration cannot have a denominator value of 0"
+ "Nominal sync period: (%llu/%llu), nominal syncs per poll: %llu, syncId: %u, matOffset: %lli\n"
+ "Nominal trigger duration too large"
+ "NtpAnchorOffsetNsec"
+ "OutOfBounds"
+ "Overflow calculating domain time for sync pulse #: %llu\n"
+ "Overflow during margin calculation:\ntriggerPeriodTicks: %llu\ntriggerMarginTicks: %llu\nsyncMarginMachTicks: %llu\n"
+ "Q20@0:8i16"
+ "Q24@0:8I16i20"
+ "Q28@0:8I16^@20"
+ "Q32@0:8@16^@24"
+ "Q32@0:8I16i20^@24"
+ "Q48@0:8I16{?=QQ}20i36^@40"
+ "Q56@0:8I16{?=QQ}20Q36i44^@48"
+ "Q56@0:8Q16Q24C32B36@40^@48"
+ "Removed MSG clock with syncId: %u\n"
+ "Removed stale MSG kernel clock for syncId: %u"
+ "SessionStopped"
+ "Sync id must be 0. Received sync id: %u\n"
+ "T@\"NSObject<OS_dispatch_group>\",&,V_dispatchGroup"
+ "T@\"NSString\",R,N,V_userId"
+ "T@\"TSDMSGClockSession\",R,N,V_session"
+ "T@?,N,V_callback"
+ "TB,N,V_clockThreadRunning"
+ "TB,N,V_hasLocalClockSourceFromNTP"
+ "TB,N,V_hasNtpAnchorOffsetNsec"
+ "TB,N,V_localClockSourceFromNTP"
+ "TB,N,V_triggerPresent"
+ "TB,V_clockThreadShouldRun"
+ "TB,V_syncSessionLocked"
+ "TC,V_syncSessionThreadState"
+ "TI,R,N,V_syncId"
+ "TQ,N,V_threadRestarts"
+ "TQ,R,N,V_clockId"
+ "TQ,R,N,V_nominalSyncDurationNsRounded"
+ "TQ,V_maxTargetDuration"
+ "TQ,V_nominalTriggerDurationNs"
+ "TSDMSGClockSession"
+ "TSDMSGExtSyncSession"
+ "TSDMSGService"
+ "TSDMSGSyncSession thread exiting.\n"
+ "TSDgPTPClock setPreferredGm(%u) = %ld"
+ "TSDgPTPClock updateNtpAnchorOffset(%lld %d) = %ld"
+ "Td,R,N,V_nominalSyncDurationNs"
+ "Ti,V_exitStatus"
+ "Timed out waiting for external sync threads to stop."
+ "Tq,N,V_ntpAnchorOffsetNsec"
+ "TriggerPresent"
+ "T{?=II{?=QQ}{?=QQ}QQQ*},R,N,V_config"
+ "T{?=QQ},R,N,V_nominalSyncDuration"
+ "T{_opaque_pthread_cond_t=q[40c]},N,V_clockSessionCond"
+ "T{_opaque_pthread_cond_t=q[40c]},N,V_sessionCond"
+ "T{_opaque_pthread_mutex_t=q[56c]},N,V_clockSessionMutex"
+ "T{_opaque_pthread_mutex_t=q[56c]},N,V_sessionMutex"
+ "T{external_sync_output=if},V_extSyncOutputs"
+ "T{shared_ptr<std::counting_semaphore<3>>=^v^{__shared_weak_count}},V_extSyncSem"
+ "T{timespec=qq},R,N,V_startTime"
+ "Unexpected error waiting for MSG clock session to start: %i"
+ "Unexpected error waiting for MSG clock session to stop: %i"
+ "Unexpected error waiting for sync session to start: %i"
+ "Unexpected frame detected after sleep. detected: %llu, desired: %llu, syncId: %u\n"
+ "]\n"
+ "_activeClockSessionsBySyncId"
+ "_activeExtSyncSessionsByPid"
+ "_callback"
+ "_clockId"
+ "_clockSessionCond"
+ "_clockSessionMutex"
+ "_clockSessionsLock"
+ "_clockThreadRunning"
+ "_clockThreadShouldRun"
+ "_config"
+ "_dispatchGroup"
+ "_exitStatus"
+ "_extSyncCallbackHandlers"
+ "_extSyncOutputs"
+ "_extSyncSem"
+ "_extSyncSessionsLock"
+ "_hasLocalClockSourceFromNTP"
+ "_hasNtpAnchorOffsetNsec"
+ "_localClockSourceFromNTP"
+ "_maxTargetDuration"
+ "_nominalSyncDuration"
+ "_nominalSyncDurationNs"
+ "_nominalSyncDurationNsRounded"
+ "_nominalTriggerDurationNs"
+ "_ntpAnchorOffsetNsec"
+ "_refCntsByPid"
+ "_session"
+ "_sessionCond"
+ "_sessionMutex"
+ "_startTime"
+ "_syncId"
+ "_syncSessionLocked"
+ "_syncSessionThreadState"
+ "_threadRestarts"
+ "_triggerPresent"
+ "_userId"
+ "addClockSessionRef:refCnt:pid:session:"
+ "addCopresencePTPInstance:ntpAndUpTimeOffsetNsec:isLocalClockSourceFromNTP:error:"
+ "addCopresencePTPInstanceRefWithError:"
+ "addMSGClock:withNominalSyncDuration:forProcess:error:"
+ "addMSGClock:withNominalSyncDuration:reply:"
+ "addMSGClockRef:forProcess:error:"
+ "addMSGClockRef:reply:"
+ "addPersistentUserFilteredClockRef:error:"
+ "addPersistentUserFilteredClockWithMachInterval:domainInterval:usingFilterShift:isAdaptive:withUserID:error:"
+ "addRef:"
+ "addRef:withCnt:"
+ "alignToExternalSync args:\nminTargetFrameDur: %llu\nmaxTargetFrameDur: %llu\nminOutputFrameDur: %llu\nmaxOutputFrameDur: %llu\nnominalSystemFramerate: %u\nfrequencyMultiplier: %u\ntriggerId: %u\nsyncId: %u\nisSimulation: %i"
+ "alignToExternalSync finished with status: 0x%x, exit state: 0x%x, detected fps:%f\n"
+ "allKeys"
+ "appendFormat:"
+ "appendString:"
+ "basic_string"
+ "callback"
+ "checkClockSessionRegistered:removeStaleKernelClock:"
+ "checkExtSyncSessionRegistered:"
+ "checkRemoveKernelClock:"
+ "checkRemoveStaleSessions:"
+ "clockId"
+ "clockSessionCond"
+ "clockSessionMutex"
+ "clockThreadRunning"
+ "clockThreadShouldRun"
+ "code"
+ "com.apple.TimeSync.MSG.message"
+ "com.apple.TimeSync.MSG.restore-clock-session"
+ "com.apple.TimeSync.MSG.start-clock-session"
+ "com.apple.TimeSync.MSG.start-external-sync"
+ "com.apple.TimeSync.MSG.stop-clock-session"
+ "com.apple.TimeSync.MSG.stop-external-sync"
+ "com.apple.private.timesync.%@.syncsession"
+ "config"
+ "createSession:nominalSyncDuration:clockId:error:"
+ "currentConnection"
+ "deregisterClockSession:pid:removeAllRefs:"
+ "deregisterExtSyncSession:pid:"
+ "detachNewThreadWithBlock:"
+ "dispatchGroup"
+ "dockReplayTimestamps:"
+ "exitStatus"
+ "extSyncCallbackHandler:msgType:args:"
+ "extSyncOutputs"
+ "extSyncSem"
+ "getClkUserIdForSyncId:"
+ "getClockSessionForSyncId:"
+ "getClockSessionRefCnt:process:"
+ "getMSGClock:error:"
+ "getMSGClock:reply:"
+ "getPersistentUserFilteredClockIdentifier:error:"
+ "getPidForSyncSession:"
+ "getPids"
+ "getRef:"
+ "getRefTotal"
+ "handleProcessDisconnect:"
+ "hasLocalClockSourceFromNTP"
+ "hasNtpAnchorOffsetNsec"
+ "i20@0:8i16"
+ "i24@0:8@16"
+ "i24@0:8Q16"
+ "i24@0:8^B16"
+ "i28@0:8I16i20B24"
+ "i36@0:8r^{?=II{?=QQ}{?=QQ}QQQ*}16i24@?28"
+ "i40@0:8I16Q20i28^@32"
+ "i48@0:8I16{?=QQ}20i36^@40"
+ "i56@0:8I16{?=QQ}20Q36i44^@48"
+ "initWithCString:encoding:"
+ "initWithSession:"
+ "isExtSyncSessionRunning"
+ "isMSGServiceAvailable:"
+ "isMSGSyncRunning:"
+ "isSimulation:"
+ "localClockSourceFromNTP"
+ "longLongValue"
+ "longValue"
+ "maxTargetDuration"
+ "mgr != nil"
+ "monitorSyncSessionThread"
+ "msgServiceNotification:arguments:"
+ "msgType"
+ "msgType: %@, args: ["
+ "msg_audio_clock"
+ "msg_ext_sync"
+ "nominalSyncDuration"
+ "nominalSyncDurationNs"
+ "nominalSyncDurationNsRounded"
+ "nominalTriggerDurationDen"
+ "nominalTriggerDurationNs"
+ "nominalTriggerDurationNum"
+ "ntpAnchorOffsetNsec"
+ "numberWithBool:"
+ "numberWithInteger:"
+ "numberWithUnsignedLong:"
+ "procName"
+ "q"
+ "q16@0:8"
+ "registerClockSession:nominalSyncDuration:pid:session:"
+ "registerExtSyncSession:pid:callback:"
+ "removeAllRefs:"
+ "removeMSGClock:forProcess:error:"
+ "removeMSGClock:reply:"
+ "removePersistentUserFilteredClock:error:"
+ "removeRef:"
+ "removeSuccess == YES"
+ "restoreClockSession:nominalSyncDuration:refCnt:pid:session:"
+ "restoreMSGClockSession:nominalSyncDuration:refCnt:forProcess:error:"
+ "restoreMSGClockSession:nominalSyncDuration:refCnt:reply:"
+ "restoreWithSyncId:nominalSyncDuration:error:"
+ "runClockSessionThread"
+ "runSyncSessionThread"
+ "self->_clockId != TSNullClockIdentifier"
+ "session"
+ "sessionCond"
+ "sessionMutex"
+ "sessionRunTimeNs:"
+ "setCallback:"
+ "setClockSessionCond:"
+ "setClockSessionMutex:"
+ "setClockThreadRunning:"
+ "setClockThreadShouldRun:"
+ "setDispatchGroup:"
+ "setExitStatus:"
+ "setExtSyncOutputs:"
+ "setExtSyncSem:"
+ "setHasLocalClockSourceFromNTP:"
+ "setHasNtpAnchorOffsetNsec:"
+ "setLocalClockSourceFromNTP:"
+ "setMaxTargetDuration:"
+ "setNominalTriggerDurationNs:"
+ "setNtpAnchorOffsetNsec:"
+ "setPreferredGM:error:"
+ "setSessionCond:"
+ "setSessionMutex:"
+ "setSyncSessionLocked:"
+ "setSyncSessionThreadState:"
+ "setThreadRestarts:"
+ "setTriggerPresent:"
+ "sharedMSGService"
+ "startClockThread:"
+ "startExternalSync:forProcess:withCallback:"
+ "startMSGExternalSync:reply:"
+ "startReplayTimestamps:"
+ "startTime"
+ "status == 0 "
+ "stop"
+ "stopAllClockSessionsForProcess:"
+ "stopAllExternalSyncsForProcess:"
+ "stopClockThread:"
+ "stopExternalSync:forProcess:"
+ "stopMSGExternalSync:reply:"
+ "stopReplayTimestamps:"
+ "stringByAppendingFormat:"
+ "sync status:\nestimatedTicksUntilFullySynced: %lli\nticksSinceLastReceivedTrigger: %u\nframesSinceLastInvalidTrigger: %u\nversion: %u\nisFullySyncedAndLocked: %u\nreceivedEnoughTriggers: %u\n"
+ "syncConfig"
+ "syncId"
+ "syncMultiplierDen"
+ "syncMultiplierNum"
+ "syncSessionLocked"
+ "syncSessionThreadState"
+ "threadRestarts"
+ "timeoutNs"
+ "toleranceExternalTriggerNs"
+ "toleranceSyncOutputNs"
+ "triggerId"
+ "triggerPresent"
+ "unsignedLongValue"
+ "updateNtpAnchorOffset:isLocalClockSourceFromNTP:error:"
+ "userId"
+ "v20@?0S8r^{ScalarArgsArrayUserReference=[16Q]I}12"
+ "v24@0:8@?<v@?B>16"
+ "v24@0:8q16"
+ "v24@0:8{external_sync_output=if}16"
+ "v28@0:8I16@?<v@?I>20"
+ "v28@0:8I16@?<v@?Q@\"NSError\">20"
+ "v28@0:8S16r^{ScalarArgsArrayUserReference=[16Q]I}20"
+ "v28@0:8i16Q20"
+ "v28@?0@\"TSDMSGExtSyncSession\"8S16r^{ScalarArgsArrayUserReference=[16Q]I}20"
+ "v32@0:8r^{?=II{?=QQ}{?=QQ}QQQ*}16@?24"
+ "v32@0:8r^{?=II{?=QQ}{?=QQ}QQQ*}16@?<v@?I>24"
+ "v32@0:8{shared_ptr<std::counting_semaphore<3>>=^v^{__shared_weak_count}}16"
+ "v36@0:8@16S24r^{ScalarArgsArrayUserReference=[16Q]I}28"
+ "v44@0:8I16{?=QQ}20@?36"
+ "v44@0:8I16{?=QQ}20@?<v@?Q@\"NSError\">36"
+ "v52@0:8I16{?=QQ}20Q36@?44"
+ "v52@0:8I16{?=QQ}20Q36@?<v@?Q@\"NSError\">44"
+ "v64@0:8{_opaque_pthread_cond_t=q[40c]}16"
+ "v80@0:8{_opaque_pthread_mutex_t=q[56c]}16"
+ "withConfig:andCallback:"
+ "withSyncId:nominalSyncDuration:error:"
+ "{?=\"numerator\"Q\"denominator\"Q}"
+ "{?=\"syncId\"I\"triggerId\"I\"nominalTriggerDuration\"{?=\"numerator\"Q\"denominator\"Q}\"syncMultiplier\"{?=\"numerator\"Q\"denominator\"Q}\"toleranceExternalTriggerNs\"Q\"toleranceSyncOutputNs\"Q\"timeoutNs\"Q\"simulationFilePath\"*}"
+ "{?=II{?=QQ}{?=QQ}QQQ*}16@0:8"
+ "{?=QQ}16@0:8"
+ "{_opaque_pthread_cond_t=\"__sig\"q\"__opaque\"[40c]}"
+ "{_opaque_pthread_cond_t=q[40c]}16@0:8"
+ "{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}"
+ "{_opaque_pthread_mutex_t=q[56c]}16@0:8"
+ "{external_sync_output=\"state\"i\"approxDetectedFPS\"f}"
+ "{external_sync_output=if}16@0:8"
+ "{shared_ptr<std::counting_semaphore<3>>=\"__ptr_\"^v\"__cntrl_\"^{__shared_weak_count}}"
+ "{shared_ptr<std::counting_semaphore<3>>=^v^{__shared_weak_count}}16@0:8"
+ "{timespec=\"tv_sec\"q\"tv_nsec\"q}"
+ "{timespec=qq}16@0:8"
- "1340.12"
- "addCopresencePTPInstance:error:"

```
