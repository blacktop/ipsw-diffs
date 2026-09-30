## AutoBugCaptureCore

> `/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/Versions/A/AutoBugCaptureCore`

```diff

-  __TEXT.__text: 0x799d4
+  __TEXT.__text: 0x799ac
   __TEXT.__objc_methlist: 0x5bcc
-  __TEXT.__cstring: 0x4e53
+  __TEXT.__cstring: 0x4e5f
   __TEXT.__const: 0x290
   __TEXT.__oslogstring: 0xe43b
   __TEXT.__gcc_except_tab: 0xdb4

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x598
-  __DATA_CONST.__got: 0x488
+  __DATA_CONST.__got: 0x4d8
   __AUTH_CONST.__const: 0x1eb0
   __AUTH_CONST.__cfstring: 0x67c0
   __AUTH_CONST.__objc_const: 0xb990

   __AUTH_CONST.__auth_got: 0x758
   __AUTH.__objc_data: 0x7d0
   __DATA.__objc_ivar: 0x634
-  __DATA.__data: 0xc08
+  __DATA.__data: 0xc10
   __DATA.__common: 0x10
   __DATA.__bss: 0xe0
   __DATA_DIRTY.__objc_data: 0x1090

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2268
-  Symbols:   5755
-  CStrings:  3009
+  Symbols:   5756
+  CStrings:  3010
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ _kNetDiagOptDiagsUseGMI
Functions:
~ ___88-[DiagnosticExtensionCaller _getAttachmentsFrom:forBundleID:withParameters:queue:reply:]_block_invoke : 304 -> 300
~ ___88-[DiagnosticExtensionCaller _getAttachmentsFrom:forBundleID:withParameters:queue:reply:]_block_invoke_3 : 720 -> 716
~ -[DiagnosticsController validateActionsDictionary:] : 744 -> 732
~ -[DiagnosticsController validateSettingsDictionary:] : 780 -> 796
~ -[DiagnosticCase _updatePayloadDictionaryArray:] : 1368 -> 1324
~ _netdiag_xpc_type_str : 56 -> 64
CStrings:
+ "diagsusegmi"

```
