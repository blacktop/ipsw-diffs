## AGXGPURawCounter

> `/System/Library/PrivateFrameworks/AGXGPURawCounter.framework/Versions/A/AGXGPURawCounter`

```diff

-324.6.0.0.0
-  __TEXT.__text: 0xdeac
-  __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__const: 0x208
-  __TEXT.__gcc_except_tab: 0x480
-  __TEXT.__cstring: 0x3d58
+325.34.1.0.0
+  __TEXT.__text: 0xed8c
+  __TEXT.__auth_stubs: 0x3e0
+  __TEXT.__const: 0x1a8
+  __TEXT.__gcc_except_tab: 0x5fc
+  __TEXT.__cstring: 0x3e05
   __TEXT.__oslogstring: 0x1f52
-  __TEXT.__unwind_info: 0x218
-  __TEXT.__objc_methname: 0xcc
-  __TEXT.__objc_stubs: 0x160
-  __DATA_CONST.__got: 0x38
-  __DATA_CONST.__const: 0x360
+  __TEXT.__unwind_info: 0x260
+  __TEXT.__objc_classname: 0x1
+  __TEXT.__objc_methname: 0x131
+  __TEXT.__objc_stubs: 0x200
+  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__const: 0x380
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x58
+  __DATA_CONST.__objc_selrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0x1e8
-  __AUTH_CONST.__const: 0x6d8
-  __AUTH_CONST.__cfstring: 0x840
+  __AUTH_CONST.__auth_got: 0x200
+  __AUTH_CONST.__const: 0x7a0
+  __AUTH_CONST.__cfstring: 0x8c0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __DATA.__data: 0x1c3

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BB5D8704-FF60-349C-AD4D-8E210631C873
-  Functions: 138
-  Symbols:   288
-  CStrings:  411
+  UUID: C65EB780-BD2A-38E2-A9F1-89B2EF5E1F28
+  Functions: 146
+  Symbols:   317
+  CStrings:  429
 
Symbols:
+ GCC_except_table100
+ GCC_except_table109
+ GCC_except_table137
+ GCC_except_table79
+ GCC_except_table81
+ GCC_except_table91
+ GCC_except_table92
+ GCC_except_table95
+ GCC_except_table98
+ _ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.103
+ _ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.110
+ _ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.77
+ _ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.81
+ _ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.87
+ _ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.91
+ _ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.97
+ __NSConcreteStackBlock
+ __ZN20AGXGPURawCounterImpl13SourceAPSImpl21setOptionsPerUSCMasksEP12NSDictionary
+ ____ZN20AGXGPURawCounterImpl13SourceAPSImpl10addTriggerEN16AGXGPURawCounter11TriggerTypeEP12NSDictionary_block_invoke
+ ____ZN20AGXGPURawCounterImpl13SourceAPSImpl10addTriggerEN16AGXGPURawCounter11TriggerTypeEP12NSDictionary_block_invoke_2
+ ____ZN20AGXGPURawCounterImpl13SourceAPSImpl10setOptionsEP12NSDictionary_block_invoke
+ ____ZN20AGXGPURawCounterImpl13SourceAPSImpl10setOptionsEP12NSDictionary_block_invoke_2
+ ____ZN20AGXGPURawCounterImpl13SourceAPSImpl20fillKernelConfigDataEP28AGXSPerfCtrSamplerControlRec_block_invoke
+ ___block_descriptor_44_ea8_32s_e45_"NSNumber"24?0"NSString"8"NSDictionary"16l
+ ___block_descriptor_48_e8_v12?0i8l
+ ___block_descriptor_52_ea8_32s40s_e28_"NSNumber"16?0"NSString"8l
+ ___block_descriptor_56_ea8_32s40s_e8_v12?0i8l
+ ___block_descriptor_60_ea8_32s40s_e8_B12?0i8l
+ ___copy_helper_block_ea8_32s
+ ___copy_helper_block_ea8_32s40s
+ ___destroy_helper_block_ea8_32s
+ ___destroy_helper_block_ea8_32s40s
+ _objc_autoreleaseReturnValue
+ _objc_enumerationMutation
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$intValue
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$unsignedIntValue
+ _objc_retainBlock
- GCC_except_table127
- GCC_except_table89
- GCC_except_table90
- _ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.62
- _ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.66
- _ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.72
- _ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.76
- _ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.82
- _ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.88
- _ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.95
- ___chkstk_darwin
CStrings:
+ "@\"NSNumber\"16@?0@\"NSString\"8"
+ "@\"NSNumber\"24@?0@\"NSString\"8@\"NSDictionary\"16"
+ "B12@?0i8"
+ "USCConfigOverride"
+ "USCMaskForMGPU"
+ "USCNumPerMGPU"
+ "addTrigger_block_invoke"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "intValue"
+ "mGPUMask"
+ "objectAtIndexedSubscript:"
+ "unsignedIntValue"
+ "v12@?0i8"

```
