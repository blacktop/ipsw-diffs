## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1616.100.2.2.1
-  __TEXT.__text: 0x19b298
-  __TEXT.__objc_methlist: 0x1b300
+1620.100.1.2.3
+  __TEXT.__text: 0x19bd3c
+  __TEXT.__objc_methlist: 0x1b458
   __TEXT.__cstring: 0x13f76
   __TEXT.__const: 0x40c8
-  __TEXT.__oslogstring: 0x13897
-  __TEXT.__gcc_except_tab: 0x1788
+  __TEXT.__oslogstring: 0x13c27
+  __TEXT.__gcc_except_tab: 0x17c8
   __TEXT.__ustring: 0xde
   __TEXT.__dlopen_cstrs: 0x845
   __TEXT.__constg_swiftt: 0xcc0

   __TEXT.__swift_as_cont: 0x13c
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x6c80
+  __TEXT.__unwind_info: 0x6cc8
   __TEXT.__eh_frame: 0x2078
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x37b0
   __DATA_CONST.__objc_classlist: 0x878
-  __DATA_CONST.__objc_catlist: 0xb8
-  __DATA_CONST.__objc_protolist: 0x408
+  __DATA_CONST.__objc_catlist: 0xc0
+  __DATA_CONST.__objc_protolist: 0x410
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb5e0
+  __DATA_CONST.__objc_selrefs: 0xb690
   __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x6d8
   __DATA_CONST.__objc_arraydata: 0x9e8
   __DATA_CONST.__got: 0xff0
   __AUTH_CONST.__const: 0x46f8
   __AUTH_CONST.__cfstring: 0x124c0
-  __AUTH_CONST.__objc_const: 0x2aa48
-  __AUTH_CONST.__objc_intobj: 0x540
+  __AUTH_CONST.__objc_const: 0x2ac80
+  __AUTH_CONST.__objc_intobj: 0x558
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x2b8
-  __AUTH_CONST.__auth_got: 0x1500
+  __AUTH_CONST.__auth_got: 0x1508
   __AUTH.__objc_data: 0x2f38
   __AUTH.__data: 0xc30
-  __DATA.__objc_ivar: 0x18dc
-  __DATA.__data: 0x3c38
+  __DATA.__objc_ivar: 0x18f4
+  __DATA.__data: 0x3c98
   __DATA.__bss: 0x7610
   __DATA.__common: 0x88
   __DATA_DIRTY.__objc_data: 0x26f0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11471
-  Symbols:   20287
-  CStrings:  4563
+  Functions: 11497
+  Symbols:   20350
+  CStrings:  4571
 
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
+ GCC_except_table152
+ GCC_except_table183
+ GCC_except_table217
+ GCC_except_table240
+ GCC_except_table245
+ GCC_except_table49
+ GCC_except_table60
+ GCC_except_table63
+ GCC_except_table72
+ _OBJC_CLASS_$_CHManager
+ _OBJC_IVAR_$_TUCallHistoryController._isPerformingRecentCallsRefresh
+ _OBJC_IVAR_$_TUCallHistoryController._recentCallsRefreshRequestedDuringFetch
+ _OBJC_IVAR_$_TUCallHistoryController._recentsDataSource
+ _OBJC_IVAR_$_TUCallServicesInterface._clientSupportsExtendedSuspensionState
+ _OBJC_IVAR_$_TUCallServicesInterface._lastOutgoingXPCMessageTime
+ _OBJC_IVAR_$_TUThumperCTCapabilitiesState._eligibleToEnable
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
- GCC_except_table149
- GCC_except_table159
- GCC_except_table215
- GCC_except_table237
- GCC_except_table242
- GCC_except_table41
- GCC_except_table65
- GCC_except_table70
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
- "Asked to pick route with unique identifier: %@"
- "Asked to pick route: %@"
- "Proxying pickLocalRouteWithUniqueIdentifier for %@ shouldWaitUntilAvailable: %d"
- "Proxying pickPairedHostDeviceRouteWithUniqueIdentifier for %@ shouldWaitUntilAvailable: %d"
- "Thumper capabilities changed from (supported=%d overCellularData=%d enabled=%d provisioningStatus=%d, associated=%d, supportsDefaultPairedDevice=%d) to (supported=%d overCellularData=%d enabled=%d provisioningStatus=%d, associated=%d, supportsDefaultPairedDevice=%d)"
```
