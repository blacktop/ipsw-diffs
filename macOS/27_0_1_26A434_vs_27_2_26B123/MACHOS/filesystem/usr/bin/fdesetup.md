## fdesetup

> `/usr/bin/fdesetup`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1842.1.1.0.0
-  __TEXT.__text: 0x2c08c
-  __TEXT.__auth_stubs: 0xfb0
-  __TEXT.__objc_stubs: 0x27a0
+1847.40.6.0.0
+  __TEXT.__text: 0x2cb30
+  __TEXT.__auth_stubs: 0x1020
+  __TEXT.__objc_stubs: 0x2780
   __TEXT.__objc_methlist: 0x61c
-  __TEXT.__const: 0x109
+  __TEXT.__const: 0x111
   __TEXT.__gcc_except_tab: 0x964
-  __TEXT.__oslogstring: 0x98bf
-  __TEXT.__cstring: 0xf767
+  __TEXT.__oslogstring: 0x9909
+  __TEXT.__cstring: 0x1022a
   __TEXT.__objc_classname: 0x6d
-  __TEXT.__objc_methname: 0x23d9
-  __TEXT.__objc_methtype: 0x377
-  __TEXT.__unwind_info: 0xb70
+  __TEXT.__objc_methname: 0x23d0
+  __TEXT.__objc_methtype: 0x37a
+  __TEXT.__unwind_info: 0xb78
   __DATA_CONST.__const: 0x590
-  __DATA_CONST.__cfstring: 0x22e0
+  __DATA_CONST.__cfstring: 0x24c0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x7e8
-  __DATA_CONST.__got: 0x398
+  __DATA_CONST.__auth_got: 0x820
+  __DATA_CONST.__got: 0x370
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x4a0
-  __DATA.__objc_selrefs: 0xac0
+  __DATA.__objc_selrefs: 0xab8
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x4ae

   - /usr/lib/libcsfde.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libodfde.dylib
-  Functions: 731
-  Symbols:   379
-  CStrings:  1803
+  Functions: 733
+  Symbols:   381
+  CStrings:  1842
 
Symbols:
+ _fchmod
+ _fchown
+ _fstatat
+ _fsync
+ _openat
+ _unlinkat
+ _write
- _NSFileGroupOwnerAccountID
- _NSFileGroupOwnerAccountName
- _NSFileOwnerAccountID
- _NSFileOwnerAccountName
- _NSFilePosixPermissions
CStrings:
+ "       Record the key below immediately.\n"
+ "       Recovery key could not be written and cannot be displayed due to\n       the managed com.apple.MCX.FileVault2/ShowRecoveryKey preference.\n       The rotated key is unrecoverable from this run.\n"
+ "       Recovery key could not be written and cannot be displayed due to\n       the managed com.apple.MCX.FileVault2/ShowRecoveryKey preference.\n       The rotated key is unrecoverable from this run. Fix the output\n       path or the managed preference and re-run.\n"
+ "."
+ ".."
+ "/System/Volumes/Data"
+ "/System/Volumes/Data/home"
+ "/etc"
+ "/etc/"
+ "/home"
+ "/home/"
+ "/private"
+ "/private/etc"
+ "/private/tmp"
+ "/private/var"
+ "/tmp"
+ "/tmp/"
+ "/var"
+ "/var/"
+ "19:37:33"
+ "Error: Cannot create output file '%s' (errno=%d).\n"
+ "Error: Cannot inspect output path '%s' (errno=%d).\n"
+ "Error: Cannot open existing output file '%s' (errno=%d).\n"
+ "Error: Cannot open output path parent '%s' (errno=%d).\n"
+ "Error: Cannot truncate output file '%s' (errno=%d).\n"
+ "Error: Cannot truncate output file '%s' (errno=%d, Operation not permitted). Check for uchg/schg flags with 'ls -laO'.\n"
+ "Error: Could not restrict permissions on output file '%s' (errno=%d).\n       Refusing to write the recovery key.\n"
+ "Error: Could not write recovery info to '%s' (errno=%d).\n"
+ "Error: FileVault was enabled but recovery key could not be written to '%s'.\n"
+ "Error: Institutional recovery key was rotated but info could not be written to '%s'.\n       The recovery keychain is in place, but the escrow record is missing.\n       Re-run with a writable, root-owned parent directory that is not a symbolic link.\n"
+ "Error: Invalid output path '%s'.\n"
+ "Error: Output path already exists and cannot be safely reused: '%s' (mode=0%o, nlink=%u, uid=%u).\n"
+ "Error: Output path changed between check and open: '%s'\n"
+ "Error: Output path contains a symlink and cannot be used: '%s'\n"
+ "Error: Output path is a symlink and cannot be used: '%s'\n"
+ "Error: Output path is immutable and cannot be overwritten: '%s' (flags=0x%x). Clear with 'sudo chflags nouchg noschg %s' if intentional.\n"
+ "Error: Output path parent directory does not exist: '%s'.\n       fdesetup does not auto-create parent directories.\n"
+ "Error: Output path parent is a protected directory: '%s'.\n"
+ "Error: Recovery key was rotated but could not be written to '%s'.\n       The previous recovery key is no longer valid.\n"
+ "Error: Refusing to enable FileVault because output path '%s' cannot be written safely.\n"
+ "Error: Refusing to rotate personal recovery key because output path '%s' cannot be written safely. Previous recovery key is unchanged.\n"
+ "Error: unable to write FileVault recovery info to '%s'. The recovery key was rotated but the new key material could not be written to the requested output path. Re-run with a writable, root-owned parent directory that is not a symbolic link.\n"
+ "Oct  3 2026"
+ "enableFDEFileVault:recoveryKey:hasPersonalRecoveryUser:authRestart:outputPath:keychainInfo:skipInternalOutputWrite:"
+ "fdesetup: WriteSerializedFDEInfoToHeldFd fchmod failed errno=%d - aborting write to '%s'"
+ "fdesetup: WriteSerializedFDEInfoToHeldFd fchown errno=%d"
+ "fdesetup: WriteSerializedFDEInfoToHeldFd ftruncate errno=%d"
+ "fdesetup: WriteSerializedFDEInfoToHeldFd write errno=%d"
+ "fdesetup: enable refused, preflight failed"
+ "i56@0:8B16^@20B28B32@36@44B52"
+ "stringByAppendingString:"
- "20:26:59"
- "Aug  8 2026"
- "enableFDEFileVault:recoveryKey:hasPersonalRecoveryUser:authRestart:outputPath:keychainInfo:"
- "fdesetup: File already exists at path '%s'.  It will be replaced.\n"
- "fdesetup: WriteFDEInfoToPath creating folder '%s' failed."
- "fdesetup: WriteFDEInfoToPath file exists at path = %s"
- "fdesetup: WriteFDEInfoToPath writing key to path '%s' failed."
- "fdesetup: WriteFDEInfoToPath writing outDataLength = %ld"
- "i52@0:8B16^@20B28B32@36@44"
- "setAttributes:ofItemAtPath:error:"
- "wheel"
- "writeToFile:atomically:"
```
