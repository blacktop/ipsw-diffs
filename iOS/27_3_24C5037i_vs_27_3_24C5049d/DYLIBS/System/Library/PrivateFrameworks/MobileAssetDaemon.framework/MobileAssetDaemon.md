## MobileAssetDaemon

> `/System/Library/PrivateFrameworks/MobileAssetDaemon.framework/MobileAssetDaemon`

```diff

-2215.60.7.0.0
-  __TEXT.__text: 0x25f050
-  __TEXT.__objc_methlist: 0x12e2c
+2215.60.11.0.0
+  __TEXT.__text: 0x25fd30
+  __TEXT.__objc_methlist: 0x12e54
   __TEXT.__const: 0x157a
-  __TEXT.__cstring: 0x3ffc7
-  __TEXT.__oslogstring: 0x5b60d
-  __TEXT.__gcc_except_tab: 0xd5b4
+  __TEXT.__cstring: 0x400b7
+  __TEXT.__oslogstring: 0x5b90d
+  __TEXT.__gcc_except_tab: 0xd63c
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__constg_swiftt: 0xf0
   __TEXT.__swift5_typeref: 0x146

   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24
-  __TEXT.__unwind_info: 0x5a68
+  __TEXT.__unwind_info: 0x5a78
   __TEXT.__eh_frame: 0x10c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3230
+  __DATA_CONST.__const: 0x32a8
   __DATA_CONST.__objc_classlist: 0x498
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb060
+  __DATA_CONST.__objc_selrefs: 0xb080
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x1048
   __DATA_CONST.__got: 0x12a0
   __AUTH_CONST.__const: 0x10c0
-  __AUTH_CONST.__cfstring: 0x335a0
+  __AUTH_CONST.__cfstring: 0x336e0
   __AUTH_CONST.__objc_const: 0x191d8
   __AUTH_CONST.__objc_arrayobj: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x13c8
   __AUTH_CONST.__objc_dictobj: 0x2d0
-  __AUTH_CONST.__auth_got: 0x1238
+  __AUTH_CONST.__auth_got: 0x1240
   __AUTH.__objc_data: 0x8c8
   __AUTH.__data: 0xc0
   __DATA.__objc_ivar: 0x1834

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7344
-  Symbols:   11526
-  CStrings:  11107
+  Functions: 7349
+  Symbols:   11532
+  CStrings:  11122
 
Symbols:
+ +[MADAutoAssetAuthorizationPolicy _accessibleAssetTypesContainSoftwareUpdateAssetType:]
+ +[MADAutoAssetAuthorizationPolicy _assetTypes:authorizedForAccessibleAssetTypes:]
+ +[MADAutoAssetAuthorizationPolicy authorizationAssetTypesFromMessage:alreadyOnStateQueue:]
+ +[MADAutoAssetSecure isPersonalized:forDescriptor:]
+ _IOServiceGetMatchingServices
+ __copyPCIID
CStrings:
+ "%@:isPersonalized"
+ "; the stage-target-all sentinel needs a software-update asset type"
+ "IOPCIDevice"
+ "Loaded built-in MobileAssetDaemon_Framework Nov 10 2026 05:21:44"
+ "MAAutoAssetStage-target-all-asset-types"
+ "RegionCodeCompatibilityVersion"
+ "VMAICapability"
+ "VMAICapabilityPreference"
+ "device-id"
+ "pvane"
+ "pvcoreai"
+ "vendor-id"
+ "{DecideNeedPersonalize} [singleton] newer asset-version already personalized, not personalizing older | assetType:%{public}@ | assetSpecifier:%{public}@ | assetVersion:%{public}@ | personalizedVersion:%{public}@"
+ "{_assetTypes:authorizedForAccessibleAssetTypes:} accessible-asset-types entitlement is %{public}@, expected an array | assetType:%{public}@"
+ "{_assetTypes:authorizedForAccessibleAssetTypes:} asset type not covered by accessible-asset-types entitlement (exact entry or com.apple.MobileAsset.<prefix>.* wildcard)%{public}@ | assetType:%{public}@, accessibleAssetTypes:%{public}@"
+ "{authorizationAssetTypesFromMessage} Found asset types: %{public}@, for message: %{public}@"
+ "{authorizationAssetTypesFromMessage} Found multiple asset types (not formally supported): %{public}@, for message: %{public}@, authorizing all of them"
+ "{isConnection:authorizedForMessage:}(%{public}@) Client does not have all requested asset types: %{public}@ (found: %{public}@)"
+ "{isConnection:authorizedForMessage:}(%{public}@) Ignoring bypass entitlement of unexpected type: %{public}@ (expected a BOOL or a string)"
- "Loaded built-in MobileAssetDaemon_Framework Oct 24 2026 03:42:45"
- "{authorizationAssetTypeFromMessage} Found asset type: %{public}@, for message: %{public}@"
- "{authorizationAssetTypeFromMessage} Found multiple asset types: %{public}@, for message: %{public}@, using first asset type found"
- "{isConnection:authorizedForMessage:}(%{public}@) Client does not have requested asset type: %@ (found: %@)"
```
