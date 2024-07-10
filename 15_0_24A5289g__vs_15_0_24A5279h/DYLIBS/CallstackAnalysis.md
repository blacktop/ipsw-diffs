## CallstackAnalysis

> `/System/Library/PrivateFrameworks/CallstackAnalysis.framework/Versions/A/CallstackAnalysis`

```diff

-79.0.0.0.0
-  __TEXT.__text: 0xb7d4
+78.0.0.0.0
+  __TEXT.__text: 0xb654
   __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__objc_methlist: 0xba4
+  __TEXT.__objc_methlist: 0xb74
   __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0xb4
-  __TEXT.__cstring: 0x1841
+  __TEXT.__cstring: 0x181e
   __TEXT.__unwind_info: 0x1b8
   __TEXT.__objc_classname: 0xb0
-  __TEXT.__objc_methname: 0x3738
+  __TEXT.__objc_methname: 0x3694
   __TEXT.__objc_methtype: 0x284
-  __TEXT.__objc_stubs: 0x1bc0
+  __TEXT.__objc_stubs: 0x1b60
   __DATA_CONST.__got: 0x98
   __DATA_CONST.__const: 0x20
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x800
+  __DATA_CONST.__objc_selrefs: 0x7e0
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x3a0
   __AUTH_CONST.__auth_got: 0xe0
   __AUTH_CONST.__const: 0x190
-  __AUTH_CONST.__cfstring: 0x13a0
-  __AUTH_CONST.__objc_const: 0x17a8
+  __AUTH_CONST.__cfstring: 0x1300
+  __AUTH_CONST.__objc_const: 0x1748
   __AUTH_CONST.__objc_dictobj: 0x8c0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x1a0
+  __DATA.__objc_ivar: 0x198
   __DATA.__data: 0x18
   __DATA.__common: 0x1
   __DATA.__bss: 0x70

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 285
-  Symbols:   760
-  CStrings:  194
+  Functions: 281
+  Symbols:   751
+  CStrings:  189
 
Symbols:
- -[TPCMatchDetails antipatternTrigger]
- -[TPCMatchDetails issueType]
- -[TPCMatchDetails setAntipatternTrigger:]
- -[TPCMatchDetails setIssueType:]
- OBJC_IVAR_$_TPCMatchDetails._antipatternTrigger
- OBJC_IVAR_$_TPCMatchDetails._issueType
- _objc_msgSend$antipatternTrigger
- _objc_msgSend$setAntipatternTrigger:
- _objc_msgSend$setIssueType:
CStrings:
- "Disk write"
- "Hang"
- "Ignore"
- "Launch"
- "None"

```
