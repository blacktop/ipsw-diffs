## sirittsd

> `/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_capture`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3610.9.1.0.0
-  __TEXT.__text: 0x59a20
-  __TEXT.__auth_stubs: 0x2fe0
+3610.14.1.0.0
+  __TEXT.__text: 0x59d7c
+  __TEXT.__auth_stubs: 0x3020
   __TEXT.__objc_stubs: 0xe60
   __TEXT.__objc_methlist: 0x650
   __TEXT.__const: 0x1240
   __TEXT.__swift5_typeref: 0xb2a
   __TEXT.__cstring: 0x8a3
-  __TEXT.__oslogstring: 0x25bd
+  __TEXT.__oslogstring: 0x25fd
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_capture: 0xb1c
   __TEXT.__objc_methtype: 0x9fd

   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__auth_got: 0x17f8
+  __DATA_CONST.__auth_got: 0x1818
   __DATA_CONST.__got: 0x900
   __DATA_CONST.__auth_ptr: 0x4e0
   __DATA.__objc_const: 0x1990

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1103
-  Symbols:   1160
-  CStrings:  594
+  Symbols:   1164
+  CStrings:  595
 
Symbols:
+ _$s14SiriTTSService13MobileGestaltV9isHomePodSbvgZ
+ _$s14SiriTTSService24TTSFeatureFlagsContainerC6sharedACvgZ
+ _$s14SiriTTSService24TTSFeatureFlagsContainerCMa
+ _$s14SiriTTSService27SynthesizingRequestProtocolPAAE19containsAudioPromptSbvg
+ _$s14SiriTTSService9PCCClientC14isPCCSupported12featureFlagsSbAA010TTSFeatureG9ContainerC_tFZ
- _$s14SiriTTSService9PCCClientC14isPCCSupportedSbvgZ
Functions:
~ sub_1000039d4 : 3292 -> 3300
~ sub_100004e54 -> sub_100004e5c : 1504 -> 1776
~ sub_1000055dc -> sub_1000056f4 : 4308 -> 4436
~ sub_100007f50 -> sub_1000080e8 : 264 -> 288
~ sub_10000815c -> sub_10000830c : 2948 -> 2964
~ sub_10000b004 -> sub_10000b1c4 : 112 -> 124
~ sub_10000e408 -> sub_10000e5d4 : 3684 -> 3712
~ sub_10000f410 -> sub_10000f5f8 : 4164 -> 4380
~ sub_100017488 -> sub_100017748 : 120 -> 144
~ sub_10001eef4 -> sub_10001f1cc : 1940 -> 1936
~ sub_100020490 -> sub_100020764 : 836 -> 876
~ sub_1000207d4 -> sub_100020ad0 : 776 -> 800
~ sub_100021b20 -> sub_100021e34 : 3172 -> 3168
~ sub_100038610 -> sub_100038920 : 1000 -> 980
~ sub_1000389f8 -> sub_100038cf4 : 828 -> 848
~ sub_100038d5c -> sub_10003906c : 872 -> 876
~ sub_100056e14 -> sub_100057128 : 260 -> 284
~ sub_100056f18 -> sub_100057244 : 316 -> 352
~ sub_1000581b0 -> sub_100058500 : 1104 -> 1116
CStrings:
+ "#PrewarmRequest %llu skipping device engine prewarm since %s is preferred."
+ "PCC voice is not enabled due to audio prompt in text."
+ "PCC voice is not enabled since PCC is not supported on this platform."
- "#PrewarmRequest %llu skipping device engine prewarm since PCC is preferred."
- "PCC voice is not enabled due to disabled SiriTTSService/pcc feature."
```
