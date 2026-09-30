## CoreUARP

> `/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP`

```diff

-1338.0.62.0.1
-  __TEXT.__text: 0x8ad20
+1338.0.72.0.0
+  __TEXT.__text: 0x8adec
   __TEXT.__auth_stubs: 0xa00
   __TEXT.__objc_methlist: 0x8b3c
   __TEXT.__const: 0x220
-  __TEXT.__cstring: 0x7b7d
-  __TEXT.__oslogstring: 0x65b1
+  __TEXT.__cstring: 0x7bc7
+  __TEXT.__oslogstring: 0x6619
   __TEXT.__gcc_except_tab: 0x88c
   __TEXT.__dlopen_cstrs: 0xa4
   __TEXT.__unwind_info: 0x25f0

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: 422A4A17-7B9C-346D-A077-AF658C107CE9
+  UUID: 7B5DE204-EB2F-37CF-8977-4F670A33113C
   Functions: 3906
   Symbols:   12408
-  CStrings:  5823
+  CStrings:  5826
 
Functions:
~ -[UARPUploaderEndpoint addTxFirmwareAsset:] : 516 -> 588
~ ___60-[UARPUploaderUARP protocolVersionSelected:protocolVersion:]_block_invoke : 1508 -> 1628
~ _uarpPlatformAssetResponseData : 424 -> 436
CStrings:
+ "%s: Calling UARPPlatformControllerReofferFirmwareAsset() for %@"
+ "-[UARPUploaderUARP protocolVersionSelected:protocolVersion:]_block_invoke"
+ "Add Tx Firmware Asset...  is null? fail"

```
