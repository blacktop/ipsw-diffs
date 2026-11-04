## HybridDatabase

> `/System/Library/PrivateFrameworks/HybridDatabase.framework/HybridDatabase`

```diff

-60.3.1.0.0
-  __TEXT.__text: 0x7dfbbc
+60.10.0.0.0
+  __TEXT.__text: 0x7dff64
   __TEXT.__init_offsets: 0x3c
-  __TEXT.__gcc_except_tab: 0x53fd8
+  __TEXT.__gcc_except_tab: 0x54008
   __TEXT.__const: 0xe86c0
   __TEXT.__swift5_typeref: 0x920
   __TEXT.__swift5_reflstr: 0x72d

   __TEXT.__constg_swiftt: 0xb1c
   __TEXT.__swift5_fieldmd: 0xb70
   __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__cstring: 0x8b73b
+  __TEXT.__cstring: 0x8b9a7
   __TEXT.__swift5_proto: 0x1ec
   __TEXT.__swift5_types: 0xf8
   __TEXT.__oslogstring: 0x314d
   __TEXT.__swift5_capture: 0x1e0
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1e970
+  __TEXT.__unwind_info: 0x1e998
   __TEXT.__eh_frame: 0x40c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4d6a8
+  __DATA_CONST.__const: 0x4d708
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x20
   __DATA_CONST.__objc_selrefs: 0xc8
   __DATA_CONST.__got: 0x550
-  __AUTH_CONST.__const: 0x396b8
+  __AUTH_CONST.__const: 0x396d8
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0xb70
   __AUTH_CONST.__weak_auth_got: 0x28

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 22305
+  Functions: 22310
   Symbols:   472
-  CStrings:  8620
+  CStrings:  8626
 
CStrings:
+ "60.10"
+ "CREATE REL TABLE {} (FROM {} TO {}) WITH (storage_direction='{}');"
+ "Cannot read file identifier. path: {}. Error: {}"
+ "Database::registerDBFilePath: trying to open file {} which has already been opened by a different HDB object in the process. Please close the other HDB object before opening a new one."
+ "MisuseMultipleDBObjectsOpenForSameFile"
+ "both"
+ "virtual FileIdentifier kuzu::common::FileSystem::getFileIdentifier(const FileInfo &) const"
+ "virtual FileIdentifier kuzu::common::LocalFileSystem::getFileIdentifier(const FileInfo &) const"
+ "void kuzu::common::string_format_detail::stringFormatHelper(std::string &, std::string_view, Arg &&, Args &&...) [Arg = std::string &, Args = <const char *const &>]"
+ "void kuzu::common::string_format_detail::stringFormatHelper(std::string &, std::string_view, Arg &&, Args &&...) [Arg = std::string &, Args = <std::string &, const char *const &>]"
+ "void kuzu::common::string_format_detail::stringFormatHelper(std::string &, std::string_view, Arg &&, Args &&...) [Arg = std::string, Args = <std::string &, std::string &, const char *const &>]"
+ "void kuzu::main::Database::registerDBFilePath(const std::string &)"
- "60.3.1"
- "A term alternative must differ from the original phrase and from the other alternatives of the same query fragment. Got '{}' more than once."
- "CREATE REL TABLE {} (FROM {} TO {}) WITH (storage_direction='fwd');"
- "Query fragments with the same terms must be given the same term alternatives. Got two fragments for '{}' with different alternatives."
- "void kuzu::fts_extension::validateConsistentPhraseAlternatives(const std::vector<PhraseGroup> &)"
- "void kuzu::fts_extension::validateDistinctPhrasesInGroup(const PhraseGroup &)"
```
