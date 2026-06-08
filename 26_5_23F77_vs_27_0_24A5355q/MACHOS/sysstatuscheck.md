## sysstatuscheck

> `/usr/libexec/sysstatuscheck`

```diff

-211.100.4.0.0
-  __TEXT.__text: 0xc090
-  __TEXT.__auth_stubs: 0x4f0
+230.0.0.0.0
+  __TEXT.__text: 0xd00c
+  __TEXT.__auth_stubs: 0x510
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x8e7
-  __TEXT.__gcc_except_tab: 0x538
-  __TEXT.__const: 0x498
-  __TEXT.__unwind_info: 0x508
-  __DATA_CONST.__auth_got: 0x280
-  __DATA_CONST.__got: 0x80
+  __TEXT.__gcc_except_tab: 0x5a4
+  __TEXT.__const: 0x548
+  __TEXT.__cstring: 0xc34
+  __TEXT.__unwind_info: 0x520
   __DATA_CONST.__const: 0x728
-  __DATA_CONST.__cfstring: 0x40
+  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0x78
   __DATA.__data: 0x60
-  __DATA.__bss: 0x4
+  __DATA.__bss: 0x4c
   __DATA.__common: 0x18
-  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: CCB3A20B-CD53-3433-B599-10CBA0919EAB
-  Functions: 246
+  UUID: 4CB02126-2F20-307A-8F0F-5D1EF5749532
+  Functions: 247
   Symbols:   128
-  CStrings:  66
+  CStrings:  82
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev
+ ___error
+ _chmod
+ _chown
+ _copyfile
+ _getpwnam
+ _mkdir
+ _os_variant_is_darwinos
+ _strerror
- _CFArrayCreate
- _CFDictionaryContainsKey
- _CFDictionaryGetValue
- _CFNumberGetValue
- _CFRelease
- _OSKextCopyLoadedKextInfo
- ___CFConstantStringClassReference
- _kCFAllocatorDefault
- _kCFTypeArrayCallBacks
CStrings:
+ "'%s' is not a directory: %x\n"
+ "'%s' is not a file: %x\n"
+ "/private/preboot/dramecc/"
+ "/private/var/hardware/dramecc/"
+ "Created database directory at '%s'.\n"
+ "Failed to copy file: %d (%s)\n"
+ "Failed to create directory '%s': %d (%s)\n"
+ "Failed to migrate ECC database (non-fatal).\n"
+ "Failed to migrate database from '%s' to '%s'.\n"
+ "Failed to panic or reboot device.\n"
+ "Failed to panic the device.\n"
+ "Failed to perform KHWM check because the device has debug boot-args.\n"
+ "Failed to perform KHWM check because we're running kasan kernel.\n"
+ "Failed to query UID for '%s'.\n"
+ "Failed to query file information for '%s': %d (%s)\n"
+ "Failed to read jetsam properties file.\n"
+ "Failed to reboot device.\n"
+ "Failed to remove file '%s': %d (%s)\n"
+ "Failed to reset darkboot flag.\n"
+ "Failed to set dark-boot flag.\n"
+ "Failed to update permisions to %04o and/or user/group ownership to %d/%d for '%s'.\n"
+ "Failed to update permissions for '%s' to %04o: %d (%s)\n"
+ "Failed to update permissions to %04o for '%s': %d (%s)\n"
+ "Failed to update user/group ownership for '%s' to %d/%d: %d (%s)\n"
+ "Failed to update user/group ownership to %d/%d for '%s': %d (%s)\n"
+ "Kernel memory exceeded limit on first pass but not second pass, not rebooting.\n"
+ "com.apple.sysstatuscheck"
+ "mobile"
- "Kernel memory exceeded limit on first pass, but not second pass, not rebooting\n"
- "OSBundleLoadTag"
- "could not do KHWM check because running kasan kernel\n"
- "could not do KHWM check because the device has debug boot-args\n"
- "could not read jetsam properties file\n"
- "could not reset darkboot\n"
- "could not set dark-boot flag\n"
- "kext not found\n"
- "no kext info\n"
- "reboot failed\n"

```
