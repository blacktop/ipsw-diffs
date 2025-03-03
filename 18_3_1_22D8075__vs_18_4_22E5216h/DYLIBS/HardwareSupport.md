## HardwareSupport

> `/System/Library/PrivateFrameworks/HardwareSupport.framework/HardwareSupport`

```diff

-32.0.0.0.0
-  __TEXT.__text: 0x6f34
-  __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_methlist: 0x7b4
+34.0.0.0.0
+  __TEXT.__text: 0x6bcc
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__objc_methlist: 0xa3c
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x823
-  __TEXT.__oslogstring: 0x375
+  __TEXT.__cstring: 0x831
+  __TEXT.__oslogstring: 0x2e4
   __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__unwind_info: 0x240
+  __TEXT.__unwind_info: 0x230
   __TEXT.__objc_classname: 0x1e4
-  __TEXT.__objc_methname: 0x10bb
-  __TEXT.__objc_methtype: 0x619
+  __TEXT.__objc_methname: 0x1088
+  __TEXT.__objc_methtype: 0x60b
   __TEXT.__objc_stubs: 0xc80
-  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__got: 0x118
   __DATA_CONST.__const: 0x148
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x480
+  __DATA_CONST.__objc_selrefs: 0x508
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x3b0
+  __DATA_CONST.__objc_superrefs: 0x70
+  __AUTH_CONST.__auth_got: 0x3a8
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x6e0
-  __AUTH_CONST.__objc_const: 0x1a20
+  __AUTH_CONST.__cfstring: 0x700
+  __AUTH_CONST.__objc_const: 0x1570
   __AUTH.__objc_data: 0x370
   __DATA.__objc_ivar: 0x7c
   __DATA.__data: 0x2a0

   - /usr/lib/libIOReport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 192
-  Symbols:   366
-  CStrings:  406
+  Functions: 187
+  Symbols:   361
+  CStrings:  402
 
Symbols:
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryFromPath
+ __os_log_default
+ _kIOMainPortDefault
+ _objc_retain_x25
+ _objc_retain_x26
- _IOIteratorNext
- _IOObjectCopyClass
- _IORegistryEntryGetChildIterator
- _IOServiceGetMatchingService
- _IOServiceNameMatching
- _kIOMasterPortDefault
CStrings:
+ "%@ISPCaptureDeviceCreate"
+ "/System/Library/MediaCapture/%@ISP.mediacapture"
+ "Could not determine soc-generation from IOReg!"
+ "Could not find arm-io entry!"
+ "Expected to find 2 matched regex groups {H\\d+, \\d+} in %@."
+ "H%ld"
+ "H(\\d+)"
+ "IODeviceTree:/arm-io"
+ "initWithData:encoding:"
+ "integerValue"
+ "soc-generation"
- "/System/Library/MediaCapture/HxISP.mediacapture"
- "@32@0:8@16@24"
- "Apple(H\\d+)CamIn"
- "Cannot determine PlugIn version from %@."
- "Expected to find 2 matched regex groups {AppleH\\d+CamIn, \\d+} in %@."
- "Found isp child named %@"
- "Hx"
- "HxISPCaptureDeviceCreate"
- "IORegistryEntryGetChildIterator failed %s."
- "IOService"
- "IOServiceGetMatchingService for name matching isp found nothing."
- "Name for child of isp is unknowable."
- "initWithFactoryFunctionSymbol:atPath:"
- "isp"
- "stringByReplacingOccurrencesOfString:withString:"

```
