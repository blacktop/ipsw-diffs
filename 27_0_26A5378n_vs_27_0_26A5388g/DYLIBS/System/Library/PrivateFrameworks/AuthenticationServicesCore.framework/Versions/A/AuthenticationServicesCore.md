## AuthenticationServicesCore

> `/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/Versions/A/AuthenticationServicesCore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-625.1.22.11.4
-  __TEXT.__text: 0xb9e28
-  __TEXT.__objc_methlist: 0x3a90
+625.1.24.11.2
+  __TEXT.__text: 0xba40c
+  __TEXT.__objc_methlist: 0x3ab8
   __TEXT.__const: 0xbfa8
-  __TEXT.__cstring: 0x3c21
-  __TEXT.__oslogstring: 0x32ed
+  __TEXT.__cstring: 0x3c61
+  __TEXT.__oslogstring: 0x337d
   __TEXT.__gcc_except_tab: 0x364
   __TEXT.__ustring: 0x48e
   __TEXT.__dlopen_cstrs: 0x5a

   __TEXT.__swift_as_cont: 0xe4
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x3360
+  __TEXT.__unwind_info: 0x3378
   __TEXT.__eh_frame: 0x4398
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x4f0
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x168
+  __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e00
+  __DATA_CONST.__objc_selrefs: 0x1e10
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0xf8
-  __DATA_CONST.__got: 0x840
+  __DATA_CONST.__got: 0x848
   __AUTH_CONST.__const: 0x6908
-  __AUTH_CONST.__cfstring: 0x1e80
-  __AUTH_CONST.__objc_const: 0x7a68
+  __AUTH_CONST.__cfstring: 0x1ee0
+  __AUTH_CONST.__objc_const: 0x7a88
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x1120
+  __AUTH_CONST.__auth_got: 0x1128
   __AUTH.__objc_data: 0x4d8
   __AUTH.__data: 0x790
   __DATA.__objc_ivar: 0x400
-  __DATA.__data: 0x22b0
+  __DATA.__data: 0x2310
   __DATA.__bss: 0xfa30
   __DATA.__common: 0x148
   __DATA_DIRTY.__objc_data: 0x2288

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4837
-  Symbols:   4092
-  CStrings:  696
+  Functions: 4843
+  Symbols:   4106
+  CStrings:  701
 
Symbols:
+ -[ASCAgent _credentialRequestedForCABLELoginChoice:completionHandler:]
+ -[ASCAgent getSafariPasswordAutoFillSettingWithCompletionHandler:]
+ -[ASCAgentProxy getSafariPasswordAutoFillSettingWithCompletionHandler:]
+ GCC_except_table106
+ GCC_except_table117
+ GCC_except_table167
+ GCC_except_table83
+ _WBSOSLogAutoFill
+ _WBSWebExtensionPointIdentifier
+ __70-[ASCAgent _credentialRequestedForCABLELoginChoice:completionHandler:]_block_invoke
+ __71-[ASCAgentProxy getSafariPasswordAutoFillSettingWithCompletionHandler:]_block_invoke_2
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASCSafariSettingsHelperProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ASCSafariSettingsHelperProtocol
+ __OBJC_$_PROTOCOL_REFS_ASCSafariSettingsHelperProtocol
+ __OBJC_LABEL_PROTOCOL_$_ASCSafariSettingsHelperProtocol
+ __OBJC_PROTOCOL_$_ASCSafariSettingsHelperProtocol
+ ___70-[ASCAgent _credentialRequestedForCABLELoginChoice:completionHandler:]_block_invoke
+ ___70-[ASCAgent _credentialRequestedForCABLELoginChoice:completionHandler:]_block_invoke_2
+ ___71-[ASCAgentProxy getSafariPasswordAutoFillSettingWithCompletionHandler:]_block_invoke
+ ___71-[ASCAgentProxy getSafariPasswordAutoFillSettingWithCompletionHandler:]_block_invoke_2
+ _objc_msgSend$_credentialRequestedForCABLELoginChoice:completionHandler:
+ _objc_msgSend$getSafariPasswordAutoFillSettingWithCompletionHandler:
+ _objc_msgSend$infoDictionary
- -[ASCAgent _credentialRequestedForCABLELoginChoice:]
- GCC_except_table102
- GCC_except_table116
- GCC_except_table166
- GCC_except_table82
- __52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke
- ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke
- ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke_2
- _objc_msgSend$_credentialRequestedForCABLELoginChoice:
CStrings:
+ "AutoFillPasswordsInSafari"
+ "Client process is not allowed to read Safari AutoFill settings"
+ "Failed to get extension record for application identifier with error: %{public}@"
+ "NSExtension"
+ "NSExtensionPointIdentifier"
```
