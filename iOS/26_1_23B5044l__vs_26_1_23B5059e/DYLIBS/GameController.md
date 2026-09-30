## GameController

> `/System/Library/Frameworks/GameController.framework/GameController`

```diff

-13.1.4.0.0
-  __TEXT.__text: 0x107648
+13.1.7.0.0
+  __TEXT.__text: 0x10567c
   __TEXT.__auth_stubs: 0x1c30
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xfe34
+  __TEXT.__objc_methlist: 0xfd8c
   __TEXT.__const: 0x3c74
-  __TEXT.__cstring: 0xa109
-  __TEXT.__gcc_except_tab: 0x5a40
-  __TEXT.__oslogstring: 0x9c78
+  __TEXT.__cstring: 0xa179
+  __TEXT.__gcc_except_tab: 0x58f8
+  __TEXT.__oslogstring: 0x97d8
   __TEXT.__dlopen_cstrs: 0xfd
   __TEXT.__swift5_typeref: 0x574
   __TEXT.__swift5_reflstr: 0x22f

   __TEXT.__swift5_types: 0x60
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_capture: 0xc4
-  __TEXT.__unwind_info: 0x5448
+  __TEXT.__unwind_info: 0x5370
   __TEXT.__eh_frame: 0xf8
-  __TEXT.__objc_classname: 0x41a8
-  __TEXT.__objc_methname: 0x190de
-  __TEXT.__objc_methtype: 0x7b31
-  __TEXT.__objc_stubs: 0xf420
-  __DATA_CONST.__got: 0xba0
-  __DATA_CONST.__const: 0x2e08
+  __TEXT.__objc_classname: 0x41ad
+  __TEXT.__objc_methname: 0x18f87
+  __TEXT.__objc_methtype: 0x7bcc
+  __TEXT.__objc_stubs: 0xf3c0
+  __DATA_CONST.__got: 0xba8
+  __DATA_CONST.__const: 0x2d68
   __DATA_CONST.__objc_classlist: 0x990
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x7e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x52f0
+  __DATA_CONST.__objc_selrefs: 0x52c0
   __DATA_CONST.__objc_protorefs: 0x4f0
   __DATA_CONST.__objc_superrefs: 0x8c8
   __DATA_CONST.__objc_arraydata: 0x570
   __AUTH_CONST.__auth_got: 0xe30
   __AUTH_CONST.__const: 0x1f78
-  __AUTH_CONST.__cfstring: 0xb420
-  __AUTH_CONST.__objc_const: 0x48f28
+  __AUTH_CONST.__cfstring: 0xb4c0
+  __AUTH_CONST.__objc_const: 0x48ed8
   __AUTH_CONST.__objc_intobj: 0x14a0
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x4fc0
+  __AUTH.__objc_data: 0x5010
   __AUTH.__data: 0xe0
-  __DATA.__objc_ivar: 0x17ac
+  __DATA.__objc_ivar: 0x17a4
   __DATA.__data: 0x5e10
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x1f20
+  __DATA.__bss: 0x1f10
   __DATA.__common: 0x78
-  __DATA_DIRTY.__objc_data: 0x1180
+  __DATA_DIRTY.__objc_data: 0x1130
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x220
+  __DATA_DIRTY.__bss: 0x228
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: CF51D4C8-D8AC-3FB5-B8A5-139EF0EE3CA9
-  Functions: 7410
-  Symbols:   27474
-  CStrings:  9788
+  UUID: D903152C-46F7-3859-82D6-18E50E0F394F
+  Functions: 7371
+  Symbols:   27364
+  CStrings:  9775
 
Symbols:
+ +[_GCHIDEventDeliveryMonitor sharedInstance]
+ +[_GCHIDEventDeliveryMonitor sharedInstance].cold.1
+ -[_GCDefaultLogicalDevice updateAdaptiveTriggersForActiveClient]
+ -[_GCDefaultLogicalDevice updateAdaptiveTriggersForActiveClient].cold.1
+ -[_GCDefaultLogicalDevice updateAnalyticsForActiveClient]
+ -[_GCHIDEventDeliveryMonitor .cxx_destruct]
+ -[_GCHIDEventDeliveryMonitor dealloc]
+ -[_GCHIDEventDeliveryMonitor deferringTarget]
+ -[_GCHIDEventDeliveryMonitor init]
+ -[_GCHIDEventDeliveryMonitor observer:deliveryChainDidUpdate:]
+ -[_GCRacingWheelManager activateWithSession:environment:]
+ -[_GCRacingWheelManager invalidateWithSession:environment:]
+ _CFSetRemoveAllValues
+ _OBJC_CLASS_$_BKSHIDEventDeliveryChainObserver
+ _OBJC_CLASS_$_BKSHIDEventDisplay
+ _OBJC_CLASS_$_GCIONotificationPort
+ _OBJC_CLASS_$__GCHIDEventDeliveryMonitor
+ _OBJC_IVAR_$__GCDefaultLogicalDevice._activeAnalyticsPID
+ _OBJC_IVAR_$__GCHIDEventDeliveryMonitor._deferringTarget
+ _OBJC_IVAR_$__GCHIDEventDeliveryMonitor._deliveryChain
+ _OBJC_IVAR_$__GCHIDEventDeliveryMonitor._deliveryChainObserver
+ _OBJC_IVAR_$__GCHIDEventDeliveryMonitor._state
+ _OBJC_METACLASS_$__GCHIDEventDeliveryMonitor
+ __OBJC_$_INSTANCE_METHODS__GCHIDEventDeliveryMonitor
+ __OBJC_$_INSTANCE_VARIABLES__GCHIDEventDeliveryMonitor
+ __OBJC_$_PROP_LIST__GCHIDEventDeliveryMonitor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKSHIDEventDeliveryChainObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKSHIDEventDeliveryChainObserving
+ __OBJC_$_PROTOCOL_REFS_BKSHIDEventDeliveryChainObserving
+ __OBJC_CLASS_PROTOCOLS_$__GCHIDEventDeliveryMonitor
+ __OBJC_CLASS_RO_$__GCHIDEventDeliveryMonitor
+ __OBJC_LABEL_PROTOCOL_$_BKSHIDEventDeliveryChainObserving
+ __OBJC_METACLASS_RO_$__GCHIDEventDeliveryMonitor
+ __OBJC_PROTOCOL_$_BKSHIDEventDeliveryChainObserving
+ ___34-[_GCHIDEventDeliveryMonitor init]_block_invoke
+ ___40+[_GCLegacyDeviceSession sharedInstance]_block_invoke.100
+ ___40+[_GCLegacyDeviceSession sharedInstance]_block_invoke.100.cold.1
+ ___44+[_GCHIDEventDeliveryMonitor sharedInstance]_block_invoke
+ ___57-[_GCRacingWheelManager activateWithSession:environment:]_block_invoke
+ ___57-[_GCRacingWheelManager activateWithSession:environment:]_block_invoke.92
+ ___57-[_GCRacingWheelManager activateWithSession:environment:]_block_invoke_2
+ ___57-[_GCRacingWheelManager activateWithSession:environment:]_block_invoke_2.cold.1
+ ___59-[_GCRacingWheelManager invalidateWithSession:environment:]_block_invoke
+ ___59-[_GCRacingWheelManager invalidateWithSession:environment:]_block_invoke_2
+ ___59-[_GCRacingWheelManager invalidateWithSession:environment:]_block_invoke_2.cold.1
+ ___block_descriptor_40_e8_32s_e22_v16?0"NSDictionary"8ls32l8
+ ___block_literal_global.152
+ _objc_msgSend$addCancellationHandler:onQueue:
+ _objc_msgSend$addChainObserver:
+ _objc_msgSend$deferringPath
+ _objc_msgSend$deferringTarget
+ _objc_msgSend$futureWithLabel:block:
+ _objc_msgSend$initWithDisplay:environment:
+ _objc_msgSend$monitorControllerEventsInBackground
+ _objc_msgSend$nullDisplay
+ _objc_msgSend$pid
+ _objc_msgSend$port
+ _objc_msgSend$setMonitorControllerEventsInBackground:
+ _objc_msgSend$setQueue:
- +[GCApplicationStateMonitor sharedInstance]
- +[GCApplicationStateMonitor sharedInstance].cold.1
- -[GCApplicationStateMonitor .cxx_destruct]
- -[GCApplicationStateMonitor addObserver:forProcessIdentifier:]
- -[GCApplicationStateMonitor dealloc]
- -[GCApplicationStateMonitor frontmostApplicationIdentifier]
- -[GCApplicationStateMonitor frontmostApplication]
- -[GCApplicationStateMonitor init]
- -[GCApplicationStateMonitor initializeForegroundMonitor]
- -[GCApplicationStateMonitor initializeStateMonitor]
- -[GCApplicationStateMonitor onFrontmostApplicationChanged:]
- -[GCApplicationStateMonitor removeObserver:]
- -[GCApplicationStateMonitor removeObserver:forProcessIdentifier:]
- -[GCApplicationStateMonitor setFrontmostApplication:]
- -[GCApplicationStateMonitor setFrontmostApplication:].cold.1
- -[GCApplicationStateMonitor setFrontmostApplication:].cold.2
- -[GCApplicationStateMonitor setFrontmostApplication:].cold.3
- -[GCApplicationStateMonitor setFrontmostApplicationIdentifier:]
- -[GCApplicationStateMonitor updateInterestedBundleIDs]
- -[_GCDefaultLogicalDevice applicationBackgrounded:]
- -[_GCDefaultLogicalDevice applicationBackgrounded:].cold.1
- -[_GCDefaultLogicalDevice applicationForegrounded:]
- -[_GCDefaultLogicalDevice applicationForegrounded:].cold.1
- -[_GCDefaultLogicalDevice setActiveApplicationPID:].cold.1
- -[_GCDefaultLogicalDevice stopObservingClientStateChanges:]
- -[_GCDefaultLogicalDevice stopObservingClientStateChanges:].cold.1
- -[_GCDefaultLogicalDevice stopObservingClientStateChangesForAllClients]
- -[_GCRacingWheelManager initWithDeviceSessionConfiguration:queue:environment:].cold.1
- GCC_except_table80
- _BKSApplicationStateProcessIDKey
- _CFSetCreateCopy
- _DeviceMatched.cold.4
- _OBJC_CLASS_$_GCApplicationStateMonitor
- _OBJC_IVAR_$_GCApplicationStateMonitor._bksStateMonitor
- _OBJC_IVAR_$_GCApplicationStateMonitor._frontmostApplication
- _OBJC_IVAR_$_GCApplicationStateMonitor._frontmostApplicationIdentifier
- _OBJC_IVAR_$_GCApplicationStateMonitor._observerToPIDs
- _OBJC_IVAR_$_GCApplicationStateMonitor._pidToBundleIdentifier
- _OBJC_IVAR_$_GCApplicationStateMonitor._pidToObservers
- _OBJC_IVAR_$_GCApplicationStateMonitor._queue
- _OBJC_METACLASS_$_GCApplicationStateMonitor
- __OBJC_$_CLASS_METHODS_GCApplicationStateMonitor
- __OBJC_$_INSTANCE_METHODS_GCApplicationStateMonitor
- __OBJC_$_INSTANCE_VARIABLES_GCApplicationStateMonitor
- __OBJC_$_PROP_LIST_GCApplicationStateMonitor
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCApplicationStateObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_GCApplicationStateObserver
- __OBJC_$_PROTOCOL_REFS_GCApplicationStateObserver
- __OBJC_CLASS_PROTOCOLS_$_GCApplicationStateMonitor
- __OBJC_CLASS_RO_$_GCApplicationStateMonitor
- __OBJC_LABEL_PROTOCOL_$_GCApplicationStateObserver
- __OBJC_METACLASS_RO_$_GCApplicationStateMonitor
- __OBJC_PROTOCOL_$_GCApplicationStateObserver
- ___40+[_GCLegacyDeviceSession sharedInstance]_block_invoke.99
- ___40+[_GCLegacyDeviceSession sharedInstance]_block_invoke.99.cold.1
- ___43+[GCApplicationStateMonitor sharedInstance]_block_invoke
- ___43+[GCApplicationStateMonitor sharedInstance]_block_invoke.cold.1
- ___44-[GCApplicationStateMonitor removeObserver:]_block_invoke
- ___44-[GCApplicationStateMonitor removeObserver:]_block_invoke.cold.1
- ___51-[GCApplicationStateMonitor initializeStateMonitor]_block_invoke
- ___51-[GCApplicationStateMonitor initializeStateMonitor]_block_invoke.92
- ___51-[GCApplicationStateMonitor initializeStateMonitor]_block_invoke.cold.1
- ___53-[GCApplicationStateMonitor setFrontmostApplication:]_block_invoke
- ___53-[GCApplicationStateMonitor setFrontmostApplication:]_block_invoke_2
- ___53-[GCApplicationStateMonitor setFrontmostApplication:]_block_invoke_2.cold.1
- ___54-[GCApplicationStateMonitor updateInterestedBundleIDs]_block_invoke
- ___54-[GCApplicationStateMonitor updateInterestedBundleIDs]_block_invoke.cold.1
- ___54-[GCApplicationStateMonitor updateInterestedBundleIDs]_block_invoke.cold.2
- ___59-[GCApplicationStateMonitor onFrontmostApplicationChanged:]_block_invoke
- ___59-[GCApplicationStateMonitor onFrontmostApplicationChanged:]_block_invoke.cold.1
- ___62-[GCApplicationStateMonitor addObserver:forProcessIdentifier:]_block_invoke
- ___62-[GCApplicationStateMonitor addObserver:forProcessIdentifier:]_block_invoke.94
- ___62-[GCApplicationStateMonitor addObserver:forProcessIdentifier:]_block_invoke.cold.1
- ___62-[GCApplicationStateMonitor addObserver:forProcessIdentifier:]_block_invoke.cold.2
- ___62-[GCApplicationStateMonitor addObserver:forProcessIdentifier:]_block_invoke_2
- ___62-[GCApplicationStateMonitor addObserver:forProcessIdentifier:]_block_invoke_2.cold.1
- ___62-[GCApplicationStateMonitor addObserver:forProcessIdentifier:]_block_invoke_2.cold.2
- ___65-[GCApplicationStateMonitor removeObserver:forProcessIdentifier:]_block_invoke
- ___65-[GCApplicationStateMonitor removeObserver:forProcessIdentifier:]_block_invoke.cold.1
- ___65-[GCApplicationStateMonitor removeObserver:forProcessIdentifier:]_block_invoke.cold.2
- ___65-[GCApplicationStateMonitor removeObserver:forProcessIdentifier:]_block_invoke.cold.3
- ___65-[GCApplicationStateMonitor removeObserver:forProcessIdentifier:]_block_invoke.cold.4
- ___65-[GCApplicationStateMonitor removeObserver:forProcessIdentifier:]_block_invoke.cold.5
- ___78-[_GCRacingWheelManager initWithDeviceSessionConfiguration:queue:environment:]_block_invoke
- ___78-[_GCRacingWheelManager initWithDeviceSessionConfiguration:queue:environment:]_block_invoke.87
- ___78-[_GCRacingWheelManager initWithDeviceSessionConfiguration:queue:environment:]_block_invoke.cold.1
- ___block_descriptor_40_e8_32w_e22_v16?0"NSDictionary"8lw32l8
- ___block_descriptor_48_e8_32s_e22_v16?0"NSDictionary"8ls32l8
- ___block_descriptor_52_e8_32s40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_56_e8_32s40r48w_e22_v16?0"NSDictionary"8lw48l8r40l8s32l8
- ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
- ___block_literal_global.151
- _objc_msgSend$addObserver:forProcessIdentifier:
- _objc_msgSend$applicationBackgrounded:
- _objc_msgSend$applicationForegrounded:
- _objc_msgSend$frontmostApplication
- _objc_msgSend$initializeForegroundMonitor
- _objc_msgSend$initializeStateMonitor
- _objc_msgSend$removeObserver:forProcessIdentifier:
- _objc_msgSend$setFrontmostApplication:
- _objc_msgSend$startTrackingSessionForClient:
- _objc_msgSend$stopObservingClientStateChanges:
- _objc_msgSend$stopObservingClientStateChangesForAllClients
- _objc_msgSend$stopTrackingSessionForClient:
- _objc_msgSend$stopTrackingSessionsForAllClients
- _objc_msgSend$updateInterestedBundleIDs
- _objc_msgSend$weakToStrongObjectsMapTable
- _sharedInstance.sharedStateMonitor
CStrings:
+ "@\"<BSInvalidatable>\""
+ "@\"BKSHIDEventDeliveryChainObserver\""
+ "@\"GCIONotificationPort\""
+ "Activate GCRacingWheelManager"
+ "BKSHIDEventDeliveryChainObserving"
+ "DeferringTarget"
+ "GCHIDEventDeliveryMonitor"
+ "GameController.LegacyHIDQueue"
+ "Invalidate GCRacingWheelManager"
+ "Notify Active HID Event Target Changed"
+ "Notify No Active HID Event Target"
+ "Remove all remaining Racing Wheel Devices: %@"
+ "TB,N,V_monitorControllerEventsInBackground"
+ "Ti,R,V_deferringTarget"
+ "[%@] Client added: %@"
+ "[%@] Client removed: %@"
+ "[%@] Update active process (%i) wants HOME button %{BOOL}d -> %{BOOL}d"
+ "[%@] setActiveApplicationPID - was %d now %d"
+ "_GCHIDEventDeliveryMonitor"
+ "_activeAnalyticsPID"
+ "_deferringTarget"
+ "_deliveryChain"
+ "_deliveryChainObserver"
+ "addCancellationHandler:onQueue:"
+ "addChainObserver:"
+ "deferringPath"
+ "deferringTarget"
+ "futureWithLabel:block:"
+ "initWithDisplay:environment:"
+ "monitorControllerEventsInBackground"
+ "nullDisplay"
+ "observer:deliveryChainDidUpdate:"
+ "pid"
+ "port"
+ "setMonitorControllerEventsInBackground:"
+ "v32@0:8@\"BKSHIDEventDeliveryChainObserver\"16@\"BKSHIDEventDeliveryChain\"24"
- "%@ application backgrounded: %d"
- "%@ application foregrounded: %d"
- "%@ stopped observing changes for PID %d, which was the active application"
- "Frontmost application is now %d"
- "GCApplicationStateMonitor"
- "GCApplicationStateMonitor is not accessible from this process."
- "GCApplicationStateObserver"
- "Racing Wheel Device Matched: %@"
- "Received user info: %@"
- "Setting frontmostApplicationIdentifier to %@"
- "Starting racing wheel support..."
- "T@\"NSString\",&,N,V_frontmostApplicationIdentifier"
- "Ti,N,V_frontmostApplication"
- "[%@] Update foreground process (%i) wants HOME button %{BOOL}d -> %{BOOL}d"
- "_bksStateMonitor"
- "_frontmostApplication"
- "_frontmostApplicationIdentifier"
- "_observerToPIDs"
- "_pidToBundleIdentifier"
- "_pidToObservers"
- "addObserver - %@ is observing the following processes: %@"
- "addObserver - Error: unable to locate bundle identifier for pid %@"
- "addObserver - Process %@ has the following observers: %@"
- "addObserver - Process %@ is already observed by %@, no need to re-register"
- "addObserver - Registered pid %@ with bundle identifier %@"
- "addObserver:forProcessIdentifier:"
- "applicationBackgrounded:"
- "applicationForegrounded:"
- "com.apple.gamecontroller.appstatemonitor"
- "frontmostApplication"
- "frontmostApplicationIdentifier"
- "initializeForegroundMonitor"
- "initializeStateMonitor"
- "onFrontmostApplicationChanged:"
- "removeObserver - %@ is no longer being observed by anything, removing bundleIdentifier mapping"
- "removeObserver - %@ is no longer being observed by anything, removing pid:observer mapping."
- "removeObserver - %@ is no longer observing anything, removing observer:pid mapping."
- "removeObserver - %@ is no longer observing the following processes: %@"
- "removeObserver - Process %@ has the following observers: %@"
- "removeObserver - Process %@ is not observed by %@, no need to unregister"
- "removeObserver - Removing all observers for %@"
- "removeObserver:forProcessIdentifier:"
- "setActiveApplicationPID - was %d now %d"
- "setFrontmostApplication %@"
- "setFrontmostApplication:"
- "setFrontmostApplicationIdentifier:"
- "startTrackingSessionForClient:"
- "stopObservingClientStateChanges:"
- "stopObservingClientStateChangesForAllClients"
- "stopTrackingSessionForClient:"
- "updateInterestedBundleIDs"
- "updateInterestedBundleIDs - observed PIDs: %@"
- "updateInterestedBundleIDs - observed bundle identifiers: %@"
- "weakToStrongObjectsMapTable"

```
