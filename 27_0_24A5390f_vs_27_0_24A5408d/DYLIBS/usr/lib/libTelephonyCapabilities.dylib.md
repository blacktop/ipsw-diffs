## libTelephonyCapabilities.dylib

> `/usr/lib/libTelephonyCapabilities.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__weak_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`

```diff

-6565.0.0.0.0
-  __TEXT.__text: 0x53f64
+6567.0.0.0.0
+  __TEXT.__text: 0x53f38
   __TEXT.__init_offsets: 0x5c
   __TEXT.__const: 0x3ed4
   __TEXT.__gcc_except_tab: 0x8ac0
Symbols:
+ __ZN12capabilities2ct32supportsOperatorPRIPushForVendorE20TelephonyRadioVendor
+ __ZN12capabilities2ctL24sSupportsOperatorPRIPushE20TelephonyRadioVendor
- __ZN12capabilities2ct33supportsOperatorPRIPushForProductE16TelephonyProduct
- __ZN12capabilities2ctL24sSupportsOperatorPRIPushE16TelephonyProduct
Functions:
~ __ZN12capabilities2ctL24sSupportsOperatorPRIPushE16TelephonyProduct -> __ZN12capabilities2ctL21sSupportsNewPhonebookE20TelephonyRadioVendor : 404 -> 360
~ __ZN12capabilities2ctL27sSupportsIPCInterfaceConfigE20TelephonyRadioVendor -> __ZN12capabilities2ctL33sSupportsIPCInterfaceConfigStage2E20TelephonyRadioVendor : 360 -> 364
~ __ZN12capabilities2ctL33sSupportsIPCInterfaceConfigStage2E20TelephonyRadioVendor -> __ZN12capabilities2ctL38sSupportsBBTimePrecisionInMillisecondsE20TelephonyRadioVendor : 364 -> 360
~ __ZN12capabilities2ct44supportsBBTimePrecisionInMillisecondsWithMCTEv -> __ZN12capabilities2ctL28sSupportsHOVirtualInterfacesE20TelephonyRadioVendor : 124 -> 360
~ __ZN12capabilities2ctL45sSupportsBBTimePrecisionInMillisecondsWithMCTE20TelephonyRadioVendor -> __ZN12capabilities2ct36supportsHOVirtualInterfacesForVendorE20TelephonyRadioVendor : 360 -> 4
~ __ZN12capabilities2ct53supportsBBTimePrecisionInMillisecondsWithMCTForVendorE20TelephonyRadioVendor -> __ZN12capabilities2ct39shouldEnableSystemDeterminationWatchdogEv : 4 -> 124
~ __ZN12capabilities2ctL40sShouldEnableSystemDeterminationWatchdogE20TelephonyRadioVendor -> __ZN12capabilities2ctL33sShouldSaveInCallIMSPrefForCSCallE20TelephonyRadioVendor : 360 -> 364
~ __ZN12capabilities2ctL33sShouldSaveInCallIMSPrefForCSCallE20TelephonyRadioVendor -> __ZN12capabilities2ctL31sSupportsCachedNetworkTimeQueryE20TelephonyRadioVendor : 364 -> 360
~ __ZN12capabilities2ctL31sSupportsCachedNetworkTimeQueryE20TelephonyRadioVendor -> __ZN12capabilities2ctL33sSupportsEnhancedNRSignalStrengthE20TelephonyRadioVendor : 360 -> 364
~ __ZN12capabilities2ctL33sSupportsEnhancedNRSignalStrengthE20TelephonyRadioVendor -> __ZN12capabilities2ctL24sSupportsTARandomizationE20TelephonyRadioVendor : 364 -> 360
```
