## Shared Screen Viewer

> `/System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/Support/Shared Screen Viewer.app/Contents/MacOS/Shared Screen Viewer`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__objc_methname`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-756.36.5.2.0
-  __TEXT.__text: 0x110d64
-  __TEXT.__auth_stubs: 0x27d0
+766.5.0.0.0
+  __TEXT.__text: 0x1123c0
+  __TEXT.__auth_stubs: 0x2800
   __TEXT.__objc_stubs: 0x19d00
   __TEXT.__objc_methlist: 0xe368
   __TEXT.__objc_classname: 0xde5
   __TEXT.__objc_methname: 0x25264
-  __TEXT.__objc_methtype: 0x6392
-  __TEXT.__cstring: 0x2aca4
-  __TEXT.__const: 0x3430
-  __TEXT.__oslogstring: 0x1676d
+  __TEXT.__objc_methtype: 0x63b2
+  __TEXT.__cstring: 0x2b237
+  __TEXT.__const: 0x3450
+  __TEXT.__oslogstring: 0x16e31
   __TEXT.__gcc_except_tab: 0xbc0
   __TEXT.__ustring: 0x126
   __TEXT.__swift5_typeref: 0xc3

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x3a80
-  __DATA_CONST.__const: 0x1658
+  __TEXT.__unwind_info: 0x3ae8
+  __DATA_CONST.__const: 0x16b8
   __DATA_CONST.__cfstring: 0x7200
   __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_floatobj: 0x10
-  __DATA_CONST.__auth_got: 0x13f8
+  __DATA_CONST.__auth_got: 0x1410
   __DATA_CONST.__got: 0xa48
   __DATA_CONST.__auth_ptr: 0x68
   __DATA.__objc_const: 0x11d88
   __DATA.__objc_selrefs: 0x8668
   __DATA.__objc_ivar: 0xfbc
   __DATA.__objc_data: 0x1e08
-  __DATA.__data: 0x18c8
+  __DATA.__data: 0x18d8
   __DATA.__common: 0x19
   - /System/Library/Frameworks/AddressBook.framework/Versions/A/AddressBook
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5335
-  Symbols:   1005
-  CStrings:  11757
+  Functions: 5363
+  Symbols:   1008
+  CStrings:  11795
 
Symbols:
+ _fstat
+ _os_log_create
+ _pthread_once
+ _readlink
- _fchmod
CStrings:
+ " -> "
+ "Clipboard: %u unconsumed bytes after a complete inflate stream (trailing data in compressed payload)"
+ "Clipboard: declared uncompressed size %u but inflated %ld"
+ "Clipboard: declared uncompressed size %u exceeds maximum %u"
+ "Clipboard: declared uncompressed size %u too small, %u input bytes unconsumed"
+ "Clipboard: inflate error %d"
+ "Clipboard: inflate init error %d"
+ "ExpandUserInfo: expected %u bytes, inflated %u"
+ "InflateCursorImage: expected %u bytes, inflated %u"
+ "Not logging to %{public}s: %{public}s (errno %d: %{public}s). Found a %{public}s there: uid=%u gid=%u mode=%04o nlink=%u dev=%d ino=%llu%{public}s%{public}s. Left in place on purpose."
+ "Not logging to %{public}s: %{public}s (errno %d: %{public}s). Nothing is at that path now."
+ "Not logging to %{public}s: could not clear O_NONBLOCK (errno %d: %{public}s)."
+ "Not logging to %{public}s: fdopen failed (errno %d: %{public}s)."
+ "Not logging to %{public}s: out of memory."
+ "Protocol error - close connection"
+ "Raw rect size %llu invalid for %d x %d at %u bytes/pixel - close connection"
+ "Unable to allocate memory - close connection"
+ "ZRLE inflate produced no data - close connection"
+ "ZRLE rect size %llu invalid for %d x %d at %u bytes/pixel - close connection"
+ "ZRLE tile stream exhausted, %u rows left - close connection"
+ "ZRLE zero-sized rect %d x %d - close connection"
+ "Zlib inflate produced %u of %u expected bytes - close connection"
+ "Zlib rect size %llu invalid for %d x %d codec %u - close connection"
+ "block device"
+ "character device"
+ "conversationManager:conversation:participant:didUpdateNickname:reason:"
+ "could not open the log"
+ "declared uncompressed size %u but inflated %u"
+ "directory"
+ "fifo"
+ "logfile"
+ "not a regular file"
+ "not enough room for  palette RLE update2 %ld"
+ "not enough room for  palette RLE update3 %ld"
+ "not enough room for 2 bit palette update %ld"
+ "not enough room for 4 bit palette update %ld"
+ "not enough room for ZRLE RLE1 %ld"
+ "not enough room for ZRLE RLE2 %ld"
+ "not enough room for one palette update %ld"
+ "path does not name the inode we opened, or that inode has other links"
+ "regular file"
+ "symlink"
+ "truncated scrap: %ld byte(s) remain, need %lu for flavorDataLength"
+ "unable to allocate %u bytes for file copy message"
+ "uncompressed size = %ld (declared %u)"
+ "user image data size out of range - %u"
+ "user image did not decompress - skipping the picture"
+ "v56@0:8@\"TUConversationManager\"16@\"TUConversation\"24@\"TUConversationParticipant\"32@\"NSString\"40Q48"
+ "v56@0:8@16@24@32@40Q48"
- "Clipboard: inflate error %d\n"
- "Clipboard: inflate init error %d\n"
- "LFOpen failed - Couldn't open '%s'. %d: %s"
- "conversationManager:conversation:participant:didUpdateNickname:"
- "not enough room for  palette RLE update2 %lu"
- "not enough room for 2 bit palette update %lu"
- "not enough room for 4 bit palette update %lu"
- "not enough room for ZRLE RLE1 %lu"
- "not enough room for ZRLE RLE2 %lu"
- "uncompressed size = %ld"
- "v48@0:8@\"TUConversationManager\"16@\"TUConversation\"24@\"TUConversationParticipant\"32@\"NSString\"40"
```
