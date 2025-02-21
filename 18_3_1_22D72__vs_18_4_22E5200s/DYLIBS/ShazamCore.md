## ShazamCore

> `/System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore`

```diff

-307.2.0.0.0
-  __TEXT.__text: 0xb024
-  __TEXT.__auth_stubs: 0x7a0
-  __TEXT.__objc_methlist: 0xd88
-  __TEXT.__const: 0x82
-  __TEXT.__cstring: 0xcbc
-  __TEXT.__oslogstring: 0x49f
-  __TEXT.__gcc_except_tab: 0xf4
-  __TEXT.__swift5_typeref: 0x5e
+312.0.0.0.0
+  __TEXT.__text: 0xc0e4
+  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__objc_methlist: 0x1070
+  __TEXT.__const: 0x7a
+  __TEXT.__cstring: 0xd8c
+  __TEXT.__oslogstring: 0x577
+  __TEXT.__gcc_except_tab: 0x108
+  __TEXT.__swift5_typeref: 0x60
   __TEXT.__swift5_capture: 0x4c
-  __TEXT.__unwind_info: 0x420
+  __TEXT.__swift_as_entry: 0x14
+  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__unwind_info: 0x470
   __TEXT.__eh_frame: 0x258
-  __TEXT.__objc_classname: 0x1e7
-  __TEXT.__objc_methname: 0x284e
-  __TEXT.__objc_methtype: 0x53c
-  __TEXT.__objc_stubs: 0x1c60
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x510
-  __DATA_CONST.__objc_classlist: 0xd0
+  __TEXT.__objc_classname: 0x238
+  __TEXT.__objc_methname: 0x2e46
+  __TEXT.__objc_methtype: 0x593
+  __TEXT.__objc_stubs: 0x1e20
+  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__const: 0x508
+  __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9d0
-  __DATA_CONST.__objc_superrefs: 0x90
-  __AUTH_CONST.__auth_got: 0x3e0
+  __DATA_CONST.__objc_selrefs: 0xb28
+  __DATA_CONST.__objc_superrefs: 0xa8
+  __AUTH_CONST.__auth_got: 0x3e8
   __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0xf40
-  __AUTH_CONST.__objc_const: 0x20c0
-  __DATA.__objc_ivar: 0xd4
+  __AUTH_CONST.__const: 0x280
+  __AUTH_CONST.__cfstring: 0x1080
+  __AUTH_CONST.__objc_const: 0x21a8
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0xf4
   __DATA.__data: 0x188
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x840

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 340
-  Symbols:   537
-  CStrings:  727
+  Functions: 379
+  Symbols:   585
+  CStrings:  790
 
Symbols:
+ _OBJC_CLASS_$_NSURLRequest
+ _OBJC_CLASS_$_SHHapticsConfiguration
+ _OBJC_CLASS_$_SHHapticsEndpoints
+ _OBJC_CLASS_$_SHMusicalFeaturesModelsConfiguration
+ _OBJC_METACLASS_$_SHHapticsConfiguration
+ _OBJC_METACLASS_$_SHHapticsEndpoints
+ _OBJC_METACLASS_$_SHMusicalFeaturesModelsConfiguration
+ _objc_retain_x24
+ _objc_retain_x25
- _objc_setProperty_nonatomic_copy
CStrings:
+ "\x04"
+ "\x0f"
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
+ "SHMusicalFeaturesModelsConfiguration"
+ "T@\"AMSBagValue\",&,N,V_hapticsEndpointsBagValue"
+ "T@\"AMSBagValue\",&,N,V_musicalFeaturesModelsConfigurationValue"
+ "T@\"AMSPromise\",R,N,V_amsPromise"
+ "T@\"NSDictionary\",R,C,N,V_hapticsEndpoints"
+ "T@\"NSDictionary\",R,N,V_availableModels"
+ "T@\"NSURLComponents\",R,C,N,V_originalComponents"
+ "T@\"SHTokenizedURL\",R,N,V_fetchHapticByAdamIDURL"
+ "T@\"SHTokenizedURL\",R,N,V_fetchHapticByISRCURL"
+ "T@\"SHTokenizedURL\",R,N,V_hasHapticForAdamIDURL"
+ "T@\"SHTokenizedURL\",R,N,V_hasHapticForISRCURL"
+ "URLWithString:relativeToURL:"
+ "_amsPromise"
+ "_availableModels"
+ "_fetchHapticByAdamIDURL"
+ "_fetchHapticByISRCURL"
+ "_hapticsEndpoints"
+ "_hapticsEndpointsBagValue"
+ "_hasHapticForAdamIDURL"
+ "_hasHapticForISRCURL"
+ "_musicalFeaturesModelsConfigurationValue"
+ "_originalComponents"
+ "adamIDLookup"
+ "amsPromise"
+ "availabilityRequestForID:ofIDType:"
+ "availableModels"
+ "availableModelsForClientIdentifier:"
+ "baseURL"
+ "baseURLString"
+ "crema"
+ "crepe"
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
+ "models"
+ "musical-features-external"
+ "musical-features-internal"
+ "musicalFeaturesConfigurationWithPromise"
+ "musicalFeaturesModelsConfigurationValue"
+ "musicalFeaturesModelsConfigurationWithCompletion:"
+ "originalComponents"
+ "originalURLString"
+ "path:containsToken:"
+ "pathStringForClientIdentifier:songResourceIDType:requestKey:"
+ "requestOfType:forID:ofIDType:"
+ "setHapticsEndpointsBagValue:"
+ "setMusicalFeaturesModelsConfigurationValue:"
+ "shazam-haptics"
+ "shazam-musical-features-models-configuration"
+ "string"
+ "stringByRemovingPercentEncoding"
+ "tokenizedURLString"
- "\r"
- "?"
- "T@\"NSString\",C,N,V_host"
- "T@\"NSString\",C,N,V_originalURLPath"
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
