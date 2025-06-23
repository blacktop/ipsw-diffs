## TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

```diff

-61123.100.169.0.0
-  __TEXT.__text: 0x1edcc4
-  __TEXT.__auth_stubs: 0x1c60
+61123.120.34.0.0
+  __TEXT.__text: 0x1fd378
+  __TEXT.__auth_stubs: 0x1d50
   __TEXT.__objc_stubs: 0x2a00
   __TEXT.__objc_methlist: 0x2934
-  __TEXT.__const: 0x80f8
-  __TEXT.__cstring: 0x1ccbb
-  __TEXT.__objc_methname: 0x7db0
+  __TEXT.__const: 0x8198
+  __TEXT.__cstring: 0x1df6f
+  __TEXT.__objc_methname: 0x801a
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x2e08
-  __TEXT.__swift5_typeref: 0x300e
-  __TEXT.__swift5_fieldmd: 0x2070
-  __TEXT.__swift5_reflstr: 0x1c8b
+  __TEXT.__constg_swiftt: 0x2e40
+  __TEXT.__swift5_typeref: 0x302a
+  __TEXT.__swift5_fieldmd: 0x20b8
+  __TEXT.__swift5_reflstr: 0x1d4b
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x348
-  __TEXT.__swift5_proto: 0x728
+  __TEXT.__swift5_proto: 0x72c
   __TEXT.__swift5_types: 0x228
   __TEXT.__objc_classname: 0x464
-  __TEXT.__objc_methtype: 0x1e3c
+  __TEXT.__objc_methtype: 0x1ed6
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__swift5_capture: 0x3080
+  __TEXT.__swift5_capture: 0x3094
   __TEXT.__gcc_except_tab: 0x148
   __TEXT.__swift5_protos: 0x18
   __TEXT.__dlopen_cstrs: 0x216
   __TEXT.__oslogstring: 0x2cc
-  __TEXT.__unwind_info: 0x4d5c
-  __TEXT.__eh_frame: 0x6098
-  __DATA_CONST.__auth_got: 0xe40
-  __DATA_CONST.__got: 0x430
+  __TEXT.__unwind_info: 0x5248
+  __TEXT.__eh_frame: 0x64a8
+  __DATA_CONST.__auth_got: 0xeb8
+  __DATA_CONST.__got: 0x478
   __DATA_CONST.__auth_ptr: 0x78
-  __DATA_CONST.__const: 0x83d0
-  __DATA_CONST.__cfstring: 0x1f20
+  __DATA_CONST.__const: 0x8408
+  __DATA_CONST.__cfstring: 0x1fe0
   __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd8

   __DATA_CONST.__objc_classrefs: 0x388
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x7618
-  __DATA.__objc_selrefs: 0x1e10
+  __DATA.__objc_const: 0x7658
+  __DATA.__objc_selrefs: 0x1e50
   __DATA.__objc_ivar: 0x2a0
-  __DATA.__objc_data: 0x2780
-  __DATA.__data: 0xe100
+  __DATA.__objc_data: 0x27c0
+  __DATA.__data: 0xe138
   __DATA.__objc_stublist: 0x78
-  __DATA.__common: 0x790
-  __DATA.__bss: 0xe1f0
+  __DATA.__common: 0x7a0
+  __DATA.__bss: 0xe270
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1E8EC3A3-7364-3795-B0C9-4E5EEF0A9401
-  Functions: 9061
-  Symbols:   456
-  CStrings:  3399
+  UUID: 50BE3271-F521-30D6-8028-12E905A2218A
+  Functions: 9099
+  Symbols:   465
+  CStrings:  3496
 
Symbols:
+ __set_user_dir_suffix
+ _confstr
+ _kSecurityRTCEventNameAllowedMIDHashMismatch
+ _kSecurityRTCEventNameDeletedMIDHashMismatch
+ _kSecurityRTCEventNameDuplicateMachineID
+ _kSecurityRTCEventNameMIDVanishedFromTDL
+ _kSecurityRTCEventNameTDLProcessingSuccess
+ _kSecurityRTCFieldEgoMachineIDVanishedFromTDL
+ _objc_retain_x1
CStrings:
+ "@\"NSArray\"24@0:8^@16"
+ "@\"TPPeer\"32@0:8@\"NSString\"16^@24"
+ "B32@0:8@?16^@24"
+ "B32@0:8@?<v@?@\"TPPeer\"^B>16^@24"
+ "B32@0:8@?<v@?@\"TPVoucher\"^B>16^@24"
+ "Couldn't find ego peer in model"
+ "Error determining whether Custodian Recovery Key is trusted: %{public}@"
+ "Error determining whether Recovery Key is enrolled: %{public}@"
+ "Error enumerating peers: %{public}@"
+ "Error enumerating vouchers: %{public}@"
+ "Error fetching all policy versions: %{public}@"
+ "Error getting ego peer from model: %{public}s"
+ "Error getting included peer (%s) from model: %{public}s"
+ "Error getting peer that trusts CRK: %{public}@"
+ "Error getting peer with machineID %{public}s: %{public}s"
+ "Error getting peerCount: %{public}@"
+ "Error getting sponsor (%s): %{public}s"
+ "Error getting trusted peer %s from model: %{public}s"
+ "Failed to fetch machineIDs: %{public}s"
+ "Failed to fetch modifiedDates: %{public}s"
+ "Failed to fetch peer count: %{public}s"
+ "Failed to get (current self) ego peer from model: %{public}s"
+ "Failed to get peer that trusts RK: %{public}@"
+ "Failed to save: %{public}s"
+ "Q24@0:8^@16"
+ "TrustedPeersHelper/Sandbox.swift"
+ "Unable to fetch dynamic info for self: %{public}@"
+ "Unable to read _CS_DARWIN_USER_TEMP_DIR!"
+ "_set_user_dir_suffix() failed!"
+ "allMachineIDsWithError:"
+ "allPeerIDs:"
+ "allPolicyVersionsWithError:"
+ "allowedMIDHashMismatch"
+ "anyTrustedPeerDistrustsOtherPeer:error:"
+ "bestRecoveryKeyForStableInfo:vouchers:error:"
+ "bestWalrusAcrossTrustedPeersWithError:"
+ "bestWalrusForStableInfo:walrusStableChanges:error:"
+ "bestWebAccessAcrossTrustedPeersWithError:"
+ "bestWebAccessForStableInfo:webAccessStableChanges:error:"
+ "com.apple.TrustedPeersHelper"
+ "com.apple.security.allowedMIDHashMismatch"
+ "com.apple.security.deletedMIDHashMismatch"
+ "com.apple.security.duplicateMachineID"
+ "com.apple.security.midVanishedFromTDL"
+ "com.apple.security.tdlProcessingSuccess"
+ "currentStatePossiblyMissingData error: %{public}@"
+ "currentStatePossiblyMissingDataWithError:"
+ "deletedMIDHashMismatch"
+ "doesOctagonContainDistrustedRecoveryKeysWithError:"
+ "duplicateMachineIDDetected"
+ "egoMachineIDVanishedFromTDL"
+ "ensureEgoConsistency failed to create TPPeerStableInfo from model: %{public}@"
+ "enumeratePeersUsingBlock:error:"
+ "enumerateVouchersUsingBlock:error:"
+ "error calling %s: %{public}@"
+ "error calling hasAnyPeers: %{public}@"
+ "error calling statusOfPeer: %{public}@"
+ "error determine whether CRK is trusted: %{public}@"
+ "error determining whether Custodian Recovery Key is trusted: %{public}@"
+ "error determining whether Recovery Key is enrolled: %{public}@"
+ "error determining whether octagon contains distrusted RKs: %{public}@"
+ "error getting peerCount: %{public}@"
+ "errorEnumeratingPeers"
+ "errorEnumeratingVouchers"
+ "fetchAccountSettings unable to find best ADP: %{public}s"
+ "fetchAccountSettings unable to find best web access: %{public}s"
+ "fetchAfterEstablish: error finding peer %{public}s in model: %{public}@"
+ "fetchTrustState error calling statusOfPeer: %{public}@"
+ "fetchTrustState: error calling getStableInfoForPeer %s: %{public}@"
+ "fetchTrustState: error calling hasPotentiallyTrustedPeerPreapprovingKey %{public}@"
+ "getDynamicInfoForPeerWithID:error:"
+ "getStableInfoForPeerWithID:error:"
+ "hasAnyPeersWithError:"
+ "hasChanges"
+ "hasPeerWithID:error:"
+ "hasPotentiallyTrustedPeerPreapprovingKey:error:"
+ "hasPotentiallyTrustedPeerWithSigningKey:error:"
+ "initWithPermanentInfo:stableInfo:dynamicInfo:checkSig:error:"
+ "initWithUnsignedInteger:"
+ "isCustodianRecoveryKeyTrusted:error:"
+ "isRecoveryKeyEnrolledWithError:"
+ "loadModel error getting peerCount: %{public}@"
+ "loadModel error getting voucherCount: %{public}@"
+ "loadModel: evictedMachineIDs: %{public}s"
+ "loadModel: ghostedMachineIDs: %{public}s"
+ "loadModel: unknownMachineIDs: %{public}s"
+ "loadModel: unknownReasonMachineIDs: %{public}s"
+ "machineID == %@ && container == %@"
+ "machineIDVanishedFromTDL"
+ "onqueueRemoveDuplicateMachineIDs error removing duplicate machineIDs: %{public}@"
+ "onqueueRemoveDuplicateMachineIDs removing: %s"
+ "peerCount:"
+ "peerCountWithError:"
+ "peerCountsByMachineIDWithError:"
+ "peerIDThatTrustsCustodianRecoveryKeys:canIntroducePeer:stableInfo:error:"
+ "peerIDThatTrustsRecoveryKeys:canIntroducePeer:stableInfo:error:"
+ "peerWithID:error:"
+ "permanentInfoWithPeerID:data:sig:keyFactory:checkSig:"
+ "preapprovedJoin: error calling hasPotentiallyTrustedPeerPreapprovingKey %{public}@"
+ "preapprovedJoin: error getting peerCount: %{public}@"
+ "preflightCustodianRecoveryKey Error finding peer with ID %{public}s: %{public}s"
+ "preflightCustodianRecoveryKey Failed to find peer with ID %{public}s"
+ "preflightCustodianRecoveryKey error getting peer that trusts CRK: %{public}@"
+ "preflightCustodianRecoveryKey: error determining whether custodian recovery key is trusted: %{public}@"
+ "preflightPreapprovedJoin: error calling hasPotentiallyTrustedPeerPreapprovingKey %{public}@"
+ "preflightPreapprovedJoin: error calling hasPotentiallyTrustedPeerWithSigningKey %{public}@"
+ "preflightRecoverOctagonWithRecoveryKey: error determining whether Recovery Key is enrolled: %{public}@"
+ "preflightRecoveryKey Error finding peer with ID %{public}s: %{public}s"
+ "preflightRecoveryKey Failed to find peer with ID %{public}s"
+ "preflightRecoveryKey failed to get peer that trusts RK: %{public}@"
+ "preflightRecoveryKey: error determine whether Recovery Key is enrolled: %{public}@"
+ "preflightVouchWithBottle Error finding peer with ID %{public}s: %{public}s"
+ "preflightVouchWithBottle found no peer to match bottle with ID %{public}s"
+ "recoveryKey is enrolled %{bool,public}d"
+ "setAllowedMachineIDs(_:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:honorIDMSListChanges:version:flowID:deviceSessionID:canSendMetrics:altDSID:trustedDeviceHash:deletedDeviceHash:trustedDevicesUpdateTimestamp:reply:)"
+ "setAllowedMachineIDsWithSpecificUser:allowedMachineIDs:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:honorIDMSListChanges:version:flowID:deviceSessionID:canSendMetrics:altDSID:trustedDeviceHash:deletedDeviceHash:trustedDevicesUpdateTimestamp:reply:"
+ "setPreapprovedKeys: error getting ego peer from model: %{public}s"
+ "sha256 of allowed list: %{public}s"
+ "sha256 of deleted list: %{public}s"
+ "statusOfPeerWithID:error:"
+ "testEgoMachineIDVanished"
+ "testHashMismatchDetected"
+ "trustedPeerCountWithError:"
+ "updateTrustIfNeeded: error calling hasPotentiallyTrustedPeerPreapprovingKey %{public}@"
+ "updateTrustIfNeeded: ignoring additional error calling statusOfPeer: %{public}@"
+ "v128@0:8@\"TPSpecificUser\"16@\"NSSet\"24@\"NSSet\"32@\"NSSet\"40@\"NSSet\"48B56@\"NSString\"60@\"NSString\"68@\"NSString\"76B84@\"NSString\"88@\"NSString\"96@\"NSString\"104@\"NSNumber\"112@?<v@?B@\"NSError\">120"
+ "v128@0:8@16@24@32@40@48B56@60@68@76B84@88@96@104@112@?120"
+ "verifyHMACWithPermanentInfoData:permanentInfoSig:stableInfoData:stableInfoSig:dynamicInfoData:dynamicInfoSig:hmacKey:hmacSig:"
+ "viablePeerCountsByModelIDWithError:"
+ "voucherCount:"
+ "voucherCountWithError:"
- "@\"NSArray\"16@0:8"
- "@\"TPPeer\"24@0:8@\"NSString\"16"
- "Failed to calculate hasAnyPeers: %{public}s"
- "Failed to verify hmac"
- "allMachineIDs"
- "allPeerIDs"
- "allPolicyVersions"
- "anyTrustedPeerDistrustsOtherPeer:"
- "bestRecoveryKeyForStableInfo:vouchers:"
- "bestWalrusAcrossTrustedPeers"
- "bestWalrusForStableInfo:walrusStableChanges:"
- "bestWebAccessAcrossTrustedPeers"
- "bestWebAccessForStableInfo:webAccessStableChanges:"
- "countOfTrustedPeers"
- "currentStatePossiblyMissingData"
- "doesOctagonContainsDistrustedRecoveryKeys"
- "enumeratePeersUsingBlock:"
- "enumerateVouchersUsingBlock:"
- "getDynamicInfoForPeerWithID:"
- "getStableInfoForPeerWithID:"
- "hasAnyPeers"
- "hasPeerWithID:"
- "hasPotentiallyTrustedPeerPreapprovingKey:"
- "hasPotentiallyTrustedPeerWithSigningKey:"
- "initWithPermanentInfo:stableInfo:dynamicInfo:hmacKey:hmacSig:error:"
- "isCustodianRecoveryKeyTrusted:"
- "isRecoveryKeyEnrolled"
- "peerCount"
- "peerIDThatTrustsCustodianRecoveryKeys:canIntroducePeer:stableInfo:"
- "peerIDThatTrustsRecoveryKeys:canIntroducePeer:stableInfo:"
- "peerWithID:"
- "preflightCustodianRecoveryKey Failed to find peer with ID"
- "preflightRecoveryKey Failed to find peer with ID"
- "preflightVouchWithBottle found no peer to match bottle"
- "recoveryKey is enrolled %{bool}d, privacy: .public)"
- "setAllowedMachineIDs(_:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:honorIDMSListChanges:version:reply:)"
- "setAllowedMachineIDsWithSpecificUser:allowedMachineIDs:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:honorIDMSListChanges:version:reply:"
- "statusOfPeerWithID:"
- "v24@0:8@?<v@?@\"TPPeer\"^B>16"
- "v24@0:8@?<v@?@\"TPVoucher\"^B>16"
- "v76@0:8@\"TPSpecificUser\"16@\"NSSet\"24@\"NSSet\"32@\"NSSet\"40@\"NSSet\"48B56@\"NSString\"60@?<v@?B@\"NSError\">68"
- "v76@0:8@16@24@32@40@48B56@60@?68"
- "voucherCount"

```
