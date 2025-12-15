## libacmobileshim.dylib

> `/usr/lib/libacmobileshim.dylib`

```diff

-25.0.0.0.0
-  __TEXT.__text: 0x3c820
-  __TEXT.__auth_stubs: 0xac0
+27.0.0.0.0
+  __TEXT.__text: 0x3c90c
+  __TEXT.__auth_stubs: 0xb20
   __TEXT.__objc_methlist: 0x7bd8
   __TEXT.__const: 0x1b0
-  __TEXT.__gcc_except_tab: 0x5c4
-  __TEXT.__cstring: 0xc6e6
+  __TEXT.__gcc_except_tab: 0x5d0
+  __TEXT.__cstring: 0xc729
   __TEXT.__ustring: 0x23dac
-  __TEXT.__unwind_info: 0x12e0
+  __TEXT.__unwind_info: 0x12f0
   __TEXT.__objc_classname: 0x1321
   __TEXT.__objc_methname: 0xc9da
   __TEXT.__objc_methtype: 0x33ce

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x368
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x570
+  __AUTH_CONST.__auth_got: 0x5a0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x12b60
   __AUTH_CONST.__objc_const: 0x174a8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0BB69876-DEC3-37CF-BC31-8384FCBE0FD2
-  Functions: 1937
-  Symbols:   7418
-  CStrings:  6545
+  UUID: B91C3A9C-343A-3F8B-803C-C33E65A26F98
+  Functions: 1939
+  Symbols:   7428
+  CStrings:  6548
 
Symbols:
+ _CFRunLoopAddSource
+ _CFRunLoopRemoveSource
+ _CFRunLoopSourceCreate
+ _CFRunLoopSourceInvalidate
+ _CFRunLoopSourceSignal
+ _CFRunLoopStop
+ __StopRunLoopPerform
+ __StopRunLoopPerform.cold.1
+ ___block_descriptor_80_e8_32r40r_e28_v24?0"NSData"8"NSError"16lr32l8r40l8
+ ___block_descriptor_96_e8_32r40r_e5_v8?0lr32l8r40l8
- ___block_descriptor_72_e8_32r40r_e28_v24?0"NSData"8"NSError"16lr32l8r40l8
- ___block_descriptor_88_e8_32r40r_e5_v8?0lr32l8r40l8
CStrings:
+ "ACMDelegate.m"
+ "_StopRunLoopPerform"
+ "runLoop == CFRunLoopGetCurrent()"

```
