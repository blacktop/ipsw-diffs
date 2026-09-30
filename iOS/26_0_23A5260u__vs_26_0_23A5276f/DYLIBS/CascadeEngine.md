## CascadeEngine

> `/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine`

```diff

-192.0.0.0.0
-  __TEXT.__text: 0x1e1d8
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x176c
-  __TEXT.__const: 0x100
-  __TEXT.__gcc_except_tab: 0x64c
-  __TEXT.__cstring: 0xfe8
-  __TEXT.__oslogstring: 0x36b3
+195.0.0.0.0
+  __TEXT.__text: 0x1f6c4
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__objc_methlist: 0x17cc
+  __TEXT.__const: 0x110
+  __TEXT.__gcc_except_tab: 0x69c
+  __TEXT.__cstring: 0x107c
+  __TEXT.__oslogstring: 0x3b51
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x7f8
-  __TEXT.__objc_classname: 0x476
-  __TEXT.__objc_methname: 0x4f76
-  __TEXT.__objc_methtype: 0xf44
-  __TEXT.__objc_stubs: 0x42a0
+  __TEXT.__unwind_info: 0x840
+  __TEXT.__objc_classname: 0x46e
+  __TEXT.__objc_methname: 0x5207
+  __TEXT.__objc_methtype: 0xfcb
+  __TEXT.__objc_stubs: 0x4460
   __DATA_CONST.__got: 0x288
-  __DATA_CONST.__const: 0xb58
-  __DATA_CONST.__objc_classlist: 0xe0
+  __DATA_CONST.__const: 0xb88
+  __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1310
+  __DATA_CONST.__objc_selrefs: 0x1388
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0xb8
-  __AUTH_CONST.__auth_got: 0x398
-  __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0xee0
-  __AUTH_CONST.__objc_const: 0x31b0
+  __AUTH_CONST.__auth_got: 0x3b0
+  __AUTH_CONST.__const: 0x140
+  __AUTH_CONST.__cfstring: 0xf40
+  __AUTH_CONST.__objc_const: 0x3120
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28

   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x258
   __DATA.__data: 0x720
-  __DATA.__bss: 0x30
-  __DATA_DIRTY.__objc_data: 0x640
+  __DATA.__bss: 0x50
+  __DATA_DIRTY.__objc_data: 0x5f0
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E5085A92-319B-306A-AA6C-E0256E8455DD
-  Functions: 675
-  Symbols:   2708
-  CStrings:  1542
+  UUID: 8B219A23-7AF0-36D0-B62C-FE5D82C2AB91
+  Functions: 694
+  Symbols:   2767
+  CStrings:  1586
 
Symbols:
+ +[CCDiscoveredSet _enumerateAndCopySets:setOptionsUsingBlock:]
+ +[CCDiscoveredSet removeOptions:fromSets:]
+ +[CCFetchMergeableDeltasResponse fetchMergeableDeltasResponseFromPeerToPeerMessage:peerPublicKey:]
+ -[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]
+ -[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:].cold.1
+ -[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:].cold.2
+ -[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:].cold.3
+ -[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:].cold.4
+ -[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:].cold.5
+ -[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:].cold.6
+ -[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:].cold.7
+ -[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:].cold.8
+ -[CCDiscoveredSet description]
+ -[CCDonateConnection remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:completion:]
+ -[CCFetchMergeableDeltasResponse .cxx_destruct]
+ -[CCFetchMergeableDeltasResponse dictionaryRepresentation]
+ -[CCFetchMergeableDeltasResponse initFromDictionary:]
+ -[CCFetchMergeableDeltasResponse peerPublicKey]
+ -[CCFetchMergeableDeltasResponse setPeerPublicKey:]
+ -[CCRapportRequest setSetsToSyncFromDevice:]
+ -[CCRapportRequest setsToSyncFromDevice]
+ -[CCRapportSyncEngine addOmittedSetsFromSetDiscovery:]
+ -[CCRapportSyncEngine addOmittedSetsFromSetDiscovery:].cold.1
+ -[CCRapportSyncEngine determineSyncOperationForDiscoveredSet:withDevice:outFetchRequest:]
+ -[CCRapportSyncEngine expireDevice:fromSet:]
+ -[CCRapportSyncEngine setIdentifiersSupportingInboundSync]
+ -[CCRapportSyncEngine setIdentifiersSupportingInboundSync].cold.1
+ -[CCRapportSyncEngine setIdentifiersSupportingOutboundSync]
+ -[CCRapportSyncEngine setIdentifiersSupportingOutboundSync].cold.1
+ -[CCRapportSyncEngine syncErrorCodeFromReadAccessError:]
+ -[CCRapportSyncEngine syncOperationForDiscoveredSet:withDevice:versionedMergeable:readAccessError:]
+ -[CCSetStoreAdminConnection .cxx_destruct]
+ -[CCSetStoreAdminConnection _shouldDeferActivityBlock]
+ -[CCSetStoreAdminConnection initWithConnection:writeAccess:]
+ -[CCSetStoreAdminConnection performMaintenanceOnAllSets:completion:]
+ -[CCSetStoreAdminConnection performMaintenanceOnAllSets:completion:].cold.1
+ -[CCSetStoreAdminConnection removeAllSets:completion:]
+ -[CCSetStoreAdminConnection removeAllSets:completion:].cold.1
+ -[CCSetStoreUpdateServiceExported remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:completion:]
+ -[CCSetVersionedMergeable _donateRemoteUpdateWithType:fromPeerDeviceUUID:peerDeviceSite:relayedDeviceSites:mergeableDelta:]
+ -[CCSetVersionedMergeable _donateRemoteUpdateWithType:fromPeerDeviceUUID:peerDeviceSite:relayedDeviceSites:mergeableDelta:].cold.1
+ -[CCSetVersionedMergeable attestInSyncPeerDeviceUUID:deviceSite:relayedDeviceSites:]
+ -[CCSetVersionedMergeable expirePeerDeviceUUID:]
+ -[CCSetVersionedMergeable hasNoPresentContent]
+ -[CCSetVersionedMergeable hasNoPresentContent].cold.1
+ -[CCSetVersionedMergeable hasNoPresentContent].cold.2
+ -[CCSetVersionedMergeable hasNoPresentContent].cold.3
+ -[CCSetVersionedMergeable mergeUpdateFromPeerDeviceUUID:deviceSite:relayedDeviceSites:mergeableDelta:]
+ -[CCSetVersionedMergeable mergeUpdateFromPeerDeviceUUID:deviceSite:relayedDeviceSites:mergeableDelta:].cold.1
+ -[CCSetVersionedMergeable storedActiveDeviceSiteWithDeviceUUID:]
+ -[CCSetVersionedMergeable storedActiveDeviceSiteWithDeviceUUID:].cold.1
+ GCC_except_table16
+ GCC_except_table63
+ GCC_except_table64
+ GCC_except_table65
+ GCC_except_table66
+ GCC_except_table7
+ GCC_except_table71
+ _CCRemoteUpdateTypeDescription
+ _CCSetErrorDomain
+ _OBJC_CLASS_$_CCSetStoreAdminConnection
+ _OBJC_IVAR_$_CCFetchMergeableDeltasResponse._peerPublicKey
+ _OBJC_IVAR_$_CCRapportRequest._setsToSyncFromDevice
+ _OBJC_IVAR_$_CCSetStoreAdminConnection._connection
+ _OBJC_IVAR_$_CCSetStoreAdminConnection._writeAccess
+ _OBJC_METACLASS_$_CCSetStoreAdminConnection
+ __OBJC_$_INSTANCE_METHODS_CCFetchMergeableDeltasResponse
+ __OBJC_$_INSTANCE_METHODS_CCSetStoreAdminConnection
+ __OBJC_$_INSTANCE_VARIABLES_CCFetchMergeableDeltasResponse
+ __OBJC_$_INSTANCE_VARIABLES_CCSetStoreAdminConnection
+ __OBJC_$_PROP_LIST_CCFetchMergeableDeltasResponse
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCSetStoreAdminService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCSetStoreAdminServiceClient
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CCSetStoreAdminService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CCSetStoreAdminServiceClient
+ __OBJC_$_PROTOCOL_REFS_CCSetStoreAdminServiceClient
+ __OBJC_$_PROTOCOL_REFS_CCSetStoreAdminServiceServer
+ __OBJC_CLASS_PROTOCOLS_$_CCSetStoreAdminConnection
+ __OBJC_CLASS_RO_$_CCSetStoreAdminConnection
+ __OBJC_LABEL_PROTOCOL_$_CCSetStoreAdminService
+ __OBJC_LABEL_PROTOCOL_$_CCSetStoreAdminServiceClient
+ __OBJC_LABEL_PROTOCOL_$_CCSetStoreAdminServiceServer
+ __OBJC_METACLASS_RO_$_CCSetStoreAdminConnection
+ __OBJC_PROTOCOL_$_CCSetStoreAdminService
+ __OBJC_PROTOCOL_$_CCSetStoreAdminServiceClient
+ __OBJC_PROTOCOL_$_CCSetStoreAdminServiceServer
+ ___105-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke
+ ___105-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.58
+ ___105-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.58.cold.1
+ ___105-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.59
+ ___105-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.59.cold.1
+ ___105-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.1
+ ___105-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.2
+ ___105-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.3
+ ___105-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.4
+ ___105-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.5
+ ___105-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.6
+ ___117-[CCDonateConnection remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:completion:]_block_invoke
+ ___117-[CCDonateConnection remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:completion:]_block_invoke_2
+ ___117-[CCDonateConnection remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:completion:]_block_invoke_2.cold.1
+ ___123-[CCSetVersionedMergeable _donateRemoteUpdateWithType:fromPeerDeviceUUID:peerDeviceSite:relayedDeviceSites:mergeableDelta:]_block_invoke
+ ___123-[CCSetVersionedMergeable _donateRemoteUpdateWithType:fromPeerDeviceUUID:peerDeviceSite:relayedDeviceSites:mergeableDelta:]_block_invoke.10
+ ___123-[CCSetVersionedMergeable _donateRemoteUpdateWithType:fromPeerDeviceUUID:peerDeviceSite:relayedDeviceSites:mergeableDelta:]_block_invoke.10.cold.1
+ ___123-[CCSetVersionedMergeable _donateRemoteUpdateWithType:fromPeerDeviceUUID:peerDeviceSite:relayedDeviceSites:mergeableDelta:]_block_invoke.10.cold.2
+ ___123-[CCSetVersionedMergeable _donateRemoteUpdateWithType:fromPeerDeviceUUID:peerDeviceSite:relayedDeviceSites:mergeableDelta:]_block_invoke.cold.1
+ ___37+[CCDiscoveredSet addOptions:toSets:]_block_invoke
+ ___42+[CCDiscoveredSet removeOptions:fromSets:]_block_invoke
+ ___49-[CCRapportSyncEngine setDiscoveryRequestHandler]_block_invoke.162
+ ___54-[CCRapportSyncEngine addOmittedSetsFromSetDiscovery:]_block_invoke
+ ___54-[CCRapportSyncEngine addOmittedSetsFromSetDiscovery:]_block_invoke.cold.1
+ ___54-[CCSetStoreAdminConnection _shouldDeferActivityBlock]_block_invoke
+ ___54-[CCSetStoreAdminConnection _shouldDeferActivityBlock]_block_invoke.1
+ ___54-[CCSetStoreAdminConnection _shouldDeferActivityBlock]_block_invoke.cold.1
+ ___54-[CCSetStoreAdminConnection _shouldDeferActivityBlock]_block_invoke_2
+ ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.175
+ ___58-[CCRapportSyncEngine setIdentifiersSupportingInboundSync]_block_invoke
+ ___59-[CCRapportSyncEngine setIdentifiersSupportingOutboundSync]_block_invoke
+ ___64-[CCRapportSyncEngine doneFetchingMergeableDeltasRequestHandler]_block_invoke.179
+ ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.129
+ ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.132
+ ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.134
+ ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.146
+ ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.146.cold.1
+ ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.147
+ ___block_descriptor_33_e8_C12?0C8l
+ ___block_descriptor_48_e8_32s40w_e88_v32?0"NSDictionary"8"NSDictionary"16?<v?"NSDictionary""NSDictionary""NSError">24lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e15_v16?0"CCSet"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s_e15_v16?0"CCSet"8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24lw56l8s32l8s48l8s40l8
+ ___block_descriptor_66_e8_32s40s48bs56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_66_e8_32s40s48bs56r_e5_v8?0ls32l8r56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24lw64l8s32l8s40l8s56l8s48l8
+ ___block_descriptor_73_e8_32s40s48s56s64bs_e45_v24?0"CCRemoteCRDTSetDonation"8"NSError"16ls32l8s64l8s40l8s48l8s56l8
+ ___block_descriptor_82_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s72l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.182
+ ___block_literal_global.184
+ ___block_literal_global.186
+ _objc_getProperty
+ _objc_msgSend$_donateRemoteUpdateWithType:fromPeerDeviceUUID:peerDeviceSite:relayedDeviceSites:mergeableDelta:
+ _objc_msgSend$_enumerateAndCopySets:setOptionsUsingBlock:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$addOmittedSetsFromSetDiscovery:
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$attestInSyncPeerDeviceUUID:deviceSite:relayedDeviceSites:
+ _objc_msgSend$checkForPresentContent:filterByDeviceRowId:error:
+ _objc_msgSend$determineSyncOperationForDiscoveredSet:withDevice:outFetchRequest:
+ _objc_msgSend$deviceRowIdForDeviceSite:
+ _objc_msgSend$enumerateAllSets:withOptions:setIdentifiers:usingBlock:
+ _objc_msgSend$expireDevice:fromSet:
+ _objc_msgSend$expirePeerDeviceUUID:
+ _objc_msgSend$expireRemoteDeviceUUID:
+ _objc_msgSend$fetchMergeableDeltasResponseFromPeerToPeerMessage:peerPublicKey:
+ _objc_msgSend$hasNoPresentContent
+ _objc_msgSend$mergeUpdateFromPeerDeviceUUID:deviceSite:relayedDeviceSites:mergeableDelta:
+ _objc_msgSend$registerRemoteDeviceSite:peerDeviceUUID:isRelayed:hasDeltas:returningRowId:
+ _objc_msgSend$remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:completion:
+ _objc_msgSend$remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:
+ _objc_msgSend$removeOptions:fromSets:
+ _objc_msgSend$setIdentifiersSupportingInboundSync
+ _objc_msgSend$setIdentifiersSupportingOutboundSync
+ _objc_msgSend$setsToSyncFromDevice
+ _objc_msgSend$storedActiveDeviceSiteWithDeviceUUID:
+ _objc_msgSend$syncErrorCodeFromReadAccessError:
+ _objc_msgSend$syncOperationForDiscoveredSet:withDevice:versionedMergeable:readAccessError:
+ _objc_msgSend$toResourceSpecifier
+ _objc_msgSend$updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:
+ _objc_setProperty_atomic
+ _setIdentifiersSupportingInboundSync.inboundSetIdentifiers
+ _setIdentifiersSupportingInboundSync.onceToken
+ _setIdentifiersSupportingOutboundSync.onceToken
+ _setIdentifiersSupportingOutboundSync.outboundSetIdentifiers
- +[CCFetchMergeableDeltasResponse fetchMergeableDeltasResponseFromPeerToPeerMessage:]
- +[CCFileTransferSessionInitiatedResponse fileTransferSessionInitiatedResponseFromPeerToPeerMessage:peerPublicKey:]
- -[CCAdminConnection .cxx_destruct]
- -[CCAdminConnection _shouldDeferActivityBlock]
- -[CCAdminConnection initWithConnection:writeAccess:]
- -[CCAdminConnection performMaintenanceOnAllSets:completion:]
- -[CCAdminConnection performMaintenanceOnAllSets:completion:].cold.1
- -[CCAdminConnection removeAllSets:completion:]
- -[CCAdminConnection removeAllSets:completion:].cold.1
- -[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]
- -[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:].cold.1
- -[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:].cold.2
- -[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:].cold.3
- -[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:].cold.4
- -[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:].cold.5
- -[CCDonateConnection mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:]
- -[CCFileTransferSessionInitiatedResponse .cxx_destruct]
- -[CCFileTransferSessionInitiatedResponse dictionaryRepresentation]
- -[CCFileTransferSessionInitiatedResponse initFromDictionary:]
- -[CCFileTransferSessionInitiatedResponse peerPublicKey]
- -[CCFileTransferSessionInitiatedResponse setPeerPublicKey:]
- -[CCRapportRequest resolvedSetsToSync]
- -[CCRapportRequest setResolvedSetsToSync:]
- -[CCRapportSyncEngine determineSyncOperationForDiscoveredSet:outFetchRequest:]
- -[CCRapportSyncEngine syncOperationForDiscoveredSet:versionedMergeable:]
- -[CCSetStoreUpdateServiceExported mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:]
- -[CCSetVersionedMergeable _remoteCRDTSetDonationWithDelta:fromDeviceSite:relayedDeviceSites:]
- -[CCSetVersionedMergeable _remoteCRDTSetDonationWithDelta:fromDeviceSite:relayedDeviceSites:].cold.1
- -[CCSetVersionedMergeable attestInSyncDeviceSite:relayedDeviceSites:]
- -[CCSetVersionedMergeable mergeRemoteDelta:fromDeviceSite:relayedDeviceSites:]
- -[CCSetVersionedMergeable mergeRemoteDelta:fromDeviceSite:relayedDeviceSites:].cold.1
- -[CCSetVersionedMergeable storedEquivalentForDeviceSite:]
- -[CCSetVersionedMergeable storedEquivalentForDeviceSite:].cold.1
- GCC_except_table15
- GCC_except_table6
- GCC_except_table61
- GCC_except_table67
- GCC_except_table69
- _OBJC_CLASS_$_CCAdminConnection
- _OBJC_CLASS_$_CCDatabaseEmptyAccess
- _OBJC_CLASS_$_CCFileTransferSessionInitiatedResponse
- _OBJC_IVAR_$_CCAdminConnection._connection
- _OBJC_IVAR_$_CCAdminConnection._writeAccess
- _OBJC_IVAR_$_CCFileTransferSessionInitiatedResponse._peerPublicKey
- _OBJC_IVAR_$_CCRapportRequest._resolvedSetsToSync
- _OBJC_METACLASS_$_CCAdminConnection
- _OBJC_METACLASS_$_CCFileTransferSessionInitiatedResponse
- __OBJC_$_CLASS_METHODS_CCFileTransferSessionInitiatedResponse
- __OBJC_$_INSTANCE_METHODS_CCAdminConnection
- __OBJC_$_INSTANCE_METHODS_CCFileTransferSessionInitiatedResponse
- __OBJC_$_INSTANCE_VARIABLES_CCAdminConnection
- __OBJC_$_INSTANCE_VARIABLES_CCFileTransferSessionInitiatedResponse
- __OBJC_$_PROP_LIST_CCFileTransferSessionInitiatedResponse
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCAdminService
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCAdminServiceClient
- __OBJC_$_PROTOCOL_METHOD_TYPES_CCAdminService
- __OBJC_$_PROTOCOL_METHOD_TYPES_CCAdminServiceClient
- __OBJC_$_PROTOCOL_REFS_CCAdminServiceClient
- __OBJC_$_PROTOCOL_REFS_CCAdminServiceServer
- __OBJC_CLASS_PROTOCOLS_$_CCAdminConnection
- __OBJC_CLASS_RO_$_CCAdminConnection
- __OBJC_CLASS_RO_$_CCFileTransferSessionInitiatedResponse
- __OBJC_LABEL_PROTOCOL_$_CCAdminService
- __OBJC_LABEL_PROTOCOL_$_CCAdminServiceClient
- __OBJC_LABEL_PROTOCOL_$_CCAdminServiceServer
- __OBJC_METACLASS_RO_$_CCAdminConnection
- __OBJC_METACLASS_RO_$_CCFileTransferSessionInitiatedResponse
- __OBJC_PROTOCOL_$_CCAdminService
- __OBJC_PROTOCOL_$_CCAdminServiceClient
- __OBJC_PROTOCOL_$_CCAdminServiceServer
- ___46-[CCAdminConnection _shouldDeferActivityBlock]_block_invoke
- ___46-[CCAdminConnection _shouldDeferActivityBlock]_block_invoke.1
- ___46-[CCAdminConnection _shouldDeferActivityBlock]_block_invoke.cold.1
- ___46-[CCAdminConnection _shouldDeferActivityBlock]_block_invoke_2
- ___49-[CCRapportSyncEngine setDiscoveryRequestHandler]_block_invoke.164
- ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.181
- ___64-[CCRapportSyncEngine doneFetchingMergeableDeltasRequestHandler]_block_invoke.185
- ___74-[CCRapportSyncEngine sendSetDiscoveryRequest:toDevice:completionHandler:]_block_invoke.cold.1
- ___76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke
- ___76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.57
- ___76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.57.cold.1
- ___76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.58
- ___76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.58.cold.1
- ___76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.1
- ___76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.2
- ___76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.3
- ___76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.4
- ___76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.5
- ___76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.6
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.130
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.133
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.135.cold.1
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.139
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.141
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.145
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke_2
- ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.150.cold.1
- ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.151
- ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.153
- ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.153.cold.1
- ___84-[CCDonateConnection mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:]_block_invoke
- ___84-[CCDonateConnection mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:]_block_invoke_2
- ___84-[CCDonateConnection mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:]_block_invoke_2.cold.1
- ___93-[CCSetVersionedMergeable _remoteCRDTSetDonationWithDelta:fromDeviceSite:relayedDeviceSites:]_block_invoke
- ___93-[CCSetVersionedMergeable _remoteCRDTSetDonationWithDelta:fromDeviceSite:relayedDeviceSites:]_block_invoke.10
- ___93-[CCSetVersionedMergeable _remoteCRDTSetDonationWithDelta:fromDeviceSite:relayedDeviceSites:]_block_invoke.10.cold.1
- ___93-[CCSetVersionedMergeable _remoteCRDTSetDonationWithDelta:fromDeviceSite:relayedDeviceSites:]_block_invoke.10.cold.2
- ___93-[CCSetVersionedMergeable _remoteCRDTSetDonationWithDelta:fromDeviceSite:relayedDeviceSites:]_block_invoke.cold.1
- ___block_descriptor_48_e8_32s40bs_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls32l8s40l8
- ___block_descriptor_49_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs48w_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24lw48l8s40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e44_v24?0"CCSetDiscoveryResponse"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48bs_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls32l8s48l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e45_v24?0"CCRemoteCRDTSetDonation"8"NSError"16ls32l8s56l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56s_e15_v16?0"CCSet"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48bs56r_e5_v8?0lr56l8s32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48bs56r_e5_v8?0ls32l8r56l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
- ___block_literal_global.188
- _objc_msgSend$_remoteCRDTSetDonationWithDelta:fromDeviceSite:relayedDeviceSites:
- _objc_msgSend$attestInSyncDeviceSite:relayedDeviceSites:
- _objc_msgSend$determineSyncOperationForDiscoveredSet:outFetchRequest:
- _objc_msgSend$enumerateAllSets:withOptions:usingBlock:
- _objc_msgSend$fetchMergeableDeltasResponseFromPeerToPeerMessage:
- _objc_msgSend$fileTransferSessionInitiatedResponseFromPeerToPeerMessage:peerPublicKey:
- _objc_msgSend$mergeRemoteDelta:fromDeviceSite:relayedDeviceSites:
- _objc_msgSend$mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:
- _objc_msgSend$mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:
- _objc_msgSend$registerRemoteDeviceSite:isPeer:hasDeltas:returningRowId:
- _objc_msgSend$resolvedSetsToSync
- _objc_msgSend$setResolvedSetsToSync:
- _objc_msgSend$storedEquivalentForDeviceSite:
- _objc_msgSend$syncOperationForDiscoveredSet:versionedMergeable:
CStrings:
+ "%@: %s %@"
+ "%@: Discovery response missing device site (found active stored site): %@ for set: %@"
+ "%@: Found no active stored equivalent for peer deviceUUID: %@ in set: %@"
+ "%@: candidate set (%u / %u): %@"
+ "%@: enqueueing sync operations for %u candidate set(s) with device %@"
+ "%@: failed to discover remote sets due to error: %@, cannot proceed to sync with device %@"
+ "%@: fetch mergeable deltas failed with error: %@ from device: %@"
+ "%@: fetch mergeable deltas response error code (%@) requires immediate expiration for any active contents stored in set: %@ from device: %@"
+ "%@: full sync required for set: %@ without local database access"
+ "%@: local set enumeration for omitted sets encountered error: %@"
+ "%@: local set enumeration found %u eligible candidate set(s) omitted from set discovery response: %@"
+ "%@: received fetchMergeableDeltas for nonexistent set: %@"
+ "%@: resolved sync operation (%@) for set: %@ with device: %@"
+ "%@: will skip empty set: %@ with nonexistent local database"
+ "%@: will skip omitted set: %@ without local database access"
+ "%@: will skip sync due to discovery error for set: %@"
+ "(%@) %@"
+ "-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]"
+ "-[CCRapportSyncEngine addOmittedSetsFromSetDiscovery:]_block_invoke"
+ "@\"CCSetStoreAdminConnection\""
+ "@80@0:8@16@24S32@36@44Q52@60S68@72"
+ "B48@0:8@16@24@32@40"
+ "B52@0:8@16S24@28@36@44"
+ "B52@0:8C16@20@28@36@44"
+ "C12@?0C8"
+ "C40@0:8@16@24^@32"
+ "C48@0:8@16@24@32@40"
+ "CCRapportDevice[%@]: \"%@\" model: %@ RapportID: %@ CascadeID: %@"
+ "CCSetStoreAdminConnection"
+ "CCSetStoreAdminService"
+ "CCSetStoreAdminServiceClient"
+ "CCSetStoreAdminServiceServer"
+ "Cannot check for local source content without device mapping: %@"
+ "Cannot resolve device site without device mapping: %@"
+ "Expected to merge deltas with options: %X but received: %@"
+ "Expiring remote deviceUUID: %@"
+ "Failed to check for local source present content: %@"
+ "Failed to resolve local device rowId from mapping: %@"
+ "Invalid remote deviceUUID: %@"
+ "Q24@0:8@16"
+ "Remote CRDT donation %@ for set %@ from deviceUUID: %@"
+ "Requesting donation for remote update (%@) from deviceUUID: %@"
+ "Set has no present content"
+ "Set omitted from set discovery response"
+ "Sync policy requires immediate sync for set: %@"
+ "T@\"NSMutableDictionary\",&,N,V_setsToSyncFromDevice"
+ "T@\"NSString\",R,V_rapportIdentifier"
+ "T@\"NSUUID\",&,V_cascadeDeviceUUID"
+ "T@\"RPCompanionLinkClient\",&,V_client"
+ "T@\"RPCompanionLinkDevice\",&,V_device"
+ "TS,R,N,V_options"
+ "Tq,R"
+ "Unexpected options: %X for method: %s with update type: %@"
+ "Vv36@0:8S16@\"NSString\"20@?<v@?S>28"
+ "Vv36@0:8S16@20@?28"
+ "Vv56@0:8S16@\"NSString\"20Q28@\"NSString\"36S44@?<v@?Sq@\"CCDonateServicePriors\">48"
+ "Vv56@0:8S16@20Q28@36S44@?48"
+ "_donateRemoteUpdateWithType:fromPeerDeviceUUID:peerDeviceSite:relayedDeviceSites:mergeableDelta:"
+ "_enumerateAndCopySets:setOptionsUsingBlock:"
+ "_setsToSyncFromDevice"
+ "addObjectsFromArray:"
+ "addOmittedSetsFromSetDiscovery:"
+ "arrayWithArray:"
+ "attestInSyncPeerDeviceUUID:deviceSite:relayedDeviceSites:"
+ "checkForPresentContent:filterByDeviceRowId:error:"
+ "determineSyncOperationForDiscoveredSet:withDevice:outFetchRequest:"
+ "deviceRowIdForDeviceSite:"
+ "enumerateAllSets:withOptions:setIdentifiers:usingBlock:"
+ "expireDevice:fromSet:"
+ "expirePeerDeviceUUID:"
+ "expireRemoteDeviceUUID:"
+ "fetchMergeableDeltasResponseFromPeerToPeerMessage:peerPublicKey:"
+ "hasNoPresentContent"
+ "mergeUpdateFromPeerDeviceUUID:deviceSite:relayedDeviceSites:mergeableDelta:"
+ "registerRemoteDeviceSite:peerDeviceUUID:isRelayed:hasDeltas:returningRowId:"
+ "remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:completion:"
+ "remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:"
+ "removeOptions:fromSets:"
+ "setIdentifiersSupportingInboundSync"
+ "setIdentifiersSupportingOutboundSync"
+ "setSetsToSyncFromDevice:"
+ "setsToSyncFromDevice"
+ "storedActiveDeviceSiteWithDeviceUUID:"
+ "syncErrorCodeFromReadAccessError:"
+ "syncOperationForDiscoveredSet:withDevice:versionedMergeable:readAccessError:"
+ "toResourceSpecifier"
+ "updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:"
+ "v60@0:8@\"NSUUID\"16S24@\"CKMergeableDelta\"28@\"CCDeviceSite\"36@\"NSArray\"44@?<v@?S>52"
+ "v60@0:8@16S24@28@36@44@?52"
- "%@: Found no active stored equivalent for device site of discovered set: %@"
- "%@: creating operations to fetch deltas for %u set(s) with device %@"
- "%@: encountered rapport messaging error %@"
- "%@: failed to discover remote sets, cannot proceed to sync with device %@"
- "%@: handling discovered set (%u / %u): %@ from device: %@"
- "%@: resolved sync operation (%@) for discovered set: %@"
- "-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]"
- "@\"CCAdminConnection\""
- "@84@0:8@16@24S32@36@44Q52@60Q68@76"
- "C32@0:8@16@24"
- "C32@0:8@16^@24"
- "CCAdminConnection"
- "CCAdminService"
- "CCAdminServiceClient"
- "CCAdminServiceServer"
- "CCFileTransferSessionInitiatedResponse"
- "CCRapportDevice[%@]: id=%@ ccID=%@ model=%@ name=%@"
- "Remote CRDT donation %@ for set %@ from device site %@"
- "Sync policy requires immmediate sync for set: %@"
- "T@\"NSArray\",&,N,V_resolvedSetsToSync"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_rapportIdentifier"
- "T@\"NSUUID\",&,N,V_cascadeDeviceUUID"
- "T@\"RPCompanionLinkClient\",&,N,V_client"
- "T@\"RPCompanionLinkDevice\",&,N,V_device"
- "TQ,R,N,V_options"
- "Tq,R,N"
- "Vv40@0:8Q16@\"NSString\"24@?<v@?S>32"
- "Vv40@0:8Q16@24@?32"
- "Vv60@0:8S16@\"NSString\"20Q28@\"NSString\"36Q44@?<v@?Sq@\"CCDonateServicePriors\">52"
- "Vv60@0:8S16@20Q28@36Q44@?52"
- "_remoteCRDTSetDonationWithDelta:fromDeviceSite:relayedDeviceSites:"
- "_resolvedSetsToSync"
- "attestInSyncDeviceSite:relayedDeviceSites:"
- "determineSyncOperationForDiscoveredSet:outFetchRequest:"
- "enumerateAllSets:withOptions:usingBlock:"
- "fetchMergeableDeltasResponseFromPeerToPeerMessage:"
- "fileTransferSessionInitiatedResponseFromPeerToPeerMessage:peerPublicKey:"
- "mergeRemoteDelta:fromDeviceSite:relayedDeviceSites:"
- "mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:"
- "mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:"
- "registerRemoteDeviceSite:isPeer:hasDeltas:returningRowId:"
- "resolvedSetsToSync"
- "setResolvedSetsToSync:"
- "storedEquivalentForDeviceSite:"
- "syncOperationForDiscoveredSet:versionedMergeable:"
- "v24@?0@\"CCSetDiscoveryResponse\"8@\"NSError\"16"
- "v48@0:8@\"CKMergeableDelta\"16@\"CCDeviceSite\"24@\"NSArray\"32@?<v@?S>40"

```
