## WebKit

> `/System/Library/Frameworks/WebKit.framework/Versions/A/WebKit`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-624.5.1.11.2
-  __TEXT.__text: 0x12e0e30
+624.5.1.11.3
+  __TEXT.__text: 0x12e0fe8
   __TEXT.__auth_stubs: 0x19a90
   __TEXT.__objc_methlist: 0x14204
   __TEXT.__dlsym_cstr: 0x870
   __TEXT.__getClass_cstr: 0x929
   __TEXT.__const: 0x5ef0
-  __TEXT.__gcc_except_tab: 0x77764
+  __TEXT.__gcc_except_tab: 0x777a4
   __TEXT.__cstring: 0x203e7b
   __TEXT.__swift5_typeref: 0x1114
   __TEXT.__constg_swiftt: 0xc68
Symbols:
+ __ZN6WebKit29setNWParametersTrackerOptionsEPU27objcproto16OS_nw_parameters8NSObjectbbbNS_5IsRTCE
- __ZN6WebKit29setNWParametersTrackerOptionsEPU27objcproto16OS_nw_parameters8NSObjectbbb
Functions:
~ __ZN6WebKit29setNWParametersTrackerOptionsEPU27objcproto16OS_nw_parameters8NSObjectbbb -> __ZN6WebKit29setNWParametersTrackerOptionsEPU27objcproto16OS_nw_parameters8NSObjectbbbNS_5IsRTCE : 104 -> 108
~ __ZN6WebKitL18createNWConnectionERNS_18NetworkRTCProviderEPKcS3_bRKN3WTF6StringENS_22RTCSocketCreationFlagsERKN7WebCore17RegistrableDomainE : 384 -> 388
~ __ZN6WebKit35NetworkRTCUDPSocketCocoaConnections19configureParametersEPU27objcproto16OS_nw_parameters8NSObject15nw_ip_version_t : 332 -> 336
~ __ZN6WebKit23NetworkTransportSession6createERNS_29NetworkConnectionToWebProcessEN3WTF23ObjectIdentifierGenericINS_33WebTransportSessionIdentifierTypeENS3_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEEONS3_3URLEON7WebCore19WebTransportOptionsEONS4_INS_26WebPageProxyIdentifierTypeENS3_38ObjectIdentifierMainThreadAccessTraitsIyEEyEEONSB_12ClientOriginE : 3744 -> 4172
CStrings:
+ "21624.5.1.11.3"
- "21624.5.1.11.2"
```
