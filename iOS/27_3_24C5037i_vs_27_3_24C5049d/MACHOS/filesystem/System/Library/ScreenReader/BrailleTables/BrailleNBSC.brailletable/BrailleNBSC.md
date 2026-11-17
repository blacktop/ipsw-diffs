## BrailleNBSC

> `/System/Library/ScreenReader/BrailleTables/BrailleNBSC.brailletable/BrailleNBSC`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-16.0.0.0.0
-  __TEXT.__text: 0x140dc
-  __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_stubs: 0x320
+19.0.0.0.0
+  __TEXT.__text: 0x1497c
+  __TEXT.__auth_stubs: 0x460
+  __TEXT.__objc_stubs: 0x3a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x22c
-  __TEXT.__cstring: 0x28b
-  __TEXT.__const: 0x1290
-  __TEXT.__ustring: 0x35e
-  __TEXT.__gcc_except_tab: 0x338
-  __TEXT.__objc_methname: 0x4e2
-  __TEXT.__oslogstring: 0x1be
+  __TEXT.__objc_methlist: 0x254
+  __TEXT.__cstring: 0x29a
+  __TEXT.__const: 0x12a8
+  __TEXT.__ustring: 0x384
+  __TEXT.__gcc_except_tab: 0x418
+  __TEXT.__objc_methname: 0x5b5
+  __TEXT.__oslogstring: 0x2a8
   __TEXT.__objc_classname: 0x36
-  __TEXT.__objc_methtype: 0x24b
-  __TEXT.__unwind_info: 0x318
+  __TEXT.__objc_methtype: 0x287
+  __TEXT.__unwind_info: 0x348
   __DATA_CONST.__const: 0x60
-  __DATA_CONST.__cfstring: 0x260
+  __DATA_CONST.__cfstring: 0x2e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0x20
-  __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x210
+  __DATA_CONST.__objc_arraydata: 0x38
+  __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA_CONST.__auth_got: 0x240
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x2e0
-  __DATA.__objc_selrefs: 0x1c8
-  __DATA.__objc_ivar: 0x14
+  __DATA.__objc_const: 0x310
+  __DATA.__objc_selrefs: 0x1f8
+  __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x8ae0
+  __DATA.__data: 0x90d0
   __DATA.__common: 0x83060
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 153
-  Symbols:   241
-  CStrings:  156
+  Functions: 161
+  Symbols:   250
+  CStrings:  174
 
Symbols:
+ _NBSCDefaultMaxChunkLength
+ __Z5EChk3Pci
+ __Z5EChk4Pci
+ __Z5EChk6Pci
+ __Z5g2SetPhw
+ __Z6UebSetPhw
+ __Z8Eiji1To2PwS_PtS0_i
+ __Z9IsEijiTo2PcPhii
+ _getpwuid
+ _getuid
+ _objc_retain_x19
+ _objc_retain_x28
+ _strncmp
+ _wmemmove
- __Z5EChk3Pc
- __Z5EChk4Pc
- __Z5EChk6Pc
- __Z8Eiji1To2PwS_PtS0_
- __Z9IsEijiTo2PcPhi
CStrings:
+ "\n\r\u2028\u2029。．！？!?"
+ " \t\u3000"
+ "%C"
+ "/Library/Accessibility/ktoa_u_kwa_v7.dic"
+ "/var/mobile"
+ "B72@0:8@16{_NSRange=QQ}24{_NSRange=QQ}40@56@64"
+ "NBSC Braille for text: Init failed: can't open the Kanji dictionary ~/Library/Accessibility/ktoa_u_kwa_v*.dic. scrod unzips it from ktoa_u_kwa in this bundle when it launches; the version scrod writes must match the one in KTOAU.CPP."
+ "Q"
+ "TQ,N,V_maxChunkLength"
+ "_appendPrintBrailleForText:range:keepingRange:toBraille:locationMap:"
+ "_maxChunkLength"
+ "ally"
+ "appendFormat:"
+ "ation"
+ "maxChunkLength"
+ "rangeOfComposedCharacterSequenceAtIndex:"
+ "rangeOfString:"
+ "setMaxChunkLength:"
+ "v24@0:8Q16"
+ "、，,"
- "/Library/Accessibility/ktoa_u_kwa_v6.dic"
- "var/mobile"
```
