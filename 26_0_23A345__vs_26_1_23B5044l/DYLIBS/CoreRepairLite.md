## CoreRepairLite

> `/System/Library/PrivateFrameworks/CoreRepairLite.framework/CoreRepairLite`

```diff

-921.0.120.0.0
-  __TEXT.__text: 0xb8d8
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x328
+921.40.47.0.0
+  __TEXT.__text: 0xb5fc
+  __TEXT.__auth_stubs: 0x740
+  __TEXT.__objc_methlist: 0x320
   __TEXT.__const: 0xc3
-  __TEXT.__oslogstring: 0x17c0
+  __TEXT.__oslogstring: 0x17da
   __TEXT.__gcc_except_tab: 0xf8
-  __TEXT.__cstring: 0x567
-  __TEXT.__unwind_info: 0x1c8
+  __TEXT.__cstring: 0x526
+  __TEXT.__unwind_info: 0x1b8
   __TEXT.__objc_classname: 0x49
-  __TEXT.__objc_methname: 0xb36
+  __TEXT.__objc_methname: 0xb1f
   __TEXT.__objc_methtype: 0x1d7
-  __TEXT.__objc_stubs: 0xc80
+  __TEXT.__objc_stubs: 0xc60
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3c0
+  __DATA_CONST.__objc_selrefs: 0x3b8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0x3b8
+  __AUTH_CONST.__auth_got: 0x3b0
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x940
+  __AUTH_CONST.__cfstring: 0x8a0
   __AUTH_CONST.__objc_const: 0x2b0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x140

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport
   - /usr/lib/libFDR.dylib
-  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5D0B296C-85D0-3625-907C-B734B1FE5242
-  Functions: 209
+  UUID: 5451AFEF-F6A0-3493-9B64-AE408BDF0DF4
+  Functions: 210
   Symbols:   763
-  CStrings:  502
+  CStrings:  491
 
Symbols:
+ +[CRFDRUtils _getPropertiesFromSealingMap].cold.1
+ +[CRFDRUtils _getPropertiesFromSealingMap].cold.2
+ _AMFDRSealingMapCopyPropertyTagsAndIdentifiers
+ _OUTLINED_FUNCTION_10
- +[CRFDRUtils _getPropertyArrayFrom:]
- +[CRFDRUtils _getPropertyArrayFrom:].cold.1
- +[CRFDRUtils _getPropertyArrayFrom:].cold.2
- _AMFDRGetSealingMap
- _MGCopyAnswer
- _objc_msgSend$_getPropertyArrayFrom:
CStrings:
+ "Failed to get properties from sealing map: %@"
+ "Property is not a dictionary"
- "Failed to get product type"
- "ManifestProperties"
- "ProductType"
- "Properties"
- "PropertyIdentifier"
- "Tag"
- "_getPropertyArrayFrom:"
- "sealingMap is invalid"

```
