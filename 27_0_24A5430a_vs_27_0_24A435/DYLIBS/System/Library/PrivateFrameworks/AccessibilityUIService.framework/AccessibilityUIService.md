## AccessibilityUIService

> `/System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService`

```diff

 3240.9.0.0.0
-  __TEXT.__text: 0x1f61c
-  __TEXT.__objc_methlist: 0x1c14
-  __TEXT.__const: 0x858
+  __TEXT.__text: 0x1fc60
+  __TEXT.__objc_methlist: 0x1c64
+  __TEXT.__const: 0x868
   __TEXT.__constg_swiftt: 0x184
   __TEXT.__swift5_typeref: 0x1d7
   __TEXT.__swift5_fieldmd: 0x120
-  __TEXT.__cstring: 0x152e
+  __TEXT.__cstring: 0x1561
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_capture: 0x44
-  __TEXT.__oslogstring: 0x16eb
+  __TEXT.__oslogstring: 0x1784
   __TEXT.__swift5_reflstr: 0xb5
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x48
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x20
-  __TEXT.__gcc_except_tab: 0x488
-  __TEXT.__unwind_info: 0x8a0
+  __TEXT.__gcc_except_tab: 0x4b0
+  __TEXT.__unwind_info: 0x8c8
   __TEXT.__eh_frame: 0x408
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8f8
+  __DATA_CONST.__const: 0x920
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1870
+  __DATA_CONST.__objc_selrefs: 0x18d8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x508
+  __DATA_CONST.__got: 0x510
   __AUTH_CONST.__const: 0x4b0
   __AUTH_CONST.__cfstring: 0xaa0
-  __AUTH_CONST.__objc_const: 0x27f0
+  __AUTH_CONST.__objc_const: 0x2880
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x888
+  __AUTH_CONST.__auth_got: 0x890
   __AUTH.__objc_data: 0x260
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x18c
+  __DATA.__objc_ivar: 0x19c
   __DATA.__data: 0x690
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x640

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 740
-  Symbols:   2135
-  CStrings:  220
+  Functions: 749
+  Symbols:   2163
+  CStrings:  222
 
Symbols:
+ -[AXUIDisplayManager _activateActiveDisplayObserverIfNeeded]
+ -[AXUIDisplayManager _handleActiveInterfaceOrientationState:]
+ -[AXUIDisplayManager activeDisplayID]
+ -[AXUIDisplayManager addActiveDisplayObserver:]
+ -[AXUIDisplayManager removeActiveDisplayObserver:]
+ -[AXUIDisplayManager setActiveDisplayID:]
+ -[AXUIDisplayManager shouldPresentUIForWindowScene:]
+ GCC_except_table328
+ GCC_except_table329
+ GCC_except_table338
+ GCC_except_table339
+ GCC_except_table357
+ GCC_except_table358
+ GCC_except_table365
+ GCC_except_table373
+ GCC_except_table378
+ GCC_except_table394
+ GCC_except_table426
+ GCC_except_table428
+ GCC_except_table445
+ _AXDeviceIsViridian
+ _OBJC_CLASS_$_FBSActiveInterfaceOrientationObserver
+ _OBJC_IVAR_$_AXUIDisplayManager._activeDisplayID
+ _OBJC_IVAR_$_AXUIDisplayManager._activeDisplayObservers
+ _OBJC_IVAR_$_AXUIDisplayManager._activeInterfaceOrientationObserver
+ _OBJC_IVAR_$_AXUIDisplayManager._hasResolvedActiveDisplay
+ ___60-[AXUIDisplayManager _activateActiveDisplayObserverIfNeeded]_block_invoke
+ ___60-[AXUIDisplayManager _activateActiveDisplayObserverIfNeeded]_block_invoke_2
+ ___block_descriptor_40_e8_32w_e50_v16?0"FBSActiveInterfaceOrientationStateUpdate"8lw32l8
+ _objc_msgSend$_activateActiveDisplayObserverIfNeeded
+ _objc_msgSend$_handleActiveInterfaceOrientationState:
+ _objc_msgSend$activateWithStateUpdateHandler:
+ _objc_msgSend$activeDisplayDidChangeToDisplayID:
+ _objc_msgSend$activeDisplayID
+ _objc_msgSend$activeInterfaceOrientationState
+ _objc_msgSend$displayID
+ _objc_msgSend$displayIdentity
+ _objc_msgSend$isExternal
+ _objc_msgSend$setActiveDisplayID:
- GCC_except_table326
- GCC_except_table327
- GCC_except_table348
- GCC_except_table349
- GCC_except_table356
- GCC_except_table364
- GCC_except_table369
- GCC_except_table385
- GCC_except_table417
- GCC_except_table419
- GCC_except_table436
CStrings:
+ "[ActiveDisplay] Active display changed to displayID=%u; notifying %lu observer(s)."
+ "[ActiveDisplay] FBS delivered displayID=%u (current=%u, resolved=%d)."
+ "v16@?0@\"FBSActiveInterfaceOrientationStateUpdate\"8"
- "\x81"
```
