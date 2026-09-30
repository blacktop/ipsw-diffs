## EAFirmwareUpdater

> `/System/Library/PrivateFrameworks/EAFirmwareUpdater.framework/Versions/A/EAFirmwareUpdater`

```diff

-1170.80.6.0.1
-  __TEXT.__text: 0xbeb0
+1207.100.66.0.0
+  __TEXT.__text: 0xc04c
   __TEXT.__auth_stubs: 0x430
-  __TEXT.__objc_methlist: 0x928
+  __TEXT.__objc_methlist: 0xb04
   __TEXT.__const: 0x70
   __TEXT.__cstring: 0x3e27
   __TEXT.__oslogstring: 0x215
-  __TEXT.__gcc_except_tab: 0xdc
+  __TEXT.__gcc_except_tab: 0xf4
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x2c8
+  __TEXT.__unwind_info: 0x2d0
   __TEXT.__objc_classname: 0x81
-  __TEXT.__objc_methname: 0x2b2c
-  __TEXT.__objc_methtype: 0x54e
-  __TEXT.__objc_stubs: 0x2480
+  __TEXT.__objc_methname: 0x2bc8
+  __TEXT.__objc_methtype: 0x55e
+  __TEXT.__objc_stubs: 0x2500
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__const: 0xd8
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb38
+  __DATA_CONST.__objc_selrefs: 0xbf0
   __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__auth_got: 0x228
   __AUTH_CONST.__const: 0x200
   __AUTH_CONST.__cfstring: 0x2ae0
-  __AUTH_CONST.__objc_const: 0x1688
+  __AUTH_CONST.__objc_const: 0x1348
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x174

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 92A4B9A8-7C5B-3FC8-8011-A40D106FDDD0
-  Functions: 262
-  Symbols:   828
-  CStrings:  1422
+  UUID: 79D5E7F0-98A1-3E3D-809F-CEC4D1812ECE
+  Functions: 279
+  Symbols:   861
+  CStrings:  1428
 
Symbols:
+ +[NSFileHandle(Availability) uarpCreateFileHandleForWritingToURL:error:]
+ -[EAFirmwareUpdater _accessoryDidConnect:].cold.1
+ -[EAFirmwareUpdater _accessoryDidConnect:].cold.2
+ -[EAFirmwareUpdater _accessoryDidDisconnect:].cold.1
+ -[EAFirmwareUpdater applyFirmware:progress:update:personalization:].cold.1
+ -[EAFirmwareUpdater createEndOfUpdateEventDict:error:].cold.1
+ -[EAFirmwareUpdater getPersonalizationID].cold.1
+ -[EAFirmwareUpdater personalizationResponse:error:].cold.1
+ -[EAFirmwareUpdater personalizationResponse:error:].cold.2
+ -[EAFirmwareUpdater stitchManifestInSuperBinary:withManifest:withId:].cold.1
+ -[EAFirmwareUpdater stitchManifestInSuperBinary:withManifest:withId:].cold.2
+ -[EAFirmwareUpdater validateAssetAttributes:].cold.1
+ -[iAUPServer personalizationComplete].cold.1
+ -[iAUPServer processInByte:].cold.1
+ -[iAUPServer processInByte:].cold.2
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __67-[EAFirmwareUpdater applyFirmware:progress:update:personalization:]_block_invoke.cold.1
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSFileHandle_$_Availability
+ _objc_msgSend$createFileAtPath:contents:attributes:
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileHandleForWritingToURL:error:
+ _objc_msgSend$removeItemAtPath:error:
CStrings:
+ "@32@0:8@16o^@24"
+ "createFileAtPath:contents:attributes:"
+ "fileExistsAtPath:"
+ "fileHandleForWritingToURL:error:"
+ "removeItemAtPath:error:"
+ "uarpCreateFileHandleForWritingToURL:error:"

```
