## AutoBugCaptureCore

> `/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore`

```diff

-383.80.2.0.0
-  __TEXT.__text: 0x7708c
-  __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_methlist: 0x5688
-  __TEXT.__cstring: 0x4f92
+383.100.15.0.0
+  __TEXT.__text: 0x7784c
+  __TEXT.__auth_stubs: 0xfa0
+  __TEXT.__objc_methlist: 0x5f44
+  __TEXT.__cstring: 0x501c
   __TEXT.__const: 0x290
-  __TEXT.__oslogstring: 0xecf4
-  __TEXT.__gcc_except_tab: 0x10ac
+  __TEXT.__oslogstring: 0xee7f
+  __TEXT.__gcc_except_tab: 0x10c0
   __TEXT.__ustring: 0x8
-  __TEXT.diag_actions: 0x545d
-  __TEXT.__unwind_info: 0x1580
-  __TEXT.__objc_classname: 0x9ec
-  __TEXT.__objc_methname: 0xe529
-  __TEXT.__objc_methtype: 0x22fe
-  __TEXT.__objc_stubs: 0xa240
-  __DATA_CONST.__got: 0x500
-  __DATA_CONST.__const: 0x2770
-  __DATA_CONST.__objc_classlist: 0x270
+  __TEXT.diag_actions: 0x54c4
+  __TEXT.__unwind_info: 0x1590
+  __TEXT.__objc_classname: 0xa08
+  __TEXT.__objc_methname: 0xe5b3
+  __TEXT.__objc_methtype: 0x231c
+  __TEXT.__objc_stubs: 0xa2c0
+  __DATA_CONST.__got: 0x510
+  __DATA_CONST.__const: 0x2790
+  __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x33e0
+  __DATA_CONST.__objc_selrefs: 0x36b0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1e8
+  __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x5b0
-  __AUTH_CONST.__auth_got: 0x7a0
-  __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x6920
-  __AUTH_CONST.__objc_const: 0xd6f8
+  __AUTH_CONST.__auth_got: 0x7e0
+  __AUTH_CONST.__const: 0x620
+  __AUTH_CONST.__cfstring: 0x69a0
+  __AUTH_CONST.__objc_const: 0xc848
   __AUTH_CONST.__objc_dictobj: 0x4b0
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x408
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x13b0
-  __DATA.__objc_ivar: 0x680
+  __AUTH.__objc_data: 0x1400
+  __DATA.__objc_ivar: 0x688
   __DATA.__data: 0xce0
-  __DATA.__bss: 0x220
-  __DATA.__common: 0x9
+  __DATA.__bss: 0x238
+  __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__bss: 0x150
   __DATA_DIRTY.__common: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2183
-  Symbols:   2902
-  CStrings:  5036
+  Functions: 2248
+  Symbols:   2992
+  CStrings:  5062
 
Symbols:
+ _IOIteratorNext
+ _IONotificationPortCreate
+ _IONotificationPortDestroy
+ _IONotificationPortSetDispatchQueue
+ _IOObjectRelease
+ _IOServiceAddInterestNotification
+ _IOServiceAddMatchingNotification
+ _IOServiceMatching
+ _OBJC_CLASS_$_CaseDampeningExceptions
+ _OBJC_METACLASS_$_CaseDampeningExceptions
+ _kIOMainPortDefault
+ _objc_retainAutoreleasedReturnValue
- _fmod
CStrings:
+ "\x04\x11\x17"
+ " StorageKernelSignal: KernelMsgSignalHandler init ++ \n"
+ "@\"KernelMsgSignalHandlerSDXC\""
+ "AppleSDXC"
+ "AppleSDXCSlot"
+ "CardDowntrainError"
+ "Completed startup of KernelMsgSignalHandler"
+ "IOGeneralInterest"
+ "IOServiceFirstMatch"
+ "KernelMsgSignalHandlerSDXC"
+ "No WiFi chipset"
+ "ProductName = %@, ProductClass = %@, ProductType = %@, ProductVersion = %@, BuildVersion = %@, BuildPlatform = %@, BuildVariant = %@, basebandCapability = %s, dualSIMCapable = %s, dualSIMEnabled = %s, Baseband Chipset = %@, WiFi Chipset = %@, InternalBuild = %s, FactoryBuild = %s, VendorBuild = %s, CarrierBuild = %s, SeedBuild = %s, CarrierSeedBuild = %s, CustomerSeedBuild = %s, DeviceSerialNumber = %@"
+ "StorageDrivers"
+ "StorageKernelSignal: ABC admin caseManager is Nil"
+ "StorageKernelSignal: ABC admin is Nil"
+ "StorageKernelSignal: Session %{public}@ accepted. (%@)"
+ "StorageKernelSignal: Session %{public}@ was NOT accepted. (Reason code: %d) (%@)"
+ "StorageKernelSignal: downtrain error detected. Triggering ABC\n"
+ "StorageKernelSignal: notification port destroyed\n"
+ "StorageKernelSignal: service matched\n"
+ "T@\"NSString\",R,N,V_wifiChipset"
+ "WifiChipset"
+ "_wifiChipset"
+ "init:"
+ "kernelHandler"
+ "releaseHandler"
+ "sdxc_listener"
+ "setProductType:"
+ "setWiFiChipset:"
+ "setupListener:"
+ "unavailable"
+ "wifiChipset"
- "\x04\x17"
- "."
- "Enabling NPI flag based on baseband chipset match"
- "Enabling NPI flag based on productType match"
- "ProductName = %@, ProductClass = %@, ProductType = %@, ProductVersion = %@, BuildVersion = %@, BuildPlatform = %@, BuildVariant = %@, basebandCapability = %s, dualSIMCapable = %s, dualSIMEnabled = %s, Baseband Chipset = %@, InternalBuild = %s, FactoryBuild = %s, VendorBuild = %s, CarrierBuild = %s, SeedBuild = %s, CarrierSeedBuild = %s, CustomerSeedBuild = %s, DeviceSerialNumber = %@"
- "iPhone15"
- "mav22"

```
