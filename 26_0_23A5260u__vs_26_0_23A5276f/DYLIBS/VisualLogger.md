## VisualLogger

> `/System/Library/PrivateFrameworks/VisualLogger.framework/VisualLogger`

```diff

-8.25.5.7.1
-  __TEXT.__text: 0x716c64
-  __TEXT.__auth_stubs: 0x1ba0
-  __TEXT.__const: 0x661f0
-  __TEXT.__gcc_except_tab: 0x5fb60
-  __TEXT.__cstring: 0x14ab9
+8.25.5.28.1
+  __TEXT.__text: 0x72d378
+  __TEXT.__auth_stubs: 0x1bc0
+  __TEXT.__const: 0x66d80
+  __TEXT.__gcc_except_tab: 0x60938
+  __TEXT.__cstring: 0x14ef0
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x1ad48
+  __TEXT.__unwind_info: 0x1b208
   __TEXT.__eh_frame: 0x88
   __TEXT.__objc_methname: 0x23
   __TEXT.__objc_stubs: 0x60
   __DATA_CONST.__got: 0x330
-  __DATA_CONST.__const: 0x14b0
+  __DATA_CONST.__const: 0x14b8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x18
-  __AUTH_CONST.__auth_got: 0xde0
-  __AUTH_CONST.__const: 0x307c0
+  __AUTH_CONST.__auth_got: 0xdf0
+  __AUTH_CONST.__const: 0x31290
   __AUTH_CONST.__cfstring: 0x280
-  __DATA.__data: 0x23f0
+  __DATA.__data: 0x2450
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x26b8
+  __DATA.__bss: 0x2838
   __DATA.__common: 0x2a8
   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__common: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4976B0B1-F0F6-3BC6-B08A-E5F65B934507
-  Functions: 16237
-  Symbols:   1111
-  CStrings:  2157
+  UUID: 74964187-7963-3C45-AB75-BC791B0DB98C
+  Functions: 16447
+  Symbols:   1132
+  CStrings:  2188
 
Symbols:
+ _CFAllocatorCreate
+ _CFDataCreate
+ _CFStringCreateWithCString
+ _VZBlobCreateCFDataCopy
+ _VZBlobCreateCFDataNoCopy
+ _VZBlobCreateWithCFDataCopy
+ _VZBlobCreateWithCFDataNoCopy
+ _VZDataIOExportLogMessageListToNewBlob
+ _VZDataIOImportLogMessageListFromBlob
+ _VZDestinationCreateWithRecorder
+ _VZLoggerLogMessage
+ _VZLoggerLogMessageList
+ _VZRecorderCopyLogMessages
+ _VZRecorderCopyNewLogMessages
+ _VZRecorderCreate
+ _VZRecorderGetMaximumMessageAgeNanoseconds
+ _VZRecorderGetTypeID
+ _VZRecorderOptionsCreate
+ _VZRecorderOptionsGetTypeID
+ _VZRecorderOptionsSetAutoCleanupSizeRatio
+ _VZRecorderOptionsSetMaximumMessageAgeNanoseconds
+ _kVZNanosecondsMax
- _nanosleep
CStrings:
+ " is processing only the first encountered timestamp, which was '"
+ " to context "
+ ", forgotten: "
+ "System"
+ "VZBlobCreateCFDataCopy"
+ "VZBlobCreateCFDataNoCopy"
+ "VZBlobCreateWithCFDataCopy"
+ "VZBlobCreateWithCFDataNoCopy"
+ "VZDataIOExportLogMessageListToNewBlob"
+ "VZDataIOImportLogMessageListFromBlob"
+ "VZDestinationCreateWithRecorder"
+ "VZLoggerLogMessage"
+ "VZLoggerLogMessageList"
+ "VZRecorderCopyLogMessages"
+ "VZRecorderCopyNewLogMessages"
+ "VZRecorderGetMaximumMessageAgeNanoseconds"
+ "VZRecorderOptionsSetAutoCleanupSizeRatio"
+ "VZRecorderOptionsSetMaximumMessageAgeNanoseconds"
+ "cannot create CFData from empty blob"
+ "entries: "
+ "exporter"
+ "limited recorder"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = VZRecorderOptions]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = VZRecorder]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::esn::OptionalRef<const cv3d::vl::visual_logger::RecorderOptions>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vl::visual_logger::RecorderOptions]"
+ "std::any owner for CFData backing store"
+ "viz::ContextStatistics"
+ "viz::LimitedRecorder"
+ "viz::Records"
+ "viz::UnlimitedRecorder"
+ "while recording data of type "
- "; exporter is exporting only the first encountered timestamp, which was '"

```
