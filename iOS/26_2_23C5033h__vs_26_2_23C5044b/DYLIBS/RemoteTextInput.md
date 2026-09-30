## RemoteTextInput

> `/System/Library/PrivateFrameworks/RemoteTextInput.framework/RemoteTextInput`

```diff

-171.0.0.0.0
-  __TEXT.__text: 0x2156c
+171.2.1.0.0
+  __TEXT.__text: 0x215c0
   __TEXT.__auth_stubs: 0x770
   __TEXT.__objc_methlist: 0x2ba4
   __TEXT.__const: 0x108

   __TEXT.__dlopen_cstrs: 0xf6
   __TEXT.__unwind_info: 0x918
   __TEXT.__objc_classname: 0x419
-  __TEXT.__objc_methname: 0x7543
+  __TEXT.__objc_methname: 0x7562
   __TEXT.__objc_methtype: 0x1760
-  __TEXT.__objc_stubs: 0x47e0
+  __TEXT.__objc_stubs: 0x4800
   __DATA_CONST.__got: 0x260
   __DATA_CONST.__const: 0xcb8
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1968
+  __DATA_CONST.__objc_selrefs: 0x1970
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 49B9F8FE-5E17-3C15-B2E7-E9B2DFA90AAD
+  UUID: C57DD461-00CD-3978-A529-AA44C21F71A7
   Functions: 1016
-  Symbols:   3674
-  CStrings:  2334
+  Symbols:   3675
+  CStrings:  2335
 
Symbols:
+ ___58-[RTIInputSystemClient _configureConnection:withMachName:]_block_invoke.134
+ ___58-[RTIInputSystemClient _configureConnection:withMachName:]_block_invoke.138
+ ___62-[RTIInputSystemClient endAllowingRemoteTextInput:completion:]_block_invoke.145
+ ___73-[RTIInputSystemClient _endSessionWithID:forServices:options:completion:]_block_invoke.150
+ ___73-[RTIInputSystemClient _endSessionWithID:forServices:options:completion:]_block_invoke_2.151
+ ___73-[RTIInputSystemClient _endSessionWithID:forServices:options:completion:]_block_invoke_2.151.cold.1
+ ___75-[RTIInputSystemClient endRemoteTextInputSessionWithID:options:completion:]_block_invoke.158
+ _objc_msgSend$shouldReconnectOnInterruption:
- ___58-[RTIInputSystemClient _configureConnection:withMachName:]_block_invoke.132
- ___58-[RTIInputSystemClient _configureConnection:withMachName:]_block_invoke.136
- ___62-[RTIInputSystemClient endAllowingRemoteTextInput:completion:]_block_invoke.143
- ___73-[RTIInputSystemClient _endSessionWithID:forServices:options:completion:]_block_invoke.148
- ___73-[RTIInputSystemClient _endSessionWithID:forServices:options:completion:]_block_invoke_2.149
- ___73-[RTIInputSystemClient _endSessionWithID:forServices:options:completion:]_block_invoke_2.149.cold.1
- ___75-[RTIInputSystemClient endRemoteTextInputSessionWithID:options:completion:]_block_invoke.156
Functions:
~ ___58-[RTIInputSystemClient _configureConnection:withMachName:]_block_invoke : 428 -> 512
CStrings:
+ "shouldReconnectOnInterruption:"

```
