## BrightnessControl

> `/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl`

```diff

-2079.42.3.0.0
-  __TEXT.__text: 0xdf50
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__objc_methlist: 0xd84
+2079.60.14.502.2
+  __TEXT.__text: 0xe514
+  __TEXT.__auth_stubs: 0x620
+  __TEXT.__objc_methlist: 0xd94
   __TEXT.__const: 0x3fd8
   __TEXT.__gcc_except_tab: 0x208
-  __TEXT.__cstring: 0x11ee
-  __TEXT.__oslogstring: 0xd29
-  __TEXT.__unwind_info: 0x470
+  __TEXT.__cstring: 0x12ed
+  __TEXT.__oslogstring: 0xda4
+  __TEXT.__unwind_info: 0x478
   __TEXT.__objc_classname: 0x1e9
-  __TEXT.__objc_methname: 0x1927
+  __TEXT.__objc_methname: 0x1944
   __TEXT.__objc_methtype: 0x62a
-  __TEXT.__objc_stubs: 0x15a0
+  __TEXT.__objc_stubs: 0x15e0
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__const: 0x388
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x770
+  __DATA_CONST.__objc_selrefs: 0x778
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x318
+  __AUTH_CONST.__auth_got: 0x328
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x18a0
-  __AUTH_CONST.__objc_const: 0x2098
+  __AUTH_CONST.__cfstring: 0x1a80
+  __AUTH_CONST.__objc_const: 0x20b8
   __AUTH_CONST.__objc_floatobj: 0x120
+  __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x160
+  __DATA.__objc_ivar: 0x164
   __DATA.__data: 0x248
   __DATA.__bss: 0x28
   __DATA.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8E148BB1-2DC5-3A97-87B0-CB9008EAE34F
-  Functions: 386
-  Symbols:   1361
-  CStrings:  1009
+  UUID: 087CDF8E-A60B-35A9-82A6-AAE731BE64E8
+  Functions: 390
+  Symbols:   1372
+  CStrings:  1044
 
Symbols:
+ -[BCAppleBacklightBrtControl parseCPMSParams]
+ -[BCAppleBacklightBrtControl setDisplayService:].cold.1
+ _CFDataGetBytePtr
+ _OBJC_IVAR_$_BCAppleBacklightBrtControl._dispService
+ _load_string_from_edt
+ _load_uint32_array_from_edt
+ _memmove
+ _objc_msgSend$newArrayFromIntegers:size:
+ _objc_msgSend$parseCPMSParams
Functions:
~ -[BCAppleBacklightBrtControl setDisplayService:] : 4 -> 248
+ -[BCAppleBacklightBrtControl parseCPMSParams]
+ _load_uint32_array_from_edt
+ _load_string_from_edt
+ -[BCAppleBacklightBrtControl setDisplayService:].cold.1
CStrings:
+ "CPMS"
+ "CPMSAPLSize"
+ "CPMSAPLTable"
+ "CPMSNitSize"
+ "CPMSNitTable"
+ "CPMSVbattCurrentNominal"
+ "CPMSWattNitConversion"
+ "Display service found. Initializing dispService related properties"
+ "Unable to find display service."
+ "_dispService"
+ "cpmsparams = %{public}@"
+ "parseCPMSParams"
+ "power-lut-data-lut"
+ "power-lut-data-x"
+ "power-lut-data-xindex"
+ "power-lut-data-y"
+ "power-lut-data-yindex"
+ "power-lut-vbatt-cur-nominal"
+ "use-cpms-lut"
+ "use-modern-cpms"

```
