## Diagnostic-8290-EFD

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8290-EFD.appex/Diagnostic-8290-EFD`

```diff

-820.40.9.0.0
-  __TEXT.__text: 0xe2bc
+820.40.18.0.0
+  __TEXT.__text: 0xeb90
   __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_stubs: 0x3200
-  __TEXT.__objc_methlist: 0x110c
-  __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x918
-  __TEXT.__objc_methname: 0x3eb2
-  __TEXT.__oslogstring: 0x125b
+  __TEXT.__objc_stubs: 0x3380
+  __TEXT.__objc_methlist: 0x1164
+  __TEXT.__const: 0xc0
+  __TEXT.__cstring: 0x984
+  __TEXT.__objc_methname: 0x3fad
+  __TEXT.__oslogstring: 0x14a5
   __TEXT.__objc_classname: 0x20e
-  __TEXT.__objc_methtype: 0x622
+  __TEXT.__objc_methtype: 0x63c
   __TEXT.__gcc_except_tab: 0x160
-  __TEXT.__unwind_info: 0x2f8
+  __TEXT.__unwind_info: 0x300
   __DATA_CONST.__auth_got: 0x378
-  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x218
-  __DATA_CONST.__cfstring: 0xca0
+  __DATA_CONST.__const: 0x240
+  __DATA_CONST.__cfstring: 0xe60
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
-  __DATA_CONST.__objc_intobj: 0x2d0
-  __DATA_CONST.__objc_arraydata: 0x18
+  __DATA_CONST.__objc_intobj: 0x300
+  __DATA_CONST.__objc_arraydata: 0x28
+  __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__objc_floatobj: 0x40
-  __DATA.__objc_const: 0x2b80
-  __DATA.__objc_selrefs: 0xd80
-  __DATA.__objc_ivar: 0x1fc
+  __DATA.__objc_const: 0x2bb0
+  __DATA.__objc_selrefs: 0xde0
+  __DATA.__objc_ivar: 0x200
   __DATA.__objc_data: 0x640
   __DATA.__data: 0x240
   __DATA.__bss: 0xc

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 411
-  Symbols:   227
-  CStrings:  1054
+  Functions: 423
+  Symbols:   230
+  CStrings:  1092
 
Symbols:
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$_NSDate
+ _objc_retain_x27
+ _OBJC_CLASS_$_NSConstantDictionary
- _MGGetBoolAnswer
CStrings:
+ "Base implementation of testID called. Please override this in your DK."
+ "t"
+ "_startTime"
+ "parseTestResults:fromOutput:withFile:parsedResults:sequenceIndex:error:"
+ "Failed to write result to file with error: [%!@(MISSING)]"
+ "_id"
+ "initWithData:encoding:"
+ "sd"
+ "com.apple.Diagnostics.8290.XXXXXXXX"
+ "Unable to include test results in archive. Prioritizing Kets over recorded audio"
+ "results.json"
+ "archiveNameTemplate"
+ "Td,N,V_startTime"
+ "s"
+ "T@\"NSNumber\",&,N,V_index"
+ "Failed to rename raw audio archive. Will use existing name in upload. Error: [%!@(MISSING)]"
+ "index"
+ "setIndex:"
+ "type"
+ "writeToURL:atomically:encoding:error:"
+ "startTime"
+ "k"
+ "testID"
+ "Mic-%!@(MISSING)Speaker-File%!@(MISSING)-Sequence%!@(MISSING).wav"
+ "RecordedAudio"
+ "XXXXXX"
+ "setStartTime:"
+ "writeCurrentResultsToJson"
+ "date"
+ "com.apple.Diagnostics.AudioSystem.XXXXXXXX"
+ "v64@0:8@16@24@32@40@48@56"
+ "timeIntervalSince1970"
+ "moveItemAtURL:toURL:error:"
+ "statusCode"
+ "$date"
+ "_index"
+ "Failed to create combined results archive with error [%!@(MISSING)]"
+ "Failed to convert result dictionary to JSON with error: [%!@(MISSING)]"
+ "Base implementation of archiveNameTemplate called. Please override this in your DK."
+ "Successfully created combined results archive at [%!@(MISSING)]"
+ "Successfully renamed raw audio archive to [%!@(MISSING)]"
+ "dataWithJSONObject:options:error:"
+ "e"
+ "Audio"
- "_internalInstall"
- "com.apple.Diagnostics.8079.XXXXXXXX"
- "TB,N,V_internalInstall"
- "setInternalInstall:"
- "Mic-%!@(MISSING)Speaker-File%!@(MISSING)"
- "apple-internal-install"
- "parseTestResults:fromOutput:withFile:parsedResults:error:"
- "internalInstall"

```
