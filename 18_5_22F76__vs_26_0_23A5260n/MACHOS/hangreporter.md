## hangreporter

> `/usr/libexec/hangreporter`

```diff

-354.4.0.0.0
-  __TEXT.__text: 0x3a9d0
-  __TEXT.__auth_stubs: 0xef0
-  __TEXT.__objc_stubs: 0x2b00
-  __TEXT.__objc_methlist: 0xefc
-  __TEXT.__const: 0x1a8
-  __TEXT.__cstring: 0x2e6f9
-  __TEXT.__oslogstring: 0x4317
-  __TEXT.__gcc_except_tab: 0xcf0
-  __TEXT.__objc_methname: 0x4ee1
-  __TEXT.__objc_classname: 0x126
-  __TEXT.__objc_methtype: 0x85b
-  __TEXT.__unwind_info: 0x498
-  __DATA_CONST.__auth_got: 0x788
-  __DATA_CONST.__got: 0x260
+375.0.0.0.0
+  __TEXT.__text: 0x3d060
+  __TEXT.__auth_stubs: 0xf10
+  __TEXT.__objc_stubs: 0x2c60
+  __TEXT.__objc_methlist: 0xfa4
+  __TEXT.__const: 0x1a0
+  __TEXT.__cstring: 0x2ea76
+  __TEXT.__oslogstring: 0x484b
+  __TEXT.__objc_classname: 0x147
+  __TEXT.__objc_methname: 0x51a9
+  __TEXT.__objc_methtype: 0x886
+  __TEXT.__gcc_except_tab: 0xcd8
+  __TEXT.__unwind_info: 0x4e8
+  __DATA_CONST.__auth_got: 0x798
+  __DATA_CONST.__got: 0x280
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1318
-  __DATA_CONST.__cfstring: 0x4900
-  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__const: 0x13a8
+  __DATA_CONST.__cfstring: 0x4b80
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x2550
-  __DATA.__objc_selrefs: 0xfc0
-  __DATA.__objc_ivar: 0x250
-  __DATA.__objc_data: 0x3c0
+  __DATA.__objc_const: 0x26a0
+  __DATA.__objc_selrefs: 0x1040
+  __DATA.__objc_ivar: 0x260
+  __DATA.__objc_data: 0x410
   __DATA.__data: 0x638
-  __DATA.__bss: 0x1b8
+  __DATA.__bss: 0x1c8
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 06DA77C8-ABB9-3DF1-97EF-ED6A90EA6483
-  Functions: 630
-  Symbols:   326
-  CStrings:  5437
+  UUID: 85A03444-F747-371E-BDD5-9BC2B1AB0551
+  Functions: 664
+  Symbols:   332
+  CStrings:  5531
 
Symbols:
+ _NSFileType
+ _NSFileTypeRegular
+ _NSPOSIXErrorDomain
+ _OBJC_CLASS_$_NSUserDefaults
+ _proc_listpids
+ _proc_name
CStrings:
+ "%s: %@"
+ "%s: Error flag set in pidForProcessName, unable to check pid for hangreporter with error:%@"
+ "%s: Failed to retrive contents of directory at path %s with error: %@"
+ "%s: Found tailspin file: %@ in spool directory: %s"
+ "%s: No error flag set in pidForProcessName with return value=%d. Hangreporter is not alive."
+ "%s: Skipping non-regular file at path:%@"
+ "%s: Unable to get file attributes of file at path:%@ with error: %@"
+ "+[HTHangreporterKickstartTelemetry collectTailspinSpoolData:error:]"
+ "+[HTHangreporterKickstartTelemetry emitTailspinProcessingEvent:error:]"
+ "B32@0:8@16^@24"
+ "B32@0:8^@16^@24"
+ "Error accessing tailspin saves: %@"
+ "Error accessing tailspins processed: %@"
+ "Error walking tree"
+ "Failed to fetch creation date for file %@"
+ "Failed to get hangreporter tailspins processed with error:%@"
+ "Failed to get successful tailspin saves with error:%@"
+ "Failed to unlink file %s: %s"
+ "Found matching pid:%d for processName:%s"
+ "Found tailspin: %@ over the threshold limit of %f seconds. Incrementing number of tailspins in spool over the reporting limit to %d"
+ "HTFGTrackingTelemetryMinEmissionThresholdSec"
+ "HTFGTrackingTelemetryPersistentEmissionRateSec"
+ "HTHangreporterKickstartTelemetry"
+ "HTPrefs shouldEmitTelemetry=%d, telemetry emission disabled"
+ "HangTracerShouldEmitTelemetry"
+ "Hangreporter has processed more tailspins than hangtracerd has requested. tailspinsProcessed:%u successfulTailspinSaves:%u. This should never happen."
+ "Hangreporter is alive, not attempting to emit telemetry."
+ "I24@0:8^@16"
+ "Invalid class type %@ for key (%@): value (%@) pair. Values in %@ domain were modified"
+ "Missing value for key (%@) from tailspinDataDict: %@"
+ "Skipping abandoned tailspin file %@ in directory %s"
+ "Skipping non-tailspin file %@ in directory %s"
+ "TB,R,V_shouldEmitTelemetry"
+ "Td,R,V_minFGEmissionThresholdSec"
+ "Td,R,V_persistentFGEmissionThresholdSec"
+ "Td,R,V_tailspinReportingThresholdSec"
+ "Unable to allocate pids buffer of size %d with error: %s"
+ "Unable to list all pids with error: %s"
+ "Updating oldest tailspin to %@, creation time was %f seconds before now"
+ "Value of %@ for key %@ is unexpected class %@. Values in %@ domain were modified"
+ "_minFGEmissionThresholdSec"
+ "_persistentFGEmissionThresholdSec"
+ "_resetHangreporterTailspinsProcessed"
+ "_resetKeysForTailspinProcessingTelemetry"
+ "_resetSuccessfulTailspinSaves"
+ "_shouldEmitTelemetry"
+ "_tailspinReportingThresholdSec"
+ "collectTailspinSpoolData:error:"
+ "com.apple.hangtracer.tailspin_processing"
+ "com.apple.hangtracer.telemetry.error"
+ "conclave limit"
+ "emitTailspinProcessingEvent:error:"
+ "getHangreporterTailspinsProcessed:"
+ "getSuccessfulTailspinSaves:"
+ "hangreporter"
+ "incrementHangreporterTailspinsProcessed"
+ "incrementSuccessfulTailspinSaves"
+ "initWithSuiteName:"
+ "minFGEmissionThresholdSec"
+ "oldestTailspinCreationSeconds"
+ "persistentFGEmissionThresholdSec"
+ "pidForProcessName"
+ "setInteger:forKey:"
+ "shouldEmitTelemetry"
+ "successfulTailspinSaves"
+ "tailspinReportingThresholdSec"
+ "tailspinsInSpool"
+ "tailspinsOverReportingThresholds"
+ "tailspinsProcessed"
+ "tailspinsUnprocessed"
+ "timeIntervalSinceDate:"
+ "unblock deadlock"
+ "unblock thread limit"
+ "\xf0\xf0Q!V!"
- "setDisplayKernelFrames:"
- "\xf0\xf0A!&!"

```
