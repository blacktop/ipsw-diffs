## DormancyCore

> `/System/Library/PrivateFrameworks/DormancyCore.framework/DormancyCore`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH.__objc_data`

```diff

-27.0.57.0.0
-  __TEXT.__text: 0x2b800
+27.0.60.0.0
+  __TEXT.__text: 0x2d49c
   __TEXT.__objc_methlist: 0xe4
-  __TEXT.__const: 0x3ddc
-  __TEXT.__cstring: 0x862
-  __TEXT.__swift5_typeref: 0xe13
-  __TEXT.__swift5_fieldmd: 0xd24
-  __TEXT.__constg_swiftt: 0xd88
-  __TEXT.__swift5_reflstr: 0x761
+  __TEXT.__const: 0x3f2c
+  __TEXT.__cstring: 0x923
+  __TEXT.__swift5_typeref: 0xe73
+  __TEXT.__swift5_fieldmd: 0xdcc
+  __TEXT.__constg_swiftt: 0xe40
+  __TEXT.__swift5_reflstr: 0x81a
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0x180
-  __TEXT.__swift5_protos: 0x24
-  __TEXT.__swift5_proto: 0x374
-  __TEXT.__swift5_types: 0x118
+  __TEXT.__swift5_protos: 0x28
+  __TEXT.__swift5_proto: 0x384
+  __TEXT.__swift5_types: 0x120
   __TEXT.__swift5_capture: 0x28
-  __TEXT.__oslogstring: 0xadd
+  __TEXT.__oslogstring: 0xb2d
   __TEXT.__swift5_mpenum: 0x3c
-  __TEXT.__unwind_info: 0xc30
-  __TEXT.__eh_frame: 0xb78
+  __TEXT.__unwind_info: 0xc60
+  __TEXT.__eh_frame: 0xbd8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x168
+  __DATA_CONST.__objc_selrefs: 0x178
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__got: 0x1a8
-  __AUTH_CONST.__const: 0x26c8
-  __AUTH_CONST.__objc_const: 0x950
-  __AUTH_CONST.__auth_got: 0x858
+  __DATA_CONST.__got: 0x1b8
+  __AUTH_CONST.__const: 0x27a8
+  __AUTH_CONST.__objc_const: 0x9b0
+  __AUTH_CONST.__auth_got: 0x870
   __AUTH.__objc_data: 0x170
-  __AUTH.__data: 0x758
+  __AUTH.__data: 0x7c8
   __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x968
-  __DATA.__bss: 0x6880
+  __DATA.__data: 0x998
+  __DATA.__bss: 0x6a00
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1212
-  Symbols:   632
-  CStrings:  119
+  Functions: 1245
+  Symbols:   644
+  CStrings:  125
 
Symbols:
+ _OBJC_CLASS_$_PDRRegistry
+ ___swift_memcpy35_8
+ _associated conformance 12DormancyCore0A7MonitorC14ExcludedReasonO26RemotelyDisabledCodingKeys33_F8D6856B5B68C23C991E3A725FE1B06ALLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 12DormancyCore0A7MonitorC14ExcludedReasonO26RemotelyDisabledCodingKeys33_F8D6856B5B68C23C991E3A725FE1B06ALLOs0H3KeyAAs28CustomDebugStringConvertible
+ _objc_msgSend$getActivePairedDeviceIncludingAltAccount
+ _objc_msgSend$isAltAccount
+ _swift_retain_x24
+ _symbolic $s12DormancyCore20TinkerDeviceDetectorP
+ _symbolic _____ 12DormancyCore0A7MonitorC14ExcludedReasonO26RemotelyDisabledCodingKeys33_F8D6856B5B68C23C991E3A725FE1B06ALLO
+ _symbolic _____ 12DormancyCore27DefaultTinkerDeviceDetectorV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 12DormancyCore0D7MonitorC14ExcludedReasonO26RemotelyDisabledCodingKeys33_F8D6856B5B68C23C991E3A725FE1B06ALLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 12DormancyCore0D7MonitorC14ExcludedReasonO26RemotelyDisabledCodingKeys33_F8D6856B5B68C23C991E3A725FE1B06ALLO
CStrings:
+ "ApplicationSurface.AppIntentExecution"
+ "ApplicationSurface.CarouselAlert"
+ "DormancyStatusManager bundleID %s, context: %s, isTinker: %{bool}d"
+ "Remotely disabled"
+ "Set promotion date to %s for %s:%s"
+ "remotelyDisabled"
+ "tinkerDefaultValue"
- "DormancyStatusManager bundleID %s, context: %s"
```
