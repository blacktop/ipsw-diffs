## Diagnostic-8079

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8079.appex/Diagnostic-8079`

```diff

-820.40.9.0.0
-  __TEXT.__text: 0x7134
+820.40.18.0.0
+  __TEXT.__text: 0x7a08
   __TEXT.__auth_stubs: 0x430
-  __TEXT.__objc_stubs: 0x1fa0
-  __TEXT.__objc_methlist: 0x8a4
-  __TEXT.__cstring: 0x515
-  __TEXT.__objc_methname: 0x24ee
+  __TEXT.__objc_stubs: 0x2120
+  __TEXT.__objc_methlist: 0x8fc
+  __TEXT.__cstring: 0x581
+  __TEXT.__objc_methname: 0x25e9
   __TEXT.__objc_classname: 0x16f
-  __TEXT.__objc_methtype: 0x29e
-  __TEXT.__const: 0x78
+  __TEXT.__objc_methtype: 0x2cd
+  __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0x118
-  __TEXT.__oslogstring: 0x7fc
-  __TEXT.__unwind_info: 0x1d0
+  __TEXT.__oslogstring: 0xa46
+  __TEXT.__unwind_info: 0x1e0
   __DATA_CONST.__auth_got: 0x228
-  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__got: 0x148
   __DATA_CONST.__const: 0x1f0
-  __DATA_CONST.__cfstring: 0x740
+  __DATA_CONST.__cfstring: 0x900
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_intobj: 0xd8
+  __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__objc_floatobj: 0x20
-  __DATA.__objc_const: 0x1910
-  __DATA.__objc_selrefs: 0x878
-  __DATA.__objc_ivar: 0xf8
+  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_dictobj: 0x28
+  __DATA.__objc_const: 0x1940
+  __DATA.__objc_selrefs: 0x8d8
+  __DATA.__objc_ivar: 0xfc
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x120
   __DATA.__bss: 0x4

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 198
-  Symbols:   156
-  CStrings:  603
+  Functions: 210
+  Symbols:   159
+  CStrings:  644
 
Symbols:
+ _objc_retain_x27
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSJSONSerialization
- _MGGetBoolAnswer
CStrings:
+ "writeCurrentResultsToJson"
+ "Failed to create combined results archive with error [%!@(MISSING)]"
+ "Base implementation of testID called. Please override this in your DK."
+ "Failed to write result to file with error: [%!@(MISSING)]"
+ "dataWithJSONObject:options:error:"
+ "k"
+ "Failed to convert result dictionary to JSON with error: [%!@(MISSING)]"
+ "setIndex:"
+ "_startTime"
+ "Unable to include test results in archive. Prioritizing Kets over recorded audio"
+ "Td,N,V_startTime"
+ "e"
+ "v24@0:8d16"
+ "parseTestResults:fromOutput:withFile:parsedResults:sequenceIndex:error:"
+ "RecordedAudio"
+ "Mic-%!@(MISSING)Speaker-File%!@(MISSING)-Sequence%!@(MISSING).wav"
+ "date"
+ "d16@0:8"
+ "results.json"
+ "d"
+ "Failed to rename raw audio archive. Will use existing name in upload. Error: [%!@(MISSING)]"
+ "$date"
+ "moveItemAtURL:toURL:error:"
+ "startTime"
+ "sd"
+ "s"
+ "writeToURL:atomically:encoding:error:"
+ "v64@0:8@16@24@32@40@48@56"
+ "setStartTime:"
+ "_id"
+ "archiveNameTemplate"
+ "T@\"NSNumber\",&,N,V_index"
+ "Successfully created combined results archive at [%!@(MISSING)]"
+ "Base implementation of archiveNameTemplate called. Please override this in your DK."
+ "Audio"
+ "testID"
+ "statusCode"
+ "initWithData:encoding:"
+ "t"
+ "type"
+ "_index"
+ "index"
+ "XXXXXX"
+ "timeIntervalSince1970"
+ "com.apple.Diagnostics.AudioSystem.XXXXXXXX"
+ "Successfully renamed raw audio archive to [%!@(MISSING)]"
- "Mic-%!@(MISSING)Speaker-File%!@(MISSING)"
- "apple-internal-install"
- "internalInstall"
- "_internalInstall"
- "setInternalInstall:"
- "parseTestResults:fromOutput:withFile:parsedResults:error:"
- "TB,N,V_internalInstall"

```
