## com.apple.CallKit.CallDirectoryMaintenance

> `/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectoryMaintenance.xpc/com.apple.CallKit.CallDirectoryMaintenance`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_data`

```diff

-153.100.1.2.29
-  __TEXT.__text: 0x20f80
-  __TEXT.__auth_stubs: 0x10b0
-  __TEXT.__objc_stubs: 0x2920
-  __TEXT.__objc_methlist: 0x1744
-  __TEXT.__const: 0x440
-  __TEXT.__cstring: 0x823
-  __TEXT.__objc_methname: 0x4041
+156.200.70.2.2
+  __TEXT.__text: 0x2374c
+  __TEXT.__auth_stubs: 0x1100
+  __TEXT.__objc_stubs: 0x2b60
+  __TEXT.__objc_methlist: 0x17bc
+  __TEXT.__const: 0x4b8
+  __TEXT.__cstring: 0x843
+  __TEXT.__objc_methname: 0x43c9
   __TEXT.__objc_classname: 0x517
-  __TEXT.__objc_methtype: 0xf0b
-  __TEXT.__gcc_except_tab: 0x2f4
-  __TEXT.__oslogstring: 0x2754
+  __TEXT.__objc_methtype: 0xfdb
+  __TEXT.__gcc_except_tab: 0x348
+  __TEXT.__oslogstring: 0x2934
   __TEXT.__constg_swiftt: 0x14c
   __TEXT.__swift5_types: 0x18
-  __TEXT.__swift5_typeref: 0x2e7
+  __TEXT.__swift5_typeref: 0x307
   __TEXT.__swift5_reflstr: 0x272
   __TEXT.__swift5_fieldmd: 0x1cc
-  __TEXT.__swift5_capture: 0xdc
+  __TEXT.__swift5_capture: 0x140
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0xc
-  __TEXT.__swift_as_entry: 0x28
-  __TEXT.__swift_as_ret: 0x28
-  __TEXT.__swift_as_cont: 0x2c
-  __TEXT.__unwind_info: 0x9a0
-  __TEXT.__eh_frame: 0x568
-  __DATA_CONST.__const: 0xb50
-  __DATA_CONST.__cfstring: 0x340
+  __TEXT.__swift_as_entry: 0x40
+  __TEXT.__swift_as_ret: 0x44
+  __TEXT.__swift_as_cont: 0x54
+  __TEXT.__unwind_info: 0xa68
+  __TEXT.__eh_frame: 0x790
+  __DATA_CONST.__const: 0xc90
+  __DATA_CONST.__cfstring: 0x3a0
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x80

   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x868
-  __DATA_CONST.__got: 0x1d8
-  __DATA_CONST.__auth_ptr: 0x90
-  __DATA.__objc_const: 0x2968
-  __DATA.__objc_selrefs: 0xd88
-  __DATA.__objc_ivar: 0x140
+  __DATA_CONST.__auth_got: 0x890
+  __DATA_CONST.__got: 0x200
+  __DATA_CONST.__auth_ptr: 0x98
+  __DATA.__objc_const: 0x29e8
+  __DATA.__objc_selrefs: 0xe10
+  __DATA.__objc_ivar: 0x14c
   __DATA.__objc_data: 0x840
-  __DATA.__data: 0x7a0
+  __DATA.__data: 0x7b8
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 754
-  Symbols:   246
-  CStrings:  1008
+  Functions: 796
+  Symbols:   248
+  CStrings:  1048
 
Symbols:
+ _OBJC_CLASS_$_NSUserDefaults
+ _swift_getObjCClassFromMetadata
+ _swift_getTypeByMangledNameInContextInMetadataState2
- _swift_release_x24
CStrings:
+ "@\"NSUserDefaults\""
+ "Already updating config, skipping duplicate update"
+ "Error synchronizing call directory extensions during maintenance: %@"
+ "ExtensionsConfig"
+ "LastLiveLookupRefreshOSBuild"
+ "Successfully synchronized call directory extensions"
+ "T@\"NSUserDefaults\",&,N,V_defaults"
+ "TB,N,V_isUpdatingLiveLookupConfig"
+ "Tq,N,R"
+ "T{os_unfair_lock_s=I},R,N,V_configUpdateLock"
+ "_configUpdateLock"
+ "_defaults"
+ "_isUpdatingLiveLookupConfig"
+ "boolForKey:"
+ "callDirectoryHost:requestedMigrationOfAllDataFromExtensionWithBundleID:toExtensionWithBundleID:withCompletionHandler:"
+ "callDirectoryHost:requestedToSynchronizeExtensionsIfPlistValidationChangedWithCompletionHandler:"
+ "configUpdateLock"
+ "defaults"
+ "initWithType:endpoint:issuer:bearerToken:featureId:privacyProxyFailOpen:useUserTierTokenKey:fetchConfigViaProxy:"
+ "instancesRespondToSelector:"
+ "integerForKey:"
+ "integerValue"
+ "isUpdatingLiveLookupConfig"
+ "liveCallerIDOptions"
+ "liveCallerIDOptionsRawValue"
+ "liveCallerIDPlistValidationDisabled"
+ "livecalleridProfileEnabled"
+ "livelookupExtensionsValidated"
+ "migrateAllDataFromExtensionWithBundleID:toExtensionWithBundleID:error:"
+ "not all previous fetches completed within %lu second(s) continuing with cache only"
+ "plistValidationEnabled"
+ "reconfigure in flight, skipping live lookup"
+ "refreshAllExtensionsConfigGroupsWithCompletionHandler:"
+ "refreshExtensionConfigGroup failed: %@"
+ "refreshLiveLookupIfVersionUpdated:"
+ "requested to synchronize extensions if plist validation changed"
+ "requestedMigrationOfAllDataFromExtensionWithBundleID:%@ fromBundleID:%@"
+ "server bag options changed (%@ -> %ld), reconfiguring active extensions"
+ "setBool:forKey:"
+ "setDefaults:"
+ "setInteger:forKey:"
+ "setIsUpdatingLiveLookupConfig:"
+ "shouldUpdateLiveLookupForServerBagChange:currentConfig:"
+ "standardUserDefaults"
+ "v12@?0B8"
+ "v24@0:8@?<v@?B>16"
+ "v32@0:8@16q24"
+ "v48@0:8@\"CXCallDirectoryHost\"16@\"NSString\"24@\"NSString\"32@?<v@?B@\"NSError\">40"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "{os_unfair_lock_s=I}16@0:8"
- "identity = %@"
- "immediateKeyExpirationEnabled"
- "liveCallerIDImmediateKeyExpirationDisabled"
- "liveCallerIDReducedMaxShardCountDisabled"
- "liveCallerIDRequirePowerOfTwoShardCountDisabled"
- "not all previous fetches completed within %lu second(s) continuing"
- "reducedMaxShardCountEnabled"
- "requirePowerOfTwoShardCountEnabled"
- "robustNetworkManagerDisabled"
- "robustNetworkManagerEnabled"
```
