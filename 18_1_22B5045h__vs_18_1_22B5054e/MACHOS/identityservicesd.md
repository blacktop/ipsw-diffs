## identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

-1925.200.52.0.0
-  __TEXT.__text: 0x7104a4
+1925.200.71.0.0
+  __TEXT.__text: 0x71692c
   __TEXT.__auth_stubs: 0x54d0
-  __TEXT.__objc_stubs: 0x44680
-  __TEXT.__objc_methlist: 0x23e34
+  __TEXT.__objc_stubs: 0x44660
+  __TEXT.__objc_methlist: 0x23e5c
   __TEXT.__const: 0x42450
-  __TEXT.__gcc_except_tab: 0x29410
-  __TEXT.__objc_methname: 0x6f6d1
-  __TEXT.__cstring: 0x55ddf
-  __TEXT.__oslogstring: 0x7aa2b
+  __TEXT.__gcc_except_tab: 0x294dc
+  __TEXT.__objc_methname: 0x6f825
+  __TEXT.__cstring: 0x55e5f
+  __TEXT.__oslogstring: 0x7ab1b
   __TEXT.__objc_classname: 0x4308
-  __TEXT.__objc_methtype: 0x11813
+  __TEXT.__objc_methtype: 0x1181c
   __TEXT.__ustring: 0x4ca
   __TEXT.__dlopen_cstrs: 0xea
-  __TEXT.__swift5_typeref: 0x36ee
-  __TEXT.__swift5_capture: 0x70c
-  __TEXT.__constg_swiftt: 0x2ca8
-  __TEXT.__swift5_reflstr: 0x1eed
-  __TEXT.__swift5_fieldmd: 0x2104
+  __TEXT.__swift5_typeref: 0x3882
+  __TEXT.__swift5_capture: 0xdd8
+  __TEXT.__constg_swiftt: 0x2ca0
+  __TEXT.__swift5_reflstr: 0x1f2d
+  __TEXT.__swift5_fieldmd: 0x210c
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_proto: 0x360
   __TEXT.__swift5_types: 0x228
   __TEXT.__swift5_assocty: 0x1f8
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xf728
-  __TEXT.__eh_frame: 0x4bd4
+  __TEXT.__unwind_info: 0xf850
+  __TEXT.__eh_frame: 0x4b64
   __DATA_CONST.__auth_got: 0x2a78
   __DATA_CONST.__got: 0x3318
-  __DATA_CONST.__auth_ptr: 0x618
-  __DATA_CONST.__const: 0x1b798
-  __DATA_CONST.__cfstring: 0x33640
+  __DATA_CONST.__auth_ptr: 0x6b0
+  __DATA_CONST.__const: 0x1c658
+  __DATA_CONST.__cfstring: 0x33680
   __DATA_CONST.__objc_classlist: 0xe78
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x768
+  __DATA_CONST.__objc_protolist: 0x760
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x120
+  __DATA_CONST.__objc_protorefs: 0x118
   __DATA_CONST.__objc_superrefs: 0xb40
   __DATA_CONST.__objc_intobj: 0x1968
-  __DATA_CONST.__objc_arraydata: 0x5e0
+  __DATA_CONST.__objc_arraydata: 0x5e8
   __DATA_CONST.__objc_arrayobj: 0x348
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x48690
-  __DATA.__objc_selrefs: 0x14690
-  __DATA.__objc_ivar: 0x3114
-  __DATA.__objc_data: 0xb510
-  __DATA.__data: 0x9f78
+  __DATA.__objc_const: 0x48640
+  __DATA.__objc_selrefs: 0x14698
+  __DATA.__objc_ivar: 0x3118
+  __DATA.__objc_data: 0xb4a0
+  __DATA.__data: 0x9fe8
   __DATA.__bss: 0x8f40
   __DATA.__common: 0x518
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 20033
+  Functions: 20229
   Symbols:   2617
-  CStrings:  33836
+  CStrings:  33842
 
CStrings:
+ "Called to perform DB cleanup tasks"
+ "deleteEndpointsWithServices:fromURI:toURI:completion:"
+ "Metrics: Reporting %!@(MISSING) with %!@(MISSING)"
+ "v52@0:8@16@24q32B40@?44"
+ "cleanupShortHandlesWithExpireDuration:completion:"
+ "deleteAllSenderKeysWithCompletion:"
+ "initWithPreviousMode:currentMode:previousPublishStatus:currentPublishStatus:previousStewieConnectionState:currentStewieConnectionState:previousNetworkConnectionState:currentNetworkConnectionState:duration:"
+ "Failed to mark keyIDs: %!s(MISSING) as didSend for senderURI: %!@(MISSING) receiverURI: %!@(MISSING) error: %!@(MISSING)"
+ "Failed to markLastActivePeerToken for token: %!@(MISSING) remoteURI: %!@(MISSING) localURI: %!@(MISSING) error: %!@(MISSING)"
+ "Got called to checkpoint Query DB cleanup run state with non null activity %!@(MISSING)"
+ "performDBCleanupTasks"
+ "ids-db-cleanup-interval-seconds"
+ "deleteEndpointsWithService:fromURI:toURI:completion:"
+ "Error cleaning up expired sessions: %!@(MISSING)"
+ "ids-short-handle-expire-duration-seconds"
+ "v32@0:8d16@?24"
+ "v72@0:8q16q24q32q40B48B52B56B60d64"
+ "Error cleaning up orphaned IDSQuerySDDevices: %!@(MISSING)"
+ "dbCleanupTimeInterval"
+ "deleteEndpointsWithService:completion:"
+ "deleteAllWithCompletion:"
+ "deleteEndpointsWithServices:toURIs:completion:"
+ "IDSSessionEndedReasonAllocbindErrorResponse"
+ "_setAndPersistOffGridMode:publishStatus:"
+ "cleanupExpiredSessionsIfNeededWithCompletion:"
+ "Told to Check In for Query DB cleanup with activity %!@(MISSING) "
+ "deletePublicIdentitiesBeforeDate:afterDate:completion:"
+ "_reportOffGridModeMetricWithPreviousMode:currentMode:previousPublishStatus:currentPublishStatus:previousStewieConnectionStatus:currentStewieConnectionStatus:previousNetworkConnectionStatus:currentNetworkConnectionStatus:duration:"
+ "16:09:05"
+ "Sep 17 2024"
+ "Failed to save registration event for bagKey: %!s(MISSING) completionTime: %!s(MISSING) error: %!@(MISSING)"
+ "Container not available."
+ "Failed to mark keyIDs %!s(MISSING) as certified delivered for receiverPushToken %!@(MISSING) error: %!@(MISSING)"
+ "Registering for Query DB cleanup"
+ "Failed to reset state for %!s(MISSING) for senderURI: %!@(MISSING) receiverURI: %!@(MISSING) error: %!@(MISSING)"
+ "com.apple.ids.query.db.cleanup"
+ "_initializeOffGridModeAndPublishStatusFromDisk"
+ "Failed to delete public identities with startDate: %!@(MISSING) endDate: %!@(MISSING) {deleteError: %!@(MISSING)}"
+ "processDonatedHandlesForMessagingKeysWithUris:fromURI:priority:isInitialDonation:completion:"
+ "cleanupInvalidSenderKeyEntriesWithCompletion:"
+ "registerForQueryDBCleanup"
- "Error updating IDSQuerySDSenderKeyDistribution instance: %!@(MISSING)"
- "B44@0:8@16@24q32B40"
- "Failed to clear all sender keys: %!@(MISSING)"
- "_setAndPersistPublishStatus:"
- "cleanupInvalidSenderKeyEntries"
- "v56@0:8q16q24B32B36@40@48"
- "cleanupExpiredSessionsIfNeeded"
- "_initializePublishStatusFromDisk"
- "latest-stewie-connection-state"
- "_reportOffGridModeMetricWithCurrentMode:previousMode:currentStewieConnectionStatus:previousStewieConnectionStatus:currentStartDate:previousStartDate:"
- "deletePublicIdentitiesBeforeDate:afterDate:error:"
- "_TtP17identityservicesd28SDPersistenceManagerProtocol_"
- "initWithPreviousMode:currentMode:previouslyConnected:currentlyConnected:duration:"
- "B48@0:8@\"NSString\"16@\"IDSURI\"24@\"IDSURI\"32^@40"
- "Successfully deleted peer and personal entries from DB"
- "deleteEndpointsWithService:error:"
- "cleanupShortHandlesWithExpireDuration:"
- "Error cleanup expired sessions: %!@(MISSING)"
- "B48@0:8@16@24@32^@40"
- "Failed to reset state for %!s(MISSING) for senderURI: %!@(MISSING) receiverURI: %!@(MISSING)"
- "B40@0:8@\"NSDate\"16@\"NSDate\"24^@32"
- "Failed to mark keyID(s) as didSend for senderURI: %!@(MISSING) receiverURI: %!@(MISSING)"
- "clearAllSenderKeys"
- "deleteEndpointsWithService:fromURI:toURI:error:"
- "latest-publish-status-date"
- "_initializeOffGridModeFromDisk"
- "Failed to mark keyIDs %!s(MISSING) as delivered for pushToken %!@(MISSING)"
- "Error fetching addressables matching condition: %!@(MISSING)"
- "18:33:44"
- "deleteEndpointsWithServices:fromURI:toURI:error:"
- "deleteEndpointsWithServices:toURIs:error:"
- "B32@0:8@\"NSString\"16^@24"
- "Failed to save registration event for bagKey: %!s(MISSING) completionTime: %!s(MISSING)"
- "deleteAllWithError:"
- "Failed to markLastActivePeerToken for token: %!@(MISSING) remoteURI: %!@(MISSING) localURI: %!@(MISSING)"
- "processDonatedHandlesForMessagingKeysWithUris:fromURI:priority:isInitialDonation:"
- "_setAndPersistOffGridMode:"
- "Sep 12 2024"

```
