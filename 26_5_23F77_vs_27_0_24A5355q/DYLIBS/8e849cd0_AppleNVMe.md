## AppleNVMe

> `/System/Library/PrivateFrameworks/AppleNVMe.framework/AppleNVMe`

```diff

-819.120.3.0.0
-  __TEXT.__text: 0x9dc sha256:0814e6001d3d9f397ba24c569372aba34e82efee95a58fa6005b74ac0d33a062
-  __TEXT.__auth_stubs: 0x180 sha256:3e6cbb618cb8e18834161e7b72d3aa3528501e6dd36e466bebc10d87914fc9fa
+876.0.0.0.0
+  __TEXT.__text: 0x22d0 sha256:35448eb421dd58225dc3c58d389d714d977e5d61d7eb73f0bd8d68eb492f598d
   __TEXT.__const: 0x40 sha256:42cccc03d09da1a6df0e5e73fa5b3feff041d993408c193356b9a8140b2e79b5
-  __TEXT.__cstring: 0x3a6 sha256:9ade036b4049a9029469d640f8ef679c3c6bc7365a0eb8b0e196f930089e9eec
-  __TEXT.__unwind_info: 0x88 sha256:dfb26a2b67bbb182ee5c91ac90a0cabbe56fcaafbf9e90f467dfe39047e6626c
-  __DATA_CONST.__got: 0x40 sha256:f5a5fd42d16a20302798ef6ed309979b43003d2320d9f0e8ea9831a92759fb4b
-  __AUTH_CONST.__auth_got: 0xc0 sha256:5d89f056865052bcb89c910d2d62872e029fb273c3db03f8968a52a41593c1b5
-  __AUTH_CONST.__cfstring: 0x60 sha256:29803f323d8c51c0aaeb9f40c16239f2a0ca4ee316a445075b01f47bfa7aca8e
-  __DATA.__data: 0x80 sha256:0740181dbac54eda60de84eda18a2c4fa1cdd8ba69edfc3b9c3b9a8dfa1490ae
+  __TEXT.__cstring: 0xbaa sha256:82b9783fff403c1891638f35b88591847b6f237c562d7d64a909c41f263b2850
+  __TEXT.__unwind_info: 0xc8 sha256:a79d16cccd74b746a8e391e41f30989cc1c8eac9833fa34e588133292e049893
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0xd8 sha256:924dbf53359978e5bc3f9b6566bdafbe7a6d9a1622b74601d074f9a2f1108785
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__cfstring: 0x140 sha256:d96d65853629fb25cea30a553662db461f414d84f70fdd9dc7bbe78472b59aa7
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__data: 0x8 sha256:38e3b02accbce65a83bc12f0922a0f2e8ea63e9436772b2b04874916d3fdb128
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  UUID: C99D13D5-DAC5-3807-B53F-9860590B186F
-  Functions: 14
-  Symbols:   54
-  CStrings:  37
+  UUID: 27C67447-BC12-3923-8B77-8D7668B24836
+  Functions: 86
+  Symbols:   211
+  CStrings:  105
 
Symbols:
+ _AppleNVMePanicLogGetSize.cold.1
+ _AppleNVMePanicLogGetSize.cold.2
+ _AppleNVMePanicLogGetSize.cold.3
+ _AppleNVMePanicLogGetSize.cold.4
+ _AppleNVMePanicLogGetSize.cold.5
+ _AppleNVMePanicLogGetSize.cold.6
+ _AppleNVMePanicLogGetSize.cold.7
+ _AppleNVMePanicLogGetSize.cold.8
+ _AppleNVMePartialSanitizeGetProgress
+ _AppleNVMePartialSanitizeStart
+ _AppleNVMeReadPanicLogData.cold.1
+ _AppleNVMeReadPanicLogData.cold.10
+ _AppleNVMeReadPanicLogData.cold.11
+ _AppleNVMeReadPanicLogData.cold.12
+ _AppleNVMeReadPanicLogData.cold.13
+ _AppleNVMeReadPanicLogData.cold.2
+ _AppleNVMeReadPanicLogData.cold.3
+ _AppleNVMeReadPanicLogData.cold.4
+ _AppleNVMeReadPanicLogData.cold.5
+ _AppleNVMeReadPanicLogData.cold.6
+ _AppleNVMeReadPanicLogData.cold.7
+ _AppleNVMeReadPanicLogData.cold.8
+ _AppleNVMeReadPanicLogData.cold.9
+ _AppleNVMeSanitizeGetProgress
+ _AppleNVMeSanitizeStart
+ _AppleNVMeSanitizeSupportsPartialSanitize
+ _AppleNVMeSanitizeSupportsSanitize
+ _AppleNVMeSideBarGetErrorStringForStatus
+ _AppleNVMeSideBarGetRootDiskInfo
+ _AppleNVMeSideBarGetRootDiskInfo.cold.1
+ _AppleNVMeSideBarGetRootDiskInfo.cold.10
+ _AppleNVMeSideBarGetRootDiskInfo.cold.11
+ _AppleNVMeSideBarGetRootDiskInfo.cold.12
+ _AppleNVMeSideBarGetRootDiskInfo.cold.13
+ _AppleNVMeSideBarGetRootDiskInfo.cold.14
+ _AppleNVMeSideBarGetRootDiskInfo.cold.15
+ _AppleNVMeSideBarGetRootDiskInfo.cold.16
+ _AppleNVMeSideBarGetRootDiskInfo.cold.17
+ _AppleNVMeSideBarGetRootDiskInfo.cold.18
+ _AppleNVMeSideBarGetRootDiskInfo.cold.19
+ _AppleNVMeSideBarGetRootDiskInfo.cold.2
+ _AppleNVMeSideBarGetRootDiskInfo.cold.20
+ _AppleNVMeSideBarGetRootDiskInfo.cold.21
+ _AppleNVMeSideBarGetRootDiskInfo.cold.22
+ _AppleNVMeSideBarGetRootDiskInfo.cold.3
+ _AppleNVMeSideBarGetRootDiskInfo.cold.4
+ _AppleNVMeSideBarGetRootDiskInfo.cold.5
+ _AppleNVMeSideBarGetRootDiskInfo.cold.6
+ _AppleNVMeSideBarGetRootDiskInfo.cold.7
+ _AppleNVMeSideBarGetRootDiskInfo.cold.8
+ _AppleNVMeSideBarGetRootDiskInfo.cold.9
+ _AppleNVMeSideBarNamespaceClean
+ _AppleNVMeSideBarNamespaceClean.cold.1
+ _AppleNVMeSideBarNamespaceClean.cold.2
+ _AppleNVMeSideBarNamespaceClean.cold.3
+ _AppleNVMeSideBarNamespaceClean.cold.4
+ _AppleNVMeSideBarNamespaceRead
+ _AppleNVMeSideBarNamespaceReadWrite
+ _AppleNVMeSideBarNamespaceReadWrite.cold.1
+ _AppleNVMeSideBarNamespaceReadWrite.cold.2
+ _AppleNVMeSideBarNamespaceReadWrite.cold.3
+ _AppleNVMeSideBarNamespaceReadWrite.cold.4
+ _AppleNVMeSideBarNamespaceReadWrite.cold.5
+ _AppleNVMeSideBarNamespaceWrite
+ _CFArrayCreate
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFGetTypeID
+ _CFNumberGetTypeID
+ _CFNumberGetValue
+ _IOBSDNameMatching
+ _IOObjectConformsTo
+ _IOObjectGetClass
+ _IORegistryEntryCreateIterator
+ _IORegistryEntryGetParentEntry
+ _IORegistryEntryGetRegistryEntryID
+ _IORegistryEntryIDMatching
+ _IORegistryEntrySearchCFProperty
+ _IORegistryGetRootEntry
+ _IOServiceGetMatchingService
+ _NVMeEmbeddedNamespaceTypeNames
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _kCFTypeArrayCallBacks
+ _strlen
+ _strncmp
+ _strstr
- _sNVMeEmbeddedNamespaceTypeNames
CStrings:
+ "%s failed, NVMe device returned error 0x%x \n"
+ "%s: Warning - Using whole disk (%s) with base offset of 0\n"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/IONVMeFamily_user/AppleNVMeFramework/Source/AppleNVMePanicLogAccess.c"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/IONVMeFamily_user/AppleNVMeFramework/Source/AppleNVMeSideBarAccess.c"
+ "A bad argument was supplied to this API"
+ "APFS"
+ "An internal API error occurred"
+ "AppleAPFSVolume"
+ "AppleEmbeddedNVMeController"
+ "AppleNVMeSideBarGetRootDiskInfo"
+ "AppleNVMeSideBarNamespaceClean"
+ "AppleNVMeSideBarNamespaceRead"
+ "AppleNVMeSideBarNamespaceWrite"
+ "AssertMacros: %s, %s file: %s, line: %d, value: %lld\n"
+ "Base"
+ "CFGetTypeID ( propertyRef ) == CFBooleanGetTypeID ( )"
+ "CFGetTypeID ( propertyRef ) == CFNumberGetTypeID ( )"
+ "Could not find a corresponding APFS physical store for the disk"
+ "Could not find a namespace device for the SideBar namespace"
+ "Could not find the NVMe device for this disk"
+ "Could not find the disk service in the registry"
+ "Could not open a connection to the NVMe driver"
+ "EmbeddedDeviceTypeSideBar"
+ "IOMedia"
+ "IONVMeController"
+ "IOObjectConformsTo ( diskService, kIOMediaClass )"
+ "IOService"
+ "Preferred Block Size"
+ "Role"
+ "Sanitize Progress"
+ "Sanitize Support"
+ "Success"
+ "System"
+ "The controller return a unsuccessful NVMe status code"
+ "The read or write call to the driver failed"
+ "This disk is hosted by a non-Apple NVMe controller"
+ "Unknown error"
+ "Whole"
+ "blockCount > 0"
+ "blockSize > 0"
+ "connection != IO_OBJECT_NULL"
+ "currentObject != IO_OBJECT_NULL"
+ "currentObject != registryRoot"
+ "disk"
+ "diskService != IO_OBJECT_NULL"
+ "driverConnection != 0"
+ "inBlockCount > 0"
+ "inBufferSize > 0"
+ "inoutBuffer != NULL"
+ "kernResult == 0 "
+ "kernReturn == 0 "
+ "kern_status == kIOReturnSuccess"
+ "numberConvertedOK == true"
+ "nvmeDeviceService != IO_OBJECT_NULL"
+ "outBuffer != NULL"
+ "outBytesRead != NULL"
+ "propertyRef != NULL"
+ "service != IO_OBJECT_NULL"
+ "sideBarNamespaceTypeString != NULL"
+ "strlen ( inBSDName ) >= strlen ( \"diskX\" )"
+ "strncmp ( \"disk\", inBSDName, strlen ( \"disk\" ) ) == 0"

```
