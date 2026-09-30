## HSAAuthentication

> `/System/Library/PrivateFrameworks/HSAAuthentication.framework/HSAAuthentication`

```diff

-1100.600.1.0.0
-  __TEXT.__text: 0x1ec8
-  __TEXT.__auth_stubs: 0x420
+1117.100.1.0.0
+  __TEXT.__text: 0x30fc
+  __TEXT.__auth_stubs: 0x400
   __TEXT.__objc_methlist: 0x80
-  __TEXT.__const: 0x58
-  __TEXT.__cstring: 0xce2
-  __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__oslogstring: 0x29
-  __TEXT.__unwind_info: 0xd0
+  __TEXT.__const: 0xa8
+  __TEXT.__gcc_except_tab: 0x550
+  __TEXT.__cstring: 0x1da
+  __TEXT.__oslogstring: 0xbad
+  __TEXT.__unwind_info: 0x170
   __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methname: 0x21c
   __TEXT.__objc_methtype: 0x5b

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x220
+  __AUTH_CONST.__auth_got: 0x210
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x880
+  __AUTH_CONST.__cfstring: 0xe0
   __AUTH_CONST.__objc_const: 0xf8
   __DATA.__objc_ivar: 0xc
   __DATA.__bss: 0x30

   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 118D99F5-0D6E-31F7-93D5-05DD7302C3B6
+  UUID: 4CC1A34B-F3F5-33F3-B79D-B6240DEFD5FE
   Functions: 31
-  Symbols:   91
-  CStrings:  191
+  Symbols:   89
+  CStrings:  130
 
Symbols:
+ _OSLogHandleForIDSCategory
- __IMAlwaysLog
- __IMWarn
- _objc_retain_x21
CStrings:
+ "Exception getting HSA first match in string: %{sensitive}@"
+ "HSA - Processing incoming message from number: %@   service: %@   body: %{sensitive}@"
+ "HSAClient - Calling back about auth token: %{sensitive}@    from: %@  service: %@  body: %{sensitive}@"
+ "HSAClient - Dropping message with empty auth token: %{sensitive}@    from: %@  service: %@  body: %{sensitive}@"
+ "HSAClient - Incoming message with auth token: %{sensitive}@    from: %@  service: %@  body: %{sensitive}@"
+ "HSAClient - received message from peer(%d): %{sensitive}s"
+ "HSAProvider - HSAAuthenticationProcessIncomingMessage: number %@,   service %@,  body: %{sensitive}@"
+ "HSAProvider - Sending request message %{sensitive}@"
+ "Ignoring incoming message from: %@  body: %{sensitive}@  --  no results found"
+ "Incoming message from: %@  body: %{sensitive}@  --  found token: %{sensitive}@"
+ "Warning"
- "Exception getting HSA first match in string: %@"
- "HSA - Processing incoming message from number: %@   service: %@   body: %@"
- "HSAClient - Calling back about auth token: %@    from: %@  service: %@  body: %@"
- "HSAClient - Disconnecting from server"
- "HSAClient - Dropping message with empty auth token: %@    from: %@  service: %@  body: %@"
- "HSAClient - Incoming message with auth token: %@    from: %@  service: %@  body: %@"
- "HSAClient - received message from peer(%d): %s"
- "HSAProvider - HSAAuthenticationProcessIncomingMessage: number %@,   service %@,  body: %@"
- "HSAProvider - Sending request message %@"
- "Ignoring incoming message from: %@  body: %@  --  no results found"
- "Incoming message from: %@  body: %@  --  found token: %@"

```
