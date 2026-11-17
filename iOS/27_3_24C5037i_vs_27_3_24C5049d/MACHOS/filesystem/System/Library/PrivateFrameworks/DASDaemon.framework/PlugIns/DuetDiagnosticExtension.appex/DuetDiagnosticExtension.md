## DuetDiagnosticExtension

> `/System/Library/PrivateFrameworks/DASDaemon.framework/PlugIns/DuetDiagnosticExtension.appex/DuetDiagnosticExtension`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-2467.60.9.0.0
-  __TEXT.__text: 0xb54
-  __TEXT.__auth_stubs: 0x190
-  __TEXT.__objc_stubs: 0x2e0
-  __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0x18
-  __TEXT.__oslogstring: 0x29a
-  __TEXT.__cstring: 0x30
+2467.60.20.0.0
+  __TEXT.__text: 0x450
+  __TEXT.__auth_stubs: 0x140
+  __TEXT.__objc_stubs: 0x1e0
+  __TEXT.__objc_methlist: 0x2c
+  __TEXT.__const: 0x10
+  __TEXT.__cstring: 0x52
+  __TEXT.__oslogstring: 0x85
   __TEXT.__objc_classname: 0x18
-  __TEXT.__objc_methname: 0x260
-  __TEXT.__objc_methtype: 0x29
-  __TEXT.__unwind_info: 0x78
+  __TEXT.__objc_methname: 0x154
+  __TEXT.__objc_methtype: 0x13
+  __TEXT.__unwind_info: 0x70
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xd0
+  __DATA_CONST.__auth_got: 0xa8
   __DATA_CONST.__got: 0x48
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0xc8
+  __DATA.__objc_selrefs: 0x88
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/DASDaemon.framework/DASDaemon
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
+  - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6
-  Symbols:   44
-  CStrings:  54
+  Functions: 4
+  Symbols:   39
+  CStrings:  27
 
Symbols:
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSDictionary
+ _PLQueryRegistered
+ _objc_retain_x21
+ _objc_retain_x22
- _NSSearchPathForDirectoriesInDomains
- _OBJC_CLASS_$_NSString
- _OBJC_CLASS_$__DASLogExtractor
- _arc4random_uniform
- _objc_release_x25
- _objc_release_x26
- _objc_release_x27
- _objc_release_x28
- _objc_retain_x20
- _objc_retain_x23
- _objc_retain_x8
CStrings:
+ "BackgroundProcessingLog"
+ "DEExtensionAttachmentsParamConsentProvidedKey"
+ "[BGProcessingDE] Attaching %@"
+ "[BGProcessingDE] Consent not provided, stopping"
+ "[BGProcessingDE] No log path returned for query %@: %@"
+ "arrayWithObjects:count:"
+ "attachmentForRegisteredQuery:"
+ "boolValue"
+ "dictionaryWithObjects:forKeys:count:"
+ "fileExistsAtPath:"
+ "folder"
+ "objectForKeyedSubscript:"
+ "path"
- "%@.txt"
- ","
- "@32@0:8@16@24"
- "Activity Name:\n%@%@"
- "ActivityName is nil, skipping"
- "ActivityName is nil, stopping"
- "Could not find directory to clean up files, skipping"
- "Could not find directory to write file, skipping"
- "Deleted file: %@"
- "DiagnosisString is nil, stopping"
- "Encountered error while deleting file %@: %@"
- "Encountered error while enumerating directory %@: %@"
- "Extractor couldn't get result string"
- "Extractor failed with error %d"
- "Failed to create extractor, stopping"
- "Failed to save activity info file for %@"
- "Failed to write file %@"
- "Finding summary for activity: %@"
- "Getting summary for %@"
- "No activity names found, stopping"
- "No parameters specified, stopping"
- "Saved %@"
- "Summary for %@ is empty, skipping"
- "Summary for %@:\n%@"
- "activitySummaryForActivityName:withExtractor:"
- "cleanUpDocumentsDirectory"
- "componentsSeparatedByString:"
- "contentsOfDirectoryAtPath:error:"
- "copyActivitySummary:startDate:endDate:detail:error:"
- "extractorForArchive:"
- "firstObject"
- "kDuetActivityNames"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "removeItemAtPath:error:"
- "stringByAppendingPathComponent:"
- "stringWithFormat:"
- "v16@0:8"
- "writeDiagnosisStringToFile:forActivity:"
- "writeToFile:atomically:encoding:error:"
```
