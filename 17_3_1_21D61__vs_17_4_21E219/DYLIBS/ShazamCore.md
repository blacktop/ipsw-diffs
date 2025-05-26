## ShazamCore

> `/System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore`

```diff

-236.16.0.0.0
-  __TEXT.__text: 0x8e50
+238.15.0.0.0
+  __TEXT.__text: 0x9adc
   __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_methlist: 0xcc4
-  __TEXT.__const: 0x72
-  __TEXT.__cstring: 0x94a
-  __TEXT.__oslogstring: 0x50a
-  __TEXT.__gcc_except_tab: 0xe4
+  __TEXT.__objc_methlist: 0xdac
+  __TEXT.__const: 0x7a
+  __TEXT.__cstring: 0xa16
+  __TEXT.__oslogstring: 0x4fb
+  __TEXT.__gcc_except_tab: 0xf4
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x374
+  __TEXT.__unwind_info: 0x3c0
   __TEXT.__eh_frame: 0x80
-  __TEXT.__objc_classname: 0x1e4
-  __TEXT.__objc_methname: 0x2692
-  __TEXT.__objc_methtype: 0x4f0
-  __TEXT.__objc_stubs: 0x1d60
+  __TEXT.__objc_classname: 0x20f
+  __TEXT.__objc_methname: 0x2a14
+  __TEXT.__objc_methtype: 0x53a
+  __TEXT.__objc_stubs: 0x1e60
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x498
-  __DATA_CONST.__objc_classlist: 0xc8
+  __DATA_CONST.__const: 0x578
+  __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1780
-  __DATA_CONST.__objc_selrefs: 0x9d0
-  __AUTH_CONST.__cfstring: 0xce0
-  __AUTH_CONST.__objc_const: 0x8a8
+  __DATA_CONST.__objc_const: 0x18f0
+  __DATA_CONST.__objc_selrefs: 0xa40
+  __DATA_CONST.__objc_classrefs: 0x190
+  __DATA_CONST.__objc_superrefs: 0x98
+  __AUTH_CONST.__cfstring: 0xda0
+  __AUTH_CONST.__objc_const: 0x938
   __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__auth_got: 0x2a0
-  __AUTH.__objc_data: 0x7d0
-  __DATA.__objc_classrefs: 0x180
-  __DATA.__objc_superrefs: 0x88
-  __DATA.__objc_ivar: 0xd0
+  __AUTH.__objc_data: 0x870
+  __DATA.__objc_ivar: 0xe0
   __DATA.__data: 0x120
   __DATA.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
-  Functions: 293
-  Symbols:   1278
-  CStrings:  703
+  Functions: 320
+  Symbols:   1365
+  CStrings:  740
 
Symbols:
+ -[SHAMPConfiguration .cxx_destruct]
+ -[SHAMPConfiguration initWithResponse:]
+ -[SHAMPConfiguration offerResponseFromResponse:]
+ -[SHAMPConfiguration offers]
+ -[SHAMPConfiguration streamingProvidersResponseFromResponse:]
+ -[SHAMPConfiguration streamingProviders]
+ -[SHAMPConfigurationRequester .cxx_destruct]
+ -[SHAMPConfigurationRequester configurationEndpoint:]
+ -[SHAMPConfigurationRequester endpointURLWithHost:path:storefront:]
+ -[SHAMPConfigurationRequester fetchOffersAtURL:completionHandler:]
+ -[SHAMPConfigurationRequester fetchShazamAMPConfiguration:completionHandler:]
+ -[SHAMPConfigurationRequester fetchStreamingProvidersAtURL:completionHandler:]
+ -[SHAMPConfigurationRequester offersWithCompletion:]
+ -[SHAMPConfigurationRequester storefront]
+ -[SHAMPConfigurationRequester streamingProvidersWithCompletion:]
+ -[SHBagContract booleanBackedByStringForKey:completionHandler:]
+ -[SHBagContract doubleBackedByStringForKey:completionHandler:]
+ -[SHBagContract integerBackedByStringForKey:completionHandler:]
+ -[SHBagContract stringForKey:withCompletionHandler:]
+ -[SHBagContract valueForKey:bagValue:completionHandler:]
+ -[SHRemoteConfiguration configurationRequester]
+ -[SHRemoteConfiguration setShazamAMPConfigurationAPIEndpointsBagValue:]
+ -[SHRemoteConfiguration shazamAMPConfigurationAPIEndpointsBagValue]
+ -[SHRemoteConfiguration shazamAMPConfigurationAPIHostWithCompletion:]
+ -[SHRemoteConfiguration streamingProviderValuesWithCompletion:]
+ -[SHStreamingProviders .cxx_destruct]
+ -[SHStreamingProviders availableBundleIdentifiers]
+ -[SHStreamingProviders availableStreamingProviders]
+ -[SHStreamingProviders buildStreamingProvidersFromResponseArray:]
+ -[SHStreamingProviders initWithResponse:]
+ -[SHStreamingProviders providerNameForBundleID:]
+ -[SHStreamingProviders providersKeyedByBundleID]
+ -[SHStreamingProviders searchURLForBundleID:title:artist:]
+ -[SHStreamingProviders songURIForBundleID:]
+ -[SHStreamingProviders streamingProviderForBundleID:]
+ GCC_except_table4
+ GCC_except_table6
+ _OBJC_CLASS_$_SHAMPConfiguration
+ _OBJC_CLASS_$_SHAMPConfigurationRequester
+ _OBJC_CLASS_$_SHStreamingProviders
+ _OBJC_IVAR_$_SHAMPConfiguration._offers
+ _OBJC_IVAR_$_SHAMPConfiguration._streamingProviders
+ _OBJC_IVAR_$_SHAMPConfigurationRequester._storefront
+ _OBJC_IVAR_$_SHRemoteConfiguration._configurationRequester
+ _OBJC_IVAR_$_SHRemoteConfiguration._shazamAMPConfigurationAPIEndpointsBagValue
+ _OBJC_IVAR_$_SHStreamingProviders._providersKeyedByBundleID
+ _OBJC_METACLASS_$_SHAMPConfiguration
+ _OBJC_METACLASS_$_SHAMPConfigurationRequester
+ _OBJC_METACLASS_$_SHStreamingProviders
+ _SHRecordingSignatureOffsetDefaultValue
+ __OBJC_$_INSTANCE_METHODS_SHAMPConfiguration
+ __OBJC_$_INSTANCE_METHODS_SHAMPConfigurationRequester
+ __OBJC_$_INSTANCE_METHODS_SHStreamingProviders
+ __OBJC_$_INSTANCE_VARIABLES_SHAMPConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_SHAMPConfigurationRequester
+ __OBJC_$_INSTANCE_VARIABLES_SHStreamingProviders
+ __OBJC_$_PROP_LIST_SHAMPConfiguration
+ __OBJC_$_PROP_LIST_SHAMPConfigurationRequester
+ __OBJC_$_PROP_LIST_SHStreamingProviders
+ __OBJC_CLASS_RO_$_SHAMPConfiguration
+ __OBJC_CLASS_RO_$_SHAMPConfigurationRequester
+ __OBJC_CLASS_RO_$_SHStreamingProviders
+ __OBJC_METACLASS_RO_$_SHAMPConfiguration
+ __OBJC_METACLASS_RO_$_SHAMPConfigurationRequester
+ __OBJC_METACLASS_RO_$_SHStreamingProviders
+ ___52-[SHAMPConfigurationRequester offersWithCompletion:]_block_invoke
+ ___53-[SHAMPConfigurationRequester configurationEndpoint:]_block_invoke
+ ___53-[SHAMPConfigurationRequester configurationEndpoint:]_block_invoke_2
+ ___53-[SHAMPConfigurationRequester configurationEndpoint:]_block_invoke_3
+ ___56-[SHBagContract valueForKey:bagValue:completionHandler:]_block_invoke
+ ___62-[SHBagContract doubleBackedByStringForKey:completionHandler:]_block_invoke
+ ___62-[SHBagContract doubleBackedByStringForKey:completionHandler:]_block_invoke_2
+ ___63-[SHBagContract booleanBackedByStringForKey:completionHandler:]_block_invoke
+ ___63-[SHBagContract booleanBackedByStringForKey:completionHandler:]_block_invoke_2
+ ___63-[SHBagContract integerBackedByStringForKey:completionHandler:]_block_invoke
+ ___63-[SHBagContract integerBackedByStringForKey:completionHandler:]_block_invoke_2
+ ___63-[SHRemoteConfiguration streamingProviderValuesWithCompletion:]_block_invoke
+ ___64-[SHAMPConfigurationRequester streamingProvidersWithCompletion:]_block_invoke
+ ___66-[SHAMPConfigurationRequester fetchOffersAtURL:completionHandler:]_block_invoke
+ ___69-[SHRemoteConfiguration shazamAMPConfigurationAPIHostWithCompletion:]_block_invoke
+ ___77-[SHAMPConfigurationRequester fetchShazamAMPConfiguration:completionHandler:]_block_invoke
+ ___78-[SHAMPConfigurationRequester fetchStreamingProvidersAtURL:completionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e20_v24?08"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e40_v24?0"SHAMPConfiguration"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e42_v24?0"SHStreamingProviders"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32bs40w_e27_v24?0"NSURL"8"NSError"16lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e23_v28?08B16"NSError"20ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e18_v16?0"NSString"8ls32l8s40l8s48l8s64l8s56l8
+ ___block_literal_global.45
+ ___block_literal_global.47
+ ___block_literal_global.49
+ ___block_literal_global.51
+ ___block_literal_global.53
+ ___block_literal_global.55
+ ___block_literal_global.57
+ ___block_literal_global.59
+ ___block_literal_global.61
+ ___block_literal_global.63
+ _objc_msgSend$allKeys
+ _objc_msgSend$buildStreamingProvidersFromResponseArray:
+ _objc_msgSend$configurationEndpoint:
+ _objc_msgSend$configurationRequester
+ _objc_msgSend$fetchShazamAMPConfiguration:completionHandler:
+ _objc_msgSend$fetchStreamingProvidersAtURL:completionHandler:
+ _objc_msgSend$initWithResponse:
+ _objc_msgSend$offerResponseFromResponse:
+ _objc_msgSend$offers
+ _objc_msgSend$providersKeyedByBundleID
+ _objc_msgSend$shazamAMPConfigurationAPIEndpointsBagValue
+ _objc_msgSend$shazamAMPConfigurationAPIHostWithCompletion:
+ _objc_msgSend$songURIForBundleID:
+ _objc_msgSend$streamingProviderForBundleID:
+ _objc_msgSend$streamingProviders
+ _objc_msgSend$streamingProvidersResponseFromResponse:
+ _objc_msgSend$streamingProvidersWithCompletion:
+ _objc_msgSend$valueForKey:bagValue:completionHandler:
- -[SHBagContract booleanBackedByStringForKey:]
- -[SHBagContract booleanForKey:]
- -[SHBagContract doubleBackedByStringForKey:]
- -[SHBagContract doubleForKey:]
- -[SHBagContract integerBackedByStringForKey:]
- -[SHBagContract integerForKey:]
- -[SHBagContract stringForKey:]
- -[SHBagContract valueForKey:bagValue:]
- -[SHOffers appleMusicOffers]
- -[SHOffersNetworkRequester .cxx_destruct]
- -[SHOffersNetworkRequester endpointURLWithHost:path:storefront:]
- -[SHOffersNetworkRequester fetchOffersAtURL:completionHandler:]
- -[SHOffersNetworkRequester offersWithCompletion:]
- -[SHOffersNetworkRequester storefront]
- -[SHRemoteConfiguration setShazamOfferAPIEndpointsBagValue:]
- -[SHRemoteConfiguration shazamOfferAPIEndpointsBagValue]
- -[SHRemoteConfiguration shazamOfferAPIHostWithCompletion:]
- _OBJC_CLASS_$_SHOffersNetworkRequester
- _OBJC_IVAR_$_SHOffersNetworkRequester._storefront
- _OBJC_IVAR_$_SHRemoteConfiguration._shazamOfferAPIEndpointsBagValue
- _OBJC_METACLASS_$_SHOffersNetworkRequester
- __OBJC_$_INSTANCE_METHODS_SHOffersNetworkRequester
- __OBJC_$_INSTANCE_VARIABLES_SHOffersNetworkRequester
- __OBJC_$_PROP_LIST_SHOffersNetworkRequester
- __OBJC_CLASS_RO_$_SHOffersNetworkRequester
- __OBJC_METACLASS_RO_$_SHOffersNetworkRequester
- ___44-[SHBagContract doubleBackedByStringForKey:]_block_invoke
- ___45-[SHBagContract booleanBackedByStringForKey:]_block_invoke
- ___45-[SHBagContract integerBackedByStringForKey:]_block_invoke
- ___49-[SHOffersNetworkRequester offersWithCompletion:]_block_invoke
- ___49-[SHOffersNetworkRequester offersWithCompletion:]_block_invoke_2
- ___49-[SHOffersNetworkRequester offersWithCompletion:]_block_invoke_3
- ___58-[SHRemoteConfiguration shazamOfferAPIHostWithCompletion:]_block_invoke
- ___63-[SHOffersNetworkRequester fetchOffersAtURL:completionHandler:]_block_invoke
- ___block_descriptor_72_e8_32s40s48s56bs64w_e18_v16?0"NSString"8ls32l8s40l8s48l8s56l8w64l8
- ___block_literal_global.44
- ___block_literal_global.46
- ___block_literal_global.48
- ___block_literal_global.50
- ___block_literal_global.52
- ___block_literal_global.54
- ___block_literal_global.56
- ___block_literal_global.58
- ___block_literal_global.60
- ___block_literal_global.62
- _objc_msgSend$appleMusicOffers
- _objc_msgSend$boolForKey:
- _objc_msgSend$doubleForKey:
- _objc_msgSend$integerForKey:
- _objc_msgSend$promise
- _objc_msgSend$resultWithTimeout:error:
- _objc_msgSend$shazamOfferAPIEndpointsBagValue
- _objc_msgSend$shazamOfferAPIHostWithCompletion:
- _objc_msgSend$valueForKey:bagValue:
- _objc_msgSend$valueWithError:
CStrings:
+ "\r"
+ "@\"SHAMPConfigurationRequester\""
+ "@\"SHOffers\""
+ "@\"SHStreamingProviders\""
+ "SHAMPConfiguration"
+ "SHAMPConfigurationRequester"
+ "SHStreamingProviders"
+ "T@\"AMSBagValue\",&,N,V_shazamAMPConfigurationAPIEndpointsBagValue"
+ "T@\"NSDictionary\",R,N,V_providersKeyedByBundleID"
+ "T@\"NSString\",?,R,C"
+ "T@\"SHAMPConfigurationRequester\",R,N,V_configurationRequester"
+ "T@\"SHOffers\",R,N,V_offers"
+ "T@\"SHStreamingProviders\",R,N,V_streamingProviders"
+ "Third party streaming providers fetch complete with value %@ error %@"
+ "_configurationRequester"
+ "_offers"
+ "_providersKeyedByBundleID"
+ "_shazamAMPConfigurationAPIEndpointsBagValue"
+ "_streamingProviders"
+ "allKeys"
+ "availableBundleIdentifiers"
+ "availableStreamingProviders"
+ "booleanBackedByStringForKey:completionHandler:"
+ "buildStreamingProvidersFromResponseArray:"
+ "bundleIdentifier"
+ "com.apple.shazam.ShazamKit"
+ "configurationEndpoint:"
+ "configurationRequester"
+ "doubleBackedByStringForKey:completionHandler:"
+ "fetchShazamAMPConfiguration:completionHandler:"
+ "fetchStreamingProvidersAtURL:completionHandler:"
+ "initWithResponse:"
+ "integerBackedByStringForKey:completionHandler:"
+ "offerResponseFromResponse:"
+ "offers"
+ "providerName"
+ "providerNameForBundleID:"
+ "providersKeyedByBundleID"
+ "searchURLForBundleID:title:artist:"
+ "setShazamAMPConfigurationAPIEndpointsBagValue:"
+ "shazamAMPConfigurationAPIEndpointsBagValue"
+ "shazamAMPConfigurationAPIHostWithCompletion:"
+ "songURI"
+ "songURIForBundleID:"
+ "streamingProviderForBundleID:"
+ "streamingProviderValuesWithCompletion:"
+ "streamingProviders"
+ "streamingProvidersResponseFromResponse:"
+ "streamingProvidersWithCompletion:"
+ "stringForKey:withCompletionHandler:"
+ "v24@?0@\"NSURL\"8@\"NSError\"16"
+ "v24@?0@\"SHAMPConfiguration\"8@\"NSError\"16"
+ "v24@?0@\"SHStreamingProviders\"8@\"NSError\"16"
+ "v24@?0@8@\"NSError\"16"
+ "v40@0:8@16@24@?32"
+ "valueForKey:bagValue:completionHandler:"
+ "{album}"
+ "{artist}"
+ "{title}"
- "\f"
- "%@ waited but did not get recorder config in time, using defaults"
- "Fetching offers..."
- "SHOffersNetworkRequester"
- "T@\"AMSBagValue\",&,N,V_shazamOfferAPIEndpointsBagValue"
- "_shazamOfferAPIEndpointsBagValue"
- "boolForKey:"
- "booleanBackedByStringForKey:"
- "booleanForKey:"
- "com.apple.ShazamKit"
- "com.shazam.Shazam"
- "d24@0:8@16"
- "doubleBackedByStringForKey:"
- "doubleForKey:"
- "integerBackedByStringForKey:"
- "integerForKey:"
- "resultWithTimeout:error:"
- "setShazamOfferAPIEndpointsBagValue:"
- "shazamOfferAPIEndpointsBagValue"
- "shazamOfferAPIHostWithCompletion:"
- "valueForKey:bagValue:"
- "valueWithError:"

```
