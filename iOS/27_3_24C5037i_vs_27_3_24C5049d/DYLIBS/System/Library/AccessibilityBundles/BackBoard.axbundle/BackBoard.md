## BackBoard

> `/System/Library/AccessibilityBundles/BackBoard.axbundle/BackBoard`

```diff

-3050.3.12.0.0
-  __TEXT.__text: 0x27cdc
-  __TEXT.__objc_methlist: 0x2364
+3050.3.22.0.0
+  __TEXT.__text: 0x29194
+  __TEXT.__objc_methlist: 0x2474
   __TEXT.__dlopen_cstrs: 0x2d9
-  __TEXT.__const: 0x520
-  __TEXT.__cstring: 0x23da
-  __TEXT.__oslogstring: 0x246d
+  __TEXT.__const: 0x530
+  __TEXT.__cstring: 0x2513
+  __TEXT.__oslogstring: 0x265f
   __TEXT.__constg_swiftt: 0x2e8
   __TEXT.__swift5_typeref: 0x18a
   __TEXT.__swift5_reflstr: 0x115

   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__gcc_except_tab: 0x5b8
-  __TEXT.__unwind_info: 0xff8
+  __TEXT.__gcc_except_tab: 0x638
+  __TEXT.__unwind_info: 0x1060
   __TEXT.__eh_frame: 0x218
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8f8
-  __DATA_CONST.__objc_classlist: 0x158
+  __DATA_CONST.__const: 0x920
+  __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c18
+  __DATA_CONST.__objc_selrefs: 0x1cd0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0xc0
+  __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x80
-  __DATA_CONST.__got: 0x6b0
-  __AUTH_CONST.__const: 0x1000
-  __AUTH_CONST.__cfstring: 0x1e20
-  __AUTH_CONST.__objc_const: 0x30b8
+  __DATA_CONST.__got: 0x6d8
+  __AUTH_CONST.__const: 0x1020
+  __AUTH_CONST.__cfstring: 0x1fa0
+  __AUTH_CONST.__objc_const: 0x32f8
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0xcb0
-  __AUTH.__objc_data: 0x260
-  __DATA.__objc_ivar: 0x160
+  __AUTH_CONST.__auth_got: 0xd10
+  __AUTH.__objc_data: 0x350
+  __DATA.__objc_ivar: 0x170
   __DATA.__data: 0x3c8
   __DATA_DIRTY.__objc_data: 0xde0
   __DATA_DIRTY.__data: 0x138
-  __DATA_DIRTY.__bss: 0x218
+  __DATA_DIRTY.__bss: 0x208
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1039
-  Symbols:   2112
-  CStrings:  508
+  Functions: 1062
+  Symbols:   2174
+  CStrings:  528
 
Symbols:
+ +[AXBKeyboardAttachmentManager canObservePrimaryKeyboardChanges]
+ +[AXBKeyboardAttachmentManager sharedManager]
+ +[BKKeyboardHIDEventProcessorAccessibility _accessibilityPerformValidations:]
+ +[BKKeyboardHIDEventProcessorAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[BKKeyboardHIDEventProcessorAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[AXBEventManager _hitTestOverrideKeyForDisplayId:]
+ -[AXBEventManager hitTestOverrideContextIdForPoint:displayId:]
+ -[AXBEventManager setHitTestOverrideFrame:contextId:displayId:]
+ -[AXBKeyboardAttachmentManager .cxx_destruct]
+ -[AXBKeyboardAttachmentManager _lock_applyAction:trigger:]
+ -[AXBKeyboardAttachmentManager _processDidExit:]
+ -[AXBKeyboardAttachmentManager enableWithInitialStateFromBackBoard]
+ -[AXBKeyboardAttachmentManager init]
+ -[AXBKeyboardAttachmentManager performPrimaryKeyboardChangeToPresent:backBoardUpdate:]
+ -[AXBKeyboardAttachmentManager setReason:active:forPID:]
+ -[AXBackBoardGlue setHitTestOverrideFrame:contextId:displayId:]
+ -[AXBackBoardServerInstance _handleSetHardwareKeyboardAttachmentReason:]
+ -[AXBackBoardServerInstance _handleSetHitTestOverrideRegion:]
+ -[BKKeyboardHIDEventProcessorAccessibility _lock_setPrimaryKeyboard:]
+ GCC_except_table244
+ GCC_except_table263
+ GCC_except_table306
+ GCC_except_table351
+ GCC_except_table353
+ GCC_except_table403
+ GCC_except_table408
+ GCC_except_table424
+ GCC_except_table432
+ GCC_except_table468
+ GCC_except_table486
+ GCC_except_table537
+ GCC_except_table583
+ GCC_except_table612
+ GCC_except_table632
+ GCC_except_table645
+ GCC_except_table657
+ GCC_except_table671
+ GCC_except_table674
+ GCC_except_table707
+ GCC_except_table745
+ GCC_except_table759
+ GCC_except_table835
+ _AXBShiftLeftEdgeEnabled.onceToken
+ _AXHardwareKeyboardAttachmentReasonDescription
+ _AXHardwareKeyboardAttachmentReasonsResetNotification
+ _CGRectContainsPoint
+ _CGRectIsEmpty
+ _CGRectIsNull
+ _GSEventIsHardwareKeyboardAttached
+ _GSEventSetHardwareKeyboardAttached
+ _OBJC_CLASS_$_AXBKeyboardAttachmentManager
+ _OBJC_CLASS_$_AXHardwareKeyboardAttachmentState
+ _OBJC_CLASS_$_BKKeyboardHIDEventProcessorAccessibility
+ _OBJC_CLASS_$_BSAuditToken
+ _OBJC_CLASS_$___BKKeyboardHIDEventProcessorAccessibility_super
+ _OBJC_IVAR_$_AXBKeyboardAttachmentManager._deathWatchersByPID
+ _OBJC_IVAR_$_AXBKeyboardAttachmentManager._enabled
+ _OBJC_IVAR_$_AXBKeyboardAttachmentManager._lock
+ _OBJC_IVAR_$_AXBKeyboardAttachmentManager._state
+ _OBJC_METACLASS_$_AXBKeyboardAttachmentManager
+ _OBJC_METACLASS_$_BKKeyboardHIDEventProcessorAccessibility
+ _OBJC_METACLASS_$___BKKeyboardHIDEventProcessorAccessibility_super
+ __AXHitTestOverrides
+ __AXHitTestOverridesLock
+ __OBJC_$_CLASS_METHODS_AXBKeyboardAttachmentManager
+ __OBJC_$_CLASS_METHODS_BKKeyboardHIDEventProcessorAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_AXBKeyboardAttachmentManager
+ __OBJC_$_INSTANCE_METHODS_BKKeyboardHIDEventProcessorAccessibility
+ __OBJC_$_INSTANCE_VARIABLES_AXBKeyboardAttachmentManager
+ __OBJC_CLASS_RO_$_AXBKeyboardAttachmentManager
+ __OBJC_CLASS_RO_$_BKKeyboardHIDEventProcessorAccessibility
+ __OBJC_CLASS_RO_$___BKKeyboardHIDEventProcessorAccessibility_super
+ __OBJC_METACLASS_RO_$_AXBKeyboardAttachmentManager
+ __OBJC_METACLASS_RO_$_BKKeyboardHIDEventProcessorAccessibility
+ __OBJC_METACLASS_RO_$___BKKeyboardHIDEventProcessorAccessibility_super
+ ___45+[AXBKeyboardAttachmentManager sharedManager]_block_invoke
+ ___56-[AXBKeyboardAttachmentManager setReason:active:forPID:]_block_invoke
+ ___67-[AXBKeyboardAttachmentManager enableWithInitialStateFromBackBoard]_block_invoke
+ ___69-[BKKeyboardHIDEventProcessorAccessibility _lock_setPrimaryKeyboard:]_block_invoke
+ ___AXBShiftLeftEdgeEnabled_block_invoke
+ ___AXBShiftLeftEdgeEnabled_block_invoke_2
+ ___block_descriptor_44_e8_32w_e5_v8?0lw32l8
+ _notify_post
+ _os_unfair_lock_assert_owner
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _sAXBShiftLeftEdgeEnabled
- GCC_except_table241
- GCC_except_table260
- GCC_except_table303
- GCC_except_table347
- GCC_except_table349
- GCC_except_table399
- GCC_except_table404
- GCC_except_table420
- GCC_except_table428
- GCC_except_table464
- GCC_except_table482
- GCC_except_table533
- GCC_except_table579
- GCC_except_table608
- GCC_except_table628
- GCC_except_table641
- GCC_except_table653
- GCC_except_table686
- GCC_except_table724
- GCC_except_table738
- GCC_except_table812
- _AXBCaseAccommodationsEnabled.onceToken
- ___AXBCaseAccommodationsEnabled_block_invoke
- ___AXBCaseAccommodationsEnabled_block_invoke_2
- _sAXBCaseAccommodationsEnabled
CStrings:
+ "#"
+ "AXKEYBOARD: %{public}@ -> no write needed [%{public}@]"
+ "AXKEYBOARD: %{public}@ -> writing hardware keyboard attached=%d [%{public}@]"
+ "AXKEYBOARD: asking clients to resend reasons"
+ "AXKEYBOARD: backboardd primary keyboard changes can't be observed; accessibility keyboard reasons are disabled"
+ "AXKEYBOARD: enabled, backboardd reports real keyboard present=%d [%{public}@]"
+ "AXKEYBOARD: ignoring %{public}@ because primary keyboard changes can't be observed"
+ "AXKEYBOARD: malformed reason message: %{public}@"
+ "BKHIDEventProcessorRegistry"
+ "BKKeyboardHIDEventProcessor"
+ "BKKeyboardHIDEventProcessorAccessibility"
+ "_lock_setPrimaryKeyboard:"
+ "active"
+ "allUsableDeviceProperties"
+ "backboardd primary keyboard present %d->%d"
+ "eventProcessorOfClass:"
+ "pid %d exited"
+ "reason"
+ "reason %@ active=%d from pid %d"
+ "reconciling with system attached=%d"
```
