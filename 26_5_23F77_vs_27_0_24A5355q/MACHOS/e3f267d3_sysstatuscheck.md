## sysstatuscheck

> `/usr/libexec/sysstatuscheck`

```diff

-211.100.4.0.0
-  __TEXT.__text: 0xc090 sha256:05057e5ff3763625d6ff3b2e3a6d4fea54de74e29fe4ff2243c29e264ebba7e3
-  __TEXT.__auth_stubs: 0x4f0 sha256:3cc07b55162d85c4522a994fa5bba5077b912ec622fe89fd65516cb52087d91f
-  __TEXT.__init_offsets: 0x4 sha256:33826d4aff0653c04e53fd36ecc2a75653ab382b03016834ec8495a7755ce92b
-  __TEXT.__cstring: 0x8e7 sha256:1cd5a182e08635e549973033c3f101b65b5a246811ca0fbfa159cca183a0e2b7
-  __TEXT.__gcc_except_tab: 0x538 sha256:91cd7ab75e8102f111d44f1662721f9213bedaaf40f86cbb9fe00a537f5e34a1
-  __TEXT.__const: 0x498 sha256:d1198c36bf1401179f6c2ff584c91a0a57c5bb43e8de300b8ab9976063044f34
-  __TEXT.__unwind_info: 0x508 sha256:e3b32ce3fefce74de564189b6cce2d209faf4bd3c5bf6381c3e0405e2d5cb705
-  __DATA_CONST.__auth_got: 0x280 sha256:cbef71e97c2ac714053fc8a0b20cb62fabf7d087813771e61963209e4313dc7f
-  __DATA_CONST.__got: 0x80 sha256:e8f1addaa815a0bfacd5d7aa8ab1ac3886c41ab68b8db1fa8ff643dbc43cdbab
-  __DATA_CONST.__const: 0x728 sha256:a30069016041dac87f706ebc8f073e35b9d12dabdc54f60d13d00364e5b145d9
-  __DATA_CONST.__cfstring: 0x40 sha256:af688b4bdbc3f73fbdde400d93ff45c801a5f66ca06d044455e980bc281140a8
+230.0.0.0.0
+  __TEXT.__text: 0xd00c sha256:3b3246b618c515d58222bb8ae40df41478e297fc0950ec789d4b1c11f757a070
+  __TEXT.__auth_stubs: 0x510 sha256:b4606f3470a05df86aeb46768a27f7ce9f990470024a190a55a0a1fd24a3c78f
+  __TEXT.__init_offsets: 0x4 sha256:e35dbd8b6a5a401a829ff3a1699e822413d82b8177dbfd19d2b4f63bd8f78ce7
+  __TEXT.__gcc_except_tab: 0x5a4 sha256:ae1d94d3f83028cd2673ac17723f0476215a17beff204f13a9c17842f7ec22f0
+  __TEXT.__const: 0x548 sha256:6c528cbc07a424b25ad7426b6619809dc277f4d43b4cbfabbefff43e826e01fa
+  __TEXT.__cstring: 0xc34 sha256:47d9c2c1419b946a88c77ab524e34350d02015ae8061addb68ab4b3a6749ee21
+  __TEXT.__unwind_info: 0x520 sha256:1a05b81a7915ad0c74f531cf53f2ae94ffbc5a1da14b5f2ff90162dbba5dda09
+  __DATA_CONST.__const: 0x728 sha256:202345c6168dc42d6cd0fed749cae591845faaefcd588ebe265a85fd9cf34e1f
+  __DATA_CONST.__auth_got: 0x290 sha256:4d4139ed7055ce6d1c1e737b48281dfb476ce92a93f1748bad963f18e4749d8a
+  __DATA_CONST.__got: 0x78 sha256:86886ce84e6e607018d058c4c0cc26b971654140667b968702b0da47eb735c6b
   __DATA.__data: 0x60 sha256:b68a94bc841e7461b54e435b7b883ece797ae9ab1bac2d3e8ebd5b39da6e7216
-  __DATA.__bss: 0x4 sha256:df3f619804a92fdb4057192dc43dd748ea778adc52bc498ce80524c014b81119
+  __DATA.__bss: 0x4c sha256:f2c0d5456a983ecd12e314fcfa19879179fc8424343baeb1325457472ae85601
   __DATA.__common: 0x18 sha256:9d908ecfb6b256def8b49a7c504e6c889c4b0e41fe6ce3e01863dd7b61a20aa0
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
