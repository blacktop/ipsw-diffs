## findmylocated

> `/usr/libexec/findmylocated`

```diff

-116.30.6.9.17
-  __TEXT.__text: 0x481b74
-  __TEXT.__auth_stubs: 0x53d0
+116.30.6.9.19
+  __TEXT.__text: 0x484a38
+  __TEXT.__auth_stubs: 0x5410
   __TEXT.__objc_methlist: 0xcac
-  __TEXT.__const: 0x19f80
-  __TEXT.__cstring: 0xd992
-  __TEXT.__swift5_typeref: 0x641e
-  __TEXT.__constg_swiftt: 0x6468
+  __TEXT.__const: 0x1a050
+  __TEXT.__cstring: 0xda02
+  __TEXT.__swift5_typeref: 0x64ba
+  __TEXT.__constg_swiftt: 0x6478
   __TEXT.__swift5_builtin: 0x12c
   __TEXT.__swift5_reflstr: 0x7593
   __TEXT.__swift5_fieldmd: 0x7fd0
   __TEXT.__swift5_assocty: 0x988
-  __TEXT.__objc_methname: 0x291f
+  __TEXT.__objc_methname: 0x2941
   __TEXT.__swift5_proto: 0x1544
   __TEXT.__swift5_types: 0x6a8
   __TEXT.__objc_classname: 0x138
   __TEXT.__objc_methtype: 0x900
   __TEXT.__swift5_protos: 0x48
   __TEXT.__swift5_mpenum: 0x38
-  __TEXT.__oslogstring: 0x17e2c
-  __TEXT.__swift_as_entry: 0x1248
-  __TEXT.__swift_as_ret: 0x1f70
-  __TEXT.__swift5_capture: 0x44a0
+  __TEXT.__oslogstring: 0x17f8c
+  __TEXT.__swift_as_entry: 0x128c
+  __TEXT.__swift_as_ret: 0x1fac
+  __TEXT.__swift5_capture: 0x4550
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x12c80
-  __TEXT.__eh_frame: 0x3b4ac
-  __DATA_CONST.__auth_got: 0x29e8
-  __DATA_CONST.__got: 0x1bc0
-  __DATA_CONST.__auth_ptr: 0x17c8
-  __DATA_CONST.__const: 0x150a8
+  __TEXT.__unwind_info: 0x12de8
+  __TEXT.__eh_frame: 0x3bc24
+  __DATA_CONST.__auth_got: 0x2a08
+  __DATA_CONST.__got: 0x1bd8
+  __DATA_CONST.__auth_ptr: 0x17d0
+  __DATA_CONST.__const: 0x15120
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0x55d0
   __DATA.__objc_selrefs: 0xbc0
   __DATA.__objc_data: 0x10d8
-  __DATA.__data: 0xd2d8
+  __DATA.__data: 0xd320
   __DATA.__bss: 0x29600
   __DATA.__common: 0x1360
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4E17BAA6-408D-30F0-8DF2-659033372E8A
-  Functions: 15377
-  Symbols:   2652
-  CStrings:  3586
+  UUID: 67AF423B-86B7-332D-8812-4FF0877ED3C4
+  Functions: 15441
+  Symbols:   2659
+  CStrings:  3592
 
Symbols:
+ _$s10FindMyBase12TimeoutErrorVMa
+ _$s10FindMyBase12TimeoutErrorVs0E0AAMc
+ _$s10FindMyBase13WorkItemQueueC7enqueueyAC0dE0CyyYaYbKcFTj
+ _$s23FindMyServerInteraction0cD10ControllerC4send8endpoint7content10credential17pinningCredentialAA8ResponseVAA8Endpoint_p_AA27RequestContentRepresentable_pAA0nK0_pSgAA07PinningK0_pSgtYaKFTjTu
+ _$s23FindMyServerInteraction0cD10ControllerC4send8endpoint7content10credentialAA8ResponseVAA8Endpoint_p_AA27RequestContentRepresentable_pAA0L10Credential_pSgtYaKF
+ _$s23FindMyServerInteraction0cD10ControllerC4send8endpoint7content10credentialAA8ResponseVAA8Endpoint_p_AA27RequestContentRepresentable_pAA0L10Credential_pSgtYaKFTu
+ _$s23FindMyServerInteraction0cD10ControllerC6upload8endpoint7content10credentialAA8ResponseVAA8Endpoint_p_AA30FileUploadContentRepresentable_pAA17RequestCredential_pSgtYaKF
+ _$s23FindMyServerInteraction0cD10ControllerC6upload8endpoint7content10credentialAA8ResponseVAA8Endpoint_p_AA30FileUploadContentRepresentable_pAA17RequestCredential_pSgtYaKFTu
+ _$s23FindMyServerInteraction17PinningCredentialMp
- _$s23FindMyServerInteraction0cD10ControllerC4send8endpoint7content10credentialAA8ResponseVAA8Endpoint_p_AA27RequestContentRepresentable_pAA0L10Credential_pSgtYaKFTjTu
- _$s23FindMyServerInteraction0cD10ControllerC6upload8endpoint7content10credentialAA8ResponseVAA8Endpoint_p_AA30FileUploadContentRepresentable_pAA17RequestCredential_pSgtYaKFTjTu
CStrings:
+ "    %s: AutoMe threshold is active, don't publish live locations. \n    Proceed to communicate location & connected devices to server."
+ "%s: AutoMe threshold is active, don't publish live locations. Proceed to communicate location & connected devices to server."
+ "%s: Proceeding with LiveLocations check"
+ "%s: skipUpdate %{bool}d, forceSave %{bool}d"
+ "Nearby Interaction call timed out after %lld milliseconds"
+ "canAcceptRequestForLiveSession()"
+ "getAsyncActivelyInteractingDiscoveryTokens:"
+ "getAsyncInteractableDiscoveryTokens:"
+ "https://findmyservice-prod.me.com/internal/mas/submit"
+ "niSessionWorkItemQueue"
+ "saveLocation(locations:returnOnlyPersisted:completion:)"
+ "setAsyncLocalDeviceInteractableDiscoveryTokens:completion:"
- "%s: Location monitoring void due to being in threshold period for autoMe"
- "activelyInteractingDiscoveryTokens"
- "https://findmyservice.me.com/internal/mas/submit"
- "interactableDiscoveryTokens"
- "niSessionSerialQueue"
- "setLocalDeviceInteractableDiscoveryTokens:"

```
