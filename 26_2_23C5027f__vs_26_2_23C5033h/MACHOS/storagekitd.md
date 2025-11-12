## storagekitd

> `/usr/libexec/storagekitd`

```diff

-1024.40.8.0.0
-  __TEXT.__text: 0x2d324
+1024.60.3.0.0
+  __TEXT.__text: 0x2d640
   __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_stubs: 0x6280
-  __TEXT.__objc_methlist: 0x286c
-  __TEXT.__objc_classname: 0x507
-  __TEXT.__objc_methname: 0x63cd
-  __TEXT.__objc_methtype: 0xebb
+  __TEXT.__objc_stubs: 0x62e0
+  __TEXT.__objc_methlist: 0x2914
+  __TEXT.__objc_classname: 0x523
+  __TEXT.__objc_methname: 0x64c9
+  __TEXT.__objc_methtype: 0xfa0
   __TEXT.__const: 0x90
   __TEXT.__gcc_except_tab: 0xc8c
-  __TEXT.__cstring: 0x2d3b
-  __TEXT.__oslogstring: 0x2741
-  __TEXT.__unwind_info: 0xa50
+  __TEXT.__cstring: 0x2dc6
+  __TEXT.__oslogstring: 0x2670
+  __TEXT.__unwind_info: 0xa80
   __DATA_CONST.__auth_got: 0x628
   __DATA_CONST.__got: 0x518
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xec8
-  __DATA_CONST.__cfstring: 0x1f60
-  __DATA_CONST.__objc_classlist: 0x188
+  __DATA_CONST.__const: 0xf60
+  __DATA_CONST.__cfstring: 0x1f00
+  __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x160
+  __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x108
   __DATA_CONST.__objc_dictobj: 0x1b8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x5da0
-  __DATA.__objc_selrefs: 0x1c58
-  __DATA.__objc_ivar: 0x2b4
-  __DATA.__objc_data: 0xf50
+  __DATA.__objc_const: 0x5f00
+  __DATA.__objc_selrefs: 0x1c70
+  __DATA.__objc_ivar: 0x2c0
+  __DATA.__objc_data: 0xfa0
   __DATA.__data: 0x700
   __DATA.__bss: 0x98
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 434C249B-330E-3389-A6DE-4B679453A512
-  Functions: 892
+  UUID: 0DF0BBF4-BC1B-3C3E-8C04-5815686BA903
+  Functions: 908
   Symbols:   372
-  CStrings:  2386
+  CStrings:  2392
 
Symbols:
+ _DADiskMountWithArgumentsAndBlockAndAuditToken
+ _kSKDiskUnmountOptionRecursive
- _DADiskMountWithArguments
- _OBJC_CLASS_$_NSRegularExpression
CStrings:
+ "-[SKDaemonConnection deleteAPFSVolume:optionsDictionary:handlingProgressForOperationUUID:withCompletionUUID:]"
+ "-[SKMountOperation newPerformOperationWithAuditToken:]"
+ "@\"SKAPFSDisk\""
+ "@\"SKDaemonConnection\""
+ "@48@0:8{?=[8I]}16"
+ "B60@0:8@16q24@32r*40B48^B52"
+ "Cannot delete LiveFS APFS volumes, not supported yet"
+ "Delete volume failed"
+ "SKDeleteAPFSVolumeOperation"
+ "T@\"SKAPFSDisk\",&,V_apfsVolume"
+ "T@\"SKDaemonConnection\",R,N,V_connection"
+ "T@?,C,V_completionBlock"
+ "TB,N,V_authorizedAsRoot"
+ "Unable to delete APFS volume operation."
+ "_apfsVolume"
+ "_authorizedAsRoot"
+ "_connection"
+ "apfsVolume"
+ "authorizedAsRoot"
+ "connection"
+ "deleteAPFSVolume:optionsDictionary:handlingProgressForOperationUUID:withCompletionUUID:"
+ "deleteAPFSVolume:progress:completionBlock:"
+ "errorWithOSStatus:debugDescription:error:"
+ "failOperationWithError:"
+ "initWithDisk:completionBlock:"
+ "newPerformOperationWithAuditToken:"
+ "preflightRequestWithSKDisk:entitlementLevel:completionUUID:prettyFunc:authorizationNeeded:authorizedAsRoot:"
+ "setApfsVolume:"
+ "setAuthorizedAsRoot:"
+ "v20@?0B8@\"NSError\"12"
+ "v20@?0f8@\"NSString\"12"
+ "v24@?0^{__DADisk=}8^{__DADissenter=}16"
+ "v40@0:8@\"SKAPFSDisk\"16@?<v@?f@\"NSString\">24@?<v@?B@\"NSError\">32"
+ "v40@0:8@16@?24@?32"
+ "v48@0:8@\"NSDictionary\"16@\"NSDictionary\"24@\"NSString\"32@\"NSString\"40"
+ "v48@0:8@16@24@32@40"
- "%s: Client %d asks to mount %@ with %@ option"
- "%s: Client is allowed to mount to %@"
- "%s: Client is not the owner of %@. clientUID = %d, path_info.st_uid = %d, asking for permission"
- "%s: Stat failed on %@, errno %d"
- "-[SKMountOperation newPerformOperation]"
- "-[SKMountOperation validateMountOptionsWithDisk:error:]"
- "-[SKMountOperation validateMountPointWithConnection:error:]"
- "-o"
- "B52@0:8@16q24@32r*40B48"
- "Client has audited mounts entitlement"
- "TB,N,V_authenticateOnInit"
- "TB,R,N,V_requiresMountAudit"
- "[a-z]+"
- "_authenticateOnInit"
- "_requiresMountAudit"
- "authenticateOnInit"
- "dev"
- "firstMatchInString:options:range:"
- "initWithPattern:options:error:"
- "lowercaseString"
- "noperm"
- "preflightRequestWithSKDisk:entitlementLevel:completionUUID:prettyFunc:authorizationNeeded:"
- "range"
- "requiresMountAudit"
- "setAuthenticateOnInit:"
- "substringWithRange:"
- "suid"

```
