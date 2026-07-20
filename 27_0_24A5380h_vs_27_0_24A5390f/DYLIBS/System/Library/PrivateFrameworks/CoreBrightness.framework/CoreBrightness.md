## CoreBrightness

> `/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-2300.0.10.0.1
-  __TEXT.__text: 0x16a888
-  __TEXT.__objc_methlist: 0xd08c
-  __TEXT.__cstring: 0xcb1a
-  __TEXT.__const: 0x169f8
-  __TEXT.__oslogstring: 0x1963d
-  __TEXT.__gcc_except_tab: 0x2768
+2300.0.18.502.1
+  __TEXT.__text: 0x16c570
+  __TEXT.__objc_methlist: 0xd1f4
+  __TEXT.__cstring: 0xcd15
+  __TEXT.__const: 0x16a08
+  __TEXT.__oslogstring: 0x1990d
+  __TEXT.__gcc_except_tab: 0x2804
   __TEXT.__dlopen_cstrs: 0x1d5
-  __TEXT.__swift5_typeref: 0xeb0
-  __TEXT.__constg_swiftt: 0xc2c
+  __TEXT.__swift5_typeref: 0xeaf
+  __TEXT.__constg_swiftt: 0xc34
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_reflstr: 0xa44
+  __TEXT.__swift5_reflstr: 0xa4e
   __TEXT.__swift5_fieldmd: 0x1018
   __TEXT.__swift5_assocty: 0x288
   __TEXT.__swift5_proto: 0x308

   __TEXT.__swift5_capture: 0x3d0
   __TEXT.__swift5_mpenum: 0x28
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x5580
+  __TEXT.__unwind_info: 0x55d8
   __TEXT.__eh_frame: 0xb90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2ec0
-  __DATA_CONST.__objc_classlist: 0x6f0
-  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__const: 0x2f60
+  __DATA_CONST.__objc_classlist: 0x6f8
+  __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x368
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x5898
+  __DATA_CONST.__objc_selrefs: 0x5958
   __DATA_CONST.__objc_protorefs: 0x138
-  __DATA_CONST.__objc_superrefs: 0x5b8
-  __DATA_CONST.__objc_arraydata: 0xcb8
-  __DATA_CONST.__got: 0x7c0
+  __DATA_CONST.__objc_superrefs: 0x5c0
+  __DATA_CONST.__objc_arraydata: 0xcc8
+  __DATA_CONST.__got: 0x7b0
   __AUTH_CONST.__const: 0x3dc8
-  __AUTH_CONST.__cfstring: 0xe380
-  __AUTH_CONST.__objc_const: 0x334e0
+  __AUTH_CONST.__cfstring: 0xe5c0
+  __AUTH_CONST.__objc_const: 0x33890
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH_CONST.__objc_intobj: 0xd80
-  __AUTH_CONST.__objc_arrayobj: 0x3d8
-  __AUTH_CONST.__objc_dictobj: 0x550
+  __AUTH_CONST.__objc_intobj: 0xdb0
+  __AUTH_CONST.__objc_arrayobj: 0x408
   __AUTH_CONST.__objc_floatobj: 0x1a0
+  __AUTH_CONST.__objc_dictobj: 0x550
   __AUTH_CONST.__auth_got: 0x1370
-  __AUTH.__objc_data: 0x2630
+  __AUTH.__objc_data: 0x2680
   __AUTH.__data: 0x640
-  __DATA.__objc_ivar: 0x16e0
-  __DATA.__data: 0x2eb78
+  __DATA.__objc_ivar: 0x1718
+  __DATA.__data: 0x34fb8
   __DATA.__bss: 0x66c0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x2238

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8675
-  Symbols:   12460
-  CStrings:  4670
+  Functions: 8711
+  Symbols:   12544
+  CStrings:  4696
 
Symbols:
+ +[NSError(BacklightdExportedObj) exportedObjError:]
+ -[BacklightdExportedObj wasDisconnected]
+ -[CBALSMitigationState alsNode]
+ -[CBALSMitigationState ceConfidenceThreshold]
+ -[CBALSMitigationState ceModelID]
+ -[CBALSMitigationState ceModule]
+ -[CBALSMitigationState dealloc]
+ -[CBALSMitigationState policyFilter]
+ -[CBALSMitigationState setAlsNode:]
+ -[CBALSMitigationState setCeConfidenceThreshold:]
+ -[CBALSMitigationState setCeModelID:]
+ -[CBALSMitigationState setCeModule:]
+ -[CBALSMitigationState setPolicyFilter:]
+ -[CBALSMitigationState setStats:]
+ -[CBALSMitigationState stats]
+ -[CBAODState fixedLuxBrightenThresholds]
+ -[CBAODState fixedLuxDimThresholds]
+ -[CBAODState initWithDisplayID:]
+ -[CBAODState isHighLuminanceAODActive]
+ -[CBAODThresholdModule applyFixedLuxThresholdsForLux:dimTarget:brightenTarget:]
+ -[CBAODThresholdModule initWithQueue:displayID:andAODState:]
+ -[CBBrightnessTransaction _completeWithError:]
+ -[CBBrightnessTransaction _setBrightness:withError:]
+ -[CBBrightnessTransaction complete]
+ -[CBBrightnessTransaction initWithClient:andHandle:commitType:timeout:]
+ -[CBColorModuleShared enableMitigationsForALSNode:]
+ -[CBColorModuleShared replaceEvent:withFilteredEvent:]
+ -[CBColorPolicyFilter initWithID:serviceID:]
+ -[CBDisplayBrightnessClient newBrightnessAdjustmentWithError:]
+ -[CBDisplayBrightnessClient setProperties:]
+ -[CBIndicatorBrightnessModule forceSILOff]
+ GCC_except_table101
+ GCC_except_table122
+ _A_SDRGF
+ _D_SDRGF
+ _L_SDRGF
+ _OBJC_CLASS_$_CBALSMitigationState
+ _OBJC_IVAR_$_BacklightdExportedObj._transactions
+ _OBJC_IVAR_$_CBALSMitigationState._alsNode
+ _OBJC_IVAR_$_CBALSMitigationState._ceConfidenceThreshold
+ _OBJC_IVAR_$_CBALSMitigationState._ceModelID
+ _OBJC_IVAR_$_CBALSMitigationState._ceModule
+ _OBJC_IVAR_$_CBALSMitigationState._policyFilter
+ _OBJC_IVAR_$_CBALSMitigationState._stats
+ _OBJC_IVAR_$_CBAODState._fixedLuxBrightenThresholds
+ _OBJC_IVAR_$_CBAODState._fixedLuxDimThresholds
+ _OBJC_IVAR_$_CBAODThresholdModule._lastPushedBrightenLuxThreshold
+ _OBJC_IVAR_$_CBAODThresholdModule._lastPushedDimLuxThreshold
+ _OBJC_IVAR_$_CBBrightnessTransaction._logHandle
+ _OBJC_IVAR_$_CBBrightnessTransaction._timeout
+ _OBJC_IVAR_$_CBBrightnessTransaction._timer
+ _OBJC_IVAR_$_CBColorModuleShared._alsMitigationState
+ _OBJC_IVAR_$_CBColorModuleShared._anyMitigationEnabled
+ _OBJC_IVAR_$_CBColorModuleShared._overrideFilters
+ _OBJC_IVAR_$_CBColorPolicyFilter._serviceID
+ _OBJC_IVAR_$_CBDisplayBrightnessClient._properties
+ _OBJC_METACLASS_$_CBALSMitigationState
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSError_$_BacklightdExportedObj
+ __OBJC_$_CATEGORY_NSError_$_BacklightdExportedObj
+ __OBJC_$_INSTANCE_METHODS_CBALSMitigationState
+ __OBJC_$_INSTANCE_VARIABLES_CBALSMitigationState
+ __OBJC_$_PROP_LIST_CBALSMitigationState
+ __OBJC_$_PROP_LIST_CBBrightnessAdjustment
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CBBrightnessAdjustment
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CBBrightnessAdjustment
+ __OBJC_$_PROTOCOL_REFS_CBBrightnessAdjustment
+ __OBJC_CLASS_PROTOCOLS_$_CBBrightnessTransaction
+ __OBJC_CLASS_RO_$_CBALSMitigationState
+ __OBJC_LABEL_PROTOCOL_$_CBBrightnessAdjustment
+ __OBJC_METACLASS_RO_$_CBALSMitigationState
+ __OBJC_PROTOCOL_$_CBBrightnessAdjustment
+ ___51-[CBColorModuleShared enableMitigationsForALSNode:]_block_invoke
+ ___52-[CBBrightnessTransaction _setBrightness:withError:]_block_invoke
+ ___59-[BrightnessSystemClientInternal copyPropertyForKey:error:]_block_invoke_2
+ ___66-[BrightnessSystemClientInternal copyPropertyForKey:handle:error:]_block_invoke_2
+ ___block_descriptor_64_e8_32o40o48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_72_e8_32o40o48o56r_e5_v8?0ls32l8s40l8s48l8r56l8
+ _kCBSPITransaction
+ _kCBSPITransactionCommit
+ _kCBSPITransactionHandle
+ _kCBSPITransactionKey
+ _kCBSPITransactionOnCommit
+ _kCBSPITransactionProperty
+ _kCBSPITransactionUUID
+ _objc_msgSend$_completeWithError:
+ _objc_msgSend$_queue
+ _objc_msgSend$_setBrightness:withError:
+ _objc_msgSend$alsNode
+ _objc_msgSend$applyFixedLuxThresholdsForLux:dimTarget:brightenTarget:
+ _objc_msgSend$ceConfidenceThreshold
+ _objc_msgSend$ceModelID
+ _objc_msgSend$ceModule
+ _objc_msgSend$complete
+ _objc_msgSend$enableMitigationsForALSNode:
+ _objc_msgSend$exportedObjError:
+ _objc_msgSend$fixedLuxBrightenThresholds
+ _objc_msgSend$fixedLuxDimThresholds
+ _objc_msgSend$forceSILOff
+ _objc_msgSend$indexOfObject:
+ _objc_msgSend$initWithClient:andHandle:commitType:timeout:
+ _objc_msgSend$initWithID:serviceID:
+ _objc_msgSend$initWithQueue:displayID:andAODState:
+ _objc_msgSend$isColorMitigationTriggered
+ _objc_msgSend$isHighLuminanceAODActive
+ _objc_msgSend$policyFilter
+ _objc_msgSend$replaceEvent:withFilteredEvent:
+ _objc_msgSend$setAlsNode:
+ _objc_msgSend$setCeConfidenceThreshold:
+ _objc_msgSend$setCeModelID:
+ _objc_msgSend$setCeModule:
+ _objc_msgSend$setPolicyFilter:
+ _objc_msgSend$setProperties:
+ _objc_msgSend$setStats:
+ _objc_msgSend$stats
+ _objc_msgSend$wasDisconnected
- -[CBABModuleiOS shouldMitigateHarmony:]
- -[CBAODThresholdModule initWithQueue:andAODState:]
- -[CBBrightnessTransaction initWithClient:andHandle:commitType:]
- -[CBColorModuleShared enableMitigations:]
- -[CBDisplayContaineriOS setColorMitigations]
- -[CBIndicatorBrightnessModule shortcutRamp]
- GCC_except_table108
- GCC_except_table85
- GCC_except_table87
- _OBJC_IVAR_$_CBColorModuleShared._ceConfidenceThreshold
- _OBJC_IVAR_$_CBColorModuleShared._ceModelID
- _OBJC_IVAR_$_CBColorModuleShared._ceModule
- _OBJC_IVAR_$_CBColorModuleShared._confidenceEstimatorStats
- _OBJC_IVAR_$_CBColorModuleShared._enableMitigations
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ColorMitigationSupportProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_ColorMitigationSupportProtocol
- __OBJC_$_PROTOCOL_REFS_ColorMitigationSupportProtocol
- __OBJC_LABEL_PROTOCOL_$_ColorMitigationSupportProtocol
- __OBJC_PROTOCOL_$_ColorMitigationSupportProtocol
- ___41-[CBColorModuleShared enableMitigations:]_block_invoke
- _objc_msgSend$boostBrightness:forLux:
- _objc_msgSend$enableMitigations:
- _objc_msgSend$initWithClient:andHandle:commitType:
- _objc_msgSend$initWithID:
- _objc_msgSend$initWithQueue:andAODState:
- _objc_msgSend$removeObjectsInArray:
- _objc_msgSend$setBrightness:withCommitType:andError:
- _objc_msgSend$setColorMitigations
- _objc_msgSend$setFloatValue:forKey:
- _objc_msgSend$shortcutRamp
- _objc_msgSend$shouldMitigateHarmony:
CStrings:
+ "-[CBAODThresholdModule initWithQueue:displayID:andAODState:]"
+ "ALS event with orientation %d discarded by color filter."
+ "ALS event with orientation %d discarded by override filter."
+ "AODFixedLuxBrightenThresholds"
+ "AODFixedLuxDimThresholds"
+ "Brightness value outside of the valid range."
+ "Committing non-existing transaction."
+ "Error committing transaction %@"
+ "Fixed lux: brighten tightened %f -> %f"
+ "Fixed lux: dim tightened %f -> %f"
+ "IOReportCopyChannelsInGroup for group=%@ subgroup=%@ failed with error=%@"
+ "Invalid data type for Transaction. Commit is not an NSNumber."
+ "Invalid data type for Transaction. Expected dictionary."
+ "Invalid data type for Transaction. Missing uuid"
+ "Per-ALS CE: serviceID=%@ model=%u threshold=%f"
+ "Thermal Brightness"
+ "Transaction"
+ "Transaction already committed"
+ "Transaction committed successfully"
+ "Transaction is missing one of property/key/onCommit"
+ "Transaction was initiated with a different handle"
+ "[Color Mitigation] ALS event with orientation %d discarded by color mitigation filter."
+ "[Color Mitigation] ALS orientation=%d placement=%d triggered=%d filteredStrength=%f"
+ "[Color Mitigation] Aggregated mitigation: count=%lu anyTriggered=%d minFilteredStrength=%f"
+ "[Color Mitigation] CE stats collect: serviceID=%@ strengthCE=%f confidenceCE=%f"
+ "[New Event] MIB dcpRoleID mismatch! Expected: %d, Received: %d"
+ "com.apple.CoreBrightness.AOD.CBAODState.%lu"
+ "com.apple.CoreBrightness.AOD.ThresholdModule.%lu"
+ "com.apple.CoreBrightness.CBBrightnessTransaction"
+ "handle"
+ "key"
+ "onCommit"
+ "property"
+ "uuid"
- "-[CBAODThresholdModule initWithQueue:andAODState:]"
- "ALS event discarded."
- "Boosted %f * %f to %f at %flux"
- "CE Confidence threshold:%f"
- "CE Model being used:%d"
- "Thermal Brighntess"
- "com.apple.CoreBrightness.AOD.CBAODState"
- "com.apple.CoreBrightness.AOD.ThresholdModule"
```
