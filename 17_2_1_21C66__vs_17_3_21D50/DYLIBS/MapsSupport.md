## MapsSupport

> `/System/Library/PrivateFrameworks/MapsSupport.framework/MapsSupport`

```diff

-2811.32.9.28.15
-  __TEXT.__text: 0x6c244
+2811.33.11.14.6
+  __TEXT.__text: 0x6ca4c
   __TEXT.__auth_stubs: 0xa50
-  __TEXT.__objc_methlist: 0x6684
+  __TEXT.__objc_methlist: 0x6694
   __TEXT.__const: 0x134
   __TEXT.__cstring: 0x53ab
-  __TEXT.__oslogstring: 0x6944
+  __TEXT.__oslogstring: 0x6afc
   __TEXT.__gcc_except_tab: 0xac0
   __TEXT.__dlopen_cstrs: 0x104
   __TEXT.__ustring: 0x2b2
   __TEXT.__unwind_info: 0x1ad4
   __TEXT.__objc_classname: 0xfde
-  __TEXT.__objc_methname: 0x100cb
+  __TEXT.__objc_methname: 0x100ab
   __TEXT.__objc_methtype: 0x30d9
   __TEXT.__objc_stubs: 0xb900
   __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x2218
+  __DATA_CONST.__const: 0x22b8
   __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xbd50
-  __DATA_CONST.__objc_selrefs: 0x3bd8
+  __DATA_CONST.__objc_selrefs: 0x3bd0
   __AUTH_CONST.__cfstring: 0x3d00
   __AUTH_CONST.__objc_const: 0x2610
   __AUTH_CONST.__const: 0x9c0

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4B86AE0D-9524-315F-8365-0317084FC793
-  Functions: 2550
-  Symbols:   8667
-  CStrings:  4906
+  UUID: D0998174-AE2B-30E3-B1E8-D63FF89276B4
+  Functions: 2551
+  Symbols:   8672
+  CStrings:  4910
 
Symbols:
+ -[MSPSenderMessageStrategy removeParticipant:]
+ -[_MSPSharedTripSingleCapabilityLevelFetcher _finishWithType:]
+ -[_MSPSharedTripSingleCapabilityLevelFetcher capabilityLevelFetcher:didUpdateCapabilityLevelsForHandles:]
+ ___105-[_MSPSharedTripSingleCapabilityLevelFetcher capabilityLevelFetcher:didUpdateCapabilityLevelsForHandles:]_block_invoke
+ ___47-[MSPSharedTripService _openConnectionIfNeeded]_block_invoke.186
+ ___60-[MSPSharedTripService _startSharingWithContact:completion:]_block_invoke.84
+ ___60-[MSPSharedTripService _startSharingWithContact:completion:]_block_invoke_2.85
+ ___60-[MSPSharedTripService stopAllSharingWithReason:completion:]_block_invoke.96
+ ___61-[MSPSharedTripService _stopAllSharingWithReason:completion:]_block_invoke.97
+ ___61-[MSPSharedTripService _stopAllSharingWithReason:completion:]_block_invoke_2.98
+ ___66-[MSPSharedTripService _stopSharingWithContact:reason:completion:]_block_invoke.94
+ ___66-[MSPSharedTripService _stopSharingWithContact:reason:completion:]_block_invoke_2.95
+ ___79-[MSPSharedTripService _subscribeToSharedTripUpdatesWithIdentifier:completion:]_block_invoke.127
+ ___block_descriptor_48_e8_32s40bs_e20_v24?0Q8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8ls32l8s40l8w48l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40bs48w_e17_v16?0"NSError"8ls32l8s40l8w48l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.100
+ ___block_literal_global.109
+ ___block_literal_global.123
+ ___block_literal_global.89
+ _objc_msgSend$_finishWithType:
- -[_MSPSharedTripSingleCapabilityLevelFetcher _finish]
- -[_MSPSharedTripSingleCapabilityLevelFetcher capabilityLevelsDidUpdateForHandles:]
- ___47-[MSPSharedTripService _openConnectionIfNeeded]_block_invoke.180
- ___60-[MSPSharedTripService _startSharingWithContact:completion:]_block_invoke_2.84
- ___60-[MSPSharedTripService _startSharingWithContact:completion:]_block_invoke_3
- ___60-[MSPSharedTripService stopAllSharingWithReason:completion:]_block_invoke_2
- ___61-[MSPSharedTripService _stopAllSharingWithReason:completion:]_block_invoke_3
- ___61-[MSPSharedTripService _stopAllSharingWithReason:completion:]_block_invoke_4
- ___66-[MSPSharedTripService _stopSharingWithContact:reason:completion:]_block_invoke_3
- ___66-[MSPSharedTripService _stopSharingWithContact:reason:completion:]_block_invoke_4
- ___79-[MSPSharedTripService _subscribeToSharedTripUpdatesWithIdentifier:completion:]_block_invoke.121
- ___82-[_MSPSharedTripSingleCapabilityLevelFetcher capabilityLevelsDidUpdateForHandles:]_block_invoke
- ___block_descriptor_40_e8_32bs_e20_v24?0Q8"NSError"16ls32l8
- ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8ls40l8s32l8w48l8
- ___block_descriptor_64_e8_32s40bs48w_e17_v16?0"NSError"8ls40l8w48l8s32l8
- ___block_literal_global.88
- ___block_literal_global.94
- _objc_msgSend$_finish
CStrings:
+ "[Sender] Asked to stop sharing but we didn't match with any of the handles"
+ "[Service] Error starting to share with contact %{private}@: %{public}@"
+ "[Service] Error stopping all sharing: %{public}@"
+ "[Service] Error stopping sharing with contact %{private}@: %{public}@"
+ "_finishWithType:"
+ "fetchCapabilityLevelForContact cleaning up and calling completion handler with type %{public}@ for contact %{private}@"
+ "fetchCapabilityLevelForContact single-fetcher finish was called multiple times for contact %{private}@"
+ "stopSharingWith: %@ wasInMinimal: %{public}@, wasInLive: %{public}@, wasInMessages: %{public}@, willSendFinishedMessage: %{public}@"
- "_finish"
- "capabilityLevelsDidUpdateForHandles:"
- "fetchCapabilityLevelForContact cleaning up and calling completion handler for contact %{private}@"
- "stopSharingWith: %@ wasInMinimal: %@, wasInLive: %@, willSendFinishedMessage: %@"

```
