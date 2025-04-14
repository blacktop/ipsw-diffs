## SpotlightEmbedding

> `/System/Library/PrivateFrameworks/SpotlightEmbedding.framework/SpotlightEmbedding`

```diff

-2333.41.0.1.0
-  __TEXT.__text: 0x3e48
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_methlist: 0x2bc
-  __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x3c5
-  __TEXT.__gcc_except_tab: 0x14c
-  __TEXT.__oslogstring: 0x446
-  __TEXT.__unwind_info: 0x148
-  __TEXT.__objc_classname: 0x4d
-  __TEXT.__objc_methname: 0xa14
-  __TEXT.__objc_methtype: 0x1b2
-  __TEXT.__objc_stubs: 0xb20
-  __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x248
-  __DATA_CONST.__objc_classlist: 0x20
+2333.47.0.0.0
+  __TEXT.__text: 0x5258
+  __TEXT.__auth_stubs: 0x420
+  __TEXT.__objc_methlist: 0x36c
+  __TEXT.__const: 0xc0
+  __TEXT.__cstring: 0x4e6
+  __TEXT.__gcc_except_tab: 0x230
+  __TEXT.__oslogstring: 0x5bd
+  __TEXT.__unwind_info: 0x178
+  __TEXT.__objc_classname: 0x67
+  __TEXT.__objc_methname: 0xc79
+  __TEXT.__objc_methtype: 0x1c7
+  __TEXT.__objc_stubs: 0xea0
+  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__const: 0x268
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x350
-  __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1c8
-  __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x320
-  __AUTH_CONST.__objc_const: 0x520
+  __DATA_CONST.__objc_selrefs: 0x440
+  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_arraydata: 0x10
+  __AUTH_CONST.__auth_got: 0x220
+  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__cfstring: 0x480
+  __AUTH_CONST.__objc_const: 0x610
   __AUTH_CONST.__objc_intobj: 0x30
-  __DATA.__objc_ivar: 0x3c
+  __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__objc_floatobj: 0x10
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x44
+  __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__bss: 0x50
+  __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 79
-  Symbols:   174
-  CStrings:  223
+  - /usr/lib/libtailspin.dylib
+  Functions: 97
+  Symbols:   217
+  CStrings:  281
 
Symbols:
+ _CFPreferencesGetAppBooleanValue
+ _NSFileModificationDate
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$_NSConstantFloatNumber
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_SPEmbeddingTailspinDumper
+ _OBJC_METACLASS_$_SPEmbeddingTailspinDumper
+ _TSPDumpOptions_Symbolicate
+ ___kCFBooleanFalse
+ _close
+ _flock
+ _isAppleInternalInstall
+ _kCFPreferencesAnyApplication
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_exception_rethrow
+ _objc_terminate
+ _open
+ _tailspin_dump_output_with_options_sync
+ _unlink
CStrings:
+ "%@%@%@"
+ "%@_"
+ ".tailspin"
+ "/private/var/mobile/Library/Logs/CrashReporter/DiagnosticLogs/Search"
+ "@\"NSDate\""
+ "A recent tailspin exists. Skipping dump."
+ "B20@0:8i16"
+ "Failed to capture tailspin at %@"
+ "Failed to create tailsipin directory: %@"
+ "Failed to open tailspin file at %@"
+ "Failed to remove old tailspin file at %@: %@"
+ "Failed to remove outdated dump file at %@: %@"
+ "SPEmbeddingTailspinDumper"
+ "SpotlightEmbeddingGenTimeoutTailspin"
+ "T@\"NSDate\",&,N,V_latestDumpDate"
+ "Tailspin"
+ "Tailspin captured at %@"
+ "Unable to acquire tailspin lock on file %@"
+ "Unable to open tailspin lock file at %@"
+ "[qid=%ld] Result marked as safe by CLIP Safety Model with confidence score : %f (threshold:%f language:%@)"
+ "[qid=%ld] Result marked as unsafe by CLIP Safety Models with confidence score : %f (threshold:%f language:%@)"
+ "_dumpQueue"
+ "_latestDumpDate"
+ "array"
+ "attributesOfItemAtPath:error:"
+ "canDump"
+ "cleanupOldDumps"
+ "com.apple.SpotlightEmbedding.tailspinDump"
+ "compare:"
+ "contentsOfDirectoryAtPath:error:"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "currentLocale"
+ "date"
+ "defaultManager"
+ "dump"
+ "dumpTailspinSync:"
+ "fileExistsAtPath:"
+ "fileSystemRepresentation"
+ "hasSuffix:"
+ "languageCode"
+ "latestDumpDate"
+ "lockFilePath"
+ "objectForKeyedSubscript:"
+ "path"
+ "processInfo"
+ "processName"
+ "q24@?0@\"NSDictionary\"8@\"NSDictionary\"16"
+ "removeItemAtPath:error:"
+ "setDateFormat:"
+ "setLatestDumpDate:"
+ "sortUsingComparator:"
+ "stringByAppendingPathComponent:"
+ "stringFromDate:"
+ "tailspin.lock"
+ "tailspinDirectory"
+ "tailspinPrefix"
+ "timeIntervalSinceDate:"
+ "yyyyMMdd_HHmmss"
+ "zh"
- "[qid=%ld] Result marked as safe by CLIP Safety Model with confidence score : %f"
- "[qid=%ld] Result marked as unsafe by CLIP Safety Model with confidence score : %f"

```
