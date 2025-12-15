## ConnectivityDE

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ConnectivityDE.appex/ConnectivityDE`

```diff

-69.0.0.0.0
-  __TEXT.__text: 0xe28
-  __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__objc_stubs: 0x400
-  __TEXT.__objc_methlist: 0x50
-  __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x1d0
-  __TEXT.__oslogstring: 0x28c
+70.1.0.0.0
+  __TEXT.__text: 0x1490
+  __TEXT.__auth_stubs: 0x1d0
+  __TEXT.__objc_stubs: 0x5e0
+  __TEXT.__objc_methlist: 0x74
+  __TEXT.__const: 0x18
+  __TEXT.__cstring: 0x245
+  __TEXT.__oslogstring: 0x332
   __TEXT.__objc_classname: 0xf
-  __TEXT.__objc_methname: 0x2e4
-  __TEXT.__objc_methtype: 0x42
-  __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0xd8
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__cfstring: 0x180
+  __TEXT.__objc_methname: 0x49b
+  __TEXT.__objc_methtype: 0x4d
+  __TEXT.__unwind_info: 0x90
+  __DATA_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__cfstring: 0x1a0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x108
+  __DATA.__objc_selrefs: 0x180
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A7D87935-BECC-3A1C-A27F-79F6D86A3B0B
-  Functions: 12
-  Symbols:   47
-  CStrings:  84
+  UUID: AB7C91E4-DE0C-35C8-B11A-05833A33103B
+  Functions: 17
+  Symbols:   57
+  CStrings:  108
 
Symbols:
+ _NSFilePosixPermissions
+ _NSURLCreationDateKey
+ _NSURLNameKey
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSString
+ _getuid
+ _objc_alloc_init
+ _objc_release_x28
+ _objc_retain_x21
- _OBJC_CLASS_$_NSUUID
- _objc_retain_x19
CStrings:
+ "-[ConnectivityDE cleanupStaleDirectories:]"
+ "-[ConnectivityDE createRootOutputDirectory]"
+ "-[ConnectivityDE getCurrentOutputDirectoryFor:]"
+ "B16@0:8"
+ "CDE: %s: failed to create output directory: %{public}@"
+ "CDE: %s: failed to create root directory"
+ "CDE: %s: failed to create root output directory: %{public}@"
+ "CDE: %s: failed to get directory list %{public}@"
+ "CDE: %s: invalid payload from ABC Client %{public}@"
+ "arrayWithObjects:count:"
+ "cleanupStaleDirectories:"
+ "compare:"
+ "containsString:"
+ "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "createRootOutputDirectory"
+ "dateWithTimeIntervalSinceNow:"
+ "dictionaryWithObjects:forKeys:count:"
+ "fileExistsAtPath:isDirectory:"
+ "generateDirPrefixFor:"
+ "getCurrentOutputDirectoryFor:"
+ "getResourceValue:forKey:error:"
+ "i"
+ "now"
+ "removeItemAtURL:error:"
+ "setDateFormat:"
+ "stringByAppendingString:"
+ "stringFromDate:"
+ "stringWithFormat:"
+ "user%u_client%lu_"
+ "v24@0:8Q16"
+ "yyyy-MM-dd_HH.mm.ss"
- "-[ConnectivityDE getOutputDirectoryForCurrentSession]"
- "/%@"
- "@16@0:8"
- "CDE: %s: failed to create output directory: %@"
- "CDE: %s: invalid payload from ABC Client %@"
- "UUID"
- "UUIDString"
- "getOutputDirectoryForCurrentSession"
- "stringByAppendingFormat:"

```
