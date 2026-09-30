## RemoteManagement

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/Versions/A/RemoteManagement`

```diff

-  __TEXT.__text: 0x4ff5c
-  __TEXT.__objc_methlist: 0x1bd0
-  __TEXT.__const: 0x1890
-  __TEXT.__cstring: 0x23d1
-  __TEXT.__oslogstring: 0x4a2b
+  __TEXT.__text: 0x52a0c
+  __TEXT.__objc_methlist: 0x1c28
+  __TEXT.__const: 0x1a70
+  __TEXT.__cstring: 0x2521
+  __TEXT.__oslogstring: 0x4aeb
   __TEXT.__gcc_except_tab: 0x3e0
-  __TEXT.__swift5_typeref: 0x66e
-  __TEXT.__constg_swiftt: 0x970
-  __TEXT.__swift5_reflstr: 0x343
-  __TEXT.__swift5_fieldmd: 0x4a0
-  __TEXT.__swift5_proto: 0x114
-  __TEXT.__swift5_types: 0x74
+  __TEXT.__swift5_typeref: 0x6ae
+  __TEXT.__constg_swiftt: 0x9dc
+  __TEXT.__swift5_reflstr: 0x373
+  __TEXT.__swift5_fieldmd: 0x4e4
+  __TEXT.__swift5_proto: 0x124
+  __TEXT.__swift5_types: 0x7c
   __TEXT.__swift5_capture: 0x17c
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xf70
-  __TEXT.__eh_frame: 0x15a4
+  __TEXT.__unwind_info: 0xfd0
+  __TEXT.__eh_frame: 0x1658
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x280
-  __DATA_CONST.__objc_classlist: 0x160
+  __DATA_CONST.__const: 0x2a8
+  __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13b8
+  __DATA_CONST.__objc_selrefs: 0x13d8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__got: 0x590
-  __AUTH_CONST.__const: 0x10b0
-  __AUTH_CONST.__cfstring: 0x1b00
-  __AUTH_CONST.__objc_const: 0x2ea8
+  __DATA_CONST.__got: 0x5f8
+  __AUTH_CONST.__const: 0x1120
+  __AUTH_CONST.__cfstring: 0x1b40
+  __AUTH_CONST.__objc_const: 0x2f50
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0xa60
-  __AUTH.__objc_data: 0x568
-  __AUTH.__data: 0x828
+  __AUTH_CONST.__auth_got: 0xb60
+  __AUTH.__objc_data: 0x898
+  __AUTH.__data: 0xae0
   __DATA.__objc_ivar: 0xc8
-  __DATA.__data: 0x700
-  __DATA.__bss: 0x23d0
-  __DATA.__common: 0x30
-  __DATA_DIRTY.__objc_data: 0x670
-  __DATA_DIRTY.__data: 0x298
+  __DATA.__data: 0x768
+  __DATA.__bss: 0x25d0
+  __DATA.__common: 0x38
+  __DATA_DIRTY.__objc_data: 0x410
+  __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData

   - /System/Library/PrivateFrameworks/RemoteManagementModel.framework/Versions/A/RemoteManagementModel
   - /System/Library/PrivateFrameworks/RemoteManagementProtocol.framework/Versions/A/RemoteManagementProtocol
   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/Versions/A/RemoteServiceDiscovery
+  - /System/Library/PrivateFrameworks/StorageContainersPrivate.framework/Versions/A/StorageContainersPrivate
   - /System/Library/PrivateFrameworks/UserManagement.framework/Versions/A/UserManagement
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftSystem.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1424
-  Symbols:   2261
-  CStrings:  920
+  Functions: 1468
+  Symbols:   2287
+  CStrings:  934
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__objc_intobj : content changed
Symbols:
+ +[RMErrorUtilities createMissingStatusValueErrorWithKeyPath:]
+ +[RMLocations oldBaseDirectoryURLInUserDomain]
+ _OBJC_CLASS_$_RMProtectedContainer
+ _OBJC_METACLASS_$_RMProtectedContainer
+ _RMSwitchToDaemonUserIfNeeded
+ _RMSwitchToMobileUserIfNeeded
+ __CLASS_METHODS_RMProtectedContainer
+ __DATA_RMProtectedContainer
+ __INSTANCE_METHODS_RMProtectedContainer
+ __IVARS_RMProtectedContainer
+ __METACLASS_DATA_RMProtectedContainer
+ __PROPERTIES_RMProtectedContainer
+ ___block_descriptor_40_e5_v8?0l
+ ___swift_memcpy16_8
+ _associated conformance 16RemoteManagement25RMProtectedContainerErrorO10Foundation09LocalizedE0AAs0E0
+ _associated conformance 16RemoteManagement25RMProtectedContainerErrorO10Foundation13CustomNSErrorAAs0E0
+ _getegid
+ _geteuid
+ _getpwnam
+ _objc_msgSend$accessWithIdentifier:error:
+ _objc_msgSend$createAndReturnError:
+ _objc_msgSend$url
+ _rootDirectoryURLInDomain:error:.protectedContainer
+ _setuid
+ _swift_getSingletonMetadata
+ _swift_updateClassMetadata2
+ _symbolic _____ 10Foundation3URLV
+ _symbolic _____ 16RemoteManagement20RMProtectedContainerC
+ _symbolic _____ 16RemoteManagement25RMProtectedContainerErrorO
+ _symbolic _____Sg 6System8FilePathV
+ _symbolic ______p 24StorageContainersPrivate9ContainerC12ScopesAccessP
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 0C17ContainersPrivate5QueryC7OptionsO
+ _type_layout_string 16RemoteManagement25RMProtectedContainerErrorO
- +[RMLocations _applicationSupportChildDirectoryURLInDomain:createIfNeeded:childName:descriptor:]
- ___96+[RMLocations _applicationSupportChildDirectoryURLInDomain:createIfNeeded:childName:descriptor:]_block_invoke
- _applicationSupportChildDirectoryURLInDomain:createIfNeeded:childName:descriptor:.onceToken
CStrings:
+ "Accessing protected system container for %{public}s at: %{public}s"
+ "Darwin User directory is %{public}@"
+ "Error.MissingStatusValue_%@"
+ "Failed to access protected system container: "
+ "Failed to find Data Vault directory"
+ "Failed to get protected container path"
+ "Failed to get protected container path for identifier: "
+ "Failed to initialize Protected Container: %{public}@"
+ "Library/Application Support"
+ "No protected system container found for identifier: "
+ "Protected Container not found: %{public}@"
+ "Protected system container at: %{public}s"
+ "RemoteManagement.RMProtectedContainer"
+ "_rmd"
- "Failed to find Application Support directory: %{public}@"
- "Failed to find Data Vault directory: %{public}@"

```
