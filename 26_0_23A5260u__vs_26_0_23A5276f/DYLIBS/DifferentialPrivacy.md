## DifferentialPrivacy

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy`

```diff

-684.0.4.0.4
-  __TEXT.__text: 0x63638
+684.0.14.0.0
+  __TEXT.__text: 0x63624
   __TEXT.__auth_stubs: 0x11b0
-  __TEXT.__objc_methlist: 0x59cc
+  __TEXT.__objc_methlist: 0x59bc
   __TEXT.__const: 0xae0
-  __TEXT.__cstring: 0x48dd
+  __TEXT.__cstring: 0x48cd
   __TEXT.__oslogstring: 0x43c1
   __TEXT.__gcc_except_tab: 0xd80
   __TEXT.__ustring: 0x4

   __TEXT.__unwind_info: 0x1920
   __TEXT.__eh_frame: 0x770
   __TEXT.__objc_classname: 0xd95
-  __TEXT.__objc_methname: 0x9e22
+  __TEXT.__objc_methname: 0x9e05
   __TEXT.__objc_methtype: 0x12fc
   __TEXT.__objc_stubs: 0x7f80
-  __DATA_CONST.__got: 0x810
-  __DATA_CONST.__const: 0x11b8
+  __DATA_CONST.__got: 0x818
+  __DATA_CONST.__const: 0x1198
   __DATA_CONST.__objc_classlist: 0x4a8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90

   __AUTH_CONST.__auth_got: 0x8f0
   __AUTH_CONST.__const: 0x7f0
   __AUTH_CONST.__cfstring: 0x4080
-  __AUTH_CONST.__objc_const: 0xb050
+  __AUTH_CONST.__objc_const: 0xb020
   __AUTH_CONST.__objc_intobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xe58
   __AUTH.__data: 0x168
-  __DATA.__objc_ivar: 0x558
+  __DATA.__objc_ivar: 0x554
   __DATA.__data: 0x998
   __DATA.__bss: 0x950
   __DATA.__common: 0x18

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B850995F-B406-3DA1-BA5D-1B8101B38A3C
-  Functions: 2512
-  Symbols:   7869
-  CStrings:  3570
+  UUID: 02DF2984-9AB8-34E1-B594-D9548F47696B
+  Functions: 2511
+  Symbols:   7858
+  CStrings:  3569
 
Symbols:
+ +[_DPRandomizerUtils dimensionFromMetadata:]
+ +[_DPRandomizerUtils dimensionFromMetadata:].cold.1
+ -[_DPPreambleRandomizer plistParameters]
+ _OBJC_IVAR_$__DPPreambleRandomizer._plistParameters
+ _objc_msgSend$sendLogWithKey:taskExpiration:minBatchSize:targetCentralEpsilon:targetCentralDelta:localEpsilon:privateAccessToken:ohttp:
- -[_DPAppleIntelligenceReportParameters dimension]
- -[_DPPreambleRandomizer plistParameter]
- -[_DPPrio3SumVectorRandomizer dimensionFromMetadata:]
- -[_DPPrio3SumVectorRandomizer dimensionFromMetadata:].cold.1
- _OBJC_IVAR_$__DPAppleIntelligenceReportParameters._dimension
- _OBJC_IVAR_$__DPPreambleRandomizer._plistParameter
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_DifferentialPrivacy
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_DifferentialPrivacy
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_DifferentialPrivacy
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_DifferentialPrivacy
- _objc_msgSend$sendLogWithKey:dimension:taskExpiration:minBatchSize:targetCentralEpsilon:targetCentralDelta:localEpsilon:privateAccessToken:ohttp:
CStrings:
+ "fedstats:com.apple.insights.content-safety.analysisB"
+ "sendLogWithKey:taskExpiration:minBatchSize:targetCentralEpsilon:targetCentralDelta:localEpsilon:privateAccessToken:ohttp:"
+ "v68@0:8@16Q24I32d36d44d52B60B64"
- "TI,R,N,V_dimension"
- "fedstats:com.apple.insights.other-analysis.analysisB"
- "sendLogWithKey:dimension:taskExpiration:minBatchSize:targetCentralEpsilon:targetCentralDelta:localEpsilon:privateAccessToken:ohttp:"
- "v72@0:8@16I24Q28I36d40d48d56B64B68"

```
