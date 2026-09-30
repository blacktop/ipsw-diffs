## BusinessChatService

> `/System/Library/PrivateFrameworks/BusinessChatService.framework/BusinessChatService`

```diff

-30110.30.6.3.2
-  __TEXT.__text: 0x6d060
+30112.30.7.8.1
+  __TEXT.__text: 0x6d4ec
   __TEXT.__auth_stubs: 0x9c0
-  __TEXT.__objc_methlist: 0x788c
+  __TEXT.__objc_methlist: 0x791c
   __TEXT.__const: 0x240
-  __TEXT.__cstring: 0x8a70
-  __TEXT.__oslogstring: 0x4d89
+  __TEXT.__cstring: 0x8ac4
+  __TEXT.__oslogstring: 0x4e34
   __TEXT.__gcc_except_tab: 0x7c0
-  __TEXT.__unwind_info: 0x1548
-  __TEXT.__objc_classname: 0x1755
-  __TEXT.__objc_methname: 0xacea
+  __TEXT.__unwind_info: 0x1558
+  __TEXT.__objc_classname: 0x1771
+  __TEXT.__objc_methname: 0xadf3
   __TEXT.__objc_methtype: 0x3153
-  __TEXT.__objc_stubs: 0x79e0
+  __TEXT.__objc_stubs: 0x7a40
   __DATA_CONST.__got: 0x3c8
-  __DATA_CONST.__const: 0x1ce0
+  __DATA_CONST.__const: 0x1cf0
   __DATA_CONST.__objc_classlist: 0x4a0
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x300
+  __DATA_CONST.__objc_protolist: 0x308
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2748
-  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_selrefs: 0x2770
+  __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x388
   __AUTH_CONST.__auth_got: 0x4f0
   __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0x4920
-  __AUTH_CONST.__objc_const: 0xfba8
+  __AUTH_CONST.__cfstring: 0x4960
+  __AUTH_CONST.__objc_const: 0xfda8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x4c8
-  __DATA.__data: 0x2400
+  __DATA.__objc_ivar: 0x4d0
+  __DATA.__data: 0x2460
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_ivar: 0x2f8
   __DATA_DIRTY.__objc_data: 0x2cb0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 2ADC1F0C-D61D-3BE5-AF94-BBAEAD02D47E
-  Functions: 2368
-  Symbols:   8336
-  CStrings:  4359
+  UUID: 3BA56DCC-B30A-39E5-87E3-9294F72933E6
+  Functions: 2379
+  Symbols:   8372
+  CStrings:  4375
 
Symbols:
+ -[BCSPIRServerEnvironment _boolFromDefaultsForKey:defaultValue:]
+ -[BCSPIRServerEnvironment disableCaching]
+ -[BCSWebPresentmentItem pirKey]
+ -[BCSWebPresentmentItem serverType]
+ -[BCSWebPresentmentItemIdentifier setServerType:]
+ -[BCSWebPresentmentItemResolver metadataEnvironment]
+ -[BCSWebPresentmentItemResolver permissionsEnvironment]
+ -[BCSWebPresentmentItemResolver setMetadataEnvironment:]
+ -[BCSWebPresentmentItemResolver setPermissionsEnvironment:]
+ -[BCSWebPresentmentPermissionsItem pirKey]
+ -[BCSWebPresentmentPermissionsItem serverType]
+ _OBJC_IVAR_$_BCSWebPresentmentItemResolver._metadataEnvironment
+ _OBJC_IVAR_$_BCSWebPresentmentItemResolver._permissionsEnvironment
+ __OBJC_$_PROP_LIST_BCSPIRServerTypeProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BCSPIRServerTypeProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BCSPIRServerTypeProviding
+ __OBJC_$_PROTOCOL_REFS_BCSPIRServerEnvironmentProtocol
+ __OBJC_LABEL_PROTOCOL_$_BCSPIRServerTypeProviding
+ __OBJC_PROTOCOL_$_BCSPIRServerTypeProviding
+ __OBJC_PROTOCOL_REFERENCE_$_BCSPIRServerTypeProviding
+ _kBCSDefaultsWebPresentmentPIRDisableCaching
+ _kBCSDefaultsWebPresentmentPermissionsPIRDisableCaching
+ _objc_msgSend$disableCaching
+ _objc_msgSend$metadataEnvironment
+ _objc_msgSend$permissionsEnvironment
CStrings:
+ "%s - Caching disabled for web presentment item type: %@"
+ "%s - Caching disabled for web presentment permissions type: %@"
+ "%s - Invalid server type (Logos (%ld)) for type: %@"
+ "BCSPIRServerTypeProviding"
+ "BCSWebPresentmentPIREnableCaching"
+ "BCSWebPresentmentPermissionsPIREnableCaching"
+ "T@\"<BCSPIRServerEnvironmentProtocol>\",&,N,V_metadataEnvironment"
+ "T@\"<BCSPIRServerEnvironmentProtocol>\",&,N,V_permissionsEnvironment"
+ "_metadataEnvironment"
+ "_permissionsEnvironment"
+ "disableCaching"
+ "messages://open?service=iMessage&recipient=%@%@"
+ "metadataEnvironment"
+ "permissionsEnvironment"
+ "setMetadataEnvironment:"
+ "setPermissionsEnvironment:"
- "Tq,R,N,V_serverType"
- "sms://open?service=iMessage&recipient=%@%@"

```
