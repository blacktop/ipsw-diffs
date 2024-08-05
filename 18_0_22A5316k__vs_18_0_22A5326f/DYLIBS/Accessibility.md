## Accessibility

> `/System/Library/Frameworks/Accessibility.framework/Accessibility`

```diff

-493.0.0.0.0
-  __TEXT.__text: 0x12490
-  __TEXT.__auth_stubs: 0xa40
+495.0.0.0.0
+  __TEXT.__text: 0x12b28
+  __TEXT.__auth_stubs: 0xa90
   __TEXT.__objc_methlist: 0xaac
   __TEXT.__const: 0x1170
-  __TEXT.__gcc_except_tab: 0x2e0
-  __TEXT.__cstring: 0xdb2
-  __TEXT.__dlopen_cstrs: 0x1d5
+  __TEXT.__gcc_except_tab: 0x2f4
+  __TEXT.__cstring: 0xdf2
+  __TEXT.__dlopen_cstrs: 0x218
   __TEXT.__oslogstring: 0x108
-  __TEXT.__swift5_typeref: 0x38a
+  __TEXT.__swift5_typeref: 0x381
   __TEXT.__constg_swiftt: 0x28c
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8

   __TEXT.__swift5_proto: 0x100
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x7f0
-  __TEXT.__eh_frame: 0x5a0
+  __TEXT.__unwind_info: 0x838
+  __TEXT.__eh_frame: 0x588
   __TEXT.__objc_classname: 0x19b
-  __TEXT.__objc_methname: 0x1ac2
+  __TEXT.__objc_methname: 0x1b4b
   __TEXT.__objc_methtype: 0x4cb
-  __TEXT.__objc_stubs: 0x11c0
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x390
+  __TEXT.__objc_stubs: 0x12a0
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__const: 0x3f0
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d8
+  __DATA_CONST.__objc_selrefs: 0x710
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x530
-  __AUTH_CONST.__auth_ptr: 0x1a8
+  __AUTH_CONST.__auth_got: 0x558
+  __AUTH_CONST.__auth_ptr: 0x1b0
   __AUTH_CONST.__const: 0x910
-  __AUTH_CONST.__cfstring: 0x940
+  __AUTH_CONST.__cfstring: 0x980
   __AUTH_CONST.__objc_const: 0x1af0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0xd8
-  __DATA.__data: 0x3a0
-  __DATA.__bss: 0x14f0
+  __DATA.__data: 0x398
+  __DATA.__bss: 0x1510
+  __DATA.__common: 0x19
   __DATA_DIRTY.__objc_data: 0x460
-  __DATA_DIRTY.__data: 0x178
+  __DATA_DIRTY.__data: 0x168
   __DATA_DIRTY.__bss: 0xac8
   __DATA_DIRTY.__common: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 731
-  Symbols:   563
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 748
+  Symbols:   600
   CStrings:  0
 
Symbols:
+ _AXTextContentSizeCategoryDidChangeNotification
+ _AXTextGetAppUsesCustomContentSize
+ _AXTextPreferredFontForTextStyle
+ _AXTextPreferredUserFontSizeForSize
+ _AXTextSetAppUsesCustomContentSize
+ _AXTextSetContentSizeCategoryOverrideForPreviews
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterGetDistributedCenter
+ _CFNotificationCenterPostNotification
+ _CFStringCompare
+ _CTFontDescriptorCopyAttribute
+ _CTFontDescriptorCreateWithTextStyleAndAttributes
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_NSUserDefaults
+ __AXSCopyPreferredContentSizeCategoryName
+ __BeginObservingPreferredContentSizeChangedNotification
+ __PreferredContentSizeCategory
+ __PreferredContentSizeChangedCallback
+ __RefreshContentSizePreferences
+ ___NSDictionary0__struct
+ __cachedPreferredContentSizeCategory
+ __cachedUsesCustomContentSize
+ __contentSizeCategoryOverrideForPreviews
+ __contentSizeCategoryToUse
+ __observingNotification
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _kAXSApplePreferredContentSizeCategoryNotification
+ _kCTFontSizeAttribute
+ _kCTUIFontTextStyleBody
- _swift_continuation_await
- _swift_continuation_init
- _swift_willThrow

```
