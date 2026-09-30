## com.apple.driver.AppleInputDeviceSupport

> `com.apple.driver.AppleInputDeviceSupport`

```diff

   __TEXT.__cstring: 0x2fb5
   __TEXT.__const: 0x78
   __TEXT.__os_log: 0xd6f
-  __TEXT_EXEC.__text: 0x1c388
+  __TEXT_EXEC.__text: 0x1c394
   __TEXT_EXEC.__auth_stubs: 0x7b0
   __DATA.__data: 0xc8
   __DATA.__common: 0x3a8
Sections:
~ __TEXT.__cstring : content changed
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Functions:
~ __ZN14AIDEventLogger16getStatIDForNameEPKc : 128 -> 140
~ __ZN17AIDReporterSimple12initReporterEP9IOServiceP12OSDictionaryty : 1760 -> 1740
~ __ZN18AIDImageDownloader15extractFromFtabEP6OSData : 596 -> 616
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OxcxL7/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/AIDImageDownloader.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OxcxL7/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/AIDService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OxcxL7/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/AIDSharedMemoryManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OxcxL7/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/FirmwareUpdate/AIDFirmwareImage4.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OxcxL7/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/FirmwareUpdate/AIDFirmwareUpdateService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OxcxL7/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/FirmwareUpdate/AIDFirmwareUpdateUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OxcxL7/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/Logger/AIDLoggerUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OxcxL7/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/Reporter/AIDEventLogger.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OxcxL7/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/Reporter/AIDReporter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OxcxL7/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/Reporter/AIDReporterSimple.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OxcxL7/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/Reporter/AIDReporterState.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OxcxL7/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/Reporter/AIDReporters.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iAsvfM/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/AIDImageDownloader.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iAsvfM/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/AIDService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iAsvfM/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/AIDSharedMemoryManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iAsvfM/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/FirmwareUpdate/AIDFirmwareImage4.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iAsvfM/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/FirmwareUpdate/AIDFirmwareUpdateService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iAsvfM/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/FirmwareUpdate/AIDFirmwareUpdateUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iAsvfM/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/Logger/AIDLoggerUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iAsvfM/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/Reporter/AIDEventLogger.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iAsvfM/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/Reporter/AIDReporter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iAsvfM/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/Reporter/AIDReporterSimple.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iAsvfM/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/Reporter/AIDReporterState.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iAsvfM/Sources/AppleInputDeviceSupport/AppleInputDeviceSupport/Reporter/AIDReporters.cpp"

```
