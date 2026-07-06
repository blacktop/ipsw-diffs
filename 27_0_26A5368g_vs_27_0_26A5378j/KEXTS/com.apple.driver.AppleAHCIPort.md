## com.apple.driver.AppleAHCIPort

> `com.apple.driver.AppleAHCIPort`

```diff

   __TEXT.__const: 0x270
-  __TEXT.__cstring: 0x27a5
-  __TEXT_EXEC.__text: 0xe70c
+  __TEXT.__cstring: 0x28ec
+  __TEXT_EXEC.__text: 0xe8a8
   __TEXT_EXEC.__auth_stubs: 0x640
   __DATA.__data: 0x120
   __DATA.__common: 0x108

   __DATA_CONST.__got: 0xc0
   Functions: 416
   Symbols:   930
-  CStrings:  319
+  CStrings:  324
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Functions:
~ __ZN9AppleAHCI5startEP9IOService : 2708 -> 2920
~ __ZN13AppleAHCIPort13InitWithRangeEPVhyjP9AppleAHCIP15IORegistryEntry : 2640 -> 2572
~ __ZN13AppleAHCIPort19EnablePortOperationEv : 916 -> 928
~ __ZN13AppleAHCIPort14ScanForDevicesEv : 1144 -> 1152
~ __ZN13AppleAHCIPort19SoftResetDevicePortEjP8OSObjectPj : 1152 -> 1400
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gQglhl/Sources/AppleAHCI/ASMediaAppleAHCI.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gQglhl/Sources/AppleAHCI/AppleAHCI.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gQglhl/Sources/AppleAHCI/AppleAHCIPort.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gQglhl/Sources/AppleAHCI/AppleAHCIPortPolledAdapter.cpp"
+ "IOServiceBusyTimeoutExtensions"
+ "[AHCI][PRT][%08X] %s::%d:SoftResetDevicePort - fatal error during SRST\n"
+ "[AHCI][PRT][%08X] %s::%d:SoftResetDevicePort - fatal error during SRST clear\n"
+ "[AHCI][PRT][%08X] %s::%d:SoftResetDevicePort - link lost during SRST\n"
+ "[AHCI][PRT][%08X] %s::%d:SoftResetDevicePort - link lost during SRST clear\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n0zBM0/Sources/AppleAHCI/ASMediaAppleAHCI.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n0zBM0/Sources/AppleAHCI/AppleAHCI.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n0zBM0/Sources/AppleAHCI/AppleAHCIPort.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n0zBM0/Sources/AppleAHCI/AppleAHCIPortPolledAdapter.cpp"

```
