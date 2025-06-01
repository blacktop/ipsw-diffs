## SignpostCollection

> `/System/Library/PrivateFrameworks/SignpostCollection.framework/SignpostCollection`

```diff

-121.0.0.0.0
-  __TEXT.__text: 0x56cc
-  __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_methlist: 0x35c
+125.0.0.0.0
+  __TEXT.__text: 0x5d94
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__objc_methlist: 0x374
   __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0x23c
-  __TEXT.__cstring: 0x62c
+  __TEXT.__gcc_except_tab: 0x270
+  __TEXT.__cstring: 0x8f1
   __TEXT.__oslogstring: 0x2d6
-  __TEXT.__unwind_info: 0x19c
+  __TEXT.__unwind_info: 0x1bc
   __TEXT.__objc_classname: 0xaf
-  __TEXT.__objc_methname: 0x1a8c
+  __TEXT.__objc_methname: 0x1b72
   __TEXT.__objc_methtype: 0x21a
-  __TEXT.__objc_stubs: 0x1c40
-  __DATA_CONST.__got: 0x20
+  __TEXT.__objc_stubs: 0x1d40
+  __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x310
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x338
-  __DATA_CONST.__objc_selrefs: 0x7a0
-  __AUTH_CONST.__cfstring: 0x480
+  __DATA_CONST.__objc_selrefs: 0x7e8
+  __DATA_CONST.__objc_classrefs: 0xc0
+  __DATA_CONST.__objc_superrefs: 0x10
+  __AUTH_CONST.__cfstring: 0x600
   __AUTH_CONST.__objc_const: 0x210
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__auth_got: 0x2b0
+  __AUTH_CONST.__auth_got: 0x2e8
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_classrefs: 0xb0
-  __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x34
+  __DATA.__data: 0x8
   __DATA.__bss: 0x48
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ktrace.framework/ktrace
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C1147B94-3201-3FFE-AA6E-76FDCA66BF4A
-  Functions: 118
-  Symbols:   657
-  CStrings:  422
+  UUID: C9EDB8B0-4DE9-3B57-A733-807B39123E34
+  Functions: 122
+  Symbols:   683
+  CStrings:  455
 
Symbols:
+ -[SignpostSupportObjectExtractor(TraceReading) _processTraceFileWithPath:startDate:endDate:errorOut:]
+ -[SignpostSupportObjectExtractor(TraceReading) _processTraceUsingKtraceLoggingDataSource:startDate:endDate:errorOut:]
+ -[SignpostSupportObjectExtractor(TraceReading) processTraceFileWithPath:startDate:endDate:errorOut:]
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_EHTYPE_$_NSException
+ _SCWriteLoggingAppleTrace
+ _SCWriteLoggingAppleTraceWithPredicate
+ ___101-[SignpostSupportObjectExtractor(TraceReading) _processTraceFileWithPath:startDate:endDate:errorOut:]_block_invoke
+ _kSCAppleTraceFileExtension
+ _ktrace_file_append_log_content_from_store
+ _ktrace_file_create
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_msgSend$_processTraceFileWithPath:startDate:endDate:errorOut:
+ _objc_msgSend$_processTraceUsingKtraceLoggingDataSource:startDate:endDate:errorOut:
+ _objc_msgSend$compare:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$pathExtension
+ _objc_msgSend$predicateWithFormat:
+ _objc_msgSend$reason
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x24
+ _objc_retain_x3
- -[SignpostSupportObjectExtractor(TraceReading) _processTraceUsingKtraceLoggingDataSource:errorOut:]
- ___82-[SignpostSupportObjectExtractor(TraceReading) processTraceFileWithPath:errorOut:]_block_invoke
- _objc_msgSend$_processTraceUsingKtraceLoggingDataSource:errorOut:
CStrings:
+ "'startDate' >= 'endDate"
+ "Could not read from input log archive '%@'. Confirm that that file exists and that you have sufficient permissions to read it."
+ "Could not read from local store. Confirm that you have the 'com.apple.private.logging.diagnostic' entitlement."
+ "Failed to create output logging AppleTrace file due to error: %s"
+ "Failed to create predicate for predicate string: '%@' due to reason '%@'. Please refer to the output of 'log help predicates' for more information on valid predicates."
+ "Failed to create trace file due to error: %s"
+ "Output path '%@' already exists"
+ "Output path '%@' does not have the required extension (*.%@)"
+ "Start date > end date"
+ "Unknown failure"
+ "_processTraceFileWithPath:startDate:endDate:errorOut:"
+ "_processTraceUsingKtraceLoggingDataSource:startDate:endDate:errorOut:"
+ "atrc"
+ "compare:"
+ "defaultManager"
+ "fileExistsAtPath:"
+ "fileURLWithPath:"
+ "nil output loggingAppleTracePath"
+ "pathExtension"
+ "predicateWithFormat:"
+ "processTraceFileWithPath:startDate:endDate:errorOut:"
+ "reason"
- "_processTraceUsingKtraceLoggingDataSource:errorOut:"

```
