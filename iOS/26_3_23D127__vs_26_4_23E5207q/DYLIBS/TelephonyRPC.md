## TelephonyRPC

> `/System/Library/PrivateFrameworks/TelephonyRPC.framework/TelephonyRPC`

```diff

-1131.2.3.0.0
-  __TEXT.__text: 0x1bef8
-  __TEXT.__auth_stubs: 0x11b0
-  __TEXT.__objc_methlist: 0x1058
-  __TEXT.__cstring: 0x1bbb
-  __TEXT.__const: 0x928
-  __TEXT.__oslogstring: 0xb43
+1131.4.11.0.0
+  __TEXT.__text: 0x1d234
+  __TEXT.__auth_stubs: 0x1150
+  __TEXT.__objc_methlist: 0x1098
+  __TEXT.__cstring: 0x1864
+  __TEXT.__const: 0x918
+  __TEXT.__oslogstring: 0xb03
   __TEXT.__ustring: 0x5c
   __TEXT.__gcc_except_tab: 0x4c
   __TEXT.__swift5_typeref: 0x418

   __TEXT.__swift_as_entry: 0x48
   __TEXT.__swift_as_ret: 0x4c
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x7a8
-  __TEXT.__eh_frame: 0xf20
-  __TEXT.__objc_classname: 0x243
-  __TEXT.__objc_methname: 0x27d2
-  __TEXT.__objc_methtype: 0x8e8
-  __TEXT.__objc_stubs: 0x1d60
+  __TEXT.__unwind_info: 0x828
+  __TEXT.__eh_frame: 0xf10
+  __TEXT.__objc_classname: 0x344
+  __TEXT.__objc_methname: 0x2b17
+  __TEXT.__objc_methtype: 0x954
+  __TEXT.__objc_stubs: 0x1fe0
   __DATA_CONST.__got: 0x3b0
   __DATA_CONST.__const: 0x370
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbc0
+  __DATA_CONST.__objc_selrefs: 0xbe8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x8e8
+  __AUTH_CONST.__auth_got: 0x8b8
   __AUTH_CONST.__const: 0x8e8
   __AUTH_CONST.__cfstring: 0xac0
-  __AUTH_CONST.__objc_const: 0x1e10
+  __AUTH_CONST.__objc_const: 0x1e60
   __AUTH.__objc_data: 0x568
   __AUTH.__data: 0x280
   __DATA.__objc_ivar: 0xc4

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 512A7703-6F95-30A6-BF4C-09F9D87B60D0
-  Functions: 599
-  Symbols:   1519
-  CStrings:  990
+  UUID: 10BD5C89-3A44-3111-8032-EFDB6E4D5ED4
+  Functions: 605
+  Symbols:   1557
+  CStrings:  989
 
Symbols:
+ +[NPHFeatureFlags isAirplaneModeManagementEnabledForNonEmergencyCalls]
+ +[NPHFeatureFlags isAirplaneModeManagementEnabled]
+ +[NPHFeatureFlags isRedialAfterDisablingAirplaneModeEnabledForNonEmergencyCalls]
+ +[NPHFeatureFlags isRedialAfterDisablingAirplaneModeEnabled]
+ +[NPHFeatureFlags isSatelliteSliderEnabled]
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _objc_msgSend$assetWithURL:
+ _objc_msgSend$combinedStringFromCaptions:
+ _objc_msgSend$contentsEqualAtPath:andPath:
+ _objc_msgSend$copyItemAtURL:toURL:error:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$initWithAsset:presetName:
+ _objc_msgSend$initWithStateSync:mailSync:delegate:delegateQueue:
+ _objc_msgSend$isAirplaneModeManagementEnabled
+ _objc_msgSend$isCloudSyncAvailableOverride
+ _objc_msgSend$postNotification:
+ _objc_msgSend$providerManager
+ _objc_msgSend$setIsCloudSyncAvailableOverride:
+ _objc_msgSend$setMetadata:
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$supportedFileTypes
+ _objc_msgSend$telephonyProvider
+ _objc_msgSend$temporaryDirectory
+ _objc_msgSend$voicemailRecording
+ _objc_msgSend$voicemailTranscript
+ _objc_retain_x27
+ _objectdestroy.76Tm
+ _swift_release_n
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x26
- _objc_retain_x3
- _objc_retain_x4
- _objectdestroy.74Tm
CStrings:
+ "SatelliteSlider"
+ "airplaneModeManagementForNonEmergencyCalls"
+ "isAirplaneModeManagementEnabled"
+ "isAirplaneModeManagementEnabledForNonEmergencyCalls"
+ "isRedialAfterDisablingAirplaneModeEnabled"
+ "isRedialAfterDisablingAirplaneModeEnabledForNonEmergencyCalls"
+ "isSatelliteSliderEnabled"
+ "redialAfterDisablingAirplaneMode"
+ "redialAfterDisablingAirplaneModeForNonEmergencyCalls"
+ "remoteAirplaneModeManagement"
- "%s: %s: needsContent: false ⇒ skipping accounts, voicemails"
- "com.apple.nanophoned"

```
