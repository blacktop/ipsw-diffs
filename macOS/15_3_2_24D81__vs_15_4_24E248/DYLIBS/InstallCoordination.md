## InstallCoordination

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Versions/A/InstallCoordination`

```diff

-631.80.9.0.0
-  __TEXT.__text: 0x57124
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_methlist: 0x2cdc
+699.100.10.0.0
+  __TEXT.__text: 0x57c3c
+  __TEXT.__auth_stubs: 0x830
+  __TEXT.__objc_methlist: 0x3ba0
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x14f18
-  __TEXT.__gcc_except_tab: 0x16e4
+  __TEXT.__cstring: 0x1510c
+  __TEXT.__gcc_except_tab: 0x16cc
   __TEXT.__oslogstring: 0x1b7
-  __TEXT.__unwind_info: 0x13e8
-  __TEXT.__objc_classname: 0x8ad
-  __TEXT.__objc_methname: 0x96ba
+  __TEXT.__unwind_info: 0x1400
+  __TEXT.__objc_classname: 0x8c2
+  __TEXT.__objc_methname: 0x992c
   __TEXT.__objc_methtype: 0x1f5c
-  __TEXT.__objc_stubs: 0x5580
-  __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0x750
-  __DATA_CONST.__objc_classlist: 0x170
+  __TEXT.__objc_stubs: 0x56a0
+  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__const: 0x768
+  __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c50
-  __AUTH_CONST.__auth_got: 0x430
+  __DATA_CONST.__objc_selrefs: 0x1d38
+  __AUTH_CONST.__auth_got: 0x428
   __AUTH_CONST.__const: 0x1670
-  __AUTH_CONST.__cfstring: 0x4fe0
-  __AUTH_CONST.__objc_const: 0xbde8
-  __AUTH.__objc_data: 0xe60
+  __AUTH_CONST.__cfstring: 0x5120
+  __AUTH_CONST.__objc_const: 0xa708
+  __AUTH.__objc_data: 0xeb0
   __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0x298
-  __DATA.__objc_superrefs: 0x108
-  __DATA.__objc_ivar: 0x19c
+  __DATA.__objc_superrefs: 0x110
+  __DATA.__objc_ivar: 0x1b4
   __DATA.__data: 0xa90
   __DATA.__bss: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 19C233C4-62EB-3733-9C87-259184302A11
-  Functions: 1480
-  Symbols:   3741
-  CStrings:  3791
+  UUID: C6F071AB-C178-33B1-B0F9-3363BCF2FC1C
+  Functions: 1507
+  Symbols:   3803
+  CStrings:  3840
 
Symbols:
+ +[IXAppInstallCoordinator defaultAppMetadataForAppIdentity:completion:]
+ +[IXAppInstallCoordinator defaultAppMetadataForAppIdentity:error:]
+ +[IXAppInstallCoordinator defaultAppMetadataListWithCompletion:]
+ +[IXAppInstallCoordinator defaultAppMetadataListWithError:]
+ +[IXAppInstallCoordinator(IXDemoteToPlaceholder) _demoteAppToPlaceholderWithApplicationIdentity:forReason:waitForDeletion:ignoreRemovability:returnEarlyForTesting:completion:].cold.1
+ +[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:withTargetDirectory:orTargetBundle:consumeSource:shouldOverrideGatekeeper:options:completion:].cold.1
+ +[IXDefaultAppMetadata supportsSecureCoding]
+ -[IXAppInstallCoordinator internalQueue].cold.1
+ -[IXAppInstallCoordinator observerCalloutQueue].cold.1
+ -[IXDefaultAppMetadata .cxx_destruct]
+ -[IXDefaultAppMetadata appType]
+ -[IXDefaultAppMetadata copyWithZone:]
+ -[IXDefaultAppMetadata description]
+ -[IXDefaultAppMetadata dictionaryRepresentation]
+ -[IXDefaultAppMetadata encodeWithCoder:]
+ -[IXDefaultAppMetadata hash]
+ -[IXDefaultAppMetadata identity]
+ -[IXDefaultAppMetadata initWithAppIdentity:appType:offloadAnswer:]
+ -[IXDefaultAppMetadata initWithCoder:]
+ -[IXDefaultAppMetadata isEqual:]
+ -[IXDefaultAppMetadata offloadAnswer]
+ -[IXPlaceholderAttributes accentColorName]
+ -[IXPlaceholderAttributes bundleShortVersionString]
+ -[IXPlaceholderAttributes setAccentColorName:]
+ -[IXPlaceholderAttributes setBundleShortVersionString:]
+ -[IXPlaceholderAttributes setUiLaunchScreen:]
+ -[IXPlaceholderAttributes uiLaunchScreen]
+ GCC_except_table143
+ GCC_except_table151
+ GCC_except_table158
+ GCC_except_table165
+ GCC_except_table172
+ GCC_except_table179
+ GCC_except_table182
+ GCC_except_table185
+ GCC_except_table188
+ GCC_except_table191
+ GCC_except_table194
+ GCC_except_table197
+ GCC_except_table200
+ GCC_except_table203
+ GCC_except_table206
+ GCC_except_table209
+ GCC_except_table212
+ GCC_except_table215
+ GCC_except_table218
+ GCC_except_table221
+ GCC_except_table224
+ GCC_except_table227
+ GCC_except_table230
+ GCC_except_table233
+ GCC_except_table236
+ GCC_except_table239
+ GCC_except_table242
+ GCC_except_table245
+ GCC_except_table248
+ GCC_except_table251
+ GCC_except_table254
+ GCC_except_table257
+ GCC_except_table260
+ GCC_except_table263
+ GCC_except_table266
+ GCC_except_table269
+ GCC_except_table276
+ GCC_except_table279
+ GCC_except_table282
+ GCC_except_table285
+ GCC_except_table288
+ GCC_except_table291
+ GCC_except_table294
+ GCC_except_table299
+ GCC_except_table302
+ GCC_except_table305
+ GCC_except_table308
+ GCC_except_table311
+ GCC_except_table314
+ GCC_except_table317
+ GCC_except_table324
+ GCC_except_table331
+ GCC_except_table345
+ GCC_except_table354
+ GCC_except_table357
+ GCC_except_table360
+ GCC_except_table363
+ GCC_except_table370
+ GCC_except_table409
+ GCC_except_table412
+ GCC_except_table421
+ GCC_except_table424
+ GCC_except_table427
+ GCC_except_table434
+ GCC_except_table437
+ IXFrameworkBundle.cold.1
+ OBJC_IVAR_$_IXDefaultAppMetadata._appType
+ OBJC_IVAR_$_IXDefaultAppMetadata._identity
+ OBJC_IVAR_$_IXDefaultAppMetadata._offloadAnswer
+ OBJC_IVAR_$_IXPlaceholderAttributes._accentColorName
+ OBJC_IVAR_$_IXPlaceholderAttributes._bundleShortVersionString
+ OBJC_IVAR_$_IXPlaceholderAttributes._uiLaunchScreen
+ _OBJC_CLASS_$_IXDefaultAppMetadata
+ _OBJC_METACLASS_$_IXDefaultAppMetadata
+ _OUTLINED_FUNCTION_5
+ __58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.749
+ __58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke_2.750
+ __OBJC_$_CLASS_METHODS_IXDefaultAppMetadata
+ __OBJC_$_CLASS_PROP_LIST_IXDefaultAppMetadata
+ __OBJC_$_INSTANCE_METHODS_IXDefaultAppMetadata
+ __OBJC_$_INSTANCE_VARIABLES_IXDefaultAppMetadata
+ __OBJC_$_PROP_LIST_IXDefaultAppMetadata
+ __OBJC_CLASS_PROTOCOLS_$_IXDefaultAppMetadata
+ __OBJC_CLASS_RO_$_IXDefaultAppMetadata
+ __OBJC_METACLASS_RO_$_IXDefaultAppMetadata
+ __block_literal_global.752
+ __block_literal_global.761
+ __block_literal_global.763
+ __kCFBundleShortVersionStringKey
+ _objc_msgSend$accentColorName
+ _objc_msgSend$appType
+ _objc_msgSend$bundleShortVersionString
+ _objc_msgSend$initWithAppIdentity:appType:offloadAnswer:
+ _objc_msgSend$offloadAnswer
+ _objc_msgSend$setAccentColorName:
+ _objc_msgSend$setBundleShortVersionString:
+ _objc_msgSend$setUiLaunchScreen:
+ _objc_msgSend$uiLaunchScreen
- GCC_except_table139
- GCC_except_table147
- GCC_except_table154
- GCC_except_table161
- GCC_except_table168
- GCC_except_table171
- GCC_except_table178
- GCC_except_table181
- GCC_except_table184
- GCC_except_table187
- GCC_except_table190
- GCC_except_table193
- GCC_except_table196
- GCC_except_table199
- GCC_except_table202
- GCC_except_table205
- GCC_except_table208
- GCC_except_table211
- GCC_except_table214
- GCC_except_table217
- GCC_except_table220
- GCC_except_table223
- GCC_except_table226
- GCC_except_table229
- GCC_except_table232
- GCC_except_table235
- GCC_except_table238
- GCC_except_table241
- GCC_except_table244
- GCC_except_table247
- GCC_except_table250
- GCC_except_table253
- GCC_except_table256
- GCC_except_table259
- GCC_except_table262
- GCC_except_table265
- GCC_except_table268
- GCC_except_table275
- GCC_except_table278
- GCC_except_table281
- GCC_except_table284
- GCC_except_table287
- GCC_except_table290
- GCC_except_table295
- GCC_except_table298
- GCC_except_table301
- GCC_except_table304
- GCC_except_table307
- GCC_except_table310
- GCC_except_table313
- GCC_except_table320
- GCC_except_table327
- GCC_except_table341
- GCC_except_table346
- GCC_except_table353
- GCC_except_table356
- GCC_except_table359
- GCC_except_table366
- GCC_except_table405
- GCC_except_table408
- GCC_except_table413
- GCC_except_table416
- GCC_except_table423
- GCC_except_table426
- GCC_except_table433
- __58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.745
- __58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke_2.746
- __block_literal_global.748
- __block_literal_global.757
- __block_literal_global.759
- _strcmp
CStrings:
+ "+[IXAppInstallCoordinator defaultAppMetadataForAppIdentity:completion:]"
+ "+[IXAppInstallCoordinator defaultAppMetadataForAppIdentity:error:]"
+ "+[IXAppInstallCoordinator defaultAppMetadataListWithCompletion:]"
+ "+[IXAppInstallCoordinator defaultAppMetadataListWithError:]"
+ "Failed to stage background update."
+ "IXAppCoordinationStateReadyForStaging"
+ "IXAppCoordinationStateStagingPending"
+ "IXDefaultAppMetadata"
+ "NSAccentColorName"
+ "T@\"IXApplicationIdentity\",R,N,V_identity"
+ "T@\"NSDictionary\",C,N,V_uiLaunchScreen"
+ "T@\"NSString\",C,N,V_accentColorName"
+ "T@\"NSString\",C,N,V_bundleShortVersionString"
+ "TQ,R,N,V_appType"
+ "TQ,R,N,V_offloadAnswer"
+ "UILaunchScreen"
+ "_accentColorName"
+ "_appType"
+ "_bundleShortVersionString"
+ "_offloadAnswer"
+ "_uiLaunchScreen"
+ "accentColorName"
+ "appType"
+ "bundleShortVersionString"
+ "com.apple.parallelpatcharchive."
+ "defaultAppMetadataForAppIdentity:completion:"
+ "defaultAppMetadataForAppIdentity:error:"
+ "defaultAppMetadataListWithCompletion:"
+ "defaultAppMetadataListWithError:"
+ "initWithAppIdentity:appType:offloadAnswer:"
+ "offloadAnswer"
+ "setAccentColorName:"
+ "setBundleShortVersionString:"
+ "setUiLaunchScreen:"
+ "uiLaunchScreen"
- "PPBundleMetadata"

```
