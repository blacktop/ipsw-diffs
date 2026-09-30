## iOSDiagnostics

> `/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iOSDiagnostics`

```diff

-  __TEXT.__text: 0x5414
-  __TEXT.__objc_methlist: 0x9fc
+  __TEXT.__text: 0x55dc
+  __TEXT.__objc_methlist: 0xa1c
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0xb07
-  __TEXT.__oslogstring: 0x402
-  __TEXT.__gcc_except_tab: 0xa8
+  __TEXT.__oslogstring: 0x4f5
+  __TEXT.__gcc_except_tab: 0xb8
   __TEXT.__unwind_info: 0x208
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x700
+  __DATA_CONST.__objc_selrefs: 0x718
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__got: 0x140
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x5a0
-  __AUTH_CONST.__objc_const: 0x1ba0
+  __AUTH_CONST.__objc_const: 0x1bb8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x2d0

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 188
-  Symbols:   893
-  CStrings:  133
+  Functions: 191
+  Symbols:   899
+  CStrings:  138
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
- ___49-[DADiagnosticsRemoteRunner _establishConnection]_block_invoke_3
CStrings:
+ "Connection successfully established to remote runner service"
+ "Establishing connection to remote runner service"
+ "XPC connection to remote runner failed: %@"
+ "XPC connection to remote runner not established"
+ "XPC connection to remote runner timed out"

```
