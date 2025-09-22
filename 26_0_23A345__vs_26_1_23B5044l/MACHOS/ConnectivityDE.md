## ConnectivityDE

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ConnectivityDE.appex/ConnectivityDE`

```diff

-67.0.1.0.0
-  __TEXT.__text: 0x73c
-  __TEXT.__auth_stubs: 0x150
-  __TEXT.__objc_stubs: 0x2c0
-  __TEXT.__objc_methlist: 0x2c
+68.0.3.0.0
+  __TEXT.__text: 0xe28
+  __TEXT.__auth_stubs: 0x1a0
+  __TEXT.__objc_stubs: 0x400
+  __TEXT.__objc_methlist: 0x50
   __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x137
-  __TEXT.__oslogstring: 0xeb
+  __TEXT.__cstring: 0x1d0
+  __TEXT.__oslogstring: 0x28c
   __TEXT.__objc_classname: 0xf
-  __TEXT.__objc_methname: 0x1f8
-  __TEXT.__objc_methtype: 0x21
-  __TEXT.__unwind_info: 0x68
-  __DATA_CONST.__auth_got: 0xb0
+  __TEXT.__objc_methname: 0x2e4
+  __TEXT.__objc_methtype: 0x42
+  __TEXT.__unwind_info: 0x80
+  __DATA_CONST.__auth_got: 0xd8
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__cfstring: 0x120
+  __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__objc_arraydata: 0x30
+  __DATA_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0xb8
+  __DATA.__objc_selrefs: 0x108
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 673C63C2-77F1-3A54-945A-CE8C9F280E1D
-  Functions: 3
-  Symbols:   42
-  CStrings:  55
+  UUID: 609E7D4C-9F39-32FE-9D42-3A02338B9A99
+  Functions: 12
+  Symbols:   47
+  CStrings:  84
 
Symbols:
+ _OBJC_CLASS_$_NSBundle
+ _objc_release_x24
+ _objc_release_x8
+ _objc_retainAutorelease
+ _objc_retain_x20
+ _os_variant_has_internal_content
+ _os_variant_has_internal_diagnostics
- ___NSArray0__struct
- _objc_release_x28
CStrings:
+ "-[ConnectivityDE createConnectivityDESummaryFile:]"
+ "@24@0:8Q16"
+ "B24@0:8Q16"
+ "CDE: %s: Failed to create outputDir"
+ "CDE: %s: failed to create DEAttachmentItem"
+ "CDE: %s: failed to create attachment for file %{public}@"
+ "CDE: %s: failed to create output directory"
+ "CDE: %s: failed to get attachments: %{public}@"
+ "CDE: %s: failed to write summary file: %{public}@"
+ "CDE: %s: invalid client for summary file"
+ "CDE: %s: invalid client or unsupported platform"
+ "CDE: %s: invalid environment for summary file"
+ "CDE: %s: invoked by %{public}@"
+ "CDE: %s: returning summary attachment"
+ "CDE: %s: unsupported log environment for client"
+ "Feedback Assistant"
+ "Log Collection Summary.txt"
+ "No errors found. Expected files: 0. Collected files: 0."
+ "Q24@0:8Q16"
+ "attachmentWithPath:"
+ "bundleIdentifier"
+ "cStringUsingEncoding:"
+ "count"
+ "createConnectivityDESummaryFile:"
+ "getCDFClientOverrideFlags:"
+ "isClientCollectionSupported:"
+ "mainBundle"
+ "stringByAppendingPathComponent:"
+ "writeToFile:atomically:encoding:error:"
- "CDE: %s: failed to create attachment for file %@"
- "CDE: %s: failed to get attachments: %@"
- "CDE: %s: invoked by %@"

```
