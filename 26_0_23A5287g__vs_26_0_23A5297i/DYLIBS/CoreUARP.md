## CoreUARP

> `/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP`

```diff

-1338.0.46.502.1
-  __TEXT.__text: 0x8a780
+1338.0.62.0.1
+  __TEXT.__text: 0x8ad20
   __TEXT.__auth_stubs: 0xa00
   __TEXT.__objc_methlist: 0x8b3c
   __TEXT.__const: 0x220
-  __TEXT.__cstring: 0x7b1a
-  __TEXT.__oslogstring: 0x647b
+  __TEXT.__cstring: 0x7b7d
+  __TEXT.__oslogstring: 0x65b1
   __TEXT.__gcc_except_tab: 0x88c
   __TEXT.__dlopen_cstrs: 0xa4
-  __TEXT.__unwind_info: 0x25e8
-  __TEXT.__objc_classname: 0x18d0
-  __TEXT.__objc_methname: 0xe0f5
+  __TEXT.__unwind_info: 0x25f0
+  __TEXT.__objc_classname: 0x18ce
+  __TEXT.__objc_methname: 0xe114
   __TEXT.__objc_methtype: 0x3f03
-  __TEXT.__objc_stubs: 0x97e0
-  __DATA_CONST.__got: 0x760
+  __TEXT.__objc_stubs: 0x97c0
+  __DATA_CONST.__got: 0x768
   __DATA_CONST.__const: 0x2080
   __DATA_CONST.__objc_classlist: 0x688
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3158
+  __DATA_CONST.__objc_selrefs: 0x3150
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x678
+  __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x510
   __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0x7180
-  __AUTH_CONST.__objc_const: 0x11a68
+  __AUTH_CONST.__cfstring: 0x71e0
+  __AUTH_CONST.__objc_const: 0x11a88
   __AUTH_CONST.__objc_intobj: 0xca8
+  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x2080
-  __DATA.__objc_ivar: 0xbc0
+  __DATA.__objc_ivar: 0xbc4
   __DATA.__data: 0x40d
   __DATA.__bss: 0x1a4b
   __DATA_DIRTY.__objc_data: 0x20d0

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: D7366875-F307-3460-822D-6905C5DB2072
-  Functions: 3899
-  Symbols:   12392
-  CStrings:  5811
+  UUID: 422A4A17-7B9C-346D-A077-AF658C107CE9
+  Functions: 3906
+  Symbols:   12408
+  CStrings:  5823
 
Symbols:
+ -[UARPDynamicAssetCrashLogEvent processCrashInstance].cold.1
+ -[UARPDynamicAssetCrashLogEvent processCrashInstance].cold.2
+ -[UARPDynamicAssetCrashLogEvent processCrashInstance].cold.3
+ -[UARPDynamicAssetCrashLogEvent processCrashInstance].cold.4
+ GCC_except_table36
+ GCC_except_table4
+ GCC_except_table64
+ _OBJC_CLASS_$_AirPodsCrashReportObjc
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_IVAR_$_UARPControllerXPC._xpcConnectionQueue
+ ___34-[UARPControllerXPC xpcConnection]_block_invoke.116
+ ___34-[UARPControllerXPC xpcConnection]_block_invoke_2
+ ___34-[UARPControllerXPC xpcConnection]_block_invoke_2.115
+ ___46-[UARPControllerXPC getAssetIDForAccessoryID:]_block_invoke.136
+ ___48-[UARPControllerXPC getAttestationCertificates:]_block_invoke.142
+ ___56-[UARPControllerXPC getSandboxExtensionTokenForAssetID:]_block_invoke.144
+ ___60-[UARPControllerXPC getSupplementalAssetNameForAccessoryID:]_block_invoke.138
+ ___61-[UARPControllerXPC getSupportedAccessories:forProductGroup:]_block_invoke.140
+ _objc_msgSend$generateReportWithBinary:testMode:productId:applicationInfo:description:
- ___46-[UARPControllerXPC getAssetIDForAccessoryID:]_block_invoke.133
- ___48-[UARPControllerXPC getAttestationCertificates:]_block_invoke.139
- ___56-[UARPControllerXPC getSandboxExtensionTokenForAssetID:]_block_invoke.141
- ___60-[UARPControllerXPC getSupplementalAssetNameForAccessoryID:]_block_invoke.135
- ___61-[UARPControllerXPC getSupportedAccessories:forProductGroup:]_block_invoke.137
- _objc_msgSend$stringByAppendingPathExtension:
- _objc_msgSend$stringByDeletingPathExtension
CStrings:
+ "%s: CoreDiagnositcs not Supported on Platform"
+ "%s: Failed to send crash report, AirPodsCrashReportObjc returned nil"
+ "-[UARPDynamicAssetCrashLogEvent processCrashInstance]"
+ ".txt"
+ "Could not produce output JSON for Crash Instance, AirPodsCrashReport is not of type NSDictionary"
+ "Could not produce output JSON for Crash Instance: %@"
+ "Successfully expanded CRSH Dynamic Asset: %@"
+ "_xpcConnectionQueue"
+ "case"
+ "generateReportWithBinary:testMode:productId:applicationInfo:description:"
+ "role"
+ "side"
+ "uarpController.xpcConnection"
- "A"
- "stringByAppendingPathExtension:"
- "stringByDeletingPathExtension"
- "txt"

```
