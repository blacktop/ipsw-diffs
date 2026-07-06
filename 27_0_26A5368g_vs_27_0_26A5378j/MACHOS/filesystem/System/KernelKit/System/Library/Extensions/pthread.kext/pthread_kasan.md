## pthread_kasan

> `/System/KernelKit/System/Library/Extensions/pthread.kext/pthread_kasan`

```diff

   __TEXT.__cstring: 0x72d
-  __TEXT_EXEC.__text: 0x8d38
+  __TEXT_EXEC.__text: 0x8d18
   __TEXT_EXEC.__auth_stubs: 0x440
   __DATA.__data: 0x148
   __DATA.__bss: 0x21
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__const : content changed
Symbols:
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jO0wXV/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/DerivedSources/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jO0wXV/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/kern_init.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jO0wXV/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/kern_support-addbc8be3a316519701a30dcfef656dd.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jO0wXV/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/kern_support-c84d895e5a8472b41520f69e7f365969.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jO0wXV/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/kern_synch.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jO0wXV/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/pthread.swiftmodule
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jO0wXV/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/pthread_info.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jO0wXV/Sources/libpthread_kernelkit/kern/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LFv4pp/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/DerivedSources/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LFv4pp/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/kern_init.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LFv4pp/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/kern_support-33476a9867ed3d52621062a6ee74c8aa.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LFv4pp/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/kern_support-6ce9755f0db02bbfc0a7816b88dd7ed5.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LFv4pp/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/kern_synch.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LFv4pp/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/pthread.swiftmodule
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LFv4pp/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/pthread_info.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LFv4pp/Sources/libpthread_kernelkit/kern/
Functions:
~ _find_nextlowseq : 168 -> 152
~ _find_nexthighseq : 168 -> 152

```
