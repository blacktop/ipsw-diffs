## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/Versions/A/TelephonyUtilities`

```diff

-1616.100.2.0.0
-  __TEXT.__text: 0x1a10e0
-  __TEXT.__objc_methlist: 0x1b2d0
-  __TEXT.__cstring: 0x121c6
+1620.100.1.1.22
+  __TEXT.__text: 0x1a1c68
+  __TEXT.__objc_methlist: 0x1b428
+  __TEXT.__cstring: 0x121e6
   __TEXT.__const: 0x40c8
-  __TEXT.__oslogstring: 0x128d7
-  __TEXT.__gcc_except_tab: 0x1364
+  __TEXT.__oslogstring: 0x12c67
+  __TEXT.__gcc_except_tab: 0x13a8
   __TEXT.__ustring: 0xde
   __TEXT.__dlopen_cstrs: 0x49b
   __TEXT.__constg_swiftt: 0xcc0

   __TEXT.__swift_as_cont: 0x13c
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x6578
+  __TEXT.__unwind_info: 0x65c8
   __TEXT.__eh_frame: 0x2078
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x18f0
   __DATA_CONST.__objc_classlist: 0x888
-  __DATA_CONST.__objc_catlist: 0xb8
-  __DATA_CONST.__objc_protolist: 0x418
+  __DATA_CONST.__objc_catlist: 0xc0
+  __DATA_CONST.__objc_protolist: 0x420
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb3d0
+  __DATA_CONST.__objc_selrefs: 0xb480
   __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x6f0
   __DATA_CONST.__objc_arraydata: 0x9e8
   __DATA_CONST.__got: 0xf88
   __AUTH_CONST.__const: 0x5f80
-  __AUTH_CONST.__cfstring: 0x121a0
-  __AUTH_CONST.__objc_const: 0x2a9a8
+  __AUTH_CONST.__cfstring: 0x121c0
+  __AUTH_CONST.__objc_const: 0x2abe0
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x2b8
-  __AUTH_CONST.__auth_got: 0x1200
+  __AUTH_CONST.__auth_got: 0x1208
   __AUTH.__objc_data: 0x2630
   __AUTH.__data: 0xb30
-  __DATA.__objc_ivar: 0x18d0
-  __DATA.__data: 0x3c48
+  __DATA.__objc_ivar: 0x18e8
+  __DATA.__data: 0x3ca8
   __DATA.__bss: 0x6b30
   __DATA.__common: 0x88
   __DATA_DIRTY.__objc_data: 0x3078

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11239
-  Symbols:   20130
-  CStrings:  4335
+  Functions: 11265
+  Symbols:   20193
+  CStrings:  4344
 
Symbols:
+ +[TUCallCapabilities canEnableThumperCalling]
+ +[TUCallHistoryController callHistoryControllerWithCoalescingStrategy:options:shouldUpdateMetadataCache:recentsDataSource:]
+ -[TUCallCenter isGreenTea]
+ -[TUCallCenter registerClientSupportsExtendedSuspensionState:]
+ -[TUCallHistoryController initWithCoalescingStrategy:options:dataSource:recentsDataSource:shouldUpdateMetadataCache:]
+ -[TUCallHistoryController isPerformingRecentCallsRefresh]
+ -[TUCallHistoryController performRecentCallsRefresh]
+ -[TUCallHistoryController recentCallsRefreshRequestedDuringFetch]
+ -[TUCallHistoryController recentsDataSource]
+ -[TUCallHistoryController requestRecentCallsRefresh]
+ -[TUCallHistoryController setIsPerformingRecentCallsRefresh:]
+ -[TUCallHistoryController setRecentCallsRefreshRequestedDuringFetch:]
+ -[TUCallHistoryController setRecentsDataSource:]
+ -[TUCallServicesInterface _shouldTearDownXPCConnectionForConnectionRequestWithNotifyStatus:daemonLaunchTime:]
+ -[TUCallServicesInterface clientSupportsExtendedSuspensionState]
+ -[TUCallServicesInterface lastOutgoingXPCMessageTime]
+ -[TUCallServicesInterface pickRouteWithUniqueIdentifier:shouldWaitUntilAvailable:routeSelectionProvenance:forRouteController:]
+ -[TUCallServicesInterface setClientSupportsExtendedSuspensionState:]
+ -[TUCallServicesInterface setLastOutgoingXPCMessageTime:]
+ -[TUCallServicesInterface stampLastOutgoingXPCMessageTime]
+ -[TURouteController pickRoute:routeSelectionProvenance:]
+ -[TURouteController pickRouteWhenAvailableWithUniqueIdentifier:routeSelectionProvenance:]
+ -[TURouteController pickRouteWithUniqueIdentifier:routeSelectionProvenance:]
+ -[TUSenderIdentityCapabilities canEnableThumperCalling]
+ -[TUThumperCTCapabilitiesState eligibleToEnable]
+ -[TUThumperCTCapabilitiesState setEligibleToEnable:]
+ GCC_except_table168
+ GCC_except_table199
+ GCC_except_table229
+ GCC_except_table255
+ GCC_except_table262
+ GCC_except_table63
+ GCC_except_table75
+ GCC_except_table78
+ GCC_except_table84
+ GCC_except_table86
+ OBJC_IVAR_$_TUCallHistoryController._isPerformingRecentCallsRefresh
+ OBJC_IVAR_$_TUCallHistoryController._recentCallsRefreshRequestedDuringFetch
+ OBJC_IVAR_$_TUCallHistoryController._recentsDataSource
+ OBJC_IVAR_$_TUCallServicesInterface._clientSupportsExtendedSuspensionState
+ OBJC_IVAR_$_TUCallServicesInterface._lastOutgoingXPCMessageTime
+ OBJC_IVAR_$_TUThumperCTCapabilitiesState._eligibleToEnable
+ _OBJC_CLASS_$_CHManager
+ __OBJC_$_CATEGORY_CHManager_$_TUCallHistoryControllerRecentsDataSourceConformance
+ __OBJC_$_PROP_LIST_CHManager_$_TUCallHistoryControllerRecentsDataSourceConformance
+ __OBJC_$_PROP_LIST_TUCallHistoryControllerRecentsDataSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TUCallHistoryControllerRecentsDataSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TUCallHistoryControllerRecentsDataSource
+ __OBJC_$_PROTOCOL_REFS_TUCallHistoryControllerRecentsDataSource
+ __OBJC_CATEGORY_PROTOCOLS_$_CHManager_$_TUCallHistoryControllerRecentsDataSourceConformance
+ __OBJC_LABEL_PROTOCOL_$_TUCallHistoryControllerRecentsDataSource
+ __OBJC_PROTOCOL_$_TUCallHistoryControllerRecentsDataSource
+ ___45+[TUCallCapabilities canEnableThumperCalling]_block_invoke
+ ___52-[TUCallHistoryController requestRecentCallsRefresh]_block_invoke
+ ___62-[TUCallCenter registerClientSupportsExtendedSuspensionState:]_block_invoke
+ _clock_gettime_nsec_np
+ _objc_msgSend$_shouldTearDownXPCConnectionForConnectionRequestWithNotifyStatus:daemonLaunchTime:
+ _objc_msgSend$callHistoryControllerWithCoalescingStrategy:options:shouldUpdateMetadataCache:recentsDataSource:
+ _objc_msgSend$canEnableThumperCalling
+ _objc_msgSend$clientSupportsExtendedSuspensionState
+ _objc_msgSend$eligibleToEnable
+ _objc_msgSend$initWithCoalescingStrategy:options:dataSource:recentsDataSource:shouldUpdateMetadataCache:
+ _objc_msgSend$isPerformingRecentCallsRefresh
+ _objc_msgSend$lastOutgoingXPCMessageTime
+ _objc_msgSend$performRecentCallsRefresh
+ _objc_msgSend$pickLocalRouteWithUniqueIdentifier:shouldWaitUntilAvailable:routeSelectionProvenance:
+ _objc_msgSend$pickPairedHostDeviceRouteWithUniqueIdentifier:shouldWaitUntilAvailable:routeSelectionProvenance:
+ _objc_msgSend$pickRoute:routeSelectionProvenance:
+ _objc_msgSend$pickRouteWhenAvailableWithUniqueIdentifier:routeSelectionProvenance:
+ _objc_msgSend$pickRouteWithUniqueIdentifier:routeSelectionProvenance:
+ _objc_msgSend$pickRouteWithUniqueIdentifier:shouldWaitUntilAvailable:routeSelectionProvenance:forRouteController:
+ _objc_msgSend$recentCallsRefreshRequestedDuringFetch
+ _objc_msgSend$recentsDataSource
+ _objc_msgSend$requestRecentCallsRefresh
+ _objc_msgSend$setClientSupportsExtendedSuspensionState:
+ _objc_msgSend$setIsPerformingRecentCallsRefresh:
+ _objc_msgSend$setRecentCallsRefreshRequestedDuringFetch:
+ _objc_msgSend$setRecentsDataSource:
+ _objc_msgSend$stampLastOutgoingXPCMessageTime
- -[TUCallHistoryController initWithCoalescingStrategy:options:dataSource:shouldUpdateMetadataCache:]
- -[TUCallServicesInterface pickRouteWithUniqueIdentifier:shouldWaitUntilAvailable:forRouteController:]
- GCC_except_table165
- GCC_except_table175
- GCC_except_table227
- GCC_except_table252
- GCC_except_table259
- GCC_except_table62
- GCC_except_table71
- GCC_except_table77
- GCC_except_table80
- _objc_msgSend$initWithCoalescingStrategy:options:dataSource:shouldUpdateMetadataCache:
- _objc_msgSend$pickLocalRouteWithUniqueIdentifier:shouldWaitUntilAvailable:
- _objc_msgSend$pickPairedHostDeviceRouteWithUniqueIdentifier:shouldWaitUntilAvailable:
- _objc_msgSend$pickRouteWithUniqueIdentifier:
- _objc_msgSend$pickRouteWithUniqueIdentifier:shouldWaitUntilAvailable:forRouteController:
CStrings:
+ "Asked to pick route with unique identifier: %@ (routeSelectionProvenance: %ld)"
+ "Asked to pick route: %@ (routeSelectionProvenance: %ld)"
+ "Client doesn't support extended suspension state - we should tear down the XPC connection"
+ "Daemon launch time (%llu nanoseconds since uptime) is at or after last outgoing message to server (%llu nanoseconds since uptime). We should tear down the XPC connection."
+ "Daemon launch time (%llu nanoseconds since uptime) precedes last outgoing message to server (%llu nanoseconds since uptime). We should not tear down the XPC connection"
+ "Proxying pickLocalRouteWithUniqueIdentifier for %@ shouldWaitUntilAvailable: %d routeSelectionProvenance: %ld"
+ "Proxying pickPairedHostDeviceRouteWithUniqueIdentifier for %@ shouldWaitUntilAvailable: %d routeSelectionProvenance: %ld"
+ "Recent calls refresh requested while a refresh is already in progress; queueing another refresh"
+ "Starting recent calls refresh"
+ "TUCallCenter registerClientSupportsExtendedSuspensionState: %@"
+ "Thumper capabilities changed from (supported=%d overCellularData=%d enabled=%d provisioningStatus=%d, associated=%d, supportsDefaultPairedDevice=%d canEnable=%d) to (supported=%d overCellularData=%d enabled=%d provisioningStatus=%d, associated=%d, supportsDefaultPairedDevice=%d canEnable=%d)"
+ "Updating clientSupportsExtendedSuspensionState to %d"
+ "[WARN] Bad status (%u) reading daemon launch time; we should tear down the XPC connection"
+ "call_waiting_tone_low_priority"
- "Asked to pick route with unique identifier: %@"
- "Asked to pick route: %@"
- "Proxying pickLocalRouteWithUniqueIdentifier for %@ shouldWaitUntilAvailable: %d"
- "Proxying pickPairedHostDeviceRouteWithUniqueIdentifier for %@ shouldWaitUntilAvailable: %d"
- "Thumper capabilities changed from (supported=%d overCellularData=%d enabled=%d provisioningStatus=%d, associated=%d, supportsDefaultPairedDevice=%d) to (supported=%d overCellularData=%d enabled=%d provisioningStatus=%d, associated=%d, supportsDefaultPairedDevice=%d)"
```
