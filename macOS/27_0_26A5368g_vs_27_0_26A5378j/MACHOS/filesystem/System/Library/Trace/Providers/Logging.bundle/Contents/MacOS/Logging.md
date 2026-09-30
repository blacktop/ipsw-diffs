## Logging

> `/System/Library/Trace/Providers/Logging.bundle/Contents/MacOS/Logging`

```diff

-  __TEXT.__text: 0xaab0
+  __TEXT.__text: 0xb074
   __TEXT.__auth_stubs: 0x820
   __TEXT.__objc_stubs: 0x320
-  __TEXT.__objc_methlist: 0x5c8
-  __TEXT.__const: 0x912
-  __TEXT.__cstring: 0x19ea
-  __TEXT.__swift5_typeref: 0x332
+  __TEXT.__objc_methlist: 0x618
+  __TEXT.__const: 0x95e
+  __TEXT.__cstring: 0x1c75
+  __TEXT.__swift5_typeref: 0x338
   __TEXT.__swift5_capture: 0x88
   __TEXT.__objc_methtype: 0x42b
   __TEXT.__objc_methname: 0x61c
-  __TEXT.__constg_swiftt: 0x358
+  __TEXT.__constg_swiftt: 0x394
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_reflstr: 0x2b0
-  __TEXT.__swift5_fieldmd: 0x2e0
-  __TEXT.__objc_classname: 0x236
+  __TEXT.__swift5_fieldmd: 0x2fc
+  __TEXT.__objc_classname: 0x25b
   __TEXT.__swift5_assocty: 0xc0
-  __TEXT.__swift5_proto: 0x60
-  __TEXT.__swift5_types: 0x3c
+  __TEXT.__swift5_proto: 0x64
+  __TEXT.__swift5_types: 0x40
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x3e0
+  __TEXT.__unwind_info: 0x400
   __TEXT.__eh_frame: 0x188
-  __DATA_CONST.__const: 0x598
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__const: 0x5c8
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__auth_got: 0x418
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA.__objc_const: 0x920
+  __DATA.__objc_const: 0x9b0
   __DATA.__objc_selrefs: 0x188
-  __DATA.__objc_data: 0x890
-  __DATA.__data: 0x4b8
+  __DATA.__objc_data: 0x950
+  __DATA.__data: 0x4e8
   __DATA.__common: 0x8
   __DATA.__bss: 0x750
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 371
+  Functions: 388
   Symbols:   92
-  CStrings:  200
+  CStrings:  210
 
Sections:
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA.__objc_selrefs : content changed
CStrings:
+ "(subsystem == \"com.apple.FoundationModels\" AND (category == \"Instrument\" OR category == \"session\" OR category == \"InstrumentSignpost\")) OR (subsystem == \"com.apple.modelmanager\" AND category == \"OSSignPoster\")"
+ "Foundation Models instrumentation"
+ "FoundationModels"
+ "InstrumentSignpost"
+ "Logging.FoundationModelsDataCategory"
+ "The 'FoundationModels' data category contains `os_signpost` instrumentation describing\nFoundation Models session, inference, tool call, and model loading events."
+ "_TtC7Logging28FoundationModelsDataCategory"
+ "com.apple.FoundationModels"
+ "com.apple.modelmanager"
+ "foundation-models"

```
