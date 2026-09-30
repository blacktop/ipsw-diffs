## findmylocated

> `/usr/libexec/findmylocated`

```diff

-  __TEXT.__text: 0x5853b4
-  __TEXT.__auth_stubs: 0x5c90
+  __TEXT.__text: 0x585adc
+  __TEXT.__auth_stubs: 0x5cc0
   __TEXT.__objc_stubs: 0x2000
-  __TEXT.__objc_methlist: 0xf1c
-  __TEXT.__const: 0x20738
-  __TEXT.__cstring: 0xb482
-  __TEXT.__swift5_typeref: 0x72ca
-  __TEXT.__constg_swiftt: 0x70bc
+  __TEXT.__objc_methlist: 0xf34
+  __TEXT.__const: 0x20718
+  __TEXT.__cstring: 0xb842
+  __TEXT.__swift5_typeref: 0x729c
+  __TEXT.__constg_swiftt: 0x70cc
   __TEXT.__swift5_builtin: 0x12c
-  __TEXT.__swift5_reflstr: 0x7cfd
-  __TEXT.__swift5_fieldmd: 0x8eac
+  __TEXT.__swift5_reflstr: 0x7e1d
+  __TEXT.__swift5_fieldmd: 0x8f84
   __TEXT.__swift5_assocty: 0xa48
   __TEXT.__swift5_proto: 0x17d8
   __TEXT.__swift5_types: 0x7f0
   __TEXT.__objc_classname: 0x1276
-  __TEXT.__objc_methname: 0x4e85
+  __TEXT.__objc_methname: 0x4eb5
   __TEXT.__objc_methtype: 0x11e8
   __TEXT.__swift5_protos: 0x48
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__oslogstring: 0x18f3c
-  __TEXT.__swift_as_entry: 0x1694
-  __TEXT.__swift_as_ret: 0x27d8
-  __TEXT.__swift_as_cont: 0x432c
-  __TEXT.__swift5_capture: 0x4d28
+  __TEXT.__oslogstring: 0x18f2c
+  __TEXT.__swift_as_entry: 0x16a4
+  __TEXT.__swift_as_ret: 0x27f4
+  __TEXT.__swift_as_cont: 0x435c
+  __TEXT.__swift5_capture: 0x4d2c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x15648
-  __TEXT.__eh_frame: 0x48008
-  __DATA_CONST.__const: 0x181a0
+  __TEXT.__unwind_info: 0x15da8
+  __TEXT.__eh_frame: 0x48098
+  __DATA_CONST.__const: 0x181c0
   __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__linkguard: 0x33
-  __DATA_CONST.__auth_got: 0x2e50
-  __DATA_CONST.__got: 0x1d10
-  __DATA_CONST.__auth_ptr: 0x1a48
-  __DATA.__objc_const: 0x6270
-  __DATA.__objc_selrefs: 0xd50
+  __DATA_CONST.__auth_got: 0x2e68
+  __DATA_CONST.__got: 0x1d20
+  __DATA_CONST.__auth_ptr: 0x1a58
+  __DATA.__objc_const: 0x6278
+  __DATA.__objc_selrefs: 0xd58
   __DATA.__objc_data: 0x1428
-  __DATA.__data: 0xefb8
+  __DATA.__data: 0xefa0
   __DATA.__bss: 0x2e380
   __DATA.__common: 0x1408
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17434
-  Symbols:   2864
-  CStrings:  3833
+  Functions: 17446
+  Symbols:   2870
+  CStrings:  3855
 
Sections:
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_entry : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__bss : content changed
~ __DATA.__common : content changed
Symbols:
+ _$s12FindMyLocate16SettingsProtocolP19clientConfigurationAA06ClientG0VyYaKFTj
+ _$s12FindMyLocate16SettingsProtocolP19clientConfigurationAA06ClientG0VyYaKFTjTu
+ _$s12FindMyLocate16SettingsProtocolP19clientConfigurationAA06ClientG0VyYaKFTq
+ _$s12FindMyLocate19ClientConfigurationV23minCallbackIntervalInMS25inaccuracyRadiusThreshold03maxghiJ0016fallbackToLegacyhI3Sec32reverseGeocodingThrottleDistance015callbackTimeouthiJ05prsId09heartbeathiR004livexM0013liveAnimationH00stU015iterationNumber0f21OfferLocationDurationiR00n21OfferLocationDurationiR014fenceSetupLink023precisionFindingSessionX0019peopleFindingNearbyV027peopleFindingConnectingTime025peopleFindingBackgroundedX0026appBackgroundSubscriptionsX024pendingRemoveGracePeriodACSd_S5ds5Int64VS4dSiS2dSSS5dSitcfC
+ _$s12FindMyLocate19ClientConfigurationVMa
+ _$s12FindMyLocate19ClientConfigurationVMn
+ _$s12FindMyLocate19ClientConfigurationVSEAAMc
- _swift_runtimeSupportsNoncopyableTypes
CStrings:
+ " appBackgroundSubscriptionsTimeout:"
+ " fenceSetupLink:"
+ " maxOfferLocationDurationInSec:"
+ " minOfferLocationDurationInSec:"
+ " pendingRemoveGracePeriod:"
+ " peopleFindingBackgroundedTimeout:"
+ " peopleFindingConnectingTime:"
+ " peopleFindingNearbyDistance:"
+ " precisionFindingSessionTimeout:"
+ "AutoMe is active - not accepting live location request."
+ "Fence %{public}s cannot be triggered because this device is not currently publishing locations"
+ "Scheduling void command to %{public}s on %{public}s WorkItem: %{public}s"
+ "appBackgroundSubscriptionsTimeout"
+ "clientConfiguration(completion:)"
+ "clientConfigurationWithCompletion:"
+ "https://support.apple.com/guide/findmy-mac/set-location-notifications-fmmeb70d2de0/mac"
+ "https://support.apple.com/guide/ipad/set-location-notifications-for-friends-ipad4c370380/ipados"
+ "https://support.apple.com/guide/iphone/set-location-notifications-for-friends-iph843dd79b6/ios"
+ "maxOfferLocationDurationInSec"
+ "minOfferLocationDurationInSec"
+ "pendingRemoveGracePeriod"
+ "peopleFindingBackgroundedTimeout"
+ "peopleFindingConnectingTime"
+ "peopleFindingNearbyDistance"
+ "precisionFindingSessionTimeout"
+ "sendVoidCommand(_:content:credential:)"
- "FenceService: dataManagerStateStream is nil — cannot monitor for friend removal"
- "FenceService: failed to set up .removedFriend monitor: %{public}@"
- "Scheduling AckAlert command to %{public}s on %{public}s WorkItem: %{public}s"
- "sendAckAlertCommand(_:content:credential:)"

```
