## scodec_host_v1.im4p

> `Firmware/scodec/scodec_host_v1.im4p`

### Sections with Same Size but Changed Content

- `__DATA.__const`
- `__DATA.__data`
- `__DATA._rtk_patchbay`
- `__DATA._afk_sys_objt`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x4ccf8
-  __TEXT.__const: 0x3920
+  __TEXT.__text: 0x4ccfc
+  __TEXT.__const: 0x3938
   __TEXT.__cstring: 0x2a21
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
Symbols:
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/standalone/RTKit/usr/lib/Debug/armv8_chinook_Oz_flto_pac/libc11.a(bzero.S~armv8_chinook_Oz_flto_pac.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/standalone/RTKit/usr/lib/Debug/armv8_chinook_Oz_flto_pac/libc11.a(memcmp.S~armv8_chinook_Oz_flto_pac.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/standalone/RTKit/usr/lib/Debug/armv8_chinook_Oz_flto_pac/libc11.a(memmove.S~armv8_chinook_Oz_flto_pac.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/standalone/RTKit/usr/lib/Debug/armv8_chinook_Oz_flto_pac/libc11.a(stack_protector.c~armv8_chinook_Oz_flto_pac.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/standalone/RTKit/usr/lib/Debug/armv8_chinook_Oz_flto_pac/libplatform~asc_v7_no_lib.a(hibernate.S~armv8_chinook_Oz_flto_pac.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/standalone/RTKit/usr/lib/Debug/armv8_chinook_Oz_flto_pac/libplatform~asc_v7_no_lib.a(start_anywhere_4k_link16m.S~armv8_chinook_Oz_flto_pac.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/standalone/RTKit/usr/lib/Debug/armv8_chinook_Oz_flto_pac/libplatform~asc_v7_no_lib.a(vectors.S~armv8_chinook_Oz_flto_pac.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/standalone/RTKit/usr/lib/Debug/armv8_chinook_Oz_flto_pac/libplatform~asc_v7_no_lib.a(wfi_workarounds.S~armv8_chinook_Oz_flto_pac.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/RTKit_armv8_chinook_Oz_flto_pac/src/arch/armv8/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/RTKit_armv8_chinook_Oz_flto_pac/src/arch/armv8/../arm/hibernate/armv8/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/RTKit_armv8_chinook_Oz_flto_pac/src/arch/armv8/./start_anywhere/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/RTKit_armv8_chinook_Oz_flto_pac/src/lib/c11/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/RTKit_armv8_chinook_Oz_flto_pac/src/lib/c11/string//armv8/
+ __rtk_scheduler_crashlog_callback
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/standalone/RTKit/usr/lib/Debug/armv8_chinook_Oz_flto_pac/libc11.a(bzero.S~armv8_chinook_Oz_flto_pac.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/standalone/RTKit/usr/lib/Debug/armv8_chinook_Oz_flto_pac/libc11.a(memcmp.S~armv8_chinook_Oz_flto_pac.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/standalone/RTKit/usr/lib/Debug/armv8_chinook_Oz_flto_pac/libc11.a(memmove.S~armv8_chinook_Oz_flto_pac.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/standalone/RTKit/usr/lib/Debug/armv8_chinook_Oz_flto_pac/libc11.a(stack_protector.c~armv8_chinook_Oz_flto_pac.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/standalone/RTKit/usr/lib/Debug/armv8_chinook_Oz_flto_pac/libplatform~asc_v7_no_lib.a(hibernate.S~armv8_chinook_Oz_flto_pac.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/standalone/RTKit/usr/lib/Debug/armv8_chinook_Oz_flto_pac/libplatform~asc_v7_no_lib.a(start_anywhere_4k_link16m.S~armv8_chinook_Oz_flto_pac.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/standalone/RTKit/usr/lib/Debug/armv8_chinook_Oz_flto_pac/libplatform~asc_v7_no_lib.a(vectors.S~armv8_chinook_Oz_flto_pac.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/standalone/RTKit/usr/lib/Debug/armv8_chinook_Oz_flto_pac/libplatform~asc_v7_no_lib.a(wfi_workarounds.S~armv8_chinook_Oz_flto_pac.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/RTKit_debug/src/arch/armv8/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/RTKit_debug/src/arch/armv8/../arm/hibernate/armv8/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/RTKit_debug/src/arch/armv8/./start_anywhere/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/RTKit_debug/src/lib/c11/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/RTKit_debug/src/lib/c11/string//armv8/
- __scheduler_crashlog_callback
Functions:
~ __scheduler_crashlog_callback -> __rtk_scheduler_crashlog_callback : 380 -> 384
```
