## ManagedConfiguration

> `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration`

```diff

-2420.1.1.0.0
-  __TEXT.__text: 0xf7d6c
+2422.0.0.0.0
+  __TEXT.__text: 0xf7f84
   __TEXT.__auth_stubs: 0x1750
-  __TEXT.__objc_methlist: 0xb14c
+  __TEXT.__objc_methlist: 0xb154
   __TEXT.__const: 0x1394
-  __TEXT.__cstring: 0x17bf7
-  __TEXT.__oslogstring: 0x8c67
-  __TEXT.__gcc_except_tab: 0x109c
+  __TEXT.__cstring: 0x17c93
+  __TEXT.__oslogstring: 0x8cc9
+  __TEXT.__gcc_except_tab: 0x10c4
   __TEXT.__ustring: 0x50
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x3070
+  __TEXT.__unwind_info: 0x3080
   __TEXT.__objc_classname: 0xc99
-  __TEXT.__objc_methname: 0x1df92
-  __TEXT.__objc_methtype: 0x2360
-  __TEXT.__objc_stubs: 0xdb80
+  __TEXT.__objc_methname: 0x1e028
+  __TEXT.__objc_methtype: 0x236c
+  __TEXT.__objc_stubs: 0xdb60
   __DATA_CONST.__got: 0xa88
-  __DATA_CONST.__const: 0x4cf0
+  __DATA_CONST.__const: 0x4d28
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5c90
+  __DATA_CONST.__objc_selrefs: 0x5ca0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0xbb8
   __AUTH_CONST.__const: 0x2070
-  __AUTH_CONST.__cfstring: 0x19200
+  __AUTH_CONST.__cfstring: 0x19240
   __AUTH_CONST.__objc_const: 0xd6a8
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_arrayobj: 0xd8

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D9D774D2-5E57-3686-B896-D2985D7C532C
-  Functions: 5618
-  Symbols:   17321
-  CStrings:  12187
+  UUID: E958E463-BD39-3F7E-8217-684030BB6638
+  Functions: 5620
+  Symbols:   17327
+  CStrings:  12197
 
Symbols:
+ -[MCProfileConnection(Private) doMCICDidRequestCurrentPasscodeNeedsExtractable:withCompletion:]
+ -[MCProfileConnection(Private) doMCICDidRequestCurrentPasscodeNeedsExtractable:withCompletion:].cold.1
+ -[MCProfileConnection(Profiles) respondToCurrentPasscodeRequestContinue:passcodeContext:]
+ -[MCProfileConnection(Profiles) respondToCurrentPasscodeRequestContinue:passcodeContext:].cold.1
+ _MCGamesBundleIdentifier
+ ___block_descriptor_tmp.128
+ ___block_descriptor_tmp.141
+ ___block_descriptor_tmp.151
+ ___block_descriptor_tmp.154
+ ___block_descriptor_tmp.170
+ ___block_literal_global.1351
+ ___block_literal_global.1353
+ ___block_literal_global.1355
+ ___block_literal_global.1357
+ ___block_literal_global.1359
+ ___block_literal_global.1361
+ ___block_literal_global.153
+ ___block_literal_global.156
+ ___block_literal_global.172
+ _objc_msgSend$profileConnectionDidRequestCurrentPasscodeContext:needsExtractablePasscode:
- -[MCProfileConnection(Private) doMCICDidRequestCurrentPasscodeWithCompletion:]
- -[MCProfileConnection(Private) doMCICDidRequestCurrentPasscodeWithCompletion:].cold.1
- ___block_descriptor_tmp.127
- ___block_descriptor_tmp.139
- ___block_descriptor_tmp.150
- ___block_descriptor_tmp.153
- ___block_descriptor_tmp.169
- ___block_literal_global.1345
- ___block_literal_global.1350
- ___block_literal_global.1352
- ___block_literal_global.1354
- ___block_literal_global.1356
- ___block_literal_global.1358
- ___block_literal_global.152
- ___block_literal_global.155
- ___block_literal_global.171
- _objc_msgSend$initWithValue:localizedKey:
- _objc_msgSend$passcodeExists
CStrings:
+ "-[MCProfileConnection(Private) doMCICDidRequestCurrentPasscodeNeedsExtractable:withCompletion:]"
+ "-[MCProfileConnection(Profiles) respondToCurrentPasscodeRequestContinue:passcodeContext:]"
+ "/.exclave"
+ "MCKeybagCopyEscrowWithContext: escrow created."
+ "MCKeybagCopyEscrowWithContext: escrow data copied."
+ "com.apple.games"
+ "doMCICDidRequestCurrentPasscodeNeedsExtractable:withCompletion:"
+ "passcodeGenerationLock"
+ "profileConnectionDidRequestCurrentPasscodeContext:needsExtractablePasscode:"
+ "respondToCurrentPasscodeRequestContinue:passcodeContext:"
+ "v28@0:8B16@?<v@?B@\"NSString\"@\"NSData\"@\"NSError\">20"
- "-[MCProfileConnection(Private) doMCICDidRequestCurrentPasscodeWithCompletion:]"
- "doMCICDidRequestCurrentPasscodeWithCompletion:"
- "v24@0:8@?<v@?B@\"NSString\"@\"NSError\">16"

```
