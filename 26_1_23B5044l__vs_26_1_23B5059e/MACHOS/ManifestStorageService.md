## ManifestStorageService

> `/System/Library/PrivateFrameworks/MobileAsset.framework/XPCServices/ManifestStorageService.xpc/ManifestStorageService`

```diff

-1837.40.40.0.0
-  __TEXT.__text: 0x3118
-  __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_stubs: 0x880
-  __TEXT.__objc_methlist: 0x384
-  __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x8f1
-  __TEXT.__oslogstring: 0x57a
-  __TEXT.__objc_methname: 0xadd
+1837.40.63.0.0
+  __TEXT.__text: 0x3788
+  __TEXT.__auth_stubs: 0x3f0
+  __TEXT.__objc_stubs: 0x8e0
+  __TEXT.__objc_methlist: 0x3a4
+  __TEXT.__const: 0xb0
+  __TEXT.__cstring: 0x919
+  __TEXT.__oslogstring: 0x677
+  __TEXT.__objc_methname: 0xb68
   __TEXT.__objc_classname: 0xb9
-  __TEXT.__objc_methtype: 0x2bc
-  __TEXT.__gcc_except_tab: 0x128
+  __TEXT.__objc_methtype: 0x2f5
+  __TEXT.__gcc_except_tab: 0x12c
   __TEXT.__unwind_info: 0x110
-  __DATA_CONST.__auth_got: 0x1e8
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x100
-  __DATA_CONST.__cfstring: 0xd00
+  __DATA_CONST.__auth_got: 0x208
+  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__const: 0x130
+  __DATA_CONST.__cfstring: 0xd20
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_intobj: 0x240
   __DATA.__objc_const: 0x568
-  __DATA.__objc_selrefs: 0x350
+  __DATA.__objc_selrefs: 0x368
   __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x120

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 460608CD-03C8-3375-8FC2-067A31F8B594
-  Functions: 56
-  Symbols:   103
-  CStrings:  423
+  UUID: 4741675B-52FF-308A-A625-D3F6E9B1A3BA
+  Functions: 61
+  Symbols:   108
+  CStrings:  439
 
Symbols:
+ __image4_trust_evaluation_preflight
+ _image4_environment_copy_nonce_digest
+ _image4_environment_set_callbacks
+ _image4_environment_set_nonce_domain
+ _memcpy
+ _objc_retain_x24
- _objc_retain_x23
CStrings:
+ "%{public}@:<<<<<<<<<<\n%{public}@\n%{public}@:>>>>>>>>>>"
+ "21:36:52"
+ "@44@0:8@16Q24@32B40"
+ "Asset type does not support Darwin: %{public}@"
+ "Asset type does not support code: %{public}@"
+ "Authenticating info plist"
+ "Authenticating live manifest"
+ "B32@0:8@16Q24"
+ "Flashing manifest"
+ "Live manifest trust evaluation failed: %d (%{public}s)"
+ "Sep 28 2025"
+ "Storing manifest (type = %s, stage = %i)"
+ "Successfully authenticated info plist: %{public}@"
+ "Successfully authenticated live manifest"
+ "SupportsLoadableTrustCache"
+ "__authenticateLiveManifest:"
+ "__flashManifest:"
+ "_assetTypeSupported:manifestType:"
+ "_authenticatePlist:manifest:manifestType:result:"
+ "_verifyManifest:manifestType:"
+ "classic"
+ "i32@0:8@16Q24"
+ "i48@0:8@16@24Q32^@40"
+ "storeManifest:manifestType:infoPlist:stage:"
+ "storeManifest:manifestType:infoPlist:stage:completion:"
+ "supportsLoadableTrustCache:"
+ "v52@0:8@\"NSData\"16Q24@\"NSData\"32B40@?<v@?@\"NSError\">44"
+ "v52@0:8@16Q24@32B40@?44"
- "%{public}@:<<<<<<<<<<\n%{public}@%{public}@:>>>>>>>>>>"
- "07:35:03"
- "Asset type is unsupported: %{public}@"
- "Authenticated plist: %{public}@"
- "Sep  5 2025"
- "Storing manifest (stage = %i)"
- "_assetTypeSupported:"
- "_authenticatePlist:manifest:result:"
- "_flashManifest:"
- "i40@0:8@16@24^@32"
- "storeManifest:infoPlist:stage:"
- "storeManifest:infoPlist:stage:completion:"
- "v44@0:8@\"NSData\"16@\"NSData\"24B32@?<v@?@\"NSError\">36"
- "v44@0:8@16@24B32@?36"

```
