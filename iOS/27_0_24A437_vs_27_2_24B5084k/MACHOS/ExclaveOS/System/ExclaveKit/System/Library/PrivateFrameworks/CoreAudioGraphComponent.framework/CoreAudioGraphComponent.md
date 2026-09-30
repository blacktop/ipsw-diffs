## CoreAudioGraphComponent

> `/System/ExclaveKit/System/Library/PrivateFrameworks/CoreAudioGraphComponent.framework/CoreAudioGraphComponent`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-95.0.0.0.0
-  __TEXT.__text: 0xb208
+95.202.0.0.0
+  __TEXT.__text: 0xaf0c
   __TEXT.__auth_stubs: 0x590
   __TEXT.__const: 0x268
   __TEXT.__gcc_except_tab: 0xec
-  __TEXT.__cstring: 0x1b24
-  __TEXT.__oslogstring: 0x689
+  __TEXT.__cstring: 0x1a2d
+  __TEXT.__oslogstring: 0x5b2
   __TEXT.__unwind_info: 0x428
   __DATA_CONST.__const: 0x650
   __DATA_CONST.__auth_got: 0x2d0

   - /System/ExclaveKit/usr/lib/libc++.dylib
   Functions: 245
   Symbols:   452
-  CStrings:  125
+  CStrings:  117
 
Symbols:
+ ____Z14create_handlerv_block_invoke_4
- ___Z14create_handlerv_block_invoke
Functions:
~ ____Z14create_handlerv_block_invoke_3 : 296 -> 80
~ __ZN21CoreAudioGraphExclave14readFromDeviceEjyyjj : 876 -> 664
~ __ZN21CoreAudioGraphExclave13writeToDeviceEjyyjj : 836 -> 644
~ ____ZN21CoreAudioGraphExclave13writeToDeviceEjyyjj_block_invoke : 408 -> 264
CStrings:
- "[%s]   Device %u: writeToStream succeeded"
- "[%s] CoreAudioGraph: Reading from device %u (identifier=%u)"
- "[%s] CoreAudioGraph: Writing to device %u"
- "[%s] CoreAudioGraph: doIO() useCaseID=%u sampleTime=%llu hostTime=%llu"
- "[DEBUG][%s]   Device %u: writeToStream succeeded\n"
- "[DEBUG][%s] CoreAudioGraph: Reading from device %u (identifier=%u)\n"
- "[DEBUG][%s] CoreAudioGraph: Writing to device %u\n"
- "[DEBUG][%s] CoreAudioGraph: doIO() useCaseID=%u sampleTime=%llu hostTime=%llu\n"
```
