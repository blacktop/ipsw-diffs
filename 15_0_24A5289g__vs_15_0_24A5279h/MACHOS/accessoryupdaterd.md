## accessoryupdaterd

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd`

```diff

-1163.0.0.0.0
-  __TEXT.__text: 0xce870
-  __TEXT.__auth_stubs: 0x1fe0
+1155.0.0.0.0
+  __TEXT.__text: 0xce748
+  __TEXT.__auth_stubs: 0x1fc0
   __TEXT.__objc_stubs: 0x85e0
-  __TEXT.__objc_methlist: 0x357c
-  __TEXT.__cstring: 0x237e3
+  __TEXT.__objc_methlist: 0x35e4
+  __TEXT.__cstring: 0x23878
   __TEXT.__const: 0x12a20
-  __TEXT.__objc_methname: 0x9cfe
-  __TEXT.__oslogstring: 0x49df
-  __TEXT.__objc_classname: 0x74f
-  __TEXT.__objc_methtype: 0x1f58
-  __TEXT.__gcc_except_tab: 0x50c
+  __TEXT.__objc_methname: 0x9cc9
+  __TEXT.__oslogstring: 0x4980
+  __TEXT.__objc_classname: 0x764
+  __TEXT.__objc_methtype: 0x1f62
+  __TEXT.__gcc_except_tab: 0x51c
   __TEXT.__ustring: 0x116
   __TEXT.__dlopen_cstrs: 0xa4
   __TEXT.__info_plist: 0x404
   __TEXT.__unwind_info: 0x2650
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0x1000
-  __DATA_CONST.__got: 0x4a8
+  __DATA_CONST.__auth_got: 0xff0
+  __DATA_CONST.__got: 0x4a0
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x5b38
+  __DATA_CONST.__const: 0x5b18
   __DATA_CONST.__cfstring: 0x11c60
-  __DATA_CONST.__objc_classlist: 0x1a8
+  __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0x1a0
+  __DATA_CONST.__objc_protorefs: 0x60
+  __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0xb368
+  __DATA.__objc_const: 0xb4c0
   __DATA.__objc_selrefs: 0x26a8
-  __DATA.__objc_ivar: 0x5b4
-  __DATA.__objc_data: 0x1090
+  __DATA.__objc_ivar: 0x5c4
+  __DATA.__objc_data: 0x10e0
   __DATA.__data: 0x132d
   __DATA.__bss: 0x1ce0
   __DATA.__common: 0x18

   - /usr/lib/libcrypto.35.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3928
-  Symbols:   671
-  CStrings:  4889
+  Functions: 3924
+  Symbols:   668
+  CStrings:  4892
 
Symbols:
- _OBJC_CLASS_$_UARPPersonalizationManager
- _UARPStringCrashAnalyticsDirectoryFilePath
- _UARPStringTapToRadarFilePath
CStrings:
+ "-[UARPManager queryPendingTssRequestsForUpdater:]"
+ "-[UARPManager tssResponse:updaterName:]"
+ "-[UARPManagerAUD queryPendingTssRequestsForUpdater:]"
+ "-[UARPManagerAUD tssResponse:updaterName:]"
+ "-[UARPPersonalizationManager getOutstandingPersonalizationRequests:reply:]"
+ "-[UARPPersonalizationManager personalizationResponse:updaterName:]"
+ "libauthinstall-1033.0.1"
+ "personalization"
- "-[UARPManagerAUD personalizationHelperQueryPendingTssRequests:]"
- "-[UARPManagerAUD personalizationHelperTssResponse:updaterName:]"
- "Ap,ProductMarketingVersion"
- "Finished copying manifest entitlements."
- "libauthinstall-1033.0.2"

```
