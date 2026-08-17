## VirtualAudio

> `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__dof_VirtualAu`
- `__TEXT.__dof_Aggregate`
- `__TEXT.__dof_VirtualA0`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1451.115.0.0.0
-  __TEXT.__text: 0x52ee30
+1451.115.30.0.0
+  __TEXT.__text: 0x530ae8
   __TEXT.__realtime: 0x14908
   __TEXT.__auth_stubs: 0x28b0
   __TEXT.__objc_stubs: 0xfa0
   __TEXT.__init_offsets: 0x1034
   __TEXT.__objc_methlist: 0x2c0
   __TEXT.__const: 0xb1418
-  __TEXT.__cstring: 0x36b5e
-  __TEXT.__gcc_except_tab: 0x5f90c
+  __TEXT.__cstring: 0x36bce
+  __TEXT.__gcc_except_tab: 0x5fbb0
   __TEXT.__swift5_typeref: 0x12b
   __TEXT.__swift5_capture: 0x168
-  __TEXT.__oslogstring: 0x56a41
+  __TEXT.__oslogstring: 0x56cb8
   __TEXT.__objc_methname: 0xdad
   __TEXT.__objc_classname: 0x9d
   __TEXT.__objc_methtype: 0x422

   __TEXT.__dof_VirtualAu: 0x340
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0x14430
+  __TEXT.__unwind_info: 0x14480
   __TEXT.__eh_frame: 0x730
-  __DATA_CONST.__const: 0x28c80
+  __DATA_CONST.__const: 0x28d10
   __DATA_CONST.__cfstring: 0x2f40
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12158
+  Functions: 12180
   Symbols:   806
-  CStrings:  12105
+  CStrings:  12114
 
CStrings:
+ "%25s:%-5d EXCEPTION (GetCurrentFormat(streamFormat, kAudioStreamPropertyPhysicalFormat)) [error GetCurrentFormat(streamFormat, kAudioStreamPropertyPhysicalFormat) is an error]: \"error getting current stream format\""
+ "%25s:%-5d Route change failed: device %u (%s) is left with nominal sample rate %.0f."
+ "%25s:%-5d Route change failed: publishing property changes accumulated before the failure: %s."
+ "%25s:%-5d Route change failed: restoring dependent sample rate %u on device %u."
+ "%25s:%-5d Route change failed: restoring nominal sample rate %.0f on device %u."
+ "%25s:%-5d Untrustworthy stream %s could not supply its physical format; %s."
+ "@@ Strips Aug  9 2026 03:26:56"
+ "] "
+ "assuming it is not an Atmos stream"
+ "using a neutral latency scale factor"
- "@@ Strips Aug  4 2026 11:01:42"
```
