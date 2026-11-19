## DockHelper

> `/System/Library/CoreServices/Dock.app/Contents/XPCServices/DockHelper.xpc/Contents/MacOS/DockHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`

```diff

-2571.0.6.402.0
-  __TEXT.__text: 0x9acc
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_stubs: 0x7c0
-  __TEXT.__objc_methlist: 0x310
-  __TEXT.__const: 0x1168
+2571.1.32.402.0
+  __TEXT.__text: 0xbe04
+  __TEXT.__auth_stubs: 0x850
+  __TEXT.__objc_stubs: 0x940
+  __TEXT.__objc_methlist: 0x390
+  __TEXT.__const: 0x14d8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x460
-  __TEXT.__swift5_typeref: 0x431
-  __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x199
-  __TEXT.__swift5_fieldmd: 0x40c
-  __TEXT.__swift5_assocty: 0x120
-  __TEXT.__swift5_proto: 0xe4
-  __TEXT.__swift5_types: 0x5c
-  __TEXT.__objc_classname: 0x207
-  __TEXT.__objc_methname: 0xa32
-  __TEXT.__objc_methtype: 0x432
+  __TEXT.__constg_swiftt: 0x584
+  __TEXT.__swift5_typeref: 0x4ea
+  __TEXT.__swift5_builtin: 0xc8
+  __TEXT.__swift5_reflstr: 0x250
+  __TEXT.__swift5_fieldmd: 0x548
+  __TEXT.__swift5_assocty: 0x168
+  __TEXT.__swift5_proto: 0x110
+  __TEXT.__swift5_types: 0x78
+  __TEXT.__objc_classname: 0x2a7
+  __TEXT.__objc_methname: 0xc49
+  __TEXT.__objc_methtype: 0x50d
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__cstring: 0xe1
-  __TEXT.__swift5_capture: 0x60
+  __TEXT.__cstring: 0x171
+  __TEXT.__swift5_capture: 0xe4
+  __TEXT.__oslogstring: 0xa6
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x6b8
-  __TEXT.__eh_frame: 0x480
-  __DATA_CONST.__const: 0x820
-  __DATA_CONST.__objc_classlist: 0x40
+  __TEXT.__unwind_info: 0x7c0
+  __TEXT.__eh_frame: 0x508
+  __DATA_CONST.__const: 0xb98
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__auth_got: 0x338
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__auth_ptr: 0x280
-  __DATA.__objc_const: 0x8b0
-  __DATA.__objc_selrefs: 0x340
-  __DATA.__objc_data: 0x328
-  __DATA.__data: 0x7c0
-  __DATA.__common: 0x30
-  __DATA.__bss: 0x1c00
+  __DATA_CONST.__auth_got: 0x430
+  __DATA_CONST.__got: 0x170
+  __DATA_CONST.__auth_ptr: 0x2a0
+  __DATA.__objc_const: 0xa60
+  __DATA.__objc_selrefs: 0x3a0
+  __DATA.__objc_data: 0x4c0
+  __DATA.__data: 0x8d8
+  __DATA.__common: 0x58
+  __DATA.__bss: 0x2180
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Carbon.framework/Versions/A/Carbon
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 592
-  Symbols:   106
-  CStrings:  187
+  Functions: 702
+  Symbols:   133
+  CStrings:  216
 
Symbols:
+ _CFRunLoopGetMain
+ _CFRunLoopWakeUp
+ _CGRectEqualToRect
+ _CGRectGetHeight
+ _CGRectGetMaxY
+ _CGRectGetMinX
+ _CGRectGetWidth
+ _CGRectNull
+ _CGRectUnion
+ _NSApp
+ _NSClassFromString
+ _NSDefaultRunLoopMode
+ _NSRunLoopCommonModes
+ _NSWindowDidMoveNotification
+ _NSWindowDidResizeNotification
+ _NSWindowWillCloseNotification
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSWindow
+ __os_log_impl
+ _os_log_type_enabled
+ _swift_getObjectType
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
CStrings:
+ "DockHelper.MenuGeometryReporter"
+ "DockHelper.MenuWindowReporter"
+ "NSPopupMenuWindow"
+ "Touch detach: no Dock connection to report the menu window context to"
+ "Touch detach: presented menu window has no context; touch can't continue into it"
+ "_TtC10DockHelperP33_C36F5F5A633AC0FE48B6819A4FF37BBF18MenuWindowReporter"
+ "_TtC10DockHelperP33_C36F5F5A633AC0FE48B6819A4FF37BBF20MenuGeometryReporter"
+ "_popUpMenuRelativeToRect:inView:preferredEdge:flags:options:"
+ "_setControllerDelegate:"
+ "_setScreenTimeIndicator:"
+ "addObserverForName:object:queue:usingBlock:"
+ "defaultCenter"
+ "frame"
+ "geometryReporter"
+ "isInvalidated"
+ "isVisible"
+ "itemArray"
+ "lastReport"
+ "menu:didDisplayWindow:contextID:"
+ "menuBoundsDidChange:"
+ "menuDidPresentWithContextIDs:"
+ "popupWithMenu:direction:rect:dark:orientation:fromKeyboard:touchInitiated:accessibilityContainer:withReply:"
+ "removeObserver:"
+ "reportIsScheduled"
+ "screenTimeRestriction"
+ "submenu"
+ "v16@?0@\"NSNotification\"8"
+ "v24@0:8@\"NSArray\"16"
+ "v36@0:8@16@24I32"
+ "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "v84@0:8@\"NSData\"16q24{FloatRect=ffff}32B48q52B60B64@\"NSData\"68@?<v@?@\"NSData\">76"
+ "v84@0:8@16q24{FloatRect=ffff}32B48q52B60B64@68@?76"
+ "windowObservers"
+ "windows"
- "_popUpMenuRelativeToRect:inView:preferredEdge:"
- "_setShowsBlockedByScreenTime:"
- "popupWithMenu:direction:rect:dark:orientation:fromKeyboard:accessibilityContainer:withReply:"
- "v80@0:8@\"NSData\"16q24{FloatRect=ffff}32B48q52B60@\"NSData\"64@?<v@?@\"NSData\">72"
- "v80@0:8@16q24{FloatRect=ffff}32B48q52B60@64@?72"
```
