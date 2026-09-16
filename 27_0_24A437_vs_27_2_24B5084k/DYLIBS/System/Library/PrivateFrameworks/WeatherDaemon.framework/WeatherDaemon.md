## WeatherDaemon

> `/System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon`

```diff

-1454.1.0.0.0
-  __TEXT.__text: 0x22cfe4
+1470.0.0.0.0
+  __TEXT.__text: 0x22e3ec
   __TEXT.__objc_methlist: 0x66c
-  __TEXT.__const: 0x1aeb8
-  __TEXT.__cstring: 0x3ec5
-  __TEXT.__oslogstring: 0xd3b5
+  __TEXT.__const: 0x1aef8
+  __TEXT.__cstring: 0x4245
+  __TEXT.__oslogstring: 0xd4a5
   __TEXT.__constg_swiftt: 0x57e4
-  __TEXT.__swift5_typeref: 0x5f96
+  __TEXT.__swift5_typeref: 0x5fdc
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_reflstr: 0x5802
   __TEXT.__swift5_fieldmd: 0x7e08

   __TEXT.__swift_as_entry: 0x348
   __TEXT.__swift_as_ret: 0x324
   __TEXT.__swift_as_cont: 0x638
-  __TEXT.__swift5_capture: 0x28b4
+  __TEXT.__swift5_capture: 0x2850
   __TEXT.__swift5_mpenum: 0x44
-  __TEXT.__unwind_info: 0xb4c8
+  __TEXT.__unwind_info: 0xb4f8
   __TEXT.__eh_frame: 0x101f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d0
+  __DATA_CONST.__objc_selrefs: 0x5e0
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__got: 0x1138
-  __AUTH_CONST.__const: 0x142d0
+  __DATA_CONST.__got: 0x1150
+  __AUTH_CONST.__const: 0x141b8
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0x41e0
   __AUTH_CONST.__auth_got: 0x3158
   __AUTH.__objc_data: 0xd8
   __AUTH.__data: 0x9c0
   __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x31b0
+  __DATA.__data: 0x3200
   __DATA.__common: 0x100
   __DATA_DIRTY.__objc_data: 0xb30
-  __DATA_DIRTY.__data: 0x8170
+  __DATA_DIRTY.__data: 0x8190
   __DATA_DIRTY.__bss: 0x10520
   __DATA_DIRTY.__common: 0x190
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 15342
-  Symbols:   4103
-  CStrings:  1337
+  Functions: 15362
+  Symbols:   4114
+  CStrings:  1349
 
Symbols:
+ _NSLocalizedDescriptionKey
+ _NSLocalizedFailureReasonErrorKey
+ _NSLocalizedRecoverySuggestionErrorKey
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$localizedRecoverySuggestion
+ _symbolic _____Sg 10Foundation12URLQueryItemV
+ _symbolic _____XDXMT 13WeatherDaemon31WDSJWTAuthenticatorServiceProxyC
+ _symbolic _____XDXMT 13WeatherDaemon34WDSJWTAuthenticatorServiceListenerC
+ _symbolic _____yS2SG s17_NativeDictionaryV
+ _symbolic _____ySS_SStG s23_ContiguousArrayStorageC
+ _symbolic _____ySSypG s18_DictionaryStorageC
CStrings:
+ " for the token request."
+ "Check the network connection and try the request again."
+ "Failed to generate token. bundleIdentifier=%{public}s, error=%{public}s"
+ "Failed to purge all lastFetch data; error=%{private,mask.hash}s"
+ "Failed to purge lastFetch data, error=%{private,mask.hash}s"
+ "Purged stale lastFetch data"
+ "The Apple Weather service returned HTTP "
+ "The Apple Weather service returned an unexpected response to the token request."
+ "The most common cause is that the WeatherKit App Service is not enabled for this app's App ID. WeatherKit has to be enabled in both the \"App Services\" tab and the \"App Capabilities\" tab of the App ID in Certificates, Identifiers & Profiles (https://developer.apple.com/account/resources/identifiers). Enabling it under \"App Capabilities\" also requires rebuilding the app with a regenerated provisioning profile. See https://developer.apple.com/help/account/services/weatherkit/"
+ "The token request could not reach the Apple Weather service."
+ "WeatherKit could not generate an authentication token for "
+ "WeatherKit setup hint: %{public}s"
+ "weatherdaemon.useGlobalAirPollutionModel"
- "Failed to generate token with error: %{public}s"
```
