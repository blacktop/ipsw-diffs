## SampleAnalysis

> `/System/Library/PrivateFrameworks/SampleAnalysis.framework/Versions/A/SampleAnalysis`

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
- `__AUTH.__thread_vars`
- `__DATA.__data`

```diff

-436.0.0.0.0
-  __TEXT.__text: 0x11db84
+438.0.0.0.0
+  __TEXT.__text: 0x11da7c
   __TEXT.__objc_methlist: 0x5e34
   __TEXT.__const: 0x328
   __TEXT.__dlopen_cstrs: 0x1ca
   __TEXT.__cstring: 0x19ae0
-  __TEXT.__oslogstring: 0xd1c4
-  __TEXT.__gcc_except_tab: 0x21950
+  __TEXT.__oslogstring: 0xd192
+  __TEXT.__gcc_except_tab: 0x2193c
   __TEXT.__unwind_info: 0x3e08
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0x2df0
   __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0x218
-  __DATA_CONST.__got: 0x470
+  __DATA_CONST.__got: 0x4a0
   __AUTH_CONST.__const: 0x3f30
   __AUTH_CONST.__cfstring: 0xd060
   __AUTH_CONST.__objc_const: 0x100f0
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__auth_got: 0xcc0
-  __AUTH.__objc_data: 0x230
+  __AUTH.__objc_data: 0x50
   __AUTH.__thread_vars: 0x60
   __AUTH.__thread_bss: 0x20
   __DATA.__objc_ivar: 0xe20

   __DATA.__bss: 0x28
   __DATA.__common: 0x4b0
   __DATA_DIRTY.__objc_ivar: 0x10
-  __DATA_DIRTY.__objc_data: 0x22b0
-  __DATA_DIRTY.__bss: 0x4f0
+  __DATA_DIRTY.__objc_data: 0x2490
+  __DATA_DIRTY.__bss: 0x4e8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2998
+  Functions: 2997
   Symbols:   7121
-  CStrings:  3857
+  CStrings:  3856
 
Symbols:
+ GCC_except_table313
+ GCC_except_table594
+ GCC_except_table597
+ GCC_except_table599
+ GCC_except_table603
+ GCC_except_table607
+ GCC_except_table609
+ GCC_except_table611
+ GCC_except_table623
+ GCC_except_table632
+ GCC_except_table637
+ _objc_msgSend$initWithOptions:capacity:
- GCC_except_table595
- GCC_except_table598
- GCC_except_table601
- GCC_except_table605
- GCC_except_table608
- GCC_except_table610
- GCC_except_table613
- GCC_except_table624
- GCC_except_table634
- GCC_except_table638
- ___31-[SASampleStore gatherKextStat]_block_invoke_3
- _objc_msgSend$weakObjectsHashTable
Functions:
~ ___SACachedNSString_block_invoke : 68 -> 76
~ -[SASampleStore handleNonMicrostackshotData:bufSize:statistics:] : 6976 -> 7036
~ ___31-[SASampleStore gatherKextStat]_block_invoke_2 : 724 -> 548
- ___31-[SASampleStore gatherKextStat]_block_invoke_3
CStrings:
- "Unable to convert kextstat output to NSString: %s"
```
