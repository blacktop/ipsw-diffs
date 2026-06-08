## AccessorySensorManagerServices

> `/System/Library/PrivateFrameworks/AccessorySensorManagerServices.framework/AccessorySensorManagerServices`

```diff

-11.28.0.0.0
-  __TEXT.__text: 0x3398
-  __TEXT.__auth_stubs: 0x210
-  __TEXT.__objc_methlist: 0x454
+20.26.0.0.1
+  __TEXT.__text: 0x63a4
+  __TEXT.__objc_methlist: 0x634
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__cstring: 0x118d
-  __TEXT.__unwind_info: 0x208
-  __TEXT.__objc_classname: 0xcb
-  __TEXT.__objc_methname: 0xa36
-  __TEXT.__objc_methtype: 0x303
-  __TEXT.__objc_stubs: 0x480
-  __DATA_CONST.__got: 0x38
-  __DATA_CONST.__const: 0x128
-  __DATA_CONST.__objc_classlist: 0x20
+  __TEXT.__gcc_except_tab: 0x2cc
+  __TEXT.__cstring: 0x21f2
+  __TEXT.__unwind_info: 0x328
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1c8
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x200
+  __DATA_CONST.__objc_selrefs: 0x2b8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x118
-  __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0xa70
-  __DATA.__objc_ivar: 0x44
-  __DATA.__data: 0x260
-  __DATA_DIRTY.__objc_data: 0x140
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__got: 0x48
+  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__cfstring: 0x80
+  __AUTH_CONST.__objc_const: 0x1110
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__objc_ivar: 0x80
+  __DATA.__data: 0x2d0
+  __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D633071A-2BC5-3F38-BCB8-32BC7F586789
-  Functions: 146
-  Symbols:   493
-  CStrings:  199
+  UUID: BD00B44E-9D22-3D07-8FD0-2758D8F2A73B
+  Functions: 227
+  Symbols:   741
+  CStrings:  148
 
Symbols:
+ +[ASMCompanionServices supportsSecureCoding]
+ -[ASMCompanionServices .cxx_destruct]
+ -[ASMCompanionServices _ensureXPCStarted]
+ -[ASMCompanionServices _interrupted]
+ -[ASMCompanionServices _interrupted].cold.1
+ -[ASMCompanionServices _invalidated]
+ -[ASMCompanionServices _invalidated].cold.1
+ -[ASMCompanionServices _invalidated].cold.2
+ -[ASMCompanionServices clientID]
+ -[ASMCompanionServices description]
+ -[ASMCompanionServices dispatchQueue]
+ -[ASMCompanionServices encodeWithCoder:]
+ -[ASMCompanionServices forceStartWiFiAwareBrowser:]
+ -[ASMCompanionServices forceStartWiFiAwareListener:]
+ -[ASMCompanionServices initWithCoder:]
+ -[ASMCompanionServices init]
+ -[ASMCompanionServices interruptionHandler]
+ -[ASMCompanionServices invalidate]
+ -[ASMCompanionServices invalidationHandler]
+ -[ASMCompanionServices setClientID:]
+ -[ASMCompanionServices setDispatchQueue:]
+ -[ASMCompanionServices setInterruptionHandler:]
+ -[ASMCompanionServices setInvalidationHandler:]
+ -[ASMCompanionServices setupDataPipeWithCompanionDevice:completion:]
+ -[ASMCompanionServices startWiFiAwarePublisherForHandoff:]
+ -[ASMCompanionServices startWiFiAwareSubscriberAndPairForHandoff:]
+ -[ASMInertialOdometryServices _attemptReconnection]
+ -[ASMInertialOdometryServices _attemptReconnection].cold.1
+ -[ASMInertialOdometryServices _attemptReconnection].cold.2
+ -[ASMInertialOdometryServices _attemptReestablishData]
+ -[ASMInertialOdometryServices _attemptReestablishData].cold.1
+ -[ASMInertialOdometryServices _cleanupFailedAvailabilityReestablishment:]
+ -[ASMInertialOdometryServices _cleanupFailedAvailabilityReestablishment:].cold.1
+ -[ASMInertialOdometryServices _cleanupFailedDataReestablishment:]
+ -[ASMInertialOdometryServices _cleanupFailedDataReestablishment:].cold.1
+ -[ASMInertialOdometryServices _clearInertialOdometryPeripheralSets]
+ -[ASMInertialOdometryServices _recordBtAddressToIdentifierMapping:identifier:]
+ -[ASMInertialOdometryServices _recordInertialOdometryAvailability:forBtAddress:]
+ -[ASMInertialOdometryServices _reestablishAvailabilityForBtAddress:]
+ -[ASMInertialOdometryServices _reestablishAvailabilityForBtAddress:].cold.1
+ -[ASMInertialOdometryServices _reestablishAvailabilityForIdentifier:]
+ -[ASMInertialOdometryServices _reestablishAvailabilityForIdentifier:].cold.1
+ -[ASMInertialOdometryServices _reestablishAvailabilityForIdentifier:].cold.2
+ -[ASMInertialOdometryServices _reestablishAvailability]
+ -[ASMInertialOdometryServices _reestablishDataForIdentifier:]
+ -[ASMInertialOdometryServices _reestablishSubscriptions]
+ -[ASMInertialOdometryServices _reestablishSubscriptions].cold.1
+ -[ASMInertialOdometryServices inertialOdometryAvailabilityChanged:forPeripheral:btAddress:]
+ -[ASMInertialOdometryServices isInertialOdometryAvailableForBtAddress:]
+ GCC_except_table11
+ GCC_except_table15
+ GCC_except_table16
+ GCC_except_table18
+ GCC_except_table19
+ GCC_except_table24
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table39
+ GCC_except_table40
+ GCC_except_table41
+ GCC_except_table45
+ GCC_except_table49
+ GCC_except_table53
+ GCC_except_table57
+ _ASMErrorF
+ _OBJC_CLASS_$_ASMCompanionServices
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_IVAR_$_ASMCompanionServices._clientID
+ _OBJC_IVAR_$_ASMCompanionServices._dispatchQueue
+ _OBJC_IVAR_$_ASMCompanionServices._interruptionHandler
+ _OBJC_IVAR_$_ASMCompanionServices._invalidateCalled
+ _OBJC_IVAR_$_ASMCompanionServices._invalidateDone
+ _OBJC_IVAR_$_ASMCompanionServices._invalidationHandler
+ _OBJC_IVAR_$_ASMCompanionServices._xpcCnx
+ _OBJC_IVAR_$_ASMInertialOdometryServices._btAddressToIdentifierMap
+ _OBJC_IVAR_$_ASMInertialOdometryServices._inertialOdometryConfigsByIdentifier
+ _OBJC_IVAR_$_ASMInertialOdometryServices._pendingDataReestablishmentByBtAddress
+ _OBJC_IVAR_$_ASMInertialOdometryServices._pendingDataReestablishmentByIdentifier
+ _OBJC_IVAR_$_ASMInertialOdometryServices._subscribedInertialOdometryAvailabilityPeripheralsByBtAddress
+ _OBJC_IVAR_$_ASMInertialOdometryServices._subscribedInertialOdometryAvailabilityPeripheralsByIdentifier
+ _OBJC_IVAR_$_ASMInertialOdometryServices._subscribedInertialOdometryDataPeripheralsByBtAddress
+ _OBJC_IVAR_$_ASMInertialOdometryServices._subscribedInertialOdometryDataPeripheralsByIdentifier
+ _OBJC_METACLASS_$_ASMCompanionServices
+ _OUTLINED_FUNCTION_5
+ __OBJC_$_CLASS_METHODS_ASMCompanionServices
+ __OBJC_$_CLASS_PROP_LIST_ASMCompanionServices
+ __OBJC_$_INSTANCE_METHODS_ASMCompanionServices
+ __OBJC_$_INSTANCE_VARIABLES_ASMCompanionServices
+ __OBJC_$_PROP_LIST_ASMCompanionServices
+ __OBJC_CLASS_PROTOCOLS_$_ASMCompanionServices
+ __OBJC_CLASS_RO_$_ASMCompanionServices
+ __OBJC_METACLASS_RO_$_ASMCompanionServices
+ ___34-[ASMCompanionServices invalidate]_block_invoke
+ ___34-[ASMCompanionServices invalidate]_block_invoke.cold.1
+ ___41-[ASMCompanionServices _ensureXPCStarted]_block_invoke
+ ___41-[ASMCompanionServices _ensureXPCStarted]_block_invoke_2
+ ___51-[ASMCompanionServices forceStartWiFiAwareBrowser:]_block_invoke
+ ___51-[ASMCompanionServices forceStartWiFiAwareBrowser:]_block_invoke.cold.1
+ ___51-[ASMCompanionServices forceStartWiFiAwareBrowser:]_block_invoke.cold.2
+ ___51-[ASMCompanionServices forceStartWiFiAwareBrowser:]_block_invoke.cold.3
+ ___51-[ASMCompanionServices forceStartWiFiAwareBrowser:]_block_invoke_2
+ ___51-[ASMCompanionServices forceStartWiFiAwareBrowser:]_block_invoke_2.cold.1
+ ___52-[ASMCompanionServices forceStartWiFiAwareListener:]_block_invoke
+ ___52-[ASMCompanionServices forceStartWiFiAwareListener:]_block_invoke.cold.1
+ ___52-[ASMCompanionServices forceStartWiFiAwareListener:]_block_invoke.cold.2
+ ___52-[ASMCompanionServices forceStartWiFiAwareListener:]_block_invoke.cold.3
+ ___52-[ASMCompanionServices forceStartWiFiAwareListener:]_block_invoke_2
+ ___52-[ASMCompanionServices forceStartWiFiAwareListener:]_block_invoke_2.cold.1
+ ___58-[ASMCompanionServices startWiFiAwarePublisherForHandoff:]_block_invoke
+ ___58-[ASMCompanionServices startWiFiAwarePublisherForHandoff:]_block_invoke.cold.1
+ ___58-[ASMCompanionServices startWiFiAwarePublisherForHandoff:]_block_invoke.cold.2
+ ___58-[ASMCompanionServices startWiFiAwarePublisherForHandoff:]_block_invoke.cold.3
+ ___58-[ASMCompanionServices startWiFiAwarePublisherForHandoff:]_block_invoke_2
+ ___58-[ASMCompanionServices startWiFiAwarePublisherForHandoff:]_block_invoke_2.cold.1
+ ___66-[ASMCompanionServices startWiFiAwareSubscriberAndPairForHandoff:]_block_invoke
+ ___66-[ASMCompanionServices startWiFiAwareSubscriberAndPairForHandoff:]_block_invoke.cold.1
+ ___66-[ASMCompanionServices startWiFiAwareSubscriberAndPairForHandoff:]_block_invoke.cold.2
+ ___66-[ASMCompanionServices startWiFiAwareSubscriberAndPairForHandoff:]_block_invoke.cold.3
+ ___66-[ASMCompanionServices startWiFiAwareSubscriberAndPairForHandoff:]_block_invoke_2
+ ___66-[ASMCompanionServices startWiFiAwareSubscriberAndPairForHandoff:]_block_invoke_2.cold.1
+ ___68-[ASMCompanionServices setupDataPipeWithCompanionDevice:completion:]_block_invoke
+ ___68-[ASMCompanionServices setupDataPipeWithCompanionDevice:completion:]_block_invoke.cold.1
+ ___68-[ASMCompanionServices setupDataPipeWithCompanionDevice:completion:]_block_invoke.cold.2
+ ___68-[ASMCompanionServices setupDataPipeWithCompanionDevice:completion:]_block_invoke.cold.3
+ ___68-[ASMCompanionServices setupDataPipeWithCompanionDevice:completion:]_block_invoke_2
+ ___68-[ASMCompanionServices setupDataPipeWithCompanionDevice:completion:]_block_invoke_2.cold.1
+ ___69-[ASMInertialOdometryServices _reestablishAvailabilityForIdentifier:]_block_invoke
+ ___69-[ASMInertialOdometryServices _reestablishAvailabilityForIdentifier:]_block_invoke_2
+ ___69-[ASMInertialOdometryServices _reestablishAvailabilityForIdentifier:]_block_invoke_2.cold.1
+ ___90-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke_3
+ ___91-[ASMInertialOdometryServices inertialOdometryAvailabilityChanged:forPeripheral:btAddress:]_block_invoke
+ ___91-[ASMInertialOdometryServices inertialOdometryAvailabilityChanged:forPeripheral:btAddress:]_block_invoke.cold.1
+ ___91-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke_3
+ ___94-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke_3
+ ___95-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithBtAddress:config:completion:]_block_invoke_3
+ ___95-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke_3
+ ___96-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithIdentifier:config:completion:]_block_invoke_3
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ ___block_literal_global.100
+ ___block_literal_global.71
+ ___block_literal_global.81
+ ___block_literal_global.88
+ ___block_literal_global.94
+ ___stack_chk_fail
+ ___stack_chk_guard
+ _gLogCategory_ASMCompanionServices
+ _objc_claimAutoreleasedReturnValue
+ _objc_enumerationMutation
+ _objc_msgSend$_attemptReconnection
+ _objc_msgSend$_attemptReestablishData
+ _objc_msgSend$_cleanupFailedAvailabilityReestablishment:
+ _objc_msgSend$_clearInertialOdometryPeripheralSets
+ _objc_msgSend$_recordBtAddressToIdentifierMapping:identifier:
+ _objc_msgSend$_recordInertialOdometryAvailability:forBtAddress:
+ _objc_msgSend$_reestablishAvailability
+ _objc_msgSend$_reestablishAvailabilityForBtAddress:
+ _objc_msgSend$_reestablishAvailabilityForIdentifier:
+ _objc_msgSend$_reestablishDataForIdentifier:
+ _objc_msgSend$_reestablishSubscriptions
+ _objc_msgSend$addObject:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$copy
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$forceStartWiFiAwareBrowser:
+ _objc_msgSend$forceStartWiFiAwareListener:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$removeObject:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$setSet:
+ _objc_msgSend$setupDataPipeWithCompanionDevice:completion:
+ _objc_msgSend$startWiFiAwarePublisherForHandoff:
+ _objc_msgSend$startWiFiAwareSubscriberAndPairForHandoff:
+ _objc_msgSend$subscribeToInertialOdometryAvailabilityChangeWithBtAddress:forPeripheral:completion:
+ _objc_msgSend$subscribeToInertialOdometryAvailabilityChangeWithIdentifier:forPeripheral:completion:
+ _objc_msgSend$unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:forPeripheral:completion:
+ _objc_msgSend$unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:forPeripheral:completion:
+ _objc_release_x23
+ _objc_release_x24
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x8
- -[ASMInertialOdometryServices inertialOdometryAvailabilityChanged:forPeripheral:]
- -[ASMInertialOdometryServices subscribeToInertialOdometryData]
- -[ASMInertialOdometryServices unsubscribeFromInertialOdometryData]
- GCC_except_table28
- GCC_except_table29
- GCC_except_table30
- ___62-[ASMInertialOdometryServices subscribeToInertialOdometryData]_block_invoke
- ___62-[ASMInertialOdometryServices subscribeToInertialOdometryData]_block_invoke.cold.1
- ___62-[ASMInertialOdometryServices subscribeToInertialOdometryData]_block_invoke.cold.2
- ___62-[ASMInertialOdometryServices subscribeToInertialOdometryData]_block_invoke.cold.3
- ___62-[ASMInertialOdometryServices subscribeToInertialOdometryData]_block_invoke_2
- ___62-[ASMInertialOdometryServices subscribeToInertialOdometryData]_block_invoke_2.cold.1
- ___66-[ASMInertialOdometryServices unsubscribeFromInertialOdometryData]_block_invoke
- ___66-[ASMInertialOdometryServices unsubscribeFromInertialOdometryData]_block_invoke.cold.1
- ___66-[ASMInertialOdometryServices unsubscribeFromInertialOdometryData]_block_invoke.cold.2
- ___66-[ASMInertialOdometryServices unsubscribeFromInertialOdometryData]_block_invoke.cold.3
- ___66-[ASMInertialOdometryServices unsubscribeFromInertialOdometryData]_block_invoke_2
- ___66-[ASMInertialOdometryServices unsubscribeFromInertialOdometryData]_block_invoke_2.cold.1
- ___81-[ASMInertialOdometryServices inertialOdometryAvailabilityChanged:forPeripheral:]_block_invoke
- ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_literal_global.48
- ___block_literal_global.53
- ___block_literal_global.57
- ___block_literal_global.64
- ___block_literal_global.69
- ___block_literal_global.73
- ___block_literal_global.77
- _objc_autoreleaseReturnValue
- _objc_msgSend$subscribeToInertialOdometryAvailabilityChangeWithBtAddress:forPeripheral:
- _objc_msgSend$subscribeToInertialOdometryAvailabilityChangeWithIdentifier:forPeripheral:
- _objc_msgSend$subscribeToInertialOdometryData:
- _objc_msgSend$unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:forPeripheral:
- _objc_msgSend$unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:forPeripheral:
- _objc_msgSend$unsubscribeFromInertialOdometryData:
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "### Availability resubscription XPC error for %@: %{error}"
+ "### Availability resubscription failed for %@: %{error}"
+ "### Failed to subscribe to inertial odometry availability for %@: %{error}"
+ "### Failed to subscribe to inertial odometry availability for btAddress %@: %{error}"
+ "### Failed to unsubscribe from inertial odometry availability for %@: %{error}"
+ "### Failed to unsubscribe from inertial odometry availability for btAddress %@: %{error}"
+ "### No identifier mapping found for btAddress %@"
+ "### Reconnection XPC start failed: %{error}"
+ "### _reestablishAvailabilityForIdentifier no XPC"
+ "### forceStartWiFiAwareBrowser XPC error: %{error}"
+ "### forceStartWiFiAwareBrowser failed to start XPC"
+ "### forceStartWiFiAwareBrowser no XPC"
+ "### forceStartWiFiAwareListener XPC error: %{error}"
+ "### forceStartWiFiAwareListener failed to start XPC"
+ "### forceStartWiFiAwareListener no XPC"
+ "### setupDataPipeWithCompanionDevice XPC error: %{error}"
+ "### setupDataPipeWithCompanionDevice failed to start XPC"
+ "### setupDataPipeWithCompanionDevice no XPC"
+ "### startWiFiAwarePublisherForHandoff XPC error: %{error}"
+ "### startWiFiAwarePublisherForHandoff failed to start XPC"
+ "### startWiFiAwarePublisherForHandoff no XPC"
+ "### startWiFiAwareSubscriberAndPairForHandoff XPC error: %{error}"
+ "### startWiFiAwareSubscriberAndPairForHandoff failed to start XPC"
+ "### startWiFiAwareSubscriberAndPairForHandoff no XPC"
+ "-[ASMCompanionServices _interrupted]"
+ "-[ASMCompanionServices _invalidated]"
+ "-[ASMCompanionServices forceStartWiFiAwareBrowser:]_block_invoke"
+ "-[ASMCompanionServices forceStartWiFiAwareBrowser:]_block_invoke_2"
+ "-[ASMCompanionServices forceStartWiFiAwareListener:]_block_invoke"
+ "-[ASMCompanionServices forceStartWiFiAwareListener:]_block_invoke_2"
+ "-[ASMCompanionServices invalidate]_block_invoke"
+ "-[ASMCompanionServices setupDataPipeWithCompanionDevice:completion:]_block_invoke"
+ "-[ASMCompanionServices setupDataPipeWithCompanionDevice:completion:]_block_invoke_2"
+ "-[ASMCompanionServices startWiFiAwarePublisherForHandoff:]_block_invoke"
+ "-[ASMCompanionServices startWiFiAwarePublisherForHandoff:]_block_invoke_2"
+ "-[ASMCompanionServices startWiFiAwareSubscriberAndPairForHandoff:]_block_invoke"
+ "-[ASMCompanionServices startWiFiAwareSubscriberAndPairForHandoff:]_block_invoke_2"
+ "-[ASMInertialOdometryServices _attemptReconnection]"
+ "-[ASMInertialOdometryServices _attemptReestablishData]"
+ "-[ASMInertialOdometryServices _cleanupFailedAvailabilityReestablishment:]"
+ "-[ASMInertialOdometryServices _cleanupFailedDataReestablishment:]"
+ "-[ASMInertialOdometryServices _recordBtAddressToIdentifierMapping:identifier:]"
+ "-[ASMInertialOdometryServices _recordInertialOdometryAvailability:forBtAddress:]"
+ "-[ASMInertialOdometryServices _recordInertialOdometryAvailability:forPeripheral:]"
+ "-[ASMInertialOdometryServices _reestablishAvailabilityForBtAddress:]"
+ "-[ASMInertialOdometryServices _reestablishAvailabilityForIdentifier:]"
+ "-[ASMInertialOdometryServices _reestablishAvailabilityForIdentifier:]_block_invoke"
+ "-[ASMInertialOdometryServices _reestablishAvailabilityForIdentifier:]_block_invoke_2"
+ "-[ASMInertialOdometryServices _reestablishSubscriptions]"
+ "-[ASMInertialOdometryServices inertialOdometryAvailabilityChanged:forPeripheral:btAddress:]_block_invoke"
+ "-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke_3"
+ "-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke_3"
+ "-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke_3"
+ "-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke_3"
+ "ASMCompanionServices"
+ "ASMCompanionServices, CID 0x%X"
+ "Attempting reconnection after interruption"
+ "Availability now available for %@, reestablishing data subscription"
+ "Cleaned up failed availability reestablishment state for %@"
+ "Cleaned up failed data reestablishment state for %@"
+ "Converting btAddress %@ to identifier %@ for availability resubscription"
+ "No XPC connection available"
+ "Recorded btAddress - %@ with identifer - %@"
+ "Reestablishing subscriptions after daemon restart"
+ "Removing inertial odometry availability subscription tracking for %@"
+ "Removing inertial odometry availability subscription tracking for btAddress %@"
+ "Resubscribing to inertial odometry availability for peripheral: %@"
+ "Successfully resubscribed to inertial odometry availability for %@"
+ "Tracking inertial odometry availability subscription for %@"
+ "Tracking inertial odometry availability subscription for btAddress %@"
+ "Updated inertial odometry availability for %@"
+ "Updating inertial odometry availability entry for %@ using identifier %@"
+ "Waiting for availability before reestablishing data subscriptions"
+ "cms"
+ "forceStartWiFiAwareBrowser, CID 0x%X"
+ "forceStartWiFiAwareListener, CID 0x%X"
+ "setupDataPipeWithCompanionDevice for btAddress:%@"
+ "startWiFiAwarePublisherForHandoff"
+ "startWiFiAwareSubscriberAndPairForHandoff"
- "### subscribeToInertialOdometryData failed to start XPC"
- "### subscribeToInertialOdometryData no XPC"
- "### unsubscribeFromInertialOdometryData failed to start XPC"
- "### unsubscribeFromInertialOdometryData no XPC"
- "-[ASMInertialOdometryServices inertialOdometryAvailabilityChanged:forPeripheral:]_block_invoke"
- "-[ASMInertialOdometryServices subscribeToInertialOdometryData]_block_invoke"
- "-[ASMInertialOdometryServices subscribeToInertialOdometryData]_block_invoke_2"
- "-[ASMInertialOdometryServices unsubscribeFromInertialOdometryData]_block_invoke"
- "-[ASMInertialOdometryServices unsubscribeFromInertialOdometryData]_block_invoke_2"
- ".cxx_destruct"
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@?"
- "@?16@0:8"
- "ASMPeripheralConfig"
- "ASMPeripheralInertialOdometryConfig"
- "ASMServicesXPCClientInterface"
- "ASMServicesXPCDaemonInterface"
- "B"
- "B16@0:8"
- "I"
- "I16@0:8"
- "NSCoding"
- "NSSecureCoding"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_dispatchQueue"
- "T@?,C,N,V_inertialOdometryAvailabilityHandler"
- "T@?,C,N,V_inertialOdometryDataReceivedHandler"
- "T@?,C,N,V_interruptionHandler"
- "T@?,C,N,V_invalidationHandler"
- "TB,R"
- "TI,N,V_clientID"
- "_clearInertialOdometryAvailabilityMap"
- "_clientID"
- "_dispatchQueue"
- "_ensureXPCStarted"
- "_inertialOdometryAvailabilityHandler"
- "_inertialOdometryAvailabilityMap"
- "_inertialOdometryDataReceivedHandler"
- "_interrupted"
- "_interruptionHandler"
- "_invalidateCalled"
- "_invalidateDone"
- "_invalidated"
- "_invalidationHandler"
- "_recordInertialOdometryAvailability:forPeripheral:"
- "_setQueue:"
- "_xpcCnx"
- "allocWithZone:"
- "asmServicesRequireReset"
- "c24@0:8@16"
- "clientID"
- "copyWithZone:"
- "description"
- "dispatchQueue"
- "encodeInt64:forKey:"
- "encodeWithCoder:"
- "inertialOdometryAvailabilityChanged:forPeripheral:"
- "inertialOdometryAvailabilityHandler"
- "inertialOdometryDataReceived:"
- "inertialOdometryDataReceivedHandler"
- "init"
- "initWithCoder:"
- "initWithMachServiceName:options:"
- "intValue"
- "interfaceWithProtocol:"
- "interruptionHandler"
- "invalidate"
- "invalidationHandler"
- "isInertialOdometryAvailableForPeripheral:"
- "modify:peripheralConfiguration:identifier:completion:"
- "modifyInertialOdometryWithBtAddress:configuration:btAddress:completion:"
- "modifyInertialOdometryWithIdentifier:configuration:identifier:completion:"
- "modifyPeripheralConfiguration:identifier:completion:"
- "modifyPeripheralInertialOdometryWithBtAddress:config:completion:"
- "modifyPeripheralInertialOdometryWithIdentifier:config:completion:"
- "numberWithChar:"
- "objectForKeyedSubscript:"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllObjects"
- "resume"
- "setClientID:"
- "setDispatchQueue:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInertialOdometryAvailabilityHandler:"
- "setInertialOdometryDataReceivedHandler:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setObject:forKeyedSubscript:"
- "setRemoteObjectInterface:"
- "subscribeToInertialOdometryAvailabilityChangeWithBtAddress:"
- "subscribeToInertialOdometryAvailabilityChangeWithBtAddress:forPeripheral:"
- "subscribeToInertialOdometryAvailabilityChangeWithIdentifier:"
- "subscribeToInertialOdometryAvailabilityChangeWithIdentifier:forPeripheral:"
- "subscribeToInertialOdometryData"
- "subscribeToInertialOdometryData:"
- "subscribing to Asen inertial odometry data"
- "supportsSecureCoding"
- "unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:"
- "unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:forPeripheral:"
- "unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:"
- "unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:forPeripheral:"
- "unsubscribeFromInertialOdometryData"
- "unsubscribeFromInertialOdometryData:"
- "unsubscribing from Asen inertial odometry data"
- "v16@0:8"
- "v20@0:8I16"
- "v24@0:8@\"ASMInertialOdometryServices\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSData\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v28@0:8c16@\"NSString\"20"
- "v28@0:8c16@20"
- "v32@0:8@\"ASMInertialOdometryServices\"16@\"NSString\"24"
- "v32@0:8@16@24"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"ASMInertialOdometryServices\"16@\"ASMPeripheralInertialOdometryConfig\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"ASMPeripheralControlServices\"16@\"ASMPeripheralConfig\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v56@0:8@\"ASMPeripheralControlServices\"16@\"NSData\"24@\"NSString\"32@\"NSString\"40@?<v@?@\"NSError\">48"
- "v56@0:8@16@24@32@40@?48"
- "write:withData:characteristic:identifier:completion:"
- "writeWithData:characteristic:identifier:completion:"

```
