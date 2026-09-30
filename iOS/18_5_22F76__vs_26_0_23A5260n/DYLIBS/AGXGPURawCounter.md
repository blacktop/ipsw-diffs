## AGXGPURawCounter

> `/System/Library/PrivateFrameworks/AGXGPURawCounter.framework/AGXGPURawCounter`

```diff

-328.3.0.0.0
-  __TEXT.__text: 0xe804
-  __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__const: 0x188
+340.6.0.0.0
+  __TEXT.__text: 0xe8d4
+  __TEXT.__auth_stubs: 0x4d0
+  __TEXT.__const: 0x1b4
   __TEXT.__gcc_except_tab: 0x5f8
-  __TEXT.__cstring: 0x3e05
-  __TEXT.__oslogstring: 0x1f52
+  __TEXT.__cstring: 0x3e55
+  __TEXT.__oslogstring: 0x1fa9
   __TEXT.__unwind_info: 0x258
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x131

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0x280
+  __AUTH_CONST.__auth_got: 0x278
   __AUTH_CONST.__const: 0x6e0
   __AUTH_CONST.__cfstring: 0x8c0
   __AUTH_CONST.__objc_intobj: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E149F8F6-0B14-3CA3-B697-D53B5055A0D6
+  UUID: 7E4ED841-0E06-3821-BA98-21E991C2963C
   Functions: 142
   Symbols:   466
-  CStrings:  429
+  CStrings:  431
 
Symbols:
+ __ZL26sAGXSWCounterValueTypeList
+ __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.105
+ __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.112
+ __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.93
+ __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.99
+ ___block_literal_global.149
- __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.102
- __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.69
- __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.73
- __ZN31AGXPerfCtrRDESampleHeaderParserL14fAbsTimeOffsetE.95
- __Znwm
- ___block_literal_global.148
Functions:
~ __ZN20AGXGPURawCounterImpl10SourceImpl14ringBufferFreeEv : 144 -> 140
~ __ZN20AGXGPURawCounterImpl10SourceImpl15postProcessDataEjPKhyPyyPhyyS3_b : 4572 -> 4556
~ __ZNK20AGXGPURawCounterImpl10SourceImpl17availableTriggersEv : 100 -> 52
~ __ZN20AGXGPURawCounterImpl10SourceImpl10addCounterEPKcjjy : 3476 -> 3760
~ __ZNK20AGXGPURawCounterImpl10SourceImpl24copyAvailableCounterListEPPN16AGXGPURawCounter11CounterDescE : 164 -> 148
~ __ZN20AGXGPURawCounterImpl4initEj : 14428 -> 14464
~ __ZN10AGXGRC_G11L17ParseSampleHeaderEPKyP17AGXSPerfCtrSamplePy : 416 -> 420
~ __ZN10AGXGRC_G12L17ParseSampleHeaderEPKyP17AGXSPerfCtrSamplePy : 452 -> 448
~ __ZN10AGXGRC_G13L17ParseSampleHeaderEPKyP17AGXSPerfCtrSamplePy : 452 -> 448
~ __ZN10AGXGRC_G14L17ParseSampleHeaderEPKyP17AGXSPerfCtrSamplePy : 452 -> 448
~ __ZN11AGXGRC_G14XL17ParseSampleHeaderEPKyP17AGXSPerfCtrSamplePy : 332 -> 328
~ __ZN11AGXGRC_G14XL26ParseSampleHeaderInheritedEPKyP17AGXSPerfCtrSamplePy : 320 -> 316
~ __ZN10AGXGRC_G15L17ParseSampleHeaderEPKyP17AGXSPerfCtrSamplePy : 332 -> 328
~ __ZN10AGXGRC_G16L17ParseSampleHeaderEPKyP17AGXSPerfCtrSamplePy : 332 -> 328
~ __ZN13AGXGRC_HAL200L17ParseSampleHeaderEPKyP17AGXSPerfCtrSamplePy : 332 -> 328
CStrings:
+ "AGXGRC:%s:%d:%s: *** counterWidth must be <= 32 as \"%s\" has only 32 valid bits\n"
+ "AGXGRC:AGXGRC:%s:%d:%s: *** counterWidth must be <= 32 as \"%s\" has only 32 valid bits\n"

```
