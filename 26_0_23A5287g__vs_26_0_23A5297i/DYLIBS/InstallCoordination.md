## InstallCoordination

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination`

```diff

-769.0.0.0.0
-  __TEXT.__text: 0x69b78
+772.0.0.0.0
+  __TEXT.__text: 0x69f90
   __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x4158
+  __TEXT.__objc_methlist: 0x4170
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0xe852
-  __TEXT.__oslogstring: 0x79a0
-  __TEXT.__gcc_except_tab: 0x1d80
+  __TEXT.__cstring: 0xe97e
+  __TEXT.__oslogstring: 0x7ab0
+  __TEXT.__gcc_except_tab: 0x1db4
+  __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x17e8
   __TEXT.__objc_classname: 0x8ae
-  __TEXT.__objc_methname: 0xad37
+  __TEXT.__objc_methname: 0xad64
   __TEXT.__objc_methtype: 0x23eb
-  __TEXT.__objc_stubs: 0x6080
+  __TEXT.__objc_stubs: 0x60c0
   __DATA_CONST.__got: 0x3f0
   __DATA_CONST.__const: 0x1bc0
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2090
+  __DATA_CONST.__objc_selrefs: 0x20a0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x108
   __AUTH_CONST.__auth_got: 0x5c0
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x5a20
-  __AUTH_CONST.__objc_const: 0xadb0
+  __AUTH_CONST.__cfstring: 0x5ac0
+  __AUTH_CONST.__objc_const: 0xadc0
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH.__objc_data: 0xf0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D1F42976-7B8F-31BA-B07E-CDC9E0011C32
-  Functions: 1961
-  Symbols:   6492
-  CStrings:  4162
+  UUID: 8E0D1253-C353-3D90-B92F-8780C5C9DD6C
+  Functions: 1967
+  Symbols:   6512
+  CStrings:  4176
 
Symbols:
+ -[IXOwnedDataPromise description]
+ -[IXPlaceholder _doInitWithSpecification:error:].cold.5
+ -[IXPlaceholder _doInitWithSpecification:error:].cold.6
+ -[IXPlaceholder _doInitWithSpecification:error:].cold.7
+ -[NSString(InstallCoordinationAdditions) containsEmbeddedNULLCharacter]
+ GCC_except_table21
+ ___31-[IXPlaceholder hasIconPromise]_block_invoke.248
+ ___35-[IXPlaceholder setMetadata:error:]_block_invoke.326
+ ___35-[IXPlaceholder setSinfData:error:]_block_invoke.337
+ ___38-[IXPlaceholder iconPromiseWithError:]_block_invoke.236
+ ___38-[IXPlaceholder iconPromiseWithError:]_block_invoke.236.cold.1
+ ___38-[IXPlaceholder iconPromiseWithError:]_block_invoke.236.cold.2
+ ___38-[IXPlaceholder setIconPromise:error:]_block_invoke.235
+ ___39-[IXPlaceholder hasEntitlementsPromise]_block_invoke.290
+ ___40-[IXPlaceholder hasIconResourcesPromise]_block_invoke.268
+ ___44-[IXPlaceholder hasInfoPlistLoctablePromise]_block_invoke.296
+ ___45-[IXPlaceholder hasPlugInPlaceholderPromises]_block_invoke.315
+ ___46-[IXPlaceholder entitlementsPromiseWithError:]_block_invoke.286
+ ___46-[IXPlaceholder entitlementsPromiseWithError:]_block_invoke.286.cold.1
+ ___46-[IXPlaceholder entitlementsPromiseWithError:]_block_invoke.286.cold.2
+ ___46-[IXPlaceholder setEntitlementsPromise:error:]_block_invoke.285
+ ___48-[IXPlaceholder _doInitWithSpecification:error:]_block_invoke.226
+ ___49-[IXPlaceholder infoPlistLocalizationsWithError:]_block_invoke.280
+ ___49-[IXPlaceholder setInfoPlistLocalizations:error:]_block_invoke.279
+ ___51-[IXPlaceholder infoPlistLoctablePromiseWithError:]_block_invoke.292
+ ___51-[IXPlaceholder infoPlistLoctablePromiseWithError:]_block_invoke.292.cold.1
+ ___51-[IXPlaceholder infoPlistLoctablePromiseWithError:]_block_invoke.292.cold.2
+ ___51-[IXPlaceholder setConfigurationCompleteWithError:]_block_invoke.316
+ ___51-[IXPlaceholder setInfoPlistLoctablePromise:error:]_block_invoke.291
+ ___58-[IXPlaceholder appExtensionPlaceholderPromisesWithError:]_block_invoke.307
+ ___58-[IXPlaceholder setAppExtensionPlaceholderPromises:error:]_block_invoke.306
+ ___64-[IXPlaceholder iconResourcesPromiseWithInfoPlistContent:error:]_block_invoke.260
+ ___64-[IXPlaceholder iconResourcesPromiseWithInfoPlistContent:error:]_block_invoke.260.cold.1
+ ___64-[IXPlaceholder iconResourcesPromiseWithInfoPlistContent:error:]_block_invoke.260.cold.2
+ ___68-[IXPlaceholder setIconResourcesPromise:withInfoPlistContent:error:]_block_invoke.259
+ _objc_msgSend$containsEmbeddedNULLCharacter
+ _objc_msgSend$rangeOfString:
- GCC_except_table20
- ___31-[IXPlaceholder hasIconPromise]_block_invoke.239
- ___35-[IXPlaceholder setMetadata:error:]_block_invoke.317
- ___35-[IXPlaceholder setSinfData:error:]_block_invoke.328
- ___38-[IXPlaceholder iconPromiseWithError:]_block_invoke.227
- ___38-[IXPlaceholder iconPromiseWithError:]_block_invoke.227.cold.1
- ___38-[IXPlaceholder iconPromiseWithError:]_block_invoke.227.cold.2
- ___38-[IXPlaceholder setIconPromise:error:]_block_invoke.226
- ___39-[IXPlaceholder hasEntitlementsPromise]_block_invoke.281
- ___40-[IXPlaceholder hasIconResourcesPromise]_block_invoke.259
- ___44-[IXPlaceholder hasInfoPlistLoctablePromise]_block_invoke.287
- ___45-[IXPlaceholder hasPlugInPlaceholderPromises]_block_invoke.306
- ___46-[IXPlaceholder entitlementsPromiseWithError:]_block_invoke.277
- ___46-[IXPlaceholder entitlementsPromiseWithError:]_block_invoke.277.cold.1
- ___46-[IXPlaceholder entitlementsPromiseWithError:]_block_invoke.277.cold.2
- ___46-[IXPlaceholder setEntitlementsPromise:error:]_block_invoke.276
- ___48-[IXPlaceholder _doInitWithSpecification:error:]_block_invoke.217
- ___49-[IXPlaceholder infoPlistLocalizationsWithError:]_block_invoke.271
- ___49-[IXPlaceholder setInfoPlistLocalizations:error:]_block_invoke.270
- ___51-[IXPlaceholder infoPlistLoctablePromiseWithError:]_block_invoke.283
- ___51-[IXPlaceholder infoPlistLoctablePromiseWithError:]_block_invoke.283.cold.1
- ___51-[IXPlaceholder infoPlistLoctablePromiseWithError:]_block_invoke.283.cold.2
- ___51-[IXPlaceholder setConfigurationCompleteWithError:]_block_invoke.307
- ___51-[IXPlaceholder setInfoPlistLoctablePromise:error:]_block_invoke.282
- ___58-[IXPlaceholder appExtensionPlaceholderPromisesWithError:]_block_invoke.298
- ___58-[IXPlaceholder setAppExtensionPlaceholderPromises:error:]_block_invoke.297
- ___64-[IXPlaceholder iconResourcesPromiseWithInfoPlistContent:error:]_block_invoke.251
- ___64-[IXPlaceholder iconResourcesPromiseWithInfoPlistContent:error:]_block_invoke.251.cold.1
- ___64-[IXPlaceholder iconResourcesPromiseWithInfoPlistContent:error:]_block_invoke.251.cold.2
- ___68-[IXPlaceholder setIconResourcesPromise:withInfoPlistContent:error:]_block_invoke.250
CStrings:
+ "%s: Bundle directory name %@ contained an embedded NULL character; this is not allowed : %@"
+ "%s: Bundle identifier %@ contained an embedded NULL character; this is not allowed : %@"
+ "%s: Localized bundle name %@ contained an embedded NULL character; this is not allowed : %@"
+ "<%@<%p> name:\"%@\" uuid:%@ creator:\"%@\" location:%@>"
+ "Bundle directory name %@ contained an embedded NULL character; this is not allowed"
+ "Bundle identifier %@ contained an embedded NULL character; this is not allowed"
+ "Localized bundle name %@ contained an embedded NULL character; this is not allowed"
+ "[%@/%@/%@]"
+ "containsEmbeddedNULLCharacter"
+ "rangeOfString:"
- "[%@/%@]"

```
