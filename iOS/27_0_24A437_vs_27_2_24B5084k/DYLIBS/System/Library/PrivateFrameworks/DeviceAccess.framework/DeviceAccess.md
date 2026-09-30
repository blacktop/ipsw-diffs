## DeviceAccess

> `/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess`

```diff

-2700.34.0.0.0
-  __TEXT.__text: 0x531e0
-  __TEXT.__objc_methlist: 0x46e4
+2701.2.0.0.0
+  __TEXT.__text: 0x553dc
+  __TEXT.__objc_methlist: 0x48bc
   __TEXT.__const: 0x908
-  __TEXT.__cstring: 0xa223
-  __TEXT.__gcc_except_tab: 0x1330
+  __TEXT.__cstring: 0xa793
+  __TEXT.__gcc_except_tab: 0x1370
   __TEXT.__constg_swiftt: 0x3b8
   __TEXT.__swift5_typeref: 0x25a
   __TEXT.__swift5_builtin: 0x3c

   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_capture: 0x1c
-  __TEXT.__unwind_info: 0x1a20
+  __TEXT.__unwind_info: 0x1a80
   __TEXT.__eh_frame: 0x4d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xe80
-  __DATA_CONST.__objc_classlist: 0x1f0
+  __DATA_CONST.__const: 0xea8
+  __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fa8
+  __DATA_CONST.__objc_selrefs: 0x2078
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x188
-  __DATA_CONST.__objc_arraydata: 0x48
-  __DATA_CONST.__got: 0x538
-  __AUTH_CONST.__const: 0x6d0
-  __AUTH_CONST.__cfstring: 0x3680
-  __AUTH_CONST.__objc_const: 0x8070
+  __DATA_CONST.__objc_superrefs: 0x190
+  __DATA_CONST.__objc_arraydata: 0x68
+  __DATA_CONST.__got: 0x540
+  __AUTH_CONST.__const: 0x6f0
+  __AUTH_CONST.__cfstring: 0x3860
+  __AUTH_CONST.__objc_const: 0x8510
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0xc20
-  __AUTH.__objc_data: 0x98
+  __AUTH_CONST.__auth_got: 0xc28
+  __AUTH.__objc_data: 0x138
   __AUTH.__data: 0x90
-  __DATA.__objc_ivar: 0x71c
+  __DATA.__objc_ivar: 0x764
   __DATA.__data: 0xc08
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1298

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2302
-  Symbols:   3960
-  CStrings:  1519
+  Functions: 2358
+  Symbols:   4045
+  CStrings:  1566
 
Symbols:
+ +[DAExtension extensionPointForType:]
+ +[DASession migrateAppAccessFromBundleID:toBundleID:migratedCount:error:]
+ -[DADeviceAppAccessInfo inheritedAccessoryOptions]
+ -[DADeviceAppAccessInfo pendingMigrationTime]
+ -[DADeviceAppAccessInfo pendingMigrationToBundleID]
+ -[DADeviceAppAccessInfo setInheritedAccessoryOptions:]
+ -[DADeviceAppAccessInfo setPendingMigrationTime:]
+ -[DADeviceAppAccessInfo setPendingMigrationToBundleID:]
+ -[DADeviceAppAccessInfo setUnclaimedMigrationFromBundleID:]
+ -[DADeviceAppAccessInfo unclaimedMigrationFromBundleID]
+ -[DAEventExtension capabilityFlags]
+ -[DAEventExtension setCapabilityFlags:]
+ -[DAExtension extensionFlags]
+ -[DAExtension sandboxProfileName]
+ -[DAExtension sessionStarted]
+ -[DAExtensionCapabilityConfiguration extensionType]
+ -[DAExtensionCapabilityConfiguration setExtensionType:]
+ -[DAExtensionConfiguration alwaysRunningOverride]
+ -[DAExtensionConfiguration extensionFlags]
+ -[DAExtensionConfiguration extensionPoint]
+ -[DAExtensionConfiguration sandboxProfileName]
+ -[DAExtensionConfiguration setAlwaysRunningOverride:]
+ -[DAExtensionConfiguration setExtensionFlags:]
+ -[DAExtensionConfiguration setExtensionPoint:]
+ -[DAExtensionConfiguration setSandboxProfileName:]
+ -[DAExtensionPoint .cxx_destruct]
+ -[DAExtensionPoint capabilityFlags]
+ -[DAExtensionPoint descriptionWithLevel:]
+ -[DAExtensionPoint description]
+ -[DAExtensionPoint extensionPointCapabilities]
+ -[DAExtensionPoint initWithDictionary:]
+ -[DAExtensionPoint pointIdentifier]
+ -[DAExtensionPoint type]
+ -[DAExtensionPointCapability .cxx_destruct]
+ -[DAExtensionPointCapability capabilityFlags]
+ -[DAExtensionPointCapability descriptionWithLevel:]
+ -[DAExtensionPointCapability description]
+ -[DAExtensionPointCapability encrypt]
+ -[DAExtensionPointCapability sandboxProfileName]
+ -[DAExtensionPointCapability setCapabilityFlags:]
+ -[DAExtensionPointCapability setEncrypt:]
+ -[DAExtensionPointCapability setSandboxProfileName:]
+ GCC_except_table127
+ GCC_except_table131
+ GCC_except_table139
+ GCC_except_table23
+ GCC_except_table40
+ GCC_except_table44
+ GCC_except_table59
+ GCC_except_table60
+ GCC_except_table65
+ GCC_except_table69
+ GCC_except_table70
+ GCC_except_table80
+ GCC_except_table82
+ GCC_except_table84
+ GCC_except_table89
+ GCC_except_table91
+ GCC_except_table97
+ GCC_except_table98
+ _OBJC_CLASS_$_DAExtensionPoint
+ _OBJC_CLASS_$_DAExtensionPointCapability
+ _OBJC_CLASS_$_EXExtensionPointCatalog
+ _OBJC_IVAR_$_DADeviceAppAccessInfo._inheritedAccessoryOptions
+ _OBJC_IVAR_$_DADeviceAppAccessInfo._pendingMigrationTime
+ _OBJC_IVAR_$_DADeviceAppAccessInfo._pendingMigrationToBundleID
+ _OBJC_IVAR_$_DADeviceAppAccessInfo._unclaimedMigrationFromBundleID
+ _OBJC_IVAR_$_DAEventExtension._capabilityFlags
+ _OBJC_IVAR_$_DAExtension._sandboxProfileName
+ _OBJC_IVAR_$_DAExtension._sessionStarted
+ _OBJC_IVAR_$_DAExtensionCapabilityConfiguration._extensionType
+ _OBJC_IVAR_$_DAExtensionConfiguration._alwaysRunningOverride
+ _OBJC_IVAR_$_DAExtensionConfiguration._extensionFlags
+ _OBJC_IVAR_$_DAExtensionConfiguration._extensionPoint
+ _OBJC_IVAR_$_DAExtensionConfiguration._sandboxProfileName
+ _OBJC_IVAR_$_DAExtensionPoint._capabilityFlags
+ _OBJC_IVAR_$_DAExtensionPoint._extensionPointCapabilities
+ _OBJC_IVAR_$_DAExtensionPoint._pointIdentifier
+ _OBJC_IVAR_$_DAExtensionPoint._type
+ _OBJC_IVAR_$_DAExtensionPointCapability._capabilityFlags
+ _OBJC_IVAR_$_DAExtensionPointCapability._encrypt
+ _OBJC_IVAR_$_DAExtensionPointCapability._sandboxProfileName
+ _OBJC_METACLASS_$_DAExtensionPoint
+ _OBJC_METACLASS_$_DAExtensionPointCapability
+ __MergedGlobals
+ __OBJC_$_CLASS_METHODS_DAExtension
+ __OBJC_$_INSTANCE_METHODS_DAExtensionPoint
+ __OBJC_$_INSTANCE_METHODS_DAExtensionPointCapability
+ __OBJC_$_INSTANCE_VARIABLES_DAExtensionPoint
+ __OBJC_$_INSTANCE_VARIABLES_DAExtensionPointCapability
+ __OBJC_$_PROP_LIST_DAExtensionPoint
+ __OBJC_$_PROP_LIST_DAExtensionPointCapability
+ __OBJC_CLASS_RO_$_DAExtensionPoint
+ __OBJC_CLASS_RO_$_DAExtensionPointCapability
+ __OBJC_METACLASS_RO_$_DAExtensionPoint
+ __OBJC_METACLASS_RO_$_DAExtensionPointCapability
+ ___73+[DASession migrateAppAccessFromBundleID:toBundleID:migratedCount:error:]_block_invoke
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ _dyld_get_active_platform
+ _objc_msgSend$SDKDictionary
+ _objc_msgSend$alwaysRunningOverride
+ _objc_msgSend$destination
+ _objc_msgSend$extensionFlags
+ _objc_msgSend$extensionPointForIdentifier:platform:
+ _objc_msgSend$extensionType
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$pathExtension
+ _objc_msgSend$sandboxProfileName
+ _objc_msgSend$setEncrypt:
+ _objc_msgSend$setSandboxProfileName:
+ _objc_msgSend$unsignedLongLongValue
- -[DAExtension alwaysRunningOverride]
- -[DAExtension setAlwaysRunningOverride:]
- -[DAExtension setName:]
- -[DAExtension setPid:]
- -[DAExtension setType:]
- -[DAExtensionCapability setExtensionType:]
- GCC_except_table117
- GCC_except_table137
- GCC_except_table32
- GCC_except_table38
- GCC_except_table42
- GCC_except_table45
- GCC_except_table51
- GCC_except_table54
- GCC_except_table55
- GCC_except_table58
- GCC_except_table63
- GCC_except_table67
- GCC_except_table72
- GCC_except_table76
- GCC_except_table81
- GCC_except_table86
- GCC_except_table87
- GCC_except_table90
- _OBJC_IVAR_$_DAEventExtension._capabilityFlag
- _objc_msgSend$setCapabilityFlag:
CStrings:
+ "### Empty extension point declaration for '%@'"
+ "### Empty extension point definition"
+ "### Event for capability %@ not hosted by this extension: %@"
+ "### Failed to parse extension point declaration for '%@'"
+ "### Module not supported for capability '%@', skipping"
+ "### No EXSandboxProfileName for capability '%@', skipping"
+ "### No capability for %@ in this extension: %@"
+ "### No extension point declaration for '%@'"
+ "### No point identifier in extension point definition: %@"
+ "### ReportEventToExtension failed with nil xpc connection"
+ "### Unsupported capability '%@', skipping"
+ "%@ <%p>"
+ "+[DAExtension extensionPointForType:]"
+ "+[DASession migrateAppAccessFromBundleID:toBundleID:migratedCount:error:]"
+ "-[DAExtensionPoint initWithDictionary:]"
+ "AccessoryLiveActivities"
+ "AccessoryNotifications"
+ "AssertWithExpiration for %@: %@"
+ "AudioAccessoryKit"
+ "Capability %@ enrolled, starting: %@"
+ "Capability %@ un-enrolled, stopping: %@"
+ "DAEncryptionRequired"
+ "DASession-MigrateAppAccess"
+ "EXSandboxProfileName"
+ "Encrypt %s"
+ "MgAA"
+ "MigrateAppAccess %@ -> %@ complete, %llu device(s)"
+ "MigrateAppAccess %@ -> %@ start"
+ "NSExtension"
+ "NSExtensionPointIdentifier"
+ "No destination bundle ID"
+ "No source bundle ID"
+ "Parsed extension point '%@': CapFl %@, Profiles %lu"
+ "PtID '%@'"
+ "Read extension point declaration '%@' from %@"
+ "SndBx '%@'"
+ "inhOp"
+ "inheritedAccessoryOptions"
+ "inheritedOptions %@"
+ "mgCnt"
+ "mgDst"
+ "mgSrc"
+ "mgUnc"
+ "pendingMigrationTime"
+ "pendingMigrationTo %@ (since %@)"
+ "pendingMigrationToBundleID"
+ "pmT"
+ "pmTo"
+ "unclaimedMigrationFrom %@"
+ "unclaimedMigrationFromBundleID"
- "AssertWithExpiration for %@, '%@': %@"
- "Capability %@"
- "Skipping capability with missing service info for %@: %@"
```
