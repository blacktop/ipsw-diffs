## UIFoundation

> `/System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation`

```diff

-1056.0.0.0.0
-  __TEXT.__text: 0x1059b4
-  __TEXT.__objc_methlist: 0xbb9c
-  __TEXT.__const: 0x78c
-  __TEXT.__gcc_except_tab: 0x3540
-  __TEXT.__cstring: 0x102c3
-  __TEXT.__ustring: 0x2b4
-  __TEXT.__oslogstring: 0xb
+1057.1.0.0.0
+  __TEXT.__text: 0x106e00
+  __TEXT.__objc_methlist: 0xbbbc
+  __TEXT.__const: 0x8bc
+  __TEXT.__gcc_except_tab: 0x35b4
+  __TEXT.__cstring: 0x10269
+  __TEXT.__ustring: 0x3c8
+  __TEXT.__oslogstring: 0x53a
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__dof_UIFoundat: 0x2bd
-  __TEXT.__unwind_info: 0x4bc8
+  __TEXT.__unwind_info: 0x4c00
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9240
-  __DATA_CONST.__objc_classlist: 0x480
+  __DATA_CONST.__const: 0x9268
+  __DATA_CONST.__objc_classlist: 0x488
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68f0
+  __DATA_CONST.__objc_selrefs: 0x6900
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x420
+  __DATA_CONST.__objc_superrefs: 0x428
   __DATA_CONST.__objc_arraydata: 0xa8
   __DATA_CONST.__got: 0x8c0
-  __AUTH_CONST.__const: 0x12d8
-  __AUTH_CONST.__cfstring: 0xcae0
-  __AUTH_CONST.__objc_const: 0x12b20
+  __AUTH_CONST.__const: 0x1318
+  __AUTH_CONST.__cfstring: 0xcb60
+  __AUTH_CONST.__objc_const: 0x12bd8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x12e8
-  __AUTH.__objc_data: 0x12c0
+  __AUTH_CONST.__auth_got: 0x1308
+  __AUTH.__objc_data: 0x1310
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x131c
+  __AUTH.__thread_vars: 0x18
+  __AUTH.__thread_bss: 0x1
+  __DATA.__objc_ivar: 0x1320
   __DATA.__data: 0xe21
+  __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0x1a40
   __DATA_DIRTY.__data: 0x81
   __DATA_DIRTY.__bss: 0x9c0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5352
-  Symbols:   11989
-  CStrings:  3220
+  Functions: 5367
+  Symbols:   12023
+  CStrings:  3248
 
Symbols:
+ -[UIFoundationInstrumentationEventObservation _initWithToken:]
+ -[UIFoundationInstrumentationEventObservation dealloc]
+ _OBJC_CLASS_$_UIFoundationInstrumentationEventObservation
+ _OBJC_IVAR_$_UIFoundationInstrumentationEventObservation._token
+ _OBJC_METACLASS_$_UIFoundationInstrumentationEventObservation
+ __OBJC_$_INSTANCE_METHODS_UIFoundationInstrumentationEventObservation
+ __OBJC_$_INSTANCE_VARIABLES_UIFoundationInstrumentationEventObservation
+ __OBJC_CLASS_RO_$_UIFoundationInstrumentationEventObservation
+ __OBJC_METACLASS_RO_$_UIFoundationInstrumentationEventObservation
+ ___UIFoundationCreateAllLogObjects.once
+ ___UIFoundationDynamicLogCache
+ ___UIFoundationDynamicLogCacheLock
+ ___UIFoundationInstrumentationEventAnySinkActiveFlag
+ ___UIFoundationInstrumentationEventEmit
+ ___UIFoundationInstrumentationEventEmit.inEmit
+ ___UIFoundationInstrumentationEventEmit.inEmit$tlv$init
+ ___UIFoundationInstrumentationEventEnsureInit
+ ___UIFoundationInstrumentationEventEnsureInit.once
+ ___UIFoundationInstrumentationEventObservers
+ ___UIFoundationInstrumentationEventRemoveObserver
+ ___UIFoundationInstrumentationEventSequence
+ ___UIFoundationLogGeneral
+ ___UIFoundationLogScrolling
+ ___UIFoundationLogStringDrawing
+ ___UIFoundationSignpostSinkEnabled
+ ___UIFoundationWriteLogDynamic
+ _____UIFoundationCreateAllLogObjects_block_invoke
+ _____UIFoundationInstrumentationEventEnsureInit_block_invoke
+ ___block_descriptor_66_e8_32r40r_e50_v32?0"NSTextLayoutFragment"8"NSTextRange"16^B24lr32l8r40l8
+ ___block_descriptor_73_e8_32o40r48r56r64r_e30_B16?0"NSTextLayoutFragment"8lr40l8s32l8r48l8r56l8r64l8
+ __os_signpost_emit_with_name_impl
+ __tlv_bootstrap
+ _log_General
+ _log_Scrolling
+ _log_StringDrawing
+ _mach_absolute_time
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _os_signpost_enabled
+ _os_signpost_id_make_with_pointer
- ___UIFoundationWriteLog
- ___UIFoundationWriteLog.onceToken
- ___UIFoundationWriteLog.uifoundationLog
- _____UIFoundationWriteLog_block_invoke
- ___block_descriptor_57_e8_32r_e50_v32?0"NSTextLayoutFragment"8"NSTextRange"16^B24lr32l8
CStrings:
+ "ContentHeightEstimate"
+ "EnableScrollingSignposts"
+ "FragmentCreate"
+ "FragmentEstimate"
+ "FragmentHeightResolved"
+ "FragmentInvalidate"
+ "FragmentLayout"
+ "PositionMapping"
+ "ScrollAnchor"
+ "Scrolling"
+ "UIFoundationInstrumentationEvent observer re-entered the emit funnel — observers must not trigger layout/emit; marshal to your own queue."
+ "UIFoundationLogging.m"
+ "ViewportLayout"
+ "ViewportOffsetDelta"
+ "ViewportRestore"
+ "bounds={%{public}f,%{public}f,%{public}f,%{public}f} offset={%{public}f,%{public}f}"
+ "entryState=%{public}u viewportController=%{public}#llx"
+ "estimatedHeight=%{public}f actualHeight=%{public}f heightDelta=%{public}f"
+ "estimatedHeight=%{public}f frameY=%{public}f"
+ "estimatedHeight=%{public}f realHeight=%{public}f elementCount=%{public}llu lastFragmentEstimated=%{public}u"
+ "frameY=%{public}f frameHeight=%{public}f viewportController=%{public}#llx"
+ "path=%{public}u anchorLayoutY=%{public}f anchorLocationOffset=%{public}lld"
+ "positionY=%{public}f skippedStateNoneCount=%{public}llu resolvedFrameY=%{public}f resolvedState=%{public}u"
+ "priorState=%{public}u discardedHeight=%{public}f"
+ "reason=%{public}u preOriginY=%{public}f postOriginY=%{public}f verticalDelta=%{public}f"
+ "viewportController=%{public}#llx"
+ "viewportOrigin={%{public}f,%{public}f} layoutRectOrigin={%{public}f,%{public}f} delta={%{public}f,%{public}f}"
+ "void __UIFoundationInstrumentationEventEmit(const UIFoundationInstrumentationEvent *)"
```
