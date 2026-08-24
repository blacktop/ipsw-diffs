## ScreenSaver

> `/System/Library/Frameworks/ScreenSaver.framework/Versions/A/ScreenSaver`

```diff

-2027.0.1.0.0
-  __TEXT.__text: 0x13620
-  __TEXT.__objc_methlist: 0x1a14
+2027.0.3.0.0
+  __TEXT.__text: 0x13774
+  __TEXT.__objc_methlist: 0x1a2c
   __TEXT.__const: 0x88
   __TEXT.__gcc_except_tab: 0x288
-  __TEXT.__cstring: 0x2541
-  __TEXT.__oslogstring: 0x1c2d
+  __TEXT.__cstring: 0x25c9
+  __TEXT.__oslogstring: 0x1cf6
   __TEXT.__unwind_info: 0x6c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1650
+  __DATA_CONST.__objc_selrefs: 0x1660
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0xe0
-  __DATA_CONST.__got: 0x348
-  __AUTH_CONST.__const: 0x6b0
-  __AUTH_CONST.__cfstring: 0x1880
-  __AUTH_CONST.__objc_const: 0x24d0
+  __DATA_CONST.__got: 0x350
+  __AUTH_CONST.__const: 0x680
+  __AUTH_CONST.__cfstring: 0x1860
+  __AUTH_CONST.__objc_const: 0x24e0
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /System/Library/Frameworks/Photos.framework/Versions/A/Photos
   - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
+  - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/SkyLight
   - /System/Library/PrivateFrameworks/SystemDesktopAppearance.framework/Versions/A/SystemDesktopAppearance

   - /System/Library/PrivateFrameworks/login.framework/Versions/A/login
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 597
+  Functions: 598
   Symbols:   1592
-  CStrings:  460
+  CStrings:  464
 
Symbols:
+ -[ScreenSaverExtensionModule setViewBridgeEndpoint:]
+ -[ScreenSaverExtensionModule viewBridgeEndpoint]
+ _UTTypeDirectory
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0l
+ _objc_msgSend$setAllowedContentTypes:
+ _objc_msgSend$setViewBridgeEndpoint:
+ _objc_msgSend$viewBridgeEndpoint
- _OUTLINED_FUNCTION_8
- __73-[ScreenSaverExtensionModule loadViewForFrame:isPreview:completionBlock:]_block_invoke_3
- ___65-[ScreenSaverExtensionModule requestConfigurationViewController:]_block_invoke_3
- ___70-[ScreenSaverExtensionModule requestConfigurationSheetViewController:]_block_invoke_3
- ___block_descriptor_64_e8_32s40s48bs_e5_v8?0l
- ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0l
- _objc_msgSend$setAllowedFileTypes:
CStrings:
+ "%s -- No viewBridgeEndpoint available for configuration sheet: %{public}@"
+ "%s -- No viewBridgeEndpoint available for configuration view: %{public}@"
+ "%s -- No viewBridgeEndpoint available for: %{public}@"
+ "-[ScreenSaverExtensionModule loadViewForFrame:isPreview:completionBlock:]_block_invoke_2"
+ "-[ScreenSaverExtensionModule requestConfigurationSheetViewController:]_block_invoke"
+ "-[ScreenSaverExtensionModule requestConfigurationViewController:]_block_invoke"
- "-[ScreenSaverExtensionModule loadViewForFrame:isPreview:completionBlock:]_block_invoke_3"
- "viewBridgeEndpoint is NULL"
```
