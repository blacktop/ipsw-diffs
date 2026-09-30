## eSCL

> `/System/Library/Image Capture/Devices/AirScanScanner.app/Contents/Frameworks/eSCL.framework/Versions/A/eSCL`

```diff

 63.2.0.0.0
-  __TEXT.__text: 0xf29c
+  __TEXT.__text: 0xf28c
   __TEXT.__auth_stubs: 0x3e0
   __TEXT.__objc_stubs: 0x2a40
-  __TEXT.__objc_methlist: 0x185c
+  __TEXT.__objc_methlist: 0x1b58
   __TEXT.__const: 0x58
   __TEXT.__cstring: 0x14d1
   __TEXT.__oslogstring: 0x7

   __TEXT.__objc_methname: 0x41c3
   __TEXT.__objc_methtype: 0xc4b
   __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__unwind_info: 0x450
+  __TEXT.__unwind_info: 0x460
   __DATA_CONST.__auth_got: 0x200
   __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__auth_ptr: 0x8

   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x4d8
   __DATA_CONST.__objc_arrayobj: 0xc0
-  __DATA.__objc_const: 0x3700
-  __DATA.__objc_selrefs: 0x10e8
+  __DATA.__objc_const: 0x3190
+  __DATA.__objc_selrefs: 0x11e0
   __DATA.__objc_ivar: 0x244
   __DATA.__objc_data: 0x780
   __DATA.__data: 0x2a0

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 868B5780-06BD-3E2E-B022-DE40A097F50D
-  Functions: 590
-  Symbols:   1480
+  UUID: A8028F9E-736D-3C6E-B18A-1D135970D521
+  Functions: 598
+  Symbols:   1488
   CStrings:  1602
 
Symbols:
+ +[DefaultESCLAuthenticationDelegate sharedInstance].cold.1
+ +[SettingProfile settingProfileWithXML:].cold.1
+ +[eSCL namespaceURIForESCLKey:].cold.1
+ +[eSCL validColorModes].cold.1
+ +[eSCL validEdgeDetectionEdges].cold.1
+ +[eSCL validImageCorrectionFeatures].cold.1
+ +[eSCL validScannerIntents].cold.1
+ _get_queue.cold.1

```
