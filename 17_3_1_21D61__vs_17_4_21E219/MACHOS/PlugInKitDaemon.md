## PlugInKitDaemon

> `/System/Library/PrivateFrameworks/PlugInKitDaemon.framework/PlugInKitDaemon`

```diff

-473.0.1.0.0
-  __TEXT.__text: 0x17478
-  __TEXT.__auth_stubs: 0xbc0
-  __TEXT.__objc_stubs: 0x3040
-  __TEXT.__objc_methlist: 0xe6c
-  __TEXT.__const: 0x62
-  __TEXT.__objc_methname: 0x2e7d
+473.100.2.0.0
+  __TEXT.__text: 0x17244
+  __TEXT.__auth_stubs: 0xb60
+  __TEXT.__objc_stubs: 0x2fc0
+  __TEXT.__objc_methlist: 0xd44
+  __TEXT.__const: 0x6a
+  __TEXT.__objc_methname: 0x2e67
   __TEXT.__oslogstring: 0x2abd
   __TEXT.__cstring: 0x1091
-  __TEXT.__objc_classname: 0x185
-  __TEXT.__objc_methtype: 0x8c3
+  __TEXT.__objc_classname: 0x190
+  __TEXT.__objc_methtype: 0x6c8
   __TEXT.__gcc_except_tab: 0x374
-  __TEXT.__unwind_info: 0x41c
-  __DATA_CONST.__auth_got: 0x5f0
+  __TEXT.__unwind_info: 0x3e4
+  __DATA_CONST.__auth_got: 0x5c0
   __DATA_CONST.__got: 0x398
-  __DATA_CONST.__const: 0x510
+  __DATA_CONST.__const: 0x4f0
   __DATA_CONST.__cfstring: 0x1020
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x148
+  __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x2c28
-  __DATA.__objc_selrefs: 0xd50
-  __DATA.__objc_classrefs: 0x150
-  __DATA.__objc_superrefs: 0x68
+  __DATA.__objc_const: 0x2a80
+  __DATA.__objc_selrefs: 0xd08
   __DATA.__objc_ivar: 0x110
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x300
-  __DATA.__bss: 0x78
+  __DATA.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 39A019F4-8AD9-3DE5-9F44-676CC2A964B4
-  Functions: 434
-  Symbols:   1477
-  CStrings:  1212
+  UUID: FFEC2791-6E37-3965-8093-D9106FEC392A
+  Functions: 412
+  Symbols:   1434
+  CStrings:  1194
 
Symbols:
+ -[PKDAnnotationStore external]
+ -[PKDAnnotationStore initWithDatabase:externalProviders:]
+ -[PKDAnnotationStore initWithDatabase:externalProviders:].cold.1
+ -[PKDAnnotationStore initWithDatabase:externalProviders:].cold.2
+ -[PKDAnnotationStore initWithDatabase:externalProviders:].cold.3
+ -[PKDContainerProvider create_or_lookup_path_for_current_user:identifier:create_if_necessary:transient:out_existed:out_error:]
+ -[PKDExternalProviders .cxx_destruct]
+ -[PKDExternalProviders container]
+ -[PKDExternalProviders initWithLaunchServicesProvider:]
+ -[PKDExternalProviders init]
+ -[PKDExternalProviders security]
+ -[PKDExternalProviders um]
+ -[PKDPlugIn initWithLSData:personaCache:discoveryInstanceUUID:extensionPointCache:externalProviders:]
+ -[PKDPlugIn initWithLSData:personaCache:discoveryInstanceUUID:extensionPointCache:externalProviders:].cold.1
+ -[PKDPlugIn initWithLSData:personaCache:discoveryInstanceUUID:extensionPointCache:externalProviders:].cold.2
+ -[PKDServer initForService:database:externalProviders:]
+ -[PKDServer initWithConnection:queue:database:externalProviders:]
+ -[PKDUserManagementProvider isMultiUser]
+ -[PKDatabase external]
+ -[PKDatabase initWithDatabase:externalProviders:]
+ OBJC_IVAR_$_PKDAnnotationStore._external
+ OBJC_IVAR_$_PKDExternalProviders._container
+ OBJC_IVAR_$_PKDExternalProviders._security
+ OBJC_IVAR_$_PKDExternalProviders._um
+ OBJC_IVAR_$_PKDatabase._external
+ _OBJC_$_PROP_LIST_PKDExternalProviders.96
+ _OBJC_$_PROP_LIST_PKDUserManagementProvider.45
+ _OBJC_CLASS_$_PKDContainerProvider
+ _OBJC_CLASS_$_PKDExternalProviders
+ _OBJC_CLASS_$_PKDSecurityProvider
+ _OBJC_CLASS_$_PKDUserManagementProvider
+ _OBJC_CLASS_$_PKExternalProviders
+ _OBJC_METACLASS_$_PKDContainerProvider
+ _OBJC_METACLASS_$_PKDExternalProviders
+ _OBJC_METACLASS_$_PKDSecurityProvider
+ _OBJC_METACLASS_$_PKDUserManagementProvider
+ _OBJC_METACLASS_$_PKExternalProviders
+ __50-[PKDServer terminatePlugIns:synchronously:reply:]_block_invoke.17
+ __50-[PKDServer terminatePlugIns:synchronously:reply:]_block_invoke.17.cold.1
+ __50-[PKDServer terminatePlugIns:synchronously:reply:]_block_invoke.17.cold.2
+ __65-[PKDServer initWithConnection:queue:database:externalProviders:]_block_invoke.11
+ __65-[PKDServer initWithConnection:queue:database:externalProviders:]_block_invoke.cold.1
+ __65-[PKDServer initWithConnection:queue:database:externalProviders:]_block_invoke.cold.2
+ __OBJC_$_INSTANCE_METHODS_PKDContainerProvider
+ __OBJC_$_INSTANCE_METHODS_PKDExternalProviders
+ __OBJC_$_INSTANCE_METHODS_PKDUserManagementProvider
+ __OBJC_$_INSTANCE_VARIABLES_PKDExternalProviders
+ __OBJC_$_PROP_LIST_PKDContainerProvider
+ __OBJC_$_PROP_LIST_PKDExternalProviders
+ __OBJC_$_PROP_LIST_PKDSecurityProvider
+ __OBJC_$_PROP_LIST_PKDUserManagementProvider
+ __OBJC_$_PROP_LIST_PKExternalProviders
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PKDContainerProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PKDExternalProviders
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PKDUserManagementProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PKExternalProviders
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PKDContainerProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PKDExternalProviders
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PKDUserManagementProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PKExternalProviders
+ __OBJC_$_PROTOCOL_REFS_PKDContainerProvider
+ __OBJC_$_PROTOCOL_REFS_PKDExternalProviders
+ __OBJC_$_PROTOCOL_REFS_PKDSecurityProvider
+ __OBJC_$_PROTOCOL_REFS_PKDUserManagementProvider
+ __OBJC_$_PROTOCOL_REFS_PKExternalProviders
+ __OBJC_CLASS_PROTOCOLS_$_PKDContainerProvider
+ __OBJC_CLASS_PROTOCOLS_$_PKDExternalProviders
+ __OBJC_CLASS_PROTOCOLS_$_PKDSecurityProvider
+ __OBJC_CLASS_PROTOCOLS_$_PKDUserManagementProvider
+ __OBJC_CLASS_RO_$_PKDContainerProvider
+ __OBJC_CLASS_RO_$_PKDExternalProviders
+ __OBJC_CLASS_RO_$_PKDSecurityProvider
+ __OBJC_CLASS_RO_$_PKDUserManagementProvider
+ __OBJC_LABEL_PROTOCOL_$_PKDContainerProvider
+ __OBJC_LABEL_PROTOCOL_$_PKDExternalProviders
+ __OBJC_LABEL_PROTOCOL_$_PKDSecurityProvider
+ __OBJC_LABEL_PROTOCOL_$_PKDUserManagementProvider
+ __OBJC_LABEL_PROTOCOL_$_PKExternalProviders
+ __OBJC_METACLASS_RO_$_PKDContainerProvider
+ __OBJC_METACLASS_RO_$_PKDExternalProviders
+ __OBJC_METACLASS_RO_$_PKDSecurityProvider
+ __OBJC_METACLASS_RO_$_PKDUserManagementProvider
+ __OBJC_PROTOCOL_$_PKDContainerProvider
+ __OBJC_PROTOCOL_$_PKDExternalProviders
+ __OBJC_PROTOCOL_$_PKDSecurityProvider
+ __OBJC_PROTOCOL_$_PKDUserManagementProvider
+ __OBJC_PROTOCOL_$_PKExternalProviders
+ ___49-[PKDatabase initWithDatabase:externalProviders:]_block_invoke
+ ___65-[PKDServer initWithConnection:queue:database:externalProviders:]_block_invoke
+ _objc_msgSend$container
+ _objc_msgSend$create_or_lookup_path_for_current_user:identifier:create_if_necessary:transient:out_existed:out_error:
+ _objc_msgSend$external
+ _objc_msgSend$filesystem
+ _objc_msgSend$initForService:database:externalProviders:
+ _objc_msgSend$initWithConnection:queue:database:externalProviders:
+ _objc_msgSend$initWithDatabase:externalProviders:
+ _objc_msgSend$initWithLSData:personaCache:discoveryInstanceUUID:extensionPointCache:externalProviders:
+ _objc_msgSend$launch
+ _objc_msgSend$ls
+ _objc_msgSend$remove_external_service:version:targetq:callback:
+ _objc_msgSend$sys
+ _objc_msgSend$um
- +[PKDFileManagerProxy defaultManager]
- +[PKDProxyFactory defaultFactory]
- +[PKDUserManagerProxy sharedManager]
- -[PKDAnnotationStore initWithDatabase:proxyFactory:]
- -[PKDAnnotationStore initWithDatabase:proxyFactory:].cold.1
- -[PKDAnnotationStore initWithDatabase:proxyFactory:].cold.2
- -[PKDAnnotationStore initWithDatabase:proxyFactory:].cold.3
- -[PKDAnnotationStore proxyFactory]
- -[PKDFileManagerProxy .cxx_destruct]
- -[PKDFileManagerProxy _underlyingManager]
- -[PKDFileManagerProxy createDirectoryAtURL:withIntermediateDirectories:attributes:error:]
- -[PKDFileManagerProxy initWithNSFileManager:]
- -[PKDPlugIn initWithLSData:personaCache:discoveryInstanceUUID:extensionPointCache:proxyFactory:]
- -[PKDPlugIn initWithLSData:personaCache:discoveryInstanceUUID:extensionPointCache:proxyFactory:].cold.1
- -[PKDPlugIn initWithLSData:personaCache:discoveryInstanceUUID:extensionPointCache:proxyFactory:].cold.2
- -[PKDProcessIdentityProxy .cxx_destruct]
- -[PKDProcessIdentityProxy _rbsObject]
- -[PKDProcessIdentityProxy initWithRBSProcessIdentity:]
- -[PKDProxyFactory CFRunLoopRun]
- -[PKDProxyFactory PKDProcessIdentityProxyClass]
- -[PKDProxyFactory access:amode:]
- -[PKDProxyFactory container_create_or_lookup_path_for_current_user:identifier:create_if_necessary:transient:out_existed:out_error:]
- -[PKDProxyFactory dataWithContentsOfURL:options:error:]
- -[PKDProxyFactory defaultFileManager]
- -[PKDProxyFactory exit:]
- -[PKDProxyFactory getenv:]
- -[PKDProxyFactory getpwuid:]
- -[PKDProxyFactory getuid]
- -[PKDProxyFactory launch_remove_external_service:version:targetq:callback:]
- -[PKDProxyFactory sharedUserManager]
- -[PKDProxyFactory userManagerProxyClass]
- -[PKDProxyFactory writeToURL:withData:options:error:]
- -[PKDServer initForService:database:proxyFactory:]
- -[PKDServer initWithConnection:queue:database:proxyFactory:]
- -[PKDUserManagerProxy .cxx_destruct]
- -[PKDUserManagerProxy _umUserManager]
- -[PKDUserManagerProxy initWithUMUserManager:]
- -[PKDUserManagerProxy isMultiUser]
- -[PKDUserManagerProxy set_umUserManager:]
- -[PKDatabase initWithDatabase:proxyFactory:]
- -[PKDatabase proxyFactory]
- OBJC_IVAR_$_PKDAnnotationStore._proxyFactory
- OBJC_IVAR_$_PKDFileManagerProxy.__underlyingManager
- OBJC_IVAR_$_PKDProcessIdentityProxy.__rbsObject
- OBJC_IVAR_$_PKDUserManagerProxy.__umUserManager
- OBJC_IVAR_$_PKDatabase._proxyFactory
- _CFRunLoopRun
- _OBJC_$_PROP_LIST_PKDUserManagerProxy.59
- _OBJC_CLASS_$_NSData
- _OBJC_CLASS_$_PKDFileManagerProxy
- _OBJC_CLASS_$_PKDProcessIdentityProxy
- _OBJC_CLASS_$_PKDProxyFactory
- _OBJC_CLASS_$_PKDUserManagerProxy
- _OBJC_CLASS_$_PKProxyFactory
- _OBJC_METACLASS_$_PKDFileManagerProxy
- _OBJC_METACLASS_$_PKDProcessIdentityProxy
- _OBJC_METACLASS_$_PKDProxyFactory
- _OBJC_METACLASS_$_PKDUserManagerProxy
- _OBJC_METACLASS_$_PKProxyFactory
- __50-[PKDServer terminatePlugIns:synchronously:reply:]_block_invoke.16
- __50-[PKDServer terminatePlugIns:synchronously:reply:]_block_invoke.16.cold.1
- __50-[PKDServer terminatePlugIns:synchronously:reply:]_block_invoke.16.cold.2
- __60-[PKDServer initWithConnection:queue:database:proxyFactory:]_block_invoke.11
- __60-[PKDServer initWithConnection:queue:database:proxyFactory:]_block_invoke.cold.1
- __60-[PKDServer initWithConnection:queue:database:proxyFactory:]_block_invoke.cold.2
- __OBJC_$_CLASS_METHODS_PKDFileManagerProxy
- __OBJC_$_CLASS_METHODS_PKDProxyFactory
- __OBJC_$_CLASS_METHODS_PKDUserManagerProxy
- __OBJC_$_INSTANCE_METHODS_PKDFileManagerProxy
- __OBJC_$_INSTANCE_METHODS_PKDProcessIdentityProxy
- __OBJC_$_INSTANCE_METHODS_PKDProxyFactory
- __OBJC_$_INSTANCE_METHODS_PKDUserManagerProxy
- __OBJC_$_INSTANCE_VARIABLES_PKDFileManagerProxy
- __OBJC_$_INSTANCE_VARIABLES_PKDProcessIdentityProxy
- __OBJC_$_INSTANCE_VARIABLES_PKDUserManagerProxy
- __OBJC_$_PROP_LIST_PKDFileManagerProxy
- __OBJC_$_PROP_LIST_PKDProcessIdentityProxy
- __OBJC_$_PROP_LIST_PKDProxyFactory
- __OBJC_$_PROP_LIST_PKDUserManagerProxy
- __OBJC_$_PROP_LIST_PKProxyFactory
- __OBJC_$_PROTOCOL_CLASS_METHODS_PKDFileManagerProxy
- __OBJC_$_PROTOCOL_CLASS_METHODS_PKDUserManagerProxy
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PKDFileManagerProxy
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PKDProxyFactory
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PKDUserManagerProxy
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PKProxyFactory
- __OBJC_$_PROTOCOL_METHOD_TYPES_PKDFileManagerProxy
- __OBJC_$_PROTOCOL_METHOD_TYPES_PKDProxyFactory
- __OBJC_$_PROTOCOL_METHOD_TYPES_PKDUserManagerProxy
- __OBJC_$_PROTOCOL_METHOD_TYPES_PKProxyFactory
- __OBJC_$_PROTOCOL_REFS_PKDFileManagerProxy
- __OBJC_$_PROTOCOL_REFS_PKDProcessIdentityProxy
- __OBJC_$_PROTOCOL_REFS_PKDProxyFactory
- __OBJC_$_PROTOCOL_REFS_PKDUserManagerProxy
- __OBJC_$_PROTOCOL_REFS_PKProxyFactory
- __OBJC_CLASS_PROTOCOLS_$_PKDFileManagerProxy
- __OBJC_CLASS_PROTOCOLS_$_PKDProcessIdentityProxy
- __OBJC_CLASS_PROTOCOLS_$_PKDProxyFactory
- __OBJC_CLASS_PROTOCOLS_$_PKDUserManagerProxy
- __OBJC_CLASS_RO_$_PKDFileManagerProxy
- __OBJC_CLASS_RO_$_PKDProcessIdentityProxy
- __OBJC_CLASS_RO_$_PKDProxyFactory
- __OBJC_CLASS_RO_$_PKDUserManagerProxy
- __OBJC_LABEL_PROTOCOL_$_PKDFileManagerProxy
- __OBJC_LABEL_PROTOCOL_$_PKDProcessIdentityProxy
- __OBJC_LABEL_PROTOCOL_$_PKDProxyFactory
- __OBJC_LABEL_PROTOCOL_$_PKDUserManagerProxy
- __OBJC_LABEL_PROTOCOL_$_PKProxyFactory
- __OBJC_METACLASS_RO_$_PKDFileManagerProxy
- __OBJC_METACLASS_RO_$_PKDProcessIdentityProxy
- __OBJC_METACLASS_RO_$_PKDProxyFactory
- __OBJC_METACLASS_RO_$_PKDUserManagerProxy
- __OBJC_PROTOCOL_$_PKDFileManagerProxy
- __OBJC_PROTOCOL_$_PKDProcessIdentityProxy
- __OBJC_PROTOCOL_$_PKDProxyFactory
- __OBJC_PROTOCOL_$_PKDUserManagerProxy
- __OBJC_PROTOCOL_$_PKProxyFactory
- ___33+[PKDProxyFactory defaultFactory]_block_invoke
- ___44-[PKDatabase initWithDatabase:proxyFactory:]_block_invoke
- ___60-[PKDServer initWithConnection:queue:database:proxyFactory:]_block_invoke
- _access
- _exit
- _getpwuid
- _launch_remove_external_service
- _objc_msgSend$PKDProcessIdentityProxyClass
- _objc_msgSend$_umUserManager
- _objc_msgSend$_underlyingManager
- _objc_msgSend$container_create_or_lookup_path_for_current_user:identifier:create_if_necessary:transient:out_existed:out_error:
- _objc_msgSend$defaultFactory
- _objc_msgSend$defaultFileManager
- _objc_msgSend$initForService:database:proxyFactory:
- _objc_msgSend$initWithConnection:queue:database:proxyFactory:
- _objc_msgSend$initWithContentsOfURL:options:error:
- _objc_msgSend$initWithDatabase:proxyFactory:
- _objc_msgSend$initWithLSData:personaCache:discoveryInstanceUUID:extensionPointCache:proxyFactory:
- _objc_msgSend$initWithNSFileManager:
- _objc_msgSend$initWithUMUserManager:
- _objc_msgSend$launch_remove_external_service:version:targetq:callback:
- _objc_msgSend$proxyFactory
- _objc_msgSend$userManagerProxyClass
- _objc_msgSend$writeToURL:options:error:
- _objc_retain_x4
- defaultFactory.defaultProxyFactory
- defaultFactory.onceToken
CStrings:
+ "@\"<PKDContainerProvider>\""
+ "@\"<PKDContainerProvider>\"16@0:8"
+ "@\"<PKDExternalProviders>\""
+ "@\"<PKDSecurityProvider>\""
+ "@\"<PKDSecurityProvider>\"16@0:8"
+ "@\"<PKDUserManagementProvider>\""
+ "@\"<PKDUserManagementProvider>\"16@0:8"
+ "@\"<PKFilesystemProvider>\"16@0:8"
+ "@\"<PKLaunchProvider>\"16@0:8"
+ "@\"<PKLaunchServicesProvider>\"16@0:8"
+ "@\"<PKRunningBoardProvider>\"16@0:8"
+ "@\"<PKSandboxProvider>\"16@0:8"
+ "@\"<PKSystemProvider>\"16@0:8"
+ "PKDContainerProvider"
+ "PKDExternalProviders"
+ "PKDSecurityProvider"
+ "PKDUserManagementProvider"
+ "PKExternalProviders"
+ "T@\"<PKDContainerProvider>\",R,N"
+ "T@\"<PKDContainerProvider>\",R,N,V_container"
+ "T@\"<PKDExternalProviders>\",R,N,V_external"
+ "T@\"<PKDSecurityProvider>\",R,N"
+ "T@\"<PKDSecurityProvider>\",R,N,V_security"
+ "T@\"<PKDUserManagementProvider>\",R,N"
+ "T@\"<PKDUserManagementProvider>\",R,N,V_um"
+ "T@\"<PKFilesystemProvider>\",R,N"
+ "T@\"<PKLaunchProvider>\",R,N"
+ "T@\"<PKLaunchServicesProvider>\",R,N"
+ "T@\"<PKRunningBoardProvider>\",R,N"
+ "T@\"<PKSandboxProvider>\",R,N"
+ "T@\"<PKSystemProvider>\",R,N"
+ "T@\"NSString\",?,R,C"
+ "_container"
+ "_external"
+ "_security"
+ "_um"
+ "container"
+ "create_or_lookup_path_for_current_user:identifier:create_if_necessary:transient:out_existed:out_error:"
+ "external"
+ "filesystem"
+ "initForService:database:externalProviders:"
+ "initWithConnection:queue:database:externalProviders:"
+ "initWithDatabase:externalProviders:"
+ "initWithLSData:personaCache:discoveryInstanceUUID:extensionPointCache:externalProviders:"
+ "initWithLaunchServicesProvider:"
+ "initWithName:extensionPointPlatform:url:bundleInfo:uuid:discoveryInstanceUUID:extensionPointCache:externalProviders:"
+ "launch"
+ "ls"
+ "remove_external_service:version:targetq:callback:"
+ "runningboard"
+ "sandbox"
+ "security"
+ "sys"
+ "um"
- "\x01"
- "*24@0:8r*16"
- "@\"<PKApplicationProxy>\"24@0:8@\"NSURL\"16"
- "@\"<PKApplicationWorkspaceProxy>\"16@0:8"
- "@\"<PKDFileManagerProxy>\"16@0:8"
- "@\"<PKDProxyFactory>\""
- "@\"<PKDUserManagerProxy>\"16@0:8"
- "@\"<PKExtensionPointProxy>\"32@0:8@\"NSString\"16@\"NSNumber\"24"
- "@\"<PKPlugInProxy>\"24@0:8@\"NSURL\"16"
- "@\"<PKPlugInProxy>\"24@0:8@\"NSUUID\"16"
- "@\"<PKPlugInRecordProxy>\"24@0:8@\"NSString\"16"
- "@\"<PKPlugInRecordProxy>\"24@0:8@\"NSUUID\"16"
- "@\"NSData\"40@0:8@\"NSURL\"16Q24^@32"
- "@\"NSFileManager\""
- "@\"PKEnumerator\"16@0:8"
- "@\"PKEnumerator\"24@0:8@\"<PKExtensionPointRecordProxy>\"16"
- "@\"PKEnumerator\"24@0:8@\"NSString\"16"
- "@\"PKEnumerator\"28@0:8@\"NSString\"16I24"
- "@\"RBSProcessIdentity\""
- "@28@0:8@16I24"
- "@40@0:8@16Q24^@32"
- "B44@0:8@\"NSURL\"16B24@\"NSDictionary\"28^@36"
- "B44@0:8@16B24@28^@36"
- "B48@0:8@\"NSURL\"16@\"NSData\"24Q32^@40"
- "B48@0:8@16@24Q32^@40"
- "PKDFileManagerProxy"
- "PKDProcessIdentityProxy"
- "PKDProcessIdentityProxyClass"
- "PKDProxyFactory"
- "PKDUserManagerProxy"
- "PKProxyFactory"
- "T@\"<PKDProxyFactory>\",R,N,V_proxyFactory"
- "T@\"NSFileManager\",R,V__underlyingManager"
- "T@\"RBSProcessIdentity\",R,V__rbsObject"
- "T@\"UMUserManager\",&,V__umUserManager"
- "TB,R,N"
- "^{passwd=**IIq****q}20@0:8I16"
- "__rbsObject"
- "__umUserManager"
- "__underlyingManager"
- "_proxyFactory"
- "_rbsObject"
- "_umUserManager"
- "_underlyingManager"
- "access:amode:"
- "container_create_or_lookup_path_for_current_user:identifier:create_if_necessary:transient:out_existed:out_error:"
- "defaultFactory"
- "defaultFileManager"
- "extensionPointForIdentifier:platform:"
- "getenv:"
- "getpwuid:"
- "getuid"
- "hasLSDatabaseAccess"
- "i28@0:8r*16i24"
- "initForService:database:proxyFactory:"
- "initWithConnection:queue:database:proxyFactory:"
- "initWithContentsOfURL:options:error:"
- "initWithDatabase:proxyFactory:"
- "initWithLSData:personaCache:discoveryInstanceUUID:extensionPointCache:proxyFactory:"
- "initWithNSFileManager:"
- "initWithName:extensionPointPlatform:url:bundleInfo:uuid:discoveryInstanceUUID:extensionPointCache:proxyFactory:"
- "initWithRBSProcessIdentity:"
- "initWithUMUserManager:"
- "launch_remove_external_service:version:targetq:callback:"
- "plugInRecordForUUID:"
- "proxyFactory"
- "set_umUserManager:"
- "userManagerProxyClass"
- "v20@0:8i16"
- "v48@0:8r*16r*24@\"NSObject<OS_dispatch_queue>\"32@?<v@?i>40"
- "v48@0:8r*16r*24@32@?40"
- "writeToURL:options:error:"

```
