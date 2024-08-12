## WiFiKit

> `/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`

```diff

-980.90.0.0.0
-  __TEXT.__text: 0x951f4
+980.101.0.0.0
+  __TEXT.__text: 0x952ec
   __TEXT.__auth_stubs: 0x1530
-  __TEXT.__objc_methlist: 0x7f84
+  __TEXT.__objc_methlist: 0x7f9c
   __TEXT.__const: 0x270
-  __TEXT.__oslogstring: 0xa881
-  __TEXT.__cstring: 0xac06
-  __TEXT.__gcc_except_tab: 0x2988
+  __TEXT.__oslogstring: 0xa8ff
+  __TEXT.__cstring: 0xab30
+  __TEXT.__gcc_except_tab: 0x2a3c
   __TEXT.__dlopen_cstrs: 0xac
   __TEXT.__ustring: 0x44
-  __TEXT.__unwind_info: 0x1b38
-  __TEXT.__objc_classname: 0xe22
-  __TEXT.__objc_methname: 0x14bd3
-  __TEXT.__objc_methtype: 0x2ae2
-  __TEXT.__objc_stubs: 0xe0c0
-  __DATA_CONST.__got: 0xbc8
+  __TEXT.__unwind_info: 0x1b48
+  __TEXT.__objc_classname: 0xe23
+  __TEXT.__objc_methname: 0x14cf7
+  __TEXT.__objc_methtype: 0x2adf
+  __TEXT.__objc_stubs: 0xe0e0
+  __DATA_CONST.__got: 0xbc0
   __DATA_CONST.__const: 0x22e8
   __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4840
+  __DATA_CONST.__objc_selrefs: 0x4868
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x198
   __AUTH_CONST.__auth_got: 0xaa8
   __AUTH_CONST.__const: 0x3a0
   __AUTH_CONST.__cfstring: 0x6b80
-  __AUTH_CONST.__objc_const: 0x1aa20
+  __AUTH_CONST.__objc_const: 0x1aae8
   __AUTH_CONST.__objc_intobj: 0x648
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH.__objc_data: 0x1590
-  __DATA.__objc_ivar: 0xb88
+  __DATA.__objc_ivar: 0xb8c
   __DATA.__data: 0x1320
   __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0xaa0

   - /usr/lib/libSystemHealth.dylib
   - /usr/lib/libnetquality.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3183
-  Symbols:   4157
-  CStrings:  6569
+  Functions: 3185
+  Symbols:   4158
+  CStrings:  6580
 
Symbols:
+ _kWFPrivateAddressModeCellIdentifier
- _kCFBooleanFalse
- _kWFRandomMACSwitchCellIdentifier
CStrings:
+ "%!@(MISSING) - autoJoinEnabled=%!d(MISSING) autoLoginEnabled=%!d(MISSING) isInSaveDataMode=%!d(MISSING) isPrivacyProxyEnabled=%!d(MISSING) _privateAddressMode=%!l(MISSING)d randomMAC='%!@(MISSING)' _randomMACAddressConfigurable=%!d(MISSING)"
+ "@48@0:8@16@24Q32B40B44"
+ "B2\x11\x12\x11\x17"
+ "Disassociate for current network when private addres mode changes"
+ "Do not disassociate for current network when transit between static and rotating"
+ "Generating new private mac when join with random address mode"
+ "Generating new private mac when switched out of off mode"
+ "PRIVATE_MAC_ADDRESS_TYPE"
+ "R!\x1f\x12\x12\x11\x12"
+ "T@?,C,N,V_privateAddressModeChangeHandler"
+ "TQ,?,N"
+ "TQ,?,N,V_privateAddressMode"
+ "TQ,N,V_privateAddressMode"
+ "User joining other network using private address mode: %!l(MISSING)d"
+ "User tried to set private address mode to : %!l(MISSING)d"
+ "WFDetailContextPrivateAddressConfig: randomMACAddress='%!@(MISSING)', hardwareMACAddress='%!@(MISSING)', privateAddressMode=%!l(MISSING)d, connectedWithHardwareAddress=%!d(MISSING), privateAddressSupported=%!d(MISSING)"
+ "_privateAddressMode"
+ "_privateAddressModeChangeHandler"
+ "failed to save private address for '%!@(MISSING)' (mode=%!l(MISSING)u, address='%!@(MISSING)')"
+ "initWithRandomMACAddress:hardwareMACAddress:privateAddressMode:connectedWithHardwareAddress:privateAddressSupported:"
+ "kWFPrivateAddressModeCellIdentifier"
+ "privateAddressMode"
+ "privateAddressModeChangeHandler"
+ "randomMACCellAtIndexPath:chinaDevice:"
+ "savePrivateAddressMode:"
+ "saved private address for '%!@(MISSING)' (mode=%!l(MISSING)u, address='%!@(MISSING)')"
+ "setPrivateAddressMode:"
+ "setPrivateAddressModeChangeHandler:"
+ "setRandomAddressModeForNetwork:mode:randomMAC:"
+ "updatePrivateAddressMode:"
+ "v40@0:8@16Q24@32"
- "%!@(MISSING) - autoJoinEnabled=%!d(MISSING) autoLoginEnabled=%!d(MISSING) isInSaveDataMode=%!d(MISSING) isPrivacyProxyEnabled=%!d(MISSING) randomMACDisabled=%!d(MISSING) randomMACSwitch=%!d(MISSING) _randomMACAddressDisabled=%!d(MISSING) randomMAC='%!@(MISSING)' _randomMACAddressConfigurable=%!d(MISSING)"
- "-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:scrollToCellType:]_block_invoke_2"
- "-[WFNetworkListController networkListViewControllerDidTapOtherNetwork:]_block_invoke_2"
- "@32@0:8@16B24B28"
- "@48@0:8@16@24B32B36B40B44"
- "B!\x1f\x12\x12\x11\x12"
- "B2\x11\x13\x17"
- "PRIVATE_MAC_ADDRESS_VALID"
- "User joining other network using physical MAC!"
- "User joining other network using random Mac!"
- "WFDetailContextPrivateAddressConfig: randomMACAddress='%!@(MISSING)', hardwareMACAddress='%!@(MISSING)', randomMACSwitchOn=%!d(MISSING), randomMACAddressDisabled=%!d(MISSING), connectedWithHardwareAddress=%!d(MISSING), privateAddressSupported=%!d(MISSING)"
- "failed to save private address for '%!@(MISSING)' (enabled=%!d(MISSING), address='%!@(MISSING)')"
- "initWithRandomMACAddress:hardwareMACAddress:randomMACSwitchOn:randomMACAddressDisabled:connectedWithHardwareAddress:privateAddressSupported:"
- "kWFRandomMACSwitchCellIdentifier"
- "private address state changed to %!d(MISSING) for '%!@(MISSING)' (address='%!@(MISSING)', currentNetwork=%!d(MISSING))"
- "randomMACCellAtIndexPath:shouldShowSwitch:chinaDevice:"
- "saveHardwareMAC"
- "saveRandomMAC"
- "saved private address for '%!@(MISSING)' (enabled=%!d(MISSING), address='%!@(MISSING)')"
- "v16@?0B8B12"

```
