## FrontBoardServices

> `/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`

```diff

-1000.0.0.0.0
-  __TEXT.__text: 0xa21b4
+1000.0.1.0.0
+  __TEXT.__text: 0xa278c
   __TEXT.__auth_stubs: 0x10f0
-  __TEXT.__objc_methlist: 0x84b8
+  __TEXT.__objc_methlist: 0x84d0
   __TEXT.__const: 0x270
   __TEXT.__cstring: 0xc816
-  __TEXT.__oslogstring: 0x3c64
-  __TEXT.__gcc_except_tab: 0x23e0
-  __TEXT.__unwind_info: 0x2c70
+  __TEXT.__oslogstring: 0x3d7d
+  __TEXT.__gcc_except_tab: 0x2410
+  __TEXT.__unwind_info: 0x2c90
   __TEXT.__objc_classname: 0x1424
-  __TEXT.__objc_methname: 0x101eb
-  __TEXT.__objc_methtype: 0x3598
-  __TEXT.__objc_stubs: 0xaec0
+  __TEXT.__objc_methname: 0x10236
+  __TEXT.__objc_methtype: 0x35a6
+  __TEXT.__objc_stubs: 0xaf00
   __DATA_CONST.__got: 0x718
-  __DATA_CONST.__const: 0x2f70
+  __DATA_CONST.__const: 0x2fc0
   __DATA_CONST.__objc_classlist: 0x490
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3cc0
+  __DATA_CONST.__objc_selrefs: 0x3cd0
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x318
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x888
   __AUTH_CONST.__const: 0x820
   __AUTH_CONST.__cfstring: 0xa140
-  __AUTH_CONST.__objc_const: 0xffd0
+  __AUTH_CONST.__objc_const: 0xffc8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0xdc0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 95203443-2441-3E3C-B4F2-F6663D73CF20
-  Functions: 4272
-  Symbols:   13576
-  CStrings:  6827
+  UUID: 1E722D6D-028F-347F-BE04-06861968CDDC
+  Functions: 4275
+  Symbols:   13588
+  CStrings:  6836
 
Symbols:
+ -[FBSOrientationObserver _getAndSetFreshestUpdateGivenUpdate:forced:]
+ -[FBSOrientationObserver _lock_getAndSetFreshestUpdateGivenUpdate:forced:]
+ -[FBSOrientationObserverClient _connectionInterrupted:]
+ -[FBSOrientationObserverClient _server:registerOrientationInterest:]
+ GCC_except_table21
+ ___58-[FBSOrientationObserver handleOrientationResetForClient:]_block_invoke
+ ___68-[FBSOrientationObserverClient _server:registerOrientationInterest:]_block_invoke
+ ___block_descriptor_40_e8_32w_e42_v24?0"FBSOrientationUpdate"8"NSError"16lw32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32bs40w_e30_v16?0"FBSOrientationUpdate"8lw40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ _objc_msgSend$_connectionInterrupted:
+ _objc_msgSend$_getAndSetFreshestUpdateGivenUpdate:forced:
+ _objc_msgSend$_lock_getAndSetFreshestUpdateGivenUpdate:forced:
+ _objc_msgSend$_server:registerOrientationInterest:
- -[FBSOrientationObserver _getAndSetFreshestUpdateGivenUpdate:]
- -[FBSOrientationObserver _lock_getAndSetFreshestUpdateGivenUpdate:]
- ___60-[FBSOrientationObserverClient registerOrientationInterest:]_block_invoke
- ___block_descriptor_40_e8_32s_e42_v24?0"FBSOrientationUpdate"8"NSError"16ls32l8
- ___block_descriptor_48_e8_32s40bs_e30_v16?0"FBSOrientationUpdate"8ls32l8s40l8
- _objc_msgSend$_getAndSetFreshestUpdateGivenUpdate:
- _objc_msgSend$_lock_getAndSetFreshestUpdateGivenUpdate:
CStrings:
+ "<%p> Invalidating client."
+ "<%p> Received orientation reset."
+ "<%p> Registering interest for orientation updates."
+ "<%p> Unregistering interest for orientation updates."
+ "<%p> connection activated: %{public}@"
+ "<%p> connection interrupted: %{public}@"
+ "<%p> connection invalidated: %{public}@"
+ "<%p> sending re-registration for orientation interest"
+ "<%p>: Received orientation update: %{public}@ that we're forcefully updating"
+ "_connectionInterrupted:"
+ "_getAndSetFreshestUpdateGivenUpdate:forced:"
+ "_lock_getAndSetFreshestUpdateGivenUpdate:forced:"
+ "_server:registerOrientationInterest:"
+ "v28@0:8@16I24"
- "%p: Invalidating client."
- "<%p>: Registering interest for orientation updates."
- "<%p>: Unregistering interest for orientation updates."
- "_getAndSetFreshestUpdateGivenUpdate:"
- "_lock_getAndSetFreshestUpdateGivenUpdate:"

```
