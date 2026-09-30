## ShazamCore

> `/System/Library/PrivateFrameworks/ShazamCore.framework/Versions/A/ShazamCore`

```diff

-307.2.0.0.0
-  __TEXT.__text: 0xc494
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0xd88
-  __TEXT.__const: 0x82
-  __TEXT.__cstring: 0xcbc
-  __TEXT.__oslogstring: 0x49f
-  __TEXT.__gcc_except_tab: 0xf4
-  __TEXT.__swift5_typeref: 0x5e
+318.0.0.0.0
+  __TEXT.__text: 0xd914
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__objc_methlist: 0x1080
+  __TEXT.__const: 0x7a
+  __TEXT.__cstring: 0xd9c
+  __TEXT.__oslogstring: 0x577
+  __TEXT.__gcc_except_tab: 0x108
+  __TEXT.__swift5_typeref: 0x60
   __TEXT.__swift5_capture: 0x4c
-  __TEXT.__unwind_info: 0x438
+  __TEXT.__swift_as_entry: 0x14
+  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__unwind_info: 0x490
   __TEXT.__eh_frame: 0x258
-  __TEXT.__objc_classname: 0x1e7
-  __TEXT.__objc_methname: 0x27d1
-  __TEXT.__objc_methtype: 0x53c
-  __TEXT.__objc_stubs: 0x1c60
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x258
-  __DATA_CONST.__objc_classlist: 0xd0
+  __TEXT.__objc_classname: 0x235
+  __TEXT.__objc_methname: 0x2de4
+  __TEXT.__objc_methtype: 0x59e
+  __TEXT.__objc_stubs: 0x1e40
+  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__const: 0x250
+  __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9d0
-  __DATA_CONST.__objc_superrefs: 0x90
-  __AUTH_CONST.__auth_got: 0x338
-  __AUTH_CONST.__const: 0x590
-  __AUTH_CONST.__cfstring: 0xf40
-  __AUTH_CONST.__objc_const: 0x20c0
-  __AUTH.__objc_data: 0x840
+  __DATA_CONST.__objc_selrefs: 0xb38
+  __DATA_CONST.__objc_superrefs: 0xa8
+  __AUTH_CONST.__auth_got: 0x330
+  __AUTH_CONST.__const: 0x5b0
+  __AUTH_CONST.__cfstring: 0x10a0
+  __AUTH_CONST.__objc_const: 0x21a8
+  __AUTH.__objc_data: 0x930
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0xd4
+  __DATA.__objc_ivar: 0xf4
   __DATA.__data: 0x188
   __DATA.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 91A9454D-0B52-3570-B331-259EDC5A4C16
-  Functions: 358
-  Symbols:   1061
-  CStrings:  842
+  UUID: 97EA6104-EEA7-37BF-858A-179FA9EC596E
+  Functions: 398
+  Symbols:   1150
+  CStrings:  918
 
Symbols:
+ +[SHLocalization shFrameworkBundle].cold.1
+ +[SHRemoteConfiguration sharedInstance].cold.1
+ -[SHDefaultConfigurationValues liveAudioMinimumRecordingDuration]
+ -[SHHapticsConfiguration .cxx_destruct]
+ -[SHHapticsConfiguration baseURLString]
+ -[SHHapticsConfiguration fetchHapticsURLStringForClientIdentifier:songResourceIDType:]
+ -[SHHapticsConfiguration hapticsAvailableURLStringForClientIdentifier:songResourceIDType:]
+ -[SHHapticsConfiguration hapticsEndpointsForStorefront:clientIdentifier:]
+ -[SHHapticsConfiguration hapticsEndpoints]
+ -[SHHapticsConfiguration initWithConfiguration:]
+ -[SHHapticsConfiguration pathStringForClientIdentifier:songResourceIDType:requestKey:]
+ -[SHHapticsEndpoints .cxx_destruct]
+ -[SHHapticsEndpoints availabilityRequestForID:ofIDType:]
+ -[SHHapticsEndpoints fetchHapticByAdamIDURL]
+ -[SHHapticsEndpoints fetchHapticByISRCURL]
+ -[SHHapticsEndpoints fetchRequestForID:ofIDType:]
+ -[SHHapticsEndpoints hasHapticForAdamIDURL]
+ -[SHHapticsEndpoints hasHapticForISRCURL]
+ -[SHHapticsEndpoints initWithFetchHapticByAdamIDURL:hasHapticForAdamIDURL:fetchHapticByISRCURL:hasHapticForISRCURL:]
+ -[SHHapticsEndpoints requestOfType:forID:ofIDType:]
+ -[SHMusicalFeaturesBagConfiguration .cxx_destruct]
+ -[SHMusicalFeaturesBagConfiguration amsPromise]
+ -[SHMusicalFeaturesBagConfiguration availableModelsForClientIdentifier:]
+ -[SHMusicalFeaturesBagConfiguration configuration]
+ -[SHMusicalFeaturesBagConfiguration initWithConfiguration:]
+ -[SHMusicalFeaturesBagConfiguration initWithPromise:]
+ -[SHMusicalFeaturesBagConfiguration minimumDurationInSecondsForClientIdentifier:]
+ -[SHRemoteConfiguration hapticsEndpointsBagValue]
+ -[SHRemoteConfiguration hapticsWithCompletion:]
+ -[SHRemoteConfiguration musicalFeaturesBagConfigurationValue]
+ -[SHRemoteConfiguration musicalFeaturesBagConfigurationWithCompletion:]
+ -[SHRemoteConfiguration musicalFeaturesBagConfigurationWithPromise]
+ -[SHRemoteConfiguration setHapticsEndpointsBagValue:]
+ -[SHRemoteConfiguration setMusicalFeaturesBagConfigurationValue:]
+ -[SHTokenizedURL initWithBaseURL:URLPath:]
+ -[SHTokenizedURL initWithURLComponents:]
+ -[SHTokenizedURL originalComponents]
+ -[SHTokenizedURL originalURLString]
+ -[SHTokenizedURL path:containsToken:]
+ -[SHTokenizedURL tokenizedURLString]
+ GCC_except_table19
+ GCC_except_table28
+ OBJC_IVAR_$_SHHapticsConfiguration._hapticsEndpoints
+ OBJC_IVAR_$_SHHapticsEndpoints._fetchHapticByAdamIDURL
+ OBJC_IVAR_$_SHHapticsEndpoints._fetchHapticByISRCURL
+ OBJC_IVAR_$_SHHapticsEndpoints._hasHapticForAdamIDURL
+ OBJC_IVAR_$_SHHapticsEndpoints._hasHapticForISRCURL
+ OBJC_IVAR_$_SHMusicalFeaturesBagConfiguration._amsPromise
+ OBJC_IVAR_$_SHMusicalFeaturesBagConfiguration._configuration
+ OBJC_IVAR_$_SHRemoteConfiguration._hapticsEndpointsBagValue
+ OBJC_IVAR_$_SHRemoteConfiguration._musicalFeaturesBagConfigurationValue
+ OBJC_IVAR_$_SHTokenizedURL._originalComponents
+ _OBJC_CLASS_$_NSURLRequest
+ _OBJC_CLASS_$_SHHapticsConfiguration
+ _OBJC_CLASS_$_SHHapticsEndpoints
+ _OBJC_CLASS_$_SHMusicalFeaturesBagConfiguration
+ _OBJC_METACLASS_$_SHHapticsConfiguration
+ _OBJC_METACLASS_$_SHHapticsEndpoints
+ _OBJC_METACLASS_$_SHMusicalFeaturesBagConfiguration
+ __OBJC_$_INSTANCE_METHODS_SHHapticsConfiguration
+ __OBJC_$_INSTANCE_METHODS_SHHapticsEndpoints
+ __OBJC_$_INSTANCE_METHODS_SHMusicalFeaturesBagConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_SHHapticsConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_SHHapticsEndpoints
+ __OBJC_$_INSTANCE_VARIABLES_SHMusicalFeaturesBagConfiguration
+ __OBJC_$_PROP_LIST_SHHapticsConfiguration
+ __OBJC_$_PROP_LIST_SHHapticsEndpoints
+ __OBJC_$_PROP_LIST_SHMusicalFeaturesBagConfiguration
+ __OBJC_CLASS_RO_$_SHHapticsConfiguration
+ __OBJC_CLASS_RO_$_SHHapticsEndpoints
+ __OBJC_CLASS_RO_$_SHMusicalFeaturesBagConfiguration
+ __OBJC_METACLASS_RO_$_SHHapticsConfiguration
+ __OBJC_METACLASS_RO_$_SHHapticsEndpoints
+ __OBJC_METACLASS_RO_$_SHMusicalFeaturesBagConfiguration
+ ___47-[SHRemoteConfiguration hapticsWithCompletion:]_block_invoke
+ ___52-[SHRemoteConfiguration populateRemoteConfiguration]_block_invoke_11
+ ___53-[SHMusicalFeaturesBagConfiguration initWithPromise:]_block_invoke
+ ___71-[SHRemoteConfiguration musicalFeaturesBagConfigurationWithCompletion:]_block_invoke
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __block_literal_global.66
+ __block_literal_global.68
+ __block_literal_global.70
+ __block_literal_global.72
+ _objc_msgSend$URLWithString:relativeToURL:
+ _objc_msgSend$availabilityRequestForID:ofIDType:
+ _objc_msgSend$baseURLString
+ _objc_msgSend$configuration
+ _objc_msgSend$fetchHapticByAdamIDURL
+ _objc_msgSend$fetchHapticByISRCURL
+ _objc_msgSend$fetchHapticsURLStringForClientIdentifier:songResourceIDType:
+ _objc_msgSend$fetchRequestForID:ofIDType:
+ _objc_msgSend$hapticsAvailableURLStringForClientIdentifier:songResourceIDType:
+ _objc_msgSend$hapticsEndpoints
+ _objc_msgSend$hapticsEndpointsBagValue
+ _objc_msgSend$hasHapticForAdamIDURL
+ _objc_msgSend$hasHapticForISRCURL
+ _objc_msgSend$initWithBaseURL:URLPath:
+ _objc_msgSend$initWithFetchHapticByAdamIDURL:hasHapticForAdamIDURL:fetchHapticByISRCURL:hasHapticForISRCURL:
+ _objc_msgSend$initWithURL:resolvingAgainstBaseURL:
+ _objc_msgSend$initWithURLComponents:
+ _objc_msgSend$musicalFeaturesBagConfigurationValue
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$originalComponents
+ _objc_msgSend$originalURLString
+ _objc_msgSend$path:containsToken:
+ _objc_msgSend$pathStringForClientIdentifier:songResourceIDType:requestKey:
+ _objc_msgSend$string
+ _objc_msgSend$stringByRemovingPercentEncoding
+ _objc_msgSend$tokenizedURLString
+ _symbolic So8NSStringCIeyBy_Sg
+ shcore_log_object.cold.1
- -[SHEndpoints hapticsURLPathForClientIdentifier:songResourceIDType:]
- -[SHTokenizedURL host]
- -[SHTokenizedURL originalURLPath]
- -[SHTokenizedURL setHost:]
- -[SHTokenizedURL setOriginalURLPath:]
- -[SHTokenizedURL tokenURLPath]
- GCC_except_table18
- GCC_except_table25
- OBJC_IVAR_$_SHTokenizedURL._host
- OBJC_IVAR_$_SHTokenizedURL._originalURLPath
- __block_literal_global.46
- __block_literal_global.48
- __block_literal_global.50
- _objc_msgSend$URL
- _objc_msgSend$componentsSeparatedByString:
- _objc_msgSend$containsTokens
- _objc_msgSend$copyWithZone:
- _objc_msgSend$firstObject
- _objc_msgSend$host
- _objc_msgSend$lastObject
- _objc_msgSend$mutableCopy
- _objc_msgSend$originalURLPath
- _objc_msgSend$setQuery:
- _objc_msgSend$tokenURLPath
- _objc_setProperty_atomic_copy
- _symbolic So8NSStringCIeyBy_
CStrings:
+ "@\"NSURLComponents\""
+ "@40@0:8@16q24@32"
+ "@40@0:8q16@24q32"
+ "@48@0:8@16@24@32@40"
+ "B32@0:8@16q24"
+ "Fetching musical features models configuration values..."
+ "Haptics endpoints..."
+ "HapticsEndpoints fetch complete with value %@ error %@"
+ "Musical features models configuration values fetch complete with value %@ error %@"
+ "Q24@0:8@16"
+ "SHHapticsConfiguration"
+ "SHHapticsEndpoints"
+ "SHMusicalFeaturesBagConfiguration"
+ "T@\"AMSBagValue\",&,V_hapticsEndpointsBagValue"
+ "T@\"AMSBagValue\",&,V_musicalFeaturesBagConfigurationValue"
+ "T@\"AMSPromise\",R,V_amsPromise"
+ "T@\"NSDictionary\",R,C,N,V_hapticsEndpoints"
+ "T@\"NSDictionary\",R,V_configuration"
+ "T@\"NSURLComponents\",R,C,V_originalComponents"
+ "T@\"SHTokenizedURL\",R,V_fetchHapticByAdamIDURL"
+ "T@\"SHTokenizedURL\",R,V_fetchHapticByISRCURL"
+ "T@\"SHTokenizedURL\",R,V_hasHapticForAdamIDURL"
+ "T@\"SHTokenizedURL\",R,V_hasHapticForISRCURL"
+ "URLWithString:relativeToURL:"
+ "_amsPromise"
+ "_configuration"
+ "_fetchHapticByAdamIDURL"
+ "_fetchHapticByISRCURL"
+ "_hapticsEndpoints"
+ "_hapticsEndpointsBagValue"
+ "_hasHapticForAdamIDURL"
+ "_hasHapticForISRCURL"
+ "_musicalFeaturesBagConfigurationValue"
+ "_originalComponents"
+ "adamIDLookup"
+ "amsPromise"
+ "availabilityRequestForID:ofIDType:"
+ "availableModelsForClientIdentifier:"
+ "baseURL"
+ "baseURLString"
+ "crema"
+ "crepe"
+ "d24@0:8@16"
+ "fetchHapticByAdamIDURL"
+ "fetchHapticByISRCURL"
+ "fetchHapticsPath"
+ "fetchHapticsURLStringForClientIdentifier:songResourceIDType:"
+ "fetchRequestForID:ofIDType:"
+ "hapticsAvailableURLStringForClientIdentifier:songResourceIDType:"
+ "hapticsEndpoints"
+ "hapticsEndpointsBagValue"
+ "hapticsEndpointsForStorefront:clientIdentifier:"
+ "hapticsWithCompletion:"
+ "hasHapticForAdamIDURL"
+ "hasHapticForISRCURL"
+ "hasHapticsPath"
+ "https://amp-api.shazam.apple.com"
+ "initWithBaseURL:URLPath:"
+ "initWithFetchHapticByAdamIDURL:hasHapticForAdamIDURL:fetchHapticByISRCURL:hasHapticForISRCURL:"
+ "initWithURL:resolvingAgainstBaseURL:"
+ "initWithURLComponents:"
+ "isrcLookup"
+ "liveAudioMinimumRecordingDuration"
+ "minimumDurationInSeconds"
+ "minimumDurationInSecondsForClientIdentifier:"
+ "models"
+ "musical-features-external"
+ "musical-features-internal"
+ "musicalFeaturesBagConfigurationValue"
+ "musicalFeaturesBagConfigurationWithCompletion:"
+ "musicalFeaturesBagConfigurationWithPromise"
+ "objectForKey:"
+ "originalComponents"
+ "originalURLString"
+ "path:containsToken:"
+ "pathStringForClientIdentifier:songResourceIDType:requestKey:"
+ "requestOfType:forID:ofIDType:"
+ "setHapticsEndpointsBagValue:"
+ "setMusicalFeaturesBagConfigurationValue:"
+ "shazam-haptics"
+ "shazam-musical-features-configuration"
+ "string"
+ "stringByRemovingPercentEncoding"
+ "tokenizedURLString"
- "\r"
- "?"
- "T@\"NSString\",C,V_host"
- "T@\"NSString\",C,V_originalURLPath"
- "URL"
- "_host"
- "_originalURLPath"
- "componentsSeparatedByString:"
- "firstObject"
- "hapticsURLPathForClientIdentifier:songResourceIDType:"
- "host"
- "lastObject"
- "mutableCopy"
- "originalURLPath"
- "q24@0:8@16"
- "setOriginalURLPath:"
- "setQuery:"
- "song-haptics-adamid"
- "song-haptics-isrc"
- "tokenURLPath"
- "{id_type}"

```
