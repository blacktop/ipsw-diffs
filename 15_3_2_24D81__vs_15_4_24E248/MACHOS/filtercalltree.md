## filtercalltree

> `/usr/bin/filtercalltree`

```diff

-64566.82.1.0.0
-  __TEXT.__text: 0x3d54
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_stubs: 0x700
+64570.34.1.0.0
+  __TEXT.__text: 0x3da4
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__objc_stubs: 0x740
   __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0x148
-  __TEXT.__cstring: 0xfc0
+  __TEXT.__gcc_except_tab: 0x180
+  __TEXT.__cstring: 0x1007
   __TEXT.__oslogstring: 0x533
   __TEXT.__objc_classname: 0x17
-  __TEXT.__objc_methname: 0x4bb
+  __TEXT.__objc_methname: 0x50c
   __TEXT.__unwind_info: 0x138
-  __DATA_CONST.__auth_got: 0x318
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x1c0
-  __DATA_CONST.__cfstring: 0x440
+  __DATA_CONST.__auth_got: 0x310
+  __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__const: 0x190
+  __DATA_CONST.__cfstring: 0x480
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x40
+  __DATA_CONST.__objc_classrefs: 0x30
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x1c0
+  __DATA.__objc_selrefs: 0x1d0
   __DATA.__objc_data: 0x50
   __DATA.__allow_alt_plat: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxcselect.dylib
-  UUID: E55AF0FA-94DA-3B29-8413-258D3E310C1A
-  Functions: 58
+  UUID: 63544DFA-DB1D-36F9-BA1E-5FFCE8FBB46C
+  Functions: 54
   Symbols:   132
-  CStrings:  213
+  CStrings:  217
 
Symbols:
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_NSError
- _OBJC_CLASS_$_VMUProcessDescription
- _strcmp
CStrings:
+ "VMUCallTreeRoot"
+ "caseInsensitiveCompare:"
+ "dictionaryWithObjects:forKeys:count:"
+ "errorWithDomain:code:userInfo:"
+ "initWithCallGraphFile:fileHeader:topFunctionsList:binaryImagesList:error:"
+ "k"
+ "m"
+ "the provided file doesn't contain a valid textual call tree.\n"
- "--"
- "-al"
- "K"
- "M"
- "initWithCallGraphFile:fileHeader:topFunctionsList:binaryImagesList:"
- "isEqualToString:"

```
