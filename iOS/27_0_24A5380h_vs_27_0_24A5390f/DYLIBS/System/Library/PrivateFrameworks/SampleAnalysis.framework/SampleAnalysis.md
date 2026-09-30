## SampleAnalysis

> `/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`

```diff

-436.0.0.0.0
-  __TEXT.__text: 0x105fc8
+438.0.0.0.0
+  __TEXT.__text: 0x105ecc
   __TEXT.__objc_methlist: 0x5dbc
   __TEXT.__const: 0x2f8
   __TEXT.__dlopen_cstrs: 0x108
   __TEXT.__cstring: 0x18c31
-  __TEXT.__oslogstring: 0xc4de
-  __TEXT.__gcc_except_tab: 0x20614
+  __TEXT.__oslogstring: 0xc4ac
+  __TEXT.__gcc_except_tab: 0x20600
   __TEXT.__unwind_info: 0x3cc0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0x2c18
   __DATA_CONST.__objc_superrefs: 0x2c0
   __DATA_CONST.__objc_arraydata: 0x218
-  __DATA_CONST.__got: 0x400
+  __DATA_CONST.__got: 0x430
   __AUTH_CONST.__const: 0xa80
   __AUTH_CONST.__cfstring: 0xcee0
   __AUTH_CONST.__objc_const: 0xfec8
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__auth_got: 0xbf0
-  __AUTH.__objc_data: 0x230
+  __AUTH.__objc_data: 0x50
   __AUTH.__thread_vars: 0x60
   __AUTH.__thread_bss: 0x20
   __DATA.__objc_ivar: 0xdf8

   __DATA.__bss: 0x28
   __DATA.__common: 0x498
   __DATA_DIRTY.__objc_ivar: 0x10
-  __DATA_DIRTY.__objc_data: 0x2260
-  __DATA_DIRTY.__bss: 0x468
+  __DATA_DIRTY.__objc_data: 0x2440
+  __DATA_DIRTY.__bss: 0x460
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2833
+  Functions: 2832
   Symbols:   6811
-  CStrings:  3716
+  CStrings:  3715
 
Symbols:
+ GCC_except_table274
+ GCC_except_table285
+ GCC_except_table556
+ GCC_except_table559
+ GCC_except_table561
+ GCC_except_table565
+ GCC_except_table569
+ GCC_except_table571
+ GCC_except_table573
+ GCC_except_table592
+ GCC_except_table597
+ _objc_msgSend$initWithOptions:capacity:
- GCC_except_table278
- GCC_except_table557
- GCC_except_table560
- GCC_except_table563
- GCC_except_table567
- GCC_except_table570
- GCC_except_table572
- GCC_except_table575
- GCC_except_table594
- GCC_except_table598
- ___31-[SASampleStore gatherKextStat]_block_invoke_3
- _objc_msgSend$weakObjectsHashTable
Functions:
~ -[SASampleStore handleNonMicrostackshotData:bufSize:statistics:] : 6724 -> 6784
~ ___SACachedNSString_block_invoke : 64 -> 72
~ ___31-[SASampleStore gatherKextStat]_block_invoke_2 : 700 -> 532
- ___31-[SASampleStore gatherKextStat]_block_invoke_3
CStrings:
- "Unable to convert kextstat output to NSString: %s"
```
