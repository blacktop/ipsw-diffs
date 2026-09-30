## AppStoreDaemon

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon`

```diff

-12.0.54.2.1
-  __TEXT.__text: 0x819c4
+12.0.60.1.1
+  __TEXT.__text: 0x82570
   __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0xaadc
+  __TEXT.__objc_methlist: 0xab64
   __TEXT.__const: 0x2d0
   __TEXT.__dlopen_cstrs: 0xb1
-  __TEXT.__cstring: 0x52a5
+  __TEXT.__cstring: 0x52e7
   __TEXT.__constg_swiftt: 0x54
   __TEXT.__swift5_typeref: 0x26
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_fieldmd: 0x28
-  __TEXT.__oslogstring: 0x46ac
+  __TEXT.__oslogstring: 0x478a
   __TEXT.__gcc_except_tab: 0x1044
-  __TEXT.__unwind_info: 0x2700
+  __TEXT.__unwind_info: 0x2710
   __TEXT.__objc_classname: 0x18ac
-  __TEXT.__objc_methname: 0x13fca
+  __TEXT.__objc_methname: 0x142ac
   __TEXT.__objc_methtype: 0x348f
-  __TEXT.__objc_stubs: 0x8580
+  __TEXT.__objc_stubs: 0x8680
   __DATA_CONST.__got: 0x620
-  __DATA_CONST.__const: 0x2740
+  __DATA_CONST.__const: 0x2768
   __DATA_CONST.__objc_classlist: 0x5d8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4340
+  __DATA_CONST.__objc_selrefs: 0x43a0
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x488
   __DATA_CONST.__objc_arraydata: 0xc8
   __AUTH_CONST.__auth_got: 0x600
   __AUTH_CONST.__const: 0x810
-  __AUTH_CONST.__cfstring: 0x66c0
-  __AUTH_CONST.__objc_const: 0x15570
+  __AUTH_CONST.__cfstring: 0x6780
+  __AUTH_CONST.__objc_const: 0x15638
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1720
-  __DATA.__objc_ivar: 0xd0c
+  __DATA.__objc_ivar: 0xd1c
   __DATA.__data: 0x18f8
   __DATA.__bss: 0x310
   __DATA_DIRTY.__objc_ivar: 0x19c

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9DA14A7B-C800-3924-88BC-21A1093C0270
-  Functions: 4308
-  Symbols:   13145
-  CStrings:  6282
+  UUID: 24E2FB8D-C1CF-3B15-9A2E-F4ACBB794AB1
+  Functions: 4322
+  Symbols:   13186
+  CStrings:  6317
 
Symbols:
+ -[ASDApp updateCodedPropertiesFromApp:]
+ -[ASDArcadeService recordAppLaunchForBundleID:additionalMetrics:replyHandler:]
+ -[ASDPurchase forceAskToBuyReason]
+ -[ASDPurchase setForceAskToBuyReason:]
+ -[ASDPurchaseHistoryApp appIconCompatibleArtworkURLString]
+ -[ASDPurchaseHistoryApp circularAppIconCompatibleArtworkURLString]
+ -[ASDPurchaseHistoryApp setAppIconCompatibleArtworkURLString:]
+ -[ASDPurchaseHistoryApp setCircularAppIconCompatibleArtworkURLString:]
+ -[ASDSoftwareUpdate installerPackagingType]
+ -[ASDSoftwareUpdate setInstallerPackagingType:]
+ _OBJC_IVAR_$_ASDPurchase._forceAskToBuyReason
+ _OBJC_IVAR_$_ASDPurchaseHistoryApp._appIconCompatibleArtworkURLString
+ _OBJC_IVAR_$_ASDPurchaseHistoryApp._circularAppIconCompatibleArtworkURLString
+ _OBJC_IVAR_$_ASDSoftwareUpdate._installerPackagingType
+ ___78-[ASDArcadeService recordAppLaunchForBundleID:additionalMetrics:replyHandler:]_block_invoke
+ ___78-[ASDArcadeService recordAppLaunchForBundleID:additionalMetrics:replyHandler:]_block_invoke.3
+ ___78-[ASDArcadeService recordAppLaunchForBundleID:additionalMetrics:replyHandler:]_block_invoke_2
+ ___78-[ASDArcadeService recordAppLaunchForBundleID:additionalMetrics:replyHandler:]_block_invoke_2.4
+ ___block_descriptor_64_e8_32s40s48s56bs_e68_v24?0"<ASDOcelotServiceProtocol><NSXPCProxyCreating>"8"NSError"16ls32l8s56l8s40l8s48l8
+ _objc_msgSend$appIconCompatibleArtworkURLString
+ _objc_msgSend$circularAppIconCompatibleArtworkURLString
+ _objc_msgSend$installerPackagingType
+ _objc_msgSend$rawUpdateData
+ _objc_msgSend$recordLaunchForBundleID:additionalMetrics:replyHandler:
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$updateCodedPropertiesFromApp:
+ _objc_msgSend$updateInstallDate
CStrings:
+ " forceATBReason: %ld"
+ "AF"
+ "AG"
+ "InstallerPackagingType"
+ "T@\"NSString\",C,V_appIconCompatibleArtworkURLString"
+ "T@\"NSString\",C,V_circularAppIconCompatibleArtworkURLString"
+ "Tq,N,GinstallerPackagingType,V_installerPackagingType"
+ "Tq,N,V_forceAskToBuyReason"
+ "[%@]: bundleID: %@ accountID: %@ bagKey: %@ buyParams: %@ extensionsToEnable: %lu isBackgroundUpdate: %d isRedownload: %d isUpdate: %d isPreorder: %d itemID: %@ itemName: %@ purchaseID: %lld vendorName: %@ softwarePlatform: %ld remoteDownloadIdentifiers: %@"
+ "[%{public}@] recordLaunch failed with error: %{public}@"
+ "[%{public}@] recordLaunch failed with xpc error: %{public}@"
+ "[%{public}@]: Forcing progress to complete after receiving update that had no remote progress: %{public}@"
+ "]"
+ "_appIconCompatibleArtworkURLString"
+ "_circularAppIconCompatibleArtworkURLString"
+ "_forceAskToBuyReason"
+ "_installerPackagingType"
+ "appIconCompatibleArtworkURLString"
+ "circularAppIconCompatibleArtworkURLString"
+ "forceATBReason"
+ "forceAskToBuyReason"
+ "installerPackagingType"
+ "recordAppLaunchForBundleID:additionalMetrics:replyHandler:"
+ "recordLaunchForBundleID:additionalMetrics:replyHandler:"
+ "setAppIconCompatibleArtworkURLString:"
+ "setCircularAppIconCompatibleArtworkURLString:"
+ "setForceAskToBuyReason:"
+ "setInstallerPackagingType:"
+ "stringByAppendingFormat:"
+ "updateCodedPropertiesFromApp:"
- "[%@]: bundleID: %@ accountID: %@ bagKey: %@ buyParams: %@ extensionsToEnable: %lu isBackgroundUpdate: %d isRedownload: %d isUpdate: %d isPreorder: %d itemID: %@ itemName: %@ purchaseID: %lld vendorName: %@ softwarePlatform: %ld remoteDownloadIdentifiers: %@]"

```
