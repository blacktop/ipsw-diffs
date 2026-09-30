## Categories

> `/System/Library/PrivateFrameworks/Categories.framework/Versions/A/Categories`

```diff

-58.0.1.0.0
-  __TEXT.__text: 0xc28c
-  __TEXT.__objc_methlist: 0x82c
-  __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0x428
-  __TEXT.__cstring: 0x2dbc
-  __TEXT.__oslogstring: 0x656
-  __TEXT.__unwind_info: 0x4c8
+58.1.3.0.0
+  __TEXT.__text: 0xbe14
+  __TEXT.__objc_methlist: 0x84c
+  __TEXT.__const: 0xc0
+  __TEXT.__gcc_except_tab: 0x3f0
+  __TEXT.__cstring: 0x2ee4
+  __TEXT.__oslogstring: 0x6bb
+  __TEXT.__unwind_info: 0x4c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x720
+  __DATA_CONST.__objc_selrefs: 0x738
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__objc_arraydata: 0xab8
+  __DATA_CONST.__objc_arraydata: 0xb30
   __DATA_CONST.__got: 0xf0
-  __AUTH_CONST.__const: 0x830
-  __AUTH_CONST.__cfstring: 0x36c0
+  __AUTH_CONST.__const: 0x820
+  __AUTH_CONST.__cfstring: 0x3760
   __AUTH_CONST.__objc_const: 0xca0
-  __AUTH_CONST.__objc_arrayobj: 0x990
+  __AUTH_CONST.__objc_intobj: 0xa8
+  __AUTH_CONST.__objc_arrayobj: 0x9a8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/ContextKit.framework/Versions/A/ContextKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 250
-  Symbols:   698
-  CStrings:  501
+  Functions: 251
+  Symbols:   702
+  CStrings:  509
 
Symbols:
+ +[CTCategory _equivalentBundleIDForDestinationScheme:fromBundleID:sourceScheme:]
+ +[CTCategory bundleIDForDeviceFamily:fromBundleID:fromDeviceFamily:]
+ +[CTCategory currentDeviceFamily]
+ +[CTCategory deviceFamilyForPlatform:]
+ +[CTCategory schemeStringForDeviceFamily:]
+ -[CTCategories bundleIDForDeviceFamily:fromBundleID:fromDeviceFamily:]
+ GCC_except_table116
+ GCC_except_table27
+ GCC_except_table30
+ GCC_except_table32
+ GCC_except_table43
+ GCC_except_table47
+ GCC_except_table51
+ GCC_except_table88
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ ___33+[CTCategory currentDeviceFamily]_block_invoke
+ ___80+[CTCategory _equivalentBundleIDForDestinationScheme:fromBundleID:sourceScheme:]_block_invoke
+ _objc_msgSend$_equivalentBundleIDForDestinationScheme:fromBundleID:sourceScheme:
+ _objc_msgSend$bundleIDForDeviceFamily:fromBundleID:fromDeviceFamily:
+ _objc_msgSend$currentDeviceFamily
+ _objc_msgSend$deviceFamilyForPlatform:
+ _objc_msgSend$integerValue
+ _objc_msgSend$schemeStringForDeviceFamily:
+ currentDeviceFamily.deviceFamily
+ currentDeviceFamily.onceToken
- +[CTCategories currentIOSDevice]
- +[CTCategory itemWith:platform:array:]
- +[CTCategory schemeStringForPlatform:]
- GCC_except_table100
- GCC_except_table117
- GCC_except_table26
- GCC_except_table29
- GCC_except_table31
- GCC_except_table40
- GCC_except_table44
- GCC_except_table48
- GCC_except_table50
- GCC_except_table85
- __38+[CTCategory itemWith:platform:array:]_block_invoke
- ___38+[CTCategory itemWith:platform:array:]_block_invoke
- ___38+[CTCategory itemWith:platform:array:]_block_invoke_2
- ___38+[CTCategory itemWith:platform:array:]_block_invoke_3
- ___38+[CTCategory itemWith:platform:array:]_block_invoke_4
- ___56+[CTCategory bundleIDForPlatform:fromBundleID:platform:]_block_invoke
- ___block_descriptor_40_e8_32r_e25_v32?0"NSString"8Q16^B24l
- _objc_msgSend$schemeStringForPlatform:
CStrings:
+ "%s: no scheme for device family (source %ld, destination %ld); one of them is outside CTDeviceFamily"
+ "+[CTCategory bundleIDForDeviceFamily:fromBundleID:fromDeviceFamily:]"
+ "com.apple.EmojiPoster"
+ "com.apple.GradientPoster"
+ "com.apple.PridePoster"
+ "q"
+ "tvos://com.apple.Fitness"
+ "tvos://com.apple.TVAppStore"
+ "tvos://com.apple.TVMusic"
+ "tvos://com.apple.TVPhotos"
+ "tvos://com.apple.TVSettings"
+ "tvos://com.apple.TVWatchList"
+ "tvos://com.apple.facetime"
+ "tvos://com.apple.podcasts"
- "ios://"
- "iosmac://"
- "macos://"
- "tvos://"
- "visionos://"
- "watchos://"
```
