## IOMFBDiagnose

> `/usr/bin/IOMFBDiagnose`

```diff

-  __TEXT.__text: 0xfe88
+  __TEXT.__text: 0x10018
   __TEXT.__auth_stubs: 0x2b0
   __TEXT.__objc_stubs: 0xe0
   __TEXT.__const: 0xab4
-  __TEXT.__cstring: 0x7d55
+  __TEXT.__cstring: 0x7e4d
   __TEXT.__objc_methname: 0x62
   __TEXT.__unwind_info: 0x1d8
-  __DATA_CONST.__const: 0xcd8
+  __DATA_CONST.__const: 0xd00
   __DATA_CONST.__cfstring: 0xc00
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x160

   - /usr/lib/libobjc.A.dylib
   Functions: 118
   Symbols:   56
-  CStrings:  1375
+  CStrings:  1381
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__objc_selrefs : content changed
Functions:
~ sub_1000100c4 : 716 -> 1116
CStrings:
+ "        Ambient: Range [%.2f, %.2f], Tolerance %.2f%s\n"
+ "        Brightness: Range [%.2f, %.2f], Tolerance %.2f%s\n"
+ "        Temperature: Range [%.2f, %.2f], Tolerance %.2f%s\n"
+ "    Stability Config:"
+ "%"
+ "NotifyPowerToTrustedServices"
+ "NotifyRunModeChangeSCLCursor"
- "%g%s "

```
