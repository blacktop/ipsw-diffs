## libFDR.dylib

> `/usr/lib/libFDR.dylib`

```diff

-  __TEXT.__text: 0x8b08c
+  __TEXT.__text: 0x8b2d8
   __TEXT.__const: 0x2008
-  __TEXT.__cstring: 0x235a2
+  __TEXT.__cstring: 0x23641
   __TEXT.__gcc_except_tab: 0x34
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__ustring: 0x38

   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0x800
+  __DATA_CONST.__const: 0x808
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x28
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xad8
-  __AUTH_CONST.__cfstring: 0xfa80
+  __AUTH_CONST.__cfstring: 0xfac0
   __AUTH_CONST.__auth_got: 0xa10
   __DATA.__objc_classrefs: 0x10
   __DATA.__data: 0x160
-  __DATA.__bss: 0xf0
+  __DATA.__bss: 0xd8
   __DATA_DIRTY.__data: 0x28
-  __DATA_DIRTY.__bss: 0x108
+  __DATA_DIRTY.__bss: 0x120
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4625
-  Symbols:   5542
-  CStrings:  6190
+  Functions: 4631
+  Symbols:   5548
+  CStrings:  6197
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __DATA.__objc_classrefs : content changed
~ __DATA.__data : content changed
Symbols:
+ AMFDRDataAddLegacyDataClassesToExport
+ _AMFDRDataAddLegacyDataClassesToExport
CStrings:
+ "AMFDRDataAddLegacyDataClassesToExport"
+ "AppendComponentType"
+ "CERTIFY"
+ "CFArrayCreateMutable failed for legacyDataClassesToExport"
+ "dataClass is not a CFStringRef: %@"

```
