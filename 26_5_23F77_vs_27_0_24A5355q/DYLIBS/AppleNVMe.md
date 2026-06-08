## AppleNVMe

> `/System/Library/PrivateFrameworks/AppleNVMe.framework/AppleNVMe`

```diff

-819.120.3.0.0
-  __TEXT.__text: 0x9dc
-  __TEXT.__auth_stubs: 0x180
+876.0.0.0.0
+  __TEXT.__text: 0x22d0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x3a6
-  __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__got: 0x40
-  __AUTH_CONST.__auth_got: 0xc0
-  __AUTH_CONST.__cfstring: 0x60
-  __DATA.__data: 0x80
+  __TEXT.__cstring: 0xbaa
+  __TEXT.__unwind_info: 0xc8
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0xd8
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__cfstring: 0x140
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__data: 0x8
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
