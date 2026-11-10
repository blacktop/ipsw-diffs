## PersonalAudio

> `/System/Library/PrivateFrameworks/PersonalAudio.framework/Versions/A/PersonalAudio`

```diff

-539.0.1.0.0
-  __TEXT.__text: 0x14a68
-  __TEXT.__objc_methlist: 0xec0
+543.2.5.0.0
+  __TEXT.__text: 0x14efc
+  __TEXT.__objc_methlist: 0xf08
   __TEXT.__const: 0xf0
   __TEXT.__gcc_except_tab: 0x348
-  __TEXT.__cstring: 0x1204
-  __TEXT.__oslogstring: 0xdf8
+  __TEXT.__cstring: 0x1206
+  __TEXT.__oslogstring: 0xe6e
   __TEXT.__dlopen_cstrs: 0x11a
-  __TEXT.__unwind_info: 0x560
+  __TEXT.__unwind_info: 0x570
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe90
+  __DATA_CONST.__objc_selrefs: 0xec8
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__got: 0x168
-  __AUTH_CONST.__const: 0x850
+  __AUTH_CONST.__const: 0x8b0
   __AUTH_CONST.__cfstring: 0x14a0
-  __AUTH_CONST.__objc_const: 0x1078
+  __AUTH_CONST.__objc_const: 0x10d8
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0xac
+  __DATA.__objc_ivar: 0xb4
   __DATA.__data: 0xc0
   __DATA.__bss: 0xa8
   __DATA_DIRTY.__objc_data: 0x320

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 418
-  Symbols:   1089
-  CStrings:  272
+  Functions: 427
+  Symbols:   1106
+  CStrings:  274
 
Symbols:
+ -[PAAccessoryManager lastSentTransparencyDataByAddress]
+ -[PAAccessoryManager pseHysteresisTimer]
+ -[PAAccessoryManager sendUpdateToAccessoryCoalesced]
+ -[PAAccessoryManager sendUpdateToAccessoryForcingWrite:]
+ -[PAAccessoryManager setLastSentTransparencyDataByAddress:]
+ -[PAAccessoryManager setPseHysteresisTimer:]
+ GCC_except_table129
+ GCC_except_table189
+ GCC_except_table190
+ GCC_except_table245
+ GCC_except_table317
+ GCC_except_table332
+ GCC_except_table353
+ GCC_except_table396
+ GCC_except_table406
+ GCC_except_table409
+ GCC_except_table414
+ GCC_except_table54
+ GCC_except_table80
+ GCC_except_table89
+ OBJC_IVAR_$_PAAccessoryManager._lastSentTransparencyDataByAddress
+ OBJC_IVAR_$_PAAccessoryManager._pseHysteresisTimer
+ ___52-[PAAccessoryManager sendUpdateToAccessoryCoalesced]_block_invoke
+ ___52-[PAAccessoryManager sendUpdateToAccessoryCoalesced]_block_invoke_2
+ ___56-[PAAccessoryManager sendUpdateToAccessoryForcingWrite:]_block_invoke
+ ___56-[PAAccessoryManager sendUpdateToAccessoryForcingWrite:]_block_invoke_2
+ ___56-[PAAccessoryManager sendUpdateToAccessoryForcingWrite:]_block_invoke_3
+ ___56-[PAAccessoryManager sendUpdateToAccessoryForcingWrite:]_block_invoke_4
+ ___block_descriptor_48_e8_32s40w_e5_v8?0l
+ ___block_descriptor_57_e8_32s40s48s_e17_v16?0"NSArray"8l
+ ___block_descriptor_57_e8_32s40s48s_e25_v32?0"NSString"8Q16^B24l
+ ___block_descriptor_66_e8_32s40s48s56s_e8_v12?0B8l
+ ___block_descriptor_66_e8_32s40s48s56s_e8_v16?0Q8l
+ _objc_msgSend$isEqualToData:
+ _objc_msgSend$lastSentTransparencyDataByAddress
+ _objc_msgSend$pseHysteresisTimer
+ _objc_msgSend$sendUpdateToAccessoryCoalesced
+ _objc_msgSend$sendUpdateToAccessoryForcingWrite:
+ _objc_msgSend$setPseHysteresisTimer:
- GCC_except_table118
- GCC_except_table178
- GCC_except_table179
- GCC_except_table234
- GCC_except_table308
- GCC_except_table323
- GCC_except_table344
- GCC_except_table387
- GCC_except_table397
- GCC_except_table400
- GCC_except_table405
- GCC_except_table50
- GCC_except_table70
- GCC_except_table79
- ___43-[PAAccessoryManager sendUpdateToAccessory]_block_invoke
- ___43-[PAAccessoryManager sendUpdateToAccessory]_block_invoke_2
- ___43-[PAAccessoryManager sendUpdateToAccessory]_block_invoke_3
- ___43-[PAAccessoryManager sendUpdateToAccessory]_block_invoke_4
- ___block_descriptor_48_e8_32s40s_e25_v32?0"NSString"8Q16^B24l
- ___block_descriptor_57_e8_32s40s48s_e8_v12?0B8l
- ___block_descriptor_57_e8_32s40s48s_e8_v16?0Q8l
- _objc_msgSend$sendUpdateToAccessory
CStrings:
+ "PAAccessoryManager: Skipping transparency update because pending timer"
+ "Skipping update to %@, configuration unchanged"
```
