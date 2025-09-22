## AccessibilityAudit

> `/System/Library/PrivateFrameworks/AccessibilityAudit.framework/AccessibilityAudit`

```diff

-186.0.0.0.0
-  __TEXT.__text: 0x225bc
-  __TEXT.__auth_stubs: 0x8f0
-  __TEXT.__objc_methlist: 0x347c
-  __TEXT.__const: 0x218
-  __TEXT.__cstring: 0x3809
+187.2.0.0.0
+  __TEXT.__text: 0x229e4
+  __TEXT.__auth_stubs: 0x920
+  __TEXT.__objc_methlist: 0x3494
+  __TEXT.__const: 0x220
+  __TEXT.__cstring: 0x3826
   __TEXT.__gcc_except_tab: 0x120
-  __TEXT.__oslogstring: 0x4d9
+  __TEXT.__oslogstring: 0x5c2
   __TEXT.__unwind_info: 0xa50
   __TEXT.__objc_classname: 0x628
   __TEXT.__objc_methname: 0x7a22

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x388
-  __AUTH_CONST.__auth_got: 0x488
+  __AUTH_CONST.__auth_got: 0x4a0
   __AUTH_CONST.__const: 0x1200
   __AUTH_CONST.__cfstring: 0x3760
   __AUTH_CONST.__objc_const: 0x56b8

   __AUTH.__objc_data: 0x1090
   __DATA.__objc_ivar: 0x35c
   __DATA.__data: 0x608
-  __DATA.__bss: 0x168
+  __DATA.__bss: 0x188
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 945427C4-AD48-3E8F-B9F4-6990AEF37B5B
-  Functions: 1194
-  Symbols:   4356
-  CStrings:  2647
+  UUID: 4F9E3DA5-2B11-3468-AA45-A8CB9B440E28
+  Functions: 1195
+  Symbols:   4366
+  CStrings:  2657
 
Symbols:
+ +[AXAuditCategory initialize]
+ __OBJC_$_CLASS_METHODS_AXAuditCategory
+ __os_signpost_emit_with_name_impl
+ _category_spid
+ _log_category_signpost
+ _log_signpost
+ _os_signpost_enabled
+ _os_signpost_id_generate
+ _spid
Functions:
~ +[AXAuditer initialize] : 20 -> 100
~ -[AXAuditer startWithAuditTypes:] : 732 -> 836
~ -[AXAuditer _runCategories:] : 348 -> 540
~ -[AXAuditer didCompleteCategory:] : 308 -> 604
+ +[AXAuditCategory initialize]
~ -[AXAuditCategory caseStartedForSelectorName:] : 328 -> 488
~ -[AXAuditCategory caseEndedForSelectorName:result:] : 296 -> 448
CStrings:
+ "AXAuditRun"
+ "Completed accessibility audit"
+ "Completed audit category: %{public}@"
+ "Completed test case: %{public}@"
+ "Running audit category: %{public}@"
+ "Starting accessibility audit"
+ "Starting test case: %{public}@"
+ "com.apple.AccessibilityAudit"

```
