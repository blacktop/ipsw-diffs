## ArchiveService

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/XPCServices/ArchiveService.xpc/ArchiveService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_classname`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_ivar`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1857.1.8.0.0
-  __TEXT.__text: 0x2d7d4
-  __TEXT.__auth_stubs: 0x1ae0
-  __TEXT.__objc_stubs: 0x1de0
-  __TEXT.__objc_methlist: 0x6dc
-  __TEXT.__gcc_except_tab: 0x4064
-  __TEXT.__const: 0x8ea
-  __TEXT.__cstring: 0x1b42
-  __TEXT.__oslogstring: 0x13d0
-  __TEXT.__objc_methname: 0x2467
+1857.2.6.0.0
+  __TEXT.__text: 0x2fe18
+  __TEXT.__auth_stubs: 0x1bb0
+  __TEXT.__objc_stubs: 0x1ec0
+  __TEXT.__objc_methlist: 0x6e4
+  __TEXT.__gcc_except_tab: 0x449c
+  __TEXT.__const: 0x8fa
+  __TEXT.__cstring: 0x1d22
+  __TEXT.__oslogstring: 0x1550
+  __TEXT.__objc_methname: 0x24e7
   __TEXT.__objc_classname: 0xd2
-  __TEXT.__objc_methtype: 0xbcf
+  __TEXT.__objc_methtype: 0xbdf
   __TEXT.__swift5_typeref: 0xb6
   __TEXT.__swift5_reflstr: 0x95
   __TEXT.__swift5_assocty: 0x18

   __TEXT.__swift5_fieldmd: 0xb8
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x1380
+  __TEXT.__unwind_info: 0x13f0
   __TEXT.__eh_frame: 0xe0
-  __DATA_CONST.__const: 0x13c0
-  __DATA_CONST.__cfstring: 0x10c0
+  __DATA_CONST.__const: 0x1408
+  __DATA_CONST.__cfstring: 0x1860
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__objc_arraydata: 0x48
-  __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0xd80
-  __DATA_CONST.__got: 0x498
+  __DATA_CONST.__objc_arraydata: 0x230
+  __DATA_CONST.__objc_arrayobj: 0x48
+  __DATA_CONST.__auth_got: 0xde8
+  __DATA_CONST.__got: 0x4a8
   __DATA_CONST.__auth_ptr: 0xf0
   __DATA.__objc_const: 0x7b8
-  __DATA.__objc_selrefs: 0x8a8
+  __DATA.__objc_selrefs: 0x8e0
   __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0x1d0
   __DATA.__data: 0x348
+  __DATA.__thread_vars: 0x30
+  __DATA.__thread_bss: 0x10
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesPriv
+  - /System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libAppleArchive.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 695
-  Symbols:   743
-  CStrings:  824
+  Functions: 707
+  Symbols:   755
+  CStrings:  901
 
Symbols:
+ _NSURLCreationDateKey
+ _NSURLNameKey
+ _NSURLVolumeAvailableCapacityKey
+ __Z10SplitFrameRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __Z15PaddedBacktraceP7NSArrayIP8NSStringE
+ __Z19kTStringLiteralDataIJEE
+ __Z25RemoveResolveFlagsFromURLP5NSURL
+ __Z43DSArchiveApplyProcessQuarantineForArchiveFDiP5NSURLmPU15__autoreleasingP7NSError
+ __Z8DemangleRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __Z8PadToMaxRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEmS7_
+ __Z9BacktraceP7NSArrayIP8NSStringE
+ ___cxa_demangle
+ __tlv_bootstrap
+ _archive_entry_set_gid
+ _archive_entry_set_perm
+ _archive_entry_set_uid
+ _archive_filter_code
+ _archive_filter_count
+ _archive_read_extract2
+ _archive_read_support_format_raw
+ _archive_write_disk_new
+ _archive_write_disk_set_options
+ _archive_write_disk_set_standard_lookup
+ _fstat
+ _objc_retainBlock
+ _objc_retain_x6
+ _objc_retain_x9
- _AAExtractArchiveOutputStreamSetQuarantine
- _OBJC_CLASS_$_DSQuarantine
- __Z19kTStringLiteralDataIJLc109ELc111ELc98ELc105ELc108ELc101EEE
- __Z19kTStringLiteralDataIJLc112ELc114ELc105ELc118ELc97ELc116ELc101EEE
- __Z19kTStringLiteralDataIJLc118ELc97ELc114EEE
- __Z19kTStringLiteralDataIJLc46EEE
- __Z19kTStringLiteralDataIJLc46ELc108ELc111ELc99ELc97ELc108ELc105ELc122ELc101ELc100EEE
- __Z19kTStringLiteralDataIJLc46ELc84ELc114ELc97ELc115ELc104EEE
- __Z19kTStringLiteralDataIJLc65ELc112ELc112ELc108ELc105ELc99ELc97ELc116ELc105ELc111ELc110ELc115EEE
- __Z19kTStringLiteralDataIJLc67ELc111ELc110ELc116ELc97ELc105ELc110ELc101ELc114ELc115EEE
- __Z19kTStringLiteralDataIJLc68ELc111ELc99ELc117ELc109ELc101ELc110ELc116ELc115EEE
- __Z19kTStringLiteralDataIJLc68ELc97ELc116ELc97EEE
- __ZN10TCFURLInfoC1Ev
- __ZN15TFileDescriptorD1Ev
- _archive_read_extract
CStrings:
+ "/Developer/Applications"
+ "7z"
+ "@32@0:8@16^{archive=}24"
+ "AccessDeniedFull"
+ "B20@?0B8^@12"
+ "B32@0:8@16Q24"
+ "B72@0:8i16@20@28@36@44B52Q56^@64"
+ "B80@0:8i16@20@28B36@40Q48@56@64^@72"
+ "B80@0:8r*16^{archive_entry=}24^{archive=}32^{archive=}40@48@56@64^@72"
+ "B96@0:8i16@20@28@36Q44B52^{?=BB}56^{archive=}64^{archive_entry=}72@?80^@88"
+ "Can't name a raw stream after %{public}@; falling back"
+ "Couldn't extract entry from archive: %@"
+ "Couldn't read available capacity of %{public}@: %@"
+ "Couldn't set %lu as output format: %@"
+ "Not expanding %{public}@ as a raw stream: filter %d carries its own member name"
+ "Not expanding %{public}@ as a raw stream: it is not compressed"
+ "Refusing to expand the raw stream %{public}@: %lld bytes free, %lld compressed"
+ "Retrying %{public}@ as a raw compressed stream"
+ "TCFURLInfo::TranslateCFError -- status: %{public}s\n\t CFError: %{public}@\n\t URL: %{public}@\n\t Backtrace:\n%{public}s"
+ "TCFURLInfo::TranslateRawPOSIXError %{errno}d -> %{public}s, path: %{public}@\n%{public}s"
+ "Unrecognized archive format"
+ "[ \\t]*([0-9]+)[ \\t]+([0-9a-zA-Z._?+]+)[ \\t]+(0x[0-9a-f]+)[ \\t]+((.|\\n)*)"
+ "[ \\t]*([0-9]+)[ \\t]+([0-9a-zA-Z._?+]+)[ \\t]+(0x[0-9a-f]+)[ \\t]+([_$a-zA-Z][_$a-zA-Z0-9]*)((.|\\n)*)"
+ "_URLByRemovingResolveFlags"
+ "_allowsRawFallbackForArchiveURL:formats:"
+ "_checkRoomForRawExpansionAtURL:archiveURL:error:"
+ "_openArchiveWithFD:url:progress:passphrases:formats:useRawFormat:passState:archive:entry:readItemHandler:error:"
+ "_rawEntryNameForArchiveURL:fromArchive:"
+ "_resolveFlags"
+ "_unarchiveAppleArchiveWithFD:url:destinationURL:progress:passphrases:addToKeychain:formats:error:"
+ "_unarchiveEntryAtPath:entry:fromArchive:writeDisk:archiveURL:destinationURL:progress:error:"
+ "_unarchiveFromArchiveFD:url:passphrases:addToKeychain:destinationURL:formats:progress:readItemGroup:error:"
+ "a"
+ "apk"
+ "ar"
+ "archive_read_support_format_raw failed: %@"
+ "archive_write_close: %s"
+ "archive_write_disk_new failed: %@"
+ "attributesOfItemAtPath:error:"
+ "bz"
+ "bzip2"
+ "cab"
+ "callStackSymbols"
+ "cb7"
+ "cbr"
+ "cbz"
+ "deb"
+ "docx"
+ "epub"
+ "grz"
+ "gz"
+ "gzip"
+ "ipa"
+ "iso"
+ "iso9660"
+ "jar"
+ "lha"
+ "lrz"
+ "lz"
+ "lz4"
+ "lzh"
+ "lzma"
+ "lzo"
+ "lzop"
+ "mtree"
+ "pax"
+ "pkg"
+ "pptx"
+ "rar"
+ "setInvalidationHandler:"
+ "substringFromIndex:"
+ "substringToIndex:"
+ "taz"
+ "tb2"
+ "tbz"
+ "tbz2"
+ "tgz"
+ "timeIntervalSinceNow"
+ "tlz"
+ "tlz4"
+ "txz"
+ "tz"
+ "tz2"
+ "tzo"
+ "tzst"
+ "udeb"
+ "war"
+ "warc"
+ "xar"
+ "xip"
+ "xlsx"
+ "xz"
+ "z"
+ "zip"
+ "zipx"
+ "zst"
+ "zstd"
- "@36@0:8i16@20^@28"
- "AAExtractArchiveOutputStreamSetQuarantine failed"
- "AccessDenied"
- "B48@0:8@16@24Q32^@40"
- "B72@0:8r*16^{archive_entry=}24^{archive=}32@40@48@56^@64"
- "B76@0:8i16@20@28@36@44B52Q56B64^@68"
- "B84@0:8i16@20@28@36Q44^{archive=}52^{archive_entry=}60@?68^@76"
- "B88@0:8i16@20@28B36@40Q48@56@64B72B76^@80"
- "Could't extract entry from archive: %@"
- "Couldn't set %lu as ouput format: %@"
- "Failed to create AA quarantine template file"
- "TCFURLInfo::TranslateCFError -- status: %{public}s\n\t CFError: %{public}@\n\t URL: %{public}@\n\t Backtrace:\n%{public}@"
- "TCFURLInfo::TranslateRawPOSIXError %{errno}d -> %{public}s, path: %{public}@\n%{public}@"
- "_openArchiveWithFD:url:progress:passphrases:formats:archive:entry:readItemHandler:error:"
- "_quarantineDataFromArchiveFD:url:error:"
- "_settleQuarantineForUnarchivedFolder:quarantineData:options:error:"
- "_unarchiveAppleArchiveWithFD:url:destinationURL:progress:passphrases:addToKeychain:formats:useDefaultQuarantine:error:"
- "_unarchiveEntryAtPath:entry:fromArchive:archiveURL:destinationURL:progress:error:"
- "_unarchiveFromArchiveFD:url:passphrases:addToKeychain:destinationURL:formats:progress:readItemGroup:isAppleArchive:applyDefaultQuarantineInline:error:"
- "writeDefaultQuarantineTemplateFile"
```
