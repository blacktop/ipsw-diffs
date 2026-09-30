## FileProviderDiagnosticExtension

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/PlugIns/FileProviderDiagnosticExtension.appex/FileProviderDiagnosticExtension`

```diff

-2732.60.128.0.0
-  __TEXT.__text: 0x1c28
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_stubs: 0x7e0
-  __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0x260
-  __TEXT.__cstring: 0x204
-  __TEXT.__oslogstring: 0x560
+2732.80.45.0.0
+  __TEXT.__text: 0x29f0
+  __TEXT.__auth_stubs: 0x390
+  __TEXT.__objc_stubs: 0xa00
+  __TEXT.__objc_methlist: 0x50
+  __TEXT.__const: 0x58
+  __TEXT.__gcc_except_tab: 0x2e0
+  __TEXT.__cstring: 0x28c
+  __TEXT.__oslogstring: 0x6d4
   __TEXT.__objc_classname: 0x20
-  __TEXT.__objc_methname: 0x57b
-  __TEXT.__objc_methtype: 0x16
-  __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x1a8
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0xa0
-  __DATA_CONST.__cfstring: 0x300
+  __TEXT.__objc_methname: 0x75e
+  __TEXT.__objc_methtype: 0x2d
+  __TEXT.__unwind_info: 0xe0
+  __DATA_CONST.__auth_got: 0x1d8
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__const: 0x108
+  __DATA_CONST.__cfstring: 0x380
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x200
+  __DATA.__objc_selrefs: 0x288
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/FileProvider.framework/FileProvider

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
-  Functions: 35
-  Symbols:   82
-  CStrings:  114
+  Functions: 49
+  Symbols:   91
+  CStrings:  148
 
Symbols:
+ _NSURLFileSizeKey
+ _NSURLIsRegularFileKey
+ __NSConcreteGlobalBlock
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_retain
+ _objc_retain_x19
+ _objc_retain_x21
+ _objc_retain_x23
CStrings:
+ "1"
+ "B24@?0@\"NSURL\"8@\"NSError\"16"
+ "B56@0:8@16@24@32@40@48"
+ "FileProvider Daemon"
+ "FileProviderDiagnosticLogs"
+ "[DEBUG] Enumerating: %@"
+ "[DEBUG] Found previously captured dump"
+ "[DEBUG] Found previously captured logs"
+ "[DEBUG] Not recognized - skipping"
+ "[DEBUG] Will filter with %@"
+ "[ERROR] Enumeration failed on %@: %@"
+ "[ERROR] Failed %@ -> %@: %@"
+ "[ERROR] Gathering old diagnostics from daemon failed: %@"
+ "[INFO] Invalid diagnostic location: %@ (%@)"
+ "[INFO] Returning previously captured data"
+ "[INFO] [FileProviderDiagnosticExtension attachmentsForParameters:ABC] Getting fileprovider oslog for past 30 mins"
+ "_gatherPersistedDiagnostics:domainID:displayName:tempDirURL:attachments:"
+ "arrayWithObjects:count:"
+ "boolValue"
+ "checkResourceIsReachableAndReturnError:"
+ "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
+ "fp_prettyPath"
+ "getSavedDiagnosticsFor:completionHandler:"
+ "hasPrefix:"
+ "integerValue"
+ "lastPathComponent"
+ "moveItemAtURL:toURL:error:"
+ "removeAllObjects"
+ "removeItemAtURL:error:"
+ "resourceValuesForKeys:error:"
+ "startAccessingSecurityScopedResource"
+ "stopAccessingSecurityScopedResource"
+ "url"
+ "useDiagnostic"
+ "v24@?0@\"FPSandboxingURLWrapper\"8@\"NSError\"16"
- "[INFO] [FileProviderDiagnosticExtension attachmentsForParameters:ABC] Getting fileprovider oslog for past 15 mins"

```
