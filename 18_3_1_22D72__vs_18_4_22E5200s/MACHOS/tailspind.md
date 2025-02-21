## tailspind

> `/usr/libexec/tailspind`

```diff

-200.2.0.0.0
-  __TEXT.__text: 0x9170
-  __TEXT.__auth_stubs: 0xb00
-  __TEXT.__objc_stubs: 0x780
-  __TEXT.__objc_methlist: 0x14c
-  __TEXT.__const: 0x12c
-  __TEXT.__cstring: 0x8cc
-  __TEXT.__objc_methname: 0x92c
-  __TEXT.__oslogstring: 0x1fa4
-  __TEXT.__objc_classname: 0x16
-  __TEXT.__objc_methtype: 0xe5
-  __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__unwind_info: 0x1a8
-  __DATA_CONST.__auth_got: 0x590
-  __DATA_CONST.__got: 0x150
+218.0.0.0.0
+  __TEXT.__text: 0xa124
+  __TEXT.__auth_stubs: 0xb50
+  __TEXT.__objc_stubs: 0x880
+  __TEXT.__objc_methlist: 0x1c4
+  __TEXT.__const: 0x124
+  __TEXT.__cstring: 0xa20
+  __TEXT.__objc_methname: 0xb81
+  __TEXT.__oslogstring: 0x2262
+  __TEXT.__objc_classname: 0x17
+  __TEXT.__objc_methtype: 0xfb
+  __TEXT.__gcc_except_tab: 0x44
+  __TEXT.__unwind_info: 0x1e8
+  __DATA_CONST.__auth_got: 0x5b8
+  __DATA_CONST.__got: 0x158
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x370
-  __DATA_CONST.__cfstring: 0x460
+  __DATA_CONST.__const: 0x3b0
+  __DATA_CONST.__cfstring: 0x540
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x210
-  __DATA.__objc_selrefs: 0x250
-  __DATA.__objc_ivar: 0x20
+  __DATA.__objc_const: 0x2a0
+  __DATA.__objc_selrefs: 0x2b0
+  __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x2168
+  __DATA.__data: 0x2160
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x470
+  __DATA.__bss: 0x488
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 153
-  Symbols:   228
-  CStrings:  330
+  Functions: 175
+  Symbols:   234
+  CStrings:  378
 
Symbols:
+ _NSStringFromClass
+ _TSPDumpOptions_EndTimestamp
+ _close
+ _dup
+ _fclonefileat
+ _ffsctl
+ _objc_retain_x24
- _objc_retain_x26
CStrings:
+ ".temp"
+ "11"
+ "<apply_config>"
+ "<apply_config_%s>"
+ "<foreground_tracing>"
+ "<profile_or_tasking>"
+ "@\"NSString\""
+ "B"
+ "B16@0:8"
+ "Client requested end timestamp that is past time window that tailspin can provide (tailspin start timestamp: %llu, client timestamp: %llu). Not saving tailspin file."
+ "CoreAnalytics Event %@ payload: %@"
+ "DidClientRequestEndTimestamp"
+ "DidPrevClientSaveOverlapWithEndTimestamp"
+ "ERROR"
+ "Failed to clone file to path %{public}@: %{errno}d"
+ "Failed to finalize force reset tailspin. Deleting"
+ "Failed to mark %{public}@ with purgeable children: %{errno}d"
+ "File descriptor %d is not read-write (flags: 0x%x)"
+ "Invalid type for TSPDumpOptions_EndTimestamp. Expect %@, found %@."
+ "Marked %{public}@ with purgeable children"
+ "PostProcessing_Libktrace"
+ "PostProcessing_Tailspin"
+ "PrevExecName"
+ "T@\"NSString\",&,N,V_prevExecName"
+ "TB,N,V_didClientRequestEndTimestamp"
+ "TB,N,V_didPrevClientSaveOverlapWithEndTimestamp"
+ "Unable to dup fd for temp file at %{public}@: %{errno}d"
+ "Unable to open dir at %{public}@: %{errno}d"
+ "Unable to save tailspin for %{public}s [%d]: file descriptor %d is not read-write (flags: 0x%x)"
+ "Unable to save tailspin for %{public}s: %@"
+ "Unable to unlink temp file at %{public}@: %{errno}d"
+ "Updating trace buffer reset event name: %s (was %s)"
+ "_didClientRequestEndTimestamp"
+ "_didPrevClientSaveOverlapWithEndTimestamp"
+ "_prevExecName"
+ "client %s [%d] requested for tailspin data but was rejected by the allowlist"
+ "com.apple.tailspind.post_processing_queue"
+ "didClientRequestEndTimestamp"
+ "didPrevClientSaveOverlapWithEndTimestamp"
+ "hangtracerd"
+ "ktrace buffer starts after client's end timestamp"
+ "numberWithBool:"
+ "prevExecName"
+ "setDidClientRequestEndTimestamp:"
+ "setDidPrevClientSaveOverlapWithEndTimestamp:"
+ "setPrevExecName:"
+ "startRecordingTimeForLibktracePostProcessing"
+ "startRecordingTimeForTailspinPostProcessing"
+ "stopRecordingTimeForLibktracePostProcessing"
+ "stopRecordingTimeForTailspinPostProcessing"
+ "stringByAppendingString:"
+ "v24@?0r*8Q16"
- "!"
- "File descriptor is not read-write %d"
- "KDBG_STATE"
- "Unable to save tailspin for %{public}s [%d]: file descriptor is not read-write %d"
- "Unable to save tailspin for %{public}s: resulting trace would be shorter than desired duration"
- "Updating trace buffer start info: %s at %llu (was %s at %llu)"

```
