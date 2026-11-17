## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

-995.0.0.0.0
-  __TEXT.__text: 0x18e60c
+996.0.0.0.0
+  __TEXT.__text: 0x18f0f0
   __TEXT.__objc_methlist: 0x1fc
   __TEXT.__const: 0xc4cf
-  __TEXT.__oslogstring: 0x164b3
-  __TEXT.__cstring: 0x5669
+  __TEXT.__oslogstring: 0x1660f
+  __TEXT.__cstring: 0x56cf
   __TEXT.__gcc_except_tab: 0xe74
-  __TEXT.__unwind_info: 0x3c58
+  __TEXT.__unwind_info: 0x3c98
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x5940
-  __AUTH_CONST.__cfstring: 0x800
+  __AUTH_CONST.__cfstring: 0x820
   __AUTH_CONST.__objc_const: 0x6e0
   __AUTH_CONST.__weak_auth_got: 0x38
   __AUTH_CONST.__objc_intobj: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4388
-  Symbols:   3658
-  CStrings:  2072
+  Functions: 4405
+  Symbols:   3662
+  CStrings:  2079
 
Symbols:
+ _SetStrictBitstreamValidation
+ _SetStrictBitstreamValidationProperty
+ __ZNK6CAHDec25strictBitstreamValidationEv
+ _kVTDecompressionPropertyKey_EnableStrictBitstreamValidation
CStrings:
+ "AVD_EnableStrictBitstreamValidation"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDSetParameter call for kAppleAVDSetStrictBitstreamValidation returned ERROR\n\n"
+ "AppleAVD: ERROR: %{public}s(): bad index %u\n"
+ "AppleAVD: ERROR: %{public}s(): propertyValue (%p) is invalid!\n\n"
+ "AppleAVD: INFO: %{public}s(): cfg4: %d %d\n"
+ "AppleAVD: WARNING: %{public}s(): trying to set kAppleAVDSetStrictBitstreamValidation before videoContext was created!\n\n"
+ "SetStrictBitstreamValidation"
+ "SetStrictBitstreamValidationProperty"
- "AppleAVD: INFO: %{public}s(): cfg4: %d\n"
```
