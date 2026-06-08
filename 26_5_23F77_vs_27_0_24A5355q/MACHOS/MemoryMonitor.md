## MemoryMonitor

> `/System/Library/UserEventPlugins/MemoryMonitor.plugin/MemoryMonitor`

```diff

-379.100.5.0.0
-  __TEXT.__text: 0x19d0
-  __TEXT.__auth_stubs: 0x3b0
+391.0.0.0.0
+  __TEXT.__text: 0x18b0
+  __TEXT.__auth_stubs: 0x3a0
   __TEXT.__objc_stubs: 0x360
   __TEXT.__const: 0xa0
   __TEXT.__gcc_except_tab: 0x44

   __TEXT.__oslogstring: 0x29b
   __TEXT.__objc_methname: 0x188
   __TEXT.__unwind_info: 0xb8
-  __DATA.__auth_got: 0x1e8
-  __DATA.__got: 0x50
   __DATA.__const: 0x1a8
   __DATA.__cfstring: 0xe0
   __DATA.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0xd8
   __DATA.__objc_intobj: 0x30
+  __DATA.__auth_got: 0x1e0
+  __DATA.__got: 0x50
   __DATA.__bss: 0x28
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CDCE2852-0DD1-3623-B6BD-46C65B50C488
+  UUID: 4BE4281C-8EAD-37F2-B480-8EFF4E0B2A53
   Functions: 20
-  Symbols:   83
+  Symbols:   82
   CStrings:  71
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x25
- _objc_retain_x26
Functions:
~ sub_9b0 : 724 -> 716
~ sub_c84 -> sub_c7c : 800 -> 740
~ sub_fa4 -> sub_f60 : 308 -> 264
~ sub_10d8 -> sub_1068 : 724 -> 660
~ sub_18cc -> sub_181c : 120 -> 112
~ sub_19bc -> sub_1904 : 476 -> 468
~ sub_1b98 -> sub_1ad8 : 460 -> 448
~ sub_1e9c -> sub_1dd0 : 744 -> 700
~ sub_2184 -> sub_208c : 488 -> 20
~ sub_236c -> sub_20a0 : 20 -> 448

```
