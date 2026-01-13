## SiriInstrumentation

> `/System/Library/PrivateFrameworks/SiriInstrumentation.framework/Versions/A/SiriInstrumentation`

```diff

-3515.3.1.0.0
-  __TEXT.__text: 0xb169f4
+3515.7.1.0.0
+  __TEXT.__text: 0xb1afdc
   __TEXT.__auth_stubs: 0xee0
-  __TEXT.__objc_methlist: 0xd52fc
+  __TEXT.__objc_methlist: 0xd58c4
   __TEXT.__const: 0x12790
   __TEXT.__constg_swiftt: 0x6580
   __TEXT.__swift5_typeref: 0x190c

   __TEXT.__swift5_assocty: 0x120
   __TEXT.__swift5_proto: 0xf44
   __TEXT.__swift5_types: 0xc18
-  __TEXT.__cstring: 0x7b9c0
+  __TEXT.__cstring: 0x7bbb3
   __TEXT.__swift5_fieldmd: 0x3e8
   __TEXT.__oslogstring: 0x95
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x2b298
+  __TEXT.__unwind_info: 0x2b350
   __TEXT.__eh_frame: 0x24d8
-  __TEXT.__objc_classname: 0x15dbf
-  __TEXT.__objc_methname: 0x127715
-  __TEXT.__objc_methtype: 0x291e1
-  __TEXT.__objc_stubs: 0x6ad80
+  __TEXT.__objc_classname: 0x15dc0
+  __TEXT.__objc_methname: 0x1281ea
+  __TEXT.__objc_methtype: 0x293fc
+  __TEXT.__objc_stubs: 0x6b180
   __DATA_CONST.__got: 0x4d88
-  __DATA_CONST.__const: 0x35828
+  __DATA_CONST.__const: 0x358c0
   __DATA_CONST.__objc_classlist: 0x4c70
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37510
+  __DATA_CONST.__objc_selrefs: 0x37760
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x7700
   __AUTH_CONST.__auth_got: 0x778
   __AUTH_CONST.__const: 0x1c0e0
-  __AUTH_CONST.__cfstring: 0x6ae80
-  __AUTH_CONST.__objc_const: 0x120930
+  __AUTH_CONST.__cfstring: 0x6b0c0
+  __AUTH_CONST.__objc_const: 0x120f50
   __AUTH_CONST.__objc_intobj: 0xb70
   __AUTH.__objc_data: 0x11508
-  __DATA.__objc_ivar: 0xe638
+  __DATA.__objc_ivar: 0xe6a0
   __DATA.__data: 0x2a48
   __DATA.__bss: 0x19180
   __DATA.__common: 0x38

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 4E64680D-5350-3262-99D4-8CB3A0C71F10
-  Functions: 77720
-  Symbols:   120974
-  CStrings:  78956
+  UUID: 13CE8B9B-2A4F-3457-92C2-D3E3E3A49AA5
+  Functions: 77844
+  Symbols:   121156
+  CStrings:  79098
 
Symbols:
+ -[ODDSiriSchemaODDAssetSetStatusDimensions deleteStatusReason]
+ -[ODDSiriSchemaODDAssetSetStatusDimensions hasStatusReason]
+ -[ODDSiriSchemaODDAssetSetStatusDimensions setHasStatusReason:]
+ -[ODDSiriSchemaODDAssetSetStatusDimensions setStatusReason:]
+ -[ODDSiriSchemaODDAssetSetStatusDimensions statusReason]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus countFactoryAssetInBytes]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus countFactoryAssets]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus countPSUSAssetsMobileAsset]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus deleteCountFactoryAssetInBytes]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus deleteCountFactoryAssets]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus deleteCountPSUSAssetsMobileAsset]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus deleteInvocationsCountWhileAvailable]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus deleteNumberOfMobileAssetAlters]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus deleteNumberOfMobileAssetEliminates]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus deleteNumberOfMobileAssetScans]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus deleteSizeInBytesPSUSAssets]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus deleteTotalBytesDownloaded]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus hasCountFactoryAssetInBytes]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus hasCountFactoryAssets]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus hasCountPSUSAssetsMobileAsset]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus hasInvocationsCountWhileAvailable]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus hasNumberOfMobileAssetAlters]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus hasNumberOfMobileAssetEliminates]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus hasNumberOfMobileAssetScans]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus hasSizeInBytesPSUSAssets]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus hasTotalBytesDownloaded]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus invocationsCountWhileAvailable]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus numberOfMobileAssetAlters]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus numberOfMobileAssetEliminates]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus numberOfMobileAssetScans]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus setCountFactoryAssetInBytes:]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus setCountFactoryAssets:]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus setCountPSUSAssetsMobileAsset:]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus setHasCountFactoryAssetInBytes:]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus setHasCountFactoryAssets:]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus setHasCountPSUSAssetsMobileAsset:]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus setHasInvocationsCountWhileAvailable:]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus setHasNumberOfMobileAssetAlters:]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus setHasNumberOfMobileAssetEliminates:]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus setHasNumberOfMobileAssetScans:]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus setHasSizeInBytesPSUSAssets:]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus setHasTotalBytesDownloaded:]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus setInvocationsCountWhileAvailable:]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus setNumberOfMobileAssetAlters:]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus setNumberOfMobileAssetEliminates:]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus setNumberOfMobileAssetScans:]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus setSizeInBytesPSUSAssets:]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus setTotalBytesDownloaded:]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus sizeInBytesPSUSAssets]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus totalBytesDownloaded]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus countFactoryAssetInBytes]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus countFactoryAssets]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus countPSUSAssetsMobileAsset]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus deleteCountFactoryAssetInBytes]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus deleteCountFactoryAssets]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus deleteCountPSUSAssetsMobileAsset]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus deleteInvocationsCountWhileAvailable]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus deleteNumberOfMobileAssetAlters]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus deleteNumberOfMobileAssetEliminates]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus deleteNumberOfMobileAssetScans]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus deleteSizeInBytesPSUSAssets]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus deleteTotalBytesDownloaded]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus hasCountFactoryAssetInBytes]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus hasCountFactoryAssets]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus hasCountPSUSAssetsMobileAsset]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus hasInvocationsCountWhileAvailable]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus hasNumberOfMobileAssetAlters]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus hasNumberOfMobileAssetEliminates]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus hasNumberOfMobileAssetScans]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus hasSizeInBytesPSUSAssets]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus hasTotalBytesDownloaded]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus invocationsCountWhileAvailable]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus numberOfMobileAssetAlters]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus numberOfMobileAssetEliminates]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus numberOfMobileAssetScans]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus setCountFactoryAssetInBytes:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus setCountFactoryAssets:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus setCountPSUSAssetsMobileAsset:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus setHasCountFactoryAssetInBytes:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus setHasCountFactoryAssets:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus setHasCountPSUSAssetsMobileAsset:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus setHasInvocationsCountWhileAvailable:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus setHasNumberOfMobileAssetAlters:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus setHasNumberOfMobileAssetEliminates:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus setHasNumberOfMobileAssetScans:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus setHasSizeInBytesPSUSAssets:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus setHasTotalBytesDownloaded:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus setInvocationsCountWhileAvailable:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus setNumberOfMobileAssetAlters:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus setNumberOfMobileAssetEliminates:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus setNumberOfMobileAssetScans:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus setSizeInBytesPSUSAssets:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus setTotalBytesDownloaded:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus sizeInBytesPSUSAssets]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus totalBytesDownloaded]
+ -[UAFSchemaUAFAsset deletePromotedOSBuild]
+ -[UAFSchemaUAFAsset deleteSourceOSBuild]
+ -[UAFSchemaUAFAsset hasPromotedOSBuild]
+ -[UAFSchemaUAFAsset hasSourceOSBuild]
+ -[UAFSchemaUAFAsset promotedOSBuild]
+ -[UAFSchemaUAFAsset setHasPromotedOSBuild:]
+ -[UAFSchemaUAFAsset setHasSourceOSBuild:]
+ -[UAFSchemaUAFAsset setPromotedOSBuild:]
+ -[UAFSchemaUAFAsset setSourceOSBuild:]
+ -[UAFSchemaUAFAsset sourceOSBuild]
+ -[UAFSchemaUAFAssetSet deleteIsfromFactory]
+ -[UAFSchemaUAFAssetSet hasIsfromFactory]
+ -[UAFSchemaUAFAssetSet isfromFactory]
+ -[UAFSchemaUAFAssetSet setHasIsfromFactory:]
+ -[UAFSchemaUAFAssetSet setIsfromFactory:]
+ -[UAFSchemaUAFAssetSetSubscription addAlteredAssetSets:]
+ -[UAFSchemaUAFAssetSetSubscription addEliminatedAssetSets:]
+ -[UAFSchemaUAFAssetSetSubscription alteredAssetSetsAtIndex:]
+ -[UAFSchemaUAFAssetSetSubscription alteredAssetSetsCount]
+ -[UAFSchemaUAFAssetSetSubscription alteredAssetSets]
+ -[UAFSchemaUAFAssetSetSubscription clearAlteredAssetSets]
+ -[UAFSchemaUAFAssetSetSubscription clearEliminatedAssetSets]
+ -[UAFSchemaUAFAssetSetSubscription deleteAlteredAssetSets]
+ -[UAFSchemaUAFAssetSetSubscription deleteEliminatedAssetSets]
+ -[UAFSchemaUAFAssetSetSubscription eliminatedAssetSetsAtIndex:]
+ -[UAFSchemaUAFAssetSetSubscription eliminatedAssetSetsCount]
+ -[UAFSchemaUAFAssetSetSubscription eliminatedAssetSets]
+ -[UAFSchemaUAFAssetSetSubscription setAlteredAssetSets:]
+ -[UAFSchemaUAFAssetSetSubscription setEliminatedAssetSets:]
+ OBJC_IVAR_$_ODDSiriSchemaODDAssetSetStatusDimensions._statusReason
+ OBJC_IVAR_$_ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus._countFactoryAssetInBytes
+ OBJC_IVAR_$_ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus._countFactoryAssets
+ OBJC_IVAR_$_ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus._countPSUSAssetsMobileAsset
+ OBJC_IVAR_$_ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus._invocationsCountWhileAvailable
+ OBJC_IVAR_$_ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus._numberOfMobileAssetAlters
+ OBJC_IVAR_$_ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus._numberOfMobileAssetEliminates
+ OBJC_IVAR_$_ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus._numberOfMobileAssetScans
+ OBJC_IVAR_$_ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus._sizeInBytesPSUSAssets
+ OBJC_IVAR_$_ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus._totalBytesDownloaded
+ OBJC_IVAR_$_SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus._countFactoryAssetInBytes
+ OBJC_IVAR_$_SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus._countFactoryAssets
+ OBJC_IVAR_$_SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus._countPSUSAssetsMobileAsset
+ OBJC_IVAR_$_SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus._invocationsCountWhileAvailable
+ OBJC_IVAR_$_SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus._numberOfMobileAssetAlters
+ OBJC_IVAR_$_SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus._numberOfMobileAssetEliminates
+ OBJC_IVAR_$_SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus._numberOfMobileAssetScans
+ OBJC_IVAR_$_SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus._sizeInBytesPSUSAssets
+ OBJC_IVAR_$_SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus._totalBytesDownloaded
+ OBJC_IVAR_$_UAFSchemaUAFAsset._hasPromotedOSBuild
+ OBJC_IVAR_$_UAFSchemaUAFAsset._hasSourceOSBuild
+ OBJC_IVAR_$_UAFSchemaUAFAsset._promotedOSBuild
+ OBJC_IVAR_$_UAFSchemaUAFAsset._sourceOSBuild
+ OBJC_IVAR_$_UAFSchemaUAFAssetSet._isfromFactory
+ OBJC_IVAR_$_UAFSchemaUAFAssetSetSubscription._alteredAssetSets
+ OBJC_IVAR_$_UAFSchemaUAFAssetSetSubscription._eliminatedAssetSets
+ _objc_msgSend$addAlteredAssetSets:
+ _objc_msgSend$addEliminatedAssetSets:
+ _objc_msgSend$alteredAssetSets
+ _objc_msgSend$clearAlteredAssetSets
+ _objc_msgSend$clearEliminatedAssetSets
+ _objc_msgSend$countFactoryAssetInBytes
+ _objc_msgSend$countFactoryAssets
+ _objc_msgSend$countPSUSAssetsMobileAsset
+ _objc_msgSend$eliminatedAssetSets
+ _objc_msgSend$invocationsCountWhileAvailable
+ _objc_msgSend$isfromFactory
+ _objc_msgSend$numberOfMobileAssetAlters
+ _objc_msgSend$numberOfMobileAssetEliminates
+ _objc_msgSend$numberOfMobileAssetScans
+ _objc_msgSend$promotedOSBuild
+ _objc_msgSend$setAlteredAssetSets:
+ _objc_msgSend$setCountFactoryAssetInBytes:
+ _objc_msgSend$setCountFactoryAssets:
+ _objc_msgSend$setCountPSUSAssetsMobileAsset:
+ _objc_msgSend$setEliminatedAssetSets:
+ _objc_msgSend$setInvocationsCountWhileAvailable:
+ _objc_msgSend$setIsfromFactory:
+ _objc_msgSend$setNumberOfMobileAssetAlters:
+ _objc_msgSend$setNumberOfMobileAssetEliminates:
+ _objc_msgSend$setNumberOfMobileAssetScans:
+ _objc_msgSend$setPromotedOSBuild:
+ _objc_msgSend$setSizeInBytesPSUSAssets:
+ _objc_msgSend$setSourceOSBuild:
+ _objc_msgSend$setTotalBytesDownloaded:
+ _objc_msgSend$sizeInBytesPSUSAssets
+ _objc_msgSend$sourceOSBuild
+ _objc_msgSend$totalBytesDownloaded
CStrings:
+ "SADAVAILABLEASSETSTATUSREASON_ASSETSET_ALTERED"
+ "SADAVAILABLEASSETSTATUSREASON_ASSETSET_DOWNLOAD_REQUESTED"
+ "SADAVAILABLEASSETSTATUSREASON_ASSETSET_ELIMINATED"
+ "T@\"NSArray\",C,N,V_alteredAssetSets"
+ "T@\"NSArray\",C,N,V_eliminatedAssetSets"
+ "T@\"NSString\",C,N,V_promotedOSBuild"
+ "T@\"NSString\",C,N,V_sourceOSBuild"
+ "TB,N,V_hasPromotedOSBuild"
+ "TB,N,V_hasSourceOSBuild"
+ "TB,N,V_isfromFactory"
+ "TI,N,V_countFactoryAssetInBytes"
+ "TI,N,V_countFactoryAssets"
+ "TI,N,V_countPSUSAssetsMobileAsset"
+ "TI,N,V_invocationsCountWhileAvailable"
+ "TI,N,V_numberOfMobileAssetAlters"
+ "TI,N,V_numberOfMobileAssetEliminates"
+ "TI,N,V_numberOfMobileAssetScans"
+ "TI,N,V_sizeInBytesPSUSAssets"
+ "TI,N,V_totalBytesDownloaded"
+ "UAFASSETSOURCE_PRESOFTWARE_UPDATE_STAGING"
+ "_alteredAssetSets"
+ "_countFactoryAssetInBytes"
+ "_countFactoryAssets"
+ "_countPSUSAssetsMobileAsset"
+ "_eliminatedAssetSets"
+ "_hasPromotedOSBuild"
+ "_hasSourceOSBuild"
+ "_invocationsCountWhileAvailable"
+ "_isfromFactory"
+ "_numberOfMobileAssetAlters"
+ "_numberOfMobileAssetEliminates"
+ "_numberOfMobileAssetScans"
+ "_promotedOSBuild"
+ "_sizeInBytesPSUSAssets"
+ "_sourceOSBuild"
+ "_totalBytesDownloaded"
+ "addAlteredAssetSets:"
+ "addEliminatedAssetSets:"
+ "alteredAssetSets"
+ "alteredAssetSetsAtIndex:"
+ "alteredAssetSetsCount"
+ "clearAlteredAssetSets"
+ "clearEliminatedAssetSets"
+ "countFactoryAssetInBytes"
+ "countFactoryAssets"
+ "countPSUSAssetsMobileAsset"
+ "deleteAlteredAssetSets"
+ "deleteCountFactoryAssetInBytes"
+ "deleteCountFactoryAssets"
+ "deleteCountPSUSAssetsMobileAsset"
+ "deleteEliminatedAssetSets"
+ "deleteInvocationsCountWhileAvailable"
+ "deleteIsfromFactory"
+ "deleteNumberOfMobileAssetAlters"
+ "deleteNumberOfMobileAssetEliminates"
+ "deleteNumberOfMobileAssetScans"
+ "deletePromotedOSBuild"
+ "deleteSizeInBytesPSUSAssets"
+ "deleteSourceOSBuild"
+ "deleteTotalBytesDownloaded"
+ "eliminatedAssetSets"
+ "eliminatedAssetSetsAtIndex:"
+ "eliminatedAssetSetsCount"
+ "hasCountFactoryAssetInBytes"
+ "hasCountFactoryAssets"
+ "hasCountPSUSAssetsMobileAsset"
+ "hasInvocationsCountWhileAvailable"
+ "hasIsfromFactory"
+ "hasNumberOfMobileAssetAlters"
+ "hasNumberOfMobileAssetEliminates"
+ "hasNumberOfMobileAssetScans"
+ "hasPromotedOSBuild"
+ "hasSizeInBytesPSUSAssets"
+ "hasSourceOSBuild"
+ "hasTotalBytesDownloaded"
+ "invocationsCountWhileAvailable"
+ "isfromFactory"
+ "numberOfMobileAssetAlters"
+ "numberOfMobileAssetEliminates"
+ "numberOfMobileAssetScans"
+ "promotedOSBuild"
+ "setAlteredAssetSets:"
+ "setCountFactoryAssetInBytes:"
+ "setCountFactoryAssets:"
+ "setCountPSUSAssetsMobileAsset:"
+ "setEliminatedAssetSets:"
+ "setHasCountFactoryAssetInBytes:"
+ "setHasCountFactoryAssets:"
+ "setHasCountPSUSAssetsMobileAsset:"
+ "setHasInvocationsCountWhileAvailable:"
+ "setHasIsfromFactory:"
+ "setHasNumberOfMobileAssetAlters:"
+ "setHasNumberOfMobileAssetEliminates:"
+ "setHasNumberOfMobileAssetScans:"
+ "setHasPromotedOSBuild:"
+ "setHasSizeInBytesPSUSAssets:"
+ "setHasSourceOSBuild:"
+ "setHasTotalBytesDownloaded:"
+ "setInvocationsCountWhileAvailable:"
+ "setIsfromFactory:"
+ "setNumberOfMobileAssetAlters:"
+ "setNumberOfMobileAssetEliminates:"
+ "setNumberOfMobileAssetScans:"
+ "setPromotedOSBuild:"
+ "setSizeInBytesPSUSAssets:"
+ "setSourceOSBuild:"
+ "setTotalBytesDownloaded:"
+ "sizeInBytesPSUSAssets"
+ "sourceOSBuild"
+ "totalBytesDownloaded"
+ "{?=\"buildInstallationTimestampInSecondsSince1970\"b1\"assetSetStatusEventTimestampInSecondsSince1970\"b1\"statusReason\"b1}"
+ "{?=\"currentStatus\"b1\"previousStatus\"b1\"timeSinceLastStatusChangeInSeconds\"b1\"timeSinceLastAvailabilityChangeInSeconds\"b1\"hasModelCatalogSubscriptionHashChangedFromLastStatus\"b1\"isAppleIntelligenceEligible\"b1\"isAppleIntelligenceAllowedThroughWaitlist\"b1\"isAppleIntelligenceToggled\"b1\"timeSinceLastEligibleChangeInSeconds\"b1\"timeSinceLastWaitlistChangeInSeconds\"b1\"timeSinceLastAppleIntelligenceToggleInSeconds\"b1\"timeSinceLastBootInSeconds\"b1\"timeSinceLastMobileAssetDownloadAttemptInSeconds\"b1\"timeSinceLastMobileAssetDownloadErrorInSeconds\"b1\"downloadState\"b1\"timeSinceLastModelCatalogSubscriptionHashChangeInSeconds\"b1\"useCase\"b1\"timeSinceLastSoftwareUpdateInSeconds\"b1\"timeSinceSampledErrorInSeconds\"b1\"buddyStatus\"b1\"invocationsCountWhileNotAvailable\"b1\"lastMobileAssetDownloadAttemptErrorUnderlyingCode\"b1\"mode\"b1\"subscriptionDownloadStatus\"b1\"timeSinceSubscriptionDownloadStatusCompleteInSeconds\"b1\"currentMode\"b1\"invocationsCountWhileAvailable\"b1\"numberOfMobileAssetAlters\"b1\"numberOfMobileAssetEliminates\"b1\"numberOfMobileAssetScans\"b1\"countFactoryAssetInBytes\"b1\"countFactoryAssets\"b1\"sizeInBytesPSUSAssets\"b1\"countPSUSAssetsMobileAsset\"b1\"totalBytesDownloaded\"b1}"
+ "{?=\"fromPreSoftwareUpdateStaging\"b1\"expensiveCellularDownloadRequested\"b1\"isfromFactory\"b1}"
+ "{?=\"locale\"b1\"status\"b1\"currentSubscriptionHash\"b1\"downloadState\"b1\"timeSinceLastMobileAssetDownloadAttemptInSeconds\"b1\"timeSinceLastMobileAssetDownloadErrorInSeconds\"b1\"lastMobileAssetDownloadAttemptErrorCode\"b1\"errorCount\"b1\"sampledErrorCode\"b1\"sampledErrorHash\"b1\"sampledErrorUnderlyingCode\"b1\"timeSinceLastAppleIntelligenceToggleInSeconds\"b1\"timeSinceLastSubscriptionHashChangeInSeconds\"b1\"timeSinceLastBootInSeconds\"b1\"countPSUSAssets\"b1\"countRequiredAssets\"b1\"timeSinceLastSoftwareUpdateInSeconds\"b1\"timeSinceSampledErrorInSeconds\"b1\"buddyStatus\"b1\"invocationsCountWhileNotAvailable\"b1\"lastMobileAssetDownloadAttemptErrorUnderlyingCode\"b1\"mode\"b1\"subscriptionDownloadStatus\"b1\"timeSinceSubscriptionDownloadStatusCompleteInSeconds\"b1\"currentMode\"b1\"invocationsCountWhileAvailable\"b1\"numberOfMobileAssetAlters\"b1\"numberOfMobileAssetEliminates\"b1\"numberOfMobileAssetScans\"b1\"countFactoryAssetInBytes\"b1\"countFactoryAssets\"b1\"sizeInBytesPSUSAssets\"b1\"countPSUSAssetsMobileAsset\"b1\"totalBytesDownloaded\"b1}"
- "{?=\"buildInstallationTimestampInSecondsSince1970\"b1\"assetSetStatusEventTimestampInSecondsSince1970\"b1}"
- "{?=\"currentStatus\"b1\"previousStatus\"b1\"timeSinceLastStatusChangeInSeconds\"b1\"timeSinceLastAvailabilityChangeInSeconds\"b1\"hasModelCatalogSubscriptionHashChangedFromLastStatus\"b1\"isAppleIntelligenceEligible\"b1\"isAppleIntelligenceAllowedThroughWaitlist\"b1\"isAppleIntelligenceToggled\"b1\"timeSinceLastEligibleChangeInSeconds\"b1\"timeSinceLastWaitlistChangeInSeconds\"b1\"timeSinceLastAppleIntelligenceToggleInSeconds\"b1\"timeSinceLastBootInSeconds\"b1\"timeSinceLastMobileAssetDownloadAttemptInSeconds\"b1\"timeSinceLastMobileAssetDownloadErrorInSeconds\"b1\"downloadState\"b1\"timeSinceLastModelCatalogSubscriptionHashChangeInSeconds\"b1\"useCase\"b1\"timeSinceLastSoftwareUpdateInSeconds\"b1\"timeSinceSampledErrorInSeconds\"b1\"buddyStatus\"b1\"invocationsCountWhileNotAvailable\"b1\"lastMobileAssetDownloadAttemptErrorUnderlyingCode\"b1\"mode\"b1\"subscriptionDownloadStatus\"b1\"timeSinceSubscriptionDownloadStatusCompleteInSeconds\"b1\"currentMode\"b1}"
- "{?=\"fromPreSoftwareUpdateStaging\"b1\"expensiveCellularDownloadRequested\"b1}"
- "{?=\"locale\"b1\"status\"b1\"currentSubscriptionHash\"b1\"downloadState\"b1\"timeSinceLastMobileAssetDownloadAttemptInSeconds\"b1\"timeSinceLastMobileAssetDownloadErrorInSeconds\"b1\"lastMobileAssetDownloadAttemptErrorCode\"b1\"errorCount\"b1\"sampledErrorCode\"b1\"sampledErrorHash\"b1\"sampledErrorUnderlyingCode\"b1\"timeSinceLastAppleIntelligenceToggleInSeconds\"b1\"timeSinceLastSubscriptionHashChangeInSeconds\"b1\"timeSinceLastBootInSeconds\"b1\"countPSUSAssets\"b1\"countRequiredAssets\"b1\"timeSinceLastSoftwareUpdateInSeconds\"b1\"timeSinceSampledErrorInSeconds\"b1\"buddyStatus\"b1\"invocationsCountWhileNotAvailable\"b1\"lastMobileAssetDownloadAttemptErrorUnderlyingCode\"b1\"mode\"b1\"subscriptionDownloadStatus\"b1\"timeSinceSubscriptionDownloadStatusCompleteInSeconds\"b1\"currentMode\"b1}"

```
