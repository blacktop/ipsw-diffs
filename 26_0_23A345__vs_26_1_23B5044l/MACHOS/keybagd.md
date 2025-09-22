## keybagd

> `/usr/libexec/keybagd`

```diff

-674.0.3.0.0
-  __TEXT.__text: 0x21c98
-  __TEXT.__auth_stubs: 0x14a0
+674.40.2.0.0
+  __TEXT.__text: 0x21b54
+  __TEXT.__auth_stubs: 0x14b0
   __TEXT.__objc_stubs: 0x1020
   __TEXT.__objc_methlist: 0x814
-  __TEXT.__cstring: 0x993e
+  __TEXT.__cstring: 0x9939
   __TEXT.__const: 0x198
   __TEXT.__gcc_except_tab: 0x478
   __TEXT.__objc_methname: 0x181c

   __TEXT.__objc_methtype: 0x967
   __TEXT.__dlopen_cstrs: 0x1c8
   __TEXT.__oslogstring: 0x281
-  __TEXT.__unwind_info: 0x788
-  __DATA_CONST.__auth_got: 0xa60
+  __TEXT.__unwind_info: 0x770
+  __DATA_CONST.__auth_got: 0xa68
   __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x1008
-  __DATA_CONST.__cfstring: 0x4ea0
+  __DATA_CONST.__const: 0x1030
+  __DATA_CONST.__cfstring: 0x4e80
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_data: 0x190
   __DATA.__data: 0x1fa
   __DATA.__common: 0x30
-  __DATA.__bss: 0x178
+  __DATA.__bss: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: BAF40F18-9F99-3094-B0B9-24B353B978A8
-  Functions: 658
-  Symbols:   399
-  CStrings:  2118
+  UUID: C526B995-5CBD-322E-91BF-5216E84574A4
+  Functions: 645
+  Symbols:   400
+  CStrings:  2116
 
Symbols:
+ _dispatch_assert_queue$V2
CStrings:
+ "-[KBXPCService changeSystemSecretfromOldSecret:oldSize:toNewSecret:newSize:opaqueData:withParams:reply:]_block_invoke_2"
+ "keybagd_SeshatEnroll_block_invoke_3"
+ "seshat_create_derived_passcode_with_opts"
- "-[KBXPCService changeSystemSecretfromOldSecret:oldSize:toNewSecret:newSize:opaqueData:withParams:reply:]_block_invoke"
- "SeshatCreateDerivedPasscodeOpts"
- "keybagd_SeshatEnroll_block_invoke_2"
- "no reset needed"

```
