## DeviceSelectionEmergencyFlow

> `/System/Library/PrivateFrameworks/DeviceSelectionEmergencyFlow.framework/DeviceSelectionEmergencyFlow`

```diff

-3605.25.1.0.0
-  __TEXT.__text: 0x17768
-  __TEXT.__objc_methlist: 0x38c
+3610.8.1.0.0
+  __TEXT.__text: 0x178f4
+  __TEXT.__objc_methlist: 0x39c
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__const: 0x1208
+  __TEXT.__const: 0x1218
   __TEXT.__swift5_typeref: 0x5a0
   __TEXT.__swift5_fieldmd: 0x624
   __TEXT.__constg_swiftt: 0x78c

   __TEXT.__swift_as_ret: 0xb8
   __TEXT.__swift_as_cont: 0x160
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__unwind_info: 0xbd8
+  __TEXT.__unwind_info: 0xbe8
   __TEXT.__eh_frame: 0x178c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b8
+  __DATA_CONST.__objc_selrefs: 0x2c8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__got: 0x188
   __AUTH_CONST.__const: 0x14a8
-  __AUTH_CONST.__objc_const: 0x10a8
-  __AUTH_CONST.__auth_got: 0x6b8
+  __AUTH_CONST.__objc_const: 0x10d8
+  __AUTH_CONST.__auth_got: 0x6c0
   __AUTH.__data: 0xa0
-  __DATA.__objc_ivar: 0x3c
+  __DATA.__objc_ivar: 0x40
   __DATA.__data: 0x2a8
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__data: 0x7c8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 937
-  Symbols:   558
+  Functions: 940
+  Symbols:   562
   CStrings:  76
 
Symbols:
+ -[WiProxAdvertiserAdapter startAdvertisingWithPayload:additionalInfo:]
+ -[WiProxDeviceInfo initWithDeviceUUID:deviceAddress:idsDeviceID:observedAtAbsoluteTime:heySiriPerceptualHash:heySiriSNR:heySiriConfidence:heySiriDeviceGroup:heySiriDeviceClass:heySiriRandom:heySiriProductType:]
+ -[WiProxDeviceInfo observedAtAbsoluteTime]
+ -[WiProxDiscoveryAdapter startScanningAndAdvertisingWithPayload:]
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_IVAR_$_WiProxDeviceInfo._observedAtAbsoluteTime
+ _WPHeySiriKeyDeviceTime
+ _WiProxMakeHeySiriPayload
+ ___65-[WiProxDiscoveryAdapter startScanningAndAdvertisingWithPayload:]_block_invoke
+ ___70-[WiProxAdvertiserAdapter startAdvertisingWithPayload:additionalInfo:]_block_invoke
+ _objc_release_x28
- -[WiProxAdvertiserAdapter startAdvertisingWithPhash:snr:random:confidence:additionalInfo:]
- -[WiProxDeviceInfo initWithDeviceUUID:deviceAddress:idsDeviceID:heySiriPerceptualHash:heySiriSNR:heySiriConfidence:heySiriDeviceGroup:heySiriDeviceClass:heySiriRandom:heySiriProductType:]
- -[WiProxDiscoveryAdapter startScanningAndAdvertisingWithPhash:snr:random:confidence:]
- _MakeHeySiriPayload
- ___85-[WiProxDiscoveryAdapter startScanningAndAdvertisingWithPhash:snr:random:confidence:]_block_invoke
- ___90-[WiProxAdvertiserAdapter startAdvertisingWithPhash:snr:random:confidence:additionalInfo:]_block_invoke
- _objc_retain_x6
```
