## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/APTransport`

```diff

-860.7.1.0.0
-  __TEXT.__text: 0x9ac68
-  __TEXT.__auth_stubs: 0x3010
-  __TEXT.__objc_methlist: 0xbcc
-  __TEXT.__cstring: 0x288a4
-  __TEXT.__const: 0x2c8
-  __TEXT.__gcc_except_tab: 0x484
+890.61.4.11.2
+  __TEXT.__text: 0xa3d54
+  __TEXT.__auth_stubs: 0x31e0
+  __TEXT.__objc_methlist: 0x12d8
+  __TEXT.__cstring: 0x2ab77
+  __TEXT.__const: 0x328
+  __TEXT.__gcc_except_tab: 0x4cc
   __TEXT.__oslogstring: 0x16e
-  __TEXT.__dlopen_cstrs: 0x146
-  __TEXT.__unwind_info: 0x2518
-  __TEXT.__objc_classname: 0x111
-  __TEXT.__objc_methname: 0x3179
-  __TEXT.__objc_methtype: 0xb27
-  __TEXT.__objc_stubs: 0x31e0
-  __DATA_CONST.__got: 0x3a0
-  __DATA_CONST.__const: 0x33d8
-  __DATA_CONST.__objc_classlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x28
+  __TEXT.__dlopen_cstrs: 0x18b
+  __TEXT.__unwind_info: 0x2658
+  __TEXT.__objc_classname: 0x1db
+  __TEXT.__objc_methname: 0x46b1
+  __TEXT.__objc_methtype: 0xf03
+  __TEXT.__objc_stubs: 0x3ee0
+  __DATA_CONST.__got: 0x3d8
+  __DATA_CONST.__const: 0x3588
+  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe60
-  __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1818
-  __AUTH_CONST.__const: 0x2978
-  __AUTH_CONST.__cfstring: 0x5740
-  __AUTH_CONST.__objc_const: 0x12c8
-  __AUTH_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__objc_selrefs: 0x1378
+  __DATA_CONST.__objc_superrefs: 0x48
+  __DATA_CONST.__objc_arraydata: 0x20
+  __AUTH_CONST.__auth_got: 0x1900
+  __AUTH_CONST.__const: 0x2b48
+  __AUTH_CONST.__cfstring: 0x5ec0
+  __AUTH_CONST.__objc_const: 0x1b40
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0xf0
+  __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x278
-  __DATA.__objc_ivar: 0x118
-  __DATA.__data: 0xfb0
-  __DATA.__bss: 0x100
-  __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__data: 0xa10
-  __DATA_DIRTY.__bss: 0x230
+  __DATA.__objc_ivar: 0x15c
+  __DATA.__data: 0x1190
+  __DATA.__bss: 0x120
+  __DATA_DIRTY.__objc_data: 0x1e0
+  __DATA_DIRTY.__data: 0xaf0
+  __DATA_DIRTY.__bss: 0x238
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
-  - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/IO80211.framework/IO80211

   - /usr/lib/libIOReport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 36153C16-EC1E-3E6E-AD12-7E2B8E7A72B6
-  Functions: 4272
-  Symbols:   11091
-  CStrings:  5280
+  UUID: 40A80443-D0DB-371A-8DA1-422B3527AB2A
+  Functions: 4478
+  Symbols:   11612
+  CStrings:  5798
 
Symbols:
+ +[APBonjourCacheHomeKit getDeviceID:]
+ +[APBonjourCacheHomeKit isDeviceCacheable:]
+ +[APBonjourCacheHomeKit prepareDeviceInfo:]
+ +[APBonjourCacheHomeKit prepareDeviceInfo:].cold.1
+ +[APBonjourCacheHomeKit prepareDeviceInfo:].cold.2
+ +[APBonjourCacheHomeKit prepareDeviceInfo:].cold.3
+ +[APBonjourCacheHomeKit prepareDeviceInfo:].cold.4
+ +[APBonjourCacheHomeKit prepareDeviceInfo:].cold.5
+ +[APBonjourCacheHomeKit prepareDeviceInfo:].cold.6
+ -[APBonjourCacheEvictionTTL setTimeToLiveSeconds:]
+ -[APBonjourCacheEvictionTTL shouldEvict:]
+ -[APBonjourCacheEvictionTTL timeToLiveSeconds]
+ -[APBonjourCacheHomeKit activateWithCompletion:]
+ -[APBonjourCacheHomeKit activateWithCompletionInternal:]
+ -[APBonjourCacheHomeKit activateWithCompletionInternal:].cold.1
+ -[APBonjourCacheHomeKit activateWithCompletionInternal:].cold.2
+ -[APBonjourCacheHomeKit activateWithCompletionInternal:].cold.3
+ -[APBonjourCacheHomeKit activateWithCompletionInternal:].cold.4
+ -[APBonjourCacheHomeKit activatedPresentDeviceStashing]
+ -[APBonjourCacheHomeKit addExpectedDeviceID:]
+ -[APBonjourCacheHomeKit availableCachedDevices]
+ -[APBonjourCacheHomeKit cacheDevice:]
+ -[APBonjourCacheHomeKit cache]
+ -[APBonjourCacheHomeKit cachedDeviceFoundHandler]
+ -[APBonjourCacheHomeKit cachedDeviceLostHandler]
+ -[APBonjourCacheHomeKit cachedDevices]
+ -[APBonjourCacheHomeKit checkAndEvictCachedDevicesIfNecessary]
+ -[APBonjourCacheHomeKit checkAndEvictCachedDevicesIfNecessary].cold.1
+ -[APBonjourCacheHomeKit checkAndEvictCachedDevicesIfNecessary].cold.2
+ -[APBonjourCacheHomeKit currentNetworkSignature]
+ -[APBonjourCacheHomeKit dealloc]
+ -[APBonjourCacheHomeKit dealloc].cold.1
+ -[APBonjourCacheHomeKit dispatchQueue]
+ -[APBonjourCacheHomeKit evictCachedDeviceWithID:]
+ -[APBonjourCacheHomeKit evictCachedDeviceWithIDInternal:]
+ -[APBonjourCacheHomeKit evictionPolicies]
+ -[APBonjourCacheHomeKit expectedDeviceIDs]
+ -[APBonjourCacheHomeKit forceReportCachedDevicesFound]
+ -[APBonjourCacheHomeKit forceReportCachedDevicesLost]
+ -[APBonjourCacheHomeKit getCacheDirectoryURLWithParentDirectory:creatingIfNecessary:]
+ -[APBonjourCacheHomeKit getCacheDirectoryURLWithParentDirectory:creatingIfNecessary:].cold.1
+ -[APBonjourCacheHomeKit getCacheDirectoryURLWithParentDirectory:creatingIfNecessary:].cold.2
+ -[APBonjourCacheHomeKit getCacheDirectoryURLWithParentDirectory:creatingIfNecessary:].cold.3
+ -[APBonjourCacheHomeKit getCacheFileURLCreatingParentDirectoriesIfNecessary:]
+ -[APBonjourCacheHomeKit getCacheFileURLCreatingParentDirectoriesIfNecessary:].cold.1
+ -[APBonjourCacheHomeKit getCacheFileURLCreatingParentDirectoriesIfNecessary:].cold.2
+ -[APBonjourCacheHomeKit getCacheFileURLCreatingParentDirectoriesIfNecessary:].cold.3
+ -[APBonjourCacheHomeKit getReportableCachedDevices]
+ -[APBonjourCacheHomeKit handleHomeKitDeviceConfigurationChanged:]
+ -[APBonjourCacheHomeKit handleNetworkSignatureChanged:]
+ -[APBonjourCacheHomeKit handleRealDeviceFoundForCachedDevice:]
+ -[APBonjourCacheHomeKit handleRealDeviceFoundForCachedDevice:].cold.1
+ -[APBonjourCacheHomeKit handleRealDeviceFoundForCachedDevice:].cold.2
+ -[APBonjourCacheHomeKit handleRealDeviceFoundForCachedDevice:].cold.3
+ -[APBonjourCacheHomeKit handleRealDeviceLostForCachedDevice:]
+ -[APBonjourCacheHomeKit handleRealDeviceLostForCachedDevice:].cold.1
+ -[APBonjourCacheHomeKit homeKitDeviceMonitor]
+ -[APBonjourCacheHomeKit init]
+ -[APBonjourCacheHomeKit init].cold.1
+ -[APBonjourCacheHomeKit init].cold.2
+ -[APBonjourCacheHomeKit internalQueue]
+ -[APBonjourCacheHomeKit invalidateInternal]
+ -[APBonjourCacheHomeKit invalidate]
+ -[APBonjourCacheHomeKit invalidated]
+ -[APBonjourCacheHomeKit isValidNetworkSignature:]
+ -[APBonjourCacheHomeKit loadCache]
+ -[APBonjourCacheHomeKit presentRealDevices]
+ -[APBonjourCacheHomeKit realDeviceFound:]
+ -[APBonjourCacheHomeKit realDeviceFoundInternal:]
+ -[APBonjourCacheHomeKit realDeviceLost:]
+ -[APBonjourCacheHomeKit realDeviceLostInternal:]
+ -[APBonjourCacheHomeKit removeAllExpectedDeviceIDs]
+ -[APBonjourCacheHomeKit removeExpectedDeviceID:]
+ -[APBonjourCacheHomeKit reportCachedDevice:found:withHandler:]
+ -[APBonjourCacheHomeKit reportedCachedDeviceIDs]
+ -[APBonjourCacheHomeKit setActivatedPresentDeviceStashing:]
+ -[APBonjourCacheHomeKit setCache:]
+ -[APBonjourCacheHomeKit setCachedDeviceFoundHandler:]
+ -[APBonjourCacheHomeKit setCachedDeviceLostHandler:]
+ -[APBonjourCacheHomeKit setCurrentNetworkSignature:]
+ -[APBonjourCacheHomeKit setDispatchQueue:]
+ -[APBonjourCacheHomeKit setEvictionPolicies:]
+ -[APBonjourCacheHomeKit setExpectedDeviceIDs:]
+ -[APBonjourCacheHomeKit setHomeKitDeviceMonitor:]
+ -[APBonjourCacheHomeKit setInternalQueue:]
+ -[APBonjourCacheHomeKit setInvalidated:]
+ -[APBonjourCacheHomeKit setPresentRealDevices:]
+ -[APBonjourCacheHomeKit setReportedCachedDeviceIDs:]
+ -[APBonjourCacheHomeKit setSystemMonitor:]
+ -[APBonjourCacheHomeKit setUsePresentDeviceStashing:]
+ -[APBonjourCacheHomeKit setUseStrictNetworkSignatureMatching:]
+ -[APBonjourCacheHomeKit setupEvictionPolicies]
+ -[APBonjourCacheHomeKit setupEvictionPolicies].cold.1
+ -[APBonjourCacheHomeKit shouldEvictDevice:policy:]
+ -[APBonjourCacheHomeKit shouldProcessDeviceForCache:]
+ -[APBonjourCacheHomeKit shouldProcessDeviceForCache:].cold.1
+ -[APBonjourCacheHomeKit systemMonitor]
+ -[APBonjourCacheHomeKit uncacheDevice:]
+ -[APBonjourCacheHomeKit updateExpectedDeviceIDsAdding:removing:]
+ -[APBonjourCacheHomeKit usePresentDeviceStashing]
+ -[APBonjourCacheHomeKit useStrictNetworkSignatureMatching]
+ -[APBonjourCacheHomeKit writeCache]
+ -[APBonjourCacheHomeKit(Introspector) copyDescriptionInternal]
+ -[APBonjourCacheHomeKit(Introspector) copyDescription]
+ -[APBonjourCacheHomeKit(Introspector) describeBonjourInfo:]
+ -[APBonjourCacheHomeKit(Introspector) setupIntrospector]
+ -[APHomeKitDeviceMonitor accessoryDidUpdateName:]
+ -[APHomeKitDeviceMonitor activateWithCompletion:]
+ -[APHomeKitDeviceMonitor activateWithCompletionInternal:]
+ -[APHomeKitDeviceMonitor activateWithCompletionInternal:].cold.1
+ -[APHomeKitDeviceMonitor activateWithCompletionInternal:].cold.2
+ -[APHomeKitDeviceMonitor activateWithCompletionInternal:].cold.3
+ -[APHomeKitDeviceMonitor activateWithCompletionInternal:].cold.4
+ -[APHomeKitDeviceMonitor dealloc]
+ -[APHomeKitDeviceMonitor dealloc].cold.1
+ -[APHomeKitDeviceMonitor dispatchQueue]
+ -[APHomeKitDeviceMonitor fullRefresh]
+ -[APHomeKitDeviceMonitor handleHomeKitAccessoriesDidChange]
+ -[APHomeKitDeviceMonitor home:didAddAccessory:]
+ -[APHomeKitDeviceMonitor home:didRemoveAccessory:]
+ -[APHomeKitDeviceMonitor homeAccessories]
+ -[APHomeKitDeviceMonitor homeConfigurationDidChangeHandler]
+ -[APHomeKitDeviceMonitor homeKitDeviceIDs]
+ -[APHomeKitDeviceMonitor homeManager:didAddHome:]
+ -[APHomeKitDeviceMonitor homeManager:didRemoveHome:]
+ -[APHomeKitDeviceMonitor homeManagerDidUpdateCurrentHome:]
+ -[APHomeKitDeviceMonitor homeManagerDidUpdateHomes:]
+ -[APHomeKitDeviceMonitor homeManager]
+ -[APHomeKitDeviceMonitor init]
+ -[APHomeKitDeviceMonitor init].cold.1
+ -[APHomeKitDeviceMonitor init].cold.2
+ -[APHomeKitDeviceMonitor internalQueue]
+ -[APHomeKitDeviceMonitor invalidateInternal]
+ -[APHomeKitDeviceMonitor invalidate]
+ -[APHomeKitDeviceMonitor invalidated]
+ -[APHomeKitDeviceMonitor refreshWithAccessory:isAddOrUpdate:notifyOnAccessoryChange:]
+ -[APHomeKitDeviceMonitor refreshWithHome:isAddOrUpdate:notifyOnAccessoriesChanged:]
+ -[APHomeKitDeviceMonitor setDispatchQueue:]
+ -[APHomeKitDeviceMonitor setHomeAccessories:]
+ -[APHomeKitDeviceMonitor setHomeConfigurationDidChangeHandler:]
+ -[APHomeKitDeviceMonitor setHomeManager:]
+ -[APHomeKitDeviceMonitor setInternalQueue:]
+ -[APHomeKitDeviceMonitor setInvalidated:]
+ -[APTNANPairingDelegate dealloc]
+ -[APTNANPairingDelegate handlePairingRequestOfType:withInputCompletionHandler:]
+ -[APTNANPairingDelegate handlePairingRequestOfType:withInputCompletionHandler:].cold.1
+ -[APTNANPairingDelegate handlePairingRequestOfType:withInputCompletionHandler:].cold.2
+ -[APTNANPairingDelegate handledPairingRequest]
+ -[APTNANPairingDelegate initWithHandleAuthorizationRequestBlock:]
+ -[APTNANPairingDelegate initWithHandleAuthorizationRequestBlock:].cold.1
+ -[APTNANPairingDelegate initWithHandleAuthorizationRequestBlock:].cold.2
+ -[APTNANPairingDelegate pairingRequestStartedForDataSession:passphraseInputCompletionHandler:]
+ -[APTNANPairingDelegate pairingRequestStartedForDataSession:pinCodeInputCompletionHandler:]
+ -[APTNANPairingDelegate setHandledPairingRequest:]
+ GCC_except_table10
+ GCC_except_table17
+ GCC_except_table44
+ GCC_except_table51
+ GCC_except_table6
+ GCC_except_table95
+ _APAdvertiserInfoCopyAirPlayDataWithNANServiceType.cold.41
+ _APAdvertiserInfoCopyAirPlayP2PDataWithNANServiceType.cold.6
+ _APAdvertiserInfoCopyAirPlayP2PDataWithNANServiceType.cold.7
+ _APAdvertiserInfoCreateAPSFeaturesFromTXTRecordEx.cold.1
+ _APAdvertiserInfoCreateAPSFeaturesFromTXTRecordEx.cold.2
+ _APAdvertiserInfoCreateAPSFeaturesFromTXTRecordEx.cold.3
+ _APAdvertiserInfoCreateWithDeviceTXTRecordDataAndDeviceName
+ _APAdvertiserInfoCreateWithDeviceTXTRecordDataAndDeviceName.cold.1
+ _APAdvertiserInfoCreateWithDeviceTXTRecordDataAndDeviceName.cold.10
+ _APAdvertiserInfoCreateWithDeviceTXTRecordDataAndDeviceName.cold.11
+ _APAdvertiserInfoCreateWithDeviceTXTRecordDataAndDeviceName.cold.2
+ _APAdvertiserInfoCreateWithDeviceTXTRecordDataAndDeviceName.cold.3
+ _APAdvertiserInfoCreateWithDeviceTXTRecordDataAndDeviceName.cold.4
+ _APAdvertiserInfoCreateWithDeviceTXTRecordDataAndDeviceName.cold.5
+ _APAdvertiserInfoCreateWithDeviceTXTRecordDataAndDeviceName.cold.6
+ _APAdvertiserInfoCreateWithDeviceTXTRecordDataAndDeviceName.cold.7
+ _APAdvertiserInfoCreateWithDeviceTXTRecordDataAndDeviceName.cold.8
+ _APAdvertiserInfoCreateWithDeviceTXTRecordDataAndDeviceName.cold.9
+ _APBrowserCopyAirPlayBonjourInfo
+ _APBrowserCreateAdvertiserInfoForDevice.cold.6
+ _APBrowserCreateAdvertiserInfoForDevice.cold.7
+ _APBrowserDeepCopyPlistAtKeyPath
+ _APSBinaryTXTRecordCopyString
+ _APSDataPacerGetTypeID
+ _APSEventRecorderGetTimeFromDictionaryIfPresent
+ _APSEventRecorderSetTimeInDictionary
+ _APSGetCurrentLocalTimeString
+ _APSIsOpenNANSenderEnabled
+ _APSSettingsGetDouble
+ _APSTXTRecordUtilsCopyCFStringFromTXTRecord
+ _APSTXTRecordUtilsGetBooleanFromTXTRecord
+ _APSTXTRecordUtilsGetInt64FromTXTRecord
+ _APTPacingControllerAddBytesSent
+ _APTPacingControllerAddBytesSent.cold.1
+ _APTPacingControllerCreate
+ _APTPacingControllerCreate.cold.1
+ _APTPacingControllerCreate.cold.2
+ _APTPacingControllerCreate.cold.3
+ _APTPacingControllerCreate.cold.4
+ _APTPacingControllerCreate.cold.5
+ _APTPacingControllerCreate.cold.6
+ _APTPacingControllerCreate.cold.7
+ _APTPacingControllerGetTypeID
+ _APTPacingControllerGetTypeID.cold.1
+ _APTPacingControllerReset
+ _APTPacingControllerReset.cold.1
+ _APTPacingControllerReset.cold.2
+ _APTPacingControllerSetMaxPacingRate
+ _APTPacingControllerYieldOnQueueWithContinuationBlock
+ _APTPacingControllerYieldOnQueueWithContinuationBlock.cold.1
+ _APTPacingControllerYieldOnQueueWithContinuationBlock.cold.2
+ _APTPacingControllerYieldOnQueueWithContinuationFunction
+ _APTPacingControllerYieldOnQueueWithContinuationFunction.cold.1
+ _APTransportConnectionUnbufferedNWCreate
+ _APTransportConnectionUnbufferedNWCreate.cold.1
+ _APTransportConnectionUnbufferedNWCreate.cold.10
+ _APTransportConnectionUnbufferedNWCreate.cold.11
+ _APTransportConnectionUnbufferedNWCreate.cold.12
+ _APTransportConnectionUnbufferedNWCreate.cold.13
+ _APTransportConnectionUnbufferedNWCreate.cold.14
+ _APTransportConnectionUnbufferedNWCreate.cold.15
+ _APTransportConnectionUnbufferedNWCreate.cold.2
+ _APTransportConnectionUnbufferedNWCreate.cold.3
+ _APTransportConnectionUnbufferedNWCreate.cold.4
+ _APTransportConnectionUnbufferedNWCreate.cold.5
+ _APTransportConnectionUnbufferedNWCreate.cold.6
+ _APTransportConnectionUnbufferedNWCreate.cold.7
+ _APTransportConnectionUnbufferedNWCreate.cold.8
+ _APTransportConnectionUnbufferedNWCreate.cold.9
+ _APTransportDeviceCopyInfo
+ _APTransportDeviceCopyInfo.cold.1
+ _APTransportDeviceCopyInfo.cold.2
+ _APTransportDeviceCopyInfo.cold.3
+ _APTransportDeviceCreateWithNetworkAddresses
+ _APTransportDeviceCreateWithNetworkAddresses.cold.1
+ _APTransportDeviceCreateWithNetworkAddresses.cold.2
+ _APTransportDeviceCreateWithNetworkAddresses.cold.3
+ _APTransportDeviceCreateWithNetworkAddresses.cold.4
+ _APTransportPackageDatagramCreate
+ _APTransportPackageDatagramCreateWithBBuf
+ _APTransportPackageDatagramCreateWithBBuf.cold.1
+ _APTransportPackageDatagramCreateWithBBuf.cold.2
+ _APTransportPackageSetArrivalTicks
+ _CFAllocatorAllocateTyped
+ _CFArrayCreateCopy
+ _CFGetCString
+ _CFPropertyListCreateDeepCopy
+ _CFPropertyListIsValid
+ _CMBaseObjectCopyProperty
+ _CMBaseObjectSetProperty
+ _CMRemoveAttachment
+ _FigCFArrayApplyBlock
+ _FigCFDictionaryGetValue
+ _FigCFDictionarySetUInt32
+ _HTTPMessageSetClientMessageType
+ _HomeKitLibrary
+ _HomeKitLibrary.cold.1
+ _HomeKitLibraryCore.frameworkLibrary
+ _IPv6AddressToCString
+ _NSStringFromClass
+ _NanosecondsToUpTicks
+ _OBJC_CLASS_$_APBonjourCacheEvictionTTL
+ _OBJC_CLASS_$_APBonjourCacheHomeKit
+ _OBJC_CLASS_$_APHomeKitDeviceMonitor
+ _OBJC_CLASS_$_APTNANPairingDelegate
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_NSSet
+ _OBJC_IVAR_$_APBonjourCacheEvictionTTL._timeToLiveSeconds
+ _OBJC_IVAR_$_APBonjourCacheHomeKit._activatedPresentDeviceStashing
+ _OBJC_IVAR_$_APBonjourCacheHomeKit._cache
+ _OBJC_IVAR_$_APBonjourCacheHomeKit._cachedDeviceFoundHandler
+ _OBJC_IVAR_$_APBonjourCacheHomeKit._cachedDeviceLostHandler
+ _OBJC_IVAR_$_APBonjourCacheHomeKit._currentNetworkSignature
+ _OBJC_IVAR_$_APBonjourCacheHomeKit._dispatchQueue
+ _OBJC_IVAR_$_APBonjourCacheHomeKit._evictionPolicies
+ _OBJC_IVAR_$_APBonjourCacheHomeKit._expectedDeviceIDs
+ _OBJC_IVAR_$_APBonjourCacheHomeKit._homeKitDeviceMonitor
+ _OBJC_IVAR_$_APBonjourCacheHomeKit._internalQueue
+ _OBJC_IVAR_$_APBonjourCacheHomeKit._invalidated
+ _OBJC_IVAR_$_APBonjourCacheHomeKit._presentRealDevices
+ _OBJC_IVAR_$_APBonjourCacheHomeKit._reportedCachedDeviceIDs
+ _OBJC_IVAR_$_APBonjourCacheHomeKit._systemMonitor
+ _OBJC_IVAR_$_APBonjourCacheHomeKit._usePresentDeviceStashing
+ _OBJC_IVAR_$_APBonjourCacheHomeKit._useStrictNetworkSignatureMatching
+ _OBJC_IVAR_$_APHomeKitDeviceMonitor._dispatchQueue
+ _OBJC_IVAR_$_APHomeKitDeviceMonitor._homeAccessories
+ _OBJC_IVAR_$_APHomeKitDeviceMonitor._homeConfigurationDidChangeHandler
+ _OBJC_IVAR_$_APHomeKitDeviceMonitor._homeManager
+ _OBJC_IVAR_$_APHomeKitDeviceMonitor._internalQueue
+ _OBJC_IVAR_$_APHomeKitDeviceMonitor._invalidated
+ _OBJC_IVAR_$_APTNANPairingDelegate._handleAuthorizationRequestBlock
+ _OBJC_IVAR_$_APTNANPairingDelegate._handledPairingRequest
+ _OBJC_METACLASS_$_APBonjourCacheEvictionTTL
+ _OBJC_METACLASS_$_APBonjourCacheHomeKit
+ _OBJC_METACLASS_$_APHomeKitDeviceMonitor
+ _OBJC_METACLASS_$_APTNANPairingDelegate
+ _OUTLINED_FUNCTION_22
+ _SockAddrCompareAddr
+ _TXTRecordContainsKey
+ __APAdvertiserInfoAddAirPlayData
+ __APAdvertiserInfoAddAirPlayData.cold.1
+ __APAdvertiserInfoAddAirPlayData.cold.2
+ __APBonjourBrowserHandleAirPlayNANEvent
+ __APBonjourBrowserHandleDeviceEventForAirPlayNANService
+ __APBonjourBrowserStopBrowsingOpenNAN
+ __APBonjourBrowserStopBrowsingOpenNAN.cold.1
+ __APBonjourBrowserStopBrowsingSecureNANPartial
+ __APBonjourBrowserStopBrowsingSecureNANPartial.cold.1
+ __APTNANDataSessionGenerateDiversifiedPIN
+ __APTNANDataSessionGenerateDiversifiedPIN.cold.1
+ __APTNANDataSessionSetProperty
+ __APTNANDataSessionSetProperty.cold.1
+ __APTNANDataSessionSetProperty.cold.2
+ __APTNANDataSessionSetProperty.cold.3
+ __APTNANDataSessionSetProperty.cold.4
+ __APTNANDataSessionSetProperty.cold.5
+ __APTNANDataSessionSetProperty.cold.6
+ __APTPacingControllerFinalize
+ __APTPacingControllerFinalize.cold.1
+ __APTPacingControllerGetTypeID
+ __APTransportConnectionUnbufferedNWGutsFinalize
+ __APTransportConnectionUnbufferedNWGutsFinalize.cold.1
+ __APTransportConnectionUnbufferedNWGutsGetTypeID
+ __OBJC_$_CLASS_METHODS_APBonjourCacheHomeKit
+ __OBJC_$_INSTANCE_METHODS_APBonjourCacheEvictionTTL
+ __OBJC_$_INSTANCE_METHODS_APBonjourCacheHomeKit(Introspector)
+ __OBJC_$_INSTANCE_METHODS_APHomeKitDeviceMonitor
+ __OBJC_$_INSTANCE_METHODS_APTNANPairingDelegate
+ __OBJC_$_INSTANCE_VARIABLES_APBonjourCacheEvictionTTL
+ __OBJC_$_INSTANCE_VARIABLES_APBonjourCacheHomeKit
+ __OBJC_$_INSTANCE_VARIABLES_APHomeKitDeviceMonitor
+ __OBJC_$_INSTANCE_VARIABLES_APTNANPairingDelegate
+ __OBJC_$_PROP_LIST_APBonjourCacheEvictionTTL
+ __OBJC_$_PROP_LIST_APBonjourCacheHomeKit
+ __OBJC_$_PROP_LIST_APHomeKitDeviceMonitor
+ __OBJC_$_PROP_LIST_APTNANPairingDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_APBonjourCacheEvictionPolicy
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMAccessoryDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMHomeDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMHomeManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WiFiAwareDataSessionPairingDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_APBonjourCacheEvictionPolicy
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMAccessoryDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMHomeDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMHomeManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WiFiAwareDataSessionPairingDelegate
+ __OBJC_$_PROTOCOL_REFS_APBonjourCacheEvictionPolicy
+ __OBJC_$_PROTOCOL_REFS_HMAccessoryDelegate
+ __OBJC_$_PROTOCOL_REFS_HMHomeDelegate
+ __OBJC_$_PROTOCOL_REFS_HMHomeManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_WiFiAwareDataSessionPairingDelegate
+ __OBJC_CLASS_PROTOCOLS_$_APBonjourCacheEvictionTTL
+ __OBJC_CLASS_PROTOCOLS_$_APHomeKitDeviceMonitor
+ __OBJC_CLASS_PROTOCOLS_$_APTNANPairingDelegate
+ __OBJC_CLASS_RO_$_APBonjourCacheEvictionTTL
+ __OBJC_CLASS_RO_$_APBonjourCacheHomeKit
+ __OBJC_CLASS_RO_$_APHomeKitDeviceMonitor
+ __OBJC_CLASS_RO_$_APTNANPairingDelegate
+ __OBJC_LABEL_PROTOCOL_$_APBonjourCacheEvictionPolicy
+ __OBJC_LABEL_PROTOCOL_$_HMAccessoryDelegate
+ __OBJC_LABEL_PROTOCOL_$_HMHomeDelegate
+ __OBJC_LABEL_PROTOCOL_$_HMHomeManagerDelegate
+ __OBJC_LABEL_PROTOCOL_$_WiFiAwareDataSessionPairingDelegate
+ __OBJC_METACLASS_RO_$_APBonjourCacheEvictionTTL
+ __OBJC_METACLASS_RO_$_APBonjourCacheHomeKit
+ __OBJC_METACLASS_RO_$_APHomeKitDeviceMonitor
+ __OBJC_METACLASS_RO_$_APTNANPairingDelegate
+ __OBJC_PROTOCOL_$_APBonjourCacheEvictionPolicy
+ __OBJC_PROTOCOL_$_HMAccessoryDelegate
+ __OBJC_PROTOCOL_$_HMHomeDelegate
+ __OBJC_PROTOCOL_$_HMHomeManagerDelegate
+ __OBJC_PROTOCOL_$_WiFiAwareDataSessionPairingDelegate
+ ___35-[APBonjourCacheHomeKit invalidate]_block_invoke
+ ___36-[APHomeKitDeviceMonitor invalidate]_block_invoke
+ ___40-[APBonjourCacheHomeKit realDeviceLost:]_block_invoke
+ ___41-[APBonjourCacheHomeKit realDeviceFound:]_block_invoke
+ ___42-[APHomeKitDeviceMonitor homeKitDeviceIDs]_block_invoke
+ ___43+[APBonjourCacheHomeKit prepareDeviceInfo:]_block_invoke
+ ___47-[APBonjourCacheHomeKit availableCachedDevices]_block_invoke
+ ___47-[APHomeKitDeviceMonitor home:didAddAccessory:]_block_invoke
+ ___48-[APBonjourCacheHomeKit activateWithCompletion:]_block_invoke
+ ___49-[APBonjourCacheHomeKit evictCachedDeviceWithID:]_block_invoke
+ ___49-[APHomeKitDeviceMonitor accessoryDidUpdateName:]_block_invoke
+ ___49-[APHomeKitDeviceMonitor activateWithCompletion:]_block_invoke
+ ___49-[APHomeKitDeviceMonitor homeManager:didAddHome:]_block_invoke
+ ___50-[APHomeKitDeviceMonitor home:didRemoveAccessory:]_block_invoke
+ ___52-[APHomeKitDeviceMonitor homeManager:didRemoveHome:]_block_invoke
+ ___52-[APHomeKitDeviceMonitor homeManagerDidUpdateHomes:]_block_invoke
+ ___53-[APBonjourCacheHomeKit shouldProcessDeviceForCache:]_block_invoke
+ ___54-[APBonjourCacheHomeKit(Introspector) copyDescription]_block_invoke
+ ___56-[APBonjourCacheHomeKit activateWithCompletionInternal:]_block_invoke
+ ___56-[APBonjourCacheHomeKit activateWithCompletionInternal:]_block_invoke_2
+ ___56-[APBonjourCacheHomeKit activateWithCompletionInternal:]_block_invoke_3
+ ___56-[APBonjourCacheHomeKit activateWithCompletionInternal:]_block_invoke_4
+ ___56-[APBonjourCacheHomeKit activateWithCompletionInternal:]_block_invoke_5
+ ___57-[APHomeKitDeviceMonitor activateWithCompletionInternal:]_block_invoke
+ ___59-[APHomeKitDeviceMonitor handleHomeKitAccessoriesDidChange]_block_invoke
+ ___62-[APBonjourCacheHomeKit handleRealDeviceFoundForCachedDevice:]_block_invoke
+ ___62-[APBonjourCacheHomeKit reportCachedDevice:found:withHandler:]_block_invoke
+ ___62-[APBonjourCacheHomeKit(Introspector) copyDescriptionInternal]_block_invoke
+ ___APBrowserCopyAirPlayBonjourInfo_block_invoke
+ ___HomeKitLibraryCore_block_invoke
+ ___NSArray0__struct
+ ____APTNANDataSessionGenerateDiversifiedPIN_block_invoke
+ ___block_descriptor_32_e11_q24?0816l
+ ___block_descriptor_36_e39_B24?0"NSDictionary"8"NSDictionary"16l
+ ___block_descriptor_48_e8_32o40b_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32o40b_e5_v8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32o40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_64_e8_32o40r48r_e21_v24?0q8"NSString"16lr40l8r48l8s32l8
+ ___block_descriptor_64_e8_32r40r48r_e5_v8?0lr32l8r40l8r48l8
+ ___block_descriptor_69_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_80_e8_32o40o48o56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_80_e8_32r40r_e10_v16?0r^v8lr32l8r40l8
+ ___block_descriptor_tmp.107
+ ___block_descriptor_tmp.108
+ ___block_descriptor_tmp.125
+ ___block_descriptor_tmp.132
+ ___block_descriptor_tmp.139
+ ___block_descriptor_tmp.140
+ ___block_descriptor_tmp.150
+ ___block_descriptor_tmp.155
+ ___block_descriptor_tmp.167
+ ___block_descriptor_tmp.182
+ ___block_descriptor_tmp.228
+ ___block_descriptor_tmp.232
+ ___block_descriptor_tmp.48
+ ___block_descriptor_tmp.62
+ ___block_descriptor_tmp.63
+ ___block_descriptor_tmp.74
+ ___block_descriptor_tmp.83
+ ___block_descriptor_tmp.86
+ ___block_literal_global.173
+ ___block_literal_global.230
+ ___block_literal_global.234
+ ___block_literal_global.339
+ ___bonjourCacheHomeKit_introspector_cmd_applyEvictions_block_invoke
+ ___bonjourCacheHomeKit_introspector_cmd_purgeCache_block_invoke
+ ___bonjourCacheHomeKit_introspector_cmd_purgeCache_block_invoke.cold.1
+ ___browser_CopyNANEndpointForDeviceID_block_invoke
+ ___browser_handleBTLEQueryEventExternal_block_invoke.cold.12
+ ___browser_handleBTLEQueryEventExternal_block_invoke.cold.13
+ ___browser_removeP2PServicesForNearbyDevices_block_invoke
+ ___getHMHomeManagerClass_block_invoke
+ ___getHMHomeManagerClass_block_invoke.cold.1
+ ___getHMMutableHomeManagerConfigurationClass_block_invoke
+ ___getHMMutableHomeManagerConfigurationClass_block_invoke.cold.1
+ ___stream_handleEventFromSendConnection_block_invoke.cold.3
+ ___transportDevice_networkAddressesToCStringRepresentation_block_invoke
+ ___unbufnwGuts_connectionHandlePackageHeader_block_invoke
+ ___unbufnwGuts_connectionHandlePackagePayload_block_invoke
+ ___unbufnwGuts_connectionReceivePackages_block_invoke
+ ___unbufnwGuts_connectionReceivePackages_block_invoke_2
+ ___unbufnwGuts_connectionSendPackages_block_invoke
+ ___unbufnwGuts_connectionSendPackages_block_invoke_2
+ ___unbufnwGuts_connectionStateChangedHandler_block_invoke
+ ___unbufnwGuts_drainEventQueueAsyncOnCallbackQueue_block_invoke
+ ___unbufnwGuts_drainEventQueueAsyncOnCallbackQueue_block_invoke_2
+ ___unbufnwGuts_handleNewConnectionGroupInternal_block_invoke
+ ___unbufnwGuts_handleNewConnectionGroupInternal_block_invoke_2
+ ___unbufnwGuts_handleNewConnectionInternal_block_invoke
+ ___unbufnwGuts_updatePackageTrackingInternal_block_invoke
+ ___unbufnw_Resume_block_invoke
+ ___unbufnw_Resume_block_invoke_2
+ ___unbufnw_Resume_block_invoke_2.cold.1
+ ___unbufnw_Resume_block_invoke_2.cold.2
+ ___unbufnw_Resume_block_invoke_2.cold.3
+ ___unbufnw_Resume_block_invoke_3
+ ___unbufnw_Resume_block_invoke_4
+ ___unbufnw_Resume_block_invoke_4.cold.1
+ ___unbufnw_Resume_block_invoke_5
+ ___unbufnw_SetProperty_block_invoke
+ ___unbufnw_SignalDataAvailable_block_invoke
+ _audit_stringHomeKit
+ _bonjourCacheHomeKit_introspector_cmd_applyEvictions
+ _bonjourCacheHomeKit_introspector_cmd_purgeCache
+ _bonjourCacheHomeKit_introspector_cmd_showInfo
+ _browser_appendFormattedDuration
+ _browser_cfstringToSockAddr
+ _browser_cfstringToSockAddr.cold.1
+ _browser_cfstringToSockAddr.cold.2
+ _browser_copyNANEndpointForOneDeviceID
+ _browser_copyNANEndpointForOneDeviceID.cold.1
+ _browser_copyNANEndpointForOneDeviceID.cold.2
+ _browser_copyNANEndpointForOneDeviceID.cold.3
+ _browser_copyNANEndpointForOneDeviceID.cold.4
+ _browser_createBonjourInfoForBTLEDevice.cold.13
+ _browser_createBonjourInfoForBTLEDevice.cold.14
+ _browser_removeP2PServicesForNearbyDevices
+ _browser_shouldQueryIPAddress
+ _browser_shouldQueryIPAddress.cold.1
+ _carPlayHelperSession_updateNetworkAndSessionState.cold.12
+ _carPlayHelperSession_usbInterfaceListeningStopped
+ _carPlayHelperSession_usbInterfaceListeningStopped.cold.1
+ _carPlayHelperSession_wifiNetworkListeningStopped
+ _carPlayHelperSession_wifiNetworkListeningStopped.cold.1
+ _datagramPackage_CopyDebugDescription
+ _datagramPackage_CopyDebugDescription.cold.1
+ _datagramPackage_CopyMessageData
+ _datagramPackage_CreateBBufRepresentation
+ _datagramPackage_CreateBBufRepresentation.cold.1
+ _datagramPackage_CreateBBufRepresentation.cold.2
+ _datagramPackage_Finalize
+ _datagramPackage_GetArrivalTicks
+ _datagramPackage_GetMessageType
+ _datagramPackage_SetArrivalTicks
+ _datagramPackage_SetMessageData
+ _datagramPackage_SetMessageType
+ _datagramPackage_updateMessageDataArrivalTicks
+ _dispatch_data_create_subrange
+ _dispatch_time_from_nsec
+ _dispatch_time_to_nsec
+ _gAPTPacingControllerInitOnce
+ _gAPTPacingControllerTypeID
+ _gAPTransportConnectionUnbufferedNWGutsInitOnce
+ _gAPTransportConnectionUnbufferedNWGutsTypeID
+ _gLogCategory_APBonjourCacheHomeKit
+ _gLogCategory_APHomeKitDeviceMonitor
+ _gLogCategory_APTPacingController
+ _gLogCategory_APTransportConnectionUnbufferedNW
+ _getHMHomeManagerClass.softClass
+ _getHMMutableHomeManagerConfigurationClass.softClass
+ _httpPackage_computeMessageTypeString
+ _kAPAdvertiserInfoProperty_CorrelationID
+ _kAPAdvertiserInfoProperty_NANServiceType
+ _kAPBonjourBrowserCreationOption_OpenNANAllowed
+ _kAPBonjourBrowserServiceType_AirPlayNAN
+ _kAPBonjourBrowserServiceType_AirPlayNANFull
+ _kAPBonjourBrowserServiceType_AirPlayNANPartial
+ _kAPBrowserCreationOption_OpenNANAllowed
+ _kAPSDataPacerNotification_PacedRateChanged
+ _kAPSTransportMessageAttachmentKey_ArrivalTicks
+ _kAPTNANDataSessionProperty_AuthorizationType
+ _kAPTNANDataSessionProperty_HandleAuthorizationRequestBlock
+ _kAPTNANDataSessionProperty_SetAuthorizationStringBlock
+ _kAPTPacingControllerClass
+ _kAPTransportAuthorizationType_PIN
+ _kAPTransportAuthorizationType_Password
+ _kAPTransportConnectionOption_IsPackageArrivalTicksEnabled
+ _kAPTransportConnectionOption_TransportProtocol
+ _kAPTransportConnectionPackageType_Datagram
+ _kAPTransportConnectionProperty_DataPacer
+ _kAPTransportConnectionProperty_TimingInformation
+ _kAPTransportConnectionTimingInformationKey_NetworkingMs
+ _kAPTransportConnectionTimingInformationKey_ReceiverMessageProcessingMs
+ _kAPTransportConnectionTimingInformationKey_TotalMessageTimeMs
+ _kAPTransportConnectionTimingInformationKey_UnspecifiedRemoteTimeMs
+ _kAPTransportConnectionUnbufNW_EndpointHierarchyProtocol
+ _kAPTransportConnectionUnbufNW_EndpointHierarchyProtocolVTable
+ _kAPTransportConnectionUnbufNW_baseProtocol
+ _kAPTransportConnectionUnbufNW_protocolEntries
+ _kAPTransportConnectionUnbufNW_protocolTable
+ _kAPTransportConnectionUnbufferedNWGutsClass
+ _kAPTransportConnectionUnbufferedNWVTable
+ _kAPTransportConnectionUnbufferedNW_BaseClassWrapper
+ _kAPTransportConnectionUnbufferedNW_Class
+ _kAPTransportSessionOption_HandleNANAuthorizationRequestBlock
+ _kAPTransportSessionOption_NANAuthorizationType
+ _kAPTransportSessionOption_SetNANAuthorizationStringBlock
+ _kAPTransportSessionStreamOption_TransportProtocol
+ _kAPTransportStreamProperty_DataPacer
+ _kAPTransportStreamProperty_TimingInformation
+ _mach_get_times
+ _nw_content_context_copy_protocol_metadata
+ _nw_ip_metadata_get_receive_time
+ _nw_ip_options_set_calculate_receive_time
+ _nw_ip_options_set_disable_fragmentation
+ _nw_parameters_copy_local_address
+ _nw_protocol_copy_ip_definition
+ _nw_protocol_copy_quic_definition
+ _nw_protocol_copy_udp_definition
+ _nw_protocol_stack_copy_internet_protocol
+ _nw_tcp_set_max_pacing_rate
+ _objc_msgSend$URLByDeletingLastPathComponent
+ _objc_msgSend$accessories
+ _objc_msgSend$activateWithCompletionInternal:
+ _objc_msgSend$activatedPresentDeviceStashing
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$airplayTargetIPv6
+ _objc_msgSend$allKeys
+ _objc_msgSend$allObjects
+ _objc_msgSend$array
+ _objc_msgSend$bytes
+ _objc_msgSend$cache
+ _objc_msgSend$cacheDevice:
+ _objc_msgSend$cachedDeviceFoundHandler
+ _objc_msgSend$cachedDeviceLostHandler
+ _objc_msgSend$cachedDevices
+ _objc_msgSend$checkAndEvictCachedDevicesIfNecessary
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$copyDescription
+ _objc_msgSend$copyDescriptionInternal
+ _objc_msgSend$currentHome
+ _objc_msgSend$currentNetworkSignature
+ _objc_msgSend$data
+ _objc_msgSend$dateWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$debugDescription
+ _objc_msgSend$describeBonjourInfo:
+ _objc_msgSend$description
+ _objc_msgSend$dictionary
+ _objc_msgSend$dictionaryWithContentsOfURL:
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$evictCachedDeviceWithIDInternal:
+ _objc_msgSend$evictionPolicies
+ _objc_msgSend$expectedDeviceIDs
+ _objc_msgSend$filterUsingPredicate:
+ _objc_msgSend$forceReportCachedDevicesFound
+ _objc_msgSend$forceReportCachedDevicesLost
+ _objc_msgSend$fullRefresh
+ _objc_msgSend$generateDiversifiedPINWithCompletionHandler:
+ _objc_msgSend$getCString:maxLength:encoding:
+ _objc_msgSend$getCacheDirectoryURLWithParentDirectory:creatingIfNecessary:
+ _objc_msgSend$getCacheFileURLCreatingParentDirectoriesIfNecessary:
+ _objc_msgSend$getDeviceID:
+ _objc_msgSend$getReportableCachedDevices
+ _objc_msgSend$handleHomeKitAccessoriesDidChange
+ _objc_msgSend$handleHomeKitDeviceConfigurationChanged:
+ _objc_msgSend$handleNetworkSignatureChanged:
+ _objc_msgSend$handlePairingRequestOfType:withInputCompletionHandler:
+ _objc_msgSend$handleRealDeviceFoundForCachedDevice:
+ _objc_msgSend$handleRealDeviceLostForCachedDevice:
+ _objc_msgSend$handledPairingRequest
+ _objc_msgSend$hash
+ _objc_msgSend$home
+ _objc_msgSend$homeAccessories
+ _objc_msgSend$homeConfigurationDidChangeHandler
+ _objc_msgSend$homeKitDeviceIDs
+ _objc_msgSend$homeKitDeviceMonitor
+ _objc_msgSend$homeManager
+ _objc_msgSend$homes
+ _objc_msgSend$initWithConfiguration:
+ _objc_msgSend$initWithHandleAuthorizationRequestBlock:
+ _objc_msgSend$initWithOptions:cachePolicy:
+ _objc_msgSend$initWithSet:
+ _objc_msgSend$internalQueue
+ _objc_msgSend$invalidateInternal
+ _objc_msgSend$invalidated
+ _objc_msgSend$isDeviceCacheable:
+ _objc_msgSend$isEqualToDictionary:
+ _objc_msgSend$isRemoteDeviceConnected
+ _objc_msgSend$isValidNetworkSignature:
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$loadCache
+ _objc_msgSend$localDataAddress
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$prepareDeviceInfo:
+ _objc_msgSend$presentRealDevices
+ _objc_msgSend$realDeviceFoundInternal:
+ _objc_msgSend$realDeviceLostInternal:
+ _objc_msgSend$refreshWithAccessory:isAddOrUpdate:notifyOnAccessoryChange:
+ _objc_msgSend$refreshWithHome:isAddOrUpdate:notifyOnAccessoriesChanged:
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$reportCachedDevice:found:withHandler:
+ _objc_msgSend$reportedCachedDeviceIDs
+ _objc_msgSend$set
+ _objc_msgSend$setActivatedPresentDeviceStashing:
+ _objc_msgSend$setCache:
+ _objc_msgSend$setCachedDeviceFoundHandler:
+ _objc_msgSend$setCachedDeviceLostHandler:
+ _objc_msgSend$setCurrentNetworkSignature:
+ _objc_msgSend$setEvictionPolicies:
+ _objc_msgSend$setExpectedDeviceIDs:
+ _objc_msgSend$setHomeAccessories:
+ _objc_msgSend$setHomeConfigurationDidChangeHandler:
+ _objc_msgSend$setHomeKitDeviceMonitor:
+ _objc_msgSend$setHomeManager:
+ _objc_msgSend$setInactiveUpdatingLevel:
+ _objc_msgSend$setInternalQueue:
+ _objc_msgSend$setInvalidated:
+ _objc_msgSend$setPresentRealDevices:
+ _objc_msgSend$setReportedCachedDeviceIDs:
+ _objc_msgSend$setSystemMonitor:
+ _objc_msgSend$setTimeToLiveSeconds:
+ _objc_msgSend$setUsePresentDeviceStashing:
+ _objc_msgSend$setWfaPairingCacheEnabled:
+ _objc_msgSend$setWfaPairingDelegate:
+ _objc_msgSend$setWfaPairingMethod:
+ _objc_msgSend$setupEvictionPolicies
+ _objc_msgSend$setupIntrospector
+ _objc_msgSend$shouldEvict:
+ _objc_msgSend$shouldEvictDevice:policy:
+ _objc_msgSend$shouldProcessDeviceForCache:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$standardizedURL
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$systemMonitor
+ _objc_msgSend$timeToLiveSeconds
+ _objc_msgSend$uncacheDevice:
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$updateExpectedDeviceIDsAdding:removing:
+ _objc_msgSend$usePresentDeviceStashing
+ _objc_msgSend$useStrictNetworkSignatureMatching
+ _objc_msgSend$writeCache
+ _objc_msgSend$writeToURL:atomically:
+ _pacingController_endYieldInternal
+ _pacingController_runAndReleaseBlock
+ _pacingController_updateYieldTimerIfNeededAsync
+ _pacingController_updateYieldTimerIfNeededAsync.cold.1
+ _pacingController_updateYieldTimerIfNeededAsync.cold.2
+ _pacingController_yieldTimerFire
+ _session_activateNANDS
+ _session_activateNANDS.cold.1
+ _shouldProcessDeviceForCache:.onceToken
+ _shouldProcessDeviceForCache:.prefOverride
+ _transportDevice_Equal
+ _transportDevice_Hash
+ _transportDevice_getNANDataSessionForAddressType
+ _transportDevice_getNANDataSessionForAddressType.cold.1
+ _udpconnection_setPropertyInternal.cold.10
+ _unbufnwGuts_callEventCallbackInternal
+ _unbufnwGuts_connectionHandlePackageHeader
+ _unbufnwGuts_connectionHandlePackageHeader.cold.1
+ _unbufnwGuts_connectionHandlePackageHeader.cold.2
+ _unbufnwGuts_connectionHandlePackageHeader.cold.3
+ _unbufnwGuts_connectionHandlePackageHeader.cold.4
+ _unbufnwGuts_connectionHandlePackageHeader.cold.5
+ _unbufnwGuts_connectionHandlePackagePayload
+ _unbufnwGuts_connectionHandlePotentialDisconnect
+ _unbufnwGuts_connectionReceivePackages
+ _unbufnwGuts_connectionSendPackages
+ _unbufnwGuts_connectionSendPackagesYieldContinuation
+ _unbufnwGuts_drainEventQueueAsyncOnCallbackQueue
+ _unbufnwGuts_handleDataPacingRateDidChange
+ _unbufnwGuts_handleNewConnectionInternal
+ _unbufnwGuts_handleNewConnectionInternal.cold.1
+ _unbufnwGuts_invalidate
+ _unbufnwGuts_invalidateInternal
+ _unbufnwGuts_readyToSendBatchSlow
+ _unbufnwGuts_setEventCallback
+ _unbufnwGuts_updateDataPacingInternal
+ _unbufnwGuts_updatePackageTrackingInternal
+ _unbufnwGuts_updateStatus
+ _unbufnwGuts_updateStatusInternal
+ _unbufnwTrackingWindowItem_Copy
+ _unbufnwTrackingWindowItem_Free
+ _unbufnw_AddEventCallback
+ _unbufnw_AddEventCallback.cold.1
+ _unbufnw_AddEventCallback.cold.2
+ _unbufnw_CopyProperty
+ _unbufnw_DumpHierarchy
+ _unbufnw_Finalize
+ _unbufnw_Invalidate
+ _unbufnw_RemoveEventCallback
+ _unbufnw_RemoveEventCallback.cold.1
+ _unbufnw_Resume
+ _unbufnw_SetProperty
+ _unbufnw_SetReadyToSendBatchCallback
+ _unbufnw_SetReadyToSendCallback
+ _unbufnw_SignalDataAvailable
- -[APDBrowserBluetoothHelper bluetoothPowerChangedListeningStarted]
- -[APDBrowserBluetoothHelper dealloc]
- -[APDBrowserBluetoothHelper dispatchEvent:withEventInfo:]
- -[APDBrowserBluetoothHelper ensureBluetoothPowerChangedListenerStopped]
- -[APDBrowserBluetoothHelper ensureBluetoothPowerEventMonitorStarted]
- -[APDBrowserBluetoothHelper eventHandlerContext]
- -[APDBrowserBluetoothHelper eventHandlerFunc]
- -[APDBrowserBluetoothHelper eventQueue]
- -[APDBrowserBluetoothHelper getBluetoothPowerOn:]
- -[APDBrowserBluetoothHelper getBluetoothPowerOn:].cold.1
- -[APDBrowserBluetoothHelper getEventString:]
- -[APDBrowserBluetoothHelper handleBluetoothChangedNotificationInternal:]
- -[APDBrowserBluetoothHelper helperRef]
- -[APDBrowserBluetoothHelper init]
- -[APDBrowserBluetoothHelper init].cold.1
- -[APDBrowserBluetoothHelper init].cold.2
- -[APDBrowserBluetoothHelper invalidate]
- -[APDBrowserBluetoothHelper isInvalidated]
- -[APDBrowserBluetoothHelper queryBluetoothPower:]
- -[APDBrowserBluetoothHelper queryBluetoothPower:].cold.1
- -[APDBrowserBluetoothHelper queue]
- -[APDBrowserBluetoothHelper setBluetoothPower:]
- -[APDBrowserBluetoothHelper setBluetoothPowerChangedListeningStarted:]
- -[APDBrowserBluetoothHelper setEventHandler:context:helperRef:]
- -[APDBrowserBluetoothHelper setEventHandlerContext:]
- -[APDBrowserBluetoothHelper setEventHandlerFunc:]
- -[APDBrowserBluetoothHelper setHelperRef:]
- -[APDBrowserBluetoothHelper setIsInvalidated:]
- -[APDBrowserBluetoothHelper setPowered:]
- -[APDBrowserBluetoothHelper startListeningToEvent:]
- -[APDBrowserBluetoothHelper startListeningToEvent:].cold.1
- -[APDBrowserBluetoothHelper startListeningToEvent:].cold.2
- -[APDBrowserBluetoothHelper startListeningToEvent:].cold.3
- -[APDBrowserBluetoothHelper startListeningToEvent:].cold.4
- -[APDBrowserBluetoothHelper stopListeningToEvent:]
- -[APDBrowserBluetoothHelper stopListeningToEvent:].cold.1
- -[APDBrowserBluetoothHelper stopListeningToEvent:].cold.2
- -[APDBrowserBluetoothHelper stopListeningToEvent:].cold.3
- -[APDBrowserBluetoothHelper stopListeningToEvent:].cold.4
- GCC_except_table0
- GCC_except_table32
- GCC_except_table38
- GCC_except_table40
- GCC_except_table42
- GCC_except_table52
- _APAdvertiserInfoCopyCFStringFromTXTRecord
- _APAdvertiserInfoCreateWithRAOPAndAirPlayDataAndDeviceName
- _APAdvertiserInfoCreateWithRAOPAndAirPlayDataAndDeviceName.cold.1
- _APAdvertiserInfoCreateWithRAOPAndAirPlayDataAndDeviceName.cold.10
- _APAdvertiserInfoCreateWithRAOPAndAirPlayDataAndDeviceName.cold.11
- _APAdvertiserInfoCreateWithRAOPAndAirPlayDataAndDeviceName.cold.2
- _APAdvertiserInfoCreateWithRAOPAndAirPlayDataAndDeviceName.cold.3
- _APAdvertiserInfoCreateWithRAOPAndAirPlayDataAndDeviceName.cold.4
- _APAdvertiserInfoCreateWithRAOPAndAirPlayDataAndDeviceName.cold.5
- _APAdvertiserInfoCreateWithRAOPAndAirPlayDataAndDeviceName.cold.6
- _APAdvertiserInfoCreateWithRAOPAndAirPlayDataAndDeviceName.cold.7
- _APAdvertiserInfoCreateWithRAOPAndAirPlayDataAndDeviceName.cold.8
- _APAdvertiserInfoCreateWithRAOPAndAirPlayDataAndDeviceName.cold.9
- _APAdvertiserInfoGetBooleanFromTXTRecord
- _APAdvertiserInfoGetInt64FromTXTRecord
- _APAdvertiserInfoGetInt64FromTXTRecord.cold.1
- _APAdvertiserInfoGetInt64FromTXTRecord.cold.2
- _APAdvertiserInfoGetInt64FromTXTRecord.cold.3
- _APAdvertiserInfoSetProperty.cold.3
- _APBrokeredReceiverCopyCFStringFromTXTRecord
- _APBrowserCreate.cold.25
- _APBrowserCreate.cold.26
- _APCarPlayHelperSessionCreate.cold.14
- _APDBluetoothHelperCreate
- _APDBluetoothHelperCreate.cold.1
- _APDBluetoothHelperCreate.cold.2
- _APDBluetoothHelperCreate.cold.3
- _APDBluetoothHelperGetTypeID
- _APDBluetoothHelperGetTypeID.cold.1
- _APDBluetoothHelperInvalidate
- _APDBluetoothHelperQueryBluetoothPower
- _APDBluetoothHelperSetBluetoothPower
- _APDBluetoothHelperSetEventHandler
- _APDBluetoothHelperStartListeningToEvent
- _APDBluetoothHelperStopListeningToEvent
- _APTNANEndpointCopyTextInfo
- _APTNANEndpointGetServiceType
- _APTransportConnectionCopyProperty
- _APTransportConnectionTCPUnbufferedNWCreate
- _APTransportConnectionTCPUnbufferedNWCreate.cold.1
- _APTransportConnectionTCPUnbufferedNWCreate.cold.10
- _APTransportConnectionTCPUnbufferedNWCreate.cold.11
- _APTransportConnectionTCPUnbufferedNWCreate.cold.12
- _APTransportConnectionTCPUnbufferedNWCreate.cold.13
- _APTransportConnectionTCPUnbufferedNWCreate.cold.2
- _APTransportConnectionTCPUnbufferedNWCreate.cold.3
- _APTransportConnectionTCPUnbufferedNWCreate.cold.4
- _APTransportConnectionTCPUnbufferedNWCreate.cold.5
- _APTransportConnectionTCPUnbufferedNWCreate.cold.6
- _APTransportConnectionTCPUnbufferedNWCreate.cold.7
- _APTransportConnectionTCPUnbufferedNWCreate.cold.8
- _APTransportConnectionTCPUnbufferedNWCreate.cold.9
- _APTransportDeviceGetAddress.cold.10
- _APTransportDeviceGetAddress.cold.11
- _APTransportDeviceIsReachable.cold.2
- _APTransportDeviceIsSameDevice
- _CFAllocatorAllocate
- _CFDictionarySetDouble
- _CFNotificationCenterAddObserver
- _CFNotificationCenterRemoveObserver
- _CFStringCreateWithBytes
- _FigCFDictionaryGetDoubleIfPresent
- _OBJC_CLASS_$_APDBrowserBluetoothHelper
- _OBJC_CLASS_$_BluetoothManager
- _OBJC_EHTYPE_$_NSException
- _OBJC_IVAR_$_APDBrowserBluetoothHelper._bluetoothPowerChangedListeningStarted
- _OBJC_IVAR_$_APDBrowserBluetoothHelper._eventHandlerContext
- _OBJC_IVAR_$_APDBrowserBluetoothHelper._eventHandlerFunc
- _OBJC_IVAR_$_APDBrowserBluetoothHelper._eventQueue
- _OBJC_IVAR_$_APDBrowserBluetoothHelper._helperRef
- _OBJC_IVAR_$_APDBrowserBluetoothHelper._isBluetoothPoweredOn
- _OBJC_IVAR_$_APDBrowserBluetoothHelper._isInvalidated
- _OBJC_IVAR_$_APDBrowserBluetoothHelper._queue
- _OBJC_METACLASS_$_APDBrowserBluetoothHelper
- __APBonjourBrowserHandleAirPlayEventOverNAN
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.1
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.10
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.11
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.12
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.13
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.14
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.15
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.16
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.17
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.18
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.19
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.2
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.20
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.21
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.22
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.23
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.3
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.4
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.5
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.6
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.7
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.8
- __APBonjourBrowserHandleAirPlayEventOverNAN.cold.9
- __APBonjourBrowserStopBrowsingNANFull
- __APBonjourBrowserStopBrowsingNANFull.cold.1
- __APBonjourBrowserStopBrowsingNANPartial
- __APBonjourBrowserStopBrowsingNANPartial.cold.1
- __APBrokerGroupSetDelegateInternal
- __APDBluetoothHelperFinalize
- __APTransportConnectionTCPUnbufferedNWGutsFinalize
- __APTransportConnectionTCPUnbufferedNWGutsFinalize.cold.1
- __APTransportConnectionTCPUnbufferedNWGutsGetTypeID
- __OBJC_$_INSTANCE_METHODS_APDBrowserBluetoothHelper
- __OBJC_$_INSTANCE_VARIABLES_APDBrowserBluetoothHelper
- __OBJC_$_PROP_LIST_APDBrowserBluetoothHelper
- __OBJC_CLASS_RO_$_APDBrowserBluetoothHelper
- __OBJC_METACLASS_RO_$_APDBrowserBluetoothHelper
- ___57-[APDBrowserBluetoothHelper dispatchEvent:withEventInfo:]_block_invoke
- ___APDBluetoothHelperGetTypeID_block_invoke
- ___APDBluetoothHelperInvalidate_block_invoke
- ___APDBluetoothHelperQueryBluetoothPower_block_invoke
- ___APDBluetoothHelperSetBluetoothPower_block_invoke
- ___APDBluetoothHelperSetEventHandler_block_invoke
- ___APDBluetoothHelperStartListeningToEvent_block_invoke
- ___APDBluetoothHelperStopListeningToEvent_block_invoke
- ___block_descriptor_52_e8_32o40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_57_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_68_e8_32o_e5_v8?0ls32l8
- ___block_descriptor_72_e8_32o40o48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_tmp.10
- ___block_descriptor_tmp.101
- ___block_descriptor_tmp.105
- ___block_descriptor_tmp.122
- ___block_descriptor_tmp.131
- ___block_descriptor_tmp.135
- ___block_descriptor_tmp.136
- ___block_descriptor_tmp.143
- ___block_descriptor_tmp.144
- ___block_descriptor_tmp.148
- ___block_descriptor_tmp.160
- ___block_descriptor_tmp.175
- ___block_descriptor_tmp.178
- ___block_descriptor_tmp.210
- ___block_descriptor_tmp.214
- ___block_descriptor_tmp.39
- ___block_descriptor_tmp.43
- ___block_descriptor_tmp.49
- ___block_descriptor_tmp.68
- ___block_descriptor_tmp.70
- ___block_descriptor_tmp.71
- ___block_literal_global.160
- ___block_literal_global.212
- ___block_literal_global.216
- ___browser_handleBluetoothHelperEventExternal_block_invoke
- ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.1
- ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.10
- ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.11
- ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.12
- ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.13
- ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.14
- ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.15
- ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.2
- ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.3
- ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.4
- ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.5
- ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.6
- ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.7
- ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.8
- ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.9
- ___carPlayHelperSession_setInterfaceWatchingEnabled_block_invoke_2
- ___handleBluetoothChangedNotification_block_invoke
- ___tcpunbufnwGuts_connectionHandlePackageHeader_block_invoke
- ___tcpunbufnwGuts_connectionHandlePackagePayload_block_invoke
- ___tcpunbufnwGuts_connectionReceivePackages_block_invoke
- ___tcpunbufnwGuts_connectionReceivePackages_block_invoke.cold.1
- ___tcpunbufnwGuts_connectionReceivePackages_block_invoke.cold.2
- ___tcpunbufnwGuts_connectionReceivePackages_block_invoke.cold.3
- ___tcpunbufnwGuts_connectionSendPackages_block_invoke
- ___tcpunbufnwGuts_connectionSendPackages_block_invoke_2
- ___tcpunbufnwGuts_connectionStateChangedHandler_block_invoke
- ___tcpunbufnwGuts_drainEventQueueAsyncOnCallbackQueue_block_invoke
- ___tcpunbufnwGuts_drainEventQueueAsyncOnCallbackQueue_block_invoke_2
- ___tcpunbufnwGuts_handleNewConnectionGroupInternal_block_invoke
- ___tcpunbufnwGuts_handleNewConnectionGroupInternal_block_invoke_2
- ___tcpunbufnwGuts_handleNewConnectionInternal_block_invoke
- ___tcpunbufnwGuts_updatePackageTrackingInternal_block_invoke
- ___tcpunbufnw_Resume_block_invoke
- ___tcpunbufnw_Resume_block_invoke.cold.1
- ___tcpunbufnw_Resume_block_invoke.cold.2
- ___tcpunbufnw_Resume_block_invoke.cold.3
- ___tcpunbufnw_Resume_block_invoke_2
- ___tcpunbufnw_Resume_block_invoke_3
- ___tcpunbufnw_Resume_block_invoke_4
- ___tcpunbufnw_Resume_block_invoke_4.cold.1
- ___tcpunbufnw_Resume_block_invoke_5
- ___tcpunbufnw_SetProperty_block_invoke
- ___tcpunbufnw_SignalDataAvailable_block_invoke
- _browser_ConfigureForMaximumDiscovery
- _browser_ConfigureForMaximumDiscovery.cold.1
- _browser_configureForMaximumDiscovery
- _browser_copyIsConfiguredForMaximumDiscovery
- _browser_copyIsConfiguredForMaximumDiscovery.cold.1
- _browser_copyIsConfiguredForMaximumDiscovery.cold.2
- _browser_copyNANEndpointForDeviceID
- _browser_copyPropertyInternal.cold.5
- _browser_copyPropertyInternal.cold.6
- _browser_copyPropertyInternal.cold.7
- _browser_copyPropertyInternal.cold.8
- _browser_handleBluetoothHelperEventExternal
- _browser_handleConnectivityHelperEventInternal.cold.14
- _browser_removeAirPlayP2PServiceForNearbyDevices
- _browser_shouldQueryIPv4Address
- _browser_shouldQueryIPv4Address.cold.1
- _browser_shouldQueryIPv4Address.cold.2
- _browser_updateConfigurationForMaximumDiscoveryStatus
- _browser_updateConfigurationForMaximumDiscoveryStatus.cold.1
- _browser_updateConfigurationForMaximumDiscoveryStatus.cold.2
- _gAPDBluetoothHelperInitOnce
- _gAPDBluetoothHelperTypeID
- _gAPTransportConnectionTCPUnbufferedNWGutsInitOnce
- _gAPTransportConnectionTCPUnbufferedNWGutsTypeID
- _gLogCategory_APDBluetoothHelper
- _gLogCategory_APTransportConnectionTCPUnbufferedNW
- _handleBluetoothChangedNotification
- _handleBluetoothChangedNotification.cold.1
- _inet_pton
- _kAPBonjourBrowserCreationOption_OpenFullNANAllowed
- _kAPBrowserCreationOption_OpenFullNANAllowed
- _kAPBrowserMaximumDiscoveryNeeds_BluetoothRadio
- _kAPBrowserMaximumDiscoveryNeeds_WiFiRadio
- _kAPBrowserProperty_IsConfiguredForMaximumDiscovery
- _kAPBrowserProperty_RadiosNeededForMaximumDiscovery
- _kAPDBluetoothHelperClass
- _kAPTransportConnectionOption_UseQUIC
- _kAPTransportConnectionProperty_AllMsgsProcessingTotalTimeMs
- _kAPTransportConnectionProperty_AllMsgsRoundTripTotalTimeMs
- _kAPTransportConnectionTCPUnbufNW_EndpointHierarchyProtocol
- _kAPTransportConnectionTCPUnbufNW_EndpointHierarchyProtocolVTable
- _kAPTransportConnectionTCPUnbufNW_baseProtocol
- _kAPTransportConnectionTCPUnbufNW_protocolEntries
- _kAPTransportConnectionTCPUnbufNW_protocolTable
- _kAPTransportConnectionTCPUnbufferedNWGutsClass
- _kAPTransportConnectionTCPUnbufferedNWVTable
- _kAPTransportConnectionTCPUnbufferedNW_BaseClassWrapper
- _kAPTransportConnectionTCPUnbufferedNW_Class
- _kAPTransportSessionStreamOption_UseQUIC
- _kAPTransportStreamProperty_AllMsgsProcessingTotalTimeMs
- _kAPTransportStreamProperty_AllMsgsRoundTripTotalTimeMs
- _objc_begin_catch
- _objc_end_catch
- _objc_msgSend$bluetoothPowerChangedListeningStarted
- _objc_msgSend$enabled
- _objc_msgSend$ensureBluetoothPowerChangedListenerStopped
- _objc_msgSend$ensureBluetoothPowerEventMonitorStarted
- _objc_msgSend$getBluetoothPowerOn:
- _objc_msgSend$getEventString:
- _objc_msgSend$handleBluetoothChangedNotificationInternal:
- _objc_msgSend$helperRef
- _objc_msgSend$queryBluetoothPower:
- _objc_msgSend$reason
- _objc_msgSend$setBluetoothPower:
- _objc_msgSend$setBluetoothPowerChangedListeningStarted:
- _objc_msgSend$setEventHandler:context:helperRef:
- _objc_msgSend$setHelperRef:
- _objc_msgSend$setPowered:
- _objc_msgSend$setSharedInstanceQueue:
- _objc_msgSend$sharedInstance
- _objc_msgSend$startListeningToEvent:
- _objc_msgSend$stopListeningToEvent:
- _session_resumeInternal.cold.6
- _stream_recordConnectionEvent.cold.5
- _strnlen
- _tcpunbufnwGuts_callEventCallbackInternal
- _tcpunbufnwGuts_connectionHandlePackagePayload
- _tcpunbufnwGuts_connectionHandlePotentialDisconnect
- _tcpunbufnwGuts_connectionReceivePackages
- _tcpunbufnwGuts_connectionSendPackages
- _tcpunbufnwGuts_drainEventQueueAsyncOnCallbackQueue
- _tcpunbufnwGuts_handleNewConnectionInternal
- _tcpunbufnwGuts_handleNewConnectionInternal.cold.1
- _tcpunbufnwGuts_invalidate
- _tcpunbufnwGuts_invalidateInternal
- _tcpunbufnwGuts_readyToSendBatchSlow
- _tcpunbufnwGuts_setEventCallback
- _tcpunbufnwGuts_updatePackageTrackingInternal
- _tcpunbufnwGuts_updateStatus
- _tcpunbufnwGuts_updateStatusInternal
- _tcpunbufnwTrackingWindowItem_Copy
- _tcpunbufnwTrackingWindowItem_Free
- _tcpunbufnw_AddEventCallback
- _tcpunbufnw_AddEventCallback.cold.1
- _tcpunbufnw_AddEventCallback.cold.2
- _tcpunbufnw_CopyProperty
- _tcpunbufnw_DumpHierarchy
- _tcpunbufnw_Finalize
- _tcpunbufnw_Invalidate
- _tcpunbufnw_RemoveEventCallback
- _tcpunbufnw_RemoveEventCallback.cold.1
- _tcpunbufnw_Resume
- _tcpunbufnw_SetProperty
- _tcpunbufnw_SetReadyToSendBatchCallback
- _tcpunbufnw_SetReadyToSendCallback
- _tcpunbufnw_SignalDataAvailable
CStrings:
+ "    %@\n"
+ "    AdvertiserInfo:%-3s"
+ "    DeviceID:%-15@ transports:"
+ "    Name:%-15s"
+ " (Current)"
+ " INVALIDATED"
+ " IP=%-45s"
+ " _airplay-p2p=%s%s%s"
+ " _airplay=%s%s%s%s%s%s"
+ " data=<flags=%@ config=%-3u IP=%-45s Port=%-5hu>\n"
+ " eventDispatched:%-31@"
+ "### [%{ptr}] unsupported transport protocol '%C'"
+ "%.6a"
+ "%@\n"
+ "%C%?{end}:%@"
+ "+[APBonjourCacheHomeKit isDeviceCacheable:]"
+ "+[APBonjourCacheHomeKit prepareDeviceInfo:]"
+ "-[APBonjourCacheHomeKit activateWithCompletionInternal:]"
+ "-[APBonjourCacheHomeKit cacheDevice:]"
+ "-[APBonjourCacheHomeKit checkAndEvictCachedDevicesIfNecessary]"
+ "-[APBonjourCacheHomeKit dealloc]"
+ "-[APBonjourCacheHomeKit evictCachedDeviceWithIDInternal:]"
+ "-[APBonjourCacheHomeKit forceReportCachedDevicesFound]"
+ "-[APBonjourCacheHomeKit forceReportCachedDevicesLost]"
+ "-[APBonjourCacheHomeKit getCacheDirectoryURLWithParentDirectory:creatingIfNecessary:]"
+ "-[APBonjourCacheHomeKit getCacheFileURLCreatingParentDirectoriesIfNecessary:]"
+ "-[APBonjourCacheHomeKit handleHomeKitDeviceConfigurationChanged:]"
+ "-[APBonjourCacheHomeKit handleNetworkSignatureChanged:]"
+ "-[APBonjourCacheHomeKit handleRealDeviceFoundForCachedDevice:]"
+ "-[APBonjourCacheHomeKit handleRealDeviceLostForCachedDevice:]"
+ "-[APBonjourCacheHomeKit init]"
+ "-[APBonjourCacheHomeKit invalidateInternal]"
+ "-[APBonjourCacheHomeKit loadCache]"
+ "-[APBonjourCacheHomeKit realDeviceFoundInternal:]"
+ "-[APBonjourCacheHomeKit realDeviceLostInternal:]"
+ "-[APBonjourCacheHomeKit reportCachedDevice:found:withHandler:]"
+ "-[APBonjourCacheHomeKit setupEvictionPolicies]"
+ "-[APBonjourCacheHomeKit uncacheDevice:]"
+ "-[APBonjourCacheHomeKit updateExpectedDeviceIDsAdding:removing:]"
+ "-[APBonjourCacheHomeKit writeCache]"
+ "-[APHomeKitDeviceMonitor accessoryDidUpdateName:]"
+ "-[APHomeKitDeviceMonitor activateWithCompletionInternal:]"
+ "-[APHomeKitDeviceMonitor dealloc]"
+ "-[APHomeKitDeviceMonitor fullRefresh]"
+ "-[APHomeKitDeviceMonitor handleHomeKitAccessoriesDidChange]"
+ "-[APHomeKitDeviceMonitor home:didAddAccessory:]"
+ "-[APHomeKitDeviceMonitor home:didRemoveAccessory:]"
+ "-[APHomeKitDeviceMonitor homeManager:didAddHome:]"
+ "-[APHomeKitDeviceMonitor homeManager:didRemoveHome:]"
+ "-[APHomeKitDeviceMonitor homeManagerDidUpdateCurrentHome:]"
+ "-[APHomeKitDeviceMonitor homeManagerDidUpdateHomes:]"
+ "-[APHomeKitDeviceMonitor init]"
+ "-[APHomeKitDeviceMonitor invalidateInternal]"
+ "-[APHomeKitDeviceMonitor refreshWithAccessory:isAddOrUpdate:notifyOnAccessoryChange:]"
+ "-[APHomeKitDeviceMonitor refreshWithHome:isAddOrUpdate:notifyOnAccessoriesChanged:]"
+ "-[APTNANPairingDelegate handlePairingRequestOfType:withInputCompletionHandler:]"
+ "-[APTNANPairingDelegate initWithHandleAuthorizationRequestBlock:]"
+ "890.61.4.11.2"
+ ";IPv4.RouterHardwareAddress="
+ ";IPv6.RouterHardwareAddress="
+ "<APTransportPackageDatagram %p [%p]>{ type='%C', data=%@ }"
+ "@\"APHomeKitDeviceMonitor\""
+ "@\"HMHomeManager\""
+ "@\"NSArray\""
+ "@20@0:8B16"
+ "@24@0:8@16"
+ "@24@0:8@?16"
+ "@28@0:8@16B24"
+ "APAdvertiserInfoCreateWithDeviceTXTRecordDataAndDeviceName"
+ "APBonjourBrowserBonjourAirPlayOpenNAN"
+ "APBonjourBrowserBonjourAirPlaySecureNANPartial"
+ "APBonjourCacheEvictionPolicy"
+ "APBonjourCacheEvictionTTL"
+ "APBonjourCacheHomeKit"
+ "APBonjourCacheHomeKit.%{ptr}.DispatchQueue"
+ "APBonjourCacheHomeKit.%{ptr}.InternalQueue"
+ "APBrowserCopyAirPlayBonjourInfo"
+ "APBrowserDeepCopyPlistAtKeyPath"
+ "APHomeKitDeviceMonitor"
+ "APHomeKitDeviceMonitor.%{ptr}.InternalQueue"
+ "APHomeKitDeviceMonitor.m"
+ "APTNANDataSessionProperty_AuthorizationType"
+ "APTNANDataSessionProperty_HandleAuthorizationRequestBlock"
+ "APTNANDataSessionProperty_SetAuthorizationStringBlock"
+ "APTNANDataSessionRef transportDevice_getNANDataSession(APTransportDeviceRef, APSNANServiceType, Boolean, OSStatus *)"
+ "APTNANPairingDelegate"
+ "APTPacingController"
+ "APTPacingControllerAddBytesSent"
+ "APTPacingControllerCreate"
+ "APTPacingControllerReset"
+ "APTPacingControllerSetMaxPacingRate"
+ "APTPacingControllerYieldOnQueueWithContinuationBlock"
+ "APTPacingControllerYieldOnQueueWithContinuationFunction"
+ "APTransportConnectionUnbufferedNW"
+ "APTransportConnectionUnbufferedNW.%{ptr}"
+ "APTransportConnectionUnbufferedNWCreate"
+ "APTransportConnectionUnbufferedNWGuts"
+ "APTransportDevice %{ptr} created with addresses %@ and deviceInfo %@\n"
+ "APTransportDeviceCopyInfo"
+ "APTransportDeviceCreateWithNetworkAddresses"
+ "APTransportPackageDatagramCreateWithBBuf"
+ "AirPlayNAN"
+ "AirPlayNANFull"
+ "AirPlayNANFullBonjourInfo"
+ "AirPlayNANPartial"
+ "AirPlayNANPartialBonjourInfo"
+ "AppleTV"
+ "AudioAccessory"
+ "AuthorizationType_PIN"
+ "AuthorizationType_Password"
+ "B24@0:8@\"NSDictionary\"16"
+ "B24@?0@\"NSDictionary\"8@\"NSDictionary\"16"
+ "B32@0:8@16B24B28"
+ "B32@0:8@16^@24"
+ "BT"
+ "BTLE Update: UUID: %@ RSSI %-3d  Flags %#{flags}  Config %-3u  IP %-45s\n"
+ "BonjourCacheHomeKit_ApplyEvictions"
+ "BonjourCacheHomeKit_PurgeCache"
+ "BonjourCacheHomeKit_ShowInfo"
+ "Boolean unbufnwGuts_connectionHandlePotentialDisconnect(APTransportConnectionUnbufferedNWGutsRef, nw_content_context_t, _Bool, nw_error_t)"
+ "C"
+ "C16@0:8"
+ "CFDictionaryRef _APBonjourBrowserCreateDeviceInfoWithAirPlayNANInfo(APBonjourBrowserRef, APBonjourBrowserEventType, CFDictionaryRef, CFDictionaryRef, CFDataRef)"
+ "Cache Entries: %u\n"
+ "Cache Files: %u\n"
+ "Cache Root:                    %@\n"
+ "Cache entries evicted: %lu\n"
+ "Cached Network Signature:      %@\n"
+ "Class getHMHomeManagerClass(void)_block_invoke"
+ "Class getHMMutableHomeManagerConfigurationClass(void)_block_invoke"
+ "Connection:[%{ptr}] (UnbufferedNW:%C) %''@ (Not Connected) Parent:[%{ptr}]\n"
+ "Connection:[%{ptr}] (UnbufferedNW:%C) %''@ Ports:%##a -> %##a Parent:[%{ptr}]\n"
+ "Created nw_listener [%{ptr}].\n"
+ "Current Cache File Version:    %@\n"
+ "Current Cache File:            %@\n"
+ "Current Network Signature:     %@\n"
+ "DataPacer"
+ "Datagram"
+ "Device %@ transports: _airplay=%s%s%s%s%s%s%s%s _raop=%s%s%s%s%s%s _airplay-p2p=%s%s%s cached=%s\n"
+ "Device found: %@ Addr: %-45s Port: %-5hu Flags: %#{flags}\n"
+ "ERROR: %@\n"
+ "Expected Device IDs: %u\n"
+ "Failed to find"
+ "Failed to initialize NAN Pairing Delegate."
+ "Found"
+ "HMAccessoryDelegate"
+ "HMHomeDelegate"
+ "HMHomeManager"
+ "HMHomeManagerDelegate"
+ "HMMutableHomeManagerConfiguration"
+ "HandleNANAuthorizationRequestBlock"
+ "IPv4.Router="
+ "IPv6.Prefix="
+ "Ignoring BTLE beacon with both IP address and flags set to zero."
+ "Ignoring IPv6 BTLE beacon with no IP address"
+ "Introspector"
+ "IsPackageArrivalTicksEnabled"
+ "Items"
+ "Monitoring"
+ "NAN (Secure)"
+ "NANAuthorizationType"
+ "NANDS [%{ptr}] Created with type (%s %s)"
+ "NANDS [%{ptr}] Wrong PIN. Translating error to auth error."
+ "NANDS [%{ptr}] created pairing delegate [%{ptr}]. Setting on CUNANDS [%{ptr}]."
+ "NANDS [%{ptr}] diversified PIN callback called%?{end} with err=%#m"
+ "NANDS [%{ptr}] enabled pairing caching"
+ "NANDS [%{ptr}] has authorization block [%{ptr}]"
+ "NANDS [%{ptr}] has authorization type %@"
+ "NANDS [%{ptr}] has set authorization block [%{ptr}]"
+ "NANDS [%{ptr}] set pairing delegate [%{ptr}]"
+ "NANDS [%{ptr}] set pairing method: %@"
+ "NetworkSignature"
+ "NetworkingMs"
+ "OSStatus APAdvertiserInfoCopyAirPlayP2PDataWithNANServiceType(APAdvertiserInfoRef, APAdvertiserInfoDeviceIDType, APSNANServiceType, CFDataRef *)"
+ "OSStatus APTNANDataSessionCreate(APSNANServiceType, APBrowserRef, uint64_t, Boolean, APTNANDataSessionRef *)"
+ "OSStatus APTPacingControllerAddBytesSent(APTPacingControllerRef, size_t)"
+ "OSStatus APTPacingControllerCreate(dispatch_queue_t, APTPacingControllerRef *)"
+ "OSStatus APTPacingControllerReset(APTPacingControllerRef)"
+ "OSStatus APTPacingControllerSetMaxPacingRate(APTPacingControllerRef, uint64_t)"
+ "OSStatus APTPacingControllerYieldOnQueueWithContinuationFunction(APTPacingControllerRef, dispatch_function_t, void *)"
+ "OSStatus APTransportConnectionUnbufferedNWCreate(CFAllocatorRef, CFStringRef, APTransportConnectionFlags, FigThreadPriority, CFDictionaryRef, APTransportConnectionRef *)"
+ "OSStatus APTransportDeviceCreateWithNetworkAddresses(CFAllocatorRef, CFArrayRef, APTransportDeviceAddressType, CFDictionaryRef, APTransportDeviceRef *)"
+ "OSStatus _APBonjourBrowserStartOpenNAN(APBonjourBrowserRef, APBonjourBrowserMode, uint32_t *, uint64_t)"
+ "OSStatus _APBonjourBrowserStartSecureNANPartial(APBonjourBrowserRef, APBonjourBrowserMode, uint32_t *, uint64_t)"
+ "OSStatus _APBonjourBrowserStopBrowsingOpenNAN(APBonjourBrowserRef, uint32_t *)"
+ "OSStatus _APBonjourBrowserStopBrowsingSecureNANPartial(APBonjourBrowserRef, uint32_t *)"
+ "OSStatus _APTNANDataSessionGenerateDiversifiedPIN(APTNANDataSessionRef, CFStringRef *)"
+ "OSStatus _APTNANDataSessionGenerateDiversifiedPIN(APTNANDataSessionRef, CFStringRef *)_block_invoke"
+ "OSStatus _APTNANDataSessionSetProperty(CMBaseObjectRef, CFStringRef, CFTypeRef)"
+ "OSStatus browser_copyNANEndpointForOneDeviceID(APBrowserRef, uint64_t, APSNANServiceType, Boolean, uint64_t *, APTNANEndpointRef *)"
+ "OSStatus browser_removeP2PServicesForNearbyDevices(APBrowserRef)_block_invoke"
+ "OSStatus queryManagerGetInfo_queryDeviceInternal(APBrowserDeviceQueryManagerRef, CFStringRef, CFStringRef, CFNumberRef, CFStringRef, APBrowserDeviceQueryManagerCompletionHandler, void *)"
+ "OSStatus queryManagerGetInfo_queryDeviceInternal(APBrowserDeviceQueryManagerRef, CFStringRef, CFStringRef, CFNumberRef, CFStringRef, APBrowserDeviceQueryManagerCompletionHandler, void *)_block_invoke"
+ "OSStatus session_activateNANDS(FigTransportSessionRef, APSNANServiceType, APTNANDataSessionRef *)"
+ "OSStatus stream_packageReceived(FigTransportStreamRef, APTransportPackageRef)"
+ "OSStatus unbufnwGuts_handleNewConnectionInternal(APTransportConnectionUnbufferedNWGutsRef, nw_connection_t, Boolean)"
+ "OSStatus unbufnwGuts_updateStatusInternal(APTransportConnectionUnbufferedNWGutsRef, APTransportConnectionStatus, OSStatus)"
+ "OSStatus unbufnw_CopyProperty(CMBaseObjectRef, CFStringRef, CFAllocatorRef, void *)"
+ "OSStatus unbufnw_Resume(APTransportConnectionRef)"
+ "OSStatus unbufnw_SetProperty(CMBaseObjectRef, CFStringRef, CFTypeRef)"
+ "OSStatus unbufnw_SignalDataAvailable(APTransportConnectionRef)_block_invoke"
+ "Open"
+ "OpenNANAllowed"
+ "PIN"
+ "Passphrase"
+ "Present Real Devices: %u\n"
+ "Purging directory URL: %@\n"
+ "R"
+ "ReceiverMessageProcessingMs"
+ "Reconfirming NAN airplay services for device with ID %@\n"
+ "Reported Cached Device IDs: %u\n"
+ "Secure"
+ "SetNANAuthorizationStringBlock"
+ "Stop monitoring"
+ "T@\"APHomeKitDeviceMonitor\",N,V_homeKitDeviceMonitor"
+ "T@\"CUSystemMonitor\",N,V_systemMonitor"
+ "T@\"HMHomeManager\",N,V_homeManager"
+ "T@\"NSArray\",&,N,V_evictionPolicies"
+ "T@\"NSArray\",R,N"
+ "T@\"NSDictionary\",R,N"
+ "T@\"NSMutableDictionary\",&,N,V_cache"
+ "T@\"NSMutableDictionary\",&,N,V_presentRealDevices"
+ "T@\"NSMutableSet\",&,N,V_expectedDeviceIDs"
+ "T@\"NSMutableSet\",&,N,V_homeAccessories"
+ "T@\"NSMutableSet\",&,N,V_reportedCachedDeviceIDs"
+ "T@\"NSObject<OS_dispatch_queue>\",N,V_dispatchQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",N,V_internalQueue"
+ "T@\"NSSet\",R,N"
+ "T@\"NSString\",&,N,V_currentNetworkSignature"
+ "T@?,C,N,V_cachedDeviceFoundHandler"
+ "T@?,C,N,V_cachedDeviceLostHandler"
+ "T@?,C,N,V_homeConfigurationDidChangeHandler"
+ "TB,N,V_activatedPresentDeviceStashing"
+ "TB,N,V_invalidated"
+ "TB,N,V_usePresentDeviceStashing"
+ "TB,N,V_useStrictNetworkSignatureMatching"
+ "TC,N,V_handledPairingRequest"
+ "Td,N,V_timeToLiveSeconds"
+ "TimingInformation"
+ "TotalMessageTimeMs"
+ "TrTy"
+ "TransportProtocol"
+ "URLByDeletingLastPathComponent"
+ "UnbufNW[%{ptr}]::RequestData"
+ "UnspecifiedRemoteTimeMs"
+ "Version"
+ "WiFiAwareDataSessionPairingDelegate"
+ "X-Apple-QR"
+ "[%@:%@] Unexpected: Sending request to rapport direct client\n"
+ "[%@] %@ '%@'"
+ "[%{ptr}]"
+ "[%{ptr}] ### send error: %#m\n"
+ "[%{ptr}] %@ %@ event for device id: %llu name: %@ serviceType: %@ %?@\n"
+ "[%{ptr}] %s '%##a' err=%#m"
+ "[%{ptr}] %s ConnectivityHelper stopped listening to USB\n"
+ "[%{ptr}] %s ConnectivityHelper stopped listening to WiFi\n"
+ "[%{ptr}] %s Home [%{ptr}]: %@%?s"
+ "[%{ptr}] %s Ignoring %@ interface\n"
+ "[%{ptr}] %s NAN endpoint [%{ptr}] deviceID=%lu isSecure=%s"
+ "[%{ptr}] %s RSD network interface changed to NULL"
+ "[%{ptr}] %s RSD network interface changed to `%@`, type: `%s`"
+ "[%{ptr}] %s Switching to use RSD interface for wired CPS: `%@`\n"
+ "[%{ptr}] %s connection %s %##a: %s"
+ "[%{ptr}] %s device %@ to cache%?{end}: %@"
+ "[%{ptr}] APTransportConnectionUnbufferedNW finalized, protocol=%C"
+ "[%{ptr}] APTransportConnectionUnbufferedNW invalidating"
+ "[%{ptr}] APTransportConnectionUnbufferedNW with name %'@ created"
+ "[%{ptr}] APTransportSession holds NANDS [%{ptr}] (%s %s)\n"
+ "[%{ptr}] Accessory [%{ptr}] didUpdateName"
+ "[%{ptr}] Activated"
+ "[%{ptr}] Activating (presentDeviceStashing=%s)"
+ "[%{ptr}] AirPlayNAN (%@) conversion successful"
+ "[%{ptr}] AirPlayNAN BonjourBrowser restarted.\n"
+ "[%{ptr}] AirPlayNAN BonjourBrowser stopped.\n"
+ "[%{ptr}] AirPlayNAN conversion beginning for %s"
+ "[%{ptr}] AirPlayNAN conversion converted binary TXT record"
+ "[%{ptr}] AirPlayNAN conversion found binary TXT record"
+ "[%{ptr}] Cache unavailable, no current network signature"
+ "[%{ptr}] Connection UUID copied for PID %llu, remote %s address: %##a"
+ "[%{ptr}] Copying AirPlayP2PData\n"
+ "[%{ptr}] Copying local network information: Failed to convert interface name '%@'\n"
+ "[%{ptr}] Copying local network information: Failed to get interface address for '%s'. Error: %#m\n"
+ "[%{ptr}] CorrelationID requested. Available: %s\n"
+ "[%{ptr}] Created APBonjourCacheHomeKit"
+ "[%{ptr}] Created APHomeKitDeviceMonitor"
+ "[%{ptr}] Deallocated APBonjourCacheHomeKit"
+ "[%{ptr}] Deallocated APHomeKitDeviceMonitor"
+ "[%{ptr}] Device ID mismatch: Bonjour (%s) vs TXTRecord (%.*s). Will use TXTRecord deviceID.\n"
+ "[%{ptr}] Failed to create cache directory: %ld"
+ "[%{ptr}] Failed to find cache. Cache directory not found"
+ "[%{ptr}] Failed to load cache with incompatible file version %'@ (expected %'@)"
+ "[%{ptr}] Failed to retrieve Caches directory: %ld"
+ "[%{ptr}] Failed to serialize cache: %@%?{end} contents:%@"
+ "[%{ptr}] Failed to start browsing for %s over NAN with error: %#m\n"
+ "[%{ptr}] Failed to write cache file data%?{end} to URL: %@ contents:%@"
+ "[%{ptr}] Force reporting cached device found %@"
+ "[%{ptr}] Force reporting cached device lost %@"
+ "[%{ptr}] Found correlationID %llu for deviceID %llu"
+ "[%{ptr}] Home [%{ptr}] didAddAccessory: %@"
+ "[%{ptr}] Home [%{ptr}] didRemoveAccessory: %@"
+ "[%{ptr}] Home [%{ptr}] | %s Accessory [%{ptr}]: (%@) %@"
+ "[%{ptr}] HomeKit accessory list changed"
+ "[%{ptr}] HomeKit device configuration changed%?{end}: %@ -> %@"
+ "[%{ptr}] HomeManager [%{ptr}] didAddHome: %@"
+ "[%{ptr}] HomeManager [%{ptr}] didRemoveHome: %@"
+ "[%{ptr}] HomeManager [%{ptr}] didUpdateCurrentHome"
+ "[%{ptr}] HomeManager [%{ptr}] didUpdateHomes"
+ "[%{ptr}] Injecting bonjourInfo: %@\n"
+ "[%{ptr}] Invalidated"
+ "[%{ptr}] Listening on %##a"
+ "[%{ptr}] NAN Pairing Delegate created with pairing block."
+ "[%{ptr}] Network signature changed: %'@ -> %'@"
+ "[%{ptr}] Pairing delegate completed pairing request. Calling completion handler."
+ "[%{ptr}] Pairing delegate received %s pairing request. Running pairing block [%{ptr}]."
+ "[%{ptr}] Policy %@ Evicting %@"
+ "[%{ptr}] Real device found for cacheable device: %@"
+ "[%{ptr}] Real device lost: %@"
+ "[%{ptr}] Reconfirming AirPlayNAN service for device with name %@\n"
+ "[%{ptr}] Reconfirming RAOP service for device with name %@\n"
+ "[%{ptr}] Reconfirming airplay services for device with name %@\n"
+ "[%{ptr}] Reconfirming alt airplay services for device with name %@\n"
+ "[%{ptr}] Refresh all accessories"
+ "[%{ptr}] Remote port set: %##a"
+ "[%{ptr}] Removed %@ for device with id: %@ name: %@.\n"
+ "[%{ptr}] Removing device %@ from cache%?{end}: %@"
+ "[%{ptr}] Reporting evicted cached device as lost %@"
+ "[%{ptr}] Reporting newly expected cached device as found %@"
+ "[%{ptr}] Reporting no longer expected cached device as lost %@"
+ "[%{ptr}] Started browsing for %s over NAN\n"
+ "[%{ptr}] Stopped browsing for %s over NAN\n"
+ "[%{ptr}] Unrecognized AirPlayNAN event %d\n"
+ "[%{ptr}] Unsupported binary TXT record received"
+ "[%{ptr}] Update device %@ property %'@%?{end} from %@ to %@"
+ "[%{ptr}] Using %s TTL of %.0f seconds"
+ "[%{ptr}] Waiting for diversified PIN"
+ "[%{ptr}] addBytesSent nowNs=%llu epochNs=%llu bytesSent=%llu"
+ "[%{ptr}] begYield nowNs=%llu epochNs=%llu bytesSent=%llu"
+ "[%{ptr}] connected %s '%##a' (%s '%##a' using '%s' interface) in %1.3f ms"
+ "[%{ptr}] created"
+ "[%{ptr}] disabling max pacing rate"
+ "[%{ptr}] endYield nowNs=%llu epochNs=%llu bytesSent=%llu"
+ "[%{ptr}] finalize"
+ "[%{ptr}] handlePackageHeader() inHeaderData is NULL!"
+ "[%{ptr}] handlePackagePayload() inData is NULL!"
+ "[%{ptr}] maxPacingRate=%llu"
+ "[%{ptr}] received unsupported package type='%C'\n"
+ "[%{ptr}] reset"
+ "[%{ptr}] setting max pacing rate to %lluB/s"
+ "[%{ptr}] updateYield nowNs=%llu epochNs=%llu bytesSent=%llu"
+ "[%{ptr}] using transport protocol '%C'"
+ "[0x%04X] %@"
+ "_APAdvertiserInfoAddAirPlayNANData"
+ "_APBonjourBrowserCreateDeviceInfoWithAirPlayNANInfo"
+ "_APBonjourBrowserHandleAirPlayNANEvent"
+ "_APBonjourBrowserHandleDeviceEventForAirPlayNANService"
+ "_APBonjourBrowserStartOpenNAN"
+ "_APBonjourBrowserStartSecureNANPartial"
+ "_APTNANDataSessionGenerateDiversifiedPIN"
+ "_APTNANDataSessionSetProperty"
+ "_activatedPresentDeviceStashing"
+ "_cache"
+ "_cachedDeviceFoundHandler"
+ "_cachedDeviceLostHandler"
+ "_currentNetworkSignature"
+ "_evictionPolicies"
+ "_expectedDeviceIDs"
+ "_handleAuthorizationRequestBlock"
+ "_handledPairingRequest"
+ "_homeAccessories"
+ "_homeConfigurationDidChangeHandler"
+ "_homeKitDeviceMonitor"
+ "_homeManager"
+ "_internalQueue"
+ "_presentRealDevices"
+ "_reportedCachedDeviceIDs"
+ "_timeToLiveSeconds"
+ "_usePresentDeviceStashing"
+ "_useStrictNetworkSignatureMatching"
+ "accessories"
+ "accessory:didAddProfile:"
+ "accessory:didRemoveProfile:"
+ "accessory:didUpdateAssociatedServiceTypeForService:"
+ "accessory:didUpdateFirmwareVersion:"
+ "accessory:didUpdateNameForService:"
+ "accessory:service:didUpdateValueForCharacteristic:"
+ "accessoryDidUpdateName:"
+ "accessoryDidUpdateReachability:"
+ "accessoryDidUpdateServices:"
+ "activateWithCompletionInternal:"
+ "activatedPresentDeviceStashing"
+ "addEntriesFromDictionary:"
+ "addExpectedDeviceID:"
+ "addObjectsFromArray:"
+ "airplay"
+ "airplayTargetIPv6"
+ "allKeys"
+ "allObjects"
+ "ap"
+ "array"
+ "availableCachedDevices"
+ "bonjourCacheHomeKitAllowAny"
+ "bonjourCacheHomeKitTTLSeconds"
+ "bonjourCacheHomeKit_introspector_cmd_purgeCache_block_invoke"
+ "browser_cfstringToSockAddr"
+ "browser_copyNANEndpointForOneDeviceID"
+ "browser_getCorrelationIDForDeviceInfo"
+ "browser_removeP2PServicesForNearbyDevices"
+ "browser_shouldQueryIPAddress"
+ "browser_wasNetworkAddressTranslated"
+ "bytes"
+ "cache"
+ "cacheDevice:"
+ "cachedDeviceFoundHandler"
+ "cachedDeviceLostHandler"
+ "cachedDevices"
+ "carPlayHelperSession_resetRSDInterfaceIfNeeded"
+ "check cache entries against eviction policies and evict as necessary"
+ "checkAndEvictCachedDevicesIfNecessary"
+ "cid"
+ "componentsJoinedByString:"
+ "copyDescription"
+ "copyDescriptionInternal"
+ "correlationID"
+ "currentHome"
+ "currentNetworkSignature"
+ "d16@0:8"
+ "data"
+ "datagramPackage_CopyDebugDescription"
+ "datagramPackage_CreateBBufRepresentation"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "default value"
+ "describeBonjourInfo:"
+ "dictionary"
+ "dictionaryWithContentsOfURL:"
+ "dictionaryWithDictionary:"
+ "dst"
+ "evictCachedDeviceWithID:"
+ "evictCachedDeviceWithIDInternal:"
+ "evictionPolicies"
+ "expectedDeviceIDs"
+ "filterUsingPredicate:"
+ "forceReportCachedDevicesFound"
+ "forceReportCachedDevicesLost"
+ "from"
+ "fullRefresh"
+ "generateDiversifiedPINWithCompletionHandler:"
+ "getCString:maxLength:encoding:"
+ "getCacheDirectoryURLWithParentDirectory:creatingIfNecessary:"
+ "getCacheFileURLCreatingParentDirectoriesIfNecessary:"
+ "getDeviceID:"
+ "getReportableCachedDevices"
+ "handleHomeKitAccessoriesDidChange"
+ "handleHomeKitDeviceConfigurationChanged:"
+ "handleNetworkSignatureChanged:"
+ "handlePairingRequestOfType:withInputCompletionHandler:"
+ "handleRealDeviceFoundForCachedDevice:"
+ "handleRealDeviceLostForCachedDevice:"
+ "handledPairingRequest"
+ "home"
+ "home:didAddAccessory:"
+ "home:didAddActionSet:"
+ "home:didAddRoom:"
+ "home:didAddRoom:toZone:"
+ "home:didAddService:toServiceGroup:"
+ "home:didAddServiceGroup:"
+ "home:didAddTrigger:"
+ "home:didAddUser:"
+ "home:didAddZone:"
+ "home:didEncounterError:forAccessory:"
+ "home:didRemoveAccessory:"
+ "home:didRemoveActionSet:"
+ "home:didRemoveRoom:"
+ "home:didRemoveRoom:fromZone:"
+ "home:didRemoveService:fromServiceGroup:"
+ "home:didRemoveServiceGroup:"
+ "home:didRemoveTrigger:"
+ "home:didRemoveUser:"
+ "home:didRemoveZone:"
+ "home:didUnblockAccessory:"
+ "home:didUpdateActionsForActionSet:"
+ "home:didUpdateHomeHubState:"
+ "home:didUpdateNameForActionSet:"
+ "home:didUpdateNameForRoom:"
+ "home:didUpdateNameForServiceGroup:"
+ "home:didUpdateNameForTrigger:"
+ "home:didUpdateNameForZone:"
+ "home:didUpdateRoom:forAccessory:"
+ "home:didUpdateTrigger:"
+ "homeAccessories"
+ "homeConfigurationDidChangeHandler"
+ "homeDidUpdateAccessControlForCurrentUser:"
+ "homeDidUpdateName:"
+ "homeDidUpdateSupportedFeatures:"
+ "homeKitDeviceIDs"
+ "homeKitDeviceMonitor"
+ "homeManager"
+ "homeManager:didAddHome:"
+ "homeManager:didReceiveAddAccessoryRequest:"
+ "homeManager:didRemoveHome:"
+ "homeManager:didUpdateAuthorizationStatus:"
+ "homeManagerDidUpdateCurrentHome:"
+ "homeManagerDidUpdateHomes:"
+ "homeManagerDidUpdatePrimaryHome:"
+ "homes"
+ "httpPackage_computeMessageTypeString"
+ "incoming"
+ "initWithConfiguration:"
+ "initWithHandleAuthorizationRequestBlock:"
+ "initWithOptions:cachePolicy:"
+ "initWithSet:"
+ "internalQueue"
+ "invalidateInternal"
+ "invalidated"
+ "isDeviceCacheable:"
+ "isEqualToDictionary:"
+ "isRemoteDeviceConnected"
+ "isValidNetworkSignature:"
+ "lastPathComponent"
+ "loadCache"
+ "localDataAddress"
+ "nanOpenFullDiscoveryTimeMs"
+ "nanOpenPartialDiscoveryTimeMs"
+ "nanSecurePartialDiscoveryTimeMs"
+ "nanServiceType"
+ "nil cache directory url"
+ "numberWithUnsignedInt:"
+ "openNANAllowed"
+ "outgoing"
+ "pacingController_leewayUs"
+ "pacingController_minYieldUs"
+ "pairingRequestStartedForDataSession:nfcTagScannedCompletionHandler:"
+ "pairingRequestStartedForDataSession:passphraseInputCompletionHandler:"
+ "pairingRequestStartedForDataSession:pinCodeInputCompletionHandler:"
+ "pairingRequestStartedForDataSession:qrCodeScannedCompletionHandler:"
+ "passphrase"
+ "predicateWithBlock:"
+ "prepareDeviceInfo:"
+ "presentRealDevices"
+ "purge cache of BonjourCacheHomeKit"
+ "q24@?0@8@16"
+ "realDeviceFound:"
+ "realDeviceFoundInternal:"
+ "realDeviceLost:"
+ "realDeviceLostInternal:"
+ "refreshWithAccessory:isAddOrUpdate:notifyOnAccessoryChange:"
+ "refreshWithHome:isAddOrUpdate:notifyOnAccessoriesChanged:"
+ "remove"
+ "removeAllExpectedDeviceIDs"
+ "removeExpectedDeviceID:"
+ "removeItemAtURL:error:"
+ "reportCachedDevice:found:withHandler:"
+ "reportedCachedDeviceIDs"
+ "session:didUpdateDLTDOAMeasurements:"
+ "session_activateNANDS"
+ "setActivatedPresentDeviceStashing:"
+ "setCache:"
+ "setCachedDeviceFoundHandler:"
+ "setCachedDeviceLostHandler:"
+ "setCurrentNetworkSignature:"
+ "setEvictionPolicies:"
+ "setExpectedDeviceIDs:"
+ "setHandledPairingRequest:"
+ "setHomeAccessories:"
+ "setHomeConfigurationDidChangeHandler:"
+ "setHomeKitDeviceMonitor:"
+ "setHomeManager:"
+ "setInactiveUpdatingLevel:"
+ "setInternalQueue:"
+ "setInvalidated:"
+ "setPresentRealDevices:"
+ "setReportedCachedDeviceIDs:"
+ "setSystemMonitor:"
+ "setTimeToLiveSeconds:"
+ "setUsePresentDeviceStashing:"
+ "setUseStrictNetworkSignatureMatching:"
+ "setWfaPairingCacheEnabled:"
+ "setWfaPairingDelegate:"
+ "setWfaPairingMethod:"
+ "setupEvictionPolicies"
+ "setupIntrospector"
+ "shouldEvict:"
+ "shouldEvictDevice:policy:"
+ "shouldProcessDeviceForCache:"
+ "show info of BonjourCacheHomeKit"
+ "softlink:r:path:/System/Library/Frameworks/HomeKit.framework/HomeKit"
+ "sortedArrayUsingComparator:"
+ "src"
+ "standardizedURL"
+ "stringWithString:"
+ "systemMonitor"
+ "timeToLiveSeconds"
+ "to"
+ "transportDevice_getNANDataSessionForAddressType"
+ "transportDevice_networkAddressesToCStringRepresentation"
+ "transportDevice_networkAddressesToCStringRepresentation_block_invoke"
+ "unbufnwGuts_callEventCallbackInternal"
+ "unbufnwGuts_connectionHandlePackageHeader"
+ "unbufnwGuts_connectionHandlePackagePayload"
+ "unbufnwGuts_connectionSendPackages"
+ "unbufnwGuts_connectionSendPackages_block_invoke"
+ "unbufnwGuts_handleNewConnectionGroupInternal"
+ "unbufnwGuts_handleNewConnectionInternal"
+ "unbufnwGuts_readyToSendBatchSlow"
+ "unbufnwGuts_updateDataPacingInternal"
+ "unbufnwGuts_updateStatusInternal"
+ "unbufnwThrottleKbps"
+ "unbufnwUsePacingController"
+ "unbufnwUseUDP"
+ "unbufnw_AddEventCallback"
+ "unbufnw_CopyProperty"
+ "unbufnw_RemoveEventCallback"
+ "unbufnw_Resume"
+ "unbufnw_Resume_block_invoke_2"
+ "unbufnw_SetProperty"
+ "unbufnw_getPackageCallbacksForPackageType"
+ "uncacheDevice:"
+ "unsignedIntValue"
+ "updateExpectedDeviceIDsAdding:removing:"
+ "usePresentDeviceStashing"
+ "useStrictNetworkSignatureMatching"
+ "user preference"
+ "v20@0:8C16"
+ "v24@0:8@\"HMAccessory\"16"
+ "v24@0:8@\"HMHome\"16"
+ "v24@0:8@\"HMHomeManager\"16"
+ "v24@0:8d16"
+ "v24@?0q8@\"NSString\"16"
+ "v32@0:8@\"HMAccessory\"16@\"HMAccessoryProfile\"24"
+ "v32@0:8@\"HMAccessory\"16@\"HMService\"24"
+ "v32@0:8@\"HMAccessory\"16@\"NSString\"24"
+ "v32@0:8@\"HMHome\"16@\"HMAccessory\"24"
+ "v32@0:8@\"HMHome\"16@\"HMActionSet\"24"
+ "v32@0:8@\"HMHome\"16@\"HMRoom\"24"
+ "v32@0:8@\"HMHome\"16@\"HMServiceGroup\"24"
+ "v32@0:8@\"HMHome\"16@\"HMTrigger\"24"
+ "v32@0:8@\"HMHome\"16@\"HMUser\"24"
+ "v32@0:8@\"HMHome\"16@\"HMZone\"24"
+ "v32@0:8@\"HMHome\"16Q24"
+ "v32@0:8@\"HMHomeManager\"16@\"HMAddAccessoryRequest\"24"
+ "v32@0:8@\"HMHomeManager\"16@\"HMHome\"24"
+ "v32@0:8@\"HMHomeManager\"16Q24"
+ "v32@0:8@\"WiFiAwareDataSession\"16@?<v@?@\"NSData\">24"
+ "v32@0:8@\"WiFiAwareDataSession\"16@?<v@?@\"NSString\">24"
+ "v32@0:8@16Q24"
+ "v32@0:8^{__CFString=}16@?24"
+ "v36@0:8@16B24@?28"
+ "v40@0:8@\"HMAccessory\"16@\"HMService\"24@\"HMCharacteristic\"32"
+ "v40@0:8@\"HMHome\"16@\"HMRoom\"24@\"HMAccessory\"32"
+ "v40@0:8@\"HMHome\"16@\"HMRoom\"24@\"HMZone\"32"
+ "v40@0:8@\"HMHome\"16@\"HMService\"24@\"HMServiceGroup\"32"
+ "v40@0:8@\"HMHome\"16@\"NSError\"24@\"HMAccessory\"32"
+ "void *HomeKitLibrary(void)"
+ "void _APBonjourBrowserHandleAirPlayNANEvent(BonjourBrowserEventType, CFDictionaryRef, void *)"
+ "void _APBonjourBrowserHandleDeviceEventForAirPlayNANService(APBonjourBrowserRef, APBonjourBrowserEventType, CFDictionaryRef, CFDictionaryRef)"
+ "void _APTPacingControllerFinalize(CFTypeRef)"
+ "void _APTransportConnectionUnbufferedNWGutsFinalize(CFTypeRef)"
+ "void carPlayHelperSession_resetRSDInterfaceIfNeeded(APCarPlayHelperRef, CFStringRef, CFArrayRef)"
+ "void carPlayHelperSession_usbInterfaceListeningStopped(APCarPlayHelperRef)"
+ "void carPlayHelperSession_wifiNetworkListeningStopped(APCarPlayHelperRef)"
+ "void pacingController_endYieldInternal(APTPacingControllerRef, uint64_t, dispatch_function_t *, void **)"
+ "void pacingController_updateYieldTimerIfNeededAsync(void *)"
+ "void unbufnwGuts_connectionHandlePackageHeader(APTransportConnectionUnbufferedNWGutsRef, dispatch_data_t, nw_content_context_t, _Bool, _Bool, nw_error_t)"
+ "void unbufnwGuts_connectionHandlePackagePayload(APTransportConnectionUnbufferedNWGutsRef, dispatch_data_t, nw_content_context_t, _Bool, _Bool, nw_error_t)"
+ "void unbufnwGuts_connectionSendPackages(APTransportConnectionUnbufferedNWGutsRef)"
+ "void unbufnwGuts_connectionSendPackages(APTransportConnectionUnbufferedNWGutsRef)_block_invoke"
+ "void unbufnwGuts_connectionSendPackages(APTransportConnectionUnbufferedNWGutsRef)_block_invoke_2"
+ "void unbufnwGuts_connectionStateChangedHandler(APTransportConnectionUnbufferedNWGutsRef, nw_connection_state_t, nw_error_t)"
+ "void unbufnwGuts_invalidateInternal(APTransportConnectionUnbufferedNWGutsRef)"
+ "void unbufnwGuts_listenerStateChangedHandler(APTransportConnectionUnbufferedNWListenerContext *, nw_listener_state_t, nw_error_t)"
+ "void unbufnwGuts_updateDataPacingInternal(APTransportConnectionUnbufferedNWGutsRef)"
+ "void unbufnwGuts_updatePackageTrackingInternal(APTransportConnectionUnbufferedNWGutsRef, APTransportPackageRef, size_t)"
+ "writeCache"
+ "writeToURL:atomically:"
- "    DeviceID:%15@"
- " AdvertiserInfo:%s"
- " IP=%-15s"
- " Name:%-15s"
- " _airplay-p2p=%s%s"
- " _airplay=%s%s%s%s%s"
- " data=<flags=%@ config=%-3u IPv4=%-15s Port=%-5hu>\n"
- " legacy=%-5@ modern=%-5@ eventDispatched=<%@>"
- "%@ %@ event for device id: %llu name: %@ serviceType: %@ %?@\n"
- "%@:%@"
- "%N"
- "-[APDBrowserBluetoothHelper ensureBluetoothPowerChangedListenerStopped]"
- "-[APDBrowserBluetoothHelper ensureBluetoothPowerEventMonitorStarted]"
- "-[APDBrowserBluetoothHelper getBluetoothPowerOn:]"
- "-[APDBrowserBluetoothHelper handleBluetoothChangedNotificationInternal:]"
- "-[APDBrowserBluetoothHelper init]"
- "-[APDBrowserBluetoothHelper invalidate]"
- "-[APDBrowserBluetoothHelper queryBluetoothPower:]"
- "-[APDBrowserBluetoothHelper setBluetoothPower:]"
- "-[APDBrowserBluetoothHelper setPowered:]"
- "-[APDBrowserBluetoothHelper startListeningToEvent:]"
- "-[APDBrowserBluetoothHelper stopListeningToEvent:]"
- "860.7.1"
- "@20@0:8I16"
- "APAdvertiserInfoCopyCFStringFromTXTRecord"
- "APAdvertiserInfoCreateWithRAOPAndAirPlayDataAndDeviceName"
- "APAdvertiserInfoGetBooleanFromTXTRecord"
- "APAdvertiserInfoGetInt64FromTXTRecord"
- "APBonjourBrowserBonjourAirPlayNANFull"
- "APBonjourBrowserBonjourAirPlayNANPartial"
- "APBrokeredReceiverCopyCFStringFromTXTRecord"
- "APBrowserBluetoothManagerEventQueue"
- "APBrowserBluetoothManagerInternalQueue"
- "APDBluetoothHelper"
- "APDBluetoothHelperCreate"
- "APDBrowserBluetoothHelper"
- "APTNANDataSessionRef transportDevice_getNANDataSession(APTransportDeviceRef, APSNANServiceType, OSStatus *)"
- "APTransportConnectionTCPUnbufferedNW"
- "APTransportConnectionTCPUnbufferedNW.%{ptr}"
- "APTransportConnectionTCPUnbufferedNWCreate"
- "APTransportConnectionTCPUnbufferedNWGuts"
- "AllMsgsRecProcessingTotalTimeMs"
- "AllMsgsRoundTripTotalTimeMs"
- "BTLE Update: UUID: %@ RSSI %-3d  Flags %#{flags}  Config %-3u  IP %-15s\n"
- "Bluetooth Bluetooth power check failed.\n"
- "Bluetooth Power Changed"
- "Bluetooth Power Changed Listening Stopped"
- "Bluetooth Power Changed listening stopped.\n"
- "Bluetooth Power state is: %s.\n"
- "Bluetooth helper was invalidated.\n"
- "Bluetooth power changed event.\n"
- "Bluetooth power changed: %s -> %s.\n"
- "Bluetooth power check failed.\n"
- "Boolean tcpunbufnwGuts_connectionHandlePotentialDisconnect(APTransportConnectionTCPUnbufferedNWGutsRef, nw_content_context_t, _Bool, nw_error_t)"
- "CFDictionaryRef _APBonjourBrowserCreateAirPlayEventFromAirPlayTXTRecord(CFDictionaryRef, CFDictionaryRef, CFDataRef)"
- "Connection:[%{ptr}] (TCPUnbufferedNW) %''@ (Not Connected) Parent:[%{ptr}]\n"
- "Connection:[%{ptr}] (TCPUnbufferedNW) %''@ Ports:%##a -> %##a Parent:[%{ptr}]\n"
- "Created nw_listenr [%{ptr}].\n"
- "Device %@ transports: _airplay=%s%s%s%s%s%s%s%s _raop=%s%s%s%s%s%s%s _airplay-p2p=%s%s cached=%s\n"
- "Device ID mismatch: Bonjour (%s) vs TXTRecord (%.*s). Will use TXTRecord deviceID.\n"
- "Device found: %@ Addr: %-15s Port: %-5hu Flags: %#{flags}\n"
- "Dispatching kAPBrowserEvent_IsConfiguredForMaximumDiscoveryStatusChanged.\n"
- "Failed to get bluetooth power.\n"
- "Failed to start browsing for %s over NAN with error: %#m\n"
- "Ignoring BTLE beacon with both IPv4 address and flags set to zero."
- "Injecting bonjourInfo: %@\n"
- "Invalid event type %@.\n"
- "MaximumDiscoveryNeeds_BluetoothRadio"
- "MaximumDiscoveryNeeds_WiFiRadio"
- "NAN _airplay checking for attached data"
- "NAN _airplay conversion beginning"
- "NAN _airplay conversion converted binary TXT record"
- "NAN _airplay conversion finished"
- "NAN _airplay conversion found binary TXT record"
- "NAN _airplay conversion successful"
- "NAN _airplay got endpoint"
- "NAN _airplay obtained custom data"
- "NANDS [%{ptr}] Created with type (%s)"
- "OSStatus APAdvertiserInfoCopyAirPlayP2PDataWithNANServiceType(APAdvertiserInfoRef, APSNANServiceType, CFDataRef *)"
- "OSStatus APTNANDataSessionCreate(APSNANServiceType, APBrowserRef, uint64_t, APTNANDataSessionRef *)"
- "OSStatus APTransportConnectionTCPUnbufferedNWCreate(CFAllocatorRef, CFStringRef, APTransportConnectionFlags, FigThreadPriority, CFDictionaryRef, APTransportConnectionRef *)"
- "OSStatus _APBonjourBrowserStartNANFull(APBonjourBrowserRef, APBonjourBrowserMode, uint32_t *, uint64_t)"
- "OSStatus _APBonjourBrowserStartNANPartial(APBonjourBrowserRef, APBonjourBrowserMode, uint32_t *, uint64_t)"
- "OSStatus _APBonjourBrowserStopBrowsingNANFull(APBonjourBrowserRef, uint32_t *)"
- "OSStatus _APBonjourBrowserStopBrowsingNANPartial(APBonjourBrowserRef, uint32_t *)"
- "OSStatus browser_copyIsConfiguredForMaximumDiscovery(APBrowserRef, CFAllocatorRef, CFBooleanRef *)"
- "OSStatus browser_handleBluetoothHelperEventInternal(APBrowserRef, APDBluetoothHelperEventType, CFDictionaryRef)"
- "OSStatus browser_handleBluetoothPowerChangedEvent(APBrowserRef)"
- "OSStatus browser_removeAirPlayP2PServiceForNearbyDevices(APBrowserRef)"
- "OSStatus browser_updateConfigurationForMaximumDiscoveryStatus(APBrowserRef)"
- "OSStatus queryManagerGetInfo_queryDeviceInternal(APBrowserDeviceQueryManagerRef, CFStringRef, CFStringRef, CFNumberRef, APBrowserDeviceQueryManagerCompletionHandler, void *)"
- "OSStatus queryManagerGetInfo_queryDeviceInternal(APBrowserDeviceQueryManagerRef, CFStringRef, CFStringRef, CFNumberRef, APBrowserDeviceQueryManagerCompletionHandler, void *)_block_invoke"
- "OSStatus session_activateNANDSIfNecessary(FigTransportSessionRef)"
- "OSStatus tcpunbufnwGuts_handleNewConnectionInternal(APTransportConnectionTCPUnbufferedNWGutsRef, nw_connection_t, Boolean)"
- "OSStatus tcpunbufnwGuts_updateStatusInternal(APTransportConnectionTCPUnbufferedNWGutsRef, APTransportConnectionStatus, OSStatus)"
- "OSStatus tcpunbufnw_CopyProperty(CMBaseObjectRef, CFStringRef, CFAllocatorRef, void *)"
- "OSStatus tcpunbufnw_Resume(APTransportConnectionRef)"
- "OSStatus tcpunbufnw_SetProperty(CMBaseObjectRef, CFStringRef, CFTypeRef)"
- "OSStatus tcpunbufnw_SignalDataAvailable(APTransportConnectionRef)_block_invoke"
- "Off"
- "On"
- "OpenFullNANAllowed"
- "Received Bluetooth power notification.\n"
- "Reconfirming RAOP service for device with name %@\n"
- "Reconfirming airplay services for device with name %@\n"
- "Reconfirming alt airplay services for device with name %@\n"
- "Remove AirPlayP2P for device with id: %@ name: %@.\n"
- "Set BT power: %s.\n"
- "Set Bluetooth power failed.\n"
- "Started browsing for %s over NAN\n"
- "Starting bluetooth power listener.\n"
- "Stopped browsing for %s over NAN\n"
- "Stopping bluetooth power listener.\n"
- "TB,N,V_bluetoothPowerChangedListeningStarted"
- "TCPUnbufNW[%{ptr}]::RequestData"
- "T^{OpaqueAPDBluetoothHelper=},N,V_helperRef"
- "Unrecognized Bluetooth helper event %d.\n"
- "Unrecognized event type %d.\n"
- "Unsupported binary TXT record received"
- "UseQUIC"
- "WiFi Power state is: %s.\n"
- "[%@:%@] Creating direct client\n"
- "[%{ptr}] ### TCP send error: %#m\n"
- "[%{ptr}] %s ConnectivityHelper stopped\n"
- "[%{ptr}] %s Failed to %s interface watching %#m\n"
- "[%{ptr}] %s to '%##a' err=%#m"
- "[%{ptr}] APTransportConnectionTCPUnbufferedNW finalized"
- "[%{ptr}] APTransportConnectionTCPUnbufferedNW invalidating"
- "[%{ptr}] APTransportConnectionTCPUnbufferedNW with name %'@ created"
- "[%{ptr}] APTransportSession holds NANDS [%{ptr}] (LL)\n"
- "[%{ptr}] APTransportSession holds NANDS [%{ptr}] (RT)\n"
- "[%{ptr}] Copying local network infomation: Failed to convert interface name '%@'\n"
- "[%{ptr}] Copying local network infomation: Failed to get interface address for '%s'. Error: %#m\n"
- "[%{ptr}] Created NANDS [%{ptr}] (LL)"
- "[%{ptr}] Created NANDS [%{ptr}] (RT)"
- "[%{ptr}] Remote port: %d"
- "[%{ptr}] connected to '%##a' (from '%##a' using '%s' interface) in %1.3f ms"
- "[%{ptr}] nw_connection %s: %s"
- "[%{ptr}] using QUIC"
- "^{OpaqueAPDBluetoothHelper=}"
- "^{OpaqueAPDBluetoothHelper=}16@0:8"
- "_APBonjourBrowserCreateAirPlayEventFromAirPlayTXTRecord"
- "_APBonjourBrowserHandleAirPlayEventOverNAN"
- "_APBonjourBrowserSendAddOrUpdateAirPlayEventsForNANAirPlayService"
- "_APBonjourBrowserSendAirPlayEventsForNANAirPlayEvent"
- "_APBonjourBrowserStartNANFull"
- "_APBonjourBrowserStartNANPartial"
- "_bluetoothPowerChangedListeningStarted"
- "_helperRef"
- "_isBluetoothPoweredOn"
- "allowOpenNANBrowsing"
- "bluetoothPowerChangedListeningStarted"
- "browser_ConfigureForMaximumDiscovery"
- "browser_configureForMaximumDiscovery"
- "browser_copyIsConfiguredForMaximumDiscovery"
- "browser_copyRadiosNeededForMaximumDiscovery"
- "browser_handleBluetoothHelperEventInternal"
- "browser_handleBluetoothPowerChangedEvent"
- "browser_removeAirPlayP2PServiceForNearbyDevices"
- "browser_shouldQueryIPv4Address"
- "browser_updateConfigurationForMaximumDiscoveryStatus"
- "carPlayHelperSession_setInterfaceWatchingEnabled_block_invoke"
- "com.apple.bluetooth.power-changed"
- "created"
- "ensureBluetoothPowerChangedListenerStopped"
- "ensureBluetoothPowerEventMonitorStarted"
- "getBluetoothPowerOn:"
- "getEventString:"
- "handleBluetoothChangedNotificationInternal:"
- "helperRef"
- "i20@0:8I16"
- "i24@0:8^B16"
- "i40@0:8^?16^v24^{OpaqueAPDBluetoothHelper=}32"
- "isConfiguredForMaximumDiscovery"
- "nanFullDiscoveryTimeMs"
- "nanPartialDiscoveryTimeMs"
- "openFullNANAllowed"
- "queryBluetoothPower:"
- "radiosNeededForMaximumDiscovery"
- "reason"
- "setBluetoothPower:"
- "setBluetoothPowerChangedListeningStarted:"
- "setEventHandler:context:helperRef:"
- "setHelperRef:"
- "setPowered:"
- "setSharedInstanceQueue exception: %@.\n"
- "setSharedInstanceQueue:"
- "sharedInstance"
- "startListeningToEvent:"
- "stopListeningToEvent:"
- "tcpunbufnwGuts_callEventCallbackInternal"
- "tcpunbufnwGuts_connectionHandlePackageHeader"
- "tcpunbufnwGuts_connectionHandlePackagePayload"
- "tcpunbufnwGuts_connectionSendPackages"
- "tcpunbufnwGuts_connectionSendPackages_block_invoke"
- "tcpunbufnwGuts_handleNewConnectionGroupInternal"
- "tcpunbufnwGuts_handleNewConnectionInternal"
- "tcpunbufnwGuts_readyToSendBatchSlow"
- "tcpunbufnwGuts_updateStatusInternal"
- "tcpunbufnw_AddEventCallback"
- "tcpunbufnw_CopyProperty"
- "tcpunbufnw_RemoveEventCallback"
- "tcpunbufnw_Resume"
- "tcpunbufnw_Resume_block_invoke"
- "tcpunbufnw_SetProperty"
- "tcpunbufnw_getPackageCallbacksForPackageType"
- "v24@0:8^{OpaqueAPDBluetoothHelper=}16"
- "void _APBonjourBrowserSendAddOrUpdateAirPlayEventsForNANAirPlayService(APBonjourBrowserRef, CFDictionaryRef, CFDictionaryRef)"
- "void _APBonjourBrowserSendAirPlayEventsForNANAirPlayEvent(APBonjourBrowserRef, BonjourBrowserEventType, CFDictionaryRef)"
- "void _APTransportConnectionTCPUnbufferedNWGutsFinalize(CFTypeRef)"
- "void handleBluetoothChangedNotification(CFNotificationCenterRef, void *, CFStringRef, const void *, CFDictionaryRef)"
- "void tcpunbufnwGuts_connectionSendPackages(APTransportConnectionTCPUnbufferedNWGutsRef)"
- "void tcpunbufnwGuts_connectionSendPackages(APTransportConnectionTCPUnbufferedNWGutsRef)_block_invoke"
- "void tcpunbufnwGuts_connectionSendPackages(APTransportConnectionTCPUnbufferedNWGutsRef)_block_invoke_2"
- "void tcpunbufnwGuts_connectionStateChangedHandler(APTransportConnectionTCPUnbufferedNWGutsRef, nw_connection_state_t, nw_error_t)"
- "void tcpunbufnwGuts_invalidateInternal(APTransportConnectionTCPUnbufferedNWGutsRef)"
- "void tcpunbufnwGuts_listenerStateChangedHandler(APTransportConnectionTCPUnbufferedNWListenerContext *, nw_listener_state_t, nw_error_t)"
- "void tcpunbufnwGuts_updatePackageTrackingInternal(APTransportConnectionTCPUnbufferedNWGutsRef, APTransportPackageRef, size_t)"

```
