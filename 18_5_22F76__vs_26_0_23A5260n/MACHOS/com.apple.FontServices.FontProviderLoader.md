## com.apple.FontServices.FontProviderLoader

> `/System/Library/PrivateFrameworks/FontServices.framework/XPCServices/com.apple.FontServices.FontProviderLoader.xpc/com.apple.FontServices.FontProviderLoader`

```diff

-137.4.0.1.0
-  __TEXT.__text: 0x2648
-  __TEXT.__auth_stubs: 0x440
+150.0.0.0.0
+  __TEXT.__text: 0x243c
+  __TEXT.__auth_stubs: 0x430
   __TEXT.__objc_stubs: 0x9a0
   __TEXT.__objc_methlist: 0x428
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x432
   __TEXT.__objc_classname: 0xc9
   __TEXT.__objc_methname: 0xd6b
   __TEXT.__objc_methtype: 0x3e5
-  __TEXT.__unwind_info: 0xf8
-  __DATA_CONST.__auth_got: 0x228
-  __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x1c0
-  __DATA_CONST.__cfstring: 0x440
+  __TEXT.__cstring: 0x402
+  __TEXT.__unwind_info: 0xf0
+  __DATA_CONST.__auth_got: 0x220
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__const: 0x1b8
+  __DATA_CONST.__cfstring: 0x400
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x938
+  __DATA.__objc_const: 0x578
   __DATA.__objc_selrefs: 0x460
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0xf0

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
-  - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/FontServices.framework/FontServices
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 885E1FF9-63DC-3917-8FD4-7E085771156C
-  Functions: 39
-  Symbols:   567
-  CStrings:  278
+  UUID: D31182DA-0AEF-3931-ABBE-85D105ADD458
+  Functions: 37
+  Symbols:   126
+  CStrings:  273
 
Symbols:
+ radr://5614542
- 
- -[FontProviderLoader .cxx_destruct]
- -[FontProviderLoader basePathForODRContentAssetPack]
- -[FontProviderLoader confirm:sceneID:]
- -[FontProviderLoader confirm:sceneID:].cold.1
- -[FontProviderLoader currentConnectionHasFontProviderEntitlement:withSuppressDialogEntitlement:forUnitTest:]
- -[FontProviderLoader doneWithInstallFonts:]
- -[FontProviderLoader fontDescriptorAttributesArrayFromFontInfoDictionary:]
- -[FontProviderLoader isDeviceInEduMode]
- -[FontProviderLoader isDeviceInEduMode].cold.1
- -[FontProviderLoader isFileURL:forApplicationBundlePath:]
- -[FontProviderLoader isOnDemandResourceFile:]
- -[FontProviderLoader ping:]
- -[FontProviderLoader registerFonts:enabled:sceneID:appInfo:completionHandler:]
- -[FontProviderLoader registeredFontsInfo:appInfo:completionHandler:]
- -[FontProviderLoader systemContainerURL]
- -[FontProviderLoader systemContainerURL].cold.1
- -[FontProviderLoader unregisterFonts:appInfo:completionHandler:]
- -[FontProviderLoader updateAppInfo:]
- -[FontProviderLoaderServiceDelegate listener:shouldAcceptNewConnection:]
- -[FontProviderViewServiceDelegate .cxx_destruct]
- -[FontProviderViewServiceDelegate fontProviderLoader]
- -[FontProviderViewServiceDelegate initWithFontProviderLoader:]
- -[FontProviderViewServiceDelegate listener:shouldAcceptNewConnection:]
- -[FontProviderViewServiceDelegate setFontProviderLoader:]
- /Library/Caches/com.apple.xbs/Binaries/FontServices/install/TempContent/Objects/FontServices.build/FontProviderLoader.build/DerivedSources/
- /Library/Caches/com.apple.xbs/Binaries/FontServices/install/TempContent/Objects/FontServices.build/FontProviderLoader.build/Objects-normal/arm64e/FontProvider.o
- /Library/Caches/com.apple.xbs/Binaries/FontServices/install/TempContent/Objects/FontServices.build/FontProviderLoader.build/Objects-normal/arm64e/FontProviderError.o
- /Library/Caches/com.apple.xbs/Binaries/FontServices/install/TempContent/Objects/FontServices.build/FontProviderLoader.build/Objects-normal/arm64e/FontProviderLoader.o
- /Library/Caches/com.apple.xbs/Binaries/FontServices/install/TempContent/Objects/FontServices.build/FontProviderLoader.build/Objects-normal/arm64e/FontProviderLoaderMain.o
- /Library/Caches/com.apple.xbs/Binaries/FontServices/install/TempContent/Objects/FontServices.build/FontProviderLoader.build/Objects-normal/arm64e/FontServicesUtils.o
- /Library/Caches/com.apple.xbs/Binaries/FontServices/install/TempContent/Objects/FontServices.build/FontProviderLoader.build/Objects-normal/arm64e/com.apple.FontServices.FontProviderLoader_vers.o
- /Library/Caches/com.apple.xbs/Sources/FontServices/FontProvider/
- /Library/Caches/com.apple.xbs/Sources/FontServices/FontProvider/FontProviderLoader/
- /Library/Caches/com.apple.xbs/Sources/FontServices/FontServices/
- FontProvider.m
- FontProviderError.m
- FontProviderLoader.m
- FontProviderLoaderMain.m
- FontServicesUtils.m
- OBJC_IVAR_$_FontProviderLoader._alertSemaphore
- OBJC_IVAR_$_FontProviderLoader._result
- OBJC_IVAR_$_FontProviderLoader._serviceDelegate
- OBJC_IVAR_$_FontProviderViewServiceDelegate._fontProviderLoader
- _FontProviderErrorIdentifierKey
- _IsApplicationIdentifierGrantedFontEnumeration
- _SANDBOX_CHECK_NO_REPORT
- _SandboxExtensionsForPathsAndAuditToken
- __OBJC_$_INSTANCE_METHODS_FontProviderLoader
- __OBJC_$_INSTANCE_METHODS_FontProviderLoaderServiceDelegate
- __OBJC_$_INSTANCE_METHODS_FontProviderViewServiceDelegate
- __OBJC_$_INSTANCE_VARIABLES_FontProviderLoader
- __OBJC_$_INSTANCE_VARIABLES_FontProviderViewServiceDelegate
- __OBJC_$_PROP_LIST_FontProviderLoaderServiceDelegate
- __OBJC_$_PROP_LIST_FontProviderViewServiceDelegate
- __OBJC_$_PROP_LIST_NSObject
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_FontProviderProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FontInstallViewServiceProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXPCListenerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBUIRemoteAlertHostInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_FontInstallViewServiceProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_FontProviderProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSXPCListenerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_SBUIRemoteAlertHostInterface
- __OBJC_$_PROTOCOL_REFS_FontInstallViewServiceProtocol
- __OBJC_$_PROTOCOL_REFS_NSXPCListenerDelegate
- __OBJC_CLASS_PROTOCOLS_$_FontProviderLoader
- __OBJC_CLASS_PROTOCOLS_$_FontProviderLoaderServiceDelegate
- __OBJC_CLASS_PROTOCOLS_$_FontProviderViewServiceDelegate
- __OBJC_CLASS_RO_$_FontProviderLoader
- __OBJC_CLASS_RO_$_FontProviderLoaderServiceDelegate
- __OBJC_CLASS_RO_$_FontProviderViewServiceDelegate
- __OBJC_LABEL_PROTOCOL_$_FontInstallViewServiceProtocol
- __OBJC_LABEL_PROTOCOL_$_FontProviderProtocol
- __OBJC_LABEL_PROTOCOL_$_NSObject
- __OBJC_LABEL_PROTOCOL_$_NSXPCListenerDelegate
- __OBJC_LABEL_PROTOCOL_$_SBUIRemoteAlertHostInterface
- __OBJC_METACLASS_RO_$_FontProviderLoader
- __OBJC_METACLASS_RO_$_FontProviderLoaderServiceDelegate
- __OBJC_METACLASS_RO_$_FontProviderViewServiceDelegate
- __OBJC_PROTOCOL_$_FontInstallViewServiceProtocol
- __OBJC_PROTOCOL_$_FontProviderProtocol
- __OBJC_PROTOCOL_$_NSObject
- __OBJC_PROTOCOL_$_NSXPCListenerDelegate
- __OBJC_PROTOCOL_$_SBUIRemoteAlertHostInterface
- __OBJC_PROTOCOL_REFERENCE_$_FontInstallViewServiceProtocol
- __OBJC_PROTOCOL_REFERENCE_$_FontProviderProtocol
- ___38-[FontProviderLoader confirm:sceneID:]_block_invoke
- ___39-[FontProviderLoader isDeviceInEduMode]_block_invoke
- ___40-[FontProviderLoader systemContainerURL]_block_invoke
- ___52-[FontProviderLoader basePathForODRContentAssetPack]_block_invoke
- ___64-[FontProviderLoader unregisterFonts:appInfo:completionHandler:]_block_invoke
- ___64-[FontProviderLoader unregisterFonts:appInfo:completionHandler:]_block_invoke_2
- ___74-[FontProviderLoader fontDescriptorAttributesArrayFromFontInfoDictionary:]_block_invoke
- ___78-[FontProviderLoader registerFonts:enabled:sceneID:appInfo:completionHandler:]_block_invoke
- ___78-[FontProviderLoader registerFonts:enabled:sceneID:appInfo:completionHandler:]_block_invoke_2
- ___78-[FontProviderLoader registerFonts:enabled:sceneID:appInfo:completionHandler:]_block_invoke_3
- ___block_descriptor_32_e5_v8?0l
- ___block_descriptor_40_e8_32s_e29_v32?0"NSDictionary"8Q16^B24ls32l8
- ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSArray"8"NSDictionary"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e35_v32?0"NSString"8"NSString"16^B24ls32l8s40l8s48l8
- ___block_descriptor_74_e8_32s40s48s56s64s_e29_v32?0"NSDictionary"8Q16^B24ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global
- __block_literal_global.169
- __block_literal_global.172
- _normalizeURLFilePath
- _objc_msgSend$URL
- _objc_msgSend$URLByAppendingPathComponent:
- _objc_msgSend$URLByStandardizingPath
- _objc_msgSend$UTF8String
- _objc_msgSend$_endpoint
- _objc_msgSend$absoluteURL
- _objc_msgSend$activateWithContext:
- _objc_msgSend$addObject:
- _objc_msgSend$addObjectsFromArray:
- _objc_msgSend$anonymousListener
- _objc_msgSend$arrayWithCapacity:
- _objc_msgSend$arrayWithObjects:count:
- _objc_msgSend$auditToken
- _objc_msgSend$basePathForODRContentAssetPack
- _objc_msgSend$boolValue
- _objc_msgSend$bundleIdentifier
- _objc_msgSend$bytes
- _objc_msgSend$confirm:sceneID:
- _objc_msgSend$containsObject:
- _objc_msgSend$count
- _objc_msgSend$countByEnumeratingWithState:objects:count:
- _objc_msgSend$currentConnection
- _objc_msgSend$currentConnectionHasFontProviderEntitlement:withSuppressDialogEntitlement:forUnitTest:
- _objc_msgSend$currentState
- _objc_msgSend$currentUser
- _objc_msgSend$dataWithBytesNoCopy:length:freeWhenDone:
- _objc_msgSend$dictionaryWithCapacity:
- _objc_msgSend$dictionaryWithObjects:forKeys:count:
- _objc_msgSend$endowmentNamespaces
- _objc_msgSend$endpoint
- _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
- _objc_msgSend$enumerateObjectsUsingBlock:
- _objc_msgSend$errorWithDomain:code:userInfo:
- _objc_msgSend$fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:
- _objc_msgSend$fontDescriptorAttributesArrayFromFontInfoDictionary:
- _objc_msgSend$handleForPredicate:error:
- _objc_msgSend$hasPrefix:
- _objc_msgSend$initWithBundleIdentifier:allowPlaceholder:error:
- _objc_msgSend$initWithFontProviderLoader:
- _objc_msgSend$initWithServiceName:viewControllerClassName:
- _objc_msgSend$installFonts:forIdentifier:enabled:appInfo:completionHandler:
- _objc_msgSend$integerForKey:
- _objc_msgSend$interfaceWithProtocol:
- _objc_msgSend$isDeviceInEduMode
- _objc_msgSend$isEqualToString:
- _objc_msgSend$isFileURL
- _objc_msgSend$isFileURL:forApplicationBundlePath:
- _objc_msgSend$isMultiUser
- _objc_msgSend$isOnDemandResourceFile:
- _objc_msgSend$mutableCopy
- _objc_msgSend$newHandleWithDefinition:configurationContext:
- _objc_msgSend$now
- _objc_msgSend$numberWithUnsignedInteger:
- _objc_msgSend$objectForKey:
- _objc_msgSend$path
- _objc_msgSend$predicateMatchingBundleIdentifier:
- _objc_msgSend$registeredFontsInfoForIdentifier:enabled:appInfo:
- _objc_msgSend$removeObjectForKey:
- _objc_msgSend$resume
- _objc_msgSend$serviceListener
- _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
- _objc_msgSend$setDelegate:
- _objc_msgSend$setExportedInterface:
- _objc_msgSend$setExportedObject:
- _objc_msgSend$setObject:forKey:
- _objc_msgSend$setUserInfo:
- _objc_msgSend$setValue:forKey:
- _objc_msgSend$setWithObjects:
- _objc_msgSend$setXpcEndpoint:
- _objc_msgSend$sharedManager
- _objc_msgSend$standardUserDefaults
- _objc_msgSend$stringByAppendingPathComponent:
- _objc_msgSend$systemContainerURL
- _objc_msgSend$timeIntervalSinceNow
- _objc_msgSend$uninstallFonts:forIdentifier:appInfo:completionHandler:
- _objc_msgSend$updateAppInfo:forIdentifier:
- _objc_msgSend$userType
- _sandbox_check_by_audit_token
- basePathForODRContentAssetPack.basePath
- basePathForODRContentAssetPack.onceToken
- com.apple.FontServices.FontProviderLoader_vers.c
- confirm:sceneID:.onceToken
- confirm:sceneID:.sInstallDialogSemaphore
- isDeviceInEduMode.eduModeEnabled
- isDeviceInEduMode.onceToken
- systemContainerURL.onceToken
- systemContainerURL.systemContainerUrl
CStrings:
- "Identifier"
- "com.apple.Preferences"
- "file-read-data"

```
