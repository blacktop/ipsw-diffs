## AGXGPURawCounter

> `/System/Library/PrivateFrameworks/AGXGPURawCounter.framework/AGXGPURawCounter`

```diff

 360.34.5.1.0
-  __TEXT.__text: 0xf644
-  __TEXT.__const: 0x200
+  __TEXT.__text: 0xf870
+  __TEXT.__const: 0x220
   __TEXT.__gcc_except_tab: 0x594
   __TEXT.__cstring: 0x400d
   __TEXT.__oslogstring: 0x2060

   __DATA_CONST.__objc_selrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x800
+  __AUTH_CONST.__const: 0x880
   __AUTH_CONST.__cfstring: 0x9a0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x270
-  __DATA.__data: 0x1f3
+  __DATA.__data: 0x223
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 165
-  Symbols:   353
+  Functions: 169
+  Symbols:   360
   CStrings:  361
 
Symbols:
+ __ZN13AGXGRC_HAL400L13HasMagicTokenEy
+ __ZN13AGXGRC_HAL400L16SampleHeaderSizeEv
+ __ZN13AGXGRC_HAL400L17ParseSampleHeaderEPKyP17AGXSPerfCtrSamplePy
+ __ZN13AGXGRC_HAL400L18KickslotConfigListE
+ __ZN13AGXGRC_HAL400L18sChipDispatchTableE
+ __ZN13AGXGRC_HAL400L21sChipDispatchTableAPSE
+ __ZN13AGXGRC_HAL400L23ResetSampleHeaderParserEy
Functions:
~ __ZN20AGXGPURawCounterImpl10SourceImpl28generateKickTimestampSamplesEjyyPKhjPNS0_13KickslotStateEPj : 1584 -> 1588
~ __ZN20AGXGPURawCounterImpl10SourceImpl14ringBufferInitEyPvj : 212 -> 216
~ __ZNK20AGXGPURawCounterImpl26chipDispatchTableForSourceEjjjPKc : 1616 -> 1788
```
