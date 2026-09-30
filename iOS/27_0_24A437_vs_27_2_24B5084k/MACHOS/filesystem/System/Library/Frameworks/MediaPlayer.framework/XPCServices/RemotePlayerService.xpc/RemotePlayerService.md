## RemotePlayerService

> `/System/Library/Frameworks/MediaPlayer.framework/XPCServices/RemotePlayerService.xpc/RemotePlayerService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-4026.110.2.0.0
-  __TEXT.__text: 0x2238
+4026.200.12.0.0
+  __TEXT.__text: 0x2390
   __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_stubs: 0x620
+  __TEXT.__objc_stubs: 0x680
   __TEXT.__objc_methlist: 0x2ec
   __TEXT.__dlopen_cstrs: 0xad
   __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0x6c
-  __TEXT.__objc_methname: 0xa60
+  __TEXT.__objc_methname: 0xa99
   __TEXT.__cstring: 0x426
-  __TEXT.__oslogstring: 0x2f7
+  __TEXT.__oslogstring: 0x3b9
   __TEXT.__objc_classname: 0x93
   __TEXT.__objc_methtype: 0x264
   __TEXT.__unwind_info: 0x140

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__auth_got: 0x1d8
-  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__got: 0x90
   __DATA.__objc_const: 0x568
-  __DATA.__objc_selrefs: 0x308
+  __DATA.__objc_selrefs: 0x320
   __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x180

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 57
-  Symbols:   81
-  CStrings:  213
+  Symbols:   84
+  CStrings:  218
 
Symbols:
+ _AVSystemController_PIDToInheritApplicationStateFrom
+ _OBJC_CLASS_$_AVSystemController
+ _OBJC_CLASS_$_NSNumber
Functions:
~ sub_1000014fc : 4 -> 348
~ sub_100001500 -> sub_100001658 : 204 -> 72
~ sub_1000015cc -> sub_1000016a0 : 348 -> 204
~ sub_100001728 -> sub_10000176c : 212 -> 348
~ sub_1000017fc -> sub_1000018c8 : 72 -> 212
~ sub_1000027a8 -> sub_100002900 : 80 -> 56
~ sub_1000027f8 -> sub_100002938 : 340 -> 80
~ sub_10000294c -> sub_100002988 : 116 -> 340
~ sub_1000029c0 -> sub_100002adc : 56 -> 116
CStrings:
+ "MPRemotePlayerService: %p: Failed to set AVSystemController_PIDToInheritApplicationStateFrom to %ld"
+ "MPRemotePlayerService: %p: Setting AVSystemController_PIDToInheritApplicationStateFrom to %ld"
+ "numberWithInt:"
+ "setAttribute:forKey:error:"
+ "sharedInstance"
```
