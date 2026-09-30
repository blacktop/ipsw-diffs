## safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

-57.0.3.0.0
-  __TEXT.__text: 0xaad54
+57.0.4.0.0
+  __TEXT.__text: 0xab288
   __TEXT.__auth_stubs: 0xec0
-  __TEXT.__objc_stubs: 0x2360
+  __TEXT.__objc_stubs: 0x23c0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x84c
   __TEXT.__const: 0x8577
-  __TEXT.__gcc_except_tab: 0xa4b0
-  __TEXT.__cstring: 0x440f
-  __TEXT.__oslogstring: 0x25b9e
+  __TEXT.__gcc_except_tab: 0xa514
+  __TEXT.__cstring: 0x443f
+  __TEXT.__oslogstring: 0x25d5f
   __TEXT.__objc_classname: 0x1b7
-  __TEXT.__objc_methname: 0x28f7
+  __TEXT.__objc_methname: 0x2929
   __TEXT.__objc_methtype: 0x111e
-  __TEXT.__unwind_info: 0x3380
+  __TEXT.__unwind_info: 0x3378
   __DATA_CONST.__auth_got: 0x770
-  __DATA_CONST.__got: 0x470
+  __DATA_CONST.__got: 0x468
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x6c78
-  __DATA_CONST.__cfstring: 0x4880
+  __DATA_CONST.__const: 0x6c90
+  __DATA_CONST.__cfstring: 0x48c0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__objc_arraydata: 0x28
+  __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0xe08
-  __DATA.__objc_selrefs: 0xc58
+  __DATA.__objc_selrefs: 0xc70
   __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x3d8
-  __DATA.__bss: 0x5d8
+  __DATA.__bss: 0x5e8
   __DATA.__common: 0x48
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2728
-  Symbols:   396
-  CStrings:  3075
+  Functions: 2730
+  Symbols:   397
+  CStrings:  3085
 
Symbols:
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantDictionary
- _OBJC_CLASS_$_NSSet
CStrings:
+ "allKeys"
+ "arrayWithArray:"
+ "containsObject:"
+ "dictionaryWithDictionary:"
+ "motionHarvestCountryConfig"
+ "motionHarvestToggles"
+ "{\"msg%{public}.0s\":\"#assetConfig,readEqSensingAsset\", \"countryConfig\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#assetConfig,readEqSensingAsset\", \"toggles\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#chsel,addCountryConfig,already in config\", \"country\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#ctsa,onAssetReceived\"}"
+ "{\"msg%{public}.0s\":\"#ctsa,onMotionHarvestPref\", \"toggles\":%{private, location:escape_only}@}"
- "setWithObjects:"

```
