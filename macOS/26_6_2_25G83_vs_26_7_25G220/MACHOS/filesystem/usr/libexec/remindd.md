## remindd

> `usr/libexec/remindd`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_reflstr`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_catlist2`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_doubleobj`
- `__DATA.__objc_stublist`

```diff

-3976.0.0.0.0
-  __TEXT.__text: 0x833004
-  __TEXT.__auth_stubs: 0x8330
-  __TEXT.__objc_stubs: 0x1b520
-  __TEXT.__objc_methlist: 0xa8e0
-  __TEXT.__const: 0x28798
-  __TEXT.__objc_methname: 0x277a1
-  __TEXT.__objc_classname: 0x5fc6
-  __TEXT.__objc_methtype: 0x4227
+3976.11.0.0.0
+  __TEXT.__text: 0x82bf68
+  __TEXT.__auth_stubs: 0x83c0
+  __TEXT.__objc_stubs: 0x1b5e0
+  __TEXT.__objc_methlist: 0xa938
+  __TEXT.__const: 0x287a8
+  __TEXT.__objc_methname: 0x278d1
+  __TEXT.__objc_classname: 0x5fe6
+  __TEXT.__objc_methtype: 0x4257
   __TEXT.__gcc_except_tab: 0x2558
-  __TEXT.__cstring: 0x17f37
-  __TEXT.__oslogstring: 0x5d680
+  __TEXT.__cstring: 0x17fd7
+  __TEXT.__oslogstring: 0x5daf0
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_typeref: 0x13e94
-  __TEXT.__swift5_fieldmd: 0xa448
-  __TEXT.__constg_swiftt: 0xca24
-  __TEXT.__swift5_builtin: 0x3c0
+  __TEXT.__swift5_typeref: 0x13ea4
+  __TEXT.__swift5_fieldmd: 0xa470
+  __TEXT.__constg_swiftt: 0xca4c
+  __TEXT.__swift5_builtin: 0x3d4
   __TEXT.__swift5_reflstr: 0xbdc5
   __TEXT.__swift5_assocty: 0x1f18
   __TEXT.__swift5_capture: 0x5e78
   __TEXT.__swift5_protos: 0x2d4
   __TEXT.__swift5_proto: 0x18f4
-  __TEXT.__swift5_types: 0xaf0
+  __TEXT.__swift5_types: 0xaf4
   __TEXT.__swift_as_entry: 0x1a0
   __TEXT.__swift_as_ret: 0x200
-  __TEXT.__swift5_mpenum: 0xc4
-  __TEXT.__unwind_info: 0x102c8
-  __TEXT.__eh_frame: 0x1f67c
-  __DATA_CONST.__auth_got: 0x41a8
-  __DATA_CONST.__got: 0x32b0
-  __DATA_CONST.__auth_ptr: 0x27b0
-  __DATA_CONST.__const: 0x24c50
+  __TEXT.__swift5_mpenum: 0xe8
+  __TEXT.__unwind_info: 0x10300
+  __TEXT.__eh_frame: 0x1f744
+  __DATA_CONST.__auth_got: 0x41f0
+  __DATA_CONST.__got: 0x32c8
+  __DATA_CONST.__auth_ptr: 0x27b8
+  __DATA_CONST.__const: 0x24ce0
   __DATA_CONST.__cfstring: 0x50e0
-  __DATA_CONST.__objc_classlist: 0xbd0
+  __DATA_CONST.__objc_classlist: 0xbd8
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_catlist2: 0x10
   __DATA_CONST.__objc_protolist: 0x520

   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_doubleobj: 0x30
-  __DATA.__objc_const: 0x1d1a8
-  __DATA.__objc_selrefs: 0x7a78
+  __DATA.__objc_const: 0x1d238
+  __DATA.__objc_selrefs: 0x7ac0
   __DATA.__objc_ivar: 0x480
-  __DATA.__objc_data: 0x8440
-  __DATA.__data: 0x1e260
+  __DATA.__objc_data: 0x8490
+  __DATA.__data: 0x1e2a0
   __DATA.__objc_stublist: 0x38
   __DATA.__bss: 0x23af0
   __DATA.__common: 0x9f0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 22135
-  Symbols:   4061
-  CStrings:  11477
+  Functions: 22151
+  Symbols:   4073
+  CStrings:  11504
 
Symbols:
+ _$s19ReminderKitInternal15REMFileDigesterO9sha512Sum10fileHandleSSSgSo06NSFileI0C_tFZ
+ _NSPOSIXErrorDomain
+ _OBJC_CLASS_$_NSFileHandle
+ _SANDBOX_CHECK_NO_REPORT
+ ___error
+ _close
+ _fcntl
+ _fcopyfile
+ _fstat
+ _lseek
+ _open
+ _sandbox_check_by_audit_token
CStrings:
+ "(file-read-data on caller-supplied attachment URL)"
+ "@56@0:8@16{?=[8I]}24"
+ "B64@0:8@16@24@32@40@48^@56"
+ "Failed to compute sha512 for attachment file through pinned handle; refusing to ingest {objectID: %{public}s, clientIdentity: %{public}s}"
+ "Failed to compute sha512 for attachment file; refusing to ingest {objectID: %{public}s, clientIdentity: %{public}s}"
+ "RDClientAttachmentSandboxCheck"
+ "Refusing to ingest attachment URL the caller cannot read {clientIdentity: %{public}s}"
+ "Refusing to ingest saved attachment URL the caller cannot read {clientIdentity: %{public}s}"
+ "[%{public}@] Attachment copy failed {attachmentID: %{public}@, copyResult: %d, copyErrno: %d, closeResult: %d, closeErrno: %d}"
+ "[%{public}@] Attachment source is not a regular file; refusing to ingest {url: %{public}@}"
+ "[%{public}@] Caller is not permitted to read attachment URL; refusing to ingest {path: %{public}s}"
+ "[%{public}@] F_GETPATH failed; refusing to ingest attachment {errno: %d}"
+ "[%{public}@] open() failed; refusing to ingest attachment {errno: %d, url: %{public}@}"
+ "[%{public}@] open(destination) failed {attachmentID: %{public}@, errno: %d}"
+ "[%{public}@] sandbox_check_by_audit_token() failed; refusing to ingest attachment {errno: %d, path: %{public}s}"
+ "authorizedReadHandleForFileURL:withAuditToken:"
+ "caller's sandbox profile"
+ "closeAndReturnError:"
+ "could not compute sha512 for attachment file"
+ "deviceIsiPhone"
+ "file-read-data"
+ "fileDescriptor"
+ "initWithFileDescriptor:closeOnDealloc:"
+ "isFileURL"
+ "supportsShoppingExperience"
+ "supportsShoppingReplicator"
+ "updateAttachmentFile:accountID:fileName:sha512Sum:sourceFileHandle:error:"
```
