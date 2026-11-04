## replayd

> `/usr/libexec/replayd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__objc_methtype`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-765.15.2.0.0
-  __TEXT.__text: 0xb97a4
-  __TEXT.__auth_stubs: 0x1920
+770.2.1.0.0
+  __TEXT.__text: 0xb98b4
+  __TEXT.__auth_stubs: 0x1930
   __TEXT.__objc_stubs: 0xf340
   __TEXT.__objc_methlist: 0x74b0
   __TEXT.__const: 0x3e4
   __TEXT.__gcc_except_tab: 0xfc8
-  __TEXT.__objc_methname: 0x15f9b
-  __TEXT.__oslogstring: 0x16809
+  __TEXT.__objc_methname: 0x15fe3
+  __TEXT.__oslogstring: 0x16863
   __TEXT.__cstring: 0x17d26
   __TEXT.__objc_classname: 0xa44
   __TEXT.__objc_methtype: 0x4410

   __DATA_CONST.__objc_doubleobj: 0x50
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0xca0
+  __DATA_CONST.__auth_got: 0xca8
   __DATA_CONST.__got: 0xc88
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x113b8
+  __DATA.__objc_const: 0x11418
   __DATA.__objc_selrefs: 0x4728
-  __DATA.__objc_ivar: 0xd88
+  __DATA.__objc_ivar: 0xd94
   __DATA.__objc_data: 0x18b0
   __DATA.__data: 0xe54
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 3683
-  Symbols:   802
-  CStrings:  7391
+  Symbols:   803
+  CStrings:  7395
 
Symbols:
+ _MGGetLogicalDeviceDisplayCount
Functions:
~ sub_100014f10 : 888 -> 880
~ sub_100015f58 -> sub_100015f50 : 720 -> 712
~ sub_1000171f0 -> sub_1000171e0 : 752 -> 744
~ sub_1000177cc -> sub_1000177b4 : 216 -> 208
~ sub_100027e98 -> sub_100027e78 : 100 -> 160
~ sub_100028ad0 -> sub_100028aec : 932 -> 1216
~ sub_100081cac -> sub_100081de4 : 448 -> 440
~ sub_100081ea4 -> sub_100081fd4 : 448 -> 440
~ sub_1000a1c68 -> sub_1000a1d90 : 784 -> 776
~ sub_1000a2b28 -> sub_1000a2c48 : 556 -> 548
~ sub_1000a36e0 -> sub_1000a37f8 : 852 -> 844
CStrings:
+ " [DEBUG] %{public}s:%d dropping frame width:%zu heigth:%zu, expected width:%zu heigth:%zu"
+ "_dropsFramesWithUnexpectedSize"
+ "_expectedFrameHeight"
+ "_expectedFrameWidth"
```
