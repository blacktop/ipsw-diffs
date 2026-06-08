## BiomeSync

> `/System/Library/PrivateFrameworks/BiomeSync.framework/BiomeSync`

```diff

-209.18.0.0.0
-  __TEXT.__text: 0x33e0
-  __TEXT.__auth_stubs: 0x230
-  __TEXT.__objc_methlist: 0x210
+236.0.2.0.0
+  __TEXT.__text: 0x3bc8
+  __TEXT.__objc_methlist: 0x240
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0xf8
-  __TEXT.__gcc_except_tab: 0x288
+  __TEXT.__cstring: 0x101
+  __TEXT.__gcc_except_tab: 0x2f8
   __TEXT.__oslogstring: 0x63
-  __TEXT.__unwind_info: 0x190
-  __TEXT.__objc_classname: 0x6a
-  __TEXT.__objc_methname: 0x5ca
-  __TEXT.__objc_methtype: 0x191
-  __TEXT.__objc_stubs: 0x4a0
-  __DATA_CONST.__got: 0x58
+  __TEXT.__unwind_info: 0x1b0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x118
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b0
+  __DATA_CONST.__objc_selrefs: 0x1d0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x128
+  __DATA_CONST.__got: 0x58
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x100
-  __AUTH_CONST.__objc_const: 0x2f0
+  __AUTH_CONST.__cfstring: 0x120
+  __AUTH_CONST.__objc_const: 0x300
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x14
   __DATA.__data: 0x180
   __DATA_DIRTY.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D33FB718-A880-3E9C-AC77-62DDC8FED0AF
-  Functions: 58
-  Symbols:   269
-  CStrings:  116
+  UUID: 73C3EA9A-0EDA-347C-BFFD-4A8433C92332
+  Functions: 64
+  Symbols:   293
+  CStrings:  25
 
Symbols:
+ -[BMSyncService cascadeCloudKitSyncForSets:errors:]
+ -[BMSyncService cascadeCloudKitSyncWithErrors:]
+ GCC_except_table45
+ GCC_except_table48
+ _NSClassFromString
+ ___27-[BMSyncService connection]_block_invoke.38
+ ___47-[BMSyncService cascadeCloudKitSyncWithErrors:]_block_invoke
+ ___47-[BMSyncService cascadeCloudKitSyncWithErrors:]_block_invoke_2
+ ___51-[BMSyncService cascadeCloudKitSyncForSets:errors:]_block_invoke
+ ___51-[BMSyncService cascadeCloudKitSyncForSets:errors:]_block_invoke_2
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$cascadeCloudKitSyncForSets:reply:
+ _objc_msgSend$cascadeCloudKitSyncWithReply:
+ _objc_release_x26
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x25
+ _objc_retain_x28
+ _objc_retain_x8
- ___27-[BMSyncService connection]_block_invoke.30
- _objc_retain
CStrings:
+ "CCSet"
- ".cxx_destruct"
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@32@0:8@16^@24"
- "@56@0:8@16@24@32@40q48"
- "B16@0:8"
- "B24@0:8^@16"
- "B32@0:8@16^@24"
- "BMDevice"
- "BMSyncService"
- "BMSyncServiceClientProtocol"
- "BMSyncServiceServerProtocol"
- "NSCoding"
- "NSSecureCoding"
- "T@\"NSString\",R,C,N,V_deviceIdentifier"
- "T@\"NSString\",R,C,N,V_idsDeviceIdentifier"
- "T@\"NSString\",R,C,N,V_model"
- "T@\"NSString\",R,C,N,V_name"
- "TB,R"
- "Tq,R,N,V_platform"
- "_deviceIdentifier"
- "_idsDeviceIdentifier"
- "_model"
- "_name"
- "_platform"
- "_xpcConnection"
- "arrayWithObjects:count:"
- "cascadeRapportSyncWithErrors:"
- "cascadeRapportSyncWithReply:"
- "cloudKitSyncWithErrors:"
- "cloudKitSyncWithReply:"
- "connection"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "description"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "init"
- "initWithCoder:"
- "initWithDeviceIdentifier:idsDeviceIdentifier:name:model:platform:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "invalidate"
- "new"
- "numberWithInteger:"
- "peerInformationWithError:"
- "peerInformationWithReply:"
- "q"
- "q16@0:8"
- "rapportSyncWithErrors:"
- "rapportSyncWithReply:"
- "remoteDevicesForAccount:error:"
- "remoteDevicesForAccount:reply:"
- "remoteDevicesWithError:"
- "remoteDevicesWithReply:"
- "remoteObjectProxyWithErrorHandler:"
- "resume"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setRemoteObjectInterface:"
- "setWithObjects:"
- "stringWithFormat:"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "triggerCloudKitSyncWithError:"
- "triggerCloudKitSyncWithReply:"
- "triggerRapportSyncDeviceIdentifiers:reply:"
- "triggerRapportSyncWithDeviceIdentifiers:error:"
- "triggerRapportSyncWithError:"
- "triggerRapportSyncWithReply:"
- "triggerSyncWithError:"
- "v16@0:8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSArray\">16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v32@0:8@\"BMAccount\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSSet\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@?24"

```
