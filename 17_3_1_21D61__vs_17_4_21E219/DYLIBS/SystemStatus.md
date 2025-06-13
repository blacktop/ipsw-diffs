## SystemStatus

> `/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus`

```diff

-165.19.0.0.0
-  __TEXT.__text: 0x4d270
+165.115.0.0.0
+  __TEXT.__text: 0x4e2dc
   __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0x6ba8
+  __TEXT.__objc_methlist: 0x6d98
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x3414
+  __TEXT.__cstring: 0x346e
   __TEXT.__oslogstring: 0xedb
   __TEXT.__gcc_except_tab: 0x3c4
-  __TEXT.__unwind_info: 0x1d38
-  __TEXT.__objc_classname: 0x1773
-  __TEXT.__objc_methname: 0x975c
-  __TEXT.__objc_methtype: 0x1419
-  __TEXT.__objc_stubs: 0x5020
+  __TEXT.__unwind_info: 0x1da8
+  __TEXT.__objc_classname: 0x17d1
+  __TEXT.__objc_methname: 0x9938
+  __TEXT.__objc_methtype: 0x143f
+  __TEXT.__objc_stubs: 0x5200
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x1650
-  __DATA_CONST.__objc_classlist: 0x4f8
+  __DATA_CONST.__const: 0x1670
+  __DATA_CONST.__objc_classlist: 0x508
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1efd0
-  __DATA_CONST.__objc_selrefs: 0x1ac0
+  __DATA_CONST.__objc_const: 0x1f590
+  __DATA_CONST.__objc_selrefs: 0x1b40
+  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_classrefs: 0x4e8
+  __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__cfstring: 0x3e00
-  __AUTH_CONST.__objc_const: 0x4770
-  __AUTH_CONST.__const: 0x740
+  __AUTH_CONST.__cfstring: 0x3e80
+  __AUTH_CONST.__objc_const: 0x4890
+  __AUTH_CONST.__const: 0x780
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x330
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x4d0
-  __DATA.__objc_superrefs: 0x368
-  __DATA.__objc_ivar: 0x450
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x458
   __DATA.__data: 0xc18
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_ivar: 0x90
-  __DATA_DIRTY.__objc_data: 0x2f30
+  __DATA_DIRTY.__objc_ivar: 0x98
+  __DATA_DIRTY.__objc_data: 0x3020
   __DATA_DIRTY.__bss: 0x160
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 77268F38-C615-3A78-B35D-C2B7FA57362C
-  Functions: 2721
-  Symbols:   9642
-  CStrings:  2950
+  UUID: 81926B36-1F8F-3829-A70F-77BAE193710D
+  Functions: 2766
+  Symbols:   9785
+  CStrings:  2988
 
Symbols:
+ +[STMediaStatusDomainMicrophoneRecordingAttribution supportsSecureCoding]
+ +[STStatusBarData(NSDateInternal) dateFormatter]
+ +[STStatusBarData(NSDateInternal) shortTimeFormatter]
+ +[STStatusBarData(NSDateInternal) timeFormatter]
+ +[STStatusBarDataDateTimeEntry _entryForDateValue:mode:]
+ +[STStatusBarDataDateTimeEntry entryForDateWithDateValue:]
+ +[STStatusBarDataDateTimeEntry entryForShortTimeWithDateValue:]
+ +[STStatusBarDataDateTimeEntry entryForTimeWithDateValue:]
+ +[STStatusBarDataDateTimeEntry supportsBSXPCSecureCoding]
+ +[STStatusBarDataDateTimeEntry supportsSecureCoding]
+ -[STMediaStatusDomainData _initWithMicrophoneAttributionListData:mutedMicrophoneRecordingAttributionListData:systemAudioRecordingAttributionListData:cameraAttributionListData:]
+ -[STMediaStatusDomainData initWithMicrophoneAttributionListData:mutedMicrophoneRecordingAttributionListData:systemAudioRecordingAttributionListData:cameraAttributionListData:]
+ -[STMediaStatusDomainData microphoneAttributionListData]
+ -[STMediaStatusDomainData microphoneAttributions]
+ -[STMediaStatusDomainDataDiff initWithMicrophoneAttributionListDataDiff:mutedMicrophoneRecordingAttributionListDataDiff:systemAudioRecordingAttributionListDataDiff:cameraAttributionListDataDiff:]
+ -[STMediaStatusDomainMicrophoneRecordingAttribution .cxx_destruct]
+ -[STMediaStatusDomainMicrophoneRecordingAttribution activityAttribution]
+ -[STMediaStatusDomainMicrophoneRecordingAttribution copyWithZone:]
+ -[STMediaStatusDomainMicrophoneRecordingAttribution descriptionBuilderWithMultilinePrefix:]
+ -[STMediaStatusDomainMicrophoneRecordingAttribution descriptionWithMultilinePrefix:]
+ -[STMediaStatusDomainMicrophoneRecordingAttribution description]
+ -[STMediaStatusDomainMicrophoneRecordingAttribution encodeWithCoder:]
+ -[STMediaStatusDomainMicrophoneRecordingAttribution hash]
+ -[STMediaStatusDomainMicrophoneRecordingAttribution initWithActivityAttribution:]
+ -[STMediaStatusDomainMicrophoneRecordingAttribution initWithActivityAttribution:maximumHistoryAccessed:]
+ -[STMediaStatusDomainMicrophoneRecordingAttribution initWithCoder:]
+ -[STMediaStatusDomainMicrophoneRecordingAttribution isEqual:]
+ -[STMediaStatusDomainMicrophoneRecordingAttribution maximumHistoryAccessed]
+ -[STMediaStatusDomainMicrophoneRecordingAttribution succinctDescriptionBuilder]
+ -[STMediaStatusDomainMicrophoneRecordingAttribution succinctDescription]
+ -[STMutableMediaStatusDomainData addMicrophoneAttribution:]
+ -[STMutableMediaStatusDomainData initWithMicrophoneAttributionListData:mutedMicrophoneRecordingAttributionListData:systemAudioRecordingAttributionListData:cameraAttributionListData:]
+ -[STMutableMediaStatusDomainData microphoneAttributionListData]
+ -[STMutableMediaStatusDomainData removeMicrophoneAttribution:]
+ -[STMutableMediaStatusDomainData setMicrophoneAttributions:]
+ -[STStatusBarDataDateTimeEntry .cxx_destruct]
+ -[STStatusBarDataDateTimeEntry _equalsBuilderWithObject:]
+ -[STStatusBarDataDateTimeEntry _hashBuilder]
+ -[STStatusBarDataDateTimeEntry dateValue]
+ -[STStatusBarDataDateTimeEntry encodeWithBSXPCCoder:]
+ -[STStatusBarDataDateTimeEntry encodeWithCoder:]
+ -[STStatusBarDataDateTimeEntry initWithBSXPCCoder:]
+ -[STStatusBarDataDateTimeEntry initWithCoder:]
+ -[STStatusBarDataDateTimeEntry succinctDescriptionBuilder]
+ GCC_except_table41
+ _OBJC_CLASS_$_NSValue
+ _OBJC_CLASS_$_STMediaStatusDomainMicrophoneRecordingAttribution
+ _OBJC_CLASS_$_STStatusBarDataDateTimeEntry
+ _OBJC_IVAR_$_STMediaStatusDomainData._microphoneAttributionListData
+ _OBJC_IVAR_$_STMediaStatusDomainDataDiff._microphoneAttributionListDataDiff
+ _OBJC_IVAR_$_STMediaStatusDomainMicrophoneRecordingAttribution._activityAttribution
+ _OBJC_IVAR_$_STMediaStatusDomainMicrophoneRecordingAttribution._maximumHistoryAccessed
+ _OBJC_METACLASS_$_STMediaStatusDomainMicrophoneRecordingAttribution
+ _OBJC_METACLASS_$_STStatusBarDataDateTimeEntry
+ __OBJC_$_CLASS_METHODS_STMediaStatusDomainMicrophoneRecordingAttribution
+ __OBJC_$_CLASS_METHODS_STStatusBarData(NSDate|NSDateInternal)
+ __OBJC_$_CLASS_METHODS_STStatusBarDataDateTimeEntry
+ __OBJC_$_CLASS_PROP_LIST_STMediaStatusDomainMicrophoneRecordingAttribution
+ __OBJC_$_INSTANCE_METHODS_STMediaStatusDomainMicrophoneRecordingAttribution
+ __OBJC_$_INSTANCE_METHODS_STStatusBarData(NSDate|NSDateInternal)
+ __OBJC_$_INSTANCE_METHODS_STStatusBarDataDateTimeEntry
+ __OBJC_$_INSTANCE_VARIABLES_STMediaStatusDomainMicrophoneRecordingAttribution
+ __OBJC_$_INSTANCE_VARIABLES_STStatusBarDataDateTimeEntry
+ __OBJC_$_PROP_LIST_STMediaStatusDomainMicrophoneRecordingAttribution
+ __OBJC_$_PROP_LIST_STMutableStatusDomainDataChangeContext.90
+ __OBJC_$_PROP_LIST_STStatusBarDataDateTimeEntry
+ __OBJC_$_PROP_LIST_STStatusDomainDataChangeContext.82
+ __OBJC_CLASS_PROTOCOLS_$_STMediaStatusDomainMicrophoneRecordingAttribution
+ __OBJC_CLASS_RO_$_STMediaStatusDomainMicrophoneRecordingAttribution
+ __OBJC_CLASS_RO_$_STStatusBarDataDateTimeEntry
+ __OBJC_METACLASS_RO_$_STMediaStatusDomainMicrophoneRecordingAttribution
+ __OBJC_METACLASS_RO_$_STStatusBarDataDateTimeEntry
+ ___57-[STStatusBarDataDateTimeEntry _equalsBuilderWithObject:]_block_invoke
+ ___57-[STStatusBarDataDateTimeEntry _equalsBuilderWithObject:]_block_invoke_2
+ ___58-[STMediaStatusDomainData microphoneRecordingAttributions]_block_invoke
+ ___61-[STMediaStatusDomainMicrophoneRecordingAttribution isEqual:]_block_invoke
+ ___61-[STMediaStatusDomainMicrophoneRecordingAttribution isEqual:]_block_invoke_2
+ ___69-[STMutableMediaStatusDomainData setMicrophoneRecordingAttributions:]_block_invoke
+ ___91-[STMediaStatusDomainMicrophoneRecordingAttribution descriptionBuilderWithMultilinePrefix:]_block_invoke
+ ___block_descriptor_32_e59_16?0"STMediaStatusDomainMicrophoneRecordingAttribution"8l
+ ___block_literal_global.121
+ ___block_literal_global.124
+ ___block_literal_global.128
+ ___block_literal_global.13
+ ___block_literal_global.130
+ ___block_literal_global.132
+ ___block_literal_global.134
+ ___block_literal_global.153
+ ___block_literal_global.155
+ ___block_literal_global.735
+ _objc_msgSend$_entryForDateValue:mode:
+ _objc_msgSend$_initWithMicrophoneAttributionListData:mutedMicrophoneRecordingAttributionListData:systemAudioRecordingAttributionListData:cameraAttributionListData:
+ _objc_msgSend$addMicrophoneAttribution:
+ _objc_msgSend$dateFormatter
+ _objc_msgSend$dateValue
+ _objc_msgSend$entryForDateWithDateValue:
+ _objc_msgSend$entryForShortTimeWithDateValue:
+ _objc_msgSend$entryForTimeWithDateValue:
+ _objc_msgSend$initWithActivityAttribution:
+ _objc_msgSend$initWithActivityAttribution:maximumHistoryAccessed:
+ _objc_msgSend$initWithMicrophoneAttributionListData:mutedMicrophoneRecordingAttributionListData:systemAudioRecordingAttributionListData:cameraAttributionListData:
+ _objc_msgSend$initWithMicrophoneAttributionListDataDiff:mutedMicrophoneRecordingAttributionListDataDiff:systemAudioRecordingAttributionListDataDiff:cameraAttributionListDataDiff:
+ _objc_msgSend$integerValue
+ _objc_msgSend$maximumHistoryAccessed
+ _objc_msgSend$microphoneAttributionListData
+ _objc_msgSend$microphoneAttributions
+ _objc_msgSend$removeMicrophoneAttribution:
+ _objc_msgSend$setMicrophoneAttributions:
+ _objc_msgSend$shortTimeFormatter
+ _objc_msgSend$timeFormatter
- -[STMediaStatusDomainData _initWithMicrophoneRecordingAttributionListData:mutedMicrophoneRecordingAttributionListData:systemAudioRecordingAttributionListData:cameraAttributionListData:]
- -[STMediaStatusDomainData initWithMicrophoneRecordingAttributionListData:mutedMicrophoneRecordingAttributionListData:systemAudioRecordingAttributionListData:cameraAttributionListData:]
- -[STMediaStatusDomainData microphoneRecordingAttributionListData]
- -[STMediaStatusDomainDataDiff initWithMicrophoneRecordingAttributionListDataDiff:mutedMicrophoneRecordingAttributionListDataDiff:systemAudioRecordingAttributionListDataDiff:cameraAttributionListDataDiff:]
- -[STMutableMediaStatusDomainData initWithMicrophoneRecordingAttributionListData:mutedMicrophoneRecordingAttributionListData:systemAudioRecordingAttributionListData:cameraAttributionListData:]
- -[STMutableMediaStatusDomainData microphoneRecordingAttributionListData]
- GCC_except_table39
- _OBJC_IVAR_$_STMediaStatusDomainData._microphoneRecordingAttributionListData
- _OBJC_IVAR_$_STMediaStatusDomainDataDiff._microphoneRecordingAttributionListDataDiff
- __OBJC_$_CLASS_METHODS_STStatusBarData(NSDate)
- __OBJC_$_CLASS_PROP_LIST_STStatusBarData
- __OBJC_$_INSTANCE_METHODS_STStatusBarData(NSDate)
- __OBJC_$_PROP_LIST_STMutableStatusDomainDataChangeContext.89
- __OBJC_$_PROP_LIST_STStatusDomainDataChangeContext.81
- ___block_literal_global.120
- ___block_literal_global.123
- ___block_literal_global.127
- ___block_literal_global.129
- ___block_literal_global.131
- ___block_literal_global.133
- ___block_literal_global.147
- ___block_literal_global.702
- _objc_msgSend$_initWithMicrophoneRecordingAttributionListData:mutedMicrophoneRecordingAttributionListData:systemAudioRecordingAttributionListData:cameraAttributionListData:
- _objc_msgSend$entryWithStringValue:
- _objc_msgSend$initWithMicrophoneRecordingAttributionListData:mutedMicrophoneRecordingAttributionListData:systemAudioRecordingAttributionListData:cameraAttributionListData:
- _objc_msgSend$initWithMicrophoneRecordingAttributionListDataDiff:mutedMicrophoneRecordingAttributionListDataDiff:systemAudioRecordingAttributionListDataDiff:cameraAttributionListDataDiff:
- _objc_msgSend$microphoneRecordingAttributionListData
CStrings:
+ "@\"NSDate\""
+ "@16@?0@\"STMediaStatusDomainMicrophoneRecordingAttribution\"8"
+ "@32@0:8@16d24"
+ "@32@0:8@16q24"
+ "NSDateInternal"
+ "STMediaStatusDomainMicrophoneRecordingAttribution"
+ "STStatusBarDataDateTimeEntry"
+ "T@\"NSDate\",R,C,N,V_dateValue"
+ "T@\"NSDateFormatter\",R,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"STListData\",R,C,N,V_microphoneAttributionListData"
+ "Td,R,N,V_maximumHistoryAccessed"
+ "_dateValue"
+ "_entryForDateValue:mode:"
+ "_initWithMicrophoneAttributionListData:mutedMicrophoneRecordingAttributionListData:systemAudioRecordingAttributionListData:cameraAttributionListData:"
+ "_maximumHistoryAccessed"
+ "_microphoneAttributionListData"
+ "_microphoneAttributionListDataDiff"
+ "_mode"
+ "addMicrophoneAttribution:"
+ "dateFormatter"
+ "dateValue"
+ "entryForDateWithDateValue:"
+ "entryForShortTimeWithDateValue:"
+ "entryForTimeWithDateValue:"
+ "initWithActivityAttribution:"
+ "initWithActivityAttribution:maximumHistoryAccessed:"
+ "initWithMicrophoneAttributionListData:mutedMicrophoneRecordingAttributionListData:systemAudioRecordingAttributionListData:cameraAttributionListData:"
+ "initWithMicrophoneAttributionListDataDiff:mutedMicrophoneRecordingAttributionListDataDiff:systemAudioRecordingAttributionListDataDiff:cameraAttributionListDataDiff:"
+ "integerValue"
+ "maximumHistoryAccessed"
+ "microphoneAttributionListData"
+ "microphoneAttributionListDataDiff"
+ "microphoneAttributions"
+ "mode"
+ "modeValue"
+ "removeMicrophoneAttribution:"
+ "setMicrophoneAttributions:"
+ "shortTimeFormatter"
+ "timeFormatter"
- "T@\"STListData\",R,C,N,V_microphoneRecordingAttributionListData"
- "_initWithMicrophoneRecordingAttributionListData:mutedMicrophoneRecordingAttributionListData:systemAudioRecordingAttributionListData:cameraAttributionListData:"
- "_microphoneRecordingAttributionListData"
- "_microphoneRecordingAttributionListDataDiff"
- "initWithMicrophoneRecordingAttributionListData:mutedMicrophoneRecordingAttributionListData:systemAudioRecordingAttributionListData:cameraAttributionListData:"
- "initWithMicrophoneRecordingAttributionListDataDiff:mutedMicrophoneRecordingAttributionListDataDiff:systemAudioRecordingAttributionListDataDiff:cameraAttributionListDataDiff:"
- "microphoneRecordingAttributionListData"
- "microphoneRecordingAttributionListDataDiff"

```
