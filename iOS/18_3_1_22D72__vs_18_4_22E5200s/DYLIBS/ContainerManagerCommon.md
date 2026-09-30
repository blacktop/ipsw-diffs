## ContainerManagerCommon

> `/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon`

```diff

-689.0.0.0.0
-  __TEXT.__text: 0xd225c
-  __TEXT.__auth_stubs: 0x1a60
-  __TEXT.__objc_methlist: 0x758c
-  __TEXT.__const: 0x310
-  __TEXT.__oslogstring: 0xddab
-  __TEXT.__cstring: 0x8163
-  __TEXT.__gcc_except_tab: 0x2ab8
-  __TEXT.__ustring: 0x16c
+689.100.4.0.0
+  __TEXT.__text: 0xd3da8
+  __TEXT.__auth_stubs: 0x1aa0
+  __TEXT.__objc_methlist: 0x9634
+  __TEXT.__const: 0x320
+  __TEXT.__cstring: 0x81a6
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0x1e18
-  __TEXT.__objc_classname: 0x1b2b
-  __TEXT.__objc_methname: 0x12280
-  __TEXT.__objc_methtype: 0x3b5b
-  __TEXT.__objc_stubs: 0xb260
-  __DATA_CONST.__got: 0x250
+  __TEXT.__oslogstring: 0xddd5
+  __TEXT.__gcc_except_tab: 0x2b14
+  __TEXT.__ustring: 0x16c
+  __TEXT.__unwind_info: 0x1e48
+  __TEXT.__objc_classname: 0x1b70
+  __TEXT.__objc_methname: 0x12493
+  __TEXT.__objc_methtype: 0x3b8b
+  __TEXT.__objc_stubs: 0xb3a0
+  __DATA_CONST.__got: 0x258
   __DATA_CONST.__const: 0x19a8
-  __DATA_CONST.__objc_classlist: 0x560
+  __DATA_CONST.__objc_classlist: 0x570
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x370
+  __DATA_CONST.__objc_protolist: 0x378
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3148
+  __DATA_CONST.__objc_selrefs: 0x3208
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x4c0
+  __DATA_CONST.__objc_superrefs: 0x4d0
   __DATA_CONST.__objc_arraydata: 0x290
-  __AUTH_CONST.__auth_got: 0xd40
+  __AUTH_CONST.__auth_got: 0xd60
   __AUTH_CONST.__const: 0x688
   __AUTH_CONST.__cfstring: 0x41e0
-  __AUTH_CONST.__objc_const: 0x167e0
+  __AUTH_CONST.__objc_const: 0x13d70
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_intobj: 0x1428
   __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_ivar: 0xaa0
-  __DATA.__data: 0x2a70
+  __AUTH.__objc_data: 0x730
+  __DATA.__objc_ivar: 0xb4c
+  __DATA.__data: 0x2ad0
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0xe8
-  __DATA_DIRTY.__objc_data: 0x2ee0
+  __DATA.__bss: 0xf8
+  __DATA_DIRTY.__objc_data: 0x2f30
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x370
+  __DATA_DIRTY.__bss: 0x360
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2860
-  Symbols:   3371
-  CStrings:  5197
+  Functions: 2912
+  Symbols:   3433
+  CStrings:  5228
 
Symbols:
+ _container_get_creator_codesign_identifier
+ _container_get_info
+ _container_get_path
+ _container_get_user_managed_assets_relative_path
+ _container_pwd_for_name
+ _container_pwd_for_uid
+ _gCMPWDSeam
- _getpwnam_r
- _getpwuid_r
CStrings:
+ "04:21:08"
+ "@24@0:8@\"NSSet\"16"
+ "@28@0:8@\"NSDictionary\"16B24"
+ "@40@0:8{container_pwd_s=II**}16"
+ "B40@?0{container_pwd_s=II**}8^^{container_error_extended_s}32"
+ "Feb 16 2025"
+ "MCMCommandUpdateInfo"
+ "MCMParametersUpdateInfo"
+ "MCMXPCMessageUpdateInfo"
+ "MobileContainerManager-689.100.4~604"
+ "No container with identity: %@"
+ "T@\"NSDictionary\",R,N,V_infoDict"
+ "T@\"NSSet\",R,N,V_deleteKeys"
+ "TB,R,D,N"
+ "TB,R,N,V_fullReplace"
+ "TB,R,N,V_includedCreator"
+ "TB,R,N,V_includedInfo"
+ "TB,R,N,V_includedPath"
+ "TB,R,N,V_includedUserManagedAssetsPath"
+ "Unable to get user (%{public}d/[%@]/%{public}d); error = %{public}s"
+ "_deleteKeys"
+ "_fullReplace"
+ "_includedCreator"
+ "_includedInfo"
+ "_includedPath"
+ "_includedUserManagedAssetsPath"
+ "_infoDict"
+ "_modifiedDictBySetttingValue:forKey:onInfo:"
+ "_posixUserWithPWD:"
+ "assertion failure: \"notificationPort != ((void*)0)\" -> %llu"
+ "deleteKeys"
+ "fullReplace"
+ "includedCreator"
+ "includedInfo"
+ "includedPath"
+ "includedUserManagedAssetsPath"
+ "infoDict"
+ "metadataByDeletingInfoDictKeys:"
+ "metadataBySettingValuesWithInfoDict:fullReplace:"
- "03:25:40"
- "@24@0:8^{passwd=**IIq****q}16"
- "Could not get _SC_GETPW_R_SIZE_MAX sysconf."
- "Jan 16 2025"
- "MobileContainerManager-689~7567"
- "NULL passwd"
- "_posixUserWithPasswdPtr:"
- "assertion failure: \"notificationPort != ((void *)0)\" -> %lld"

```
