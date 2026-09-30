## CoreServices

> `/System/Library/Frameworks/CoreServices.framework/CoreServices`

```diff

-1444.2.11.0.0
-  __TEXT.__text: 0x1acbac
+1444.3.2.0.0
+  __TEXT.__text: 0x1ad5f0
   __TEXT.__auth_stubs: 0x30e0
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0x16c
-  __TEXT.__objc_methlist: 0xcd44
+  __TEXT.__objc_methlist: 0xcd74
   __TEXT.__const: 0x910
-  __TEXT.__cstring: 0x24abd
-  __TEXT.__oslogstring: 0x13831
-  __TEXT.__gcc_except_tab: 0x27310
+  __TEXT.__cstring: 0x24aee
+  __TEXT.__oslogstring: 0x13942
+  __TEXT.__gcc_except_tab: 0x273fc
   __TEXT.__ustring: 0x23c
-  __TEXT.__unwind_info: 0xb1c8
+  __TEXT.__unwind_info: 0xb200
   __TEXT.__eh_frame: 0x60
   __TEXT.__objc_classname: 0x1f0e
-  __TEXT.__objc_methname: 0x1d1f7
-  __TEXT.__objc_methtype: 0xaa50
-  __TEXT.__objc_stubs: 0x10380
+  __TEXT.__objc_methname: 0x1d2a3
+  __TEXT.__objc_methtype: 0xaac4
+  __TEXT.__objc_stubs: 0x103c0
   __DATA_CONST.__got: 0xa90
-  __DATA_CONST.__const: 0x6d00
+  __DATA_CONST.__const: 0x6d50
   __DATA_CONST.__objc_classlist: 0x6b8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5ea8
+  __DATA_CONST.__objc_selrefs: 0x5eb8
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x570
   __DATA_CONST.__objc_arraydata: 0x188
   __AUTH_CONST.__auth_got: 0x1890
   __AUTH_CONST.__const: 0x3690
-  __AUTH_CONST.__cfstring: 0x16b00
-  __AUTH_CONST.__objc_const: 0x13140
+  __AUTH_CONST.__cfstring: 0x16b40
+  __AUTH_CONST.__objc_const: 0x13148
   __AUTH_CONST.__objc_intobj: 0x828
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x138

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: ADA5FD68-13A1-3B13-A3FB-FF7A520FA29E
-  Functions: 8676
-  Symbols:   28208
-  CStrings:  13673
+  UUID: 95E2D0B0-A900-312E-8E55-E389BA357BBB
+  Functions: 8682
+  Symbols:   28225
+  CStrings:  13689
 
Symbols:
+ -[LSApplicationExtensionRecord compatibilityObject]
+ -[LSApplicationExtensionRecord compatibilityObject].cold.1
+ -[_LSDReadClient _getRedactedPluginProxy:appexRecord:UUID:node:bundleIdentifier:platform:error:]
+ -[_LSDReadClient getRedactedPluginProxyForSystemAppexWithUUID:node:bundleIdentifier:platform:completionHandler:]
+ ___51-[LSApplicationExtensionRecord compatibilityObject]_block_invoke
+ ___51-[LSApplicationExtensionRecord compatibilityObject]_block_invoke_2
+ ____ZL15_LSContainerAddP9LSContextP6FSNodeP6NSDataS2_S4_tyhU13block_pointerFvjP7NSErrorE_block_invoke_2
+ ___block_descriptor_48_ea8_32r40r_e38_v24?0"LSPlugInKitProxy"8"NSError"16lr32l8r40l8
+ ___block_descriptor_50_ea8_32r40r_e19_v32?0I8r^v12I20*24lr32l8r40l8
+ _objc_msgSend$_getRedactedPluginProxy:appexRecord:UUID:node:bundleIdentifier:platform:error:
+ _objc_msgSend$getRedactedPluginProxyForSystemAppexWithUUID:node:bundleIdentifier:platform:completionHandler:
- ____ZL15_LSContainerAddP9LSContextP6FSNodeP6NSDataS2_S4_tyhU13block_pointerFvjP7NSErrorE_block_invoke.cold.4
CStrings:
+ "-[_LSDReadClient _getRedactedPluginProxy:appexRecord:UUID:node:bundleIdentifier:platform:error:]"
+ "B68@0:8^@16^@24@32@40@48I56^@60"
+ "T@\"LSPlugInKitProxy\",R,N"
+ "Updating state of volume 0x%llx %{private}@ to mounted with volume ID %llu"
+ "_getRedactedPluginProxy:appexRecord:UUID:node:bundleIdentifier:platform:error:"
+ "adding container for %@"
+ "found mounted container unit 0x%llx"
+ "found preboot volume in fallback path"
+ "found unmounted container unit 0x%llx (noting mounted)"
+ "getRedactedPluginProxyForSystemAppexWithUUID:node:bundleIdentifier:platform:completionHandler:"
+ "isOnPrebootVolume"
+ "preboot"
+ "register container %{public}@"
+ "unable to get redacted proxy for redacted appex record: %@"
+ "update container unit 0x%llx"
+ "v24@?0@\"LSPlugInKitProxy\"8@\"NSError\"16"
+ "v52@0:8@\"NSUUID\"16@\"FSNode\"24@\"NSString\"32I40@?<v@?@\"LSPlugInKitProxy\"@\"NSError\">44"
- "-[_LSDReadClient getRedactedAppexRecordForSystemAppexWithUUID:node:bundleIdentifier:platform:completionHandler:]"
- "T@\"LSPlugInKitProxy\",R,D,N"
- "Updating state of volume %llx %{private}@ to mounted with volume ID %llu"

```
