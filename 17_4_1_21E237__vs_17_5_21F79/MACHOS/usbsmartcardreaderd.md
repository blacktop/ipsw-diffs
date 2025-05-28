## usbsmartcardreaderd

> `/System/Library/CryptoTokenKit/usbsmartcardreaderd.slotd/usbsmartcardreaderd`

```diff

-685.100.14.0.0
-  __TEXT.__text: 0x15d2c
+685.120.5.0.0
+  __TEXT.__text: 0x1676c
   __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_stubs: 0x2f00
-  __TEXT.__objc_methlist: 0x1488
+  __TEXT.__objc_stubs: 0x2f80
+  __TEXT.__objc_methlist: 0x14b0
   __TEXT.__const: 0x230
   __TEXT.__objc_classname: 0x1f9
-  __TEXT.__objc_methname: 0x2217
+  __TEXT.__objc_methname: 0x2283
   __TEXT.__objc_methtype: 0x86f
-  __TEXT.__oslogstring: 0x12bd
-  __TEXT.__cstring: 0x17b7
+  __TEXT.__oslogstring: 0x138f
+  __TEXT.__cstring: 0x15a3
   __TEXT.__gcc_except_tab: 0x1d0
-  __TEXT.__unwind_info: 0x564
+  __TEXT.__unwind_info: 0x574
   __DATA_CONST.__auth_got: 0x330
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x7a8
-  __DATA_CONST.__cfstring: 0x2460
+  __DATA_CONST.__const: 0x7b8
+  __DATA_CONST.__cfstring: 0x20e0
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x158
   __DATA_CONST.__objc_superrefs: 0xc0
-  __DATA_CONST.__objc_intobj: 0x3f0
+  __DATA_CONST.__objc_intobj: 0x408
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__objc_arraydata: 0xc0
+  __DATA_CONST.__objc_arraydata: 0xe0
+  __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x120
-  __DATA.__objc_const: 0x2a10
-  __DATA.__objc_selrefs: 0xcd0
-  __DATA.__objc_ivar: 0xdc
+  __DATA.__objc_const: 0x2a40
+  __DATA.__objc_selrefs: 0xcf0
+  __DATA.__objc_ivar: 0xe0
   __DATA.__objc_data: 0x8c0
   __DATA.__data: 0x190
   __DATA.__bss: 0xd0

   - /System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 648
-  Symbols:   143
-  CStrings:  1140
+  Functions: 664
+  Symbols:   144
+  CStrings:  1123
 
Symbols:
+ _OBJC_CLASS_$_NSConstantDictionary
CStrings:
+ "    defaultClock: %.1f MHz\n"
+ "    dwDataRate: %.3f kbps\n"
+ "    dwMaxDataRate: %.3f kbps\n"
+ "    dwMaximumClock: %.1f MHz\n"
+ "%.3f kbps for fMax: %.1fMHz) }"
+ "(%.3f kbps at 4.0MHz, "
+ "Di: %2d "
+ "Fi: %4d "
+ "PPSVersion"
+ "Set reader data rate to: %.3f kbps"
+ "T@\"NSString\",R,V_slotName"
+ "The %{public}@ does not implement 'GetParameters'"
+ "_PPSVersion"
+ "arrayWithObjects:count:"
+ "card accepted FIndexDIndex: %{public}@"
+ "card card in specific mode"
+ "card rejected FIndexDIndex: %{public}@"
+ "com.apple.CryptoTokenKit.ccid"
+ "failed to Negotiate transmission parameters"
+ "failed to set parameters: %{public}@"
+ "findSuitableFDIndexes:"
+ "native"
+ "setProtocol_v1:"
+ "setProtocol_v2:"
+ "slotName"
- "    defaultClock: %d\n"
- "    dwDataRate: %d\n"
- "    dwMaxDataRate: %d\n"
- "    dwMaximumClock: %d\n"
- "%d bits/s for fMax: %.1fMHz) }"
- "(%d bits/s at 4.0MHz, "
- "Di: %d "
- "Failed to get parameters."
- "Fi: %d "
- "Set reader data rate to: %d bits/s"
- "com.apple.CryptoTokenKit.ccid.descriptor"
- "com.apple.CryptoTokenKit.ccid.features"
- "numberWithBool:"
- "sendAnalytics:"

```
