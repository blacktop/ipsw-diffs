## appconduitd

> `/System/Library/PrivateFrameworks/AppConduit.framework/Support/appconduitd`

```diff

-395.0.0.0.0
-  __TEXT.__text: 0x58c04
-  __TEXT.__auth_stubs: 0xa00
-  __TEXT.__objc_stubs: 0x7e60
-  __TEXT.__objc_methlist: 0x3bec
+396.100.2.0.0
+  __TEXT.__text: 0x5d560
+  __TEXT.__auth_stubs: 0x9d0
+  __TEXT.__objc_stubs: 0x7fe0
+  __TEXT.__objc_methlist: 0x3c74
   __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0xb24
-  __TEXT.__objc_methname: 0xbc38
-  __TEXT.__cstring: 0x14843
+  __TEXT.__gcc_except_tab: 0xae0
+  __TEXT.__objc_methname: 0xbebe
+  __TEXT.__cstring: 0x14e40
   __TEXT.__objc_classname: 0x5da
-  __TEXT.__objc_methtype: 0x1ddc
+  __TEXT.__objc_methtype: 0x1e52
   __TEXT.__oslogstring: 0x1a0
-  __TEXT.__unwind_info: 0x1258
-  __DATA_CONST.__auth_got: 0x510
-  __DATA_CONST.__got: 0x3f8
+  __TEXT.__unwind_info: 0x1470
+  __DATA_CONST.__auth_got: 0x4f8
+  __DATA_CONST.__got: 0x400
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1908
-  __DATA_CONST.__cfstring: 0x9080
+  __DATA_CONST.__const: 0x18f8
+  __DATA_CONST.__cfstring: 0x9380
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x120
-  __DATA_CONST.__objc_intobj: 0x3d8
-  __DATA_CONST.__objc_arraydata: 0x100
+  __DATA_CONST.__objc_intobj: 0x480
+  __DATA_CONST.__objc_arraydata: 0x150
   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x8a78
-  __DATA.__objc_selrefs: 0x2590
-  __DATA.__objc_ivar: 0x3e8
+  __DATA_CONST.__objc_arrayobj: 0x90
+  __DATA.__objc_const: 0x8ae8
+  __DATA.__objc_selrefs: 0x25f0
+  __DATA.__objc_ivar: 0x3f0
   __DATA.__objc_data: 0xbe0
   __DATA.__data: 0x7c0
   __DATA.__bss: 0x148

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F8624F4C-9101-3A07-AA3B-120E63241AF2
-  Functions: 1588
-  Symbols:   302
-  CStrings:  4796
+  UUID: 930F9C98-6EB8-330F-8E55-C9338D639947
+  Functions: 1601
+  Symbols:   301
+  CStrings:  4872
 
Symbols:
+ _OBJC_CLASS_$_ACXFeatureFlags
+ _OBJC_CLASS_$_NSConstantArray
+ _objc_release_x2
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ "-[ACXRemoteAppList _onQueue_replayFromCurrentState]"
+ "-[ACXRemoteAppList _onQueue_transitionToSyncState:alwaysExpectingResync:]"
+ "-[ACXRemoteAppList _onQueue_validateRequest:alwaysExpectingResync:acceptingStates:]"
+ "-[ACXRemoteAppList _onQueue_validateResponse:alwaysExpectingResync:againstResponseSessionGUID:acceptingStates:remoteDeviceOSVersion:]"
+ "-[ACXRemoteAppList attemptReplayFromCurrentStateForError:]_block_invoke"
+ "-[ACXRemoteAppList reportAppEvents:forDBUUID:startingSequenceNumber:sessionGUID:remoteDeviceOSVersion:]_block_invoke"
+ "-[ACXRemoteAppList updateAppInfoWithRecords:currentRemoteDBUUID:sessionGUID:remoteDeviceOSVersion:]_block_invoke"
+ "-[ACXRemoteAppList updateBundleIDList:currentRemoteDBUUID:lastSequenceNumber:sessionGUID:remoteDeviceOSVersion:]_block_invoke"
+ "26.4"
+ ">"
+ ">="
+ "Acknowledging app events for UUID %@ through sequence number %lu for session %@"
+ "Attempted to retry sync from invalid state %@"
+ "Attempting retry in 5 seconds from current state %@ due to failure: %@"
+ "B36@0:8r*16B24@28"
+ "B52@0:8r*16B24@28@36@44"
+ "Complete"
+ "Expected received response %s to contain a non-nil session GUID coming from a device running %@ which is %s %@"
+ "Getting app events for session %@"
+ "Getting app info for %lu bundle IDs in session %@"
+ "Getting bundle ID list for session %@"
+ "Got %lu app events for DBUUID %@ starting with sequence number %lu for session %@"
+ "Got %lu app info records for session %@"
+ "Got %lu bundle IDs for UUID %@ last sequence %lu for session %@; fetching app records"
+ "Invalid response %s for current state %@"
+ "Invalid state transition attempted from %@ to %@"
+ "Invalid transition from current state (%@) to new state (%@)"
+ "Jan 26 2026"
+ "Received invalid request %s outside of a resync session"
+ "Received invalid response %s outside of a resync session"
+ "ReceivedAppRecords"
+ "ReceivedBundleIDList"
+ "ReceivedOutstandingEvents"
+ "Rejecting invalid attempt to set state %@ outside of a resync session"
+ "Rejecting invalid request %s from state %@"
+ "Rejecting replay request; max retry attempts exceeded"
+ "RequestedAppRecords"
+ "RequestedBundleIDList"
+ "RequestedOutstandingAppRecords"
+ "RequestedOutstandingEvents"
+ "Requesting all remote bundle IDs to resync for session %@"
+ "Requesting apps for bundle IDs %@ in session %@"
+ "Requesting outstanding app events for session %@"
+ "SG"
+ "T@\"NSUUID\",&,N,V_sessionGUID"
+ "TQ,N,V_replayCount"
+ "TQ,R,N,V_state"
+ "Unexpectedly found existing session GUID %@ in the messageDict %@"
+ "Unexpectedly received a response %s for a message that was sent from another session %@ which does not match the current session %@"
+ "Unknown state: %lu"
+ "_FetchBundleIDList_block_invoke"
+ "_FetchOutstandingAppEvents_block_invoke"
+ "_IncludeSessionGUIDInMessage"
+ "_ValidateSyncStateTransition"
+ "_onQueue_finishResync"
+ "_onQueue_replayFromCurrentState"
+ "_onQueue_reportTotalSyncFailure"
+ "_onQueue_transitionToSyncState:alwaysExpectingResync:"
+ "_onQueue_validateRequest:alwaysExpectingResync:acceptingStates:"
+ "_onQueue_validateResponse:alwaysExpectingResync:againstResponseSessionGUID:acceptingStates:remoteDeviceOSVersion:"
+ "_replayCount"
+ "_sessionGUID"
+ "_state"
+ "acknowledgeAppEventsForDBUUID:throughSequenceNumber:sessionGUID:"
+ "attemptReplayFromCurrentStateForError:"
+ "com.apple.appconduitd.replay"
+ "fetchAppInfoForBundleIDs:sessionGUID:"
+ "fetchBundleIDListForSessionGUID:"
+ "fetchOutstandingAppEventsForSessionGUID:"
+ "isPerformingResync"
+ "replayCount"
+ "reportAppEvents:forDBUUID:startingSequenceNumber:sessionGUID:remoteDeviceOSVersion:"
+ "resyncSessionGUIDEnforcementEnabled"
+ "sessionGUID"
+ "setReplayCount:"
+ "setSessionGUID:"
+ "state"
+ "updateAppInfoWithRecords:currentRemoteDBUUID:sessionGUID:remoteDeviceOSVersion:"
+ "updateBundleIDList:currentRemoteDBUUID:lastSequenceNumber:sessionGUID:remoteDeviceOSVersion:"
+ "v28@0:8Q16B24"
+ "v32@0:8@\"NSSet\"16@\"NSUUID\"24"
+ "v40@0:8@\"NSUUID\"16Q24@\"NSUUID\"32"
+ "v40@0:8@16Q24@32"
+ "v56@0:8@16@24Q32@40@48"
+ "\xa1"
- "-[ACXRemoteAppList reportAppEvents:forDBUUID:startingSequenceNumber:]_block_invoke"
- "-[ACXRemoteAppList updateAppInfoWithRecords:currentRemoteDBUUID:]_block_invoke"
- "-[ACXRemoteAppList updateBundleIDList:currentRemoteDBUUID:lastSequenceNumber:]_block_invoke"
- "Acknowledging app events for UUID %@ through sequence number %lu"
- "App event fetch message was not successfully sent after 10 tries."
- "App info fetch message was not successfully sent after 10 tries."
- "Bundle ID fetch message was not successfully sent after 10 tries."
- "Got %lu bundle IDs for UUID %@ last sequence %lu; fetching app records"
- "Jan 16 2026"
- "Requesting all remote bundle IDs to resync"
- "Requesting apps for bundle IDs: %@"
- "Requesting outstanding app events"
- "Retrying app info fetch in 5 seconds..."
- "Retrying bundle ID fetch in 5 seconds..."
- "TB,N,V_performingResync"
- "_FetchBundleIDListWithRetryCount_block_invoke"
- "_FetchOutstandingAppEventsWithRetryCount_block_invoke"
- "_performingResync"
- "acknowledgeAppEventsForDBUUID:throughSequenceNumber:"
- "com.apple.appconduitd.FetchBundleIDListRetry"
- "com.apple.appconduitd.FetchInfoForBundleIDsRetry"
- "com.apple.appconduitd.FetchOutstandingAppEventsRetry"
- "fetchAppInfoForBundleIDs:"
- "fetchBundleIDList"
- "fetchOutstandingAppEvents"
- "performingResync"
- "reportAppEvents:forDBUUID:startingSequenceNumber:"
- "setPerformingResync:"
- "updateAppInfoWithRecords:currentRemoteDBUUID:"
- "updateBundleIDList:currentRemoteDBUUID:lastSequenceNumber:"
- "v24@0:8@\"NSSet\"16"
- "v32@0:8@\"NSUUID\"16Q24"

```
