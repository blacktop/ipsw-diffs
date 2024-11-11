## installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

-631.60.47.0.0
-  __TEXT.__text: 0x93574
+631.60.50.0.0
+  __TEXT.__text: 0x9668c
   __TEXT.__auth_stubs: 0x1060
-  __TEXT.__objc_stubs: 0xa1c0
-  __TEXT.__objc_methlist: 0x49d0
+  __TEXT.__objc_stubs: 0xa3c0
+  __TEXT.__objc_methlist: 0x4bc8
   __TEXT.__const: 0x1f8
-  __TEXT.__cstring: 0x16844
-  __TEXT.__objc_classname: 0x945
-  __TEXT.__oslogstring: 0xcaba
-  __TEXT.__objc_methtype: 0x2131
-  __TEXT.__objc_methname: 0xf77f
-  __TEXT.__gcc_except_tab: 0x28a4
+  __TEXT.__cstring: 0x16e84
+  __TEXT.__objc_classname: 0x99e
+  __TEXT.__oslogstring: 0xccb0
+  __TEXT.__objc_methtype: 0x21a9
+  __TEXT.__objc_methname: 0xfab1
+  __TEXT.__gcc_except_tab: 0x28b0
   __TEXT.__ustring: 0x22d0
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x21f8
+  __TEXT.__unwind_info: 0x22a0
   __DATA_CONST.__auth_got: 0x840
-  __DATA_CONST.__got: 0x400
+  __DATA_CONST.__got: 0x408
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x27e8
-  __DATA_CONST.__cfstring: 0x8f20
-  __DATA_CONST.__objc_classlist: 0x218
+  __DATA_CONST.__const: 0x2918
+  __DATA_CONST.__cfstring: 0x91a0
+  __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1c0
+  __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_intobj: 0x150
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xc820
-  __DATA.__objc_selrefs: 0x2ee0
-  __DATA.__objc_ivar: 0x43c
-  __DATA.__objc_data: 0x14f0
+  __DATA.__objc_const: 0xcc00
+  __DATA.__objc_selrefs: 0x2f78
+  __DATA.__objc_ivar: 0x448
+  __DATA.__objc_data: 0x15e0
   __DATA.__data: 0x650
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x238
+  __DATA.__bss: 0x240
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2976
-  Symbols:   405
-  CStrings:  5106
+  Functions: 3057
+  Symbols:   406
+  CStrings:  5176
 
Symbols:
+ __xpc_error_connection_invalid
CStrings:
+ "%!s(MISSING): Cannot display deletion alert for unsupported default app type %!l(MISSING)u"
+ "%!s(MISSING): Failed to deserialize removability metadata for identity %!@(MISSING), version %!l(MISSING)u"
+ "%!s(MISSING): Failed to dismiss deletion sheet; connection to AppDeletionUIHost lost"
+ "%!s(MISSING): Failed to find removability entry for %!@(MISSING) : %!@(MISSING)"
+ "%!s(MISSING): Failed to get removability dictionary for entry: %!@(MISSING)"
+ "%!s(MISSING): Got XPC error on listenerConnection handler: %!@(MISSING) : %!@(MISSING)"
+ "%!s(MISSING): Got XPC error on serviceConnection handler: %!@(MISSING) : %!@(MISSING)"
+ "%!s(MISSING): Got unknown XPC event on listenerConnection handler: %!s(MISSING) : %!@(MISSING)"
+ "%!s(MISSING): Got unknown XPC event on serviceConnection handler: %!s(MISSING) : %!@(MISSING)"
+ "%!s(MISSING): ListenerConnection invalidated"
+ "%!s(MISSING): NRPairedDeviceRegistry returned %!c(MISSING) for watch paired state"
+ "%!s(MISSING): Returning removability %!@(MISSING) set for %!@(MISSING) by client %!@(MISSING) to caller %!@(MISSING)"
+ "%!s(MISSING): ServiceConnection invalidated"
+ "-[IXSAppRemovabilityManager clearRemovabilityStateForIdentity:error:]_block_invoke_2"
+ "-[IXSClientConnection _remote_removabilityForAppWithIdentity:byClient:completion:]"
+ "-[IXSDefaultAppDeleteAlert message]"
+ "-[IXSDefaultAppDeletionManager getAppRecordNeedsDefaultAppDeletionAlert:forRecord:defaultAppType:gateDeletionOfLastApp:error:]"
+ "-[IXSRemoteDeletionPromptConnection dismissAlert]"
+ "-[IXSRemoteDeletionPromptConnection startConnectionWithConfig:alertDefinition:completion:]_block_invoke"
+ "-[IXSRemoteDeletionPromptConnection startConnectionWithConfig:alertDefinition:completion:]_block_invoke_2"
+ "-[IXSRemoteDeletionPromptManager _constructRelevantAppData:showArchiveOption:]"
+ "-[IXSRemoteDeletionPromptManager displayDeletionAlertForRecord:showArchiveOption:completion:]"
+ "-[IXSRemoteDeletionPromptManager watchIsPaired]"
+ "-[IXSUninstallAlert appHasiCloudDataOrDocuments]_block_invoke"
+ "18:23:04"
+ "@\"IXSRemoteDeletionPromptConnection\""
+ "B24@?0@\"IXApplicationIdentity\"8@\"IXAppRemovabilityMetadataList\"16"
+ "B56@0:8^B16@24^Q32^B40^@48"
+ "DEFAULT_APP_APPSTORE_NOT_AVAILABLE_DELETE_APP_UI_ALERT_TITLE"
+ "DEFAULT_APP_APPSTORE_SELECT_DELETE_APP_UI_ALERT_TITLE"
+ "DEFAULT_APP_CONTACTLESS_SELECT_DELETE_APP_UI_ALERT_TITLE"
+ "DEFAULT_APP_DOWNLOAD_APP_MARKETPLACE_UI_ALERT_BODY_FIRST"
+ "DEFAULT_APP_DOWNLOAD_BROWSER_APP_UI_ALERT_BODY_FIRST"
+ "DEFAULT_APP_DOWNLOAD_MESSAGING_APP_UI_ALERT_BODY_FIRST"
+ "DEFAULT_APP_MAIL_SELECT_DELETE_APP_UI_ALERT_TITLE"
+ "DEFAULT_APP_MESSAGES_SELECT_DELETE_APP_UI_ALERT_TITLE"
+ "DEFAULT_APP_MESSAGING_NOT_AVAILABLE_DELETE_APP_UI_ALERT_TITLE"
+ "DEFAULT_APP_SAFARI_NOT_AVAILABLE_DELETE_APP_UI_ALERT_TITLE"
+ "DEFAULT_APP_SAFARI_SELECT_DELETE_APP_UI_ALERT_TITLE"
+ "Delete Default App"
+ "Failed to find removability entry for %!@(MISSING)"
+ "Got XPC error on listenerConnection handler: %!@(MISSING)"
+ "Got XPC error on serviceConnection handler: %!@(MISSING)"
+ "Got unknown XPC event on listenerConnection handler: %!s(MISSING)"
+ "Got unknown XPC event on serviceConnection handler: %!s(MISSING)"
+ "IXAppRemovabilityMetadataList"
+ "IXCopyRemovabilityStorageWithChangeClockURL"
+ "IXSDefaultAppDeleteAlert"
+ "IXSRemoteDeletionPromptConnection"
+ "Nov  2 2024"
+ "Q32@0:8@16Q24"
+ "Q32@0:8Q16Q24"
+ "RemovabilityMetadataWithMultipleSources.plist"
+ "ShowArchiveOption"
+ "T@\"IXSRemoteDeletionPromptConnection\",&,N,V_connection"
+ "T@\"NSDictionary\",&,N,V_clientToRemovabilityMetadataMap"
+ "T@\"NSObject<OS_xpc_object>\",&,N,V_listenerConnection"
+ "TEST_MODE_APP_DELETION_UI_SAD_ICLOUD_ON_KEY"
+ "TEST_MODE_APP_DELETION_UI_SAD_NUM_MEDIA_SHARED_KEY"
+ "TEST_MODE_APP_DELETION_UI_SAD_SOS_AVAILABLE_KEY"
+ "TEST_MODE_APP_DELETION_UI_SAD_WATCH_PAIRED_KEY"
+ "TestSOSAvailable"
+ "UNINSTALL_ICON_BODY_CONTACTLESS"
+ "UNINSTALL_ICON_BODY_MAIL"
+ "UNINSTALL_ICON_BODY_PHONE"
+ "WatchIsPaired"
+ "You do not have any other calling apps on this iPhone."
+ "You do not have any other contactless apps on this iPhone."
+ "You do not have any other email apps on this iPhone."
+ "_DeserializeRemovabilityMetadata"
+ "_GetRemovabilityData"
+ "_RemovabilityPListWithoutChangeClockToMetadata_block_invoke"
+ "_clientToRemovabilityMetadataMap"
+ "_connection"
+ "_constructRelevantAppData:showArchiveOption:"
+ "_listenerConnection"
+ "_remote_removabilityForAppWithIdentity:byClient:completion:"
+ "clientToRemovabilityMetadataMap"
+ "connection"
+ "dismissAlert"
+ "displayDeletionAlertForRecord:showArchiveOption:completion:"
+ "getAppRecordNeedsDefaultAppDeletionAlert:forRecord:defaultAppType:gateDeletionOfLastApp:error:"
+ "initWithInitialRemovability:client:"
+ "initWithInitialRemovabilityMetadata:"
+ "initWithSerializedDictionary:"
+ "isEmpty"
+ "isUnknown"
+ "listenerConnection"
+ "localizedStringWithFormat:"
+ "mostRestrictiveRemovabilityMetadata"
+ "propertyListRepresentation"
+ "removabilityForAppWithIdentity:client:"
+ "removabilityForClient:notFoundRemovability:"
+ "setClientToRemovabilityMetadataMap:"
+ "setConnection:"
+ "setListenerConnection:"
+ "startConnectionWithConfig:alertDefinition:completion:"
+ "updateRemovability:forClient:"
+ "updateRemovabilityWithMetadata:"
+ "v32@?0@\"IXApplicationIdentity\"8@\"IXAppRemovabilityMetadataList\"16^B24"
+ "v32@?0@\"IXApplicationIdentity\"8Q16^B24"
+ "v32@?0@\"NSNumber\"8@\"IXAppRemovabilityMetadata\"16^B24"
+ "v32@?0@8Q16^B24"
+ "v36@0:8@16B24@?28"
+ "v40@0:8@\"IXApplicationIdentity\"16Q24@?<v@?Q@\"NSError\">32"
+ "watchIsPaired"
- "%!s(MISSING): Failed to clear removability for %!@(MISSING) : %!@(MISSING)"
- "%!s(MISSING): Got XPC error on listenerConnection handler: %!@(MISSING)"
- "%!s(MISSING): Got XPC error on serviceConnection handler: %!@(MISSING)"
- "%!s(MISSING): Got unknown XPC event on listenerConnection handler: %!s(MISSING)"
- "%!s(MISSING): Got unknown XPC event on serviceConnection handler: %!s(MISSING)"
- "-[IXSAppUninstallAlert appHasiCloudDataOrDocuments]_block_invoke"
- "-[IXSDefaultAppDeletionManager getAppRecordNeedsDefaultAppDeletionAlert:forRecord:defaultAppType:error:]"
- "-[IXSRemoteDeletionPromptManager _constructRelevantAppData:]"
- "-[IXSRemoteDeletionPromptManager displayDeletionAlertForRecord:completion:]"
- "-[IXSRemoteDeletionPromptManager displayDeletionAlertForRecord:completion:]_block_invoke"
- "10:20:08"
- "@\"SBSRemoteAlertHandle\""
- "B24@?0@\"IXApplicationIdentity\"8@\"IXAppRemovabilityMetadata\"16"
- "B48@0:8^B16@24^Q32^@40"
- "DEFAULT_APP_APPSTORE_NOT_AVAILABLE_DELETE_APP_TITLE"
- "DEFAULT_APP_APPSTORE_SELECT_DELETE_APP_TITLE"
- "DEFAULT_APP_CONTACTLESS_SELECT_DELETE_APP_TITLE"
- "DEFAULT_APP_DOWNLOAD_APP_MARKETPLACE_BODY_FIRST"
- "DEFAULT_APP_DOWNLOAD_BROWSER_APP_BODY_FIRST"
- "DEFAULT_APP_DOWNLOAD_MESSAGING_APP_BODY_FIRST"
- "DEFAULT_APP_MAIL_SELECT_DELETE_APP_TITLE"
- "DEFAULT_APP_MESSAGES_SELECT_DELETE_APP_TITLE"
- "DEFAULT_APP_MESSAGING_NOT_AVAILABLE_DELETE_APP_TITLE"
- "DEFAULT_APP_SAFARI_NOT_AVAILABLE_DELETE_APP_TITLE"
- "DEFAULT_APP_SAFARI_SELECT_DELETE_APP_TITLE"
- "Failed to clear removability for %!@(MISSING)"
- "IXGetUncachedRemovabilityMetadataForApp"
- "NumAppsInstalled"
- "Oct 26 2024"
- "T@\"SBSRemoteAlertHandle\",&,N,V_alertHandle"
- "_alertHandle"
- "_constructRelevantAppData:"
- "alertHandle"
- "displayDeletionAlertForRecord:completion:"
- "getAppRecordNeedsDefaultAppDeletionAlert:forRecord:defaultAppType:error:"
- "setAlertHandle:"
- "unsignedIntValue"
- "v32@?0@\"IXApplicationIdentity\"8@\"IXAppRemovabilityMetadata\"16^B24"

```
