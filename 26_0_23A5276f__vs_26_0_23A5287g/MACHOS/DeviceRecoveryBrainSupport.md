## DeviceRecoveryBrainSupport

> `/System/Library/PrivateFrameworks/DeviceRecoveryBrainSupport.framework/DeviceRecoveryBrainSupport`

```diff

-82.0.0.502.1
-  __TEXT.__text: 0x181f0
-  __TEXT.__auth_stubs: 0xab0
-  __TEXT.__objc_methlist: 0x9b4
+85.0.0.0.9
+  __TEXT.__text: 0x19590
+  __TEXT.__auth_stubs: 0xad0
+  __TEXT.__objc_methlist: 0x9ec
   __TEXT.__const: 0x150
   __TEXT.__gcc_except_tab: 0x49c
-  __TEXT.__cstring: 0x3301
-  __TEXT.__oslogstring: 0x2556
-  __TEXT.__unwind_info: 0x3f8
+  __TEXT.__cstring: 0x361f
+  __TEXT.__oslogstring: 0x2786
+  __TEXT.__unwind_info: 0x448
   __TEXT.__eh_frame: 0xa0
-  __TEXT.__objc_classname: 0x118
-  __TEXT.__objc_methname: 0x1994
+  __TEXT.__objc_classname: 0x12d
+  __TEXT.__objc_methname: 0x1a27
   __TEXT.__objc_methtype: 0x38f
-  __TEXT.__objc_stubs: 0x1700
-  __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0x870
+  __TEXT.__objc_stubs: 0x17a0
+  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__const: 0x880
   __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x828
+  __DATA_CONST.__objc_selrefs: 0x850
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0x568
+  __AUTH_CONST.__auth_got: 0x578
   __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0x20e0
-  __AUTH_CONST.__objc_const: 0x9e0
+  __AUTH_CONST.__cfstring: 0x21c0
+  __AUTH_CONST.__objc_const: 0xa20
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x48
-  __DATA.__data: 0x244
+  __DATA.__data: 0x23c
   __DATA.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FEA08C11-B55D-3BCB-AC07-677109EFA211
-  Functions: 377
-  Symbols:   1053
-  CStrings:  1254
+  UUID: 4BB4828B-C131-395C-A203-4113600C7E3C
+  Functions: 409
+  Symbols:   1101
+  CStrings:  1295
 
Symbols:
+ -[DeviceRecoveryBrain client:hasBooleanEntitlement:]
+ -[DeviceRecoveryBrain client:hasBooleanEntitlement:].cold.1
+ -[DeviceRecoveryBrain client:hasBooleanEntitlement:].cold.2
+ -[DeviceRecoveryBrain client:hasBooleanEntitlement:].cold.3
+ -[DeviceRecoveryBrain client:hasBooleanEntitlement:].cold.4
+ -[DeviceRecoveryBrain client:hasBooleanEntitlement:].cold.5
+ -[DeviceRecoveryBrain client:hasBooleanEntitlement:].cold.6
+ -[DeviceRecoveryBrain clientHasRecoveryBrainControllerEntitlement:]
+ -[DeviceRecoveryBrain init]
+ -[DeviceRecoveryBrain init].cold.1
+ -[DeviceRecoveryBrain listener:shouldAcceptNewConnection:].cold.4
+ -[DeviceRecoveryBrain recoverDevice:].cold.7
+ -[DeviceRecoveryBrain recoverDevice:].cold.8
+ -[DeviceRecoveryBrain recoverDevice:].cold.9
+ -[DeviceRecoveryBrain scanForIssues:].cold.3
+ -[NSFileManager(DeviceRecoveryExtras) fileAtPathIsSymlink:]
+ -[NSFileManager(DeviceRecoveryExtras) fileAtPathIsSymlink:].cold.1
+ -[NSFileManager(DeviceRecoveryExtras) fileAtPathIsSymlink:].cold.2
+ -[NSFileManager(DeviceRecoveryExtras) fileAtPathIsSymlink:].cold.3
+ GCC_except_table14
+ GCC_except_table22
+ _DeviceRecoveryErrorAttributePasscodeBackOffEndDate
+ _ERMContentsPresent.cold.1
+ _ERMContentsPresent.cold.2
+ _NSFileType
+ _NSFileTypeSymbolicLink
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ __37-[DeviceRecoveryBrain recoverDevice:]_block_invoke.190
+ __37-[DeviceRecoveryBrain scanForIssues:]_block_invoke.118
+ __40-[DeviceRecoveryBrain reclaimFreeSpace:]_block_invoke.125
+ __58-[DeviceRecoveryBrain listener:shouldAcceptNewConnection:]_block_invoke.48
+ __ERMContentsPresent
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSFileManager_$_DeviceRecoveryExtras
+ __OBJC_$_CATEGORY_NSFileManager_$_DeviceRecoveryExtras
+ __ProcessNameForPid
+ _kDeviceRecoveryStaticStringKey
+ _objc_msgSend$client:hasBooleanEntitlement:
+ _objc_msgSend$clientHasRecoveryBrainControllerEntitlement:
+ _objc_msgSend$fileAtPathIsSymlink:
+ _objc_msgSend$fileExistsAtPath:isDirectory:
+ _objc_msgSend$valueForEntitlement:
+ _objc_retain_x24
+ _os_variant_allows_internal_security_policies
- -[DeviceRecoveryBrain configureBrain:completion:].cold.14
- -[DeviceRecoveryBrain configureBrain:completion:].cold.15
- GCC_except_table10
- GCC_except_table17
- _DRBrainAttributeIsInternalBuild
- __37-[DeviceRecoveryBrain recoverDevice:]_block_invoke.163
- __37-[DeviceRecoveryBrain scanForIssues:]_block_invoke.103
- __40-[DeviceRecoveryBrain reclaimFreeSpace:]_block_invoke.110
- __58-[DeviceRecoveryBrain listener:shouldAcceptNewConnection:]_block_invoke.35
CStrings:
+ "%{public}s: %{public}s: AssertMacros: %{public}s - Failed to get file attributes: %{public}@ - %{public}@, %{public}s file: %{public}s, line: %{public}d\n"
+ "%{public}s: %{public}s: AssertMacros: %{public}s, %{public}s file: %{public}s, line: %{public}d\n"
+ "%{public}s: ERM artifacts path %{public}@ exists but is not a directory"
+ "%{public}s: ERM data path %{public}@ exists but is not a directory"
+ "%{public}s: Found ERM content to remove"
+ "%{public}s: Test file '%{public}@' is a symlink - skipping"
+ "%{public}s: client '%{public}@' is missing entitlement: '%{public}@'"
+ "%{public}s: entitlement '%{public}@' on client '%{public}@' is not an NSNumber: %{public}@"
+ "-[DeviceRecoveryBrain client:hasBooleanEntitlement:]"
+ "-[DeviceRecoveryBrain init]"
+ "-[NSFileManager(DeviceRecoveryExtras) fileAtPathIsSymlink:]"
+ "/private/preboot/supplemental/"
+ "/private/var/erm"
+ "Denying client connection - client does not have 'com.apple.DeviceRecovery.BrainController' entitlement"
+ "DeviceRecoveryExtras"
+ "Found Extended Research content to remove"
+ "PasscodeBackOffEndDate"
+ "StaticString"
+ "[recoveryControlEntitlement isKindOfClass:[NSNumber class]]"
+ "[self clientHasRecoveryBrainControllerEntitlement:newConnection]"
+ "_ERMContentsPresent"
+ "attributes != nil"
+ "client:hasBooleanEntitlement:"
+ "clientConnection != nil"
+ "clientHasRecoveryBrainControllerEntitlement:"
+ "com.apple.private.DeviceRecovery.BrainController"
+ "entitlementName != nil"
+ "failed to remove Extended Research artifacts"
+ "failed to remove Extended Research data"
+ "fileAtPathIsSymlink:"
+ "fileExistsAtPath:isDirectory:"
+ "fileType != nil"
+ "recoveryControlEntitlement != nil"
+ "recoveryControlEntitlement.boolValue"
+ "self != nil"
+ "valueForEntitlement:"
- "%{public}s: %{public}s: AssertMacros: %{public}s, %{public}s file: %{public}s, line: %d\n"
- "IsInternalBuild"

```
