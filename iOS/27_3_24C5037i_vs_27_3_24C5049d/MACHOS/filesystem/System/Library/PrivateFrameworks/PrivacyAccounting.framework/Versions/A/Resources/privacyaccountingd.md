## privacyaccountingd

> `/System/Library/PrivateFrameworks/PrivacyAccounting.framework/Versions/A/Resources/privacyaccountingd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-150.0.0.0.0
-  __TEXT.__text: 0xc258
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_stubs: 0x22c0
-  __TEXT.__objc_methlist: 0xc0c
-  __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0x324
-  __TEXT.__cstring: 0xfcf
-  __TEXT.__oslogstring: 0x1176
-  __TEXT.__objc_methname: 0x2c64
+150.0.1.0.0
+  __TEXT.__text: 0xc654
+  __TEXT.__auth_stubs: 0x860
+  __TEXT.__objc_stubs: 0x2320
+  __TEXT.__objc_methlist: 0xc3c
+  __TEXT.__const: 0xf8
+  __TEXT.__gcc_except_tab: 0x338
+  __TEXT.__cstring: 0x1008
+  __TEXT.__oslogstring: 0x12b4
+  __TEXT.__objc_methname: 0x2cd4
   __TEXT.__objc_classname: 0x1e1
   __TEXT.__objc_methtype: 0x852
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x530
+  __TEXT.__unwind_info: 0x550
   __DATA_CONST.__const: 0x698
   __DATA_CONST.__cfstring: 0xa20
   __DATA_CONST.__objc_classlist: 0x60

   __DATA_CONST.__objc_arraydata: 0xf0
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x430
-  __DATA_CONST.__got: 0x260
-  __DATA.__objc_const: 0x18b0
-  __DATA.__objc_selrefs: 0xb40
-  __DATA.__objc_ivar: 0x110
+  __DATA_CONST.__auth_got: 0x440
+  __DATA_CONST.__got: 0x268
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA.__objc_const: 0x18d0
+  __DATA.__objc_selrefs: 0xb58
+  __DATA.__objc_ivar: 0x114
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x430
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 322
-  Symbols:   217
-  CStrings:  807
+  Functions: 329
+  Symbols:   220
+  CStrings:  819
 
Symbols:
+ __os_log_default
+ _os_eligibility_bring_up_daemon_4_network_prompt
+ _os_eligibility_get_error_description
CStrings:
+ "\n("
+ "Eligibility changed; contacts access counts within minute: %{bool}d -> %{bool}d"
+ "Failed to bring up eligibilityd: %{public}s (%u)"
+ "Failed to register for eligibility changed notifications with code=%u"
+ "Received eligibility changed notification with token=%d"
+ "Registered for eligibility changed notifications with token=%d"
+ "_eligibilityChangedNotificationToken"
+ "com.apple.os-eligibility-domain.change.oganesson"
+ "refreshLoggingOptions"
+ "startObservingEligibilityChanges"
+ "unknown"
+ "wakeOSEligibilityUp"
+ "\xf0Q"
- "\xf0A"
```
