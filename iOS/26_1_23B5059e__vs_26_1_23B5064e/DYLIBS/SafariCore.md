## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`

```diff

-622.2.9.10.3
-  __TEXT.__text: 0x11b464
-  __TEXT.__auth_stubs: 0x2ea0
+622.2.10.10.1
+  __TEXT.__text: 0x11b6e8
+  __TEXT.__auth_stubs: 0x2eb0
   __TEXT.__objc_methlist: 0xb63c
   __TEXT.__const: 0x2a24
-  __TEXT.__gcc_except_tab: 0x66a0
-  __TEXT.__cstring: 0x11c35
+  __TEXT.__gcc_except_tab: 0x66d8
+  __TEXT.__cstring: 0x11cb5
   __TEXT.__ustring: 0x2810
-  __TEXT.__oslogstring: 0xa02d
+  __TEXT.__oslogstring: 0xa15d
   __TEXT.__dlopen_cstrs: 0x19b
   __TEXT.__swift5_typeref: 0xd42
   __TEXT.__swift5_fieldmd: 0x804

   __TEXT.__swift_as_entry: 0xd0
   __TEXT.__swift_as_ret: 0xbc
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x6008
+  __TEXT.__unwind_info: 0x6010
   __TEXT.__eh_frame: 0x2d30
   __TEXT.__objc_classname: 0x19d8
-  __TEXT.__objc_methname: 0x23def
+  __TEXT.__objc_methname: 0x23dfa
   __TEXT.__objc_methtype: 0x3db9
   __TEXT.__objc_stubs: 0x11600
   __DATA_CONST.__got: 0xdf8

   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x480
   __DATA_CONST.__objc_arraydata: 0x2790
-  __AUTH_CONST.__auth_got: 0x1768
+  __AUTH_CONST.__auth_got: 0x1770
   __AUTH_CONST.__const: 0x4c38
   __AUTH_CONST.__cfstring: 0x185a0
   __AUTH_CONST.__objc_const: 0x12ba0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D5E42121-E262-357B-A320-6E8509864154
-  Functions: 6769
-  Symbols:   18567
-  CStrings:  12492
+  UUID: 8EF04182-EA00-3196-98FB-4FE4ECA2895B
+  Functions: 6772
+  Symbols:   18576
+  CStrings:  12496
 
Symbols:
+ -[WBSSQLiteStore _acquireDatabaseCoordinationLockForDatabaseURL:].cold.3
+ ___76-[WBSSavedAccountStore setShouldShowServiceNamesForPasswordAndPasskeyItems:]_block_invoke_3
+ ___76-[WBSSavedAccountStore setShouldShowServiceNamesForPasswordAndPasskeyItems:]_block_invoke_4
+ ___block_literal_global.893
+ ___block_literal_global.899
+ _fsetxattr
+ _objc_msgSend$setWebsiteNameConsumer:completion:
- ___block_literal_global.814
- ___block_literal_global.891
- ___block_literal_global.897
- _objc_msgSend$setWebsiteNameConsumer:
CStrings:
+ "-[WBSSavedAccountStore setShouldShowServiceNamesForPasswordAndPasskeyItems:]_block_invoke"
+ "Failed to set can-suspend-locked Runningboard attribute for coordination lock at %s: %{errno}d"
+ "In %s, found websiteNameProvider that didn't respond to -setWebsiteNameConsumer:completion:, indicating that AuthenticationServices framework category wasn't loaded. Service names will not function properly."
+ "com.apple.runningboard.can-suspend-locked"
+ "setWebsiteNameConsumer:completion:"
- "setWebsiteNameConsumer:"

```
