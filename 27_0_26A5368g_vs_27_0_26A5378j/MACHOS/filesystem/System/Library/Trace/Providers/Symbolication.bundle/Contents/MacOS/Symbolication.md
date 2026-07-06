## Symbolication

> `/System/Library/Trace/Providers/Symbolication.bundle/Contents/MacOS/Symbolication`

```diff

-  __TEXT.__text: 0xcac
+  __TEXT.__text: 0xe50
   __TEXT.__auth_stubs: 0x1b0
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0x13c
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0xa0
-  __TEXT.__cstring: 0x58f
+  __TEXT.__cstring: 0x7a1
   __TEXT.__objc_methname: 0x2d0
   __TEXT.__objc_classname: 0x28
   __TEXT.__objc_methtype: 0x1cd
   __TEXT.__unwind_info: 0xb8
   __DATA_CONST.__const: 0x68
-  __DATA_CONST.__cfstring: 0x3a0
+  __DATA_CONST.__cfstring: 0x4e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 19
   Symbols:   52
-  CStrings:  113
+  CStrings:  133
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Functions:
~ sub_114c : 1584 -> 1964
~ sub_177c -> sub_18f8 : 40 -> 80
CStrings:
+ "AppleConnect authentication failed; please sign in to AppleConnect and retry"
+ "AppleConnectClient is not available; install AppleConnect to use BulkSymbolication"
+ "BulkSymbolication failed"
+ "BulkSymbolication is only supported on macOS"
+ "BulkSymbolication returned no results for any library in the trace"
+ "BulkSymbolication timed out"
+ "Failed to create BulkSymbolication job"
+ "Installed AppleConnect does not support OAuth; please update AppleConnect"
+ "Invalid value for option 'method': bulk"
+ "No symbolicatable addresses were found in the trace"

```
