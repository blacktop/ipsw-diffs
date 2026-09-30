## MigrationKit

> `/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_types2`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA_DIRTY.__objc_data`

```diff

-  __TEXT.__text: 0x8373cc
-  __TEXT.__auth_stubs: 0x67a0
-  __TEXT.__objc_methlist: 0x6f20
-  __TEXT.__const: 0x3a720
-  __TEXT.__oslogstring: 0xfe4c
-  __TEXT.__cstring: 0x19ae1
-  __TEXT.__gcc_except_tab: 0x1788
-  __TEXT.__constg_swiftt: 0xeed8
-  __TEXT.__swift5_typeref: 0xc121
-  __TEXT.__swift5_builtin: 0x320
-  __TEXT.__swift5_reflstr: 0xcd12
-  __TEXT.__swift5_fieldmd: 0xddfc
-  __TEXT.__swift5_assocty: 0x2350
-  __TEXT.__swift5_proto: 0x23d0
-  __TEXT.__swift5_types: 0xcf8
-  __TEXT.__swift_as_entry: 0x1690
-  __TEXT.__swift_as_ret: 0x1c64
-  __TEXT.__swift5_capture: 0x2da0
+  __TEXT.__text: 0x86c654
+  __TEXT.__auth_stubs: 0x67f0
+  __TEXT.__objc_methlist: 0x6f68
+  __TEXT.__const: 0x3b130
+  __TEXT.__oslogstring: 0x1001c
+  __TEXT.__cstring: 0x1a0e1
+  __TEXT.__gcc_except_tab: 0x1984
+  __TEXT.__constg_swiftt: 0xf1c4
+  __TEXT.__swift5_typeref: 0xc579
+  __TEXT.__swift5_builtin: 0x334
+  __TEXT.__swift5_reflstr: 0xcee2
+  __TEXT.__swift5_fieldmd: 0xe108
+  __TEXT.__swift5_assocty: 0x2398
+  __TEXT.__swift5_proto: 0x2430
+  __TEXT.__swift5_types: 0xd28
+  __TEXT.__swift_as_entry: 0x1764
+  __TEXT.__swift_as_ret: 0x1d38
+  __TEXT.__swift5_capture: 0x2e3c
   __TEXT.__swift5_protos: 0x160
-  __TEXT.__swift5_mpenum: 0xd8
+  __TEXT.__swift5_mpenum: 0xe0
   __TEXT.__swift5_types2: 0x8
-  __TEXT.__unwind_info: 0x18ce0
-  __TEXT.__eh_frame: 0x47500
-  __TEXT.__objc_classname: 0x4421
-  __TEXT.__objc_methname: 0x14596
-  __TEXT.__objc_methtype: 0x457e
-  __TEXT.__objc_stubs: 0x10000
-  __DATA_CONST.__got: 0x2370
-  __DATA_CONST.__const: 0xb50
-  __DATA_CONST.__objc_classlist: 0xc58
+  __TEXT.__unwind_info: 0x1a128
+  __TEXT.__eh_frame: 0x49160
+  __TEXT.__objc_classname: 0x4451
+  __TEXT.__objc_methname: 0x14656
+  __TEXT.__objc_methtype: 0x45be
+  __TEXT.__objc_stubs: 0x10080
+  __DATA_CONST.__got: 0x2380
+  __DATA_CONST.__const: 0xb78
+  __DATA_CONST.__objc_classlist: 0xc60
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x2c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4ce0
+  __DATA_CONST.__objc_selrefs: 0x4d00
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x340
   __DATA_CONST.__objc_arraydata: 0x488
-  __AUTH_CONST.__auth_got: 0x33e8
-  __AUTH_CONST.__const: 0x18c78
+  __AUTH_CONST.__auth_got: 0x3410
+  __AUTH_CONST.__const: 0x19338
   __AUTH_CONST.__cfstring: 0x5780
-  __AUTH_CONST.__objc_const: 0x1bfb0
+  __AUTH_CONST.__objc_const: 0x1c1f0
   __AUTH_CONST.__objc_intobj: 0xcc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x210
-  __AUTH.__objc_data: 0x7d20
-  __AUTH.__data: 0x16f28
-  __DATA.__objc_ivar: 0x7d8
-  __DATA.__data: 0xe010
-  __DATA.__bss: 0x3e9e0
-  __DATA.__common: 0x1b98
+  __AUTH.__objc_data: 0x7cd0
+  __AUTH.__data: 0x17178
+  __DATA.__objc_ivar: 0x7e8
+  __DATA.__data: 0xe3e0
+  __DATA.__bss: 0x3f5f0
+  __DATA.__common: 0x1b80
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 24871
-  Symbols:   12226
-  CStrings:  8911
+  Functions: 25233
+  Symbols:   12314
+  CStrings:  8977
 
Symbols:
+ -[MKHPMInterface forceDeviceModeWithError:]
+ -[MKUSBDevice deregisterExistingMigrationInterface]
+ -[MKUSBDevice isCancelled]
+ -[MKUSBDevice usbRoleChanged:]
+ -[MKUSBMonitor startMonitoringWithError:]
+ -[MKUSBMonitor stopMonitoring]
+ _OBJC_IVAR_$_MKUSBDevice._cancelled
+ _OBJC_IVAR_$_MKUSBDevice._hpmInterface
+ _OBJC_IVAR_$_MKUSBDevice._monitor
+ _OBJC_IVAR_$_MKUSBDevice._roleSemaphore
+ __DATA__TtC12MigrationKit15ServedCountsBox
+ __DATA__TtC12MigrationKit22InFlightExportRegistry
+ __IVARS__TtC12MigrationKit15ServedCountsBox
+ __IVARS__TtC12MigrationKit22InFlightExportRegistry
+ __IVARS__TtC12MigrationKitP33_5DC9EB87917FF34D1159C27DFDA0847512KeysetCursor
+ __METACLASS_DATA__TtC12MigrationKit15ServedCountsBox
+ __METACLASS_DATA__TtC12MigrationKit22InFlightExportRegistry
+ __OBJC_CLASS_PROTOCOLS_$_MKUSBDevice
+ ___30-[MKUSBMonitor stopMonitoring]_block_invoke
+ ___41-[MKUSBMonitor startMonitoringWithError:]_block_invoke
+ ___43-[MKHPMInterface forceDeviceModeWithError:]_block_invoke
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___swift_memcpy192_8
+ ___unnamed_11
+ ___unnamed_4
+ _associated conformance 12MigrationKit17TransferAnalyticsC12SessionState33_DD39688A8C346E70754E4717F326607DLLOSHAASQ
+ _associated conformance 12MigrationKit19OnEachAsyncSequenceV8IteratorVyx_GScIAA7FailureScI_s5Error
+ _associated conformance 12MigrationKit19OnEachAsyncSequenceVyxGSciAA0E8IteratorSci_ScI
+ _associated conformance 12MigrationKit34BackgroundImportContextPersistenceV10CodingKeys33_C381B5EF9784980CACC61CC173204B05LLOSHAASQ
+ _associated conformance 12MigrationKit34BackgroundImportContextPersistenceV10CodingKeys33_C381B5EF9784980CACC61CC173204B05LLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 12MigrationKit34BackgroundImportContextPersistenceV10CodingKeys33_C381B5EF9784980CACC61CC173204B05LLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 12MigrationKit6CountsV10CodingKeys015_07A8E7F8D8FDD1I16C5A7BF6E99FC4266LLOSHAASQ
+ _associated conformance 12MigrationKit6CountsV10CodingKeys015_07A8E7F8D8FDD1I16C5A7BF6E99FC4266LLOs0D3KeyAAs23CustomStringConvertible
+ _associated conformance 12MigrationKit6CountsV10CodingKeys015_07A8E7F8D8FDD1I16C5A7BF6E99FC4266LLOs0D3KeyAAs28CustomDebugStringConvertible
+ _get_enum_tag_for_layout_string 12MigrationKit8HTTPPathVAA6CountsVIeghHgn_Sg
+ _objc_msgSend$deregisterExistingMigrationInterface
+ _objc_msgSend$forceDeviceModeWithError:
+ _objc_msgSend$startMonitoringWithError:
+ _objc_msgSend$stopMonitoring
+ _objectdestroy.162Tm
+ _objectdestroy.94Tm
+ _symbolic SDySS_____G 12MigrationKit22InFlightExportRegistryC5Entry33_009F3BAA1966D5D3F75713DFB313808ELLV
+ _symbolic SDy__________G 12MigrationKit20OSMigrationDataClassO AA17TransferAnalyticsC0dE9Lifecycle33_DD39688A8C346E70754E4717F326607DLLV
+ _symbolic SS3key_yXl5valuet
+ _symbolic SayxGq_Sg_SitYac
+ _symbolic Si11pendingSkip_t
+ _symbolic Si7nextRow_t
+ _symbolic SiIeghHy_
+ _symbolic _____ 12MigrationKit10Pagination33_5DC9EB87917FF34D1159C27DFDA08475LLO
+ _symbolic _____ 12MigrationKit12KeysetCursor33_5DC9EB87917FF34D1159C27DFDA08475LLC
+ _symbolic _____ 12MigrationKit15ServedCountsBoxC
+ _symbolic _____ 12MigrationKit17TransferAnalyticsC12SessionState33_DD39688A8C346E70754E4717F326607DLLO
+ _symbolic _____ 12MigrationKit17TransferAnalyticsC18DataClassLifecycle33_DD39688A8C346E70754E4717F326607DLLV
+ _symbolic _____ 12MigrationKit19OnEachAsyncSequenceV
+ _symbolic _____ 12MigrationKit19OnEachAsyncSequenceV8IteratorV
+ _symbolic _____ 12MigrationKit22InFlightExportRegistryC
+ _symbolic _____ 12MigrationKit22InFlightExportRegistryC5Entry33_009F3BAA1966D5D3F75713DFB313808ELLV
+ _symbolic _____ 12MigrationKit34BackgroundImportContextPersistenceV
+ _symbolic _____ 12MigrationKit34BackgroundImportContextPersistenceV10CodingKeys33_C381B5EF9784980CACC61CC173204B05LLO
+ _symbolic _____ 12MigrationKit6CountsV
+ _symbolic _____ 12MigrationKit6CountsV10CodingKeys015_07A8E7F8D8FDD1I16C5A7BF6E99FC4266LLO
+ _symbolic _____3key______5valuet 12MigrationKit20OSMigrationDataClassO AA17TransferAnalyticsC0dE9Lifecycle33_DD39688A8C346E70754E4717F326607DLLV
+ _symbolic _____3key______5valuetSg 12MigrationKit20OSMigrationDataClassO AA17TransferAnalyticsC0dE9Lifecycle33_DD39688A8C346E70754E4717F326607DLLV
+ _symbolic _____Sg 12MigrationKit17OriginatingUIFlowO
+ _symbolic _____Sg 12MigrationKit17TransferAnalyticsC18DataClassLifecycle33_DD39688A8C346E70754E4717F326607DLLV
+ _symbolic _____Sg 12MigrationKit34BackgroundImportContextPersistenceV
+ _symbolic ___________pIeghHrzo_ 10Foundation3URLV s5ErrorP
+ _symbolic ___________t 12MigrationKit20OSMigrationDataClassO AA17TransferAnalyticsC0dE9Lifecycle33_DD39688A8C346E70754E4717F326607DLLV
+ _symbolic ______p5error_Si5countSi12firstSeenIdxt s5ErrorP
+ _symbolic _____x______pXj r0_lScI_px7ElementRts_q_7FailureRtsXPXGMq s5ErrorP
+ _symbolic _____x______pXj r0_lSci_px7ElementRts_q_7FailureRtsXPXGMq s5ErrorP
+ _symbolic _____ySS3key_yXl5valuetG s23_ContiguousArrayStorageC
+ _symbolic _____ySS_____G s18_DictionaryStorageC 12MigrationKit22InFlightExportRegistryC5Entry33_009F3BAA1966D5D3F75713DFB313808ELLV
+ _symbolic _____ySS______p5error_Si5countSi12firstSeenIdxtG s18_DictionaryStorageC s5ErrorP
+ _symbolic _____y_____G 12MigrationKit19OnEachAsyncSequenceV AA16HTTPPartResponseC
+ _symbolic _____y_____G 2os21OSAllocatedUnfairLockV 12MigrationKit6CountsV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 12MigrationKit34BackgroundImportContextPersistenceV10CodingKeys33_C381B5EF9784980CACC61CC173204B05LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 12MigrationKit6CountsV10CodingKeys015_07A8E7F8D8FDD1L16C5A7BF6E99FC4266LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 12MigrationKit34BackgroundImportContextPersistenceV10CodingKeys33_C381B5EF9784980CACC61CC173204B05LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 12MigrationKit6CountsV10CodingKeys015_07A8E7F8D8FDD1L16C5A7BF6E99FC4266LLO
+ _symbolic _____y_____SSG 12MigrationKit12KeysetCursor33_5DC9EB87917FF34D1159C27DFDA08475LLC AA33PhotoLibraryPersistenceCollectionV
+ _symbolic _____y__________G 12MigrationKit12KeysetCursor33_5DC9EB87917FF34D1159C27DFDA08475LLC AA28PhotoLibraryPersistenceAssetV s6UInt64V
+ _symbolic _____y__________G s13ManagedBufferCsRi__rlE 12MigrationKit6CountsV So16os_unfair_lock_sV
+ _symbolic _____y__________G s18_DictionaryStorageC 12MigrationKit20OSMigrationDataClassO AC17TransferAnalyticsC0fG9Lifecycle33_DD39688A8C346E70754E4717F326607DLLV
+ _symbolic _____y______p5error_Si5countSi12firstSeenIdxtG s23_ContiguousArrayStorageC s5ErrorP
+ _symbolic _____y______y______y______GSSG_____y_SSGG 10Foundation20PredicateExpressionsO10ComparisonV AC7KeyPathV AC8VariableV 12MigrationKit38PhotoLibraryPersistenceCollectionModelC AC5ValueV
+ _symbolic _____y______y______y______GSSG_____y_SSGG 10Foundation20PredicateExpressionsO10ComparisonV AC7KeyPathV AC8VariableV 12MigrationKit40PhotoLibraryPersistenceRelationshipModelC AC5ValueV
+ _symbolic _____y______y______y______G_____G_____y_AFGG 10Foundation20PredicateExpressionsO10ComparisonV AC7KeyPathV AC8VariableV 12MigrationKit33PhotoLibraryPersistenceAssetModelC s6UInt64V AC5ValueV
+ _symbolic _____y______y______y______G_____G_____y_AFGG 10Foundation20PredicateExpressionsO10ComparisonV AC7KeyPathV AC8VariableV 12MigrationKit40PhotoLibraryPersistenceRelationshipModelC s6UInt64V AC5ValueV
+ _symbolic _____y______y______y______G_____G_____y_AFGG 10Foundation20PredicateExpressionsO5EqualV AC7KeyPathV AC8VariableV 12MigrationKit40PhotoLibraryPersistenceRelationshipModelC s6UInt64V AC5ValueV
+ _symbolic _____y______y______y______y______GSSG_____y_SSGG_____y_ACy_AF_____GAHy_ALGGG 10Foundation20PredicateExpressionsO11ConjunctionV AC5EqualV AC7KeyPathV AC8VariableV 12MigrationKit33PhotoLibraryPersistenceAssetModelC AC5ValueV AC10ComparisonV s6UInt64V
+ _symbolic _____y______y______y______y______GSSG_____y_SSGG_____y_ACy_AF_____GAHy_ALGGG 10Foundation20PredicateExpressionsO11ConjunctionV AC5EqualV AC7KeyPathV AC8VariableV 12MigrationKit40PhotoLibraryPersistenceRelationshipModelC AC5ValueV AC10ComparisonV s6UInt64V
+ _symbolic _____y______y______y______y______GSiG_____y_SiGG_____y_ACy_AF_____GAHy_ALGGG 10Foundation20PredicateExpressionsO11ConjunctionV AC5EqualV AC7KeyPathV AC8VariableV 12MigrationKit33PhotoLibraryPersistenceAssetModelC AC5ValueV AC10ComparisonV s6UInt64V
+ _symbolic _____y______y______y______y______G_____G_____y_AGGG_____y_ACy_AFSSGAIy_SSGGG 10Foundation20PredicateExpressionsO11ConjunctionV AC5EqualV AC7KeyPathV AC8VariableV 12MigrationKit40PhotoLibraryPersistenceRelationshipModelC s6UInt64V AC5ValueV AC10ComparisonV
+ _symbolic _____yx_G 12MigrationKit19OnEachAsyncSequenceV8IteratorV
+ _symbolic q_Sg
+ _symbolic q_xc
+ _symbolic y___________tYaYbcSg 12MigrationKit8HTTPPathV AA6CountsV
+ _symbolic yxYac
+ _symbolic yyYacSg
+ _type_layout_string 12MigrationKit22InFlightExportRegistryC5Entry33_009F3BAA1966D5D3F75713DFB313808ELLV
+ _type_layout_string 12MigrationKit6CountsV
+ _type_layout_string l12MigrationKit19OnEachAsyncSequenceV8IteratorVyx_G
+ _type_layout_string l12MigrationKit19OnEachAsyncSequenceVyxG
- __DATA__TtC12MigrationKit14FeaturePayload
- __IVARS__TtC12MigrationKit14FeaturePayload
- __METACLASS_DATA__TtC12MigrationKit14FeaturePayload
- ___swift_memcpy224_8
- _get_enum_tag_for_layout_string 12MigrationKit8HTTPPathVIeghHg_Sg
- _objectdestroy.122Tm
- _objectdestroy.154Tm
- _objectdestroy.91Tm
- _symbolic _____ 12MigrationKit14FeaturePayloadC
- _symbolic _____y_SSSgG 10Foundation20PredicateExpressionsO5ValueV
- _symbolic _____y______SgG 10Foundation20PredicateExpressionsO5ValueV s6UInt64V
- _symbolic _____y______y_SSSgGSSG 10Foundation20PredicateExpressionsO12ForcedUnwrapV AC5ValueV
- _symbolic _____y______y______SgGACG 10Foundation20PredicateExpressionsO12ForcedUnwrapV AC5ValueV s6UInt64V
- _symbolic _____y______y______y______GSSG_____y______y_SSSgGSSGG 10Foundation20PredicateExpressionsO5EqualV AC7KeyPathV AC8VariableV 12MigrationKit40PhotoLibraryPersistenceRelationshipModelC AC12ForcedUnwrapV AC5ValueV
- _symbolic _____y______y______y______G_____G_____y______y_AFSgGAFGG 10Foundation20PredicateExpressionsO5EqualV AC7KeyPathV AC8VariableV 12MigrationKit40PhotoLibraryPersistenceRelationshipModelC s6UInt64V AC12ForcedUnwrapV AC5ValueV
- _symbolic y_____YaYbcSg 12MigrationKit8HTTPPathV
CStrings:
+ "@\"MKHPMInterface\""
+ "@\"MKUSBMonitor\""
+ "@\"NSObject<OS_dispatch_semaphore>\""
+ "Attaching to existing export for %{public}s"
+ "Attester unavailable when verifying peer message"
+ "Cloud content only available in FCI mode"
+ "Device must be connected to the Internet"
+ "Failed to load background import context from plist"
+ "Failed to save background import context to plist"
+ "MigrationKit/BackgroundImportContextPersistence.swift"
+ "MigrationKit/Environment.swift"
+ "MigrationKit/InFlightExportRegistry.swift"
+ "MigrationKit/Reason+Conversion.swift"
+ "MigrationKit/TransferAnalytics.swift"
+ "Peer capability mismatch"
+ "Peer disconnected: "
+ "Peer reported critical battery"
+ "Peer reported device reboot"
+ "Peer reported failure state"
+ "Peer reported insufficient space"
+ "SKU check overridden by attestation force verdict profile"
+ "Starting export for %{public}s"
+ "User cancelled migration"
+ "Zero size attachment"
+ "[%s] GoOffAndOnBus(empty) failed: 0x%x"
+ "[%s] SetDescription(empty) failed: 0x%x"
+ "[%s] USB monitor failed to start: %@"
+ "[%s] USB role detected: %ld"
+ "[%s] USB role swap failed: %@"
+ "[%s] USB role swap failed: HPMInterface is nil"
+ "[%s] attempting USB role swap to device"
+ "[%s] cleared stale migration interface from IORegistry"
+ "[%s] failed to create empty description"
+ "[%s] failed to undo USB role swap: %@"
+ "[%s] no stale migration interface in IORegistry; skipping off/on-bus cycle"
+ "[%s] waiting for USB cable..."
+ "_TtC12MigrationKit15ServedCountsBox"
+ "_TtC12MigrationKit22InFlightExportRegistry"
+ "_cancelled"
+ "_connect(code:)"
+ "_dataControlRouterReceivedState(_:)"
+ "_hpmInterface"
+ "_monitor"
+ "_roleSemaphore"
+ "asPeerDisconnectFailure"
+ "attester"
+ "background context is not import; skipping telemetry."
+ "capabilityDetermined(success:capability:)"
+ "counts"
+ "deregisterExistingMigrationInterface"
+ "extract"
+ "fetch"
+ "fired backgroundStart."
+ "fired heartbeat #%ld"
+ "forceDeviceModeWithError:"
+ "handleConnectionFailure(_:_:)"
+ "heartbeat reached telemetryId cap (99); stopping"
+ "heartbeat task cancelled"
+ "homescreenLayout"
+ "inFlight"
+ "migrationDirection"
+ "nextID"
+ "no background import context; skipping telemetry."
+ "onWiFiAwareUsed"
+ "originatingUIFlow"
+ "passwordsAndPasskeys"
+ "servedCounts"
+ "serverChangedState(newState:)"
+ "sessionState"
+ "startEventEmitted"
+ "startMonitoringWithError:"
+ "stopMonitoring"
+ "\xb1"
+ "║ TELEMETRY → "
- "Failed sending %s telemetry to CoreAnalytics"
- "Invalid attachment size: "
- "Sending %s telemetry to CoreAnalytics: %s"
- "Successfully sent %s telemetry to CoreAnalytics"
- "_TtC12MigrationKit14FeaturePayload"
- "failedItemCount"
- "networkLost(_:)"
- "networkLost(_:isCurrent:)"
```
