## libLogRedirect.dylib

> `/usr/lib/libLogRedirect.dylib`

```diff

-64566.82.1.0.0
-  __TEXT.__text: 0x1f64
+64570.34.1.0.0
+  __TEXT.__text: 0x1f14
   __TEXT.__auth_stubs: 0x260
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x60
   __TEXT.__cstring: 0x462
   __TEXT.__oslogstring: 0x19
-  __TEXT.__unwind_info: 0xc0
+  __TEXT.__unwind_info: 0xb8
   __DATA_CONST.__auth_got: 0x130
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x48
+  __AUTH_CONST.__interpose: 0x50
   __DATA.__data: 0x58
-  __DATA.__interpose: 0x50
   __DATA.__common: 0x18
   __DATA.__bss: 0x218c
   - /usr/lib/libSystem.B.dylib
-  UUID: 998E4189-D950-3FE7-A30F-A4F3993F9D2F
-  Functions: 22
+  UUID: 91CA5582-BCF9-3A01-A981-60C8198A04CA
+  Functions: 21
   Symbols:   107
   CStrings:  61
 
Functions:
~ _resetDyldInsertLibraries : 436 -> 432
~ _LogRedirect_init : 272 -> 276
~ _LogRedirectWrite : 416 -> 404
~ _LogRedirectWritev : 504 -> 492
~ _LogRedirectSendToOSLog : 596 -> 584
~ _LogHook_init : 324 -> 316
~ _LibLogRedirect_InitComplete : 792 -> 788
~ _HookWriteError : 336 -> 332
~ ___LibLogRedirect_OSLogHook_block_invoke : 2756 -> 2748
~ _HookBufferAppendEscapedString : 552 -> 556
- sub_2754

```
