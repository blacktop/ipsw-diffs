## BTAudioHALPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/Contents/MacOS/BTAudioHALPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-2700.46.1.1.0
-  __TEXT.__text: 0x93254
+2700.51.0.0.0
+  __TEXT.__text: 0x934e4
   __TEXT.__auth_stubs: 0x1220
   __TEXT.__objc_stubs: 0x1f20
   __TEXT.__init_offsets: 0xb4
   __TEXT.__objc_methlist: 0xcac
   __TEXT.__gcc_except_tab: 0x2840
   __TEXT.__const: 0x1cec
-  __TEXT.__cstring: 0x539b
-  __TEXT.__oslogstring: 0x19e35
+  __TEXT.__cstring: 0x53d1
+  __TEXT.__oslogstring: 0x19ed3
   __TEXT.__objc_methname: 0x2967
   __TEXT.__objc_classname: 0x112
   __TEXT.__objc_methtype: 0x7b4
-  __TEXT.__unwind_info: 0x2090
+  __TEXT.__unwind_info: 0x2098
   __TEXT.__eh_frame: 0x50
   __DATA_CONST.__const: 0x79d8
   __DATA_CONST.__cfstring: 0x1780

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3280
+  Functions: 3285
   Symbols:   425
-  CStrings:  3048
+  CStrings:  3055
 
CStrings:
+ "BT Virtual Device GetDbVolume no active reference device"
+ "BT Virtual Device GetMaxDbVolume no active reference device"
+ "BT Virtual Device GetMinDbVolume no active reference device"
+ "GetDbVolume"
+ "GetMaxDbVolume"
+ "GetMinDbVolume"
+ "HostGrid no-op c:%llu,Q:%f~%u,curr:%f,ATs:%f,bufSize:%u"
+ "HostGrid reA prevATs:%f,prevQ:%f~%u,drop:%f,Q:%f~%u,curr:%f,ATs:%f,bufSize:%u,Seq:%u,%llu"
+ "SetDbVolume"
- "HostGrid reA prevATs:%f,prevQ:%f~%u,drop:%f,Q:%f~%u,curr:%f,ATs:%f,bufSize:%u,Seq:%u , @ %llu"
- "HostGrid should not come here c:%llu,Q:%f~%u,curr:%f,ATs:%f,bufSize:%u"
```
