## MediaAnalysisServices

> `/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices`

```diff

-405.3.1.0.0
-  __TEXT.__text: 0x3d088
+415.5.1.0.0
+  __TEXT.__text: 0x3d07c
   __TEXT.__auth_stubs: 0x8e0
   __TEXT.__objc_methlist: 0x4c9c
-  __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x366c
+  __TEXT.__const: 0x148
+  __TEXT.__cstring: 0x3670
   __TEXT.__gcc_except_tab: 0x4834
   __TEXT.__oslogstring: 0x2349
   __TEXT.__dlopen_cstrs: 0x417

   __TEXT.__objc_methtype: 0x2404
   __TEXT.__objc_stubs: 0x2720
   __DATA_CONST.__got: 0x4d8
-  __DATA_CONST.__const: 0xae0
+  __DATA_CONST.__const: 0xaf0
   __DATA_CONST.__objc_classlist: 0x410
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x3d8
   __AUTH_CONST.__auth_got: 0x488
   __AUTH_CONST.__const: 0x318
-  __AUTH_CONST.__cfstring: 0x4b40
+  __AUTH_CONST.__cfstring: 0x4b60
   __AUTH_CONST.__objc_const: 0x9c98
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0x12c0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 018C2F4C-704B-310B-83FF-474D3742AEFF
+  UUID: EF64983C-7EFC-37F9-B655-17AE3C439F52
   Functions: 1649
   Symbols:   5950
-  CStrings:  3134
+  CStrings:  3136
 
Functions:
~ +[MADTextInput csuTokenizerRevision] : 52 -> 56
~ -[MADImageEmbeddingRequest init] : 160 -> 156
~ -[MADTextTokenizationRequest init] : 124 -> 120
~ +[MADTextTokenizationRequest maxTokenSize] : 108 -> 104
~ -[MADTextEmbeddingRequest init] : 136 -> 132
CStrings:
+ "MD8"
+ "SearchUnifiedEmbeddingMD8"
- "SearchUnifiedEmbeddingMD7"

```
