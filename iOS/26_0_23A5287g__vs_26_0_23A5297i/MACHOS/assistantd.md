## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

-3500.108.6.0.0
-  __TEXT.__text: 0x3710ac
+3500.113.1.1.1
+  __TEXT.__text: 0x372238
   __TEXT.__auth_stubs: 0x34b0
-  __TEXT.__objc_stubs: 0x446e0
-  __TEXT.__objc_methlist: 0x22248
-  __TEXT.__const: 0x109c8
+  __TEXT.__objc_stubs: 0x44720
+  __TEXT.__objc_methlist: 0x22258
+  __TEXT.__const: 0x109d8
   __TEXT.__dlopen_cstrs: 0xafa
-  __TEXT.__gcc_except_tab: 0x49a0
-  __TEXT.__cstring: 0x5128b
-  __TEXT.__oslogstring: 0x3fdb1
+  __TEXT.__gcc_except_tab: 0x49a8
+  __TEXT.__cstring: 0x51406
+  __TEXT.__oslogstring: 0x4020f
   __TEXT.__objc_classname: 0x517c
-  __TEXT.__objc_methname: 0x5c48b
+  __TEXT.__objc_methname: 0x5c455
   __TEXT.__objc_methtype: 0xf108
   __TEXT.__ustring: 0x2b0
-  __TEXT.__unwind_info: 0xa310
+  __TEXT.__unwind_info: 0xa330
   __TEXT.__eh_frame: 0x80
   __DATA_CONST.__auth_got: 0x1a68
   __DATA_CONST.__got: 0x3a70
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x14d00
-  __DATA_CONST.__cfstring: 0x127c0
+  __DATA_CONST.__const: 0x14d20
+  __DATA_CONST.__cfstring: 0x128e0
   __DATA_CONST.__objc_classlist: 0xd20
   __DATA_CONST.__objc_catlist: 0x620
   __DATA_CONST.__objc_protolist: 0x6d8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0xb08
-  __DATA_CONST.__objc_arraydata: 0x388
+  __DATA_CONST.__objc_arraydata: 0x458
   __DATA_CONST.__objc_arrayobj: 0x150
-  __DATA_CONST.__objc_intobj: 0x828
-  __DATA_CONST.__objc_dictobj: 0x2d0
+  __DATA_CONST.__objc_intobj: 0x960
+  __DATA_CONST.__objc_dictobj: 0x2f8
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA.__objc_const: 0x33558
+  __DATA.__objc_const: 0x33548
   __DATA.__objc_selrefs: 0x14560
-  __DATA.__objc_ivar: 0x2558
+  __DATA.__objc_ivar: 0x255c
   __DATA.__objc_data: 0x8340
   __DATA.__data: 0x5630
-  __DATA.__bss: 0xe08
+  __DATA.__bss: 0xe18
   __DATA.__common: 0xa18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 9D4C91E4-48E1-32AC-82FD-22F546CB06A8
-  Functions: 14260
+  UUID: 908F3389-F365-33F8-A5DD-BA88AA095798
+  Functions: 14267
   Symbols:   2865
-  CStrings:  29311
+  CStrings:  29348
 
CStrings:
+ "%s ADCloudKitManager is deallocated unexpectedly while waiting for updating accountInfo and isCloudSyncEnabledForZone to complete."
+ "%s ADCloudkitManager does not have sharedZone."
+ "%s Announce in CarPlay setting is enabled, currentlyAbleToAnnounce: %d"
+ "%s Calling into INSExtensionService"
+ "%s CarPlay connection state not initialized before checking currentlyAbleToAnnounce, isConnected = %d"
+ "%s Fetching audioRecordRouteAndDeviceIdentification"
+ "%s Fetching audioSession"
+ "%s Ignoring incoming language & voice because of outdated version with current language: %@"
+ "%s Locale is nil for locale identifier %@, not checking GMS availability."
+ "%s Refreshing meDevice cache at: %@"
+ "%s Setting up _multiUserRecordZoneInfo CKRecordZone."
+ "%s Skipping sync of version 13 voice for language (%@) : %@"
+ "%s Synching default voice for version 13 sync clients (%@) : %@"
+ "%s Synching voice for version 13 sync clients as well (%@) : %@"
+ "%s Updated accountInfo and isCloudSyncEnabledForZone = (%d) for %@"
+ "%s Updating sharedZone for _sharedZoneUpdater."
+ "%s _mirroredContainer multiUserRecordZoneInfo is nil, using _multiUserRecordZoneInfo."
+ "%s _sharedZoneUpdater does not have sharedZone set."
+ "%s multiUserRecordZoneInfo does not have CKRecordZone."
+ "-[ADCloudKitManager _validateAndUpdateSharedZoneUpdater]"
+ "-[ADMultiUserMeDevice isMeDevice]"
+ "-[ADMultiUserMeDevice meDeviceIDSIdentifier]"
+ "-[AFCarPlayAnnouncementRequestCapabilityProvider currentlyAbleToAnnounce]_block_invoke_2"
+ "MobileAssistantDaemons-3500.113.1.1.1"
+ "Output Voice v14"
+ "VOICENAME_ENUSWORKOUTA"
+ "VOICENAME_ENUSWORKOUTB"
+ "VOICENAME_ENUSWORKOUTC"
+ "VOICENAME_ENUSWORKOUTD"
+ "VOICENAME_PTPTA"
+ "VOICENAME_PTPTB"
+ "_carPlayConnectionState"
+ "_lastUpdated"
+ "_validateAndUpdateSharedZoneUpdater"
+ "currentlyAbleToAnnounce"
+ "pt-PT"
+ "vi-VI"
- "%s Loading GMS availability via deprecated SPI"
- "%s Loading GMS availability via locale based SPI"
- "25"
- "MobileAssistantDaemons-3500.108.6"
- "T@\"NSNumber\",R,N,V_isMeDevice"
- "T@\"NSString\",R,N,V_meDeviceIDSIdentifier"
- "_isCarPlayConnected"
- "currentWithUseCaseIdentifiers:"
- "home:didEnableNotifications:"

```
