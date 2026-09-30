## libauthinstall.dylib

> `/usr/lib/libauthinstall.dylib`

```diff

 1104.60.4.0.0
-  __TEXT.__text: 0x9c2d0
+  __TEXT.__text: 0x9c1e8
   __TEXT.__auth_stubs: 0x1930
   __TEXT.__objc_methlist: 0x27f4
   __TEXT.__cstring: 0x1ee84

   - /usr/lib/updaters/libAppleTconUARPUpdater.dylib
   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: D362F961-2778-3A54-BC98-B0081E503B7C
-  Functions: 3270
-  Symbols:   9390
+  UUID: 845AE979-EE0D-3AA7-BAAF-2E75805BAD4E
+  Functions: 3273
+  Symbols:   9404
   CStrings:  7275
 
Symbols:
+ _OUTLINED_FUNCTION_50
Functions:
~ _OUTLINED_FUNCTION_1 : 20 -> 16
~ _AMAuthInstallPlatformCopyURLWithAppendedComponent : 164 -> 160
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_13
~ _OUTLINED_FUNCTION_16 : 24 -> 16
~ _OUTLINED_FUNCTION_17 : 12 -> 16
~ _OUTLINED_FUNCTION_18 : 16 -> 24
~ _OUTLINED_FUNCTION_19 : 20 -> 12
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_23
- _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_4
~ __ZN13SERestoreInfo11UpdateTableC2ERK7DERItem : 2056 -> 2068
~ __ZNSt3__16vectorINS0_ItNS_9allocatorItEEEENS1_IS3_EEE24__emplace_back_slow_pathIJRS3_EEEPS3_DpOT_ : 304 -> 300
~ __ZNSt3__16vectorIN13SERestoreInfo4BLOBENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIN13SERestoreInfo16UpdateTableEntryENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRS2_EEEPS2_DpOT_ : 376 -> 380
~ __ZNSt3__16vectorINS0_ItNS_9allocatorItEEEENS1_IS3_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorIN13SERestoreInfo2UTENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorItNS_9allocatorItEEE11__vallocateB8ne200100Em : 56 -> 60
~ __ZNSt3__16vectorIN13SERestoreInfo8ApduBLOBENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_ : 344 -> 348
~ __ZNSt3__16__treeINS_12__value_typeI11ImageType_tN13SERestoreInfo4BLOBEEENS_19__map_value_compareIS2_S5_NS_4lessIS2_EELb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIS2_JRKNS_21piecewise_construct_tENS_5tupleIJRKS2_EEENSH_IJEEEEEENS_4pairINS_15__tree_iteratorIS5_PNS_11__tree_nodeIS5_PvEElEEbEERKT_DpOT0_ : 256 -> 264
~ __ZN13SERestoreInfo14SEFirmwareBaseC2EPK8__CFData : 1272 -> 1276
~ __ZNK13SERestoreInfo17SERestoreInfoBase14getRequestDictEv.cold.1 : 76 -> 72
~ _AMAuthInstallBasebandEnablePersonalization : 28 -> 24
~ _AMAuthInstallApEnablePersonalization : 28 -> 24
~ _AMAuthInstallSetLocale : 96 -> 92
~ _AMAuthInstallSetEntitlements : 68 -> 64
~ _AMAuthInstallSetRecoveryOSVariant : 80 -> 76
~ _AMAuthInstallSetMacOSVariantIsPresent : 28 -> 24
~ _AMAuthInstallApSupportsGlobalSigning : 132 -> 128
~ _AMAuthInstallApImg4SetApNonceSlotID : 132 -> 120
~ _AMAuthInstallApSetNonce : 244 -> 232
~ _AMAuthInstallApWriteSignatureStripped : 136 -> 132
~ _AMAuthInstallApSoftwareCoprocessorSetParameters : 80 -> 76
~ _AMAuthInstallApImg3IsImg3Payload : 44 -> 40
~ _AMAuthInstallApImg4SetSepNonce : 148 -> 136
~ _AMAuthInstallApImg4SetSepNonceSlotID : 132 -> 120
~ _AMAuthInstallApImg4ServerRequestAddUIDMode : 244 -> 240
~ _AMAuthInstallApImg4ForceLocalSigning : 36 -> 32
~ _AMAuthInstallApImg4ForceServerSigning : 36 -> 32
~ _AMAuthInstallApImg4SetParameters : 408 -> 396
~ _AMAuthInstallApImg4LocalRegisterKeys : 740 -> 728
~ _AMAuthInstallBasebandCopyAllPersonalizedComponents : 2008 -> 1992
~ _AMAuthInstallBasebandLocalSigningEnabled : 220 -> 208
~ _AMAuthInstallBasebandSupportsServerSigning : 388 -> 376
~ _AMAuthInstallBasebandSetKeyHashRootManifest : 168 -> 164
~ _AMAuthInstallBasebandPersonalizationRequired : 120 -> 116
~ _AMAuthInstallBasebandSetKeyHash : 188 -> 184
~ _AMAuthInstallBasebandSetFusingProfileName : 76 -> 72
~ _AMAuthInstallBasebandCopyNextComponentName : 472 -> 484
~ _AMAuthInstallBasebandSupportsLocalSigning : 372 -> 364
~ _AMAuthInstallBasebandSetKeyHashInternal : 200 -> 196
~ _AMAuthInstallBasebandStitchCopyFile : 64 -> 60
~ _AMAuthInstallBasebandLocalProvisionDevice : 472 -> 484
~ _AMAuthInstallBasebandSetAntennaType : 76 -> 72
~ _AMAuthInstallBasebandSetBehavior : 76 -> 72
~ _AMAuthInstallBasebandIsFused : 72 -> 68
~ _AMAuthInstallBasebandGetChipID : 48 -> 44
~ _AMAuthInstallBasebandSupportsFDR : 212 -> 208
~ _AMAuthInstallBasebandICE3CopyNextComponentName : 184 -> 172
~ _AMAuthInstallBasebandN92LocalProvisionDevice : 112 -> 124
~ _AMAuthInstallBasebandVinylAddMeasurementTags : 508 -> 496
~ _AMAuthInstallBundleOverrideBuildManifestEntries : 188 -> 184
~ _AMAuthInstallBundleOverrideEntries : 192 -> 188
~ _AMAuthInstallBundleAllowLinks : 36 -> 32
~ _AMAuthInstallBundlePreferBuildManifest : 28 -> 24
~ _AMAuthInstallBundleSkipInstallation : 28 -> 24
~ _AMAuthInstallBundleRequestTicketWithoutNonce : 28 -> 24
~ __AMAuthInstallBundleGetValueForReservedKey : 376 -> 372
~ _AMAuthInstallMonetStitchCopyIfPersonalized : 84 -> 80
~ _AMAuthInstallMonetStitchPartitionTable : 84 -> 80
~ _AMAuthInstallProvisioningSetItem : 124 -> 120
~ __AMAuthInstallRembrandtLocalCreatePSIStitchData : 2036 -> 2024
~ _AMAuthInstallRembrandtLocalCreateDigestForKey : 152 -> 144
~ _AMAuthInstallSsoEnable : 104 -> 100
~ _AMAuthInstallVinylCheckVinylFwLdrVerLegacy : 80 -> 76
~ _AMAuthInstallVinylServerRequestAddRequiredTags : 460 -> 448
~ _BbfwReaderClose : 36 -> 32
~ _DERImg4DecodePayloadWithProperties : 184 -> 180
~ _DERImg4DecodePayloadProperties : 128 -> 124
~ _DERImg4DecodeRestoreInfo : 128 -> 124
~ _Img4DecodeGetPayloadVersionPropertyString : 224 -> 220
CStrings:
+ "VinylRestore-144~7522"
- "VinylRestore-144~7456"

```
