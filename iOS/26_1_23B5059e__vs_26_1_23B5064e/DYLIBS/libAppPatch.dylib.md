## libAppPatch.dylib

> `/usr/lib/libAppPatch.dylib`

```diff

-1513.40.11.502.1
-  __TEXT.__text: 0x14c24
+1513.40.14.0.0
+  __TEXT.__text: 0x14c78
   __TEXT.__auth_stubs: 0xd50
   __TEXT.__objc_methlist: 0x4ec
-  __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x59da
+  __TEXT.__const: 0xe8
+  __TEXT.__cstring: 0x5a79
   __TEXT.__oslogstring: 0x23a
   __TEXT.__gcc_except_tab: 0x2f8
   __TEXT.__unwind_info: 0x3b8
   __TEXT.__objc_classname: 0x5a
   __TEXT.__objc_methname: 0x1826
   __TEXT.__objc_methtype: 0x44e
-  __TEXT.__objc_stubs: 0xf80
+  __TEXT.__objc_stubs: 0xf60
   __DATA_CONST.__got: 0x150
   __DATA_CONST.__const: 0x448
   __DATA_CONST.__objc_classlist: 0x18

   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0x6b8
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x36e0
+  __AUTH_CONST.__cfstring: 0x3720
   __AUTH_CONST.__objc_const: 0x278
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x190

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 52C64257-C1EB-36DF-ACAF-F5A0C8E5115C
-  Functions: 230
-  Symbols:   948
-  CStrings:  1270
+  UUID: 1091DDA5-7FDA-33F9-BE22-FBB7E35968CE
+  Functions: 231
+  Symbols:   949
+  CStrings:  1274
 
Symbols:
+ _MICreateCFBundleEnforcingInfoPlistSize
+ ___block_literal_global.129
- ___block_literal_global.124
- _objc_msgSend$itemIsFileAtURL:error:
Functions:
~ _MICreateCFBundle : 752 -> 16
+ _MICreateCFBundleEnforcingInfoPlistSize
~ _MILoadInfoPlistWithError : 224 -> 228
~ _MILoadRawInfoPlist : 252 -> 256
CStrings:
+ "Expected Info.plist file at %@ but found something that was not a file (found mode 0%o)."
+ "MICreateCFBundleEnforcingInfoPlistSize"
+ "The Info.plist at %@ is too large. Found %lld bytes on disk, but maximum allowed size is %lld bytes."
+ "lstat of %@ failed"
- "Expected Info.plist file at %@ but found something that was not a file."
- "MICreateCFBundle"

```
