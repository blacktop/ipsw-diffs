## watchlistd

> `/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-952.0.1.0.0
-  __TEXT.__text: 0x28e58
+952.10.6.0.0
+  __TEXT.__text: 0x28eac
   __TEXT.__auth_stubs: 0x7a0
-  __TEXT.__objc_stubs: 0x4ec0
+  __TEXT.__objc_stubs: 0x4f00
   __TEXT.__objc_methlist: 0x255c
-  __TEXT.__cstring: 0x4250
+  __TEXT.__cstring: 0x4259
   __TEXT.__oslogstring: 0x2728
   __TEXT.__objc_classname: 0x3fb
   __TEXT.__objc_methtype: 0xf69
-  __TEXT.__objc_methname: 0x5c74
+  __TEXT.__objc_methname: 0x5c96
   __TEXT.__const: 0x118
   __TEXT.__gcc_except_tab: 0xc60
   __TEXT.__unwind_info: 0xcf8

   __DATA_CONST.__auth_got: 0x3e0
   __DATA_CONST.__got: 0x4b8
   __DATA.__objc_const: 0x48c0
-  __DATA.__objc_selrefs: 0x1b20
+  __DATA.__objc_selrefs: 0x1b30
   __DATA.__objc_ivar: 0x26c
   __DATA.__objc_data: 0xaa0
   __DATA.__data: 0x4b0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 924
-  Symbols:   2472
-  CStrings:  1910
+  Symbols:   2474
+  CStrings:  1913
 
Symbols:
+ _objc_msgSend$defaultBagV3
+ _objc_msgSend$prewarmBagV3
+ _objc_msgSend$responseStatusCode
- _objc_msgSend$statusCode
Functions:
~ +[AMSBag(WLKAdditions) wlk_defaultBag] : 260 -> 328
~ -[WLDClientConnection prewarm] : 80 -> 116
~ __54+[WLDPlaybackReporter _decorateVODSummary:completion:]_block_invoke.38 : 720 -> 700
CStrings:
+ "defaultBagV3"
+ "prewarmBagV3"
+ "responseStatusCode"
+ "tricycle"
- "statusCode"
```
