## PersonalAudio

> `/System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio`

```diff

-543.2.1.0.0
-  __TEXT.__text: 0x1393c
-  __TEXT.__objc_methlist: 0xee8
+543.2.3.0.0
+  __TEXT.__text: 0x13d94
+  __TEXT.__objc_methlist: 0xf30
   __TEXT.__const: 0x110
   __TEXT.__dlopen_cstrs: 0x163
   __TEXT.__gcc_except_tab: 0x39c
-  __TEXT.__cstring: 0x1283
-  __TEXT.__oslogstring: 0xdb8
-  __TEXT.__unwind_info: 0x670
+  __TEXT.__cstring: 0x1285
+  __TEXT.__oslogstring: 0xe2e
+  __TEXT.__unwind_info: 0x680
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6d0
+  __DATA_CONST.__const: 0x720
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xef0
+  __DATA_CONST.__objc_selrefs: 0xf28
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__got: 0x198
   __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__cfstring: 0x1520
-  __AUTH_CONST.__objc_const: 0x1078
+  __AUTH_CONST.__objc_const: 0x10d8
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0xac
+  __DATA.__objc_ivar: 0xb4
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0xc0
+  __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 409
-  Symbols:   751
-  CStrings:  280
+  Functions: 418
+  Symbols:   763
+  CStrings:  282
 
Symbols:
+ -[PAAccessoryManager lastSentTransparencyDataByAddress]
+ -[PAAccessoryManager pseHysteresisTimer]
+ -[PAAccessoryManager sendUpdateToAccessoryCoalesced]
+ -[PAAccessoryManager sendUpdateToAccessoryForcingWrite:]
+ -[PAAccessoryManager setLastSentTransparencyDataByAddress:]
+ -[PAAccessoryManager setPseHysteresisTimer:]
+ GCC_except_table115
+ GCC_except_table173
+ GCC_except_table174
+ GCC_except_table229
+ GCC_except_table240
+ GCC_except_table251
+ GCC_except_table311
+ GCC_except_table326
+ GCC_except_table348
+ GCC_except_table389
+ GCC_except_table399
+ GCC_except_table402
+ GCC_except_table405
+ GCC_except_table50
+ GCC_except_table68
+ GCC_except_table77
+ _OBJC_IVAR_$_PAAccessoryManager._lastSentTransparencyDataByAddress
+ _OBJC_IVAR_$_PAAccessoryManager._pseHysteresisTimer
+ ___52-[PAAccessoryManager sendUpdateToAccessoryCoalesced]_block_invoke
+ ___52-[PAAccessoryManager sendUpdateToAccessoryCoalesced]_block_invoke_2
+ ___56-[PAAccessoryManager sendUpdateToAccessoryForcingWrite:]_block_invoke
+ ___56-[PAAccessoryManager sendUpdateToAccessoryForcingWrite:]_block_invoke_2
+ ___56-[PAAccessoryManager sendUpdateToAccessoryForcingWrite:]_block_invoke_3
+ ___56-[PAAccessoryManager sendUpdateToAccessoryForcingWrite:]_block_invoke_4
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_57_e8_32s40s48s_e17_v16?0"NSArray"8ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_66_e8_32s40s48s56s_e8_v12?0B8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_66_e8_32s40s48s56s_e8_v16?0Q8ls32l8s40l8s48l8s56l8
- GCC_except_table106
- GCC_except_table164
- GCC_except_table165
- GCC_except_table220
- GCC_except_table231
- GCC_except_table242
- GCC_except_table302
- GCC_except_table317
- GCC_except_table339
- GCC_except_table380
- GCC_except_table390
- GCC_except_table393
- GCC_except_table396
- GCC_except_table46
- GCC_except_table60
- GCC_except_table69
- ___43-[PAAccessoryManager sendUpdateToAccessory]_block_invoke
- ___43-[PAAccessoryManager sendUpdateToAccessory]_block_invoke_2
- ___43-[PAAccessoryManager sendUpdateToAccessory]_block_invoke_3
- ___43-[PAAccessoryManager sendUpdateToAccessory]_block_invoke_4
- ___block_descriptor_48_e8_32s40s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8
- ___block_descriptor_57_e8_32s40s48s_e8_v12?0B8ls32l8s40l8s48l8
- ___block_descriptor_57_e8_32s40s48s_e8_v16?0Q8ls32l8s40l8s48l8
CStrings:
+ "PAAccessoryManager: Skipping transparency update because pending timer"
+ "Skipping update to %@, configuration unchanged"
```
