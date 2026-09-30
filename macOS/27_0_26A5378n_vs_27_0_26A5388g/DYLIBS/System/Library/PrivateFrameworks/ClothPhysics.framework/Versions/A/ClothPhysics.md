## ClothPhysics

> `/System/Library/PrivateFrameworks/ClothPhysics.framework/Versions/A/ClothPhysics`

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
- `__DATA.__data`

```diff

-21.0.2.0.0
-  __TEXT.__text: 0xbcad4
+21.0.3.0.0
+  __TEXT.__text: 0xbca40
   __TEXT.__objc_methlist: 0x238
   __TEXT.__const: 0x2bf0
   __TEXT.__oslogstring: 0x5028
-  __TEXT.__cstring: 0x918b
+  __TEXT.__cstring: 0x91e7
   __TEXT.__gcc_except_tab: 0x5b60
-  __TEXT.__unwind_info: 0x3600
+  __TEXT.__unwind_info: 0x35f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __AUTH_CONST.__objc_const: 0x2c8
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__auth_got: 0x450
-  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0xf0
   __DATA.__bss: 0x1a0
   __DATA.__common: 0x19
+  __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Metal.framework/Versions/A/Metal

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libc++abi.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3927
-  Symbols:   5424
-  CStrings:  1721
+  Functions: 3925
+  Symbols:   5422
+  CStrings:  1725
 
Symbols:
+ _ZN5cloth14PickingVolumes10encodeDragEPNS_14ComputeEncoderERKNS_16VolumeDragParamsERKNS_20SimulationParametersE
+ _ZN5cloth14PickingVolumes10encodePickEPNS_14ComputeEncoderERKNS_16VolumePickParamsEbNS_18GenericBufferSliceILb0EEE
+ __ZN5cloth14PickingVolumes10encodeDragEPNS_14ComputeEncoderERKNS_16VolumeDragParamsERKNS_20SimulationParametersE
+ __ZN5cloth14PickingVolumes10encodePickEPNS_14ComputeEncoderERKNS_16VolumePickParamsEbNS_18GenericBufferSliceILb0EEE
- _ZN5cloth14PickingVolumes10encodeDragEPNS_14ComputeEncoderERKNS_16VolumeDragParamsERKNS_20SimulationParametersEf
- _ZN5cloth14PickingVolumes10encodePickEPNS_14ComputeEncoderERKNS_16VolumePickParamsENS_18GenericBufferSliceILb0EEE
- _ZN5cloth14PickingVolumes19computeFalloffRangeEj
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
