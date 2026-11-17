## localspeechrecognition

> `/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_types2`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3610.9.1.0.0
-  __TEXT.__text: 0x1036a4
-  __TEXT.__auth_stubs: 0x28a0
-  __TEXT.__objc_stubs: 0x60a0
-  __TEXT.__objc_methlist: 0x1c54
+3610.12.1.0.0
+  __TEXT.__text: 0x1059fc
+  __TEXT.__auth_stubs: 0x2930
+  __TEXT.__objc_stubs: 0x6180
+  __TEXT.__objc_methlist: 0x1ccc
   __TEXT.__const: 0x18e70
   __TEXT.__objc_classname: 0x10e7
-  __TEXT.__objc_methname: 0x8e05
-  __TEXT.__objc_methtype: 0x22a2
+  __TEXT.__objc_methname: 0x9125
+  __TEXT.__objc_methtype: 0x233d
   __TEXT.__constg_swiftt: 0x5248
   __TEXT.__swift5_typeref: 0x3ada
   __TEXT.__swift5_reflstr: 0x3b13
   __TEXT.__swift5_fieldmd: 0x4fb8
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_assocty: 0x390
-  __TEXT.__oslogstring: 0x3af4
-  __TEXT.__cstring: 0x5098
+  __TEXT.__oslogstring: 0x3dc2
+  __TEXT.__cstring: 0x527d
   __TEXT.__swift5_proto: 0x1270
   __TEXT.__swift5_types: 0x41c
   __TEXT.__swift5_capture: 0x18e4

   __TEXT.__swift_as_cont: 0xf8
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x4e8
-  __TEXT.__unwind_info: 0x6e30
-  __TEXT.__eh_frame: 0x94f0
+  __TEXT.__gcc_except_tab: 0x690
+  __TEXT.__unwind_info: 0x6e90
+  __TEXT.__eh_frame: 0x94d0
   __DATA_CONST.__const: 0x61d0
-  __DATA_CONST.__cfstring: 0x7a0
+  __DATA_CONST.__cfstring: 0x7c0
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x158

   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x1460
-  __DATA_CONST.__got: 0xaf8
+  __DATA_CONST.__auth_got: 0x14a8
+  __DATA_CONST.__got: 0xb00
   __DATA_CONST.__auth_ptr: 0x4f8
   __DATA.__objc_const: 0x5740
-  __DATA.__objc_selrefs: 0x1c98
+  __DATA.__objc_selrefs: 0x1d18
   __DATA.__objc_ivar: 0x9c
   __DATA.__objc_data: 0x2040
   __DATA.__data: 0xea28

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8884
-  Symbols:   20184
-  CStrings:  2250
+  Functions: 8903
+  Symbols:   20214
+  CStrings:  2298
 
Symbols:
+ -[LSRConnection _callerHasPrivilege:forOpenFD:]
+ -[LSRConnection _commitTempFileNamed:inDirectoryFD:toFinalName:]
+ -[LSRConnection _createTempFileInDirectoryFD:tempName:]
+ -[LSRConnection _discardTempFileNamed:inDirectoryFD:]
+ -[LSRConnection _pinnedDirectoryFileDescriptorForURL:]
+ -[LSRConnection _pinnedReadFileDescriptorForURL:]
+ -[LSRLanguageModel appLmNeedsRebuildFD:language:error:]
+ -[LSRLanguageModel createNgramCountsArtifactFromPhraseCountFD:saveToFD:]
+ -[LSRLanguageModel createPhraseCountArtifactWithIdentifier:rawPhraseCountsFD:customPronunciationsFD:saveToFD:]
+ -[LSRLanguageModel trainAppLmFromNgramCountsArtifactFD:forApp:language:appLmArtifactFD:vocabFileFD:appLmArtifactSucceeded:vocabFileSucceeded:]
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/SpeechFramework/install/TempContent/Objects/SpeechRecognition.build/localspeechrecognition.build/Objects-normal/arm64e/LSRUtilities-d4aeff528d555667ea38b8b960cbe3e3.o
+ GCC_except_table165
+ GCC_except_table167
+ GCC_except_table17
+ GCC_except_table185
+ GCC_except_table216
+ GCC_except_table242
+ GCC_except_table35
+ GCC_except_table5
+ GCC_except_table66
+ _OBJC_CLASS_$_NSFileHandle
+ ___142-[LSRLanguageModel trainAppLmFromNgramCountsArtifactFD:forApp:language:appLmArtifactFD:vocabFileFD:appLmArtifactSucceeded:vocabFileSucceeded:]_block_invoke
+ ___142-[LSRLanguageModel trainAppLmFromNgramCountsArtifactFD:forApp:language:appLmArtifactFD:vocabFileFD:appLmArtifactSucceeded:vocabFileSucceeded:]_block_invoke_2
+ _close
+ _fcntl
+ _fstat
+ _lseek
+ _objc_msgSend$_callerHasPrivilege:forOpenFD:
+ _objc_msgSend$createPhraseCountsArtifactFD:version:locale:rawPhraseCountsFD:customPronunciationsFD:saveToFD:
+ _objc_msgSend$initWithFileDescriptor:
+ _objc_msgSend$initWithFileDescriptor:closeOnDealloc:
+ _objc_msgSend$isValidFD:
+ _objc_msgSend$transitionArtifactAtFD:toStage:configPath:dataRoot:estimationRoot:minimize:saveToFD:
+ _objc_msgSend$writeData:
+ _open
+ _openat
+ _renameat
+ _swift_release_x10
+ _unlinkat
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/SpeechFramework/install/TempContent/Objects/SpeechRecognition.build/localspeechrecognition.build/Objects-normal/arm64e/LSRUtilities-d95bf14c0f1b523fd0453ca0d7345700.o
- GCC_except_table152
- GCC_except_table154
- GCC_except_table172
- GCC_except_table203
- GCC_except_table210
- GCC_except_table22
- GCC_except_table4
- GCC_except_table53
CStrings:
+ "%s %@ is not a regular file"
+ "%s Caller lacks %s access to the resolved path of fd %d"
+ "%s Cannot open a nil directory for pinned directory access"
+ "%s Failed to clear O_NONBLOCK for %@: errno=%d"
+ "%s Failed to commit %@ to %@: errno=%d"
+ "%s Failed to create temp output file: errno=%d"
+ "%s Failed to load language model artifact from fd %d"
+ "%s Failed to open %@ for pinned directory access: errno=%d"
+ "%s Failed to open %@ for pinned read: errno=%d"
+ "%s Failed to read ngram counts artifact from fd %d"
+ "%s Failed to resolve path for fd %d: errno=%d"
+ "%s Failed to rewind appLmArtifactFD for re-read: errno=%d"
+ "%s Failed to rewind ngramCountsFD for re-read: errno=%d"
+ "%s Failed to write profile data to fd:%d"
+ "%s Wrote profile data to fd:%d"
+ "-[LSRConnection _callerHasPrivilege:forOpenFD:]"
+ "-[LSRConnection _commitTempFileNamed:inDirectoryFD:toFinalName:]"
+ "-[LSRConnection _createTempFileInDirectoryFD:tempName:]"
+ "-[LSRConnection _pinnedDirectoryFileDescriptorForURL:]"
+ "-[LSRConnection _pinnedReadFileDescriptorForURL:]"
+ "-[LSRLanguageModel appLmNeedsRebuildFD:language:error:]"
+ "-[LSRLanguageModel trainAppLmFromNgramCountsArtifactFD:forApp:language:appLmArtifactFD:vocabFileFD:appLmArtifactSucceeded:vocabFileSucceeded:]"
+ ".lsr-tmp-%@"
+ "B24@0:8i16i20"
+ "B28@0:8r*16i24"
+ "B36@0:8@16i24@28"
+ "B36@0:8@16i24i28i32"
+ "B36@0:8i16@20^@28"
+ "_callerHasPrivilege:forOpenFD:"
+ "_commitTempFileNamed:inDirectoryFD:toFinalName:"
+ "_createTempFileInDirectoryFD:tempName:"
+ "_discardTempFileNamed:inDirectoryFD:"
+ "_pinnedDirectoryFileDescriptorForURL:"
+ "_pinnedReadFileDescriptorForURL:"
+ "appLmNeedsRebuildFD:language:error:"
+ "createNgramCountsArtifactFromPhraseCountFD:saveToFD:"
+ "createPhraseCountArtifactWithIdentifier:rawPhraseCountsFD:customPronunciationsFD:saveToFD:"
+ "createPhraseCountsArtifactFD:version:locale:rawPhraseCountsFD:customPronunciationsFD:saveToFD:"
+ "i24@0:8@16"
+ "i28@0:8i16^@20"
+ "initWithFileDescriptor:"
+ "initWithFileDescriptor:closeOnDealloc:"
+ "isValidFD:"
+ "trainAppLmFromNgramCountsArtifactFD:forApp:language:appLmArtifactFD:vocabFileFD:appLmArtifactSucceeded:vocabFileSucceeded:"
+ "transitionArtifactAtFD:toStage:configPath:dataRoot:estimationRoot:minimize:saveToFD:"
+ "v28@0:8@16i24"
+ "v60@0:8i16@20@28i36i40^B44^B52"
+ "writeData:"
```
