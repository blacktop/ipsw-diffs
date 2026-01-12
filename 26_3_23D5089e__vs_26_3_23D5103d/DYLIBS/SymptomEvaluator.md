## SymptomEvaluator

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator`

```diff

-2158.80.9.0.0
-  __TEXT.__text: 0x27a04c
+2158.80.10.0.0
+  __TEXT.__text: 0x27a1f8
   __TEXT.__auth_stubs: 0x2c70
-  __TEXT.__objc_methlist: 0x17788
-  __TEXT.__cstring: 0x25199
+  __TEXT.__objc_methlist: 0x17790
+  __TEXT.__cstring: 0x251a9
   __TEXT.__const: 0xf80
   __TEXT.__oslogstring: 0x4311f
   __TEXT.__gcc_except_tab: 0x53e4

   __TEXT.bb_MAV_clp: 0x89e0
   __TEXT.bb_INT_clp: 0x6a10
   __TEXT.modules_clp: 0x16e0
-  __TEXT.__unwind_info: 0x6a78
+  __TEXT.__unwind_info: 0x6a80
   __TEXT.__eh_frame: 0x698
   __TEXT.__objc_classname: 0x1d5c
-  __TEXT.__objc_methname: 0x3c741
-  __TEXT.__objc_methtype: 0x6c5b
-  __TEXT.__objc_stubs: 0x25a00
+  __TEXT.__objc_methname: 0x3c76e
+  __TEXT.__objc_methtype: 0x6c61
+  __TEXT.__objc_stubs: 0x25a20
   __DATA_CONST.__got: 0xf50
   __DATA_CONST.__const: 0x66f0
   __DATA_CONST.__objc_classlist: 0x860
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xca68
+  __DATA_CONST.__objc_selrefs: 0xca70
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x588
   __DATA_CONST.__objc_arraydata: 0x8c0
   __AUTH_CONST.__auth_got: 0x1650
   __AUTH_CONST.__const: 0x2c30
-  __AUTH_CONST.__cfstring: 0x1cec0
-  __AUTH_CONST.__objc_const: 0x3c168
+  __AUTH_CONST.__cfstring: 0x1cee0
+  __AUTH_CONST.__objc_const: 0x3c198
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x938
   __AUTH_CONST.__objc_intobj: 0x840

   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH.__objc_data: 0x15b0
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x2d40
+  __DATA.__objc_ivar: 0x2d44
   __DATA.__data: 0x1e08
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xf50

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: ACDF90A1-FDB8-3A0B-9E61-3C06CDFB24E2
-  Functions: 11311
-  Symbols:   36493
-  CStrings:  26592
+  UUID: 862D0756-47B3-3026-9E31-A80BF15196CB
+  Functions: 11312
+  Symbols:   36497
+  CStrings:  26597
 
Symbols:
+ -[DataStallHandler processStall:procName:endpoint:foreground:interfaceType:stallType:silent:]
+ -[TimedEndpoint initWithEndpoint:trigger:interfaceType:stallType:foreground:silent:]
+ -[TimedEndpoint silent]
+ _OBJC_IVAR_$_TimedEndpoint._silent
+ ___block_descriptor_109_e8_32s40s48s56s64s72bs_e20_v20?0B8"NSError"12ls72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_109_e8_32s40s48s56s64s72bs_e5_v8?0ls72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_40_e8_32s_e104_v88?0"NSString"8"NSString"16i24i28"NSString"32"NSString"40Q48"NSNumber"56i64i68i72"NSString"76B84ls32l8
+ ___block_descriptor_48_e8_32s40s_e104_v88?0"NSString"8"NSString"16i24i28"NSString"32"NSString"40Q48"NSNumber"56i64i68i72"NSString"76B84ls32l8s40l8
+ _objc_msgSend$initWithEndpoint:trigger:interfaceType:stallType:foreground:silent:
+ _objc_msgSend$processStall:procName:endpoint:foreground:interfaceType:stallType:silent:
+ _objc_msgSend$silent
- -[DataStallHandler processStall:procName:endpoint:foreground:interfaceType:stallType:]
- -[TimedEndpoint initWithEndpoint:trigger:interfaceType:stallType:foreground:]
- ___block_descriptor_108_e8_32s40s48s56s64s72bs_e20_v20?0B8"NSError"12ls72l8s32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_108_e8_32s40s48s56s64s72bs_e5_v8?0ls72l8s32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_40_e8_32s_e101_v84?0"NSString"8"NSString"16i24i28"NSString"32"NSString"40Q48"NSNumber"56i64i68i72"NSString"76ls32l8
- ___block_descriptor_48_e8_32s40s_e101_v84?0"NSString"8"NSString"16i24i28"NSString"32"NSString"40Q48"NSNumber"56i64i68i72"NSString"76ls32l8s40l8
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
