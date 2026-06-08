## AGXGPURawCounter

> `/System/Library/PrivateFrameworks/AGXGPURawCounter.framework/AGXGPURawCounter`

```diff

-351.1.0.0.0
-  __TEXT.__text: 0xef94
-  __TEXT.__auth_stubs: 0x470
-  __TEXT.__const: 0x1e4
-  __TEXT.__gcc_except_tab: 0x624
-  __TEXT.__cstring: 0x3f95
-  __TEXT.__oslogstring: 0x20ac
-  __TEXT.__unwind_info: 0x258
-  __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x14d
-  __TEXT.__objc_stubs: 0x220
-  __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0x420
+360.27.0.0.0
+  __TEXT.__text: 0xf670
+  __TEXT.__const: 0x200
+  __TEXT.__gcc_except_tab: 0x598
+  __TEXT.__cstring: 0x400d
+  __TEXT.__oslogstring: 0x2060
+  __TEXT.__unwind_info: 0x288
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
+  __DATA_CONST.__const: 0x460
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x88
+  __DATA_CONST.__objc_selrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0x248
-  __AUTH_CONST.__const: 0x760
-  __AUTH_CONST.__cfstring: 0x920
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x800
+  __AUTH_CONST.__cfstring: 0x9a0
+  __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x270
   __DATA.__data: 0x1f3
-  __DATA.__bss: 0x6f8
+  __DATA.__bss: 0x7c8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 918592F4-58F0-36E7-96D1-4266C710265A
-  Functions: 148
-  Symbols:   478
-  CStrings:  440
+  UUID: EFB2C609-EBF5-360D-B1E2-F5705293B5F5
+  Functions: 165
+  Symbols:   523
+  CStrings:  437
 
Symbols:
+ GCC_except_table106
+ GCC_except_table108
+ GCC_except_table109
+ GCC_except_table110
+ GCC_except_table111
+ GCC_except_table124
+ GCC_except_table152
+ GCC_except_table35
+ GCC_except_table37
+ GCC_except_table42
+ GCC_except_table59
+ GCC_except_table71
+ GCC_except_table72
+ _CFArrayApplyFunction
+ _CFDictionaryApplyFunction
+ _CFDictionaryGetCount
+ _CFStringGetCStringPtr
+ __Z30perfCtrSamplerAddSourceCounterjPKN20AGXGPURawCounterImpl15CounterDescImplEjjj
+ __ZN20AGXGPURawCounterImpl10SourceImpl10addCounterERN16AGXGPURawCounter14CounterReqDescE
+ __ZN20AGXGPURawCounterImpl10SourceImpl12resetOptionsEv
+ __ZN20AGXGPURawCounterImpl12resetOptionsEv
+ __ZN20AGXGPURawCounterImpl13SourceAPSImpl12resetOptionsEv
+ __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.101
+ __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.108
+ __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.68
+ __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.72
+ __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.78
+ __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.82
+ __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.88
+ __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.94
+ __ZNK20AGXGPURawCounterImpl10SourceImpl13getSourceTypeEv
+ __ZNK20AGXGPURawCounterImpl10SourceImpl18addEventSelectListERN16AGXGPURawCounter14CounterReqDescEy
+ __ZNK20AGXGPURawCounterImpl10SourceImpl21getEventSelectsNumMaxEPKc
+ __ZNK20AGXGPURawCounterImpl13SourceAPSImpl18addEventSelectListERN16AGXGPURawCounter14CounterReqDescEy
+ __ZNK20AGXGPURawCounterImpl13SourceAPSImpl21getEventSelectsNumMaxEPKc
+ __ZNSt3__122__libcpp_verbose_abortEPKcz
+ __ZNSt3__127__throw_bad_optional_accessB9fqn220100Ev
+ __ZZN20AGXGPURawCounterImpl10SourceImpl10addCounterERN16AGXGPURawCounter14CounterReqDescEE18uscProfileDataName
+ __ZZN20AGXGPURawCounterImpl4initEjEN3$_08__invokeEPKvPv
+ __ZZN20AGXGPURawCounterImpl4initEjEN3$_18__invokeEPKvPv
+ __ZZN20AGXGPURawCounterImpl4initEjEN3$_28__invokeEPKvPv
+ __ZZN20AGXGPURawCounterImpl4initEjEN3$_38__invokeEPKvS2_Pv
+ __ZZN20AGXGPURawCounterImpl4initEjEN3$_48__invokeEPKvS2_Pv
+ __ZZN20AGXGPURawCounterImpl4initEjENK3$_5clEv
+ __ZZN20AGXGPURawCounterImpl4initEjENK3$_6clEv
+ ____ZN20AGXGPURawCounterImpl10SourceImpl10addCounterERN16AGXGPURawCounter14CounterReqDescE_block_invoke
+ ____ZNK20AGXGPURawCounterImpl13SourceAPSImpl18addEventSelectListERN16AGXGPURawCounter14CounterReqDescEy_block_invoke
+ ____ZNK20AGXGPURawCounterImpl13SourceAPSImpl21getEventSelectsNumMaxEPKc_block_invoke
+ ___block_literal_global.141
+ ___block_literal_global.2
+ ___block_literal_global.57
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$unsignedCharValue
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
+ _objc_storeStrong
- GCC_except_table135
- GCC_except_table26
- GCC_except_table34
- GCC_except_table36
- GCC_except_table51
- GCC_except_table61
- GCC_except_table67
- GCC_except_table81
- GCC_except_table83
- GCC_except_table94
- GCC_except_table96
- GCC_except_table97
- GCC_except_table98
- __Z24obfuscatedUSCProfileNamejj
- __Z30perfCtrSamplerAddSourceCounterjPKN20AGXGPURawCounterImpl15CounterDescImplEjj
- __ZN20AGXGPURawCounterImpl10SourceImpl10addCounterEPKcjjy
- __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.105
- __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.112
- __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.119
- __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.79
- __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.83
- __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.89
- __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.93
- __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.99
- __ZZN20AGXGPURawCounterImpl10SourceImpl10addCounterEPKcjjyE18uscProfileDataName
- ____ZN20AGXGPURawCounterImpl10SourceImpl10addCounterEPKcjjy_block_invoke
- ___block_literal_global.153
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x23
CStrings:
+ "AGXGRC:%s:%d:%s: *** \"(_partitionInfoList[index].optInfo = (OptionalPartitionInfo*)malloc(sizeof(OptionalPartitionInfo))) != NULL\"\n"
+ "AGXGRC:%s:%d:%s: *** \"(counterDesc.nameLen >= 2) && (counterDesc.descriptionLen >= 2)\"\n"
+ "AGXGRC:%s:%d:%s: *** \"CFNumberGetValue(cfEventSelectsNumMax, kCFNumberSInt32Type, &eventSelectsNumMax)\"\n"
+ "AGXGRC:%s:%d:%s: *** \"buildMasterCounterListFinalize()\"\n"
+ "AGXGRC:%s:%d:%s: *** \"buildMasterCounterListInitialize()\"\n"
+ "AGXGRC:%s:%d:%s: *** \"ret && (perfCtrIdx != 0) && (sourceMaskAll != 0)\"\n"
+ "AGXGRC:%s:%d:%s: *** Cannot add user-defined counter (%s) using GPURawCounter internal partition!\n"
+ "AGXGRC:%s:%d:%s: *** Counter width must be 16, 32, 48, or 64!\n"
+ "AGXGRC:%s:%d:%s: *** Counter width must be <= 32 as \"%s\" has only 32 valid bits\n"
+ "AGXGRC:%s:%d:%s: *** Failed to reserve pre-determined counterDesc space from allocator!\n"
+ "AGXGRC:%s:%d:%s: *** Failed to retrieve dictionary info for perf counter '%s'\n"
+ "AGXGRC:%s:%d:%s: *** Selectable events must be specified via the EventSelect array option\n"
+ "AGXGRC:AGXGRC:%s:%d:%s: *** \"(_partitionInfoList[index].optInfo = (OptionalPartitionInfo*)malloc(sizeof(OptionalPartitionInfo))) != NULL\"\n"
+ "AGXGRC:AGXGRC:%s:%d:%s: *** \"(counterDesc.nameLen >= 2) && (counterDesc.descriptionLen >= 2)\"\n"
+ "AGXGRC:AGXGRC:%s:%d:%s: *** \"CFNumberGetValue(cfEventSelectsNumMax, kCFNumberSInt32Type, &eventSelectsNumMax)\"\n"
+ "AGXGRC:AGXGRC:%s:%d:%s: *** \"buildMasterCounterListFinalize()\"\n"
+ "AGXGRC:AGXGRC:%s:%d:%s: *** \"buildMasterCounterListInitialize()\"\n"
+ "AGXGRC:AGXGRC:%s:%d:%s: *** \"ret && (perfCtrIdx != 0) && (sourceMaskAll != 0)\"\n"
+ "AGXGRC:AGXGRC:%s:%d:%s: *** Cannot add user-defined counter (%s) using GPURawCounter internal partition!\n"
+ "AGXGRC:AGXGRC:%s:%d:%s: *** Counter width must be 16, 32, 48, or 64!\n"
+ "AGXGRC:AGXGRC:%s:%d:%s: *** Counter width must be <= 32 as \"%s\" has only 32 valid bits\n"
+ "AGXGRC:AGXGRC:%s:%d:%s: *** Failed to reserve pre-determined counterDesc space from allocator!\n"
+ "AGXGRC:AGXGRC:%s:%d:%s: *** Failed to retrieve dictionary info for perf counter '%s'\n"
+ "AGXGRC:AGXGRC:%s:%d:%s: *** Selectable events must be specified via the EventSelect array option\n"
+ "DeviceAPSEventSelects"
+ "DisablePowerOff"
+ "ReadThreshold"
+ "Unknown"
+ "bad_optional_access was thrown in -fno-exceptions mode"
+ "event_selects_num_max_list"
+ "operator()"
+ "virtual void AGXGPURawCounterImpl::resetOptions()"
- "AGXGRC:%s:%d:%s: *** \"(cfPerfCtrFlag == NULL) || CFNumberGetValue(cfPerfCtrFlag, kCFNumberSInt32Type, &perfCtrFlag)\"\n"
- "AGXGRC:%s:%d:%s: *** \"(cfPerfCtrInfo != NULL) && (cfPerfCtrPartition != NULL) && (cfPerfCtrSelect != NULL) && (cfPerfCtrDesc != NULL)\"\n"
- "AGXGRC:%s:%d:%s: *** \"(counterDesc.description = (char*)(allocator.reserve(counterDesc.descriptionLen + 1))) != NULL\"\n"
- "AGXGRC:%s:%d:%s: *** \"(counterDesc.name = (char*)(allocator.reserve(counterDesc.nameLen + 1))) != NULL\"\n"
- "AGXGRC:%s:%d:%s: *** \"(perfCtrIdx != 0) && (sourceMaskAll != 0)\"\n"
- "AGXGRC:%s:%d:%s: *** \"CFNumberGetValue(cfPerfCtrPartition, kCFNumberSInt32Type, &perfCtrPartition) && (perfCtrPartition < _partitionInfoNum)\"\n"
- "AGXGRC:%s:%d:%s: *** Cannot add user defined counter (%s) using GPURawCounter internal partition!\n"
- "AGXGRC:%s:%d:%s: *** Cannot add user defined counter (%s)! Both partition (0x%x) and select (0x%llx) must be specified!\n"
- "AGXGRC:%s:%d:%s: *** counterName cannot be NULL!\n"
- "AGXGRC:%s:%d:%s: *** counterWidth must be 16, 32, 48, or 64!\n"
- "AGXGRC:%s:%d:%s: *** counterWidth must be <= 32 as \"%s\" has only 32 valid bits\n"
- "AGXGRC:AGXGRC:%s:%d:%s: *** \"(cfPerfCtrFlag == NULL) || CFNumberGetValue(cfPerfCtrFlag, kCFNumberSInt32Type, &perfCtrFlag)\"\n"
- "AGXGRC:AGXGRC:%s:%d:%s: *** \"(cfPerfCtrInfo != NULL) && (cfPerfCtrPartition != NULL) && (cfPerfCtrSelect != NULL) && (cfPerfCtrDesc != NULL)\"\n"
- "AGXGRC:AGXGRC:%s:%d:%s: *** \"(counterDesc.description = (char*)(allocator.reserve(counterDesc.descriptionLen + 1))) != NULL\"\n"
- "AGXGRC:AGXGRC:%s:%d:%s: *** \"(counterDesc.name = (char*)(allocator.reserve(counterDesc.nameLen + 1))) != NULL\"\n"
- "AGXGRC:AGXGRC:%s:%d:%s: *** \"(perfCtrIdx != 0) && (sourceMaskAll != 0)\"\n"
- "AGXGRC:AGXGRC:%s:%d:%s: *** \"CFNumberGetValue(cfPerfCtrPartition, kCFNumberSInt32Type, &perfCtrPartition) && (perfCtrPartition < _partitionInfoNum)\"\n"
- "AGXGRC:AGXGRC:%s:%d:%s: *** Cannot add user defined counter (%s) using GPURawCounter internal partition!\n"
- "AGXGRC:AGXGRC:%s:%d:%s: *** Cannot add user defined counter (%s)! Both partition (0x%x) and select (0x%llx) must be specified!\n"
- "AGXGRC:AGXGRC:%s:%d:%s: *** counterName cannot be NULL!\n"
- "AGXGRC:AGXGRC:%s:%d:%s: *** counterWidth must be 16, 32, 48, or 64!\n"
- "AGXGRC:AGXGRC:%s:%d:%s: *** counterWidth must be <= 32 as \"%s\" has only 32 valid bits\n"
- "UTF8String"
- "boolValue"
- "bundleWithPath:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "intValue"
- "numberWithUnsignedInt:"
- "numberWithUnsignedLongLong:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "pathForResource:ofType:"
- "setObject:forKeyedSubscript:"
- "shortValue"
- "stringWithFormat:"
- "unsignedIntValue"
- "unsignedLongValue"
- "unsignedShortValue"

```
