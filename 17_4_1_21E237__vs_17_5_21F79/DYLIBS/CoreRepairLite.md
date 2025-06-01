## CoreRepairLite

> `/System/Library/PrivateFrameworks/CoreRepairLite.framework/CoreRepairLite`

```diff

-397.100.12.0.0
-  __TEXT.__text: 0x89c4
-  __TEXT.__auth_stubs: 0x630
+397.120.5.0.0
+  __TEXT.__text: 0x8b88
+  __TEXT.__auth_stubs: 0x660
   __TEXT.__objc_methlist: 0x1e8
   __TEXT.__const: 0x5f
-  __TEXT.__oslogstring: 0x13e1
-  __TEXT.__gcc_except_tab: 0xc4
+  __TEXT.__oslogstring: 0x13f8
+  __TEXT.__gcc_except_tab: 0xd8
   __TEXT.__cstring: 0x399
   __TEXT.__unwind_info: 0x108
   __TEXT.__objc_classname: 0x33
   __TEXT.__objc_methname: 0x776
   __TEXT.__objc_methtype: 0x14d
   __TEXT.__objc_stubs: 0x940
-  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH_CONST.__cfstring: 0x400
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__auth_got: 0x328
+  __AUTH_CONST.__auth_got: 0x340
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x4
   __DATA.__bss: 0x18

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libFDR.dylib
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 384025D5-A9BB-3E1E-BF5E-F60803972049
+  UUID: 0954D50F-E4C9-3E08-99C2-187A88E03681
   Functions: 170
-  Symbols:   133
-  CStrings:  336
+  Symbols:   137
+  CStrings:  337
 
Symbols:
+ _AMFDRSealingMapCreateLocalMultiDataBlobForClass
+ _AMFDRSealingMapEntryHasAttribute
+ _MGGetProductType
+ _kAMFDRSealingMapAttributeEarlyAccessMultiData
CStrings:
+ "Copying multi data: %@"

```
