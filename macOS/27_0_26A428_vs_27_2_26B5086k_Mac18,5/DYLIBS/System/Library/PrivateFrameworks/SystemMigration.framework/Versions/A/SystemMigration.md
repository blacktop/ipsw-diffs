## SystemMigration

> `/System/Library/PrivateFrameworks/SystemMigration.framework/Versions/A/SystemMigration`

```diff

-6164.1.2.0.0
-  __TEXT.__text: 0xfc264
-  __TEXT.__objc_methlist: 0x105a0
+6164.40.7.0.0
+  __TEXT.__text: 0xfe188
+  __TEXT.__objc_methlist: 0x109a0
   __TEXT.__const: 0x214
-  __TEXT.__gcc_except_tab: 0x3924
-  __TEXT.__cstring: 0x2321a
+  __TEXT.__gcc_except_tab: 0x3bf0
+  __TEXT.__cstring: 0x23aca
   __TEXT.__oslogstring: 0x402
   __TEXT.__ustring: 0x147c
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_typeref: 0x1a
   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x3c40
+  __TEXT.__unwind_info: 0x3cd8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xc58
-  __DATA_CONST.__objc_classlist: 0x5e0
+  __DATA_CONST.__const: 0xd50
+  __DATA_CONST.__objc_classlist: 0x5e8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8328
+  __DATA_CONST.__objc_selrefs: 0x85b8
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x4b0
-  __DATA_CONST.__objc_arraydata: 0x6b8
-  __DATA_CONST.__got: 0xec8
+  __DATA_CONST.__objc_arraydata: 0x778
+  __DATA_CONST.__got: 0xed0
   __AUTH_CONST.__const: 0x1bd0
-  __AUTH_CONST.__cfstring: 0x19480
-  __AUTH_CONST.__objc_const: 0x16e08
-  __AUTH_CONST.__objc_intobj: 0x690
+  __AUTH_CONST.__cfstring: 0x19be0
+  __AUTH_CONST.__objc_const: 0x174f8
+  __AUTH_CONST.__objc_intobj: 0x780
   __AUTH_CONST.__objc_arrayobj: 0x438
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x9a0
-  __AUTH.__objc_data: 0x3a60
+  __AUTH.__objc_data: 0x3ab0
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x121c
+  __DATA.__objc_ivar: 0x12a4
   __DATA.__data: 0x1310
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x78

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5619
-  Symbols:   13009
-  CStrings:  4007
+  Functions: 5703
+  Symbols:   13239
+  CStrings:  4066
 
Symbols:
+ +[SMDiscoveryIneligibleReasonTransformer allowsReverseTransformation]
+ +[SMDiscoveryIneligibleReasonTransformer transformedValueClass]
+ +[SMManager currentSystemRetainBalance]
+ -[SMDiscoveryIneligibleReasonTransformer transformedValue:]
+ -[SMTelemetryHandler beginDiscoverySession]
+ -[SMTelemetryHandler didFlushDiscoverySnapshot]
+ -[SMTelemetryHandler didSendAnyEvent]
+ -[SMTelemetryHandler discoveryMetricsBaseline]
+ -[SMTelemetryHandler flushDiscoverySnapshotIfNeeded]
+ -[SMTelemetryHandler payloadLock]
+ -[SMTelemetryHandler recordDiscoveredSourceOfType:]
+ -[SMTelemetryHandler recordDiscoveryIneligibleReason:]
+ -[SMTelemetryHandler recordDiscoveryMountAttempt]
+ -[SMTelemetryHandler recordDiscoveryMountFailure]
+ -[SMTelemetryHandler recordDiscoveryUnsupportedDeviceSkipped]
+ -[SMTelemetryHandler recordPairingAttempted]
+ -[SMTelemetryHandler recordPairingFailureReason:]
+ -[SMTelemetryHandler recordPairingSucceeded]
+ -[SMTelemetryHandler recordSystemRetainBalanceAtStop:]
+ -[SMTelemetryHandler sendDiscoveryBeginSnapshot]
+ -[SMTelemetryHandler setDidFlushDiscoverySnapshot:]
+ -[SMTelemetryHandler setDidSendAnyEvent:]
+ -[SMTelemetryHandler setDiscoveryMetricsBaseline:]
+ -[SMTelemetryHandler setPayloadLock:]
+ -[SMTelemetryPayload discoveryIneligibleCaseSensitivityMismatchCount]
+ -[SMTelemetryPayload discoveryIneligibleCount]
+ -[SMTelemetryPayload discoveryIneligibleDamagedOrOtherCount]
+ -[SMTelemetryPayload discoveryIneligibleDestNeedsUpgradeCount]
+ -[SMTelemetryPayload discoveryIneligibleInstallMediaCount]
+ -[SMTelemetryPayload discoveryIneligibleMissingDataVolumeCount]
+ -[SMTelemetryPayload discoveryIneligibleNotMacOSCount]
+ -[SMTelemetryPayload discoveryIneligibleServerInstallCount]
+ -[SMTelemetryPayload discoveryIneligibleSourceOSTooOldCount]
+ -[SMTelemetryPayload discoveryIneligibleWindowsClientTooNewCount]
+ -[SMTelemetryPayload discoveryIneligibleWindowsClientTooOldCount]
+ -[SMTelemetryPayload discoveryMountAttempts]
+ -[SMTelemetryPayload discoveryMountFailures]
+ -[SMTelemetryPayload discoveryPeerAppearances]
+ -[SMTelemetryPayload discoveryPeerDisappearances]
+ -[SMTelemetryPayload discoveryResolveAttempts]
+ -[SMTelemetryPayload discoveryResolveRetries]
+ -[SMTelemetryPayload discoveryResolveTimeouts]
+ -[SMTelemetryPayload discoverySilentRejectCount]
+ -[SMTelemetryPayload discoverySourcesLocalDisk]
+ -[SMTelemetryPayload discoverySourcesMac]
+ -[SMTelemetryPayload discoverySourcesNetworkShare]
+ -[SMTelemetryPayload discoverySourcesTimeMachine]
+ -[SMTelemetryPayload discoverySourcesTotal]
+ -[SMTelemetryPayload discoverySourcesWindows]
+ -[SMTelemetryPayload discoveryUnsupportedDeviceSkipped]
+ -[SMTelemetryPayload pairingAttempted]
+ -[SMTelemetryPayload pairingFailureReason]
+ -[SMTelemetryPayload pairingSucceeded]
+ -[SMTelemetryPayload setDiscoveryIneligibleCaseSensitivityMismatchCount:]
+ -[SMTelemetryPayload setDiscoveryIneligibleCount:]
+ -[SMTelemetryPayload setDiscoveryIneligibleDamagedOrOtherCount:]
+ -[SMTelemetryPayload setDiscoveryIneligibleDestNeedsUpgradeCount:]
+ -[SMTelemetryPayload setDiscoveryIneligibleInstallMediaCount:]
+ -[SMTelemetryPayload setDiscoveryIneligibleMissingDataVolumeCount:]
+ -[SMTelemetryPayload setDiscoveryIneligibleNotMacOSCount:]
+ -[SMTelemetryPayload setDiscoveryIneligibleServerInstallCount:]
+ -[SMTelemetryPayload setDiscoveryIneligibleSourceOSTooOldCount:]
+ -[SMTelemetryPayload setDiscoveryIneligibleWindowsClientTooNewCount:]
+ -[SMTelemetryPayload setDiscoveryIneligibleWindowsClientTooOldCount:]
+ -[SMTelemetryPayload setDiscoveryMountAttempts:]
+ -[SMTelemetryPayload setDiscoveryMountFailures:]
+ -[SMTelemetryPayload setDiscoveryPeerAppearances:]
+ -[SMTelemetryPayload setDiscoveryPeerDisappearances:]
+ -[SMTelemetryPayload setDiscoveryResolveAttempts:]
+ -[SMTelemetryPayload setDiscoveryResolveRetries:]
+ -[SMTelemetryPayload setDiscoveryResolveTimeouts:]
+ -[SMTelemetryPayload setDiscoverySilentRejectCount:]
+ -[SMTelemetryPayload setDiscoverySourcesLocalDisk:]
+ -[SMTelemetryPayload setDiscoverySourcesMac:]
+ -[SMTelemetryPayload setDiscoverySourcesNetworkShare:]
+ -[SMTelemetryPayload setDiscoverySourcesTimeMachine:]
+ -[SMTelemetryPayload setDiscoverySourcesTotal:]
+ -[SMTelemetryPayload setDiscoverySourcesWindows:]
+ -[SMTelemetryPayload setDiscoveryUnsupportedDeviceSkipped:]
+ -[SMTelemetryPayload setPairingAttempted:]
+ -[SMTelemetryPayload setPairingFailureReason:]
+ -[SMTelemetryPayload setPairingSucceeded:]
+ -[SMTelemetryPayload setSystemRetainBalanceAtStop:]
+ -[SMTelemetryPayload systemRetainBalanceAtStop]
+ GCC_except_table33
+ OBJC_IVAR_$_SMTelemetryHandler._didFlushDiscoverySnapshot
+ OBJC_IVAR_$_SMTelemetryHandler._didSendAnyEvent
+ OBJC_IVAR_$_SMTelemetryHandler._discoveryMetricsBaseline
+ OBJC_IVAR_$_SMTelemetryHandler._payloadLock
+ OBJC_IVAR_$_SMTelemetryPayload._discoveryIneligibleCaseSensitivityMismatchCount
+ OBJC_IVAR_$_SMTelemetryPayload._discoveryIneligibleCount
+ OBJC_IVAR_$_SMTelemetryPayload._discoveryIneligibleDamagedOrOtherCount
+ OBJC_IVAR_$_SMTelemetryPayload._discoveryIneligibleDestNeedsUpgradeCount
+ OBJC_IVAR_$_SMTelemetryPayload._discoveryIneligibleInstallMediaCount
+ OBJC_IVAR_$_SMTelemetryPayload._discoveryIneligibleMissingDataVolumeCount
+ OBJC_IVAR_$_SMTelemetryPayload._discoveryIneligibleNotMacOSCount
+ OBJC_IVAR_$_SMTelemetryPayload._discoveryIneligibleServerInstallCount
+ OBJC_IVAR_$_SMTelemetryPayload._discoveryIneligibleSourceOSTooOldCount
+ OBJC_IVAR_$_SMTelemetryPayload._discoveryIneligibleWindowsClientTooNewCount
+ OBJC_IVAR_$_SMTelemetryPayload._discoveryIneligibleWindowsClientTooOldCount
+ OBJC_IVAR_$_SMTelemetryPayload._discoveryMountAttempts
+ OBJC_IVAR_$_SMTelemetryPayload._discoveryMountFailures
+ OBJC_IVAR_$_SMTelemetryPayload._discoveryPeerAppearances
+ OBJC_IVAR_$_SMTelemetryPayload._discoveryPeerDisappearances
+ OBJC_IVAR_$_SMTelemetryPayload._discoveryResolveAttempts
+ OBJC_IVAR_$_SMTelemetryPayload._discoveryResolveRetries
+ OBJC_IVAR_$_SMTelemetryPayload._discoveryResolveTimeouts
+ OBJC_IVAR_$_SMTelemetryPayload._discoverySilentRejectCount
+ OBJC_IVAR_$_SMTelemetryPayload._discoverySourcesLocalDisk
+ OBJC_IVAR_$_SMTelemetryPayload._discoverySourcesMac
+ OBJC_IVAR_$_SMTelemetryPayload._discoverySourcesNetworkShare
+ OBJC_IVAR_$_SMTelemetryPayload._discoverySourcesTimeMachine
+ OBJC_IVAR_$_SMTelemetryPayload._discoverySourcesTotal
+ OBJC_IVAR_$_SMTelemetryPayload._discoverySourcesWindows
+ OBJC_IVAR_$_SMTelemetryPayload._discoveryUnsupportedDeviceSkipped
+ OBJC_IVAR_$_SMTelemetryPayload._pairingAttempted
+ OBJC_IVAR_$_SMTelemetryPayload._pairingFailureReason
+ OBJC_IVAR_$_SMTelemetryPayload._pairingSucceeded
+ OBJC_IVAR_$_SMTelemetryPayload._systemRetainBalanceAtStop
+ _OBJC_CLASS_$_SMDiscoveryIneligibleReasonTransformer
+ _OBJC_CLASS_$_SMNDiscoveryMetrics
+ _OBJC_METACLASS_$_SMDiscoveryIneligibleReasonTransformer
+ _SMDiscoveryIneligibleCaseSensitivityMismatchCountKey
+ _SMDiscoveryIneligibleCountKey
+ _SMDiscoveryIneligibleDamagedOrOtherCountKey
+ _SMDiscoveryIneligibleDestNeedsUpgradeCountKey
+ _SMDiscoveryIneligibleInstallMediaCountKey
+ _SMDiscoveryIneligibleMissingDataVolumeCountKey
+ _SMDiscoveryIneligibleNotMacOSCountKey
+ _SMDiscoveryIneligibleServerInstallCountKey
+ _SMDiscoveryIneligibleSourceOSTooOldCountKey
+ _SMDiscoveryIneligibleWindowsClientTooNewCountKey
+ _SMDiscoveryIneligibleWindowsClientTooOldCountKey
+ _SMDiscoveryMountAttemptsKey
+ _SMDiscoveryMountFailuresKey
+ _SMDiscoveryPeerAppearancesKey
+ _SMDiscoveryPeerDisappearancesKey
+ _SMDiscoveryResolveAttemptsKey
+ _SMDiscoveryResolveRetriesKey
+ _SMDiscoveryResolveTimeoutsKey
+ _SMDiscoverySilentRejectCountKey
+ _SMDiscoverySourcesLocalDiskKey
+ _SMDiscoverySourcesMacKey
+ _SMDiscoverySourcesNetworkShareKey
+ _SMDiscoverySourcesTimeMachineKey
+ _SMDiscoverySourcesTotalKey
+ _SMDiscoverySourcesWindowsKey
+ _SMDiscoveryUnsupportedDeviceSkippedKey
+ _SMPairingAttemptedKey
+ _SMPairingFailureReasonKey
+ _SMPairingSucceededKey
+ _SMSystemRetainBalanceAtStopKey
+ __OBJC_$_CLASS_METHODS_SMDiscoveryIneligibleReasonTransformer
+ __OBJC_$_INSTANCE_METHODS_SMDiscoveryIneligibleReasonTransformer
+ __OBJC_CLASS_RO_$_SMDiscoveryIneligibleReasonTransformer
+ __OBJC_METACLASS_RO_$_SMDiscoveryIneligibleReasonTransformer
+ ___block_descriptor_81_e8_32s40s48s56r64r72r_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56r64r72r
+ ___destroy_helper_block_e8_32s40s48s56r64r72r
+ _objc_msgSend$beginDiscoverySession
+ _objc_msgSend$currentSystemRetainBalance
+ _objc_msgSend$discoveryIneligibleCaseSensitivityMismatchCount
+ _objc_msgSend$discoveryIneligibleCount
+ _objc_msgSend$discoveryIneligibleDamagedOrOtherCount
+ _objc_msgSend$discoveryIneligibleDestNeedsUpgradeCount
+ _objc_msgSend$discoveryIneligibleInstallMediaCount
+ _objc_msgSend$discoveryIneligibleMissingDataVolumeCount
+ _objc_msgSend$discoveryIneligibleNotMacOSCount
+ _objc_msgSend$discoveryIneligibleServerInstallCount
+ _objc_msgSend$discoveryIneligibleSourceOSTooOldCount
+ _objc_msgSend$discoveryIneligibleWindowsClientTooNewCount
+ _objc_msgSend$discoveryIneligibleWindowsClientTooOldCount
+ _objc_msgSend$discoveryMountAttempts
+ _objc_msgSend$discoveryMountFailures
+ _objc_msgSend$discoveryPeerAppearances
+ _objc_msgSend$discoveryPeerDisappearances
+ _objc_msgSend$discoveryResolveAttempts
+ _objc_msgSend$discoveryResolveRetries
+ _objc_msgSend$discoveryResolveTimeouts
+ _objc_msgSend$discoverySilentRejectCount
+ _objc_msgSend$discoverySourcesLocalDisk
+ _objc_msgSend$discoverySourcesMac
+ _objc_msgSend$discoverySourcesNetworkShare
+ _objc_msgSend$discoverySourcesTimeMachine
+ _objc_msgSend$discoverySourcesTotal
+ _objc_msgSend$discoverySourcesWindows
+ _objc_msgSend$discoveryUnsupportedDeviceSkipped
+ _objc_msgSend$flushDiscoverySnapshotIfNeeded
+ _objc_msgSend$pairingAttempted
+ _objc_msgSend$pairingFailureReason
+ _objc_msgSend$pairingSucceeded
+ _objc_msgSend$recordDiscoveredSourceOfType:
+ _objc_msgSend$recordDiscoveryIneligibleReason:
+ _objc_msgSend$recordDiscoveryMountAttempt
+ _objc_msgSend$recordDiscoveryMountFailure
+ _objc_msgSend$recordDiscoveryUnsupportedDeviceSkipped
+ _objc_msgSend$recordPairingAttempted
+ _objc_msgSend$recordPairingFailureReason:
+ _objc_msgSend$recordPairingSucceeded
+ _objc_msgSend$recordSystemRetainBalanceAtStop:
+ _objc_msgSend$sendDiscoveryBeginSnapshot
+ _objc_msgSend$setDiscoveryIneligibleCaseSensitivityMismatchCount:
+ _objc_msgSend$setDiscoveryIneligibleCount:
+ _objc_msgSend$setDiscoveryIneligibleDamagedOrOtherCount:
+ _objc_msgSend$setDiscoveryIneligibleDestNeedsUpgradeCount:
+ _objc_msgSend$setDiscoveryIneligibleInstallMediaCount:
+ _objc_msgSend$setDiscoveryIneligibleMissingDataVolumeCount:
+ _objc_msgSend$setDiscoveryIneligibleNotMacOSCount:
+ _objc_msgSend$setDiscoveryIneligibleServerInstallCount:
+ _objc_msgSend$setDiscoveryIneligibleSourceOSTooOldCount:
+ _objc_msgSend$setDiscoveryIneligibleWindowsClientTooNewCount:
+ _objc_msgSend$setDiscoveryIneligibleWindowsClientTooOldCount:
+ _objc_msgSend$setDiscoveryMountAttempts:
+ _objc_msgSend$setDiscoveryMountFailures:
+ _objc_msgSend$setDiscoveryPeerAppearances:
+ _objc_msgSend$setDiscoveryPeerDisappearances:
+ _objc_msgSend$setDiscoveryResolveAttempts:
+ _objc_msgSend$setDiscoveryResolveRetries:
+ _objc_msgSend$setDiscoveryResolveTimeouts:
+ _objc_msgSend$setDiscoverySilentRejectCount:
+ _objc_msgSend$setDiscoverySourcesLocalDisk:
+ _objc_msgSend$setDiscoverySourcesMac:
+ _objc_msgSend$setDiscoverySourcesNetworkShare:
+ _objc_msgSend$setDiscoverySourcesTimeMachine:
+ _objc_msgSend$setDiscoverySourcesTotal:
+ _objc_msgSend$setDiscoverySourcesWindows:
+ _objc_msgSend$setDiscoveryUnsupportedDeviceSkipped:
+ _objc_msgSend$setPairingAttempted:
+ _objc_msgSend$setPairingFailureReason:
+ _objc_msgSend$setPairingSucceeded:
+ _objc_msgSend$setSystemRetainBalanceAtStop:
+ _objc_msgSend$snapshot
+ _objc_msgSend$systemRetainBalanceAtStop
- ___block_descriptor_73_e8_32s40s48s56r64r_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56r64r
- ___destroy_helper_block_e8_32s40s48s56r64r
CStrings:
+ "DiscoveryFlush"
+ "DiscoveryIneligibleCaseSensitivityMismatchCount"
+ "DiscoveryIneligibleCount"
+ "DiscoveryIneligibleDamagedOrOtherCount"
+ "DiscoveryIneligibleDestNeedsUpgradeCount"
+ "DiscoveryIneligibleInstallMediaCount"
+ "DiscoveryIneligibleMissingDataVolumeCount"
+ "DiscoveryIneligibleNotMacOSCount"
+ "DiscoveryIneligibleServerInstallCount"
+ "DiscoveryIneligibleSourceOSTooOldCount"
+ "DiscoveryIneligibleWindowsClientTooNewCount"
+ "DiscoveryIneligibleWindowsClientTooOldCount"
+ "DiscoveryMountAttempts"
+ "DiscoveryMountFailures"
+ "DiscoveryPeerAppearances"
+ "DiscoveryPeerDisappearances"
+ "DiscoveryResolveAttempts"
+ "DiscoveryResolveRetries"
+ "DiscoveryResolveTimeouts"
+ "DiscoverySilentRejectCount"
+ "DiscoverySourcesLocalDisk"
+ "DiscoverySourcesMac"
+ "DiscoverySourcesNetworkShare"
+ "DiscoverySourcesTimeMachine"
+ "DiscoverySourcesTotal"
+ "DiscoverySourcesWindows"
+ "DiscoveryUnsupportedDeviceSkipped"
+ "INELIGIBLE_MACOS_TOO_OLD"
+ "INELIGIBLE_OSX_TOO_OLD"
+ "Library/IdentityServices/NGMTrustStore-identityservicesd.db"
+ "Library/IdentityServices/NGMTrustStore-identityservicesd.db-shm"
+ "Library/IdentityServices/NGMTrustStore-identityservicesd.db-wal"
+ "Library/IdentityServices/PDS/"
+ "Library/IdentityServices/PacketLogs/"
+ "Library/IdentityServices/RegistrationOperations/"
+ "Library/IdentityServices/files/"
+ "Library/IdentityServices/ids-firewall-identityservicesd.db"
+ "Library/IdentityServices/ids-firewall-identityservicesd.db-shm"
+ "Library/IdentityServices/ids-firewall-identityservicesd.db-wal"
+ "Library/IdentityServices/ids-gossip.db"
+ "Library/IdentityServices/ids-gossip.db-shm"
+ "Library/IdentityServices/ids-gossip.db-wal"
+ "Library/IdentityServices/ids-hashes-identityservicesd.db"
+ "Library/IdentityServices/ids-hashes-identityservicesd.db-shm"
+ "Library/IdentityServices/ids-hashes-identityservicesd.db-wal"
+ "Library/IdentityServices/ids-query.db"
+ "Library/IdentityServices/ids-query.db-shm"
+ "Library/IdentityServices/ids-query.db-wal"
+ "Library/IdentityServices/ids.db"
+ "Library/IdentityServices/ids.db-shm"
+ "Library/IdentityServices/ids.db-wal"
+ "Library/IdentityServices/idstatuscache.plist"
+ "Library/IdentityServices/incomingfiles/"
+ "PairingAttempted"
+ "PairingFailureReason"
+ "PairingSucceeded"
+ "SMDiscoveryIneligibleReasonTransformer"
+ "Scanner: SMDiscoveryIneligibleReasonTransformer did not resolve; counting as DamagedOrOther"
+ "SystemRetainBalanceAtStop"
```
