## DMCApps

> `/System/Library/PrivateFrameworks/DMCApps.framework/DMCApps`

```diff

-3.26.2.3.0
-  __TEXT.__text: 0x64e0
-  __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__const: 0x338
-  __TEXT.__cstring: 0x1d1
-  __TEXT.__constg_swiftt: 0x2f0
-  __TEXT.__swift5_typeref: 0x1e6
-  __TEXT.__swift5_reflstr: 0x1d4
-  __TEXT.__swift5_fieldmd: 0x23c
-  __TEXT.__swift5_proto: 0x24
-  __TEXT.__swift5_types: 0x28
-  __TEXT.__swift5_protos: 0x1c
+3.26.3.6.0
+  __TEXT.__text: 0x9f8c
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__const: 0x49a
+  __TEXT.__cstring: 0x49c
+  __TEXT.__swift5_typeref: 0x268
+  __TEXT.__constg_swiftt: 0x390
+  __TEXT.__swift5_reflstr: 0x267
+  __TEXT.__swift5_fieldmd: 0x2b8
+  __TEXT.__swift5_proto: 0x3c
+  __TEXT.__swift5_types: 0x30
+  __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x27c
-  __TEXT.__eh_frame: 0x3f8
-  __TEXT.__objc_methname: 0x1c6
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0xb0
+  __TEXT.__unwind_info: 0x3d8
+  __TEXT.__eh_frame: 0x8e0
+  __TEXT.__objc_methname: 0x29e
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc0
-  __AUTH_CONST.__const: 0x598
-  __AUTH_CONST.__auth_got: 0x250
+  __DATA_CONST.__objc_selrefs: 0x118
+  __AUTH_CONST.__const: 0x778
+  __AUTH_CONST.__auth_ptr: 0x8
+  __AUTH_CONST.__auth_got: 0x300
   __AUTH.__data: 0x120
-  __DATA.__objc_classrefs: 0x40
-  __DATA.__data: 0x1a8
-  __DATA.__bss: 0x180
+  __DATA.__objc_classrefs: 0x78
+  __DATA.__data: 0x218
+  __DATA.__bss: 0x380
   __DATA.__common: 0x18
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/DEPClientLibrary.framework/DEPClientLibrary
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement
   - /System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 264
-  Symbols:   148
-  CStrings:  34
+  Functions: 347
+  Symbols:   191
+  CStrings:  57
 
Symbols:
+ _MDMFilePath
+ _OBJC_CLASS_$_DMFSetAppAssociatedDomainsEnableDirectDownloadsRequest
+ _OBJC_CLASS_$_DMFSetAppAssociatedDomainsRequest
+ _OBJC_CLASS_$_DMFSetAppExtensionUUIDsRequest
+ _OBJC_CLASS_$_DMFSetAppTapToPayScreenLockRequest
+ _OBJC_CLASS_$_MCProfileConnection
+ _OBJC_CLASS_$_MDMCloudConfiguration
+ _OBJC_CLASS_$_NSInputStream
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ ___chkstk_darwin
+ ___swift_destroy_boxed_opaque_existential_4Tm
+ ___swift_memcpy16_8
+ ___swift_memcpy17_8
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swift_stdlib_malloc_size
+ _associated conformance 7DMCApps10PlistErrorOSHAASQ
+ _block_descriptor.30
+ _block_descriptor.32
+ _block_descriptor.40
+ _block_descriptor.41
+ _block_descriptor.43
+ _kCCOrganizationNameKey
+ _kMDMManagedAppAttributeRelayUUID
+ _kMDMManagedAppAttributeTapToPayScreenLock
+ _kMDMRequiredAppIDForMDMKey
+ _malloc_size
+ _memmove
+ _objc_release_x8
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain_n
+ _swift_getObjectType
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRelease_n
+ _swift_unknownObjectRetain
+ _swift_unknownObjectRetain_n
+ _symbolic $s7DMCApps21DMCAppStateReporting3P
+ _symbolic $s7DMCApps21DMCAppStateReporting4P
+ _symbolic SDySSyXlG
+ _symbolic _____ 7DMCApps0A13InternalErrorO
+ _symbolic _____ 7DMCApps10PlistErrorO
+ _symbolic _____ySSyXlG s18_DictionaryStorageC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
- _OBJC_CLASS_$_DMFMDMv1UpdateAppRequest
- ___swift_memcpy9_8
- _block_descriptor.18
- _block_descriptor.20
- _block_descriptor.21
- _block_descriptor.23
- _objc_release_x28
CStrings:
+ "Could not look up distinguished app ID because of a bad URL."
+ "Could not look up distinguished app ID because of an unexpected error."
+ "Could not look up distinguished app ID because the RequiredAppIDForMDM key was not a number."
+ "Could not look up distinguished app ID because the plist could not be parsed."
+ "DMFSetAppAssociatedDomainsEnableDirectDownloadsRequest"
+ "DMFSetAppAssociatedDomainsRequest"
+ "DMFSetAppExtensionUUIDsRequest"
+ "DMFSetAppTapToPayScreenLockRequest"
+ "Declarative Device Management"
+ "Failed to set UUID app attributes on app %s, error: %@"
+ "Failed to set app attribute %s on app %s, error: %@"
+ "Unable to create DMFMDMv1StartManagingAppRequest for %s"
+ "close"
+ "initWithURL:"
+ "isSupervised"
+ "managingOrganizationInformation"
+ "open"
+ "propertyListWithStream:options:format:error:"
+ "setRelayUUIDString:"
+ "setTapToPayScreenLock:"
+ "sharedConfiguration"
+ "sharedConnection"
+ "some UUID attribute"
+ "unsignedLongLongValue"
- "Failed to perform update app request with error: %@"

```
