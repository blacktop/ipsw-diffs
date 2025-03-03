## CalendarDatabase

> `/System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase`

```diff

-1253.3.2.0.0
-  __TEXT.__text: 0xd91c4
-  __TEXT.__auth_stubs: 0x1f80
-  __TEXT.__objc_methlist: 0x19f0
-  __TEXT.__cstring: 0x1e06c
-  __TEXT.__const: 0x74c
-  __TEXT.__gcc_except_tab: 0x19ac
-  __TEXT.__oslogstring: 0xc71a
+1253.5.4.0.0
+  __TEXT.__text: 0xdadcc
+  __TEXT.__auth_stubs: 0x1f70
+  __TEXT.__objc_methlist: 0x1d94
+  __TEXT.__cstring: 0x1dfc9
+  __TEXT.__const: 0x73c
+  __TEXT.__gcc_except_tab: 0x19b0
+  __TEXT.__oslogstring: 0xc846
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__unwind_info: 0x2b78
+  __TEXT.__unwind_info: 0x2bd8
   __TEXT.__objc_classname: 0x567
-  __TEXT.__objc_methname: 0x8dc2
+  __TEXT.__objc_methname: 0x8dcd
   __TEXT.__objc_methtype: 0x4513
-  __TEXT.__objc_stubs: 0x82a0
-  __DATA_CONST.__got: 0x9a8
-  __DATA_CONST.__const: 0xe020
+  __TEXT.__objc_stubs: 0x82e0
+  __DATA_CONST.__got: 0x9b0
+  __DATA_CONST.__const: 0xe038
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23f0
+  __DATA_CONST.__objc_selrefs: 0x2488
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0xfd0
+  __AUTH_CONST.__auth_got: 0xfc8
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x2150
   __AUTH_CONST.__cfstring: 0xc580
-  __AUTH_CONST.__objc_const: 0x3cb0
+  __AUTH_CONST.__objc_const: 0x35f0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x820
+  __AUTH.__objc_data: 0x7d0
   __DATA.__objc_ivar: 0x1a0
-  __DATA.__data: 0x700
-  __DATA.__bss: 0x2c8
+  __DATA.__data: 0x6f8
+  __DATA.__bss: 0x2b8
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x4b0
+  __DATA_DIRTY.__objc_data: 0x500
   __DATA_DIRTY.__data: 0x248
   __DATA_DIRTY.__common: 0x30
   __DATA_DIRTY.__bss: 0x168

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 4122
-  Symbols:   5617
-  CStrings:  4663
+  Functions: 4162
+  Symbols:   5671
+  CStrings:  4671
 
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
- _CalAlertSharedEventChanges
- _CalAlertUnacknowledgedInvitations
- _CalDatabaseCopyEventIDsThatMatchLocationOrSummary
- _EKAttachmentProperty_securityScopedURLWrapperForPendingFileCopy
- _NSFileProtectionCompleteUnlessOpen
- _NSFileProtectionKey
- __CalAttachmentFileSetQuarantineAttributesForFile
- _kCalSecurityScopedURLWrapperMethods
- _pthread_cond_signal
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
+ "setResourceValues:error:"
- "CalDatabaseCopyEventIDsThatMatchLocationOrSummary"
- "Failed to change dataclass of attachment at path %@. Error = %@"
- "Failed to copy attachment (error: %@)."
- "InvitationAlerts"
- "SELECT rowid FROM CalendarItem WHERE location LIKE '%%%@%%' or summary LIKE '%%%@%%';"
- "SharedEventAlerts"
- "absoluteURL"
- "copyItemAtPath:toPath:error:"
- "securityScopedURLWrapperForPendingFileCopy"
- "setAttributes:ofItemAtPath:error:"

```
