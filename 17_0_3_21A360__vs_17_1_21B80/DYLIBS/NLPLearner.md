## NLPLearner

> `/System/Library/PrivateFrameworks/NLPLearner.framework/NLPLearner`

```diff

-60.0.0.0.0
-  __TEXT.__text: 0xd42c
-  __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_methlist: 0x950
+61.0.0.0.0
+  __TEXT.__text: 0xdde4
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__objc_methlist: 0x964
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0xc58
-  __TEXT.__oslogstring: 0xb81
+  __TEXT.__cstring: 0xcfe
+  __TEXT.__oslogstring: 0xc8b
   __TEXT.__ustring: 0x58
   __TEXT.__gcc_except_tab: 0xbf4
-  __TEXT.__unwind_info: 0x520
+  __TEXT.__unwind_info: 0x53c
   __TEXT.__eh_frame: 0x74
   __TEXT.__objc_classname: 0x235
-  __TEXT.__objc_methname: 0x1dfd
+  __TEXT.__objc_methname: 0x1ebb
   __TEXT.__objc_methtype: 0x39d
-  __TEXT.__objc_stubs: 0x1ea0
+  __TEXT.__objc_stubs: 0x1fa0
   __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__const: 0x390
   __DATA_CONST.__objc_classlist: 0x88

   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xd78
-  __DATA_CONST.__objc_selrefs: 0x878
-  __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0xb40
+  __DATA_CONST.__objc_selrefs: 0x8b8
+  __DATA_CONST.__objc_arraydata: 0xb8
+  __AUTH_CONST.__const: 0x100
+  __AUTH_CONST.__cfstring: 0xc60
   __AUTH_CONST.__objc_const: 0x8b0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x140
-  __AUTH_CONST.__auth_got: 0x428
+  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__auth_got: 0x438
   __AUTH.__objc_data: 0x550
-  __DATA.__objc_classrefs: 0x1a8
+  __DATA.__objc_classrefs: 0x1b0
   __DATA.__objc_superrefs: 0x48
   __DATA.__objc_ivar: 0xb0
   __DATA.__data: 0xc0
-  __DATA.__bss: 0xa8
+  __DATA.__bss: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 322
-  Symbols:   1426
-  CStrings:  666
+  Functions: 331
+  Symbols:   1464
+  CStrings:  687
 
Symbols:
+ +[NLPLearnerACTShadowEvaluator actParamFilesAtPath:]
+ +[NLPLearnerACTShadowEvaluator actParamFilesAtPath:].cold.1
+ +[NLPLearnerACTShadowEvaluator actParamFilesAtPath:].cold.2
+ -[NLPLearnerACTShadowEvaluator runACTWithConfig:data:]
+ -[NLPLearnerACTShadowEvaluator runACTWithConfig:data:].cold.1
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSPredicate
+ ___54-[NLPLearnerACTShadowEvaluator runACTWithConfig:data:]_block_invoke
+ ___block_literal_global.102
+ ___block_literal_global.97
+ ___overrideWordErrorCountForMetrics_block_invoke
+ ___supportedMetrics_block_invoke
+ __unnamed_array_storage.95
+ __unnamed_array_storage.99
+ _objc_msgSend$URLByAppendingPathComponent:
+ _objc_msgSend$actParamFilesAtPath:
+ _objc_msgSend$contentsOfDirectoryAtPath:error:
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$isEqual:
+ _objc_msgSend$predicateWithFormat:
+ _objc_msgSend$runACTWithConfig:data:
+ _objc_msgSend$stringByDeletingPathExtension
+ _objc_opt_new
+ _objc_retain_x28
+ _overrideWordErrorCountForMetrics.onceToken
+ _overrideWordErrorCountForMetrics.overrideWordErrorCountForMetrics
+ _supportedMetrics
+ _supportedMetrics.onceToken
+ _supportedMetrics.supportedMetrics
- ___81-[NLPLearnerACTShadowEvaluator evaluateModel:onRecords:options:completion:error:]_block_invoke
- __unnamed_array_storage.20
CStrings:
+ "%@%@"
+ "AverageJoanna"
+ "Cannot get list of act param files in : %@ with error: %@"
+ "Cannot load act param files in : %@"
+ "Cannot load params file for ACT evaluation"
+ "CorrectedAway"
+ "In the ACT result for Params: %@, Key: %@, expected Value: %@ where as actual Value: %@"
+ "InsertedCharacterCount"
+ "KSR"
+ "Run ACT with params : %@"
+ "The specified params file name is : %@ but it should be %@"
+ "TouchErrorRecovery"
+ "URLByAppendingPathComponent:"
+ "WordErrorCount"
+ "actParamFilesAtPath:"
+ "contentsOfDirectoryAtPath:error:"
+ "filteredArrayUsingPredicate:"
+ "pathExtension MATCHES 'json'"
+ "predicateWithFormat:"
+ "runACTWithConfig:data:"
+ "stringByDeletingPathExtension"

```
