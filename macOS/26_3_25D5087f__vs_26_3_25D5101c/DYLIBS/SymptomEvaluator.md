## SymptomEvaluator

> `/System/Library/PrivateFrameworks/Symptoms.framework/Versions/A/Frameworks/SymptomEvaluator.framework/Versions/A/SymptomEvaluator`

```diff

-2158.80.9.0.0
-  __TEXT.__text: 0x1e7b28
+2158.80.10.0.0
+  __TEXT.__text: 0x1e7d18
   __TEXT.__auth_stubs: 0x25c0
-  __TEXT.__objc_methlist: 0x11374
-  __TEXT.__cstring: 0x1a618
+  __TEXT.__objc_methlist: 0x1137c
+  __TEXT.__cstring: 0x1a628
   __TEXT.__const: 0xc82
   __TEXT.__oslogstring: 0x288ef
   __TEXT.__gcc_except_tab: 0x35c8

   __TEXT.__swift_as_entry: 0x3c
   __TEXT.__swift_as_ret: 0x60
   __TEXT.evaluator_cfg: 0x647c
-  __TEXT.__unwind_info: 0x50a8
+  __TEXT.__unwind_info: 0x50b0
   __TEXT.__eh_frame: 0x698
   __TEXT.__objc_classname: 0x167a
-  __TEXT.__objc_methname: 0x29efc
-  __TEXT.__objc_methtype: 0x4dd7
-  __TEXT.__objc_stubs: 0x18020
+  __TEXT.__objc_methname: 0x29f29
+  __TEXT.__objc_methtype: 0x4ddd
+  __TEXT.__objc_stubs: 0x18040
   __DATA_CONST.__got: 0xbe0
   __DATA_CONST.__const: 0x2b78
   __DATA_CONST.__objc_classlist: 0x6a0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9678
+  __DATA_CONST.__objc_selrefs: 0x9680
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x448
   __DATA_CONST.__objc_arraydata: 0xc8
   __AUTH_CONST.__auth_got: 0x12f8
   __AUTH_CONST.__const: 0x4d40
-  __AUTH_CONST.__cfstring: 0x14ec0
-  __AUTH_CONST.__objc_const: 0x2a538
+  __AUTH_CONST.__cfstring: 0x14ee0
+  __AUTH_CONST.__objc_const: 0x2a568
   __AUTH_CONST.__objc_intobj: 0x600
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x1060
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x1c98
+  __DATA.__objc_ivar: 0x1c9c
   __DATA.__data: 0x17e8
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xe38

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 0915C1A2-7335-30D4-8C25-62B6F4873BA3
-  Functions: 8827
-  Symbols:   18746
-  CStrings:  19073
+  UUID: CF2A22FD-E80D-387B-95E3-F2F988BE3E7F
+  Functions: 8828
+  Symbols:   18749
+  CStrings:  19078
 
Symbols:
+ -[DataStallHandler processStall:procName:endpoint:foreground:interfaceType:stallType:silent:]
+ -[TimedEndpoint initWithEndpoint:trigger:interfaceType:stallType:foreground:silent:]
+ -[TimedEndpoint silent]
+ GCC_except_table28
+ OBJC_IVAR_$_TimedEndpoint._silent
+ ___block_descriptor_109_e8_32s40s48s56s64s72bs_e20_v20?0B8"NSError"12l
+ ___block_descriptor_109_e8_32s40s48s56s64s72bs_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e104_v88?0"NSString"8"NSString"16i24i28"NSString"32"NSString"40Q48"NSNumber"56i64i68i72"NSString"76B84l
+ ___block_descriptor_48_e8_32s40s_e104_v88?0"NSString"8"NSString"16i24i28"NSString"32"NSString"40Q48"NSNumber"56i64i68i72"NSString"76B84l
+ _objc_msgSend$initWithEndpoint:trigger:interfaceType:stallType:foreground:silent:
+ _objc_msgSend$processStall:procName:endpoint:foreground:interfaceType:stallType:silent:
+ _objc_msgSend$silent
- -[DataStallHandler processStall:procName:endpoint:foreground:interfaceType:stallType:]
- -[TimedEndpoint initWithEndpoint:trigger:interfaceType:stallType:foreground:]
- GCC_except_table26
- ___block_descriptor_108_e8_32s40s48s56s64s72bs_e20_v20?0B8"NSError"12l
- ___block_descriptor_108_e8_32s40s48s56s64s72bs_e5_v8?0l
- ___block_descriptor_40_e8_32s_e101_v84?0"NSString"8"NSString"16i24i28"NSString"32"NSString"40Q48"NSNumber"56i64i68i72"NSString"76l
- ___block_descriptor_48_e8_32s40s_e101_v84?0"NSString"8"NSString"16i24i28"NSString"32"NSString"40Q48"NSNumber"56i64i68i72"NSString"76l
- _objc_msgSend$initWithEndpoint:trigger:interfaceType:stallType:foreground:
- _objc_msgSend$processStall:procName:endpoint:foreground:interfaceType:stallType:
CStrings:
+ "@56@0:8@16@24q32Q40B48B52"
+ "PRIVATE"
+ "TB,R,N,V_silent"
+ "_silent"
+ "initWithEndpoint:trigger:interfaceType:stallType:foreground:silent:"
+ "libnetcore symptom with no qualifier 0"
+ "libnetcore symptom with no qualifier 1"
+ "processStall:procName:endpoint:foreground:interfaceType:stallType:silent:"
+ "silent"
+ "v64@0:8@16@24@32B40q44Q52B60"
+ "v88@?0@\"NSString\"8@\"NSString\"16i24i28@\"NSString\"32@\"NSString\"40Q48@\"NSNumber\"56i64i68i72@\"NSString\"76B84"
- "@52@0:8@16@24q32Q40B48"
- "initWithEndpoint:trigger:interfaceType:stallType:foreground:"
- "libnetcore symptom with no qualifier"
- "libnetcore symptom with no qualifier1"
- "processStall:procName:endpoint:foreground:interfaceType:stallType:"
- "v60@0:8@16@24@32B40q44Q52"
- "v84@?0@\"NSString\"8@\"NSString\"16i24i28@\"NSString\"32@\"NSString\"40Q48@\"NSNumber\"56i64i68i72@\"NSString\"76"

```
