## FileProviderDiagnosticExtension

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/PlugIns/FileProviderDiagnosticExtension.appex/FileProviderDiagnosticExtension`

```diff

-2732.80.49.0.0
-  __TEXT.__text: 0x29f0
+2882.100.384.0.0
+  __TEXT.__text: 0x2c44
   __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_stubs: 0xa00
-  __TEXT.__objc_methlist: 0x50
-  __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0x2e0
-  __TEXT.__cstring: 0x28c
-  __TEXT.__oslogstring: 0x6d4
+  __TEXT.__objc_stubs: 0xa20
+  __TEXT.__objc_methlist: 0x5c
+  __TEXT.__const: 0x60
+  __TEXT.__gcc_except_tab: 0x304
+  __TEXT.__cstring: 0x2c2
+  __TEXT.__oslogstring: 0x708
   __TEXT.__objc_classname: 0x20
-  __TEXT.__objc_methname: 0x75e
-  __TEXT.__objc_methtype: 0x2d
-  __TEXT.__unwind_info: 0xe0
+  __TEXT.__objc_methname: 0x77a
+  __TEXT.__objc_methtype: 0x35
+  __TEXT.__unwind_info: 0xf0
   __DATA_CONST.__auth_got: 0x1d8
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__const: 0x108
-  __DATA_CONST.__cfstring: 0x380
+  __DATA_CONST.__cfstring: 0x3a0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x288
+  __DATA.__objc_selrefs: 0x290
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/FileProvider.framework/FileProvider
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
-  - /System/Library/PrivateFrameworks/FPFS.framework/FPFS
   - /System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon
   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
-  Functions: 49
+  Functions: 53
   Symbols:   91
-  CStrings:  148
+  CStrings:  152
 
Symbols:
+ _fpfs_is_internal_build
- _objc_retain_x26
CStrings:
+ "\nERROR: Log Collection could not complete, timed out."
+ "[ERROR] Failed writing log line '%@' to file %@: %@"
+ "[INFO] [FileProviderDiagnosticExtension attachmentsForParameters:ABC] Getting fileprovider oslog for past %f mins"
+ "d16@0:8"
+ "logCollectionInterval"
+ "writeData:error:"
- "[INFO] [FileProviderDiagnosticExtension attachmentsForParameters:ABC] Getting fileprovider oslog for past 30 mins"
- "writeData:"

```
