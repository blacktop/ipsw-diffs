## PrivacyAccounting

> `/System/Library/PrivateFrameworks/PrivacyAccounting.framework/PrivacyAccounting`

```diff

-150.0.0.0.0
-  __TEXT.__text: 0x1c7d0
-  __TEXT.__objc_methlist: 0x2114
-  __TEXT.__const: 0x6b0
-  __TEXT.__cstring: 0x113c
-  __TEXT.__oslogstring: 0xa3f
-  __TEXT.__gcc_except_tab: 0x574
+150.0.1.0.0
+  __TEXT.__text: 0x1cb5c
+  __TEXT.__objc_methlist: 0x212c
+  __TEXT.__const: 0x6c0
+  __TEXT.__cstring: 0x116c
+  __TEXT.__oslogstring: 0xb4f
+  __TEXT.__gcc_except_tab: 0x590
   __TEXT.__constg_swiftt: 0x26c
   __TEXT.__swift5_typeref: 0x213
   __TEXT.__swift5_fieldmd: 0x14c

   __TEXT.__swift5_types: 0x28
   __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xce8
+  __TEXT.__unwind_info: 0xd08
   __TEXT.__eh_frame: 0x1f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe10
+  __DATA_CONST.__objc_selrefs: 0xe20
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__got: 0x330

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 884
-  Symbols:   1747
-  CStrings:  210
+  Functions: 888
+  Symbols:   1751
+  CStrings:  215
 
Symbols:
+ -[PAAccessLogger refreshLoggingOptions]
+ -[PAAccessLogger startObservingEligibilityChanges]
+ GCC_except_table23
+ GCC_except_table31
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table46
+ GCC_except_table57
+ _OBJC_IVAR_$_PAAccessLogger._eligibilityChangedNotificationToken
+ ___50-[PAAccessLogger startObservingEligibilityChanges]_block_invoke
- GCC_except_table20
- GCC_except_table25
- GCC_except_table27
- GCC_except_table42
- GCC_except_table54
- _OBJC_IVAR_$_PACoalescingIntervalTracker._loggingOptions
CStrings:
+ "Eligibility changed; contacts access counts within minute: %{bool}d -> %{bool}d"
+ "Failed to register for eligibility changed notifications with code=%u"
+ "Received eligibility changed notification with token=%d"
+ "Registered for eligibility changed notifications with token=%d"
+ "com.apple.os-eligibility-domain.change.oganesson"
```
