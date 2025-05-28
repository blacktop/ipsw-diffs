## eligibilityd

> `/usr/libexec/eligibilityd`

```diff

-47.102.5.0.0
-  __TEXT.__text: 0x1b6f8
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_stubs: 0x20c0
-  __TEXT.__objc_methlist: 0x2180
+47.120.13.0.0
+  __TEXT.__text: 0x1ce70
+  __TEXT.__auth_stubs: 0x790
+  __TEXT.__objc_stubs: 0x22c0
+  __TEXT.__objc_methlist: 0x2378
   __TEXT.__const: 0x64
-  __TEXT.__gcc_except_tab: 0x298
-  __TEXT.__cstring: 0x3b5a
-  __TEXT.__objc_methname: 0x20e2
-  __TEXT.__objc_classname: 0x393
-  __TEXT.__objc_methtype: 0x3b5
-  __TEXT.__oslogstring: 0x1668
-  __TEXT.__unwind_info: 0x7ac
-  __DATA_CONST.__auth_got: 0x3c8
-  __DATA_CONST.__got: 0x78
+  __TEXT.__gcc_except_tab: 0x2a8
+  __TEXT.__cstring: 0x3ea0
+  __TEXT.__objc_methname: 0x2412
+  __TEXT.__objc_classname: 0x3de
+  __TEXT.__objc_methtype: 0x3d1
+  __TEXT.__oslogstring: 0x1753
+  __TEXT.__unwind_info: 0x830
+  __DATA_CONST.__auth_got: 0x3d8
+  __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x898
-  __DATA_CONST.__cfstring: 0x1cc0
-  __DATA_CONST.__objc_classlist: 0x1d8
+  __DATA_CONST.__const: 0x930
+  __DATA_CONST.__cfstring: 0x1ec0
+  __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x290
-  __DATA_CONST.__objc_superrefs: 0x1d8
-  __DATA_CONST.__objc_intobj: 0xf0
-  __DATA_CONST.__objc_arraydata: 0x1d98
-  __DATA_CONST.__objc_dictobj: 0x460
-  __DATA_CONST.__objc_arrayobj: 0x2b8
-  __DATA.__objc_const: 0x3d78
-  __DATA.__objc_selrefs: 0x8a0
-  __DATA.__objc_ivar: 0x148
-  __DATA.__objc_data: 0x1270
+  __DATA_CONST.__objc_classrefs: 0x2b0
+  __DATA_CONST.__objc_superrefs: 0x1f0
+  __DATA_CONST.__objc_intobj: 0x138
+  __DATA_CONST.__objc_arraydata: 0x1ed8
+  __DATA_CONST.__objc_dictobj: 0x4d8
+  __DATA_CONST.__objc_arrayobj: 0x378
+  __DATA.__objc_const: 0x40f0
+  __DATA.__objc_selrefs: 0x920
+  __DATA.__objc_ivar: 0x160
+  __DATA.__objc_data: 0x1360
   __DATA.__data: 0x120
   __DATA.__bss: 0x49
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 720
-  Symbols:   172
-  CStrings:  1156
+  Functions: 762
+  Symbols:   176
+  CStrings:  1223
 
Symbols:
+ _OBJC_CLASS_$_MAAutoAssetNotifications
+ __xpc_event_key_name
+ _notify_register_dispatch
+ _xpc_set_event_stream_handler
CStrings:
+ "\x03"
+ "\x0f\n"
+ "\x11\x16"
+ "%@ %@ %@ %@ %@ %@"
+ "%c%c%c%c%c%c"
+ "%s: AUTO-ASSET-NOTIFICATION: %@"
+ "%s: Done updating values with new MobileAsset"
+ "%s: Failed to update MobileAsset on update notification: %@"
+ "%s: Got darwin notification %s"
+ "%s: Mobile Asset does not contain the Podcasts Transcripts domain"
+ "-[DeviceRegionCodeInput isEqual:]"
+ "-[MobileAssetManager registerForMobileAssetUpdateNotification]_block_invoke"
+ "-[PodcastsTranscriptsAsset initWithDictionary:]"
+ "-[PodcastsTranscriptsAsset isEqual:]"
+ "07:10:33"
+ "47.120.13"
+ "?7"
+ "@\"PodcastsTranscriptsAsset\""
+ "ASSET_VERSION_DOWNLOADED"
+ "Apr 13 2024"
+ "BY"
+ "CH"
+ "CN"
+ "DeviceRegionCodeInput"
+ "Disabled Country Codes"
+ "Disabled Region SKUs"
+ "Disabled Storefronts"
+ "OS_ELIGIBILITY_DOMAIN_PODCASTS_TRANSCRIPTS"
+ "OS_ELIGIBILITY_INPUT_DEVICE_REGION_CODE"
+ "Podcasts Transcripts"
+ "PodcastsTranscriptsAsset"
+ "PodcastsTranscriptsDomain"
+ "RegionCode"
+ "T@\"NSSet\",&,N,V_deviceRegionCodesOfInterest"
+ "T@\"NSSet\",&,N,V_disabledCountryCodes"
+ "T@\"NSSet\",&,N,V_disabledRegionSKUs"
+ "T@\"NSSet\",&,N,V_disabledStorefronts"
+ "T@\"NSString\",&,N,V_deviceRegionCode"
+ "T@\"PodcastsTranscriptsAsset\",C,N,V_podcastsTranscriptsAsset"
+ "US"
+ "[DeviceRegionCodeInput deviceRegionCode:\"%@\" %@]"
+ "[Podcasts Transcripts Asset disabledStorefronts:%@ disabledRegionSKUs:%@ disabledCountryCodes:%@]"
+ "_deviceRegionCode"
+ "_deviceRegionCodesOfInterest"
+ "_disabledCountryCodes"
+ "_disabledRegionSKUs"
+ "_disabledStorefronts"
+ "_mgDeviceRegionCode"
+ "_podcastsTranscriptsAsset"
+ "com.apple.eligibility.notifications"
+ "com.apple.notifyd.matching"
+ "com.apple.os-eligibility-domain.change.podcasts-transcripts"
+ "computeInputStatusForDeviceRegionCodesInput:"
+ "deviceRegionCode"
+ "deviceRegionCodesOfInterest"
+ "disabledCountryCodes"
+ "disabledRegionSKUs"
+ "disabledStorefronts"
+ "main_block_invoke_2"
+ "notifyRegistrationName:forAssetType:"
+ "podcastsTranscriptsAsset"
+ "regionCodes: %@"
+ "registerForMobileAssetUpdateNotification"
+ "setDeviceRegionCode:"
+ "setDeviceRegionCodesOfInterest:"
+ "setDisabledCountryCodes:"
+ "setDisabledRegionSKUs:"
+ "setDisabledStorefronts:"
+ "setPodcastsTranscriptsAsset:"
+ "v12@?0i8"
- "\x0f\t"
- "\x11\x15"
- "%@ %@ %@ %@ %@"
- "%c%c%c%c%c"
- "01:09:41"
- "47.102.5"
- "?6"
- "Mar  9 2024"

```
