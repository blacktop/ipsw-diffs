## smbclientd

> `/System/Library/PrivateFrameworks/SMBClientProvider.framework/smbclientd`

```diff

-231.0.0.0.0
-  __TEXT.__text: 0x64684
-  __TEXT.__auth_stubs: 0x840
+231.100.5.0.0
+  __TEXT.__text: 0x5dfd4
+  __TEXT.__auth_stubs: 0x7b0
   __TEXT.__objc_stubs: 0x5340
   __TEXT.__objc_methlist: 0x2138
-  __TEXT.__const: 0x2bc
+  __TEXT.__const: 0x2cc
   __TEXT.__cstring: 0x143c
   __TEXT.__oslogstring: 0xe26d
   __TEXT.__objc_classname: 0x1ca
   __TEXT.__objc_methname: 0x65fa
   __TEXT.__objc_methtype: 0x2011
-  __TEXT.__gcc_except_tab: 0x2a00
+  __TEXT.__gcc_except_tab: 0x29fc
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x13d8
-  __DATA_CONST.__auth_got: 0x430
+  __TEXT.__unwind_info: 0x1380
+  __DATA_CONST.__auth_got: 0x3e8
   __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x22e8
   __DATA_CONST.__cfstring: 0xb20
   __DATA_CONST.__objc_classlist: 0xa0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppSSO.framework/AppSSO
+  - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /System/Library/PrivateFrameworks/LiveFS.framework/LiveFS
   - /System/Library/PrivateFrameworks/LiveFSFPHelper.framework/LiveFSFPHelper
   - /System/Library/PrivateFrameworks/SMBClientEngine.framework/SMBClientEngine
   - /System/Library/PrivateFrameworks/SMBSearch.framework/SMBSearch
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C7BBCA3C-4BFF-3522-90FA-DABAF3A4A4CD
-  Functions: 2285
-  Symbols:   240
+  UUID: 71826D84-6EF3-3F8D-8E48-C201FC52ECEE
+  Functions: 2284
+  Symbols:   230
   CStrings:  2657
 
Symbols:
+ _OBJC_CLASS_$_FSSharedMutableBuffer
+ _objc_retainAutoreleasedReturnValue
- _OBJC_CLASS_$_LiveFSSharedMutableBuffer
- ___chkstk_darwin
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x10
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "T{_FSFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II},V_liAttr"
+ "v200@0:8{_FSFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}16"
+ "{_FSFileAttributes=\"__fa_rsvd0\"Q\"fa_validmask\"Q\"fa_seqno\"Q\"fa_type\"I\"fa_mode\"I\"fa_nlink\"I\"fa_uid\"I\"fa_gid\"I\"fa_bsd_flags\"I\"fa_size\"Q\"fa_allocsize\"Q\"fa_fileid\"Q\"fa_parentid\"Q\"fa_atime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_mtime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_ctime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_birthtime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_backuptime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_addedtime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_int_flags\"I\"_pad0\"I}"
+ "{_FSFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}16@0:8"
- "T{_LIFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II},V_liAttr"
- "v200@0:8{_LIFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}16"
- "{_LIFileAttributes=\"__fa_rsvd0\"Q\"fa_validmask\"Q\"fa_seqno\"Q\"fa_type\"I\"fa_mode\"I\"fa_nlink\"I\"fa_uid\"I\"fa_gid\"I\"fa_bsd_flags\"I\"fa_size\"Q\"fa_allocsize\"Q\"fa_fileid\"Q\"fa_parentid\"Q\"fa_atime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_mtime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_ctime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_birthtime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_backuptime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_addedtime\"{timespec=\"tv_sec\"q\"tv_nsec\"q}\"fa_int_flags\"I\"_pad0\"I}"
- "{_LIFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}16@0:8"

```
