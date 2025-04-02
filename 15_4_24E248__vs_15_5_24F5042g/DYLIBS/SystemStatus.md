## SystemStatus

> `/System/Library/PrivateFrameworks/SystemStatus.framework/Versions/A/SystemStatus`

```diff

-210.4.13.0.0
-  __TEXT.__text: 0x3da24
-  __TEXT.__auth_stubs: 0x490
-  __TEXT.__objc_methlist: 0x4cd0
-  __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x2b08
-  __TEXT.__gcc_except_tab: 0x3ec
-  __TEXT.__oslogstring: 0x128e
-  __TEXT.__unwind_info: 0x15d8
-  __TEXT.__objc_classname: 0x10ee
-  __TEXT.__objc_methname: 0x675e
-  __TEXT.__objc_methtype: 0x1215
-  __TEXT.__objc_stubs: 0x3f80
-  __DATA_CONST.__got: 0x3b0
-  __DATA_CONST.__const: 0x648
-  __DATA_CONST.__objc_classlist: 0x358
+210.5.2.0.0
+  __TEXT.__text: 0x40e58
+  __TEXT.__auth_stubs: 0x4c0
+  __TEXT.__objc_methlist: 0x5190
+  __TEXT.__const: 0x108
+  __TEXT.__cstring: 0x2cd2
+  __TEXT.__gcc_except_tab: 0x418
+  __TEXT.__oslogstring: 0x140b
+  __TEXT.__unwind_info: 0x1708
+  __TEXT.__objc_classname: 0x11a5
+  __TEXT.__objc_methname: 0x6f51
+  __TEXT.__objc_methtype: 0x130f
+  __TEXT.__objc_stubs: 0x41e0
+  __DATA_CONST.__got: 0x3d0
+  __DATA_CONST.__const: 0x710
+  __DATA_CONST.__objc_classlist: 0x388
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1400
+  __DATA_CONST.__objc_selrefs: 0x1530
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x238
+  __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x258
-  __AUTH_CONST.__const: 0x1580
-  __AUTH_CONST.__cfstring: 0x2920
-  __AUTH_CONST.__objc_const: 0x9128
+  __AUTH_CONST.__auth_got: 0x270
+  __AUTH_CONST.__const: 0x1720
+  __AUTH_CONST.__cfstring: 0x2b80
+  __AUTH_CONST.__objc_const: 0x9970
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x2170
-  __DATA.__objc_ivar: 0x314
+  __AUTH.__objc_data: 0x2350
+  __DATA.__objc_ivar: 0x33c
   __DATA.__data: 0xcc8
   __DATA.__bss: 0x100
-  __DATA.__common: 0x40
+  __DATA.__common: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/BaseBoard.framework/Versions/A/BaseBoard
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1890
-  Symbols:   4048
-  CStrings:  1750
+  Functions: 2015
+  Symbols:   4273
+  CStrings:  1857
 
Symbols:
+ +[STDataAccessAttribution supportsSecureCoding]
+ +[STDataAccessStatusDomain statusDomainName]
+ +[STDataAccessStatusDomainData supportsSecureCoding]
+ +[STDataAccessStatusDomainDataDiff diffFromData:toData:]
+ +[STDataAccessStatusDomainDataDiff supportsSecureCoding]
+ +[STDataAccessStatusDomainPublisher emptyData]
+ +[STDataAccessStatusDomainPublisher statusDomainName]
+ -[STDataAccessAttribution .cxx_destruct]
+ -[STDataAccessAttribution accessDuration]
+ -[STDataAccessAttribution accessEndTimestamp]
+ -[STDataAccessAttribution accessStartTimestamp]
+ -[STDataAccessAttribution activityAttribution]
+ -[STDataAccessAttribution attributedEntity]
+ -[STDataAccessAttribution audioRecordingActivityAttribution]
+ -[STDataAccessAttribution cameraCaptureAttribution]
+ -[STDataAccessAttribution copyWithZone:]
+ -[STDataAccessAttribution dataAccessType]
+ -[STDataAccessAttribution descriptionBuilderWithMultilinePrefix:]
+ -[STDataAccessAttribution descriptionWithMultilinePrefix:]
+ -[STDataAccessAttribution description]
+ -[STDataAccessAttribution encodeWithCoder:]
+ -[STDataAccessAttribution hasSatisfiedMinimumOnTime]
+ -[STDataAccessAttribution hash]
+ -[STDataAccessAttribution initWithAudioRecordingActivityAttribution:recent:startTimestamp:endTimestamp:]
+ -[STDataAccessAttribution initWithCameraCaptureAttribution:recent:startTimestamp:endTimestamp:]
+ -[STDataAccessAttribution initWithCoder:]
+ -[STDataAccessAttribution initWithDataAccessAttribution:]
+ -[STDataAccessAttribution initWithDataAccessType:microphoneRecordingAttribution:cameraCaptureAttribution:locationAttribution:recent:startTimestamp:endTimestamp:]
+ -[STDataAccessAttribution initWithLocationAttribution:recent:startTimestamp:endTimestamp:]
+ -[STDataAccessAttribution initWithMicrophoneRecordingAttribution:recent:startTimestamp:endTimestamp:]
+ -[STDataAccessAttribution isEqual:]
+ -[STDataAccessAttribution isRecent]
+ -[STDataAccessAttribution locationAttribution]
+ -[STDataAccessAttribution microphoneRecordingAttribution]
+ -[STDataAccessAttribution succinctDescriptionBuilder]
+ -[STDataAccessAttribution succinctDescription]
+ -[STDataAccessStatusDomainData .cxx_destruct]
+ -[STDataAccessStatusDomainData _allEntities]
+ -[STDataAccessStatusDomainData _dataWithAttributionFilter:]
+ -[STDataAccessStatusDomainData _initWithAttributionListData:]
+ -[STDataAccessStatusDomainData activeAttributionData]
+ -[STDataAccessStatusDomainData attributedEntities]
+ -[STDataAccessStatusDomainData attributionListData]
+ -[STDataAccessStatusDomainData copyWithZone:]
+ -[STDataAccessStatusDomainData dataAccessAttributions]
+ -[STDataAccessStatusDomainData dataByApplyingDiff:]
+ -[STDataAccessStatusDomainData dataWithAccessType:]
+ -[STDataAccessStatusDomainData dataWithAttributedEntity:]
+ -[STDataAccessStatusDomainData dataWithEntitiesThatAreSystemServices:]
+ -[STDataAccessStatusDomainData dataWithExecutableIdentity:]
+ -[STDataAccessStatusDomainData dataWithUserIdentity:]
+ -[STDataAccessStatusDomainData descriptionBuilderWithMultilinePrefix:]
+ -[STDataAccessStatusDomainData descriptionWithMultilinePrefix:]
+ -[STDataAccessStatusDomainData description]
+ -[STDataAccessStatusDomainData diffFromData:]
+ -[STDataAccessStatusDomainData encodeWithCoder:]
+ -[STDataAccessStatusDomainData executableIdentities]
+ -[STDataAccessStatusDomainData hash]
+ -[STDataAccessStatusDomainData initWithAttributionListData:]
+ -[STDataAccessStatusDomainData initWithCoder:]
+ -[STDataAccessStatusDomainData initWithData:]
+ -[STDataAccessStatusDomainData init]
+ -[STDataAccessStatusDomainData isEqual:]
+ -[STDataAccessStatusDomainData mutableCopyWithZone:]
+ -[STDataAccessStatusDomainData recentAttributionData]
+ -[STDataAccessStatusDomainData succinctDescriptionBuilder]
+ -[STDataAccessStatusDomainData succinctDescription]
+ -[STDataAccessStatusDomainData unsatisfiedMinimumOnTimeAttributionData]
+ -[STDataAccessStatusDomainData userIdentities]
+ -[STDataAccessStatusDomainDataDiff .cxx_destruct]
+ -[STDataAccessStatusDomainDataDiff _descriptionBuilderWithMultilinePrefix:forDebug:]
+ -[STDataAccessStatusDomainDataDiff applyToMutableData:]
+ -[STDataAccessStatusDomainDataDiff dataByApplyingToData:]
+ -[STDataAccessStatusDomainDataDiff debugDescriptionWithMultilinePrefix:]
+ -[STDataAccessStatusDomainDataDiff descriptionBuilderWithMultilinePrefix:]
+ -[STDataAccessStatusDomainDataDiff descriptionWithMultilinePrefix:]
+ -[STDataAccessStatusDomainDataDiff description]
+ -[STDataAccessStatusDomainDataDiff diffByApplyingDiff:]
+ -[STDataAccessStatusDomainDataDiff encodeWithCoder:]
+ -[STDataAccessStatusDomainDataDiff hash]
+ -[STDataAccessStatusDomainDataDiff initWithAttributionListDataDiff:]
+ -[STDataAccessStatusDomainDataDiff initWithCoder:]
+ -[STDataAccessStatusDomainDataDiff init]
+ -[STDataAccessStatusDomainDataDiff isEmpty]
+ -[STDataAccessStatusDomainDataDiff isEqual:]
+ -[STDataAccessStatusDomainDataDiff isOrthogonalToDiff:]
+ -[STDataAccessStatusDomainDataDiff succinctDescriptionBuilder]
+ -[STDataAccessStatusDomainDataDiff succinctDescription]
+ -[STMutableDataAccessStatusDomainData applyDiff:]
+ -[STMutableDataAccessStatusDomainData attributionListData]
+ -[STMutableDataAccessStatusDomainData copyWithZone:]
+ -[STMutableDataAccessStatusDomainData initWithAttributionListData:]
+ -[STMutableDataAccessStatusDomainData setDataAccessAttributions:]
+ -[STStatusDomain initWithServerHandle:wantsUntransformedData:]
+ -[STStatusDomain wantsUntransformedData]
+ -[STStatusDomainXPCServerHandle dataForDomain:client:]
+ -[STStatusDomainXPCServerHandle serverDataForDomains:preferredLocalizations:]
+ -[STToolSupportServerDataFetcher serverDataForDomains:preferredLocalizations:]
+ GCC_except_table41
+ OBJC_IVAR_$_STDataAccessAttribution._accessEndTimestamp
+ OBJC_IVAR_$_STDataAccessAttribution._accessStartTimestamp
+ OBJC_IVAR_$_STDataAccessAttribution._cameraCaptureAttribution
+ OBJC_IVAR_$_STDataAccessAttribution._dataAccessType
+ OBJC_IVAR_$_STDataAccessAttribution._locationAttribution
+ OBJC_IVAR_$_STDataAccessAttribution._microphoneRecordingAttribution
+ OBJC_IVAR_$_STDataAccessAttribution._recent
+ OBJC_IVAR_$_STDataAccessStatusDomainData._attributionListData
+ OBJC_IVAR_$_STDataAccessStatusDomainDataDiff._attributionListDataDiff
+ OBJC_IVAR_$_STStatusDomain._wantsUntransformedData
+ STSystemStatusLogDataIntegrity.__logObj
+ STSystemStatusLogDataIntegrity.onceToken
+ _BSContinuousMachTimeNow
+ _BSFloatGreaterThanOrEqualToFloat
+ _BSFloatLessThanFloat
+ _OBJC_CLASS_$_STDataAccessAttribution
+ _OBJC_CLASS_$_STDataAccessStatusDomain
+ _OBJC_CLASS_$_STDataAccessStatusDomainData
+ _OBJC_CLASS_$_STDataAccessStatusDomainDataDiff
+ _OBJC_CLASS_$_STDataAccessStatusDomainPublisher
+ _OBJC_CLASS_$_STMutableDataAccessStatusDomainData
+ _OBJC_METACLASS_$_STDataAccessAttribution
+ _OBJC_METACLASS_$_STDataAccessStatusDomain
+ _OBJC_METACLASS_$_STDataAccessStatusDomainData
+ _OBJC_METACLASS_$_STDataAccessStatusDomainDataDiff
+ _OBJC_METACLASS_$_STDataAccessStatusDomainPublisher
+ _OBJC_METACLASS_$_STMutableDataAccessStatusDomainData
+ _STDataAccessStatusDomainMinumumOnTime
+ _STDataAccessTypeIsValid
+ _STDescriptionForDataAccessType
+ _STStatusDomainEntitlementValueDataAccess
+ _STSystemStatusLogDataIntegrity
+ _STTimestampIsValid
+ _STTimestampNow
+ __35-[STDataAccessAttribution isEqual:]_block_invoke.23
+ __35-[STDataAccessAttribution isEqual:]_block_invoke.27
+ __35-[STDataAccessAttribution isEqual:]_block_invoke.31
+ __77-[STStatusDomainXPCServerHandle serverDataForDomains:preferredLocalizations:]_block_invoke.22
+ __77-[STStatusDomainXPCServerHandle serverDataForDomains:preferredLocalizations:]_block_invoke.31
+ __77-[STStatusDomainXPCServerHandle serverDataForDomains:preferredLocalizations:]_block_invoke_2.24
+ __OBJC_$_CLASS_METHODS_STDataAccessAttribution
+ __OBJC_$_CLASS_METHODS_STDataAccessStatusDomain
+ __OBJC_$_CLASS_METHODS_STDataAccessStatusDomainData
+ __OBJC_$_CLASS_METHODS_STDataAccessStatusDomainDataDiff
+ __OBJC_$_CLASS_METHODS_STDataAccessStatusDomainPublisher
+ __OBJC_$_CLASS_PROP_LIST_STDataAccessAttribution
+ __OBJC_$_CLASS_PROP_LIST_STDataAccessStatusDomainData
+ __OBJC_$_CLASS_PROP_LIST_STDataAccessStatusDomainDataDiff
+ __OBJC_$_INSTANCE_METHODS_STDataAccessAttribution
+ __OBJC_$_INSTANCE_METHODS_STDataAccessStatusDomainData
+ __OBJC_$_INSTANCE_METHODS_STDataAccessStatusDomainDataDiff
+ __OBJC_$_INSTANCE_METHODS_STMutableDataAccessStatusDomainData
+ __OBJC_$_INSTANCE_VARIABLES_STDataAccessAttribution
+ __OBJC_$_INSTANCE_VARIABLES_STDataAccessStatusDomainData
+ __OBJC_$_INSTANCE_VARIABLES_STDataAccessStatusDomainDataDiff
+ __OBJC_$_PROP_LIST_STDataAccessAttribution
+ __OBJC_$_PROP_LIST_STDataAccessStatusDomainData
+ __OBJC_$_PROP_LIST_STDataAccessStatusDomainDataDiff
+ __OBJC_$_PROP_LIST_STMutableDataAccessStatusDomainData
+ __OBJC_CLASS_PROTOCOLS_$_STDataAccessAttribution
+ __OBJC_CLASS_PROTOCOLS_$_STDataAccessStatusDomainData
+ __OBJC_CLASS_PROTOCOLS_$_STDataAccessStatusDomainDataDiff
+ __OBJC_CLASS_PROTOCOLS_$_STMutableDataAccessStatusDomainData
+ __OBJC_CLASS_RO_$_STDataAccessAttribution
+ __OBJC_CLASS_RO_$_STDataAccessStatusDomain
+ __OBJC_CLASS_RO_$_STDataAccessStatusDomainData
+ __OBJC_CLASS_RO_$_STDataAccessStatusDomainDataDiff
+ __OBJC_CLASS_RO_$_STDataAccessStatusDomainPublisher
+ __OBJC_CLASS_RO_$_STMutableDataAccessStatusDomainData
+ __OBJC_METACLASS_RO_$_STDataAccessAttribution
+ __OBJC_METACLASS_RO_$_STDataAccessStatusDomain
+ __OBJC_METACLASS_RO_$_STDataAccessStatusDomainData
+ __OBJC_METACLASS_RO_$_STDataAccessStatusDomainDataDiff
+ __OBJC_METACLASS_RO_$_STDataAccessStatusDomainPublisher
+ __OBJC_METACLASS_RO_$_STMutableDataAccessStatusDomainData
+ ___35-[STDataAccessAttribution isEqual:]_block_invoke
+ ___35-[STDataAccessAttribution isEqual:]_block_invoke_2
+ ___35-[STDataAccessAttribution isEqual:]_block_invoke_3
+ ___40-[STDataAccessStatusDomainData isEqual:]_block_invoke
+ ___44-[STDataAccessStatusDomainData _allEntities]_block_invoke
+ ___44-[STDataAccessStatusDomainDataDiff isEqual:]_block_invoke
+ ___46-[STDataAccessStatusDomainData initWithCoder:]_block_invoke_2
+ ___50-[STDataAccessStatusDomainData _allUserIdentities]_block_invoke
+ ___51-[STDataAccessStatusDomainData dataWithAccessType:]_block_invoke
+ ___52-[STDataAccessStatusDomainData _sortedAttributions:]_block_invoke
+ ___52-[STDataAccessStatusDomainData executableIdentities]_block_invoke
+ ___53-[STDataAccessStatusDomainData activeAttributionData]_block_invoke
+ ___53-[STDataAccessStatusDomainData dataWithUserIdentity:]_block_invoke
+ ___53-[STDataAccessStatusDomainData recentAttributionData]_block_invoke
+ ___54-[STStatusDomainXPCServerHandle dataForDomain:client:]_block_invoke
+ ___57-[STDataAccessStatusDomainData dataWithAttributedEntity:]_block_invoke
+ ___59-[STDataAccessStatusDomainData dataWithExecutableIdentity:]_block_invoke
+ ___65-[STDataAccessAttribution descriptionBuilderWithMultilinePrefix:]_block_invoke
+ ___70-[STDataAccessStatusDomainData dataWithEntitiesThatAreSystemServices:]_block_invoke
+ ___71-[STDataAccessStatusDomainData unsatisfiedMinimumOnTimeAttributionData]_block_invoke
+ ___77-[STStatusDomainXPCServerHandle serverDataForDomains:preferredLocalizations:]_block_invoke
+ ___77-[STStatusDomainXPCServerHandle serverDataForDomains:preferredLocalizations:]_block_invoke_2
+ ___84-[STDataAccessStatusDomainDataDiff _descriptionBuilderWithMultilinePrefix:forDebug:]_block_invoke
+ ___STSystemStatusLogDataIntegrity_block_invoke
+ ___block_descriptor_32_e28_16?0"STAttributedEntity"8l
+ ___block_descriptor_32_e33_16?0"STDataAccessAttribution"8l
+ ___block_descriptor_32_e33_B16?0"STDataAccessAttribution"8l
+ ___block_descriptor_32_e61_q24?0"STDataAccessAttribution"8"STDataAccessAttribution"16l
+ ___block_descriptor_33_e33_B16?0"STDataAccessAttribution"8l
+ ___block_descriptor_40_e33_B16?0"STDataAccessAttribution"8l
+ ___block_descriptor_40_e8_32r_e24_v24?0"<NSObject>"8^B16l
+ ___block_descriptor_40_e8_32s_e33_B16?0"STDataAccessAttribution"8l
+ ___block_descriptor_40_e8_32s_e36_"NSDictionary"16?0"NSDictionary"8l
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56r
+ __block_literal_global.44
+ __block_literal_global.6
+ __block_literal_global.8
+ _objc_msgSend$_initWithAttributionListData:
+ _objc_msgSend$accessEndTimestamp
+ _objc_msgSend$accessStartTimestamp
+ _objc_msgSend$attributionListData
+ _objc_msgSend$cameraCaptureAttribution
+ _objc_msgSend$dataAccessAttributions
+ _objc_msgSend$dataAccessType
+ _objc_msgSend$dataForDomain:client:
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$hasSatisfiedMinimumOnTime
+ _objc_msgSend$initWithAttributionListData:
+ _objc_msgSend$initWithAttributionListDataDiff:
+ _objc_msgSend$initWithDataAccessType:microphoneRecordingAttribution:cameraCaptureAttribution:locationAttribution:recent:startTimestamp:endTimestamp:
+ _objc_msgSend$initWithServerHandle:wantsUntransformedData:
+ _objc_msgSend$isRecent
+ _objc_msgSend$locationAttribution
+ _objc_msgSend$matchesAttributedEntity:
+ _objc_msgSend$microphoneRecordingAttribution
+ _objc_msgSend$serverDataForDomains:preferredLocalizations:
+ _objc_msgSend$serverDataForDomains:preferredLocalizations:reply:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$stringByAppendingString:
- -[STStatusDomainXPCServerHandle dataForDomain:]
- -[STStatusDomainXPCServerHandle serverDataForDomains:]
- -[STToolSupportServerDataFetcher serverDataForDomains:]
- __54-[STStatusDomainXPCServerHandle serverDataForDomains:]_block_invoke.22
- __54-[STStatusDomainXPCServerHandle serverDataForDomains:]_block_invoke.31
- __54-[STStatusDomainXPCServerHandle serverDataForDomains:]_block_invoke_2.27
- ___47-[STStatusDomainXPCServerHandle dataForDomain:]_block_invoke
- ___54-[STStatusDomainXPCServerHandle serverDataForDomains:]_block_invoke
- ___54-[STStatusDomainXPCServerHandle serverDataForDomains:]_block_invoke_2
- ___block_descriptor_32_e36_"NSDictionary"16?0"NSDictionary"8l
- __block_literal_global.38
- _objc_msgSend$dataForDomain:
- _objc_msgSend$serverDataForDomains:
- _objc_msgSend$serverDataForDomains:reply:
CStrings:
+ " (in minimum on time)"
+ "@\"<STStatusDomainData>\"32@0:8Q16@\"<STStatusDomainClientHandle>\"24"
+ "@\"STLocationStatusDomainLocationAttribution\""
+ "@\"STMediaStatusDomainCameraCaptureAttribution\""
+ "@\"STMediaStatusDomainMicrophoneRecordingAttribution\""
+ "@16@?0@\"STAttributedEntity\"8"
+ "@16@?0@\"STDataAccessAttribution\"8"
+ "@20@0:8B16"
+ "@44@0:8@16B24d28d36"
+ "@68@0:8Q16@24@32@40B48d52d60"
+ "B16@?0@\"STDataAccessAttribution\"8"
+ "DataIntegrity"
+ "STDataAccessAttribution"
+ "STDataAccessStatusDomain"
+ "STDataAccessStatusDomainData"
+ "STDataAccessStatusDomainDataDiff"
+ "STDataAccessStatusDomainPublisher"
+ "STMutableDataAccessStatusDomainData"
+ "T@\"STActivityAttribution\",R,C,N"
+ "T@\"STAttributedEntity\",R,C,N"
+ "T@\"STDataAccessStatusDomainData\",R,C,N"
+ "T@\"STListData\",R,C,N,V_attributionListData"
+ "T@\"STLocationStatusDomainLocationAttribution\",R,C,N,V_locationAttribution"
+ "T@\"STMediaStatusDomainCameraCaptureAttribution\",R,C,N,V_cameraCaptureAttribution"
+ "T@\"STMediaStatusDomainMicrophoneRecordingAttribution\",R,C,N,V_microphoneRecordingAttribution"
+ "TB,R,N,GisRecent,V_recent"
+ "TQ,R,N,V_dataAccessType"
+ "Td,R,N"
+ "Td,R,N,V_accessEndTimestamp"
+ "Td,R,N,V_accessStartTimestamp"
+ "_accessEndTimestamp"
+ "_accessStartTimestamp"
+ "_attributionListData"
+ "_attributionListDataDiff"
+ "_cameraCaptureAttribution"
+ "_dataAccessType"
+ "_initWithAttributionListData:"
+ "_locationAttribution"
+ "_microphoneRecordingAttribution"
+ "_recent"
+ "_wantsUntransformedData"
+ "accessDuration"
+ "accessEndTimestamp"
+ "accessStartTimestamp"
+ "activeAttributionData"
+ "attributedEntities"
+ "attribution"
+ "attributionListData"
+ "attributionListDataDiff"
+ "audioRecordingActivityAttribution"
+ "camera"
+ "cameraCaptureAttribution"
+ "data-access"
+ "dataAccessAttributions"
+ "dataAccessType"
+ "dataForDomain:client:"
+ "dataWithAccessType:"
+ "dataWithAttributedEntity:"
+ "dataWithEntitiesThatAreSystemServices:"
+ "dataWithExecutableIdentity:"
+ "dataWithUserIdentity:"
+ "dateWithTimeIntervalSinceNow:"
+ "decoded invalid background activities domain data"
+ "decoded invalid calling domain data"
+ "decoded invalid data access attribution of type: %{public}lu (%{public}@)"
+ "decoded invalid data access domain data"
+ "decoded invalid dictionary data"
+ "decoded invalid list data"
+ "decoded invalid location domain data"
+ "decoded invalid media domain data"
+ "decoded invalid server data for domains: %{public}@"
+ "endDate"
+ "executableIdentities"
+ "hasSatisfiedMinimumOnTime"
+ "initWithAttributionListData:"
+ "initWithAttributionListDataDiff:"
+ "initWithAudioRecordingActivityAttribution:recent:startTimestamp:endTimestamp:"
+ "initWithCameraCaptureAttribution:recent:startTimestamp:endTimestamp:"
+ "initWithDataAccessAttribution:"
+ "initWithDataAccessType:microphoneRecordingAttribution:cameraCaptureAttribution:locationAttribution:recent:startTimestamp:endTimestamp:"
+ "initWithLocationAttribution:recent:startTimestamp:endTimestamp:"
+ "initWithMicrophoneRecordingAttribution:recent:startTimestamp:endTimestamp:"
+ "initWithServerHandle:wantsUntransformedData:"
+ "invalid"
+ "isRecent"
+ "locationAttribution"
+ "microphoneRecordingAttribution"
+ "q24@?0@\"STDataAccessAttribution\"8@\"STDataAccessAttribution\"16"
+ "recent"
+ "recentAttributionData"
+ "serverDataForDomains:preferredLocalizations:"
+ "serverDataForDomains:preferredLocalizations:reply:"
+ "setDataAccessAttributions:"
+ "sortedArrayUsingComparator:"
+ "startDate"
+ "state"
+ "stringByAppendingString:"
+ "type"
+ "unsatisfiedMinimumOnTimeAttributionData"
+ "userIdentities"
+ "v40@0:8@\"NSSet\"16@\"NSArray\"24@?<v@?@\"NSDictionary\">32"
+ "wantsUntransformedData"
- "@\"<STStatusDomainData>\"24@0:8Q16"
- "dataForDomain:"
- "serverDataForDomains:"
- "serverDataForDomains:reply:"
- "v32@0:8@\"NSSet\"16@?<v@?@\"NSDictionary\">24"

```
