## PosterPlatformSupport

> `/System/Library/PrivateFrameworks/PosterPlatformSupport.framework/PosterPlatformSupport`

```diff

-228.2.10.100.0
-  __TEXT.__text: 0x40
-  __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0x40
-  __TEXT.__unwind_info: 0x58
-  __TEXT.__objc_classname: 0x19
-  __TEXT.__objc_methname: 0xb3
-  __TEXT.__objc_methtype: 0x13
-  __TEXT.__objc_stubs: 0x20
-  __DATA_CONST.__got: 0x8
-  __DATA_CONST.__objc_classlist: 0x8
+228.2.16.0.0
+  __TEXT.__text: 0x147c
+  __TEXT.__auth_stubs: 0x2b0
+  __TEXT.__objc_methlist: 0x10c
+  __TEXT.__const: 0x68
+  __TEXT.__gcc_except_tab: 0x58
+  __TEXT.__cstring: 0x12e
+  __TEXT.__oslogstring: 0x374
+  __TEXT.__unwind_info: 0xb0
+  __TEXT.__objc_classname: 0x51
+  __TEXT.__objc_methname: 0x4fa
+  __TEXT.__objc_methtype: 0x100
+  __TEXT.__objc_stubs: 0x460
+  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__const: 0x98
+  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x8
-  __AUTH_CONST.__objc_const: 0x90
+  __DATA_CONST.__objc_selrefs: 0x180
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x8
+  __AUTH_CONST.__auth_got: 0x168
+  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__cfstring: 0xe0
+  __AUTH_CONST.__objc_const: 0x1c8
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0xc
+  __DATA.__data: 0x60
+  __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x50
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices
   - /System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5
-  Symbols:   14
-  CStrings:  9
+  Functions: 40
+  Symbols:   109
+  CStrings:  97
 
Symbols:
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$_PPSHostConfigurationManager
+ _OBJC_CLASS_$_PRSHostConfiguration
+ _OBJC_METACLASS_$_PPSHostConfigurationManager
+ _PPSLogCommon
+ _PPSLogHostConfiguration
+ _PosterPlatformSupportLoggingSubsystem
+ __Block_object_dispose
+ __NSConcreteGlobalBlock
+ __NSConcreteStackBlock
+ __Unwind_Resume
+ ___CFConstantStringClassReference
+ ___objc_personality_v0
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __os_log_debug_impl
+ __os_log_error_impl
+ __os_log_impl
+ __os_signpost_emit_with_name_impl
+ _dispatch_once
+ _objc_alloc
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSendSuper2
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_opt_new
+ _objc_release
+ _objc_release_x1
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x8
+ _objc_release_x9
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x22
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_storeStrong
+ _os_log_create
+ _os_log_type_enabled
+ _os_signpost_enabled
+ _os_signpost_id_generate
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
CStrings:
+ "\x12"
+ ".cxx_destruct"
+ "<Unknown Error>"
+ "@\"NSMutableSet\""
+ "@\"NSUserDefaults\""
+ "@16@0:8"
+ "@24@0:8@16"
+ "@32@0:8@16^B24"
+ "Already know there's no bundle for role: %!{(MISSING)public}@"
+ "AmbientHostConfigurationProvider.bundle"
+ "Checking for host configuration bundle %!{(MISSING)public}@ for role %!{(MISSING)public}@"
+ "Common"
+ "Connection failed loading host configuration for role %!{(MISSING)public}@"
+ "Deleted cached host configuration for %!{(MISSING)public}@"
+ "Did not find any host configuration for %!{(MISSING)public}@"
+ "Error unarchiving PRSHostConfiguration for %!{(MISSING)public}@: %!{(MISSING)public}@"
+ "Failed to load host configuration for role %!{(MISSING)public}@: %!{(MISSING)public}@"
+ "Failed to load host configuration for role %!{(MISSING)public}@: There is no /System/Library directory??"
+ "Failed to set PRSHostConfiguration for role %!{(MISSING)public}@: %!{(MISSING)public}@"
+ "Found cached host configuration for %!{(MISSING)public}@"
+ "HostConfiguration"
+ "HostConfigurationProviders"
+ "Loaded bundled host configuration for %!{(MISSING)public}@: %!{(MISSING)public}@"
+ "No bundle at %!{(MISSING)public}@ for role %!{(MISSING)public}@"
+ "PPSBundleServiceProtocol"
+ "PPSHostConfigurationManager"
+ "PPSHostConfiguration_"
+ "PRPosterRoleAmbient"
+ "Posters"
+ "Role %!{(MISSING)public}@ not compatible with bundle-based host configuration"
+ "T@\"NSUserDefaults\",&,N,V_userDefaults"
+ "URLByAppendingPathComponent:"
+ "URLsForDirectory:inDomains:"
+ "_lock"
+ "_lock_cachedHostConfigurationForRole:"
+ "_lock_deleteHostConfigurationForRole:"
+ "_lock_hostConfigurationForRole:outCacheHit:"
+ "_lock_loadBundledHostConfigurationForRole:"
+ "_lock_rolesWithoutHostConfigurations"
+ "_lock_setHostConfiguration:forRole:"
+ "_userDefaults"
+ "addObject:"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "bundleNameForRole:"
+ "com.apple.PosterPlatformSupport"
+ "com.apple.PosterPlatformSupportBundleService"
+ "containsObject:"
+ "count"
+ "defaultManager"
+ "defaultsKeyForRole:"
+ "deleteHostConfigurationForRole:"
+ "fileExistsAtPath:"
+ "firstObject"
+ "hostConfigurationForBundleAtURL:forRole:completion:"
+ "hostConfigurationForRole"
+ "hostConfigurationForRole:"
+ "init"
+ "initWithServiceName:"
+ "initWithUserDefaults:"
+ "interfaceWithProtocol:"
+ "invalidate"
+ "isEqualToString:"
+ "localizedDescription"
+ "objectForKey:"
+ "path"
+ "removeObject:"
+ "removeObjectForKey:"
+ "resume"
+ "setHostConfiguration:forRole:"
+ "setObject:forKey:"
+ "setRemoteObjectInterface:"
+ "setUserDefaults:"
+ "sharedHostConfigurationManager"
+ "standardUserDefaults"
+ "stringByAppendingString:"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "unarchivedObjectOfClass:fromData:error:"
+ "userDefaults"
+ "v16@0:8"
+ "v16@?0@\"NSError\"8"
+ "v24@0:8@16"
+ "v24@?0@\"PRSHostConfiguration\"8@\"NSError\"16"
+ "v32@0:8@16@24"
+ "v40@0:8@\"NSURL\"16@\"NSString\"24@?<v@?@\"PRSHostConfiguration\"@\"NSError\">32"
+ "v40@0:8@16@24@?32"
+ "v8@?0"
+ "wasHostConfigurationLoaded=%!{(MISSING)BOOL}u wasCacheHit=%!{(MISSING)BOOL}u"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
