## BusinessServices

> `/System/Library/PrivateFrameworks/BusinessServices.framework/BusinessServices`

```diff

-30095.35.3.18.4
-  __TEXT.__text: 0x21964
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_methlist: 0x7a4
-  __TEXT.__swift5_typeref: 0x8ba
-  __TEXT.__const: 0x1178
-  __TEXT.__swift5_reflstr: 0x661
-  __TEXT.__swift5_assocty: 0x60
-  __TEXT.__swift5_fieldmd: 0x6ec
-  __TEXT.__constg_swiftt: 0xda0
-  __TEXT.__cstring: 0xde9
+30109.30.5.20.1
+  __TEXT.__text: 0x29060
+  __TEXT.__auth_stubs: 0xeb0
+  __TEXT.__objc_methlist: 0x944
+  __TEXT.__const: 0x1888
+  __TEXT.__swift5_typeref: 0xa26
+  __TEXT.__swift5_reflstr: 0x771
+  __TEXT.__swift5_assocty: 0xc0
+  __TEXT.__constg_swiftt: 0xf68
+  __TEXT.__swift5_fieldmd: 0x9c0
   __TEXT.__swift5_builtin: 0x50
+  __TEXT.__cstring: 0xfe8
   __TEXT.__swift5_protos: 0x34
-  __TEXT.__swift5_proto: 0xb8
-  __TEXT.__swift5_types: 0x94
-  __TEXT.__swift_as_entry: 0x48
-  __TEXT.__swift_as_ret: 0x44
-  __TEXT.__swift5_capture: 0x2ec
-  __TEXT.__oslogstring: 0xa40
-  __TEXT.__unwind_info: 0x918
-  __TEXT.__eh_frame: 0x9a0
-  __TEXT.__objc_classname: 0xc8
-  __TEXT.__objc_methname: 0xefc
-  __TEXT.__objc_methtype: 0x3a3
-  __TEXT.__objc_stubs: 0x760
-  __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0x150
+  __TEXT.__swift5_proto: 0x118
+  __TEXT.__swift5_types: 0xac
+  __TEXT.__swift_as_entry: 0x54
+  __TEXT.__swift_as_ret: 0x50
+  __TEXT.__swift5_capture: 0x464
+  __TEXT.__oslogstring: 0xb9a
+  __TEXT.__unwind_info: 0xc58
+  __TEXT.__eh_frame: 0xbf0
+  __TEXT.__objc_classname: 0xe7
+  __TEXT.__objc_methname: 0x112d
+  __TEXT.__objc_methtype: 0x482
+  __TEXT.__objc_stubs: 0x940
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__const: 0x170
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x538
+  __DATA_CONST.__objc_selrefs: 0x5d8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x670
-  __AUTH_CONST.__const: 0x11d8
-  __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0x14f0
-  __AUTH.__objc_data: 0x830
-  __AUTH.__data: 0xba0
+  __AUTH_CONST.__auth_got: 0x760
+  __AUTH_CONST.__const: 0x18a8
+  __AUTH_CONST.__cfstring: 0xa0
+  __AUTH_CONST.__objc_const: 0x1670
+  __AUTH.__objc_data: 0x640
+  __AUTH.__data: 0x920
   __DATA.__objc_ivar: 0x28
-  __DATA.__data: 0x5c8
-  __DATA.__bss: 0xf80
-  __DATA.__common: 0x40
-  __DATA_DIRTY.__data: 0x198
+  __DATA.__data: 0x5a8
+  __DATA.__bss: 0x1b00
+  __DATA.__common: 0x28
+  __DATA_DIRTY.__objc_data: 0x240
+  __DATA_DIRTY.__data: 0x670
+  __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 36AF5D90-E6AF-38E8-8E3E-E959D1638B8B
-  Functions: 905
-  Symbols:   833
-  CStrings:  414
+  UUID: 7C670AAD-1354-3A90-B72C-34BA4A9A1126
+  Functions: 1291
+  Symbols:   941
+  CStrings:  474
 
Symbols:
+ -[BSBrand brandInfo]
+ -[BSBrand brandType]
+ -[BSBrand primaryLogoURL]
+ -[BSBrand secondaryLogoURL]
+ -[BSBrand(OnDeviceSupport) appBundleID]
+ -[BSBrand(OnDeviceSupport) deepLinkURL]
+ -[BSBrand(OnDeviceSupport) fallBackURL]
+ -[BSBrand(WebPresentment) brandID]
+ -[BSBrand(WebPresentment) businessID]
+ -[BSBrand(WebPresentment) companyID]
+ -[BSBrand(WebPresentment) logoURL]
+ -[BSBrand(WebPresentment) permissions:completion:]
+ -[BSBrandManager brandAssetWithIdentifier:forService:completion:]
+ -[BSBrandManager brandWithIdentifier:forService:completion:]
+ -[BSBrandManager isBrandRegisteredWithIdentifier:forService:completion:]
+ -[BSBrandManager isBrandRegisteredWithIdentifier:forService:timeout:error:]
+ _BSBrandServiceTypeOnDeviceSupport
+ _BSBrandServiceTypeWebPresentment
+ __OBJC_$_CLASS_METHODS_BSBrand(BrandURI|Placeholder|OnDeviceSupport|WebPresentment)
+ __OBJC_$_CLASS_METHODS_BSBrandObjcShim(BusinessServices|BusinessServices1|BusinessServices2)
+ __OBJC_$_INSTANCE_METHODS_BSBrand(BrandURI|Placeholder|OnDeviceSupport|WebPresentment)
+ __OBJC_$_INSTANCE_METHODS_BSBrandObjcShim(BusinessServices|BusinessServices1|BusinessServices2)
+ ___60-[BSBrandManager brandWithIdentifier:forService:completion:]_block_invoke
+ ___65-[BSBrandManager brandAssetWithIdentifier:forService:completion:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e28_v24?0"NSData"8"NSError"16ls32l8
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_BusinessServices
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_BusinessServices
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_BusinessServices
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_BusinessServices
+ _associated conformance 16BusinessServices12GenericBrandV10CodingKeys33_FE9FACF63624755D20D66DF41BF92B19LLOSHAASQ
+ _associated conformance 16BusinessServices12GenericBrandV10CodingKeys33_FE9FACF63624755D20D66DF41BF92B19LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 16BusinessServices12GenericBrandV10CodingKeys33_FE9FACF63624755D20D66DF41BF92B19LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 16BusinessServices12GenericBrandVSHAASQ
+ _associated conformance 16BusinessServices12GenericBrandVs12IdentifiableAA2IDsADP_SH
+ _associated conformance 16BusinessServices9BrandTypeOSHAASQ
+ _associated conformance So18BSBrandServiceTypeaSHSCSQ
+ _associated conformance So18BSBrandServiceTypeas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So18BSBrandServiceTypeas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _block_copy_helper.14
+ _block_copy_helper.17
+ _block_copy_helper.24
+ _block_copy_helper.32
+ _block_copy_helper.41
+ _block_copy_helper.47
+ _block_copy_helper.53
+ _block_copy_helper.59
+ _block_copy_helper.62
+ _block_descriptor.16
+ _block_descriptor.19
+ _block_descriptor.26
+ _block_descriptor.34
+ _block_descriptor.43
+ _block_descriptor.49
+ _block_descriptor.55
+ _block_descriptor.61
+ _block_descriptor.64
+ _block_destroy_helper.15
+ _block_destroy_helper.18
+ _block_destroy_helper.25
+ _block_destroy_helper.33
+ _block_destroy_helper.42
+ _block_destroy_helper.48
+ _block_destroy_helper.54
+ _block_destroy_helper.60
+ _block_destroy_helper.63
+ _objc_autorelease
+ _objc_msgSend$appBundleID
+ _objc_msgSend$brandAssetWithIdentifier:forService:completion:
+ _objc_msgSend$brandInfo
+ _objc_msgSend$brandType
+ _objc_msgSend$brandWithIdentifier:forService:completion:
+ _objc_msgSend$businessID
+ _objc_msgSend$companyID
+ _objc_msgSend$deepLinkURL
+ _objc_msgSend$fallBackURL
+ _objc_msgSend$isBrandRegisteredWithIdentifier:forService:completion:
+ _objc_msgSend$isBrandRegisteredWithIdentifier:forService:timeout:error:
+ _objc_msgSend$logoURL
+ _objc_msgSend$permissions:completionHandler:
+ _objc_msgSend$primaryLogoURL
+ _objc_msgSend$secondaryLogoURL
+ _objc_retain_x25
+ _objc_retain_x27
+ _objectdestroy.13Tm
+ _swift_setDeallocating
+ _swift_unexpectedError
+ _symbolic $ss21_ObjectiveCBridgeableP
+ _symbolic SDyS2SG
+ _symbolic SDyS2SGSg
+ _symbolic SbSo7NSErrorCSgIegyg_
+ _symbolic Sbz_Xx
+ _symbolic ScCy___________pG 10Foundation4DataV s5ErrorP
+ _symbolic So6NSDataCSgSo7NSErrorCSgIeggg_
+ _symbolic So8NSStringC
+ _symbolic So8NSStringCSg
+ _symbolic _____ 16BusinessServices12GenericBrandV
+ _symbolic _____ 16BusinessServices12GenericBrandV10CodingKeys33_FE9FACF63624755D20D66DF41BF92B19LLO
+ _symbolic _____ 16BusinessServices27GenericBrandLogoURLProviderV
+ _symbolic _____ 16BusinessServices30WebPresentmentBrandDetailsKeysV
+ _symbolic _____ 16BusinessServices31OnDeviceSupportBrandDetailsKeysV
+ _symbolic _____ 16BusinessServices9BrandTypeO
+ _symbolic _____ So18BSBrandServiceTypea
+ _symbolic _____So7NSErrorCSgIeyByy_ 10ObjectiveC8ObjCBoolV
+ _symbolic ______pSg s5ErrorP
+ _symbolic ______pSgz_Xx s5ErrorP
+ _symbolic _____ySDySSSayy_____y______p_______pt______pGcGGG 2os21OSAllocatedUnfairLockV s6ResultOsRi_zRi0_zrlE 16BusinessServices10BrandModelP AF0H15LogoURLProviderP s5ErrorP
+ _symbolic _____ySDySSSayy_____y______p_______pt______pGcGG_____G s13ManagedBufferCsRi__rlE s6ResultOsRi_zRi0_zrlE 16BusinessServices10BrandModelP AE0F15LogoURLProviderP s5ErrorP So16os_unfair_lock_sV
+ _symbolic _____ySSSayy_____y______p_______pt______pGcGG s18_DictionaryStorageC s6ResultOsRi_zRi0_zrlE 16BusinessServices10BrandModelP AE0F15LogoURLProviderP s5ErrorP
+ _symbolic _____ySb______pGIegg_ s6ResultOsRi_zRi0_zrlE s5ErrorP
+ _symbolic _____y_____G s22KeyedDecodingContainerV 16BusinessServices12GenericBrandV10CodingKeys33_FE9FACF63624755D20D66DF41BF92B19LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 16BusinessServices12GenericBrandV10CodingKeys33_FE9FACF63624755D20D66DF41BF92B19LLO
+ _symbolic _____y___________pGIegg_ s6ResultOsRi_zRi0_zrlE 10Foundation4DataV s5ErrorP
+ _symbolic _____y___________pGIegg_ s6ResultOsRi_zRi0_zrlE 16BusinessServices5BrandC s5ErrorP
+ _symbolic _____y______p_______p______pSgt______pG s6ResultOsRi_zRi0_zrlE 16BusinessServices10BrandModelP AC0D15LogoURLProviderP AC0dF12DataProviderP s5ErrorP
+ _symbolic _____y______p_______p______pSgt______pGIegn_ s6ResultOsRi_zRi0_zrlE 16BusinessServices10BrandModelP AC0D15LogoURLProviderP AC0dF12DataProviderP s5ErrorP
+ _symbolic _____y______p_______pt______pG s6ResultOsRi_zRi0_zrlE 16BusinessServices10BrandModelP AC0D15LogoURLProviderP s5ErrorP
+ _symbolic _____y______p_______pt______pGIegn_ s6ResultOsRi_zRi0_zrlE 16BusinessServices10BrandModelP AC0D15LogoURLProviderP s5ErrorP
+ _symbolic _____yy_____y______p_______pt______pGcG s23_ContiguousArrayStorageC s6ResultOsRi_zRi0_zrlE 16BusinessServices10BrandModelP AE0G15LogoURLProviderP s5ErrorP
+ _type_layout_string So18BSBrandServiceTypea
- __INSTANCE_METHODS_BSBrandObjcShim
- __OBJC_$_CLASS_METHODS_BSBrand(BrandURI|Placeholder)
- __OBJC_$_CLASS_METHODS_BSBrandObjcShim(BusinessServices)
- __OBJC_$_INSTANCE_METHODS_BSBrand(BrandURI|Placeholder)
- __PROPERTIES_BSBrandObjcShim
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_BusinessServices
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_BusinessServices
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_BusinessServices
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_BusinessServices
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_BusinessServices
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_BusinessServices
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_BusinessServices
- _block_copy_helper.11
- _block_copy_helper.15
- _block_copy_helper.23
- _block_copy_helper.26
- _block_descriptor.13
- _block_descriptor.17
- _block_descriptor.25
- _block_descriptor.28
- _block_destroy_helper.12
- _block_destroy_helper.16
- _block_destroy_helper.24
- _block_destroy_helper.27
- _objc_retain_x26
- _objectdestroy.29Tm
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
- _symbolic _____ So15BSBrandLogoTypeV
- _symbolic _____ySDySSSayy_____y______p_______pt______pGcGGG 2os21OSAllocatedUnfairLockV s6ResultOsRi_zrlE 16BusinessServices10BrandModelP AF0H15LogoURLProviderP s5ErrorP
- _symbolic _____ySDySSSayy_____y______p_______pt______pGcGG_____G s13ManagedBufferCsRi__rlE s6ResultOsRi_zrlE 16BusinessServices10BrandModelP AE0F15LogoURLProviderP s5ErrorP So16os_unfair_lock_sV
- _symbolic _____ySSSayy_____y______p_______pt______pGcGG s18_DictionaryStorageC s6ResultOsRi_zrlE 16BusinessServices10BrandModelP AE0F15LogoURLProviderP s5ErrorP
- _symbolic _____y___________pGIegg_ s6ResultOsRi_zrlE 10Foundation4DataV s5ErrorP
- _symbolic _____y___________pGIegg_ s6ResultOsRi_zrlE 16BusinessServices5BrandC s5ErrorP
- _symbolic _____y______p_______p______pSgt______pG s6ResultOsRi_zrlE 16BusinessServices10BrandModelP AC0D15LogoURLProviderP AC0dF12DataProviderP s5ErrorP
- _symbolic _____y______p_______p______pSgt______pGIegn_ s6ResultOsRi_zrlE 16BusinessServices10BrandModelP AC0D15LogoURLProviderP AC0dF12DataProviderP s5ErrorP
- _symbolic _____y______p_______pt______pG s6ResultOsRi_zrlE 16BusinessServices10BrandModelP AC0D15LogoURLProviderP s5ErrorP
- _symbolic _____y______p_______pt______pGIegn_ s6ResultOsRi_zrlE 16BusinessServices10BrandModelP AC0D15LogoURLProviderP s5ErrorP
- _symbolic _____yy_____y______p_______pt______pGcG s23_ContiguousArrayStorageC s6ResultOsRi_zrlE 16BusinessServices10BrandModelP AE0G15LogoURLProviderP s5ErrorP
CStrings:
+ "B48@0:8@16@24d32^@40"
+ "BusinessServices/BrandService.swift"
+ "BusinessServices1"
+ "BusinessServices2"
+ "Error connecting to remote object: %@"
+ "Error fetching brand asset for Service %s Key %s Error: %s"
+ "Error fetching brand for Service %s Key %s Error: %s"
+ "Error fetching isBrandRegistered for Service %s Key %s Error: %s"
+ "OnDeviceSupport"
+ "SIM ID given is nil %@ "
+ "T@\"NSDictionary\",N,R"
+ "T@\"NSURL\",R,N"
+ "Tq,N,R"
+ "Tq,R,N"
+ "Unsupported asset type"
+ "WebPresentment"
+ "[%{public}s] Fetching brand asset with URI: %{public}s"
+ "[%{public}s] Fetching brand with URI: %{public}s"
+ "appBundleID"
+ "brandAssetWithIdentifier:forService:completion:"
+ "brandDataWithIdentifier:forService:completion:"
+ "brandID"
+ "brandInfo"
+ "brandType"
+ "brandWithIdentifier:forService:completion:"
+ "businessID"
+ "com.apple.businessservices.brandservice"
+ "companyID"
+ "deepLinkURL"
+ "fallBackURL"
+ "isBrandRegisteredWithIdentifier:forService:completion:"
+ "isBrandRegisteredWithIdentifier:forService:timeout:completion:"
+ "isBrandRegisteredWithIdentifier:forService:timeout:error:"
+ "logoURL"
+ "permissions:completion:"
+ "permissions:completionHandler:"
+ "primaryLogoURL"
+ "q16@0:8"
+ "secondaryLogoURL"
+ "serialQueue"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "v20@?0B8@\"NSError\"12"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
+ "v48@0:8@\"NSString\"16@\"NSString\"24d32@?<v@?B@\"NSError\">40"
+ "v48@0:8@16@24d32@?40"
- "No matching subscription for SIM ID %@"
- "SIM ID given is nil %@"
- "Unsupported logo type"

```
