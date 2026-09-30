## ClothPhysics

> `/System/Library/PrivateFrameworks/ClothPhysics.framework/ClothPhysics`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__DATA.__data`

```diff

-21.0.2.0.0
-  __TEXT.__text: 0xc1048
+21.0.3.0.0
+  __TEXT.__text: 0xc0ff0
   __TEXT.__objc_methlist: 0x238
   __TEXT.__const: 0x2bc0
   __TEXT.__oslogstring: 0x4ff5
-  __TEXT.__cstring: 0x91b1
+  __TEXT.__cstring: 0x920d
   __TEXT.__gcc_except_tab: 0x5b2c
-  __TEXT.__unwind_info: 0x3610
+  __TEXT.__unwind_info: 0x3608
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __AUTH_CONST.__objc_const: 0x2c8
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__auth_got: 0x4c8
-  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0xf0
   __DATA.__bss: 0x1a0
   __DATA.__common: 0x19
+  __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Metal.framework/Metal

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libc++abi.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3931
-  Symbols:   4475
-  CStrings:  1720
+  Functions: 3929
+  Symbols:   4474
+  CStrings:  1724
 
Symbols:
+ __ZN5cloth14PickingVolumes10encodeDragEPNS_14ComputeEncoderERKNS_16VolumeDragParamsERKNS_20SimulationParametersE
+ __ZN5cloth14PickingVolumes10encodePickEPNS_14ComputeEncoderERKNS_16VolumePickParamsEbNS_18GenericBufferSliceILb0EEE
- __ZN5cloth14PickingVolumes10encodeDragEPNS_14ComputeEncoderERKNS_16VolumeDragParamsERKNS_20SimulationParametersEf
- __ZN5cloth14PickingVolumes10encodePickEPNS_14ComputeEncoderERKNS_16VolumePickParamsENS_18GenericBufferSliceILb0EEE
- __ZN5cloth14PickingVolumes19computeFalloffRangeEj
CStrings:
+ "Volume pick depth range"
+ "volumePickReduceDepth"
+ "volumePickResetDepthRange"
+ "volumePick_falloff"
+ "volumePick_noFalloff"
- "computeFalloffRange"
```
