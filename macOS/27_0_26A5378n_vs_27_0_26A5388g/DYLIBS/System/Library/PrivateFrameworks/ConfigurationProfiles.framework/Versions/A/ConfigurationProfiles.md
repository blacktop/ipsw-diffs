## ConfigurationProfiles

> `/System/Library/PrivateFrameworks/ConfigurationProfiles.framework/Versions/A/ConfigurationProfiles`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__objc_intobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1839.0.0.0.0
-  __TEXT.__text: 0x6584c
-  __TEXT.__objc_methlist: 0x1494
-  __TEXT.__const: 0x3e1
-  __TEXT.__gcc_except_tab: 0x8d4
-  __TEXT.__oslogstring: 0x1026c
-  __TEXT.__cstring: 0x176cb
-  __TEXT.__unwind_info: 0x12f0
+1841.0.0.0.0
+  __TEXT.__text: 0x66294
+  __TEXT.__objc_methlist: 0x14fc
+  __TEXT.__const: 0x3f1
+  __TEXT.__gcc_except_tab: 0x8fc
+  __TEXT.__oslogstring: 0x10363
+  __TEXT.__cstring: 0x17812
+  __TEXT.__unwind_info: 0x1320
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x138
-  __DATA_CONST.__objc_classlist: 0x80
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1408
+  __DATA_CONST.__objc_selrefs: 0x1438
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x70
-  __DATA_CONST.__objc_arraydata: 0x3b0
-  __DATA_CONST.__got: 0x480
-  __AUTH_CONST.__const: 0x6a0
-  __AUTH_CONST.__cfstring: 0x6c20
-  __AUTH_CONST.__objc_const: 0x20d0
-  __AUTH_CONST.__objc_arrayobj: 0x168
-  __AUTH_CONST.__objc_dictobj: 0x118
+  __DATA_CONST.__objc_superrefs: 0x80
+  __DATA_CONST.__objc_arraydata: 0x3d0
+  __DATA_CONST.__got: 0x488
+  __AUTH_CONST.__const: 0x6f0
+  __AUTH_CONST.__cfstring: 0x6c80
+  __AUTH_CONST.__objc_const: 0x2260
+  __AUTH_CONST.__objc_arrayobj: 0x180
+  __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH_CONST.__auth_got: 0xbc0
-  __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0xc4
+  __AUTH_CONST.__auth_got: 0xbd8
+  __AUTH.__objc_data: 0x410
+  __DATA.__objc_ivar: 0xd0
   __DATA.__data: 0x63a
   __DATA.__common: 0x54c
-  __DATA.__bss: 0x198
+  __DATA.__bss: 0x1a8
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__data: 0xc
   __DATA_DIRTY.__bss: 0x60

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2045
-  Symbols:   2894
-  CStrings:  2394
+  Functions: 2063
+  Symbols:   2941
+  CStrings:  2403
 
Symbols:
+ +[MCXManagedDomainPublishWaiter waiterForDomains:]
+ -[MCXManagedDomainPublishWaiter cancel]
+ -[MCXManagedDomainPublishWaiter dealloc]
+ -[MCXManagedDomainPublishWaiter waitUpTo:]
+ -[_MCXSemBox dealloc]
+ -[_MCXSemBox init]
+ GCC_except_table29
+ GCC_except_table31
+ GCC_except_table8
+ MCXSignpostLog
+ MCXSignpostLog.onceToken
+ MCXSignpostLog.signpostLog
+ OBJC_IVAR_$_MCXManagedDomainPublishWaiter._observer
+ OBJC_IVAR_$_MCXManagedDomainPublishWaiter._semBox
+ OBJC_IVAR_$__MCXSemBox.sem
+ _CP_MDMUserPushToken
+ _CP_RemoteManagementTransferProfileAccount
+ _DockRelevantManagedDomains
+ _MCXSignpostLog
+ _OBJC_CLASS_$_MCXManagedDomainPublishWaiter
+ _OBJC_CLASS_$_NSAssertionHandler
+ _OBJC_CLASS_$__MCXSemBox
+ _OBJC_METACLASS_$_MCXManagedDomainPublishWaiter
+ _OBJC_METACLASS_$__MCXSemBox
+ __50+[MCXManagedDomainPublishWaiter waiterForDomains:]_block_invoke
+ __OBJC_$_CLASS_METHODS_MCXManagedDomainPublishWaiter
+ __OBJC_$_INSTANCE_METHODS_MCXManagedDomainPublishWaiter
+ __OBJC_$_INSTANCE_METHODS__MCXSemBox
+ __OBJC_$_INSTANCE_VARIABLES_MCXManagedDomainPublishWaiter
+ __OBJC_$_INSTANCE_VARIABLES__MCXSemBox
+ __OBJC_CLASS_RO_$_MCXManagedDomainPublishWaiter
+ __OBJC_CLASS_RO_$__MCXSemBox
+ __OBJC_METACLASS_RO_$_MCXManagedDomainPublishWaiter
+ __OBJC_METACLASS_RO_$__MCXSemBox
+ ___50+[MCXManagedDomainPublishWaiter waiterForDomains:]_block_invoke
+ ___MCXSignpostLog_block_invoke
+ ___block_descriptor_48_e8_32o40o_e24_v16?0"NSNotification"8l
+ ___copy_helper_block_e8_32o40o
+ ___destroy_helper_block_e8_32o40o
+ __os_signpost_emit_with_name_impl
+ _objc_msgSend$cancel
+ _objc_msgSend$currentHandler
+ _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
+ _objc_msgSend$remoteManagementTransferProfileAccount:newManagingOwnerIdentifier:error:
+ _objc_msgSend$waitUpTo:
+ _objc_msgSend$waiterForDomains:
+ _os_signpost_enabled
+ _os_signpost_id_generate
- GCC_except_table9
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
+ "01:25:57"
+ "CPProfileManager.m"
+ "Jul 11 2026"
+ "MCXManagedDomainPublishWaiter"
+ "MCXManagedDomainPublishWaiter -waitUpTo: must not be called on the main thread"
+ "MCXManagedDomainPublishWaiter matched domain - %s"
+ "MDMUserPushToken"
+ "PointsOfInterest"
+ "RestartDock: TIMED OUT waiting for managed Dock prefs publish; restarting anyway"
+ "RestartDock: waiting for cfprefsd to publish managed Dock prefs"
+ "published=%{public}d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "01:12:27"
- "Jun 27 2026"
```
