## UARPAssetManagerServiceMobileAsset

> `/System/Library/PrivateFrameworks/UARPAssetManager.framework/XPCServices/UARPAssetManagerServiceMobileAsset.xpc/UARPAssetManagerServiceMobileAsset`

```diff

-1338.60.22.0.0
-  __TEXT.__text: 0xb62c
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_stubs: 0x1aa0
-  __TEXT.__objc_methlist: 0xac4
-  __TEXT.__objc_classname: 0x202
-  __TEXT.__objc_methname: 0x1b26
-  __TEXT.__objc_methtype: 0x569
-  __TEXT.__cstring: 0xde1
-  __TEXT.__oslogstring: 0xf37
-  __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__unwind_info: 0x2e0
-  __DATA_CONST.__auth_got: 0x238
+1338.80.29.0.0
+  __TEXT.__text: 0xce70
+  __TEXT.__auth_stubs: 0x460
+  __TEXT.__objc_stubs: 0x1bc0
+  __TEXT.__objc_methlist: 0xc44
+  __TEXT.__objc_classname: 0x25b
+  __TEXT.__objc_methname: 0x1d46
+  __TEXT.__objc_methtype: 0x5b8
+  __TEXT.__cstring: 0xf81
+  __TEXT.__oslogstring: 0x1047
+  __TEXT.__const: 0x88
+  __TEXT.__gcc_except_tab: 0x50
+  __TEXT.__unwind_info: 0x340
+  __DATA_CONST.__auth_got: 0x240
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__const: 0x338
-  __DATA_CONST.__cfstring: 0xc20
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__cfstring: 0xca0
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x17a0
-  __DATA.__objc_selrefs: 0x7e8
-  __DATA.__objc_ivar: 0xac
-  __DATA.__objc_data: 0x370
+  __DATA.__objc_const: 0x19e0
+  __DATA.__objc_selrefs: 0x840
+  __DATA.__objc_ivar: 0xbc
+  __DATA.__objc_data: 0x410
   __DATA.__data: 0x300
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 471065D0-E0EC-3D73-AD03-7D1B8E49DD79
-  Functions: 254
-  Symbols:   196
-  CStrings:  704
+  UUID: ADF92C6C-A9B6-3A90-965B-1933E2CEFC4A
+  Functions: 287
+  Symbols:   203
+  CStrings:  746
 
Symbols:
+ _OBJC_CLASS_$_UARPAssetManagerServiceMobileAssetPendingSubscription
+ _OBJC_CLASS_$_UARPAssetSubscriptionMobileAssetSU
+ _OBJC_METACLASS_$_UARPAssetManagerServiceMobileAssetPendingSubscription
+ _OBJC_METACLASS_$_UARPAssetSubscriptionMobileAssetSU
+ _compareOSVersion
+ _mobileAssetNewerThanRestoreVersion
+ _mobileAssetPrefixForSubscription
+ _objc_retain_x5
- _mobileAssetPrefixForAppleModelNumber
CStrings:
+ "%s: Asset version %@ not comparable with %@"
+ "%s: Marking entry %@ for deletion for subscription: %@"
+ "%s: OS Version check failed %@ <= %@ <= %@"
+ "%s: Unsubscribing for :%@"
+ "-[UARPAssetManagerServiceAssetCache assetExpirationTime:]"
+ "-[UARPAssetManagerServiceAssetCache subscriptionSupportsExpirationTime:]"
+ "-[UARPAssetManagerServiceAssetCache unsubscribeForAsset:]_block_invoke"
+ "-[UARPAssetManagerServiceMobileAsset unsubscribeForAsset:]_block_invoke"
+ "<%@: %@ asyncUpdate=%d>"
+ "<%@: modelNumber=%@, hwFusing=%@ assetLocation=%@ domain=%@>"
+ "<%@: modelNumber=%@, hwFusing=%@ assetLocation=%@/%u activeVersion=%@/%u variant=%u force=%u domain=%@>"
+ "@\"UARPAssetSubscriptionMobileAsset\""
+ "@28@0:8@16B24"
+ "@56@0:8@16@24@32@40B48B52"
+ "Auto update for subscription disabled %@"
+ "Found %{public}@, but it is older than subscription %{public}@"
+ "T@\"NSString\",R,V_activeVersion"
+ "T@\"UARPAssetSubscriptionMobileAsset\",R,V_subscription"
+ "TB,R,V_asyncUpdate"
+ "TB,R,V_internalVersion"
+ "TB,V_forceInstall"
+ "TB,V_internalVariant"
+ "TB,V_softwareUpdateDefaultAssetAudience"
+ "UARPAssetManagerServiceMobileAssetPendingSubscription"
+ "UARPAssetSubscriptionMobileAssetSU"
+ "_activeVersion"
+ "_asyncUpdate"
+ "_forceInstall"
+ "_internalVariant"
+ "_internalVersion"
+ "_softwareUpdateDefaultAssetAudience"
+ "activeVersion"
+ "assetExpirationTime:"
+ "asyncUpdate"
+ "autoUpdateEnabledForSubscription:"
+ "checkForAssetUpdate:"
+ "checkForUpdate:"
+ "d24@0:8@16"
+ "forceInstall"
+ "initWithAppleModelNumber:hwFusing:domain:activeVersion:internalVersion:internalVariant:"
+ "initWithSubscription:asyncUpdate:"
+ "internalVariant"
+ "internalVersion"
+ "mobileAssetNewerThanRestoreVersion"
+ "setForceInstall:"
+ "setInternalVariant:"
+ "setSoftwareUpdateDefaultAssetAudience:"
+ "softwareUpdateDefaultAssetAudience"
+ "suDefaultAssetAudience"
+ "subscriptionSupportsExpirationTime:"
+ "unsubscribeForAsset:"
- "-[UARPAssetManagerServiceAssetCache assetExpirationTime]"
- "<%@: modelNumber=%@, hwFusing=%@ assetLocation=%@ internal/su=%u/%u domain=%@>"
- "A2525"
- "TB,V_internalAsset"
- "TB,V_softwareUpdateAsset"
- "_internalAsset"
- "_outstandingAsyncAssetSubscriptions"
- "_softwareUpdateAsset"
- "assetExpirationTime"
- "checkForUpdate"
- "d16@0:8"
- "internalAsset"
- "setInternalAsset:"
- "setSoftwareUpdateAsset:"
- "softwareUpdateAsset"
- "suAsset"

```
