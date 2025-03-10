## VectorSearch

> `/System/Library/PrivateFrameworks/VectorSearch.framework/VectorSearch`

```diff

-38.0.0.0.0
-  __TEXT.__text: 0x65770
-  __TEXT.__auth_stubs: 0x1bd0
+38.1.0.0.0
+  __TEXT.__text: 0x65f3c
+  __TEXT.__auth_stubs: 0x1b60
   __TEXT.__objc_methlist: 0x8d4
-  __TEXT.__const: 0x2718
-  __TEXT.__cstring: 0x4315
-  __TEXT.__constg_swiftt: 0xf90
-  __TEXT.__swift5_typeref: 0x1034
-  __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_reflstr: 0xb55
-  __TEXT.__swift5_fieldmd: 0xcec
-  __TEXT.__swift5_types: 0xe8
+  __TEXT.__const: 0x2760
+  __TEXT.__cstring: 0x43f5
+  __TEXT.__constg_swiftt: 0xf4c
+  __TEXT.__swift5_typeref: 0x100e
+  __TEXT.__swift5_builtin: 0xa0
+  __TEXT.__swift5_reflstr: 0xbe5
+  __TEXT.__swift5_fieldmd: 0xd10
+  __TEXT.__swift5_types: 0xec
   __TEXT.__swift5_capture: 0x694
-  __TEXT.__oslogstring: 0xd74
+  __TEXT.__oslogstring: 0xfc4
   __TEXT.__swift5_proto: 0x184
-  __TEXT.__swift5_protos: 0x1c
+  __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__swift5_mpenum: 0x34
+  __TEXT.__swift5_mpenum: 0x3c
   __TEXT.__swift_as_entry: 0x20
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0x1610
-  __TEXT.__eh_frame: 0x42b0
+  __TEXT.__unwind_info: 0x1620
+  __TEXT.__eh_frame: 0x42b8
   __TEXT.__objc_classname: 0xa6
   __TEXT.__objc_methname: 0x196c
   __TEXT.__objc_methtype: 0x4d6
   __TEXT.__objc_stubs: 0x8e0
-  __DATA_CONST.__got: 0x320
+  __DATA_CONST.__got: 0x318
   __DATA_CONST.__const: 0xc8
-  __DATA_CONST.__objc_classlist: 0x100
+  __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x458
   __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0xdf0
+  __AUTH_CONST.__auth_got: 0xdb8
   __AUTH_CONST.__auth_ptr: 0x4d8
-  __AUTH_CONST.__const: 0x2248
+  __AUTH_CONST.__const: 0x22f8
   __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__objc_const: 0x1b30
+  __AUTH_CONST.__objc_const: 0x1a58
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x2c8
-  __AUTH.__data: 0x188
+  __AUTH.__data: 0x228
   __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x368
-  __DATA.__bss: 0x1480
+  __DATA.__bss: 0x1500
   __DATA_DIRTY.__objc_data: 0x928
-  __DATA_DIRTY.__data: 0x15c8
+  __DATA_DIRTY.__data: 0x1478
   __DATA_DIRTY.__bss: 0x1500
   __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1688
-  Symbols:   258
-  CStrings:  655
+  Functions: 1696
+  Symbols:   257
+  CStrings:  668
 
Symbols:
+ _sqlite3_close
- _sqlite3_close_v2
- _swift_conformsToProtocol2
CStrings:
+ ", and sqlite error message: "
+ ". Extended error code: "
+ "An error explaining that the base tokenizer could not be found."
+ "An error explaining that the tokenizer instance could not be created"
+ "An error explaining that the unicode61wrapper tokenizer could not be created."
+ "Could not create tokenizer instance. SQLite Code: "
+ "Could not create unicode61wrapper Tokenizer. Error: "
+ "Could not create unicode61wrapper. SQLite code: "
+ "Could not find base tokenizer. SQLite Code: "
+ "Failed to close database connection with error code: %d. Error message: %s. Dangling pointer."
+ "SQLExpressionEvaluator: deinitializer"
+ "Unicode61Tokenizer: Could not create unicode61 tokenizer. Error: %d."
+ "Unicode61Tokenizer: Could not find unicode61 tokenizer. Error: %d"
+ "Unicode61Tokenizer: Internal failure during xCreateTokenizer: %d."
+ "Unicode61TokenizerWrapper already added to database connection."
+ "Unicode61Tokenizers: Created successfully."
+ "_TtC12VectorSearch38Unicode61WrapperTokenizerDataReference"
+ "tokenizerDataPointer"
+ "unicode61"
+ "unicode61WrapperCreate: Begin"
+ "unicode61WrapperCreate: Finish"
+ "unicode61WrapperCreate: Malformed pCtx"
+ "unicode61WrapperDelete: Begin"
+ "unicode61WrapperDelete: End"
+ "unicode61WrapperTokenizerDataReference"
- "Failed to close database connection with error code: %d. Error message: %s"
- "Internal error in fts5_tokenizer.xCreate: "
- "Internal error in xFindTokenizer"
- "Internal error: nil tokenizer"
- "Internal failure during xTokenizer: "
- "_TtC12VectorSearchP33_F6F6291BE4184B60FBC77E314B7DB2C923FTS5RegisteredTokenizer"
- "_TtC12VectorSearchP33_F6F6291BE4184B60FBC77E314B7DB2C924FTS5TokenizerConstructor"
- "constructor"
- "db"
- "nil fts5_tokenizer.xCreate"
- "tokenizerPointer"
- "xTokenizer"

```
