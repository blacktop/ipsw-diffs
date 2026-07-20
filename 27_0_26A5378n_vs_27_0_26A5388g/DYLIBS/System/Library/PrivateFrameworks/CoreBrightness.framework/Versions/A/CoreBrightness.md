## CoreBrightness

> `/System/Library/PrivateFrameworks/CoreBrightness.framework/Versions/A/CoreBrightness`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-2300.0.10.0.1
-  __TEXT.__text: 0x15fbf8
-  __TEXT.__objc_methlist: 0xd02c
-  __TEXT.__cstring: 0xcada
-  __TEXT.__const: 0x138d0
-  __TEXT.__gcc_except_tab: 0x1f10
-  __TEXT.__oslogstring: 0x1816a
+2300.0.18.0.0
+  __TEXT.__text: 0x1616b8
+  __TEXT.__objc_methlist: 0xd17c
+  __TEXT.__cstring: 0xcc95
+  __TEXT.__const: 0x13900
+  __TEXT.__gcc_except_tab: 0x1f88
+  __TEXT.__oslogstring: 0x183cd
   __TEXT.__dlopen_cstrs: 0x10d
-  __TEXT.__swift5_typeref: 0xeb0
-  __TEXT.__constg_swiftt: 0xc2c
-  __TEXT.__swift5_reflstr: 0xa3c
+  __TEXT.__swift5_typeref: 0xeaf
+  __TEXT.__constg_swiftt: 0xc34
+  __TEXT.__swift5_reflstr: 0xa4e
   __TEXT.__swift5_assocty: 0x288
   __TEXT.__swift5_fieldmd: 0x100c
   __TEXT.__swift5_builtin: 0xdc

   __TEXT.__swift5_proto: 0x308
   __TEXT.__swift5_types: 0x120
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x5290
+  __TEXT.__unwind_info: 0x52d0
   __TEXT.__eh_frame: 0xb88
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1190
-  __DATA_CONST.__objc_classlist: 0x6d8
-  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__const: 0x11c8
+  __DATA_CONST.__objc_classlist: 0x6e0
+  __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x330
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x5590
+  __DATA_CONST.__objc_selrefs: 0x5638
   __DATA_CONST.__objc_protorefs: 0x130
-  __DATA_CONST.__objc_superrefs: 0x5a0
+  __DATA_CONST.__objc_superrefs: 0x5a8
   __DATA_CONST.__objc_arraydata: 0xba0
-  __DATA_CONST.__got: 0x768
+  __DATA_CONST.__got: 0x760
   __AUTH_CONST.__const: 0x5880
-  __AUTH_CONST.__cfstring: 0xe3a0
-  __AUTH_CONST.__objc_const: 0x33648
+  __AUTH_CONST.__cfstring: 0xe540
+  __AUTH_CONST.__objc_const: 0x33968
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0xcf0
   __AUTH_CONST.__objc_floatobj: 0x180
-  __AUTH_CONST.__objc_arrayobj: 0x2b8
-  __AUTH_CONST.__objc_dictobj: 0x5f0
   __AUTH_CONST.__objc_doubleobj: 0x40
+  __AUTH_CONST.__objc_dictobj: 0x5f0
+  __AUTH_CONST.__objc_arrayobj: 0x2b8
   __AUTH_CONST.__auth_got: 0x1278
-  __AUTH.__objc_data: 0x2590
-  __AUTH.__data: 0x628
-  __DATA.__objc_ivar: 0x1708
+  __AUTH.__objc_data: 0x25e0
+  __AUTH.__data: 0x630
+  __DATA.__objc_ivar: 0x1730
   __DATA.__data: 0x5a670
   __DATA.__bss: 0x63e0
   __DATA.__common: 0x10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8120
-  Symbols:   12680
-  CStrings:  4608
+  Functions: 8150
+  Symbols:   12759
+  CStrings:  4631
 
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
+ -[CBBrightnessTransaction _completeWithError:]
+ -[CBBrightnessTransaction _setBrightness:withError:]
+ -[CBBrightnessTransaction complete]
+ -[CBBrightnessTransaction initWithClient:andHandle:commitType:timeout:]
+ -[CBColorModuleShared enableMitigationsForALSNode:]
+ -[CBColorModuleShared replaceEvent:withFilteredEvent:]
+ -[CBColorPolicyFilter initWithID:serviceID:]
+ -[CBDisplayBrightnessClient newBrightnessAdjustmentWithError:]
+ -[CBDynamicSlider enabled]
+ -[CBDynamicSlider setEnabled:]
+ -[CBIndicatorBrightnessModule forceSILOff]
+ GCC_except_table104
+ GCC_except_table108
+ GCC_except_table136
+ GCC_except_table198
+ GCC_except_table235
+ GCC_except_table250
+ GCC_except_table37
+ GCC_except_table44
+ GCC_except_table45
+ OBJC_IVAR_$_BacklightdExportedObj._transactions
+ OBJC_IVAR_$_CBALSMitigationState._alsNode
+ OBJC_IVAR_$_CBALSMitigationState._ceConfidenceThreshold
+ OBJC_IVAR_$_CBALSMitigationState._ceModelID
+ OBJC_IVAR_$_CBALSMitigationState._ceModule
+ OBJC_IVAR_$_CBALSMitigationState._policyFilter
+ OBJC_IVAR_$_CBALSMitigationState._stats
+ OBJC_IVAR_$_CBBrightnessTransaction._logHandle
+ OBJC_IVAR_$_CBBrightnessTransaction._timeout
+ OBJC_IVAR_$_CBBrightnessTransaction._timer
+ OBJC_IVAR_$_CBColorModuleShared._alsMitigationState
+ OBJC_IVAR_$_CBColorModuleShared._anyMitigationEnabled
+ OBJC_IVAR_$_CBColorModuleShared._overrideFilters
+ OBJC_IVAR_$_CBColorPolicyFilter._serviceID
+ OBJC_IVAR_$_CBDynamicSlider._enabled
+ _OBJC_CLASS_$_CBALSMitigationState
+ _OBJC_METACLASS_$_CBALSMitigationState
+ __51-[CBColorModuleShared enableMitigationsForALSNode:]_block_invoke
+ __66-[BrightnessSystemClientInternal copyPropertyForKey:handle:error:]_block_invoke_2
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
+ _objc_msgSend$ceConfidenceThreshold
+ _objc_msgSend$ceModel
+ _objc_msgSend$ceModelID
+ _objc_msgSend$ceModule
+ _objc_msgSend$ceThreshold
+ _objc_msgSend$colorMitigation
+ _objc_msgSend$complete
+ _objc_msgSend$exportedObjError:
+ _objc_msgSend$forceSILOff
+ _objc_msgSend$handleAABStateChange:immediate:
+ _objc_msgSend$handleDisablement:immediate:
+ _objc_msgSend$indexOfObject:
+ _objc_msgSend$initWithClient:andHandle:commitType:timeout:
+ _objc_msgSend$initWithID:serviceID:
+ _objc_msgSend$isColorMitigationTriggered
+ _objc_msgSend$policyFilter
+ _objc_msgSend$replaceEvent:withFilteredEvent:
+ _objc_msgSend$setAlsNode:
+ _objc_msgSend$setCeConfidenceThreshold:
+ _objc_msgSend$setCeModelID:
+ _objc_msgSend$setCeModule:
+ _objc_msgSend$setPolicyFilter:
+ _objc_msgSend$setStats:
+ _objc_msgSend$stats
+ _objc_msgSend$wasDisconnected
- -[CBBrightnessTransaction initWithClient:andHandle:commitType:]
- -[CBColorModuleShared enableMitigations:]
- -[CBIndicatorBrightnessModule shortcutRamp]
- GCC_except_table122
- GCC_except_table196
- GCC_except_table233
- GCC_except_table248
- GCC_except_table41
- GCC_except_table88
- GCC_except_table94
- OBJC_IVAR_$_CBColorModuleShared._ceConfidenceThreshold
- OBJC_IVAR_$_CBColorModuleShared._ceModelID
- OBJC_IVAR_$_CBColorModuleShared._ceModule
- OBJC_IVAR_$_CBColorModuleShared._confidenceEstimatorStats
- OBJC_IVAR_$_CBColorModuleShared._enableMitigations
- __41-[CBColorModuleShared enableMitigations:]_block_invoke
- __66-[BrightnessSystemClientInternal copyPropertyForKey:handle:error:]_block_invoke
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ColorMitigationSupportProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_ColorMitigationSupportProtocol
- __OBJC_$_PROTOCOL_REFS_ColorMitigationSupportProtocol
- __OBJC_LABEL_PROTOCOL_$_ColorMitigationSupportProtocol
- __OBJC_PROTOCOL_$_ColorMitigationSupportProtocol
- ___41-[CBColorModuleShared enableMitigations:]_block_invoke
- _objc_msgSend$handleAABStateChange:
- _objc_msgSend$initWithClient:andHandle:commitType:
- _objc_msgSend$initWithID:
- _objc_msgSend$removeObjectsInArray:
- _objc_msgSend$setBrightness:withCommitType:andError:
- _objc_msgSend$shortcutRamp
CStrings:
+ "ALS event with orientation %d discarded by color filter."
+ "ALS event with orientation %d discarded by override filter."
+ "Brightness value outside of the valid range."
+ "Committing non-existing transaction."
+ "Error committing transaction %@"
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
+ "com.apple.CoreBrightness.CBBrightnessTransaction"
+ "handle"
+ "key"
+ "onCommit"
+ "property"
+ "uuid"
- "ALS event discarded."
- "Boosted %f * %f to %f at %flux"
- "Thermal Brighntess"
```
