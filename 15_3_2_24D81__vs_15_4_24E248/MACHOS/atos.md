## atos

> `/usr/bin/atos`

```diff

-64566.82.1.0.0
-  __TEXT.__text: 0x6838
+64570.34.1.0.0
+  __TEXT.__text: 0x6964
   __TEXT.__auth_stubs: 0x8b0
   __TEXT.__objc_stubs: 0x8e0
   __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x2ec
-  __TEXT.__cstring: 0x1577
+  __TEXT.__gcc_except_tab: 0x2f0
+  __TEXT.__cstring: 0x156a
   __TEXT.__objc_classname: 0x17
   __TEXT.__oslogstring: 0x5d3
-  __TEXT.__objc_methname: 0x5d0
+  __TEXT.__objc_methname: 0x566
   __TEXT.__unwind_info: 0x198
   __DATA_CONST.__auth_got: 0x468
-  __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x390
-  __DATA_CONST.__cfstring: 0x7a0
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__const: 0x3c0
+  __DATA_CONST.__cfstring: 0x7c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxcselect.dylib
-  UUID: CCD47C97-AAF9-3253-BBC3-4A3410785ADD
-  Functions: 90
-  Symbols:   176
+  UUID: C1F7B50B-6894-35A0-93E4-553EA085D718
+  Functions: 88
+  Symbols:   175
   CStrings:  312
 
Symbols:
- _OBJC_CLASS_$_VMUProcessDescription
CStrings:
+ "Only one of -s, -l, -textExecAddress or -offset can be passed"
+ "Target process:  %@ [%u] (%@)\n"
+ "[-p pid] [-o executable/dSYM] [-f file-of-input-addresses] [-s slide | -l loadAddress | -textExecAddress addr | -offset] [-arch architecture] [-printHeader] [-fullPath] [-inlineFrames] [-d delimiter] [address ...]"
+ "core file"
+ "corpse"
+ "isCore"
+ "live task"
+ "taskIsCorpse"
- "--"
- "-al"
- "Only one of -s, -l or -offset can be passed"
- "Target process:  %@ [%u]\n"
- "[-p pid] [-o executable/dSYM] [-f file-of-input-addresses] [-s slide | -l loadAddress | -offset] [-arch architecture] [-printHeader] [-fullPath] [-inlineFrames] [-d delimiter] [address ...]"
- "addr"
- "initWithTask:getBinariesList:"
- "registerOptionWithLongName:shortName:argumentKind:argumentName:optionDescription:flags:handler:"
- "use instead of load address with kernel-space binaries on arm64(e) devices"

```
