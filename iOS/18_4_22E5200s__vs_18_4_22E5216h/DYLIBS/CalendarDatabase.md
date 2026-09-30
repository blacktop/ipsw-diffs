## CalendarDatabase

> `/System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase`

```diff

-1253.5.3.0.0
-  __TEXT.__text: 0xda8c4
+1253.5.4.0.0
+  __TEXT.__text: 0xdadcc
   __TEXT.__auth_stubs: 0x1f70
   __TEXT.__objc_methlist: 0x1d94
-  __TEXT.__cstring: 0x1dfd7
+  __TEXT.__cstring: 0x1dfc9
   __TEXT.__const: 0x73c
   __TEXT.__gcc_except_tab: 0x19b0
-  __TEXT.__oslogstring: 0xc73f
+  __TEXT.__oslogstring: 0xc846
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__unwind_info: 0x2bc8
+  __TEXT.__unwind_info: 0x2bd8
   __TEXT.__objc_classname: 0x567
-  __TEXT.__objc_methname: 0x8deb
+  __TEXT.__objc_methname: 0x8dcd
   __TEXT.__objc_methtype: 0x4513
   __TEXT.__objc_stubs: 0x82e0
-  __DATA_CONST.__got: 0x9a8
+  __DATA_CONST.__got: 0x9b0
   __DATA_CONST.__const: 0xe038
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8

   __AUTH.__objc_data: 0x7d0
   __DATA.__objc_ivar: 0x1a0
   __DATA.__data: 0x6f8
-  __DATA.__bss: 0x2c8
+  __DATA.__bss: 0x2b8
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x500
   __DATA_DIRTY.__data: 0x248

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 4160
-  Symbols:   5668
-  CStrings:  4665
+  Functions: 4162
+  Symbols:   5671
+  CStrings:  4671
 
Symbols:
+ _EKAttachmentProperty_URLWrapperForPendingFileCopy
+ _NSURLFileProtectionCompleteUnlessOpen
+ _NSURLFileProtectionKey
+ _OBJC_CLASS_$_CalOpenFileURLWrapper
+ __CalAttachmentFileSetProtectionAndQuarantineAttributesWithFile
+ _fcopyfile
+ _kCalOpenFileURLWrapperMethods
+ _lseek
- _CFURLCopyPathExtension
- _CFURLStartAccessingSecurityScopedResource
- _EKAttachmentProperty_securityScopedURLWrapperForPendingFileCopy
- _NSFileProtectionCompleteUnlessOpen
- _NSFileProtectionKey
- __CalAttachmentFileSetQuarantineAttributesForFile
- _kCalSecurityScopedURLWrapperMethods
CStrings:
+ "Copy failed"
+ "Couldn't create a local file for the attachment file %d"
+ "Couldn't rewind file to be copied: %i"
+ "Encountered an error setting protection/quarantine attributes with %@: %@"
+ "Error checking if url to be protected (%@) is a directory: %@"
+ "Error setting file data: %i"
+ "Error setting resource attributes for URL %@: %@"
+ "Failed to close target file following copy: %i"
+ "URLWrapperForPendingFileCopy"
+ "fileDescriptor"
+ "setResourceValues:error:"
- "Failed to change dataclass of attachment at path %@. Error = %@"
- "Failed to copy attachment (error: %@)."
- "absoluteURL"
- "copyItemAtPath:toPath:error:"
- "securityScopedURLWrapperForPendingFileCopy"
- "setAttributes:ofItemAtPath:error:"

```
