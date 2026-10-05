## CoreUI

> `/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`

```diff

-1011.2.0.0.0
-  __TEXT.__text: 0xe34ac
+1011.4.0.0.0
+  __TEXT.__text: 0xe35e0
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0xa4
   __TEXT.__objc_methlist: 0xa420
   __TEXT.__const: 0x64d8
-  __TEXT.__gcc_except_tab: 0x2c7c
-  __TEXT.__cstring: 0x25f71
+  __TEXT.__gcc_except_tab: 0x2cac
+  __TEXT.__cstring: 0x26071
   __TEXT.__oslogstring: 0x200
   __TEXT.__constg_swiftt: 0x2fc
   __TEXT.__swift5_typeref: 0x38e

   __TEXT.__swift5_capture: 0x168
   __TEXT.__swift5_proto: 0x20
   __TEXT.__swift5_assocty: 0x58
-  __TEXT.__unwind_info: 0x50d8
+  __TEXT.__unwind_info: 0x50e0
   __TEXT.__eh_frame: 0x120
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__auth_got: 0x17b8
-  __AUTH.__objc_data: 0x22e0
+  __AUTH_CONST.__auth_got: 0x17e0
+  __AUTH.__objc_data: 0x2290
   __AUTH.__data: 0x128
   __DATA.__objc_ivar: 0xc34
   __DATA.__data: 0x79c
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0xff0
+  __DATA_DIRTY.__objc_data: 0x1040
   __DATA_DIRTY.__crash_info: 0x148
   __DATA_DIRTY.__bss: 0x538
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 5830
-  Symbols:   9211
-  CStrings:  5513
+  Symbols:   9218
+  CStrings:  5518
 
Symbols:
+ __ZGVZL15__CSIBVGCLocalevE7localeC
+ __ZZL15__CSIBVGCLocalevE7localeC
+ ___cxa_guard_abort
+ ___cxa_guard_acquire
+ ___cxa_guard_release
+ _newlocale
+ _snprintf_l
Functions:
~ _CUIUncompressDeepmap2ImageData : 1040 -> 1140
~ ___CUIUncompressDeepmap2ImageData_block_invoke : 276 -> 272
~ __ZN24CSIBVGNumericListDecoder11appendValueEd : 172 -> 284
~ _CUIUncompressDeepmapImageData : 1024 -> 1124
~ ___CUIUncompressDeepmapImageData_block_invoke : 220 -> 216
~ sub_1bbcaaacc -> sub_1bac9fbfc : 3340 -> 3344
~ sub_1bbcadf5c -> sub_1baca3090 : 240 -> 384
~ sub_1bbcae04c -> sub_1baca3210 : 384 -> 240
CStrings:
+ "C"
+ "CoreUI: Deepmap 2.0 block length %zu is smaller than its header"
+ "CoreUI: Deepmap 2.0 compressedBytes %llu exceeds block length %zu"
+ "CoreUI: Deepmap block length %zu is smaller than its header"
+ "CoreUI: Deepmap compressedBytes %llu exceeds block length %zu"
```
