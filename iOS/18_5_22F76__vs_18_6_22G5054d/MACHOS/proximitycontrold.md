## proximitycontrold

> `/usr/libexec/proximitycontrold`

```diff

-228.50.20.0.0
-  __TEXT.__text: 0x252b64
-  __TEXT.__auth_stubs: 0x3150
+228.60.6.0.0
+  __TEXT.__text: 0x25006c
+  __TEXT.__auth_stubs: 0x3160
   __TEXT.__objc_stubs: 0x220
   __TEXT.__objc_methlist: 0x28f4
   __TEXT.__objc_classname: 0x48b
-  __TEXT.__objc_methname: 0x6b0f
+  __TEXT.__objc_methname: 0x6adc
   __TEXT.__objc_methtype: 0x2d00
-  __TEXT.__const: 0x26438
-  __TEXT.__cstring: 0x16a66
-  __TEXT.__swift5_typeref: 0x12790
-  __TEXT.__constg_swiftt: 0x10140
-  __TEXT.__swift5_reflstr: 0xa173
-  __TEXT.__swift5_fieldmd: 0xab6c
+  __TEXT.__const: 0x267c8
+  __TEXT.__cstring: 0x169d6
+  __TEXT.__swift5_typeref: 0x127d2
+  __TEXT.__constg_swiftt: 0x10188
+  __TEXT.__swift5_reflstr: 0xa253
+  __TEXT.__swift5_fieldmd: 0xac50
   __TEXT.__swift5_builtin: 0x604
   __TEXT.__swift5_assocty: 0xf60
-  __TEXT.__swift5_capture: 0x371c
-  __TEXT.__oslogstring: 0x1ad8
-  __TEXT.__swift5_proto: 0x2230
+  __TEXT.__swift5_capture: 0x36d4
+  __TEXT.__oslogstring: 0x1ba8
+  __TEXT.__swift5_proto: 0x2254
   __TEXT.__swift5_types: 0xa68
   __TEXT.__swift5_protos: 0x320
   __TEXT.__swift5_mpenum: 0x174
-  __TEXT.__swift_as_entry: 0xc4
-  __TEXT.__swift_as_ret: 0xc4
-  __TEXT.__unwind_info: 0x79d0
-  __TEXT.__eh_frame: 0x7804
-  __DATA_CONST.__auth_got: 0x18b0
-  __DATA_CONST.__got: 0xe50
-  __DATA_CONST.__auth_ptr: 0x32a8
-  __DATA_CONST.__const: 0x1a4d8
+  __TEXT.__swift_as_entry: 0xc0
+  __TEXT.__swift_as_ret: 0xc0
+  __TEXT.__unwind_info: 0x79c8
+  __TEXT.__eh_frame: 0x76e0
+  __DATA_CONST.__auth_got: 0x18b8
+  __DATA_CONST.__got: 0xe60
+  __DATA_CONST.__auth_ptr: 0x2cd8
+  __DATA_CONST.__const: 0x1a4e0
   __DATA_CONST.__cfstring: 0x480
   __DATA_CONST.__objc_classlist: 0x440
   __DATA_CONST.__objc_catlist: 0x28

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x180
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x183f8
-  __DATA.__objc_selrefs: 0x1cd0
+  __DATA.__objc_const: 0x18458
+  __DATA.__objc_selrefs: 0x1cc8
   __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0x2f58
-  __DATA.__data: 0x18e10
-  __DATA.__bss: 0x3a270
-  __DATA.__common: 0x7f8
+  __DATA.__data: 0x18c90
+  __DATA.__bss: 0x3a760
+  __DATA.__common: 0x7e8
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 29881446-A7F7-3594-B7FB-6A1255F90D77
-  Functions: 11668
-  Symbols:   1529
+  UUID: 0BE491B6-1FDA-3741-87FC-B6AEA4A5EC91
+  Functions: 11664
+  Symbols:   1532
   CStrings:  4239
 
Symbols:
+ _$sShyxGSEsSERzrlMc
+ _$sShyxGSesSeRzrlMc
+ _$ss22KeyedDecodingContainerV15decodeIfPresent_6forKeySbSgSbm_xtKF
+ _$ss22KeyedEncodingContainerV15encodeIfPresent_6forKeyySbSg_xtKF
- _$s2os12OSSignpostIDV3logACSo03OS_a1_D0C_tcfC
CStrings:
+ "%s: %s, local=%s, remote=%s"
+ "@QE ProximityControl.deviceMotionStateDismissedSession"
+ "Determined policy: Automatic! %s, %s"
+ "Determined policy: Not Automatic: (%s). %s, %s"
+ "Existing active transfer: %s"
+ "Please explain the expected vs. actual behavior."
+ "Proximity Handoff Impact"
+ "_boopBehaviorCallNeighborhoodPushAuto"
+ "_boopBehaviorCallRoutePushAuto"
+ "_requirePermissionToHandoffCall"
+ "boopBehaviorCallNeighborhoodPushAuto"
+ "boopBehaviorCallRoutePushAuto"
+ "deviceMotionStateDismissedSession"
+ "failureInUse"
+ "failureNotRecognized"
+ "failureNotUnlocked"
+ "handleResolveRemoteStatusEffect(for:)"
+ "isHandoffReady: enableModelBasedRangingCapabilities"
+ "isHandoffReady: isAdvertisingDeviceClose"
+ "isHandoffReady: nearbyID exists"
+ "remoteStatus"
+ "requirePermissionToHandoffCall"
+ "resolveRemoteStatus"
+ "resolveRemoteStatusFailed( "
+ "resolveRemoteStatusSucceeded( "
+ "sessionReport"
+ "transferrableActivity(device:allowedTypes:)"
- " - no resolved PermissionToHandoff"
- "### %s No deviceModelCode?"
- "### Failed to decode response: %@"
- "### Failed to resolve permission: %@"
- "### Invalid call to "
- "### No active call, falling back to "
- "### No transferrableActivity?"
- "Determined policy: Automatic! "
- "Determined policy: Not Automatic: ("
- "Existing active transfer: "
- "Failed to cast payload to PermissionToHandoffRequest.Response"
- "HandoffNotPermitted"
- "HandoffV2 Impact"
- "Nearby Interaction"
- "No remoteTransportLink"
- "No response payload"
- "Prox Handoff Unintentional Trigger"
- "_failureEnabled"
- "com.apple.proximitycontroldemo"
- "handleResolvePermissionEffect(for:)"
- "initWithCallUUID:conversationUUID:isVideo:service:"
- "localizedUserMessage(deviceModelCode:)"
- "permissionToHandoff"
- "resolvePermission"
- "resolvedPermission( "
- "transferrableActivity(device:allowedTypes:): "
- "unlockNeededPrompt"

```
