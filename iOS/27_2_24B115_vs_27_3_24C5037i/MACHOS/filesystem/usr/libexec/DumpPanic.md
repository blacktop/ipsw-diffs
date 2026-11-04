## DumpPanic

> `/usr/libexec/DumpPanic`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-41.40.7.0.0
-  __TEXT.__text: 0x2aee0
-  __TEXT.__auth_stubs: 0x1180
-  __TEXT.__objc_stubs: 0x2660
-  __TEXT.__objc_methlist: 0x8bc
-  __TEXT.__cstring: 0x2b8b
+41.60.2.0.0
+  __TEXT.__text: 0x2c190
+  __TEXT.__auth_stubs: 0x11f0
+  __TEXT.__objc_stubs: 0x26c0
+  __TEXT.__objc_methlist: 0x8dc
+  __TEXT.__cstring: 0x2b0b
   __TEXT.__objc_classname: 0x12c
   __TEXT.__objc_methtype: 0x546
-  __TEXT.__objc_methname: 0x1fdb
-  __TEXT.__const: 0x2e0
+  __TEXT.__objc_methname: 0x204d
+  __TEXT.__const: 0x2f0
   __TEXT.__gcc_except_tab: 0xbdc
-  __TEXT.__oslogstring: 0x49a8
+  __TEXT.__oslogstring: 0x4e98
   __TEXT.__ustring: 0x1c6
   __TEXT.__constg_swiftt: 0x90
   __TEXT.__swift5_typeref: 0x8b
   __TEXT.__swift5_reflstr: 0x27
   __TEXT.__swift5_fieldmd: 0x34
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xd80
+  __TEXT.__unwind_info: 0xde0
   __TEXT.__eh_frame: 0xa0
   __DATA_CONST.__const: 0x780
   __DATA_CONST.__cfstring: 0x2400

   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA_CONST.__auth_got: 0x8d8
+  __DATA_CONST.__auth_got: 0x910
   __DATA_CONST.__got: 0x2b0
   __DATA_CONST.__auth_ptr: 0x78
-  __DATA.__objc_const: 0x10e0
-  __DATA.__objc_selrefs: 0xb08
-  __DATA.__objc_ivar: 0xa0
+  __DATA.__objc_const: 0x1140
+  __DATA.__objc_selrefs: 0xb20
+  __DATA.__objc_ivar: 0xac
   __DATA.__objc_data: 0x528
   __DATA.__data: 0x3b8
   __DATA.__common: 0x28

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 870
-  Symbols:   400
-  CStrings:  1340
+  Functions: 898
+  Symbols:   408
+  CStrings:  1368
 
Symbols:
+ __os_log_fault_impl
+ _arc4random
+ _dirname_r
+ _fdopen
+ _fgetxattr
+ _fsetxattr
+ _geteuid
+ _gzdopen
+ _mkstemp
+ _openat
+ _renameat
+ _unlinkat
- _getxattr
- _mktemp
- _rename
- _setxattr
CStrings:
+ "%s no longer refers to the core we processed, not removing it"
+ "/private/var/tmp/panicregion.XXXXXXXX"
+ "2"
+ "Cannot remove untrusted staged '%{public}@' : %{public}@"
+ "DumpPanicDone cookie already exists at path %s"
+ "DumpPanicDone cookie at %s is not the file we wrote (mode 0%o uid %u)"
+ "Failed to open %s core compressed output file"
+ "Failed to rename compressed %s from %s to %s with error : %s"
+ "_input_core_dev"
+ "_input_core_fd"
+ "_input_core_ino"
+ "closeInputCore"
+ "directory %s was not owned by root:wheel (uid %u gid %u), taking ownership"
+ "failed to create DumpPanicDone cookie at path %s with error %s"
+ "failed to create a temporary file for the panic region. Error: %s"
+ "failed to create staged file %s with error: %s"
+ "failed to derive the directory holding %s with error: %s"
+ "failed to open directory %s with error: %s"
+ "failed to open the directory holding %s with error: %s"
+ "failed to remove %s with error: %s"
+ "fdopen of %s failed with error: %s"
+ "fgetxattr %s returned error : %s"
+ "fstat of %s failed with error: %s"
+ "fstat of directory %s failed with error: %s"
+ "gzdopen of %s/%s failed"
+ "gzdopen(%s, wb) error: %s"
+ "lstat of %s failed with error: %s"
+ "lstat of staged '%{public}@' failed with error %s"
+ "open(%s) error: %s"
+ "refusing core at %s : not a regular file (mode 0%o)"
+ "refusing core at %s : owned by uid %u and not from a directory only uid %u can write"
+ "refusing core at %s : unexpected link count %u"
+ "refusing core at %s : writable by others (mode 0%o)"
+ "refusing to pull in staged '%{public}@' : not a file we wrote (mode 0%o uid %u nlink %u)"
+ "refusing untrusted directory %s (uid %u mode 0%o)"
+ "removeOriginalCore"
+ "stagedFileIsOurs:"
+ "staging compressed %s core at %s/%s"
+ "tempUserSpaceCore.%08x%08x"
- "-[CoreFileHandler getPanicRegion]"
- "/private/var/mobile/Library/Logs/CrashReporter/Panics/staged/tempUserSpaceCore.XXX"
- "/private/var/tmp/panicregion.XXX"
- "Failed to open %s core compressed output file with error %s"
- "Failed to rename compressed %s from %s to %s"
- "failed to creat() DumpPanicDone cookie at path %s with error %s"
- "getxattr %s returned error : %s"
- "gzopen %s"
- "gzopen(%s, wb) error: %s"
- "handlekernelcore.m"
- "panicRegionTempFile != NULL"
```
