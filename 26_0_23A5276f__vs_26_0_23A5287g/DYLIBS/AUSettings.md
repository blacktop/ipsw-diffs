## AUSettings

> `/System/Library/PrivateFrameworks/AUSettings.framework/AUSettings`

```diff

-1338.0.37.0.0
-  __TEXT.__text: 0x4d40
-  __TEXT.__auth_stubs: 0x320
-  __TEXT.__objc_methlist: 0x5fc
+1338.0.46.502.1
+  __TEXT.__text: 0x52f0
+  __TEXT.__auth_stubs: 0x340
+  __TEXT.__objc_methlist: 0x674
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0xc47
-  __TEXT.__oslogstring: 0x18c
+  __TEXT.__cstring: 0xd38
+  __TEXT.__oslogstring: 0x1bb
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x160
-  __TEXT.__objc_classname: 0x9d
-  __TEXT.__objc_methname: 0x11f6
-  __TEXT.__objc_methtype: 0x256
-  __TEXT.__objc_stubs: 0x940
-  __DATA_CONST.__got: 0xa8
+  __TEXT.__unwind_info: 0x168
+  __TEXT.__objc_classname: 0xeb
+  __TEXT.__objc_methname: 0x126a
+  __TEXT.__objc_methtype: 0x28a
+  __TEXT.__objc_stubs: 0x9e0
+  __DATA_CONST.__got: 0xb8
   __DATA_CONST.__const: 0x558
-  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c8
-  __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x1a0
-  __AUTH_CONST.__const: 0x40
+  __DATA_CONST.__objc_selrefs: 0x4f8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x20
+  __AUTH_CONST.__auth_got: 0x1b0
+  __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0xee0
-  __AUTH_CONST.__objc_const: 0x938
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x74
-  __DATA.__data: 0x1e0
+  __AUTH_CONST.__objc_const: 0xd08
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x7c
+  __DATA.__data: 0x240
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CBBB71CB-0E3B-356B-8C5D-C2C060FA451C
-  Functions: 131
-  Symbols:   602
-  CStrings:  541
+  UUID: BF9A995A-28F2-3D4C-B144-441D6BDD5FC0
+  Functions: 141
+  Symbols:   650
+  CStrings:  559
 
Symbols:
+ +[AUInternalSettingsAssetManagerXPC xpcConnectionToDaemon]
+ +[AUInternalSettingsAssetManagerXPC xpcConnectionToDaemon].cold.1
+ +[AUInternalSettingsAssetManagerXPC xpcConnectionToDaemon].cold.2
+ -[AUInternalSettingsAssetManagerXPC .cxx_destruct]
+ -[AUInternalSettingsAssetManagerXPC dealloc]
+ -[AUInternalSettingsAssetManagerXPC init]
+ -[AUInternalSettingsAssetManagerXPC remoteObject]
+ -[AUInternalSettingsAssetManagerXPC settingsChangedForSerialNumber:]
+ _OBJC_CLASS_$_AUInternalSettingsAssetManagerXPC
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_IVAR_$_AUInternalSettingsAssetManagerXPC._internalQueue
+ _OBJC_IVAR_$_AUInternalSettingsAssetManagerXPC._xpcConnection
+ _OBJC_METACLASS_$_AUInternalSettingsAssetManagerXPC
+ __OBJC_$_CLASS_METHODS_AUInternalSettingsAssetManagerXPC
+ __OBJC_$_INSTANCE_METHODS_AUInternalSettingsAssetManagerXPC
+ __OBJC_$_INSTANCE_VARIABLES_AUInternalSettingsAssetManagerXPC
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AUInternalSettingsAssetManagerXPCProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AUInternalSettingsAssetManagerXPCProvider
+ __OBJC_$_PROTOCOL_REFS_AUInternalSettingsAssetManagerXPCProvider
+ __OBJC_CLASS_RO_$_AUInternalSettingsAssetManagerXPC
+ __OBJC_LABEL_PROTOCOL_$_AUInternalSettingsAssetManagerXPCProvider
+ __OBJC_METACLASS_RO_$_AUInternalSettingsAssetManagerXPC
+ __OBJC_PROTOCOL_$_AUInternalSettingsAssetManagerXPCProvider
+ __OBJC_PROTOCOL_REFERENCE_$_AUInternalSettingsAssetManagerXPCProvider
+ ___49-[AUInternalSettingsAssetManagerXPC remoteObject]_block_invoke
+ ___49-[AUInternalSettingsAssetManagerXPC remoteObject]_block_invoke.cold.1
+ _dispatch_queue_create
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$invalidate
+ _objc_msgSend$mainBundle
+ _objc_msgSend$settingsChangedForSerialNumber:
+ _objc_msgSend$xpcConnectionToDaemon
+ _objc_retainAutorelease
CStrings:
+ "%s"
+ "%s: Got xpc connection"
+ "%s: remoteObject: %@"
+ "+[AUInternalSettingsAssetManagerXPC xpcConnectionToDaemon]"
+ "-[AUInternalSettingsAssetManagerXPC remoteObject]"
+ "-[AUInternalSettingsAssetManagerXPC remoteObject]_block_invoke"
+ "-[AUInternalSettingsAssetManagerXPC settingsChangedForSerialNumber:]"
+ "@\"NSObject<OS_dispatch_queue>\""
+ "AUInternalSettingsAssetManagerXPC"
+ "AUInternalSettingsAssetManagerXPCProvider"
+ "_internalQueue"
+ "bundleIdentifier"
+ "dealloc"
+ "invalidate"
+ "mainBundle"
+ "settingsChangedForSerialNumber:"
+ "v24@0:8@\"NSString\"16"
+ "xpcConnectionToDaemon"

```
