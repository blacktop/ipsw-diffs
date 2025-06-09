## diskarbitrationd

> `/usr/libexec/diskarbitrationd`

```diff

-490.120.6.0.1
-  __TEXT.__text: 0x191f0
-  __TEXT.__auth_stubs: 0x1690
-  __TEXT.__objc_stubs: 0x520
+535.0.0.0.0
+  __TEXT.__text: 0x19ad4
+  __TEXT.__auth_stubs: 0x16b0
+  __TEXT.__objc_stubs: 0x5c0
   __TEXT.__objc_methlist: 0xc8
-  __TEXT.__cstring: 0x2cfc
-  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x2eb2
+  __TEXT.__const: 0x88
   __TEXT.__oslogstring: 0xb
-  __TEXT.__gcc_except_tab: 0xd4
+  __TEXT.__gcc_except_tab: 0xe0
   __TEXT.__objc_classname: 0x2b
-  __TEXT.__objc_methname: 0x475
+  __TEXT.__objc_methname: 0x4c9
   __TEXT.__objc_methtype: 0x102
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x5c8
-  __DATA_CONST.__auth_got: 0xb58
+  __TEXT.__unwind_info: 0x5d0
+  __DATA_CONST.__auth_got: 0xb68
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xd48
-  __DATA_CONST.__cfstring: 0x1e00
+  __DATA_CONST.__const: 0xda8
+  __DATA_CONST.__cfstring: 0x1f20
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x168
-  __DATA.__objc_selrefs: 0x188
+  __DATA.__objc_selrefs: 0x1b0
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x130

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 85B2CB67-7F72-3BA0-856F-AF6900366BD6
-  Functions: 494
-  Symbols:   408
-  CStrings:  872
+  UUID: A195F9DF-104C-3553-8300-862471B47228
+  Functions: 499
+  Symbols:   410
+  CStrings:  903
 
Symbols:
+ _objc_alloc
+ _objc_retain_x24
+ _setenv
+ _sysctlbyname
- _objc_opt_new
- _objc_retain_x23
CStrings:
+ " created filesystem, id = %@. %@"
+ "-X"
+ "0"
+ "0E239BC6-F960-3107-89CF-1C97F78BB46B"
+ "DAMountAlwaysRepair"
+ "DARepairRunning"
+ "FSKitModulesProbe"
+ "MallocXzoneEarlyAlloc"
+ "Skipping exfat.fs as FSKitModulesProbe pref is on"
+ "Skipping msdos.fs as %s pref is on"
+ "apfs_fskit"
+ "com.apple.private.diskarbitrationd.user_audit_token"
+ "containsString:"
+ "exfat"
+ "exfat.fs"
+ "hfs_fskit"
+ "initWithFormat:"
+ "initWithUTF8String:"
+ "invoking sysctl(vfs.generic.print_busy_vnodes) to enable busy vnodes %@"
+ "invoking unmount after enabling busy vnodes %@"
+ "msdos-efi"
+ "proxyResourceForBSDName:isWritable:"
+ "rangeOfCharacterFromSet:"
+ "setLimited:"
+ "sharedInstance"
+ "substringToIndex:"
+ "sysctl(vfs.generic.print_busy_vnodes) failed with %x %d"
+ "vfs.generic.print_busy_vnodes"
- " created filesystem, id = %@."
- "Skipping msdos.fs as msdosUseFSKitModule pref is on"
- "enableFSKitModules"
- "proxyResourceForBSDName:writable:"
- "stringWithFormat:"
- "stringWithUTF8String:"

```
