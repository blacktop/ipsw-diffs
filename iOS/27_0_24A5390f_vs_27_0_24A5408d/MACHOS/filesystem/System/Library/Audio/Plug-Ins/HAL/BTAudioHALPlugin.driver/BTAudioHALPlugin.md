## BTAudioHALPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-2700.46.1.1.0
-  __TEXT.__text: 0x7dae0
+2700.51.1.1.0
+  __TEXT.__text: 0x7dbf0
   __TEXT.__auth_stubs: 0x1370
   __TEXT.__objc_stubs: 0x2800
   __TEXT.__init_offsets: 0xa4
   __TEXT.__objc_methlist: 0x118c
-  __TEXT.__gcc_except_tab: 0x2064
+  __TEXT.__gcc_except_tab: 0x2074
   __TEXT.__const: 0x1aec
   __TEXT.__cstring: 0x4f78
-  __TEXT.__oslogstring: 0x16dc1
+  __TEXT.__oslogstring: 0x16dae
   __TEXT.__objc_methname: 0x3ecc
   __TEXT.__objc_classname: 0x154
   __TEXT.__objc_methtype: 0x1257
Functions:
~ sub_84ec : 1540 -> 1556
~ sub_133e0 -> sub_133f0 : 4 -> 8
~ sub_133e4 -> sub_133f8 : 4 -> 8
~ sub_133e8 -> sub_13400 : 8 -> 4
~ sub_133f0 -> sub_13404 : 8 -> 4
~ sub_2595c -> sub_2596c : 4 -> 8
~ sub_25960 -> sub_25974 : 4 -> 8
~ sub_25964 -> sub_2597c : 8 -> 4
~ sub_2596c -> sub_25980 : 8 -> 4
~ sub_28b18 -> sub_28b28 : 4 -> 8
~ sub_28b1c -> sub_28b30 : 4 -> 8
~ sub_28b20 -> sub_28b38 : 8 -> 4
~ sub_28b28 -> sub_28b3c : 8 -> 4
~ sub_2cc88 -> sub_2cc98 : 4 -> 8
~ sub_2cc8c -> sub_2cca0 : 4 -> 8
~ sub_2cc90 -> sub_2cca8 : 8 -> 4
~ sub_2cc98 -> sub_2ccac : 8 -> 4
~ sub_43898 -> sub_438a8 : 16 -> 8
~ sub_438a8 -> sub_438b0 : 16 -> 8
~ sub_438b8 : 24 -> 16
~ sub_438d0 -> sub_438c8 : 8 -> 16
~ sub_438d8 : 8 -> 24
~ sub_4c3c4 -> sub_4c3d4 : 4 -> 8
~ sub_4c3d0 -> sub_4c3e4 : 8 -> 4
~ sub_6c928 -> sub_6c938 : 540 -> 796
~ sub_6ef78 -> sub_6f088 : 4 -> 8
~ sub_6ef84 -> sub_6f098 : 8 -> 4
~ sub_6ef8c -> sub_6f09c : 8 -> 4
~ sub_6ef9c -> sub_6f0a8 : 4 -> 8
CStrings:
+ "HostGrid no-op c:%llu,Q:%f~%u,curr:%f,ATs:%f,bufSize:%u"
+ "HostGrid reA prevATs:%f,prevQ:%f~%u,drop:%f,Q:%f~%u,curr:%f,ATs:%f,bufSize:%u,Seq:%u,%llu"
- "HostGrid reA prevATs:%f,prevQ:%f~%u,drop:%f,Q:%f~%u,curr:%f,ATs:%f,bufSize:%u,Seq:%u , @ %llu"
- "HostGrid should not come here c:%llu,Q:%f~%u,curr:%f,ATs:%f,bufSize:%u"
```
