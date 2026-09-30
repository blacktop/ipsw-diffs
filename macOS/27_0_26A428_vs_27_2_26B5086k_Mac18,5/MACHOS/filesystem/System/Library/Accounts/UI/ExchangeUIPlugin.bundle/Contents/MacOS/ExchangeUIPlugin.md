## ExchangeUIPlugin

> `/System/Library/Accounts/UI/ExchangeUIPlugin.bundle/Contents/MacOS/ExchangeUIPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-844.0.0.0.0
-  __TEXT.__text: 0x88f4
-  __TEXT.__auth_stubs: 0x310
-  __TEXT.__objc_stubs: 0x20c0
-  __TEXT.__objc_methlist: 0x724
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x1289
-  __TEXT.__objc_methname: 0x209b
-  __TEXT.__objc_classname: 0xb9
+846.200.41.1.1
+  __TEXT.__text: 0x9ae0
+  __TEXT.__auth_stubs: 0x3a0
+  __TEXT.__objc_stubs: 0x2160
+  __TEXT.__objc_methlist: 0x75c
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x1351
+  __TEXT.__objc_methname: 0x2159
+  __TEXT.__objc_classname: 0xd2
   __TEXT.__objc_methtype: 0x3ac
-  __TEXT.__oslogstring: 0x170
+  __TEXT.__gcc_except_tab: 0x58
+  __TEXT.__oslogstring: 0x2aa
   __TEXT.__ustring: 0x9a
-  __TEXT.__unwind_info: 0x248
-  __DATA_CONST.__const: 0x340
-  __DATA_CONST.__cfstring: 0x960
-  __DATA_CONST.__objc_classlist: 0x30
+  __TEXT.__unwind_info: 0x2e0
+  __DATA_CONST.__const: 0x4b0
+  __DATA_CONST.__cfstring: 0x9a0
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x190
+  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__auth_got: 0x1e0
   __DATA_CONST.__got: 0x2e8
-  __DATA.__objc_const: 0x998
-  __DATA.__objc_selrefs: 0x9f0
-  __DATA.__objc_ivar: 0x64
-  __DATA.__objc_data: 0x1e0
+  __DATA.__objc_const: 0xa68
+  __DATA.__objc_selrefs: 0xa20
+  __DATA.__objc_ivar: 0x6c
+  __DATA.__objc_data: 0x230
   __DATA.__data: 0xc0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /System/Library/PrivateFrameworks/ExchangeWebServices.framework/Versions/A/ExchangeWebServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 166
-  Symbols:   172
-  CStrings:  547
+  Functions: 195
+  Symbols:   184
+  CStrings:  564
 
Symbols:
+ _OBJC_CLASS_$_ExchangeUIOAuthDiscovery
+ _OBJC_METACLASS_$_ExchangeUIOAuthDiscovery
+ __Block_object_dispose
+ __Unwind_Resume
+ ___objc_personality_v0
+ _dispatch_after
+ _dispatch_time
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_retainBlock
CStrings:
+ "-[ExchangeOAuthWebLoginViewController viewDidLoad]_block_invoke"
+ "Cannot discover sign-in URL: account has no identity email address"
+ "Discovered authorize URL could not be upgraded to V2; not persisting"
+ "ExchangeUIOAuthDiscovery"
+ "Failed to persist discovered sign-in URL: %{public}@"
+ "OAuthDiscovery"
+ "Sign-in URL discovery did not yield an Exchange Online authorize URL (hasURI=%d isEXO=%d issuer=%{public}@ error=%{public}@)"
+ "Sign-in URL heal failed for %@ with error %@"
+ "Sign-in URL heal reported success but the authorize URL is still nil for %@"
+ "_healCancelled"
+ "_healInFlight"
+ "_needsSignInURLHeal"
+ "discoverAndPersistSignInURLForAccount:accountStore:completion:"
+ "loadRequest:"
+ "saveAccount:withCompletionHandler:"
+ "viewDidLoad"
+ "viewWillDisappear"
```
