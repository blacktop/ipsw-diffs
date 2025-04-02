## SystemStatus

> `/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus`

```diff

-210.4.13.0.0
-  __TEXT.__text: 0x53c3c
-  __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_methlist: 0x7a88
-  __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x38e6
-  __TEXT.__oslogstring: 0x128e
-  __TEXT.__gcc_except_tab: 0x444
-  __TEXT.__unwind_info: 0x1f60
-  __TEXT.__objc_classname: 0x1902
-  __TEXT.__objc_methname: 0xa392
-  __TEXT.__objc_methtype: 0x15f2
-  __TEXT.__objc_stubs: 0x54e0
-  __DATA_CONST.__got: 0x550
-  __DATA_CONST.__const: 0x1868
-  __DATA_CONST.__objc_classlist: 0x540
+210.5.2.0.0
+  __TEXT.__text: 0x56b14
+  __TEXT.__auth_stubs: 0x6b0
+  __TEXT.__objc_methlist: 0x7f38
+  __TEXT.__const: 0x100
+  __TEXT.__cstring: 0x3aa5
+  __TEXT.__oslogstring: 0x146a
+  __TEXT.__gcc_except_tab: 0x470
+  __TEXT.__unwind_info: 0x2018
+  __TEXT.__objc_classname: 0x19b7
+  __TEXT.__objc_methname: 0xaba0
+  __TEXT.__objc_methtype: 0x16e1
+  __TEXT.__objc_stubs: 0x5740
+  __DATA_CONST.__got: 0x570
+  __DATA_CONST.__const: 0x19a8
+  __DATA_CONST.__objc_classlist: 0x570
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d28
+  __DATA_CONST.__objc_selrefs: 0x1e50
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x3b8
+  __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x350
-  __AUTH_CONST.__const: 0x800
-  __AUTH_CONST.__cfstring: 0x4200
-  __AUTH_CONST.__objc_const: 0xe3f0
+  __AUTH_CONST.__auth_got: 0x368
+  __AUTH_CONST.__const: 0x8c0
+  __AUTH_CONST.__cfstring: 0x4420
+  __AUTH_CONST.__objc_const: 0xec58
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x4bc
+  __AUTH.__objc_data: 0x3c0
+  __DATA.__objc_ivar: 0x4e8
   __DATA.__data: 0xd28
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_ivar: 0xa0
   __DATA_DIRTY.__objc_data: 0x32a0
   __DATA_DIRTY.__bss: 0x170

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2913
-  Symbols:   3667
-  CStrings:  2654
+  Functions: 3034
+  Symbols:   3805
+  CStrings:  2760
 
Symbols:
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
CStrings:
+ " (in minimum on time)"
+ "@\"<STStatusDomainData>\"32@0:8Q16@\"<STStatusDomainClientHandle>\"24"
+ "@\"STLocationStatusDomainLocationAttribution\""
+ "@\"STMediaStatusDomainCameraCaptureAttribution\""
+ "@\"STMediaStatusDomainMicrophoneRecordingAttribution\""
+ "@16@?0@\"STAttributedEntity\"8"
+ "@16@?0@\"STDataAccessAttribution\"8"
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
+ "T@\"NSSet\",R,C,N,V_userIdentities"
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
+ "_userIdentities"
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
+ "decoded invalid status bar data additions domain data"
+ "decoded invalid status items domain data"
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
+ "stringByAppendingString:"
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
