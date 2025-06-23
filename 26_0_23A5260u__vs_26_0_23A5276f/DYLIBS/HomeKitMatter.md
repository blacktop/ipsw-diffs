## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

```diff

-1323.0.6.0.1
-  __TEXT.__text: 0x13699c
+1334.0.0.0.1
+  __TEXT.__text: 0x13bb64
   __TEXT.__auth_stubs: 0xa40
-  __TEXT.__objc_methlist: 0x9e6c
-  __TEXT.__const: 0x168
+  __TEXT.__objc_methlist: 0x9f94
+  __TEXT.__const: 0x160
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__gcc_except_tab: 0x2b10
-  __TEXT.__cstring: 0x6287
-  __TEXT.__oslogstring: 0x2665c
+  __TEXT.__gcc_except_tab: 0x2b88
+  __TEXT.__cstring: 0x684b
+  __TEXT.__oslogstring: 0x279f9
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x2d28
-  __TEXT.__objc_classname: 0x137b
-  __TEXT.__objc_methname: 0x245b0
-  __TEXT.__objc_methtype: 0x394c
-  __TEXT.__objc_stubs: 0x159e0
-  __DATA_CONST.__got: 0x9a0
-  __DATA_CONST.__const: 0x4580
-  __DATA_CONST.__objc_classlist: 0x3f8
+  __TEXT.__unwind_info: 0x2d60
+  __TEXT.__objc_classname: 0x13be
+  __TEXT.__objc_methname: 0x24ae7
+  __TEXT.__objc_methtype: 0x3997
+  __TEXT.__objc_stubs: 0x15ca0
+  __DATA_CONST.__got: 0x998
+  __DATA_CONST.__const: 0x4658
+  __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68c0
+  __DATA_CONST.__objc_selrefs: 0x6988
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x2d0
-  __DATA_CONST.__objc_arraydata: 0x228
+  __DATA_CONST.__objc_superrefs: 0x2c8
+  __DATA_CONST.__objc_arraydata: 0x230
   __AUTH_CONST.__auth_got: 0x530
-  __AUTH_CONST.__const: 0xf40
-  __AUTH_CONST.__cfstring: 0x6580
-  __AUTH_CONST.__objc_const: 0xec68
-  __AUTH_CONST.__objc_intobj: 0x1638
-  __AUTH_CONST.__objc_arrayobj: 0x180
-  __AUTH_CONST.__objc_doubleobj: 0x20
+  __AUTH_CONST.__const: 0xfa0
+  __AUTH_CONST.__cfstring: 0x6a00
+  __AUTH_CONST.__objc_const: 0xeda8
+  __AUTH_CONST.__objc_intobj: 0x1728
+  __AUTH_CONST.__objc_arrayobj: 0x198
+  __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x1c70
-  __DATA.__objc_ivar: 0xa5c
+  __AUTH.__objc_data: 0x1cc0
+  __DATA.__objc_ivar: 0xa60
   __DATA.__data: 0xd80
-  __DATA.__bss: 0x418
+  __DATA.__bss: 0x428
   __DATA_DIRTY.__objc_data: 0xb40
   __DATA_DIRTY.__bss: 0xb0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B6A42461-DCF0-3E66-A454-8B9E371FA47F
-  Functions: 4114
-  Symbols:   14218
-  CStrings:  9113
+  UUID: 4B89A236-08E3-37B6-829D-430F8C7F97FA
+  Functions: 4126
+  Symbols:   14284
+  CStrings:  9281
 
Symbols:
+ +[HMMTRProtocolMap mapChangeIndicationToFilterChangeIndication:]
+ +[HMMTRSyncClusterActivatedCarbonFilterMonitoring logCategory]
+ +[HMMTRSyncClusterHEPAFilterMonitoring logCategory]
+ +[HMMTRSyncClusterWindowCovering logCategory]
+ -[HMMTRAccessoryConnectionRequest hasPendingLowPriorityConnectionRequest]
+ -[HMMTRAccessoryConnectionRequest initWithQueue:server:priority:completion:]
+ -[HMMTRAccessoryConnectionRequest updateConnectionIdleTime:force:]
+ -[HMMTRAccessoryServer notifyDelegateOfUnauthenticatedAccessoryPromptEnded]
+ -[HMMTRAccessoryServer notifyDelegateOfUnauthenticatedAccessoryPromptStarted]
+ -[HMMTRAccessoryServer readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]
+ -[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]
+ -[HMMTRAccessoryServer(DiagnosticsInternal) generalDiagnosticsClusterFromEndpoints:topology:device:definitelyUnsupported:]
+ -[HMMTRAccessoryServerBrowser _isWedPollingDisabledForTests]
+ -[HMMTRAccessoryServerBrowser _pollWedAccessoriesIfAllowed]
+ -[HMMTRAccessoryServerBrowser connectToAccessoryWhenAllowed:priority:completion:]
+ -[HMMTRDescriptorClusterManager _populateMeasuredValueAttributeForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:]
+ -[HMMTRDescriptorClusterManager hapServiceDescriptionForServiceType:linkedServiceTypes:clustersInUse:endpoint:name:hapToCHIPClusterMappingArray:clusterClassesToQuery:hapServicesToCheckForFeatureMap:hapServicesToCheckForOptionalMatterAttribute:hapServicesToCheckForRequiredAttributeValues:hapCharacteristicsToCheckForRequiredAttributeValues:server:]
+ -[HMMTRDescriptorClusterManager isEndpointPresentForClusterID:endpoint:device:callbackQueue:completionHandler:]
+ -[HMMTRDescriptorClusterManager isEndpointPresentForClusterID:endpoint:mtrDevice:callbackQueue:completionHandler:]
+ -[HMMTRDeviceTopology getHAPLinkedServiceTypesAtEndpoint:]
+ -[HMMTRDeviceTopology hapLinkedServiceTypes]
+ -[HMMTRDeviceTopology setHapLinkedServiceTypes:]
+ -[HMMTRFabricConnectionRequest hasPendingLowPriorityConnectionRequestsOnly]
+ -[HMMTRHAPServiceDescription initWithType:linkedServiceTypes:endpoint:name:]
+ -[HMMTRHAPServiceDescription initWithType:linkedServiceTypes:endpoint:name:optionalServiceLabelIndexIncluded:]
+ -[HMMTRHAPServiceDescription linkedServiceTypes]
+ -[HMMTRMutableDeviceTopology setHAPLinkedServiceTypes:atEndpoint:]
+ -[HMMTRProtocolMap _chipClusterFunctionNameForOperationType:operationDictionary:value:forMTRCluster:forHMMTRCluster:]
+ -[HMMTRProtocolMap getBaseClusterName:]
+ -[HMMTRSoftwareUpdateProvider triggerQueryImageWithPairing:accessoryInitiated:requestParams:completionHandler:]
+ -[HMMTRSyncClusterActivatedCarbonFilterMonitoring readAttributePluginConditionWithParams:]
+ -[HMMTRSyncClusterActivatedCarbonFilterMonitoring updatedValuePluginConditionForAttributeReport:responseHandler:]
+ -[HMMTRSyncClusterColorControl moveToCustomColorTemperatureValue:transitionTime:completionHandler:]
+ -[HMMTRSyncClusterColorControl moveToCustomColorTemperatureWithParams:completionHandler:]
+ -[HMMTRSyncClusterColorControl readColorModeAndColorTemperatureWithCompletion:]
+ -[HMMTRSyncClusterColorControl readColorTemperatureAttributesWithCompletion:]
+ -[HMMTRSyncClusterColorControl readStartUpColorTemperatureWithCompletion:]
+ -[HMMTRSyncClusterColorControl stopMoveToColorTemperatureCommandWithCompletion:]
+ -[HMMTRSyncClusterColorControl supportsColorTemperatureRangeWithMinColorTemperature:maxColorTemperature:completion:]
+ -[HMMTRSyncClusterColorControl writeStartUpColorTemperature:completion:]
+ -[HMMTRSyncClusterColorControl(Test) initWithQueue:]
+ -[HMMTRSyncClusterDoorLock addOrUpdatePinCodeWithValue:forUserIndex:flow:]
+ -[HMMTRSyncClusterDoorLock getAllPinCodesWithFlow:]
+ -[HMMTRSyncClusterDoorLock getMaxPINCodeLengthWithFlow:]
+ -[HMMTRSyncClusterDoorLock getMinPINCodeLengthWithFlow:]
+ -[HMMTRSyncClusterDoorLock removePinCodeForUserIndex:flow:]
+ -[HMMTRSyncClusterDoorLock removeUsersCreatedByOurFabricWithFlow:notInUserUniqueIDs:]
+ -[HMMTRSyncClusterHEPAFilterMonitoring readAttributePluginConditionWithParams:]
+ -[HMMTRSyncClusterHEPAFilterMonitoring updatedValuePluginConditionForAttributeReport:responseHandler:]
+ -[HMMTRSyncClusterWindowCovering readAttributePluginCurrentPositionLiftPercent100thsWithParams:]
+ -[HMMTRSyncClusterWindowCovering readAttributePluginTargetPositionLiftPercent100thsWithParams:]
+ -[HMMTRSyncClusterWindowCovering sendUpOrDownCommand:expectedValueInterval:]
+ -[HMMTRVendorMetadataFileStore initWithFileURL:uarpController:fileManager:preferences:]
+ -[HMMTRVendorMetadataFileStore overrideMetadata]
+ -[HMMTRVendorMetadataFileStore preferences]
+ GCC_except_table1052
+ GCC_except_table1112
+ GCC_except_table1158
+ GCC_except_table1166
+ GCC_except_table1215
+ GCC_except_table1223
+ GCC_except_table1260
+ GCC_except_table1297
+ GCC_except_table1326
+ GCC_except_table1527
+ GCC_except_table1566
+ GCC_except_table1716
+ GCC_except_table1717
+ GCC_except_table1719
+ GCC_except_table1739
+ GCC_except_table1740
+ GCC_except_table1741
+ GCC_except_table1742
+ GCC_except_table1743
+ GCC_except_table1746
+ GCC_except_table1749
+ GCC_except_table1750
+ GCC_except_table1751
+ GCC_except_table1752
+ GCC_except_table1753
+ GCC_except_table1754
+ GCC_except_table1755
+ GCC_except_table1814
+ GCC_except_table1820
+ GCC_except_table1897
+ GCC_except_table2031
+ GCC_except_table2039
+ GCC_except_table2041
+ GCC_except_table2089
+ GCC_except_table2130
+ GCC_except_table2192
+ GCC_except_table2431
+ GCC_except_table2435
+ GCC_except_table2487
+ GCC_except_table2528
+ GCC_except_table2571
+ GCC_except_table2573
+ GCC_except_table2598
+ GCC_except_table2599
+ GCC_except_table2600
+ GCC_except_table2621
+ GCC_except_table2622
+ GCC_except_table2623
+ GCC_except_table2624
+ GCC_except_table2625
+ GCC_except_table2626
+ GCC_except_table2627
+ GCC_except_table2628
+ GCC_except_table2640
+ GCC_except_table2642
+ GCC_except_table2661
+ GCC_except_table2677
+ GCC_except_table2683
+ GCC_except_table2694
+ GCC_except_table2697
+ GCC_except_table2701
+ GCC_except_table2716
+ GCC_except_table2719
+ GCC_except_table2723
+ GCC_except_table2725
+ GCC_except_table2744
+ GCC_except_table2750
+ GCC_except_table2755
+ GCC_except_table2768
+ GCC_except_table2819
+ GCC_except_table2820
+ GCC_except_table3178
+ GCC_except_table3179
+ GCC_except_table3184
+ GCC_except_table3189
+ GCC_except_table3192
+ GCC_except_table3206
+ GCC_except_table3222
+ GCC_except_table3287
+ GCC_except_table3306
+ GCC_except_table3308
+ GCC_except_table3315
+ GCC_except_table3316
+ GCC_except_table3339
+ GCC_except_table3340
+ GCC_except_table3349
+ GCC_except_table3372
+ GCC_except_table3375
+ GCC_except_table3383
+ GCC_except_table3402
+ GCC_except_table3405
+ GCC_except_table3441
+ GCC_except_table3445
+ GCC_except_table3461
+ GCC_except_table3463
+ GCC_except_table3481
+ GCC_except_table3544
+ GCC_except_table3588
+ GCC_except_table3606
+ GCC_except_table3629
+ GCC_except_table3633
+ GCC_except_table3648
+ GCC_except_table3649
+ GCC_except_table3654
+ GCC_except_table3661
+ GCC_except_table3718
+ GCC_except_table3738
+ GCC_except_table3792
+ GCC_except_table3797
+ GCC_except_table3800
+ GCC_except_table3879
+ GCC_except_table3880
+ GCC_except_table3935
+ GCC_except_table3938
+ GCC_except_table4000
+ GCC_except_table4062
+ GCC_except_table4066
+ GCC_except_table4070
+ GCC_except_table4073
+ GCC_except_table4106
+ GCC_except_table424
+ GCC_except_table499
+ GCC_except_table678
+ GCC_except_table682
+ GCC_except_table743
+ GCC_except_table744
+ GCC_except_table745
+ GCC_except_table813
+ GCC_except_table876
+ GCC_except_table880
+ GCC_except_table882
+ GCC_except_table884
+ GCC_except_table886
+ GCC_except_table890
+ GCC_except_table894
+ GCC_except_table897
+ GCC_except_table940
+ GCC_except_table944
+ GCC_except_table946
+ _HMFPreferenceAllowVendorDataOverride
+ _OBJC_CLASS_$_HMMTRSyncClusterActivatedCarbonFilterMonitoring
+ _OBJC_CLASS_$_HMMTRSyncClusterHEPAFilterMonitoring
+ _OBJC_CLASS_$_MTRClusterActivatedCarbonFilterMonitoring
+ _OBJC_CLASS_$_MTRClusterHEPAFilterMonitoring
+ _OBJC_IVAR_$_HMMTRDeviceTopology._hapLinkedServiceTypes
+ _OBJC_IVAR_$_HMMTRHAPServiceDescription._linkedServiceTypes
+ _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._preferences
+ _OBJC_METACLASS_$_HMMTRSyncClusterActivatedCarbonFilterMonitoring
+ _OBJC_METACLASS_$_HMMTRSyncClusterHEPAFilterMonitoring
+ _OBJC_METACLASS_$_MTRClusterActivatedCarbonFilterMonitoring
+ _OBJC_METACLASS_$_MTRClusterHEPAFilterMonitoring
+ __OBJC_$_CLASS_METHODS_HMMTRSyncClusterActivatedCarbonFilterMonitoring
+ __OBJC_$_CLASS_METHODS_HMMTRSyncClusterHEPAFilterMonitoring
+ __OBJC_$_CLASS_METHODS_HMMTRSyncClusterWindowCovering
+ __OBJC_$_INSTANCE_METHODS_HMMTRSyncClusterActivatedCarbonFilterMonitoring
+ __OBJC_$_INSTANCE_METHODS_HMMTRSyncClusterColorControl(Test)
+ __OBJC_$_INSTANCE_METHODS_HMMTRSyncClusterHEPAFilterMonitoring
+ __OBJC_$_PROP_LIST_HMMTRSyncClusterActivatedCarbonFilterMonitoring
+ __OBJC_$_PROP_LIST_HMMTRSyncClusterHEPAFilterMonitoring
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRSyncClusterActivatedCarbonFilterMonitoring
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRSyncClusterHEPAFilterMonitoring
+ __OBJC_CLASS_RO_$_HMMTRSyncClusterActivatedCarbonFilterMonitoring
+ __OBJC_CLASS_RO_$_HMMTRSyncClusterHEPAFilterMonitoring
+ __OBJC_METACLASS_RO_$_HMMTRSyncClusterActivatedCarbonFilterMonitoring
+ __OBJC_METACLASS_RO_$_HMMTRSyncClusterHEPAFilterMonitoring
+ ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.811
+ ___102-[HMMTRAccessoryServer updateAllCharacteristicValuesPostHAPServiceEnumerationForAccessory:completion:]_block_invoke.770
+ ___102-[HMMTRSyncClusterDoorLock updateSchedulesForUserIndex:withWeekDaySchedules:andYearDaySchedules:flow:]_block_invoke.273
+ ___107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.202
+ ___107-[HMMTRSyncClusterDoorLock setScheduleOfScheduleType:withSchedule:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke.350
+ ___109-[HMMTRDescriptorClusterManager fetchHAPCategoryForCHIPDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.127
+ ___109-[HMMTRDescriptorClusterManager fetchHAPCategoryWithMTRDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.132
+ ___109-[HMMTRDescriptorClusterManager fetchHAPServicesWithMTRDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.121
+ ___109-[HMMTRDescriptorClusterManager fetchHAPServicesWithMTRDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.123
+ ___109-[HMMTRDescriptorClusterManager fetchHAPServicesWithMTRDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke_2.124
+ ___110-[HMMTRAccessoryServerBrowser removeAllDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.204
+ ___111-[HMMTRDescriptorClusterManager isEndpointPresentForClusterID:endpoint:device:callbackQueue:completionHandler:]_block_invoke
+ ___111-[HMMTRSoftwareUpdateProvider triggerQueryImageWithPairing:accessoryInitiated:requestParams:completionHandler:]_block_invoke
+ ___112-[HMMTRAccessoryServer _updateAdditionalCharacteristicsFromCharacteristicUpdate:service:path:completionHandler:]_block_invoke.376
+ ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.887
+ ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.890
+ ___114-[HMMTRProtocolMap _selectedServiceTypeForServiceArray:device:mtrDevice:endpoint:callbackQueue:completionHandler:]_block_invoke.422
+ ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.256
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.497
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.498
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.499
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.500
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.503
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.506
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.501
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.504
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_3.502
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_3.505
+ ___119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.200
+ ___125-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:requireFullScheduleAudit:flow:]_block_invoke.271
+ ___125-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:requireFullScheduleAudit:flow:]_block_invoke.272
+ ___131-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:device:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.341
+ ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.108
+ ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.113
+ ___134-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:mtrDevice:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.342
+ ___147-[HMMTRProtocolOperationManager registerOperation:accessoryServer:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:]_block_invoke.119
+ ___147-[HMMTRProtocolOperationManager registerOperation:accessoryServer:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:]_block_invoke.120
+ ___147-[HMMTRProtocolOperationManager registerOperation:accessoryServer:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:]_block_invoke.121
+ ___147-[HMMTRProtocolOperationManager registerOperation:accessoryServer:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:]_block_invoke.125
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.319
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.320
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.321
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.322
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.323
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.324
+ ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.352
+ ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.356
+ ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke_2.353
+ ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.316
+ ___278-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.187
+ ___280-[HMMTRDescriptorClusterManager _verifyHAPCharacteristicSupportAtCHIPEndpoint:device:endpointDeviceTypes:callbackQueue:clusterClassToQueryForFeatureMap:hapServicesToCheckForFeatureMap:hapServicesInUse:deviceTopology:bridgeAggregateNodeEndpoint:server:lastError:completionHandler:]_block_invoke.295
+ ___37-[HMMTRAccessoryServer finishPairing]_block_invoke.750
+ ___37-[HMMTRAccessoryServer timerDidFire:]_block_invoke.273
+ ___38-[HMMTROTAAnnounceTimer timerDidFire:]_block_invoke.9
+ ___39-[HMMTRSyncClusterDoorLock getAllUsers]_block_invoke.267
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.625
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.626
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.627
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.628
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.630
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.634
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.635
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.636
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.637
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.629
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.638
+ ___40-[HMMTRAccessoryServerBrowser configure]_block_invoke.131
+ ___42-[HMMTRAccessoryServer _setupMatterDevice]_block_invoke.304
+ ___43-[HMMTRAccessoryServer _setupThreadPairing]_block_invoke.459
+ ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke.296
+ ___43-[HMMTRAccessoryServer discoverAccessories]_block_invoke.299
+ ___45+[HMMTRSyncClusterWindowCovering logCategory]_block_invoke
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.861
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.863
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.864
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.866
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke_2.862
+ ___45-[HMMTRAccessoryServer stopPairingWithError:]_block_invoke.285
+ ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.950
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.835
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.838
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.840
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.839
+ ___49-[HMMTRAccessoryServerBrowser startBluetoothScan]_block_invoke.355
+ ___51+[HMMTRSyncClusterHEPAFilterMonitoring logCategory]_block_invoke
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.794
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.798
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.799
+ ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.951
+ ___51-[HMMTRSyncClusterDoorLock getAllPinCodesWithFlow:]_block_invoke
+ ___51-[HMMTRSyncClusterDoorLock getAllPinCodesWithFlow:]_block_invoke.217
+ ___51-[HMMTRSyncClusterDoorLock getAllPinCodesWithFlow:]_block_invoke.220
+ ___51-[HMMTRSyncClusterDoorLock getAllPinCodesWithFlow:]_block_invoke.222
+ ___51-[HMMTRSyncClusterDoorLock getAllPinCodesWithFlow:]_block_invoke_2
+ ___51-[HMMTRSyncClusterDoorLock getAllPinCodesWithFlow:]_block_invoke_2.225
+ ___51-[HMMTRSyncClusterDoorLock getAllPinCodesWithFlow:]_block_invoke_3
+ ___51-[HMMTRSyncClusterDoorLock getAllPinCodesWithFlow:]_block_invoke_3.230
+ ___51-[HMMTRSyncClusterDoorLock getAllPinCodesWithFlow:]_block_invoke_4
+ ___52-[HMMTRAccessoryServer populateACLEntriesForPairing]_block_invoke.623
+ ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.306
+ ___53-[HMMTRAccessoryServer _tryPairingUsingMatterSupport]_block_invoke.250
+ ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.949
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.417
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.418
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.419
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.420
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.421
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.422
+ ___56-[HMMTRSyncClusterDoorLock getMaxPINCodeLengthWithFlow:]_block_invoke
+ ___56-[HMMTRSyncClusterDoorLock getMinPINCodeLengthWithFlow:]_block_invoke
+ ___57-[HMMTRSyncClusterDoorLock _removeUserWithUniqueID:flow:]_block_invoke.200
+ ___58-[HMMTRProtocolMap _buildEventMapper:characteristicsDict:]_block_invoke.297
+ ___58-[HMMTRSyncClusterDoorLock addOrUpdateReaderKeyData:flow:]_block_invoke.245
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.429
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.430
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.431
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.433
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.434
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.435
+ ___59-[HMMTRAccessoryServerBrowser _pollWedAccessoriesIfAllowed]_block_invoke
+ ___59-[HMMTRSyncClusterDoorLock readSchedulesForUserIndex:flow:]_block_invoke.274
+ ___59-[HMMTRSyncClusterDoorLock removePinCodeForUserIndex:flow:]_block_invoke
+ ___59-[HMMTRSyncClusterDoorLock removePinCodeForUserIndex:flow:]_block_invoke.235
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.892
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.894
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.898
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.900
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.423
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.424
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.425
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.426
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.427
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.428
+ ___62+[HMMTRSyncClusterActivatedCarbonFilterMonitoring logCategory]_block_invoke
+ ___62-[HMMTRAccessoryServerBrowser stopDiscoveringAccessoryServers]_block_invoke.176
+ ___62-[HMMTRSyncClusterDoorLock readAliroSupportedVersionWithFlow:]_block_invoke.277
+ ___62-[HMMTRSyncClusterDoorLock readAliroSupportedVersionWithFlow:]_block_invoke.278
+ ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.792
+ ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.793
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.477
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.478
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.479
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.480
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.481
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.482
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.447
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.448
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.449
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.450
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.451
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.913
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.914
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.915
+ ___64-[HMMTRAccessoryServerBrowser _initializeAndStartBonjourBrowser]_block_invoke.139
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.442
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.443
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.444
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.445
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.446
+ ___66-[HMMTRSyncClusterDoorLock fetchAvailableUserSlotsWithLimit:flow:]_block_invoke.318
+ ___67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke.248
+ ___67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke.252
+ ___67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke.255
+ ___67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke.259
+ ___67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke_2.256
+ ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.436
+ ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.437
+ ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.438
+ ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.441
+ ___68-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:userType:flow:]_block_invoke.312
+ ___68-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:userType:flow:]_block_invoke.314
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.466
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.467
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.468
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.471
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.475
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.476
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.409
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.414
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.415
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.416
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.177
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.182
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.184
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke_2.183
+ ___71-[HMMTRAccessoryServer validateAttestationDeviceInfo:error:completion:]_block_invoke.275
+ ___71-[HMMTRIdentifyDevice _processChildNodesForEndpoint:completionHandler:]_block_invoke.73
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.394
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.400
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.401
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.402
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.460
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.461
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.462
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.464
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.465
+ ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.262
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.787
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.788
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.790
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.791
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.771
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.772
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.782
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.783
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.785
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.786
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.845
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.846
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.850
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke_2.852
+ ___74-[HMMTRSyncClusterDoorLock addOrUpdateIssuerKeyData:forUserUniqueID:flow:]_block_invoke.262
+ ___74-[HMMTRSyncClusterDoorLock addOrUpdateIssuerKeyData:forUserUniqueID:flow:]_block_invoke.263
+ ___74-[HMMTRSyncClusterDoorLock addOrUpdateIssuerKeyData:forUserUniqueID:flow:]_block_invoke.264
+ ___74-[HMMTRSyncClusterDoorLock addOrUpdatePinCodeWithValue:forUserIndex:flow:]_block_invoke
+ ___74-[HMMTRSyncClusterDoorLock addOrUpdatePinCodeWithValue:forUserIndex:flow:]_block_invoke.231
+ ___74-[HMMTRSyncClusterDoorLock addOrUpdatePinCodeWithValue:forUserIndex:flow:]_block_invoke_2
+ ___74-[HMMTRSyncClusterDoorLock addOrUpdatePinCodeWithValue:forUserIndex:flow:]_block_invoke_3
+ ___74-[HMMTRSyncClusterDoorLock addOrUpdatePinCodeWithValue:forUserIndex:flow:]_block_invoke_4
+ ___75+[HMMTRSyncClusterDoorLock validateFutureResults:ofClass:areNullable:flow:]_block_invoke.299
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.288
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.289
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.290
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.291
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.294
+ ___76-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithNodeID:completion:]_block_invoke.185
+ ___76-[HMMTRIdentifyDevice _childNodesWithIdentifyForEndpoint:completionHandler:]_block_invoke.68
+ ___76-[HMMTRIdentifyDevice _childNodesWithIdentifyForEndpoint:completionHandler:]_block_invoke.69
+ ___76-[HMMTRSyncClusterWindowCovering sendUpOrDownCommand:expectedValueInterval:]_block_invoke
+ ___76-[HMMTRSyncClusterWindowCovering sendUpOrDownCommand:expectedValueInterval:]_block_invoke.2
+ ___78-[HMMTRIdentifyDevice identifyBridgeWithAggregatorEndpoint:completionHandler:]_block_invoke.74
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.403
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.404
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.405
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.407
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.408
+ ___79-[HMMTRAccessoryServerBrowser _updateAccessoryControlListForServer:completion:]_block_invoke.311
+ ___79-[HMMTRSyncClusterDoorLock clearAllUsersWithDeletedCreatorFabricIndexWithFlow:]_block_invoke.241
+ ___79-[HMMTRSyncClusterDoorLock clearAllUsersWithDeletedCreatorFabricIndexWithFlow:]_block_invoke_2.242
+ ___80-[HMMTRSyncClusterColorControl stopMoveToColorTemperatureCommandWithCompletion:]_block_invoke
+ ___80-[HMMTRSyncClusterDoorLock addDeviceCredentialKeyData:ofType:forUserIndex:flow:]_block_invoke.247
+ ___81-[HMMTRAccessoryServerBrowser connectToAccessoryWhenAllowed:priority:completion:]_block_invoke
+ ___82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.901
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.869
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.870
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.871
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.874
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke_2.873
+ ___82-[HMMTRAccessoryServer(Diagnostics) resetWiFiNetworkDiagnosticsCountForAccessory:]_block_invoke.217
+ ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.151
+ ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.153
+ ___82-[HMMTRProtocolMap _buildValueMapper:characteristicsDict:operation:forMTRCluster:]_block_invoke.276
+ ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.812
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.380
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.382
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.875
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.876
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.877
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.878
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.882
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.883
+ ___84-[HMMTRAccessoryServer(Diagnostics) resetThreadNetworkDiagnosticsCountForAccessory:]_block_invoke.215
+ ___85-[HMMTRSyncClusterDoorLock removeUsersCreatedByOurFabricWithFlow:notInUserUniqueIDs:]_block_invoke
+ ___85-[HMMTRSyncClusterDoorLock removeUsersCreatedByOurFabricWithFlow:notInUserUniqueIDs:]_block_invoke.193
+ ___85-[HMMTRSyncClusterDoorLock removeUsersCreatedByOurFabricWithFlow:notInUserUniqueIDs:]_block_invoke.194
+ ___85-[HMMTRSyncClusterDoorLock removeUsersCreatedByOurFabricWithFlow:notInUserUniqueIDs:]_block_invoke.196
+ ___85-[HMMTRSyncClusterDoorLock removeUsersCreatedByOurFabricWithFlow:notInUserUniqueIDs:]_block_invoke.197
+ ___85-[HMMTRSyncClusterDoorLock removeUsersCreatedByOurFabricWithFlow:notInUserUniqueIDs:]_block_invoke_2
+ ___85-[HMMTRSyncClusterDoorLock removeUsersCreatedByOurFabricWithFlow:notInUserUniqueIDs:]_block_invoke_3
+ ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.916
+ ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.917
+ ___86-[HMMTRSyncClusterDoorLock addPinCredentialAtIndex:withValue:forUserAtUserIndex:flow:]_block_invoke.337
+ ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.347
+ ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.348
+ ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.349
+ ___89-[HMMTRSyncClusterColorControl moveToCustomColorTemperatureWithParams:completionHandler:]_block_invoke
+ ___89-[HMMTRSyncClusterDoorLock updatePinCredentialAtIndex:withValue:forUserAtUserIndex:flow:]_block_invoke.338
+ ___90-[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:flow:]_block_invoke.201
+ ___90-[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:flow:]_block_invoke_2.202
+ ___90-[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:flow:]_block_invoke_3.203
+ ___90-[HMMTRSyncClusterDoorLock fetchAvailableCredentialSlotsWithLimit:forCredentialType:flow:]_block_invoke.316
+ ___91-[HMMTRProtocolMap servicesForDeviceTypes:device:endpoint:callbackQueue:completionHandler:]_block_invoke.425
+ ___92-[HMMTRAccessoryServer _createFirmwareUpdateServiceWithInstanceID:device:completionHandler:]_block_invoke.763
+ ___92-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]_block_invoke.309
+ ___92-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]_block_invoke.310
+ ___93-[HMMTRDescriptorClusterManager endpointForClusterID:device:callbackQueue:completionHandler:]_block_invoke.391
+ ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.810
+ ___94-[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:]_block_invoke.160
+ ___94-[HMMTRSyncClusterDoorLock getScheduleOfScheduleType:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke.357
+ ___94-[HMMTRSyncClusterDoorLock getScheduleOfScheduleType:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke_2.362
+ ___96-[HMMTRDescriptorClusterManager endpointForClusterID:mtrDevice:callbackQueue:completionHandler:]_block_invoke.393
+ ___96-[HMMTRProtocolMap servicesOfMTRDevice:forDeviceTypes:endpoint:callbackQueue:completionHandler:]_block_invoke.426
+ ___96-[HMMTRSyncClusterDoorLock addCredentialData:forCredentialType:atIndex:forUserAtUserIndex:flow:]_block_invoke.339
+ ___96-[HMMTRSyncClusterDoorLock clearScheduleOfScheduleType:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke.349
+ ___97-[HMMTRAccessoryServerBrowser removeAccessoryServer:fromDiscoveredAccessoryServerListWithReason:]_block_invoke.294
+ ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.253
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.507
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.508
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.509
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.510
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.512
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.513
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke_2
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke_2.511
+ ___99-[HMMTRSyncClusterColorControl moveToCustomColorTemperatureValue:transitionTime:completionHandler:]_block_invoke
+ ___99-[HMMTRSyncClusterDoorLock updateCredentialData:forCredentialType:atIndex:forUserAtUserIndex:flow:]_block_invoke.340
+ ___Block_byref_object_copy_.10045
+ ___Block_byref_object_copy_.10788
+ ___Block_byref_object_copy_.11480
+ ___Block_byref_object_copy_.12174
+ ___Block_byref_object_copy_.12338
+ ___Block_byref_object_copy_.1776
+ ___Block_byref_object_copy_.3135
+ ___Block_byref_object_copy_.3416
+ ___Block_byref_object_copy_.4552
+ ___Block_byref_object_copy_.5713
+ ___Block_byref_object_copy_.7556
+ ___Block_byref_object_copy_.7975
+ ___Block_byref_object_copy_.9085
+ ___Block_byref_object_dispose_.10046
+ ___Block_byref_object_dispose_.10789
+ ___Block_byref_object_dispose_.11481
+ ___Block_byref_object_dispose_.12175
+ ___Block_byref_object_dispose_.12339
+ ___Block_byref_object_dispose_.1777
+ ___Block_byref_object_dispose_.3136
+ ___Block_byref_object_dispose_.3417
+ ___Block_byref_object_dispose_.4553
+ ___Block_byref_object_dispose_.5714
+ ___Block_byref_object_dispose_.7557
+ ___Block_byref_object_dispose_.7976
+ ___Block_byref_object_dispose_.9086
+ ___block_descriptor_145_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136bs_e46_v32?0"NSArray"8"NSDictionary"16"NSError"24ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8s136l8
+ ___block_descriptor_40_e8_32s_e49_B16?0"MTRDoorLockClusterGetUserResponseParams"8ls32l8
+ ___block_descriptor_40_e8_32w_e68_v24?0"HMMTRSoftwareUpdateProviderQueryResponseParams"8"NSError"16lw32l8
+ ___block_descriptor_48_e8_32s40s_e60_"HMFFuture"16?0"MTRDoorLockClusterGetUserResponseParams"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e16_"HMFFuture"8?0ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e43_{_HMFFutureBlockOutcome=q}16?0"NSArray"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e5_v8?0ls32l8r56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e20_v20?0B8"NSError"12ls56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e5_v8?0lr56l8s48l8s32l8s40l8r64l8
+ ___block_descriptor_72_e8_32s40s48r56r64w_e35_v24?0"THCredentials"8"NSError"16lw64l8s32l8r48l8r56l8s40l8
+ ___block_descriptor_72_e8_32s40s48r56r64w_e5_v8?0lw64l8r48l8s32l8r56l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e46_v32?0"NSArray"8"NSDictionary"16"NSError"24lr56l8r64l8s32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e5_v8?0ls32l8s40l8s48l8r64l8r72l8s56l8
+ ___block_descriptor_96_e8_32s40s48s56bs64r72r80r88r_e5_v8?0ls32l8r64l8s40l8s48l8s56l8r72l8r80l8r88l8
+ ___block_literal_global.10526
+ ___block_literal_global.11078
+ ___block_literal_global.11303
+ ___block_literal_global.1134
+ ___block_literal_global.11515
+ ___block_literal_global.11653
+ ___block_literal_global.11782
+ ___block_literal_global.11999
+ ___block_literal_global.124
+ ___block_literal_global.1250
+ ___block_literal_global.134
+ ___block_literal_global.1356
+ ___block_literal_global.1433
+ ___block_literal_global.1650
+ ___block_literal_global.1899
+ ___block_literal_global.1953
+ ___block_literal_global.1999
+ ___block_literal_global.204
+ ___block_literal_global.2085
+ ___block_literal_global.224
+ ___block_literal_global.234
+ ___block_literal_global.237
+ ___block_literal_global.2451
+ ___block_literal_global.250
+ ___block_literal_global.254
+ ___block_literal_global.258
+ ___block_literal_global.2590
+ ___block_literal_global.261
+ ___block_literal_global.266
+ ___block_literal_global.276
+ ___block_literal_global.283
+ ___block_literal_global.284
+ ___block_literal_global.2896
+ ___block_literal_global.298
+ ___block_literal_global.300
+ ___block_literal_global.303
+ ___block_literal_global.303.9042
+ ___block_literal_global.3039
+ ___block_literal_global.305
+ ___block_literal_global.3068
+ ___block_literal_global.307
+ ___block_literal_global.3160
+ ___block_literal_global.327
+ ___block_literal_global.3311
+ ___block_literal_global.336
+ ___block_literal_global.344
+ ___block_literal_global.3503
+ ___block_literal_global.359
+ ___block_literal_global.360
+ ___block_literal_global.363
+ ___block_literal_global.367
+ ___block_literal_global.3675
+ ___block_literal_global.370
+ ___block_literal_global.3799
+ ___block_literal_global.400
+ ___block_literal_global.43
+ ___block_literal_global.4313
+ ___block_literal_global.4646
+ ___block_literal_global.49
+ ___block_literal_global.4938
+ ___block_literal_global.494
+ ___block_literal_global.5072
+ ___block_literal_global.5173
+ ___block_literal_global.540
+ ___block_literal_global.5430
+ ___block_literal_global.5602
+ ___block_literal_global.58
+ ___block_literal_global.5840
+ ___block_literal_global.5970
+ ___block_literal_global.6111
+ ___block_literal_global.614
+ ___block_literal_global.6220
+ ___block_literal_global.6254
+ ___block_literal_global.6275
+ ___block_literal_global.6525
+ ___block_literal_global.6538
+ ___block_literal_global.6632
+ ___block_literal_global.6726
+ ___block_literal_global.6820
+ ___block_literal_global.6923
+ ___block_literal_global.7017
+ ___block_literal_global.7111
+ ___block_literal_global.7252
+ ___block_literal_global.7357
+ ___block_literal_global.7426
+ ___block_literal_global.75.9842
+ ___block_literal_global.768
+ ___block_literal_global.775
+ ___block_literal_global.7758
+ ___block_literal_global.7986
+ ___block_literal_global.8319
+ ___block_literal_global.8443
+ ___block_literal_global.8576
+ ___block_literal_global.861
+ ___block_literal_global.9117
+ ___block_literal_global.946
+ ___block_literal_global.9521
+ ___block_literal_global.958
+ ___block_literal_global.9841
+ ___block_literal_global.9917
+ _logCategory._hmf_once_t0.3038
+ _logCategory._hmf_once_t0.5601
+ _logCategory._hmf_once_t0.6253
+ _logCategory._hmf_once_t106
+ _logCategory._hmf_once_t13.3159
+ _logCategory._hmf_once_t13.3502
+ _logCategory._hmf_once_t14.1265
+ _logCategory._hmf_once_t14.358
+ _logCategory._hmf_once_t14.6537
+ _logCategory._hmf_once_t14.6631
+ _logCategory._hmf_once_t14.6725
+ _logCategory._hmf_once_t14.6922
+ _logCategory._hmf_once_t14.7016
+ _logCategory._hmf_once_t14.7110
+ _logCategory._hmf_once_t2.5172
+ _logCategory._hmf_once_t2.6219
+ _logCategory._hmf_once_t2.7251
+ _logCategory._hmf_once_t2.9916
+ _logCategory._hmf_once_t20.11652
+ _logCategory._hmf_once_t202
+ _logCategory._hmf_once_t26.6819
+ _logCategory._hmf_once_t27
+ _logCategory._hmf_once_t280
+ _logCategory._hmf_once_t3.1355
+ _logCategory._hmf_once_t3.1432
+ _logCategory._hmf_once_t30
+ _logCategory._hmf_once_t31.11781
+ _logCategory._hmf_once_t32
+ _logCategory._hmf_once_t370
+ _logCategory._hmf_once_t4.3674
+ _logCategory._hmf_once_t4.7356
+ _logCategory._hmf_once_t6.2084
+ _logCategory._hmf_once_t671
+ _logCategory._hmf_once_t8.11302
+ _logCategory._hmf_once_t8.8442
+ _logCategory._hmf_once_t9.5969
+ _logCategory._hmf_once_v1.3040
+ _logCategory._hmf_once_v1.5603
+ _logCategory._hmf_once_v1.6255
+ _logCategory._hmf_once_v10.5971
+ _logCategory._hmf_once_v107
+ _logCategory._hmf_once_v14.3161
+ _logCategory._hmf_once_v14.3504
+ _logCategory._hmf_once_v15.1266
+ _logCategory._hmf_once_v15.360
+ _logCategory._hmf_once_v15.6539
+ _logCategory._hmf_once_v15.6633
+ _logCategory._hmf_once_v15.6727
+ _logCategory._hmf_once_v15.6924
+ _logCategory._hmf_once_v15.7018
+ _logCategory._hmf_once_v15.7112
+ _logCategory._hmf_once_v203
+ _logCategory._hmf_once_v21.11654
+ _logCategory._hmf_once_v27.6821
+ _logCategory._hmf_once_v28
+ _logCategory._hmf_once_v281
+ _logCategory._hmf_once_v3.5174
+ _logCategory._hmf_once_v3.6221
+ _logCategory._hmf_once_v3.7253
+ _logCategory._hmf_once_v3.9918
+ _logCategory._hmf_once_v31
+ _logCategory._hmf_once_v32.11783
+ _logCategory._hmf_once_v33
+ _logCategory._hmf_once_v371
+ _logCategory._hmf_once_v4.1357
+ _logCategory._hmf_once_v4.1434
+ _logCategory._hmf_once_v5.3676
+ _logCategory._hmf_once_v5.7358
+ _logCategory._hmf_once_v672
+ _logCategory._hmf_once_v7.2086
+ _logCategory._hmf_once_v9.11304
+ _logCategory._hmf_once_v9.8444
+ _objc_msgSend$URLWithString:relativeToURL:
+ _objc_msgSend$_chipClusterFunctionNameForOperationType:operationDictionary:value:forMTRCluster:forHMMTRCluster:
+ _objc_msgSend$_isWedPollingDisabledForTests
+ _objc_msgSend$_pollWedAccessoriesIfAllowed
+ _objc_msgSend$_populateMeasuredValueAttributeForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:
+ _objc_msgSend$absoluteURL
+ _objc_msgSend$connectToAccessoryWhenAllowed:priority:completion:
+ _objc_msgSend$getBaseClusterName:
+ _objc_msgSend$getHAPLinkedServiceTypesAtEndpoint:
+ _objc_msgSend$hapLinkedServiceTypes
+ _objc_msgSend$hapServiceDescriptionForServiceType:linkedServiceTypes:clustersInUse:endpoint:name:hapToCHIPClusterMappingArray:clusterClassesToQuery:hapServicesToCheckForFeatureMap:hapServicesToCheckForOptionalMatterAttribute:hapServicesToCheckForRequiredAttributeValues:hapCharacteristicsToCheckForRequiredAttributeValues:server:
+ _objc_msgSend$hasPendingLowPriorityConnectionRequest
+ _objc_msgSend$hasPendingLowPriorityConnectionRequestsOnly
+ _objc_msgSend$initWithFileURL:uarpController:fileManager:preferences:
+ _objc_msgSend$initWithQueue:server:priority:completion:
+ _objc_msgSend$initWithType:linkedServiceTypes:endpoint:name:optionalServiceLabelIndexIncluded:
+ _objc_msgSend$isEndpointPresentForClusterID:endpoint:mtrDevice:callbackQueue:completionHandler:
+ _objc_msgSend$linkedServiceTypes
+ _objc_msgSend$mapChangeIndicationToFilterChangeIndication:
+ _objc_msgSend$moveToColorTemperatureWithParams:expectedValues:expectedValueInterval:completion:
+ _objc_msgSend$notifyDelegateOfUnauthenticatedAccessoryPromptEnded
+ _objc_msgSend$notifyDelegateOfUnauthenticatedAccessoryPromptStarted
+ _objc_msgSend$notifyUnauthenticatedMatterAccessoryPromptEnded
+ _objc_msgSend$notifyUnauthenticatedMatterAccessoryPromptStarted
+ _objc_msgSend$overrideMetadata
+ _objc_msgSend$pathExtension
+ _objc_msgSend$preferences
+ _objc_msgSend$primaryAccessoryCategoryForNodeID:
+ _objc_msgSend$queryImageWithPairing:requestParams:queue:accessoryInitiated:completionHandler:
+ _objc_msgSend$readAttributeColorCapabilitiesWithParams:
+ _objc_msgSend$readAttributeConditionWithParams:
+ _objc_msgSend$readAttributeCurrentPositionLiftPercent100thsWithParams:
+ _objc_msgSend$readAttributeCurrentPositionTiltPercent100thsWithParams:
+ _objc_msgSend$readAttributeDegradationDirectionWithParams:
+ _objc_msgSend$readAttributeMaxMeasuredValueWithParams:
+ _objc_msgSend$readAttributeMinMeasuredValueWithParams:
+ _objc_msgSend$readAttributeRemainingTimeWithParams:
+ _objc_msgSend$readAttributeStartUpColorTemperatureMiredsWithParams:
+ _objc_msgSend$readAttributeTargetPositionLiftPercent100thsWithParams:
+ _objc_msgSend$readAttributeTargetPositionTiltPercent100thsWithParams:
+ _objc_msgSend$sendUpOrDownCommand:expectedValueInterval:
+ _objc_msgSend$setHAPLinkedServiceTypes:atEndpoint:
+ _objc_msgSend$stopMoveStepWithParams:expectedValues:expectedValueInterval:completion:
+ _objc_msgSend$stringByAppendingPathExtension:
+ _objc_msgSend$stringByDeletingPathExtension
+ _objc_msgSend$triggerQueryImageWithPairing:accessoryInitiated:requestParams:completionHandler:
+ _objc_msgSend$updateConnectionIdleTime:force:
+ _objc_msgSend$writeAttributePluginTargetPositionTiltWithSetValue:expectedValueInterval:
+ _objc_msgSend$writeAttributeStartUpColorTemperatureMiredsWithValue:expectedValueInterval:params:
- +[HMMTRColorControl logCategory]
- -[HMMTRAccessoryServer _startInitialReachableStateTimerWithCompletion:]
- -[HMMTRAccessoryServer _updateMetrics]
- -[HMMTRAccessoryServer initialMTRDeviceStateTimeoutId]
- -[HMMTRAccessoryServer pairingTimer]
- -[HMMTRAccessoryServer readCharacteristicValues:timeout:completionQueue:completionHandler:]
- -[HMMTRAccessoryServer setInitialMTRDeviceStateTimeoutId:]
- -[HMMTRAccessoryServer setPairingTimer:]
- -[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]
- -[HMMTRAccessoryServer(Diagnostics) generalDiagnosticsClusterFromEndpoints:topology:device:definitelyUnsupported:]
- -[HMMTRColorControl initWithDevice:endpointID:queue:]
- -[HMMTRColorControl logIdentifier]
- -[HMMTRColorControl moveToCustomColorTemperatureValue:transitionTime:completionHandler:]
- -[HMMTRColorControl moveToCustomColorTemperatureWithParams:completionHandler:]
- -[HMMTRColorControl moveToPluginColorTemperatureWithParams:completionHandler:]
- -[HMMTRColorControl readAttributePluginColorTemperatureMiredsWithCompletionHandler:]
- -[HMMTRColorControl readColorModeAndColorTemperatureWithCompletion:]
- -[HMMTRColorControl readColorTemperatureAttributesWithCompletion:queue:]
- -[HMMTRColorControl readStartUpColorTemperatureWithCompletion:]
- -[HMMTRColorControl stopMoveToColorTemperatureCommandWithCompletion:]
- -[HMMTRColorControl subscribeAttributeReportForColorModeWithCompletion:]
- -[HMMTRColorControl supportsColorTemperatureRangeWithMinColorTemperature:maxColorTemperature:completion:queue:]
- -[HMMTRColorControl writeStartUpColorTemperature:completion:]
- -[HMMTRColorControl(Test) initWithQueue:]
- -[HMMTRDescriptorClusterManager hapServiceDescriptionForServiceType:clustersInUse:endpoint:name:hapToCHIPClusterMappingArray:clusterClassesToQuery:hapServicesToCheckForFeatureMap:hapServicesToCheckForOptionalMatterAttribute:hapServicesToCheckForRequiredAttributeValues:hapCharacteristicsToCheckForRequiredAttributeValues:server:]
- -[HMMTRDescriptorClusterManager queryEndpointForClusterID:endpoint:device:callbackQueue:completionHandler:]
- -[HMMTRHAPServiceDescription initWithType:endpoint:name:]
- -[HMMTRHAPServiceDescription initWithType:endpoint:name:optionalServiceLabelIndexIncluded:]
- -[HMMTRProtocolMap _chipClusterFunctionNameForOperationType:operationDictionary:value:forMTRCluster:]
- -[HMMTRSoftwareUpdateProvider notifyDelegateOfQueryImageWithPairing:requestParams:completionHandler:]
- -[HMMTRSyncClusterDoorLock addOrUpdatePinCodeWithValue:forUserIndex:]
- -[HMMTRSyncClusterDoorLock getAllPinCodes]
- -[HMMTRSyncClusterDoorLock getMaxPINCodeLength]
- -[HMMTRSyncClusterDoorLock getMinPINCodeLength]
- -[HMMTRSyncClusterDoorLock removePinCodeForUserIndex:]
- -[HMMTRVendorMetadataFileStore initWithFileURL:uarpController:fileManager:]
- GCC_except_table1010
- GCC_except_table1070
- GCC_except_table1116
- GCC_except_table1124
- GCC_except_table1173
- GCC_except_table1181
- GCC_except_table1218
- GCC_except_table1255
- GCC_except_table1480
- GCC_except_table1519
- GCC_except_table1669
- GCC_except_table1670
- GCC_except_table1672
- GCC_except_table1691
- GCC_except_table1692
- GCC_except_table1693
- GCC_except_table1694
- GCC_except_table1695
- GCC_except_table1698
- GCC_except_table1701
- GCC_except_table1702
- GCC_except_table1703
- GCC_except_table1704
- GCC_except_table1705
- GCC_except_table1706
- GCC_except_table1707
- GCC_except_table1766
- GCC_except_table1772
- GCC_except_table1849
- GCC_except_table1970
- GCC_except_table1997
- GCC_except_table2026
- GCC_except_table2034
- GCC_except_table2036
- GCC_except_table2083
- GCC_except_table2123
- GCC_except_table2185
- GCC_except_table2424
- GCC_except_table2428
- GCC_except_table2480
- GCC_except_table2521
- GCC_except_table2564
- GCC_except_table2566
- GCC_except_table2591
- GCC_except_table2592
- GCC_except_table2593
- GCC_except_table2611
- GCC_except_table2612
- GCC_except_table2613
- GCC_except_table2614
- GCC_except_table2615
- GCC_except_table2616
- GCC_except_table2617
- GCC_except_table2618
- GCC_except_table2630
- GCC_except_table2632
- GCC_except_table2651
- GCC_except_table2667
- GCC_except_table2673
- GCC_except_table2684
- GCC_except_table2687
- GCC_except_table2691
- GCC_except_table2706
- GCC_except_table2709
- GCC_except_table2713
- GCC_except_table2715
- GCC_except_table2734
- GCC_except_table2740
- GCC_except_table2745
- GCC_except_table2757
- GCC_except_table2808
- GCC_except_table2809
- GCC_except_table3169
- GCC_except_table3170
- GCC_except_table3171
- GCC_except_table3175
- GCC_except_table3183
- GCC_except_table3197
- GCC_except_table3213
- GCC_except_table3279
- GCC_except_table3294
- GCC_except_table3296
- GCC_except_table3303
- GCC_except_table3304
- GCC_except_table3327
- GCC_except_table3328
- GCC_except_table3337
- GCC_except_table3360
- GCC_except_table3363
- GCC_except_table3371
- GCC_except_table3390
- GCC_except_table3393
- GCC_except_table3429
- GCC_except_table3433
- GCC_except_table3449
- GCC_except_table3451
- GCC_except_table3469
- GCC_except_table3532
- GCC_except_table3576
- GCC_except_table3593
- GCC_except_table3618
- GCC_except_table3622
- GCC_except_table3637
- GCC_except_table3638
- GCC_except_table3643
- GCC_except_table3650
- GCC_except_table3708
- GCC_except_table3728
- GCC_except_table3782
- GCC_except_table3787
- GCC_except_table3790
- GCC_except_table3867
- GCC_except_table3868
- GCC_except_table3923
- GCC_except_table3926
- GCC_except_table3988
- GCC_except_table403
- GCC_except_table4050
- GCC_except_table4054
- GCC_except_table4058
- GCC_except_table4061
- GCC_except_table4094
- GCC_except_table470
- GCC_except_table640
- GCC_except_table643
- GCC_except_table703
- GCC_except_table704
- GCC_except_table705
- GCC_except_table771
- GCC_except_table834
- GCC_except_table838
- GCC_except_table840
- GCC_except_table842
- GCC_except_table844
- GCC_except_table848
- GCC_except_table852
- GCC_except_table855
- GCC_except_table898
- GCC_except_table902
- GCC_except_table904
- _OBJC_CLASS_$_HMMTRColorControl
- _OBJC_CLASS_$_MTRBaseClusterColorControl
- _OBJC_CLASS_$_MTRSubscribeParams
- _OBJC_IVAR_$_HMMTRAccessoryServer._initialMTRDeviceStateTimeoutId
- _OBJC_IVAR_$_HMMTRAccessoryServer._pairingTimer
- _OBJC_METACLASS_$_HMMTRColorControl
- _OBJC_METACLASS_$_MTRBaseClusterColorControl
- __OBJC_$_CLASS_METHODS_HMMTRColorControl
- __OBJC_$_INSTANCE_METHODS_HMMTRColorControl(Test)
- __OBJC_$_INSTANCE_METHODS_HMMTRSyncClusterColorControl
- __OBJC_$_PROP_LIST_HMMTRColorControl
- __OBJC_CLASS_PROTOCOLS_$_HMMTRColorControl
- __OBJC_CLASS_RO_$_HMMTRColorControl
- __OBJC_METACLASS_RO_$_HMMTRColorControl
- ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.794
- ___101-[HMMTRSoftwareUpdateProvider notifyDelegateOfQueryImageWithPairing:requestParams:completionHandler:]_block_invoke
- ___102-[HMMTRAccessoryServer updateAllCharacteristicValuesPostHAPServiceEnumerationForAccessory:completion:]_block_invoke.753
- ___102-[HMMTRSyncClusterDoorLock updateSchedulesForUserIndex:withWeekDaySchedules:andYearDaySchedules:flow:]_block_invoke.267
- ___103-[HMMTRSyncClusterWindowCovering writeAttributePluginTargetPositionWithSetValue:expectedValueInterval:]_block_invoke.4
- ___103-[HMMTRSyncClusterWindowCovering writeAttributePluginTargetPositionWithSetValue:expectedValueInterval:]_block_invoke.5
- ___107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.198
- ___107-[HMMTRDescriptorClusterManager queryEndpointForClusterID:endpoint:device:callbackQueue:completionHandler:]_block_invoke
- ___107-[HMMTRSyncClusterDoorLock setScheduleOfScheduleType:withSchedule:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke.344
- ___107-[HMMTRSyncClusterWindowCovering writeAttributePluginTargetPositionTiltWithSetValue:expectedValueInterval:]_block_invoke.7
- ___107-[HMMTRSyncClusterWindowCovering writeAttributePluginTargetPositionTiltWithSetValue:expectedValueInterval:]_block_invoke.8
- ___109-[HMMTRDescriptorClusterManager fetchHAPCategoryForCHIPDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.124
- ___109-[HMMTRDescriptorClusterManager fetchHAPCategoryWithMTRDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.129
- ___109-[HMMTRDescriptorClusterManager fetchHAPServicesWithMTRDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.117
- ___109-[HMMTRDescriptorClusterManager fetchHAPServicesWithMTRDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.118
- ___109-[HMMTRDescriptorClusterManager fetchHAPServicesWithMTRDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke_2.121
- ___110-[HMMTRAccessoryServerBrowser removeAllDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.200
- ___111-[HMMTRColorControl supportsColorTemperatureRangeWithMinColorTemperature:maxColorTemperature:completion:queue:]_block_invoke
- ___111-[HMMTRColorControl supportsColorTemperatureRangeWithMinColorTemperature:maxColorTemperature:completion:queue:]_block_invoke.4
- ___111-[HMMTRColorControl supportsColorTemperatureRangeWithMinColorTemperature:maxColorTemperature:completion:queue:]_block_invoke.5
- ___111-[HMMTRColorControl supportsColorTemperatureRangeWithMinColorTemperature:maxColorTemperature:completion:queue:]_block_invoke.6
- ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.866
- ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.869
- ___114-[HMMTRProtocolMap _selectedServiceTypeForServiceArray:device:mtrDevice:endpoint:callbackQueue:completionHandler:]_block_invoke.411
- ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.258
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.483
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.484
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.485
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.486
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.489
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.492
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.487
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.490
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_3.488
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_3.491
- ___119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.196
- ___125-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:requireFullScheduleAudit:flow:]_block_invoke.265
- ___125-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:requireFullScheduleAudit:flow:]_block_invoke.266
- ___131-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:device:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.285
- ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.105
- ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.107
- ___134-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:mtrDevice:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.286
- ___147-[HMMTRProtocolOperationManager registerOperation:accessoryServer:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:]_block_invoke.116
- ___147-[HMMTRProtocolOperationManager registerOperation:accessoryServer:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:]_block_invoke.117
- ___147-[HMMTRProtocolOperationManager registerOperation:accessoryServer:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:]_block_invoke.118
- ___147-[HMMTRProtocolOperationManager registerOperation:accessoryServer:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:]_block_invoke.122
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.310
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.311
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.313
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.314
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.315
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.318
- ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.296
- ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.299
- ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke_2.297
- ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.260
- ___278-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.183
- ___280-[HMMTRDescriptorClusterManager _verifyHAPCharacteristicSupportAtCHIPEndpoint:device:endpointDeviceTypes:callbackQueue:clusterClassToQueryForFeatureMap:hapServicesToCheckForFeatureMap:hapServicesInUse:deviceTopology:bridgeAggregateNodeEndpoint:server:lastError:completionHandler:]_block_invoke.239
- ___32+[HMMTRColorControl logCategory]_block_invoke
- ___37-[HMMTRAccessoryServer finishPairing]_block_invoke.733
- ___37-[HMMTRAccessoryServer timerDidFire:]_block_invoke.277
- ___39-[HMMTRSyncClusterDoorLock getAllUsers]_block_invoke.261
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.611
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.612
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.613
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.614
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.616
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.620
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.621
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.622
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.623
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.615
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.624
- ___40-[HMMTRAccessoryServerBrowser configure]_block_invoke.128
- ___42-[HMMTRAccessoryServer _setupMatterDevice]_block_invoke.307
- ___42-[HMMTRAccessoryServer _setupMatterDevice]_block_invoke.309
- ___42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke
- ___42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.211
- ___42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.214
- ___42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.216
- ___42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke_2
- ___42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke_2.219
- ___42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke_3
- ___42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke_3.224
- ___42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke_4
- ___43-[HMMTRAccessoryServer _setupThreadPairing]_block_invoke.445
- ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke.300
- ___43-[HMMTRAccessoryServer discoverAccessories]_block_invoke.303
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.844
- ___45-[HMMTRAccessoryServer stopPairingWithError:]_block_invoke.289
- ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.930
- ___47-[HMMTRSyncClusterDoorLock getMaxPINCodeLength]_block_invoke
- ___47-[HMMTRSyncClusterDoorLock getMinPINCodeLength]_block_invoke
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.818
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.821
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.823
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.822
- ___49-[HMMTRAccessoryServerBrowser startBluetoothScan]_block_invoke.349
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.777
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.781
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.782
- ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.931
- ___52-[HMMTRAccessoryServer populateACLEntriesForPairing]_block_invoke.609
- ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.300
- ___53-[HMMTRAccessoryServer _tryPairingUsingMatterSupport]_block_invoke.251
- ___54-[HMMTRSyncClusterDoorLock removePinCodeForUserIndex:]_block_invoke
- ___54-[HMMTRSyncClusterDoorLock removePinCodeForUserIndex:]_block_invoke.229
- ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.929
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.403
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.404
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.405
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.406
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.407
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.408
- ___57-[HMMTRSyncClusterDoorLock _removeUserWithUniqueID:flow:]_block_invoke.194
- ___58-[HMMTRProtocolMap _buildEventMapper:characteristicsDict:]_block_invoke.287
- ___58-[HMMTRSyncClusterDoorLock addOrUpdateReaderKeyData:flow:]_block_invoke.239
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.415
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.416
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.417
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.419
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.420
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.421
- ___59-[HMMTRSyncClusterDoorLock readSchedulesForUserIndex:flow:]_block_invoke.268
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.871
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.873
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.877
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.879
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.409
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.410
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.411
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.412
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.413
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.414
- ___61-[HMMTRColorControl writeStartUpColorTemperature:completion:]_block_invoke
- ___62-[HMMTRAccessoryServerBrowser stopDiscoveringAccessoryServers]_block_invoke.172
- ___62-[HMMTRSyncClusterDoorLock readAliroSupportedVersionWithFlow:]_block_invoke.271
- ___62-[HMMTRSyncClusterDoorLock readAliroSupportedVersionWithFlow:]_block_invoke.272
- ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.775
- ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.776
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.463
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.464
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.465
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.466
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.467
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.468
- ___63-[HMMTRColorControl readStartUpColorTemperatureWithCompletion:]_block_invoke
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.433
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.434
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.435
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.436
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.437
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.893
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.894
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.895
- ___64-[HMMTRAccessoryServerBrowser _initializeAndStartBonjourBrowser]_block_invoke.135
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.428
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.429
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.430
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.431
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.432
- ___66-[HMMTRSyncClusterDoorLock fetchAvailableUserSlotsWithLimit:flow:]_block_invoke.312
- ___67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke.242
- ___67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke.246
- ___67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke.249
- ___67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke.253
- ___67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke_2.250
- ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.422
- ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.423
- ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.424
- ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.427
- ___68-[HMMTRColorControl readColorModeAndColorTemperatureWithCompletion:]_block_invoke
- ___68-[HMMTRColorControl readColorModeAndColorTemperatureWithCompletion:]_block_invoke_2
- ___68-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:userType:flow:]_block_invoke.306
- ___68-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:userType:flow:]_block_invoke.308
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.452
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.453
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.454
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.457
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.461
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.462
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.395
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.400
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.401
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.402
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.173
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.176
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.178
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke_2.179
- ___69-[HMMTRColorControl stopMoveToColorTemperatureCommandWithCompletion:]_block_invoke
- ___69-[HMMTRColorControl stopMoveToColorTemperatureCommandWithCompletion:]_block_invoke_2
- ___69-[HMMTRSyncClusterDoorLock addOrUpdatePinCodeWithValue:forUserIndex:]_block_invoke
- ___69-[HMMTRSyncClusterDoorLock addOrUpdatePinCodeWithValue:forUserIndex:]_block_invoke.225
- ___69-[HMMTRSyncClusterDoorLock addOrUpdatePinCodeWithValue:forUserIndex:]_block_invoke_2
- ___69-[HMMTRSyncClusterDoorLock addOrUpdatePinCodeWithValue:forUserIndex:]_block_invoke_3
- ___69-[HMMTRSyncClusterDoorLock addOrUpdatePinCodeWithValue:forUserIndex:]_block_invoke_4
- ___71-[HMMTRAccessoryServer validateAttestationDeviceInfo:error:completion:]_block_invoke.279
- ___71-[HMMTRIdentifyDevice _processChildNodesForEndpoint:completionHandler:]_block_invoke.70
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.380
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.386
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.387
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.388
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.446
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.447
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.448
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.450
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.451
- ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.266
- ___72-[HMMTRColorControl readColorTemperatureAttributesWithCompletion:queue:]_block_invoke
- ___72-[HMMTRColorControl readColorTemperatureAttributesWithCompletion:queue:]_block_invoke_2
- ___72-[HMMTRColorControl readColorTemperatureAttributesWithCompletion:queue:]_block_invoke_3
- ___72-[HMMTRColorControl readColorTemperatureAttributesWithCompletion:queue:]_block_invoke_4
- ___72-[HMMTRColorControl subscribeAttributeReportForColorModeWithCompletion:]_block_invoke
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.770
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.771
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.773
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.774
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.754
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.755
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.765
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.766
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.768
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.769
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.828
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.829
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.833
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke_2.835
- ___74-[HMMTRSyncClusterDoorLock addOrUpdateIssuerKeyData:forUserUniqueID:flow:]_block_invoke.256
- ___74-[HMMTRSyncClusterDoorLock addOrUpdateIssuerKeyData:forUserUniqueID:flow:]_block_invoke.257
- ___74-[HMMTRSyncClusterDoorLock addOrUpdateIssuerKeyData:forUserUniqueID:flow:]_block_invoke.258
- ___75+[HMMTRSyncClusterDoorLock validateFutureResults:ofClass:areNullable:flow:]_block_invoke.293
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.294
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.296
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.297
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.295
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.298
- ___76-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithNodeID:completion:]_block_invoke.181
- ___76-[HMMTRIdentifyDevice _childNodesWithIdentifyForEndpoint:completionHandler:]_block_invoke.63
- ___76-[HMMTRIdentifyDevice _childNodesWithIdentifyForEndpoint:completionHandler:]_block_invoke.65
- ___78-[HMMTRColorControl moveToCustomColorTemperatureWithParams:completionHandler:]_block_invoke
- ___78-[HMMTRColorControl moveToPluginColorTemperatureWithParams:completionHandler:]_block_invoke
- ___78-[HMMTRIdentifyDevice identifyBridgeWithAggregatorEndpoint:completionHandler:]_block_invoke.71
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.389
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.390
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.391
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.393
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.394
- ___79-[HMMTRAccessoryServerBrowser _updateAccessoryControlListForServer:completion:]_block_invoke.305
- ___79-[HMMTRSyncClusterDoorLock clearAllUsersWithDeletedCreatorFabricIndexWithFlow:]_block_invoke.235
- ___79-[HMMTRSyncClusterDoorLock clearAllUsersWithDeletedCreatorFabricIndexWithFlow:]_block_invoke_2.236
- ___80-[HMMTRSyncClusterDoorLock addDeviceCredentialKeyData:ofType:forUserIndex:flow:]_block_invoke.241
- ___82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.880
- ___82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.882
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.848
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.849
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.850
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.853
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke_2.852
- ___82-[HMMTRAccessoryServer(Diagnostics) resetWiFiNetworkDiagnosticsCountForAccessory:]_block_invoke.214
- ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.147
- ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.149
- ___82-[HMMTRProtocolMap _buildValueMapper:characteristicsDict:operation:forMTRCluster:]_block_invoke.266
- ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.795
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.366
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.368
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.854
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.855
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.856
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.857
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.861
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.862
- ___84-[HMMTRAccessoryServer(Diagnostics) resetThreadNetworkDiagnosticsCountForAccessory:]_block_invoke.212
- ___84-[HMMTRColorControl readAttributePluginColorTemperatureMiredsWithCompletionHandler:]_block_invoke
- ___84-[HMMTRColorControl readAttributePluginColorTemperatureMiredsWithCompletionHandler:]_block_invoke.14
- ___85-[HMMTRAccessoryServerBrowser connectToAccessoryWhenAllowed:highPriority:completion:]_block_invoke
- ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.896
- ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.897
- ___86-[HMMTRSyncClusterDoorLock addPinCredentialAtIndex:withValue:forUserAtUserIndex:flow:]_block_invoke.331
- ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.341
- ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.342
- ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.343
- ___88-[HMMTRColorControl moveToCustomColorTemperatureValue:transitionTime:completionHandler:]_block_invoke
- ___89-[HMMTRSyncClusterDoorLock updatePinCredentialAtIndex:withValue:forUserAtUserIndex:flow:]_block_invoke.332
- ___90-[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:flow:]_block_invoke.195
- ___90-[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:flow:]_block_invoke_2.196
- ___90-[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:flow:]_block_invoke_3.197
- ___90-[HMMTRSyncClusterDoorLock fetchAvailableCredentialSlotsWithLimit:forCredentialType:flow:]_block_invoke.310
- ___91-[HMMTRProtocolMap servicesForDeviceTypes:device:endpoint:callbackQueue:completionHandler:]_block_invoke.414
- ___92-[HMMTRAccessoryServer _createFirmwareUpdateServiceWithInstanceID:device:completionHandler:]_block_invoke.746
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.493
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.494
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.495
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.496
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.498
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.499
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke_2
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke_2.497
- ___92-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]_block_invoke.303
- ___92-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]_block_invoke.304
- ___93-[HMMTRDescriptorClusterManager endpointForClusterID:device:callbackQueue:completionHandler:]_block_invoke.334
- ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.793
- ___94-[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:]_block_invoke.156
- ___94-[HMMTRSyncClusterDoorLock getScheduleOfScheduleType:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke.351
- ___94-[HMMTRSyncClusterDoorLock getScheduleOfScheduleType:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke_2.356
- ___96-[HMMTRDescriptorClusterManager endpointForClusterID:mtrDevice:callbackQueue:completionHandler:]_block_invoke.336
- ___96-[HMMTRProtocolMap servicesOfMTRDevice:forDeviceTypes:endpoint:callbackQueue:completionHandler:]_block_invoke.415
- ___96-[HMMTRSyncClusterDoorLock addCredentialData:forCredentialType:atIndex:forUserAtUserIndex:flow:]_block_invoke.333
- ___96-[HMMTRSyncClusterDoorLock clearScheduleOfScheduleType:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke.343
- ___97-[HMMTRAccessoryServerBrowser removeAccessoryServer:fromDiscoveredAccessoryServerListWithReason:]_block_invoke.290
- ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.255
- ___99-[HMMTRSyncClusterDoorLock updateCredentialData:forCredentialType:atIndex:forUserAtUserIndex:flow:]_block_invoke.334
- ___Block_byref_object_copy_.10592
- ___Block_byref_object_copy_.11263
- ___Block_byref_object_copy_.11961
- ___Block_byref_object_copy_.12127
- ___Block_byref_object_copy_.1553
- ___Block_byref_object_copy_.2907
- ___Block_byref_object_copy_.3186
- ___Block_byref_object_copy_.4274
- ___Block_byref_object_copy_.5430
- ___Block_byref_object_copy_.7071
- ___Block_byref_object_copy_.7417
- ___Block_byref_object_copy_.7837
- ___Block_byref_object_copy_.8927
- ___Block_byref_object_copy_.9879
- ___Block_byref_object_dispose_.10593
- ___Block_byref_object_dispose_.11264
- ___Block_byref_object_dispose_.11962
- ___Block_byref_object_dispose_.12128
- ___Block_byref_object_dispose_.1554
- ___Block_byref_object_dispose_.2908
- ___Block_byref_object_dispose_.3187
- ___Block_byref_object_dispose_.4275
- ___Block_byref_object_dispose_.5431
- ___Block_byref_object_dispose_.7072
- ___Block_byref_object_dispose_.7418
- ___Block_byref_object_dispose_.7838
- ___Block_byref_object_dispose_.8928
- ___Block_byref_object_dispose_.9880
- ___block_descriptor_145_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8s136l8
- ___block_descriptor_48_e8_32s_e16_"HMFFuture"8?0ls32l8
- ___block_descriptor_56_e8_32s40s48bs_e16_"HMFFuture"8?0ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48r_e30_v24?0"NSNumber"8"NSError"16ls32l8r48l8s40l8
- ___block_descriptor_64_e8_32s40s48bs56r_e5_v8?0lr56l8s48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48r56r_e30_v24?0"NSNumber"8"NSError"16lr48l8s32l8r56l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56r_e29_v24?0"NSArray"8"NSError"16lr56l8s32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56w_e35_v24?0"THCredentials"8"NSError"16lw56l8s32l8s40l8s48l8
- ___block_descriptor_88_e8_32s40s48s56bs64r72r80r_e5_v8?0ls32l8r64l8s40l8s48l8s56l8r72l8r80l8
- ___block_descriptor_96_e8_32s40s48s56bs64r72r80r88r_e5_v8?0ls32l8r64l8r72l8r80l8s40l8s48l8r88l8s56l8
- ___block_literal_global.1026
- ___block_literal_global.10331
- ___block_literal_global.10859
- ___block_literal_global.11084
- ___block_literal_global.1130
- ___block_literal_global.11300
- ___block_literal_global.11437
- ___block_literal_global.11570
- ___block_literal_global.11788
- ___block_literal_global.1208
- ___block_literal_global.131
- ___block_literal_global.132
- ___block_literal_global.1421
- ___block_literal_global.1674
- ___block_literal_global.1726
- ___block_literal_global.1772
- ___block_literal_global.1860
- ___block_literal_global.197
- ___block_literal_global.218
- ___block_literal_global.222
- ___block_literal_global.2222
- ___block_literal_global.231
- ___block_literal_global.2362
- ___block_literal_global.238
- ___block_literal_global.245
- ___block_literal_global.252
- ___block_literal_global.255
- ___block_literal_global.260
- ___block_literal_global.2668
- ___block_literal_global.268
- ___block_literal_global.270
- ___block_literal_global.280
- ___block_literal_global.2811
- ___block_literal_global.2840
- ___block_literal_global.292
- ___block_literal_global.2932
- ___block_literal_global.296
- ___block_literal_global.297
- ___block_literal_global.299
- ___block_literal_global.301
- ___block_literal_global.3085
- ___block_literal_global.315
- ___block_literal_global.321
- ___block_literal_global.3279
- ___block_literal_global.338
- ___block_literal_global.3421
- ___block_literal_global.343
- ___block_literal_global.348
- ___block_literal_global.3532
- ___block_literal_global.357
- ___block_literal_global.358
- ___block_literal_global.361
- ___block_literal_global.40
- ___block_literal_global.4037
- ___block_literal_global.412
- ___block_literal_global.4365
- ___block_literal_global.46.9679
- ___block_literal_global.4654
- ___block_literal_global.4788
- ___block_literal_global.485
- ___block_literal_global.4889
- ___block_literal_global.5147
- ___block_literal_global.5319
- ___block_literal_global.5556
- ___block_literal_global.5686
- ___block_literal_global.5922
- ___block_literal_global.5956
- ___block_literal_global.5977
- ___block_literal_global.6227
- ___block_literal_global.6239
- ___block_literal_global.6335
- ___block_literal_global.6432
- ___block_literal_global.651
- ___block_literal_global.6528
- ___block_literal_global.6636
- ___block_literal_global.6733
- ___block_literal_global.6830
- ___block_literal_global.6974
- ___block_literal_global.7113
- ___block_literal_global.7223
- ___block_literal_global.7294
- ___block_literal_global.743
- ___block_literal_global.75.9680
- ___block_literal_global.751
- ___block_literal_global.758
- ___block_literal_global.7621
- ___block_literal_global.7848
- ___block_literal_global.8179
- ___block_literal_global.8302
- ___block_literal_global.84
- ___block_literal_global.8434
- ___block_literal_global.8957
- ___block_literal_global.909
- ___block_literal_global.9359
- ___block_literal_global.938
- ___block_literal_global.9678
- ___block_literal_global.9757
- _logCategory._hmf_once_t0.2810
- _logCategory._hmf_once_t0.5318
- _logCategory._hmf_once_t0.5955
- _logCategory._hmf_once_t10.11787
- _logCategory._hmf_once_t13.2931
- _logCategory._hmf_once_t13.3278
- _logCategory._hmf_once_t195
- _logCategory._hmf_once_t2.4888
- _logCategory._hmf_once_t2.5921
- _logCategory._hmf_once_t2.6973
- _logCategory._hmf_once_t2.9756
- _logCategory._hmf_once_t20.11436
- _logCategory._hmf_once_t22
- _logCategory._hmf_once_t23.6334
- _logCategory._hmf_once_t23.6431
- _logCategory._hmf_once_t23.6635
- _logCategory._hmf_once_t23.6732
- _logCategory._hmf_once_t23.6829
- _logCategory._hmf_once_t26.1420
- _logCategory._hmf_once_t274
- _logCategory._hmf_once_t3.1129
- _logCategory._hmf_once_t3.1207
- _logCategory._hmf_once_t31.11569
- _logCategory._hmf_once_t356
- _logCategory._hmf_once_t4.3420
- _logCategory._hmf_once_t4.7222
- _logCategory._hmf_once_t44
- _logCategory._hmf_once_t5
- _logCategory._hmf_once_t6.1771
- _logCategory._hmf_once_t6.1859
- _logCategory._hmf_once_t663
- _logCategory._hmf_once_t8.11083
- _logCategory._hmf_once_t87.10833
- _logCategory._hmf_once_t9.5685
- _logCategory._hmf_once_v1.2812
- _logCategory._hmf_once_v1.5320
- _logCategory._hmf_once_v1.5957
- _logCategory._hmf_once_v10.5687
- _logCategory._hmf_once_v11.11789
- _logCategory._hmf_once_v14.2933
- _logCategory._hmf_once_v14.3280
- _logCategory._hmf_once_v196
- _logCategory._hmf_once_v21.11438
- _logCategory._hmf_once_v23
- _logCategory._hmf_once_v24.6336
- _logCategory._hmf_once_v24.6433
- _logCategory._hmf_once_v24.6637
- _logCategory._hmf_once_v24.6734
- _logCategory._hmf_once_v24.6831
- _logCategory._hmf_once_v27.1422
- _logCategory._hmf_once_v275
- _logCategory._hmf_once_v3.4890
- _logCategory._hmf_once_v3.5923
- _logCategory._hmf_once_v3.6975
- _logCategory._hmf_once_v3.9758
- _logCategory._hmf_once_v32.11571
- _logCategory._hmf_once_v357
- _logCategory._hmf_once_v4.1131
- _logCategory._hmf_once_v4.1209
- _logCategory._hmf_once_v45
- _logCategory._hmf_once_v5.3422
- _logCategory._hmf_once_v5.7224
- _logCategory._hmf_once_v6
- _logCategory._hmf_once_v664
- _logCategory._hmf_once_v7.1773
- _logCategory._hmf_once_v7.1861
- _logCategory._hmf_once_v88.10834
- _logCategory._hmf_once_v9.11085
- _objc_msgSend$_chipClusterFunctionNameForOperationType:operationDictionary:value:forMTRCluster:
- _objc_msgSend$_startInitialReachableStateTimerWithCompletion:
- _objc_msgSend$_updateMetrics
- _objc_msgSend$cancelCommissioningForNodeID:error:
- _objc_msgSend$hapServiceDescriptionForServiceType:clustersInUse:endpoint:name:hapToCHIPClusterMappingArray:clusterClassesToQuery:hapServicesToCheckForFeatureMap:hapServicesToCheckForOptionalMatterAttribute:hapServicesToCheckForRequiredAttributeValues:hapCharacteristicsToCheckForRequiredAttributeValues:server:
- _objc_msgSend$initWithMinInterval:maxInterval:
- _objc_msgSend$initWithType:endpoint:name:optionalServiceLabelIndexIncluded:
- _objc_msgSend$initialMTRDeviceStateTimeoutId
- _objc_msgSend$moveToColorTemperatureWithParams:completion:
- _objc_msgSend$moveToColorTemperatureWithParams:completionHandler:
- _objc_msgSend$notifyDelegateOfQueryImageWithPairing:requestParams:completionHandler:
- _objc_msgSend$pairingTimer
- _objc_msgSend$queryEndpointForClusterID:endpoint:device:callbackQueue:completionHandler:
- _objc_msgSend$queryImageWithPairing:requestParams:queue:completionHandler:
- _objc_msgSend$readAttributeColorCapabilitiesWithCompletion:
- _objc_msgSend$readAttributeColorModeWithCompletion:
- _objc_msgSend$readAttributeColorModeWithCompletionHandler:
- _objc_msgSend$readAttributeColorTempPhysicalMaxMiredsWithCompletion:
- _objc_msgSend$readAttributeColorTempPhysicalMinMiredsWithCompletion:
- _objc_msgSend$readAttributeColorTemperatureMiredsWithCompletion:
- _objc_msgSend$readAttributeRemainingTimeWithCompletion:
- _objc_msgSend$readAttributeStartUpColorTemperatureMiredsWithCompletion:
- _objc_msgSend$setInitialMTRDeviceStateTimeoutId:
- _objc_msgSend$setPairingTimer:
- _objc_msgSend$stopMoveStepWithParams:completion:
- _objc_msgSend$subscribeAttributeColorModeWithParams:subscriptionEstablished:reportHandler:
- _objc_msgSend$writeAttributeStartUpColorTemperatureMiredsWithValue:completion:
- _productId
- _vendorId
CStrings:
+ "\f"
+ "%{public}@Accessory does not support expected color temp range"
+ "%{public}@Accessory supports expected color temp range"
+ "%{public}@All selected linked service types: %@"
+ "%{public}@An error occurred while trying to read Degradation Direction attribute from MTRClusterActivatedCarbonFilterMonitoring cluster"
+ "%{public}@An error occurred while trying to read Degradation Direction attribute from MTRClusterHEPAFilterMonitoring cluster"
+ "%{public}@Cannot get the status of the software update, ignore calling announceOTAProvider cmd %@."
+ "%{public}@Error: Invalid %@ value read for Condition attribute from MTRClusterActivatedCarbonFilterMonitoring cluster"
+ "%{public}@Error: Invalid %@ value read for Condition attribute from MTRClusterHEPAFilterMonitoring cluster"
+ "%{public}@Error: Invalid %@ value read for Degradation Direction attribute from MTRClusterActivatedCarbonFilterMonitoring cluster"
+ "%{public}@Error: Invalid %@ value read for Degradation Direction attribute from MTRClusterHEPAFilterMonitoring cluster"
+ "%{public}@Error: Invalid %@ value received from Condition attribute report for MTRClusterActivatedCarbonFilterMonitoring cluster"
+ "%{public}@Error: Invalid %@ value received from Condition attribute report for MTRClusterHEPAFilterMonitoring cluster"
+ "%{public}@Error: Invalid nil value read for Condition attribute from MTRClusterActivatedCarbonFilterMonitoring cluster"
+ "%{public}@Error: Invalid nil value read for Condition attribute from MTRClusterHEPAFilterMonitoring cluster"
+ "%{public}@Error: Invalid nil value read for Degradation Direction attribute from MTRClusterActivatedCarbonFilterMonitoring cluster"
+ "%{public}@Error: Invalid nil value read for Degradation Direction attribute from MTRClusterHEPAFilterMonitoring cluster"
+ "%{public}@Error: Window covering cluster's feature map does NOT have neither Lift nor Tilt features enabled"
+ "%{public}@Error: nil read for MeasurementUnit attribute for cluster %@, using min/max defaults"
+ "%{public}@Error: nil received for Measured Value attribute, returning 0."
+ "%{public}@Failed to fetch additional Thread network information - aborting pairing: %@"
+ "%{public}@Failed to read color control attribute color mode."
+ "%{public}@Failed to read color control attribute color temperature mireds."
+ "%{public}@Failed to read color control attribute color temperature."
+ "%{public}@Failed to read color control attribute colorCapabilities."
+ "%{public}@Failed to read color control attribute physical max mired."
+ "%{public}@Failed to read color control attribute physical min mired."
+ "%{public}@Failed to read color control attribute remaining time."
+ "%{public}@Failed to read color mode attribute."
+ "%{public}@Failed to read startup color temperature attribute."
+ "%{public}@HMMTRAccessoryServer deallocated before receiving Thread credentials"
+ "%{public}@Ignoring invalid override vendor metadata from %@"
+ "%{public}@Invalid request priority: %lu"
+ "%{public}@MTRDevice unavailable to get Feature Map %@"
+ "%{public}@MaxMeasuredValue %@ for %@ cluster"
+ "%{public}@MaxMeasuredValue attribute from the %@ cluster endpoint:%@ absent from cache of node %@"
+ "%{public}@MeasurementUnit attribute from the %@ cluster endpoint:%@ absent from cache of node %@"
+ "%{public}@MeasurementUnit type %@ for cluster %@ is not supported"
+ "%{public}@MinMeasuredValue %@ for %@ cluster"
+ "%{public}@MinMeasuredValue attribute from the %@ cluster endpoint:%@ absent from cache of node %@"
+ "%{public}@No attributes found for cluster %@ on endpoint %@. Use default MeasuredValue Min/Max %@, %@"
+ "%{public}@No endpoint found to fetch color control cluster"
+ "%{public}@Notifying delegate of unauthenticated accessory prompt end"
+ "%{public}@Notifying delegate of unauthenticated accessory prompt start"
+ "%{public}@QueryImage state %@ indicates that the download protocol is not supported for accessory %@"
+ "%{public}@Read color control attribute colorCapabilities supportsColorTempFeature: %@ accessoryRange: [%@ : %@]  allowedRange: [%@ : %@]"
+ "%{public}@Skipping cloud fetch of metadata because override metadata is active"
+ "%{public}@The Lift Current Value is not supported by this device, so we map it to Tilt Current Value instead"
+ "%{public}@The Lift Target Value is not supported by this device, so we map it to Tilt Target Value instead"
+ "%{public}@The Lift is not supported by this device, so we map Lift commands to Tilt instead"
+ "%{public}@The linked services for the device types  %@ : %@"
+ "%{public}@The linked services for the device types %@ : %@"
+ "%{public}@The software update is not available yet, no need to call announceOTAProvider cmd"
+ "%{public}@This object is already deallocated, we cannot call announceOTAProvider cmd"
+ "%{public}@Thread credentials retrieved with error: %@"
+ "%{public}@Unable to get browser ref for handleUpdateRequestedForAccessoryServer:%@"
+ "%{public}@Unable to get browser ref for updateOTAProviderStateForNodeID:%@"
+ "%{public}@Unexpected, position characteristic not found on endpoint %@"
+ "%{public}@Using override vendor metadata from %@"
+ "%{public}@WED polling accessory: %@"
+ "%{public}@WED polling not scheduled: connected to thread network"
+ "%{public}@WED polling not scheduled: current fabric UUID is nil"
+ "%{public}@WED polling not scheduled: current fabric UUID is system commissioner"
+ "%{public}@WED polling not scheduled: device controller is not running for current fabric"
+ "%{public}@WED polling not scheduled: device doesn't support thread"
+ "%{public}@WED polling not scheduled: disabled via preference"
+ "%{public}@WED polling not scheduled: in pairing mode"
+ "%{public}@WED polling not scheduled: no active clients"
+ "%{public}@WED polling not scheduled: no wed accessories in home"
+ "%{public}@WED polling not scheduled: not ready to establish wed connection"
+ "%{public}@WED polling not scheduled: resident is reachable"
+ "%{public}@WED polling scheduled for the following accessories: %@"
+ "%{public}@Window covering Feature Map from device %tu"
+ "%{public}@[Flow: %@] Failed to find current fabric index, not removing any users."
+ "%{public}@[Flow: %@] Failed to remove user with index: %@ and uniqueID: %@. Error: %@"
+ "%{public}@[Flow: %@] Found %lu users to remove"
+ "%{public}@[Flow: %@] No more available slots"
+ "%{public}@[Flow: %@] Removing user with index: %@ and uniqueID: %@"
+ "%{public}@[Flow: %@] Removing users created by our fabric not in userUniqueIDs: %@"
+ "%{public}@[Flow: %@] addOrUpdatePinCodeWithValue: %@, forUserIndex: %ld"
+ "%{public}@[Flow: %@] getAllPinCodes"
+ "%{public}@[Flow: %@] getMaxPINCodeLength"
+ "%{public}@[Flow: %@] getMinPINCodeLength"
+ "%{public}@[Flow: %@] removePinCodeForUserIndex: %ld"
+ "%{public}@[NewFlow: %@ {\"Feature\":\"Event Reports\"}] HMMTRAccessoryServer Handling custom event report=%@"
+ "%{public}@[NewFlow: %@ {\"Feature\":\"Event Reports\"}] HMMTRAccessoryServer Handling parsed event report=%@"
+ "%{public}@[NewFlow: %@ {\"Feature\":\"Lock ReadWrite\"}] Locking door with accessoryUUID: %@ completionHandler: %@"
+ "%{public}@[NewFlow: %@ {\"Feature\":\"Lock ReadWrite\"}] Unlocking door with accessoryUUID: %@ completionHandler: %@"
+ "%{public}@[NewFlow: %@ {\"Feature\":\"Matter Users\"}] Getting all users"
+ "%{public}@[NewFlow: %@ {\"Feature\":\"Matter Users\"}] Removing all users"
+ "%{public}@[NewFlow: %@ {\"Feature\":\"Matter Users\"}] Removing user with uniqueID: %@"
+ "%{public}@readColorModeAndColorTemperatureWithCompletion"
+ "%{public}@triggerQueryImageWithPairing method is called and accessoryInitiated is %d"
+ "-local"
+ "0000006C-0000-1000-8000-0026BB765291"
+ "0000006D-0000-1000-8000-0026BB765291"
+ "00000090-0000-1000-8000-0026BB765291"
+ "00000091-0000-1000-8000-0026BB765291"
+ "00000093-0000-1000-8000-0026BB765291"
+ "00000094-0000-1000-8000-0026BB765291"
+ "000000AC-0000-1000-8000-0026BB765291"
+ "000000C3-0000-1000-8000-0026BB765291"
+ "000000C4-0000-1000-8000-0026BB765291"
+ "000000C6-0000-1000-8000-0026BB765291"
+ "000000C7-0000-1000-8000-0026BB765291"
+ "000000C8-0000-1000-8000-0026BB765291"
+ "@\"HMFFuture\"16@?0@\"MTRDoorLockClusterGetUserResponseParams\"8"
+ "@\"HMFPreferences\""
+ "@112@0:8@16@24@32@40@48@56@64@72@80@88@96@104"
+ "@48@0:8@16@24Q32@?40"
+ "@48@0:8Q16@24@32B40B44"
+ "@52@0:8@16@24@32@40B48"
+ "B16@?0@\"MTRDoorLockClusterGetUserResponseParams\"8"
+ "HAPLinkedServiceTypes"
+ "HMMTRCluster"
+ "HMMTRSyncClusterActivatedCarbonFilterMonitoring"
+ "HMMTRSyncClusterHEPAFilterMonitoring"
+ "LinkedServiceTypes"
+ "MTRClusterCarbonDioxideConcentrationMeasurement"
+ "MTRClusterCarbonMonoxideConcentrationMeasurement"
+ "MTRClusterNitrogenDioxideConcentrationMeasurement"
+ "MTRClusterOzoneConcentrationMeasurement"
+ "MTRClusterPM10ConcentrationMeasurement"
+ "MTRClusterPM25ConcentrationMeasurement"
+ "MTRClusterTotalVolatileOrganicCompoundsConcentrationMeasurement"
+ "MaxMeasuredValue"
+ "MeasurementUnit"
+ "MinMeasuredValue"
+ "OptionalLinkedHAPServiceTypes"
+ "T@\"HMFPreferences\",R,V_preferences"
+ "T@\"NSArray\",R,V_linkedServiceTypes"
+ "T@\"NSMutableDictionary\",&,N,V_hapLinkedServiceTypes"
+ "URLWithString:relativeToURL:"
+ "_chipClusterFunctionNameForOperationType:operationDictionary:value:forMTRCluster:forHMMTRCluster:"
+ "_hapLinkedServiceTypes"
+ "_isWedPollingDisabledForTests"
+ "_linkedServiceTypes"
+ "_pollWedAccessoriesIfAllowed"
+ "_populateMeasuredValueAttributeForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:"
+ "_preferences"
+ "absoluteURL"
+ "addOrUpdatePinCodeWithValue:forUserIndex:flow:"
+ "allowVendorDataOverride"
+ "connectToAccessoryWhenAllowed:priority:completion:"
+ "getAllPinCodesWithFlow:"
+ "getBaseClusterName:"
+ "getHAPLinkedServiceTypesAtEndpoint:"
+ "getMaxPINCodeLengthWithFlow:"
+ "getMinPINCodeLengthWithFlow:"
+ "hapLinkedServiceTypes"
+ "hapServiceDescriptionForServiceType:linkedServiceTypes:clustersInUse:endpoint:name:hapToCHIPClusterMappingArray:clusterClassesToQuery:hapServicesToCheckForFeatureMap:hapServicesToCheckForOptionalMatterAttribute:hapServicesToCheckForRequiredAttributeValues:hapCharacteristicsToCheckForRequiredAttributeValues:server:"
+ "hasPendingLowPriorityConnectionRequest"
+ "hasPendingLowPriorityConnectionRequestsOnly"
+ "hmmtr.ActivatedCarbonFilterMonitoring"
+ "hmmtr.HEPAFilterMonitoring"
+ "hmmtr.thread.wed.polling.disable"
+ "hmmtr.windowcovering"
+ "initWithFileURL:uarpController:fileManager:preferences:"
+ "initWithQueue:server:priority:completion:"
+ "initWithType:linkedServiceTypes:endpoint:name:"
+ "initWithType:linkedServiceTypes:endpoint:name:optionalServiceLabelIndexIncluded:"
+ "isEndpointPresentForClusterID:endpoint:device:callbackQueue:completionHandler:"
+ "isEndpointPresentForClusterID:endpoint:mtrDevice:callbackQueue:completionHandler:"
+ "linkedServiceTypes"
+ "mapChangeIndicationToFilterChangeIndication:"
+ "moveToColorTemperatureWithParams:expectedValues:expectedValueInterval:completion:"
+ "notifyDelegateOfUnauthenticatedAccessoryPromptEnded"
+ "notifyDelegateOfUnauthenticatedAccessoryPromptStarted"
+ "notifyUnauthenticatedMatterAccessoryPromptEnded"
+ "notifyUnauthenticatedMatterAccessoryPromptStarted"
+ "overrideMetadata"
+ "pathExtension"
+ "preferences"
+ "primaryAccessoryCategoryForNodeID:"
+ "queryImageWithPairing:requestParams:queue:accessoryInitiated:completionHandler:"
+ "readAttributeColorCapabilitiesWithParams:"
+ "readAttributeConditionWithParams:"
+ "readAttributeCurrentPositionLiftPercent100thsWithParams:"
+ "readAttributeCurrentPositionTiltPercent100thsWithParams:"
+ "readAttributeDegradationDirectionWithParams:"
+ "readAttributeMaxMeasuredValueWithParams:"
+ "readAttributeMinMeasuredValueWithParams:"
+ "readAttributePluginConditionWithParams:"
+ "readAttributePluginCurrentPositionLiftPercent100thsWithParams:"
+ "readAttributePluginTargetPositionLiftPercent100thsWithParams:"
+ "readAttributeRemainingTimeWithParams:"
+ "readAttributeStartUpColorTemperatureMiredsWithParams:"
+ "readAttributeTargetPositionLiftPercent100thsWithParams:"
+ "readAttributeTargetPositionTiltPercent100thsWithParams:"
+ "readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:"
+ "readColorTemperatureAttributesWithCompletion:"
+ "removePinCodeForUserIndex:flow:"
+ "removeUsersCreatedByOurFabricWithFlow:notInUserUniqueIDs:"
+ "sendUpOrDownCommand:expectedValueInterval:"
+ "setHAPLinkedServiceTypes:atEndpoint:"
+ "setHapLinkedServiceTypes:"
+ "stopMoveStepWithParams:expectedValues:expectedValueInterval:completion:"
+ "stringByAppendingPathExtension:"
+ "stringByDeletingPathExtension"
+ "supportsColorTemperatureRangeWithMinColorTemperature:maxColorTemperature:completion:"
+ "triggerQueryImageWithPairing:accessoryInitiated:requestParams:completionHandler:"
+ "updateConnectionIdleTime:force:"
+ "updatedValuePluginConditionForAttributeReport:responseHandler:"
+ "v24@0:8C16B20"
+ "v32@?0@\"NSArray\"8@\"NSDictionary\"16@\"NSError\"24"
+ "v40@0:8@16Q24@?32"
+ "v56@0:8@16d24@32@40@?48"
+ "vendor-metadata-local"
+ "writeAttributeStartUpColorTemperatureMiredsWithValue:expectedValueInterval:params:"
+ "writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:"
+ "\xf0\x82\xf0\xf0\xa1\xc1"
- "\v"
- "%{public}@An error occurred while trying to read Measured Value attribute"
- "%{public}@An error occurred while trying to read Measurement Unit attribute"
- "%{public}@An error occurred while trying to read Measurement Unit attribute. Cannot handle Measured Value attribute."
- "%{public}@An error occurred while trying to read Peak Measured Value attribute"
- "%{public}@Error: nil recieved for Measured Value attribute, returning 0."
- "%{public}@Failed to read color control attribute colorCapabilities with error: %@"
- "%{public}@Failed to read color control attribute physicalMaxMireds with error: %@"
- "%{public}@Failed to read color control attribute physicalMinMireds with error: %@"
- "%{public}@Failed to read colorMode for endPoint: %@ with error: %@"
- "%{public}@Found operational hardware address: %@"
- "%{public}@No MTRDevice state was reported for %d seconds. Reporting unreachable state."
- "%{public}@No Matter device available to fetch color control cluster"
- "%{public}@No Matter device controller available to fetch color control cluster, hapAccessory: %@"
- "%{public}@Pairing Timeout: Accessory Server: %@ was not paired in over %d seconds. Cancelling pairing..."
- "%{public}@Primary: Found color control cluster at endpoint: %@"
- "%{public}@Read color control attribute colorCapabilities supportsColorTempFeature: %@ accessoryRange: [%@ : %@]  allowedRange: [%@ : %@] error: %@"
- "%{public}@Received attribute report for colorMode value: %@ error: %@"
- "%{public}@[NewFlow: %@] Getting all users"
- "%{public}@[NewFlow: %@] HMMTRAccessoryServer Handling custom event report=%@"
- "%{public}@[NewFlow: %@] HMMTRAccessoryServer Handling parsed event report=%@"
- "%{public}@[NewFlow: %@] Locking door with accessoryUUID: %@ completionHandler: %@"
- "%{public}@[NewFlow: %@] Removing all users"
- "%{public}@[NewFlow: %@] Removing user with uniqueID: %@"
- "%{public}@[NewFlow: %@] Unlocking door with accessoryUUID: %@ completionHandler: %@"
- "%{public}@[NewFlow: %@] addOrUpdatePinCodeWithValue: %@, forUserIndex: %ld"
- "%{public}@[NewFlow: %@] getAllPinCodes"
- "%{public}@[NewFlow: %@] getMaxPINCodeLength"
- "%{public}@[NewFlow: %@] getMinPINCodeLength"
- "%{public}@[NewFlow: %@] removePinCodeForUserIndex: %ld"
- "%{public}@moveToColorTemperatureWithParams colorTemperature %@, optionsMask %@, error %@"
- "@104@0:8@16@24@32@40@48@56@64@72@80@88@96"
- "@32@0:8@16q24"
- "@44@0:8Q16@24@32B40"
- "Failed to pair Matter Accessory in time"
- "HMMTRAccessoryPairingKnownToSystemCommissioner"
- "OptionalHAPServiceTypes"
- "T@\"HMFTimer\",&,N,V_pairingTimer"
- "T@\"NSUUID\",&,V_initialMTRDeviceStateTimeoutId"
- "_chipClusterFunctionNameForOperationType:operationDictionary:value:forMTRCluster:"
- "_initialMTRDeviceStateTimeoutId"
- "_pairingTimer"
- "_startInitialReachableStateTimerWithCompletion:"
- "_updateMetrics"
- "addOrUpdatePinCodeWithValue:forUserIndex:"
- "cancelCommissioningForNodeID:error:"
- "enddePoint/%@"
- "getAllPinCodes"
- "getMaxPINCodeLength"
- "getMinPINCodeLength"
- "hapServiceDescriptionForServiceType:clustersInUse:endpoint:name:hapToCHIPClusterMappingArray:clusterClassesToQuery:hapServicesToCheckForFeatureMap:hapServicesToCheckForOptionalMatterAttribute:hapServicesToCheckForRequiredAttributeValues:hapCharacteristicsToCheckForRequiredAttributeValues:server:"
- "hmmtr.colorcontrol"
- "initWithMinInterval:maxInterval:"
- "initWithType:endpoint:name:"
- "initWithType:endpoint:name:optionalServiceLabelIndexIncluded:"
- "initialMTRDeviceStateTimeoutId"
- "moveToColorTemperatureWithParams:completion:"
- "moveToColorTemperatureWithParams:completionHandler:"
- "moveToPluginColorTemperatureWithParams:completionHandler:"
- "notifyDelegateOfQueryImageWithPairing:requestParams:completionHandler:"
- "pairingTimer"
- "queryEndpointForClusterID:endpoint:device:callbackQueue:completionHandler:"
- "queryImageWithPairing:requestParams:queue:completionHandler:"
- "readAttributeColorCapabilitiesWithCompletion:"
- "readAttributeColorModeWithCompletion:"
- "readAttributeColorModeWithCompletionHandler:"
- "readAttributeColorTempPhysicalMaxMiredsWithCompletion:"
- "readAttributeColorTempPhysicalMinMiredsWithCompletion:"
- "readAttributeColorTemperatureMiredsWithCompletion:"
- "readAttributePluginColorTemperatureMiredsWithCompletionHandler:"
- "readAttributeRemainingTimeWithCompletion:"
- "readAttributeStartUpColorTemperatureMiredsWithCompletion:"
- "readCharacteristicValues:timeout:completionQueue:completionHandler:"
- "readColorTemperatureAttributesWithCompletion:queue:"
- "removePinCodeForUserIndex:"
- "setInitialMTRDeviceStateTimeoutId:"
- "setPairingTimer:"
- "stopMoveStepWithParams:completion:"
- "subscribeAttributeColorModeWithParams:subscriptionEstablished:reportHandler:"
- "subscribeAttributeReportForColorModeWithCompletion:"
- "supportsColorTemperatureRangeWithMinColorTemperature:maxColorTemperature:completion:queue:"
- "v32@0:8@?16@24"
- "v48@0:8@16@24@?32@40"
- "writeAttributeStartUpColorTemperatureMiredsWithValue:completion:"
- "writeCharacteristicValues:timeout:completionQueue:completionHandler:"
- "\xf0\x82\xf0\xf0\xc1\xc1"

```
