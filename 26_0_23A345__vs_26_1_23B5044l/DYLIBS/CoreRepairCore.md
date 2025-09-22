## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

```diff

-921.0.120.0.0
-  __TEXT.__text: 0x84530
-  __TEXT.__auth_stubs: 0x1680
-  __TEXT.__objc_methlist: 0x3a8c
+921.40.47.0.0
+  __TEXT.__text: 0x84290
+  __TEXT.__auth_stubs: 0x1670
+  __TEXT.__objc_methlist: 0x3a7c
   __TEXT.__const: 0x7f8
-  __TEXT.__oslogstring: 0x912f
-  __TEXT.__cstring: 0x5aa0
-  __TEXT.__gcc_except_tab: 0x1750
-  __TEXT.__unwind_info: 0x11c8
+  __TEXT.__oslogstring: 0x917f
+  __TEXT.__cstring: 0x5ab3
+  __TEXT.__gcc_except_tab: 0x1758
+  __TEXT.__unwind_info: 0x11c0
   __TEXT.__objc_classname: 0x7f0
-  __TEXT.__objc_methname: 0x7fc0
+  __TEXT.__objc_methname: 0x7f7d
   __TEXT.__objc_methtype: 0x1538
-  __TEXT.__objc_stubs: 0x6540
+  __TEXT.__objc_stubs: 0x64e0
   __DATA_CONST.__got: 0x560
   __DATA_CONST.__const: 0x8b0
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ff8
+  __DATA_CONST.__objc_selrefs: 0x1fe0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0xa60
-  __AUTH_CONST.__auth_got: 0xb50
+  __AUTH_CONST.__auth_got: 0xb48
   __AUTH_CONST.__const: 0x520
   __AUTH_CONST.__cfstring: 0x7280
   __AUTH_CONST.__objc_const: 0x58b8

   __DATA.__common: 0x30
   __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0xcd0
-  __DATA_DIRTY.__bss: 0x170
+  __DATA_DIRTY.__bss: 0x168
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: FFEED41E-A266-3EDA-B533-D646A4F75069
+  UUID: E428B5BD-8B9A-38B9-96FF-FE18EC6A7B81
   Functions: 2260
-  Symbols:   7470
-  CStrings:  4800
+  Symbols:   7466
+  CStrings:  4799
 
Symbols:
+ +[CRFDRUtils _getPropertiesFromSealingMap].cold.1
+ +[CRFDRUtils _getPropertiesFromSealingMap].cold.2
+ -[CRCCertificate dealloc]
+ _AMFDRSealingMapCopyPropertyTagsAndIdentifiers
+ ___60-[CRFDRBaseDeviceHandler challengeComponentsWith:withReply:]_block_invoke.255
+ _objc_msgSend$isStrongComponent:
- +[CRFDRBaseDeviceHandler _populateSealingMapProperties]
- +[CRFDRBaseDeviceHandler getSealingMap]
- +[CRFDRUtils _getPropertyArrayFrom:]
- +[CRFDRUtils _getPropertyArrayFrom:].cold.1
- +[CRFDRUtils _getPropertyArrayFrom:].cold.2
- _AMFDRGetSealingMap
- _AMFDRSealingMapCallMGCopyAnswer
- ___60-[CRFDRBaseDeviceHandler challengeComponentsWith:withReply:]_block_invoke.256
- _gSealingMapPropertyDict
- _objc_msgSend$_getPropertyArrayFrom:
- _objc_msgSend$_populateSealingMapProperties
- _objc_msgSend$getPropertyArrayFrom:
- _objc_msgSend$getSealingMap
CStrings:
+ "Failed to get properties from sealing map: %@"
+ "Property is not a dictionary"
+ "Unable to fetch property: %@"
+ "Unsupported data type of property %@"
+ "copied property %@ : %@"
- "PropertyIdentifier"
- "Unable to fetch property:%@"
- "_getPropertyArrayFrom:"
- "_populateSealingMapProperties"
- "copied property:%@"
- "getSealingMap"

```
