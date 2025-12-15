## DumpPanic

> `/usr/libexec/DumpPanic`

```diff

-373.60.3.0.0
-  __TEXT.__text: 0x26580
-  __TEXT.__auth_stubs: 0x1000
+373.80.4.0.0
+  __TEXT.__text: 0x268c4
+  __TEXT.__auth_stubs: 0x1030
   __TEXT.__objc_stubs: 0x2360
-  __TEXT.__objc_methlist: 0x730
+  __TEXT.__objc_methlist: 0x740
   __TEXT.__const: 0x2e2
-  __TEXT.__cstring: 0x2d73
-  __TEXT.__objc_methname: 0x1da5
+  __TEXT.__cstring: 0x2f31
+  __TEXT.__objc_methname: 0x1db7
   __TEXT.__constg_swiftt: 0x70
   __TEXT.__swift5_typeref: 0x5b
   __TEXT.__swift5_reflstr: 0x1b
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__oslogstring: 0x498e
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0xad0
+  __TEXT.__gcc_except_tab: 0xad4
   __TEXT.__ustring: 0x1c6
   __TEXT.__objc_classname: 0xed
   __TEXT.__objc_methtype: 0x456
-  __TEXT.__unwind_info: 0x600
-  __DATA_CONST.__auth_got: 0x810
-  __DATA_CONST.__got: 0x260
+  __TEXT.__unwind_info: 0x610
+  __DATA_CONST.__auth_got: 0x828
+  __DATA_CONST.__got: 0x278
   __DATA_CONST.__auth_ptr: 0x68
   __DATA_CONST.__const: 0x7f0
   __DATA_CONST.__cfstring: 0x2e00

   __DATA.__objc_selrefs: 0x980
   __DATA.__objc_ivar: 0xd8
   __DATA.__objc_data: 0x500
-  __DATA.__data: 0x170
-  __DATA.__bss: 0xac0
+  __DATA.__data: 0x190
+  __DATA.__bss: 0xaa0
   __INFO_FILTER.__disable: 0x0
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: E883659D-396D-39DB-80FE-BFCECE123EB2
-  Functions: 509
-  Symbols:   364
-  CStrings:  1695
+  UUID: 9E114618-9254-3DDA-A33D-D93556BAC3D1
+  Functions: 514
+  Symbols:   370
+  CStrings:  1717
 
Symbols:
+ _$s15CoreDiagnostics16DiagnosticReportV17writeCommonFields7bugType13sectionWriterySS_ySDys11AnyHashableVypGSgXEtFZ
+ _$sSD10FoundationE19_bridgeToObjectiveCSo12NSDictionaryCyF
+ _$ss11AnyHashableVN
+ _$ss11AnyHashableVSHsWP
+ _$sypN
+ _OBJC_CLASS_$_CDStackshotReport
+ _OBJC_METACLASS_$_CDStackshotReport
+ ___assert_rtn
- _OBJC_CLASS_$_OSAStackShotReport
- _OBJC_METACLASS_$_OSAStackShotReport
CStrings:
+ "!(cur_metadata->lm_flags & IBOOT_PANICLOG_BAD_MAGIC_FLAG)"
+ "+[ArgParser withArgs:count:]"
+ "-[ArgParser usage]"
+ "-[CoreFileHandler getPanicRegion]"
+ "0"
+ "ARMPanicSupport.m"
+ "ArgParser.m"
+ "Shared.m"
+ "aeaDecryptStreamClose"
+ "aeaDecryptStreamRead"
+ "check_log_metadata"
+ "corefilestreams.m"
+ "data"
+ "gzipOutputStreamWrite"
+ "handlekernelcore.m"
+ "lz4DecodeStreamClose"
+ "lz4DecodeStreamRead"
+ "panicRegionTempFile != NULL"
+ "sectionInputStreamRead"
+ "unlock_register"
+ "unlock_sema != nil"
+ "v24@0:8@?16"
+ "writePanicReportBodyWithSectionWriter:"
- "commonFieldsForBody:"

```
