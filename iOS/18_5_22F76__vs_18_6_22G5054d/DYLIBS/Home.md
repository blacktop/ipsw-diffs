## Home

> `/System/Library/PrivateFrameworks/Home.framework/Home`

```diff

-1026.6.29.1.2
-  __TEXT.__text: 0x35ecf4
+1026.7.14.0.0
+  __TEXT.__text: 0x35f8f4
   __TEXT.__auth_stubs: 0x3200
-  __TEXT.__objc_methlist: 0x2b1f4
-  __TEXT.__const: 0x2c80
+  __TEXT.__objc_methlist: 0x2b224
+  __TEXT.__const: 0x3220
   __TEXT.__dlopen_cstrs: 0x4b
-  __TEXT.__cstring: 0x33101
+  __TEXT.__cstring: 0x33166
   __TEXT.__swift5_typeref: 0x1d0e
   __TEXT.__swift5_reflstr: 0x774
   __TEXT.__swift5_assocty: 0x288

   __TEXT.__swift5_proto: 0x180
   __TEXT.__swift5_types: 0xd0
   __TEXT.__swift5_capture: 0x814
-  __TEXT.__oslogstring: 0x1ae11
+  __TEXT.__oslogstring: 0x1b08e
   __TEXT.__swift_as_entry: 0x17c
   __TEXT.__swift_as_ret: 0x19c
   __TEXT.__swift5_protos: 0x34

   __TEXT.__unwind_info: 0xd288
   __TEXT.__eh_frame: 0x5b68
   __TEXT.__objc_classname: 0x69cf
-  __TEXT.__objc_methname: 0x57d3e
+  __TEXT.__objc_methname: 0x57daa
   __TEXT.__objc_methtype: 0x74b1
-  __TEXT.__objc_stubs: 0x392c0
-  __DATA_CONST.__got: 0x2d98
+  __TEXT.__objc_stubs: 0x392e0
+  __DATA_CONST.__got: 0x2da8
   __DATA_CONST.__const: 0x10db8
   __DATA_CONST.__objc_classlist: 0x1788
   __DATA_CONST.__objc_catlist: 0x400
   __DATA_CONST.__objc_protolist: 0x828
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12238
+  __DATA_CONST.__objc_selrefs: 0x12258
   __DATA_CONST.__objc_protorefs: 0x320
   __DATA_CONST.__objc_superrefs: 0x1308
   __DATA_CONST.__objc_arraydata: 0x380
   __AUTH_CONST.__auth_got: 0x1910
   __AUTH_CONST.__const: 0xd6d0
   __AUTH_CONST.__cfstring: 0x25e00
-  __AUTH_CONST.__objc_const: 0x49ce0
+  __AUTH_CONST.__objc_const: 0x49d00
   __AUTH_CONST.__objc_intobj: 0x2178
   __AUTH_CONST.__objc_doubleobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x258

   __AUTH.__objc_data: 0x9b78
   __AUTH.__data: 0xb10
   __DATA.__objc_ivar: 0x14fc
-  __DATA.__data: 0x71c0
+  __DATA.__data: 0x6be8
   __DATA.__objc_stublist: 0x10
   __DATA.__bss: 0x2668
   __DATA.__common: 0x118
   __DATA_DIRTY.__objc_ivar: 0xcb4
   __DATA_DIRTY.__objc_data: 0x5f68
-  __DATA_DIRTY.__data: 0x418
+  __DATA_DIRTY.__data: 0x408
   __DATA_DIRTY.__bss: 0x18d8
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 0F534288-4939-364B-B20F-952C12C018FF
-  Functions: 19472
-  Symbols:   55694
-  CStrings:  27808
+  UUID: C4A277F5-37F3-3D3E-9D7D-AE6191138484
+  Functions: 19474
+  Symbols:   55699
+  CStrings:  27817
 
Symbols:
+ -[HFItemManager(HomeKitDelegates) accessory:didUpdateHH1EOLEnabled:]
+ -[HMAccessory(HFMediaAdditions) hf_isHH1EOLEnabled]
+ GCC_except_table104
+ ___55-[HFHomeKitDispatcher _setupLocationSensingCoordinator]_block_invoke.605
+ ___block_literal_global.514
+ ___block_literal_global.517
+ ___block_literal_global.546
+ ___block_literal_global.567
+ ___block_literal_global.576
+ ___block_literal_global.614
+ ___block_literal_global.627
+ _objc_msgSend$isHH1EOLEnabled
- GCC_except_table103
- GCC_except_table179
- GCC_except_table87
- ___55-[HFHomeKitDispatcher _setupLocationSensingCoordinator]_block_invoke.603
- ___block_literal_global.512
- ___block_literal_global.515
- ___block_literal_global.544
- ___block_literal_global.565
- ___block_literal_global.574
- ___block_literal_global.612
- ___block_literal_global.625
CStrings:
+ "%@ (%{public}@): Failed to update face recognition enabled(%d) for person manager %@ with error %@"
+ "%s Matter snapshot changed, but does not match current home. Snapshot: %{public}s, current home controller ID: %{public}s, current home ID: %{public}s"
+ "%s Triggering item update because Matter snapshot changed. snapshot: (%{public}s) items: %{public}s devices: (%{public}s)"
+ "(%s) Among %@, wallet key device states of compatible paired watches are %@ | uniqueIdentifier = %{public}@"
+ "(%s) Returning %{BOOL}d because current device and paired watches are not wallet key compatible | uniqueIdentifier = %{public}@"
+ "(%s) Returning NO for wallet key compatibility for current device because of %@ | uniqueIdentifier = %{public}@"
+ "(%s) accessory %@ (uniqueIdentifier: %{public}@) | hh1EOLEnabled = %{BOOL}d"
+ "-[HFItemManager(HomeKitDelegates) accessory:didUpdateHH1EOLEnabled:]"
+ "Home %@ (%{public}@) does not have any resident device, which is required for Face Recognition feature"
+ "No cameras in home %@ (%{public}@) support recording"
+ "Successfully turned on has onboarded for access code flag for home %@ (%{public}@)"
+ "When turning on has onboarded for access code flag for home %@ (%{public}@), error occurred: %@"
+ "[hf_hasReachableResidents] Total residents: %lu - Reachable: %@ | home = %@ (%{public}@)"
+ "[hf_shouldBlockCurrentUserFromHomeForRoarUpgrade] User is blocked from home. HMHomeAccessNotAllowedReasonCode %lu | home = %@ (%{public}@)"
+ "accessory:didUpdateHH1EOLEnabled:"
+ "hf_isHH1EOLEnabled"
+ "isHH1EOLEnabled"
+ "registerMatterDelegates()"
+ "residentDevice:didUpdateHH1EOLEnabled:"
- "%@: Failed to update face recognition enabled(%d) for person manager %@ with error %@"
- "%@:%@ Total residents: %lu - Reachable: %@"
- "(%@:%s) Among %@, wallet key device states of compatible paired watches are %@"
- "(%@:%s) Returning %{BOOL}d because current device and paired watches are not wallet key compatible"
- "(%@:%s) Returning NO for wallet key compatibility for current device because of %@"
- "Home %@ does not have any resident device, which is required for Face Recognition feature"
- "No cameras in home %@ support recording"
- "Successfully turned on has onboarded for access code flag for home %@"
- "User is blocked from home. HMHomeAccessNotAllowedReasonCode %lu"
- "When turning on has onboarded for access code flag for home %@, error occurred: %@"

```
