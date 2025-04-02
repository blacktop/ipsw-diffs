## SystemStatusServer

> `/System/Library/PrivateFrameworks/SystemStatusServer.framework/SystemStatusServer`

```diff

-210.4.13.0.0
-  __TEXT.__text: 0x1a56c
-  __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__objc_methlist: 0x1980
-  __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x1887
-  __TEXT.__gcc_except_tab: 0x1f4
-  __TEXT.__oslogstring: 0x9d5
-  __TEXT.__unwind_info: 0x728
-  __TEXT.__objc_classname: 0x751
-  __TEXT.__objc_methname: 0x4bdd
-  __TEXT.__objc_methtype: 0x1776
-  __TEXT.__objc_stubs: 0x3780
-  __DATA_CONST.__got: 0x3d8
-  __DATA_CONST.__const: 0xbf0
-  __DATA_CONST.__objc_classlist: 0xe8
-  __DATA_CONST.__objc_protolist: 0xe8
+210.5.2.0.0
+  __TEXT.__text: 0x1ce04
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_methlist: 0x1aa0
+  __TEXT.__const: 0xc8
+  __TEXT.__cstring: 0x1a3c
+  __TEXT.__gcc_except_tab: 0x30c
+  __TEXT.__oslogstring: 0xa2f
+  __TEXT.__unwind_info: 0x7c0
+  __TEXT.__objc_classname: 0x825
+  __TEXT.__objc_methname: 0x507c
+  __TEXT.__objc_methtype: 0x1883
+  __TEXT.__objc_stubs: 0x3b00
+  __DATA_CONST.__got: 0x430
+  __DATA_CONST.__const: 0xd18
+  __DATA_CONST.__objc_classlist: 0x108
+  __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1130
-  __DATA_CONST.__objc_superrefs: 0xc8
-  __AUTH_CONST.__auth_got: 0x370
-  __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0x15c0
-  __AUTH_CONST.__objc_const: 0x3658
-  __AUTH_CONST.__objc_intobj: 0x30
-  __DATA.__objc_ivar: 0x21c
-  __DATA.__data: 0xae0
+  __DATA_CONST.__objc_selrefs: 0x1218
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__const: 0x240
+  __AUTH_CONST.__cfstring: 0x1600
+  __AUTH_CONST.__objc_const: 0x3b68
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x258
+  __DATA.__data: 0xb40
   __DATA_DIRTY.__objc_ivar: 0x8
   __DATA_DIRTY.__objc_data: 0x910
   __DATA_DIRTY.__bss: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 622
-  Symbols:   933
-  CStrings:  1261
+  Functions: 659
+  Symbols:   990
+  CStrings:  1321
 
Symbols:
+ _BSFloatGreaterThanFloat
+ _OBJC_CLASS_$_BSContinuousMachTimer
+ _OBJC_CLASS_$_STAttributedEntityResolverProvider
+ _OBJC_CLASS_$_STDataAccessAttribution
+ _OBJC_CLASS_$_STDataAccessStatusDomainData
+ _OBJC_CLASS_$_STDataAccessStatusDomainDataProvider
+ _OBJC_CLASS_$_STDataAccessStatusDomainDisplayNameTransformer
+ _OBJC_CLASS_$_STDataAccessStatusDomainDisplayNameTransformerProvider
+ _OBJC_CLASS_$_STDataAccessStatusDomainPublisher
+ _OBJC_CLASS_$_STLocationStatusDomain
+ _OBJC_CLASS_$_STMediaStatusDomain
+ _OBJC_CLASS_$_STMutableDataAccessStatusDomainData
+ _OBJC_METACLASS_$_STAttributedEntityResolverProvider
+ _OBJC_METACLASS_$_STDataAccessStatusDomainDataProvider
+ _OBJC_METACLASS_$_STDataAccessStatusDomainDisplayNameTransformer
+ _OBJC_METACLASS_$_STDataAccessStatusDomainDisplayNameTransformerProvider
+ _STDataAccessStatusDomainMinumumOnTime
+ _STDescriptionForDataAccessType
+ _STStatusDomainEntitlementValueDataAccess
+ _STSystemStatusLogDataIntegrity
+ _STTimestampNow
- _OBJC_CLASS_$_NSConstantIntegerNumber
CStrings:
+ "\x1a"
+ "@\"<STAttributedEntityResolverProviding>\""
+ "@\"<STStatusDomainData>\"32@0:8Q16@\"<STStatusDomainClientHandle>\"24"
+ "@\"NSMutableArray\""
+ "@\"STAttributedEntityResolver\"24@0:8@\"NSArray\"16"
+ "@\"STDataAccessAttribution\"16@?0@8"
+ "@\"STDataAccessStatusDomainData\""
+ "@\"STDataAccessStatusDomainPublisher\""
+ "@\"STLocationStatusDomain\""
+ "@\"STMediaStatusDomain\""
+ "@16@?0@\"STDataAccessAttribution\"8"
+ "@32@0:8Q16@24"
+ "B16@?0@\"STLocationStatusDomainLocationAttribution\"8"
+ "STAttributedEntityResolverProvider"
+ "STAttributedEntityResolverProviding"
+ "STDataAccessStatusDomain-MinimumDisplayTime"
+ "STDataAccessStatusDomain-RecentAttributionExpiration"
+ "STDataAccessStatusDomainDataProvider"
+ "STDataAccessStatusDomainDisplayNameTransformer"
+ "STDataAccessStatusDomainDisplayNameTransformerProvider"
+ "_activeAttributionMinimumDisplayTimers"
+ "_activeAttributions"
+ "_attributionsWaitingForMinimumDisplayTime"
+ "_currentData"
+ "_dataAccessPublisher"
+ "_entityResolverProvider"
+ "_locationDomain"
+ "_mediaDomain"
+ "_recentAttributionExpirationTimers"
+ "_recentAttributions"
+ "accessDuration"
+ "accessEndTimestamp"
+ "accessStartTimestamp"
+ "allValues"
+ "audioRecordingActivityAttribution"
+ "bs_filter:"
+ "cameraCaptureAttribution"
+ "com.apple.systemstatus.data-access.internalqueue"
+ "dataAccessAttributions"
+ "dataAccessType"
+ "dataForDomain:client:"
+ "initWithAudioRecordingActivityAttribution:recent:startTimestamp:endTimestamp:"
+ "initWithCameraCaptureAttribution:recent:startTimestamp:endTimestamp:"
+ "initWithEntityResolverProvider:"
+ "initWithIdentifier:"
+ "initWithIdentityResolver:"
+ "initWithLocationAttribution:recent:startTimestamp:endTimestamp:"
+ "initWithMicrophoneRecordingAttribution:recent:startTimestamp:endTimestamp:"
+ "initWithPreferredLocalizations:identityResolver:"
+ "initWithServerHandle:publisherServerHandle:"
+ "initWithServerHandle:wantsUntransformedData:"
+ "isRecent"
+ "locationAttribution"
+ "microphoneRecordingAttribution"
+ "observeData:"
+ "resolverForPreferredLocalizations:"
+ "scheduleWithFireInterval:leewayInterval:queue:handler:"
+ "serverDataForDomains:preferredLocalizations:reply:"
+ "setDataAccessAttributions:"
+ "setVolatileData:"
+ "transformer encountered data access attribution of invalid type: %{public}lu (%{public}@)"
+ "v16@?0@\"BSContinuousMachTimer\"8"
+ "v24@?0@\"STLocationStatusDomainData\"8@\"STLocationStatusDomainDataChangeContext\"16"
+ "v24@?0@\"STMediaStatusDomainData\"8@\"<STStatusDomainDataChangeContext>\"16"
+ "v40@0:8@\"NSSet\"16@\"NSArray\"24@?<v@?@\"NSDictionary\">32"
+ "wantsUntransformedData"
- "@\"<STStatusDomainData>\"24@0:8Q16"
- "data-access"
- "dataForDomain:"
- "serverDataForDomains:reply:"
- "v32@0:8@\"NSSet\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@16@?24"

```
