## ArchiveService

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/XPCServices/ArchiveService.xpc/ArchiveService`

```diff

-1728.0.0.0.0
-  __TEXT.__text: 0x1a38c
-  __TEXT.__auth_stubs: 0x1320
-  __TEXT.__objc_stubs: 0x1c00
-  __TEXT.__objc_methlist: 0x590
+1731.0.1.0.0
+  __TEXT.__text: 0x1a660
+  __TEXT.__auth_stubs: 0x1340
+  __TEXT.__objc_stubs: 0x1c20
+  __TEXT.__objc_methlist: 0x598
   __TEXT.__const: 0x128
-  __TEXT.__gcc_except_tab: 0x3600
-  __TEXT.__objc_methname: 0x24c1
-  __TEXT.__cstring: 0xb1d
+  __TEXT.__gcc_except_tab: 0x365c
+  __TEXT.__objc_methname: 0x24dd
+  __TEXT.__cstring: 0xb3c
   __TEXT.__objc_classname: 0x130
-  __TEXT.__objc_methtype: 0xdcf
-  __TEXT.__oslogstring: 0x104c
+  __TEXT.__objc_methtype: 0xdf3
+  __TEXT.__oslogstring: 0x106f
   __TEXT.__unwind_info: 0xc10
-  __DATA_CONST.__auth_got: 0x9a0
+  __DATA_CONST.__auth_got: 0x9b0
   __DATA_CONST.__got: 0x378
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x750
-  __DATA_CONST.__cfstring: 0x960
+  __DATA_CONST.__cfstring: 0x980
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0xdc8
-  __DATA.__objc_selrefs: 0x7e0
+  __DATA.__objc_selrefs: 0x7e8
   __DATA.__objc_ivar: 0x40
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x338

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 369
-  Symbols:   542
-  CStrings:  657
+  Symbols:   544
+  CStrings:  661
 
Symbols:
+ _AAFileStreamOpenWithFD
+ _archive_read_open_fd
+ _lseek
- _archive_read_open_filename
CStrings:
+ "@36@0:8i16@20^@28"
+ "@68@0:8i16@20@28@36Q44@52^@60"
+ "B68@0:8i16@20@28@36Q44@?52^@60"
+ "B72@0:8i16@20@28@36@44B52Q56^@64"
+ "B80@0:8i16@20@28B36@40Q48@56@64^@72"
+ "B84@0:8i16@20@28@36Q44^{archive=}52^{archive_entry=}60@?68^@76"
+ "Couldn't open the archive file"
+ "Couldn't open the archive file: %!@(MISSING)"
+ "^{AAByteStream_impl=}72@0:8i16@20@28@36B44^^{AEAContext_impl}48Q56^@64"
+ "_listAppleArchiveWithFD:url:progress:passphrases:formats:listItemHandler:error:"
+ "_openAppleArchiveReadStreamWithFD:url:progress:passphrases:addToKeychain:aeaContext:formats:error:"
+ "_openArchiveWithFD:url:progress:passphrases:formats:archive:entry:readItemHandler:error:"
+ "_openArchiveWithFD:url:progress:passphrases:formats:readItemHandler:error:"
+ "_quarantineDataFromArchiveFD:url:error:"
+ "_unarchiveAppleArchiveWithFD:url:destinationURL:progress:passphrases:addToKeychain:formats:error:"
+ "_unarchiveFromArchiveFD:url:passphrases:addToKeychain:destinationURL:formats:progress:readItemGroup:error:"
+ "archivedItemDescriptorsForFD:url:passphrases:progress:formats:destinationFolderURL:error:"
+ "i32@0:8@16^@24"
+ "openArchiveFile:error:"
- "@32@0:8@16^@24"
- "@64@0:8@16@24@32Q40@48^@56"
- "B64@0:8@16@24@32Q40@?48^@56"
- "B68@0:8@16@24@32@40B48Q52^@60"
- "B76@0:8@16@24B32@36Q44@52@60^@68"
- "B80@0:8@16@24@32Q40^{archive=}48^{archive_entry=}56@?64^@72"
- "^{AAByteStream_impl=}68@0:8@16@24@32B40^^{AEAContext_impl}44Q52^@60"
- "_listAppleArchiveWithItemURL:progress:passphrases:formats:listItemHandler:error:"
- "_openAppleArchiveReadStreamWithItemURL:progress:passphrases:addToKeychain:aeaContext:formats:error:"
- "_openArchiveWithItemURL:progress:passphrases:formats:archive:entry:readItemHandler:error:"
- "_openArchiveWithItemURL:progress:passphrases:formats:readItemHandler:error:"
- "_quarantineDataFromArchive:error:"
- "_unarchiveAppleArchiveWithItemURL:destinationURL:progress:passphrases:addToKeychain:formats:error:"
- "_unarchiveFromItemURL:passphrases:addToKeychain:destinationURL:formats:progress:readItemGroup:error:"
- "archivedItemsDescriptorsForItemURL:passphrases:progress:formats:destinationFolderURL:error:"

```
