## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

```diff

-1418.5.9.0.1
+1418.5.13.0.1
   __TEXT.__text: 0x1520d0
   __TEXT.__auth_stubs: 0xa30
-  __TEXT.__objc_methlist: 0xa69c
+  __TEXT.__objc_methlist: 0xa6a4
   __TEXT.__const: 0x170
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__gcc_except_tab: 0x3320

   __TEXT.__ustring: 0x68
   __TEXT.__unwind_info: 0x3440
   __TEXT.__objc_classname: 0x14b0
-  __TEXT.__objc_methname: 0x25e60
-  __TEXT.__objc_methtype: 0x3e11
+  __TEXT.__objc_methname: 0x25e81
+  __TEXT.__objc_methtype: 0x3e30
   __TEXT.__objc_stubs: 0x16780
   __DATA_CONST.__got: 0x9b0
   __DATA_CONST.__const: 0x4688

   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6cf8
+  __DATA_CONST.__objc_selrefs: 0x6d00
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2f8
   __DATA_CONST.__objc_arraydata: 0x228
   __AUTH_CONST.__auth_got: 0x528
   __AUTH_CONST.__const: 0x10a0
   __AUTH_CONST.__cfstring: 0x6c80
-  __AUTH_CONST.__objc_const: 0xf920
+  __AUTH_CONST.__objc_const: 0xf928
   __AUTH_CONST.__objc_intobj: 0x16e0
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x60

   - /System/Library/PrivateFrameworks/UARPKit.framework/UARPKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5F338F1E-C213-3462-96FB-08A1B5112E25
+  UUID: 7119B61F-1A0B-3A40-84CC-E6BCD728D54C
   Functions: 4297
   Symbols:   14827
-  CStrings:  9579
+  CStrings:  9581
 
Symbols:
+ ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.862
+ ___102-[HMMTRAccessoryServer updateAllCharacteristicValuesPostHAPServiceEnumerationForAccessory:completion:]_block_invoke.810
+ ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.920
+ ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.923
+ ___37-[HMMTRAccessoryServer finishPairing]_block_invoke.790
+ ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.989
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.890
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.889
+ ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.990
+ ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.988
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.927
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.933
+ ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.840
+ ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.841
+ ___64-[HMMTRAccessoryServer _commissioning:complete:abstractMetrics:]_block_invoke.948
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.954
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.955
+ ___70-[HMMTRAccessoryServer _onThreadScanResults:commissioning:completion:]_block_invoke.897
+ ___70-[HMMTRAccessoryServer _onThreadScanResults:commissioning:completion:]_block_invoke.898
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.834
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.835
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.838
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.839
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke_2.836
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.811
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.812
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.821
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.829
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.832
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.833
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke_2.825
+ ___82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.934
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.903
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.904
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.907
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke_2.906
+ ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.863
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.910
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.911
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.915
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.916
+ ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.956
+ ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.957
+ ___92-[HMMTRAccessoryServer _createFirmwareUpdateServiceWithInstanceID:device:completionHandler:]_block_invoke.803
+ ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.861
+ ___Block_byref_object_copy_.10543
+ ___Block_byref_object_copy_.11205
+ ___Block_byref_object_copy_.11810
+ ___Block_byref_object_copy_.12496
+ ___Block_byref_object_copy_.12659
+ ___Block_byref_object_dispose_.10544
+ ___Block_byref_object_dispose_.11206
+ ___Block_byref_object_dispose_.11811
+ ___Block_byref_object_dispose_.12497
+ ___Block_byref_object_dispose_.12660
+ ___block_literal_global.11033
+ ___block_literal_global.11460
+ ___block_literal_global.11630
+ ___block_literal_global.11844
+ ___block_literal_global.12042
+ ___block_literal_global.12100
+ ___block_literal_global.12318
+ ___block_literal_global.549.11130
+ ___block_literal_global.808
+ ___block_literal_global.815
+ ___block_literal_global.824
+ ___block_literal_global.828
+ ___block_literal_global.997
+ _logCategory._hmf_once_t20.12041
+ _logCategory._hmf_once_t31.12099
+ _logCategory._hmf_once_t8.11629
+ _logCategory._hmf_once_v21.12043
+ _logCategory._hmf_once_v32.12101
+ _logCategory._hmf_once_v9.11631
- ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.860
- ___102-[HMMTRAccessoryServer updateAllCharacteristicValuesPostHAPServiceEnumerationForAccessory:completion:]_block_invoke.808
- ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.918
- ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.921
- ___37-[HMMTRAccessoryServer finishPairing]_block_invoke.788
- ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.987
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.884
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.887
- ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.988
- ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.986
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.923
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.929
- ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.838
- ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.839
- ___64-[HMMTRAccessoryServer _commissioning:complete:abstractMetrics:]_block_invoke.946
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.951
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.952
- ___70-[HMMTRAccessoryServer _onThreadScanResults:commissioning:completion:]_block_invoke.895
- ___70-[HMMTRAccessoryServer _onThreadScanResults:commissioning:completion:]_block_invoke.896
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.832
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.833
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.836
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.837
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke_2.834
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.809
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.810
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.819
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.827
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.828
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.831
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke_2.823
- ___82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.932
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.900
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.901
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.905
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke_2.904
- ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.861
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.906
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.907
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.913
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.914
- ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.954
- ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.955
- ___92-[HMMTRAccessoryServer _createFirmwareUpdateServiceWithInstanceID:device:completionHandler:]_block_invoke.801
- ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.859
- ___Block_byref_object_copy_.10542
- ___Block_byref_object_copy_.11204
- ___Block_byref_object_copy_.11809
- ___Block_byref_object_copy_.12495
- ___Block_byref_object_copy_.12658
- ___Block_byref_object_dispose_.10543
- ___Block_byref_object_dispose_.11205
- ___Block_byref_object_dispose_.11810
- ___Block_byref_object_dispose_.12496
- ___Block_byref_object_dispose_.12659
- ___block_literal_global.11032
- ___block_literal_global.11459
- ___block_literal_global.11629
- ___block_literal_global.11843
- ___block_literal_global.12041
- ___block_literal_global.12099
- ___block_literal_global.12317
- ___block_literal_global.549.11129
- ___block_literal_global.806
- ___block_literal_global.813
- ___block_literal_global.822
- ___block_literal_global.826
- ___block_literal_global.995
- _logCategory._hmf_once_t20.12040
- _logCategory._hmf_once_t31.12098
- _logCategory._hmf_once_t8.11628
- _logCategory._hmf_once_v21.12042
- _logCategory._hmf_once_v32.12100
- _logCategory._hmf_once_v9.11630
CStrings:
+ "B24@0:8@\"HAPAccessoryServer\"16"
+ "accessoryServerHasActiveClients:"

```
