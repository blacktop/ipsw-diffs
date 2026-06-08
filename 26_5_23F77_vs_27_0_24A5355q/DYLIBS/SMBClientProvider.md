## SMBClientProvider

> `/System/Library/PrivateFrameworks/SMBClientProvider.framework/SMBClientProvider`

```diff

-231.120.1.0.1
-  __TEXT.__text: 0x1870
-  __TEXT.__auth_stubs: 0x1f0
+245.0.0.0.1
+  __TEXT.__text: 0x1778
   __TEXT.__objc_methlist: 0x170
   __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0xe8
+  __TEXT.__gcc_except_tab: 0xec
   __TEXT.__cstring: 0x122
   __TEXT.__oslogstring: 0xe2
-  __TEXT.__unwind_info: 0x108
-  __TEXT.__objc_classname: 0x34
-  __TEXT.__objc_methname: 0x4c5
-  __TEXT.__objc_methtype: 0x373
-  __TEXT.__objc_stubs: 0x280
-  __DATA_CONST.__got: 0x50
+  __TEXT.__unwind_info: 0x100
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x140
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_selrefs: 0x138
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x108
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x110
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__data: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/LiveFS.framework/LiveFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9F395320-A61B-3E6E-9B47-09E22E059854
-  Functions: 47
-  Symbols:   191
-  CStrings:  83
+  UUID: 3B8CE221-7D07-3B84-B852-C1272F205F29
+  Functions: 45
+  Symbols:   195
+  CStrings:  15
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x8
+ _objc_storeStrong
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _objc_retainAutoreleasedReturnValue
CStrings:
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@32@0:8@16^@24"
- "@48@0:8@16@24q32@40"
- "@48@0:8@16q24@32^@40"
- "LiveFSVolumeManager"
- "SMBClientManager"
- "SMBClientMount"
- "SMBClientProtocolCredentialsForServer:completionHandler:"
- "addDisk:fileSystemType:reply:"
- "addObject:"
- "addSMBServerOrShare:completionHandler:"
- "addVolume:atServer:credentialType:credential:"
- "addVolume:atServer:credentialType:credential:reply:"
- "addVolume:listener:description:reply:"
- "addVolumes:atServer:credentialType:credential:completionHandler:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "credentialTypes:"
- "credentialTypesForServer:completionHandler:"
- "ejectDisk:usingFlags:reply:"
- "ejectVolume:usingFlags:reply:"
- "errorWithDomain:code:userInfo:"
- "forgetVolume:"
- "forgetVolume:completionHandler:"
- "forgetVolume:withFlags:"
- "forgetVolume:withFlags:completionHandler:"
- "interfaceWithProtocol:"
- "listVolumes:"
- "listenerForVolume:completionHandler:"
- "listenerForVolume:error:"
- "listenerForVolume:reply:"
- "lock"
- "newConnectionForService:"
- "newManager"
- "remoteObjectProxyWithErrorHandler:"
- "setObject:forKey:"
- "setRemoteObjectInterface:"
- "sharesAtServer:credentialType:credential:completionHandler:"
- "sharesAtServer:credentialType:credential:error:"
- "sharesAtServer:credentialType:credential:reply:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "uniqueNameForName:reply:"
- "unlock"
- "unlockVolume:password:saveToKeychain:completionHandler:"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\">16"
- "v24@0:8@?<v@?@\"NSDictionary\">16"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v36@0:8@\"NSString\"16I24@?<v@?@\"NSError\">28"
- "v36@0:8@16I24@?28"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\"@\"NSArray\">32"
- "v40@0:8@16@24@?32"
- "v44@0:8@\"NSString\"16@\"NSString\"24B32@?<v@?@\"NSError\">36"
- "v44@0:8@16@24B32@?36"
- "v48@0:8@\"NSString\"16@\"NSXPCListenerEndpoint\"24@32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSString\"16q24@\"NSDictionary\"32@?<v@?@\"NSArray\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16q24@32@?40"
- "v56@0:8@\"NSString\"16@\"NSString\"24q32@\"NSDictionary\"40@?<v@?@\"NSError\">48"
- "v56@0:8@16@24q32@40@?48"
- "volumes:"
- "volumesWithCompletionHandler:"

```
