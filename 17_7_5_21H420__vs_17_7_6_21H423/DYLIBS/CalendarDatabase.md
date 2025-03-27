## CalendarDatabase

> `/System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase`

```diff

-1232.4.4.0.0
-  __TEXT.__text: 0xc58c8
+1232.4.6.0.0
+  __TEXT.__text: 0xc5f30
   __TEXT.__stubs: 0x17b8
   __TEXT.__objc_methlist: 0x19a0
-  __TEXT.__cstring: 0x1c3a5
+  __TEXT.__cstring: 0x1c3ad
   __TEXT.__const: 0x80c
   __TEXT.__gcc_except_tab: 0xcf0
-  __TEXT.__oslogstring: 0xb471
+  __TEXT.__oslogstring: 0xb59d
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__unwind_info: 0x29f4
+  __TEXT.__unwind_info: 0x2a14
   __TEXT.__objc_classname: 0x567
-  __TEXT.__objc_methname: 0x8aca
+  __TEXT.__objc_methname: 0x8ae4
   __TEXT.__objc_methtype: 0x44d1
-  __TEXT.__objc_stubs: 0x7e20
+  __TEXT.__objc_stubs: 0x7e80
   __DATA_CONST.__got: 0x1580
   __DATA_CONST.__const: 0xfbd8
-  __DATA_CONST.__cfstring: 0xbde0
+  __DATA_CONST.__cfstring: 0xbe40
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x56f8
-  __DATA_CONST.__objc_selrefs: 0x22f8
-  __DATA_CONST.__objc_classrefs: 0x3e0
+  __DATA_CONST.__objc_selrefs: 0x2310
+  __DATA_CONST.__objc_classrefs: 0x3e8
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30

   __DATA.__objc_ivar: 0x1a0
   __DATA.__objc_data: 0x910
   __DATA.__data: 0x768
-  __DATA.__bss: 0x230
+  __DATA.__bss: 0x220
   __DATA_DIRTY.__objc_data: 0x3c0
   __DATA_DIRTY.__data: 0x250
   __DATA_DIRTY.__common: 0x30

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 4055
-  Symbols:   5508
-  CStrings:  4475
+  Functions: 4059
+  Symbols:   5513
+  CStrings:  4488
 
Symbols:
+ _EKAttachmentProperty_URLWrapperForPendingFileCopy
+ _NSURLFileProtectionCompleteUnlessOpen
+ _NSURLFileProtectionKey
+ _OBJC_CLASS_$_CalOpenFileURLWrapper
+ __CalAttachmentFileSetProtectionAndQuarantineAttributesWithFile
+ __CalAttachmentFileValidateLocalRelativePath
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
+ "/.."
+ "/../"
+ "Attachment file path (%@) is invalid"
+ "Attachments/"
+ "Copy failed"
+ "Couldn't create a local file for the attachment file %d"
+ "Couldn't rewind file to be copied: %i"
+ "Encountered an error setting protection/quarantine attributes with %@: %@"
+ "Error checking if url to be protected (%@) is a directory: %@"
+ "Error setting file data: %i"
+ "Error setting resource attributes for URL %@: %@"
+ "Failed to close target file following copy: %i"
+ "URLWrapperForPendingFileCopy"
+ "characterAtIndex:"
+ "compare:options:range:"
+ "fileDescriptor"
+ "nextObject"
+ "setResourceValues:error:"
- "Failed to change dataclass of attachment at path %@. Error = %@"
- "Failed to copy attachment (error: %@)."
- "absoluteURL"
- "copyItemAtPath:toPath:error:"
- "securityScopedURLWrapperForPendingFileCopy"
- "setAttributes:ofItemAtPath:error:"

```
