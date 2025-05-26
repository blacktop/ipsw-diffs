## CarPlayUIServices

> `/System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices`

```diff

-309.5.3.1.0
-  __TEXT.__text: 0x9d20
-  __TEXT.__auth_stubs: 0x420
-  __TEXT.__objc_methlist: 0xf1c
+309.5.4.1.0
+  __TEXT.__text: 0xa018
+  __TEXT.__auth_stubs: 0x430
+  __TEXT.__objc_methlist: 0xf54
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0xa00
   __TEXT.__gcc_except_tab: 0x104
-  __TEXT.__oslogstring: 0x3b0
-  __TEXT.__unwind_info: 0x304
+  __TEXT.__oslogstring: 0x425
+  __TEXT.__unwind_info: 0x308
   __TEXT.__objc_classname: 0x81c
-  __TEXT.__objc_methname: 0x2add
-  __TEXT.__objc_methtype: 0x8a8
-  __TEXT.__objc_stubs: 0x20a0
+  __TEXT.__objc_methname: 0x2b83
+  __TEXT.__objc_methtype: 0x8e1
+  __TEXT.__objc_stubs: 0x2100
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x498
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5468
-  __DATA_CONST.__objc_selrefs: 0xab8
+  __DATA_CONST.__objc_const: 0x54c8
+  __DATA_CONST.__objc_selrefs: 0xae0
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__objc_const: 0xdf0
   __AUTH_CONST.__cfstring: 0x8c0
-  __AUTH_CONST.__auth_got: 0x220
+  __AUTH_CONST.__auth_got: 0x228
   __AUTH.__objc_data: 0xd20
   __DATA.__objc_protorefs: 0x40
   __DATA.__objc_classrefs: 0x1f8
   __DATA.__objc_superrefs: 0x78
-  __DATA.__objc_ivar: 0xb4
+  __DATA.__objc_ivar: 0xbc
   __DATA.__data: 0x908
   __DATA.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 350
-  Symbols:   1736
-  CStrings:  738
+  Functions: 355
+  Symbols:   1752
+  CStrings:  752
 
Symbols:
+ -[CRSUIDashboardWidgetWindow _lock_invalidateConnection]
+ -[CRSUIDashboardWidgetWindow _lock_invalidateCurrentFocusableItems]
+ -[CRSUIDashboardWidgetWindow isInvalidated]
+ -[CRSUIDashboardWidgetWindow lock]
+ -[CRSUIDashboardWidgetWindow setInvalidated:]
+ -[CRSUIDashboardWidgetWindow setLock:]
+ _OBJC_IVAR_$_CRSUIDashboardWidgetWindow._invalidated
+ _OBJC_IVAR_$_CRSUIDashboardWidgetWindow._lock
+ ___67-[CRSUIDashboardWidgetWindow _lock_invalidateCurrentFocusableItems]_block_invoke
+ _dispatch_assert_queue$V2
+ _objc_msgSend$_lock_invalidateConnection
+ _objc_msgSend$_lock_invalidateCurrentFocusableItems
+ _objc_msgSend$isInvalidated
+ _objc_msgSend$setInvalidated:
- -[CRSUIDashboardWidgetWindow _invalidateCurrentFocusableItems]
- ___62-[CRSUIDashboardWidgetWindow _invalidateCurrentFocusableItems]_block_invoke
- _objc_msgSend$_invalidateCurrentFocusableItems
CStrings:
+ "Invalidating window: %{public}@"
+ "TB,N,GisInvalidated,V_invalidated"
+ "T{os_unfair_lock_s=I},N,V_lock"
+ "Window: %{public}@ already invalidated"
+ "Window: %{public}@ not invalidated in dealloc"
+ "_invalidated"
+ "_lock_invalidateConnection"
+ "_lock_invalidateCurrentFocusableItems"
+ "invalidated"
+ "isInvalidated"
+ "lock"
+ "setInvalidated:"
+ "setLock:"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "{os_unfair_lock_s=I}16@0:8"
- "_invalidateCurrentFocusableItems"

```
