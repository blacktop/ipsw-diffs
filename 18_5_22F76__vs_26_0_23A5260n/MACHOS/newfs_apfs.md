## newfs_apfs

> `/System/Library/Filesystems/apfs.fs/newfs_apfs`

```diff

-2332.120.31.0.2
-  __TEXT.__text: 0x51974
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__cstring: 0xfde7
-  __TEXT.__const: 0x7fd0
-  __TEXT.__unwind_info: 0x858
-  __DATA_CONST.__auth_got: 0x418
+2632.0.15.0.1
+  __TEXT.__text: 0x512e8
+  __TEXT.__auth_stubs: 0x8c0
+  __TEXT.__cstring: 0xfb8f
+  __TEXT.__const: 0x8380
+  __TEXT.__unwind_info: 0x840
+  __DATA_CONST.__auth_got: 0x460
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x510
+  __DATA_CONST.__const: 0x570
   __DATA_CONST.__cfstring: 0x140
   __DATA.__data: 0x150
   __DATA.__common: 0x418
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 432CE288-DA51-3A89-8B0C-00ACD1A98654
-  Functions: 706
-  Symbols:   146
-  CStrings:  1344
+  UUID: 2A9C0A91-4172-35C3-BA53-5CC969FE38A3
+  Functions: 703
+  Symbols:   155
+  CStrings:  1343
 
Symbols:
+ _CFCopyTypeIDDescription
+ _CFDictionaryApplyFunction
+ _CFNumberGetTypeID
+ _CFNumberGetValue
+ _CFStringGetCString
+ _CFStringGetCStringPtr
+ _IORegistryEntryCreateCFProperties
+ ___strlcat_chk
+ _printf
CStrings:
+ " ("
+ " ???"
+ "%03llu"
+ "%llu%s"
+ "%s > %s : %s"
+ "%s Err: unable to fetch properties\n"
+ "%s%llu %cB%s"
+ "%s%llu%-*.*s %cB%s"
+ "%s%llu.%.*s %cB%s"
+ "%s:%d: %s Fusion is not supported anymore\n"
+ "%s:%d: %s clonegroup tree creation failed: %s\n"
+ "%s:%d: %s clonegroups enabled for this volume\n"
+ "%s:%d: %s entitled reserve: reserved space underflow: %lld (%lld)\n"
+ "%s:%d: %s failed to delete fs clonegroup tree after fs creation failed: %d\n"
+ "%s:%d: %s superblock container size %lld greater than device size %lld\n"
+ "%s:%d: %s this volume requires valid UUID option specified\n"
+ "%s:%d: %s unentitled reserve: reserved space underflow: %lld (%lld)\n"
+ "%s:%d: %s<->superblock mismatch on fusion uuid\n"
+ "%s:%d: Volume role 0x%x is not supported"
+ "%s:%d: failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n"
+ "%ss%d\n"
+ ")"
+ "."
+ "2632.0.15.0.1"
+ "61706673-7575-6964-0300-766f6c756d00"
+ ":b:ieo:q:r:s:v:wACDWEG:PR:S:U:Txca"
+ "No"
+ "Yes"
+ "[-o options] [-b block-size] [[-s volume-size] | [-r volume-reserve] [-q volume-quota]] [-v volume-name] [-i | -e] [-U uid] [-G gid] [-E [-S passphrase | -W (empty password) ]] [-A | -C] [-R role] [-D] [-w] [-x] [-T] [-c] [-a] device"
+ "apfs-clonegroup-lock-mutex"
+ "authapfs_validate_node"
+ "nx_reaper_add_ext"
- "%s:%d: %s WBC area was not allocated on main device\n"
- "%s:%d: %s container block size too small for tier2 device block size (%d < %d)\n"
- "%s:%d: %s couldn't read tier2 device superblock of size %d\n"
- "%s:%d: %s failed to set tier2 device: %d\n"
- "%s:%d: %s failed to write superblock to fusion tier2 device block 0: %d\n"
- "%s:%d: %s superblock container size %lld greater than device size(s) %lld\n"
- "%s:%d: %s tier2 device superblock doesn't agree with main superblock\n"
- "%s:%d: %s xid %lld failed to write superblock to fusion tier2 device block 0: %d\n"
- "%s:%d: %s<->superblock mismatch on fusion uuid, tier2=%d\n"
- "%s:%d: Fusion creation failed: %d - %s\n"
- "%s:%d: FusionLC autodetect: LC Fusion\n"
- "%s:%d: FusionLC autodetect: regular Fusion\n"
- "%s:%d: It looks like you are trying to create an upside down Fusion: Main tier (%llu GB) is larger than Tier2 (%llu GB)\n"
- "%s:%d: error: block size %d is not an even multiple of tier2 device block size %d\n"
- "%s:%d: error: tier2 device is not writable!\n"
- "%s:%d: failed to set tier2 device\n"
- "%s:%d: tier2 device initialization failed: %d\n"
- "%s:%d: tier2 device initialization failed: %d - %s\n"
- "%s:%d: warning: fs block size too small for tier2 device block size (%d < %d)\n"
- "2332.120.31.0.2"
- ":b:ieo:q:r:s:v:wACDWEF:G:PR:S:U:Txca"
- "[-o options] [-b block-size] [[-s volume-size] | [-r volume-reserve] [-q volume-quota]] [-v volume-name] [-i | -e] [-U uid] [-G gid] [-E [-S passphrase | -W (empty password) ]] [-A | -C] [-F fusion] [-R role] [-D] [-w] [-x] [-T] [-c] [-a] device"
- "conflicting '-A' and '-F' options"
- "failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n"
- "fusionlc=no"
- "fusionlc=yes"
- "nx-fusion-mt-lock"
- "nx_rc_allocation_lock"
- "nx_reaper_add"
- "omap_set"
- "specify different 'main' and 'tier2' Fusion devices"
- "specify only a single 'tier2' Fusion device"
- "wbcsize="

```
