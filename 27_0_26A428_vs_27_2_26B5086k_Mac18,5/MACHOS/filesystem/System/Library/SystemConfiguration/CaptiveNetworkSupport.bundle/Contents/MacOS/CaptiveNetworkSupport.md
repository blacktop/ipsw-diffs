## CaptiveNetworkSupport

> `/System/Library/SystemConfiguration/CaptiveNetworkSupport.bundle/Contents/MacOS/CaptiveNetworkSupport`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-542.0.0.0.1
-  __TEXT.__text: 0x254d4
+545.40.1.0.0
+  __TEXT.__text: 0x2551c
   __TEXT.__auth_stubs: 0x11a0
   __TEXT.__objc_stubs: 0x120
   __TEXT.__const: 0x1d0
-  __TEXT.__oslogstring: 0x47fc
-  __TEXT.__cstring: 0x18fd
+  __TEXT.__oslogstring: 0x47fe
+  __TEXT.__cstring: 0x1986
   __TEXT.__objc_methname: 0x9a
-  __TEXT.__unwind_info: 0x970
-  __DATA_CONST.__const: 0xe88
+  __TEXT.__unwind_info: 0x978
+  __DATA_CONST.__const: 0xfb8
   __DATA_CONST.__cfstring: 0x1a20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x8d8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 604
-  Symbols:   1148
-  CStrings:  898
+  Functions: 605
+  Symbols:   1149
+  CStrings:  907
 
Symbols:
+ _WISPrResultName
Functions:
~ _CaptiveHandleRedirect : 2684 -> 2720
+ _WISPrResultName
CStrings:
+ "%@: probe result '%s' (%d), assuming online"
+ "APIIsCaptive"
+ "AllowList"
+ "CaptiveNetworkSupport-545.40.1"
+ "InsecureTokenAuthServer"
+ "InternalError"
+ "TLSAbortError"
+ "TLSTrustError"
+ "TokenAuthFailure"
+ "TokenAuthUnsupported"
+ "UnknownState"
- "CaptiveNetworkSupport-542.0.0.0.1"
- "Unknown result value: %d, assuming online"
```
