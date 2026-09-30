## NetworkQuality

> `/System/Library/PrivateFrameworks/NetworkQuality.framework/NetworkQuality`

```diff

-194.0.3.0.0
-  __TEXT.__text: 0x193a4
+194.40.3.0.0
+  __TEXT.__text: 0x19440
   __TEXT.__auth_stubs: 0xb80
   __TEXT.__objc_methlist: 0x1734
   __TEXT.__const: 0x188
   __TEXT.__gcc_except_tab: 0x538
   __TEXT.__cstring: 0x253f
-  __TEXT.__oslogstring: 0x177a
+  __TEXT.__oslogstring: 0x17bf
   __TEXT.__unwind_info: 0x4e0
   __TEXT.__objc_classname: 0x344
-  __TEXT.__objc_methname: 0x4014
+  __TEXT.__objc_methname: 0x4028
   __TEXT.__objc_methtype: 0xcd8
   __TEXT.__objc_stubs: 0x34c0
   __DATA_CONST.__got: 0x190

   __AUTH_CONST.__auth_got: 0x5d0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x19e0
-  __AUTH_CONST.__objc_const: 0x37b0
+  __AUTH_CONST.__objc_const: 0x37d0
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x7d0
-  __DATA.__objc_ivar: 0x3c8
+  __DATA.__objc_ivar: 0x3cc
   __DATA.__data: 0x360
   __DATA.__bss: 0x20
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AC9F3122-C651-30F4-84B5-3DFAFE50F91A
+  UUID: A67345D1-E27C-33C3-B69D-5D5CE95348CF
   Functions: 567
-  Symbols:   2333
-  CStrings:  1636
+  Symbols:   2334
+  CStrings:  1638
 
Symbols:
+ _OBJC_IVAR_$_NetworkQualityExecutions._drainingInProgress
Functions:
~ -[NetworkQualityExecutions initWithConfiguration:] : 428 -> 432
~ -[NetworkQualityExecutions drain] : 1308 -> 1436
~ ___33-[NetworkQualityExecutions drain]_block_invoke.51 : 416 -> 424
~ ___33-[NetworkQualityExecutions drain]_block_invoke.55 : 416 -> 424
~ ___33-[NetworkQualityExecutions drain]_block_invoke.56 : 416 -> 424
CStrings:
+ "%s:%u - [Staging] Drain already in progress, ignoring duplicate call"
+ "_drainingInProgress"

```
