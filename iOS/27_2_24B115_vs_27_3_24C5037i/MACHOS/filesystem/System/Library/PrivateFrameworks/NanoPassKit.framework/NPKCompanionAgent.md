## NPKCompanionAgent

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1355.1.0.0.0
-  __TEXT.__text: 0x4221c
+1355.2.5.0.0
+  __TEXT.__text: 0x4388c
   __TEXT.__auth_stubs: 0xd90
-  __TEXT.__objc_stubs: 0x7e00
-  __TEXT.__objc_methlist: 0x35f8
+  __TEXT.__objc_stubs: 0x7f80
+  __TEXT.__objc_methlist: 0x3668
   __TEXT.__const: 0x128
-  __TEXT.__gcc_except_tab: 0x1060
-  __TEXT.__cstring: 0x28bc
-  __TEXT.__objc_methname: 0xc725
-  __TEXT.__oslogstring: 0x9e4c
+  __TEXT.__gcc_except_tab: 0x10b0
+  __TEXT.__cstring: 0x292c
+  __TEXT.__objc_methname: 0xca03
+  __TEXT.__oslogstring: 0xa1ce
   __TEXT.__objc_classname: 0x6c3
-  __TEXT.__objc_methtype: 0x3629
+  __TEXT.__objc_methtype: 0x36ad
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x11d0
-  __DATA_CONST.__const: 0x1f48
-  __DATA_CONST.__cfstring: 0x1200
+  __TEXT.__unwind_info: 0x1218
+  __DATA_CONST.__const: 0x1fc0
+  __DATA_CONST.__cfstring: 0x1220
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__auth_got: 0x6d8
-  __DATA_CONST.__got: 0x6f0
-  __DATA.__objc_const: 0x5c60
-  __DATA.__objc_selrefs: 0x2928
-  __DATA.__objc_ivar: 0x1c4
+  __DATA_CONST.__got: 0x6f8
+  __DATA.__objc_const: 0x5cd0
+  __DATA.__objc_selrefs: 0x2990
+  __DATA.__objc_ivar: 0x1cc
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0xc68
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1164
+  Functions: 1183
   Symbols:   453
-  CStrings:  2766
+  CStrings:  2796
 
Symbols:
+ _OBJC_CLASS_$_NPKProtoCompanionPrearmTrustKeyMaterialResponse
- _OBJC_CLASS_$_NSConstantDoubleNumber
CStrings:
+ "@\"NSString\"24@0:8@\"NPDCompanionMaintenanceService\"16"
+ "@40@0:8@16@24d32"
+ "Error: Pass %@ in the gizmo database is missing its pass type identifier; rebuilding it from the companion payment pass database"
+ "Error: Unable to rebuild gizmo database pass %@: companion payment pass database has no usable copy (found pass?: %@)"
+ "Error: [BarcodeEvent] Failed to send metadataResponse"
+ "Error: [CompanionPrearmTrust] Failed to send pre-arm trust response for response identifier %@"
+ "Error: [CompanionPrearmTrust] No active remote device ID; cannot generate pre-arm trust key material"
+ "No active paired device session"
+ "Notice: Rebuilt gizmo database pass %@ from the companion payment pass database"
+ "Notice: [CompanionPrearmTrust] Received pre-arm trust key material request for response identifier %@"
+ "Notice: [CompanionPrearmTrust] Requesting pre-arm trust key material from passd"
+ "Notice: [CompanionPrearmTrust] Resolved deviceID %{private}@ for response identifier %@"
+ "Notice: [CompanionPrearmTrust] Sending pre-arm trust response for response identifier %@. Key material: %lu bytes, error: %@"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_companionPassQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
+ "_addPassToDatabaseAndPrepareForTransmissionToGizmo:isUpdate:preservingDeviceOwnedSettings:withCompletion:"
+ "_companionPassQueue"
+ "_handleCompanionPrearmTrustKeyMaterialRequest:"
+ "_rebuildGizmoDatabasePassWithUniqueID:settings:completion:"
+ "_sendMaintenanceResponseWithData:incomingProtobuf:timeout:"
+ "com.apple.NPKCompanionAgent.companionPass"
+ "companionMaintenanceServiceRemoteDeviceID:"
+ "companionPassQueue"
+ "generateIdentityPrearmTrustKeyMaterialForDeviceID:completion:"
+ "getPassLocalizedStringsForKeys:uniqueID:handler:"
+ "initWithCompanionPaymentPassDatabase:queue:"
+ "keyMaterialData"
+ "localizedStrings:completion:"
+ "npkPassWithUniqueID:queue:completion:"
+ "npkPassesOfType:queue:completion:"
+ "npkSanitizePass:queue:completion:"
+ "remoteDeviceID"
+ "setCompanionPassQueue:"
+ "setKeyMaterialData:"
+ "setSettingsWithoutUpdatingDataAccessor:"
+ "v16@?0@\"NSDictionary\"8"
+ "v24@?0@\"PKAuxiliaryCapabilityRequirementKeyMaterial\"8@\"NSError\"16"
+ "v40@0:8@\"NSSet\"16@\"NSString\"24@?<v@?@\"NSDictionary\">32"
+ "v40@0:8Q16@24@?32"
- "@24@0:8Q16"
- "Error: [BarcodeEvent] Failed to send message with identifier %@ due to %@"
- "_sendBarcodeEventResponseWithData:incomingProtobuf:"
- "localizedString:"
- "npkPassWithUniqueID:"
- "npkPassesOfType:"
- "npkSanitizePass:"
- "v24@?0@\"PKBeacon\"8^B16"
- "v32@?0@\"PKLocation\"8Q16^B24"
```
