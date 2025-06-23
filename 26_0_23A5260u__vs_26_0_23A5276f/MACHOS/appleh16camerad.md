## appleh16camerad

> `/usr/sbin/appleh16camerad`

```diff

-4.12.4.0.0
-  __TEXT.__text: 0x80cd0
-  __TEXT.__auth_stubs: 0x1e40
-  __TEXT.__objc_stubs: 0x1420
+4.15.3.0.0
+  __TEXT.__text: 0x827a8
+  __TEXT.__auth_stubs: 0x1f00
+  __TEXT.__objc_stubs: 0x1440
   __TEXT.__init_offsets: 0x14
   __TEXT.__objc_methlist: 0x268
-  __TEXT.__gcc_except_tab: 0x2230
+  __TEXT.__gcc_except_tab: 0x22c4
   __TEXT.__const: 0x2d90
-  __TEXT.__cstring: 0x88fc
+  __TEXT.__cstring: 0x89ff
   __TEXT.__objc_classname: 0x89
-  __TEXT.__oslogstring: 0x56ea
-  __TEXT.__objc_methname: 0x1567
+  __TEXT.__oslogstring: 0x5a50
+  __TEXT.__objc_methname: 0x1577
   __TEXT.__objc_methtype: 0x10b3
-  __TEXT.__unwind_info: 0x14c8
+  __TEXT.__unwind_info: 0x1508
   __TEXT.__eh_frame: 0xa0
-  __DATA_CONST.__auth_got: 0xf30
-  __DATA_CONST.__got: 0xb28
+  __DATA_CONST.__auth_got: 0xf90
+  __DATA_CONST.__got: 0xb78
   __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0xa340
+  __DATA_CONST.__const: 0xae58
   __DATA_CONST.__cfstring: 0x3280
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x5a8
-  __DATA.__objc_selrefs: 0x620
+  __DATA.__objc_selrefs: 0x628
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x35cd78
+  __DATA.__data: 0x35cd88
   __DATA.__bss: 0x201
   __DATA.__common: 0x5c
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 114C08F6-CDDC-3A84-9B9B-573AA6215AB2
-  Functions: 1614
-  Symbols:   865
-  CStrings:  2394
+  UUID: D60D6225-5BD5-3C1A-B96E-9A77E9C9682F
+  Functions: 1635
+  Symbols:   887
+  CStrings:  2427
 
Symbols:
+ _TSPDumpOptions_CollectAriadnePlists
+ _TSPDumpOptions_CollectOsLogs
+ _TSPDumpOptions_CollectOsSignposts
+ _TSPDumpOptions_CollectTrials
+ _TSPDumpOptions_NoSymbolicate
+ _TSPDumpOptions_ReasonString
+ _TSPDumpOptions_ScrubOutput
+ _TSPDumpOptions_TargetPID
+ ___kCFBooleanTrue
+ ___strncpy_chk
+ _closedir
+ _dispatch_get_global_queue
+ _fsync
+ _kFigCaptureStreamMetadata_SynchronizedStreamsAWBStatisticsPrimaryPortType
+ _lstat
+ _opendir
+ _os_variant_has_internal_diagnostics
+ _readdir
+ _strnlen
+ _strrchr
+ _tailspin_dump_output_with_options
+ _tailspin_dump_output_with_options_sync
CStrings:
+ "%s - Failed to open directory %s, errno=%d\n"
+ "%s - Failed to purge %s\n"
+ "%s - Successfully purged %s\n"
+ "%s - attempted to trigger tailspin, but action is unsupported on os variant\n"
+ "%s%s"
+ "/private/var/mobile/Library/Logs/CrashReporter/appleh16camerad/"
+ "/usr/local/share/firmware/isp/dcs_isp_fw.bin"
+ "4.15.3"
+ "500ms frame receiver timeout"
+ "Dump tailspin end ...\n"
+ "Dump tailspin to %s begin ...\n"
+ "Frame receiver stalled for 500ms, calling dumpTailspinInBackground\n"
+ "FrameReceiverTimeout"
+ "Tailspin with reason '%@' stored at path %s\n"
+ "TriggerTailspin"
+ "Unable to store tailspin with reason '%@' at path %s\n"
+ "[TAILSPIN]Failed to complete file name with strftime!\n"
+ "[TAILSPIN]Failed to create CFString for reason: %s\n"
+ "[TAILSPIN]Failed to create directory %s: %d!\n"
+ "[TAILSPIN]Failed to open(\"%s\", O_RDWR | O_CREAT, 0644): %s!\n"
+ "[TAILSPIN]dirAndPrefix is longer than PATH_MAX\n"
+ "[TAILSPIN]time function failed!\n"
+ "_%Y.%m.%d_%H-%M-%S%z.tailspin"
+ "creating directory %s\n"
+ "creating tailspin file %s\n"
+ "dumpTailspinWithOptionsOnQueue %s %@ %p %p\n"
+ "failed"
+ "numberWithBool:"
+ "purgeTailspins"
+ "started"
+ "succeeded"
+ "tailspin %s\n"
+ "tailspin requested but tailspin generation rate limited for %f seconds\n"
+ "v12@?0B8"
- "4.12.4"

```
