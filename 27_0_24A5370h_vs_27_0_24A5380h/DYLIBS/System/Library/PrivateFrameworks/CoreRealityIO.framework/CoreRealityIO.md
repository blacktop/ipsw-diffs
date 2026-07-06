## CoreRealityIO

> `/System/Library/PrivateFrameworks/CoreRealityIO.framework/CoreRealityIO`

```diff

-  __TEXT.__text: 0x2c5aa4
+  __TEXT.__text: 0x2c4e78
   __TEXT.__const: 0x213f0
-  __TEXT.__gcc_except_tab: 0x36024
-  __TEXT.__cstring: 0x114b6
-  __TEXT.__oslogstring: 0x3e27
+  __TEXT.__gcc_except_tab: 0x360c0
+  __TEXT.__cstring: 0x114fb
+  __TEXT.__oslogstring: 0x3e74
   __TEXT.__unwind_info: 0x108f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x390
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x30
-  __DATA_CONST.__objc_selrefs: 0x3f8
+  __DATA_CONST.__objc_selrefs: 0x408
   __DATA_CONST.__got: 0x530
   __AUTH_CONST.__const: 0x1b898
   __AUTH_CONST.__cfstring: 0xfa0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/usd/libusd_ms.dylib
-  Functions: 13379
-  Symbols:   38168
-  CStrings:  2295
+  Functions: 13381
+  Symbols:   38175
+  CStrings:  2302
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH.__tf_func : content changed
~ __AUTH.__data : content changed
~ __AUTH.__thread_vars : content changed
~ __DATA.__data : content changed
Symbols:
+ __ZN12_GLOBAL__N_122getSamplerMinMagFilterEN32pxrInternal__aapl__pxrReserved__7TfTokenE
+ __ZN12_GLOBAL__N_122getSamplerMinMagFilterERN32pxrInternal__aapl__pxrReserved__12UsdAttributeE
+ __ZN12_GLOBAL__N_126samplerForTextureAttributeEN32pxrInternal__aapl__pxrReserved__7TfTokenES1_S1_S1_
+ __ZN12_GLOBAL__N_133uvNameAndTransformForTextureInputERKNSt3__13mapIN32pxrInternal__aapl__pxrReserved__7TfTokenENS2_7VtValueENS0_4lessIS3_EENS0_9allocatorINS0_4pairIKS3_S4_EEEEEES3_RNS0_12basic_stringIcNS0_11char_traitsIcEENS7_IcEEEERDv4_fRDv2_fRS3_SP_SP_SP_
+ _objc_msgSend$setMagFilter:
+ _objc_msgSend$setMinFilter:
- __ZN12_GLOBAL__N_126samplerForTextureAttributeEN32pxrInternal__aapl__pxrReserved__7TfTokenES1_
- __ZN12_GLOBAL__N_133uvNameAndTransformForTextureInputERKNSt3__13mapIN32pxrInternal__aapl__pxrReserved__7TfTokenENS2_7VtValueENS0_4lessIS3_EENS0_9allocatorINS0_4pairIKS3_S4_EEEEEES3_RNS0_12basic_stringIcNS0_11char_traitsIcEENS7_IcEEEERDv4_fRDv2_fRS3_SP_
CStrings:
+ "MinMag filter for imported USD was an invalid option; defaulting to \"linear\""
+ "inputs:magFilter"
+ "inputs:minFilter"
+ "linear"
+ "magFilter"
+ "minFilter"
+ "nearest"

```
