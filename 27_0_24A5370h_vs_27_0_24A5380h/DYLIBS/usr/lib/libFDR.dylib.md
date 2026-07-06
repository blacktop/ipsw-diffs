## libFDR.dylib

> `/usr/lib/libFDR.dylib`

```diff

-  __TEXT.__text: 0x8b490
+  __TEXT.__text: 0x8b6dc
   __TEXT.__const: 0x2000
-  __TEXT.__cstring: 0x234aa
+  __TEXT.__cstring: 0x23549
   __TEXT.__gcc_except_tab: 0x34
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__ustring: 0x38
-  __TEXT.__unwind_info: 0x1228
+  __TEXT.__unwind_info: 0x1220
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0x8f0
+  __DATA_CONST.__const: 0x8f8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x28
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x9b8
-  __AUTH_CONST.__cfstring: 0xfa60
+  __AUTH_CONST.__cfstring: 0xfaa0
   __AUTH_CONST.__auth_got: 0xa08
   __DATA.__data: 0x160
-  __DATA.__bss: 0xf0
+  __DATA.__bss: 0xb8
   __DATA_DIRTY.__data: 0x28
-  __DATA_DIRTY.__bss: 0x108
+  __DATA_DIRTY.__bss: 0x140
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4626
-  Symbols:   10086
-  CStrings:  6186
+  Functions: 4632
+  Symbols:   10097
+  CStrings:  6193
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __DATA.__data : content changed
Symbols:
+ _AMFDRDataAddLegacyDataClassesToExport
CStrings:
+ "AMFDRDataAddLegacyDataClassesToExport"
+ "AppendComponentType"
+ "CERTIFY"
+ "CFArrayCreateMutable failed for legacyDataClassesToExport"
+ "dataClass is not a CFStringRef: %@"

```
