## AccessoryDeveloperSettings

> `/System/Library/PreferenceBundles/AccessoryDeveloperSettings.bundle/AccessoryDeveloperSettings`

```diff

-760.20.1.0.0
-  __TEXT.__text: 0x1c98
-  __TEXT.__auth_stubs: 0x180
-  __TEXT.__objc_stubs: 0x960
+770.8.1.0.0
+  __TEXT.__text: 0x28f4
+  __TEXT.__auth_stubs: 0x3e0
+  __TEXT.__objc_stubs: 0xb00
   __TEXT.__objc_methlist: 0x184
   __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__objc_methname: 0xb28
-  __TEXT.__cstring: 0x5df
+  __TEXT.__gcc_except_tab: 0x90
+  __TEXT.__objc_methname: 0xc5c
+  __TEXT.__cstring: 0x655
   __TEXT.__ustring: 0x26
   __TEXT.__objc_classname: 0x61
   __TEXT.__objc_methtype: 0x1ce
-  __TEXT.__unwind_info: 0xec
-  __DATA_CONST.__auth_got: 0xd0
-  __DATA_CONST.__got: 0x90
+  __TEXT.__oslogstring: 0x5c3
+  __TEXT.__unwind_info: 0xe8
+  __DATA_CONST.__auth_got: 0x200
+  __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0x190
-  __DATA_CONST.__cfstring: 0x740
+  __DATA_CONST.__cfstring: 0x860
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x70
+  __DATA_CONST.__objc_classrefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x500
-  __DATA.__objc_selrefs: 0x2e8
+  __DATA.__objc_selrefs: 0x350
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C543A740-76E3-397D-93B6-B324616A870F
+  UUID: 39349D44-EC2C-303B-B4F0-B75C0284FDF4
   Functions: 41
-  Symbols:   67
-  CStrings:  269
+  Symbols:   109
+  CStrings:  323
 
Symbols:
+ _NSCocoaErrorDomain
+ _NSFilePosixPermissions
+ _NSPageSize
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSString
+ ___error
+ __os_log_error_impl
+ __os_log_fault_impl
+ __os_log_impl
+ _archive_entry_filetype
+ _archive_entry_pathname_utf8
+ _archive_entry_perm
+ _archive_entry_set_perm
+ _archive_entry_size
+ _archive_entry_size_is_set
+ _archive_entry_update_pathname_utf8
+ _archive_error_string
+ _archive_read_close
+ _archive_read_data_block
+ _archive_read_free
+ _archive_read_new
+ _archive_read_next_header
+ _archive_read_open_fd
+ _archive_read_support_filter_all
+ _archive_read_support_format_zip
+ _archive_write_close
+ _archive_write_data_block
+ _archive_write_disk_new
+ _archive_write_disk_set_options
+ _archive_write_disk_set_standard_lookup
+ _archive_write_finish_entry
+ _archive_write_free
+ _archive_write_header
+ _close
+ _free
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _open
+ _os_log_type_enabled
+ _realpath$DARWIN_EXTSN
+ _strerror
+ _strlen
CStrings:
+ "%@"
+ "%@ %@"
+ "(%@)"
+ "?"
+ "ADSUnarchiver: archive_entry with absolute path encountered...ignoring leading %zu of %zu bytes."
+ "ADSUnarchiver: archive_entry with no path after sanitization encountered."
+ "ADSUnarchiver: archive_entry with no path encountered."
+ "ADSUnarchiver: archive_read unable to set supported compression formats - %{public}s."
+ "ADSUnarchiver: archive_read unable to set supported formats - %{public}s."
+ "ADSUnarchiver: archive_read_data_block failed - %{public}s."
+ "ADSUnarchiver: archive_read_next_header failed - %{public}s."
+ "ADSUnarchiver: archive_write_data_block failed - %{public}s."
+ "ADSUnarchiver: archive_write_disk unable to set lookup functions - %{public}s."
+ "ADSUnarchiver: archive_write_disk unable to set options - %{public}s."
+ "ADSUnarchiver: archive_write_finish_entry failed - %{public}s."
+ "ADSUnarchiver: archive_write_header failed - %{public}s."
+ "ADSUnarchiver: failed to create directory at %@ - %@."
+ "ADSUnarchiver: unable to close archive_read - %{public}s."
+ "ADSUnarchiver: unable to close archive_write_disk - %{public}s."
+ "ADSUnarchiver: unable to close file descriptor %{public}d for %@ (leaking) - %{public}s."
+ "ADSUnarchiver: unable to free archive_read (leaking) - %{public}s."
+ "ADSUnarchiver: unable to free archive_write_disk (leaking) - %{public}s."
+ "ADSUnarchiver: unable to open archive_read - %{public}s."
+ "ADSUnarchiver: unable to open file %@ - %{public}s."
+ "ADSUnarchiver: unable to open non-file URL %@."
+ "ADSUnarchiver: unable to resolve physical path for destination path %@ - %s."
+ "CFBundleVersion"
+ "Disclaimer"
+ "Info.plist"
+ "URLByAppendingPathComponent:"
+ "code"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "dictionaryWithContentsOfURL:"
+ "dictionaryWithObjects:forKeys:count:"
+ "domain"
+ "failed to unzip theme asset"
+ "fileSystemRepresentation"
+ "i"
+ "initWithUTF8String:"
+ "isFileURL"
+ "length"
+ "objectForKey:"
+ "stringByAppendingPathComponent:"
+ "stringWithFormat:"
+ "unzipped theme asset"
+ "v28@?0@\"NSURL\"8@\"NSString\"16B24"
- "v20@?0@\"NSURL\"8B16"

```
