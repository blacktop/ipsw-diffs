## CoreWiFi

> `/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1030.74.0.0.0
-  __TEXT.__text: 0x1fd69c
-  __TEXT.__objc_methlist: 0x1261c
+1030.81.0.0.0
+  __TEXT.__text: 0x1fed90
+  __TEXT.__objc_methlist: 0x12674
   __TEXT.__const: 0x7cc0
   __TEXT.__dlopen_cstrs: 0xab0
   __TEXT.__swift5_typeref: 0x13b4

   __TEXT.__swift5_assocty: 0x108
   __TEXT.__constg_swiftt: 0xe88
   __TEXT.__swift5_fieldmd: 0x108c
-  __TEXT.__cstring: 0x2556c
+  __TEXT.__cstring: 0x25616
   __TEXT.__swift5_proto: 0x6b4
   __TEXT.__swift5_types: 0x1b0
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__oslogstring: 0x20f97
-  __TEXT.__gcc_except_tab: 0x752c
+  __TEXT.__oslogstring: 0x2115b
+  __TEXT.__gcc_except_tab: 0x75ec
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x6d68
+  __TEXT.__unwind_info: 0x6da0
   __TEXT.__eh_frame: 0x1498
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5cb0
+  __DATA_CONST.__const: 0x5cc8
   __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9320
+  __DATA_CONST.__objc_selrefs: 0x9358
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x390
-  __DATA_CONST.__objc_arraydata: 0x2070
+  __DATA_CONST.__objc_arraydata: 0x2030
   __DATA_CONST.__got: 0x9c0
-  __AUTH_CONST.__const: 0x50b8
-  __AUTH_CONST.__cfstring: 0x1cf60
-  __AUTH_CONST.__objc_const: 0x18288
-  __AUTH_CONST.__objc_intobj: 0x3db0
-  __AUTH_CONST.__objc_arrayobj: 0x4c8
+  __AUTH_CONST.__const: 0x50d8
+  __AUTH_CONST.__cfstring: 0x1d060
+  __AUTH_CONST.__objc_const: 0x182b0
+  __AUTH_CONST.__objc_intobj: 0x3e28
+  __AUTH_CONST.__objc_arrayobj: 0x498
   __AUTH_CONST.__objc_dictobj: 0x230
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x1078

   __AUTH.__data: 0x1b8
   __DATA.__objc_ivar: 0x1500
   __DATA.__data: 0x2200
-  __DATA.__bss: 0xd9a8
+  __DATA.__bss: 0xd9c8
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_ivar: 0x84
   __DATA_DIRTY.__objc_data: 0x12e8
   __DATA_DIRTY.__data: 0x200
-  __DATA_DIRTY.__bss: 0x2f0
+  __DATA_DIRTY.__bss: 0x2e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9432
-  Symbols:   1184
-  CStrings:  6340
+  Functions: 9446
+  Symbols:   1185
+  CStrings:  6350
 
Symbols:
+ _CWFNetworkProfilePropertyConnectivityAssistEnabledKey
CStrings:
+ "ConnectivityAssistEnabled"
+ "GET NAN RADIO SCHEDULE"
+ "NANRTM"
+ "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) Matched cached hybrid interface %{public}@ for APPLE80211_VIRT_IF_ROLE_NAN_DISCOVERY"
+ "[corewifi] AUTO-JOIN: [internal] Applying defaults override for [CWFAutoJoinTriggerAssociatedToNetworkRetry : CWFAutoJoinTriggerNANRealTimeModeEnded] throttle interval (default=%lus, override=%lus)"
+ "[corewifi] [wifi-network-sharing] Already added network for clientID (clientID=%{public}@, knownNetwork=%{public}@)"
+ "assoc_retry_nan_rt_throttle_interval"
+ "connectivityAssist=no, "
+ "isConnectivityAssistEnabled"
+ "nan_rt_ended"
+ "remotedevicekitwifid"
- "hrmwifid"
```
