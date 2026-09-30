## pthread

> `/System/KernelKit/System/Library/Extensions/pthread.kext/pthread`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__const`

```diff

-553.0.0.0.0
+553.0.1.0.0
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0x72d
-  __TEXT_EXEC.__text: 0x6408
+  __TEXT_EXEC.__text: 0x6438
   __TEXT_EXEC.__auth_stubs: 0x370
   __DATA.__data: 0x13c
   __DATA.__bss: 0x21
Symbols:
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4JVyFt/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/DerivedSources/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4JVyFt/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-normal/arm64e/kern_support-cb1df991c07348c645760ceb342a09b1.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4JVyFt/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-normal/arm64e/pthread.swiftmodule
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4JVyFt/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-normal/arm64e/pthread_lto.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4JVyFt/Sources/libpthread_kernelkit/kern/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jO0wXV/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/DerivedSources/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jO0wXV/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-normal/arm64e/kern_support-addbc8be3a316519701a30dcfef656dd.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jO0wXV/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-normal/arm64e/pthread.swiftmodule
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jO0wXV/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-normal/arm64e/pthread_lto.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jO0wXV/Sources/libpthread_kernelkit/kern/
Functions:
~ __bsdthread_register : 1176 -> 1224
```
